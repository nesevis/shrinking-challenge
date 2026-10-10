# Nested Flatmap (product sequence), depth 3

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductSequenceBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 295.1 | 290.0 |
| Original input length | 386.3 | 252.5 |
| Wall time (ms) | 6.499 | 5.300 |
| Wall time, Linux/Windows build (ms) | 75.580 | 69.044 |
| generation (ms) | 0.049 | 0.041 |
| reductions (ms) | 6.260 | 5.080 |
| total (ms) | 6.312 | 5.126 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthThreeProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 78% | 🎯 `(4, 3, 2, 0x23 + 1x1)` |
| 16% | `(6, 2, 2, 0x23 + 1x1)` |
| 3% | `(9, 3, 1, 0x26 + 1x1)` |
| 3% | `(7, 2, 2, 0x27 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 16.47 | 16.42 | 18.05 |
| Source core / debug runner (on macOS) | 17.36 | 17.33 | 19.25 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthThreeProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
