# Leap Day

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/leapDay.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 34.0 | 34.0 |
| Original input length | 25.0 | 25.0 |
| Wall time (ms) | 0.820 | 0.820 |
| Wall time, Linux/Windows build (ms) | 1.074 | 1.074 |
| reductions (ms) | 0.240 | 0.240 |
| total (ms) | 0.805 | 0.805 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/leapDay.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `2088-02-29 00:00:00 +0000` |

## Running

```sh
swift run ExhaustRunner --challenge leapDay --iterations 100 --seed 1337 --report-path ../failures
```
