# Hash Collision (M = 10)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionTen.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 198.6 | 166.5 |
| Original input length | 29.9 | 27.0 |
| Wall time (ms) | 1.117 | 0.973 |
| Wall time, Linux/Windows build (ms) | 3.354 | 3.006 |
| generation (ms) | 0.056 | 0.049 |
| reductions (ms) | 1.000 | 0.860 |
| total (ms) | 1.106 | 0.963 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionTen.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `([(0, 0)], 10, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 14.53 | 14.53 | 14.66 |
| Source core / debug runner (on macOS) | 15.61 | 15.61 | 15.77 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionTen --iterations 100 --seed 1337 --report-path ../failures
```
