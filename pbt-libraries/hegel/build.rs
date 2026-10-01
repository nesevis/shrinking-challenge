fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    let rustc = std::env::var("RUSTC").unwrap_or_else(|_| "rustc".into());
    let output = std::process::Command::new(rustc)
        .arg("--version")
        .output()
        .expect("rustc version");
    let version = String::from_utf8(output.stdout).expect("rustc version is UTF-8");
    println!("cargo:rustc-env=HEGEL_BENCH_RUSTC={}", version.trim());
}
