# Coupling Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[1, 0]` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 6.0 | 25.0 | 7.0 | 7.9 | 7.7–8.1 |
| Reduction time (ms) | 0.07 | 0.42 | 0.1 | 0.1 | 0.1–0.11 |
| Iterations to failure | 1.0 | 47.0 | 4.0 | 5.9 | 5.6–6.3 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge coupling --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
