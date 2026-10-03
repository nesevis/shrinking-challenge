# Refund Allocation (derived)

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](refund_allocation_derived.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 168.3 |
| Original counterexample length | 42.6 |
| Total elapsed time (ms) | 16.07 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (7 distinct)

| Share | Counterexample |
|---|---|
| 80% | `RefundRequest([31, 34], 2)` |
| 15% | 🎯 `RefundRequest([31, 33], 4)` |
| 1% | `RefundRequest([61, 5079374505385], 62852702378)` |
| 1% | `RefundRequest([93, 790301990554], 21244677169)` |
| 1% | `RefundRequest([31, 1736534408644545], 28008619494300)` |
| 1% | `RefundRequest([33, 31], 2)` |
| 1% | `RefundRequest([31, 599688524507359], 36738571086018)` |
