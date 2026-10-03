from hypothesis import assume, given

from refund_allocation_model import invariant, is_valid, requests


@given(requests())
def test(request):
    assume(is_valid(request))
    assert invariant(request)
