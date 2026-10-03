"""Refund allocation with a non-refundable fee and deliberately gross-based weights."""

from dataclasses import dataclass

from hypothesis import strategies as st

PROCESSING_FEE_CENTS = 30
CHARGE_LIMIT = 20
MAX_AMOUNT = 2**63 - 1


@dataclass(frozen=True)
class Charge:
    paid_cents: int

    @property
    def refundable_cents(self):
        return self.paid_cents - PROCESSING_FEE_CENTS


@dataclass(frozen=True)
class RefundRequest:
    charges: list[Charge]
    refund_cents: int

    def __repr__(self):
        return f"RefundRequest({[charge.paid_cents for charge in self.charges]!r}, {self.refund_cents})"


def total_refundable(charges):
    return sum(charge.refundable_cents for charge in charges)


def is_valid(request):
    return (
        1 <= len(request.charges) <= CHARGE_LIMIT
        and all(
            PROCESSING_FEE_CENTS < charge.paid_cents <= MAX_AMOUNT
            for charge in request.charges
        )
        and 0 <= request.refund_cents <= MAX_AMOUNT
        and request.refund_cents <= total_refundable(request.charges)
    )


@st.composite
def requests(draw):
    charges = draw(
        st.lists(
            st.builds(Charge, st.integers(PROCESSING_FEE_CENTS + 1, MAX_AMOUNT)),
            min_size=1,
            max_size=CHARGE_LIMIT,
        )
    )
    refund = draw(st.integers(0, min(total_refundable(charges), MAX_AMOUNT)))
    return RefundRequest(charges, refund)


def allocate_refund(request):
    # Deliberate bug: gross payments include the retained processing fees.
    weights = [charge.paid_cents for charge in request.charges]
    total = sum(weights)
    numerators = [request.refund_cents * weight for weight in weights]
    allocations = [numerator // total for numerator in numerators]
    remaining = request.refund_cents - sum(allocations)
    priority = sorted(
        range(len(weights)), key=lambda index: (-(numerators[index] % total), index)
    )
    for index in priority[:remaining]:
        allocations[index] += 1
    return allocations


def satisfies_contract(request, allocations):
    if not is_valid(request) or len(allocations) != len(request.charges):
        return False
    if sum(allocations) != request.refund_cents:
        return False
    total = total_refundable(request.charges)
    remainders = []
    rounded_up = []
    for charge, allocation in zip(request.charges, allocations):
        if not 0 <= allocation <= charge.refundable_cents:
            return False
        floor, remainder = divmod(request.refund_cents * charge.refundable_cents, total)
        ceiling = floor + (remainder != 0)
        if allocation not in (floor, ceiling):
            return False
        remainders.append(remainder)
        rounded_up.append(allocation > floor)
    for recipient in range(len(allocations)):
        if not rounded_up[recipient]:
            continue
        for other in range(len(allocations)):
            if not rounded_up[other] and (
                remainders[other] > remainders[recipient]
                or (remainders[other] == remainders[recipient] and other < recipient)
            ):
                return False
    return True


def invariant(request):
    return satisfies_contract(request, allocate_refund(request))
