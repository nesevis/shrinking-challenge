# Bind4 (Sum-Sized Payload) Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

Four dependent factors `1 ≤ d ≤ c ≤ b ≤ a ≤ 100` and a payload of zeros and ones whose length is `a + b + c + d`. The property fails when the payload has at least 24 elements and contains a `1`. Counterexamples are written as `(factors…, payload)`.

## Normalization

Exhaust produced 1 distinct counterexample across 100 test runs:

| Prevalence | Length | Counterexample |
|---|---|---|
| 100% | 24 | `(6, 6, 6, 6, [0] * 23 + [1])` |

The minimal counterexample is `(6, 6, 6, 6, [0] * 23 + [1])`. All 100 runs reached it, and all 100 reached the minimum payload length of 24.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/depthFourSumBind.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 191.0 | 2041.0 | 530.5 | 734.4 | 621.0–847.8 |
| Reduction time (ms) | 12.54 | 101.11 | 36.24 | 36.68 | 32.11–41.24 |
| Iterations to failure | 1.0 | 2.0 | 1.0 | 1.1 | 1.1–1.2 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge depthFourSumBind --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
