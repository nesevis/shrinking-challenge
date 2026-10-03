"""Check Exhaust's recorded inputs against independent challenge oracles."""

import ast
import datetime
import json
import os
import re
import sys
import unicodedata
import unittest
from pathlib import Path

from refresh_reports import ROOT, SPECS, value

# Shared benchmark contracts, not an invocation of any shrinking library.
sys.path.insert(0, str(ROOT.parent / "hegel" / "support"))
from test_results import commands, hash_step, is_failure

ALIASES = {
    "binaryHeap": "binheap",
    "modularMapping": "modular_mapping",
    "weightedLinearPreservation": "weighted_linear_preservation",
    "invoiceDiscount": "invoice_discount",
    "invoiceDiscountDerived": "invoice_discount_derived",
    "refundAllocation": "refund_allocation",
    "refundAllocationDerived": "refund_allocation_derived",
    "floatCancellation": "float_cancellation",
    "chunkedDecoder": "chunked_decoder",
    "depthFourSumBind": "nested_flatmap_sum_4",
}
for depth, word in enumerate(("Two", "Three", "Four", "Five", "Six"), 2):
    ALIASES[f"depth{word}ProductBind"] = f"nested_flatmap_product_{depth}"
    ALIASES[f"depth{word}ProductSequenceBind"] = f"nested_flatmap_sequence_{depth}"
for modulus, word in ((10, "Ten"), (100, "Hundred"), (1000, "Thousand")):
    ALIASES[f"hashCollision{word}"] = f"hash_collision_{modulus}"


def calculator_fails(text):
    expression = ast.literal_eval(text)
    def validate(node, depth=0):
        if isinstance(node, int):
            assert -2**63 <= node <= 2**63 - 1
            return
        assert depth < 5
        operation, left, right = node
        assert operation in ("+", "/") and not (operation == "/" and right == 0)
        validate(left, depth + 1)
        validate(right, depth + 1)
    def evaluate(node):
        if isinstance(node, int):
            return node
        operation, left, right = node
        if operation == "+":
            return (evaluate(left) + evaluate(right) + 2**63) % 2**64 - 2**63
        denominator = evaluate(right)
        if denominator == 0:
            raise ZeroDivisionError
        numerator = evaluate(left)
        assert not (numerator == -2**63 and denominator == -1)
        quotient = abs(numerator) // abs(denominator)
        return -quotient if (numerator < 0) != (denominator < 0) else quotient
    validate(expression)
    try:
        evaluate(expression)
    except ZeroDivisionError:
        return True
    return False


def snapshot_fails(text):
    writes, versions, snapshots = [], {}, {}
    created = 0
    for command in commands(text):
        if command.startswith("put("):
            key, val = ast.literal_eval(command[3:])
            assert 0 <= key <= 9 and 0 <= val <= 9
            writes.append((key, val))
            versions.setdefault(key, []).append((len(writes), val))
        elif " = snapshot()" in command:
            name = command.split(" = ")[0]
            assert name == f"s{created}"
            created += 1
            snapshots[name] = len(writes)
        elif command.startswith("release("):
            name = command[8:-1]
            assert name in snapshots
            del snapshots[name]
        elif command == "compact()":
            horizon = max(snapshots.values(), default=len(writes))
            for key, history in versions.items():
                floors = [i for i, (stamp, _) in enumerate(history) if stamp <= horizon]
                if floors:
                    versions[key] = history[floors[-1]:]
        else:
            if command.startswith("read("):
                name, key = command[5:-1].split(", ")
                key = int(key)
                assert name in snapshots
                visible = snapshots[name]
            else:
                assert command.startswith("get(")
                key = int(command[4:-1])
                visible = len(writes)
            assert 0 <= key <= 9
            actual = next((v for stamp, v in reversed(versions.get(key, [])) if stamp <= visible), None)
            expected = next((v for k, v in reversed(writes[:visible]) if k == key), None)
            if actual != expected:
                return True
    return False


