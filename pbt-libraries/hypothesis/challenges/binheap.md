# Report for Hypothesis Shrinking on "binheap"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 3 distinct results in 100 test runs.

These were:

* ``(0, None, (0, (0, None, None), (1, None, None)))`` (85.00%)
* ``(0, None, (0, None, (0, (0, None, None), (1, None, None))))`` (14.00%)
* ``(0, None, (0, (0, None, None), (0, None, (1, None, None))))`` (1.00%)

## Performance

Over 100 runs, Hypothesis performed between 67 and 209 evaluations during shrinking,
with a mean cost of 102.48 (95% confidence interval 97.45 - 107.27).
