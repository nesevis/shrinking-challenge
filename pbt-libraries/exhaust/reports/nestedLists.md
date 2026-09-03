# Nested Lists Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 1 distinct counterexample across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/nestedListsFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 23.0 | 69.0 | 36.0 | 37.1 | 36.6–37.5 |
| Reduction time (ms) | 0.14 | 0.6 | 0.28 | 0.29 | 0.29–0.3 |
| Iterations to failure | 4.0 | 13.0 | 6.0 | 6.4 | 6.3–6.5 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge nestedLists --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
