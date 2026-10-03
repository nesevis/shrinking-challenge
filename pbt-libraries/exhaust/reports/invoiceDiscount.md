# Invoice Discount

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscount.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 58.4 | 55.0 |
| Original input length | 19.7 | 20.0 |
| Wall time (ms) | 0.346 | 0.336 |
| generation (ms) | 0.005 | 0.004 |
| reductions (ms) | 0.300 | 0.290 |
| total (ms) | 0.341 | 0.331 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 84% | `Invoice(12, 84, 1)` |
| 11% | `Invoice(11, 91, 1)` |
| 4% | 🎯 `Invoice(10, 100, 1)` |
| 1% | `Invoice(23, 44, 1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge invoiceDiscount --iterations 100 --seed 1337 --report-path ../failures
```
