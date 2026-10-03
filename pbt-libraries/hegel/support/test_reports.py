import json
import unittest
from copy import deepcopy
from decimal import Decimal
from unittest.mock import patch

from make_reports import (
    ROOT, SPECS, code, compact, examples, markdown, summarise, table_row,
    timing_table, timing_totals, update_comparison, validate_comparison,
)


def report(name="modular_mapping", values=(925, 925, 927)):
    return {
        "challenge": name, "hegel_version": "0.48.1", "engine_version": "0.44.1",
        "build_profile": "release",
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
                "| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.md) | original |\n"
                "|  | [Exhaust](/pbt-libraries/exhaust/reports/modularMapping.md) | original |\n"
                "\nUser timing note\n"
                "| Challenge | Hypothesis generation (ms) | Exhaust generation (ms) | Hypothesis reduction (ms) | Exhaust reduction (ms) |\n"
                "|---|---|---|---|---|\n"
                "| Modular Mapping | 4.33 | 0.01 | 3.23 | 0.02 |\n"
                "\n## Total timings\nKeep the timing explanation.\n"
                "| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |\n"
                "|---|---|---|---|\n"
                "| Modular Mapping | 8.37 | **0.04** | 999.00 |\n")
        data = {"modular_mapping": report()}
        first = update_comparison(text, data)
        self.assertEqual(update_comparison(first, data), first)
        self.assertIn("User introduction", first)
        self.assertIn("User timing note", first)
        self.assertIn("modularMapping.md) | original |", first)
        self.assertEqual(first.count("[Hegel]("), 1)
        self.assertIn("| Modular Mapping | 8.37 | **0.04** | 1.00 |", first)
        self.assertIn("Keep the timing explanation.", first)
        self.assertNotIn("## Hegel total timings", first)
        self.assertNotIn("[Modular Mapping]", first)
        with_following_section = first + "\n## User section\nKeep this text.\n"
        self.assertEqual(update_comparison(with_following_section, data), with_following_section)

    def test_timing_totals_preserve_wall_times_and_distinguish_state_machine_rows(self):
        text = ("| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |\n"
                "|---|---|---|---|\n"
                "| Hash Collision (M = 1000) | 1,119.13 | **1.44** | 16.08 |\n"
                "| Hash Collision (M = 1000) (state machine) | 449.59 | **1.77** | 80.75 |\n")
        data = {name: report(name) for name in
                ("hash_collision_1000", "hash_collision_state_machine_1000")}
        table = timing_table(data, timing_totals(text))
        self.assertIn("| Hash Collision (M = 1000) | 1,119.13 | 1.44 | **1.00** |", table)
        self.assertIn("| Hash Collision (M = 1000) (state machine) | 449.59 | 1.77 | **1.00** |", table)
        self.assertNotIn("/hegel/reports/", table)

    def test_refund_json_links_refresh_without_moving_its_table(self):
        text = ("## Handwritten and derived generators\n"
                "| Refund Allocation | [Hypothesis](/pbt-libraries/hypothesis/challenges/refund_allocation.json) | original |\n"
                "|  | [Exhaust](/pbt-libraries/exhaust/reports/refundAllocation.txt) | original |\n"
                "|  | [Hegel](/pbt-libraries/hegel/reports/refund_allocation.json) | old |\n"
                "\n## State machines\nKeep this section.\n"
                "\n## Total timings\n"
                "| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |\n"
                "|---|---|---|---|\n")
        data = {"refund_allocation": report("refund_allocation", ("RefundRequest([31, 33], 4)",))}
        with patch("make_reports.refund_totals", return_value=(Decimal("95.83"), Decimal("3.96"))):
            first = update_comparison(text, data)
            self.assertEqual(first, update_comparison(first, data))
        self.assertIn("| Refund Allocation | 95.83 | 3.96 | **1.00** |", first)
        self.assertIn("[Hegel](/pbt-libraries/hegel/reports/refund_allocation.md)", first.split("## State machines")[0])
        self.assertIn("## State machines\nKeep this section.", first)
        self.assertEqual(first.count("[Hegel]("), 1)

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
                item["build_profile"] = "debug"
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
