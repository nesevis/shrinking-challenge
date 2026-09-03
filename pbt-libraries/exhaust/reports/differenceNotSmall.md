# Difference: Not Small Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[10, 6]` |

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/differenceNotSmall.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 35.0 | 193.0 | 89.0 | 85.6 | 83.2–88.0 |
| Reduction time (ms) | 0.05 | 0.25 | 0.13 | 0.12 | 0.12–0.13 |
| Iterations to failure | 6.0 | 2811.0 | 307.0 | 399.5 | 374.3–424.7 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge differenceNotSmall --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
