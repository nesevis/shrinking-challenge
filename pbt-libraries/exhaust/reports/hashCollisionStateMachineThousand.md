# Hash Collision (M = 1000) (state machine)

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/hashCollisionStateMachineThousand.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 729.3 | 705.0 |
| Original input length | 512.5 | 530.0 |
| Wall time (ms) | 11.086 | 9.361 |
| Wall time, Linux/Windows build (ms) | 23.157 | 21.440 |
| generation (ms) | 0.000 | 0.000 |
| reductions (ms) | 8.670 | 7.280 |
| total (ms) | 11.063 | 9.338 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/hashCollisionStateMachineThousand.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 36% | 🎯 `[put(0, 0), put(1000, 1)]` |
| 23% | `[put(0, 0), put(9000, 1)]` |
| 15% | `[put(0, 0), put(3000, 1)]` |
| 14% | `[put(0, 0), put(7000, 1)]` |
| 12% | `[put(0, 0), put(5000, 1)]` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.94 | 15.97 | 16.33 |
| Source core / debug runner (on macOS) | 17.18 | 17.20 | 17.53 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge hashCollisionStateMachineThousand --iterations 100 --seed 1337 --report-path ../failures
```
