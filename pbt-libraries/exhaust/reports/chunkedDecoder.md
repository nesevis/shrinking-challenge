# Chunked Decoder

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/chunkedDecoder.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 84.1 | 76.0 |
| Original input length | 31.2 | 30.0 |
| Wall time (ms) | 0.928 | 0.855 |
| Wall time, Linux/Windows build (ms) | 2.732 | 2.611 |
| generation (ms) | 0.030 | 0.025 |
| reductions (ms) | 0.820 | 0.750 |
| total (ms) | 0.919 | 0.846 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/chunkedDecoder.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 56% | `(text, "\u{10000}", [3, 1])` |
| 40% | `(text, "\u{800}", [2, 1])` |
| 2% | 🎯 `(text, "\u{80}", [1, 1])` |
| 1% | `(text, "\u{10000}\u{800}", [6, 1])` |
| 1% | `(text, "\u{10000}\u{10000}", [7, 1])` |

## Running

```sh
swift run ExhaustRunner --challenge chunkedDecoder --iterations 100 --seed 1337 --report-path ../failures
```
