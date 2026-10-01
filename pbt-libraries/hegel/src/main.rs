use hegel_runner::{ENGINE_VERSION, HEGEL_VERSION, challenges::Challenge, run};
use serde_json::json;
use std::collections::BTreeMap;
use std::path::PathBuf;

fn main() {
    if let Err(error) = execute() {
        eprintln!("{error}");
        std::process::exit(1);
    }
}

fn execute() -> Result<(), Box<dyn std::error::Error>> {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let mut selected = "all".to_string();
    let mut iterations = 100usize;
    let mut seed = None;
    let mut output = root.join("reports");
    let mut seed_file = root.join("support/seeds.json");
    let mut args = std::env::args().skip(1);
    while let Some(arg) = args.next() {
        if arg == "--help" || arg == "-h" {
            println!(
                "hegel-runner [--challenge NAME|all] [--iterations N] [--seed N]\n\
                \x20            [--seed-file PATH] [--output DIR] [--list]\n\
                Defaults: all challenges, 100 seeds from support/seeds.json, reports/.\n\
                --seed runs one seed of one challenge, ignoring --iterations."
            );
            return Ok(());
        }
        if arg == "--list" {
            for challenge in Challenge::all() {
                println!("{}", challenge.name());
            }
            return Ok(());
        }
        let value = args
            .next()
            .ok_or_else(|| format!("missing value for {arg}"))?;
        match arg.as_str() {
            "--challenge" => selected = value,
            "--iterations" => iterations = value.parse()?,
            "--seed" => seed = Some(value.parse::<u64>()?),
            "--output" => output = value.into(),
            "--seed-file" => seed_file = value.into(),
            _ => return Err(format!("unknown option: {arg}").into()),
        }
    }
    if iterations == 0 {
        return Err("--iterations must be positive".into());
    }
    if seed.is_some() && selected == "all" {
        return Err("--seed requires --challenge NAME".into());
    }
    let challenges: Vec<_> = Challenge::all()
        .into_iter()
        .filter(|c| selected == "all" || c.name() == selected)
        .collect();
    if challenges.is_empty() {
        return Err(format!("unknown challenge: {selected}").into());
    }
    let seeds: BTreeMap<String, Vec<u64>> = if seed.is_some() {
        BTreeMap::new()
    } else {
        serde_json::from_slice(&std::fs::read(seed_file)?)?
    };
    std::fs::create_dir_all(&output)?;
    let environment = json!({
        "rustc": env!("HEGEL_BENCH_RUSTC"),
        "os": std::env::consts::OS, "arch": std::env::consts::ARCH,
        "os_version": if cfg!(target_os = "macos") { command_output("sw_vers", &["-productVersion"]) }
            else { command_output("uname", &["-r"]) },
        "cpu": if cfg!(target_os = "macos") { command_output("sysctl", &["-n", "machdep.cpu.brand_string"]) }
            else { None },
    });
    for challenge in challenges {
        let name = challenge.name();
        let run_seeds = if let Some(seed) = seed {
            vec![seed]
        } else {
            let available = seeds
                .get(&name)
                .ok_or_else(|| format!("no seeds for {name}"))?;
            if iterations > available.len() {
                return Err(format!(
                    "{name}: requested {iterations} runs, only {} seeds available",
                    available.len()
                )
                .into());
            }
            available[..iterations].to_vec()
        };
        let mut records = Vec::new();
        for (index, seed) in run_seeds.iter().enumerate() {
            records.push(run(challenge, *seed)?);
            eprintln!("{name}: {}/{}", index + 1, run_seeds.len());
        }
        let report = json!({
            "challenge": name, "hegel_version": HEGEL_VERSION,
            "engine_version": ENGINE_VERSION,
            "build_profile": if cfg!(debug_assertions) { "debug" } else { "release" },
            "environment": environment,
            "runs": records,
        });
        // Replace only after every requested seed has completed successfully.
        let temporary = output.join(format!("{name}.json.tmp"));
        std::fs::write(
            &temporary,
            format!("{}\n", serde_json::to_string_pretty(&report)?),
        )?;
        std::fs::rename(temporary, output.join(format!("{name}.json")))?;
    }
    Ok(())
}

fn command_output(program: &str, args: &[&str]) -> Option<String> {
    let output = std::process::Command::new(program)
        .args(args)
        .output()
        .ok()?;
    output
        .status
        .success()
        .then(|| String::from_utf8_lossy(&output.stdout).trim().to_string())
}
