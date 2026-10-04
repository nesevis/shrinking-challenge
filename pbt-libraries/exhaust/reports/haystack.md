# Haystack

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/haystack.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 407.0 | 407.0 |
| Original input length | 480.0 | 480.0 |
| Wall time (ms) | 8.828 | 8.828 |
| Wall time, Linux/Windows build (ms) | 60.167 | 60.167 |
| reductions (ms) | 6.870 | 6.870 |
| total (ms) | 8.804 | 8.804 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/haystack.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"CREEPIDIOT"` |

## Running

```sh
swift run ExhaustRunner --challenge haystack --iterations 100 --seed 1337 --report-path ../failures
```
