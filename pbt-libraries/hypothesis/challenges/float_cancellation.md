# Report for Hypothesis Shrinking on "float cancellation"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 82 distinct results in 100 test runs.

The most common were:

* ``(1.0, 3.1)`` (3.00%)
* ``(1.1125369292536007e-308, 1.0)`` (3.00%)
* ``(1.0, 3.9)`` (3.00%)
* ``(1.0, 0.99999)`` (3.00%)
* ``(1.0, 3.00001)`` (3.00%)
* ``(2.225073858507e-311, 1.0)`` (3.00%)
* ``(1.175494351e-38, 1.0)`` (3.00%)
* ``(2.2250738585e-313, 1.0)`` (2.00%)
* ``(48577.0, 999999.9999999999)`` (2.00%)
* ``(1.0, 1.0000000000000002)`` (2.00%)

## Performance

Over 100 runs, Hypothesis performed between 23 and 299 evaluations during shrinking,
with a mean cost of 66.10 (95% confidence interval 50.24 - 80.34).
