# Distinct Sum

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/distinctSum.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 636.0 | 636.0 |
| Original input length | 36.0 | 36.0 |
| Wall time (ms) | 2.753 | 2.753 |
| Wall time, Linux/Windows build (ms) | 8.277 | 8.277 |
| reductions (ms) | 2.550 | 2.550 |
| total (ms) | 2.638 | 2.638 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/distinctSum.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `[-2, -1, 0, 1, 53]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.44 | 14.44 | 14.44 |
| Source core / debug runner (on macOS) | 15.55 | 15.55 | 15.55 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge distinctSum --iterations 100 --seed 1337 --report-path ../failures
```
