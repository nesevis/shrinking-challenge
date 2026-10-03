# Shrinking Challenge: Hypothesis vs Exhaust vs Hegel

A comparison of [Hypothesis](/pbt-libraries/hypothesis/README.md) 6.168.3, [Exhaust](/pbt-libraries/exhaust/README.md) 1.5.5, and [Hegel](/pbt-libraries/hegel/README.md) 0.48.1 (native engine 0.44.1) on seeded and fixed-start shrinking challenges.

Links point to challenge reports or verification artifacts. 🎯 marks the ~minimal counterexample.

## Fixed start

Hypothesis and Exhaust reduce the same fixed failing input once, with no generation phase. Fixed-start rows use each runner's reported evaluation count directly; the +1 adjustment to Exhaust applies to the generated rows below.

| Challenge | Library | Evaluations | Counterexample |
|---|---|---|---|
| Anagrams | [Hypothesis](/pbt-libraries/hypothesis/challenges/anagrams.md) | 798 | `("000000000000000000000000011", "000000000000000000000000110")` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/anagrams.md) | 1239 | 🎯 `(" \0", "\0 ")` |
|  |  |  |  |
| Username and Password | [Hypothesis](/pbt-libraries/hypothesis/challenges/username_password.md) | 301 | `("u: p0000000", "p: p0000000")` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/usernamePassword.md) | 731 | 🎯 `("u: 0000", "p: 0000")` |
|  |  |  |  |
| Duplicated Text | [Hypothesis](/pbt-libraries/hypothesis/challenges/duplicated_text.md) | 30 | 🎯 `("00000012", "00000012")` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/duplicatedText.md) | 54 | `("10210210", "10210210")` |
|  |  |  |  |
| Haystack | [Hypothesis](/pbt-libraries/hypothesis/challenges/haystack.md) | 242 | 🎯 `"CREEPIDIOT"` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/haystack.md) | 407 | 🎯 `"CREEPIDIOT"` |
|  |  |  |  |
| Zalgo Haystack | [Hypothesis](/challenges/zalgo-haystack.md#verification) | 444 | 🎯 `"THE ICHOR PERMEATES"` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/zalgoHaystack.md) | 461 | 🎯 `"THE ICHOR PERMEATES"` |
|  |  |  |  |
| Distinct Sum | [Hypothesis](/pbt-libraries/hypothesis/challenges/distinct_sum.md) | 133 | 🎯 `[0, 1, -1, 2, 49]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/distinctSum.md) | 130 | `[-2, -1, 0, 1, 53]` |
|  |  |  |  |
| Leap Day | [Hypothesis](/pbt-libraries/hypothesis/challenges/leap_day.md) | 25 | 🎯 `2000-02-29 00:00:00 +0000` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/leapDay.md) | 34 | `2088-02-29 00:00:00 +0000` |
|  |  |  |  |
| Branch Switching | [Hypothesis](/pbt-libraries/hypothesis/challenges/branch_switching.md) | 44 | 🎯 `1001` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/branchSwitching.md) | 16 | `"    "` |

## 100 seeds

Each library generated and reduced a failure in each of 100 seeded runs.

Exhaust and Hegel use 100 consecutive seeds starting at 1337. Hypothesis hashes each challenge's filename with SHA1 to seed a PRNG, then draws 100 seeds from it.

- **Top counterexamples**: the share of runs ending at each counterexample. The top three are shown, followed by the minimal counterexample if it occurred outside them.
- **Distinct CEs**: the number of different counterexamples across the 100 runs.
- **Mean evaluations / Median evaluations**: both calculated across the 100 runs, using the counting conventions below.
- **Mean original length**: the average character length of the first failing input's rendering, with nested flatmap payloads unabbreviated. Quoting and Unicode escape conventions differ between libraries.

Calculator's Hegel generator uses signed-64-bit leaves and a maximum depth of 5; Hypothesis's integer and recursive expression domains are unbounded. Hegel evaluates with exact widened arithmetic and Python-style floor division, while Exhaust uses wrapping addition and truncating division.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples |
|---|---|---|---|---|---|---|
| Binary Heap | [Hypothesis](/pbt-libraries/hypothesis/challenges/binheap.md) | 3 | 102.5 | 97.5 | 151.1 | 85% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>14% `(0, None, (0, None, (0, (0, None, None), (1, None, None))))`<br>1% `(0, None, (0, (0, None, None), (0, None, (1, None, None))))` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/binaryHeap.md) | 2 | 128.5 | 105.5 | 384.4 | 66% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>34% `(0, (0, (1, None, None), None), (0, None, None))` |
|  | [Hegel](/pbt-libraries/hegel/reports/binheap.md) | 2 | 5837.4 | 5175.0 | 312.2 | 99% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>1% `(127, None, (55190086533789320, (401787435511877632, None, (7196582761221413107, None, None)), (7196582761221412864, (7196582761221413107, None, None), None)))` |
|  |  |  |  |  |  |  |
| Calculator | [Hypothesis](/pbt-libraries/hypothesis/challenges/calculator.md) | 1 | 90.5 | 81.0 | 125.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/calculator.md) | 1 | 50.1 | 51.0 | 63.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Hegel](/pbt-libraries/hegel/reports/calculator.md) | 1 | 442.5 | 442.0 | 241.9 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_2.md) | 3 | 71.5 | 63.0 | 118.4 | 43% `(8, 3, 0x23 + 1x1)`<br>39% 🎯 `(6, 4, 0x23 + 1x1)`<br>18% `(5, 5, 0x24 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthTwoProductSequenceBind.md) | 2 | 311.8 | 328.5 | 141.0 | 99% 🎯 `(6, 4, 0x23 + 1x1)`<br>1% `(9, 3, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_2.md) | 2 | 1274.4 | 1361.5 | 142.5 | 73% 🎯 `(6, 4, 0x23 + 1x1)`<br>27% `(8, 3, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_3.md) | 6 | 86.9 | 79.5 | 210.4 | 32% `(6, 2, 2, 0x23 + 1x1)`<br>23% `(8, 3, 1, 0x23 + 1x1)`<br>21% 🎯 `(4, 3, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthThreeProductSequenceBind.md) | 5 | 275.0 | 277.5 | 386.3 | 67% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>22% `(6, 2, 2, 0x23 + 1x1)`<br>5% `(8, 3, 1, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_3.md) | 2 | 1740.1 | 1832.5 | 410.6 | 84% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>16% `(8, 3, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_4.md) | 8 | 80.5 | 72.0 | 272.1 | 27% `(8, 3, 1, 1, 0x23 + 1x1)`<br>18% `(6, 4, 1, 1, 0x23 + 1x1)`<br>14% `(4, 3, 2, 1, 0x23 + 1x1)`<br>12% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthFourProductSequenceBind.md) | 7 | 298.5 | 214.0 | 1107.9 | 83% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)`<br>9% `(3, 3, 3, 1, 0x26 + 1x1)`<br>3% `(9, 3, 1, 1, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_4.md) | 3 | 1842.7 | 1841.5 | 1074.1 | 68% `(4, 3, 2, 1, 0x23 + 1x1)`<br>16% `(8, 3, 1, 1, 0x23 + 1x1)`<br>16% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_5.md) | 17 | 64.5 | 49.5 | 248.8 | 12% `(6, 4, 1, 1, 1, 0x23 + 1x1)`<br>10% `(7, 4, 1, 1, 1, 0x27 + 1x1)`<br>10% `(6, 2, 2, 1, 1, 0x23 + 1x1)`<br>4% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthFiveProductSequenceBind.md) | 24 | 692.8 | 154.5 | 3737.7 | 71% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)`<br>2% `(9, 2, 2, 2, 1, 0x71 + 1x1)`<br>2% `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_5.md) | 4 | 1884.8 | 1788.0 | 2049.6 | 65% `(4, 3, 2, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 0x23 + 1x1)`<br>12% `(2, 2, 2, 2, 2, 0x31 + 1x1)`<br>8% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_6.md) | 20 | 62.8 | 48.5 | 261.4 | 20% `(6, 4, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)`<br>5% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthSixProductSequenceBind.md) | 43 | 1040.6 | 111.5 | 5867.6 | 47% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>3% `(5, 5, 5, 1, 1, 1, 0x124 + 1x1)`<br>2% `(9, 3, 1, 1, 1, 1, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_6.md) | 5 | 2273.6 | 1800.5 | 3735.3 | 63% `(4, 3, 2, 1, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>12% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>8% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_2.md) | 1 | 18.8 | 18.0 | 6.3 | 100% 🎯 `(5, 5)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthTwoProductBind.md) | 1 | 30.4 | 33.0 | 6.2 | 100% 🎯 `(5, 5)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_2.md) | 1 | 3532.3 | 3640.0 | 6.3 | 100% 🎯 `(5, 5)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_3.md) | 1 | 22.1 | 20.0 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthThreeProductBind.md) | 1 | 59.1 | 64.0 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_3.md) | 1 | 4171.8 | 4240.5 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_4.md) | 1 | 24.3 | 23.5 | 12.3 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthFourProductBind.md) | 1 | 73.4 | 82.5 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_4.md) | 1 | 4743.4 | 4744.0 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_5.md) | 1 | 26.2 | 25.0 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthFiveProductBind.md) | 1 | 70.8 | 44.5 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_5.md) | 1 | 4239.9 | 4324.5 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (product), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_6.md) | 1 | 28.1 | 29.5 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthSixProductBind.md) | 1 | 31.5 | 32.0 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_6.md) | 1 | 3596.3 | 2924.0 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  |  |  |  |  |  |  |
| Nested Flatmap (sum), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_sum_4.md) | 1 | 162.3 | 160.5 | 368.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthFourSumBind.md) | 1 | 735.4 | 531.5 | 344.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_sum_4.md) | 1 | 3297.9 | 3287.0 | 342.9 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  |  |  |  |  |  |  |
| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.md) | 12 | 20.6 | 20.0 | 3.0 | 32% 🎯 `925`<br>16% `921`<br>10% `917` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/modularMapping.md) | 18 | 18.5 | 17.0 | 3.0 | 15% 🎯 `925`<br>13% `921`<br>10% `901` |
|  | [Hegel](/pbt-libraries/hegel/reports/modular_mapping.md) | 6 | 32.8 | 32.0 | 3.0 | 71% 🎯 `925`<br>14% `926`<br>6% `927` |
|  |  |  |  |  |  |  |
| Weighted Linear Preservation | [Hypothesis](/pbt-libraries/hypothesis/challenges/weighted_linear_preservation.md) | 8 | 53.8 | 51.0 | 9.5 | 25% `(10, 0, 0)`<br>24% `(5, 0, 10)`<br>15% 🎯 `(0, 0, 20)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/weightedLinearPreservation.md) | 11 | 43.0 | 44.0 | 9.6 | 22% 🎯 `(0, 0, 20)`<br>16% `(2, 0, 16)`<br>14% `(1, 0, 18)` |
|  | [Hegel](/pbt-libraries/hegel/reports/weighted_linear_preservation.md) | 1 | 63.8 | 66.0 | 9.4 | 100% 🎯 `(0, 0, 20)` |
|  |  |  |  |  |  |  |
| Float Cancellation | [Hypothesis](/pbt-libraries/hypothesis/challenges/float_cancellation.md) | 82 | 66.1 | 30.0 | 41.3 | 3% `(1.0, 3.1)`<br>3% `(1.1125369292536007e-308, 1.0)`<br>3% `(1.0, 3.9)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/floatCancellation.md) | 100 | 307.0 | 268.5 | 39.5 | 1% `(208381.0, 315907.7322945033)`<br>1% `(-674879.0, -373697.223055313)`<br>1% `(-380887.9292787704, -143401.0)` |
|  | [Hegel](/pbt-libraries/hegel/reports/float_cancellation.md) | 32 | 552.2 | 436.5 | 43.4 | 33% `(1.0, 524287.00000000006)`<br>23% `(1.0, 1.0000000000000002)`<br>6% `(1.0, 65535.00000000001)` |
|  |  |  |  |  |  |  |
| Chunked Decoder | [Hypothesis](/pbt-libraries/hypothesis/challenges/chunked_decoder.md) | 1 | 50.2 | 47.0 | 61.8 | 100% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/chunkedDecoder.md) | 5 | 85.1 | 77.0 | 31.2 | 56% `(text, "\u{10000}", [3, 1])`<br>40% `(text, "\u{800}", [2, 1])`<br>2% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Hegel](/pbt-libraries/hegel/reports/chunked_decoder.md) | 70 | 1847.7 | 1630.5 | 91.9 | 8% 🎯 `(text, "\u{80}", [1, 1])`<br>6% `(text, "\u{10000}\u{10000}", [7, 1])`<br>6% `(text, "\u{10000}", [3, 1])` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_10.md) | 10 | 75.1 | 75.5 | 44.1 | 30% `([(10, 0)], 0, 1)`<br>17% `([(30, 0)], 0, 1)`<br>14% 🎯 `([(0, 0)], 10, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollisionTen.md) | 6 | 71.2 | 74.0 | 29.9 | 64% 🎯 `([(0, 0)], 10, 1)`<br>12% `([(1, 0)], 11, 1)`<br>11% `([(0, 0)], 70, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_10.md) | 1 | 440.3 | 458.5 | 87.6 | 100% 🎯 `([(0, 0)], 10, 1)` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_100.md) | 8 | 131.9 | 114.5 | 64.3 | 62% `([(100, 0)], 0, 1)`<br>20% 🎯 `([(0, 0)], 100, 1)`<br>7% `([(300, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollisionHundred.md) | 5 | 107.8 | 105.5 | 61.8 | 54% 🎯 `([(0, 0)], 100, 1)`<br>20% `([(0, 0)], 300, 1)`<br>16% `([(0, 0)], 500, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_100.md) | 1 | 508.6 | 489.0 | 114.1 | 100% 🎯 `([(0, 0)], 100, 1)` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_1000.md) | 9 | 771.1 | 969.5 | 101.6 | 40% `([(1000, 0)], 0, 1)`<br>22% 🎯 `([(0, 0)], 1000, 1)`<br>13% `([(3000, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollisionThousand.md) | 5 | 144.1 | 142.5 | 117.5 | 71% 🎯 `([(0, 0)], 1000, 1)`<br>14% `([(0, 0)], 3000, 1)`<br>9% `([(0, 0)], 5000, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_1000.md) | 1 | 532.3 | 544.5 | 110.0 | 100% 🎯 `([(0, 0)], 1000, 1)` |

