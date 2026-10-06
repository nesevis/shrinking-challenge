# Nested Flatmap (sum), depth 4

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/depthFourSumBind.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 734.4 | 530.5 |
| Original input length | 344.8 | 339.5 |
| Wall time (ms) | 19.947 | 15.071 |
| Wall time, Linux/Windows build (ms) | 217.132 | 130.159 |
| generation (ms) | 0.047 | 0.047 |
| reductions (ms) | 19.730 | 14.870 |
| total (ms) | 19.925 | 15.054 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/depthFourSumBind.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 17.51 | 17.22 | 20.16 |
| Source core / debug runner (on macOS) | 18.75 | 18.38 | 21.41 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge depthFourSumBind --iterations 100 --seed 1337 --report-path ../failures
```
