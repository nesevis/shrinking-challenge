# Hash Collision (M = 10)

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](hash_collision_10.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 440.3 |
| Original counterexample length | 87.6 |
| Total elapsed time (ms) | 6.50 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `([(0, 0)], 10, 1)` |
