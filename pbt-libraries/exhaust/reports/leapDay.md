# Leap Day

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/leapDay.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 34.0 | 34.0 |
| Original input length | 25.0 | 25.0 |
| Wall time (ms) | 3.701 | 3.701 |
| Wall time, Linux/Windows build (ms) | 4.802 | 4.802 |
| reductions (ms) | 0.720 | 0.720 |
| total (ms) | 3.571 | 3.571 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/leapDay.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `2088-02-29 00:00:00 +0000` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 17.00 | 17.00 | 17.00 |
| Source core / debug runner (on macOS) | 17.80 | 17.80 | 17.80 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge leapDay --iterations 100 --seed 1337 --report-path ../failures
```
