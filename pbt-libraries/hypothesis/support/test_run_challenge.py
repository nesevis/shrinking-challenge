import ast
import json
import tempfile
import unittest
from pathlib import Path

from hypothesis.errors import Unsatisfiable

from run_challenge import main


class AssumptionRecordingTests(unittest.TestCase):
    def test_rejected_inputs_are_not_recorded_as_original_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "assumptions.py"
            path.write_text(
                "from hypothesis import assume, given, strategies as st\n"
                "@given(st.integers(min_value=0, max_value=10))\n"
                "def test(value):\n"
                "    assume(value >= 5)\n"
                "    assert value < 5\n"
            )
            main(str(path), 1)
            records = json.loads(path.with_suffix(".json").read_text())
            self.assertEqual(len(records), 1)
            record = records[0]
            for field in ("original", "shrunk"):
                self.assertGreaterEqual(ast.literal_eval(record[field]["value"]), 5)
            self.assertGreater(record["evaluations"], 0)

    def test_all_rejected_inputs_cannot_produce_a_failure_report(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "all_rejected.py"
            path.write_text(
                "from hypothesis import assume, given, strategies as st\n"
                "@given(st.just(0))\n"
                "def test(value):\n"
                "    assume(False)\n"
            )
            with self.assertRaises(Unsatisfiable):
                main(str(path), 1)
            self.assertFalse(path.with_suffix(".json").exists())


if __name__ == "__main__":
    unittest.main()
