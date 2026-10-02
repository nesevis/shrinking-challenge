# Wrong Binary Heap — Hegel

Hegel 0.48.1, native engine 0.44.1, release build. **100 generated-and-shrunk
runs**, using the same numeric seeds as Hypothesis. [Raw results](binheap.json).
Equal seeds do not imply equal generated starting heaps.

The generator matches Exhaust's depth controller (`0...20`), dependent nonnegative
signed-64-bit keys, and 1:5 empty/node multiplicity. Hegel's `one_of!` uses an empty
alternative followed by five equivalent node alternatives. The property checks
sortedness and preservation of the original multiset; the deliberately buggy
implementation traverses the merged children rather than repeatedly extracting
the minimum.

| Metric | Value |
|---|---:|
| Runs | 100 |
| Distinct reduced counterexamples | 1 |
| Known four-node minimum | 100% |
| Mean evaluations from first failure | 5886.23 |
| Mean total elapsed time (ms) | 296.48 |

All runs reduced to:

```text
(0, None, (0, (0, None, None), (1, None, None)))
```

Its buggy output is `[0, 0, 1, 0]`. Evaluation counts include confirmation and
final replay; elapsed time includes generation and shrinking. All 100 original
and reduced heaps were validated against the Python fixture's heap invariant and
buggy traversal.

## Hypothesis comparison

Hypothesis 6.168.3 found the same minimum in 85% of runs; the remaining 15% had
five nodes. It averaged 102.46 evaluations and 137.17 ms total elapsed time.
These are library-specific generated starts, not a paired-start reducer A/B test.
Evaluation accounting differs between libraries.

## Reproduction

From `pbt-libraries/hegel`:

```sh
cargo run --release --locked -- --challenge binheap --iterations 100 --seed-file support/binheap-seeds.json --output reports
```

This standalone port is available through `--list` and explicit
`--challenge binheap`. It is not included in the existing 24-challenge published
comparison, its default seed file, or comparison-report scripts.
