# Weighted Linear Preservation Report for Exhaust

These results are from Exhaust v1.5.1, September 30th, 2026.

## Normalization

Exhaust produced 11 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 22% | `(0, 0, 20)` |
| 16% | `(2, 0, 16)` |
| 14% | `(1, 0, 18)` |
| 12% | `(3, 0, 14)` |
| 12% | `(6, 0, 8)` |
| 10% | `(5, 0, 10)` |
| 6% | `(4, 0, 12)` |
| 5% | `(7, 0, 6)` |
| 1% | `(8, 0, 4)` |
| 1% | `(9, 0, 2)` |
| 1% | `(10, 0, 0)` |

The lexicographic minimum is `(0, 0, 20)`. 22 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/weightedLinearPreservation.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 19.0 | 51.0 | 43.0 | 42.0 | 40.4–43.6 |
| Reduction time (ms) | 0.04 | 0.61 | 0.1 | 0.1 | 0.09–0.12 |
| Iterations to failure | 1.0 | 401.0 | 49.5 | 77.9 | 62.9–92.9 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge weightedLinearPreservation --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
