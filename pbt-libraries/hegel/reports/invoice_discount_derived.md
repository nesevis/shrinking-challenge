# Invoice Discount (derived)

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](invoice_discount_derived.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 482.8 |
| Original counterexample length | 18.9 |
| Total elapsed time (ms) | 5.44 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (9 distinct)

| Share | Counterexample |
|---|---|
| 36% | 🎯 `Invoice(10, 100, 1)` |
| 28% | `Invoice(18, 56, 1)` |
| 27% | `Invoice(14, 72, 1)` |
| 3% | `Invoice(16, 63, 1)` |
| 2% | `Invoice(19, 53, 1)` |
| 1% | `Invoice(13, 77, 1)` |
| 1% | `Invoice(11, 91, 1)` |
| 1% | `Invoice(17, 59, 1)` |
| 1% | `Invoice(12, 84, 1)` |
