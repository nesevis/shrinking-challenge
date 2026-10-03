# Hash Collision (M = 100) (state machine)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineHundred.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 109.1 | 107.0 |
| Original input length | 421.7 | 436.5 |
| Wall time (ms) | 1.246 | 1.233 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 1.170 | 1.140 |
| total (ms) | 1.234 | 1.221 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (8 distinct)

| Share | Counterexample |
|---|---|
| 33% | 🎯 `[put(0, 0), put(100, 1)]` |
| 20% | `[put(0, 1), put(100, 0)]` |
| 13% | `[put(0, 0), put(300, 1)]` |
| 10% | `[put(0, 0), put(500, 1)]` |
| 10% | `[put(0, 1), put(300, 0)]` |
| 6% | `[put(0, 1), put(500, 0)]` |
| 5% | `[put(0, 0), put(700, 1)]` |
| 3% | `[put(0, 1), put(700, 0)]` |

## Running

```sh
swift run -c release ExhaustRunner --challenge hashCollisionStateMachineHundred --iterations 100 --seed 1337 --report-path ../failures
```
