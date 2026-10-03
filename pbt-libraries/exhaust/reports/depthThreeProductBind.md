# Nested Flatmap (product), depth 3

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 58.1 | 63.0 |
| Original input length | 9.2 | 9.0 |
| Wall time (ms) | 0.814 | 0.963 |
| generation (ms) | 0.005 | 0.004 |
| reductions (ms) | 0.780 | 0.930 |
| total (ms) | 0.808 | 0.957 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 3, 3)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthThreeProductBind --iterations 100 --seed 1337 --report-path ../failures
```
