# Zalgo Haystack

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/zalgoHaystack.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 461.0 | 461.0 |
| Original input length | 3237.0 | 3237.0 |
| Wall time (ms) | 16.748 | 16.748 |
| Wall time, Linux/Windows build (ms) | 110.073 | 110.073 |
| reductions (ms) | 12.820 | 12.820 |
| total (ms) | 16.577 | 16.577 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/zalgoHaystack.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `"THE ICHOR PERMEATES"` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 22.70 | 22.70 | 22.70 |
| Source core / debug runner (on macOS) | 23.83 | 23.83 | 23.83 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge zalgoHaystack --iterations 100 --seed 1337 --report-path ../failures
```
