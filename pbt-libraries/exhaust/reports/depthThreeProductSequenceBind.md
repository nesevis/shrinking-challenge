# Nested Flatmap (product sequence), depth 3

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductSequenceBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 274.0 | 276.5 |
| Original input length | 386.3 | 252.5 |
| Wall time (ms) | 6.454 | 5.761 |
| generation (ms) | 0.041 | 0.030 |
| reductions (ms) | 6.330 | 5.640 |
| total (ms) | 6.446 | 5.753 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 67% | 🎯 `(4, 3, 2, 0x23 + 1x1)` |
| 22% | `(6, 2, 2, 0x23 + 1x1)` |
| 5% | `(8, 3, 1, 0x23 + 1x1)` |
| 3% | `(9, 3, 1, 0x26 + 1x1)` |
| 3% | `(7, 2, 2, 0x27 + 1x1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthThreeProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
