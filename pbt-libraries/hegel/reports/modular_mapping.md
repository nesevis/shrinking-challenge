# Modular Mapping

Hegel 0.49.14, native engine 0.45.13, debug build. 100 seeded runs; [raw results](modular_mapping.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 32.9 |
| Original counterexample length | 3.0 |
| Total elapsed time (ms) | 1.06 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 82% | 🎯 `925` |
| 14% | `926` |
| 2% | `905` |
| 1% | `901` |
| 1% | `930` |
