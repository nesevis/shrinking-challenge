# Invoice Discount

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscount.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 90.4 | 82.0 |
| Original input length | 19.7 | 20.0 |
| Wall time (ms) | 1.534 | 1.509 |
| Wall time, Linux/Windows build (ms) | 5.540 | 5.442 |
| generation (ms) | 0.005 | 0.004 |
| reductions (ms) | 1.470 | 1.440 |
| total (ms) | 1.525 | 1.500 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/invoiceDiscount.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `Invoice(10, 100, 1)` |

## Running

```sh
swift run ExhaustRunner --challenge invoiceDiscount --iterations 100 --seed 1337 --report-path ../failures
```
