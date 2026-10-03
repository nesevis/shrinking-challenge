# Zalgo Haystack

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/zalgoHaystack.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 461.0 | 461.0 |
| Original input length | 3237.0 | 3237.0 |
| Wall time (ms) | 13.997 | 13.997 |
| reductions (ms) | 10.730 | 10.730 |
| total (ms) | 13.945 | 13.945 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"THE ICHOR PERMEATES"` |

## Running

```sh
swift run -c release ExhaustRunner --challenge zalgoHaystack --iterations 100 --seed 1337 --report-path ../failures
```
