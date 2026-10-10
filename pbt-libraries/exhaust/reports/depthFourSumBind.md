# Nested Flatmap (sum), depth 4

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourSumBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 734.4 | 530.5 |
| Original input length | 344.8 | 339.5 |
| Wall time (ms) | 20.249 | 15.428 |
| Wall time, Linux/Windows build (ms) | 251.551 | 146.267 |
| generation (ms) | 0.053 | 0.051 |
| reductions (ms) | 19.970 | 15.130 |
| total (ms) | 20.030 | 15.195 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourSumBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 17.74 | 17.39 | 20.56 |
| Source core / debug runner (on macOS) | 18.68 | 18.34 | 21.48 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthFourSumBind --iterations 100 --seed 1337 --report-path ../failures
```
