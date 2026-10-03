# Username and Password

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/usernamePassword.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 731.0 | 731.0 |
| Original input length | 30.0 | 30.0 |
| Wall time (ms) | 2.871 | 2.871 |
| reductions (ms) | 2.810 | 2.810 |
| total (ms) | 2.858 | 2.858 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `("u: 0000", "p: 0000")` |

## Running

```sh
swift run -c release ExhaustRunner --challenge usernamePassword --iterations 100 --seed 1337 --report-path ../failures
```
