# Anagrams Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

## Normalization

Exhaust reduced the fixed starting example `("a gentle man and astronomer", "elegant man and moon starer")` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `(" \0", "\0 ")` |

Here `\0` is U+0000. Each string has two characters, the size of a minimal counterexample.

See [the starting input](/pbt-libraries/exhaust/failures/anagrams.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 1222 |
| Reduction time (ms) | 8.56 |
| Wall time (ms) | 9.096 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge anagrams --iterations 1`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
