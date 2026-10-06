# Calculator

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/calculator.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 43.1 | 44.0 |
| Original input length | 63.7 | 58.5 |
| Wall time (ms) | 0.682 | 0.654 |
| Wall time, Linux/Windows build (ms) | 3.274 | 3.250 |
| generation (ms) | 0.046 | 0.037 |
| reductions (ms) | 0.540 | 0.540 |
| total (ms) | 0.671 | 0.644 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/calculator.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `('/', 0, ('+', 0, 0))` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.27 | 15.28 | 15.50 |
| Source core / debug runner (on macOS) | 16.53 | 16.55 | 16.78 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge calculator --iterations 100 --seed 1337 --report-path ../failures
```
