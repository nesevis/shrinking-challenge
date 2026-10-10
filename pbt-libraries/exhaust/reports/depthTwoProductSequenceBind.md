# Nested Flatmap (product sequence), depth 2

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductSequenceBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 310.8 | 327.5 |
| Original input length | 141.0 | 122.0 |
| Wall time (ms) | 4.116 | 4.172 |
| Wall time, Linux/Windows build (ms) | 52.594 | 53.796 |
| generation (ms) | 0.027 | 0.024 |
| reductions (ms) | 3.910 | 3.980 |
| total (ms) | 3.936 | 4.006 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthTwoProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 99% | 🎯 `(6, 4, 0x23 + 1x1)` |
| 1% | `(9, 3, 0x26 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 16.00 | 16.00 | 16.42 |
| Source core / debug runner (on macOS) | 16.82 | 16.81 | 17.25 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthTwoProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
