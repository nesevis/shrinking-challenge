# Anagrams

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/anagrams.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1239.0 | 1239.0 |
| Original input length | 62.0 | 62.0 |
| Wall time (ms) | 8.063 | 8.063 |
| reductions (ms) | 7.890 | 7.890 |
| total (ms) | 8.051 | 8.051 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(" \0", "\0 ")` |

## Running

```sh
swift run -c release ExhaustRunner --challenge anagrams --iterations 100 --seed 1337 --report-path ../failures
```
