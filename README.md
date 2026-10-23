# Ad hoc shrinking challenge: Hypothesis vs Exhaust vs Hegel

A fast and loose comparison of:

- [Hypothesis](/pbt-libraries/hypothesis/README.md) 6.168.3
- [Exhaust](/pbt-libraries/exhaust/README.md) 1.7.4
- [Hegel](/pbt-libraries/hegel/README.md) 0.49.14 (native engine 0.45.13)

Library links point to each implementation of the challenge. 🎯 marks the ~minimal counterexample. For Binary Heap, 🎯 marks only the absolute shortlex minimum.

This document has five parts:
- Fixed start (reflecting or inverting and then reducing, no generation)
- 100 seeded runs of a number of new and old challenges
- 100 seeded runs of handwritten and derived generators for the same two challenges
- 100 seeded runs of state machine tests
- Best-effort representative wall clock timings

This is largely generated using Claude, so caveats apply to the Hypothesis and Hegel implementations as to how idiomatic they are.

Exhaust doesn't count the first failing evaluation in its stats, so 1 has been added to all numbers.

## Fixed start

Hypothesis and Exhaust reduce the same fixed failing input once, with no generation phase. Fixed-start rows use each runner's reported evaluation count directly.

| Challenge | Library | Evaluations | Counterexample |
|---|---|---|---|
| Anagrams | [Hypothesis](/pbt-libraries/hypothesis/challenges/anagrams.py) | 798 | `("000000000000000000000000011", "000000000000000000000000110")` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Anagrams.swift) | 1285 | 🎯 `(" \0", "\0 ")` |
|  |  |  |  |
| Username and Password | [Hypothesis](/pbt-libraries/hypothesis/challenges/username_password.py) | 301 | `("u: p0000000", "p: p0000000")` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/UsernamePasswordChallenge.swift) | 750 | 🎯 `("u: 0000", "p: 0000")` |
|  |  |  |  |
| Duplicated Text | [Hypothesis](/pbt-libraries/hypothesis/challenges/duplicated_text.py) | 30 | 🎯 `("00000012", "00000012")` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/DuplicatedTextChallenge.swift) | 54 | `("10210210", "10210210")` |
|  |  |  |  |
| Haystack | [Hypothesis](/pbt-libraries/hypothesis/challenges/haystack.py) | 242 | 🎯 `"CREEPIDIOT"` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HaystackChallenge.swift) | 332 | 🎯 `"CREEPIDIOT"` |
|  |  |  |  |
| Zalgo Haystack | [Hypothesis](/pbt-libraries/hypothesis/challenges/zalgo_haystack.py) | 444 | 🎯 `"THE ICHOR PERMEATES"` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ZalgoHaystackChallenge.swift) | 465 | 🎯 `"THE ICHOR PERMEATES"` |
|  |  |  |  |
| Distinct Sum | [Hypothesis](/pbt-libraries/hypothesis/challenges/distinct_sum.py) | 133 | 🎯 `[0, 1, -1, 2, 49]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/DistinctSumChallenge.swift) | 960 | 🎯 `[-1, 0, 1, 2, 49]` |
|  |  |  |  |
| Leap Day | [Hypothesis](/pbt-libraries/hypothesis/challenges/leap_day.py) | 25 | 🎯 `2000-02-29 00:00:00 +0000` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/LeapDayChallenge.swift) | 34 | `2088-02-29 00:00:00 +0000` |
|  |  |  |  |
| Branch Switching | [Hypothesis](/pbt-libraries/hypothesis/challenges/branch_switching.py) | 44 | 🎯 `1001` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/BranchSwitchingChallenge.swift) | 17 | `"    "` |

## 100 seeds

Each library generated and reduced a failure in each of 100 seeded runs.

Exhaust and Hegel use 100 consecutive seeds starting at 1337. Hypothesis hashes each challenge's filename with SHA1 to seed a PRNG, then draws 100 seeds from it.

- **Top counterexamples**: the share of runs ending at each counterexample. The top three are shown, followed by the minimal counterexample if it occurred outside them
- **Distinct CEs**: the number of different counterexamples across the 100 runs.
- **Mean evaluations / Median evaluations**: both calculated across the 100 runs, using the counting conventions below
- **Mean original length**: the average character length of the first failing input's rendering.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples<br><img src="assets/spacer.gif" width="1000" height="1" alt=""> |
|---|---|---|---|---|---|---|
| Binary Heap | [Hypothesis](/pbt-libraries/hypothesis/challenges/binheap.py) | 3 | 102.5 | 97.5 | 151.1 | 85% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>14% `(0, None, (0, None, (0, (0, None, None), (1, None, None))))`<br>1% `(0, None, (0, (0, None, None), (0, None, (1, None, None))))` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/BinaryHeap.swift) | 2 | 98.5 | 87.0 | 384.4 | 66% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>34% `(0, (0, (1, None, None), None), (0, None, None))` |
|  | [Hegel](/pbt-libraries/hegel/src/binary_heap.rs) | 2 | 5837.7 | 5176.0 | 312.2 | 99% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>1% `(127, None, (55190086533789320, (401787435511877632, None, (7196582761221413107, None, None)), (7196582761221412864, (7196582761221413107, None, None), None)))` |
|  |  |  |  |  |  |  |
| Calculator | [Hypothesis](/pbt-libraries/hypothesis/challenges/calculator.py) | 1 | 90.5 | 81.0 | 125.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Calculator.swift) | 1 | 78.3 | 101.5 | 63.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Hegel](/pbt-libraries/hegel/src/calculator.rs) | 1 | 442.2 | 441.0 | 239.2 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_2.py) | 3 | 71.5 | 63.0 | 118.4 | 43% `(8, 3, 0x23 + 1x1)`<br>39% 🎯 `(6, 4, 0x23 + 1x1)`<br>18% `(5, 5, 0x24 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L11) | 1 | 297.5 | 300.0 | 141.0 | 100% 🎯 `(6, 4, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 2 | 1274.4 | 1361.5 | 142.5 | 73% 🎯 `(6, 4, 0x23 + 1x1)`<br>27% `(8, 3, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_3.py) | 6 | 86.9 | 79.5 | 210.4 | 32% `(6, 2, 2, 0x23 + 1x1)`<br>23% `(8, 3, 1, 0x23 + 1x1)`<br>21% 🎯 `(4, 3, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L18) | 1 | 364.7 | 354.0 | 386.3 | 100% 🎯 `(4, 3, 2, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 2 | 1740.1 | 1832.5 | 410.6 | 84% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>16% `(8, 3, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_4.py) | 8 | 80.5 | 72.0 | 272.1 | 27% `(8, 3, 1, 1, 0x23 + 1x1)`<br>18% `(6, 4, 1, 1, 0x23 + 1x1)`<br>14% `(4, 3, 2, 1, 0x23 + 1x1)`<br>12% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L27) | 1 | 401.2 | 411.0 | 1107.9 | 100% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 3 | 1843.0 | 1841.5 | 1074.1 | 68% `(4, 3, 2, 1, 0x23 + 1x1)`<br>16% `(8, 3, 1, 1, 0x23 + 1x1)`<br>16% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_5.py) | 17 | 64.5 | 49.5 | 248.8 | 12% `(6, 4, 1, 1, 1, 0x23 + 1x1)`<br>10% `(7, 4, 1, 1, 1, 0x27 + 1x1)`<br>10% `(6, 2, 2, 1, 1, 0x23 + 1x1)`<br>4% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L38) | 1 | 391.8 | 390.5 | 3737.7 | 100% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 4 | 1888.0 | 1788.0 | 2049.6 | 65% `(4, 3, 2, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 0x23 + 1x1)`<br>12% `(2, 2, 2, 2, 2, 0x31 + 1x1)`<br>8% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_6.py) | 20 | 62.9 | 48.5 | 261.4 | 20% `(6, 4, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)`<br>5% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L51) | 1 | 403.2 | 412.0 | 5867.6 | 100% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 6 | 2162.1 | 1800.5 | 3735.3 | 62% `(4, 3, 2, 1, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>12% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>8% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_2.py) | 1 | 18.8 | 18.0 | 6.3 | 100% 🎯 `(5, 5)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L67) | 1 | 22.6 | 21.0 | 6.2 | 100% 🎯 `(5, 5)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 1 | 3532.3 | 3640.0 | 6.3 | 100% 🎯 `(5, 5)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_3.py) | 1 | 22.1 | 20.0 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L72) | 1 | 22.0 | 19.0 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 1 | 4171.8 | 4240.5 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_4.py) | 1 | 24.3 | 23.5 | 12.3 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L79) | 1 | 22.7 | 19.0 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 1 | 4743.4 | 4744.0 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_5.py) | 1 | 26.2 | 25.0 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L88) | 1 | 23.5 | 23.0 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 1 | 4239.9 | 4324.5 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_6.py) | 1 | 28.1 | 29.5 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L99) | 1 | 25.0 | 23.0 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L100) | 1 | 3596.3 | 2924.0 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (sum), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_sum_4.py) | 1 | 162.3 | 160.5 | 368.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L113) | 1 | 1502.6 | 1552.0 | 344.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L112) | 1 | 3298.5 | 3287.5 | 342.9 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.py) | 12 | 20.6 | 20.0 | 3.0 | 32% 🎯 `925`<br>16% `921`<br>10% `917` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ModularMappingChallenge.swift) | 18 | 18.9 | 17.0 | 3.0 | 15% 🎯 `925`<br>13% `921`<br>10% `901` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L117) | 5 | 32.9 | 32.0 | 3.0 | 82% 🎯 `925`<br>14% `926`<br>2% `905` |
|  |  |  |  |  |  |  |
| Weighted Linear Preservation | [Hypothesis](/pbt-libraries/hypothesis/challenges/weighted_linear_preservation.py) | 8 | 53.8 | 51.0 | 9.5 | 25% `(10, 0, 0)`<br>24% `(5, 0, 10)`<br>15% 🎯 `(0, 0, 20)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/WeightedLinearPreservationChallenge.swift) | 1 | 157.8 | 94.0 | 9.6 | 100% 🎯 `(0, 0, 20)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L126) | 1 | 61.2 | 64.5 | 9.5 | 100% 🎯 `(0, 0, 20)` |
|  |  |  |  |  |  |  |
| AscendingArray | [Hypothesis](/pbt-libraries/hypothesis/challenges/ascending_array.py) | 4 | 131.8 | 128.0 | 48.0 | 57% `[-3, -2, -1, 0, 1]`<br>28% `[-2, -1, 0, 1, 2]`<br>13% `[-1, 0, 1, 2, 3]`<br>2% 🎯 `[0, 1, 2, 3, 4]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/AscendingArrayChallenge.swift) | 1 | 585.4 | 572.0 | 51.0 | 100% 🎯 `[0, 1, 2, 3, 4]` |
|  | [Hegel](/pbt-libraries/hegel/src/ascending_array.rs) | 4 | 277.8 | 224.5 | 45.7 | 34% `[-2, -1, 0, 1, 2]`<br>26% `[-1, 0, 1, 2, 3]`<br>24% 🎯 `[0, 1, 2, 3, 4]` |
|  |  |  |  |  |  |  |
| Float Cancellation | [Hypothesis](/pbt-libraries/hypothesis/challenges/float_cancellation.py) | 82 | 66.1 | 30.0 | 41.3 | 3% `(1.0, 3.1)`<br>3% `(1.1125369292536007e-308, 1.0)`<br>3% `(1.0, 3.9)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/FloatCancellationChallenge.swift) | 1 | 259.3 | 196.0 | 40.9 | 100% `(1.0, 1.0000000000000002)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L143) | 32 | 552.2 | 436.5 | 43.4 | 33% `(1.0, 524287.00000000006)`<br>23% `(1.0, 1.0000000000000002)`<br>6% `(1.0, 65535.00000000001)` |
|  |  |  |  |  |  |  |
| Chunked Decoder | [Hypothesis](/pbt-libraries/hypothesis/challenges/chunked_decoder.py) | 1 | 50.1 | 47.0 | 61.2 | 100% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ChunkedDecoderChallenge.swift) | 5 | 24.4 | 23.5 | 31.2 | 64% 🎯 `(text, "\u{80}", [1, 1])`<br>28% `(text, "\u{800}", [2, 1])`<br>6% `(text, "\u{10000}", [3, 1])` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L150) | 69 | 1761.0 | 1573.0 | 87.9 | 11% 🎯 `(text, "\u{80}", [1, 1])`<br>6% `(text, "\u{10000}\u{10000}", [7, 1])`<br>6% `(text, "\u{10000}", [3, 1])` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_10.py) | 10 | 75.1 | 75.5 | 44.1 | 30% `([(10, 0)], 0, 1)`<br>17% `([(30, 0)], 0, 1)`<br>14% 🎯 `([(0, 0)], 10, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L46) | 1 | 198.4 | 163.0 | 29.9 | 100% 🎯 `([(0, 0)], 10, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L154) | 1 | 439.2 | 453.0 | 90.4 | 100% 🎯 `([(0, 0)], 10, 1)` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_100.py) | 8 | 132.0 | 114.5 | 64.3 | 62% `([(100, 0)], 0, 1)`<br>20% 🎯 `([(0, 0)], 100, 1)`<br>7% `([(300, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L46) | 4 | 698.3 | 614.0 | 61.8 | 73% 🎯 `([(0, 0)], 100, 1)`<br>19% `([(0, 0)], 300, 1)`<br>7% `([(0, 0)], 700, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L154) | 1 | 519.1 | 530.5 | 120.5 | 100% 🎯 `([(0, 0)], 100, 1)` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_1000.py) | 9 | 771.4 | 969.5 | 101.6 | 40% `([(1000, 0)], 0, 1)`<br>22% 🎯 `([(0, 0)], 1000, 1)`<br>13% `([(3000, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L46) | 5 | 654.8 | 656.5 | 117.5 | 71% 🎯 `([(0, 0)], 1000, 1)`<br>14% `([(0, 0)], 3000, 1)`<br>9% `([(0, 0)], 5000, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L154) | 1 | 522.9 | 535.5 | 107.0 | 100% 🎯 `([(0, 0)], 1000, 1)` |

