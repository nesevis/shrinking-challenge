# Binary Heap Report for Exhaust

These results are from Exhaust v1.1.0, September 3rd, 2026.

## Normalization

Exhaust produced 3 distinct counterexamples across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 64.6% | `(0, None, (0, (0, None, None), (1, None, None)))` |
| 33.7% | `(0, (0, (1, None, None), None), (0, None, None))` |
| 1.7% | `(0, None, (0, None, (0, (0, None, None), (1, None, None))))` |

See [the first 50 failing inputs before shrinking](/pbt-libraries/exhaust/failures/binaryHeapFailures.md).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 57.0 | 219.0 | 105.0 | 127.5 | 124.9–130.2 |
| Reduction time (ms) | 1.4 | 10.25 | 3.34 | 4.16 | 4.05–4.28 |
| Iterations to failure | 1.0 | 13.0 | 1.0 | 1.8 | 1.7–1.8 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge binaryHeap --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
