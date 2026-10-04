# Refund Allocation (derived)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocationDerived.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 9133.6 | 768.5 |
| Original input length | 55.6 | 53.0 |
| Wall time (ms) | 39.102 | 4.261 |
| Wall time, Linux/Windows build (ms) | 123.028 | 12.804 |
| generation (ms) | 0.144 | 0.087 |
| reductions (ms) | 38.840 | 4.050 |
| total (ms) | 39.091 | 4.251 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/refundAllocationDerived.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (6 distinct)

| Share | Counterexample |
|---|---|
| 32% | `RefundRequest([31, 31, 33], 3)` |
| 31% | 🎯 `RefundRequest([31, 33], 4)` |
| 28% | `RefundRequest([33, 31], 2)` |
| 5% | `RefundRequest([31, 34], 2)` |
| 3% | `RefundRequest([31, 31, 31, 33], 4)` |
| 1% | `RefundRequest([31, 33, 33], 4)` |

## Running

```sh
swift run ExhaustRunner --challenge refundAllocationDerived --iterations 100 --seed 1337 --report-path ../failures
```
