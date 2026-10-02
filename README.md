# Shrinking Challenge: Hypothesis vs Exhaust vs Hegel

A comparison of [Hypothesis](/pbt-libraries/hypothesis/README.md) 6.168.3, [Exhaust](/pbt-libraries/exhaust/README.md) 1.5.4, and [Hegel](/pbt-libraries/hegel/README.md) 0.48.1 (native engine 0.44.1) on seeded and fixed-start shrinking challenges.

Each challenge links to the participating libraries' reports. 🎯 marks the ~minimal counterexample.

## Fixed start

Hypothesis and Exhaust reduce the same fixed failing input once, with no generation phase. Fixed-start rows use each runner's reported evaluation count directly; the +1 adjustment to Exhaust applies to the generated rows below.

| Challenge | Library | Evaluations | Counterexample |
|---|---|---|---|
| Anagrams | [Hypothesis](/pbt-libraries/hypothesis/challenges/anagrams.md) | 798 | `("000000000000000000000000011", "000000000000000000000000110")` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/anagrams.md) | 1226 | 🎯 `(" \0", "\0 ")` |
|  |  |  |  |
| Username and Password | [Hypothesis](/pbt-libraries/hypothesis/challenges/username_password.md) | 301 | `("u: p0000000", "p: p0000000")` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/usernamePassword.md) | 723 | 🎯 `("u: 0000", "p: 0000")` |
|  |  |  |  |
| Duplicated Text | [Hypothesis](/pbt-libraries/hypothesis/challenges/duplicated_text.md) | 30 | 🎯 `("00000012", "00000012")` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/duplicatedText.md) | 54 | `("10210210", "10210210")` |
|  |  |  |  |
| Haystack | [Hypothesis](/pbt-libraries/hypothesis/challenges/haystack.md) | 242 | 🎯 `"CREEPIDIOT"` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/haystack.md) | 407 | 🎯 `"CREEPIDIOT"` |
|  |  |  |  |
| Zalgo Haystack | [Hypothesis](/challenges/zalgo-haystack.md#verification) | 444 | 🎯 `"THE ICHOR PERMEATES"` |
|  | [Exhaust](/pbt-libraries/exhaust/failures/zalgoHaystack.json) | 461 | 🎯 `"THE ICHOR PERMEATES"` |
|  |  |  |  |
| Distinct Sum | [Hypothesis](/pbt-libraries/hypothesis/challenges/distinct_sum.md) | 133 | 🎯 `[0, 1, -1, 2, 49]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/distinctSum.md) | 130 | `[-2, -1, 0, 1, 53]` |
|  |  |  |  |
| Leap Day | [Hypothesis](/pbt-libraries/hypothesis/challenges/leap_day.md) | 25 | 🎯 `2000-02-29 00:00:00 +0000` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/leapDay.md) | 34 | `2088-02-29 00:00:00 +0000` |
|  |  |  |  |
| Branch Switching | [Hypothesis](/pbt-libraries/hypothesis/challenges/branch_switching.md) | 44 | 🎯 `1001` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/branchSwitching.md) | 17 | `"    "` |

## 100 seeds

Each library generates and reduces a failure in each of 100 seeded runs.

Exhaust results come from the 1.5.4 release run with seeds 1337–1436. The [full run log](/pbt-libraries/exhaust/reports/exhaust-1.5.4-custom-100-release.log) records phase timings; per-run JSON under [`failures/`](/pbt-libraries/exhaust/failures/) records original inputs, reduced inputs, evaluation counts, and wall times. The linked individual Exhaust Markdown reports have not yet been regenerated.

- **Top counterexamples**: the share of runs ending at each counterexample. The top three are shown, followed by the minimal counterexample if it occurred outside them.
- **Distinct CEs**: the number of different counterexamples across the 100 runs.
- **Evaluations**: the mean across the 100 runs. How each library counts them is described below the table.
- **Mean original length**: the average length in characters of each run's first failing input, before shrinking. All libraries' output is written in the same notation, with nested flatmap payloads written out in full.

Hegel uses the same numeric seeds as the corresponding Hypothesis runs, but equal seeds do not imply equal generated inputs.

Hegel's fully derived invoice uses raw signed 64-bit fields, as Exhaust's does, rather than Hypothesis's arbitrary-precision integers.

Calculator's Hegel generator uses signed-64-bit leaves and a maximum depth of 5; Hypothesis's integer and recursive expression domains are unbounded. Hegel evaluates with exact widened arithmetic and Python-style floor division, while Exhaust uses wrapping addition and truncating division.

| Challenge | Library | Distinct CEs | Evaluations | Mean original length | Top counterexamples |
|---|---|---|---|---|---|
| Binary Heap | [Hypothesis](/pbt-libraries/hypothesis/challenges/binheap.md) | 3 | 102.5 | 151.1 | 85% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>14% `(0, None, (0, None, (0, (0, None, None), (1, None, None))))`<br>1% `(0, None, (0, (0, None, None), (0, None, (1, None, None))))` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/binaryHeap.md) | 2 | 128.5 | 384.4 | 66% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))`<br>34% `(0, (0, (1, None, None), None), (0, None, None))` |
|  | [Hegel](/pbt-libraries/hegel/reports/binheap.md) | 1 | 5886.2 | 292.4 | 100% 🎯 `(0, None, (0, (0, None, None), (1, None, None)))` |
|  |  |  |  |  |  |
| Calculator | [Hypothesis](/pbt-libraries/hypothesis/challenges/calculator.md) | 1 | 90.5 | 125.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/calculator.md) | 1 | 54.2 | 63.7 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  | [Hegel](/pbt-libraries/hegel/reports/calculator.md) | 1 | 446.9 | 240.6 | 100% 🎯 `('/', 0, ('+', 0, 0))` |
|  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_2.md) | 3 | 71.5 | 118.4 | 43% `(8, 3, 0x23 + 1x1)`<br>39% 🎯 `(6, 4, 0x23 + 1x1)`<br>18% `(5, 5, 0x24 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProductSequence.md#depth-2) | 2 | 311.8 | 141.0 | 99% 🎯 `(6, 4, 0x23 + 1x1)`<br>1% `(9, 3, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_2.md) | 2 | 1290.1 | 155.0 | 77% 🎯 `(6, 4, 0x23 + 1x1)`<br>23% `(8, 3, 0x23 + 1x1)` |
|  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_3.md) | 6 | 86.9 | 210.4 | 32% `(6, 2, 2, 0x23 + 1x1)`<br>23% `(8, 3, 1, 0x23 + 1x1)`<br>21% 🎯 `(4, 3, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProductSequence.md#depth-3) | 5 | 275.0 | 386.3 | 67% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>22% `(6, 2, 2, 0x23 + 1x1)`<br>5% `(8, 3, 1, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_3.md) | 2 | 1776.7 | 409.2 | 89% 🎯 `(4, 3, 2, 0x23 + 1x1)`<br>11% `(8, 3, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_4.md) | 8 | 80.5 | 272.1 | 27% `(8, 3, 1, 1, 0x23 + 1x1)`<br>18% `(6, 4, 1, 1, 0x23 + 1x1)`<br>14% `(4, 3, 2, 1, 0x23 + 1x1)`<br>12% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProductSequence.md#depth-4) | 7 | 298.5 | 1107.9 | 83% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)`<br>9% `(3, 3, 3, 1, 0x26 + 1x1)`<br>3% `(9, 3, 1, 1, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_4.md) | 3 | 1901.1 | 1261.6 | 60% `(4, 3, 2, 1, 0x23 + 1x1)`<br>22% 🎯 `(3, 2, 2, 2, 0x23 + 1x1)`<br>18% `(8, 3, 1, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_5.md) | 17 | 64.5 | 248.8 | 12% `(6, 4, 1, 1, 1, 0x23 + 1x1)`<br>10% `(7, 4, 1, 1, 1, 0x27 + 1x1)`<br>10% `(6, 2, 2, 1, 1, 0x23 + 1x1)`<br>4% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProductSequence.md#depth-5) | 24 | 692.8 | 3737.7 | 71% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)`<br>2% `(9, 2, 2, 2, 1, 0x71 + 1x1)`<br>2% `(6, 5, 1, 1, 1, 0x29 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_5.md) | 4 | 1843.3 | 1597.0 | 70% `(4, 3, 2, 1, 1, 0x23 + 1x1)`<br>15% `(8, 3, 1, 1, 1, 0x23 + 1x1)`<br>8% `(2, 2, 2, 2, 2, 0x31 + 1x1)`<br>7% 🎯 `(3, 2, 2, 2, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |
| Nested Flatmap (product sequence), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_sequence_6.md) | 20 | 62.8 | 261.4 | 20% `(6, 4, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(8, 3, 1, 1, 1, 1, 0x23 + 1x1)`<br>10% `(5, 5, 1, 1, 1, 1, 0x24 + 1x1)`<br>5% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProductSequence.md#depth-6) | 43 | 1040.6 | 5867.6 | 47% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>3% `(5, 5, 5, 1, 1, 1, 0x124 + 1x1)`<br>2% `(9, 3, 1, 1, 1, 1, 0x26 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_6.md) | 6 | 2765.1 | 6536.2 | 63% `(4, 3, 2, 1, 1, 1, 0x23 + 1x1)`<br>14% `(2, 2, 2, 2, 2, 1, 0x31 + 1x1)`<br>11% 🎯 `(3, 2, 2, 2, 1, 1, 0x23 + 1x1)` |
|  |  |  |  |  |  |
| Nested Flatmap (product), depth 2 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_2.md) | 1 | 18.8 | 6.3 | 100% 🎯 `(5, 5)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProduct.md#depth-2) | 1 | 30.4 | 6.2 | 100% 🎯 `(5, 5)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_2.md) | 1 | 3514.0 | 6.2 | 100% 🎯 `(5, 5)` |
|  |  |  |  |  |  |
| Nested Flatmap (product), depth 3 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_3.md) | 1 | 22.1 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProduct.md#depth-3) | 1 | 59.1 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_3.md) | 1 | 4214.8 | 9.2 | 100% 🎯 `(3, 3, 3)` |
|  |  |  |  |  |  |
| Nested Flatmap (product), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_4.md) | 1 | 24.3 | 12.3 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProduct.md#depth-4) | 1 | 73.4 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_4.md) | 1 | 4696.7 | 12.2 | 100% 🎯 `(3, 2, 2, 2)` |
|  |  |  |  |  |  |
| Nested Flatmap (product), depth 5 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_5.md) | 1 | 26.2 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProduct.md#depth-5) | 1 | 70.8 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_5.md) | 1 | 4327.4 | 15.2 | 100% 🎯 `(2, 2, 2, 2, 2)` |
|  |  |  |  |  |  |
| Nested Flatmap (product), depth 6 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_product_6.md) | 1 | 28.1 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/nestedFlatmapProduct.md#depth-6) | 1 | 31.5 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_product_6.md) | 1 | 3590.6 | 18.2 | 100% 🎯 `(2, 2, 2, 2, 2, 1)` |
|  |  |  |  |  |  |
| Nested Flatmap (sum), depth 4 | [Hypothesis](/pbt-libraries/hypothesis/challenges/nested_flatmap_sum_4.md) | 1 | 162.3 | 368.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/depthFourSumBind.md) | 1 | 735.4 | 344.8 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/nested_flatmap_sum_4.md) | 1 | 3282.0 | 336.2 | 100% 🎯 `(6, 6, 6, 6, 0x23 + 1x1)` |
|  |  |  |  |  |  |
| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.md) | 12 | 20.6 | 3.0 | 32% 🎯 `925`<br>16% `921`<br>10% `917` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/modularMapping.md) | 18 | 18.5 | 3.0 | 15% 🎯 `925`<br>13% `921`<br>10% `901` |
|  | [Hegel](/pbt-libraries/hegel/reports/modular_mapping.md) | 6 | 32.6 | 3.0 | 63% 🎯 `925`<br>15% `927`<br>12% `926` |
|  |  |  |  |  |  |
| Weighted Linear Preservation | [Hypothesis](/pbt-libraries/hypothesis/challenges/weighted_linear_preservation.md) | 8 | 53.8 | 9.5 | 25% `(10, 0, 0)`<br>24% `(5, 0, 10)`<br>15% 🎯 `(0, 0, 20)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/weightedLinearPreservation.md) | 11 | 43.0 | 9.6 | 22% 🎯 `(0, 0, 20)`<br>16% `(2, 0, 16)`<br>14% `(1, 0, 18)` |
|  | [Hegel](/pbt-libraries/hegel/reports/weighted_linear_preservation.md) | 1 | 62.4 | 9.5 | 100% 🎯 `(0, 0, 20)` |
|  |  |  |  |  |  |
| Invoice Discount | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount.md) | 22 | 61.5 | 19.6 | 40% `Invoice(28, 36, 1)`<br>8% `Invoice(201, 5, 1)`<br>6% `Invoice(11, 91, 1)`<br>4% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/invoiceDiscount.md) | 4 | 59.4 | 19.7 | 84% `Invoice(12, 84, 1)`<br>11% `Invoice(11, 91, 1)`<br>4% 🎯 `Invoice(10, 100, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/invoice_discount.md) | 1 | 665.9 | 19.6 | 100% 🎯 `Invoice(10, 100, 1)` |
|  |  |  |  |  |  |
| Invoice Discount (derived) | [Hypothesis](/pbt-libraries/hypothesis/challenges/invoice_discount_derived.md) | 9 | 748.8 | 19.1 | 86% `Invoice(28, 36, 1)`<br>5% `Invoice(101, 10, 1)`<br>3% `Invoice(11, 91, 1)`<br>1% 🎯 `Invoice(10, 100, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/invoiceDiscountDerived.md) | 16 | 120.4 | 19.0 | 14% `Invoice(25, 40, 1)`<br>14% `Invoice(15, 67, 1)`<br>12% `Invoice(14, 72, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/invoice_discount_derived.md) | 9 | 482.8 | 18.9 | 36% 🎯 `Invoice(10, 100, 1)`<br>28% `Invoice(18, 56, 1)`<br>27% `Invoice(14, 72, 1)` |
|  |  |  |  |  |  |
| Float Cancellation | [Hypothesis](/pbt-libraries/hypothesis/challenges/float_cancellation.md) | 82 | 66.1 | 41.3 | 3% `(1.0, 3.1)`<br>3% `(1.1125369292536007e-308, 1.0)`<br>3% `(1.0, 3.9)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/floatCancellation.md) | 100 | 307.0 | 39.5 | 1% `(208381.0, 315907.7322945033)`<br>1% `(-674879.0, -373697.223055313)`<br>1% `(-380887.9292787704, -143401.0)` |
|  | [Hegel](/pbt-libraries/hegel/reports/float_cancellation.md) | 31 | 562.5 | 43.5 | 26% `(1.0, 524287.00000000006)`<br>24% `(1.0, 1.0000000000000002)`<br>6% `(1.0, 16383.000000000002)` |
|  |  |  |  |  |  |
| Chunked Decoder | [Hypothesis](/pbt-libraries/hypothesis/challenges/chunked_decoder.md) | 1 | 50.2 | 61.8 | 100% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/chunkedDecoder.md) | 5 | 85.1 | 31.2 | 56% `(text, "\u{10000}", [3, 1])`<br>40% `(text, "\u{800}", [2, 1])`<br>2% 🎯 `(text, "\u{80}", [1, 1])` |
|  | [Hegel](/pbt-libraries/hegel/reports/chunked_decoder.md) | 55 | 1636.2 | 78.7 | 11% `(text, "\u{10000}", [3, 1])`<br>10% `(text, "\u{10000}\u{10000}", [7, 1])`<br>6% `(text, "0\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}\u{800}", [42, 1])`<br>4% 🎯 `(text, "\u{80}", [1, 1])` |
|  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_10.md) | 10 | 75.1 | 44.1 | 30% `([(10, 0)], 0, 1)`<br>17% `([(30, 0)], 0, 1)`<br>14% 🎯 `([(0, 0)], 10, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollision.md#generator-m--10) | 6 | 71.2 | 29.9 | 64% 🎯 `([(0, 0)], 10, 1)`<br>12% `([(1, 0)], 11, 1)`<br>11% `([(0, 0)], 70, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_10.md) | 1 | 408.9 | 97.3 | 100% 🎯 `([(0, 0)], 10, 1)` |
|  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_100.md) | 8 | 131.9 | 64.3 | 62% `([(100, 0)], 0, 1)`<br>20% 🎯 `([(0, 0)], 100, 1)`<br>7% `([(300, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollision.md#generator-m--100) | 5 | 107.8 | 61.8 | 54% 🎯 `([(0, 0)], 100, 1)`<br>20% `([(0, 0)], 300, 1)`<br>16% `([(0, 0)], 500, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_100.md) | 1 | 512.4 | 100.5 | 100% 🎯 `([(0, 0)], 100, 1)` |
|  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_1000.md) | 9 | 771.1 | 101.6 | 40% `([(1000, 0)], 0, 1)`<br>22% 🎯 `([(0, 0)], 1000, 1)`<br>13% `([(3000, 0)], 0, 1)` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollision.md#generator-m--1000) | 5 | 144.1 | 117.5 | 71% 🎯 `([(0, 0)], 1000, 1)`<br>14% `([(0, 0)], 3000, 1)`<br>9% `([(0, 0)], 5000, 1)` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_1000.md) | 1 | 545.5 | 122.9 | 100% 🎯 `([(0, 0)], 1000, 1)` |

