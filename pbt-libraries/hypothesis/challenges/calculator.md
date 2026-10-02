# Report for Hypothesis Shrinking on "calculator"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis currently normalises this example to ``('/', 0, ('+', 0, 0))``

## Performance

Over 100 runs, Hypothesis performed between 23 and 254 evaluations during shrinking,
with a mean cost of 90.47 (95% confidence interval 81.95 - 98.63).

The bootstrap estimate above differs slightly from the raw arithmetic mean of
90.53 evaluations used in the README. Counts start at the first actual property
failure and include completed property calls thereafter. Assumption rejections
are excluded: the harness was corrected before this 100-seed rerun.

| Timing | Mean (ms) |
|---|---:|
| Generation | 1496.90 |
| Shrinking | 40.03 |
| Total elapsed | 1538.10 |

All 100 original and reduced expressions passed the literal-zero-divisor
precondition and independently reproduced a `ZeroDivisionError`.
