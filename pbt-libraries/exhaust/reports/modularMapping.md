# Modular Mapping

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/modularMapping.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 17.5 | 16.0 |
| Original input length | 3.0 | 3.0 |
| Wall time (ms) | 0.063 | 0.054 |
| Wall time, Linux/Windows build (ms) | 0.203 | 0.184 |
| generation (ms) | 0.003 | 0.002 |
| reductions (ms) | 0.030 | 0.030 |
| total (ms) | 0.035 | 0.030 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/modularMapping.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (18 distinct)

| Share | Counterexample |
|---|---|
| 15% | 🎯 `925` |
| 13% | `921` |
| 10% | `901` |
| 9% | `917` |
| 9% | `913` |
| 8% | `909` |
| 8% | `905` |
| 8% | `934` |
| 5% | `910` |
| 3% | `906` |
| 3% | `932` |
| 2% | `926` |
| 2% | `902` |
| 1% | `904` |
| 1% | `931` |
| 1% | `922` |
| 1% | `927` |
| 1% | `918` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.09 | 14.09 | 14.20 |
| Source core / debug runner (on macOS) | 15.01 | 15.03 | 15.11 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge modularMapping --iterations 100 --seed 1337 --report-path ../failures
```
