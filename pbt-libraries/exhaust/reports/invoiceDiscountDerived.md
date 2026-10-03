# Invoice Discount (derived)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscountDerived.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 119.4 | 121.5 |
| Original input length | 19.0 | 19.0 |
| Wall time (ms) | 0.653 | 0.551 |
| generation (ms) | 0.367 | 0.263 |
| reductions (ms) | 0.240 | 0.230 |
| total (ms) | 0.647 | 0.545 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (16 distinct)

| Share | Counterexample |
|---|---|
| 14% | `Invoice(15, 67, 1)` |
| 14% | `Invoice(25, 40, 1)` |
| 12% | `Invoice(14, 72, 1)` |
| 10% | `Invoice(28, 36, 1)` |
| 8% | `Invoice(13, 77, 1)` |
| 6% | `Invoice(12, 84, 1)` |
| 6% | `Invoice(19, 53, 1)` |
| 6% | `Invoice(16, 63, 1)` |
| 5% | `Invoice(11, 91, 1)` |
| 4% | `Invoice(22, 46, 1)` |
| 4% | `Invoice(17, 59, 1)` |
| 3% | `Invoice(18, 56, 1)` |
| 3% | `Invoice(21, 48, 1)` |
| 2% | `Invoice(24, 42, 1)` |
| 2% | `Invoice(20, 50, 1)` |
| 1% | `Invoice(23, 44, 1)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge invoiceDiscountDerived --iterations 100 --seed 1337 --report-path ../failures
```
