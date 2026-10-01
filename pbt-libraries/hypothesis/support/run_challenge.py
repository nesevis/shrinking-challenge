import hashlib
import json
import os
import sys
from random import Random
from time import perf_counter

from tqdm import trange

from hypothesis import HealthCheck, Phase, Verbosity
from hypothesis import seed as with_seed
from hypothesis import settings
from hypothesis.internal.reflection import proxies
from hypothesis.statistics import collector


def main(filename, n_runs=100):
    if n_runs < 1:
        raise ValueError("n_runs must be positive")
    target = os.path.splitext(filename)[0] + ".json"

    random = Random(
        int.from_bytes(
            hashlib.sha1(os.path.basename(filename).encode("utf-8")).digest(), "big"
        )
    )

    results = []

    with open(filename, "r") as i:
        source = i.read()

    compiled = compile(source, filename, "exec")

    # Fixed-start challenges bypass generation and the 100-run benchmark loop.
    namespace = {}
    exec(compiled, namespace)
    if "shrink_once" in namespace:
        results.append(namespace["shrink_once"](random.getrandbits(64)))
        with open(target, "w") as o:
            o.write(json.dumps(results, sort_keys=True, indent=4))
        return

    for _ in trange(n_runs):
        seed = random.getrandbits(64)

        namespace = {}

        exec(compiled, namespace)

        test = namespace["test"]

        assert getattr(test, "is_hypothesis_test", False)

        base_function = test.hypothesis.inner_test
        # Challenges whose arguments have no useful repr, such as state machines, can describe a run themselves
        describe = namespace.get("describe")

        stats = {
            "seed": seed,
            "evaluations": 0,
        }

        def record(kwargs, interesting):
            if interesting:
                if describe is not None:
                    kwargs = describe(kwargs)
                else:
                    kwargs = {name: repr(value) for name, value in kwargs.items()}

                if "original" not in stats:
                    stats["original"] = kwargs
                stats["shrunk"] = kwargs
            if "original" in stats:
                stats["evaluations"] += 1

        @proxies(base_function)
        def replacement_function(**kwargs):
            try:
                base_function(**kwargs)
                record(kwargs, False)
            except Exception:
                record(kwargs, True)
                raise

        test.hypothesis.inner_test = replacement_function

        test = with_seed(seed)(
            settings(
                database=None,
                suppress_health_check=list(HealthCheck),
                max_examples=10 ** 6,
                phases=[Phase.generate, Phase.shrink],
                verbosity=Verbosity.quiet,
            )(test)
        )

        phase_statistics = []
        started = perf_counter()
        with collector.with_value(phase_statistics.append):
            try:
                test()
            except Exception:
                if "original" not in stats:
                    raise
        stats["total_seconds"] = perf_counter() - started
        if phase_statistics:
            phases = phase_statistics[-1]
            for phase in ("generate", "shrink"):
                stats[phase + "_seconds"] = phases.get(phase + "-phase", {}).get(
                    "duration-seconds", 0.0
                )

        results.append(stats)
    with open(target, "w") as o:
        o.write(json.dumps(results, sort_keys=True, indent=4,))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 100)
