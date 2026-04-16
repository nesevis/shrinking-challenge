# Exhaust

[Exhaust](https://github.com/nesevis/exhaust) is a property-based testing library for Swift. It was inspired by [Harrison Goldstein](https://harrisongoldste.in)'s work on [Reflective Generators](https://dl.acm.org/doi/10.1145/3607842) and by the general excellence of [Hypothesis](https://hypothesis.works).

The library is packaged as a public API module that consumes a pre-compiled core framework. This is done so that users can enjoy increased performance in debug builds.

## Exhaust's Shrinking Approach

Exhaust's reducer is a graph-based, dependency-aware integrated shrinker. It does not require any hints or generator co-design.

All constraints expressed during generation are preserved during shrinking.

## Implemented Challenges

| Challenge | Code | Report |
|---|---|---|
| [Binary Heap](/challenges/binheap.md) | [BinaryHeap.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/BinaryHeap.swift) | [binaryHeap.md](/pbt-libraries/exhaust/reports/binaryHeap.md) |
| [Bound5](/challenges/bound5.md) | [Bound5.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Bound5.swift) | [bound5.md](/pbt-libraries/exhaust/reports/bound5.md) |
| [Calculator](/challenges/calculator.md) | [Calculator.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Calculator.swift) | [calculator.md](/pbt-libraries/exhaust/reports/calculator.md) |
| [Coupling](/challenges/coupling.md) | [Coupling.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Coupling.swift) | [coupling.md](/pbt-libraries/exhaust/reports/coupling.md) |
| [Deletion](/challenges/deletion.md) | [Deletion.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Deletion.swift) | [deletion.md](/pbt-libraries/exhaust/reports/deletion.md) |
| [Difference](/challenges/difference.md) | [Difference.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Difference.swift) | [differenceNotOne.md](/pbt-libraries/exhaust/reports/differenceNotOne.md) |
|  |  | [differenceNotSmall.md](/pbt-libraries/exhaust/reports/differenceNotSmall.md) |
|  |  | [differenceNotZero.md](/pbt-libraries/exhaust/reports/differenceNotZero.md) |
| [Distinct](/challenges/distinct.md) | [Distinct.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Distinct.swift) | [distinct.md](/pbt-libraries/exhaust/reports/distinct.md) |
| [Large Union List](/challenges/large_union_list.md) | [LargeUnionList.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/LargeUnionList.swift) | [largeUnionList.md](/pbt-libraries/exhaust/reports/largeUnionList.md) |
| [Length List](/challenges/lengthlist.md) | [LengthListChallenge.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/LengthListChallenge.swift) | [lengthList.md](/pbt-libraries/exhaust/reports/lengthList.md) |
| [Nested Lists](/challenges/nestedlists.md) | [NestedListsChallenge.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedListsChallenge.swift) | [nestedLists.md](/pbt-libraries/exhaust/reports/nestedLists.md) |
| [Reverse](/challenges/reverse.md) | [ReverseChallenge.swift](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ReverseChallenge.swift) | [reverse.md](/pbt-libraries/exhaust/reports/reverse.md) |

## Results

All figures are means across 1,000 single-threaded runs on an M4 Max running macOS 26.4. 

This is an unoptimised debug build, mirroring the experience of using Exhaust inside a `swift test` target rather than a best-case release benchmark.

See each linked report for counterexample(s) and statistical breakdown.

| Challenge | Results | Evaluations | Reduction (ms) | Iterations to failure |
|---|---|---|---|---|
| [Binary Heap](/pbt-libraries/exhaust/reports/binaryHeap.md) | 3 | 321.6 | 26.24 | 1.7 |
| [Bound5](/pbt-libraries/exhaust/reports/bound5.md) | 1 | 124.5 | 1.67 | 7.5 |
| [Calculator](/pbt-libraries/exhaust/reports/calculator.md) | 1 | 24.7 | 0.91 | 28.2 |
| [Coupling](/pbt-libraries/exhaust/reports/coupling.md) | 1 | 16.6 | 0.28 | 3.7 |
| [Deletion](/pbt-libraries/exhaust/reports/deletion.md) | 1 | 4.5 | 0.17 | 16.9 |
| [Difference: Not One](/pbt-libraries/exhaust/reports/differenceNotOne.md) | 1 | 107.5 | 0.28 | 1642.1 |
| [Difference: Not Small](/pbt-libraries/exhaust/reports/differenceNotSmall.md) | 1 | 93.1 | 0.25 | 399.5 |
| [Difference: Not Zero](/pbt-libraries/exhaust/reports/differenceNotZero.md) | 1 | 105.6 | 0.28 | 3380.4 |
| [Distinct](/pbt-libraries/exhaust/reports/distinct.md) | 1 | 15.2 | 0.14 | 2.5 |
| [Large Union List](/pbt-libraries/exhaust/reports/largeUnionList.md) | 1 | 121.9 | 0.96 | 4.6 |
| [Length List](/pbt-libraries/exhaust/reports/lengthList.md) | 1 | 20.8 | 0.77 | 1.1 |
| [Nested Lists](/pbt-libraries/exhaust/reports/nestedLists.md) | 1 | 37.1 | 0.75 | 6.4 |
| [Reverse](/pbt-libraries/exhaust/reports/reverse.md) | 1 | 7.8 | 0.16 | 1.3 |

## Running examples

You need Swift 6.2 or newer and macOS 15/Sequoia or higher.

```bash
cd pbt-libraries/exhaust/src
swift run ExhaustRunner --iterations 1000
```

Run a single challenge:

```bash
swift run ExhaustRunner --challenge bound5 --iterations 1000
```
