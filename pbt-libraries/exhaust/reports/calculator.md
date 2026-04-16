# Calculator Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `div(value(0), add(value(0), value(0)))` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 79.0 | 240.0 | 91.0 | 93.9 | 93–94.7 |
| Reduction time (ms) | 1.12 | 7.71 | 1.53 | 1.6 | 1.56–1.63 |
| Iterations to failure | 1.0 | 219.0 | 20.0 | 28.1 | 26.5–29.8 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge calculator --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
