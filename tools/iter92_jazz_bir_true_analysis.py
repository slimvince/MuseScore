#!/usr/bin/env python3
"""
iter92_jazz_bir_true_analysis.py — characterize the 136 Jazz BIR=true cases.

For each three-way genuine BIR=true error, report:
  - score / measure / beat
  - our chord (root, quality, symbol, bassPc, distinctPcs)
  - DCML ground truth (root, quality, symbol)
  - music21 chord (root, quality)
  - whether all 3 triad tones of OUR chord are present > extensionThreshold (0.20)
    (this is the w_complete signature from Iter 92)
  - whether any alternative has root matching DCML and bass != root
    (slash-chord that should have won)
  - alternative #2 detail

Output: tab-separated lines for further clustering.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

EXT_THRESHOLD = 0.20  # mirror chordanalyzer's extensionThreshold

QUALITY_INTERVALS = {
    "Major":          (0, 4, 7),
    "Minor":          (0, 3, 7),
    "Diminished":     (0, 3, 6),
    "Augmented":      (0, 4, 8),
    "HalfDiminished": (0, 3, 6),  # treat root+3+5 like Dim for w_complete
    "Dominant7":      (0, 4, 7),
    "Major7":         (0, 4, 7),
    "Minor7":         (0, 3, 7),
    "MinorMajor7":    (0, 3, 7),
    "Diminished7":    (0, 3, 6),
    "Suspended2":     (0, 2, 7),
    "Suspended4":     (0, 5, 7),
    "Power":          (0, 7),
}


def triad_present(our_region_raw: dict, root_pc: int, quality: str) -> bool:
    """Check if root + 3rd + 5th of (root_pc, quality) triad are all present
    above EXT_THRESHOLD in the region's tones aggregated pcWeights."""
    intervals = QUALITY_INTERVALS.get(quality)
    if not intervals or len(intervals) < 3:
        return False
    # Aggregate pcWeights from tones list (mirroring analyzer aggregation)
    pcw = [0.0] * 12
    for t in our_region_raw.get("tones", []):
        pc = t.get("pitch", 0) % 12
        pcw[pc] += max(0.1, float(t.get("weight", 0.0)))
    for iv in intervals:
        if pcw[(root_pc + iv) % 12] <= EXT_THRESHOLD:
            return False
    return True


def distinct_pcs(our_region_raw: dict) -> int:
    s = set()
    for t in our_region_raw.get("tones", []):
        s.add(t.get("pitch", 0) % 12)
    return len(s)


def find_dcml_match_alt(our_region_raw: dict, dcml_root_pc: int):
    """Return alternative dict whose rootPitchClass == dcml_root_pc, or None."""
    for alt in our_region_raw.get("alternatives", []):
        if alt.get("rootPitchClass") == dcml_root_pc:
            return alt
    return None


