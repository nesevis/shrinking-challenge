# Distinct Sum

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/distinctSum.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 636.0 | 636.0 |
| Original input length | 36.0 | 36.0 |
| Wall time (ms) | 1.825 | 1.825 |
| Wall time, Linux/Windows build (ms) | 6.337 | 6.337 |
| reductions (ms) | 1.770 | 1.770 |
| total (ms) | 1.810 | 1.810 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/distinctSum.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `[-2, -1, 0, 1, 53]` |

## Running

```sh
swift run ExhaustRunner --challenge distinctSum --iterations 100 --seed 1337 --report-path ../failures
```