How each library counts evaluations:

- **Hypothesis and Hegel** count every completed property call from the original failing input onwards. That includes any further generation calls after the first failure, and the final replay of the reduced counterexample.
- **Hegel** also counts its confirmation calls. Both harnesses exclude assumption rejections and overruns that never reach a property verdict from failure recording and evaluation counts. For state machines, an evaluation is a whole command history, not an individual command.
- **Exhaust** reports only the calls made during reduction, so both its mean and median here have 1 added to count the original failing input. Exhaust makes no final replay. Binary Heap's reduction mean of 127.5 is therefore shown as 128.5, and Calculator's 53.2 as 54.2.

## Handwritten and derived generators

Each challenge pairs a handwritten generator with raw type derivation. Columns and evaluation counts follow the 100 seeds table above.

Hegel's fully derived invoice uses raw signed 64-bit fields, as Exhaust's does, rather than Hypothesis's arbitrary-precision integers.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples |
|---|---|---|---|---|---|---|
| Invoice Discount | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount.md) | 22 | 61.5 | 57.5 | 19.6 | 40% `Invoice(28, 36, 1)`<br>8% `Invoice(201, 5, 1)`<br>6% `Invoice(11, 91, 1)`<br>4% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/invoiceDiscount.md) | 4 | 59.4 | 56.0 | 19.7 | 84% `Invoice(12, 84, 1)`<br>11% `Invoice(11, 91, 1)`<br>4% 🎯 `Invoice(10, 100, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/invoice_discount.md) | 1 | 657.0 | 630.0 | 19.5 | 100% 🎯 `Invoice(10, 100, 1)` |
|  |  |  |  |  |  |  |
| Invoice Discount (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount_derived.md) | 9 | 748.8 | 881.0 | 19.1 | 86% `Invoice(28, 36, 1)`<br>5% `Invoice(101, 10, 1)`<br>3% `Invoice(11, 91, 1)`<br>1% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/invoiceDiscountDerived.md) | 16 | 120.4 | 122.5 | 19.0 | 14% `Invoice(25, 40, 1)`<br>14% `Invoice(15, 67, 1)`<br>12% `Invoice(14, 72, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/invoice_discount_derived.md) | 8 | 459.8 | 477.5 | 18.8 | 29% `Invoice(18, 56, 1)`<br>28% 🎯 `Invoice(10, 100, 1)`<br>27% `Invoice(14, 72, 1)` |
|  |  |  |  |  |  |  |
| Refund Allocation | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation.json) | 5 | 175.7 | 127.5 | 45.8 | 78% `RefundRequest([31, 34], 2)`<br>13% `RefundRequest([33, 31], 2)`<br>5% 🎯 `RefundRequest([31, 33], 4)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/refundAllocation.md) | 2 | 884.4 | 629.0 | 78.6 | 98% `RefundRequest([31, 34], 2)`<br>2% 🎯 `RefundRequest([31, 33], 4)` |
|  | [Hegel](/pbt-libraries/hegel/reports/refund_allocation.md) | 5 | 1498.0 | 1438.0 | 60.8 | 96% 🎯 `RefundRequest([31, 33], 4)`<br>1% `RefundRequest([31, 36], 3)`<br>1% `RefundRequest([31, 35183], 2386)` |
|  |  |  |  |  |  |  |
| Refund Allocation (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation_derived.json) | 4 | 129.4 | 108.5 | 46.1 | 69% `RefundRequest([33, 31], 2)`<br>28% `RefundRequest([31, 34], 2)`<br>2% `RefundRequest([31, 31, 33], 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/refundAllocationDerived.md) | 6 | 9134.6 | 769.5 | 55.6 | 32% `RefundRequest([31, 31, 33], 3)`<br>31% 🎯 `RefundRequest([31, 33], 4)`<br>28% `RefundRequest([33, 31], 2)` |
|  | [Hegel](/pbt-libraries/hegel/reports/refund_allocation_derived.md) | 7 | 168.3 | 116.0 | 42.6 | 80% `RefundRequest([31, 34], 2)`<br>15% 🎯 `RefundRequest([31, 33], 4)`<br>1% `RefundRequest([61, 5079374505385], 62852702378)` |

