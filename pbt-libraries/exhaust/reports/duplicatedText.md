# Duplicated Text

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/duplicatedText.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 54.0 | 54.0 |
| Original input length | 24.0 | 24.0 |
| Wall time (ms) | 1.391 | 1.391 |
| Wall time, Linux/Windows build (ms) | 4.468 | 4.468 |
| reductions (ms) | 1.120 | 1.120 |
| total (ms) | 1.246 | 1.246 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/duplicatedText.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `("10210210", "10210210")` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.80 | 14.80 | 14.80 |
| Source core / debug runner (on macOS) | 15.81 | 15.81 | 15.81 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge duplicatedText --iterations 100 --seed 1337 --report-path ../failures
```
