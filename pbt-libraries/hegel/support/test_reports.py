import json
import unittest
from copy import deepcopy

from make_reports import ROOT, SPECS, code, compact, examples, markdown, summarise, table_row, timing_table, phase_time_totals, update_comparison, validate_comparison


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
        data = report()
        summary = summarise(data)
        self.assertEqual(summary["distinct"], 2)
        self.assertEqual(summary["evaluations"], 2)
        self.assertEqual(summary["total_ms"], 1)
        self.assertIn("66.6667% 🎯 `925`", table_row(data))

    def test_refresh_is_idempotent_and_preserves_other_libraries(self):
        text = ("User introduction\n"
                "| Modular Mapping | [Hypothesis](/pbt-libraries/hypothesis/challenges/modular_mapping.md) | original |\n"
                "|  | [Exhaust](/pbt-libraries/exhaust/reports/modularMapping.md) | original |\n"
                "\nUser timing note\n"
                "| Challenge | Hypothesis generation (ms) | Exhaust generation (ms) | Hypothesis reduction (ms) | Exhaust reduction (ms) |\n"
                "|---|---|---|---|---|\n"
                "| Modular Mapping | 4.33 | 0.01 | 3.23 | 0.02 |\n")
        data = {"modular_mapping": report()}
        first = update_comparison(text, data)
        self.assertEqual(update_comparison(first, data), first)
        self.assertIn("User introduction", first)
        self.assertIn("User timing note", first)
        self.assertIn("modularMapping.md) | original |", first)
        self.assertEqual(first.count("[Hegel]("), 1)
        self.assertNotIn("<!-- hegel-timings:", first)
        with_following_section = first + "\n## User section\nKeep this text.\n"
        self.assertEqual(update_comparison(with_following_section, data), with_following_section)

    def test_timing_totals_distinguish_generator_and_state_machine_rows(self):
        text = ("| Challenge | Hypothesis generation (ms) | Exhaust generation (ms) | Hypothesis reduction (ms) | Exhaust reduction (ms) |\n"
                "|---|---|---|---|---|\n"
                "| Hash Collision (M = 1000) | 1,055 | 0.95 | 62.61 | 0.60 |\n"
                "| Hash Collision (M = 1000) | 56.09 | 0.16 | 392 | 2.02 |\n")
        data = {name: report(name) for name in
                ("hash_collision_1000", "hash_collision_state_machine_1000")}
        table = timing_table(data, phase_time_totals(text))
        self.assertIn("hash_collision_1000.md) | 1,117.61 | 1.55 | 1.00 |", table)
        self.assertIn("hash_collision_state_machine_1000.md) | 448.09 | 2.18 | 1.00 |", table)

    def test_markdown_protects_table_pipes_and_embedded_backticks(self):
        self.assertEqual(code('(text, "a|b`c", [1, 1])'), '``(text, "a\\|b`c", [1, 1])``')

    def test_comparison_rejects_mixed_or_unpaired_results(self):
        reports = {name: report(name, (925,) * 100) for name in SPECS}
        seeds = {name: list(range(100)) for name in SPECS}
        validate_comparison(reports, seeds)
        for change in ("count", "seed", "environment", "profile"):
            invalid = deepcopy(reports)
            item = invalid["modular_mapping"]
            if change == "count":
                item["runs"].pop()
            elif change == "seed":
                item["runs"][0]["seed"] = 999
            elif change == "environment":
                item["environment"]["cpu"] = "different CPU"
            else:
                item["build_profile"] = "debug"
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_comparison(invalid, seeds)

    def test_committed_seed_lists_match_hypothesis(self):
        seeds = json.loads((ROOT / "support/seeds.json").read_text())
        self.assertEqual(set(seeds), set(SPECS))
        for name, values in seeds.items():
            hypothesis = json.loads((ROOT.parent / "hypothesis/challenges" / f"{name}.json").read_text())
            self.assertEqual(values, [run["seed"] for run in hypothesis])
            self.assertEqual(len(values), 100)


if __name__ == "__main__":
    unittest.main()
