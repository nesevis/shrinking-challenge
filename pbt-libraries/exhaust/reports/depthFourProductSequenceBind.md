# Nested Flatmap (product sequence), depth 4

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductSequenceBind.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 304.6 | 213.0 |
| Original input length | 1107.9 | 374.5 |
| Wall time (ms) | 46.510 | 9.991 |
| Wall time, Linux/Windows build (ms) | 339.917 | 87.867 |
| generation (ms) | 0.110 | 0.045 |
| reductions (ms) | 46.200 | 9.760 |
| total (ms) | 46.308 | 9.806 |

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
| macOS XCFramework / debug runner | 17.97 | 17.48 | 30.55 |
| Source core / debug runner (on macOS) | 18.87 | 18.36 | 29.27 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge depthFourProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
