# Invoice Discount (derived)

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](invoice_discount_derived.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 459.8 |
| Original counterexample length | 18.8 |
| Total elapsed time (ms) | 5.73 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (8 distinct)

| Share | Counterexample |
|---|---|
| 29% | `Invoice(18, 56, 1)` |
| 28% | 🎯 `Invoice(10, 100, 1)` |
| 27% | `Invoice(14, 72, 1)` |
| 10% | `Invoice(16, 63, 1)` |
| 3% | `Invoice(13, 77, 1)` |
| 1% | `Invoice(19, 53, 1)` |
| 1% | `Invoice(12, 84, 1)` |
| 1% | `Invoice(15, 67, 1)` |
