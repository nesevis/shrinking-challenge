# Nested Flatmap (product sequence), depth 3

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductSequenceBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 299.3 | 290.0 |
| Original input length | 386.3 | 252.5 |
| Wall time (ms) | 6.063 | 4.949 |
| Wall time, Linux/Windows build (ms) | 64.500 | 57.258 |
| generation (ms) | 0.041 | 0.030 |
| reductions (ms) | 5.910 | 4.800 |
| total (ms) | 6.052 | 4.938 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthThreeProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (4 distinct)

| Share | Counterexample |
|---|---|
| 80% | 🎯 `(4, 3, 2, 0x23 + 1x1)` |
| 16% | `(6, 2, 2, 0x23 + 1x1)` |
| 3% | `(7, 2, 2, 0x27 + 1x1)` |
| 1% | `(9, 3, 1, 0x26 + 1x1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthThreeProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
