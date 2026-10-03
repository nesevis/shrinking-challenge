# Hash Collision (M = 1000)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionThousand.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 143.1 | 141.5 |
| Original input length | 117.5 | 119.5 |
| Wall time (ms) | 1.479 | 1.230 |
| generation (ms) | 0.854 | 0.614 |
| reductions (ms) | 0.590 | 0.580 |
| total (ms) | 1.473 | 1.224 |

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
swift run -c release ExhaustRunner --challenge hashCollisionThousand --iterations 100 --seed 1337 --report-path ../failures
```
