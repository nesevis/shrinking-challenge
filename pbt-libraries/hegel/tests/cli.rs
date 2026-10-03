use serde_json::Value;
use std::path::PathBuf;
use std::process::{Command, Output};
use std::sync::atomic::{AtomicUsize, Ordering};

struct OutputDirectory(PathBuf);
impl OutputDirectory {
    fn new() -> Self {
        static NEXT: AtomicUsize = AtomicUsize::new(0);
        let path = std::env::temp_dir().join(format!(
            "hegel-runner-cli-{}-{}",
            std::process::id(),
            NEXT.fetch_add(1, Ordering::Relaxed)
        ));
        std::fs::create_dir(&path).unwrap();
        Self(path)
    }
    fn invoke(&self, args: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_hegel-runner"))
            .args(args)
            .arg("--output")
            .arg(&self.0)
            .output()
            .unwrap()
    }
}
impl Drop for OutputDirectory {
    fn drop(&mut self) {
        let _ = std::fs::remove_dir_all(&self.0);
    }
}

#[test]
fn one_seed_produces_reproducible_results_and_environment_metadata() {
    let directory = OutputDirectory::new();
    let args = [
        "--challenge",
        "modular_mapping",
        "--seed",
        "42",
        "--iterations",
        "1",
    ];
    let first = directory.invoke(&args);
    assert!(
        first.status.success(),
        "{}",
        String::from_utf8_lossy(&first.stderr)
    );
    let path = directory.0.join("modular_mapping.json");
    let first: Value = serde_json::from_slice(&std::fs::read(&path).unwrap()).unwrap();
    assert_eq!(first["runs"].as_array().unwrap().len(), 1);
    assert_eq!(first["runs"][0]["seed"], 42);
    assert!(
        first["runs"][0]["shrunk"]["value"]
            .as_str()
            .unwrap()
            .parse::<i64>()
            .unwrap()
            >= 900
    );
    assert!(
        first["environment"]["rustc"]
            .as_str()
            .unwrap()
            .starts_with("rustc ")
    );
    assert_eq!(first["environment"]["os"], std::env::consts::OS);
    let second = directory.invoke(&args);
    assert!(second.status.success());
    let second: Value = serde_json::from_slice(&std::fs::read(&path).unwrap()).unwrap();
    for field in ["seed", "original", "shrunk", "evaluations"] {
        assert_eq!(first["runs"][0][field], second["runs"][0][field]);
    }
    assert!(!directory.0.join("modular_mapping.json.tmp").exists());
}

#[test]
fn binary_heap_port_is_listed_and_reduces_a_generated_failure() {
    let directory = OutputDirectory::new();
    let listed = directory.invoke(&["--list"]);
    assert!(listed.status.success());
    assert!(
        String::from_utf8_lossy(&listed.stdout)
            .lines()
            .any(|name| name == "binheap")
    );
    let result = directory.invoke(&[
        "--challenge",
        "binheap",
        "--seed",
        "42",
        "--iterations",
        "1",
    ]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("binheap.json")).unwrap()).unwrap();
    assert_eq!(report["challenge"], "binheap");
    assert_eq!(report["runs"][0]["seed"], 42);
    assert_eq!(
        report["runs"][0]["shrunk"]["value"],
        "(0, None, (0, (0, None, None), (1, None, None)))"
    );
    assert_ne!(report["runs"][0]["original"], report["runs"][0]["shrunk"]);
}

#[test]
fn calculator_port_is_listed_and_reduces_a_computed_zero_divisor() {
    let directory = OutputDirectory::new();
    let listed = directory.invoke(&["--list"]);
    assert!(listed.status.success());
    assert!(
        String::from_utf8_lossy(&listed.stdout)
            .lines()
            .any(|name| name == "calculator")
    );
    let result = directory.invoke(&[
        "--challenge",
        "calculator",
        "--seed",
        "42",
        "--iterations",
        "1",
    ]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("calculator.json")).unwrap())
            .unwrap();
    assert_eq!(report["challenge"], "calculator");
    assert_eq!(report["runs"][0]["seed"], 42);
    assert_eq!(
        report["runs"][0]["shrunk"]["value"],
        "('/', 0, ('+', 0, 0))"
    );
    assert_ne!(report["runs"][0]["original"], report["runs"][0]["shrunk"]);
}

#[test]
fn refund_allocation_ports_are_listed_and_find_reproducible_fee_failures() {
    let directory = OutputDirectory::new();
    let listed = directory.invoke(&["--list"]);
    assert!(listed.status.success());
    for name in ["refund_allocation", "refund_allocation_derived"] {
        assert!(
            String::from_utf8_lossy(&listed.stdout)
                .lines()
                .any(|line| line == name)
        );
        let arguments = ["--challenge", name, "--seed", "42", "--iterations", "1"];
        let result = directory.invoke(&arguments);
        assert!(
            result.status.success(),
            "{}",
            String::from_utf8_lossy(&result.stderr)
        );
        let path = directory.0.join(format!("{name}.json"));
        let first: Value = serde_json::from_slice(&std::fs::read(&path).unwrap()).unwrap();
        assert_eq!(first["challenge"], name);
        assert_eq!(first["runs"][0]["seed"], 42);
        assert!(first["runs"][0]["evaluations"].as_u64().unwrap() > 0);
        assert!(
            first["runs"][0]["shrunk"]["value"]
                .as_str()
                .unwrap()
                .starts_with("RefundRequest([")
        );
        let repeated = directory.invoke(&arguments);
        assert!(repeated.status.success());
        let second: Value = serde_json::from_slice(&std::fs::read(path).unwrap()).unwrap();
        for field in ["original", "shrunk", "evaluations"] {
            assert_eq!(first["runs"][0][field], second["runs"][0][field]);
        }
    }
}

