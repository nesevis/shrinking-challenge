# Report for Hypothesis Shrinking on "hash collision state machine 100"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 59 distinct results in 100 test runs.

The most common were:

* ``[put(0, 0), put(100, 1)]`` (39.00%)
* ``[put(499, 0), put(99, 1)]`` (2.00%)
* ``[put(100, 0), put(0, 1)]`` (2.00%)
* ``[put(0, 0), put(700, 1)]`` (2.00%)
* ``[put(722, 0), put(322, 1)]`` (1.00%)
* ``[put(322, 0), put(222, 1)]`` (1.00%)
* ``[put(88, 0), put(388, 1)]`` (1.00%)
* ``[put(304, 0), put(604, 1)]`` (1.00%)
* ``[put(254, 0), put(354, 1)]`` (1.00%)
* ``[put(259, 0), put(159, 1)]`` (1.00%)

## Performance

Over 100 runs, Hypothesis performed between 20 and 94 evaluations during shrinking,
with a mean cost of 46.47 (95% confidence interval 43.18 - 49.70).
