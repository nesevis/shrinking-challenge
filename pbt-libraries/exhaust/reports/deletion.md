# Deletion Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `([0, 0], 0)` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 0.0 | 21.0 | 4.0 | 4.5 | 4.3–4.7 |
| Reduction time (ms) | 0.03 | 0.44 | 0.16 | 0.17 | 0.16–0.17 |
| Iterations to failure | 1.0 | 60.0 | 15.0 | 16.9 | 16.2–17.6 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge deletion --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
