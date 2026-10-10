# Refund Allocation (derived)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocationDerived.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 9133.6 | 768.5 |
| Original input length | 55.6 | 53.0 |
| Wall time (ms) | 40.613 | 4.354 |
| Wall time, Linux/Windows build (ms) | 135.786 | 14.569 |
| generation (ms) | 0.158 | 0.095 |
| reductions (ms) | 40.270 | 4.130 |
| total (ms) | 40.430 | 4.237 |

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

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.99 | 15.77 | 23.94 |
| Source core / debug runner (on macOS) | 17.06 | 16.83 | 25.16 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge refundAllocationDerived --iterations 100 --seed 1337 --report-path ../failures
```
