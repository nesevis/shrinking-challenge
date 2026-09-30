from random import Random
from time import perf_counter

from hypothesis import Phase, settings, strategies as st
from hypothesis.control import BuildContext
from hypothesis.internal.conjecture.data import ConjectureData, Status
from hypothesis.internal.conjecture.engine import ConjectureRunner
from hypothesis.internal.escalation import InterestingOrigin

# The unique list generator never proposes duplicates while shrinking.
strategy = st.lists(st.integers(), unique=True)
start = [9973, 4421, 8810, 1203, 7777, 5050]


def invariant(xs):
    return len(set(xs)) < 5 or sum(xs) <= 50


def draw_value(data):
    with BuildContext(data, wrapped_test=lambda: None):
        return data.draw(strategy)


def shrink_once(seed):
    """Shrink the fixed starting value once, without a generation phase."""
    started = perf_counter()
    choices = strategy._invert(start)

    evaluations = 0
    origin = InterestingOrigin(AssertionError, "distinct_sum", 0, (), ())

    def test_function(data):
        nonlocal evaluations
        value = draw_value(data)
        evaluations += 1
        if not invariant(value):
            data.mark_interesting(origin)

    runner = ConjectureRunner(
        test_function,
        settings=settings(database=None, phases=[Phase.shrink]),
        random=Random(seed),
        ignore_limits=True,
    )
    initial = runner.cached_test_function(choices)
    shrinker = runner.new_shrinker(
        initial, predicate=lambda result: result.status == Status.INTERESTING
    )
    shrinker.max_stall = 2000
    shrink_started = perf_counter()
    shrinker.shrink()
    shrink_seconds = perf_counter() - shrink_started

    output = draw_value(ConjectureData.for_choices(shrinker.choices))
    return {
        "seed": seed,
        "evaluations": evaluations,
        "original": {"xs": repr(start)},
        "shrunk": {"xs": repr(output)},
        "generate_seconds": 0.0,
        "shrink_seconds": shrink_seconds,
        "total_seconds": perf_counter() - started,
    }
