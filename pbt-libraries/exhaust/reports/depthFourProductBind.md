# Nested Flatmap (product), depth 4

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 72.4 | 81.5 |
| Original input length | 12.2 | 12.0 |
| Wall time (ms) | 2.231 | 2.386 |
| generation (ms) | 0.006 | 0.006 |
| reductions (ms) | 2.190 | 2.340 |
| total (ms) | 2.224 | 2.379 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 2, 2, 2)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthFourProductBind --iterations 100 --seed 1337 --report-path ../failures
```
