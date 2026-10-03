# Nested Flatmap (product), depth 5

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 69.8 | 43.5 |
| Original input length | 15.2 | 15.0 |
| Wall time (ms) | 6.040 | 5.813 |
| generation (ms) | 0.008 | 0.007 |
| reductions (ms) | 5.980 | 5.760 |
| total (ms) | 6.030 | 5.805 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthFiveProductBind --iterations 100 --seed 1337 --report-path ../failures
```
