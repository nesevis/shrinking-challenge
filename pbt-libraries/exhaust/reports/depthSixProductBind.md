# Nested Flatmap (product), depth 6

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthSixProductBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 30.5 | 31.0 |
| Original input length | 18.2 | 18.0 |
| Wall time (ms) | 13.816 | 14.181 |
| generation (ms) | 0.010 | 0.009 |
| reductions (ms) | 13.740 | 14.100 |
| total (ms) | 13.803 | 14.169 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2, 1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthSixProductBind --iterations 100 --seed 1337 --report-path ../failures
```
