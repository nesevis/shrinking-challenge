# Nested Flatmap (product), depth 6

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthSixProductBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 30.5 | 31.0 |
| Original input length | 18.2 | 18.0 |
| Wall time (ms) | 13.071 | 13.338 |
| Wall time, Linux/Windows build (ms) | 67.172 | 68.354 |
| generation (ms) | 0.008 | 0.007 |
| reductions (ms) | 13.000 | 13.260 |
| total (ms) | 13.062 | 13.327 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthSixProductBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(2, 2, 2, 2, 2, 1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthSixProductBind --iterations 100 --seed 1337 --report-path ../failures
```
