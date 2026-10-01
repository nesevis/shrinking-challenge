# Hash Collision Report for Exhaust

These results are from Exhaust v1.5.2, October 1st, 2026.

A hash map whose hash code is the key modulo `M` has a deliberate bug: `put` and `get` match entries by hash code rather than by key. Both make the same mistake, so the postcondition "after `put(a, v)`, `get(a) == v`" still holds. Only the frame property catches it: putting a key leaves every other key in the map unchanged. It fails when two distinct keys are congruent modulo `M`, so the reducer has to lower both keys together, in steps of `M`. Keys are drawn from `0...(10M - 1)` and values from `0...9`.

The same property runs two ways for each modulus. The generator variant builds a map from up to 20 generated entries and checks one final put; counterexamples are written as `(entries, key, value)`. The state machine variant has a single `put` command that checks the frame property after every put, and runs with `mode: .sequential` and `.commandLimit(50)`, matching Hypothesis's default `stateful_step_count`; counterexamples list the puts that ran.

## Generator (M = 10)

### Normalization

Exhaust produced 6 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 64% | `([(0, 0)], 10, 1)` |
| 12% | `([(1, 0)], 11, 1)` |
| 11% | `([(0, 0)], 70, 1)` |
| 9% | `([(0, 0)], 90, 1)` |
| 3% | `([(11, 0)], 1, 1)` |
| 1% | `([(1, 0)], 71, 1)` |

The minimal counterexample is `([(0, 0)], 10, 1)`. 64 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionTen.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 31.0 | 107.0 | 73.0 | 70.2 | 66.9–73.5 |
| Reduction time (ms) | 0.16 | 1.25 | 0.35 | 0.36 | 0.34–0.39 |
| Iterations to failure | 3.0 | 33.0 | 15.0 | 14.7 | 13.4–16.0 |

`swift run -c release ExhaustRunner --challenge hashCollisionTen --iterations 100`

## Generator (M = 100)

### Normalization

Exhaust produced 5 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 54% | `([(0, 0)], 100, 1)` |
| 20% | `([(0, 0)], 300, 1)` |
| 16% | `([(0, 0)], 500, 1)` |
| 7% | `([(0, 0)], 700, 1)` |
| 3% | `([(0, 0)], 900, 1)` |

The minimal counterexample is `([(0, 0)], 100, 1)`. 54 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionHundred.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 64.0 | 162.0 | 104.5 | 106.8 | 103.6–110.1 |
| Reduction time (ms) | 0.26 | 0.91 | 0.44 | 0.45 | 0.43–0.46 |
| Iterations to failure | 8.0 | 95.0 | 38.5 | 38.9 | 35.2–42.5 |

`swift run -c release ExhaustRunner --challenge hashCollisionHundred --iterations 100`

## Generator (M = 1000)

### Normalization

Exhaust produced 5 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 71% | `([(0, 0)], 1000, 1)` |
| 14% | `([(0, 0)], 3000, 1)` |
| 9% | `([(0, 0)], 5000, 1)` |
| 4% | `([(0, 0)], 7000, 1)` |
| 2% | `([(0, 0)], 9000, 1)` |

The minimal counterexample is `([(0, 0)], 1000, 1)`. 71 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionThousand.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 52.0 | 189.0 | 141.5 | 143.1 | 139.2–147.1 |
| Reduction time (ms) | 0.34 | 0.94 | 0.58 | 0.6 | 0.58–0.62 |
| Iterations to failure | 19.0 | 1495.0 | 191.5 | 285.4 | 230.0–340.7 |

`swift run -c release ExhaustRunner --challenge hashCollisionThousand --iterations 100`

## State machine (M = 10)

### Normalization

