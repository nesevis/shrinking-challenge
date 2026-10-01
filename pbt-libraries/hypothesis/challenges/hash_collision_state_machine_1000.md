# Report for Hypothesis Shrinking on "hash collision state machine 1000"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 98 distinct results in 100 test runs.

A few examples of these were:

* ``[put(140, 0), put(1140, 1)]``
* ``[put(4148, 0), put(148, 1)]``
* ``[put(3871, 0), put(7871, 1)]``
* ``[put(124, 0), put(1124, 1)]``
* ``[put(6541, 0), put(541, 1)]``

## Performance

Over 100 runs, Hypothesis performed between 34 and 171 evaluations during shrinking,
with a mean cost of 103.50 (95% confidence interval 97.59 - 109.41).
