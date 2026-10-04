# Hash Collision (M = 100) (state machine)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineHundred.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 746.9 | 714.5 |
| Original input length | 421.7 | 436.5 |
| Wall time (ms) | 5.607 | 5.187 |
| Wall time, Linux/Windows build (ms) | 15.696 | 15.163 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 5.360 | 4.920 |
| total (ms) | 5.594 | 5.176 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineHundred.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (3 distinct)

| Share | Counterexample |
|---|---|
| 80% | 🎯 `[put(0, 0), put(100, 1)]` |
| 14% | `[put(0, 0), put(300, 1)]` |
| 6% | `[put(0, 0), put(700, 1)]` |

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineHundred --iterations 100 --seed 1337 --report-path ../failures
```
