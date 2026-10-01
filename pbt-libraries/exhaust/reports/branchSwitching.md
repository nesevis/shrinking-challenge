# Branch Switching Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

## Normalization

Exhaust reduced the fixed starting example `"a branch switch"` once, passing it to `#exhaust` with `reflecting:` instead of generating a failure:

| Counterexample |
|---|
| `"    "` |

A value is an integer or a string, generated from an `@Exhaustable` enum with the integer case first. The property fails for integers over 1,000 and strings of four or more characters. The minimal counterexample is `1001`, in the integer branch.

See [the starting input](/pbt-libraries/exhaust/failures/branchSwitching.json).

## Performance

| Metric | Value |
|---|---|
| Evaluations | 17 |
| Reduction time (ms) | 1.09 |
| Wall time (ms) | 1.19 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge branchSwitching --iterations 1`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
