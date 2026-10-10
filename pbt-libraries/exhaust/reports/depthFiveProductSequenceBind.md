# Nested Flatmap (product sequence), depth 5

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductSequenceBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 707.9 | 167.5 |
| Original input length | 3737.7 | 398.0 |
| Wall time (ms) | 1054.140 | 33.035 |
| Wall time, Linux/Windows build (ms) | 4387.547 | 279.965 |
| generation (ms) | 0.355 | 0.055 |
| reductions (ms) | 1053.530 | 32.790 |
| total (ms) | 1053.889 | 32.822 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFiveProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (10 distinct)

| Share | Counterexample |
|---|---|
| 86% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 0x26 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 0x41 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 0x27 + 1x1)` |
| 1% | `(9, 7, 2, 1, 1, 0x125 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 0x55 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 0x55 + 1x1)` |

## Source-debug counterexamples (13 distinct)

| Share | Counterexample |
|---|---|
| 83% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 0x26 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 0x41 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 0x27 + 1x1)` |
| 1% | `(8, 8, 8, 7, 6, 0x19393 + 1x2111)` |
| 1% | `(9, 7, 2, 1, 1, 0x125 + 1x1)` |
| 1% | `(10, 8, 8, 8, 6, 0x21719 + 1x9001)` |
| 1% | `(10, 8, 8, 7, 5, 0x19698 + 1x2702)` |
| 1% | `(7, 2, 2, 2, 1, 0x55 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 0x55 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 22.20 | 19.80 | 98.22 |
| Source core / debug runner (on macOS) | 22.55 | 20.48 | 76.72 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthFiveProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
