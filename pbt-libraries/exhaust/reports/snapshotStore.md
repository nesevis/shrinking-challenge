# Snapshot Store

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/snapshotStore.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 240.6 | 223.5 |
| Original input length | 497.0 | 501.5 |
| Wall time (ms) | 8.386 | 7.143 |
| Wall time, Linux/Windows build (ms) | 34.828 | 32.008 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 5.810 | 5.070 |
| total (ms) | 8.341 | 7.100 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/snapshotStore.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (10 distinct)

| Share | Counterexample |
|---|---|
| 73% | 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 9% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
| 7% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
| 4% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 0)]` |
| 2% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), release(s3), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), release(s2), compact(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), release(s4), s5 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), read(s0, 0)]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.92 | 15.91 | 16.28 |
| Source core / debug runner (on macOS) | 17.37 | 17.37 | 17.73 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge snapshotStore --iterations 100 --seed 1337 --report-path ../failures
```
