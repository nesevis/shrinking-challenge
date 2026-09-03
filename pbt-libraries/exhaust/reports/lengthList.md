# Length List Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[900]` |

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/lengthList.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 11.0 | 25.0 | 20.0 | 19.8 | 19.7–19.9 |
| Reduction time (ms) | 0.03 | 0.33 | 0.17 | 0.17 | 0.17–0.18 |
| Iterations to failure | 1.0 | 5.0 | 1.0 | 1.1 | 1.1–1.1 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge lengthList --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
