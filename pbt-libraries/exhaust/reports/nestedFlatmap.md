# Nested Flatmap Report for Exhaust

These results are from Exhaust v1.5.1, September 30th, 2026.

Each depth is a separate challenge. Counterexamples are written as `(factors…, payload)`, with the payload shown as `[0] * n + [1]`.

## Depth 2

### Normalization

Exhaust produced 2 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 99% | 24 | `(6, 4, [0] * 23 + [1])` |
| 1% | 27 | `(9, 3, [0] * 26 + [1])` |

The known semantic optimum is `(6, 4, [0] * 23 + [1])`. 99 of 100 runs reached it, and 99 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthTwoBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 55.0 | 361.0 | 326.5 | 309.8 | 299.6–320.0 |
| Reduction time (ms) | 0.62 | 4.4 | 2.77 | 2.72 | 2.61–2.83 |
| Iterations to failure | 1.0 | 10.0 | 2.0 | 2.5 | 2.1–2.9 |

`swift run -c release ExhaustRunner --challenge depthTwoBind --iterations 100`

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

The known semantic optimum is `(4, 3, 2, [0] * 23 + [1])`. 67 of 100 runs reached it, and 94 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthThreeBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 26.0 | 572.0 | 275.5 | 272.6 | 251.9–293.4 |
| Reduction time (ms) | 0.94 | 23.46 | 5.1 | 5.71 | 4.95–6.47 |
| Iterations to failure | 1.0 | 7.0 | 1.0 | 1.8 | 1.6–2.1 |

`swift run -c release ExhaustRunner --challenge depthThreeBind --iterations 100`

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

