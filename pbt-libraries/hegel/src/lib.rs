pub mod challenges;
mod stateful;

use challenges::Challenge;
use hegel::{HealthCheck, Hegel, Phase, Settings, TestCase, Verbosity};
use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;
use std::panic::{AssertUnwindSafe, catch_unwind, panic_any};
use std::time::Instant;

pub const HEGEL_VERSION: &str = "0.48.1";
pub const ENGINE_VERSION: &str = "0.44.1";

#[derive(Debug)]
struct BenchmarkFailure;

#[derive(Debug, Serialize, Deserialize)]
pub struct Run {
    pub seed: u64,
    pub evaluations: usize,
    pub original: BTreeMap<String, String>,
    pub shrunk: BTreeMap<String, String>,
    pub total_seconds: f64,
}

#[derive(Default)]
struct Recorder {
    original: Option<String>,
    shrunk: Option<String>,
    evaluations: usize,
}
impl Recorder {
    fn record(&mut self, value: String, holds: bool) {
        if !holds {
            if self.original.is_none() {
                self.original = Some(value.clone());
            }
            self.shrunk = Some(value);
        }
        if self.original.is_some() {
            self.evaluations += 1;
        }
    }
}

pub fn run(challenge: Challenge, seed: u64) -> Result<Run, String> {
    let settings = Settings::from_profile("base")
        .seed(Some(seed))
        .database(None)
        .test_cases(1_000_000)
        .phases([Phase::Generate, Phase::Shrink])
        .suppress_health_check(HealthCheck::all())
        .report_multiple_failures(false)
        .verbosity(Verbosity::Quiet)
        .print_blob(false);
    let mut recorder = Recorder::default();
    let started = Instant::now();
    let result = catch_unwind(AssertUnwindSafe(|| {
        Hegel::new(|tc: TestCase| {
            let (value, holds) = if challenge.is_state_machine() {
                stateful::evaluate(challenge, tc)
            } else {
                challenge.evaluate(&tc)
            };
            recorder.record(value, holds);
            if !holds {
                panic_any(BenchmarkFailure);
            }
        })
        .settings(settings)
        .run();
    }));
    let total_seconds = started.elapsed().as_secs_f64();
    match (result, recorder.original, recorder.shrunk) {
        (Err(payload), Some(original), Some(shrunk)) if payload.is::<BenchmarkFailure>() => {
            let name = if challenge.is_state_machine() {
                "steps"
            } else {
                "value"
            };
            Ok(Run {
                seed,
                evaluations: recorder.evaluations,
                original: BTreeMap::from([(name.into(), original)]),
                shrunk: BTreeMap::from([(name.into(), shrunk)]),
                total_seconds,
            })
        }
        (Ok(()), _, _) => Err(format!(
            "{} seed {seed}: no failure found",
            challenge.name()
        )),
        (Err(payload), _, _) => {
            let message = payload
                .downcast_ref::<String>()
                .map(String::as_str)
                .or_else(|| payload.downcast_ref::<&str>().copied())
                .unwrap_or("unknown panic");
            Err(format!(
                "{} seed {seed}: runner error: {message}",
                challenge.name()
            ))
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn recorder_counts_from_first_failure_and_includes_replay() {
        let mut recorder = Recorder::default();
        recorder.record("passing".into(), true);
        recorder.record("first".into(), false);
        recorder.record("passing".into(), true);
        recorder.record("reduced".into(), false);
        recorder.record("reduced".into(), false);
        assert_eq!(recorder.evaluations, 4);
        assert_eq!(recorder.original.as_deref(), Some("first"));
        assert_eq!(recorder.shrunk.as_deref(), Some("reduced"));
    }
    #[test]
    fn seeded_generation_and_reduction_are_reproducible() {
        let first = run(Challenge::ModularMapping, 42).unwrap();
        let second = run(Challenge::ModularMapping, 42).unwrap();
        assert_eq!(first.original, second.original);
        assert_eq!(first.shrunk, second.shrunk);
        assert_eq!(first.evaluations, second.evaluations);
        assert!(first.shrunk["value"].parse::<i64>().unwrap() >= 900);
        assert!(first.evaluations > 1);
    }
    #[test]
    fn native_state_machine_reduces_a_real_collision() {
        let result = run(Challenge::HashCollisionMachine(10), 42).unwrap();
        assert_eq!(result.shrunk["steps"], "[put(0, 0), put(10, 1)]");
        assert!(result.evaluations > 1);
    }
}
