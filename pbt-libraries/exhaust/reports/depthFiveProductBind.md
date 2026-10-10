# Nested Flatmap (product), depth 5

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 69.8 | 43.5 |
| Original input length | 15.2 | 15.0 |
| Wall time (ms) | 6.094 | 5.871 |
| Wall time, Linux/Windows build (ms) | 33.757 | 32.647 |
| generation (ms) | 0.009 | 0.008 |
| reductions (ms) | 5.990 | 5.760 |
| total (ms) | 5.999 | 5.766 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFiveProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.39 | 15.38 | 15.61 |
| Source core / debug runner (on macOS) | 16.35 | 16.34 | 16.61 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthFiveProductBind --iterations 100 --seed 1337 --report-path ../failures
```