Exhaust produced 52 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 8% | `[put(0, 0), put(10, 1)]` |
| 7% | `[put(3, 0), put(13, 1)]` |
| 6% | `[put(9, 0), put(19, 1)]` |
| 6% | `[put(4, 0), put(14, 1)]` |
| 5% | `[put(7, 0), put(17, 1)]` |
| 5% | `[put(1, 0), put(11, 1)]` |
| 4% | `[put(2, 0), put(12, 1)]` |
| 3% | `[put(2, 0), put(92, 1)]` |
| 3% | `[put(5, 0), put(95, 1)]` |
| 3% | `[put(5, 0), put(75, 1)]` |
| 3% | `[put(8, 0), put(18, 1)]` |
| 2% | `[put(9, 0), put(89, 1)]` |
| 2% | `[put(4, 1), put(14, 0)]` |
| 2% | `[put(68, 0), put(8, 1)]` |
| 2% | `[put(8, 1), put(18, 0)]` |
| 2% | `[put(3, 0), put(73, 1)]` |
| 2% | `[put(5, 0), put(15, 1)]` |
| 1% | `[put(78, 0), put(98, 1)]` |
| 1% | `[put(0, 0), put(70, 1)]` |
| 1% | `[put(12, 0), put(2, 1)]` |
| 1% | `[put(98, 1), put(68, 0)]` |
| 1% | `[put(4, 0), put(74, 1)]` |
| 1% | `[put(2, 0), put(72, 1)]` |
| 1% | `[put(76, 0), put(96, 1)]` |
| 1% | `[put(7, 1), put(97, 0)]` |
| 1% | `[put(69, 0), put(9, 1)]` |
| 1% | `[put(14, 0), put(4, 1)]` |
| 1% | `[put(1, 1), put(11, 0)]` |
| 1% | `[put(6, 0), put(16, 1)]` |
| 1% | `[put(89, 1), put(9, 0)]` |
| 1% | `[put(75, 0), put(5, 1)]` |
| 1% | `[put(89, 0), put(9, 1)]` |
| 1% | `[put(2, 1), put(12, 0)]` |
| 1% | `[put(18, 1), put(8, 0)]` |
| 1% | `[put(97, 0), put(67, 1)]` |
| 1% | `[put(8, 0), put(88, 1)]` |
| 1% | `[put(71, 0), put(1, 1)]` |
| 1% | `[put(11, 1), put(1, 0)]` |
| 1% | `[put(13, 0), put(3, 1)]` |
| 1% | `[put(16, 0), put(6, 1)]` |
| 1% | `[put(7, 0), put(87, 1)]` |
| 1% | `[put(97, 0), put(7, 1)]` |
| 1% | `[put(98, 0), put(8, 1)]` |
| 1% | `[put(17, 1), put(7, 0)]` |
| 1% | `[put(6, 0), put(76, 1)]` |
| 1% | `[put(5, 1), put(15, 0)]` |
| 1% | `[put(1, 0), put(71, 1)]` |
| 1% | `[put(1, 0), put(91, 1)]` |
| 1% | `[put(3, 1), put(13, 0)]` |
| 1% | `[put(6, 0), put(66, 1)]` |
| 1% | `[put(10, 0), put(0, 1)]` |
| 1% | `[put(4, 0), put(94, 1)]` |

The minimal counterexample is `[put(0, 0), put(10, 1)]`. 8 of 100 runs reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionStateMachineTen.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 28.0 | 87.0 | 54.0 | 53.8 | 51.7–56.0 |
| Reduction time (ms) | 0.28 | 1.01 | 0.62 | 0.63 | 0.6–0.66 |
| Iterations to failure | 1.0 | 3.0 | 1.0 | 1.2 | 1.1–1.2 |

Iterations to failure counts generated command sequences.

`swift run -c release ExhaustRunner --challenge hashCollisionStateMachineTen --iterations 100`

## State machine (M = 100)

### Normalization

