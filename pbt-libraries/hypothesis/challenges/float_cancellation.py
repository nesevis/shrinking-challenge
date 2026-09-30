from hypothesis import given, strategies as st


strategy = st.tuples(
    st.floats(-1e6, 1e6),
    st.floats(-1e6, 1e6),
)


@given(strategy)
def test(value):
    a, b = value
    assert (a + b) - b == a
