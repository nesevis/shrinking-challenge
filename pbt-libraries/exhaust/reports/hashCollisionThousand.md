# Hash Collision (M = 1000)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionThousand.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 651.5 | 650.5 |
| Original input length | 117.5 | 119.5 |
| Wall time (ms) | 6.601 | 5.543 |
| Wall time, Linux/Windows build (ms) | 14.976 | 13.632 |
| generation (ms) | 3.532 | 2.519 |
| reductions (ms) | 2.970 | 2.960 |
| total (ms) | 6.502 | 5.460 |

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
| macOS XCFramework / debug runner | 14.98 | 14.98 | 15.16 |
| Source core / debug runner (on macOS) | 15.94 | 15.94 | 16.16 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionThousand --iterations 100 --seed 1337 --report-path ../failures
```
