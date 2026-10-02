from hypothesis import given, strategies as st

MAX_KEY = (1 << 63) - 1


@st.composite
def heaps(draw, minimum=0, depth=None):
    # Match Exhaust's depth controller and 1:5 empty/node alternatives.
    if depth is None:
        depth = draw(st.integers(min_value=0, max_value=20))
    if depth == 0 or draw(st.integers(min_value=0, max_value=5)) == 0:
        return None
    key = draw(st.integers(min_value=minimum, max_value=MAX_KEY))
    left = draw(heaps(minimum=key, depth=depth // 2))
    right = draw(heaps(minimum=key, depth=depth // 2))
    return (key, left, right)


strategy = heaps()


def heap_to_list(heap):
    # Deliberately match the original's right-before-left stack traversal.
    stack, result = [heap], []
    while stack:
        current = stack.pop()
        if current is not None:
            key, left, right = current
            result.append(key)
            stack.append(left)
            stack.append(right)
    return result


def heap_merge(first, second):
    if first is None:
        return second
    if second is None:
        return first
    x, left_x, right_x = first
    y, left_y, right_y = second
    if x <= y:
        return (x, heap_merge(right_x, second), left_x)
    return (y, heap_merge(right_y, first), left_y)


def wrong_to_sorted_list(heap):
    if heap is None:
        return []
    key, left, right = heap
    # The bug: traverse the merged heap instead of repeatedly extracting its minimum.
    return [key] + heap_to_list(heap_merge(left, right))


def heap_invariant(heap, minimum=0):
    if heap is None:
        return True
    key, left, right = heap
    return (
        minimum <= key <= MAX_KEY
        and heap_invariant(left, key)
        and heap_invariant(right, key)
    )


def invariant(heap):
    if not heap_invariant(heap):
        return True
    actual = wrong_to_sorted_list(heap)
    ordered = sorted(actual)
    return sorted(heap_to_list(heap)) == ordered and actual == ordered


@given(strategy)
def test(value):
    assert invariant(value)
