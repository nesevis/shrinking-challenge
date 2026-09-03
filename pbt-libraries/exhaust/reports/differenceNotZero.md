# Difference: Not Zero Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[10, 10]` |

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/differenceNotZero.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 36.0 | 184.0 | 85.0 | 91.2 | 89.5–93.0 |
| Reduction time (ms) | 0.05 | 0.21 | 0.12 | 0.12 | 0.12–0.12 |
| Iterations to failure | 6.0 | 20506.0 | 2407.5 | 3380.4 | 3173.8–3587.1 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge differenceNotZero --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
