# Length List Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[900]` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 11.0 | 21.0 | 15.0 | 14.7 | 14.6–14.8 |
| Reduction time (ms) | 0.06 | 0.24 | 0.09 | 0.1 | 0.1–0.1 |
| Iterations to failure | 1.0 | 14.0 | 4.0 | 4.2 | 4–4.3 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge lengthList --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
