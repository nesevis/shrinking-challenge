from random import Random
from time import perf_counter

from hypothesis import Phase, settings, strategies as st
from hypothesis.control import BuildContext
from hypothesis.internal.conjecture.data import ConjectureData, Status
from hypothesis.internal.conjecture.engine import ConjectureRunner
from hypothesis.internal.escalation import InterestingOrigin

# Macbeth, Act 5, Scene 5. Shrinking has to delete everything around and between the two needles.
strategy = st.text()
start = """She should have died hereafter;
There would have been a time for such a word.
Tomorrow, and tomorrow, and tomorrow,
Creeps in this petty pace from day to day,
To the last syllable of recorded time;
And all our yesterdays have lighted fools
The way to dusty death. Out, out, brief candle!
Life's but a walking shadow, a poor player,
That struts and frets his hour upon the stage,
And then is heard no more. It is a tale
Told by an idiot, full of sound and fury,
Signifying nothing."""


def invariant(text):
    lowered = text.lower()
    return "creep" not in lowered or "idiot" not in lowered


def draw_value(data):
    with BuildContext(data, wrapped_test=lambda: None):
        return data.draw(strategy)


def shrink_once(seed):
    """Shrink the fixed starting value once, without a generation phase."""
    started = perf_counter()
    choices = strategy._invert(start)

    evaluations = 0
    origin = InterestingOrigin(AssertionError, "haystack", 0, (), ())

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
        "original": {"text": repr(start)},
        "shrunk": {"text": repr(output)},
        "generate_seconds": 0.0,
        "shrink_seconds": shrink_seconds,
        "total_seconds": perf_counter() - started,
    }
