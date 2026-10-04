# Nested Flatmap (product), depth 5

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFiveProductBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 69.8 | 43.5 |
| Original input length | 15.2 | 15.0 |
| Wall time (ms) | 5.803 | 5.625 |
| Wall time, Linux/Windows build (ms) | 28.416 | 27.221 |
| generation (ms) | 0.007 | 0.007 |
| reductions (ms) | 5.740 | 5.560 |
| total (ms) | 5.794 | 5.616 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFiveProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2)` |

## Running

```sh
swift run ExhaustRunner --challenge depthFiveProductBind --iterations 100 --seed 1337 --report-path ../failures
```
