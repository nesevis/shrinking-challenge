from math import prod

from hypothesis import given, strategies as st


@st.composite
def strategy(draw):
    factors = []
    upper = 10
    for _ in range(6):
        factor = draw(st.integers(1, upper))
        factors.append(factor)
        upper = factor
    size = prod(factors)
    payload = draw(st.lists(st.integers(0, 1), min_size=size, max_size=size))
    return (*factors, payload)


@given(strategy())
def test(value):
    assert len(value[-1]) < 24 or 1 not in value[-1]
