# Anagrams Report for Exhaust

These results are from Exhaust v1.5.1, September 30th, 2026.

## Normalization

Exhaust reduced the fixed starting example `("a gentle man and astronomer", "elegant man and moon starer")` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `(" \0", "\0 ")` |

Here `\0` is U+0000. Each string has two characters, the size of a globally minimal counterexample.

See [the starting input](/pbt-libraries/exhaust/failures/anagrams.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 1222.0 | 1222.0 | 1222.0 | 1222.0 | 1222.0–1222.0 |
| Reduction time (ms) | 8.41 | 8.41 | 8.41 | 8.41 | 8.41–8.41 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge anagrams --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
