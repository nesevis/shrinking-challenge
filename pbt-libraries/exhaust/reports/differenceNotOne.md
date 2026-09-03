# Difference: Not One Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[10, 9]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/differenceNotOneFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 37.0 | 198.0 | 93.0 | 97.3 | 95.2–99.4 |
| Reduction time (ms) | 0.05 | 0.27 | 0.13 | 0.14 | 0.13–0.14 |
| Iterations to failure | 6.0 | 12808.0 | 1007.0 | 1642.1 | 1533.6–1750.6 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge differenceNotOne --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
