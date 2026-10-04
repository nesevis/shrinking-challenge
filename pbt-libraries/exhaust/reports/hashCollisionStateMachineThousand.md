# Hash Collision (M = 1000) (state machine)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineThousand.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 729.3 | 705.0 |
| Original input length | 512.5 | 530.0 |
| Wall time (ms) | 10.460 | 8.860 |
| Wall time, Linux/Windows build (ms) | 21.932 | 20.610 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 8.140 | 6.830 |
| total (ms) | 10.445 | 8.847 |

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

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineThousand --iterations 100 --seed 1337 --report-path ../failures
```
