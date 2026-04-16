# Length List Report for Exhaust

These results are from Exhaust v0.3.15, April 20th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[900]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/lengthListFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 12.0 | 26.0 | 21.0 | 20.8 | 20.6–20.9 |
| Reduction time (ms) | 0.08 | 3.73 | 0.72 | 0.77 | 0.74–0.79 |
| Iterations to failure | 1.0 | 5.0 | 1.0 | 1.1 | 1.1–1.1 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge lengthList --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
