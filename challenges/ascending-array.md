# AscendingArray

Generate raw arrays of signed integers and shrink a failure while preserving
strictly ascending order. Negative values, zero, and positive values are allowed.
Do not sort, filter, repair, or enforce uniqueness in the generator.

## Generated arrays: 5–10 values

The comparison generates arrays of 5–10 values. The deliberately false property
fails exactly when the array equals its sorted copy and all its values are unique.
Duplicates and any out-of-order pair pass. The generator enforces the 5–10-element
length constraint.

The unique shortlex minimum is **`[0, 1, 2, 3, 4]`**, using the libraries' integer
simplicity order `0, 1, -1, 2, -2, …`. Negative-leading consecutive arrays have
minimum length but are not globally shortlex-minimal.

The [comparison results](../reports/ascending-array/README.md) cover
seeds 1337–1436 with a 25,000-example budget per seed. Exhaust is run first;
Hypothesis and Hegel follow after successful discovery. All three found failures
in every run. The earlier [fixed-length-5 experiment](../reports/ascending5-generated/README.md)
is retained separately.

## Standard challenge runners

All three standard runners use the same generated 5–10-element challenge, with a
25,000-example discovery budget per seed. There is no fixed input, reflection, or
inversion path for AscendingArray.

```sh
cd pbt-libraries/exhaust/src
swift test --filter AscendingArrayTests
swift run ExhaustRunner --challenge ascendingArray --iterations 100 --seed 1337
cd ../../hypothesis
venv/bin/python -m unittest support.test_ascending_array
venv/bin/python support/run_challenge.py challenges/ascending_array.py 100
cd ../hegel
cargo test --locked --offline ascending_array
cargo run --locked --offline -- --challenge ascending_array --iterations 100 --seed 1337
```

The Hypothesis CLI uses its usual filename-derived seeds. The linked comparison
report shows how to pass seeds 1337–1436 to the standard runner for reproduction. Hegel lists this
challenge individually; the existing release-refresh batch is unchanged.

[Exhaust implementation](../pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/AscendingArrayChallenge.swift)
· [Hypothesis implementation](../pbt-libraries/hypothesis/challenges/ascending_array.py)
· [Hegel implementation](../pbt-libraries/hegel/src/ascending_array.rs).
