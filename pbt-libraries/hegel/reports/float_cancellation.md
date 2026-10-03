# Float Cancellation

Hegel 0.48.1, native engine 0.44.1, release build. 100 seeded runs; [raw results](float_cancellation.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 552.2 |
| Original counterexample length | 43.4 |
| Total elapsed time (ms) | 3.71 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (32 distinct)

| Share | Counterexample |
|---|---|
| 33% | `(1.0, 524287.00000000006)` |
| 23% | `(1.0, 1.0000000000000002)` |
| 6% | `(1.0, 65535.00000000001)` |
| 3% | `(-0.7499999999997797, 65.0)` |
| 3% | `(1.0, 8191.000000000001)` |
| 2% | `(-0.7499904632568288, 65.0)` |
| 2% | `(-0.7499999996507611, 65.0)` |
| 2% | `(-0.7441406250000071, 65.0)` |
| 2% | `(-0.7499999999781792, 65.0)` |
| 2% | `(1.0, 32767.000000000004)` |
| 1% | `(-0.7499994039535451, 65.0)` |
| 1% | `(-0.7499999988358397, 65.0)` |
| 1% | `(-0.7109374999999929, 65.0)` |
| 1% | `(-0.7499809265136648, 65.0)` |
| 1% | `(1.0, 0.5000000000000001)` |
| 1% | `(-0.7304687499999929, 65.0)` |
| 1% | `(-0.7499985694885325, 65.0)` |
| 1% | `(-0.7499976158142019, 65.0)` |
| 1% | `(-0.7499999999997087, 65.0)` |
| 1% | `(1.0, 16383.000000000002)` |
| 1% | `(-0.7499999813735414, 65.0)` |
| 1% | `(-0.7499999850988459, 65.0)` |
| 1% | `(-0.7499999994179163, 65.0)` |
| 1% | `(-0.7499999998544737, 65.0)` |
| 1% | `(24.0, 40.50000000000001)` |
| 1% | `(-0.7499618530273366, 65.0)` |
| 1% | `(-0.7499999997089546, 65.0)` |
| 1% | `(-0.7499999999986429, 65.0)` |
| 1% | `(-0.7499999999998508, 65.0)` |
| 1% | `(-0.7499237060546804, 65.0)` |
| 1% | `(-0.7402343749999929, 65.0)` |
| 1% | `(60.0, 4.500000000000007)` |
