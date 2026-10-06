# Chunked Decoder

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/chunkedDecoder.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 84.1 | 76.0 |
| Original input length | 31.2 | 30.0 |
| Wall time (ms) | 1.065 | 0.980 |
| Wall time, Linux/Windows build (ms) | 3.001 | 2.843 |
| generation (ms) | 0.034 | 0.027 |
| reductions (ms) | 0.930 | 0.850 |
| total (ms) | 1.053 | 0.968 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/chunkedDecoder.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 56% | `(text, "\u{10000}", [3, 1])` |
| 40% | `(text, "\u{800}", [2, 1])` |
| 2% | 🎯 `(text, "\u{80}", [1, 1])` |
| 1% | `(text, "\u{10000}\u{800}", [6, 1])` |
| 1% | `(text, "\u{10000}\u{10000}", [7, 1])` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.68 | 15.67 | 15.83 |
| Source core / debug runner (on macOS) | 16.90 | 16.91 | 17.00 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge chunkedDecoder --iterations 100 --seed 1337 --report-path ../failures
```
