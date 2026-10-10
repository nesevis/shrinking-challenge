# Haystack

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/haystack.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 332.0 | 332.0 |
| Original input length | 480.0 | 480.0 |
| Wall time (ms) | 8.904 | 8.904 |
| Wall time, Linux/Windows build (ms) | 54.673 | 54.673 |
| reductions (ms) | 5.860 | 5.860 |
| total (ms) | 8.749 | 8.749 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/haystack.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"CREEPIDIOT"` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 18.73 | 18.73 | 18.73 |
| Source core / debug runner (on macOS) | 19.61 | 19.61 | 19.61 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge haystack --iterations 100 --seed 1337 --report-path ../failures
```