How each library counts evaluations:

- **Hypothesis and Hegel** count every completed property call from the original failing input onwards. That includes any further generation calls after the first failure, and the final replay of the reduced counterexample.
- **Hegel** also counts its confirmation calls. Rejected or overrun inputs that never reach a property verdict are not counted. Hypothesis's updated Calculator run likewise excludes assumption rejections from failure recording and evaluation counts.
- **Exhaust** reports only the calls made during reduction, so its means here have 1 added to count the original failing input. Exhaust makes no final replay. Binary Heap's reduction mean of 127.5 is therefore shown as 128.5, and Calculator's 53.2 as 54.2.

## State machines

Each library runs 100 seeded state machine tests, generating command histories of up to 50 commands and reducing the first failing history. Exhaust uses `.commandLimit(50)` and Hegel uses `.steps(50)`, to match Hypothesis's default `stateful_step_count`.

The columns are as in the 100 seeds table, with the same +1 added to Exhaust's evaluations.

The Hash Collision rows run the same frame property as the generator rows above, checked after every put. Together, the two tables show how each library's reduction changes with the encoding.

| Challenge | Library | Distinct CEs | Evaluations | Mean original length | Top counterexamples |
|---|---|---|---|---|---|
| Snapshot Store | [Hypothesis](/pbt-libraries/hypothesis/challenges/snapshot_store.md) | 21 | 430.9 | 456.9 | 37% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>18% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]`<br>7% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/snapshotStore.md) | 17 | 232.9 | 497.0 | 67% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>6% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), s2 = snapshot(), read(s0, 0)]`<br>5% `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), release(s1), read(s0, 0)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/snapshot_store.md) | 3 | 1926.7 | 484.8 | 79% 🎯 `[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]`<br>15% `[s0 = snapshot(), put(0, 0), s1 = snapshot(), put(0, 0), s2 = snapshot(), compact(), read(s1, 0)]`<br>6% `[s0 = snapshot(), s1 = snapshot(), put(0, 0), s2 = snapshot(), put(0, 0), s3 = snapshot(), compact(), read(s2, 0)]` |
|  |  |  |  |  |  |
| Hash Collision (M = 10) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_10.md) | 77 | 34.4 | 59.0 | 7% 🎯 `[put(0, 0), put(10, 1)]`<br>5% `[put(30, 0), put(0, 1)]`<br>4% `[put(0, 0), put(30, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollision.md#state-machine-m--10) | 12 | 75.1 | 355.0 | 53% 🎯 `[put(0, 0), put(10, 1)]`<br>16% `[put(0, 1), put(10, 0)]`<br>9% `[put(0, 0), put(70, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_state_machine_10.md) | 1 | 421.8 | 61.9 | 100% 🎯 `[put(0, 0), put(10, 1)]` |
|  |  |  |  |  |  |
| Hash Collision (M = 100) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_100.md) | 59 | 46.5 | 184.5 | 39% 🎯 `[put(0, 0), put(100, 1)]`<br>2% `[put(499, 0), put(99, 1)]`<br>2% `[put(100, 0), put(0, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollision.md#state-machine-m--100) | 8 | 105.8 | 421.7 | 33% 🎯 `[put(0, 0), put(100, 1)]`<br>20% `[put(0, 1), put(100, 0)]`<br>13% `[put(0, 0), put(300, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_state_machine_100.md) | 1 | 294.6 | 204.2 | 100% 🎯 `[put(0, 0), put(100, 1)]` |
|  |  |  |  |  |  |
| Hash Collision (M = 1000) | [Hypothesis](/pbt-libraries/hypothesis/challenges/hash_collision_state_machine_1000.md) | 98 | 103.5 | 434.6 | 2% `[put(140, 0), put(1140, 1)]`<br>2% `[put(4148, 0), put(148, 1)]`<br>1% `[put(3871, 0), put(7871, 1)]`<br>1% 🎯 `[put(0, 0), put(1000, 1)]` |
|  | [Exhaust](/pbt-libraries/exhaust/reports/hashCollision.md#state-machine-m--1000) | 9 | 153.1 | 512.5 | 30% `[put(0, 1), put(1000, 0)]`<br>28% 🎯 `[put(0, 0), put(1000, 1)]`<br>10% `[put(0, 0), put(3000, 1)]` |
|  | [Hegel](/pbt-libraries/hegel/reports/hash_collision_state_machine_1000.md) | 1 | 348.2 | 415.6 | 100% 🎯 `[put(0, 0), put(1000, 1)]` |


## Apples-to-oranges timings

Mean milliseconds per run. Exhaust 1.5.4 was run in release mode on an Apple M4 Max running macOS 26.6.2. Hypothesis 6.168.3 runs on Python 3.12; its earlier results used macOS 26.4.

- **Generation** is Hypothesis's generate phase and Exhaust's reported generation metric. Exhaust's state-machine runners do not populate that metric, so their generation column uses total interpreter time minus reduction time, including remaining harness overhead. Fixed-start challenges have no generation phase.
- **Reduction** is Hypothesis's shrink phase and Exhaust's reduction time.

Hegel's total timings are reported separately below, because its Rust API does not expose structured generation and reduction durations.

The new Binary Heap, Calculator, and Zalgo Haystack Hypothesis runs used macOS 26.6.2. All Exhaust timings below are from the same 1.5.4 release run.

| Challenge | Hypothesis generation (ms) | Exhaust generation (ms) | Hypothesis reduction (ms) | Exhaust reduction (ms) |
|---|---|---|---|---|
| Anagrams | — | — | 177 | 7.76 |
| Username and Password | — | — | 39.48 | 2.95 |
| Duplicated Text | — | — | 5.23 | 0.41 |
| Haystack | — | — | 112 | 6.05 |
| Zalgo Haystack | — | — | 2,872.52 | 9.26 |
| Distinct Sum | — | — | 47.81 | 0.54 |
| Leap Day | — | — | 8.83 | 0.26 |
| Branch Switching | — | — | 5.62 | 0.28 |
| Binary Heap | 60.69 | 0.073 | 75.30 | 4.65 |
| Calculator | 1496.90 | 0.038 | 40.03 | 0.45 |
| Nested Flatmap (product sequence), depth 2 | 13.37 | 0.020 | 215 | 2.88 |
| Nested Flatmap (product sequence), depth 3 | 19.65 | 0.042 | 381 | 6.29 |
| Nested Flatmap (product sequence), depth 4 | 32.10 | 0.109 | 385 | 63.34 |
| Nested Flatmap (product sequence), depth 5 | 38.21 | 0.336 | 455 | 984.21 |
| Nested Flatmap (product sequence), depth 6 | 40.26 | 0.527 | 486 | 2,671.84 |
| Nested Flatmap (product), depth 2 | 4.05 | 0.004 | 3.35 | 0.17 |
| Nested Flatmap (product), depth 3 | 4.16 | 0.005 | 5.72 | 0.76 |
| Nested Flatmap (product), depth 4 | 4.35 | 0.006 | 9.36 | 2.13 |
| Nested Flatmap (product), depth 5 | 4.65 | 0.008 | 11.49 | 5.84 |
| Nested Flatmap (product), depth 6 | 4.88 | 0.010 | 13.56 | 13.42 |
| Nested Flatmap (sum), depth 4 | 12.56 | 0.048 | 591 | 36.10 |
| Modular Mapping | 4.33 | 0.002 | 3.23 | 0.02 |
| Weighted Linear Preservation | 14.36 | 0.034 | 7.92 | 0.10 |
| Invoice Discount | 3.87 | 0.004 | 21.48 | 0.28 |
| Invoice Discount (derived) | 414 | 0.356 | 22.36 | 0.23 |
| Float Cancellation | 4.29 | 0.007 | 16.63 | 0.57 |
| Chunked Decoder | 7.55 | 0.021 | 29.32 | 0.59 |
| Hash Collision (M = 10) | 19.71 | 0.029 | 31.47 | 0.28 |
| Hash Collision (M = 100) | 76.11 | 0.091 | 34.49 | 0.42 |
| Hash Collision (M = 1000) | 1,055 | 0.841 | 62.61 | 0.56 |
| Snapshot Store | 1,744 | 1.40 | 847 | 4.58 |
| Hash Collision (M = 10) | 10.23 | 0.05 | 56.21 | 0.76 |
| Hash Collision (M = 100) | 16.72 | 0.06 | 91.97 | 1.06 |
| Hash Collision (M = 1000) | 56.09 | 0.16 | 392 | 1.60 |

## Total timings

Hegel 0.48.1 / libhegel 0.44.1, rustc 1.93.1 (01f6ddf75 2026-02-11), release build with a statically linked native engine, on Apple M4 Max running macOS 26.6.2.

All three columns are mean wall-clock milliseconds per run:

- **Hegel**: total time, including generation, reduction, counterexample recording, confirmation calls and final replay. These are not reduction-only timings, because Hegel does not expose phase durations through its Rust API.
- **Hypothesis**: its recorded `total_seconds`, which includes its final replay.
- **Exhaust**: its recorded `wallMilliseconds`, which covers generation and reduction. Exhaust makes no final replay.

| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |
|---|---|---|---|
| [Binary Heap](/pbt-libraries/hegel/reports/binheap.md) | 137.17 | **4.86** | 296.48 |
| [Calculator](/pbt-libraries/hegel/reports/calculator.md) | 1538.10 | **0.55** | 101.94 |
| [Nested Flatmap (product sequence), depth 2](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_2.md) | 230.04 | **2.98** | 66.84 |
| [Nested Flatmap (product sequence), depth 3](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_3.md) | 401.65 | **6.42** | 104.09 |
| [Nested Flatmap (product sequence), depth 4](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_4.md) | 418.53 | **63.58** | 213.11 |
| [Nested Flatmap (product sequence), depth 5](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_5.md) | 494.57 | 984.73 | **406.29** |
| [Nested Flatmap (product sequence), depth 6](/pbt-libraries/hegel/reports/nested_flatmap_product_sequence_6.md) | **527.75** | 2,672.62 | 7,375.74 |
| [Nested Flatmap (product), depth 2](/pbt-libraries/hegel/reports/nested_flatmap_product_2.md) | 8.15 | **0.20** | 21.06 |
| [Nested Flatmap (product), depth 3](/pbt-libraries/hegel/reports/nested_flatmap_product_3.md) | 10.61 | **0.80** | 23.32 |
| [Nested Flatmap (product), depth 4](/pbt-libraries/hegel/reports/nested_flatmap_product_4.md) | 14.47 | **2.17** | 29.63 |
| [Nested Flatmap (product), depth 5](/pbt-libraries/hegel/reports/nested_flatmap_product_5.md) | 16.91 | **5.90** | 26.31 |
| [Nested Flatmap (product), depth 6](/pbt-libraries/hegel/reports/nested_flatmap_product_6.md) | 19.25 | **13.50** | 22.72 |
| [Nested Flatmap (sum), depth 4](/pbt-libraries/hegel/reports/nested_flatmap_sum_4.md) | 604.27 | **36.27** | 86.56 |
| [Modular Mapping](/pbt-libraries/hegel/reports/modular_mapping.md) | 8.37 | **0.04** | 0.51 |
| [Weighted Linear Preservation](/pbt-libraries/hegel/reports/weighted_linear_preservation.md) | 23.14 | **0.16** | 1.07 |
| [Invoice Discount](/pbt-libraries/hegel/reports/invoice_discount.md) | 26.28 | **0.33** | 2.21 |
| [Invoice Discount (derived)](/pbt-libraries/hegel/reports/invoice_discount_derived.md) | 436.97 | **0.63** | 5.44 |
| [Float Cancellation](/pbt-libraries/hegel/reports/float_cancellation.md) | 21.64 | **0.60** | 3.63 |
| [Chunked Decoder](/pbt-libraries/hegel/reports/chunked_decoder.md) | 37.79 | **0.67** | 17.59 |
| [Hash Collision (M = 10)](/pbt-libraries/hegel/reports/hash_collision_10.md) | 52.25 | **0.35** | 6.34 |
| [Hash Collision (M = 100)](/pbt-libraries/hegel/reports/hash_collision_100.md) | 111.66 | **0.55** | 8.04 |
| [Hash Collision (M = 1000)](/pbt-libraries/hegel/reports/hash_collision_1000.md) | 1,119.13 | **1.44** | 16.08 |
| [Snapshot Store](/pbt-libraries/hegel/reports/snapshot_store.md) | 2,592.94 | **6.00** | 513.02 |
| [Hash Collision (M = 10) (state machine)](/pbt-libraries/hegel/reports/hash_collision_state_machine_10.md) | 68.35 | **0.81** | 78.73 |
| [Hash Collision (M = 100) (state machine)](/pbt-libraries/hegel/reports/hash_collision_state_machine_100.md) | 110.53 | **1.13** | 76.20 |
| [Hash Collision (M = 1000) (state machine)](/pbt-libraries/hegel/reports/hash_collision_state_machine_1000.md) | 449.59 | **1.77** | 80.75 |
