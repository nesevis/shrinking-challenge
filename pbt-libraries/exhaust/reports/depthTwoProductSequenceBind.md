# Nested Flatmap (product sequence), depth 2

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductSequenceBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 310.8 | 327.5 |
| Original input length | 141.0 | 122.0 |
| Wall time (ms) | 3.242 | 3.356 |
| Wall time, Linux/Windows build (ms) | 38.819 | 39.731 |
| generation (ms) | 0.020 | 0.018 |
| reductions (ms) | 3.120 | 3.230 |
| total (ms) | 3.231 | 3.346 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthTwoProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 99% | 🎯 `(6, 4, 0x23 + 1x1)` |
| 1% | `(9, 3, 0x26 + 1x1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthTwoProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
