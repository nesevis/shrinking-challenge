# Hash Collision (M = 100) (state machine)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineHundred.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 746.9 | 714.5 |
| Original input length | 421.7 | 436.5 |
| Wall time (ms) | 5.937 | 5.524 |
| Wall time, Linux/Windows build (ms) | 16.962 | 16.388 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 5.660 | 5.200 |
| total (ms) | 5.919 | 5.507 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineHundred.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (3 distinct)

| Share | Counterexample |
|---|---|
| 80% | 🎯 `[put(0, 0), put(100, 1)]` |
| 14% | `[put(0, 0), put(300, 1)]` |
| 6% | `[put(0, 0), put(700, 1)]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.79 | 15.80 | 16.19 |
| Source core / debug runner (on macOS) | 17.04 | 17.04 | 17.44 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineHundred --iterations 100 --seed 1337 --report-path ../failures
```
