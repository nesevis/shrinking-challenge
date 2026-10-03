# Nested Flatmap (product), depth 2

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 29.4 | 32.0 |
| Original input length | 6.2 | 6.0 |
| Wall time (ms) | 0.206 | 0.216 |
| generation (ms) | 0.004 | 0.004 |
| reductions (ms) | 0.180 | 0.190 |
| total (ms) | 0.200 | 0.211 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(5, 5)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthTwoProductBind --iterations 100 --seed 1337 --report-path ../failures
```
