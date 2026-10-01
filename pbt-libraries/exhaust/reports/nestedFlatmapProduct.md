# Nested Flatmap (Product) Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

Each depth is a separate challenge. Each factor is drawn from `1...previous`, starting at `1...10`, and the property fails when the product of the factors is at least 24. There is no payload. Counterexamples are written as `(factors…)`. The minimal counterexample is the smallest failing tuple under shortlex.

## Depth 2

### Normalization

Exhaust produced 1 distinct counterexample across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `(5, 5)` |

The minimal counterexample is `(5, 5)`. All 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthTwoProductBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 14.0 | 36.0 | 32.0 | 29.4 | 28.1–30.6 |
| Reduction time (ms) | 0.06 | 0.3 | 0.18 | 0.17 | 0.16–0.18 |
| Iterations to failure | 1.0 | 10.0 | 2.0 | 2.5 | 2.1–2.9 |

`swift run -c release ExhaustRunner --challenge depthTwoProductBind --iterations 100`

## Depth 3

### Normalization

Exhaust produced 1 distinct counterexample across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `(3, 3, 3)` |

The minimal counterexample is `(3, 3, 3)`. All 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthThreeProductBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 27.0 | 70.0 | 63.0 | 58.1 | 56.1–60.1 |
| Reduction time (ms) | 0.22 | 2.03 | 0.93 | 0.81 | 0.76–0.87 |
| Iterations to failure | 1.0 | 7.0 | 1.0 | 1.8 | 1.6–2.1 |

`swift run -c release ExhaustRunner --challenge depthThreeProductBind --iterations 100`

## Depth 4

### Normalization

Exhaust produced 1 distinct counterexample across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `(3, 2, 2, 2)` |

The minimal counterexample is `(3, 2, 2, 2)`. All 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFourProductBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 25.0 | 97.0 | 81.5 | 72.4 | 68.6–76.2 |
| Reduction time (ms) | 0.55 | 3.07 | 2.31 | 2.13 | 2.02–2.25 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthFourProductBind --iterations 100`

## Depth 5

### Normalization

Exhaust produced 1 distinct counterexample across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `(2, 2, 2, 2, 2)` |

The minimal counterexample is `(2, 2, 2, 2, 2)`. All 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFiveProductBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 25.0 | 136.0 | 43.5 | 69.8 | 61.3–78.2 |
| Reduction time (ms) | 5.11 | 7.96 | 5.68 | 5.87 | 5.75–5.99 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthFiveProductBind --iterations 100`

## Depth 6

### Normalization

Exhaust produced 1 distinct counterexample across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 100% | `(2, 2, 2, 2, 2, 1)` |

The minimal counterexample is `(2, 2, 2, 2, 2, 1)`. All 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthSixProductBind.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 10.0 | 54.0 | 31.0 | 30.5 | 28.1–32.9 |
| Reduction time (ms) | 6.82 | 19.84 | 13.44 | 13.08 | 12.52–13.64 |
| Iterations to failure | 1.0 | 6.0 | 1.0 | 1.7 | 1.5–1.9 |

`swift run -c release ExhaustRunner --challenge depthSixProductBind --iterations 100`

## Reproduction

From the `exhaust/src` folder, run the command listed under each depth.

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
