# Hash Collision (M = 1000)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionThousand.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 651.7 | 650.5 |
| Original input length | 117.5 | 119.5 |
| Wall time (ms) | 5.943 | 5.083 |
| Wall time, Linux/Windows build (ms) | 12.698 | 11.431 |
| generation (ms) | 3.032 | 2.138 |
| reductions (ms) | 2.830 | 2.810 |
| total (ms) | 5.928 | 5.071 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionThousand.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 71% | 🎯 `([(0, 0)], 1000, 1)` |
| 14% | `([(0, 0)], 3000, 1)` |
| 9% | `([(0, 0)], 5000, 1)` |
| 4% | `([(0, 0)], 7000, 1)` |
| 2% | `([(0, 0)], 9000, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.73 | 14.73 | 14.91 |
| Source core / debug runner (on macOS) | 15.81 | 15.83 | 16.00 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionThousand --iterations 100 --seed 1337 --report-path ../failures
```
