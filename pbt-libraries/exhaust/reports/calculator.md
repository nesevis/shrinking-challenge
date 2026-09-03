# Calculator Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `div(value(0), add(value(0), value(0)))` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/calculatorFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 6.0 | 52.0 | 13.0 | 13.3 | 13.0–13.6 |
| Reduction time (ms) | 0.11 | 0.92 | 0.22 | 0.23 | 0.23–0.24 |
| Iterations to failure | 1.0 | 219.0 | 20.0 | 28.2 | 26.5–29.9 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge calculator --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
