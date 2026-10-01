# Distinct Sum Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

## Normalization

Exhaust reduced the fixed starting example `[9973, 4421, 8810, 1203, 7777, 5050]` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `[-2, -1, 0, 1, 53]` |

The property fails when the list has at least five distinct elements and a sum over 50. The generator is `.int().unique().array()`. Its uniqueness applies while generating, not during reduction, so the property itself requires distinct elements.

See [the starting input](/pbt-libraries/exhaust/failures/distinctSum.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 130 |
| Reduction time (ms) | 0.56 |
| Wall time (ms) | 0.644 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge distinctSum --iterations 1`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
