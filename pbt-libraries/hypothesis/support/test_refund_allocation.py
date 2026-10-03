"""Contract, public-generator, rejection-recording, and runner checks."""

import ast
import json
import runpy
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from hypothesis import HealthCheck, Phase, given, settings
from hypothesis.errors import UnsatisfiedAssumption

# The benchmark entry point makes support/ importable when executing challenge files.
SUPPORT = Path(__file__).resolve().parent
sys.path.insert(0, str(SUPPORT))
import refund_allocation_model as refund
from run_challenge import main as run_challenge


HANDWRITTEN = runpy.run_path(str(SUPPORT.parent / "challenges/refund_allocation.py"))
DERIVED = runpy.run_path(
    str(SUPPORT.parent / "challenges/refund_allocation_derived.py")
)


def request(payments, amount):
    return refund.RefundRequest(
        [refund.Charge(payment) for payment in payments], amount
    )


def repaired_allocations(value):
    # Exact rational shares provide an independent arithmetic representation.
    total = refund.total_refundable(value.charges)
    shares = [
        Fraction(value.refund_cents * charge.refundable_cents, total)
        for charge in value.charges
    ]
    allocations = [share.numerator // share.denominator for share in shares]
    priority = sorted(
        range(len(shares)), key=lambda i: (-(shares[i] - allocations[i]), i)
    )
    for i in priority[: value.refund_cents - sum(allocations)]:
        allocations[i] += 1
    return allocations


class RefundAllocationTests(unittest.TestCase):
    def test_fee_imbalance_and_shared_representation(self):
        value = request([31, 33], 4)
        self.assertEqual(repr(value), "RefundRequest([31, 33], 4)")
        self.assertEqual(refund.allocate_refund(value), [2, 2])
        self.assertFalse(refund.invariant(value))
        self.assertTrue(refund.satisfies_contract(value, [1, 3]))
        for value in [
            request([31, 34], 2),
            request([33, 31], 2),
            request([31, 31, 33], 3),
        ]:
            self.assertEqual(sum(refund.allocate_refund(value)), value.refund_cents)
            self.assertFalse(refund.invariant(value))
            self.assertTrue(
                refund.satisfies_contract(value, repaired_allocations(value))
            )

    def test_small_passing_requests_and_stable_remainder_ties(self):
        for value in [request([31, 31], 1), request([31], 1), request([31, 33], 0)]:
            self.assertTrue(refund.invariant(value))
        value = request([31, 31], 1)
        self.assertTrue(refund.satisfies_contract(value, [1, 0]))
        self.assertFalse(refund.satisfies_contract(value, [0, 1]))
        self.assertFalse(refund.satisfies_contract(value, [1]))
        self.assertFalse(refund.satisfies_contract(value, [-1, 2]))
        self.assertFalse(refund.satisfies_contract(value, [0, 0]))

    def test_domain_boundaries_and_unrelated_overflow_are_excluded(self):
        for value in [
            request([], 0),
            request([30], 0),
            request([-(2**63)], 0),
            request([31], -1),
            request([31], 2),
            request([31] * 21, 0),
            request([refund.MAX_AMOUNT + 1], 0),
            request([refund.MAX_AMOUNT] * 2, refund.MAX_AMOUNT + 1),
        ]:
            self.assertFalse(refund.is_valid(value))
            self.assertFalse(refund.satisfies_contract(value, []))
        value = request([refund.MAX_AMOUNT] * 20, refund.MAX_AMOUNT)
        self.assertTrue(refund.is_valid(value))
        self.assertTrue(refund.invariant(value))

    @settings(
        max_examples=2000, database=None, phases=[Phase.generate], derandomize=True
    )
    @given(refund.requests())
    def test_constructive_requests_and_correct_net_allocations(self, value):
        self.assertTrue(refund.is_valid(value))
        self.assertTrue(refund.satisfies_contract(value, repaired_allocations(value)))
        self.assertEqual(sum(refund.allocate_refund(value)), value.refund_cents)
        self.assertTrue(
            refund.invariant(
                request(
                    [value.charges[0].paid_cents],
                    min(value.refund_cents, value.charges[0].refundable_cents),
                )
            )
        )

    @settings(
        max_examples=2000,
        database=None,
        phases=[Phase.generate],
        derandomize=True,
        suppress_health_check=list(HealthCheck),
    )
    @given(DERIVED["requests"])
    def test_raw_inference_and_invalid_input_rejection(self, value):
        self.assertIsInstance(value, refund.RefundRequest)
        self.assertTrue(
            all(isinstance(charge, refund.Charge) for charge in value.charges)
        )
        if refund.is_valid(value):
            self.assertTrue(
                refund.satisfies_contract(value, repaired_allocations(value))
            )
        else:
            with self.assertRaises(UnsatisfiedAssumption):
                DERIVED["test"].hypothesis.inner_test(value)

    def test_existing_harness_records_real_failures_for_both_variants(self):
        for name in ["refund_allocation", "refund_allocation_derived"]:
            source = (SUPPORT.parent / "challenges" / f"{name}.py").read_text()
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / f"{name}.py"
                path.write_text(source)
                run_challenge(str(path), n_runs=1)
                results = json.loads(path.with_suffix(".json").read_text())
                self.assertEqual(len(results), 1)
                result = results[0]
                self.assertGreater(result["evaluations"], 0)
                for field in ["original", "shrunk"]:
                    rendered = result[field]["request"]
                    self.assertTrue(rendered.startswith("RefundRequest("))
                    payments, amount = ast.literal_eval(
                        rendered[len("RefundRequest(") : -1]
                    )
                    value = request(payments, amount)
                    self.assertTrue(refund.is_valid(value))
                    self.assertFalse(refund.invariant(value))


if __name__ == "__main__":
    unittest.main()
