# Nested Flatmap (product sequence), depth 6

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthSixProductSequenceBind.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1055.9 | 145.0 |
| Original input length | 5867.6 | 422.5 |
| Wall time (ms) | 2044.170 | 128.902 |
| Wall time, Linux/Windows build (ms) | 6775.176 | 927.239 |
| generation (ms) | 0.500 | 0.052 |
| reductions (ms) | 2043.410 | 128.360 |
| total (ms) | 2044.147 | 128.882 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthSixProductSequenceBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (27 distinct)

| Share | Counterexample |
|---|---|
| 56% | `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)` |
| 4% | `(6, 5, 2, 2, 1, 1, 0x119 + 1x1)` |
| 4% | `(6, 5, 1, 1, 1, 1, 0x29 + 1x1)` |
| 4% | `(4, 3, 3, 1, 1, 1, 0x35 + 1x1)` |
| 3% | `(6, 4, 3, 1, 1, 1, 0x71 + 1x1)` |
| 3% | `(5, 5, 5, 1, 1, 1, 0x124 + 1x1)` |
| 2% | `(4, 2, 2, 2, 1, 1, 0x31 + 1x1)` |
| 2% | `(3, 3, 3, 1, 1, 1, 0x26 + 1x1)` |
| 2% | `(3, 3, 3, 2, 1, 1, 0x53 + 1x1)` |
| 2% | `(7, 3, 2, 1, 1, 1, 0x41 + 1x1)` |
| 2% | `(8, 5, 2, 2, 1, 1, 0x159 + 1x1)` |
| 1% | `(6, 5, 2, 1, 1, 1, 0x59 + 1x1)` |
| 1% | `(7, 3, 2, 2, 1, 1, 0x83 + 1x1)` |
| 1% | `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)` |
| 1% | `(8, 7, 2, 2, 1, 1, 0x223 + 1x1)` |
| 1% | `(5, 3, 3, 1, 1, 1, 0x44 + 1x1)` |
| 1% | `(5, 2, 2, 2, 1, 1, 0x39 + 1x1)` |
| 1% | `(6, 5, 3, 1, 1, 1, 0x89 + 1x1)` |
| 1% | `(7, 4, 2, 2, 1, 1, 0x111 + 1x1)` |
| 1% | `(7, 2, 2, 1, 1, 1, 0x27 + 1x1)` |
| 1% | `(9, 7, 2, 1, 1, 1, 0x125 + 1x1)` |
| 1% | `(10, 7, 2, 1, 1, 1, 0x139 + 1x1)` |
| 1% | `(6, 3, 2, 2, 2, 1, 0x143 + 1x1)` |
| 1% | `(4, 3, 2, 2, 1, 1, 0x47 + 1x1)` |
| 1% | `(7, 2, 2, 2, 1, 1, 0x55 + 1x1)` |
| 1% | `(7, 2, 2, 2, 2, 1, 0x111 + 1x1)` |
| 1% | `(8, 7, 1, 1, 1, 1, 0x55 + 1x1)` |

## Running

```sh
swift run ExhaustRunner --challenge depthSixProductSequenceBind --iterations 100 --seed 1337 --report-path ../failures
```
