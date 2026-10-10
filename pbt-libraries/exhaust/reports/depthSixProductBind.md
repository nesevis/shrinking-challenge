# Nested Flatmap (product), depth 6

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthSixProductBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 30.5 | 31.0 |
| Original input length | 18.2 | 18.0 |
| Wall time (ms) | 13.876 | 14.139 |
| Wall time, Linux/Windows build (ms) | 78.633 | 80.266 |
| generation (ms) | 0.013 | 0.012 |
| reductions (ms) | 13.720 | 14.010 |
| total (ms) | 13.739 | 14.021 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthSixProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.81 | 15.77 | 16.38 |
| Source core / debug runner (on macOS) | 16.79 | 16.77 | 17.41 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthSixProductBind --iterations 100 --seed 1337 --report-path ../failures
```
