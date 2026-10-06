# Refund Allocation (derived)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocationDerived.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 9133.6 | 768.5 |
| Original input length | 55.6 | 53.0 |
| Wall time (ms) | 41.914 | 4.767 |
| Wall time, Linux/Windows build (ms) | 129.203 | 13.717 |
| generation (ms) | 0.160 | 0.094 |
| reductions (ms) | 41.570 | 4.440 |
| total (ms) | 41.892 | 4.750 |

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
| macOS XCFramework / debug runner | 15.79 | 15.53 | 24.03 |
| Source core / debug runner (on macOS) | 17.01 | 16.76 | 25.17 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge refundAllocationDerived --iterations 100 --seed 1337 --report-path ../failures
```
