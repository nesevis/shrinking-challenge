# Duplicated Text

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/duplicatedText.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 54.0 | 54.0 |
| Original input length | 24.0 | 24.0 |
| Wall time (ms) | 1.317 | 1.317 |
| Wall time, Linux/Windows build (ms) | 4.051 | 4.051 |
| reductions (ms) | 1.070 | 1.070 |
| total (ms) | 1.186 | 1.186 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/duplicatedText.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `("10210210", "10210210")` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.67 | 14.67 | 14.67 |
| Source core / debug runner (on macOS) | 15.86 | 15.86 | 15.86 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge duplicatedText --iterations 100 --seed 1337 --report-path ../failures
```
