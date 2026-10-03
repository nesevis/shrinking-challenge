# Modular Mapping

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](modular_mapping.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 32.8 |
| Original counterexample length | 3.0 |
| Total elapsed time (ms) | 0.56 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (6 distinct)

| Share | Counterexample |
|---|---|
| 71% | 🎯 `925` |
| 14% | `926` |
| 6% | `927` |
| 6% | `905` |
| 2% | `930` |
| 1% | `901` |
