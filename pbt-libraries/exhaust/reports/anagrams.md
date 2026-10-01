# Anagrams Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

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
| Reduction time (ms) | 19.15 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge anagrams --iterations 1`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
