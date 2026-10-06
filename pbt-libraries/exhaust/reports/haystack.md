# Haystack

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/haystack.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 407.0 | 407.0 |
| Original input length | 480.0 | 480.0 |
| Wall time (ms) | 11.236 | 11.236 |
| Wall time, Linux/Windows build (ms) | 67.076 | 67.076 |
| reductions (ms) | 8.070 | 8.070 |
| total (ms) | 11.094 | 11.094 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/haystack.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"CREEPIDIOT"` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 18.59 | 18.59 | 18.59 |
| Source core / debug runner (on macOS) | 19.89 | 19.89 | 19.89 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge haystack --iterations 100 --seed 1337 --report-path ../failures
```
