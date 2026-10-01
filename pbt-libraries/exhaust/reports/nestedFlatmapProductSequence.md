# Nested Flatmap (Product Sequence) Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

Each depth is a separate challenge. Counterexamples are written as `(factors…, payload)`, with the payload shown as `[0] * n + [1]`.

## Depth 2

### Normalization

Exhaust produced 2 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 99% | 24 | `(6, 4, [0] * 23 + [1])` |
| 1% | 27 | `(9, 3, [0] * 26 + [1])` |

The minimal counterexample is `(6, 4, [0] * 23 + [1])`. 99 of 100 runs reached it, and 99 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthTwoProductSequenceBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 56.0 | 362.0 | 327.5 | 310.8 | 300.7–321.0 |
| Reduction time (ms) | 0.7 | 4.46 | 3.15 | 3.07 | 2.95–3.19 |
| Iterations to failure | 1.0 | 10.0 | 2.0 | 2.5 | 2.1–2.9 |

`swift run -c release ExhaustRunner --challenge depthTwoProductSequenceBind --iterations 100`

## Depth 3

### Normalization

Exhaust produced 5 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 67% | 24 | `(4, 3, 2, [0] * 23 + [1])` |
| 22% | 24 | `(6, 2, 2, [0] * 23 + [1])` |
| 5% | 24 | `(8, 3, 1, [0] * 23 + [1])` |
| 3% | 28 | `(7, 2, 2, [0] * 27 + [1])` |
| 3% | 27 | `(9, 3, 1, [0] * 26 + [1])` |

The minimal counterexample is `(4, 3, 2, [0] * 23 + [1])`. 67 of 100 runs reached it, and 94 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthThreeProductSequenceBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 31.0 | 573.0 | 276.5 | 274.0 | 253.4–294.6 |
| Reduction time (ms) | 1.22 | 25.75 | 5.6 | 6.31 | 5.49–7.12 |
| Iterations to failure | 1.0 | 7.0 | 1.0 | 1.8 | 1.6–2.1 |

`swift run -c release ExhaustRunner --challenge depthThreeProductSequenceBind --iterations 100`

## Depth 4

### Normalization

Exhaust produced 7 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 83% | 24 | `(3, 2, 2, 2, [0] * 23 + [1])` |
| 9% | 27 | `(3, 3, 3, 1, [0] * 26 + [1])` |
| 3% | 27 | `(9, 3, 1, 1, [0] * 26 + [1])` |
| 2% | 36 | `(9, 4, 1, 1, [0] * 35 + [1])` |
| 1% | 30 | `(10, 3, 1, 1, [0] * 29 + [1])` |
| 1% | 32 | `(8, 2, 2, 1, [0] * 31 + [1])` |
| 1% | 28 | `(7, 2, 2, 1, [0] * 27 + [1])` |

