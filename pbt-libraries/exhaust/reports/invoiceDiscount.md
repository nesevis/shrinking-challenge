# Invoice Discount

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/invoiceDiscount.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 90.4 | 82.0 |
| Original input length | 19.7 | 20.0 |
| Wall time (ms) | 1.673 | 1.632 |
| Wall time, Linux/Windows build (ms) | 7.909 | 7.764 |
| generation (ms) | 0.005 | 0.005 |
| reductions (ms) | 1.580 | 1.550 |
| total (ms) | 1.583 | 1.557 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/invoiceDiscount.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `Invoice(10, 100, 1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.33 | 15.33 | 15.45 |
| Source core / debug runner (on macOS) | 16.35 | 16.36 | 16.45 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge invoiceDiscount --iterations 100 --seed 1337 --report-path ../failures
```
