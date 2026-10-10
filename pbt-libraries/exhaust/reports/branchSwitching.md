# Branch Switching

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/branchSwitching.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 17.0 | 17.0 |
| Original input length | 17.0 | 17.0 |
| Wall time (ms) | 2.163 | 2.163 |
| Wall time, Linux/Windows build (ms) | 3.968 | 3.968 |
| reductions (ms) | 1.880 | 1.880 |
| total (ms) | 2.038 | 2.038 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/branchSwitching.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | `"    "` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.78 | 15.78 | 15.78 |
| Source core / debug runner (on macOS) | 16.86 | 16.86 | 16.86 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge branchSwitching --iterations 100 --seed 1337 --report-path ../failures
```
