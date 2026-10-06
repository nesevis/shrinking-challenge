# Username and Password

Exhaust 1.5.8 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/usernamePassword.json). Dependency revision: `50b3b752872795b0637f4e34a5e604877d414e2f`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 731.0 | 731.0 |
| Original input length | 30.0 | 30.0 |
| Wall time (ms) | 4.588 | 4.588 |
| Wall time, Linux/Windows build (ms) | 21.350 | 21.350 |
| reductions (ms) | 4.360 | 4.360 |
| total (ms) | 4.481 | 4.481 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/usernamePassword.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `("u: 0000", "p: 0000")` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.12 | 15.12 | 15.12 |
| Source core / debug runner (on macOS) | 16.19 | 16.19 | 16.19 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.5.8/).

## Running

```sh
swift run ExhaustRunner --challenge usernamePassword --iterations 100 --seed 1337 --report-path ../failures
```
