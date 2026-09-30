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


@st.composite
def invoices(draw):
    price = draw(st.integers(1, 1_000))
    quantity = draw(st.integers(1, 100))
    eligible = price * quantity >= 1_000
    discount = draw(st.integers(0, 50)) if eligible else 0
    return Invoice(price, quantity, discount)


@given(invoices())
def test(invoice):
    assert invoice.total_cents() == expected_total(invoice)
