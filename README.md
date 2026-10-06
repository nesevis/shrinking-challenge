# Ad hoc shrinking challenge: Hypothesis vs Exhaust vs Hegel

A fast and loose comparison of:

- [Hypothesis](/pbt-libraries/hypothesis/README.md) 6.168.3
- [Exhaust](/pbt-libraries/exhaust/README.md) 1.5.8
- [Hegel](/pbt-libraries/hegel/README.md) 0.48.1 (native engine 0.44.1)

Library links point to each implementation of the challenge. 🎯 marks the ~minimal counterexample.

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
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Anagrams.swift) | 1239 | 🎯 `(" \0", "\0 ")` |
|  |  |  |  |
| Username and Password | [Hypothesis](/pbt-libraries/hypothesis/challenges/username_password.py) | 301 | `("u: p0000000", "p: p0000000")` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/UsernamePasswordChallenge.swift) | 731 | 🎯 `("u: 0000", "p: 0000")` |
|  |  |  |  |
| Duplicated Text | [Hypothesis](/pbt-libraries/hypothesis/challenges/duplicated_text.py) | 30 | 🎯 `("00000012", "00000012")` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/DuplicatedTextChallenge.swift) | 54 | `("10210210", "10210210")` |
|  |  |  |  |
| Haystack | [Hypothesis](/pbt-libraries/hypothesis/challenges/haystack.py) | 242 | 🎯 `"CREEPIDIOT"` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HaystackChallenge.swift) | 407 | 🎯 `"CREEPIDIOT"` |
|  |  |  |  |
| Zalgo Haystack | [Hypothesis](/pbt-libraries/hypothesis/challenges/zalgo_haystack.py) | 444 | 🎯 `"THE ICHOR PERMEATES"` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ZalgoHaystackChallenge.swift) | 461 | 🎯 `"THE ICHOR PERMEATES"` |
|  |  |  |  |
| Distinct Sum | [Hypothesis](/pbt-libraries/hypothesis/challenges/distinct_sum.py) | 133 | 🎯 `[0, 1, -1, 2, 49]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/DistinctSumChallenge.swift) | 636 | `[-2, -1, 0, 1, 53]` |
|  |  |  |  |
| Leap Day | [Hypothesis](/pbt-libraries/hypothesis/challenges/leap_day.py) | 25 | 🎯 `2000-02-29 00:00:00 +0000` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/LeapDayChallenge.swift) | 34 | `2088-02-29 00:00:00 +0000` |
|  |  |  |  |
| Branch Switching | [Hypothesis](/pbt-libraries/hypothesis/challenges/branch_switching.py) | 44 | 🎯 `1001` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/BranchSwitchingChallenge.swift) | 15 | `"    "` |

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
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/BinaryHeap.swift) | 2 | 118.9 | 95.5 | 384.4 | 66% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>34% `(0, (0, (1, None, None), None), (0, None, None))` |
|  | [Hegel](/pbt-libraries/hegel/src/binary_heap.rs) | 2 | 5837.4 | 5175.0 | 312.2 | 99% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>1% `(127, None, (55190086533789320, (401787435511877632, None, (7196582761221413107, None, None)), (7196582761221412864, (7196582761221413107, None, None), None)))` |
|  |  |  |  |  |  |  |
| Calculator | [Hypothesis](/pbt-libraries/hypothesis/challenges/calculator.py) | 1 | 90.5 | 81.0 | 125.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/Calculator.swift) | 1 | 44.1 | 45.0 | 63.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Hegel](/pbt-libraries/hegel/src/calculator.rs) | 1 | 442.5 | 442.0 | 241.9 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_2.py) | 3 | 71.5 | 63.0 | 118.4 | 43% `(8, 3, 0x23 + 1x1)`<br>39% 🎯 `(6, 4, 0x23 + 1x1)`<br>18% `(5, 5, 0x24 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L11) | 2 | 311.8 | 328.5 | 141.0 | 99% 🎯 `(6, 4, 0x23 + 1x1)`<br>1% `(9, 3, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 2 | 1274.4 | 1361.5 | 142.5 | 73% 🎯 `(6, 4, 0x23 + 1x1)`<br>27% `(8, 3, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_3.py) | 6 | 86.9 | 79.5 | 210.4 | 32% `(6, 2, 2, 0x23 + 1x1)`<br>23% `(8, 3, 1, 0x23 + 1x1)`<br>21% 🎯 `(4, 3, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L18) | 4 | 300.3 | 291.0 | 386.3 | 80% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>16% `(6, 2, 2, 0x23 + 1x1)`<br>3% `(7, 2, 2, 0x27 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 2 | 1740.1 | 1832.5 | 410.6 | 84% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>16% `(8, 3, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_4.py) | 8 | 80.5 | 72.0 | 272.1 | 27% `(8, 3, 1, 1, 0x23 + 1x1)`<br>18% `(6, 4, 1, 1, 0x23 + 1x1)`<br>14% `(4, 3, 2, 1, 0x23 + 1x1)`<br>12% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L27) | 4 | 305.6 | 214.0 | 1107.9 | 89% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)`<br>9% `(3, 3, 3, 1, 0x26 + 1x1)`<br>1% `(9, 3, 1, 1, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 3 | 1842.7 | 1841.5 | 1074.1 | 68% `(4, 3, 2, 1, 0x23 + 1x1)`<br>16% `(8, 3, 1, 1, 0x23 + 1x1)`<br>16% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_5.py) | 17 | 64.5 | 49.5 | 248.8 | 12% `(6, 4, 1, 1, 1, 0x23 + 1x1)`<br>10% `(7, 4, 1, 1, 1, 0x27 + 1x1)`<br>10% `(6, 2, 2, 1, 1, 0x23 + 1x1)`<br>4% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L38) | 11 | 708.0 | 166.5 | 3737.7 | 85% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)`<br>4% `(6, 5, 1, 1, 1, 0x29 + 1x1)`<br>2% `(3, 3, 3, 1, 1, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 4 | 1884.8 | 1788.0 | 2049.6 | 65% `(4, 3, 2, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 0x23 + 1x1)`<br>12% `(2, 2, 2, 2, 2, 0x31 + 1x1)`<br>8% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_6.py) | 20 | 62.9 | 48.5 | 261.4 | 20% `(6, 4, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)`<br>5% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L51) | 27 | 1056.9 | 146.0 | 5867.6 | 56% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>4% `(6, 5, 2, 2, 1, 1, 0x119 + 1x1)`<br>4% `(6, 5, 1, 1, 1, 1, 0x29 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 6 | 2148.0 | 1800.5 | 3735.3 | 62% `(4, 3, 2, 1, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>12% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>8% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_2.py) | 1 | 18.8 | 18.0 | 6.3 | 100% 🎯 `(5, 5)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L67) | 1 | 33.3 | 36.0 | 6.2 | 100% 🎯 `(5, 5)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 1 | 3532.3 | 3640.0 | 6.3 | 100% 🎯 `(5, 5)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_3.py) | 1 | 22.1 | 20.0 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L72) | 1 | 59.1 | 64.0 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 1 | 4171.8 | 4240.5 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_4.py) | 1 | 24.3 | 23.5 | 12.3 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L79) | 1 | 73.5 | 82.5 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 1 | 4743.4 | 4744.0 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_5.py) | 1 | 26.2 | 25.0 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L88) | 1 | 70.8 | 44.5 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 1 | 4239.9 | 4324.5 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_6.py) | 1 | 28.1 | 29.5 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L99) | 1 | 31.5 | 32.0 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L93) | 1 | 3596.3 | 2924.0 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (sum), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_sum_4.py) | 1 | 162.3 | 160.5 | 368.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/NestedBinds.swift#L113) | 1 | 735.4 | 531.5 | 344.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L105) | 1 | 3297.9 | 3287.0 | 342.9 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.py) | 12 | 20.6 | 20.0 | 3.0 | 32% 🎯 `925`<br>16% `921`<br>10% `917` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ModularMappingChallenge.swift) | 18 | 18.5 | 17.0 | 3.0 | 15% 🎯 `925`<br>13% `921`<br>10% `901` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L110) | 6 | 32.8 | 32.0 | 3.0 | 71% 🎯 `925`<br>14% `926`<br>6% `927` |
|  |  |  |  |  |  |  |
| Weighted Linear Preservation | [Hypothesis](/pbt-libraries/hypothesis/challenges/weighted_linear_preservation.py) | 8 | 53.8 | 51.0 | 9.5 | 25% `(10, 0, 0)`<br>24% `(5, 0, 10)`<br>15% 🎯 `(0, 0, 20)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/WeightedLinearPreservationChallenge.swift) | 1 | 155.4 | 94.0 | 9.6 | 100% 🎯 `(0, 0, 20)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L119) | 1 | 63.8 | 66.0 | 9.4 | 100% 🎯 `(0, 0, 20)` |
|  |  |  |  |  |  |  |
| Float Cancellation | [Hypothesis](/pbt-libraries/hypothesis/challenges/float_cancellation.py) | 82 | 66.1 | 30.0 | 41.3 | 3% `(1.0, 3.1)`<br>3% `(1.1125369292536007e-308, 1.0)`<br>3% `(1.0, 3.9)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/FloatCancellationChallenge.swift) | 82 | 9635.2 | 872.0 | 39.5 | 11% `(1.0, 65535.93750000001)`<br>9% `(-65535.93750000001, -1.0)`<br>1% `(1.0, 524287.34689438395)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L136) | 32 | 552.2 | 436.5 | 43.4 | 33% `(1.0, 524287.00000000006)`<br>23% `(1.0, 1.0000000000000002)`<br>6% `(1.0, 65535.00000000001)` |
|  |  |  |  |  |  |  |
| Chunked Decoder | [Hypothesis](/pbt-libraries/hypothesis/challenges/chunked_decoder.py) | 1 | 50.1 | 47.0 | 61.2 | 100% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ChunkedDecoderChallenge.swift) | 5 | 85.1 | 77.0 | 31.2 | 56% `(text, "\u{10000}", [3, 1])`<br>40% `(text, "\u{800}", [2, 1])`<br>2% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L143) | 70 | 1847.7 | 1630.5 | 91.9 | 8% 🎯 `(text, "\u{80}", [1, 1])`<br>6% `(text, "\u{10000}\u{10000}", [7, 1])`<br>6% `(text, "\u{10000}", [3, 1])` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_10.py) | 10 | 75.1 | 75.5 | 44.1 | 30% `([(10, 0)], 0, 1)`<br>17% `([(30, 0)], 0, 1)`<br>14% 🎯 `([(0, 0)], 10, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L46) | 1 | 199.6 | 167.5 | 29.9 | 100% 🎯 `([(0, 0)], 10, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L147) | 1 | 440.3 | 458.5 | 87.6 | 100% 🎯 `([(0, 0)], 10, 1)` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_100.py) | 8 | 132.0 | 114.5 | 64.3 | 62% `([(100, 0)], 0, 1)`<br>20% 🎯 `([(0, 0)], 100, 1)`<br>7% `([(300, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L46) | 4 | 693.3 | 617.0 | 61.8 | 70% 🎯 `([(0, 0)], 100, 1)`<br>20% `([(0, 0)], 300, 1)`<br>7% `([(0, 0)], 700, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L147) | 1 | 508.6 | 489.0 | 114.1 | 100% 🎯 `([(0, 0)], 100, 1)` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_1000.py) | 9 | 771.4 | 969.5 | 101.6 | 40% `([(1000, 0)], 0, 1)`<br>22% 🎯 `([(0, 0)], 1000, 1)`<br>13% `([(3000, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L46) | 5 | 652.7 | 651.5 | 117.5 | 71% 🎯 `([(0, 0)], 1000, 1)`<br>14% `([(0, 0)], 3000, 1)`<br>9% `([(0, 0)], 5000, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L147) | 1 | 532.3 | 544.5 | 110.0 | 100% 🎯 `([(0, 0)], 1000, 1)` |

