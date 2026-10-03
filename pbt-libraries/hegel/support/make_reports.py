"""Generate Hegel reports and optionally refresh only its README rows (stdlib only)."""
import argparse
import ast
import itertools
import json
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]


def specifications():
    specs = {
        "binheap": ("Binary Heap", "(0, None, (0, (0, None, None), (1, None, None)))"),
        "calculator": ("Calculator", "('/', 0, ('+', 0, 0))"),
        "refund_allocation": ("Refund Allocation", "RefundRequest([31, 33], 4)"),
        "refund_allocation_derived": ("Refund Allocation (derived)", "RefundRequest([31, 33], 4)"),
    }
    products = {2: (5, 5), 3: (3, 3, 3), 4: (3, 2, 2, 2),
                5: (2, 2, 2, 2, 2), 6: (2, 2, 2, 2, 2, 1)}
    sequences = {2: (6, 4), 3: (4, 3, 2), 4: (3, 2, 2, 2),
                 5: (3, 2, 2, 2, 1), 6: (3, 2, 2, 2, 1, 1)}
    for depth, factors in sequences.items():
        minimal = "(" + ", ".join(map(str, factors)) + ", 0x23 + 1x1)"
        specs[f"nested_flatmap_product_sequence_{depth}"] = (
            f"Nested Flatmap (product sequence), depth {depth}", minimal)
    for depth, factors in products.items():
        specs[f"nested_flatmap_product_{depth}"] = (
            f"Nested Flatmap (product), depth {depth}", repr(factors))
    specs.update({
        "nested_flatmap_sum_4": ("Nested Flatmap (sum), depth 4", "(6, 6, 6, 6, 0x23 + 1x1)"),
        "modular_mapping": ("Modular Mapping", "925"),
        "weighted_linear_preservation": ("Weighted Linear Preservation", "(0, 0, 20)"),
        "invoice_discount": ("Invoice Discount", "Invoice(10, 100, 1)"),
        "invoice_discount_derived": ("Invoice Discount (derived)", "Invoice(10, 100, 1)"),
        "float_cancellation": ("Float Cancellation", None),
        "chunked_decoder": ("Chunked Decoder", '(text, "\\u{80}", [1, 1])'),
    })
    for modulus in (10, 100, 1000):
        specs[f"hash_collision_{modulus}"] = (
            f"Hash Collision (M = {modulus})", f"([(0, 0)], {modulus}, 1)")
    specs["snapshot_store"] = ("Snapshot Store", "[put(0, 0), s0 = snapshot(), put(0, 0), "
                               "s1 = snapshot(), compact(), read(s0, 0)]")
    for modulus in (10, 100, 1000):
        specs[f"hash_collision_state_machine_{modulus}"] = (
            f"Hash Collision (M = {modulus})", f"[put(0, 0), put({modulus}, 1)]")
    return specs


SPECS = specifications()


def value(record, field):
    return next(iter(record[field].values()))


def canonical(name, text):
    if name == "float_cancellation":
        # Rust writes 1e-5; Python writes 1e-05. Measure the same notation.
        return repr(ast.literal_eval(text))
    return text


def compact(name, text):
    text = canonical(name, text)
    if "product_sequence" not in name and name != "nested_flatmap_sum_4":
        return text
    fields = ast.literal_eval(text)
    payload = fields[-1]
    runs = " + ".join(f"{bit}x{len(list(group))}" for bit, group in itertools.groupby(payload))
    return "(" + ", ".join(map(str, fields[:-1])) + ", " + runs + ")"


def summarise(report):
    name = report["challenge"]
    runs = report["runs"]
    if not runs:
        raise ValueError(f"{name}: no runs")
    counts = Counter(compact(name, value(run, "shrunk")) for run in runs)
    return {
        "count": len(runs), "counts": counts, "distinct": len(counts),
        "evaluations": mean(run["evaluations"] for run in runs),
        "median_evaluations": median(run["evaluations"] for run in runs),
        "original_length": mean(len(canonical(name, value(run, "original"))) for run in runs),
        "total_ms": 1000 * mean(run["total_seconds"] for run in runs),
    }


def examples(summary, minimal, limit=None):
    entries = summary["counts"].most_common(limit)
    if limit and minimal in summary["counts"] and minimal not in dict(entries):
        entries.append((minimal, summary["counts"][minimal]))
    return [(text, 100 * count / summary["count"], text == minimal) for text, count in entries]


def code(text):
    # Backticks inside text and pipes inside table cells need Markdown protection.
    delimiter = "`" * (1 + max((len(m[0]) for m in re.finditer(r"`+", text)), default=0))
    return delimiter + text.replace("|", "\\|") + delimiter


def table_row(report):
    name = report["challenge"]
    summary = summarise(report)
    minimal = SPECS[name][1]
    top = "<br>".join(f"{percent:g}% {'🎯 ' if target else ''}{code(text)}"
                        for text, percent, target in examples(summary, minimal, 3))
    return (f"|  | [Hegel](/pbt-libraries/hegel/reports/{name}.md) | {summary['distinct']} | "
            f"{summary['evaluations']:.1f} | {summary['median_evaluations']:.1f} | "
            f"{summary['original_length']:.1f} | {top} |")


