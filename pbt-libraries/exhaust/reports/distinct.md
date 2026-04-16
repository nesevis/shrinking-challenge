# Distinct Report for Exhaust

These results are from Exhaust v0.3.15, April 20th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[-1, 0, 1]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/distinctFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 8.0 | 31.0 | 15.0 | 15.2 | 14.9–15.4 |
| Reduction time (ms) | 0.08 | 0.24 | 0.14 | 0.14 | 0.14–0.14 |
| Iterations to failure | 1.0 | 6.0 | 3.0 | 2.5 | 2.5–2.6 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge distinct --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
