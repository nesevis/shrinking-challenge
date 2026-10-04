# Binary Heap

Hegel 0.48.1, native engine 0.44.1, debug build. 100 seeded runs; [raw results](binheap.json).

| Metric | Mean |
|---|---|
| Evaluations from first failure | 5837.4 |
| Original counterexample length | 312.2 |
| Total elapsed time (ms) | 700.81 |

Evaluations include the starting failure, subsequent property calls, confirmation calls and final replay. Rejected/overrun histories that never reach a property verdict are not counted. Total time includes generation, shrinking, recording and replay; phase timings are not exposed.

Original length uses the full counterexample notation, including the complete nested payload. Payloads below use run-length notation. 🎯 matches the reference counterexample in the main comparison.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 99% | 🎯 `(0, None, (0, (0, None, None), (1, None, None)))` |
| 1% | `(127, None, (55190086533789320, (401787435511877632, None, (7196582761221413107, None, None)), (7196582761221412864, (7196582761221413107, None, None), None)))` |
