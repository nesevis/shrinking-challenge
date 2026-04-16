# Large Union List Report for Exhaust

These results are from Exhaust v0.3.15, April 20th, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[[-2, -1, 0, 1, 2]]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/largeUnionListFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 71.0 | 178.0 | 127.0 | 121.9 | 120.3–123.6 |
| Reduction time (ms) | 0.6 | 2.7 | 0.97 | 0.96 | 0.95–0.97 |
| Iterations to failure | 3.0 | 9.0 | 4.0 | 4.6 | 4.5–4.7 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge largeUnionList --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
