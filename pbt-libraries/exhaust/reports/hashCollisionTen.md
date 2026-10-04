# Hash Collision (M = 10)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionTen.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 198.6 | 166.5 |
| Original input length | 29.9 | 27.0 |
| Wall time (ms) | 1.004 | 0.887 |
| Wall time, Linux/Windows build (ms) | 3.050 | 2.719 |
| generation (ms) | 0.051 | 0.045 |
| reductions (ms) | 0.900 | 0.780 |
| total (ms) | 0.995 | 0.878 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionTen.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `([(0, 0)], 10, 1)` |

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionTen --iterations 100 --seed 1337 --report-path ../failures
```
