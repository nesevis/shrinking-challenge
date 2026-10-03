"""Refresh Exhaust reports and README rows from one complete custom-suite run."""

import argparse
import ast
import json
import math
import re
from collections import Counter
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]


def specifications():
    specs = {
        "binaryHeap": ("Binary Heap", "(0, None, (0, (0, None, None), (1, None, None)))"),
        "calculator": ("Calculator", "('/', 0, ('+', 0, 0))"),
        "anagrams": ("Anagrams", '(" \\0", "\\0 ")'),
        "usernamePassword": ("Username and Password", '("u: 0000", "p: 0000")'),
        "duplicatedText": ("Duplicated Text", '("00000012", "00000012")'),
        "haystack": ("Haystack", '"CREEPIDIOT"'),
        "zalgoHaystack": ("Zalgo Haystack", '"THE ICHOR PERMEATES"'),
        "distinctSum": ("Distinct Sum", "[0, 1, -1, 2, 49]"),
        "leapDay": ("Leap Day", "2000-02-29 00:00:00 +0000"),
        "branchSwitching": ("Branch Switching", "1001"),
        "modularMapping": ("Modular Mapping", "925"),
        "weightedLinearPreservation": ("Weighted Linear Preservation", "(0, 0, 20)"),
        "invoiceDiscount": ("Invoice Discount", "Invoice(10, 100, 1)"),
        "invoiceDiscountDerived": ("Invoice Discount (derived)", "Invoice(10, 100, 1)"),
        "refundAllocation": ("Refund Allocation", "RefundRequest([31, 33], 4)"),
        "refundAllocationDerived": ("Refund Allocation (derived)", "RefundRequest([31, 33], 4)"),
        "floatCancellation": ("Float Cancellation", None),
        "chunkedDecoder": ("Chunked Decoder", '(text, "\\u{80}", [1, 1])'),
        "depthFourSumBind": ("Nested Flatmap (sum), depth 4", "(6, 6, 6, 6, 0x23 + 1x1)"),
        "snapshotStore": ("Snapshot Store", "[put(0, 0), s0 = snapshot(), put(0, 0), s1 = snapshot(), compact(), read(s0, 0)]"),
    }
    products = {2: (5, 5), 3: (3, 3, 3), 4: (3, 2, 2, 2), 5: (2, 2, 2, 2, 2), 6: (2, 2, 2, 2, 2, 1)}
    sequences = {2: (6, 4), 3: (4, 3, 2), 4: (3, 2, 2, 2), 5: (3, 2, 2, 2, 1), 6: (3, 2, 2, 2, 1, 1)}
    for depth, word in enumerate(("Two", "Three", "Four", "Five", "Six"), 2):
        specs[f"depth{word}ProductBind"] = (f"Nested Flatmap (product), depth {depth}", repr(products[depth]))
        reference = "(" + ", ".join(map(str, sequences[depth])) + ", 0x23 + 1x1)"
        specs[f"depth{word}ProductSequenceBind"] = (f"Nested Flatmap (product sequence), depth {depth}", reference)
    for modulus, word in ((10, "Ten"), (100, "Hundred"), (1000, "Thousand")):
        specs[f"hashCollision{word}"] = (f"Hash Collision (M = {modulus})", f"([(0, 0)], {modulus}, 1)")
        specs[f"hashCollisionStateMachine{word}"] = (f"Hash Collision (M = {modulus}) (state machine)", f"[put(0, 0), put({modulus}, 1)]")
    return specs


SPECS = specifications()
FIXED = {"anagrams", "usernamePassword", "duplicatedText", "haystack", "zalgoHaystack", "distinctSum", "leapDay", "branchSwitching"}
BY_TITLE = {title: key for key, (title, _) in SPECS.items()}


def value(run, field):
    return next(iter(run[field].values()))


def compact(key, text):
    if key.endswith("ProductSequenceBind") or key == "depthFourSumBind":
        match = re.fullmatch(r"(.*), (\d+) length, \[0,…,1(?:x(\d+))?\]", text)
        if match:
            length, ones = int(match[2]), int(match[3] or 1)
            return f"({match[1]}, 0x{length - ones} + 1x{ones})"
        fields = ast.literal_eval(text)
        payload = fields[-1]
        groups = []
        for item in payload:
            if groups and groups[-1][0] == item:
                groups[-1][1] += 1
            else:
                groups.append([item, 1])
        return "(" + ", ".join(map(str, fields[:-1])) + ", " + " + ".join(f"{item}x{count}" for item, count in groups) + ")"
    return text.replace("\0", r"\0")


def code(text):
    delimiter = "`" * (1 + max((len(match[0]) for match in re.finditer(r"`+", text)), default=0))
    return delimiter + text.replace("|", r"\|") + delimiter


