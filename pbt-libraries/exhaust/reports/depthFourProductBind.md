# Nested Flatmap (product), depth 4

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourProductBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 72.5 | 81.5 |
| Original input length | 12.2 | 12.0 |
| Wall time (ms) | 2.165 | 2.355 |
| Wall time, Linux/Windows build (ms) | 10.193 | 11.069 |
| generation (ms) | 0.006 | 0.005 |
| reductions (ms) | 2.110 | 2.300 |
| total (ms) | 2.156 | 2.345 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(3, 2, 2, 2)` |

## Running

```sh
swift run ExhaustRunner --challenge depthFourProductBind --iterations 100 --seed 1337 --report-path ../failures
```
