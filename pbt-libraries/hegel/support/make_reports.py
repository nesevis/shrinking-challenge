"""Generate Hegel reports and optionally refresh only its README rows (stdlib only)."""
import argparse
import ast
import itertools
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]


def specifications():
    specs = {}
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
            f"{summary['evaluations']:.1f} | {summary['original_length']:.1f} | {top} |")


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


def phase_time_totals(text):
    header = "| Challenge | Hypothesis generation (ms) | Exhaust generation (ms) | Hypothesis reduction (ms) | Exhaust reduction (ms) |"
    if header not in text:
        raise ValueError("Hypothesis/Exhaust phase timing table is missing")
    rows = text.split(header, 1)[1].strip().splitlines()
    totals = defaultdict(list)
    for row in rows:
        if not row.startswith("|"):
            break
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        if cells[0].startswith("---"):
            continue
        numbers = [Decimal(cell.replace(",", "")) if cell != "—" else Decimal(0)
                   for cell in cells[1:]]
        totals[cells[0]].append((numbers[0] + numbers[2], numbers[1] + numbers[3]))
    return totals


def timing_table(reports, phase_totals):
    report = next(iter(reports.values()))
    env = report["environment"]
    machine = env.get("cpu") or env["arch"]
    system = "macOS" if env["os"] == "macos" else env["os"]
    version = env.get("os_version") or "(version not recorded)"
    lines = ["## Hegel total timings", "",
             f"Hegel {report['hegel_version']} / libhegel {report['engine_version']}, "
             f"{env['rustc']}, {report['build_profile']} build with a statically linked native "
             f"engine, on {machine} running {system} {version}. "
             "These are total wall-clock milliseconds per run, including generation, "
             "reduction, counterexample recording, confirmation calls and final replay. "
             "They are not reduction-only timings. Hegel does not expose structured "
             "phase durations through its Rust API. Hypothesis and Exhaust totals below "
             "are the sums of their mean generation and reduction times in the preceding "
             "table, using its displayed values.", "",
             "| Challenge | Hypothesis total (ms) | Exhaust total (ms) | Hegel total (ms) |",
             "|---|---|---|---|"]
    for name in SPECS:
        if name in reports:
            label = SPECS[name][0]
            occurrence = 1 if "state_machine" in name else 0
            if label not in phase_totals or occurrence >= len(phase_totals[label]):
                raise ValueError(f"{name}: matching phase timing row is missing")
            hypothesis, exhaust = phase_totals[label][occurrence]
            if "state_machine" in name:
                label += " (state machine)"
            lines.append(f"| [{label}](/pbt-libraries/hegel/reports/{name}.md) | "
                         f"{hypothesis:,.2f} | {exhaust:,.2f} | "
                         f"{summarise(reports[name])['total_ms']:,.2f} |")
    return "\n".join(lines)


def update_comparison(text, reports):
    # Preserve every existing library's data and any unrelated user edits.
    phase_totals = phase_time_totals(text)
    lines = text.splitlines()
    updated = []
    current = None
    for line in lines:
        if "[Hegel](/pbt-libraries/hegel/reports/" in line:
            continue
        if "[Hypothesis](/pbt-libraries/hypothesis/challenges/" in line:
            current = line.split("/challenges/", 1)[1].split(".md", 1)[0]
        updated.append(line)
        if "[Exhaust](/pbt-libraries/exhaust/reports/" in line and current in reports:
            updated.append(table_row(reports[current]))
            current = None
    result = "\n".join(updated).rstrip() + "\n"
    heading = "## Hegel total timings"
    if heading in result:
        before, remaining = result.split(heading, 1)
        section, separator, following = remaining.lstrip("\n").partition("\n## ")
        spacing = section[len(section.rstrip("\n")):]
        after = spacing + "\n## " + following if separator else "\n"
        result = before + timing_table(reports, phase_totals) + after
    else:
        result += "\n" + timing_table(reports, phase_totals) + "\n"
    return result


def validate_comparison(reports, seeds):
    if set(reports) != set(SPECS):
        raise ValueError("README comparison requires all 24 challenges")
    first = next(iter(reports.values()))
    for name, report in reports.items():
        runs = report["runs"]
        if len(runs) != 100:
            raise ValueError(f"{name}: README comparison requires 100 runs")
        if [run["seed"] for run in runs] != seeds[name]:
            raise ValueError(f"{name}: seeds differ from the checked-in comparison seeds")
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
        seeds = json.loads((ROOT / "support/seeds.json").read_text())
        try:
            validate_comparison(reports, seeds)
        except ValueError as error:
            parser.error(str(error))
        path = PROJECT / "README.md"
        path.write_text(update_comparison(path.read_text(), reports))


if __name__ == "__main__":
    main()
