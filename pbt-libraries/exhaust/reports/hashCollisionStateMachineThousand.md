# Hash Collision (M = 1000) (state machine)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineThousand.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 726.3 | 701.5 |
| Original input length | 512.5 | 530.0 |
| Wall time (ms) | 11.715 | 10.079 |
| Wall time, Linux/Windows build (ms) | 25.678 | 23.991 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 8.680 | 7.310 |
| total (ms) | 11.674 | 10.040 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineThousand.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 36% | 🎯 `[put(0, 0), put(1000, 1)]` |
| 23% | `[put(0, 0), put(9000, 1)]` |
| 15% | `[put(0, 0), put(3000, 1)]` |
| 14% | `[put(0, 0), put(7000, 1)]` |
| 12% | `[put(0, 0), put(5000, 1)]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.78 | 15.80 | 16.12 |
| Source core / debug runner (on macOS) | 17.11 | 17.12 | 17.55 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineThousand --iterations 100 --seed 1337 --report-path ../failures
```
