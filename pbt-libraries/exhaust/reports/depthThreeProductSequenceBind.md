# Nested Flatmap (product sequence), depth 3

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductSequenceBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 299.3 | 290.0 |
| Original input length | 386.3 | 252.5 |
| Wall time (ms) | 6.336 | 5.189 |
| Wall time, Linux/Windows build (ms) | 66.670 | 58.976 |
| generation (ms) | 0.047 | 0.038 |
| reductions (ms) | 6.150 | 5.000 |
| total (ms) | 6.321 | 5.173 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthThreeProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 80% | 🎯 `(4, 3, 2, 0x23 + 1x1)` |
| 16% | `(6, 2, 2, 0x23 + 1x1)` |
| 3% | `(7, 2, 2, 0x27 + 1x1)` |
| 1% | `(9, 3, 1, 0x26 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 16.23 | 16.15 | 18.09 |
| Source core / debug runner (on macOS) | 17.39 | 17.31 | 19.20 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthThreeProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
