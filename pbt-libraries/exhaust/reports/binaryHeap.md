# Binary Heap Report for Exhaust

These results are from Exhaust v0.3.9, April 16th, 2026.

## Normalization

Exhaust produced 3 distinct counterexamples across 1000 test runs:

| Prevalence | Counterexample |
|---|---|
| 54.3% | `(0, (0, (1, None, None), (0, None, None)), None)` |
| 32.0% | `(0, (0, (0, None, None), None), (1, None, None))` |
| 13.7% | `(0, None, (0, (1, None, None), (0, None, None)))` |

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 380.0 | 627.0 | 495.0 | 492.4 | 490–494.7 |
| Reduction time (ms) | 17.94 | 61.38 | 35.39 | 34.83 | 34.39–35.27 |
| Iterations to failure | 1.0 | 9.0 | 1.0 | 1.7 | 1.7–1.8 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run ExhaustRunner --challenge binaryHeap --iterations 1000`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.
