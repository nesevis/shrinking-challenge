# Report for Hypothesis Shrinking on "hash collision 100"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 8 distinct results in 100 test runs.

These were:

* ``([(100, 0)], 0, 1)`` (62.00%)
* ``([(0, 0)], 100, 1)`` (20.00%)
* ``([(300, 0)], 0, 1)`` (7.00%)
* ``([(0, 0)], 300, 1)`` (4.00%)
* ``([(500, 0)], 0, 1)`` (4.00%)
* ``([(0, 0)], 900, 1)`` (1.00%)
* ``([(0, 0)], 500, 1)`` (1.00%)
* ``([(0, 0)], 700, 1)`` (1.00%)

## Performance

Over 100 runs, Hypothesis performed between 28 and 452 evaluations during shrinking,
with a mean cost of 131.94 (95% confidence interval 117.08 - 145.71).
