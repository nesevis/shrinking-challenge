# Nested Flatmap (product sequence), depth 6

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](nested_flatmap_product_sequence_6.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 2273.6 |
| Original counterexample length | 3735.3 |
| Total elapsed time (ms) | 4716.38 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 63% | `(4, 3, 2, 1, 1, 1, 0x23 + 1x1)` |
| 15% | `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)` |
| 12% | `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)` |
| 8% | 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 1, 0x26 + 1x1)` |
