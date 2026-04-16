# Difference: Not One Report for Exhaust

These results are from Exhaust v0.3.15, April 20th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[10, 9]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/differenceNotOneFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 47.0 | 215.0 | 102.0 | 107.5 | 105.3–109.7 |
| Reduction time (ms) | 0.11 | 0.49 | 0.27 | 0.28 | 0.27–0.28 |
| Iterations to failure | 6.0 | 12808.0 | 1007.0 | 1642.1 | 1533.6–1750.6 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge differenceNotOne --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
