# Nested Flatmap (product sequence), depth 3

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](nested_flatmap_product_sequence_3.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 1740.1 |
| Original counterexample length | 410.6 |
| Total elapsed time (ms) | 107.11 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 84% | 🎯 `(4, 3, 2, 0x23 + 1x1)` |
| 16% | `(8, 3, 1, 0x23 + 1x1)` |
