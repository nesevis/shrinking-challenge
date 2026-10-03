# Leap Day

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/leapDay.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 34.0 | 34.0 |
| Original input length | 25.0 | 25.0 |
| Wall time (ms) | 0.807 | 0.807 |
| reductions (ms) | 0.220 | 0.220 |
| total (ms) | 0.796 | 0.796 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `2088-02-29 00:00:00 +0000` |

## Running

```sh
swift run -c release ExhaustRunner --challenge leapDay --iterations 100 --seed 1337 --report-path ../failures
```
