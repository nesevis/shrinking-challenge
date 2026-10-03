# Nested Flatmap (product sequence), depth 2

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductSequenceBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 310.8 | 327.5 |
| Original input length | 141.0 | 122.0 |
| Wall time (ms) | 2.997 | 3.110 |
| generation (ms) | 0.019 | 0.018 |
| reductions (ms) | 2.900 | 3.020 |
| total (ms) | 2.991 | 3.104 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 99% | 🎯 `(6, 4, 0x23 + 1x1)` |
| 1% | `(9, 3, 0x26 + 1x1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthTwoProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
