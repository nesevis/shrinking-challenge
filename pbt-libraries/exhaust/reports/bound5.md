# Bound5 Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `([], [], [], [-32768], [-1])` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/bound5Failures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 58.0 | 210.0 | 103.0 | 104.9 | 104.0–105.9 |
| Reduction time (ms) | 0.37 | 1.69 | 0.66 | 0.68 | 0.67–0.69 |
| Iterations to failure | 5.0 | 23.0 | 7.0 | 7.5 | 7.3–7.6 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge bound5 --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
