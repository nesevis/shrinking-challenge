from math import prod

from hypothesis import given, strategies as st


# No payload: the product of the factors is the only thing the property sees.
@st.composite
def strategy(draw):
    factors = []
    upper = 10
    for _ in range(3):
        factor = draw(st.integers(1, upper))
        factors.append(factor)
        upper = factor
    return tuple(factors)


@given(strategy())
def test(value):
    assert prod(value) < 24
