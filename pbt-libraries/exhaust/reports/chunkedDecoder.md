# Chunked Decoder

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/chunkedDecoder.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 86.5 | 80.5 |
| Original input length | 31.2 | 30.0 |
| Wall time (ms) | 1.113 | 1.016 |
| Wall time, Linux/Windows build (ms) | 3.192 | 3.018 |
| generation (ms) | 0.036 | 0.028 |
| reductions (ms) | 0.950 | 0.870 |
| total (ms) | 0.991 | 0.919 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/chunkedDecoder.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 57% | `(text, "\u{10000}", [3, 1])` |
| 39% | `(text, "\u{800}", [2, 1])` |
| 2% | 🎯 `(text, "\u{80}", [1, 1])` |
| 1% | `(text, "\u{10000}\u{800}", [6, 1])` |
| 1% | `(text, "\u{10000}\u{10000}", [7, 1])` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.87 | 15.86 | 16.08 |
| Source core / debug runner (on macOS) | 16.85 | 16.86 | 16.98 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge chunkedDecoder --iterations 100 --seed 1337 --report-path ../failures
```
