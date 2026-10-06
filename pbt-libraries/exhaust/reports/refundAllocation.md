# Refund Allocation

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocation.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 902.8 | 648.0 |
| Original input length | 78.6 | 78.0 |
| Wall time (ms) | 10.135 | 7.268 |
| Wall time, Linux/Windows build (ms) | 22.158 | 17.252 |
| generation (ms) | 0.035 | 0.031 |
| reductions (ms) | 9.950 | 7.140 |
| total (ms) | 10.116 | 7.256 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/refundAllocation.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `RefundRequest([31, 33], 4)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.35 | 15.34 | 15.77 |
| Source core / debug runner (on macOS) | 16.41 | 16.41 | 16.88 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge refundAllocation --iterations 100 --seed 1337 --report-path ../failures
```
