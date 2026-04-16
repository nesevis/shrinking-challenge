# Coupling Report for Exhaust

These results are from Exhaust v0.3.15, April 20th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[1, 0]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/couplingFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 6.0 | 88.0 | 13.0 | 16.6 | 15.8–17.4 |
| Reduction time (ms) | 0.08 | 2.74 | 0.23 | 0.28 | 0.27–0.29 |
| Iterations to failure | 1.0 | 27.0 | 3.0 | 3.7 | 3.5–3.9 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge coupling --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
