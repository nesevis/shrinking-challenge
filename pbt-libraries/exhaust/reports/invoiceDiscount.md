# Invoice Discount Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

## Normalization

Exhaust produced 4 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 84% | `Invoice(12, 84, 1)` |
| 11% | `Invoice(11, 91, 1)` |
| 4% | `Invoice(10, 100, 1)` |
| 1% | `Invoice(23, 44, 1)` |

The minimal counterexample under shortlex on `(unit_price_cents, quantity, discount_percent)` is `Invoice(10, 100, 1)`. 4 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/invoiceDiscount.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 29.0 | 88.0 | 55.0 | 58.4 | 56.5–60.3 |
| Reduction time (ms) | 0.16 | 0.41 | 0.27 | 0.28 | 0.27–0.29 |
| Wall time (ms) | 0.205 | 0.463 | 0.314 | 0.326 | 0.317–0.335 |
| Iterations to failure | 1.0 | 3.0 | 1.0 | 1.2 | 1.1–1.2 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge invoiceDiscount --iterations 100`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
