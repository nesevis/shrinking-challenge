# Calculator

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/calculator.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 43.1 | 44.0 |
| Original input length | 63.7 | 58.5 |
| Wall time (ms) | 0.647 | 0.626 |
| Wall time, Linux/Windows build (ms) | 3.608 | 3.591 |
| generation (ms) | 0.046 | 0.039 |
| reductions (ms) | 0.490 | 0.480 |
| total (ms) | 0.537 | 0.529 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/calculator.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `('/', 0, ('+', 0, 0))` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.54 | 15.53 | 15.72 |
| Source core / debug runner (on macOS) | 16.52 | 16.53 | 16.78 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge calculator --iterations 100 --seed 1337 --report-path ../failures
```
