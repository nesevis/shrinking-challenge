# Snapshot Store Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

A state machine challenge. The system under test is a versioned key-value store with `put`, `get`, `snapshot`, `read` (through a snapshot), `release` and `compact`. A snapshot sees the store as it was when it was taken, and compaction may discard any version no live snapshot can see. The model never compacts: it keeps every write, and each snapshot remembers how many writes it can see. The deliberate bug makes compaction keep history back to the newest live snapshot when it should keep it back to the oldest, so it only shows up with two live snapshots. Keys and values are drawn from `0...9`. Commands refer to snapshots by an index drawn from `0...999`, resolved newest first against the live snapshots with `%`: index 0 is the newest snapshot, as when Hypothesis draws from a bundle. The wide range keeps every live snapshot reachable and the modulo's bias negligible.

The spec runs with `mode: .sequential` and `.commandLimit(50)`, matching Hypothesis's default `stateful_step_count`, so both libraries generate histories of up to 50 commands. Counterexamples list the commands that ran, naming snapshots `s0`, `s1`, … in creation order.

## Normalization

Exhaust produced 37 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 51% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 8% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
| 3% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
| 2% | `[put(7, 0), s0 = snapshot(), put(7, 0), s1 = snapshot(), compact(), read(s0, 7)]` |
| 2% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), compact(), read(s0, 8)]` |
| 2% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 0)]` |
| 2% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), release(s2), compact(), read(s0, 0)]` |
| 1% | `[put(6, 0), s0 = snapshot(), put(6, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), release(s4), compact(), s5 = snapshot(), release(s5), read(s0, 6)]` |
| 1% | `[put(1, 0), s0 = snapshot(), put(1, 0), s1 = snapshot(), compact(), read(s0, 1)]` |
| 1% | `[put(3, 0), s0 = snapshot(), put(3, 0), s1 = snapshot(), release(s1), s2 = snapshot(), s3 = snapshot(), release(s3), compact(), s4 = snapshot(), read(s0, 3)]` |
| 1% | `[put(1, 0), s0 = snapshot(), put(1, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), read(s0, 1)]` |
| 1% | `[put(7, 0), s0 = snapshot(), put(7, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 7)]` |
| 1% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), s2 = snapshot(), release(s2), compact(), read(s0, 8)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), release(s3), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), release(s4), s5 = snapshot(), read(s0, 8)]` |
| 1% | `[put(4, 0), s0 = snapshot(), put(4, 0), s1 = snapshot(), release(s1), s2 = snapshot(), compact(), s3 = snapshot(), read(s0, 4)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), compact(), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(4, 0), s0 = snapshot(), put(4, 0), s1 = snapshot(), compact(), s2 = snapshot(), s3 = snapshot(), read(s0, 4)]` |
| 1% | `[put(5, 0), s0 = snapshot(), put(5, 0), s1 = snapshot(), release(s1), s2 = snapshot(), compact(), release(s2), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), release(s5), read(s0, 5)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), release(s3), s4 = snapshot(), s5 = snapshot(), compact(), release(s5), s6 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), s2 = snapshot(), release(s2), read(s0, 0)]` |
| 1% | `[put(9, 0), s0 = snapshot(), put(9, 0), s1 = snapshot(), s2 = snapshot(), release(s2), release(s1), s3 = snapshot(), s4 = snapshot(), release(s4), compact(), read(s0, 9)]` |
| 1% | `[put(2, 0), s0 = snapshot(), put(2, 0), s1 = snapshot(), release(s1), s2 = snapshot(), compact(), read(s0, 2)]` |
| 1% | `[put(5, 0), s0 = snapshot(), put(5, 0), s1 = snapshot(), compact(), read(s0, 5)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), release(s2), release(s1), read(s0, 0)]` |
| 1% | `[put(9, 0), s0 = snapshot(), put(9, 0), s1 = snapshot(), compact(), read(s0, 9)]` |
| 1% | `[put(3, 0), s0 = snapshot(), put(3, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 3)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 0)]` |
| 1% | `[put(5, 0), s0 = snapshot(), put(5, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), compact(), s4 = snapshot(), read(s0, 5)]` |
| 1% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), compact(), release(s1), read(s0, 8)]` |
| 1% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), release(s1), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), compact(), read(s0, 8)]` |
| 1% | `[put(7, 0), s0 = snapshot(), put(7, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 7)]` |
| 1% | `[put(6, 0), s0 = snapshot(), put(6, 0), s1 = snapshot(), compact(), read(s0, 6)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), release(s2), s3 = snapshot(), read(s0, 0)]` |
| 1% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), release(s3), compact(), read(s0, 0)]` |
| 1% | `[put(6, 0), s0 = snapshot(), put(6, 0), s1 = snapshot(), s2 = snapshot(), compact(), read(s0, 6)]` |
| 1% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), release(s1), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), release(s4), s5 = snapshot(), compact(), read(s0, 8)]` |

The minimal counterexample is `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`. Every step is needed: without either write the older snapshot has nothing to lose, without the second snapshot the newest and oldest live snapshots are the same, and without the compaction nothing is discarded. 51 of 100 runs reached it.

Every reduced counterexample keeps the same core structure. The rest differ in the key, or keep an extra `release` or `snapshot()`.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/snapshotStore.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 61.0 | 562.0 | 220.5 | 236.3 | 217.0–255.7 |
| Reduction time (ms) | 1.12 | 13.98 | 4.59 | 5.06 | 4.57–5.54 |
| Iterations to failure | 1.0 | 866.0 | 82.0 | 126.6 | 98.1–155.1 |

Iterations to failure counts generated command sequences.

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge snapshotStore --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
