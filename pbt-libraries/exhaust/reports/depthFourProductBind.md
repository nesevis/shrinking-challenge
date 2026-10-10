# Nested Flatmap (product), depth 4

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 73.6 | 82.5 |
| Original input length | 12.2 | 12.0 |
| Wall time (ms) | 2.334 | 2.482 |
| Wall time, Linux/Windows build (ms) | 12.201 | 13.149 |
| generation (ms) | 0.007 | 0.006 |
| reductions (ms) | 2.250 | 2.410 |
| total (ms) | 2.262 | 2.420 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 2, 2, 2)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.94 | 14.95 | 15.09 |
| Source core / debug runner (on macOS) | 15.91 | 15.92 | 16.06 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthFourProductBind --iterations 100 --seed 1337 --report-path ../failures
```
