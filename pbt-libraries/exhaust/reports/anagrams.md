# Anagrams

Exhaust 1.5.6 package, runner built in debug on macOS, which links the prebuilt `ExhaustCore`. One fixed-start reduction.

[Raw results](../failures/anagrams.json). Dependency revision: `6bad138e956e568d57b041e4063bd0de0f964dc0`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 1239.0 | 1239.0 |
| Original input length | 62.0 | 62.0 |
| Wall time (ms) | 18.309 | 18.309 |
| Wall time, Linux/Windows build (ms) | 60.902 | 60.902 |
| reductions (ms) | 18.090 | 18.090 |
| total (ms) | 18.281 | 18.281 |

The Linux/Windows build compiles the same source entirely in debug, as on platforms without the XCFramework ([raw results](../failures-linux/anagrams.json)).

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (1 distinct)

| Share | Counterexample |
|---|---|
| 100% | 🎯 `(" \0", "\0 ")` |

## Running

```sh
swift run ExhaustRunner --challenge anagrams --iterations 100 --seed 1337 --report-path ../failures
```