Exhaust produced 100 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 1% | `[put(352, 1), put(852, 0)]` |
| 1% | `[put(333, 0), put(433, 1)]` |
| 1% | `[put(559, 0), put(659, 1)]` |
| 1% | `[put(744, 0), put(944, 1)]` |
| 1% | `[put(843, 0), put(243, 1)]` |
| 1% | `[put(708, 0), put(608, 1)]` |
| 1% | `[put(137, 1), put(37, 0)]` |
| 1% | `[put(734, 0), put(234, 1)]` |
| 1% | `[put(579, 1), put(379, 0)]` |
| 1% | `[put(6, 0), put(306, 1)]` |
| 1% | `[put(877, 0), put(277, 1)]` |
| 1% | `[put(713, 0), put(913, 1)]` |
| 1% | `[put(462, 0), put(262, 1)]` |
| 1% | `[put(178, 0), put(78, 1)]` |
| 1% | `[put(122, 0), put(822, 1)]` |
| 1% | `[put(527, 0), put(27, 1)]` |
| 1% | `[put(221, 0), put(921, 1)]` |
| 1% | `[put(363, 0), put(863, 1)]` |
| 1% | `[put(171, 0), put(671, 1)]` |
| 1% | `[put(276, 1), put(776, 0)]` |
| 1% | `[put(219, 0), put(19, 1)]` |
| 1% | `[put(0, 0), put(300, 1)]` |
| 1% | `[put(577, 0), put(77, 1)]` |
| 1% | `[put(26, 1), put(726, 0)]` |
| 1% | `[put(225, 0), put(425, 1)]` |
| 1% | `[put(6, 0), put(606, 1)]` |
| 1% | `[put(454, 0), put(954, 1)]` |
| 1% | `[put(365, 0), put(265, 1)]` |
| 1% | `[put(448, 0), put(648, 1)]` |
| 1% | `[put(85, 0), put(185, 1)]` |
| 1% | `[put(559, 0), put(759, 1)]` |
| 1% | `[put(615, 0), put(715, 1)]` |
| 1% | `[put(483, 1), put(283, 0)]` |
| 1% | `[put(428, 0), put(928, 1)]` |
| 1% | `[put(173, 0), put(373, 1)]` |
| 1% | `[put(811, 0), put(911, 1)]` |
| 1% | `[put(364, 0), put(964, 1)]` |
| 1% | `[put(131, 0), put(631, 1)]` |
| 1% | `[put(4, 0), put(404, 1)]` |
| 1% | `[put(796, 0), put(996, 1)]` |
| 1% | `[put(417, 0), put(717, 1)]` |
| 1% | `[put(6, 0), put(706, 1)]` |
| 1% | `[put(4, 0), put(104, 1)]` |
| 1% | `[put(415, 0), put(115, 1)]` |
| 1% | `[put(764, 0), put(464, 1)]` |
| 1% | `[put(511, 0), put(111, 1)]` |
| 1% | `[put(299, 0), put(99, 1)]` |
| 1% | `[put(394, 0), put(994, 1)]` |
| 1% | `[put(116, 0), put(616, 1)]` |
| 1% | `[put(873, 0), put(173, 1)]` |
| 1% | `[put(98, 0), put(298, 1)]` |
| 1% | `[put(934, 1), put(734, 0)]` |
| 1% | `[put(627, 0), put(827, 1)]` |
| 1% | `[put(651, 0), put(551, 1)]` |
| 1% | `[put(865, 1), put(65, 0)]` |
| 1% | `[put(150, 0), put(50, 1)]` |
| 1% | `[put(73, 0), put(873, 1)]` |
| 1% | `[put(15, 0), put(215, 1)]` |
| 1% | `[put(584, 0), put(884, 1)]` |
| 1% | `[put(729, 1), put(629, 0)]` |
| 1% | `[put(397, 0), put(897, 1)]` |
| 1% | `[put(21, 0), put(121, 1)]` |
| 1% | `[put(415, 1), put(115, 0)]` |
| 1% | `[put(89, 0), put(389, 1)]` |
| 1% | `[put(317, 1), put(617, 0)]` |
| 1% | `[put(420, 1), put(320, 0)]` |
| 1% | `[put(655, 0), put(955, 1)]` |
| 1% | `[put(78, 0), put(678, 1)]` |
| 1% | `[put(694, 0), put(594, 1)]` |
| 1% | `[put(20, 0), put(520, 1)]` |
| 1% | `[put(296, 0), put(996, 1)]` |
| 1% | `[put(760, 0), put(460, 1)]` |
| 1% | `[put(53, 0), put(753, 1)]` |
| 1% | `[put(688, 0), put(588, 1)]` |
| 1% | `[put(197, 0), put(697, 1)]` |
| 1% | `[put(739, 1), put(639, 0)]` |
| 1% | `[put(276, 0), put(176, 1)]` |
| 1% | `[put(637, 0), put(137, 1)]` |
| 1% | `[put(17, 1), put(117, 0)]` |
| 1% | `[put(964, 0), put(264, 1)]` |
| 1% | `[put(292, 0), put(692, 1)]` |
| 1% | `[put(937, 1), put(737, 0)]` |
| 1% | `[put(462, 0), put(162, 1)]` |
| 1% | `[put(396, 0), put(196, 1)]` |
| 1% | `[put(242, 1), put(42, 0)]` |
| 1% | `[put(756, 0), put(656, 1)]` |
| 1% | `[put(377, 1), put(677, 0)]` |
| 1% | `[put(865, 0), put(965, 1)]` |
| 1% | `[put(307, 0), put(7, 1)]` |
| 1% | `[put(449, 0), put(549, 1)]` |
| 1% | `[put(614, 0), put(914, 1)]` |
| 1% | `[put(834, 0), put(634, 1)]` |
| 1% | `[put(469, 0), put(169, 1)]` |
| 1% | `[put(3, 0), put(603, 1)]` |
| 1% | `[put(340, 0), put(240, 1)]` |
| 1% | `[put(522, 0), put(422, 1)]` |
| 1% | `[put(695, 0), put(595, 1)]` |
| 1% | `[put(484, 0), put(84, 1)]` |
| 1% | `[put(421, 0), put(621, 1)]` |
| 1% | `[put(295, 0), put(795, 1)]` |

