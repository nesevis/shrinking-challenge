# Nested Flatmap (product), depth 2

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 32.3 | 35.0 |
| Original input length | 6.2 | 6.0 |
| Wall time (ms) | 0.279 | 0.279 |
| Wall time, Linux/Windows build (ms) | 1.139 | 1.191 |
| generation (ms) | 0.005 | 0.004 |
| reductions (ms) | 0.220 | 0.230 |
| total (ms) | 0.228 | 0.232 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthTwoProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(5, 5)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.51 | 14.53 | 14.62 |
| Source core / debug runner (on macOS) | 15.44 | 15.47 | 15.55 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthTwoProductBind --iterations 100 --seed 1337 --report-path ../failures
```
