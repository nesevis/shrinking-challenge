# Report for Hypothesis Shrinking on "hash collision state machine 10"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 77 distinct results in 100 test runs.

The most common were:

* ``[put(0, 0), put(10, 1)]`` (7.00%)
* ``[put(30, 0), put(0, 1)]`` (5.00%)
* ``[put(0, 0), put(30, 1)]`` (4.00%)
* ``[put(10, 0), put(0, 1)]`` (4.00%)
* ``[put(70, 0), put(0, 1)]`` (3.00%)
* ``[put(9, 0), put(19, 1)]`` (2.00%)
* ``[put(90, 0), put(0, 1)]`` (2.00%)
* ``[put(49, 0), put(9, 1)]`` (2.00%)
* ``[put(42, 0), put(62, 1)]`` (2.00%)
* ``[put(71, 0), put(1, 1)]`` (2.00%)

## Performance

Over 100 runs, Hypothesis performed between 20 and 75 evaluations during shrinking,
with a mean cost of 34.41 (95% confidence interval 32.45 - 36.24).
