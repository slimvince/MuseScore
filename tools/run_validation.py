#!/usr/bin/env python3
"""
run_validation.py — Orchestrates the full harmonic-analysis validation pipeline.

Steps:
  1. music21_batch.py  — exports Bach chorales to MusicXML and .music21.json
  2. batch_analyze     — runs our C++ analysis on each MusicXML file → .ours.json
  3. compare_analyses  — aligns and classifies each pair → per-chorale stats
  4. HTML report       — aggregates all results into one report file

Usage:
    python tools/run_validation.py [OPTIONS]

    --single bach/bwv66.6   Process only this chorale (diagnostic mode)
    --output DIR            Where to write the corpus/ data and reports/
                            (default: tools/)
    --batch-analyze PATH    Path to the batch_analyze executable
                            (default: ninja_build/batch_analyze.exe on Windows,
                                      ninja_build/batch_analyze elsewhere)
    --skip-music21          Skip step 1 (re-use existing .xml and .music21.json files)
    --skip-cpp              Skip step 2 (re-use existing .ours.json files)
    --help

Examples:
    # Full corpus (371 chorales)
    python tools/run_validation.py --output tools/

    # Single chorale spot-check
    python tools/run_validation.py --single bach/bwv66.6

    # Re-run comparison only (corpus already generated)
    python tools/run_validation.py --skip-music21 --skip-cpp
"""

from __future__ import annotations

import argparse
import datetime
import html as html_lib
import json
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

import compare_analyses as cmp
import music21_batch as m21
try:
    import dcml_parser as dcml
    _DCML_AVAILABLE = True
except ImportError:
    _DCML_AVAILABLE = False


# ══════════════════════════════════════════════════════════════════════════
# Helpers
# ══════════════════════════════════════════════════════════════════════════

