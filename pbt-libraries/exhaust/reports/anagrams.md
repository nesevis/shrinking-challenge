# Anagrams

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/anagrams.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1285.0 | 1285.0 |
| Original input length | 62.0 | 62.0 |
| Wall time (ms) | 24.643 | 24.643 |
| Wall time, Linux/Windows build (ms) | 82.533 | 82.533 |
| reductions (ms) | 24.320 | 24.320 |
| total (ms) | 24.506 | 24.506 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/anagrams.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(" \0", "\0 ")` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.64 | 15.64 | 15.64 |
| Source core / debug runner (on macOS) | 16.73 | 16.73 | 16.73 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge anagrams --iterations 100 --seed 1337 --report-path ../failures
```
