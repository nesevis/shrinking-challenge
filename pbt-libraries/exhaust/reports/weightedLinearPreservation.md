# Weighted Linear Preservation

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/weightedLinearPreservation.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 156.8 | 93.0 |
| Original input length | 9.6 | 10.0 |
| Wall time (ms) | 0.507 | 0.379 |
| Wall time, Linux/Windows build (ms) | 2.587 | 1.718 |
| generation (ms) | 0.039 | 0.027 |
| reductions (ms) | 0.410 | 0.260 |
| total (ms) | 0.450 | 0.326 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/weightedLinearPreservation.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(0, 0, 20)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.49 | 14.52 | 14.70 |
| Source core / debug runner (on macOS) | 15.51 | 15.54 | 15.70 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge weightedLinearPreservation --iterations 100 --seed 1337 --report-path ../failures
```
