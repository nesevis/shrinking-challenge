# Hash Collision (M = 1000) (state machine)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineThousand.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 158.0 | 153.5 |
| Original input length | 512.5 | 530.0 |
| Wall time (ms) | 1.970 | 1.846 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 1.800 | 1.680 |
| total (ms) | 1.957 | 1.833 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (9 distinct)

| Share | Counterexample |
|---|---|
| 30% | `[put(0, 1), put(1000, 0)]` |
| 28% | 🎯 `[put(0, 0), put(1000, 1)]` |
| 10% | `[put(0, 0), put(3000, 1)]` |
| 10% | `[put(0, 1), put(3000, 0)]` |
| 6% | `[put(0, 1), put(5000, 0)]` |
| 6% | `[put(0, 0), put(5000, 1)]` |
| 5% | `[put(0, 1), put(7000, 0)]` |
| 4% | `[put(0, 0), put(7000, 1)]` |
| 1% | `[put(0, 1), put(9000, 0)]` |

## Running

```sh
swift run -c release ExhaustRunner --challenge hashCollisionStateMachineThousand --iterations 100 --seed 1337 --report-path ../failures
```
