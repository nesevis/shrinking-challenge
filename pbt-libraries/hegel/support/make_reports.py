"""Generate Hegel reports and optionally refresh only its README rows (stdlib only)."""
import argparse
import ast
import itertools
import json
import re
from collections import Counter
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
COMPARISON_PROFILE = "debug"


def implementations():
    # Source file plus the line that dispatches each challenge, located at refresh time.
    files = {
        "binheap": ("binary_heap.rs", None),
        "calculator": ("calculator.rs", None),
        "refund_allocation": ("refund_allocation.rs", r"pub\(crate\) fn evaluate\("),
        "refund_allocation_derived": ("refund_allocation.rs", r"pub\(crate\) fn evaluate\("),
        "nested_flatmap_sum_4": ("challenges.rs", r"Self::Sum => \{"),
        "modular_mapping": ("challenges.rs", r"Self::ModularMapping => \{"),
        "weighted_linear_preservation": ("challenges.rs", r"Self::WeightedLinear => \{"),
        "invoice_discount": ("challenges.rs", r"Self::Invoice \| Self::InvoiceDerived => \{"),
        "invoice_discount_derived": ("challenges.rs", r"Self::Invoice \| Self::InvoiceDerived => \{"),
        "float_cancellation": ("challenges.rs", r"Self::FloatCancellation => \{"),
        "chunked_decoder": ("challenges.rs", r"Self::ChunkedDecoder => \{"),
        "snapshot_store": ("stateful.rs", r"Challenge::SnapshotStore => \{"),
    }
    for depth in range(2, 7):
        files[f"nested_flatmap_product_{depth}"] = ("challenges.rs", r"Self::ProductSequence\(depth\) \| Self::Product\(depth\) => \{")
        files[f"nested_flatmap_product_sequence_{depth}"] = files[f"nested_flatmap_product_{depth}"]
    for modulus in (10, 100, 1000):
        files[f"hash_collision_{modulus}"] = ("challenges.rs", r"Self::HashCollision\(modulus\) => \{")
        files[f"hash_collision_state_machine_{modulus}"] = ("stateful.rs", r"Challenge::HashCollisionMachine\(modulus\) => \{")
    return files


IMPLEMENTATIONS = implementations()


def implementation_link(name):
    filename, anchor = IMPLEMENTATIONS[name]
    link = f"/pbt-libraries/hegel/src/{filename}"
    if anchor is None:
        return link
    source = (ROOT / "src" / filename).read_text().splitlines()
    lines = [number for number, line in enumerate(source, 1) if re.search(anchor, line)]
    if len(lines) != 1:
        raise ValueError(f"{name}: expected one {anchor!r} in {filename}, found {len(lines)}")
    return f"{link}#L{lines[0]}"


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
    return (f"|  | [Hegel]({implementation_link(name)}) | {summary['distinct']} | "
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


TIMING_HEADER = "| Challenge | Hypothesis | Hegel (default/opt-1) | Exhaust (macOS) | Exhaust (Linux/Windows) |"


def timing_label(name):
    return SPECS[name][0] + (" (state machine)" if "state_machine" in name else "")


def update_timings(text, reports):
    # Only the Hegel column changes; other libraries' recorded wall times are preserved.
    names = {timing_label(name): name for name in reports}
    lines = text.splitlines()
    try:
        start = lines.index(TIMING_HEADER)
    except ValueError:
        raise ValueError("timing table is missing") from None
    updated = 0
    for index in range(start + 2, len(lines)):
        if not lines[index].startswith("| "):
            break
        cells = [cell.strip() for cell in lines[index].strip("|").split("|")]
        if cells[0] in names:
            cells[2] = f"{summarise(reports[names[cells[0]]])['total_ms']:,.2f}"
            lines[index] = "| " + " | ".join(cells) + " |"
            updated += 1
    if updated != len(reports):
        raise ValueError(f"timing table covers {updated} of {len(reports)} Hegel challenges")
    return "\n".join(lines) + "\n"


def update_comparison(text, reports):
    updated = []
    current = None
    for line in text.splitlines():
        if line.startswith("|  | [Hegel]("):
            continue
        hypothesis = re.search(r"\[Hypothesis\]\(/pbt-libraries/hypothesis/challenges/([^/.]+)\.(?:py|md|json)\)", line)
        if hypothesis:
            current = hypothesis[1]
        updated.append(line)
        if line.startswith("|  | [Exhaust](") and current in reports:
            updated.append(table_row(reports[current]))
            current = None
    return update_timings("\n".join(updated).rstrip() + "\n", reports)


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
        if report["build_profile"] != COMPARISON_PROFILE:
            raise ValueError(f"{name}: README comparison requires a {COMPARISON_PROFILE} build")
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
