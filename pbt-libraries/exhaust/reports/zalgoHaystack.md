# Zalgo Haystack

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/zalgoHaystack.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 465.0 | 465.0 |
| Original input length | 3237.0 | 3237.0 |
| Wall time (ms) | 14.795 | 14.795 |
| Wall time, Linux/Windows build (ms) | 106.039 | 106.039 |
| reductions (ms) | 11.080 | 11.080 |
| total (ms) | 14.614 | 14.614 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/zalgoHaystack.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"THE ICHOR PERMEATES"` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 22.78 | 22.78 | 22.78 |
| Source core / debug runner (on macOS) | 23.53 | 23.53 | 23.53 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge zalgoHaystack --iterations 100 --seed 1337 --report-path ../failures
```
