# Snapshot Store

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/snapshotStore.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 240.4 | 214.0 |
| Original input length | 497.0 | 501.5 |
| Wall time (ms) | 8.922 | 8.166 |
| Wall time, Linux/Windows build (ms) | 32.845 | 29.532 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 6.260 | 5.430 |
| total (ms) | 8.896 | 8.143 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/snapshotStore.json)).

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

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 16.16 | 16.17 | 16.56 |
| Source core / debug runner (on macOS) | 17.47 | 17.48 | 17.78 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge snapshotStore --iterations 100 --seed 1337 --report-path ../failures
```
