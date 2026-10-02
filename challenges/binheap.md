# Wrong Binary Heap

[Original source](https://github.com/mc-imperial/hypothesis-ecoop-2020-artifact/tree/master/smartcheck-benchmarks/evaluations/binheap)

This is based on an example from QuickCheck's test suite (via the SmartCheck paper). 
It generates binary heaps, and then uses a wrong implementation of a function 
that converts the binary heap to a sorted list and asserts that the result is sorted.

Interestingly most libraries seem to never find the smallest example here, 
which is the four valued heap (0, None, (0, (0, None, None), (1, None, None))). 
This is essentially because small examples are "too sparse", so it's very hard to find one by luck.

## New 100-seed results

The new Hypothesis and Hegel ports both use generated starts, the same numeric
seed list, and the Exhaust generator's domains and empty/node multiplicity.
Equal seeds do not imply equal starting heaps. Sequential runs on an Apple M4 Max:

| Library | Four-node minimum | Mean evaluations | Mean total time (ms) |
|---|---:|---:|---:|
| Hypothesis 6.168.3 | 85/100 | 102.46 | 137.17 |
| Hegel 0.48.1 / engine 0.44.1 | 100/100 | 5886.23 | 296.48 |

Hypothesis's other 15 results had five nodes. Hegel produced one distinct result;
Hypothesis produced three. Total time includes generation and reduction;
evaluation counts use each library's existing harness conventions. All 400
recorded original/reduced heaps satisfy the heap invariant and reproduce the
bug. These are not paired-start reducer performance measurements.

## Implementors

| Library   | Code                                                                                                   | Report                                                    |
|-----------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Americium | [HeapTest.java](/pbt-libraries/americium/src/test/java/challenges/binheap/HeapTest.java)               | [binheap.md](/pbt-libraries/americium/reports/binheap.md) |
| jqwik     | [BinheapProperties.java](/pbt-libraries/jqwik/src/test/java/challenges/binheap/BinheapProperties.java) | [binheap.md](/pbt-libraries/jqwik/reports/binheap.md)     |
| CsCheck   | [ShrinkingChallengeTests.cs](/pbt-libraries/cscheck/ShrinkingChallengeTests.cs#L128)                   | [binheap.md](/pbt-libraries/cscheck/reports/binheap.md)   |
| elm-test  | [BinHeap.elm](/pbt-libraries/elm-test/src/Challenge/BinHeap.elm)                                       | [binHeap.md](/pbt-libraries/elm-test/reports/binHeap.md)  |
| Hypothesis | [binheap.py](/pbt-libraries/hypothesis/challenges/binheap.py) | [binheap.md](/pbt-libraries/hypothesis/challenges/binheap.md) |
| Hegel | [binary_heap.rs](/pbt-libraries/hegel/src/binary_heap.rs) | [binheap.md](/pbt-libraries/hegel/reports/binheap.md) |
| Exhaust   | [BinaryHeap.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/BinaryHeap.swift)       | [binaryHeap.md](/pbt-libraries/exhaust/reports/binaryHeap.md) |