The minimal counterexample is `[put(0, 0), put(100, 1)]`. No run reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionStateMachineHundred.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 43.0 | 165.0 | 72.0 | 80.1 | 75.2–84.9 |
| Reduction time (ms) | 0.33 | 3.34 | 0.87 | 1.04 | 0.93–1.15 |
| Iterations to failure | 1.0 | 5.0 | 1.0 | 1.4 | 1.3–1.6 |

Iterations to failure counts generated command sequences.

`swift run -c release ExhaustRunner --challenge hashCollisionStateMachineHundred --iterations 100`

## State machine (M = 1000)

### Normalization

Exhaust produced 100 distinct counterexamples across 100 test runs:

| Prevalence | Counterexample |
|---|---|
| 1% | `[put(346, 0), put(1346, 1)]` |
| 1% | `[put(9864, 0), put(2864, 1)]` |
| 1% | `[put(6947, 0), put(5947, 1)]` |
| 1% | `[put(7712, 0), put(4712, 1)]` |
| 1% | `[put(544, 0), put(5544, 1)]` |
| 1% | `[put(2283, 0), put(1283, 1)]` |
| 1% | `[put(5554, 0), put(8554, 1)]` |
| 1% | `[put(4517, 1), put(8517, 0)]` |
| 1% | `[put(4200, 1), put(200, 0)]` |
| 1% | `[put(3132, 0), put(6132, 1)]` |
| 1% | `[put(1062, 0), put(62, 1)]` |
| 1% | `[put(381, 1), put(1381, 0)]` |
| 1% | `[put(744, 1), put(4744, 0)]` |
| 1% | `[put(140, 0), put(8140, 1)]` |
| 1% | `[put(6379, 0), put(7379, 1)]` |
| 1% | `[put(4742, 0), put(5742, 1)]` |
| 1% | `[put(2458, 0), put(8458, 1)]` |
| 1% | `[put(9451, 0), put(6451, 1)]` |
| 1% | `[put(2011, 0), put(4011, 1)]` |
| 1% | `[put(854, 0), put(6854, 1)]` |
| 1% | `[put(6652, 0), put(3652, 1)]` |
| 1% | `[put(3698, 0), put(698, 1)]` |
| 1% | `[put(5099, 0), put(2099, 1)]` |
| 1% | `[put(4131, 0), put(6131, 1)]` |
| 1% | `[put(8465, 0), put(2465, 1)]` |
| 1% | `[put(1106, 0), put(8106, 1)]` |
| 1% | `[put(2720, 0), put(3720, 1)]` |
| 1% | `[put(5325, 0), put(1325, 1)]` |
| 1% | `[put(5253, 0), put(1253, 1)]` |
| 1% | `[put(4044, 1), put(9044, 0)]` |
| 1% | `[put(4409, 0), put(7409, 1)]` |
| 1% | `[put(9940, 0), put(2940, 1)]` |
| 1% | `[put(3192, 0), put(4192, 1)]` |
| 1% | `[put(4733, 0), put(5733, 1)]` |
| 1% | `[put(8513, 0), put(2513, 1)]` |
| 1% | `[put(8743, 0), put(3743, 1)]` |
| 1% | `[put(4214, 0), put(2214, 1)]` |
| 1% | `[put(6155, 0), put(7155, 1)]` |
| 1% | `[put(9704, 0), put(7704, 1)]` |
| 1% | `[put(6723, 0), put(4723, 1)]` |
| 1% | `[put(5144, 0), put(7144, 1)]` |
| 1% | `[put(868, 0), put(6868, 1)]` |
| 1% | `[put(1560, 0), put(9560, 1)]` |
| 1% | `[put(730, 0), put(2730, 1)]` |
| 1% | `[put(1033, 1), put(2033, 0)]` |
| 1% | `[put(3192, 0), put(192, 1)]` |
| 1% | `[put(4378, 0), put(3378, 1)]` |
| 1% | `[put(4200, 1), put(6200, 0)]` |
| 1% | `[put(4852, 1), put(8852, 0)]` |
| 1% | `[put(4576, 0), put(5576, 1)]` |
| 1% | `[put(8413, 0), put(1413, 1)]` |
| 1% | `[put(2415, 0), put(415, 1)]` |
| 1% | `[put(3564, 0), put(564, 1)]` |
| 1% | `[put(8186, 0), put(9186, 1)]` |
| 1% | `[put(1279, 0), put(279, 1)]` |
| 1% | `[put(5471, 0), put(4471, 1)]` |
| 1% | `[put(376, 0), put(7376, 1)]` |
| 1% | `[put(1096, 0), put(96, 1)]` |
| 1% | `[put(1401, 0), put(6401, 1)]` |
| 1% | `[put(6632, 1), put(4632, 0)]` |
| 1% | `[put(9472, 0), put(4472, 1)]` |
| 1% | `[put(5878, 0), put(7878, 1)]` |
| 1% | `[put(6733, 0), put(9733, 1)]` |
| 1% | `[put(1018, 1), put(2018, 0)]` |
| 1% | `[put(6420, 0), put(8420, 1)]` |
| 1% | `[put(1142, 0), put(142, 1)]` |
| 1% | `[put(69, 0), put(5069, 1)]` |
| 1% | `[put(7444, 0), put(9444, 1)]` |
| 1% | `[put(6144, 0), put(9144, 1)]` |
| 1% | `[put(2075, 0), put(6075, 1)]` |
| 1% | `[put(2951, 0), put(951, 1)]` |
| 1% | `[put(4058, 0), put(2058, 1)]` |
| 1% | `[put(2169, 1), put(6169, 0)]` |
| 1% | `[put(1342, 0), put(8342, 1)]` |
| 1% | `[put(2942, 0), put(7942, 1)]` |
| 1% | `[put(1342, 1), put(2342, 0)]` |
| 1% | `[put(2, 0), put(3002, 1)]` |
| 1% | `[put(8268, 0), put(9268, 1)]` |
| 1% | `[put(9077, 0), put(8077, 1)]` |
| 1% | `[put(1316, 1), put(8316, 0)]` |
| 1% | `[put(1030, 1), put(30, 0)]` |
| 1% | `[put(2492, 0), put(1492, 1)]` |
| 1% | `[put(1129, 0), put(6129, 1)]` |
| 1% | `[put(2363, 0), put(4363, 1)]` |
| 1% | `[put(5456, 0), put(456, 1)]` |
| 1% | `[put(2763, 1), put(7763, 0)]` |
| 1% | `[put(7296, 0), put(6296, 1)]` |
| 1% | `[put(7598, 0), put(2598, 1)]` |
| 1% | `[put(4289, 0), put(9289, 1)]` |
| 1% | `[put(6288, 0), put(8288, 1)]` |
| 1% | `[put(1871, 0), put(7871, 1)]` |
| 1% | `[put(8369, 0), put(1369, 1)]` |
| 1% | `[put(7228, 1), put(228, 0)]` |
| 1% | `[put(174, 1), put(1174, 0)]` |
| 1% | `[put(2251, 0), put(4251, 1)]` |
| 1% | `[put(9548, 0), put(548, 1)]` |
| 1% | `[put(1926, 1), put(5926, 0)]` |
| 1% | `[put(8368, 0), put(5368, 1)]` |
| 1% | `[put(9371, 1), put(7371, 0)]` |
| 1% | `[put(2494, 0), put(6494, 1)]` |

The minimal counterexample is `[put(0, 0), put(1000, 1)]`. No run reached it.

See [the first 100 failing inputs before shrinking](/pbt-libraries/exhaust/failures/hashCollisionStateMachineThousand.json).

### Performance

| Metric | Min | Max | Median | Mean | 95% CI |
|---|---|---|---|---|---|
| Evaluations | 54.0 | 229.0 | 113.0 | 119.9 | 111.5–128.3 |
| Reduction time (ms) | 0.58 | 6.63 | 1.57 | 2.02 | 1.74–2.3 |
| Iterations to failure | 1.0 | 21.0 | 3.0 | 3.9 | 3.2–4.6 |

Iterations to failure counts generated command sequences.

`swift run -c release ExhaustRunner --challenge hashCollisionStateMachineThousand --iterations 100`

## Reproduction

From the `exhaust/src` folder, run the command listed under each variant.

The reduction time reflects running on an M4 Max running macOS 26.4. This is an optimised release build.
