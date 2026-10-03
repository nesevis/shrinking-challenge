# Refund Allocation

A payment processor retains a flat **30-cent non-refundable processing fee per
charge**. A partial refund must be allocated proportionally to each charge's
remaining refundable balance, not its original gross payment.

For each charge, `refundableCents = paidCents - 30`. A request asks for a refund
between zero and the sum of those balances. The allocator must:

- Return one allocation per charge.
- Preserve the requested refund total exactly.
- Keep each allocation between zero and that charge's refundable balance.
- Allocate each charge the floor or ceiling of its exact net-proportional share.
- Give leftover cents to the largest fractional remainders, breaking ties by
  original charge order.

The deliberate defect uses **gross payments as allocation weights**, but otherwise
correctly distributes rounding remainders. It conserves money while potentially
refunding retained fees or violating net-proportional allocation.

```text
RefundRequest([31, 33], 4)
Refundable balances: [1, 3]
Correct allocation:  [1, 3]
Buggy allocation:    [2, 2]
```

The first charge receives two cents despite having only one refundable cent.
Smaller valid requests can pass: equal minimum payments `[31, 31]` with refund `1`
allocate correctly. Zero refunds and valid single-charge refunds also pass.
The 30-cent fee is a business rule, not a threshold activating the defect.

## Exhaust generators

- `refundAllocation`: a handwritten generator constructs payments with positive
  refundable balances, then chooses a refund from zero through the smaller of
  the combined refundable balance and `Int.max`.
- `refundAllocationDerived`: raw `RefundRequest.gen()`, including derived nested
  `Charge` values. No domain settings, payload overrides, filters, or repair.

Both use the same property. Invalid requests throw `PropertySkip()`. The accepted
benchmark domain has 1–20 charges, each gross payment in `31...Int.max`, and a
nonnegative `Int` refund no greater than the total refundable balance. Twenty
charges is a resource bound shared by both treatments; larger valid payment
histories are outside this benchmark. Charges whose payment cannot cover the fee
and leave a positive refundable balance are outside this domain. The derived
structural budget remains the library default.

Totals, proportional products, and contract checks use exact `Int128` arithmetic
on the runner's 64-bit platforms. Allocations fit in `Int` because no share exceeds
the requested refund. Overflow is not the intended failure.

The property checks cardinality, bounds, conservation, floor/ceiling shares, and
remainder priority directly against net balances. A repaired net-based allocator
exists only in validation tests to demonstrate that a correct implementation
satisfies these checks.

Run either treatment with the existing CLI and existing statistics:

```sh
cd pbt-libraries/exhaust/src
swift run -c release ExhaustRunner --challenge refundAllocation --iterations 100
swift run -c release ExhaustRunner --challenge refundAllocationDerived --iterations 100
```

## Hegel ports

`refund_allocation` constructs valid requests with Hegel's public composite and
vector generators. `refund_allocation_derived` uses raw
`gs::default::<RefundRequest>()` with `#[derive(DefaultGenerator)]` on the request
and charge types. Invalid requests are rejected with `tc.assume` before the
benchmark recorder sees a verdict. The contract, fee, signed-64-bit domain,
`i128` arithmetic, stable tie rule, and defect match Exhaust.

Both are standalone CLI challenges, excluded from Hegel's existing published
comparison suite. The runner defaults to 100 consecutive seeds starting at 1337;
`--seed N --iterations K` selects another consecutive range. There are no seed-list
files or seed-file options. Equal numeric seeds do not give equal starting inputs
across libraries; raw-derived distributions and structural budgets remain each
library's own defaults.

## Hypothesis ports

`challenges/refund_allocation.py` uses a constructive composite strategy;
`challenges/refund_allocation_derived.py` uses plain `st.from_type(RefundRequest)`
over typed dataclasses. Shared types, contract checks, and the faulty allocator
live in `support/refund_allocation_model.py`. No registered type strategies,
overrides, filters, or repair are applied to raw derivation.

Both properties use `assume(is_valid(request))`. The accepted domain matches the
other ports: 1–20 charges, payments in `31...2**63-1`, and an `Int64`-sized refund
within the net total. Raw inferred Python integers are unbounded; out-of-domain
values are rejected rather than recorded as property verdicts. Python arithmetic
is exact.

Run from `pbt-libraries/hypothesis`:

```sh
venv/bin/python support/run_challenge.py challenges/refund_allocation.py 100
venv/bin/python support/run_challenge.py challenges/refund_allocation_derived.py 100
```

The existing harness derives each run's seed sequence from SHA1 of its challenge
filename. Thus neither the two Hypothesis treatments nor the different libraries
start from paired inputs.

No reporting fields or comparison tables are added for this challenge.
