# Duplicated Text

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/duplicatedText.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 54.0 | 54.0 |
| Original input length | 24.0 | 24.0 |
| Wall time (ms) | 0.418 | 0.418 |
| Wall time, Linux/Windows build (ms) | 2.222 | 2.222 |
| reductions (ms) | 0.370 | 0.370 |
| total (ms) | 0.406 | 0.406 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/duplicatedText.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `("10210210", "10210210")` |

## Running

```sh
swift run ExhaustRunner --challenge duplicatedText --iterations 100 --seed 1337 --report-path ../failures
```
