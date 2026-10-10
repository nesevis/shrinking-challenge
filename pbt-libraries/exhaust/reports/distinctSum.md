# Distinct Sum

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/distinctSum.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 638.0 | 638.0 |
| Original input length | 36.0 | 36.0 |
| Wall time (ms) | 3.073 | 3.073 |
| Wall time, Linux/Windows build (ms) | 10.955 | 10.955 |
| reductions (ms) | 2.850 | 2.850 |
| total (ms) | 2.956 | 2.956 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/distinctSum.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `[-2, -1, 0, 1, 53]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.67 | 14.67 | 14.67 |
| Source core / debug runner (on macOS) | 15.53 | 15.53 | 15.53 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge distinctSum --iterations 100 --seed 1337 --report-path ../failures
```
