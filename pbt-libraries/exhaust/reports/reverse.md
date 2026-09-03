# Reverse Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[0, 1]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/reverseFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 3.0 | 14.0 | 8.0 | 7.8 | 7.7–7.9 |
| Reduction time (ms) | 0.02 | 0.13 | 0.07 | 0.07 | 0.07–0.07 |
| Iterations to failure | 1.0 | 3.0 | 1.0 | 1.3 | 1.3–1.4 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge reverse --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
