"""Replay recorded counterexamples against independent fixture checks."""
import ast
import json
import math
import re
import unittest

from make_reports import ROOT, SPECS, value


def hash_put(entries, modulus, key, val):
    for index, (old, _) in enumerate(entries):
        if old % modulus == key % modulus:
            entries[index] = (old, val)
            return
    entries.append((key, val))


def hash_get(entries, modulus, key):
    return next((val for old, val in entries if old % modulus == key % modulus), None)


def hash_step(entries, keys, modulus, key, val):
    assert 0 <= key < 10 * modulus and 0 <= val <= 9
    others = sorted(keys - {key})
    before = [hash_get(entries, modulus, k) for k in others]
    hash_put(entries, modulus, key, val)
    keys.add(key)
    return before == [hash_get(entries, modulus, k) for k in others]


def commands(text):
    parts = re.findall(r"s\d+ = snapshot\(\)|(?:put|read)\([^)]*\)|(?:get|release)\([^)]*\)|compact\(\)", text)
    assert "[" + ", ".join(parts) + "]" == text
    assert len(parts) <= 50
    return parts


def snapshot_fails(text):
    writes, versions, snapshots = [], {}, {}
    created = 0
    steps = commands(text)
    for index, command in enumerate(steps):
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
                return index == len(steps) - 1
    return False


def decode_text(literal):
    assert literal[0] == literal[-1] == '"'
    text, i = [], 1
    while i < len(literal) - 1:
        if literal[i] != "\\":
            text.append(literal[i])
            i += 1
        elif literal[i + 1] == "u":
            end = literal.index("}", i)
            text.append(chr(int(literal[i + 3:end], 16)))
            i = end + 1
        else:
            assert literal[i + 1] in ('"', "\\")
            text.append(literal[i + 1])
            i += 2
    return "".join(text)


def is_failure(name, text):
    if name.startswith("nested_flatmap_"):
        fields = ast.literal_eval(text)
        with_payload = "sequence" in name or "sum" in name
        factors = fields[:-1] if with_payload else fields
        assert len(factors) == int(name.rsplit("_", 1)[1])
        upper = 100 if "sum" in name else 10
        for factor in factors:
            assert 1 <= factor <= upper
            upper = factor
        size = sum(factors) if "sum" in name else math.prod(factors)
        if not with_payload:
            return size >= 24
        payload = fields[-1]
        assert len(payload) == size and set(payload) <= {0, 1}
        return size >= 24 and 1 in payload
    if name == "modular_mapping":
        n = int(text)
        assert 0 <= n <= 1000
        return n >= 900
    if name == "weighted_linear_preservation":
        x, y, z = ast.literal_eval(text)
        assert all(0 <= n <= 20 for n in (x, y, z))
        return 2 * x + y + z == 20
    if name.startswith("invoice_discount"):
        p, q, d = ast.literal_eval(text[len("Invoice"):])
        valid = 1 <= p <= 1000 and 1 <= q <= 100 and 0 <= d <= 50 and (p * q >= 1000 or d == 0)
        return valid and (p * (100 - d) // 100) * q != p * q * (100 - d) // 100
    if name == "float_cancellation":
        a, b = ast.literal_eval(text)
        assert all(math.isfinite(x) and -1e6 <= x <= 1e6 for x in (a, b))
        return (a + b) - b != a
    if name == "chunked_decoder":
        assert text.startswith("(text, ")  # Binary messages cannot fail this property.
        literal, sizes = text[7:-1].rsplit(", [", 1)
        sizes = "[" + sizes
        original = decode_text(literal)
        assert len(original) <= 16
        data = original.encode("utf-8")
        sizes = ast.literal_eval(sizes)
        assert sum(sizes) == len(data) and all(n > 0 for n in sizes)
        offset, chunks = 0, []
        for size in sizes:
            chunks.append(data[offset:offset + size])
            offset += size
        return "".join(chunk.decode("utf-8", errors="replace") for chunk in chunks) != original
    if name == "snapshot_store":
        return snapshot_fails(text)
    if name.startswith("hash_collision_state_machine_"):
        modulus = int(name.rsplit("_", 1)[1])
        entries, keys = [], set()
        steps = commands(text)
        for index, step in enumerate(steps):
            assert step.startswith("put(")
            key, val = ast.literal_eval(step[3:])
            if not hash_step(entries, keys, modulus, key, val):
                return index == len(steps) - 1
        return False
    if name.startswith("hash_collision_"):
        modulus = int(name.rsplit("_", 1)[1])
        initial, key, val = ast.literal_eval(text)
        assert len(initial) <= 20
        entries, keys = [], set()
        for k, v in initial:
            assert 0 <= k < 10 * modulus and 0 <= v <= 9
            hash_put(entries, modulus, k, v)
            keys.add(k)
        return not hash_step(entries, keys, modulus, key, val)
    raise AssertionError(name)


class RecordedResultsTests(unittest.TestCase):
    def test_every_recorded_original_and_reduced_example_reproduces(self):
        seeds = json.loads((ROOT / "support/seeds.json").read_text())
        for name in SPECS:
            path = ROOT / "reports" / f"{name}.json"
            with self.subTest(challenge=name):
                report = json.loads(path.read_text())
                self.assertEqual(report["challenge"], name)
                self.assertEqual(report["build_profile"], "release")
                runs = report["runs"]
                self.assertEqual([r["seed"] for r in runs], seeds[name])
                for record in runs:
                    with self.subTest(seed=record["seed"]):
                        self.assertGreater(record["evaluations"], 0)
                        self.assertGreater(record["total_seconds"], 0)
                        self.assertTrue(is_failure(name, value(record, "original")))
                        self.assertTrue(is_failure(name, value(record, "shrunk")))


if __name__ == "__main__":
    unittest.main()
