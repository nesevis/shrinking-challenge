import json
import unittest
from copy import deepcopy

from make_reports import (
    COMPARISON_PROFILE, IMPLEMENTATIONS, ROOT, SPECS, TIMING_HEADER, code, compact,
    examples, implementation_link, markdown, summarise, table_row, update_comparison,
    update_timings, validate_comparison,
)


def report(name="modular_mapping", values=(925, 925, 927)):
    return {
        "challenge": name, "hegel_version": "0.48.1", "engine_version": "0.44.1",
        "build_profile": COMPARISON_PROFILE,
        "environment": {"os": "macos", "os_version": "test", "cpu": "test CPU",
                        "arch": "aarch64", "rustc": "test rustc"},
        "runs": [{"seed": i, "evaluations": i + 1,
                  "original": {"value": "1000"}, "shrunk": {"value": str(value)},
                  "total_seconds": .001} for i, value in enumerate(values)],
    }


class ReportsTests(unittest.TestCase):
    def test_full_payload_length_and_lossless_run_length_display(self):
        text = "(4, 3, 2, [0, 0, 1, 1, 0])"
        self.assertEqual(compact("nested_flatmap_product_sequence_3", text),
                         "(4, 3, 2, 0x2 + 1x2 + 0x1)")
        data = report("nested_flatmap_product_sequence_3", (text,))
        data["runs"][0]["original"]["value"] = text
        self.assertEqual(summarise(data)["original_length"], len(text))
        self.assertIn("0x2 + 1x2 + 0x1", markdown(data))

    def test_float_exponents_use_the_common_python_notation(self):
        data = report("float_cancellation", ("(1e-5, 1.0)",))
        data["runs"][0]["original"]["value"] = "(1e-5, 1.0)"
        summary = summarise(data)
        self.assertEqual(summary["original_length"], len("(1e-05, 1.0)"))
        self.assertIn("(1e-05, 1.0)", summary["counts"])

    def test_top_three_keeps_reference_when_outside_top_three(self):
        summary = summarise(report(values=(927, 927, 927, 926, 926, 921, 921, 925)))
        self.assertEqual([x[0] for x in examples(summary, "925", 3)],
                         ["927", "926", "921", "925"])
        self.assertTrue(examples(summary, "925", 3)[-1][2])
        self.assertEqual(len(examples(summary, "900", 3)), 3)

    def test_counts_and_times_use_actual_number_of_runs(self):
        summary = summarise(report())
        self.assertEqual(summary["distinct"], 2)
        self.assertEqual(summary["evaluations"], 2)
        self.assertEqual(summary["total_ms"], 1)
        self.assertIn("66.6667% 🎯 `925`", table_row(report()))

    def test_evaluation_columns_distinguish_outliers_and_even_sample_medians(self):
        data = report(values=(925,) * 4)
        for run, count in zip(data["runs"], (1, 2, 2, 101)):
            run["evaluations"] = count
        summary = summarise(data)
        self.assertEqual(summary["evaluations"], 26.5)
        self.assertEqual(summary["median_evaluations"], 2)
        cells = [cell.strip() for cell in table_row(data).strip("|").split("|")]
        self.assertEqual(len(cells), 7)
        self.assertEqual(cells[3:5], ["26.5", "2.0"])

        data["runs"] = data["runs"][:2]
        self.assertEqual(summarise(data)["median_evaluations"], 1.5)
        cells = [cell.strip() for cell in table_row(data).strip("|").split("|")]
        self.assertEqual(cells[3:5], ["1.5", "1.5"])

    def test_refresh_is_idempotent_and_preserves_other_libraries(self):
        text = ("User introduction\n"
                "| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.py) | original |\n"
                "|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/ModularMappingChallenge.swift) | original |\n"
                "\n## Timings\nKeep the timing explanation.\n\n"
                f"{TIMING_HEADER}\n"
                "|---|---|---|---|---|\n"
                "| Anagrams | 172.95 | — | 18.31 | 60.90 |\n"
                "| Modular Mapping | 8.37 | 999.00 | 0.04 | 0.15 |\n")
        data = {"modular_mapping": report()}
        first = update_comparison(text, data)
        self.assertEqual(update_comparison(first, data), first)
        self.assertIn("User introduction", first)
        self.assertIn("ModularMappingChallenge.swift) | original |", first)
        self.assertEqual(first.count("[Hegel]("), 1)
        self.assertIn(f"[Hegel]({implementation_link('modular_mapping')})", first)
        self.assertIn("| Anagrams | 172.95 | — | 18.31 | 60.90 |", first)
        self.assertIn("| Modular Mapping | 8.37 | 1.00 | 0.04 | 0.15 |", first)
        self.assertIn("Keep the timing explanation.", first)
        self.assertNotIn("**", first)
        with_following_section = first + "\n## User section\nKeep this text.\n"
        self.assertEqual(update_comparison(with_following_section, data), with_following_section)

    def test_timings_update_only_hegel_column_and_distinguish_state_machine_rows(self):
        text = (f"{TIMING_HEADER}\n"
                "|---|---|---|---|---|\n"
                "| Hash Collision (M = 1000) | 1,117.16 | 38.60 | 5.68 | 12.19 |\n"
                "| Hash Collision (M = 1000) (state machine) | 450.29 | 152.28 | 10.46 | 21.93 |\n")
        data = {name: report(name) for name in
                ("hash_collision_1000", "hash_collision_state_machine_1000")}
        table = update_timings(text, data)
        self.assertIn("| Hash Collision (M = 1000) | 1,117.16 | 1.00 | 5.68 | 12.19 |", table)
        self.assertIn("| Hash Collision (M = 1000) (state machine) | 450.29 | 1.00 | 10.46 | 21.93 |", table)

    def test_timings_reject_missing_rows_or_table(self):
        data = {"modular_mapping": report()}
        with self.assertRaisesRegex(ValueError, "timing table is missing"):
            update_timings("| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |\n", data)
        with self.assertRaisesRegex(ValueError, "covers 0 of 1"):
            update_timings(f"{TIMING_HEADER}\n|---|---|---|---|---|\n| Anagrams | 1 | — | 1 | 1 |\n", data)

    def test_refund_rows_refresh_without_moving_their_table(self):
        text = ("## Handwritten and derived generators\n"
                "| Refund Allocation | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation.py) | original |\n"
                "|  | [Exhaust](/pbt-libraries/exhaust/src/Sources/ExhaustRunner/Challenges/RefundAllocationChallenge.swift#L31) | original |\n"
                "|  | [Hegel](/pbt-libraries/hegel/reports/refund_allocation.json) | old |\n"
                "\n## State machines\nKeep this section.\n"
                "\n## Timings\n"
                f"{TIMING_HEADER}\n"
                "|---|---|---|---|---|\n"
                "| Refund Allocation | 95.83 | 193.90 | 3.96 | 20.53 |\n")
        data = {"refund_allocation": report("refund_allocation", ("RefundRequest([31, 33], 4)",))}
        first = update_comparison(text, data)
        self.assertEqual(first, update_comparison(first, data))
        self.assertIn("| Refund Allocation | 95.83 | 1.00 | 3.96 | 20.53 |", first)
        self.assertIn(f"[Hegel]({implementation_link('refund_allocation')})", first.split("## State machines")[0])
        self.assertIn("## State machines\nKeep this section.", first)
        self.assertEqual(first.count("[Hegel]("), 1)

    def test_implementation_anchors_land_on_the_challenge_dispatch(self):
        self.assertEqual(set(IMPLEMENTATIONS), set(SPECS))
        for name, (filename, anchor) in IMPLEMENTATIONS.items():
            with self.subTest(challenge=name):
                source = (ROOT / "src" / filename).read_text().splitlines()
                link = implementation_link(name)
                if anchor is None:
                    self.assertEqual(link, f"/pbt-libraries/hegel/src/{filename}")
                else:
                    self.assertRegex(source[int(link.rsplit("#L", 1)[1]) - 1], anchor)

    def test_markdown_protects_table_pipes_and_embedded_backticks(self):
        self.assertEqual(code('(text, "a|b`c", [1, 1])'), '``(text, "a\\|b`c", [1, 1])``')

    def test_comparison_rejects_mixed_or_inconsistent_results(self):
        reports = {name: report(name, (925,) * 100) for name in SPECS}
        validate_comparison(reports)
        for change in ("count", "seed", "range", "environment", "profile"):
            invalid = deepcopy(reports)
            item = invalid["modular_mapping"]
            if change == "count":
                item["runs"].pop()
            elif change == "seed":
                item["runs"][0]["seed"] = 999
            elif change == "range":
                for run in item["runs"]:
                    run["seed"] += 1
            elif change == "environment":
                item["environment"]["cpu"] = "different CPU"
            else:
                item["build_profile"] = "release"
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_comparison(invalid)

    def test_checked_in_consecutive_reports_remain_valid(self):
        reports = {name: json.loads((ROOT / "reports" / f"{name}.json").read_text()) for name in SPECS}
        validate_comparison(reports)
        invalid = deepcopy(reports)
        invalid["modular_mapping"]["runs"][0]["seed"] += 1
        with self.assertRaises(ValueError):
            validate_comparison(invalid)


if __name__ == "__main__":
    unittest.main()
