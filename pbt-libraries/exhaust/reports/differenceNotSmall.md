# Difference: Not Small Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[10, 6]` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 43.0 | 204.0 | 94.0 | 93.1 | 90.8–95.4 |
| Reduction time (ms) | 0.1 | 0.44 | 0.24 | 0.24 | 0.23–0.24 |
| Iterations to failure | 6.0 | 2811.0 | 307.0 | 399.5 | 374.3–424.7 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge differenceNotSmall --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
