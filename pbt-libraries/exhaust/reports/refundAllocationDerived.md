# Refund Allocation (derived)

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocationDerived.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 9133.6 | 768.5 |
| Original input length | 55.6 | 53.0 |
| Wall time (ms) | 31.350 | 3.349 |
| generation (ms) | 0.122 | 0.071 |
| reductions (ms) | 31.110 | 3.130 |
| total (ms) | 31.338 | 3.338 |

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

## Running

```sh
swift run -c release ExhaustRunner --challenge refundAllocationDerived --iterations 100 --seed 1337 --report-path ../failures
```
