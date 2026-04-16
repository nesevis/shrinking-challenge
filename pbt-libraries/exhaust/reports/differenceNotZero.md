# Difference: Not Zero Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[10, 10]` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 46.0 | 200.0 | 97.0 | 105.6 | 103.8–107.5 |
| Reduction time (ms) | 0.1 | 0.56 | 0.27 | 0.28 | 0.27–0.28 |
| Iterations to failure | 6.0 | 20506.0 | 2407.5 | 3380.4 | 3173.8–3587.1 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge differenceNotZero --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
