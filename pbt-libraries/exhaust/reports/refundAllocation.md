# Refund Allocation

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocation.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 902.9 | 648.0 |
| Original input length | 78.6 | 78.0 |
| Wall time (ms) | 10.414 | 7.572 |
| Wall time, Linux/Windows build (ms) | 24.185 | 19.075 |
| generation (ms) | 0.037 | 0.033 |
| reductions (ms) | 10.210 | 7.380 |
| total (ms) | 10.244 | 7.426 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/refundAllocation.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `RefundRequest([31, 33], 4)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.61 | 15.61 | 15.86 |
| Source core / debug runner (on macOS) | 16.52 | 16.52 | 16.78 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge refundAllocation --iterations 100 --seed 1337 --report-path ../failures
```
