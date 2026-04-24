#!/usr/bin/env python3
"""
analyze_inversion_errors.py — Section 6.1 analysis of bassIsRoot genuine errors.

Identifies music21_dcml_agree regions (confirmed genuine errors where both
music21 and WiR DCML agree against us) and analyzes:
  - chordScoreMargin distribution
  - best non-bass alternative quality
  - noteCount distribution
  - beat position distribution

Usage:
    python tools/analyze_inversion_errors.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "reports" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


def main():
    # ── Find enriched JSON files ──────────────────────────────────────────
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))
    if not ours_files:
        print("ERROR: No .ours.json files in tools/reports/corpus/", file=sys.stderr)
        sys.exit(1)

    # Verify enriched fields present
    sample_data, sample_regions = cmp.load_analysis(ours_files[0])
    if sample_regions and sample_regions[0].bass_is_root is None:
        print("ERROR: .ours.json files lack enriched fields. Re-run validation pipeline.",
              file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(ours_files)} enriched .ours.json files")

    # ── Accumulate all chord_disagree regions (two-way) and WiR three-way ─
    all_bir_errors_2way   = []   # chord_disagree bassIsRoot=true (two-way vs music21)
    all_nonbir_errors_2way= []
    genuine_bir_errors    = []   # music21_dcml_agree bassIsRoot=true (three-way confirmed)
    genuine_nonbir_errors = []

    processed = skipped_no_m21 = skipped_no_regions = 0
    wir_coverage = 0

    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        music21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not music21_path.exists():
            skipped_no_m21 += 1
            continue

        try:
            _, ours_regions  = cmp.load_analysis(ours_path)
            _, m21_regions   = cmp.load_analysis(music21_path)
        except Exception as exc:
            skipped_no_regions += 1
            continue

        if not ours_regions:
            skipped_no_regions += 1
            continue

        # Two-way alignment
        aligned = cmp.align_regions(ours_regions, m21_regions)

        # WiR three-way (optional)
        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        wir_regions = []
        if wir_path:
            try:
                wir_regions = dcml.parse_rntxt_file(wir_path)
                wir_coverage += 1
            except Exception:
                pass

        # Build our-region index for fast WiR lookup
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None] * len(ours_regions)

        processed += 1

        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != "chord_disagree":
                continue

            bir = our_r.bass_is_root

            # Two-way accumulation
            if bir:
                all_bir_errors_2way.append(our_r)
            else:
                all_nonbir_errors_2way.append(our_r)

            # Three-way: check WiR
            if wir_regions and i < len(wir_aligned):
                wir_r = wir_aligned[i]
                wir_pc = wir_r.root_pc if wir_r is not None else None
                category = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
                if category == "music21_dcml_agree":
                    if bir:
                        genuine_bir_errors.append(our_r)
                    else:
                        genuine_nonbir_errors.append(our_r)

    total_2way = len(all_bir_errors_2way) + len(all_nonbir_errors_2way)
    total_genuine = len(genuine_bir_errors) + len(genuine_nonbir_errors)

    print(f"Processed {processed} chorales  ({wir_coverage} with WiR three-way coverage)")
    print(f"\nTwo-way chord_disagree:  {total_2way}")
    print(f"  bassIsRoot=true:  {len(all_bir_errors_2way)} ({100*len(all_bir_errors_2way)/max(1,total_2way):.1f}%)")
    print(f"  bassIsRoot=false: {len(all_nonbir_errors_2way)} ({100*len(all_nonbir_errors_2way)/max(1,total_2way):.1f}%)")
    print(f"\nThree-way music21_dcml_agree genuine errors: {total_genuine}")
    if total_genuine > 0:
        print(f"  bassIsRoot=true:  {len(genuine_bir_errors)} ({100*len(genuine_bir_errors)/max(1,total_genuine):.1f}%)")
        print(f"  bassIsRoot=false: {len(genuine_nonbir_errors)} ({100*len(genuine_nonbir_errors)/max(1,total_genuine):.1f}%)")

    # Use three-way genuine errors if we have them; fall back to two-way
    errors = genuine_bir_errors if genuine_bir_errors else all_bir_errors_2way
    source = "three-way genuine errors" if genuine_bir_errors else "two-way chord_disagree"
    n = len(errors)
    if n == 0:
        print("\nNo bassIsRoot=true errors to analyze.")
        return

    print(f"\n{'='*70}")
    print(f"DETAILED ANALYSIS: bassIsRoot=true errors ({source}, n={n})")
    print(f"{'='*70}")

    # ── Q1: chordScoreMargin distribution ─────────────────────────────────
    margins = [r.chord_score_margin or 0.0 for r in errors]
    lt_025 = sum(1 for m in margins if m < 0.25)
    lt_05  = sum(1 for m in margins if m < 0.5)
    lt_1   = sum(1 for m in margins if m < 1.0)
    lt_15  = sum(1 for m in margins if m < 1.5)
    lt_2   = sum(1 for m in margins if m < 2.0)
    gt_2   = sum(1 for m in margins if m >= 2.0)
    bt_05_2 = sum(1 for m in margins if 0.5 <= m < 2.0)

    print(f"\n── chordScoreMargin distribution ──")
    print(f"  margin < 0.25  (barely wins):           {lt_025:4d}  ({100*lt_025/n:.1f}%)")
    print(f"  margin < 0.50  (low confidence):        {lt_05:4d}  ({100*lt_05/n:.1f}%)")
    print(f"  margin < 1.00:                          {lt_1:4d}  ({100*lt_1/n:.1f}%)")
    print(f"  margin < 1.50:                          {lt_15:4d}  ({100*lt_15/n:.1f}%)")
    print(f"  0.5 ≤ margin < 2.0  (moderate):        {bt_05_2:4d}  ({100*bt_05_2/n:.1f}%)")
    print(f"  margin >= 2.0  (wins convincingly):     {gt_2:4d}  ({100*gt_2/n:.1f}%)")

    # ── Q2: best alternative quality ──────────────────────────────────────
    CLEAN = {"Major", "Minor", "Diminished", "HalfDiminished",
             "Dominant7", "Major7", "Minor7", "Diminished7"}
    has_clean_alt = dirty_alt_only = no_alt = 0
    alt_quality_counts: Counter = Counter()

    for r in errors:
        alts = r.alternatives
        if not alts:
            no_alt += 1
            continue
        found_clean = False
        for alt in alts:
            q = alt.get("quality", "")
            alt_quality_counts[q] += 1
            if q in CLEAN:
                found_clean = True
        if found_clean:
            has_clean_alt += 1
        else:
            dirty_alt_only += 1

    print(f"\n── Best alternative quality ──")
    print(f"  Has clean triad/7th alt (fixable):  {has_clean_alt:4d}  ({100*has_clean_alt/n:.1f}%)")
    print(f"  No alternatives listed:             {no_alt:4d}  ({100*no_alt/n:.1f}%)")
    print(f"  Only non-clean alts:                {dirty_alt_only:4d}  ({100*dirty_alt_only/n:.1f}%)")
    print(f"  Top alternative qualities:")
    for q, cnt in alt_quality_counts.most_common(8):
        print(f"    {q:<22} {cnt:4d}")

    # ── Q3: noteCount distribution ─────────────────────────────────────────
    note_counts: Counter = Counter(r.note_count or 0 for r in errors)
    nc1  = note_counts.get(1, 0)
    nc2  = note_counts.get(2, 0)
    nc3p = sum(v for k, v in note_counts.items() if k >= 3)

    print(f"\n── noteCount distribution ──")
    for nc in sorted(note_counts.keys()):
        print(f"  noteCount={nc}: {note_counts[nc]:4d}  ({100*note_counts[nc]/n:.1f}%)")
    print(f"  -- grouped --")
    print(f"  noteCount=1 (arpeggio artifact):  {nc1:4d}  ({100*nc1/n:.1f}%)")
    print(f"  noteCount=2 (ambiguous):          {nc2:4d}  ({100*nc2/n:.1f}%)")
    print(f"  noteCount>=3 (genuine chord):     {nc3p:4d}  ({100*nc3p/n:.1f}%)")

    # ── Q4: beat position distribution ────────────────────────────────────
    beats = [r.beat for r in errors]
    beat_counts: Counter = Counter(round(b) for b in beats)
    beat1 = sum(1 for b in beats if abs(b - 1.0) < 0.26)
    beat2 = sum(1 for b in beats if abs(b - 2.0) < 0.26)
    beat3 = sum(1 for b in beats if abs(b - 3.0) < 0.26)
    beat4 = sum(1 for b in beats if abs(b - 4.0) < 0.26)
    other = n - beat1 - beat2 - beat3 - beat4

    print(f"\n── Beat position distribution ──")
    print(f"  Beat 1 (downbeat): {beat1:4d}  ({100*beat1/n:.1f}%)")
    print(f"  Beat 2:            {beat2:4d}  ({100*beat2/n:.1f}%)")
    print(f"  Beat 3:            {beat3:4d}  ({100*beat3/n:.1f}%)")
    print(f"  Beat 4:            {beat4:4d}  ({100*beat4/n:.1f}%)")
    print(f"  Other (offbeats):  {other:4d}  ({100*other/n:.1f}%)")

    # ── Summary for fix design ─────────────────────────────────────────────
    targetable_margin = sum(1 for r in errors
                            if (r.chord_score_margin or 0) < 0.5
                            and (r.note_count or 0) >= 3)
    targetable_margin1 = sum(1 for r in errors
                             if (r.chord_score_margin or 0) < 1.0
                             and (r.note_count or 0) >= 3)

    print(f"\n{'='*70}")
    print("FIX DESIGN SUMMARY")
    print(f"{'='*70}")
    print(f"Total bassIsRoot=true errors analyzed:         {n}")
    print(f"Targetable at margin<0.5, noteCount>=3:        {targetable_margin}  ({100*targetable_margin/n:.1f}%)")
    print(f"Targetable at margin<1.0, noteCount>=3:        {targetable_margin1}  ({100*targetable_margin1/n:.1f}%)")
    print(f"Arpeggio artifacts (noteCount=1):              {nc1}  ({100*nc1/n:.1f}%)  -- need separate fix")
    print(f"High-confidence bass-root (margin>=2.0):       {gt_2}  ({100*gt_2/n:.1f}%)  -- fix won't help, likely correct")

    # Margin histogram for threshold selection
    print(f"\nMargin histogram (0.25 bins):")
    bins = [(i*0.25, (i+1)*0.25) for i in range(12)]
    for lo, hi in bins:
        cnt = sum(1 for m in margins if lo <= m < hi)
        bar = '█' * (cnt * 40 // max(1, n))
        print(f"  [{lo:.2f}, {hi:.2f}): {cnt:4d}  {bar}")
    hi_cnt = sum(1 for m in margins if m >= 3.0)
    if hi_cnt:
        print(f"  [3.00, ∞   ): {hi_cnt:4d}")


if __name__ == "__main__":
    main()
