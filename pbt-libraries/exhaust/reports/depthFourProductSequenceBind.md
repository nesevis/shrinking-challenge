# Nested Flatmap (product sequence), depth 4

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductSequenceBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 304.6 | 213.0 |
| Original input length | 1107.9 | 374.5 |
| Wall time (ms) | 44.440 | 9.695 |
| Wall time, Linux/Windows build (ms) | 301.598 | 72.513 |
| generation (ms) | 0.103 | 0.040 |
| reductions (ms) | 44.210 | 9.500 |
| total (ms) | 44.429 | 9.686 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 89% | 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
| 9% | `(3, 3, 3, 1, 0x26 + 1x1)` |
| 1% | `(9, 3, 1, 1, 0x26 + 1x1)` |
| 1% | `(7, 2, 2, 1, 0x27 + 1x1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthFourProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
