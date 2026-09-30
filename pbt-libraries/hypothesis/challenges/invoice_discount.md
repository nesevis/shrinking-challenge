# Report for Hypothesis Shrinking on "invoice discount"

This report was generated with Hypothesis 6.168.3

## Normalization

Hypothesis produced 22 distinct results in 100 test runs.

The most common were:

* ``Invoice(unit_price_cents=28, quantity=36, discount_percent=1)`` (40.00%)
* ``Invoice(unit_price_cents=201, quantity=5, discount_percent=1)`` (8.00%)
* ``Invoice(unit_price_cents=11, quantity=91, discount_percent=1)`` (6.00%)
* ``Invoice(unit_price_cents=12, quantity=84, discount_percent=1)`` (5.00%)
* ``Invoice(unit_price_cents=13, quantity=77, discount_percent=1)`` (5.00%)
* ``Invoice(unit_price_cents=10, quantity=100, discount_percent=1)`` (4.00%)
* ``Invoice(unit_price_cents=14, quantity=72, discount_percent=1)`` (4.00%)
* ``Invoice(unit_price_cents=19, quantity=53, discount_percent=1)`` (4.00%)
* ``Invoice(unit_price_cents=18, quantity=56, discount_percent=1)`` (3.00%)
* ``Invoice(unit_price_cents=15, quantity=67, discount_percent=1)`` (3.00%)

## Performance

Over 100 runs, Hypothesis performed between 30 and 152 evaluations during shrinking,
with a mean cost of 61.52 (95% confidence interval 56.84 - 65.76).
