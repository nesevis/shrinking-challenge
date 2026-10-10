# Invoice Discount (derived)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscountDerived.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1182.5 | 728.5 |
| Original input length | 19.0 | 19.0 |
| Wall time (ms) | 2.675 | 2.183 |
| Wall time, Linux/Windows build (ms) | 13.384 | 9.727 |
| generation (ms) | 0.418 | 0.298 |
| reductions (ms) | 2.160 | 1.360 |
| total (ms) | 2.579 | 2.105 |

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

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.49 | 15.47 | 15.66 |
| Source core / debug runner (on macOS) | 16.48 | 16.48 | 16.69 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge invoiceDiscountDerived --iterations 100 --seed 1337 --report-path ../failures
```
