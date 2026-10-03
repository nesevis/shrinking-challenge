# Distinct Sum

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/distinctSum.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 130.0 | 130.0 |
| Original input length | 36.0 | 36.0 |
| Wall time (ms) | 0.537 | 0.537 |
| reductions (ms) | 0.490 | 0.490 |
| total (ms) | 0.526 | 0.526 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `[-2, -1, 0, 1, 53]` |

## Running

```sh
swift run -c release ExhaustRunner --challenge distinctSum --iterations 100 --seed 1337 --report-path ../failures
```
