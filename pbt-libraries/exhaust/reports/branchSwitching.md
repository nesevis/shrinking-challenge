# Branch Switching

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/branchSwitching.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 15.0 | 15.0 |
| Original input length | 17.0 | 17.0 |
| Wall time (ms) | 2.030 | 2.030 |
| Wall time, Linux/Windows build (ms) | 4.038 | 4.038 |
| reductions (ms) | 1.770 | 1.770 |
| total (ms) | 1.915 | 1.915 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/branchSwitching.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `"    "` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.66 | 15.66 | 15.66 |
| Source core / debug runner (on macOS) | 16.89 | 16.89 | 16.89 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge branchSwitching --iterations 100 --seed 1337 --report-path ../failures
```
