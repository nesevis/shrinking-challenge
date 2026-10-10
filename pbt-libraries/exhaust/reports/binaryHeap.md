# Binary Heap

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/binaryHeap.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 117.9 | 94.5 |
| Original input length | 384.4 | 352.0 |
| Wall time (ms) | 5.503 | 4.386 |
| Wall time, Linux/Windows build (ms) | 29.833 | 25.332 |
| generation (ms) | 0.108 | 0.092 |
| reductions (ms) | 5.170 | 3.980 |
| total (ms) | 5.280 | 4.137 |

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
| macOS XCFramework / debug runner | 16.69 | 16.61 | 18.03 |
| Source core / debug runner (on macOS) | 17.76 | 17.70 | 19.05 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge binaryHeap --iterations 100 --seed 1337 --report-path ../failures
```
