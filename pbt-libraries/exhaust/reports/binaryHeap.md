# Binary Heap Report for Exhaust

These results are from Exhaust v0.3.15, April 20th, 2026.

## Normalization

Exhaust produced 3 distinct counterexamples across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 54.7% | `(0, (0, (1, None, None), (0, None, None)), None)` |
| 32.0% | `(0, (0, (0, None, None), None), (1, None, None))` |
| 13.3% | `(0, None, (0, (1, None, None), (0, None, None)))` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/binaryHeapFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 203.0 | 434.0 | 311.0 | 321.6 | 318.7–324.4 |
| Reduction time (ms) | 16.26 | 40.98 | 26.98 | 26.24 | 25.98–26.5 |
| Iterations to failure | 1.0 | 9.0 | 1.0 | 1.7 | 1.7–1.8 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge binaryHeap --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
