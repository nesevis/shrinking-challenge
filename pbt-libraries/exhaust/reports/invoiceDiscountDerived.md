# Invoice Discount (derived)

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscountDerived.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1219.5 | 768.5 |
| Original input length | 19.0 | 19.0 |
| Wall time (ms) | 2.436 | 2.019 |
| Wall time, Linux/Windows build (ms) | 10.109 | 7.507 |
| generation (ms) | 0.401 | 0.288 |
| reductions (ms) | 1.970 | 1.180 |
| total (ms) | 2.427 | 2.010 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/invoiceDiscountDerived.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 69% | `Invoice(15, 67, 1)` |
| 12% | `Invoice(14, 72, 1)` |
| 8% | `Invoice(13, 77, 1)` |
| 6% | `Invoice(12, 84, 1)` |
| 5% | `Invoice(11, 91, 1)` |

## Running

```sh
swift run ExhaustRunner --challenge invoiceDiscountDerived --iterations 100 --seed 1337 --report-path ../failures
```