#[test]
fn invalid_requests_fail_without_replacing_existing_results() {
    let directory = OutputDirectory::new();
    let path = directory.0.join("modular_mapping.json");
    std::fs::write(&path, "existing results").unwrap();
    for args in [
        vec!["--challenge", "not_a_challenge"],
        vec!["--challenge", "modular_mapping", "--iterations", "0"],
        vec!["--seed", "18446744073709551615", "--iterations", "2"],
        vec!["--seed", "42", "--seed-file", "unused.json"],
        vec!["--seed-file", "does-not-exist.json"],
        vec!["--challenge", "modular_mapping", "--seed", "not_a_number"],
    ] {
        let result = directory.invoke(&args);
        assert!(!result.status.success(), "unexpected success for {args:?}");
        assert!(!result.stderr.is_empty());
        assert_eq!(std::fs::read_to_string(&path).unwrap(), "existing results");
    }
}

#[test]
fn iterations_selects_consecutive_seeds_from_the_default_start() {
    let directory = OutputDirectory::new();
    let result = directory.invoke(&["--challenge", "modular_mapping", "--iterations", "2"]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("modular_mapping.json")).unwrap())
            .unwrap();
    let seeds: Vec<_> = report["runs"]
        .as_array()
        .unwrap()
        .iter()
        .map(|run| run["seed"].as_u64().unwrap())
        .collect();
    assert_eq!(seeds, [1337, 1338]);
}

#[test]
fn starting_seed_honors_iterations_for_both_refund_variants() {
    let directory = OutputDirectory::new();
    for name in ["refund_allocation", "refund_allocation_derived"] {
        let result = directory.invoke(&["--challenge", name, "--seed", "42", "--iterations", "3"]);
        assert!(
            result.status.success(),
            "{}",
            String::from_utf8_lossy(&result.stderr)
        );
        let report: Value = serde_json::from_slice(
            &std::fs::read(directory.0.join(format!("{name}.json"))).unwrap(),
        )
        .unwrap();
        let seeds: Vec<_> = report["runs"]
            .as_array()
            .unwrap()
            .iter()
            .map(|run| run["seed"].as_u64().unwrap())
            .collect();
        assert_eq!(seeds, [42, 43, 44]);
    }
}

#[test]
fn sequential_runs_are_not_limited_to_historical_seed_lists() {
    let directory = OutputDirectory::new();
    let result = directory.invoke(&["--challenge", "modular_mapping", "--iterations", "101"]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("modular_mapping.json")).unwrap())
            .unwrap();
    let seeds: Vec<_> = report["runs"]
        .as_array()
        .unwrap()
        .iter()
        .map(|run| run["seed"].as_u64().unwrap())
        .collect();
    assert_eq!(seeds, (1337..1438).collect::<Vec<u64>>());

    let result = directory.invoke(&["--challenge", "modular_mapping", "--seed", "42"]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("modular_mapping.json")).unwrap())
            .unwrap();
    let seeds: Vec<_> = report["runs"]
        .as_array()
        .unwrap()
        .iter()
        .map(|run| run["seed"].as_u64().unwrap())
        .collect();
    assert_eq!(seeds, (42..142).collect::<Vec<u64>>());

    let result = directory.invoke(&["--challenge", "refund_allocation", "--iterations", "2"]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("refund_allocation.json")).unwrap())
            .unwrap();
    assert_eq!(report["runs"][0]["seed"], 1337);
    assert_eq!(report["runs"][1]["seed"], 1338);
}

#[test]
fn maximum_seed_is_valid_for_one_iteration_and_overflow_is_explicit() {
    let directory = OutputDirectory::new();
    let result = directory.invoke(&[
        "--challenge",
        "modular_mapping",
        "--seed",
        "18446744073709551615",
        "--iterations",
        "1",
    ]);
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let report: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("modular_mapping.json")).unwrap())
            .unwrap();
    assert_eq!(report["runs"][0]["seed"].as_u64(), Some(u64::MAX));
    let result = directory.invoke(&[
        "--challenge",
        "all",
        "--seed",
        "18446744073709551615",
        "--iterations",
        "2",
    ]);
    assert!(!result.status.success());
    assert!(String::from_utf8_lossy(&result.stderr).contains("seed range exceeds u64::MAX"));
}

#[test]
fn seed_file_option_is_no_longer_supported() {
    let directory = OutputDirectory::new();
    let result = directory.invoke(&["--seed-file", "unused.json"]);
    assert!(!result.status.success());
    assert!(String::from_utf8_lossy(&result.stderr).contains("unknown option: --seed-file"));
    assert_eq!(std::fs::read_dir(&directory.0).unwrap().count(), 0);

    let help = directory.invoke(&["--help"]);
    assert!(help.status.success());
    assert!(!String::from_utf8_lossy(&help.stdout).contains("--seed-file"));
}