def main():
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))

    out_rows = []
    cluster_counts = Counter()
    bass_promotion_cases = []  # cases where DCML chord exists as alternative with different bass

    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        music21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not music21_path.exists():
            continue

        try:
            with open(ours_path, encoding="utf-8") as fh:
                ours_raw = json.load(fh)
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions = cmp.load_analysis(music21_path)
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
        if not wir_regions:
            continue
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions)

        ours_raw_regions = ours_raw.get("regions", [])

        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != "chord_disagree":
                continue
            if not our_r.bass_is_root:
                continue
            if i >= len(wir_aligned):
                continue
            wir_r = wir_aligned[i]
            if wir_r is None or wir_r.root_pc is None:
                continue
            cat = cmp.three_way_classify(our_r.root_pc,
                                          their_r.root_pc if their_r else None,
                                          wir_r.root_pc)
            if cat != "music21_dcml_agree":
                continue

            # Genuine BIR=true error
            raw_idx = i
            our_raw = ours_raw_regions[raw_idx] if raw_idx < len(ours_raw_regions) else {}

            d_pcs = distinct_pcs(our_raw)
            triad_complete = triad_present(our_raw, our_r.root_pc, our_r.quality)
            dcml_alt = find_dcml_match_alt(our_raw, wir_r.root_pc)
            margin = our_r.chord_score_margin or 0.0

            # Pattern: w_complete signature -- distinctPcs>=3, root+3+5 present,
            # and DCML root differs from our root
            w_complete_signature = (d_pcs >= 3 and triad_complete
                                    and our_r.root_pc != wir_r.root_pc)

            # Slash-chord regression signature: dcml root appears as alt with bass = our root
            slash_promotion = False
            slash_alt = None
            if dcml_alt is not None:
                dcml_alt_bass = dcml_alt.get("bassPitchClass")
                # The would-be DCML reading has its bass = our root_pc (i.e. our root
                # is acting as the bass of a slash chord)
                if dcml_alt_bass == our_r.root_pc:
                    slash_promotion = True
                    slash_alt = dcml_alt

            # Classify cluster
            quality_key = our_r.quality
            interval_from_dcml = (our_r.root_pc - wir_r.root_pc + 12) % 12

            if w_complete_signature:
                key = f"WCOMP_{quality_key}_interval{interval_from_dcml}"
                cluster_counts[key] += 1
            else:
                cluster_counts[f"OTHER_{quality_key}"] += 1

            if slash_promotion:
                bass_promotion_cases.append({
                    "stem": stem,
                    "measure": our_r.measure_number,
                    "beat": our_r.beat,
                    "our_root": our_r.root_pc,
                    "our_quality": our_r.quality,
                    "our_symbol": our_r.chord_symbol,
                    "dcml_root": wir_r.root_pc,
                    "dcml_symbol": wir_r.chord_symbol,
                    "dcml_alt": slash_alt,
                    "margin": margin,
                    "d_pcs": d_pcs,
                    "triad_complete": triad_complete,
                })

            out_rows.append({
                "stem": stem,
                "measure": our_r.measure_number,
                "beat": our_r.beat,
                "our_root": our_r.root_pc,
                "our_quality": our_r.quality,
                "our_symbol": our_r.chord_symbol,
                "our_bass": our_r.bass_pc,
                "dcml_root": wir_r.root_pc,
                "dcml_symbol": wir_r.chord_symbol,
                "m21_root": their_r.root_pc if their_r else None,
                "m21_quality": their_r.quality if their_r else None,
                "d_pcs": d_pcs,
                "triad_complete": triad_complete,
                "w_complete_signature": w_complete_signature,
                "slash_promotion": slash_promotion,
                "interval_our_minus_dcml": interval_from_dcml,
                "margin": margin,
                "alt1_root": (our_raw.get("alternatives") or [{}])[0].get("rootPitchClass"),
                "alt2_root": (our_raw.get("alternatives") + [{}, {}])[1].get("rootPitchClass")
                              if our_raw.get("alternatives") else None,
                "alt2_quality": (our_raw.get("alternatives") + [{}, {}])[1].get("quality")
                                 if our_raw.get("alternatives") else None,
                "alt2_bass": (our_raw.get("alternatives") + [{}, {}])[1].get("bassPitchClass")
                              if our_raw.get("alternatives") else None,
            })

    PC_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    def pc_str(p):
        return PC_NAMES[p % 12] if p is not None else "?"

    print(f"Total Jazz BIR=true genuine errors: {len(out_rows)}")
    w_comp_count = sum(1 for r in out_rows if r["w_complete_signature"])
    slash_count = sum(1 for r in out_rows if r["slash_promotion"])
    print(f"  with w_complete signature (distinctPcs>=3, root+3+5 present, our_root!=dcml_root): {w_comp_count}")
    print(f"  with slash_promotion (dcml chord exists as alt with bass = our root): {slash_count}")
    print()

    # Print full table
    print("=" * 120)
    print(f"{'stem':<28} {'m':>3} {'b':>5}  {'our':>10}  {'dcml':>10}  {'m21':>10}  "
          f"{'pcs':>3} {'triad':>5} {'wc':>3} {'sl':>3} {'iv':>3} {'mgn':>5}")
    print("=" * 120)
    for r in out_rows:
        our = f"{pc_str(r['our_root'])} {r['our_quality'][:3]}"
        if r["our_bass"] is not None and r["our_bass"] != r["our_root"]:
            our += f"/{pc_str(r['our_bass'])}"
        dcml_s = f"{pc_str(r['dcml_root'])} {r['dcml_symbol'][:6]}"
        m21_s = f"{pc_str(r['m21_root'])} {(r['m21_quality'] or '')[:3]}"
        print(f"{r['stem']:<28} {r['measure']:>3} {r['beat']:>5.2f}  "
              f"{our:>10}  {dcml_s:>10}  {m21_s:>10}  "
              f"{r['d_pcs']:>3} {'Y' if r['triad_complete'] else 'N':>5} "
              f"{'Y' if r['w_complete_signature'] else 'N':>3} "
              f"{'Y' if r['slash_promotion'] else 'N':>3} "
              f"{r['interval_our_minus_dcml']:>3} {r['margin']:>5.2f}")

    print()
    print("=" * 80)
    print("CLUSTER COUNTS")
    print("=" * 80)
    for key, cnt in cluster_counts.most_common():
        print(f"  {cnt:>4}  {key}")

    print()
    print("=" * 80)
    print(f"SLASH PROMOTION CASES (n={len(bass_promotion_cases)}):")
    print(f"  These are cases where the DCML reading is available as an alternative")
    print(f"  with its bass = our root, i.e. the analyzer flipped slash → root-position.")
    print("=" * 80)
    for c in bass_promotion_cases[:50]:
        dcml_alt = c["dcml_alt"]
        alt_str = (f"root={pc_str(dcml_alt.get('rootPitchClass'))} "
                   f"q={dcml_alt.get('quality')[:4]} "
                   f"bass={pc_str(dcml_alt.get('bassPitchClass'))} "
                   f"score={dcml_alt.get('score', 0):.2f}")
        print(f"  {c['stem']:<28} m{c['measure']:<3} b{c['beat']:.1f}  "
              f"our={pc_str(c['our_root'])}_{c['our_quality'][:3]}  "
              f"dcml={pc_str(c['dcml_root'])}_{c['dcml_symbol'][:6]}  "
              f"alt: {alt_str}  mgn={c['margin']:.2f}")


if __name__ == "__main__":
    main()