def _find_batch_analyze(hint: str | None) -> Path | None:
    if hint:
        p = Path(hint)
        if p.exists():
            return p
        print(f"WARNING: --batch-analyze path {hint!r} not found", file=sys.stderr)

    candidates = [
        Path("ninja_build_rel/batch_analyze.exe"),
        Path("ninja_build/batch_analyze.exe"),
        Path("ninja_build_rel/batch_analyze"),
        Path("ninja_build/batch_analyze"),
        Path("../ninja_build_rel/batch_analyze.exe"),
        Path("../ninja_build/batch_analyze.exe"),
        Path("../ninja_build_rel/batch_analyze"),
        Path("../ninja_build/batch_analyze"),
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def _to_unix_path(p: Path) -> str:
    """Convert Windows path to /drive/... form for use as bash executable path."""
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')


def _to_win_path(p: Path) -> str:
    """Convert path to C:/... form for file arguments to native Windows binaries."""
    return str(p.resolve()).replace('\\', '/')


def _find_git_bash() -> Path | None:
    candidates = [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def _run_batch_analyze(exe: Path, xml_path: Path, out_path: Path, preset: str = "Standard") -> bool:
    """Run batch_analyze on xml_path, writing JSON to out_path.  Returns True on success."""
    preset_arg = f'--preset {preset}'
    try:
        # On Windows, launching the Qt binary directly from Python subprocess
        # triggers an access violation (0xC0000005).  Route through Git Bash.
        import platform
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = f'{_to_unix_path(exe)} "{_to_win_path(xml_path)}" "{_to_win_path(out_path)}" {preset_arg}'
                result = subprocess.run(
                    [str(bash), '-c', cmd],
                    stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                    timeout=120,
                )
                if result.returncode != 0:
                    stderr_text = result.stderr.decode('utf-8', errors='replace').strip()
                    print(f"    batch_analyze failed (rc={result.returncode}): "
                          f"{stderr_text[:200]}", file=sys.stderr)
                    return False
                return True

        result = subprocess.run(
            [str(exe), str(xml_path), str(out_path), '--preset', preset],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
            timeout=120,
        )
        if result.returncode != 0:
            stderr_text = result.stderr.decode('utf-8', errors='replace').strip()
            print(f"    batch_analyze failed (rc={result.returncode}): "
                  f"{stderr_text[:200]}", file=sys.stderr)
            return False
        return True
    except subprocess.TimeoutExpired:
        print("    batch_analyze timed out (>120 s)", file=sys.stderr)
        return False
    except Exception as exc:
        print(f"    batch_analyze error: {exc}", file=sys.stderr)
        return False


# ══════════════════════════════════════════════════════════════════════════
# HTML report generation
# ══════════════════════════════════════════════════════════════════════════

_HTML_HEAD = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Harmonic Analysis Validation Report</title>
<style>
  body { font-family: sans-serif; font-size: 13px; margin: 20px; }
  h1   { font-size: 1.4em; }
  h2   { font-size: 1.1em; margin-top: 24px; }
  table.summary { border-collapse: collapse; margin: 12px 0; }
  table.summary td, table.summary th { border: 1px solid #ccc; padding: 4px 8px; }
  table.summary th { background: #f0f0f0; }
  details { margin: 6px 0; }
  details summary { cursor: pointer; padding: 4px 6px; background: #f8f8f8;
                    border: 1px solid #ddd; border-radius: 3px; }
  .category-bar { display: inline-block; height: 12px; vertical-align: middle; }
  .legend { display: flex; gap: 12px; flex-wrap: wrap; margin: 8px 0; }
  .legend span { padding: 2px 8px; border-radius: 3px; font-size: 11px; }
</style>
</head>
<body>
"""

_LEGEND_HTML = """
<div class="legend">
  <span style="background:#2ecc71">full_agree</span>
  <span style="background:#82e0aa">near_agree</span>
  <span style="background:#f7dc6f">chord_agree_rn_differs</span>
  <span style="background:#fad7a0">chord_agree_key_differs</span>
  <span style="background:#e74c3c;color:white">chord_disagree</span>
  <span style="background:#bdc3c7">unaligned</span>
</div>
"""

_HTML_FOOT = "</body></html>\n"


def _build_three_way_html(all_results: list[dict]) -> str:
    """Build the global three-way comparison section for the HTML report."""
    tw_total: dict[str, int] = {c: 0 for c in cmp.THREE_WAY_CATEGORIES}
    mode_counts: dict[str, int] = {}
    error_patterns: dict[str, int] = {}
    chorales_with_dcml = 0

    for r in all_results:
        compared = r["compared"]
        has_dcml = any(cr.three_way_cat != 'no_dcml' for cr in compared)
        if has_dcml:
            chorales_with_dcml += 1
        tw = cmp.three_way_summarize(compared)
        for cat in cmp.THREE_WAY_CATEGORIES:
            tw_total[cat] += tw[cat]
        for mode, cnt in cmp.mode_breakdown_of_errors(compared).items():
            mode_counts[mode] = mode_counts.get(mode, 0) + cnt
        for cr in compared:
            if cr.three_way_cat == 'music21_dcml_agree' and cr.theirs:
                pat = f"{cr.ours.chord_symbol} → {cr.theirs.chord_symbol}"
                error_patterns[pat] = error_patterns.get(pat, 0) + 1

    if chorales_with_dcml == 0:
        return ""

    covered = sum(tw_total[c] for c in cmp.THREE_WAY_CATEGORIES if c != 'no_dcml')
    labels = {
        'all_agree':           'all_agree (all three match)',
        'dcml_ours_agree':     'dcml_ours_agree (music21 wrong)',
        'music21_dcml_agree':  'music21_dcml_agree (we wrong — genuine errors)',
        'all_differ':          'all_differ (genuinely ambiguous)',
        'no_dcml':             'no_dcml_data',
    }
    colours = {
        'all_agree':           '#2ecc71',
        'dcml_ours_agree':     '#f7dc6f',
        'music21_dcml_agree':  '#e74c3c',
        'all_differ':          '#e8a0e8',
        'no_dcml':             '#eeeeee',
    }
    tw_rows = "".join(
        f"<tr style='background:{colours[c]}'>"
        f"<td>{labels[c]}</td>"
        f"<td>{tw_total[c]}</td>"
        f"<td>{tw_total[c]/max(covered,1):.1%}</td>"
        f"</tr>"
        for c in cmp.THREE_WAY_CATEGORIES
    )

    mode_rows = "".join(
        f"<tr style='background:{'#ffdddd' if m not in ('maj','min') else '#ffffff'}'>"
        f"<td>{m}</td><td>{cnt}</td>"
        f"<td>{'diatonic' if m in ('maj','min') else '⚠ non-diatonic'}</td>"
        f"</tr>"
        for m, cnt in sorted(mode_counts.items(), key=lambda x: -x[1])[:20]
    )

    top_errors = "".join(
        f"<tr><td>{p}</td><td>{n}</td></tr>"
        for p, n in sorted(error_patterns.items(), key=lambda x: -x[1])[:15]
    )

    return (
        f"<h2>Three-Way Comparison (ours vs music21 vs DCML)</h2>\n"
        f"<p><strong>{chorales_with_dcml}</strong> of {len(all_results)} chorales "
        f"had matching DCML annotation files. "
        f"<strong>{covered}</strong> regions with DCML data.</p>\n"
        f"<table class='summary'><thead><tr>"
        f"<th>Category</th><th>Count</th><th>% of DCML-covered</th>"
        f"</tr></thead><tbody>{tw_rows}</tbody></table>\n"
        f"<h3>Mode breakdown of genuine errors (music21_dcml_agree)</h3>\n"
        f"<p>Non-diatonic modes appearing here may indicate mode inference errors "
        f"introduced by the 21-mode expansion.</p>\n"
        f"<table class='summary'><thead><tr>"
        f"<th>Our inferred mode</th><th>Error count</th><th>Note</th>"
        f"</tr></thead><tbody>{mode_rows}</tbody></table>\n"
        f"<h3>Top error patterns (ours → DCML/music21)</h3>\n"
        f"<table class='summary'><thead><tr>"
        f"<th>Pattern</th><th>Count</th>"
        f"</tr></thead><tbody>{top_errors}</tbody></table>\n"
    )


def _build_html_report(
    timestamp: str,
    all_results: list[dict],    # list of {source, ours_meta, m21_meta, compared, counts}
) -> str:
    total_regions   = sum(r["total"]    for r in all_results)
    total_full      = sum(r["counts"]["full_agree"]             for r in all_results)
    total_near      = sum(r["counts"]["near_agree"]             for r in all_results)
    total_disagree  = sum(r["counts"]["chord_disagree"]         for r in all_results)
    total_rn_diff   = sum(r["counts"]["chord_agree_rn_differs"] for r in all_results)
    total_key_diff  = sum(r["counts"]["chord_agree_key_differs"]for r in all_results)
    total_unaligned = sum(r["counts"]["unaligned"]              for r in all_results)
    total_aligned   = total_regions - total_unaligned
    global_rate     = (total_full + total_near) / max(total_regions, 1)
    chord_id_count  = total_full + total_rn_diff + total_key_diff
    chord_id_rate   = chord_id_count / max(total_aligned, 1)

    # Most common disagree patterns
    disagree_patterns: dict[str, int] = {}
    for r in all_results:
        for cr in r["compared"]:
            if cr.category == "chord_disagree" and cr.theirs:
                key = f"{cr.ours.chord_symbol} vs {cr.theirs.chord_symbol}"
                disagree_patterns[key] = disagree_patterns.get(key, 0) + 1
    top_disagree = sorted(disagree_patterns.items(), key=lambda x: -x[1])[:20]

    # Per-chorale table
    chorale_rows = []
    for r in sorted(all_results, key=lambda x: x["agreement"]):
        src = html_lib.escape(r["source"])
        ag  = r["agreement"]
        c   = r["counts"]
        tot = r["total"]
        chorale_rows.append(
            f"<tr>"
            f"<td><a href='#{html_lib.escape(r['source'])}'>{src}</a></td>"
            f"<td>{ag:.1%}</td>"
            f"<td>{c['full_agree']}</td>"
            f"<td>{c['near_agree']}</td>"
            f"<td>{c['chord_agree_rn_differs']}</td>"
            f"<td>{c['chord_agree_key_differs']}</td>"
            f"<td>{c['chord_disagree']}</td>"
            f"<td>{c['unaligned']}</td>"
            f"<td>{tot}</td>"
            f"</tr>"
        )

    disagree_rows = "".join(
        f"<tr><td>{html_lib.escape(p)}</td><td>{n}</td></tr>"
        for p, n in top_disagree
    )

    fragments = "".join(r["html_fragment"] for r in all_results)

    return (
        _HTML_HEAD
        + f"<h1>Harmonic Analysis Validation — {timestamp}</h1>\n"
        + _LEGEND_HTML
        + f"<h2>Summary</h2>\n"
        + f"<p><strong>{len(all_results)}</strong> chorales &nbsp;|&nbsp; "
        + f"<strong>{total_regions}</strong> regions &nbsp;|&nbsp; "
        + f"agreement: <strong>{global_rate:.1%}</strong> "
        + f"({total_full} full + {total_near} near out of {total_regions})"
        + f" &nbsp;|&nbsp; "
        + f"<strong>Chord identity agreement (root+quality, key-independent):"
        + f" {chord_id_rate:.1%}</strong>"
        + f" ({chord_id_count}/{total_aligned} aligned regions)</p>\n"
        + "<table class='summary'>\n"
        + "<thead><tr><th>Chorale</th><th>Agreement</th>"
        + "<th>Full</th><th>Near</th><th>RN↗</th><th>Key↗</th>"
        + "<th>Disagree</th><th>Unaligned</th><th>Total</th></tr></thead>\n"
        + "<tbody>\n" + "\n".join(chorale_rows) + "\n</tbody></table>\n"
        + "<h2>Most Common Disagreements</h2>\n"
        + "<table class='summary'><thead><tr><th>Pattern</th><th>Count</th></tr></thead>\n"
        + "<tbody>" + disagree_rows + "</tbody></table>\n"
        + _build_three_way_html(all_results)
        + "<h2>Per-Chorale Detail</h2>\n"
        + fragments
        + _HTML_FOOT
    )


# ══════════════════════════════════════════════════════════════════════════
# Single-chorale mode
# ══════════════════════════════════════════════════════════════════════════

def run_single(name: str, output_root: Path, exe: Path | None,
               skip_music21: bool, skip_cpp: bool,
               preset: str = "Standard") -> None:
    corpus_dir = output_root / "corpus"
    corpus_dir.mkdir(parents=True, exist_ok=True)

    stem = m21.stem_from_corpus_path(name)
    xml_path  = corpus_dir / f"{stem}.xml"
    m21_path  = corpus_dir / f"{stem}.music21.json"
    ours_path = corpus_dir / f"{stem}.ours.json"

    # Step 1 — music21
    if not skip_music21:
        print(f"[1/3] music21_batch --single {name}")
        m21.run_single(name)                        # prints diagnostic
        result = m21.process_chorale(name, corpus_dir)
        if result is None:
            print("ERROR: music21 processing failed", file=sys.stderr)
            sys.exit(1)
    else:
        print("[1/3] music21 skipped")

    # Step 2 — batch_analyze
    if not skip_cpp:
        if exe is None:
            print("ERROR: batch_analyze not found; build it first with setup_and_build_fast.bat",
                  file=sys.stderr)
            sys.exit(1)
        print(f"[2/3] batch_analyze {xml_path}")
        ok = _run_batch_analyze(exe, xml_path, ours_path, preset=preset)
        if not ok:
            print("ERROR: batch_analyze failed", file=sys.stderr)
            sys.exit(1)
    else:
        print("[2/3] C++ analysis skipped")

    # Step 3 — compare
    print("[3/3] Comparing …")
    ours_meta, m21_meta, compared = cmp.compare_files(ours_path, m21_path)
    cmp.print_report(ours_meta, m21_meta, compared)


# ══════════════════════════════════════════════════════════════════════════
# Full corpus mode
# ══════════════════════════════════════════════════════════════════════════

def run_full(output_root: Path, exe: Path | None,
             skip_music21: bool, skip_cpp: bool,
             dcml_dir: Path | None = None,
             preset: str = "Standard") -> None:

    corpus_dir  = output_root / "corpus"
    reports_dir = output_root / "reports"
    corpus_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    # ── Step 1: music21 ───────────────────────────────────────────────────
    if not skip_music21:
        print("Step 1/3 — Exporting chorales via music21 …")
        m21.run_batch(corpus_dir)
    else:
        print("Step 1/3 — music21 skipped")

    # ── Collect XML files ─────────────────────────────────────────────────
    # Exclude _m21.xml files (inject_m21_rn.py output that may land here).
    xml_files = sorted(f for f in corpus_dir.glob("*.xml")
                       if not f.stem.endswith("_m21"))
    total = len(xml_files)
    if total == 0:
        print("ERROR: no .xml files found in corpus directory", file=sys.stderr)
        sys.exit(1)

    print(f"\nStep 2/3 — C++ analysis of {total} chorales …")

    # ── Step 2: batch_analyze ─────────────────────────────────────────────
    cpp_ok = 0
    for idx, xml_path in enumerate(xml_files, 1):
        ours_path = xml_path.with_suffix(".ours.json")
        stem      = xml_path.stem

        if skip_cpp and ours_path.exists():
            cpp_ok += 1
            continue

        if exe is None:
            print(f"  [{idx}/{total}] SKIP (no batch_analyze executable)")
            continue

        ok = _run_batch_analyze(exe, xml_path, ours_path, preset=preset)
        status = "ok" if ok else "FAILED"
        print(f"  [{idx:>3}/{total}] {stem:<30}  {status}")
        if ok:
            cpp_ok += 1

    print(f"  {cpp_ok}/{total} C++ analyses succeeded")

    # ── Step 3: compare all pairs ─────────────────────────────────────────
    print(f"\nStep 3/3 — Comparing {total} chorale pairs …")

    timestamp   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    all_results = []
    agree_sum   = 0.0
    compared_n  = 0

    for idx, xml_path in enumerate(xml_files, 1):
        stem      = xml_path.stem
        ours_path = xml_path.with_suffix(".ours.json")
        m21_path  = xml_path.with_suffix(".music21.json")

        if not ours_path.exists() or not m21_path.exists():
            print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (missing files)")
            continue

        # Load When-in-Rome annotations if available
        dcml_regions = None
        if dcml_dir is not None and _DCML_AVAILABLE:
            wir_path = dcml.find_wir_file(str(dcml_dir), stem)
            if wir_path:
                try:
                    dcml_regions = dcml.parse_rntxt_file(wir_path)
                except Exception:
                    dcml_regions = None

        try:
            ours_meta, m21_meta, compared = cmp.compare_files(
                ours_path, m21_path, dcml_regions=dcml_regions)
        except Exception as exc:
            print(f"  [{idx:>3}/{total}] {stem:<30}  ERROR: {exc}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            continue

        counts   = cmp.summarize(compared)
        rate     = cmp.agreement_rate(counts)
        total_r  = sum(counts.values())
        m21_n    = len(m21_meta.get("regions", []))

        print(
            f"  [{idx:>3}/{total}] {stem:<30}"
            f"  music21: {m21_n:>3} regions,"
            f"  ours: {total_r:>3} regions,"
            f"  agreement: {rate:.0%}"
        )

        fragment = cmp.render_html_fragment(ours_meta, m21_meta, compared)
        all_results.append({
            "source":        ours_meta.get("source", stem),
            "ours_meta":     ours_meta,
            "m21_meta":      m21_meta,
            "compared":      compared,
            "counts":        counts,
            "total":         total_r,
            "agreement":     rate,
            "html_fragment": fragment,
        })

        agree_sum  += rate
        compared_n += 1

    if compared_n == 0:
        print("No pairs could be compared.", file=sys.stderr)
        return

    avg_rate    = agree_sum / compared_n
    report_path = reports_dir / f"validation_{timestamp}.html"
    html        = _build_html_report(timestamp, all_results)
    report_path.write_text(html, encoding="utf-8")

    print(f"\nComplete. {compared_n} chorales compared, average agreement: {avg_rate:.1%}")
    print(f"Report written to {report_path}")


# ══════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Orchestrate the full harmonic-analysis validation pipeline.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--single",        metavar="NAME",
                        help="Process a single chorale in diagnostic mode")
    parser.add_argument("--output",        default="tools",
                        help="Root directory; corpus/ and reports/ are created beneath it "
                             "(default: tools — resolves to tools/tools/ when run from tools/)")
    parser.add_argument("--batch-analyze", metavar="PATH",
                        help="Path to the batch_analyze executable")
    parser.add_argument("--skip-music21",  action="store_true",
                        help="Skip music21 export (re-use existing .xml and .music21.json)")
    parser.add_argument("--skip-cpp",      action="store_true",
                        help="Skip C++ analysis (re-use existing .ours.json)")
    parser.add_argument("--dcml",          metavar="DIR", default=None,
                        help="Path to DCML annotations directory for three-way comparison "
                             "(e.g. tools/dcml/bach_chorales/harmonies/)")
    parser.add_argument("--preset",        metavar="NAME", default="Standard",
                        help="Preset to pass to batch_analyze (default: Standard)")
    args = parser.parse_args()

    output_root = Path(args.output)
    exe         = _find_batch_analyze(args.batch_analyze)
    dcml_dir    = Path(args.dcml) if args.dcml else None

    if dcml_dir and not _DCML_AVAILABLE:
        print("WARNING: --dcml supplied but dcml_parser.py not found on path", file=sys.stderr)
    if dcml_dir and dcml_dir.exists():
        print(f"DCML annotations directory: {dcml_dir}")

    if not args.skip_cpp and exe is None:
        print("WARNING: batch_analyze executable not found.  "
              "Build it first:\n"
              "  cmd.exe //c C:\\s\\MS\\setup_and_build_fast.bat\n"
              "Or pass --skip-cpp to skip the C++ step.", file=sys.stderr)

    if args.single:
        run_single(args.single, output_root, exe, args.skip_music21, args.skip_cpp,
                   preset=args.preset)
    else:
        run_full(output_root, exe, args.skip_music21, args.skip_cpp, dcml_dir=dcml_dir,
                 preset=args.preset)


if __name__ == "__main__":
    main()
