# Username and Password

Exhaust 1.6.0 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/usernamePassword.json). Dependency revision: `ccc7e4c2e9749fc6eb4d75c24ba01702840c2eee`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 750.0 | 750.0 |
| Original input length | 30.0 | 30.0 |
| Wall time (ms) | 4.835 | 4.835 |
| Wall time, Linux/Windows build (ms) | 25.112 | 25.112 |
| reductions (ms) | 4.540 | 4.540 |
| total (ms) | 4.686 | 4.686 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/usernamePassword.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `("u: 0000", "p: 0000")` |

## Peak resident memory

| Configuration | Mean (MiB) | Median (MiB) | Max (MiB) |
|---|---:|---:|---:|
| macOS XCFramework / debug runner | 15.25 | 15.25 | 15.25 |
| Source core / debug runner (on macOS) | 16.20 | 16.20 | 16.20 |

[Per-run memory logs and summaries](/reports/memory-exhaust-1.6.0/).

## Running

```sh
swift run ExhaustRunner --challenge usernamePassword --iterations 100 --seed 1337 --report-path ../failures
```
