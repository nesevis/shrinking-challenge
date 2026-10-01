# Hegel

[Hegel for Rust](https://github.com/hegeldev/hegel-rust) is a property-based testing
library derived from Hypothesis. This runner pins `hegeltest` **0.48.1** and its
native engine `hegeltest-c` **0.44.1**, statically linked into the executable. No
Python runtime is used by generation or reduction. Python 3.9+ is needed only to
generate Markdown reports, with no third-party Python packages.

Hegel is in beta. The runner uses its programmatic `Hegel` builder, which is
public but marked `doc(hidden)`; the crate versions and `Cargo.lock` are pinned.

## Challenges

All 20 generated challenges and four state-machine variants from the main
comparison are implemented. Fixed-start challenges are intentionally omitted.

- Nested product and product-sequence composites, depths 2–6; depth-four sum.
- Modular mapping and weighted linear preservation.
- Invoice discount, constrained and fully derived.
- Float cancellation and chunked UTF-8 decoding.
- Hash collision at moduli 10, 100 and 1000, as generators and native state machines.
- Snapshot store, using a native state machine and Hegel pools for reusable and
  consumed snapshot references.

Generator/property ports are in [`src/challenges.rs`](src/challenges.rs), state
machines in [`src/stateful.rs`](src/stateful.rs), and recording in
[`src/lib.rs`](src/lib.rs). Per-challenge reports and raw results are under
[`reports/`](reports/).

## Running

Rust 1.86+; the checked-in results use Rust 1.93.1 and a release build.

```sh
cd pbt-libraries/hegel
make benchmark
```

This runs 100 seeds for each challenge, generates the reports, and refreshes
only Hegel's data rows and total-timing section in the root `README.md`.

Run one challenge, then generate its report:

```sh
cargo run --release --locked -- --challenge modular_mapping --iterations 100
python3 support/make_reports.py
```

List challenge names or replay one seed into a separate output directory:

```sh
cargo run --release --locked -- --list
cargo run --release --locked -- --challenge modular_mapping --seed 42 --output /tmp/hegel-results
python3 support/make_reports.py --reports /tmp/hegel-results
```

`--seed` reruns generation and shrinking under that seed; it is not direct
counterexample replay. `--iterations N` uses the first N seeds of the checked-in
100-seed list. `--seed-file PATH` can supply alternative lists, in the same JSON
format. A challenge's JSON is replaced only when every requested run succeeds;
a no-failure result or unexpected runner error causes a nonzero exit.

Regenerate Markdown and the comparison from existing 100-run JSON, without
rerunning the benchmark:

```sh
make comparison
```

## Comparison conventions

- [`support/seeds.json`](support/seeds.json) copies the numeric seeds from the
  corresponding Hypothesis JSON files. Equal seeds do not imply equal inputs
  across libraries. Generation uses each library's own distribution.
- Database reuse and targeting are disabled. Generation and shrinking are
  enabled, with one million allowed valid examples and health checks suppressed,
  matching the Hypothesis harness. Multiple-failure reporting is disabled.
- Evaluation counts start at the first property failure and include subsequent
  property calls, Hegel's confirmation calls, and final replay. A state-machine
  evaluation is a whole history, not an individual command. Rejected/overrun
  histories that never reach a property verdict are not counted.
- Counterexamples are rendered only when the property fails, as in the
  Hypothesis harness. Nested payloads are stored in full in JSON and included in
  original-length measurements; Markdown uses run-length notation. Float
  summaries normalise Rust's exponent spelling to Python's tuple representation.
- State machines use `.steps(50)` to match the comparison's command limit.
  Snapshot names are assigned in creation order, and released snapshots are
  removed from the pool. Sorted maps/sets make fixture iteration deterministic.
- The fully derived invoice uses `DefaultGenerator` with raw **i64** fields, no
  bounds, custom field generators, or assumption filtering. Invalid business
  inputs return a passing verdict, matching Hypothesis. This matches Swift's
  finite signed integer domain, not Python's arbitrary-precision `int` domain.
- Float cancellation uses `f64` in `[-1e6, 1e6]`; text uses Unicode scalars and
  sizes measured in characters, with UTF-8 byte boundaries used for chunking.
- Hegel's default shrink budgets are retained. No claim is made that its shrink
  policy/budget exactly matches Hypothesis 6.168.3.

## Timings

Only **total wall-clock time** is reported: generation, reduction,
recording, confirmation and final replay. The Rust API does not expose structured
phase durations, so no generation/reduction split is inferred from the time of
the first failure. Compilation, settings construction and environment discovery
are outside the timed region. JSON records the build profile, compiler, OS and
CPU metadata where available. The root comparison documents the recorded host
separately from the earlier Hypothesis/Exhaust measurements.

## Tests

```sh
make test
```

Tests exercise the deliberate fixture bugs, dependent generator constraints,
seeded generation/reduction, native state-machine shrinking, evaluation counting,
CLI output/error handling, report formatting, README refresh idempotence and
seed-list parity. Every checked-in original and reduced counterexample is also
replayed against independent fixture checks in Python.

README updates require all 24 release-build result files, the checked-in seed
lists, and consistent compiler/OS/CPU metadata.
