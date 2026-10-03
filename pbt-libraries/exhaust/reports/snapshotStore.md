# Snapshot Store

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/snapshotStore.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 229.7 | 204.5 |
| Original input length | 497.0 | 501.5 |
| Wall time (ms) | 6.279 | 5.765 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 4.830 | 4.240 |
| total (ms) | 6.257 | 5.747 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (17 distinct)

| Share | Counterexample |
|---|---|
| 67% | 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 6% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
| 5% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
| 4% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), release(s2), compact(), read(s0, 0)]` |
| 3% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 0)]` |
| 3% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 0)]` |
| 2% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), s3 = snapshot(), release(s3), compact(), s4 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), release(s3), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), release(s3), release(s2), release(s1), s4 = snapshot(), s5 = snapshot(), s6 = snapshot(), compact(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), release(s3), s4 = snapshot(), s5 = snapshot(), compact(), release(s5), s6 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), s4 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), compact(), s3 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), release(s4), s5 = snapshot(), read(s0, 0)]` |

## Running

```sh
swift run -c release ExhaustRunner --challenge snapshotStore --iterations 100 --seed 1337 --report-path ../failures
```
