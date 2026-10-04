# Branch Switching

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/branchSwitching.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 15.0 | 15.0 |
| Original input length | 17.0 | 17.0 |
| Wall time (ms) | 0.351 | 0.351 |
| Wall time, Linux/Windows build (ms) | 1.338 | 1.338 |
| reductions (ms) | 0.250 | 0.250 |
| total (ms) | 0.336 | 0.336 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/branchSwitching.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `"    "` |

## Running

```sh
swift run ExhaustRunner --challenge branchSwitching --iterations 100 --seed 1337 --report-path ../failures
```