def markdown(report):
    name = report["challenge"]
    title, minimal = SPECS[name]
    summary = summarise(report)
    lines = [f"# {title}", "", f"Hegel {report['hegel_version']}, native engine "
             f"{report['engine_version']}, {report['build_profile']} build. "
             f"{summary['count']} seeded runs; [raw results]({name}.json).", "",
             "| Metric | Mean |", "|---|---|",
             f"| Evaluations from first failure | {summary['evaluations']:.1f} |",
             f"| Original counterexample length | {summary['original_length']:.1f} |",
             f"| Total elapsed time (ms) | {summary['total_ms']:.2f} |", "",
             "Evaluations include the starting failure, subsequent property calls, "
             "confirmation calls and final replay. Rejected/overrun histories that "
             "never reach a property verdict are not counted. Total time includes "
             "generation, shrinking, recording and replay; phase timings are not exposed.", "",
             "Original length uses the full counterexample notation, including the complete "
             "nested payload. Payloads below use run-length notation. 🎯 matches the "
             "reference counterexample in the main comparison.", "",
             f"## Counterexamples ({summary['distinct']} distinct)", "",
             "| Share | Counterexample |", "|---|---|"]
    for text, percent, target in examples(summary, minimal):
        lines.append(f"| {percent:g}% | {'🎯 ' if target else ''}{code(text)} |")
    return "\n".join(lines) + "\n"


TOTAL_HEADER = "| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |"
TOTAL_TABLE = re.compile(re.escape(TOTAL_HEADER) + r"\n(?:\|[^\n]*\n)+")


def timing_totals(text):
    table = TOTAL_TABLE.search(text)
    if table is None:
        raise ValueError("total wall-time table is missing")
    totals = {}
    for row in table[0].splitlines()[2:]:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        label = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cells[0])
        totals[label] = tuple(Decimal(cell.replace(",", "").replace("**", ""))
                              for cell in cells[1:3])
    return totals


def refund_totals(name):
    hypothesis = json.loads((ROOT.parent / "hypothesis/challenges" / f"{name}.json").read_text())
    hypothesis_ms = Decimal(str(1000 * mean(run["total_seconds"] for run in hypothesis)))
    filename = "refundAllocationDerived" if name.endswith("_derived") else "refundAllocation"
    log = (ROOT.parent / "exhaust/reports" / f"{filename}.txt").read_text()
    match = re.search(r"^\s+wall \(ms\): .*?mean=([0-9.]+)", log, re.MULTILINE)
    if match is None:
        raise ValueError(f"{name}: Exhaust wall time is missing")
    return hypothesis_ms, Decimal(match[1])


def timing_label(name):
    return SPECS[name][0] + (" (state machine)" if "state_machine" in name else "")


def timing_table(reports, existing_totals):
    names = {timing_label(name): name for name in reports}
    labels = [label for label in existing_totals if label in names]
    labels.extend(label for label in names if label not in existing_totals)
    lines = [TOTAL_HEADER, "|---|---|---|---|"]
    for label in labels:
        name = names[label]
        totals = existing_totals.get(label)
        if totals is None:
            if not name.startswith("refund_allocation"):
                raise ValueError(f"{name}: existing wall-time row is missing")
            totals = refund_totals(name)
        numbers = [number.quantize(Decimal(".01")) for number in totals]
        numbers.append(Decimal(f"{summarise(reports[name])['total_ms']:.2f}"))
        smallest = min(numbers)
        cells = [f"**{number:,.2f}**" if number == smallest else f"{number:,.2f}"
                 for number in numbers]
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def update_comparison(text, reports):
    # Preserve other libraries' recorded wall times, never substitute phase sums.
    totals = timing_totals(text)
    updated = []
    current = None
    for line in text.splitlines():
        hegel = re.search(r"\[Hegel\]\(/pbt-libraries/hegel/reports/([^/.]+)\.(?:md|json)\)", line)
        if hegel and hegel[1] in reports:
            continue
        hypothesis = re.search(r"\[Hypothesis\]\(/pbt-libraries/hypothesis/challenges/([^/.]+)\.(?:md|json)\)", line)
        if hypothesis:
            current = hypothesis[1]
        updated.append(line)
        if "[Exhaust](/pbt-libraries/exhaust/reports/" in line and current in reports:
            updated.append(table_row(reports[current]))
            current = None
    result = "\n".join(updated).rstrip() + "\n"
    return TOTAL_TABLE.sub(lambda _: timing_table(reports, totals), result, count=1)


def validate_comparison(reports):
    if set(reports) != set(SPECS):
        raise ValueError(f"README comparison requires all {len(SPECS)} challenges")
    first = next(iter(reports.values()))
    first_seeds = [run["seed"] for run in first["runs"]]
    consecutive = bool(first_seeds) and first_seeds == list(range(first_seeds[0], first_seeds[0] + 100))
    for name, report in reports.items():
        runs = report["runs"]
        if len(runs) != 100:
            raise ValueError(f"{name}: README comparison requires 100 runs")
        if not consecutive or [run["seed"] for run in runs] != first_seeds:
            raise ValueError(f"{name}: inconsistent comparison seed schedule")
        if report["build_profile"] != "release":
            raise ValueError(f"{name}: README comparison requires a release build")
        for field in ("hegel_version", "engine_version", "build_profile", "environment"):
            if report[field] != first[field]:
                raise ValueError(f"{name}: mixed {field} metadata in comparison results")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reports", type=Path, default=ROOT / "reports")
    parser.add_argument("--update-readme", action="store_true")
    args = parser.parse_args()
    reports = {}
    for name in SPECS:
        path = args.reports / f"{name}.json"
        if path.exists():
            report = json.loads(path.read_text())
            if report["challenge"] != name:
                raise ValueError(f"{path}: challenge does not match filename")
            reports[name] = report
            path.with_suffix(".md").write_text(markdown(report))
    if not reports:
        parser.error("no result JSON files found; run the Rust runner first")
    if args.update_readme:
        try:
            validate_comparison(reports)
        except ValueError as error:
            parser.error(str(error))
        path = PROJECT / "README.md"
        path.write_text(update_comparison(path.read_text(), reports))


if __name__ == "__main__":
    main()
