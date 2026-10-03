# Hash Collision (M = 10) (state machine)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineTen.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 76.7 | 79.0 |
| Original input length | 355.0 | 369.0 |
| Wall time (ms) | 0.906 | 0.886 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 0.840 | 0.830 |
| total (ms) | 0.895 | 0.876 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (6 distinct)

| Share | Counterexample |
|---|---|
| 60% | 🎯 `[put(0, 0), put(10, 1)]` |
| 18% | `[put(0, 1), put(10, 0)]` |
| 10% | `[put(0, 0), put(70, 1)]` |
| 7% | `[put(0, 0), put(90, 1)]` |
| 3% | `[put(0, 1), put(90, 0)]` |
| 2% | `[put(0, 1), put(70, 0)]` |

## Running

```sh
swift run -c release ExhaustRunner --challenge hashCollisionStateMachineTen --iterations 100 --seed 1337 --report-path ../failures
```