## Handwritten and derived generators

Each challenge pairs a handwritten generator with raw type derivation. Columns and evaluation counts follow the 100 seeds table above.

Hegel's fully derived invoice uses raw signed 64-bit fields, as Exhaust's does, rather than Hypothesis's arbitrary-precision integers.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples<br><img src="assets/spacer.gif" width="1000" height="1" alt=""> |
|---|---|---|---|---|---|---|
| Invoice Discount | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount.py) | 22 | 61.5 | 57.5 | 19.6 | 40% `Invoice(28, 36, 1)`<br>8% `Invoice(201, 5, 1)`<br>6% `Invoice(11, 91, 1)`<br>4% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/InvoiceDiscountChallenge.swift#L28) | 1 | 91.4 | 83.0 | 19.7 | 100% 🎯 `Invoice(10, 100, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L127) | 1 | 657.0 | 630.0 | 19.5 | 100% 🎯 `Invoice(10, 100, 1)` |
|  |  |  |  |  |  |  |
| Invoice Discount (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount_derived.py) | 9 | 748.5 | 881.0 | 19.1 | 86% `Invoice(28, 36, 1)`<br>5% `Invoice(101, 10, 1)`<br>3% `Invoice(11, 91, 1)`<br>1% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/InvoiceDiscountChallenge.swift#L38) | 5 | 1220.5 | 769.5 | 19.0 | 69% `Invoice(15, 67, 1)`<br>12% `Invoice(14, 72, 1)`<br>8% `Invoice(13, 77, 1)` |
|  | [Hegel](/pbt-libraries/hegel/src/challenges.rs#L127) | 8 | 459.8 | 477.5 | 18.8 | 29% `Invoice(18, 56, 1)`<br>28% 🎯 `Invoice(10, 100, 1)`<br>27% `Invoice(14, 72, 1)` |
|  |  |  |  |  |  |  |
| Refund Allocation | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation.py) | 5 | 175.7 | 127.5 | 45.8 | 78% `RefundRequest([31, 34], 2)`<br>13% `RefundRequest([33, 31], 2)`<br>5% 🎯 `RefundRequest([31, 33], 4)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/RefundAllocationChallenge.swift#L31) | 1 | 903.8 | 649.0 | 78.6 | 100% 🎯 `RefundRequest([31, 33], 4)` |
|  | [Hegel](/pbt-libraries/hegel/src/refund_allocation.rs#L153) | 5 | 1498.0 | 1438.0 | 60.8 | 96% 🎯 `RefundRequest([31, 33], 4)`<br>1% `RefundRequest([31, 36], 3)`<br>1% `RefundRequest([31, 35183], 2386)` |
|  |  |  |  |  |  |  |
| Refund Allocation (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation_derived.py) | 4 | 129.3 | 108.5 | 46.1 | 69% `RefundRequest([33, 31], 2)`<br>28% `RefundRequest([31, 34], 2)`<br>2% `RefundRequest([31, 31, 33], 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/RefundAllocationChallenge.swift#L46) | 6 | 9134.6 | 769.5 | 55.6 | 32% `RefundRequest([31, 31, 33], 3)`<br>31% 🎯 `RefundRequest([31, 33], 4)`<br>28% `RefundRequest([33, 31], 2)` |
|  | [Hegel](/pbt-libraries/hegel/src/refund_allocation.rs#L153) | 7 | 168.3 | 116.0 | 42.6 | 80% `RefundRequest([31, 34], 2)`<br>15% 🎯 `RefundRequest([31, 33], 4)`<br>1% `RefundRequest([61, 5079374505385], 62852702378)` |

## State machines

The recorded results cover 100 seeded state machine tests per library, generating command histories of up to 50 commands and reducing the first failing history. Exhaust uses `.commandLimit(50)` and Hegel uses `.steps(50)`, to match Hypothesis's default `stateful_step_count`.

The Hash Collision rows run the same frame property as the generator rows above, checked after every put. Together, the two tables show how each library's reduction changes with the encoding.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples<br><img src="assets/spacer.gif" width="1000" height="1" alt=""> |
|---|---|---|---|---|---|---|
| Snapshot Store | [Hypothesis](/pbt-libraries/hypothesis/challenges/snapshot_store.py) | 21 | 431.3 | 377.5 | 456.9 | 37% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>18% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]`<br>7% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/SnapshotStoreChallenge.swift) | 17 | 241.4 | 215.0 | 497.0 | 67% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>6% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]`<br>5% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L33) | 5 | 2268.7 | 1908.0 | 484.9 | 71% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>17% `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]`<br>10% `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_10.py) | 77 | 34.4 | 32.0 | 59.0 | 7% 🎯 `[put(0, 0), put(10, 1)]`<br>5% `[put(30, 0), put(0, 1)]`<br>4% `[put(0, 0), put(30, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L83) | 1 | 222.5 | 178.0 | 355.0 | 100% 🎯 `[put(0, 0), put(10, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L24) | 1 | 407.6 | 376.0 | 60.4 | 100% 🎯 `[put(0, 0), put(10, 1)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_100.py) | 59 | 46.5 | 45.0 | 184.5 | 39% 🎯 `[put(0, 0), put(100, 1)]`<br>2% `[put(499, 0), put(99, 1)]`<br>2% `[put(100, 0), put(0, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L100) | 3 | 747.9 | 715.5 | 421.7 | 80% 🎯 `[put(0, 0), put(100, 1)]`<br>14% `[put(0, 0), put(300, 1)]`<br>6% `[put(0, 0), put(700, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L24) | 1 | 298.1 | 292.0 | 210.2 | 100% 🎯 `[put(0, 0), put(100, 1)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_1000.py) | 98 | 103.5 | 107.0 | 434.6 | 2% `[put(140, 0), put(1140, 1)]`<br>2% `[put(4148, 0), put(148, 1)]`<br>1% `[put(3871, 0), put(7871, 1)]`<br>1% 🎯 `[put(0, 0), put(1000, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/HashCollisionChallenge.swift#L117) | 5 | 730.3 | 706.0 | 512.5 | 36% 🎯 `[put(0, 0), put(1000, 1)]`<br>23% `[put(0, 0), put(9000, 1)]`<br>15% `[put(0, 0), put(3000, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/src/stateful.rs#L24) | 1 | 348.1 | 353.5 | 418.3 | 100% 🎯 `[put(0, 0), put(1000, 1)]` |


## Timings

Mean wall-clock milliseconds / mean peak resident memory in MiB per single-threaded run on an Apple M4 Max, over the same runs as the tables above.

Each column is the build a developer gets by default on that platform:

- **Hypothesis**: Hypothesis 6.168.3 on Python 3.12. Its recorded `total_seconds` includes the final replay.
- **Hegel (default/opt-1)**: `cargo build` without the `static-engine` feature. The runner is unoptimised and loads `libhegel_c` as a shared library built at Cargo's dev-profile `opt-level = 1`. Covers generation, reduction, counterexample recording, confirmation calls and final replay.
- **Exhaust (macOS)**: the 1.5.8 package with the runner built in debug. On Apple platforms the package links a prebuilt, optimised `ExhaustCore` XCFramework. Its `wallMilliseconds` covers generation and reduction; Exhaust makes no final replay.
- **Exhaust (Linux/Windows)**: the same 1.5.8 source built entirely in debug, as on platforms without the XCFramework, where `ExhaustCore` is compiled from source alongside the test target.

Hegel (default/opt-1) stops one depth-6 run (seed 1361) at its 300-second shrink deadline, ending at a larger counterexample than the release build reaches. 

Exhaust (Linux/Windows) stops three runs at each of depths 5 and 6 (seeds 1388, 1403 and 1404) at its 125-second reduction deadline.

| Challenge | Hypothesis | Hegel (default/opt-1) | Exhaust (macOS) | Exhaust (Linux/Windows) |
|---|---|---|---|---|
| Anagrams | 172.95 ms<br>40.5 MiB | — | 22.96 ms<br>15.6 MiB | 66.75 ms<br>16.8 MiB |
| Username and Password | 41.12 ms<br>38.7 MiB | — | 4.59 ms<br>15.1 MiB | 21.35 ms<br>16.2 MiB |
| Duplicated Text | 8.65 ms<br>37.7 MiB | — | 1.32 ms<br>14.7 MiB | 4.05 ms<br>15.9 MiB |
| Haystack | 116.59 ms<br>39.1 MiB | — | 11.24 ms<br>18.6 MiB | 67.08 ms<br>19.9 MiB |
| Zalgo Haystack | 2,994.38 ms<br>41.6 MiB | — | 16.75 ms<br>22.7 MiB | 110.07 ms<br>23.8 MiB |
| Distinct Sum | 46.29 ms<br>38.1 MiB | — | 2.75 ms<br>14.4 MiB | 8.28 ms<br>15.5 MiB |
| Leap Day | 9.18 ms<br>37.0 MiB | — | 3.70 ms<br>17.0 MiB | 4.21 ms<br>17.8 MiB |
| Branch Switching | 11.47 ms<br>38.3 MiB | — | 2.03 ms<br>15.7 MiB | 4.04 ms<br>16.9 MiB |
| Binary Heap | 133.68 ms<br>40.1 MiB | 700.81 ms<br>26.3 MiB | 5.82 ms<br>16.4 MiB | 27.60 ms<br>17.8 MiB |
| Calculator | 1,499.83 ms<br>61.6 MiB | 194.23 ms<br>8.2 MiB | 0.68 ms<br>15.3 MiB | 3.27 ms<br>16.5 MiB |
| Nested Flatmap (product sequence), depth 2 | 229.91 ms<br>39.9 MiB | 141.89 ms<br>11.8 MiB | 3.41 ms<br>15.6 MiB | 40.87 ms<br>16.7 MiB |
| Nested Flatmap (product sequence), depth 3 | 401.54 ms<br>41.8 MiB | 221.14 ms<br>19.9 MiB | 6.34 ms<br>16.2 MiB | 66.67 ms<br>17.4 MiB |
| Nested Flatmap (product sequence), depth 4 | 417.64 ms<br>43.3 MiB | 398.79 ms<br>32.0 MiB | 45.54 ms<br>17.6 MiB | 313.94 ms<br>18.9 MiB |
| Nested Flatmap (product sequence), depth 5 | 493.79 ms<br>44.2 MiB | 1,510.60 ms<br>38.8 MiB | 1,055.70 ms<br>21.8 MiB | 4,326.29 ms<br>22.7 MiB |
| Nested Flatmap (product sequence), depth 6 | 528.69 ms<br>45.0 MiB | 6,480.88 ms<br>45.2 MiB | 2,176.61 ms<br>28.9 MiB | 6,881.07 ms<br>30.3 MiB |
| Nested Flatmap (product), depth 2 | 8.50 ms<br>38.0 MiB | 36.93 ms<br>6.0 MiB | 0.27 ms<br>14.3 MiB | 1.02 ms<br>15.3 MiB |
| Nested Flatmap (product), depth 3 | 11.17 ms<br>38.2 MiB | 41.93 ms<br>6.3 MiB | 0.94 ms<br>14.5 MiB | 3.95 ms<br>15.6 MiB |
| Nested Flatmap (product), depth 4 | 14.94 ms<br>38.4 MiB | 53.16 ms<br>6.8 MiB | 2.45 ms<br>14.7 MiB | 11.33 ms<br>15.8 MiB |
| Nested Flatmap (product), depth 5 | 17.54 ms<br>38.5 MiB | 47.21 ms<br>7.1 MiB | 6.31 ms<br>15.1 MiB | 30.28 ms<br>16.3 MiB |
| Nested Flatmap (product), depth 6 | 19.56 ms<br>38.6 MiB | 42.59 ms<br>7.2 MiB | 14.26 ms<br>15.5 MiB | 71.51 ms<br>16.8 MiB |
| Nested Flatmap (sum), depth 4 | 629.88 ms<br>43.2 MiB | 164.02 ms<br>25.8 MiB | 19.95 ms<br>17.5 MiB | 217.13 ms<br>18.7 MiB |
| Modular Mapping | 7.86 ms<br>38.2 MiB | 0.96 ms<br>5.7 MiB | 0.06 ms<br>13.9 MiB | 0.20 ms<br>15.0 MiB |
| Weighted Linear Preservation | 21.31 ms<br>38.5 MiB | 2.08 ms<br>5.9 MiB | 0.51 ms<br>14.2 MiB | 2.14 ms<br>15.4 MiB |
| Invoice Discount | 25.45 ms<br>38.5 MiB | 4.60 ms<br>6.1 MiB | 1.67 ms<br>15.0 MiB | 5.90 ms<br>16.3 MiB |
| Invoice Discount (derived) | 454.02 ms<br>47.0 MiB | 10.92 ms<br>6.7 MiB | 2.66 ms<br>15.2 MiB | 11.08 ms<br>16.4 MiB |
| Refund Allocation | 99.28 ms<br>41.5 MiB | 193.90 ms<br>7.6 MiB | 10.13 ms<br>15.3 MiB | 22.16 ms<br>16.4 MiB |
| Refund Allocation (derived) | 216.35 ms<br>44.4 MiB | 26.63 ms<br>7.4 MiB | 41.91 ms<br>15.8 MiB | 129.20 ms<br>17.0 MiB |
| Float Cancellation | 22.49 ms<br>38.4 MiB | 6.72 ms<br>6.4 MiB | 17.19 ms<br>14.3 MiB | 242.09 ms<br>15.5 MiB |
| Chunked Decoder | 38.76 ms<br>40.9 MiB | 49.27 ms<br>12.0 MiB | 1.07 ms<br>15.7 MiB | 3.00 ms<br>16.9 MiB |
| Hash Collision (M = 10) | 46.86 ms<br>39.4 MiB | 12.99 ms<br>7.1 MiB | 1.12 ms<br>14.5 MiB | 3.35 ms<br>15.6 MiB |
| Hash Collision (M = 100) | 104.49 ms<br>40.9 MiB | 16.46 ms<br>7.5 MiB | 3.22 ms<br>14.6 MiB | 9.20 ms<br>15.7 MiB |
| Hash Collision (M = 1000) | 1,117.16 ms<br>61.8 MiB | 38.60 ms<br>7.9 MiB | 5.94 ms<br>14.7 MiB | 12.70 ms<br>15.8 MiB |
| Snapshot Store | 2,617.18 ms<br>99.4 MiB | 1,010.38 ms<br>14.3 MiB | 8.92 ms<br>16.2 MiB | 32.85 ms<br>17.5 MiB |
| Hash Collision (M = 10) (state machine) | 70.15 ms<br>40.5 MiB | 127.65 ms<br>7.4 MiB | 2.06 ms<br>15.7 MiB | 7.63 ms<br>16.9 MiB |
| Hash Collision (M = 100) (state machine) | 113.31 ms<br>41.4 MiB | 134.54 ms<br>7.9 MiB | 5.94 ms<br>15.8 MiB | 16.96 ms<br>17.0 MiB |
| Hash Collision (M = 1000) (state machine) | 450.29 ms<br>46.6 MiB | 152.28 ms<br>10.6 MiB | 11.09 ms<br>15.9 MiB | 23.16 ms<br>17.2 MiB |