The minimal counterexample is `(3, 2, 2, 2, [0] * 23 + [1])`. 83 of 100 runs reached it, and 83 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFourProductSequenceBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 27.0 | 2667.0 | 213.0 | 297.5 | 221.3–373.7 |
| Reduction time (ms) | 6.62 | 1053.05 | 35.23 | 63.11 | 36.65–89.57 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthFourProductSequenceBind --iterations 100`

## Depth 5

### Normalization

Exhaust produced 24 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 71% | 24 | `(3, 2, 2, 2, 1, [0] * 23 + [1])` |
| 2% | 72 | `(9, 2, 2, 2, 1, [0] * 71 + [1])` |
| 2% | 30 | `(6, 5, 1, 1, 1, [0] * 29 + [1])` |
| 2% | 30 | `(10, 3, 1, 1, 1, [0] * 29 + [1])` |
| 2% | 27 | `(9, 3, 1, 1, 1, [0] * 26 + [1])` |
| 2% | 54 | `(6, 3, 3, 1, 1, [0] * 53 + [1])` |
| 2% | 36 | `(9, 4, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 56 | `(7, 2, 2, 2, 1, [0] * 55 + [1])` |
| 1% | 84 | `(7, 3, 2, 2, 1, [0] * 83 + [1])` |
| 1% | 56 | `(8, 7, 1, 1, 1, [0] * 55 + [1])` |
| 1% | 32 | `(8, 2, 2, 1, 1, [0] * 31 + [1])` |
| 1% | 42 | `(7, 6, 1, 1, 1, [0] * 41 + [1])` |
| 1% | 120 | `(10, 4, 3, 1, 1, [0] * 119 + [1])` |
| 1% | 25 | `(5, 5, 1, 1, 1, [0] * 24 + [1])` |
| 1% | 64 | `(8, 4, 2, 1, 1, [0] * 63 + [1])` |
| 1% | 126 | `(9, 7, 2, 1, 1, [0] * 125 + [1])` |
| 1% | 72 | `(9, 8, 1, 1, 1, [0] * 71 + [1])` |
| 1% | 90 | `(9, 5, 2, 1, 1, [0] * 89 + [1])` |
| 1% | 40 | `(10, 2, 2, 1, 1, [0] * 39 + [1])` |
| 1% | 42 | `(7, 3, 2, 1, 1, [0] * 41 + [1])` |
| 1% | 28 | `(7, 2, 2, 1, 1, [0] * 27 + [1])` |
| 1% | 60 | `(10, 6, 1, 1, 1, [0] * 59 + [1])` |
| 1% | 36 | `(6, 6, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 48 | `(6, 4, 2, 1, 1, [0] * 47 + [1])` |

The minimal counterexample is `(3, 2, 2, 2, 1, [0] * 23 + [1])`. 71 of 100 runs reached it, and 71 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFiveProductSequenceBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 27.0 | 15598.0 | 153.5 | 691.8 | 264.5–1119.1 |
| Reduction time (ms) | 121.11 | 35412.69 | 186.03 | 967.47 | 126.29–1808.65 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthFiveProductSequenceBind --iterations 100`

## Depth 6

### Normalization

Exhaust produced 43 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 47% | 32 | `(2, 2, 2, 2, 2, 1, [0] * 31 + [1])` |
| 3% | 125 | `(5, 5, 5, 1, 1, 1, [0] * 124 + [1])` |
| 2% | 27 | `(9, 3, 1, 1, 1, 1, [0] * 26 + [1])` |
| 2% | 120 | `(10, 3, 2, 2, 1, 1, [0] * 119 + [1])` |
| 2% | 72 | `(6, 6, 2, 1, 1, 1, [0] * 71 + [1])` |
| 2% | 144 | `(9, 2, 2, 2, 2, 1, [0] * 143 + [1])` |
| 2% | 54 | `(6, 3, 3, 1, 1, 1, [0] * 53 + [1])` |
| 2% | 72 | `(9, 2, 2, 2, 1, 1, [0] * 71 + [1])` |
| 2% | 36 | `(9, 4, 1, 1, 1, 1, [0] * 35 + [1])` |
| 2% | 30 | `(10, 3, 1, 1, 1, 1, [0] * 29 + [1])` |
| 2% | 30 | `(6, 5, 1, 1, 1, 1, [0] * 29 + [1])` |
| 1% | 120 | `(10, 4, 3, 1, 1, 1, [0] * 119 + [1])` |
| 1% | 36 | `(4, 3, 3, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 36 | `(6, 6, 1, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 128 | `(8, 2, 2, 2, 2, 1, [0] * 127 + [1])` |
| 1% | 540 | `(10, 9, 3, 2, 1, 1, [0] * 539 + [1])` |
| 1% | 32 | `(8, 2, 2, 1, 1, 1, [0] * 31 + [1])` |
| 1% | 56 | `(8, 7, 1, 1, 1, 1, [0] * 55 + [1])` |
| 1% | 224 | `(8, 7, 2, 2, 1, 1, [0] * 223 + [1])` |
| 1% | 42 | `(7, 3, 2, 1, 1, 1, [0] * 41 + [1])` |
| 1% | 45 | `(5, 3, 3, 1, 1, 1, [0] * 44 + [1])` |
| 1% | 160 | `(8, 5, 4, 1, 1, 1, [0] * 159 + [1])` |
| 1% | 84 | `(7, 3, 2, 2, 1, 1, [0] * 83 + [1])` |
| 1% | 120 | `(6, 5, 4, 1, 1, 1, [0] * 119 + [1])` |
| 1% | 192 | `(8, 6, 4, 1, 1, 1, [0] * 191 + [1])` |
| 1% | 90 | `(9, 5, 2, 1, 1, 1, [0] * 89 + [1])` |
| 1% | 64 | `(8, 4, 2, 1, 1, 1, [0] * 63 + [1])` |
| 1% | 126 | `(9, 7, 2, 1, 1, 1, [0] * 125 + [1])` |
| 1% | 160 | `(10, 8, 2, 1, 1, 1, [0] * 159 + [1])` |
| 1% | 72 | `(9, 8, 1, 1, 1, 1, [0] * 71 + [1])` |
| 1% | 40 | `(10, 2, 2, 1, 1, 1, [0] * 39 + [1])` |
| 1% | 96 | `(6, 2, 2, 2, 2, 1, [0] * 95 + [1])` |
| 1% | 56 | `(7, 2, 2, 2, 1, 1, [0] * 55 + [1])` |
| 1% | 32 | `(4, 4, 2, 1, 1, 1, [0] * 31 + [1])` |
| 1% | 28 | `(7, 2, 2, 1, 1, 1, [0] * 27 + [1])` |
| 1% | 112 | `(7, 4, 4, 1, 1, 1, [0] * 111 + [1])` |
| 1% | 42 | `(7, 6, 1, 1, 1, 1, [0] * 41 + [1])` |
| 1% | 60 | `(10, 6, 1, 1, 1, 1, [0] * 59 + [1])` |
| 1% | 48 | `(6, 4, 2, 1, 1, 1, [0] * 47 + [1])` |
| 1% | 25 | `(5, 5, 1, 1, 1, 1, [0] * 24 + [1])` |
| 1% | 140 | `(10, 7, 2, 1, 1, 1, [0] * 139 + [1])` |
| 1% | 112 | `(7, 2, 2, 2, 2, 1, [0] * 111 + [1])` |
| 1% | 32 | `(4, 2, 2, 2, 1, 1, [0] * 31 + [1])` |

The minimal counterexample is `(3, 2, 2, 2, 1, 1, [0] * 23 + [1])`. 0 of 100 runs reached it, and 0 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthSixProductSequenceBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 27.0 | 22309.0 | 110.5 | 1039.6 | 439.0–1640.1 |
| Reduction time (ms) | 212.65 | 74990.93 | 971.88 | 2649.53 | 1005.36–4293.71 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthSixProductSequenceBind --iterations 100`

## Reproduction

From the `exhaust/src` folder, run the command listed under each depth.

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
