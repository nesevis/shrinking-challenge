# Hash Collision (M = 100)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionHundred.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 692.1 | 616.0 |
| Original input length | 61.8 | 53.5 |
| Wall time (ms) | 3.458 | 3.076 |
| Wall time, Linux/Windows build (ms) | 10.848 | 9.829 |
| generation (ms) | 0.263 | 0.215 |
| reductions (ms) | 3.100 | 2.770 |
| total (ms) | 3.367 | 2.997 |

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
| macOS XCFramework / debug runner | 14.86 | 14.86 | 15.00 |
| Source core / debug runner (on macOS) | 15.84 | 15.86 | 16.00 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionHundred --iterations 100 --seed 1337 --report-path ../failures
```
