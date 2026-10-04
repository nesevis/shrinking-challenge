# Hash Collision (M = 1000)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionThousand.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 651.7 | 650.5 |
| Original input length | 117.5 | 119.5 |
| Wall time (ms) | 5.679 | 4.786 |
| Wall time, Linux/Windows build (ms) | 12.193 | 11.012 |
| generation (ms) | 2.944 | 2.099 |
| reductions (ms) | 2.680 | 2.680 |
| total (ms) | 5.670 | 4.777 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionThousand.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 71% | 🎯 `([(0, 0)], 1000, 1)` |
| 14% | `([(0, 0)], 3000, 1)` |
| 9% | `([(0, 0)], 5000, 1)` |
| 4% | `([(0, 0)], 7000, 1)` |
| 2% | `([(0, 0)], 9000, 1)` |

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionThousand --iterations 100 --seed 1337 --report-path ../failures
```
