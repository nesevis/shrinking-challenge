# Binary Heap

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/binaryHeap.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 117.9 | 94.5 |
| Original input length | 384.4 | 352.0 |
| Wall time (ms) | 5.825 | 4.517 |
| Wall time, Linux/Windows build (ms) | 27.597 | 23.631 |
| generation (ms) | 0.103 | 0.088 |
| reductions (ms) | 5.530 | 4.270 |
| total (ms) | 5.803 | 4.504 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/binaryHeap.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (2 distinct)

| Share | Counterexample |
|---|---|
| 66% | 🎯 `(0, None, (0, (0, None, None), (1, None, None)))` |
| 34% | `(0, (0, (1, None, None), None), (0, None, None))` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 16.39 | 16.30 | 17.70 |
| Source core / debug runner (on macOS) | 17.79 | 17.69 | 19.12 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge binaryHeap --iterations 100 --seed 1337 --report-path ../failures
```
