# Hash Collision (M = 100)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionHundred.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 692.3 | 616.0 |
| Original input length | 61.8 | 53.5 |
| Wall time (ms) | 3.028 | 2.741 |
| Wall time, Linux/Windows build (ms) | 8.554 | 7.733 |
| generation (ms) | 0.222 | 0.182 |
| reductions (ms) | 2.750 | 2.480 |
| total (ms) | 3.018 | 2.732 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionHundred.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 70% | 🎯 `([(0, 0)], 100, 1)` |
| 20% | `([(0, 0)], 300, 1)` |
| 7% | `([(0, 0)], 700, 1)` |
| 3% | `([(0, 0)], 900, 1)` |

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionHundred --iterations 100 --seed 1337 --report-path ../failures
```
