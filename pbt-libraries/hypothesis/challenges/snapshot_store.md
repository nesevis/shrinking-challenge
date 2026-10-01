# Report for Hypothesis Shrinking on "snapshot store"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 21 distinct results in 100 test runs.

The most common were:

* ``[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`` (37.00%)
* ``[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]`` (18.00%)
* ``[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]`` (7.00%)
* ``[put(3, 0), s0 = snapshot(), put(3, 0), s1 = snapshot(), compact(), read(s0, 3)]`` (6.00%)
* ``[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), read(s0, 0)]`` (5.00%)
* ``[put(4, 0), s0 = snapshot(), put(4, 0), s1 = snapshot(), compact(), release(s1), read(s0, 4)]`` (4.00%)
* ``[put(4, 0), s0 = snapshot(), put(4, 0), s1 = snapshot(), compact(), read(s0, 4)]`` (4.00%)
* ``[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), s3 = snapshot(), read(s0, 0)]`` (2.00%)
* ``[put(3, 0), s0 = snapshot(), put(3, 0), s1 = snapshot(), compact(), release(s1), read(s0, 3)]`` (2.00%)
* ``[put(1, 0), s0 = snapshot(), put(1, 0), s1 = snapshot(), compact(), read(s0, 1)]`` (2.00%)

## Performance

Over 100 runs, Hypothesis performed between 102 and 1110 evaluations during shrinking,
with a mean cost of 430.89 (95% confidence interval 384.69 - 474.72).
