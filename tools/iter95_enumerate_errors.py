#!/usr/bin/env python3
"""
iter95_enumerate_errors.py — full enumeration of BIR=true and BIR=false
genuine errors (three-way music21+DCML agree) with the fields needed for
Iter 95 candidate evaluation:
  - score stem, measure, beat, startTick
  - our chord symbol + quality + (rootPc, bassPc)
  - DCML root pc + DCML chord string (effective)
  - interval (DCML_root - our_root) mod 12
  - distinctPcs (popcount of pitchClassSet bitmask)
  - quick pattern tag (third_above_bass, root_below_bass, etc.)

Usage:
    python tools/iter95_enumerate_errors.py --which bir_false > out.txt
    python tools/iter95_enumerate_errors.py --which bir_true  > out.txt
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"


def popcount(n: int) -> int:
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c


def pc_name(pc: int) -> str:
    return ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"][pc % 12]


def interval_name(semis: int) -> str:
    NAMES = ["P1", "m2", "M2", "m3", "M3", "P4", "TT", "P5", "m6", "M6", "m7", "M7"]
    return NAMES[semis % 12]


def pattern_tag(our_root_pc: int, dcml_root_pc: int, our_bass_pc: int) -> str:
    """Quick semantic label for the root-vs-DCML relationship."""
    interval = (dcml_root_pc - our_root_pc) % 12
    # Common patterns:
    # +0  : same root, quality differs (root agrees — should already be near_agree, rare here)
    # +3  : DCML root is a minor 3rd above ours (iii vs I confusion)
    # +4  : DCML root a major 3rd above (vi vs IV confusion? V/vi confusion?)
    # +8  : DCML root is a minor 6th above (= minor 3rd BELOW our root,
    #        often "iii triad mistaken for I" — e.g. {C,E,G} = C major vs Em/G mistake)
    # +9  : DCML root is a major 6th above (= minor 3rd BELOW our root,
    #        "I triad mistaken for vi" — e.g. {C,E,G} = Am/C mistake by us)
    # In general for the "we picked the third instead of the root" pattern:
    #   if DCML root sits a third BELOW our root (interval == 8 [m3 below] or 9 [M3 below])
    #   AND our root equals our bass: bass-as-root error.
    bass_is_root = (our_bass_pc == our_root_pc)
    if interval == 0:
        return "same_root_quality_diff"
    # Most common Iter 90 finding: our root was the THIRD of the DCML chord.
    # That means DCML root is a m3 or M3 BELOW our root, i.e. (dcml - our) % 12 in {8, 9}.
    if interval == 8 and bass_is_root:
        return "we_picked_M3_above_dcml_root"          # DCML root a m6 above (= m3 below)
    if interval == 9 and bass_is_root:
        return "we_picked_m3_above_dcml_root"          # DCML root a M6 above (= M3 below)
    # Inverse: our root is BELOW the dcml root, third-substitution
    if interval == 3:
        return "dcml_root_m3_above_ours"
    if interval == 4:
        return "dcml_root_M3_above_ours"
    # If our root equals our bass, but DCML root sits a P4 / P5 / TT away
    if interval == 5:
        return "dcml_root_P4_above_ours"
    if interval == 7:
        return "dcml_root_P5_above_ours"
    if interval == 6:
        return "dcml_root_TT_from_ours"
    if interval == 1:
        return "dcml_root_m2_above_ours"
    if interval == 2:
        return "dcml_root_M2_above_ours"
    if interval == 10:
        return "dcml_root_m7_above_ours"
    if interval == 11:
        return "dcml_root_M7_above_ours"
    return f"interval_{interval}"


def w_seq_candidate(our_bass_pc: int, our_root_pc: int, dcml_root_pc: int) -> bool:
    """
    The user's pre-existing 'w_seq' target description: 'root a third above
    bass, temporal context would help'. That maps to:
      - our analyzer picked a root one third ABOVE the bass (so bass != root)
      - AND the DCML root is the BASS pc, i.e. ours is a third-substitution
        (e.g. score has bass = C, content = C-E-G; analyzer picked Em with C
        as the third-below-bass, DCML says C).
    But we also need to capture cases where bass == our root and DCML root
    is a third BELOW (i.e. bass IS the third of the true chord, and the
    true root sits a third lower in the sequence — w_seq would help if the
    surrounding regions imply the true root).
    """
    # Case A: bass is a third BELOW our root (we picked the third as root).
    # That means our_root_pc - bass_pc in {3, 4}.
    diff_root_bass = (our_root_pc - our_bass_pc) % 12
    if diff_root_bass in (3, 4):
        # And DCML root equals the bass (true chord is rooted on the bass)
        if dcml_root_pc == our_bass_pc:
            return True
    # Case B: bass IS root (bass_is_root=true), but DCML root sits a third
    # below — i.e. our root is the third of the true chord, the true root
    # would be revealed by the previous/next region's bass.
    if our_bass_pc == our_root_pc:
        interval = (dcml_root_pc - our_root_pc) % 12
        if interval in (8, 9):
            return True
    return False


def load_pairs(which: str):
    """Yield (stem, our_region, music21_region, dcml_region) for each
    three-way music21_dcml_agree case where bass_is_root matches `which`."""
    target_bir = True if which == "bir_true" else False
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))
    rows = []
    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        m21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not m21_path.exists():
            continue
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions  = cmp.load_analysis(m21_path)
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
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None] * len(ours_regions)
        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != "chord_disagree":
                continue
            bir = our_r.bass_is_root
            if bir != target_bir:
                continue
            wir_r = wir_aligned[i] if i < len(wir_aligned) else None
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat = cmp.three_way_classify(
                our_r.root_pc,
                their_r.root_pc if their_r else None,
                wir_pc,
            )
            if cat != "music21_dcml_agree":
                continue
            rows.append((stem, our_r, their_r, wir_r))
    return rows


def fmt_row(idx: int, stem: str, our, m21, wir) -> str:
    pcs_count = popcount(our.pitch_class_set or 0) if our.pitch_class_set is not None else 0
    interval = (wir.root_pc - our.root_pc) % 12
    int_str = interval_name(interval)
    bass = our.bass_pc if our.bass_pc is not None else our.root_pc
    tag = pattern_tag(our.root_pc, wir.root_pc, bass)
    wseq = "Y" if w_seq_candidate(bass, our.root_pc, wir.root_pc) else "."
    dcml_str = f"{wir.roman_numeral}/{wir.local_key}"
    return (f"  {idx:3d}  {stem:<18} m{our.measure_number:>3d} b{our.beat:>4.2f}  "
            f"tick={our.start_tick:>6d}  ours={our.chord_symbol:<14} ({our.quality:<14}) "
            f"r={pc_name(our.root_pc):>2}({our.root_pc:>2}) "
            f"b={pc_name(bass):>2}({bass:>2})  "
            f"DCML={dcml_str:<14} r={pc_name(wir.root_pc):>2}({wir.root_pc:>2})  "
            f"int={int_str:<3}(+{interval:>2})  "
            f"pcs={pcs_count:>1}  margin={our.chord_score_margin or 0:.3f}  "
            f"wseq={wseq}  {tag}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--which", choices=["bir_true", "bir_false"], required=True)
    args = ap.parse_args()

    rows = load_pairs(args.which)
    print(f"=== Iter 95 enumeration: {args.which} (three-way music21+DCML agree) ===")
    print(f"Total: {len(rows)}\n")

    # Header
    print(f"  {'#':>3}  {'stem':<18} {'meas':>5} {'beat':>5}  {'tick':>11}  "
          f"{'our_chord':<14}  {'quality':<16} {'root':>6} {'bass':>6}  "
          f"{'dcml':<14}  {'dcml_root':>6}  {'int':>7}  pcs  margin  wseq  pattern")
    print("-" * 200)
    for i, (stem, our, m21, wir) in enumerate(rows, 1):
        print(fmt_row(i, stem, our, m21, wir))

    # Pattern aggregation
    print()
    print("─" * 70)
    print(f"Pattern tag distribution (n={len(rows)}):")
    tags = Counter()
    intervals = Counter()
    wseq_n = 0
    quality_pairs = Counter()  # (our_quality, dcml_quality_unknown) — we lack DCML quality cleanly
    pcs_dist = Counter()
    for stem, our, m21, wir in rows:
        bass = our.bass_pc if our.bass_pc is not None else our.root_pc
        tag = pattern_tag(our.root_pc, wir.root_pc, bass)
        tags[tag] += 1
        intervals[(wir.root_pc - our.root_pc) % 12] += 1
        if w_seq_candidate(bass, our.root_pc, wir.root_pc):
            wseq_n += 1
        pcs_dist[popcount(our.pitch_class_set or 0)] += 1
        quality_pairs[our.quality] += 1
    for tag, n in tags.most_common():
        print(f"  {tag:<40} {n:>4}  ({100*n/max(1,len(rows)):.1f}%)")

    print()
    print(f"Interval distribution (DCML_root - our_root) mod 12 — n={len(rows)}:")
    for iv in range(12):
        n = intervals.get(iv, 0)
        if n == 0:
            continue
        bar = "#" * (n * 40 // max(1, len(rows)))
        print(f"  +{iv:>2} ({interval_name(iv):<3}): {n:>4}  {bar}")

    print()
    print(f"distinctPcs distribution — n={len(rows)}:")
    for k in sorted(pcs_dist.keys()):
        print(f"  pcs={k}: {pcs_dist[k]}")

    print()
    print(f"Our quality distribution (genuine errors only):")
    for q, n in quality_pairs.most_common():
        print(f"  {q:<22} {n:>4}")

    print()
    print(f"w_seq candidates (root a third above bass with surrounding context implying lower root): "
          f"{wseq_n}/{len(rows)} = {100*wseq_n/max(1,len(rows)):.1f}%")


if __name__ == "__main__":
    main()
