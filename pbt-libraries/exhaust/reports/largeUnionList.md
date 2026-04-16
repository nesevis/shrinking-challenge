# Large Union List Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[[-2, -1, 0, 1, 2]]` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 54.0 | 157.0 | 110.0 | 104.3 | 102.6–106 |
| Reduction time (ms) | 0.47 | 1.43 | 0.85 | 0.84 | 0.83–0.85 |
| Iterations to failure | 3.0 | 9.0 | 5.0 | 5.0 | 4.9–5.1 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge largeUnionList --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
