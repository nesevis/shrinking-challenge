# Nested Flatmap (product sequence), depth 5

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductSequenceBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 707.0 | 165.5 |
| Original input length | 3737.7 | 398.0 |
| Wall time (ms) | 985.337 | 32.883 |
| Wall time, Linux/Windows build (ms) | 4306.575 | 233.929 |
| generation (ms) | 0.326 | 0.050 |
| reductions (ms) | 984.840 | 32.720 |
| total (ms) | 985.320 | 32.871 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFiveProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (11 distinct)

| Share | Counterexample |
|---|---|
| 85% | 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 0x26 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 0x41 + 1x1)` |
| 1% | `(6, 5, 2, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 0x27 + 1x1)` |
| 1% | `(9, 7, 2, 1, 1, 0x125 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 0x55 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 0x55 + 1x1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthFiveProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
