# Nested Flatmap (product sequence), depth 4

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductSequenceBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 297.5 | 213.0 |
| Original input length | 1107.9 | 374.5 |
| Wall time (ms) | 63.352 | 35.358 |
| generation (ms) | 0.107 | 0.042 |
| reductions (ms) | 63.120 | 35.180 |
| total (ms) | 63.336 | 35.344 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (7 distinct)

| Share | Counterexample |
|---|---|
| 83% | 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
| 9% | `(3, 3, 3, 1, 0x26 + 1x1)` |
| 3% | `(9, 3, 1, 1, 0x26 + 1x1)` |
| 2% | `(9, 4, 1, 1, 0x35 + 1x1)` |
| 1% | `(7, 2, 2, 1, 0x27 + 1x1)` |
| 1% | `(8, 2, 2, 1, 0x31 + 1x1)` |
| 1% | `(10, 3, 1, 1, 0x29 + 1x1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthFourProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
