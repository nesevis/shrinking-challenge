# Branch Switching

Exhaust 1.5.5, release build. One fixed-start reduction.

[Raw results](../failures/branchSwitching.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 16.0 | 16.0 |
| Original input length | 17.0 | 17.0 |
| Wall time (ms) | 0.336 | 0.336 |
| reductions (ms) | 0.240 | 0.240 |
| total (ms) | 0.325 | 0.325 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `"    "` |

## Running

```sh
swift run -c release ExhaustRunner --challenge branchSwitching --iterations 100 --seed 1337 --report-path ../failures
```
