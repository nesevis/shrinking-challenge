# Nested Flatmap (product sequence), depth 5

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductSequenceBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 707.0 | 165.5 |
| Original input length | 3737.7 | 398.0 |
| Wall time (ms) | 1055.697 | 34.008 |
| Wall time, Linux/Windows build (ms) | 4326.288 | 249.195 |
| generation (ms) | 0.346 | 0.051 |
| reductions (ms) | 1055.140 | 33.730 |
| total (ms) | 1055.670 | 33.985 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFiveProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (11 distinct)

| Share | Counterexample |
|---|---|
| 85% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 0x26 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 0x41 + 1x1)` |
| 1% | `(6, 5, 2, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 0x27 + 1x1)` |
| 1% | `(9, 7, 2, 1, 1, 0x125 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 0x55 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 0x55 + 1x1)` |

## Source-debug counterexamples (14 distinct)

| Share | Counterexample |
|---|---|
| 82% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 0x26 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 0x41 + 1x1)` |
| 1% | `(6, 5, 2, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 0x27 + 1x1)` |
| 1% | `(8, 8, 8, 7, 6, 0x19983 + 1x1521)` |
| 1% | `(9, 7, 2, 1, 1, 0x125 + 1x1)` |
| 1% | `(10, 8, 8, 8, 6, 0x22232 + 1x8488)` |
| 1% | `(10, 8, 8, 7, 5, 0x20322 + 1x2078)` |
| 1% | `(7, 2, 2, 2, 1, 0x55 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 0x55 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 21.75 | 19.38 | 95.39 |
| Source core / debug runner (on macOS) | 22.73 | 20.85 | 76.62 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthFiveProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
