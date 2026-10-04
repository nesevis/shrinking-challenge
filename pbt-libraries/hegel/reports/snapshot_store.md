# Snapshot Store

Hegel 0.48.1, native engine 0.44.1, debug build. 100 seeded runs; [raw results](snapshot_store.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 2268.7 |
| Original counterexample length | 484.9 |
| Total elapsed time (ms) | 1010.38 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 71% | 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 17% | `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]` |
| 10% | `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
| 1% | `[s0 = snapshot(), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), put(0, 0), s5 = snapshot(), put(0, 0), s6 = snapshot(), compact(), read(s5, 0)]` |
| 1% | `[s0 = snapshot(), s1 = snapshot(), s2 = snapshot(), s3 = snapshot(), s4 = snapshot(), s5 = snapshot(), s6 = snapshot(), put(0, 0), s7 = snapshot(), put(0, 0), s8 = snapshot(), compact(), read(s7, 0)]` |
