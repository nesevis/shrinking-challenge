# Report for Hypothesis Shrinking on "hash collision 1000"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 9 distinct results in 100 test runs.

These were:

* ``([(1000, 0)], 0, 1)`` (40.00%)
* ``([(0, 0)], 1000, 1)`` (22.00%)
* ``([(3000, 0)], 0, 1)`` (13.00%)
* ``([(0, 0)], 3000, 1)`` (11.00%)
* ``([(0, 0)], 5000, 1)`` (4.00%)
* ``([(0, 0)], 7000, 1)`` (3.00%)
* ``([(5000, 0)], 0, 1)`` (3.00%)
* ``([(7000, 0)], 0, 1)`` (2.00%)
* ``([(9000, 0)], 0, 1)`` (2.00%)

## Performance

Over 100 runs, Hypothesis performed between 82 and 1086 evaluations during shrinking,
with a mean cost of 771.10 (95% confidence interval 716.07 - 828.05).
