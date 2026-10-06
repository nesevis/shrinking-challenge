# Nested Flatmap (product), depth 6

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthSixProductBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 30.5 | 31.0 |
| Original input length | 18.2 | 18.0 |
| Wall time (ms) | 14.264 | 14.614 |
| Wall time, Linux/Windows build (ms) | 71.512 | 72.810 |
| generation (ms) | 0.011 | 0.010 |
| reductions (ms) | 14.150 | 14.510 |
| total (ms) | 14.244 | 14.596 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthSixProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.54 | 15.52 | 16.09 |
| Source core / debug runner (on macOS) | 16.77 | 16.73 | 17.33 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthSixProductBind --iterations 100 --seed 1337 --report-path ../failures
```
