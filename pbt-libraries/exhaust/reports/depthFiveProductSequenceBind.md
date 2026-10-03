# Nested Flatmap (product sequence), depth 5

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductSequenceBind.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 691.8 | 153.5 |
| Original input length | 3737.7 | 398.0 |
| Wall time (ms) | 992.557 | 185.223 |
| generation (ms) | 0.343 | 0.055 |
| reductions (ms) | 992.030 | 184.900 |
| total (ms) | 992.531 | 185.193 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (24 distinct)

| Share | Counterexample |
|---|---|
| 71% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
| 2% | `(9, 3, 1, 1, 1, 0x26 + 1x1)` |
| 2% | `(6, 3, 3, 1, 1, 0x53 + 1x1)` |
| 2% | `(10, 3, 1, 1, 1, 0x29 + 1x1)` |
| 2% | `(9, 4, 1, 1, 1, 0x35 + 1x1)` |
| 2% | `(9, 2, 2, 2, 1, 0x71 + 1x1)` |
| 2% | `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
| 1% | `(10, 6, 1, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(10, 2, 2, 1, 1, 0x39 + 1x1)` |
| 1% | `(9, 8, 1, 1, 1, 0x71 + 1x1)` |
| 1% | `(9, 5, 2, 1, 1, 0x89 + 1x1)` |
| 1% | `(7, 3, 2, 1, 1, 0x41 + 1x1)` |
| 1% | `(10, 4, 3, 1, 1, 0x119 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 0x27 + 1x1)` |
| 1% | `(8, 4, 2, 1, 1, 0x63 + 1x1)` |
| 1% | `(9, 7, 2, 1, 1, 0x125 + 1x1)` |
| 1% | `(8, 2, 2, 1, 1, 0x31 + 1x1)` |
| 1% | `(6, 6, 1, 1, 1, 0x35 + 1x1)` |
| 1% | `(6, 4, 2, 1, 1, 0x47 + 1x1)` |
| 1% | `(7, 6, 1, 1, 1, 0x41 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 0x55 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 0x55 + 1x1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge depthFiveProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
