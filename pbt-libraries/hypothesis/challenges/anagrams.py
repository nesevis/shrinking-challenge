from random import Random
from time import perf_counter

from hypothesis import Phase, settings, strategies as st
from hypothesis.control import BuildContext
from hypothesis.internal.conjecture.data import ConjectureData, Status
from hypothesis.internal.conjecture.engine import ConjectureRunner
from hypothesis.internal.escalation import InterestingOrigin


text = st.text()
strategy = st.tuples(text, text)
start = ("a gentle man and astronomer", "elegant man and moon starer")


def invariant(a, b):
    return a == b or sorted(a) != sorted(b)


def draw_pair(data):
    with BuildContext(data, wrapped_test=lambda: None):
        return data.draw(strategy)


def shrink_once(seed):
    """Shrink the fixed failing example once, without a generation phase."""
    started = perf_counter()
    choices = strategy._invert(start)

    evaluations = 0
    origin = InterestingOrigin(AssertionError, "anagrams", 0, (), ())

    def test_function(data):
        nonlocal evaluations
        pair = draw_pair(data)
        evaluations += 1
        if not invariant(*pair):
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

    output = draw_pair(ConjectureData.for_choices(shrinker.choices))

    return {
        "seed": seed,
        "evaluations": evaluations,
        "original": {"a": repr(start[0]), "b": repr(start[1])},
        "shrunk": {"a": repr(output[0]), "b": repr(output[1])},
        "generate_seconds": 0.0,
        "shrink_seconds": shrink_seconds,
        "total_seconds": perf_counter() - started,
    }
