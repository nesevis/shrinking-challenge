# Weighted Linear Preservation

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/weightedLinearPreservation.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 154.4 | 93.0 |
| Original input length | 9.6 | 10.0 |
| Wall time (ms) | 0.439 | 0.345 |
| Wall time, Linux/Windows build (ms) | 1.895 | 1.310 |
| generation (ms) | 0.036 | 0.024 |
| reductions (ms) | 0.360 | 0.230 |
| total (ms) | 0.430 | 0.337 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/weightedLinearPreservation.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(0, 0, 20)` |

## Running

```sh
swift run ExhaustRunner --challenge weightedLinearPreservation --iterations 100 --seed 1337 --report-path ../failures
```
