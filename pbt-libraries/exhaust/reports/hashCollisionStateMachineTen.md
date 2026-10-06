# Hash Collision (M = 10) (state machine)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineTen.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 221.5 | 177.0 |
| Original input length | 355.0 | 369.0 |
| Wall time (ms) | 2.065 | 1.911 |
| Wall time, Linux/Windows build (ms) | 7.626 | 7.444 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 1.970 | 1.800 |
| total (ms) | 2.050 | 1.897 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineTen.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `[put(0, 0), put(10, 1)]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.66 | 15.67 | 16.11 |
| Source core / debug runner (on macOS) | 16.93 | 16.95 | 17.39 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineTen --iterations 100 --seed 1337 --report-path ../failures
```
