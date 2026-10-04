# Refund Allocation

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocation.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 902.8 | 648.0 |
| Original input length | 78.6 | 78.0 |
| Wall time (ms) | 9.587 | 6.915 |
| Wall time, Linux/Windows build (ms) | 20.530 | 16.107 |
| generation (ms) | 0.032 | 0.028 |
| reductions (ms) | 9.450 | 6.780 |
| total (ms) | 9.577 | 6.905 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/refundAllocation.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `RefundRequest([31, 33], 4)` |

## Running

```sh
swift run ExhaustRunner --challenge refundAllocation --iterations 100 --seed 1337 --report-path ../failures
```
