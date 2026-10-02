"""Fixture and public-generator checks for the wrong binary heap port."""
import runpy
import unittest
from pathlib import Path

from hypothesis import Phase, given, settings


CHALLENGE = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / "challenges/binheap.py")
)


class BinaryHeapTests(unittest.TestCase):
    def test_known_four_node_failure(self):
        heap = (0, None, (0, (0, None, None), (1, None, None)))
        self.assertTrue(CHALLENGE["heap_invariant"](heap))
        self.assertEqual(CHALLENGE["wrong_to_sorted_list"](heap), [0, 0, 1, 0])
        self.assertFalse(CHALLENGE["invariant"](heap))
        self.assertTrue(CHALLENGE["invariant"](None))
        self.assertTrue(CHALLENGE["invariant"]((0, None, (1, None, None))))

    @settings(max_examples=50, database=None, phases=[Phase.generate], derandomize=True)
    @given(CHALLENGE["strategy"])
    def test_generated_heaps(self, heap):
        self.assertTrue(CHALLENGE["heap_invariant"](heap))
        original = CHALLENGE["heap_to_list"](heap)
        self.assertLessEqual(len(original), 31)
        self.assertEqual(sorted(original), sorted(CHALLENGE["wrong_to_sorted_list"](heap)))

    @settings(max_examples=20, database=None, phases=[Phase.generate], derandomize=True)
    @given(CHALLENGE["heaps"](minimum=CHALLENGE["MAX_KEY"], depth=20))
    def test_maximum_key_boundary(self, heap):
        self.assertTrue(all(key == CHALLENGE["MAX_KEY"] for key in CHALLENGE["heap_to_list"](heap)))
        self.assertTrue(CHALLENGE["invariant"](heap))


if __name__ == "__main__":
    unittest.main()
