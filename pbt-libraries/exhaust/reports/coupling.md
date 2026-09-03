# Coupling Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[1, 0]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/couplingFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 5.0 | 86.0 | 17.0 | 23.2 | 22.1–24.3 |
| Reduction time (ms) | 0.05 | 0.64 | 0.15 | 0.19 | 0.18–0.2 |
| Iterations to failure | 1.0 | 27.0 | 3.0 | 3.7 | 3.5–3.9 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge coupling --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
