"""Contract, generation domain, and multi-seed harness checks for AscendingArray."""

import ast
import json
import runpy
import tempfile
import unittest
from pathlib import Path

from hypothesis import Phase, given, settings
from support.run_challenge import main

ROOT = Path(__file__).resolve().parents[1]
CHALLENGE_PATH = ROOT / "challenges/ascending_array.py"
CHALLENGE = runpy.run_path(str(CHALLENGE_PATH))


class AscendingArrayTests(unittest.TestCase):
    def test_property_contract(self):
        invariant = CHALLENGE["invariant"]
        for values in (list(range(-2, 3)), list(range(-5, 0)), list(range(5)), list(range(10))):
            self.assertFalse(invariant(values))
        for values in ([0] * 5, [0, 1, 2, 3, 4, 3]):
            self.assertTrue(invariant(values))
        for index in range(4):
            duplicate = list(range(-2, 3))
            duplicate[index + 1] = duplicate[index]
            self.assertTrue(invariant(duplicate))
            inverted = list(range(-2, 3))
            inverted[index], inverted[index + 1] = inverted[index + 1], inverted[index]
            self.assertTrue(invariant(inverted))

    def test_no_fixed_start_dispatch(self):
        self.assertNotIn("shrink_once", CHALLENGE)
        self.assertNotIn("start", CHALLENGE)
        self.assertEqual(CHALLENGE["generation_budget"], 25000)
        self.assertTrue(CHALLENGE["test"].is_hypothesis_test)

    @settings(max_examples=100, database=None, phases=[Phase.generate], derandomize=True)
    @given(CHALLENGE["strategy"])
    def test_generated_domain(self, values):
        self.assertTrue(5 <= len(values) <= 10)
        self.assertTrue(all(-(2**63) <= value < 2**63 for value in values))

    def test_real_harness_discovers_three_separate_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "ascending_array.json"
            main(str(CHALLENGE_PATH), 3, seeds=[1337, 1338, 1339], output=str(output))
            records = json.loads(output.read_text())
        self.assertEqual([r["seed"] for r in records], [1337, 1338, 1339])
        # A regression to multiple-bug discovery adds hundreds of generation calls
        # after the first failure. These seeds require fewer than 500 calls each
        # when the runner moves straight to shrinking.
        self.assertTrue(all(record["evaluations"] < 500 for record in records))
        for record in records:
            original = ast.literal_eval(record["original"]["values"])
            reduced = ast.literal_eval(record["shrunk"]["values"])
            self.assertTrue(5 <= len(original) <= 10)
            self.assertFalse(CHALLENGE["invariant"](original))
            self.assertFalse(CHALLENGE["invariant"](reduced))
            self.assertEqual(len(reduced), 5)
            self.assertGreater(record["generate_seconds"], 0)


if __name__ == "__main__":
    unittest.main()
