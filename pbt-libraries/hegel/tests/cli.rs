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
    let args = ["--challenge", "modular_mapping", "--seed", "42"];
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
fn invalid_requests_fail_without_replacing_existing_results() {
    let directory = OutputDirectory::new();
    let path = directory.0.join("modular_mapping.json");
    std::fs::write(&path, "existing results").unwrap();
    for args in [
        vec!["--challenge", "not_a_challenge"],
        vec!["--challenge", "modular_mapping", "--iterations", "0"],
        vec!["--challenge", "modular_mapping", "--iterations", "101"],
        vec!["--seed", "42"],
        vec!["--challenge", "modular_mapping", "--seed", "not_a_number"],
    ] {
        let result = directory.invoke(&args);
        assert!(!result.status.success(), "unexpected success for {args:?}");
        assert!(!result.stderr.is_empty());
        assert_eq!(std::fs::read_to_string(&path).unwrap(), "existing results");
    }
}

#[test]
fn iterations_selects_the_checked_in_seed_list() {
    let directory = OutputDirectory::new();
    let result = directory.invoke(&["--challenge", "modular_mapping", "--iterations", "2"]);
    assert!(result.status.success());
    let output: Value =
        serde_json::from_slice(&std::fs::read(directory.0.join("modular_mapping.json")).unwrap())
            .unwrap();
    let seeds: Value = serde_json::from_str(include_str!("../support/seeds.json")).unwrap();
    let actual: Vec<_> = output["runs"]
        .as_array()
        .unwrap()
        .iter()
        .map(|run| &run["seed"])
        .collect();
    assert_eq!(
        actual,
        seeds["modular_mapping"].as_array().unwrap()[..2]
            .iter()
            .collect::<Vec<_>>()
    );
}
