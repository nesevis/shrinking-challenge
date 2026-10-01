# Snapshot Store Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

A state machine challenge. The system under test is a versioned key-value store with `put`, `get`, `snapshot`, `read` (through a snapshot), `release` and `compact`. A snapshot sees the store as it was when it was taken, and compaction may discard any version no live snapshot can see. The model never compacts: it keeps every write, and each snapshot remembers how many writes it can see. The deliberate bug makes compaction keep history back to the newest live snapshot when it should keep it back to the oldest, so it only shows up with two live snapshots. Keys and values are drawn from `0...9`, and commands refer to snapshots by an index into the live snapshots, wrapped with `%`.

The spec runs with `mode: .sequential` and `.commandLimit(50)`, matching Hypothesis's default `stateful_step_count`, so both libraries generate histories of up to 50 commands. Counterexamples list the commands that ran, naming snapshots `s0`, `s1`, … in creation order.

## Normalization

Exhaust produced 10 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 85% | `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 2% | `[put(9, 0), s0 = snapshot(), put(9, 0), s1 = snapshot(), compact(), read(s0, 9)]` |
| 2% | `[put(2, 0), s0 = snapshot(), put(2, 0), s1 = snapshot(), compact(), read(s0, 2)]` |
| 2% | `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), release(s0), read(s1, 0)]` |
| 2% | `[put(1, 0), s0 = snapshot(), put(1, 0), s1 = snapshot(), compact(), read(s0, 1)]` |
| 2% | `[put(8, 0), s0 = snapshot(), put(8, 0), s1 = snapshot(), compact(), read(s0, 8)]` |
| 2% | `[put(6, 0), s0 = snapshot(), put(6, 0), s1 = snapshot(), compact(), read(s0, 6)]` |
| 1% | `[put(7, 0), s0 = snapshot(), put(7, 0), s1 = snapshot(), compact(), read(s0, 7)]` |
| 1% | `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), release(s0), compact(), read(s1, 0)]` |
| 1% | `[s0 = snapshot(), put(6, 0), s1 = snapshot(), put(6, 0), s2 = snapshot(), compact(), read(s1, 6)]` |

The minimal counterexample is `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`. Every step is needed: without either write the older snapshot has nothing to lose, without the second snapshot the newest and oldest live snapshots are the same, and without the compaction nothing is discarded. 85 of 100 runs reached it.

The first failing histories have a median of 40 commands. Every reduced counterexample has the same core structure; the rest differ only in the key, or keep an extra leading snapshot.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/snapshotStore.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 92.0 | 515.0 | 202.0 | 220.1 | 202.9–237.2 |
| Reduction time (ms) | 1.46 | 12.04 | 4.18 | 4.72 | 4.3–5.13 |
| Iterations to failure | 1.0 | 678.0 | 111.5 | 144.3 | 118.3–170.4 |

Iterations to failure counts generated command sequences.

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge snapshotStore --iterations 100`

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