def summary(key, runs):
    adjustment = 0 if key in FIXED else 1
    return {
        "counts": Counter(compact(key, value(run, "shrunk")) for run in runs),
        "mean": mean(run["evaluations"] for run in runs) + adjustment,
        "median": median(run["evaluations"] for run in runs) + adjustment,
        "original_length": mean(len(value(run, "original")) for run in runs),
        "wall": mean(run["wallMilliseconds"] for run in runs),
    }


def examples(key, counts, previous=(), limit=3):
    order = list(dict.fromkeys((*previous, *counts)))
    selected = sorted(counts, key=lambda text: (-counts[text], order.index(text)))[:limit]
    reference = SPECS[key][1]
    if reference in counts and reference not in selected:
        selected.append(reference)
    return selected


def parse_log(text):
    blocks = {}
    for block in text.split("\n\n"):
        written = re.search(r"wrote (\d+) entries to (.+\.json)", block)
        if not written:
            continue
        key = Path(written[2]).stem
        metrics = {}
        for line in block.splitlines():
            match = re.match(r"  (.+?): min=.*?median=([\d.]+) mean=([\d.]+) ", line)
            if match:
                metrics[match[1]] = {"median": float(match[2]), "mean": float(match[3])}
        blocks[key] = {"entries": int(written[1]), "metrics": metrics}
    return blocks


def validate(reports, blocks):
    if set(reports) != set(SPECS) or set(blocks) != set(SPECS):
        raise ValueError("requires all 36 custom challenges and matching log blocks")
    for key, runs in reports.items():
        expected_seeds = [1337] if key in FIXED else list(range(1337, 1437))
        if [run["seed"] for run in runs] != expected_seeds or blocks[key]["entries"] != len(runs):
            raise ValueError(f"{key}: incomplete seed schedule or mismatched log")
        for run in runs:
            if not isinstance(run["evaluations"], int) or run["evaluations"] < 0:
                raise ValueError(f"{key}: invalid evaluation count")
            if not math.isfinite(run["wallMilliseconds"]) or run["wallMilliseconds"] <= 0:
                raise ValueError(f"{key}: invalid wall time")
            for field in ("original", "shrunk"):
                if len(run[field]) != 1 or not isinstance(value(run, field), str):
                    raise ValueError(f"{key}: missing input description")
        metrics = blocks[key]["metrics"]
        if abs(metrics["evaluations"]["mean"] - mean(run["evaluations"] for run in runs)) > .051:
            raise ValueError(f"{key}: evaluation mean differs from log")
        if abs(metrics["evaluations"]["median"] - median(run["evaluations"] for run in runs)) > .051:
            raise ValueError(f"{key}: evaluation median differs from log")
        if abs(metrics["wall (ms)"]["mean"] - mean(run["wallMilliseconds"] for run in runs)) > .00051:
            raise ValueError(f"{key}: wall mean differs from log")


def refresh_readme(text, reports, blocks, version):
    mode, label = None, None
    occurrences = Counter()
    updated = []
    quality_count = phase_count = total_count = 0
    for line in text.splitlines():
        if line.startswith("## "):
            mode = {"## Fixed start": "fixed", "## 100 seeds": "generated", "## Handwritten and derived generators": "generated", "## State machines": "state", "## Apples-to-oranges timings": "phase", "## Total timings": "total"}.get(line)
        if line.startswith("| "):
            cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip("|"))]
            if mode in ("fixed", "generated", "state"):
                if cells[0] in BY_TITLE:
                    label = cells[0] + (" (state machine)" if mode == "state" and cells[0].startswith("Hash Collision") else "")
                if len(cells) > 1 and cells[1].startswith("[Exhaust]"):
                    key = BY_TITLE[label]
                    runs = reports[key]
                    data = summary(key, runs)
                    cells[1] = f"[Exhaust](/pbt-libraries/exhaust/reports/{key}.md)"
                    if mode == "fixed":
                        example = compact(key, value(runs[0], "shrunk"))
                        cells[2] = str(runs[0]["evaluations"])
                        cells[3] = ("🎯 " if example == SPECS[key][1] else "") + code(example)
                    else:
                        previous = re.findall(r"`([^`]+)`", cells[-1])
                        chosen = examples(key, data["counts"], previous)
                        cells[2:6] = [str(len(data["counts"])), f"{data['mean']:.1f}", f"{data['median']:.1f}", f"{data['original_length']:.1f}"]
                        cells[6] = "<br>".join(f"{100 * data['counts'][example] / len(runs):g}% {'🎯 ' if example == SPECS[key][1] else ''}{code(example)}" for example in chosen)
                    line = "| " + " | ".join(cells) + " |"
                    quality_count += 1
            elif mode == "phase" and cells[0] in BY_TITLE:
                title = cells[0]
                occurrence = occurrences[title]
                occurrences[title] += 1
                if title.startswith("Hash Collision") and occurrence:
                    title += " (state machine)"
                key = BY_TITLE[title]
                metrics = blocks[key]["metrics"]
                if key in FIXED:
                    cells[2] = "—"
                elif key == "snapshotStore" or "StateMachine" in key:
                    cells[2] = f"{metrics['total (ms)']['mean'] - metrics['reductions (ms)']['mean']:,.2f}"
                else:
                    cells[2] = f"{metrics['generation (ms)']['mean']:.3f}"
                cells[4] = f"{metrics['reductions (ms)']['mean']:,.2f}"
                line = "| " + " | ".join(cells) + " |"
                phase_count += 1
            elif mode == "total" and cells[0] in BY_TITLE:
                key = BY_TITLE[cells[0]]
                cells[2] = f"{summary(key, reports[key])['wall']:,.2f}"
                numbers = [float(cell.replace(",", "").replace("**", "")) for cell in cells[1:]]
                cells[1:] = [f"**{cell.replace('**', '')}**" if number == min(numbers) else cell.replace("**", "") for cell, number in zip(cells[1:], numbers)]
                line = "| " + " | ".join(cells) + " |"
                total_count += 1
        updated.append(line)
    if (quality_count, phase_count, total_count) != (36, 34, 28):
        raise ValueError(f"unexpected README coverage: {quality_count}, {phase_count}, {total_count}")
    result = "\n".join(updated) + "\n"
    result, count = re.subn(r"(\[Exhaust\]\(/pbt-libraries/exhaust/README\.md\) )\d+\.\d+\.\d+", lambda match: match[1] + version, result, count=1)
    if count != 1:
        raise ValueError("opening Exhaust version is missing")
    return result.replace("Exhaust's refund summaries omit original-input lengths and the checkout revision.\n\n", "")


