# Hash Collision (M = 10)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionTen.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 70.2 | 73.0 |
| Original input length | 29.9 | 27.0 |
| Wall time (ms) | 0.365 | 0.368 |
| generation (ms) | 0.030 | 0.028 |
| reductions (ms) | 0.300 | 0.300 |
| total (ms) | 0.359 | 0.363 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (6 distinct)

| Share | Counterexample |
|---|---|
| 64% | 🎯 `([(0, 0)], 10, 1)` |
| 12% | `([(1, 0)], 11, 1)` |
| 11% | `([(0, 0)], 70, 1)` |
| 9% | `([(0, 0)], 90, 1)` |
| 3% | `([(11, 0)], 1, 1)` |
| 1% | `([(1, 0)], 71, 1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge hashCollisionTen --iterations 100 --seed 1337 --report-path ../failures
```
