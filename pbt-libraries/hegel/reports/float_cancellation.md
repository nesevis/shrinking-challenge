# Float Cancellation

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](float_cancellation.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 562.5 |
| Original counterexample length | 43.5 |
| Total elapsed time (ms) | 3.63 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (31 distinct)

| Share | Counterexample |
|---|---|
| 26% | `(1.0, 524287.00000000006)` |
| 24% | `(1.0, 1.0000000000000002)` |
| 6% | `(1.0, 16383.000000000002)` |
| 6% | `(1.0, 65535.00000000001)` |
| 3% | `(-0.7499999996507611, 65.0)` |
| 3% | `(-0.7499999999954454, 65.0)` |
| 2% | `(1.0, 0.5000000000000001)` |
| 2% | `(-0.7499999999977192, 65.0)` |
| 2% | `(-0.7499999999997797, 65.0)` |
| 2% | `(1.0, 32767.000000000004)` |
| 2% | `(-0.7499999999986429, 65.0)` |
| 2% | `(-0.7499618530273366, 65.0)` |
| 2% | `(-0.7499976158142019, 65.0)` |
| 1% | `(-0.7499999999999929, 65.0)` |
| 1% | `(-0.7499999999781792, 65.0)` |
| 1% | `(-0.7499999999963691, 65.0)` |
| 1% | `(1.0, 0.12500000000000008)` |
| 1% | `(-0.7499999999999218, 65.0)` |
| 1% | `(-0.7304687499999929, 65.0)` |
| 1% | `(-0.7499999999998508, 65.0)` |
| 1% | `(-0.7499999994179163, 65.0)` |
| 1% | `(-0.7499809265136648, 65.0)` |
| 1% | `(-0.749999701976769, 65.0)` |
| 1% | `(-0.7499999906867671, 65.0)` |
| 1% | `(0.5, 0.03125000000000004)` |
| 1% | `(-0.749999999998856, 65.0)` |
| 1% | `(-0.74999999534338, 65.0)` |
| 1% | `(-0.7499237060546804, 65.0)` |
| 1% | `(1.0, 8191.000000000001)` |
| 1% | `(-0.7499999254941869, 65.0)` |
| 1% | `(-0.7499999944120717, 65.0)` |
