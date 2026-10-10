# Hash Collision (M = 10) (state machine)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineTen.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 219.8 | 176.0 |
| Original input length | 355.0 | 369.0 |
| Wall time (ms) | 1.972 | 1.785 |
| Wall time, Linux/Windows build (ms) | 8.593 | 8.244 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 1.880 | 1.690 |
| total (ms) | 1.947 | 1.762 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineTen.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `[put(0, 0), put(10, 1)]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.50 | 15.51 | 15.97 |
| Source core / debug runner (on macOS) | 16.87 | 16.89 | 17.38 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineTen --iterations 100 --seed 1337 --report-path ../failures
```
