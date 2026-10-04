# Calculator

Hegel 0.48.1, native engine 0.44.1, debug build. 100 seeded runs; [raw results](calculator.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 442.5 |
| Original counterexample length | 241.9 |
| Total elapsed time (ms) | 194.23 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `('/', 0, ('+', 0, 0))` |
