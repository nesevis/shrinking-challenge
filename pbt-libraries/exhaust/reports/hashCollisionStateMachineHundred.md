# Hash Collision (M = 100) (state machine)

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineHundred.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 747.4 | 718.0 |
| Original input length | 421.7 | 436.5 |
| Wall time (ms) | 5.826 | 5.252 |
| Wall time, Linux/Windows build (ms) | 19.014 | 18.385 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 5.510 | 5.090 |
| total (ms) | 5.795 | 5.225 |

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
| macOS XCFramework / debug runner | 15.64 | 15.64 | 16.05 |
| Source core / debug runner (on macOS) | 16.99 | 17.02 | 17.38 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineHundred --iterations 100 --seed 1337 --report-path ../failures
```
