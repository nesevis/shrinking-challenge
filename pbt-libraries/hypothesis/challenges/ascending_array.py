"""AscendingArray: ordinary generation of 5–10 signed 64-bit integers."""

from hypothesis import given, strategies as st


generation_budget = 25_000


def arrays(minimum=5, maximum=10):
    return st.lists(
        st.integers(min_value=-(2**63), max_value=2**63 - 1),
        min_size=minimum,
        max_size=maximum,
    )


def invariant(values):
    return not (len(set(values)) == len(values) and values == sorted(values))


strategy = arrays()


@given(values=strategy)
def test(values):
    assert invariant(values)
