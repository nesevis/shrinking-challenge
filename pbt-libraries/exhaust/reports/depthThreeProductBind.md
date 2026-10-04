# Nested Flatmap (product), depth 3

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthThreeProductBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 58.1 | 63.0 |
| Original input length | 9.2 | 9.0 |
| Wall time (ms) | 0.818 | 0.970 |
| Wall time, Linux/Windows build (ms) | 3.626 | 4.379 |
| generation (ms) | 0.005 | 0.004 |
| reductions (ms) | 0.770 | 0.920 |
| total (ms) | 0.809 | 0.962 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthThreeProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 3, 3)` |

## Running

```sh
swift run ExhaustRunner --challenge depthThreeProductBind --iterations 100 --seed 1337 --report-path ../failures
```
