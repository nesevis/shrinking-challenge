# Weighted Linear Preservation

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/weightedLinearPreservation.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 154.4 | 93.0 |
| Original input length | 9.6 | 10.0 |
| Wall time (ms) | 0.507 | 0.383 |
| Wall time, Linux/Windows build (ms) | 2.136 | 1.449 |
| generation (ms) | 0.039 | 0.028 |
| reductions (ms) | 0.420 | 0.270 |
| total (ms) | 0.497 | 0.375 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/weightedLinearPreservation.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(0, 0, 20)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.24 | 14.27 | 14.39 |
| Source core / debug runner (on macOS) | 15.43 | 15.46 | 15.61 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge weightedLinearPreservation --iterations 100 --seed 1337 --report-path ../failures
```
