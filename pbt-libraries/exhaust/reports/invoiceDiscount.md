# Invoice Discount Report for Exhaust

These results are from Exhaust v1.5.1, September 30th, 2026.

## Normalization

Exhaust produced 28 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 12% | `Invoice(12, 84, 1)` |
| 7% | `Invoice(14, 72, 1)` |
| 7% | `Invoice(23, 44, 1)` |
| 6% | `Invoice(17, 59, 1)` |
| 6% | `Invoice(15, 67, 1)` |
| 5% | `Invoice(16, 63, 1)` |
| 5% | `Invoice(13, 77, 1)` |
| 5% | `Invoice(20, 50, 1)` |
| 4% | `Invoice(25, 40, 1)` |
| 4% | `Invoice(29, 35, 1)` |
| 4% | `Invoice(21, 48, 1)` |
| 3% | `Invoice(19, 53, 1)` |
| 3% | `Invoice(24, 42, 1)` |
| 3% | `Invoice(27, 38, 1)` |
| 3% | `Invoice(11, 91, 1)` |
| 3% | `Invoice(112, 9, 1)` |
| 3% | `Invoice(18, 56, 1)` |
| 3% | `Invoice(26, 39, 1)` |
| 2% | `Invoice(250, 4, 1)` |
| 2% | `Invoice(22, 46, 1)` |
| 2% | `Invoice(31, 33, 1)` |
| 2% | `Invoice(30, 34, 1)` |
| 1% | `Invoice(32, 32, 1)` |
| 1% | `Invoice(10, 100, 1)` |
| 1% | `Invoice(28, 36, 1)` |
| 1% | `Invoice(334, 3, 1)` |
| 1% | `Invoice(167, 6, 1)` |
| 1% | `Invoice(125, 8, 1)` |

The minimum failing invoice under lexicographic order on `(unit_price_cents, quantity, discount_percent)` is `Invoice(10, 100, 1)`. 1 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/invoiceDiscount.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 29.0 | 115.0 | 85.0 | 75.8 | 71.2–80.4 |
| Reduction time (ms) | 0.12 | 0.65 | 0.26 | 0.25 | 0.24–0.27 |
| Iterations to failure | 1.0 | 3.0 | 1.0 | 1.2 | 1.1–1.2 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge invoiceDiscount --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
