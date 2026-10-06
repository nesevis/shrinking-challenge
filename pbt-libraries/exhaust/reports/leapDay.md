# Leap Day

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/leapDay.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 34.0 | 34.0 |
| Original input length | 25.0 | 25.0 |
| Wall time (ms) | 3.702 | 3.702 |
| Wall time, Linux/Windows build (ms) | 4.206 | 4.206 |
| reductions (ms) | 0.690 | 0.690 |
| total (ms) | 3.600 | 3.600 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/leapDay.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `2088-02-29 00:00:00 +0000` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 16.95 | 16.95 | 16.95 |
| Source core / debug runner (on macOS) | 17.80 | 17.80 | 17.80 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge leapDay --iterations 100 --seed 1337 --report-path ../failures
```
