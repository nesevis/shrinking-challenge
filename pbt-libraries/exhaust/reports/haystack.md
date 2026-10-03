# Haystack

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/haystack.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 407.0 | 407.0 |
| Original input length | 480.0 | 480.0 |
| Wall time (ms) | 9.527 | 9.527 |
| reductions (ms) | 6.550 | 6.550 |
| total (ms) | 9.506 | 9.506 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"CREEPIDIOT"` |

## Running

```sh
swift run -c release ExhaustRunner --challenge haystack --iterations 100 --seed 1337 --report-path ../failures
```
