# Zalgo Haystack

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/zalgoHaystack.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 461.0 | 461.0 |
| Original input length | 3237.0 | 3237.0 |
| Wall time (ms) | 14.895 | 14.895 |
| Wall time, Linux/Windows build (ms) | 101.679 | 101.679 |
| reductions (ms) | 11.470 | 11.470 |
| total (ms) | 14.838 | 14.838 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/zalgoHaystack.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"THE ICHOR PERMEATES"` |

## Running

```sh
swift run ExhaustRunner --challenge zalgoHaystack --iterations 100 --seed 1337 --report-path ../failures
```
