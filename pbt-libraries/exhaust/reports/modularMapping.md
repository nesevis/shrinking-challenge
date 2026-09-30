# Modular Mapping Report for Exhaust

These results are from Exhaust v1.5.1, September 30th, 2026.

## Normalization

Exhaust produced 18 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 15% | `925` |
| 13% | `921` |
| 10% | `901` |
| 9% | `913` |
| 9% | `917` |
| 8% | `909` |
| 8% | `934` |
| 8% | `905` |
| 5% | `910` |
| 3% | `906` |
| 3% | `932` |
| 2% | `902` |
| 2% | `926` |
| 1% | `931` |
| 1% | `922` |
| 1% | `927` |
| 1% | `918` |
| 1% | `904` |

The numeric-output optimum is `900`. 0 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/modularMapping.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 12.0 | 32.0 | 16.0 | 17.5 | 16.5–18.5 |
| Reduction time (ms) | 0.02 | 0.22 | 0.02 | 0.03 | 0.02–0.03 |
| Iterations to failure | 1.0 | 38.0 | 6.5 | 8.5 | 7.0–10.0 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge modularMapping --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
