# Invoice Discount

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscount.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 90.4 | 82.0 |
| Original input length | 19.7 | 20.0 |
| Wall time (ms) | 1.670 | 1.627 |
| Wall time, Linux/Windows build (ms) | 5.900 | 5.755 |
| generation (ms) | 0.005 | 0.005 |
| reductions (ms) | 1.590 | 1.560 |
| total (ms) | 1.659 | 1.617 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/invoiceDiscount.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `Invoice(10, 100, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.04 | 15.03 | 15.14 |
| Source core / debug runner (on macOS) | 16.27 | 16.28 | 16.38 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge invoiceDiscount --iterations 100 --seed 1337 --report-path ../failures
```
