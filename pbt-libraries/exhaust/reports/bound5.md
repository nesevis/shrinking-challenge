# Bound5 Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `([], [], [], [-32768], [-1])` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 63.0 | 266.0 | 122.0 | 124.5 | 123.3–125.6 |
| Reduction time (ms) | 0.89 | 3.63 | 1.56 | 1.6 | 1.59–1.62 |
| Iterations to failure | 5.0 | 23.0 | 7.0 | 7.5 | 7.3–7.6 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge bound5 --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
