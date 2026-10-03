# Duplicated Text

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/duplicatedText.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 54.0 | 54.0 |
| Original input length | 24.0 | 24.0 |
| Wall time (ms) | 0.383 | 0.383 |
| reductions (ms) | 0.340 | 0.340 |
| total (ms) | 0.374 | 0.374 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `("10210210", "10210210")` |

## Running

```sh
swift run -c release ExhaustRunner --challenge duplicatedText --iterations 100 --seed 1337 --report-path ../failures
```
