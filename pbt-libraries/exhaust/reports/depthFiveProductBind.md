# Nested Flatmap (product), depth 5

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 69.8 | 43.5 |
| Original input length | 15.2 | 15.0 |
| Wall time (ms) | 6.311 | 6.087 |
| Wall time, Linux/Windows build (ms) | 30.282 | 29.168 |
| generation (ms) | 0.008 | 0.007 |
| reductions (ms) | 6.230 | 6.010 |
| total (ms) | 6.297 | 6.074 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFiveProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.09 | 15.09 | 15.28 |
| Source core / debug runner (on macOS) | 16.29 | 16.28 | 16.47 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthFiveProductBind --iterations 100 --seed 1337 --report-path ../failures
```
