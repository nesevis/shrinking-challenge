from dataclasses import dataclass

from hypothesis import given, strategies as st


@dataclass
class Invoice:
    unit_price_cents: int
    quantity: int
    discount_percent: int

    def total_cents(self):
        # Deliberate bug: round each unit before multiplying by quantity.
        discounted_unit = (
            self.unit_price_cents * (100 - self.discount_percent)
        ) // 100
        return discounted_unit * self.quantity


def expected_total(invoice):
    # Business rule: discount the whole invoice, then round down once.
    return (
        invoice.unit_price_cents
        * invoice.quantity
        * (100 - invoice.discount_percent)
    ) // 100


def is_valid(invoice):
    return (
        1 <= invoice.unit_price_cents <= 1_000
        and 1 <= invoice.quantity <= 100
        and 0 <= invoice.discount_percent <= 50
        and (
            invoice.unit_price_cents * invoice.quantity >= 1_000
            or invoice.discount_percent == 0
        )
    )


# Fully inferred from the dataclass annotations: no bounds or custom strategies.
invoices = st.from_type(Invoice)


@given(invoices)
def test(invoice):
    # Invalid business inputs are rejected; keep generation fully derived.
    if not is_valid(invoice):
        return
    assert invoice.total_cents() == expected_total(invoice)