def failure(key, text):
    if key.endswith("ProductSequenceBind") or key == "depthFourSumBind":
        match = re.fullmatch(r"(.*), (\d+) length, \[0,…,1(?:x(\d+))?\]", text)
        if match:
            # The runner records payload length and one-count, not positions.
            length, ones = int(match[2]), int(match[3] or 1)
            assert 0 < ones <= length
            text = f"({match[1]}, {repr([0] * (length - ones) + [1] * ones)})"
    if key in ALIASES:
        return is_failure(ALIASES[key], text)
    if key == "calculator":
        return calculator_fails(text)
    if key == "snapshotStore":
        # Exhaust can retain an unexecuted suffix after the first failing command.
        return snapshot_fails(text)
    if key.startswith("hashCollisionStateMachine"):
        modulus = {"Ten": 10, "Hundred": 100, "Thousand": 1000}[key.removeprefix("hashCollisionStateMachine")]
        entries, keys = [], set()
        for step in commands(text):
            assert step.startswith("put(")
            k, val = ast.literal_eval(step[3:])
            if not hash_step(entries, keys, modulus, k, val):
                return True
        return False
    if key in ("anagrams", "usernamePassword", "duplicatedText"):
        left, right = ast.literal_eval(text.replace("\0", r"\0"))
        if key == "anagrams":
            return left != right and sorted(left) == sorted(right)
        if key == "duplicatedText":
            assert len(left) == len(right) == 8 and set(left + right) <= set("abcdefghijklmnopqrstuvwxyz0123456789")
            return left == right and len(set(left)) >= 3
        if not (left.startswith("u: ") and right.startswith("p: ")):
            return False
        password = right[3:]
        return len(password) >= 4 and set(password) <= set("abcdefghijklmnopqrstuvwxyz0123456789") and left[3:] == password
    if key in ("haystack", "zalgoHaystack"):
        if text.startswith('"') and text.endswith('"'):
            text = ast.literal_eval(text)
        if key == "haystack":
            return "creep" in text.casefold() and "idiot" in text.casefold()
        searchable = "".join(char for char in unicodedata.normalize("NFD", text) if unicodedata.category(char) not in ("Mn", "Mc", "Me", "Cf")).lower()
        return "the ichor permeates" in searchable
    if key == "distinctSum":
        numbers = ast.literal_eval(text)
        assert len(set(numbers)) == len(numbers)
        return len(numbers) >= 5 and sum(numbers) > 50
    if key == "leapDay":
        timestamp = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S %z")
        return (timestamp.month, timestamp.day) == (2, 29)
    if key == "branchSwitching":
        if text.startswith('"'):
            return len(ast.literal_eval(text)) >= 4
        return int(text) > 1000
    raise AssertionError(key)


class RecordedResultsTests(unittest.TestCase):
    def test_oracles_distinguish_passing_inputs(self):
        for key, passing in {
            "calculator": "('/', -3, 2)",
            "snapshotStore": "[put(0, 0), s0 = snapshot(), read(s0, 0)]",
            "hashCollisionStateMachineTen": "[put(0, 0), put(1, 1)]",
            "anagrams": '("ab", "cd")',
            "usernamePassword": '("u: 0000", "p: 0001")',
            "duplicatedText": '("00000001", "00000001")',
            "haystack": '"CREEP"',
            "zalgoHaystack": '"THE ICHOR"',
            "distinctSum": "[0, 1, 2, 3, 4]",
            "leapDay": "2088-02-28 00:00:00 +0000",
            "branchSwitching": "1000",
        }.items():
            with self.subTest(challenge=key):
                self.assertFalse(failure(key, passing))
        self.assertTrue(failure("calculator", "('/', 0, ('+', 0, 0))"))
        self.assertTrue(failure("snapshotStore", "[put(0, 0), s0 = snapshot(), put(0, 1), s1 = snapshot(), compact(), read(s0, 0), get(0)]"))

    def test_all_original_and_reduced_counterexamples(self):
        folder = Path(os.environ.get("EXHAUST_REPORT_FAILURES", ROOT / "failures"))
        checked = 0
        for key in SPECS:
            runs = json.loads((folder / f"{key}.json").read_text())
            for run in runs:
                for field in ("original", "shrunk"):
                    with self.subTest(challenge=key, seed=run["seed"], field=field):
                        self.assertTrue(failure(key, value(run, field)))
                        checked += 1
        self.assertEqual(checked, 5616)


if __name__ == "__main__":
    unittest.main()
