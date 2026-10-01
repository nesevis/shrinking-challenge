# Hash Collision Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

A hash map whose hash code is the key modulo `M` has a deliberate bug: `put` and `get` match entries by hash code rather than by key. Both make the same mistake, so the postcondition "after `put(a, v)`, `get(a) == v`" still holds. Only the frame property catches it: putting a key leaves every other key in the map unchanged. It fails when two distinct keys are congruent modulo `M`, so the reducer has to lower both keys together, in steps of `M`. Keys are drawn from `0...(10M - 1)` and values from `0...9`.

The same property runs two ways for each modulus. The generator variant builds a map from up to 20 generated entries and checks one final put; counterexamples are written as `(entries, key, value)`. The state machine variant has a single `put` command that checks the frame property after every put, and runs with `mode: .sequential` and `.commandLimit(50)`, matching Hypothesis's default `stateful_step_count`; counterexamples list the puts that ran.

## Generator (M = 10)

### Normalization

Exhaust produced 6 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 64% | `([(0, 0)], 10, 1)` |
| 12% | `([(1, 0)], 11, 1)` |
| 11% | `([(0, 0)], 70, 1)` |
| 9% | `([(0, 0)], 90, 1)` |
| 3% | `([(11, 0)], 1, 1)` |
| 1% | `([(1, 0)], 71, 1)` |

The minimal counterexample is `([(0, 0)], 10, 1)`. 64 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionTen.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 31.0 | 107.0 | 73.0 | 70.2 | 66.9–73.5 |
| Reduction time (ms) | 0.13 | 0.38 | 0.28 | 0.28 | 0.26–0.29 |
| Wall time (ms) | 0.183 | 0.531 | 0.348 | 0.343 | 0.33–0.355 |
| Iterations to failure | 3.0 | 33.0 | 15.0 | 14.7 | 13.4–16.0 |

`swift run -c release ExhaustRunner --challenge hashCollisionTen --iterations 100`

## Generator (M = 100)

### Normalization

Exhaust produced 5 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 54% | `([(0, 0)], 100, 1)` |
| 20% | `([(0, 0)], 300, 1)` |
| 16% | `([(0, 0)], 500, 1)` |
| 7% | `([(0, 0)], 700, 1)` |
| 3% | `([(0, 0)], 900, 1)` |

The minimal counterexample is `([(0, 0)], 100, 1)`. 54 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionHundred.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 64.0 | 162.0 | 104.5 | 106.8 | 103.6–110.1 |
| Reduction time (ms) | 0.25 | 0.61 | 0.4 | 0.41 | 0.4–0.42 |
| Wall time (ms) | 0.317 | 0.833 | 0.514 | 0.539 | 0.518–0.561 |
| Iterations to failure | 8.0 | 95.0 | 38.5 | 38.9 | 35.2–42.5 |

`swift run -c release ExhaustRunner --challenge hashCollisionHundred --iterations 100`

## Generator (M = 1000)

### Normalization

Exhaust produced 5 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 71% | `([(0, 0)], 1000, 1)` |
| 14% | `([(0, 0)], 3000, 1)` |
| 9% | `([(0, 0)], 5000, 1)` |
| 4% | `([(0, 0)], 7000, 1)` |
| 2% | `([(0, 0)], 9000, 1)` |

The minimal counterexample is `([(0, 0)], 1000, 1)`. 71 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionThousand.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 52.0 | 189.0 | 141.5 | 143.1 | 139.2–147.1 |
| Reduction time (ms) | 0.32 | 0.79 | 0.55 | 0.56 | 0.54–0.58 |
| Wall time (ms) | 0.529 | 5.36 | 1.199 | 1.453 | 1.283–1.622 |
| Iterations to failure | 19.0 | 1495.0 | 191.5 | 285.4 | 230.0–340.7 |

`swift run -c release ExhaustRunner --challenge hashCollisionThousand --iterations 100`

## State machine (M = 10)

### Normalization

