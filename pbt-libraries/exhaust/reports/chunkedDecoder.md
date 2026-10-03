# Chunked Decoder

Exhaust 1.5.5, release build. 100 runs on seeds 1337–1436; 100 failures.

[Raw results](../failures/chunkedDecoder.json). Dependency revision: `c7dbb96f2c713e463cd284b41db92d478799b61c`.

| Metric | Mean | Median |
|---|---:|---:|
| Reduction invocations | 84.1 | 76.0 |
| Original input length | 31.2 | 30.0 |
| Wall time (ms) | 0.697 | 0.676 |
| generation (ms) | 0.021 | 0.018 |
| reductions (ms) | 0.620 | 0.580 |
| total (ms) | 0.691 | 0.670 |

The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.

## Counterexamples (5 distinct)

| Share | Counterexample |
|---|---|
| 56% | `(text, "\u{10000}", [3, 1])` |
| 40% | `(text, "\u{800}", [2, 1])` |
| 2% | 🎯 `(text, "\u{80}", [1, 1])` |
| 1% | `(text, "\u{10000}\u{800}", [6, 1])` |
| 1% | `(text, "\u{10000}\u{10000}", [7, 1])` |

## Running

```sh
swift run -c release ExhaustRunner --challenge chunkedDecoder --iterations 100 --seed 1337 --report-path ../failures
```
