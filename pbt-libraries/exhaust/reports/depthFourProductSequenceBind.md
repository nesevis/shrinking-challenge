# Nested Flatmap (product sequence), depth 4

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductSequenceBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 304.6 | 213.0 |
| Original input length | 1107.9 | 374.5 |
| Wall time (ms) | 45.543 | 10.166 |
| Wall time, Linux/Windows build (ms) | 313.938 | 75.951 |
| generation (ms) | 0.112 | 0.044 |
| reductions (ms) | 45.260 | 9.960 |
| total (ms) | 45.521 | 10.143 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 89% | 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
| 9% | `(3, 3, 3, 1, 0x26 + 1x1)` |
| 1% | `(9, 3, 1, 1, 0x26 + 1x1)` |
| 1% | `(7, 2, 2, 1, 0x27 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 17.62 | 17.15 | 26.66 |
| Source core / debug runner (on macOS) | 18.93 | 18.38 | 30.31 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthFourProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
