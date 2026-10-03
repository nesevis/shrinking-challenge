# Refund Allocation

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](refund_allocation.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 1498.0 |
| Original counterexample length | 60.8 |
| Total elapsed time (ms) | 119.66 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 96% | 🎯 `RefundRequest([31, 33], 4)` |
| 1% | `RefundRequest([31, 36], 3)` |
| 1% | `RefundRequest([31, 35183], 2386)` |
| 1% | `RefundRequest([31, 18896645105], 316274154)` |
| 1% | `RefundRequest([31, 572178641182401], 9228687761060)` |