Exhaust produced 12 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 53% | `[put(0, 0), put(10, 1)]` |
| 16% | `[put(0, 1), put(10, 0)]` |
| 9% | `[put(0, 0), put(70, 1)]` |
| 7% | `[put(0, 0), put(90, 1)]` |
| 6% | `[put(1, 0), put(11, 1)]` |
| 3% | `[put(0, 1), put(90, 0)]` |
| 1% | `[put(1, 1), put(71, 0)]` |
| 1% | `[put(1, 0), put(91, 1)]` |
| 1% | `[put(2, 1), put(12, 0)]` |
| 1% | `[put(0, 1), put(70, 0)]` |
| 1% | `[put(1, 0), put(71, 1)]` |
| 1% | `[put(1, 1), put(11, 0)]` |

The minimal counterexample is `[put(0, 0), put(10, 1)]`. 53 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionStateMachineTen.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 33.0 | 109.0 | 78.0 | 74.8 | 71.8–77.8 |
| Reduction time (ms) | 0.39 | 1.14 | 0.74 | 0.75 | 0.72–0.78 |
| Wall time (ms) | 0.424 | 1.207 | 0.81 | 0.812 | 0.776–0.848 |
| Iterations to failure | 1.0 | 3.0 | 1.0 | 1.2 | 1.1–1.2 |

Iterations to failure counts generated command sequences.

`swift run -c release ExhaustRunner --challenge hashCollisionStateMachineTen --iterations 100`

## State machine (M = 100)

### Normalization

Exhaust produced 8 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 33% | `[put(0, 0), put(100, 1)]` |
| 20% | `[put(0, 1), put(100, 0)]` |
| 13% | `[put(0, 0), put(300, 1)]` |
| 10% | `[put(0, 0), put(500, 1)]` |
| 10% | `[put(0, 1), put(300, 0)]` |
| 6% | `[put(0, 1), put(500, 0)]` |
| 5% | `[put(0, 0), put(700, 1)]` |
| 3% | `[put(0, 1), put(700, 0)]` |

The minimal counterexample is `[put(0, 0), put(100, 1)]`. 33 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionStateMachineHundred.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 77.0 | 199.0 | 106.5 | 113.2 | 108.4–117.9 |
| Reduction time (ms) | 0.52 | 3.61 | 1.06 | 1.26 | 1.14–1.38 |
| Wall time (ms) | 0.56 | 3.686 | 1.148 | 1.341 | 1.219–1.462 |
| Iterations to failure | 1.0 | 5.0 | 1.0 | 1.4 | 1.3–1.6 |

Iterations to failure counts generated command sequences.

`swift run -c release ExhaustRunner --challenge hashCollisionStateMachineHundred --iterations 100`

## State machine (M = 1000)

### Normalization

Exhaust produced 9 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 30% | `[put(0, 1), put(1000, 0)]` |
| 28% | `[put(0, 0), put(1000, 1)]` |
| 10% | `[put(0, 0), put(3000, 1)]` |
| 10% | `[put(0, 1), put(3000, 0)]` |
| 6% | `[put(0, 1), put(5000, 0)]` |
| 6% | `[put(0, 0), put(5000, 1)]` |
| 5% | `[put(0, 1), put(7000, 0)]` |
| 4% | `[put(0, 0), put(7000, 1)]` |
| 1% | `[put(0, 1), put(9000, 0)]` |

The minimal counterexample is `[put(0, 0), put(1000, 1)]`. 28 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionStateMachineThousand.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 107.0 | 307.0 | 171.0 | 180.1 | 170.8–189.3 |
| Reduction time (ms) | 0.8 | 6.99 | 1.91 | 2.42 | 2.12–2.71 |
| Wall time (ms) | 0.851 | 7.106 | 2.1 | 2.596 | 2.301–2.892 |
| Iterations to failure | 1.0 | 21.0 | 3.0 | 3.9 | 3.2–4.6 |

Iterations to failure counts generated command sequences.

`swift run -c release ExhaustRunner --challenge hashCollisionStateMachineThousand --iterations 100`

## Reproduction

From the `exhaust/src` folder, run the command listed under each variant.

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
