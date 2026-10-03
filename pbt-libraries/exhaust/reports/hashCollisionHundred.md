# Hash Collision (M = 100)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionHundred.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 106.8 | 104.5 |
| Original input length | 61.8 | 53.5 |
| Wall time (ms) | 0.561 | 0.534 |
| generation (ms) | 0.091 | 0.084 |
| reductions (ms) | 0.430 | 0.430 |
| total (ms) | 0.555 | 0.529 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 54% | 🎯 `([(0, 0)], 100, 1)` |
| 20% | `([(0, 0)], 300, 1)` |
| 16% | `([(0, 0)], 500, 1)` |
| 7% | `([(0, 0)], 700, 1)` |
| 3% | `([(0, 0)], 900, 1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge hashCollisionHundred --iterations 100 --seed 1337 --report-path ../failures
```
