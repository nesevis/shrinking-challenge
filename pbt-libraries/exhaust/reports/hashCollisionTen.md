# Hash Collision (M = 10)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionTen.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 198.8 | 167.0 |
| Original input length | 29.9 | 27.0 |
| Wall time (ms) | 1.150 | 1.001 |
| Wall time, Linux/Windows build (ms) | 3.935 | 3.438 |
| generation (ms) | 0.058 | 0.052 |
| reductions (ms) | 1.020 | 0.870 |
| total (ms) | 1.077 | 0.929 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionTen.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `([(0, 0)], 10, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.77 | 14.78 | 14.92 |
| Source core / debug runner (on macOS) | 15.73 | 15.72 | 15.89 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionTen --iterations 100 --seed 1337 --report-path ../failures
```