def markdown(key, runs, metrics, version, revision):
    data = summary(key, runs)
    fixed = key in FIXED
    description = "One fixed-start reduction." if fixed else "100 runs on seeds 1337–1436; 100 failures."
    lines = [f"# {SPECS[key][0]}", "", f"Exhaust {version}, release build. {description}", "", f"[Raw results](../failures/{key}.json). Dependency revision: `{revision}`.", "", "| Metric | Mean | Median |", "|---|---:|---:|", f"| Reduction invocations | {mean(run['evaluations'] for run in runs):.1f} | {median(run['evaluations'] for run in runs):.1f} |", f"| Original input length | {data['original_length']:.1f} | {median(len(value(run, 'original')) for run in runs):.1f} |", f"| Wall time (ms) | {data['wall']:.3f} | {median(run['wallMilliseconds'] for run in runs):.3f} |"]
    for name in ("generation (ms)", "reductions (ms)", "total (ms)"):
        if name in metrics:
            lines.append(f"| {name} | {metrics[name]['mean']:.3f} | {metrics[name]['median']:.3f} |")
    lines.extend(["", "The main README adds the original failing call to generated-run evaluation counts; fixed-start counts are used directly.", "", f"## Counterexamples ({len(data['counts'])} distinct)", "", "| Share | Counterexample |", "|---|---|"])
    for example, count in data["counts"].most_common():
        lines.append(f"| {100 * count / len(runs):g}% | {'🎯 ' if example == SPECS[key][1] else ''}{code(example)} |")
    lines.extend(["", "## Running", "", "```sh", f"swift run -c release ExhaustRunner --challenge {key} --iterations 100 --seed 1337 --report-path ../failures", "```", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--failures", type=Path, default=ROOT / "failures")
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, default=ROOT / "reports")
    parser.add_argument("--readme", type=Path, default=PROJECT / "README.md")
    parser.add_argument("--update-readme", action="store_true")
    args = parser.parse_args()
    log = args.log.read_text()
    provenance = re.search(r"Verified Exhaust ([\d.]+): ([0-9a-f]{40})", log)
    if provenance is None:
        parser.error("verified dependency version and revision are missing from log")
    version, revision = provenance.groups()
    reports = {key: json.loads((args.failures / f"{key}.json").read_text()) for key in SPECS}
    blocks = parse_log(log)
    validate(reports, blocks)
    readme = refresh_readme(args.readme.read_text(), reports, blocks, version) if args.update_readme else None
    args.report_dir.mkdir(parents=True, exist_ok=True)
    for key, runs in reports.items():
        (args.report_dir / f"{key}.md").write_text(markdown(key, runs, blocks[key]["metrics"], version, revision))
    if readme is not None:
        args.readme.write_text(readme)
    print(f"Validated and reported {len(reports)} challenges, {sum(map(len, reports.values()))} entries.")


if __name__ == "__main__":
    main()
