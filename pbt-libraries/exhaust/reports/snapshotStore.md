# Snapshot Store Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

A state machine challenge. The system under test is a versioned key-value store with `put`, `get`, `snapshot`, `read` (through a snapshot), `release` and `compact`. A snapshot sees the store as it was when it was taken, and compaction may discard any version no live snapshot can see. The model never compacts: it keeps every write, and each snapshot remembers how many writes it can see. The deliberate bug makes compaction keep history back to the newest live snapshot when it should keep it back to the oldest, so it only shows up with two live snapshots. Keys and values are drawn from `0...9`. Commands refer to snapshots by an index drawn from `0...999`, resolved newest first against the live snapshots with `%`: index 0 is the newest snapshot, as when Hypothesis draws from a bundle. The wide range keeps every live snapshot reachable and the modulo's bias negligible.

The spec runs with `mode: .sequential` and `.commandLimit(50)`, matching Hypothesis's default `stateful_step_count`, so both libraries generate histories of up to 50 commands. Counterexamples list the commands that ran, naming snapshots `s0`, `s1`, … in creation order.

## Normalization

Exhaust produced 22 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 61% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 6% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
| 5% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 0)]` |
| 5% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
| 3% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 0)]` |
| 3% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), release(s2), compact(), read(s0, 0)]` |
| 2% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), release(s3), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), release(s3), s4 = snapshot(), s5 = snapshot(), compact(), release(s5), s6 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), compact(), s3 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), s4 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), s3 = snapshot(), release(s3), compact(), s4 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), release(s4), s5 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), compact(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), s5 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), release(s2), release(s1), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), compact(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), s2 = snapshot(), release(s2), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), release(s1), s2 = snapshot(), release(s2), s3 = snapshot(), release(s3), s4 = snapshot(), compact(), read(s0, 0)]` |

The minimal counterexample is `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`. Every step is needed: without either write the older snapshot has nothing to lose, without the second snapshot the newest and oldest live snapshots are the same, and without the compaction nothing is discarded. 61 of 100 runs reached it.

Every reduced counterexample keeps the same core structure and key 0. The rest keep an extra `release` or `snapshot()`.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/snapshotStore.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 95.0 | 713.0 | 269.0 | 293.9 | 270.2–317.6 |
| Reduction time (ms) | 1.48 | 16.12 | 5.26 | 5.9 | 5.34–6.47 |
| Wall time (ms) | 2.555 | 16.335 | 6.707 | 7.32 | 6.678–7.962 |
| Iterations to failure | 1.0 | 866.0 | 82.0 | 126.6 | 98.1–155.1 |

Iterations to failure counts generated command sequences.

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge snapshotStore --iterations 100`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