## State machines

The recorded results cover 100 seeded state machine tests per library, generating command histories of up to 50 commands and reducing the first failing history. Exhaust uses `.commandLimit(50)` and Hegel uses `.steps(50)`, to match Hypothesis's default `stateful_step_count`.

The columns are as in the 100 seeds table, with the same +1 added to Exhaust's evaluations.

The Hash Collision rows run the same frame property as the generator rows above, checked after every put. Together, the two tables show how each library's reduction changes with the encoding.

| Challenge | Library | Distinct CEs | Mean evaluations | Median evaluations | Mean original length | Top counterexamples |
|---|---|---|---|---|---|---|
| Snapshot Store | [Hypothesis](/pbt-libraries/hypothesis/challenges/snapshot_store.md) | 21 | 430.9 | 377.5 | 456.9 | 37% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>18% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]`<br>7% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/snapshotStore.md) | 17 | 230.7 | 205.5 | 497.0 | 67% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>6% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]`<br>5% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/snapshot_store.md) | 5 | 2268.7 | 1908.0 | 484.9 | 71% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>17% `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]`<br>10% `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_10.md) | 77 | 34.4 | 32.0 | 59.0 | 7% 🎯 `[put(0, 0), put(10, 1)]`<br>5% `[put(30, 0), put(0, 1)]`<br>4% `[put(0, 0), put(30, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollisionStateMachineTen.md) | 6 | 77.7 | 80.0 | 355.0 | 60% 🎯 `[put(0, 0), put(10, 1)]`<br>18% `[put(0, 1), put(10, 0)]`<br>10% `[put(0, 0), put(70, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_state_machine_10.md) | 1 | 407.6 | 376.0 | 60.4 | 100% 🎯 `[put(0, 0), put(10, 1)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_100.md) | 59 | 46.5 | 45.0 | 184.5 | 39% 🎯 `[put(0, 0), put(100, 1)]`<br>2% `[put(499, 0), put(99, 1)]`<br>2% `[put(100, 0), put(0, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollisionStateMachineHundred.md) | 8 | 110.1 | 108.0 | 421.7 | 33% 🎯 `[put(0, 0), put(100, 1)]`<br>20% `[put(0, 1), put(100, 0)]`<br>13% `[put(0, 0), put(300, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_state_machine_100.md) | 1 | 298.1 | 292.0 | 210.2 | 100% 🎯 `[put(0, 0), put(100, 1)]` |
|  |  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_1000.md) | 98 | 103.5 | 107.0 | 434.6 | 2% `[put(140, 0), put(1140, 1)]`<br>2% `[put(4148, 0), put(148, 1)]`<br>1% `[put(3871, 0), put(7871, 1)]`<br>1% 🎯 `[put(0, 0), put(1000, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollisionStateMachineThousand.md) | 9 | 159.0 | 154.5 | 512.5 | 30% `[put(0, 1), put(1000, 0)]`<br>28% 🎯 `[put(0, 0), put(1000, 1)]`<br>10% `[put(0, 0), put(3000, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_state_machine_1000.md) | 1 | 348.1 | 353.5 | 418.3 | 100% 🎯 `[put(0, 0), put(1000, 1)]` |


## Apples-to-oranges timings

Mean milliseconds per run. Exhaust and Hegel used release builds on an Apple M4 Max; Hypothesis ran on Python 3.12.

- **Generation** is Hypothesis's generate phase and Exhaust's reported generation metric. Exhaust's state-machine generation column uses total interpreter time minus reduction time, including interpreter overhead. Fixed-start challenges have no generation phase.
- **Reduction** is Hypothesis's shrink phase and Exhaust's reduction time.

Hegel's Rust API exposes only total durations, reported below.

| Challenge | Hypothesis generation (ms) | Exhaust generation (ms) | Hypothesis reduction (ms) | Exhaust reduction (ms) |
|---|---|---|---|---|
| Anagrams | — | — | 177 | 7.89 |
| Username and Password | — | — | 39.48 | 2.81 |
| Duplicated Text | — | — | 5.23 | 0.34 |
| Haystack | — | — | 112 | 6.55 |
| Zalgo Haystack | — | — | 2,872.52 | 10.73 |
| Distinct Sum | — | — | 47.81 | 0.49 |
| Leap Day | — | — | 8.83 | 0.22 |
| Branch Switching | — | — | 5.62 | 0.24 |
| Binary Heap | 60.69 | 0.073 | 75.30 | 4.72 |
| Calculator | 1496.90 | 0.038 | 40.03 | 0.45 |
| Nested Flatmap (product sequence), depth 2 | 13.37 | 0.019 | 215 | 2.90 |
| Nested Flatmap (product sequence), depth 3 | 19.65 | 0.041 | 381 | 6.33 |
| Nested Flatmap (product sequence), depth 4 | 32.10 | 0.107 | 385 | 63.12 |
| Nested Flatmap (product sequence), depth 5 | 38.21 | 0.343 | 455 | 992.03 |
| Nested Flatmap (product sequence), depth 6 | 40.26 | 0.527 | 486 | 2,676.22 |
| Nested Flatmap (product), depth 2 | 4.05 | 0.004 | 3.35 | 0.18 |
| Nested Flatmap (product), depth 3 | 4.16 | 0.005 | 5.72 | 0.78 |
| Nested Flatmap (product), depth 4 | 4.35 | 0.006 | 9.36 | 2.19 |
| Nested Flatmap (product), depth 5 | 4.65 | 0.008 | 11.49 | 5.98 |
| Nested Flatmap (product), depth 6 | 4.88 | 0.010 | 13.56 | 13.74 |
| Nested Flatmap (sum), depth 4 | 12.56 | 0.049 | 591 | 36.88 |
| Modular Mapping | 4.33 | 0.003 | 3.23 | 0.03 |
| Weighted Linear Preservation | 14.36 | 0.035 | 7.92 | 0.10 |
| Invoice Discount | 3.87 | 0.005 | 21.48 | 0.30 |
| Invoice Discount (derived) | 414 | 0.367 | 22.36 | 0.24 |
| Float Cancellation | 4.29 | 0.007 | 16.63 | 0.58 |
| Chunked Decoder | 7.55 | 0.021 | 29.32 | 0.62 |
| Hash Collision (M = 10) | 19.71 | 0.030 | 31.47 | 0.30 |
| Hash Collision (M = 100) | 76.11 | 0.091 | 34.49 | 0.43 |
| Hash Collision (M = 1000) | 1,055 | 0.854 | 62.61 | 0.59 |
| Snapshot Store | 1,744 | 1.43 | 847 | 4.83 |
| Hash Collision (M = 10) | 10.23 | 0.06 | 56.21 | 0.84 |
| Hash Collision (M = 100) | 16.72 | 0.06 | 91.97 | 1.17 |
| Hash Collision (M = 1000) | 56.09 | 0.16 | 392 | 1.80 |

## Total timings

All three columns are mean wall-clock milliseconds per run:

- **Hegel**: generation, reduction, counterexample recording, confirmation calls and final replay.
- **Hypothesis**: its recorded `total_seconds`, which includes its final replay.
- **Exhaust**: its recorded `wallMilliseconds`, which covers generation and reduction. Exhaust makes no final replay.

| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |
|---|---|---|---|
| Binary Heap | 137.17 | **4.91** | 264.43 |
| Calculator | 1,538.10 | **0.55** | 107.12 |
| Nested Flatmap (product sequence), depth 2 | 230.04 | **3.00** | 67.67 |
| Nested Flatmap (product sequence), depth 3 | 401.65 | **6.45** | 107.11 |
| Nested Flatmap (product sequence), depth 4 | 418.53 | **63.35** | 200.33 |
| Nested Flatmap (product sequence), depth 5 | **494.57** | 992.56 | 791.40 |
| Nested Flatmap (product sequence), depth 6 | **527.75** | 2,677.00 | 4,716.38 |
| Nested Flatmap (product), depth 2 | 8.15 | **0.21** | 21.18 |
| Nested Flatmap (product), depth 3 | 10.61 | **0.81** | 23.29 |
| Nested Flatmap (product), depth 4 | 14.47 | **2.23** | 29.81 |
| Nested Flatmap (product), depth 5 | 16.91 | **6.04** | 26.07 |
| Nested Flatmap (product), depth 6 | 19.25 | **13.82** | 22.73 |
| Nested Flatmap (sum), depth 4 | 604.27 | **37.06** | 82.37 |
| Modular Mapping | 8.37 | **0.04** | 0.56 |
| Weighted Linear Preservation | 23.14 | **0.16** | 1.13 |
| Invoice Discount | 26.28 | **0.35** | 2.24 |
| Invoice Discount (derived) | 436.97 | **0.65** | 5.73 |
| Refund Allocation | 95.83 | **4.25** | 119.66 |
| Refund Allocation (derived) | 214.57 | 31.35 | **16.07** |
| Float Cancellation | 21.64 | **0.62** | 3.71 |
| Chunked Decoder | 37.79 | **0.70** | 20.88 |
| Hash Collision (M = 10) | 52.25 | **0.36** | 6.50 |
| Hash Collision (M = 100) | 111.66 | **0.56** | 8.14 |
| Hash Collision (M = 1000) | 1,119.13 | **1.48** | 17.57 |
| Snapshot Store | 2,592.94 | **6.28** | 523.97 |
| Hash Collision (M = 10) (state machine) | 68.35 | **0.91** | 76.09 |
| Hash Collision (M = 100) (state machine) | 110.53 | **1.25** | 78.89 |
| Hash Collision (M = 1000) (state machine) | 449.59 | **1.97** | 84.22 |
