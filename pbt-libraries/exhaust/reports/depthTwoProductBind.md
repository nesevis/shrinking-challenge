# Nested Flatmap (product), depth 2

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 32.3 | 35.0 |
| Original input length | 6.2 | 6.0 |
| Wall time (ms) | 0.273 | 0.284 |
| Wall time, Linux/Windows build (ms) | 1.019 | 1.046 |
| generation (ms) | 0.005 | 0.004 |
| reductions (ms) | 0.230 | 0.240 |
| total (ms) | 0.263 | 0.275 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthTwoProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(5, 5)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.27 | 14.30 | 14.36 |
| Source core / debug runner (on macOS) | 15.33 | 15.35 | 15.42 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthTwoProductBind --iterations 100 --seed 1337 --report-path ../failures
```
