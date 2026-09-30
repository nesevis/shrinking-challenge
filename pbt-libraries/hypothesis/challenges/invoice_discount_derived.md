# Report for Hypothesis Shrinking on "invoice discount derived"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 9 distinct results in 100 test runs.

These were:

* ``Invoice(unit_price_cents=28, quantity=36, discount_percent=1)`` (86.00%)
* ``Invoice(unit_price_cents=101, quantity=10, discount_percent=1)`` (5.00%)
* ``Invoice(unit_price_cents=11, quantity=91, discount_percent=1)`` (3.00%)
* ``Invoice(unit_price_cents=17, quantity=59, discount_percent=1)`` (1.00%)
* ``Invoice(unit_price_cents=201, quantity=5, discount_percent=1)`` (1.00%)
* ``Invoice(unit_price_cents=10, quantity=100, discount_percent=1)`` (1.00%)
* ``Invoice(unit_price_cents=501, quantity=2, discount_percent=1)`` (1.00%)
* ``Invoice(unit_price_cents=401, quantity=3, discount_percent=1)`` (1.00%)
* ``Invoice(unit_price_cents=14, quantity=72, discount_percent=1)`` (1.00%)

## Performance

Over 100 runs, Hypothesis performed between 119 and 1228 evaluations during shrinking,
with a mean cost of 748.78 (95% confidence interval 677.72 - 820.37).
