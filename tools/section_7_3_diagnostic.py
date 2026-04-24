#!/usr/bin/env python3
"""
section_7_3_diagnostic.py — Consolidated cross-corpus diagnostic report.

Analyses bassIsRoot errors across four corpora:
  - Bach chorales       (tools/reports/corpus/ + music21 + WiR)
  - Beethoven quartets  (tools/reports/beethoven/ + DCML ABC TSV)
    - Mozart sonatas      (latest tools/reports/mozart_YYYYMMDD_HHMMSS/ + DCML TSV)
  - Corelli sonatas     (tools/reports/corelli_20260405_221113/ + DCML TSV)

For each corpus reports:
  - Agreement / disagreement / bassIsRoot fraction
  - noteCount distribution of bassIsRoot errors
  - Beat position distribution of bassIsRoot errors
  - chordScoreMargin distribution of bassIsRoot errors (where available)

Usage:
    python tools/section_7_3_diagnostic.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


def _latest_timestamped_run(prefix: str) -> tuple[str, Path]:
    pattern = re.compile(rf"^{re.escape(prefix)}_(\d{{8}}_\d{{6}})$")
    runs_root = _ROOT / 'tools' / 'reports'
    candidates: list[tuple[str, Path]] = []

    for entry in runs_root.iterdir():
        if not entry.is_dir():
            continue
        match = pattern.match(entry.name)
        if match:
            candidates.append((match.group(1), entry))

    if not candidates:
        raise FileNotFoundError(f"No timestamped runs found for prefix '{prefix}'")

    return max(candidates, key=lambda item: item[0])


_MOZART_RUN_TS, _MOZART_DIR = _latest_timestamped_run('mozart')
_MOZART_REPORT = _ROOT / 'tools' / 'reports' / 'reports' / f'mozart_{_MOZART_RUN_TS}.json'


# ── Corpus configurations ─────────────────────────────────────────────────────

CORPORA = [
    {
        'name': 'Bach chorales',
        'ours_dir': _ROOT / 'tools/reports/corpus',
        'ours_glob': '*.ours.json',
        'ref_type': 'music21',
        'ref_dir': _ROOT / 'tools/reports/corpus',
        'ref_glob': '*.music21.json',
        'report': 'tools/reports/reports/validation_20260405_214122.html',
        'run_ts': '20260405_214122',
        # Known aggregate from HTML report (parsed separately)
        'known_aggregate': {
            'aligned': 4058, 'agree': 3385, 'disagree': 673,
            'bass_is_root_in_disagree': 500,
        },
    },
    {
        'name': 'Beethoven quartets',
        'ours_dir': _ROOT / 'tools/reports/beethoven',
        'ours_glob': '*.ours.json',
        'ref_type': 'dcml_tsv',
        'ref_dir': _ROOT / 'tools/dcml/ABC/harmonies',
        'ref_glob': '*.harmonies.tsv',
        'report': 'tools/reports/reports/beethoven_20260405_194709.json',
        'run_ts': '20260405_194709',
    },
    {
        'name': 'Mozart sonatas',
        'ours_dir': _MOZART_DIR,
        'ours_glob': '*.ours.json',
        'ref_type': 'dcml_tsv',
        'ref_dir': _ROOT / 'tools/dcml/mozart_piano_sonatas/harmonies',
        'ref_glob': '*.harmonies.tsv',
        'report': _MOZART_REPORT.relative_to(_ROOT).as_posix(),
        'run_ts': _MOZART_RUN_TS,
    },
    {
        'name': 'Corelli sonatas',
        'ours_dir': _ROOT / 'tools/reports/corelli_20260405_221113',
        'ours_glob': '*.ours.json',
        'ref_type': 'dcml_tsv',
        'ref_dir': _ROOT / 'tools/dcml/corelli/harmonies',
        'ref_glob': '*.harmonies.tsv',
        'report': 'tools/reports/reports/corelli_20260405_221113.json',
        'run_ts': '20260405_221113',
    },
]


def collect_bir_errors(corpus: dict) -> list[dict]:
    """Return a list of region dicts for every bassIsRoot=true disagreement."""
    errors = []
    ours_dir = corpus['ours_dir']
    ref_type  = corpus['ref_type']

    for ours_path in sorted(ours_dir.glob(corpus['ours_glob'])):
        stem = ours_path.stem.replace('.ours', '')

        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except Exception:
            continue

        if ref_type == 'music21':
            ref_path = corpus['ref_dir'] / f"{stem}.music21.json"
            if not ref_path.exists():
                continue
            try:
                _, ref_regions = cmp.load_analysis(ref_path)
            except Exception:
                continue
            aligned = cmp.align_regions(ours_regions, ref_regions)
            for our_r, their_r in aligned:
                result = cmp.classify(our_r, their_r)
                if result.category == 'chord_disagree' and our_r.bass_is_root:
                    errors.append({
                        'note_count': our_r.note_count or 0,
                        'beat': our_r.beat or 1.0,
                        'margin': our_r.chord_score_margin or 0.0,
                        'chord_symbol': our_r.chord_symbol or '',
                    })

        elif ref_type == 'dcml_tsv':
            tsv_path = corpus['ref_dir'] / f"{stem}.harmonies.tsv"
            if not tsv_path.exists():
                continue
            try:
                dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
            except Exception:
                continue
            direct = cmp.compare_ours_vs_dcml_direct(ours_regions, dcml_regions)
            for entry in direct:
                if entry.category == 'dcml_disagree' and entry.ours.bass_is_root:
                    errors.append({
                        'note_count': entry.ours.note_count or 0,
                        'beat': entry.ours.beat or 1.0,
                        'margin': entry.ours.chord_score_margin or 0.0,
                        'chord_symbol': entry.ours.chord_symbol or '',
                    })

    return errors


def print_distribution(label: str, errors: list[dict], total_disagree: int) -> None:
    n = len(errors)
    if n == 0:
        print(f"  {label}: no bassIsRoot errors")
        return

    print(f"\n  -- {label} (n={n}, {100*n/max(1,total_disagree):.1f}% of disagree) --")

    # noteCount
    nc_counts: Counter = Counter(e['note_count'] for e in errors)
    print(f"  noteCount distribution:")
    for nc in sorted(nc_counts):
        print(f"    noteCount={nc}: {nc_counts[nc]:4d}  ({100*nc_counts[nc]/n:.1f}%)")

    # Beat position
    beats = [e['beat'] for e in errors]
    b1 = sum(1 for b in beats if abs(b - 1.0) < 0.26)
    b2 = sum(1 for b in beats if abs(b - 2.0) < 0.26)
    b3 = sum(1 for b in beats if abs(b - 3.0) < 0.26)
    b4 = sum(1 for b in beats if abs(b - 4.0) < 0.26)
    other = n - b1 - b2 - b3 - b4
    print(f"  Beat position:")
    print(f"    Beat 1: {b1:4d} ({100*b1/n:.1f}%)  Beat 2: {b2:4d} ({100*b2/n:.1f}%)  "
          f"Beat 3: {b3:4d} ({100*b3/n:.1f}%)  Beat 4: {b4:4d} ({100*b4/n:.1f}%)  "
          f"Other: {other:4d} ({100*other/n:.1f}%)")

    # Margin distribution (where available)
    margins = [e['margin'] for e in errors if e['margin'] is not None]
    if margins:
        lt_025 = sum(1 for m in margins if m < 0.25)
        lt_065 = sum(1 for m in margins if m < 0.65)
        lt_1   = sum(1 for m in margins if m < 1.0)
        ge_1   = sum(1 for m in margins if m >= 1.0)
        print(f"  chordScoreMargin:")
        print(f"    < 0.25: {lt_025:4d} ({100*lt_025/n:.1f}%)  "
              f"< 0.65: {lt_065:4d} ({100*lt_065/n:.1f}%)  "
              f"< 1.0: {lt_1:4d} ({100*lt_1/n:.1f}%)  "
              f">= 1.0: {ge_1:4d} ({100*ge_1/n:.1f}%)")


def main() -> None:
    print("=" * 72)
    print("SECTION 7.3 — CROSS-CORPUS DIAGNOSTIC REPORT")
    print("Git hash: 80fc2d2ca1 (inversion fix reverted)")
    print("=" * 72)

    summary_rows = []

    for corpus in CORPORA:
        name = corpus['name']
        print(f"\n{'─'*72}")
        print(f"CORPUS: {name}  (run {corpus['run_ts']})")
        print(f"{'─'*72}")

        # Load aggregate — from hardcoded known values, then JSON report
        ka = corpus.get('known_aggregate', {})
        agg_aligned  = ka.get('aligned', 0)
        agg_agree    = ka.get('agree', 0)
        agg_disagree = ka.get('disagree', 0)
        agg_bir      = ka.get('bass_is_root_in_disagree', 0)

        if not agg_aligned:
            report_path = _ROOT / corpus['report']
            if report_path.suffix == '.json' and report_path.exists():
                try:
                    rpt = json.loads(report_path.read_text(encoding='utf-8'))
                    a = rpt.get('aggregate', {})
                    agg_aligned   = a.get('aligned', 0)
                    agg_agree     = a.get('agree', 0)
                    agg_disagree  = a.get('disagree', 0)
                    agg_bir       = a.get('bass_is_root_in_disagree', 0)
                except Exception:
                    pass

        if agg_aligned:
            bir_pct = 100 * agg_bir / agg_disagree if agg_disagree else 0
            print(f"  Aligned: {agg_aligned}  Agree: {agg_agree} ({100*agg_agree/agg_aligned:.1f}%)  "
                  f"Disagree: {agg_disagree}  bassIsRoot errors: {agg_bir} ({bir_pct:.1f}%)")

        # Collect per-region data for distribution analysis
        errors = collect_bir_errors(corpus)
        print_distribution("bassIsRoot=true errors", errors, agg_disagree or len(errors))

        summary_rows.append({
            'corpus': name,
            'aligned': agg_aligned,
            'agree_pct': round(100*agg_agree/agg_aligned, 1) if agg_aligned else 0,
            'disagree': agg_disagree,
            'bir': agg_bir,
            'bir_pct': round(100*agg_bir/agg_disagree, 1) if agg_disagree else 0,
            'nc1': sum(1 for e in errors if e['note_count'] == 1),
            'nc2': sum(1 for e in errors if e['note_count'] == 2),
            'nc3p': sum(1 for e in errors if e['note_count'] >= 3),
            'margin_lt_025': sum(1 for e in errors if e['margin'] < 0.25),
            'margin_lt_065': sum(1 for e in errors if e['margin'] < 0.65),
        })

    # ── Cross-corpus summary table ────────────────────────────────────────
    print(f"\n{'='*72}")
    print("CROSS-CORPUS SUMMARY")
    print(f"{'='*72}")
    print(f"{'Corpus':<22} {'Agree%':>7} {'Disagree':>9} {'BIR':>6} {'BIR%':>6} "
          f"{'nc=1':>5} {'nc=2':>5} {'nc>=3':>6} {'m<.25':>6} {'m<.65':>6}")
    print(f"{'─'*22} {'─'*7} {'─'*9} {'─'*6} {'─'*6} "
          f"{'─'*5} {'─'*5} {'─'*6} {'─'*6} {'─'*6}")
    for r in summary_rows:
        print(f"{r['corpus']:<22} {r['agree_pct']:>6.1f}% {r['disagree']:>9} "
              f"{r['bir']:>6} {r['bir_pct']:>5.1f}% "
              f"{r['nc1']:>5} {r['nc2']:>5} {r['nc3p']:>6} "
              f"{r['margin_lt_025']:>6} {r['margin_lt_065']:>6}")

    print(f"\nKey: BIR = bassIsRoot errors, m<.25/.65 = chordScoreMargin threshold counts")


if __name__ == "__main__":
    main()
