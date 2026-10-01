# Leap Day Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

## Normalization

Exhaust reduced the fixed starting example `2088-02-29 13:47:00 UTC` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `2088-02-29 00:00:00 +0000` |

The property fails on February 29. The generator is Exhaust's default `Date` generator, `.date(between: .distantPast ... .distantFuture, interval: .seconds(60))`, which reduces a date as a single step index towards `.distantPast`, so its own minimal counterexample is the first leap day after `.distantPast`, around `0004-02-29 00:00:00`.

See [the starting input](/pbt-libraries/exhaust/failures/leapDay.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 34 |
| Reduction time (ms) | 0.29 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge leapDay --iterations 1`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
