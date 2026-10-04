# Nested Flatmap (sum), depth 4

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourSumBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 734.4 | 530.5 |
| Original input length | 344.8 | 339.5 |
| Wall time (ms) | 18.932 | 14.282 |
| Wall time, Linux/Windows build (ms) | 205.388 | 120.497 |
| generation (ms) | 0.041 | 0.040 |
| reductions (ms) | 18.760 | 14.120 |
| total (ms) | 18.919 | 14.271 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourSumBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthFourSumBind --iterations 100 --seed 1337 --report-path ../failures
```
