# Hash Collision (M = 10) (state machine)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineTen.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 221.5 | 177.0 |
| Original input length | 355.0 | 369.0 |
| Wall time (ms) | 1.920 | 1.794 |
| Wall time, Linux/Windows build (ms) | 6.977 | 6.805 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 1.830 | 1.690 |
| total (ms) | 1.907 | 1.781 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineTen.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `[put(0, 0), put(10, 1)]` |

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineTen --iterations 100 --seed 1337 --report-path ../failures
```