## Handwritten and derived generators

Each challenge pairs a handwritten generator with raw type derivation. Columns and evaluation counts follow the 100 seeds table above.

Hegel's fully derived invoice uses raw signed 64-bit fields, as Exhaust's does, rather than Hypothesis's arbitrary-precision integers.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples<br><img src="assets/spacer.gif" width="1000" height="1" alt=""> |
|---|---|---|---|---|---|---|
| Invoice Discount | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount.py) | 22 | 61.5 | 57.5 | 19.6 | 40% `Invoice(28, 36, 1)`<br>8% `Invoice(201, 5, 1)`<br>6% `Invoice(11, 91, 1)`<br>4% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/InvoiceDiscountChallenge.swift#L28) | 1 | 362.7 | 111.0 | 19.7 | 100% 🎯 `Invoice(10, 100, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L134) | 1 | 661.4 | 634.5 | 19.5 | 100% 🎯 `Invoice(10, 100, 1)` |
|  |  |  |  |  |  |  |
| Invoice Discount (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount_derived.py) | 9 | 748.5 | 881.0 | 19.1 | 86% `Invoice(28, 36, 1)`<br>5% `Invoice(101, 10, 1)`<br>3% `Invoice(11, 91, 1)`<br>1% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/InvoiceDiscountChallenge.swift#L38) | 5 | 1177.0 | 727.0 | 19.0 | 69% `Invoice(15, 67, 1)`<br>12% `Invoice(14, 72, 1)`<br>8% `Invoice(13, 77, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L134) | 9 | 463.5 | 479.0 | 18.9 | 33% `Invoice(18, 56, 1)`<br>27% 🎯 `Invoice(10, 100, 1)`<br>25% `Invoice(14, 72, 1)` |
|  |  |  |  |  |  |  |
| Refund Allocation | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation.py) | 5 | 175.7 | 127.5 | 45.8 | 78% `RefundRequest([31, 34], 2)`<br>13% `RefundRequest([33, 31], 2)`<br>5% 🎯 `RefundRequest([31, 33], 4)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/RefundAllocationChallenge.swift#L31) | 1 | 60.7 | 60.0 | 78.6 | 100% 🎯 `RefundRequest([31, 33], 4)` |
|  | [Hegel](/pbt-libraries/hegel/src/refund_allocation.rs#L153) | 7 | 1514.3 | 1447.5 | 62.6 | 94% 🎯 `RefundRequest([31, 33], 4)`<br>1% `RefundRequest([31, 36], 3)`<br>1% `RefundRequest([31, 32080508], 623195)` |
|  |  |  |  |  |  |  |
| Refund Allocation (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation_derived.py) | 4 | 129.3 | 108.5 | 46.1 | 69% `RefundRequest([33, 31], 2)`<br>28% `RefundRequest([31, 34], 2)`<br>2% `RefundRequest([31, 31, 33], 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/RefundAllocationChallenge.swift#L46) | 3 | 757.2 | 344.0 | 55.6 | 63% 🎯 `RefundRequest([31, 33], 4)`<br>22% `RefundRequest([33, 31], 2)`<br>15% `RefundRequest([31, 31, 33], 3)` |
|  | [Hegel](/pbt-libraries/hegel/src/refund_allocation.rs#L153) | 7 | 160.6 | 114.0 | 41.9 | 81% `RefundRequest([31, 34], 2)`<br>14% 🎯 `RefundRequest([31, 33], 4)`<br>1% `RefundRequest([61, 5079374505385], 62852702378)` |

## State machines

The recorded results cover 100 seeded state machine tests per library, generating command histories of up to 50 commands and reducing the first failing history. Exhaust uses `.commandLimit(50)` and Hegel uses `.steps(50)`, to match Hypothesis's default `stateful_step_count`.

The Hash Collision rows run the same frame property as the generator rows above, checked after every put. Together, the two tables show how each library's reduction changes with the encoding.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples<br><img src="assets/spacer.gif" width="1000" height="1" alt=""> |
|---|---|---|---|---|---|---|
| Snapshot Store | [Hypothesis](/pbt-libraries/hypothesis/challenges/snapshot_store.py) | 21 | 431.3 | 377.5 | 456.9 | 37% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>18% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]`<br>7% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/SnapshotStoreChallenge.swift) | 10 | 239.8 | 216.5 | 497.0 | 76% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>10% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]`<br>6% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L33) | 4 | 2147.5 | 1832.0 | 484.9 | 75% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>16% `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]`<br>8% `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_10.py) | 77 | 34.4 | 32.0 | 59.0 | 7% 🎯 `[put(0, 0), put(10, 1)]`<br>5% `[put(30, 0), put(0, 1)]`<br>4% `[put(0, 0), put(30, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L83) | 1 | 223.2 | 172.0 | 355.0 | 100% 🎯 `[put(0, 0), put(10, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L24) | 1 | 407.6 | 376.0 | 60.4 | 100% 🎯 `[put(0, 0), put(10, 1)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_100.py) | 59 | 46.5 | 45.0 | 184.5 | 39% 🎯 `[put(0, 0), put(100, 1)]`<br>2% `[put(499, 0), put(99, 1)]`<br>2% `[put(100, 0), put(0, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L100) | 3 | 744.1 | 715.5 | 421.7 | 81% 🎯 `[put(0, 0), put(100, 1)]`<br>14% `[put(0, 0), put(300, 1)]`<br>5% `[put(0, 0), put(700, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L24) | 1 | 299.1 | 292.0 | 210.2 | 100% 🎯 `[put(0, 0), put(100, 1)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_1000.py) | 98 | 103.5 | 107.0 | 434.6 | 2% `[put(140, 0), put(1140, 1)]`<br>2% `[put(4148, 0), put(148, 1)]`<br>1% `[put(3871, 0), put(7871, 1)]`<br>1% 🎯 `[put(0, 0), put(1000, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L117) | 5 | 729.6 | 706.0 | 512.5 | 36% 🎯 `[put(0, 0), put(1000, 1)]`<br>23% `[put(0, 0), put(9000, 1)]`<br>15% `[put(0, 0), put(3000, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L24) | 1 | 348.1 | 353.5 | 418.3 | 100% 🎯 `[put(0, 0), put(1000, 1)]` |


## Timings

Mean wall-clock milliseconds / mean peak resident memory in MiB per single-threaded run on an Apple M4 Max, over the same workloads and seeds as the tables above. Exhaust 1.7.4 timings come from multi-seed runs; peak RSS is measured separately in fresh processes.

Each column is the build a developer gets by default on that platform:

- **Hypothesis**: Hypothesis 6.168.3 on Python 3.12. Its recorded `total_seconds` includes the final replay.
- **Hegel (default/opt-1)**: `cargo build` without the `static-engine` feature. The runner is unoptimised and loads `libhegel_c` as a shared library built at Cargo's dev-profile `opt-level = 1`. Covers generation, reduction, counterexample recording, confirmation calls and final replay.
- **Exhaust (macOS)**: the 1.7.4 package with the runner built in debug. On Apple platforms the package links a prebuilt, optimised `ExhaustCore` XCFramework. Its `wallMilliseconds` covers generation and reduction; Exhaust makes no final replay.
- **Exhaust (Linux/Windows)**: the tagged 1.7.4 source built entirely in debug on the same Mac, as on platforms without the XCFramework, where `ExhaustCore` is compiled from source alongside the test target.

Exhaust retains a 125-second reduction deadline for these workloads.

| Challenge | Hypothesis | Hegel (default/opt-1) | Exhaust (macOS) | Exhaust (Linux/Windows) |
|---|---|---|---|---|
| Anagrams | 172.95 ms<br>40.5 MiB | — | 23.81 ms<br>15.9 MiB | 75.98 ms<br>17.0 MiB |
| Username and Password | 41.12 ms<br>38.7 MiB | — | 4.45 ms<br>15.4 MiB | 23.15 ms<br>16.6 MiB |
| Duplicated Text | 8.65 ms<br>37.7 MiB | — | 1.14 ms<br>15.0 MiB | 4.25 ms<br>16.1 MiB |
| Haystack | 116.59 ms<br>39.1 MiB | — | 9.42 ms<br>18.9 MiB | 58.59 ms<br>20.5 MiB |
| Zalgo Haystack | 2,994.38 ms<br>41.6 MiB | — | 14.17 ms<br>22.6 MiB | 115.14 ms<br>23.6 MiB |
| Distinct Sum | 46.29 ms<br>38.1 MiB | — | 5.02 ms<br>15.0 MiB | 16.93 ms<br>15.9 MiB |
| Leap Day | 9.18 ms<br>37.0 MiB | — | 3.50 ms<br>17.3 MiB | 4.87 ms<br>18.0 MiB |
| Branch Switching | 11.47 ms<br>38.3 MiB | — | 2.15 ms<br>16.1 MiB | 3.92 ms<br>17.2 MiB |
| Binary Heap | 133.68 ms<br>40.1 MiB | 734.00 ms<br>23.3 MiB | 6.55 ms<br>17.8 MiB | 36.23 ms<br>19.0 MiB |
| Calculator | 1,499.83 ms<br>61.6 MiB | 202.76 ms<br>8.2 MiB | 0.70 ms<br>15.7 MiB | 4.11 ms<br>16.8 MiB |
| Nested Flatmap (product sequence), depth 2 | 229.91 ms<br>39.9 MiB | 142.30 ms<br>10.9 MiB | 2.83 ms<br>16.0 MiB | 38.52 ms<br>16.9 MiB |
| Nested Flatmap (product sequence), depth 3 | 401.54 ms<br>41.8 MiB | 227.35 ms<br>16.7 MiB | 3.58 ms<br>16.3 MiB | 44.64 ms<br>17.3 MiB |
| Nested Flatmap (product sequence), depth 4 | 417.64 ms<br>43.3 MiB | 420.90 ms<br>25.1 MiB | 7.55 ms<br>17.8 MiB | 78.43 ms<br>18.8 MiB |
| Nested Flatmap (product sequence), depth 5 | 493.79 ms<br>44.2 MiB | 1,607.59 ms<br>30.7 MiB | 14.95 ms<br>19.8 MiB | 161.53 ms<br>21.0 MiB |
| Nested Flatmap (product sequence), depth 6 | 528.69 ms<br>45.0 MiB | 6,940.49 ms<br>35.2 MiB | 24.32 ms<br>22.2 MiB | 269.37 ms<br>23.5 MiB |
| Nested Flatmap (product), depth 2 | 8.50 ms<br>38.0 MiB | 40.19 ms<br>6.3 MiB | 0.16 ms<br>14.6 MiB | 0.73 ms<br>15.5 MiB |
| Nested Flatmap (product), depth 3 | 11.17 ms<br>38.2 MiB | 45.69 ms<br>6.5 MiB | 0.50 ms<br>14.8 MiB | 2.52 ms<br>15.7 MiB |
| Nested Flatmap (product), depth 4 | 14.94 ms<br>38.4 MiB | 57.71 ms<br>7.0 MiB | 1.21 ms<br>15.0 MiB | 6.75 ms<br>15.9 MiB |
| Nested Flatmap (product), depth 5 | 17.54 ms<br>38.5 MiB | 50.38 ms<br>7.2 MiB | 3.16 ms<br>15.3 MiB | 17.73 ms<br>16.2 MiB |
| Nested Flatmap (product), depth 6 | 19.56 ms<br>38.6 MiB | 44.52 ms<br>7.3 MiB | 7.73 ms<br>15.7 MiB | 44.93 ms<br>16.6 MiB |
| Nested Flatmap (sum), depth 4 | 629.88 ms<br>43.2 MiB | 170.79 ms<br>21.5 MiB | 18.08 ms<br>17.9 MiB | 176.27 ms<br>19.0 MiB |
| Modular Mapping | 7.86 ms<br>38.2 MiB | 1.06 ms<br>6.0 MiB | 0.06 ms<br>14.2 MiB | 0.20 ms<br>15.1 MiB |
| Weighted Linear Preservation | 21.31 ms<br>38.5 MiB | 2.06 ms<br>6.2 MiB | 0.47 ms<br>14.7 MiB | 2.65 ms<br>15.7 MiB |
| AscendingArray | 942.27 ms<br>60.7 MiB | 55.05 ms<br>7.7 MiB | 2.19 ms<br>15.0 MiB | 9.76 ms<br>15.8 MiB |
| Invoice Discount | 25.45 ms<br>38.5 MiB | 4.90 ms<br>6.3 MiB | 2.66 ms<br>15.6 MiB | 14.64 ms<br>16.6 MiB |
| Invoice Discount (derived) | 454.02 ms<br>47.0 MiB | 10.05 ms<br>6.9 MiB | 2.60 ms<br>15.8 MiB | 14.85 ms<br>16.8 MiB |
| Refund Allocation | 99.28 ms<br>41.5 MiB | 199.96 ms<br>7.8 MiB | 1.00 ms<br>15.7 MiB | 3.13 ms<br>16.7 MiB |
| Refund Allocation (derived) | 216.35 ms<br>44.4 MiB | 27.35 ms<br>7.5 MiB | 4.41 ms<br>15.9 MiB | 15.24 ms<br>17.0 MiB |
| Float Cancellation | 22.49 ms<br>38.4 MiB | 7.00 ms<br>6.8 MiB | 0.63 ms<br>14.6 MiB | 6.53 ms<br>15.5 MiB |
| Chunked Decoder | 38.76 ms<br>40.9 MiB | 47.30 ms<br>12.0 MiB | 0.49 ms<br>16.1 MiB | 1.86 ms<br>17.2 MiB |
| Hash Collision (M = 10) | 46.86 ms<br>39.4 MiB | 13.48 ms<br>7.3 MiB | 1.09 ms<br>15.0 MiB | 4.23 ms<br>16.0 MiB |
| Hash Collision (M = 100) | 104.49 ms<br>40.9 MiB | 16.93 ms<br>7.7 MiB | 3.29 ms<br>15.1 MiB | 12.77 ms<br>16.0 MiB |
| Hash Collision (M = 1000) | 1,117.16 ms<br>61.8 MiB | 29.57 ms<br>7.8 MiB | 6.34 ms<br>15.2 MiB | 16.25 ms<br>16.1 MiB |
| Snapshot Store | 2,617.18 ms<br>99.4 MiB | 995.72 ms<br>13.5 MiB | 8.00 ms<br>16.0 MiB | 33.35 ms<br>17.5 MiB |
| Hash Collision (M = 10) (state machine) | 70.15 ms<br>40.5 MiB | 135.30 ms<br>7.5 MiB | 1.84 ms<br>15.7 MiB | 8.93 ms<br>17.1 MiB |
| Hash Collision (M = 100) (state machine) | 113.31 ms<br>41.4 MiB | 142.88 ms<br>7.9 MiB | 5.61 ms<br>15.8 MiB | 20.73 ms<br>17.2 MiB |
| Hash Collision (M = 1000) (state machine) | 450.29 ms<br>46.6 MiB | 158.72 ms<br>10.2 MiB | 11.20 ms<br>15.9 MiB | 27.02 ms<br>17.3 MiB |

[Generation speed and value complexity](GENERATION.md).
