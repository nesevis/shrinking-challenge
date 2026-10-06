# Nested Flatmap (product), depth 3

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 58.1 | 63.0 |
| Original input length | 9.2 | 9.0 |
| Wall time (ms) | 0.937 | 1.085 |
| Wall time, Linux/Windows build (ms) | 3.952 | 4.672 |
| generation (ms) | 0.006 | 0.005 |
| reductions (ms) | 0.880 | 1.030 |
| total (ms) | 0.926 | 1.076 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthThreeProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 3, 3)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.47 | 14.47 | 14.56 |
| Source core / debug runner (on macOS) | 15.56 | 15.57 | 15.69 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthThreeProductBind --iterations 100 --seed 1337 --report-path ../failures
```
