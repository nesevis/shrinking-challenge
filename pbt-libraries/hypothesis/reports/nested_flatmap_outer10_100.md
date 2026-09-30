# Nested flatmap: 100 trials, outer maximum 10

Recorded depths 2–5: 2026-09-29T21:56:41Z
Recorded depth 6: 2026-09-29T22:12:45Z
Hypothesis: 6.168.3 | Python: 3.12.12 | Platform: macOS 26.6.2 arm64

Sequential runs; 100 filename-seeded trials per depth; empty database;
`max_examples=10**6`; default shrink budget (`max_stall=200`).

| Depth | Exact optimum | Final lengths (count) | Mean evaluations | Mean generation ms | Mean shrink ms | Median shrink ms | Total test seconds |
|---|---|---|---|---|---|---|---|
| 2 | 39/100 | 24 (84); 25 (16) | 70.67 | 13.87 | 239.19 | 166.92 | 25.48 |
| 3 | 20/100 | 24 (87); 25 (9); 27 (4) | 87.87 | 21.66 | 368.07 | 367.40 | 39.15 |
| 4 | 26/100 | 24 (93); 25 (5); 27 (2) | 82.07 | 37.82 | 378.55 | 390.82 | 41.82 |
| 5 | 6/100 | 24 (47); 25 (4); 27 (12); 28 (19); 30 (8); 32 (5); 36 (1); 40 (4) | 61.75 | 43.52 | 437.22 | 252.54 | 48.26 |
| 6 | 5/100 | 24 (35); 25 (11); 27 (16); 28 (7); 30 (10); 32 (6); 36 (7); 40 (7); 42 (1) | 63.04 | 60.57 | 487.69 | 282.65 | 55.03 |

Timings are wall-clock measurements. Generation and shrink times come from
Hypothesis phase statistics; total time includes test-wrapper overhead and final
replay. Evaluation counts run from the first failure onward, not exclusively the
dedicated shrink phase. All 500 original and final counterexamples were checked
against the factor bounds, exact payload size, and failure predicate. All final
payloads contain exactly one `1`.

Per-trial seeds, starting/final values, evaluations, and timings:
`../challenges/nested_flatmap_{2,3,4,5,6}.json`.
Progress logs: `nested_flatmap_{2,3,4,5,6}.log`.
Normalization reports: `../challenges/nested_flatmap_{2,3,4,5,6}.md`.

Reproduce from `pbt-libraries/hypothesis/`:

```sh
for depth in 2 3 4 5 6; do
  venv/bin/python support/run_challenge.py challenges/nested_flatmap_${depth}.py 100
  venv/bin/python support/make_report.py challenges/nested_flatmap_${depth}.json
done
```
