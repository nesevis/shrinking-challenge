# Refund Allocation (derived)

Hegel 0.49.14, native engine 0.45.13, debug build. 100 seeded runs; [raw results](refund_allocation_derived.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 160.6 |
| Original counterexample length | 41.9 |
| Total elapsed time (ms) | 27.35 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (7 distinct)

| Share | Counterexample |
|---|---|
| 81% | `RefundRequest([31, 34], 2)` |
| 14% | 🎯 `RefundRequest([31, 33], 4)` |
| 1% | `RefundRequest([61, 5079374505385], 62852702378)` |
| 1% | `RefundRequest([93, 790301990554], 21244677169)` |
| 1% | `RefundRequest([31, 1736534408644545], 28008619494300)` |
| 1% | `RefundRequest([33, 31], 2)` |
| 1% | `RefundRequest([31, 599688524507359], 36738571086018)` |
