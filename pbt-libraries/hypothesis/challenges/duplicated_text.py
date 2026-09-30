from random import Random
from string import ascii_lowercase, digits
from time import perf_counter

from hypothesis import Phase, settings, strategies as st
from hypothesis.control import BuildContext
from hypothesis.internal.conjecture.data import ConjectureData, Status
from hypothesis.internal.conjecture.engine import ConjectureRunner
from hypothesis.internal.escalation import InterestingOrigin


# Fixed-length strings, so equal values can only shrink by rewriting characters in both.
text = st.text(alphabet=ascii_lowercase + digits, min_size=8, max_size=8)
strategy = st.tuples(text, text)
start = ("q7zq7zq7", "q7zq7zq7")


def invariant(a, b):
    return a != b or len(set(a)) < 3


def draw_pair(data):
    with BuildContext(data, wrapped_test=lambda: None):
        return data.draw(strategy)


def shrink_once(seed):
    """Shrink the fixed duplicated pair once, without a generation phase."""
    started = perf_counter()
    choices = strategy._invert(start)

    evaluations = 0
    origin = InterestingOrigin(AssertionError, "duplicated_text", 0, (), ())

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
