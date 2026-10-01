# Chunked Decoder Report for Exhaust

These results are from Exhaust v1.5.3, October 1st, 2026.

A message is either binary (up to 64 bytes) or text (up to 16 Unicode scalars), chosen with `oneOf`. Its content is encoded to bytes, and the transport may split those bytes anywhere: the generator draws one cut flag per gap between bytes, so the chunking depends on the encoded byte count. The property is that decoding the reassembled chunks gives back the original message. The deliberate bug decodes each text chunk on its own, so a scalar split across two chunks turns into replacement characters. Counterexamples are written as `(kind, content, chunk sizes)`, with every scalar outside printable ASCII escaped as `\u{…}`.

## Normalization

Exhaust produced 5 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 56% | `(text, "\u{10000}", [3, 1])` |
| 40% | `(text, "\u{800}", [2, 1])` |
| 2% | `(text, "\u{80}", [1, 1])` |
| 1% | `(text, "\u{10000}\u{800}", [6, 1])` |
| 1% | `(text, "\u{10000}\u{10000}", [7, 1])` |

The minimal counterexample is `(text, "\u{80}", [1, 1])`: U+0080 is the smallest scalar with a 2-byte UTF-8 encoding, split after its first byte. 2 of 100 runs reached it.

Exhaust reduces the split scalar to the smallest one of the same encoded width: U+10000 for 4 bytes, U+0800 for 3 bytes. It rarely moves to a narrower encoding, because that changes the byte count the cut flags were generated from. In this run it never went below 3 bytes, and it went from 4 bytes to 3 in 13 of the 71 runs that started with a 4-byte scalar.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/chunkedDecoder.json).

## Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 16.0 | 222.0 | 76.0 | 84.1 | 78.0–90.2 |
| Reduction time (ms) | 0.15 | 1.58 | 0.55 | 0.58 | 0.54–0.62 |
| Wall time (ms) | 0.245 | 1.673 | 0.629 | 0.66 | 0.621–0.7 |
| Iterations to failure | 3.0 | 21.0 | 6.0 | 6.8 | 6.1–7.5 |

## Reproduction

From the `exhaust/src` folder, run the following command:

`swift run -c release ExhaustRunner --challenge chunkedDecoder --iterations 100`

The reduction and wall times reflect running on an M4 Max running macOS 26.4. Wall time covers generation and reduction. This is an optimised release build.
