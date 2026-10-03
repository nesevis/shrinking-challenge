# Nested Flatmap (product sequence), depth 4

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](nested_flatmap_product_sequence_4.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 1842.7 |
| Original counterexample length | 1074.1 |
| Total elapsed time (ms) | 200.33 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (3 distinct)

| Share | Counterexample |
|---|---|
| 68% | `(4, 3, 2, 1, 0x23 + 1x1)` |
| 16% | `(8, 3, 1, 1, 0x23 + 1x1)` |
| 16% | 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
