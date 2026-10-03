# Nested Flatmap (sum), depth 4

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourSumBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 734.4 | 530.5 |
| Original input length | 344.8 | 339.5 |
| Wall time (ms) | 37.062 | 36.665 |
| generation (ms) | 0.049 | 0.050 |
| reductions (ms) | 36.880 | 36.490 |
| total (ms) | 37.043 | 36.646 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthFourSumBind --iterations 100 --seed 1337 --report-path ../failures
```
