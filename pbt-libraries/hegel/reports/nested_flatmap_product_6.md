# Nested Flatmap (product), depth 6

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](nested_flatmap_product_6.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 3596.3 |
| Original counterexample length | 18.2 |
| Total elapsed time (ms) | 22.73 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2, 1)` |
