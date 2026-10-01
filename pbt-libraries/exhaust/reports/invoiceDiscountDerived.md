# Invoice Discount (Derived Generator) Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

This variant generates `Invoice` with `@Exhaustable`'s derived generator, `Invoice.gen()`, which draws the three fields independently from the full `Int` range. The derived generator cannot express the field ranges or the discount eligibility rule, so the property discards any invoice outside them by throwing `PropertySkip()`. Evaluations include the discarded reduction probes.

## Normalization

Exhaust produced 16 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 14% | `Invoice(25, 40, 1)` |
| 14% | `Invoice(15, 67, 1)` |
| 12% | `Invoice(14, 72, 1)` |
| 10% | `Invoice(28, 36, 1)` |
| 8% | `Invoice(13, 77, 1)` |
| 6% | `Invoice(16, 63, 1)` |
| 6% | `Invoice(12, 84, 1)` |
| 6% | `Invoice(19, 53, 1)` |
| 5% | `Invoice(11, 91, 1)` |
| 4% | `Invoice(22, 46, 1)` |
| 4% | `Invoice(17, 59, 1)` |
| 3% | `Invoice(21, 48, 1)` |
| 3% | `Invoice(18, 56, 1)` |
| 2% | `Invoice(24, 42, 1)` |
| 2% | `Invoice(20, 50, 1)` |
| 1% | `Invoice(23, 44, 1)` |

The minimal counterexample under shortlex on `(unit_price_cents, quantity, discount_percent)` is `Invoice(10, 100, 1)`. No run reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/invoiceDiscountDerived.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 75.0 | 245.0 | 121.5 | 119.4 | 110.9–127.9 |
| Reduction time (ms) | 0.15 | 0.44 | 0.22 | 0.23 | 0.21–0.24 |
| Wall time (ms) | 0.218 | 2.185 | 0.529 | 0.634 | 0.562–0.705 |
| Iterations to failure | 9.0 | 3310.0 | 510.0 | 708.4 | 572.9–843.9 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge invoiceDiscountDerived --iterations 100`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