The known semantic optimum is `(3, 2, 2, 2, [0] * 23 + [1])`. 83 of 100 runs reached it, and 83 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFourBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 24.0 | 2667.0 | 213.0 | 297.0 | 220.8–373.2 |
| Reduction time (ms) | 5.7 | 966.69 | 30.37 | 55.55 | 31.26–79.85 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthFourBind --iterations 100`

## Depth 5

### Normalization

Exhaust produced 24 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 71% | 24 | `(3, 2, 2, 2, 1, [0] * 23 + [1])` |
| 2% | 54 | `(6, 3, 3, 1, 1, [0] * 53 + [1])` |
| 2% | 27 | `(9, 3, 1, 1, 1, [0] * 26 + [1])` |
| 2% | 36 | `(9, 4, 1, 1, 1, [0] * 35 + [1])` |
| 2% | 72 | `(9, 2, 2, 2, 1, [0] * 71 + [1])` |
| 2% | 30 | `(6, 5, 1, 1, 1, [0] * 29 + [1])` |
| 2% | 30 | `(10, 3, 1, 1, 1, [0] * 29 + [1])` |
| 1% | 42 | `(7, 3, 2, 1, 1, [0] * 41 + [1])` |
| 1% | 90 | `(9, 5, 2, 1, 1, [0] * 89 + [1])` |
| 1% | 56 | `(8, 7, 1, 1, 1, [0] * 55 + [1])` |
| 1% | 36 | `(6, 6, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 126 | `(9, 7, 2, 1, 1, [0] * 125 + [1])` |
| 1% | 120 | `(10, 4, 3, 1, 1, [0] * 119 + [1])` |
| 1% | 42 | `(7, 6, 1, 1, 1, [0] * 41 + [1])` |
| 1% | 48 | `(6, 4, 2, 1, 1, [0] * 47 + [1])` |
| 1% | 72 | `(9, 8, 1, 1, 1, [0] * 71 + [1])` |
| 1% | 56 | `(7, 2, 2, 2, 1, [0] * 55 + [1])` |
| 1% | 28 | `(7, 2, 2, 1, 1, [0] * 27 + [1])` |
| 1% | 60 | `(10, 6, 1, 1, 1, [0] * 59 + [1])` |
| 1% | 25 | `(5, 5, 1, 1, 1, [0] * 24 + [1])` |
| 1% | 40 | `(10, 2, 2, 1, 1, [0] * 39 + [1])` |
| 1% | 64 | `(8, 4, 2, 1, 1, [0] * 63 + [1])` |
| 1% | 84 | `(7, 3, 2, 2, 1, [0] * 83 + [1])` |
| 1% | 32 | `(8, 2, 2, 1, 1, [0] * 31 + [1])` |

The known semantic optimum is `(3, 2, 2, 2, 1, [0] * 23 + [1])`. 71 of 100 runs reached it, and 71 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFiveBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 25.0 | 15597.0 | 152.5 | 689.9 | 262.5–1117.3 |
| Reduction time (ms) | 98.07 | 33420.79 | 152.71 | 882.33 | 90.97–1673.7 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthFiveBind --iterations 100`

## Depth 6

### Normalization

Exhaust produced 43 distinct counterexamples across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 47% | 32 | `(2, 2, 2, 2, 2, 1, [0] * 31 + [1])` |
| 3% | 125 | `(5, 5, 5, 1, 1, 1, [0] * 124 + [1])` |
| 2% | 30 | `(6, 5, 1, 1, 1, 1, [0] * 29 + [1])` |
| 2% | 30 | `(10, 3, 1, 1, 1, 1, [0] * 29 + [1])` |
| 2% | 72 | `(9, 2, 2, 2, 1, 1, [0] * 71 + [1])` |
| 2% | 27 | `(9, 3, 1, 1, 1, 1, [0] * 26 + [1])` |
| 2% | 36 | `(9, 4, 1, 1, 1, 1, [0] * 35 + [1])` |
| 2% | 120 | `(10, 3, 2, 2, 1, 1, [0] * 119 + [1])` |
| 2% | 54 | `(6, 3, 3, 1, 1, 1, [0] * 53 + [1])` |
| 2% | 72 | `(6, 6, 2, 1, 1, 1, [0] * 71 + [1])` |
| 2% | 144 | `(9, 2, 2, 2, 2, 1, [0] * 143 + [1])` |
| 1% | 42 | `(7, 6, 1, 1, 1, 1, [0] * 41 + [1])` |
| 1% | 192 | `(8, 6, 4, 1, 1, 1, [0] * 191 + [1])` |
| 1% | 56 | `(7, 2, 2, 2, 1, 1, [0] * 55 + [1])` |
| 1% | 90 | `(9, 5, 2, 1, 1, 1, [0] * 89 + [1])` |
| 1% | 64 | `(8, 4, 2, 1, 1, 1, [0] * 63 + [1])` |
| 1% | 126 | `(9, 7, 2, 1, 1, 1, [0] * 125 + [1])` |
| 1% | 28 | `(7, 2, 2, 1, 1, 1, [0] * 27 + [1])` |
| 1% | 540 | `(10, 9, 3, 2, 1, 1, [0] * 539 + [1])` |
| 1% | 72 | `(9, 8, 1, 1, 1, 1, [0] * 71 + [1])` |
| 1% | 36 | `(4, 3, 3, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 32 | `(8, 2, 2, 1, 1, 1, [0] * 31 + [1])` |
| 1% | 224 | `(8, 7, 2, 2, 1, 1, [0] * 223 + [1])` |
| 1% | 112 | `(7, 2, 2, 2, 2, 1, [0] * 111 + [1])` |
| 1% | 42 | `(7, 3, 2, 1, 1, 1, [0] * 41 + [1])` |
| 1% | 96 | `(6, 2, 2, 2, 2, 1, [0] * 95 + [1])` |
| 1% | 40 | `(10, 2, 2, 1, 1, 1, [0] * 39 + [1])` |
| 1% | 25 | `(5, 5, 1, 1, 1, 1, [0] * 24 + [1])` |
| 1% | 128 | `(8, 2, 2, 2, 2, 1, [0] * 127 + [1])` |
| 1% | 56 | `(8, 7, 1, 1, 1, 1, [0] * 55 + [1])` |
| 1% | 36 | `(6, 6, 1, 1, 1, 1, [0] * 35 + [1])` |
| 1% | 84 | `(7, 3, 2, 2, 1, 1, [0] * 83 + [1])` |
| 1% | 32 | `(4, 2, 2, 2, 1, 1, [0] * 31 + [1])` |
| 1% | 32 | `(4, 4, 2, 1, 1, 1, [0] * 31 + [1])` |
| 1% | 112 | `(7, 4, 4, 1, 1, 1, [0] * 111 + [1])` |
| 1% | 60 | `(10, 6, 1, 1, 1, 1, [0] * 59 + [1])` |
| 1% | 160 | `(10, 8, 2, 1, 1, 1, [0] * 159 + [1])` |
| 1% | 120 | `(6, 5, 4, 1, 1, 1, [0] * 119 + [1])` |
| 1% | 140 | `(10, 7, 2, 1, 1, 1, [0] * 139 + [1])` |
| 1% | 48 | `(6, 4, 2, 1, 1, 1, [0] * 47 + [1])` |
| 1% | 45 | `(5, 3, 3, 1, 1, 1, [0] * 44 + [1])` |
| 1% | 120 | `(10, 4, 3, 1, 1, 1, [0] * 119 + [1])` |
| 1% | 160 | `(8, 5, 4, 1, 1, 1, [0] * 159 + [1])` |

The known semantic optimum is `(3, 2, 2, 2, 1, 1, [0] * 23 + [1])`. 0 of 100 runs reached it, and 0 of 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthSixBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 24.0 | 22309.0 | 105.0 | 1037.2 | 436.5–1637.9 |
| Reduction time (ms) | 160.54 | 69753.3 | 798.31 | 2311.93 | 782.9–3840.97 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthSixBind --iterations 100`

## Reproduction

From the `exhaust/src` folder, run the command listed under each depth.

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
