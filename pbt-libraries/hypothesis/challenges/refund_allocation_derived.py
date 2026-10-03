from hypothesis import assume, given, strategies as st

from refund_allocation_model import RefundRequest, invariant, is_valid


# Raw type inference: no bounds, overrides, filters, or request repair.
requests = st.from_type(RefundRequest)


@given(requests)
def test(request):
    assume(is_valid(request))
    assert invariant(request)
