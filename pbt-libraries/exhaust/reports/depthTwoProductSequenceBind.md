# Nested Flatmap (product sequence), depth 2

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductSequenceBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 310.8 | 327.5 |
| Original input length | 141.0 | 122.0 |
| Wall time (ms) | 3.409 | 3.493 |
| Wall time, Linux/Windows build (ms) | 40.872 | 41.579 |
| generation (ms) | 0.021 | 0.020 |
| reductions (ms) | 3.270 | 3.360 |
| total (ms) | 3.396 | 3.482 |

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
| macOS XCFramework / debug runner | 15.57 | 15.54 | 16.00 |
| Source core / debug runner (on macOS) | 16.70 | 16.68 | 17.16 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthTwoProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
