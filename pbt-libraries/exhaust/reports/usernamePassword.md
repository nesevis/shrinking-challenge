# Username and Password

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/usernamePassword.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 731.0 | 731.0 |
| Original input length | 30.0 | 30.0 |
| Wall time (ms) | 3.235 | 3.235 |
| Wall time, Linux/Windows build (ms) | 18.021 | 18.021 |
| reductions (ms) | 3.180 | 3.180 |
| total (ms) | 3.221 | 3.221 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/usernamePassword.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `("u: 0000", "p: 0000")` |

## Running

```sh
swift run ExhaustRunner --challenge usernamePassword --iterations 100 --seed 1337 --report-path ../failures
```
