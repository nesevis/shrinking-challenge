# Weighted Linear Preservation

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/weightedLinearPreservation.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 42.0 | 43.0 |
| Original input length | 9.6 | 10.0 |
| Wall time (ms) | 0.165 | 0.165 |
| generation (ms) | 0.035 | 0.023 |
| reductions (ms) | 0.100 | 0.100 |
| total (ms) | 0.159 | 0.159 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (11 distinct)

| Share | Counterexample |
|---|---|
| 22% | 🎯 `(0, 0, 20)` |
| 16% | `(2, 0, 16)` |
| 14% | `(1, 0, 18)` |
| 12% | `(3, 0, 14)` |
| 12% | `(6, 0, 8)` |
| 10% | `(5, 0, 10)` |
| 6% | `(4, 0, 12)` |
| 5% | `(7, 0, 6)` |
| 1% | `(10, 0, 0)` |
| 1% | `(9, 0, 2)` |
| 1% | `(8, 0, 4)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge weightedLinearPreservation --iterations 100 --seed 1337 --report-path ../failures
```
