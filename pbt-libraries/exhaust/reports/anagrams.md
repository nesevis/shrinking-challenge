# Anagrams

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/anagrams.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1239.0 | 1239.0 |
| Original input length | 62.0 | 62.0 |
| Wall time (ms) | 22.960 | 22.960 |
| Wall time, Linux/Windows build (ms) | 66.754 | 66.754 |
| reductions (ms) | 22.620 | 22.620 |
| total (ms) | 22.827 | 22.827 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/anagrams.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(" \0", "\0 ")` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.59 | 15.59 | 15.59 |
| Source core / debug runner (on macOS) | 16.81 | 16.81 | 16.81 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge anagrams --iterations 100 --seed 1337 --report-path ../failures
```
