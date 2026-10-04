# Nested Flatmap (product sequence), depth 5

Hegel 0.48.1, native engine 0.44.1, debug build. 100 seeded runs; [raw results](nested_flatmap_product_sequence_5.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 1884.8 |
| Original counterexample length | 2049.6 |
| Total elapsed time (ms) | 1510.60 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 65% | `(4, 3, 2, 1, 1, 0x23 + 1x1)` |
| 15% | `(8, 3, 1, 1, 1, 0x23 + 1x1)` |
| 12% | `(2, 2, 2, 2, 2, 0x31 + 1x1)` |
| 8% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
