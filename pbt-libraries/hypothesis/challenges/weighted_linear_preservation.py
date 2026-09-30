from hypothesis import given, strategies as st


strategy = st.tuples(
    st.integers(0, 20),
    st.integers(0, 20),
    st.integers(0, 20),
)


@given(strategy)
def test(value):
    x, y, z = value
    assert 2 * x + y + z != 20
