# Refund Allocation

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/refundAllocation.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 883.4 | 628.0 |
| Original input length | 78.6 | 78.0 |
| Wall time (ms) | 4.245 | 3.136 |
| generation (ms) | 0.013 | 0.012 |
| reductions (ms) | 4.140 | 3.040 |
| total (ms) | 4.237 | 3.128 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 98% | `RefundRequest([31, 34], 2)` |
| 2% | 🎯 `RefundRequest([31, 33], 4)` |

## Running

```sh
swift run -c release ExhaustRunner --challenge refundAllocation --iterations 100 --seed 1337 --report-path ../failures
```
