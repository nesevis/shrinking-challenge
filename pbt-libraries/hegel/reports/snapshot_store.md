# Snapshot Store

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](snapshot_store.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 1926.7 |
| Original counterexample length | 484.8 |
| Total elapsed time (ms) | 513.02 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (3 distinct)

| Share | Counterexample |
|---|---|
| 79% | 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 15% | `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]` |
| 6% | `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
