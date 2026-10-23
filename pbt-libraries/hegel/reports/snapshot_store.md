# Snapshot Store

Hegel 0.49.14, native engine 0.45.13, debug build. 100 seeded runs; [raw results](snapshot_store.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 2147.5 |
| Original counterexample length | 484.9 |
| Total elapsed time (ms) | 995.72 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 75% | 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]` |
| 16% | `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]` |
| 8% | `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
| 1% | `[s0 = snapshot(), s1 = snapshot(), s2 = snapshot(), put(0, 0), s3 = snapshot(), put(0, 0), s4 = snapshot(), compact(), read(s3, 0)]` |
