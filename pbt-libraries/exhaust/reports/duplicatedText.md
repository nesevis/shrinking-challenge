# Duplicated Text Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

## Normalization

Exhaust reduced the fixed starting example `("q7zq7zq7", "q7zq7zq7")` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `("10210210", "10210210")` |

The property fails when the two strings are equal and contain at least three distinct characters. Both strings are exactly eight characters from `a–z0–9`. The minimal counterexample is `("00000012", "00000012")`.

See [the starting input](/pbt-libraries/exhaust/failures/duplicatedText.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 54 |
| Reduction time (ms) | 0.36 |
| Wall time (ms) | 0.426 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge duplicatedText --iterations 1`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
