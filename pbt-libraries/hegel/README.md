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

This runs seeds 1337–1436 for each challenge, generates the reports, and refreshes
only Hegel's data rows and total-timing section in the root `README.md`.

Run one challenge, then generate its report:

```sh
cargo run --release --locked -- --challenge modular_mapping --iterations 100
python3 support/make_reports.py
```

List challenge names or replay one seed into a separate output directory:

```sh
cargo run --release --locked -- --list
cargo run --release --locked -- --challenge modular_mapping --seed 42 --iterations 1 --output /tmp/hegel-results
python3 support/make_reports.py --reports /tmp/hegel-results
```

The CLI defaults to 100 consecutive seeds starting at **1337**. `--seed N` sets
the starting seed, and `--iterations K` runs `N` through `N + K - 1` for each
selected challenge. Use `--iterations 1` for a single seed. `--seed` also works
with `--challenge all`; no JSON seed file is needed. Generation and shrinking
are rerun, rather than directly replaying a counterexample. Seed overflow is
rejected before running.

A challenge's JSON is replaced only when every requested run succeeds;
a no-failure result or unexpected runner error causes a nonzero exit.

Regenerate Markdown and the comparison from existing 100-run JSON, without
rerunning the benchmark:

```sh
make comparison
```

## Binary heap port

The original [wrong binary heap challenge](../../challenges/binheap.md) is also
implemented in [`src/binary_heap.rs`](src/binary_heap.rs). It matches Exhaust's
bounded depth, dependent signed-64-bit keys, empty/node multiplicity, and buggy
right-before-left traversal. [100-seed results](reports/binheap.md) are kept separate
from the existing published comparison.

```sh
cargo run --release --locked -- --challenge binheap --seed 42 --iterations 1 --output /tmp/hegel-binheap
cargo run --release --locked -- --challenge binheap --seed 1337 --iterations 100 --output reports
```

`--list` includes this standalone port; `--challenge all` retains the existing
comparison suite. The existing comparison-report scripts remain scoped to the published suite.

## Calculator port

The original [calculator challenge](../../challenges/calculator.md) is implemented
in [`src/calculator.rs`](src/calculator.rs), using the public recursive generator
with signed-64-bit leaves and a maximum depth of 5. Literal `x / 0` subterms are
rejected, but a computed zero denominator still fails. Exact widened arithmetic
and floor division follow Python's evaluation semantics within the bounded
expression domain, avoiding machine-overflow failures.

```sh
cargo run --release --locked -- --challenge calculator --seed 42 --iterations 1 --output /tmp/hegel-calculator
cargo run --release --locked -- --challenge calculator --seed 1337 --iterations 100 --output reports
```

This is another standalone port listed by `--list`, outside `--challenge all` and
the existing comparison-report scripts. See [the 100-seed report](reports/calculator.md)
for results and generator/domain differences from Hypothesis and Exhaust.

## Refund allocation ports

The [refund allocation challenge](../../challenges/refund-allocation.md) is implemented
in [`src/refund_allocation.rs`](src/refund_allocation.rs), with handwritten and raw
`DefaultGenerator` treatments. Both preserve Exhaust's 30-cent non-refundable fee,
1–20-charge domain, signed-64-bit amounts, exact widened arithmetic, stable remainder
ties, and deliberately incorrect gross-payment weighting. Invalid requests are
rejected with `tc.assume`, before recording any property verdict.

```sh
cargo run --release --locked -- --challenge refund_allocation --seed 42 --iterations 1 --output /tmp/hegel-refund
cargo run --release --locked -- --challenge refund_allocation_derived --seed 1337 \
  --iterations 100 --output /tmp/hegel-refund
```

Both appear in `--list`, outside `--challenge all` and the published comparison
scripts. Sequential runs starting at 1337 match Exhaust's numeric seeds, not its
generated inputs. Existing reporting is unchanged.

## Comparison conventions

- New runs use consecutive seeds, starting at 1337 by default. Historical checked-in
  results used the numeric seeds from the corresponding Hypothesis JSON files.
  Those recorded seeds remain in the result JSON; replay an individual run with
  `--seed N --iterations 1`. Equal seeds do not imply equal inputs across libraries.
  Report refresh accepts a consistent consecutive schedule or the historical
  Hypothesis-derived schedules, and rejects mixed schedules. Generation uses each
  library's own distribution.
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
seed-schedule consistency. Every checked-in original and reduced counterexample is also
replayed against independent fixture checks in Python.

README updates require all 24 release-build result files, the checked-in seed
lists, and consistent compiler/OS/CPU metadata.
