#!/usr/bin/env python3
"""
enumerate_near_agree_iter38.py — Enumerate BIR=true near_agree cases.

For each region where our winner has bassIsRoot=True but music21's chord matches
one of our alternatives (near_agree classification), reports all structured fields.

Reports two sets:
  ALL:  all near_agree + bassIsRoot=true cases (two-way, n=53)
  DCML: subset where DCML also agrees with music21 = our alt (three-way genuine, n=16)
        These are the cases that moved from BIR=true=48 → BIR=true=32 in Iter 36.

Standing rule: uses ONLY structured numeric/enum fields from JSON
(rootPitchClass, bassPitchClass, quality, score, bassIsRoot, etc.).
No chord symbol string parsing of any kind.

Usage:
    cd C:\\s\\MS && python tools/enumerate_near_agree_iter38.py
"""
from __future__ import annotations

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


def _norm_quality(q: str) -> str:
    return cmp._norm_quality(q)


def _find_matching_alt(ours: cmp.Region, theirs: cmp.Region) -> dict | None:
    """
    Re-run the _matches_alternative check and return the first matching alt dict.
    Uses only rootPitchClass (int) and quality (enum string) — no symbol parsing.
    """
    for alt in ours.alternatives:
        rpc = alt.get("rootPitchClass")
        q   = alt.get("quality", "")
        if rpc is None:
            continue
        if (int(rpc) == theirs.root_pc
                and _norm_quality(q) == _norm_quality(theirs.quality)):
            return alt
    return None


def _print_cases(cases: list[dict], label: str) -> None:
    print(f"{label} ({len(cases)} cases):")
    print(f"  {'File':<14} {'m':>4} {'beat':>5}  "
          f"{'winner_q':<16} {'wRpc':>5} {'wBpc':>5}  "
          f"{'alt_q':<16} {'aRpc':>5} {'aBpc':>5}  "
          f"{'margin':>8}")
    print("  " + "-" * 96)
    for c in cases:
        print(f"  {c['stem']:<14} m{c['measure']:>3}  b{c['beat']:>4.1f}  "
              f"{c['winner_quality']:<16} {c['winner_root_pc']:>5} {c['winner_bass_pc']:>5}  "
              f"{c['alt_quality']:<16} {c['alt_root_pc']:>5} {c['alt_bass_pc']:>5}  "
              f"{c['margin']:>+8.3f}")
    print()


def _quality_pairs(cases: list[dict]) -> Counter:
    return Counter(f"({c['winner_quality']}→{c['alt_quality']})" for c in cases)


def _margin_dist(cases: list[dict]) -> None:
    margins = [c["margin"] for c in cases]
    eq_0   = sum(1 for m in margins if abs(m) < 0.001)
    le_020 = sum(1 for m in margins if m <= 0.20)
    le_035 = sum(1 for m in margins if m <= 0.35)
    le_050 = sum(1 for m in margins if m <= 0.50)
    print(f"  margin == 0.00 (exact tie):  {eq_0}")
    print(f"  margin <= 0.20:              {le_020}")
    print(f"  margin <= 0.35:              {le_035}")
    print(f"  margin <= 0.50:              {le_050}")
    print(f"  total cases:                 {len(cases)}")
    print()


def main() -> None:
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))
    if not ours_files:
        print("ERROR: No .ours.json files found in tools/corpus/", file=sys.stderr)
        sys.exit(1)

    all_cases:  list[dict] = []   # all near_agree + bassIsRoot=true (two-way)
    dcml_cases: list[dict] = []   # subset: DCML also agrees (three-way genuine)

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

        aligned = cmp.align_regions(ours_regions, m21_regions)

        # Load DCML (WiR) for three-way filter
        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        wir_regions: list = []
        if wir_path:
            try:
                wir_regions = dcml.parse_rntxt_file(wir_path)
            except Exception:
                pass
        wir_aligned = (cmp.align_dcml_regions(ours_regions, wir_regions)
                       if wir_regions else [None] * len(ours_regions))

        for i, (our_r, their_r) in enumerate(aligned):
            if their_r is None:
                continue
            if not our_r.bass_is_root:
                continue
            result = cmp.classify(our_r, their_r)
            if result.category != "near_agree":
                continue

            matched_alt = _find_matching_alt(our_r, their_r)
            if matched_alt is None:
                print(f"WARNING: near_agree re-find failed for {stem} "
                      f"m{our_r.measure_number}", file=sys.stderr)
                continue

            winner_score = our_r.chord_score or 0.0
            alt_score    = float(matched_alt.get("score", 0.0))
            margin       = winner_score - alt_score

            alt_bass_raw = matched_alt.get("bassPitchClass")
            alt_bass_pc  = int(alt_bass_raw) if alt_bass_raw is not None else -1
            alt_root_pc  = int(matched_alt.get("rootPitchClass", -1))

            case = {
                "stem":           stem,
                "measure":        our_r.measure_number,
                "beat":           our_r.beat,
                "winner_quality": _norm_quality(our_r.quality),
                "winner_root_pc": our_r.root_pc,
                "winner_bass_pc": (our_r.bass_pc if our_r.bass_pc is not None
                                   else our_r.root_pc),
                "winner_score":   winner_score,
                "alt_quality":    _norm_quality(matched_alt.get("quality", "")),
                "alt_root_pc":    alt_root_pc,
                "alt_bass_pc":    alt_bass_pc,
                "alt_score":      alt_score,
                "margin":         margin,
            }
            all_cases.append(case)

            # Three-way filter: DCML root_pc == matched alt's rootPitchClass
            # (which equals theirs.root_pc since _matches_alternative confirmed that)
            wir_r = wir_aligned[i] if i < len(wir_aligned) else None
            wir_pc = wir_r.root_pc if wir_r is not None else None
            tw_cat = cmp.three_way_classify(our_r.root_pc, their_r.root_pc, wir_pc)
            if tw_cat == "music21_dcml_agree":
                dcml_cases.append(case)

    # ── ALL cases ─────────────────────────────────────────────────────────
    _print_cases(all_cases, "ALL near_agree BIR=true cases (two-way)")

    print("Quality-pair breakdown — ALL (sorted by count desc):")
    for pair, count in _quality_pairs(all_cases).most_common():
        print(f"  {pair} = {count}")
    print()

    print("Margin distribution — ALL:")
    _margin_dist(all_cases)

    # ── DCML-confirmed (three-way genuine) subset ─────────────────────────
    print("=" * 70)
    _print_cases(dcml_cases,
                 "DCML-confirmed near_agree BIR=true (three-way genuine, moved from BIR=true=48)")

    print("Quality-pair breakdown — DCML-confirmed (sorted by count desc):")
    for pair, count in _quality_pairs(dcml_cases).most_common():
        print(f"  {pair} = {count}")
    print()

    print("Margin distribution — DCML-confirmed:")
    _margin_dist(dcml_cases)


if __name__ == "__main__":
    main()
