"""Regression tests using the published Exhaust benchmark consumer."""

import json
import unittest
from collections import Counter

from refresh_reports import (
    FIXED, PROJECT, ROOT, SPECS, compact, examples, parse_log,
    refresh_readme, summary, validate, value,
)


class RefreshReportsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports = {key: json.loads((ROOT / "failures" / f"{key}.json").read_text()) for key in SPECS}
        cls.blocks = parse_log((ROOT / "reports" / "exhaust-1.5.5-custom-100-release.log").read_text())

    def test_complete_published_run(self):
        validate(self.reports, self.blocks)
        self.assertEqual(sum(map(len, self.reports.values())), 2808)

    def test_real_readme_is_idempotent(self):
        text = (PROJECT / "README.md").read_text()
        self.assertEqual(refresh_readme(text, self.reports, self.blocks, "1.5.5"), text)

    def test_incomplete_seed_schedule_is_rejected(self):
        reports = dict(self.reports)
        reports["calculator"] = reports["calculator"][:-1]
        with self.assertRaisesRegex(ValueError, "seed schedule"):
            validate(reports, self.blocks)

    def test_mismatched_log_is_rejected(self):
        blocks = {key: {**block, "metrics": dict(block["metrics"])} for key, block in self.blocks.items()}
        blocks["calculator"]["metrics"]["wall (ms)"] = {"mean": 123456, "median": 123456}
        with self.assertRaisesRegex(ValueError, "wall mean"):
            validate(self.reports, blocks)

    def test_generated_counts_include_initial_failure_but_fixed_counts_do_not(self):
        for key, runs in self.reports.items():
            with self.subTest(challenge=key):
                data = summary(key, runs)
                adjustment = 0 if key in FIXED else 1
                self.assertAlmostEqual(data["mean"], sum(run["evaluations"] for run in runs) / len(runs) + adjustment)
                ordered = sorted(run["evaluations"] for run in runs)
                midpoint = len(ordered) // 2
                raw_median = ordered[midpoint] if len(ordered) % 2 else (ordered[midpoint - 1] + ordered[midpoint]) / 2
                self.assertEqual(data["median"], raw_median + adjustment)

    def test_top_three_plus_minimum_only_if_observed(self):
        minimum = SPECS["refundAllocation"][1]
        counts = Counter({"first": 40, "second": 30, "third": 20, minimum: 10})
        self.assertEqual(examples("refundAllocation", counts), ["first", "second", "third", minimum])
        del counts[minimum]
        self.assertEqual(examples("refundAllocation", counts), ["first", "second", "third"])

    def test_every_readme_exhaust_report_links_to_published_raw_data(self):
        import re
        text = (PROJECT / "README.md").read_text()
        links = re.findall(r"\[Exhaust\]\(/pbt-libraries/exhaust/reports/(\w+)\.md\)", text)
        self.assertEqual(set(links), set(SPECS))
        self.assertEqual(len(links), 36)
        for key in links:
            report = (ROOT / "reports" / f"{key}.md").read_text()
            self.assertIn(f"../failures/{key}.json", report)
            for run in self.reports[key]:
                self.assertIn(compact(key, value(run, "shrunk")).replace("|", r"\|"), report)


if __name__ == "__main__":
    unittest.main()
