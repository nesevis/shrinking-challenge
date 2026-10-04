# Nested Flatmap (product), depth 5

Hegel 0.48.1, native engine 0.44.1, debug build. 100 seeded runs; [raw results](nested_flatmap_product_5.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 4239.9 |
| Original counterexample length | 15.2 |
| Total elapsed time (ms) | 47.21 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2)` |
