#!/usr/bin/env python3
"""
compare_inversion_regressions.py — Diagnose BIR=false genuine errors.

Reads corpus_baroque .ours.json files, identifies genuine BIR=false errors
(we said "inverted", both music21 and WiR DCML say we're wrong), and
classifies them by error pattern.

With --baseline-dir: compares against a pre-temporal corpus to find the
specific regions that moved from correct to BIR=false.

Usage:
    python tools/compare_inversion_regressions.py [--ours-dir DIR] [--baseline-dir DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"           # music21.json lives here
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


_PC_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def _pc_name(pc: int | None) -> str:
    if pc is None or pc < 0:
        return "?"
    return _PC_NAMES[pc % 12]


def _classify_error(our_root_pc: int, our_bass_pc: int | None, dcml_root_pc: int | None) -> str:
    """Classify a BIR=false genuine error by pattern type."""
    if dcml_root_pc is None:
        return "NoDCML"
    if our_bass_pc is not None and dcml_root_pc == our_bass_pc % 12:
        return "BassIsActualRoot"   # We called the true root the bass note (enharmonic confusion)
    if dcml_root_pc == our_root_pc % 12:
        return "OurRootCorrectWrongInversion"  # Root right, but we said inverted when root-pos
    return "WrongRoot"              # Neither our root nor our bass matches DCML root


def _top_alt_symbol(alternatives: list[dict], bass_pc: int | None) -> str:
    """Return the top alternative chord symbol that is root-position (bassIsRoot implied)."""
    for alt in alternatives:
        sym = alt.get("chordSymbol", "")
        if "/" not in sym:           # no slash = root position
            return sym
    # Fallback: any first alternative
    return alternatives[0].get("chordSymbol", "") if alternatives else ""


def _load_genuine_nonbir_errors(ours_dir: Path) -> list[dict]:
    """Return all genuine BIR=false errors from ours_dir vs music21 + WiR."""
    ours_files = sorted(ours_dir.glob("*.ours.json"))
    errors = []

    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        music21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not music21_path.exists():
            continue

        try:
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions  = cmp.load_analysis(music21_path)
        except Exception:
            continue

        if not ours_regions:
            continue

        aligned = cmp.align_regions(ours_regions, m21_regions)

        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        wir_regions = []
        if wir_path:
            try:
                wir_regions = dcml.parse_rntxt_file(wir_path)
            except Exception:
                pass

        wir_aligned = (cmp.align_dcml_regions(ours_regions, wir_regions)
                       if wir_regions else [None] * len(ours_regions))

        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != "chord_disagree":
                continue
            if our_r.bass_is_root is not False:
                continue  # only want BIR=false

            wir_r = wir_aligned[i] if i < len(wir_aligned) else None
            wir_pc = wir_r.root_pc if wir_r is not None else None
            wir_sym = wir_r.chord_symbol if wir_r is not None else None

            category = cmp.three_way_classify(
                our_r.root_pc,
                their_r.root_pc if their_r else None,
                wir_pc)
            if category != "music21_dcml_agree":
                continue  # not a genuine error confirmed by both references

            errors.append({
                "stem":         stem,
                "measure":      our_r.measure_number,
                "beat":         our_r.beat,
                "our_symbol":   our_r.chord_symbol,
                "our_root_pc":  our_r.root_pc,
                "our_bass_pc":  our_r.bass_pc,
                "our_quality":  our_r.quality,
                "our_margin":   our_r.chord_score_margin,
                "note_count":   our_r.note_count,
                "alternatives": our_r.alternatives or [],
                "m21_root_pc":  their_r.root_pc if their_r else None,
                "m21_symbol":   their_r.chord_symbol if their_r else None,
                "dcml_root_pc": wir_pc,
                "dcml_symbol":  wir_sym,
                "error_type":   _classify_error(our_r.root_pc, our_r.bass_pc, wir_pc),
            })

    return errors


def _region_key(e: dict) -> str:
    """Stable identity key for a region across two corpus runs."""
    return f"{e['stem']}|m{e['measure']}|b{e['beat']:.2f}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, add_help=True)
    parser.add_argument("--ours-dir", default=str(_ROOT / "tools" / "corpus_baroque"),
                        help="Directory with committed Baroque .ours.json files")
    parser.add_argument("--baseline-dir", default=None,
                        help="Directory with pre-temporal .ours.json files for delta comparison")
    parser.add_argument("--sample", type=int, default=20,
                        help="Max cases to show in the sample listing")
    args = parser.parse_args()

    ours_dir = Path(args.ours_dir).resolve()
    print(f"Loading current corpus: {ours_dir}")
    current_errors = _load_genuine_nonbir_errors(ours_dir)
    current_keys   = {_region_key(e) for e in current_errors}

    baseline_errors: list[dict] = []
    new_errors:      list[dict] = []
    recovered:       list[dict] = []

    if args.baseline_dir:
        baseline_dir = Path(args.baseline_dir).resolve()
        print(f"Loading baseline corpus: {baseline_dir}")
        baseline_errors = _load_genuine_nonbir_errors(baseline_dir)
        baseline_keys   = {_region_key(e) for e in baseline_errors}
        new_errors      = [e for e in current_errors if _region_key(e) not in baseline_keys]
        recovered       = [e for e in baseline_errors if _region_key(e) not in current_keys]
    else:
        print("(No --baseline-dir; analysing all current BIR=false errors)")
        new_errors = current_errors

    analyze_set = new_errors if args.baseline_dir else current_errors

    # ── Summary ─────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    if args.baseline_dir:
        print(f"BIR=false genuine errors — baseline: {len(baseline_errors)}, "
              f"current: {len(current_errors)}")
        print(f"  New regressions (current − baseline): {len(new_errors)}")
        print(f"  Recovered   (baseline − current):     {len(recovered)}")
    else:
        print(f"BIR=false genuine errors (current corpus): {len(current_errors)}")
    print(f"{'='*72}")

    if not analyze_set:
        print("No errors to analyze.")
        return

    n = len(analyze_set)

    # ── Error type breakdown ────────────────────────────────────────────────
    type_counts: Counter = Counter(e["error_type"] for e in analyze_set)
    print(f"\nError type breakdown (n={n}):")
    for etype, cnt in type_counts.most_common():
        pct = 100 * cnt / n
        desc = {
            "BassIsActualRoot":            "DCML root == our bass  (enharmonic confusion)",
            "OurRootCorrectWrongInversion":"Our root correct, but we said inverted",
            "WrongRoot":                   "DCML root matches neither our root nor our bass",
            "NoDCML":                      "No WiR DCML data available",
        }.get(etype, etype)
        print(f"  {etype:<35} {cnt:4d}  ({pct:.1f}%)  — {desc}")

    # ── Piece concentration ─────────────────────────────────────────────────
    piece_counts: Counter = Counter(e["stem"] for e in analyze_set)
    print(f"\nPiece concentration (top 15 scores by error count):")
    for stem, cnt in piece_counts.most_common(15):
        print(f"  {stem:<25} {cnt:3d} error(s)")

    # ── Common our-symbol patterns ───────────────────────────────────────────
    sym_counts: Counter = Counter(e["our_symbol"] for e in analyze_set)
    print(f"\nMost frequent erroneous inversions we output (top 20):")
    for sym, cnt in sym_counts.most_common(20):
        print(f"  {sym:<20} {cnt:3d}")

    # ── BassIsActualRoot: what are the bass pitch classes? ───────────────────
    bar_errors = [e for e in analyze_set if e["error_type"] == "BassIsActualRoot"]
    if bar_errors:
        bass_pc_counter: Counter = Counter(_pc_name(e["our_bass_pc"]) for e in bar_errors)
        print(f"\nBassIsActualRoot — bass pitch classes (we confused these as inversions):")
        for name, cnt in bass_pc_counter.most_common(12):
            pct = 100 * cnt / len(bar_errors)
            print(f"  {name:<6} {cnt:3d}  ({pct:.1f}%)")

    # ── Sample listing ──────────────────────────────────────────────────────
    sample = analyze_set[:args.sample]
    print(f"\n{'='*72}")
    header = "SAMPLE LISTING — NEW REGRESSIONS" if args.baseline_dir else \
             "SAMPLE LISTING — BIR=false genuine errors"
    print(f"{header} (up to {args.sample} cases)")
    print(f"{'='*72}")
    print(f"{'Score':<18} {'M':>4} {'Bt':>5}  {'Our chord':<22} "
          f"{'Best alt':<18} {'DCML sym':<14} {'Type'}")
    print("-" * 100)

    for e in sample:
        best_alt = _top_alt_symbol(e["alternatives"], e["our_bass_pc"])
        dcml_str = e["dcml_symbol"] or f"root={_pc_name(e['dcml_root_pc'])}"
        print(f"{e['stem']:<18} {e['measure']:>4} {e['beat']:>5.1f}  "
              f"{e['our_symbol']:<22} {best_alt:<18} {dcml_str:<14} "
              f"{e['error_type']}")

    # ── Whether the correct answer is in our alternatives list ───────────────
    correct_in_alts = 0
    for e in analyze_set:
        dcml_pc = e["dcml_root_pc"]
        if dcml_pc is None:
            continue
        for alt in e["alternatives"]:
            sym = alt.get("chordSymbol", "")
            # Infer root pc from the alt symbol's root name
            m = __import__("re").match(r'^([A-G][#b]?)', sym)
            if m:
                note = m.group(1)
                alt_pc = _PC_NAMES.index(note) if note in _PC_NAMES else None
                if alt_pc is not None and alt_pc == dcml_pc:
                    correct_in_alts += 1
                    break

    print(f"\n{'='*72}")
    print(f"ADDITIONAL STATS")
    print(f"{'='*72}")
    pct_in_alts = 100 * correct_in_alts / n if n else 0
    print(f"  Correct answer present in our alternatives list: "
          f"{correct_in_alts}/{n} ({pct_in_alts:.1f}%)")

    # ── Score margin distribution ────────────────────────────────────────────
    margins = [e["our_margin"] or 0.0 for e in analyze_set]
    lt_05 = sum(1 for m in margins if m < 0.5)
    lt_1  = sum(1 for m in margins if m < 1.0)
    gt_1  = sum(1 for m in margins if m >= 1.0)
    print(f"\n  chordScoreMargin of the (incorrect) winner:")
    print(f"    < 0.5  (narrow win — flip-prone):  {lt_05:4d}  ({100*lt_05/n:.1f}%)")
    print(f"    < 1.0:                             {lt_1:4d}  ({100*lt_1/n:.1f}%)")
    print(f"    >= 1.0 (convinced wrong answer):   {gt_1:4d}  ({100*gt_1/n:.1f}%)")

    print(f"\nDone. Analyzed {n} BIR=false genuine error(s).")


if __name__ == "__main__":
    main()
