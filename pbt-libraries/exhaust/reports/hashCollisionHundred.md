# Hash Collision (M = 100)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionHundred.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 692.3 | 616.0 |
| Original input length | 61.8 | 53.5 |
| Wall time (ms) | 3.215 | 2.891 |
| Wall time, Linux/Windows build (ms) | 9.197 | 8.356 |
| generation (ms) | 0.236 | 0.195 |
| reductions (ms) | 2.910 | 2.620 |
| total (ms) | 3.203 | 2.881 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionHundred.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 70% | 🎯 `([(0, 0)], 100, 1)` |
| 20% | `([(0, 0)], 300, 1)` |
| 7% | `([(0, 0)], 700, 1)` |
| 3% | `([(0, 0)], 900, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.63 | 14.64 | 14.84 |
| Source core / debug runner (on macOS) | 15.72 | 15.72 | 15.91 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionHundred --iterations 100 --seed 1337 --report-path ../failures
```
