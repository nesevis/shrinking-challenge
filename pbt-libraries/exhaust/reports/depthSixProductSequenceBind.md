# Nested Flatmap (product sequence), depth 6

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthSixProductSequenceBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1057.6 | 155.0 |
| Original input length | 5867.6 | 422.5 |
| Wall time (ms) | 2201.560 | 146.276 |
| Wall time, Linux/Windows build (ms) | 7211.751 | 1263.460 |
| generation (ms) | 0.523 | 0.058 |
| reductions (ms) | 2200.670 | 145.780 |
| total (ms) | 2201.202 | 145.967 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthSixProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (29 distinct)

| Share | Counterexample |
|---|---|
| 57% | `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)` |
| 4% | `(5, 4, 3, 2, 1, 1, 0x119 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 1, 0x29 + 1x1)` |
| 3% | `(4, 3, 3, 1, 1, 1, 0x35 + 1x1)` |
| 3% | `(5, 5, 5, 1, 1, 1, 0x124 + 1x1)` |
| 2% | `(4, 2, 2, 2, 1, 1, 0x31 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 1, 0x26 + 1x1)` |
| 2% | `(3, 3, 3, 2, 1, 1, 0x53 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 1, 0x41 + 1x1)` |
| 2% | `(8, 5, 2, 2, 1, 1, 0x159 + 1x1)` |
| 1% | `(5, 4, 3, 1, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(8, 7, 2, 2, 1, 1, 0x223 + 1x1)` |
| 1% | `(5, 3, 3, 1, 1, 1, 0x44 + 1x1)` |
| 1% | `(5, 2, 2, 2, 1, 1, 0x39 + 1x1)` |
| 1% | `(6, 4, 3, 1, 1, 1, 0x71 + 1x1)` |
| 1% | `(5, 3, 3, 2, 1, 1, 0x89 + 1x1)` |
| 1% | `(7, 4, 2, 2, 1, 1, 0x111 + 1x1)` |
| 1% | `(10, 9, 3, 2, 1, 1, 0x539 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 1, 0x27 + 1x1)` |
| 1% | `(9, 7, 2, 1, 1, 1, 0x125 + 1x1)` |
| 1% | `(10, 7, 2, 1, 1, 1, 0x139 + 1x1)` |
| 1% | `(6, 3, 2, 2, 2, 1, 0x143 + 1x1)` |
| 1% | `(4, 3, 2, 2, 1, 1, 0x47 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 1, 0x55 + 1x1)` |
| 1% | `(7, 2, 2, 2, 2, 1, 0x111 + 1x1)` |
| 1% | `(3, 3, 2, 2, 1, 1, 0x35 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 1, 0x55 + 1x1)` |

## Source-debug counterexamples (32 distinct)

| Share | Counterexample |
|---|---|
| 54% | `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)` |
| 4% | `(5, 4, 3, 2, 1, 1, 0x119 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 1, 0x29 + 1x1)` |
| 3% | `(4, 3, 3, 1, 1, 1, 0x35 + 1x1)` |
| 3% | `(5, 5, 5, 1, 1, 1, 0x124 + 1x1)` |
| 2% | `(4, 2, 2, 2, 1, 1, 0x31 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 1, 0x26 + 1x1)` |
| 2% | `(3, 3, 3, 2, 1, 1, 0x53 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 1, 0x41 + 1x1)` |
| 2% | `(8, 5, 2, 2, 1, 1, 0x159 + 1x1)` |
| 1% | `(5, 4, 3, 1, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(8, 7, 2, 2, 1, 1, 0x223 + 1x1)` |
| 1% | `(5, 3, 3, 1, 1, 1, 0x44 + 1x1)` |
| 1% | `(5, 2, 2, 2, 1, 1, 0x39 + 1x1)` |
| 1% | `(6, 4, 3, 1, 1, 1, 0x71 + 1x1)` |
| 1% | `(5, 3, 3, 2, 1, 1, 0x89 + 1x1)` |
| 1% | `(7, 4, 2, 2, 1, 1, 0x111 + 1x1)` |
| 1% | `(10, 9, 3, 2, 1, 1, 0x539 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 1, 0x27 + 1x1)` |
| 1% | `(8, 8, 8, 7, 6, 1, 0x19341 + 1x2163)` |
| 1% | `(9, 7, 2, 1, 1, 1, 0x125 + 1x1)` |
| 1% | `(10, 7, 2, 1, 1, 1, 0x139 + 1x1)` |
| 1% | `(6, 3, 2, 2, 2, 1, 0x143 + 1x1)` |
| 1% | `(10, 8, 8, 8, 6, 1, 0x21673 + 1x9047)` |
| 1% | `(10, 8, 8, 7, 5, 2, 0x27164 + 1x17636)` |
| 1% | `(4, 3, 2, 2, 1, 1, 0x47 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 1, 0x55 + 1x1)` |
| 1% | `(7, 2, 2, 2, 2, 1, 0x111 + 1x1)` |
| 1% | `(3, 3, 2, 2, 1, 1, 0x35 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 1, 0x55 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 29.45 | 24.34 | 124.28 |
| Source core / debug runner (on macOS) | 30.62 | 26.18 | 89.66 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthSixProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
