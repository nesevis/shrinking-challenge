# Nested Flatmap (product), depth 4

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 72.5 | 81.5 |
| Original input length | 12.2 | 12.0 |
| Wall time (ms) | 2.450 | 2.604 |
| Wall time, Linux/Windows build (ms) | 11.333 | 12.122 |
| generation (ms) | 0.008 | 0.007 |
| reductions (ms) | 2.370 | 2.530 |
| total (ms) | 2.435 | 2.591 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 2, 2, 2)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.66 | 14.67 | 14.84 |
| Source core / debug runner (on macOS) | 15.79 | 15.81 | 15.95 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthFourProductBind --iterations 100 --seed 1337 --report-path ../failures
```
