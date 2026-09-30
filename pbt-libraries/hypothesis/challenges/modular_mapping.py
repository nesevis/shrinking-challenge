from hypothesis import given, strategies as st


strategy = st.integers(0, 1_000).map(lambda n: (n * 37) % 1_001)


@given(strategy)
def test(value):
    assert value < 900
