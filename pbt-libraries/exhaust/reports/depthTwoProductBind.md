# Nested Flatmap (product), depth 2

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthTwoProductBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 32.3 | 35.0 |
| Original input length | 6.2 | 6.0 |
| Wall time (ms) | 0.226 | 0.240 |
| Wall time, Linux/Windows build (ms) | 0.855 | 0.891 |
| generation (ms) | 0.004 | 0.004 |
| reductions (ms) | 0.190 | 0.200 |
| total (ms) | 0.218 | 0.232 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthTwoProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(5, 5)` |

## Running

```sh
swift run ExhaustRunner --challenge depthTwoProductBind --iterations 100 --seed 1337 --report-path ../failures
```
