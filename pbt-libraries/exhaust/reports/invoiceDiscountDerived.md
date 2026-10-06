# Invoice Discount (derived)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscountDerived.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1219.5 | 768.5 |
| Original input length | 19.0 | 19.0 |
| Wall time (ms) | 2.659 | 2.184 |
| Wall time, Linux/Windows build (ms) | 11.077 | 8.033 |
| generation (ms) | 0.429 | 0.307 |
| reductions (ms) | 2.150 | 1.280 |
| total (ms) | 2.648 | 2.174 |

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
| macOS XCFramework / debug runner | 15.23 | 15.23 | 15.39 |
| Source core / debug runner (on macOS) | 16.36 | 16.37 | 16.56 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge invoiceDiscountDerived --iterations 100 --seed 1337 --report-path ../failures
```
