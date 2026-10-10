# Nested Flatmap (product), depth 3

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 60.1 | 65.0 |
| Original input length | 9.2 | 9.0 |
| Wall time (ms) | 1.000 | 1.097 |
| Wall time, Linux/Windows build (ms) | 4.468 | 5.248 |
| generation (ms) | 0.007 | 0.006 |
| reductions (ms) | 0.910 | 1.030 |
| total (ms) | 0.922 | 1.038 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthThreeProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 3, 3)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.72 | 14.73 | 14.84 |
| Source core / debug runner (on macOS) | 15.70 | 15.70 | 15.83 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthThreeProductBind --iterations 100 --seed 1337 --report-path ../failures
```
