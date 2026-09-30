from random import Random
from string import ascii_lowercase, digits
from time import perf_counter

from hypothesis import Phase, settings, strategies as st
from hypothesis.control import BuildContext
from hypothesis.internal.conjecture.data import ConjectureData, Status
from hypothesis.internal.conjecture.engine import ConjectureRunner
from hypothesis.internal.escalation import InterestingOrigin


# Draw whole strings independently so labels and credentials share the encoding.
user_prefix = "u: "
password_prefix = "p: "
credential_characters = ascii_lowercase + digits
text = st.text(alphabet=credential_characters + ": ")
strategy = st.tuples(text, text)
start = (user_prefix + "passw0rd", password_prefix + "passw0rd")


def invariant(username, password):
    if not username.startswith(user_prefix):
        return True
    if not password.startswith(password_prefix):
        return True

    user = username.removeprefix(user_prefix)
    secret = password.removeprefix(password_prefix)
    if len(secret) < 4 or any(c not in credential_characters for c in secret):
        return True
    return user != secret


def draw_pair(data):
    with BuildContext(data, wrapped_test=lambda: None):
        return data.draw(strategy)


def shrink_once(seed):
    """Reduce one credential collision without random failure discovery."""
    started = perf_counter()
    choices = strategy._invert(start)

    evaluations = 0
    origin = InterestingOrigin(AssertionError, "username_password", 0, (), ())

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
        "original": {"username": repr(start[0]), "password": repr(start[1])},
        "shrunk": {"username": repr(output[0]), "password": repr(output[1])},
        "generate_seconds": 0.0,
        "shrink_seconds": shrink_seconds,
        "total_seconds": perf_counter() - started,
    }
