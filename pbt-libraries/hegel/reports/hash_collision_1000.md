# Hash Collision (M = 1000)

Hegel 0.49.14, native engine 0.45.13, debug build. 100 seeded runs; [raw results](hash_collision_1000.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 522.9 |
| Original counterexample length | 107.0 |
| Total elapsed time (ms) | 29.57 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `([(0, 0)], 1000, 1)` |
