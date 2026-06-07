#!/usr/bin/env python3
"""
iter94_jazz_regression_analysis.py
==================================

Diagnose which Jazz BIR=true cases in the current corpus are NEW due to the
Iter 94 w_stepIn / w_stepOut bonus (+0.10 each, capped +0.20 combined).

For each three-way genuine BIR=true error in the Jazz corpus, this script:

  1. Reads previous and next region bassPitchClass from the same score's
     ours.json (parent-scope neighbor bass — exactly what Iter 94 supplies
     to analyzeChord).
  2. Computes whether w_stepIn would fire on the WINNING candidate
     (winner is root-position AND (rootPc - prevBass) %% 12 in {1,2,10,11}).
  3. Computes whether w_stepOut would fire on the WINNING candidate
     (winner is root-position AND (nextBass - rootPc) %% 12 in {1,2,10,11}).
  4. Searches alternatives for one with rootPitchClass == dcml_root_pc whose
     score is within +0.20 of the winner (i.e. the bonus could have flipped
     the order). Reports the alt's bass, quality, score, and the gap that
     the bonus would close.
  5. Clusters cases by (winner-quality, step-fire pattern, gap-closable-by-bonus)
     and reports the dominant pattern(s).

Output: a printable summary plus a tab-separated table for clustering.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as _dcml
dcml = _dcml

K_STEP_BONUS_EACH = 0.10
K_STEP_BONUS_MAX  = 0.20  # both stepIn + stepOut

PC_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def pc_str(p):
    return PC_NAMES[p % 12] if p is not None else "?"


def is_step(delta: int) -> bool:
    """delta is (target - source) mod 12; semitone or whole-tone in either dir."""
    return delta in (1, 2, 10, 11)


def step_fires(winner_root: int, winner_bass: int, prev_bass: int | None,
               next_bass: int | None) -> tuple[bool, bool]:
    """Return (stepIn_fires, stepOut_fires) for the WINNING candidate.

    Step bonus only fires on root-position candidates per Iter 94 guard
    (candBassPc == rootPc).
    """
    if winner_bass != winner_root:
        return (False, False)
    step_in = False
    step_out = False
    if prev_bass is not None and prev_bass != winner_root:
        delta = (winner_root - prev_bass + 12) % 12
        step_in = is_step(delta)
    if next_bass is not None and next_bass != winner_root:
        delta = (next_bass - winner_root + 12) % 12
        step_out = is_step(delta)
    return (step_in, step_out)


def find_dcml_alt(alternatives: list[dict], dcml_root_pc: int) -> dict | None:
    for a in alternatives:
        if a.get("rootPitchClass") == dcml_root_pc:
            return a
    return None


def main():
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))

    rows = []
    cluster_counts = Counter()
    quality_step_pattern = Counter()

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

        # Jazz corpus only — the preset is stamped at the top of ours.json
        if ours_raw.get("preset", "").lower() != "jazz":
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
            if i >= len(ours_raw_regions):
                continue

            raw = ours_raw_regions[i]
            alts = raw.get("alternatives", []) or []
            winner_score = raw.get("chordScore", 0.0)
            winner_root = raw.get("rootPitchClass")
            winner_bass = raw.get("bassPitchClass")

            # Neighbor parent regions' bass PCs.  ours_raw_regions is the
            # *post-segmentation* region list — same scope the bridge uses
            # when supplying parent-scope prev/next bass to analyzeChord.
            prev_bass = (ours_raw_regions[i - 1].get("bassPitchClass")
                         if i > 0 else None)
            next_bass = (ours_raw_regions[i + 1].get("bassPitchClass")
                         if i + 1 < len(ours_raw_regions) else None)

            step_in, step_out = step_fires(winner_root, winner_bass,
                                           prev_bass, next_bass)
            applied_bonus = (K_STEP_BONUS_EACH if step_in else 0.0) + \
                            (K_STEP_BONUS_EACH if step_out else 0.0)

            # Does an alt with DCML-matching root exist whose post-removal
            # score would beat the winner's post-removal score?  We don't
            # know whether the step bonus also fired on the alt (it didn't
            # in the run; if it had, the alt would have moved up too — we
            # treat the bonus as applied only to the winner since the alt
            # didn't win).  Effective gap to close: applied_bonus.
            dcml_alt = find_dcml_alt(alts, wir_r.root_pc)
            alt_score = dcml_alt.get("score", 0.0) if dcml_alt else None
            margin = (winner_score - alt_score) if alt_score is not None else None
            flips_if_bonus_removed = (
                margin is not None
                and applied_bonus > 0.0
                and margin <= applied_bonus + 1e-6
            )

            # Even if the DCML root isn't in alternatives, the bonus might
            # have promoted the winner over OTHER non-DCML alts — but only
            # the DCML-flip case is a regression caused by Iter 94.

            row = {
                "stem": stem,
                "measure": our_r.measure_number,
                "beat": our_r.beat,
                "start_tick": raw.get("startTick"),
                "winner_root": winner_root,
                "winner_quality": raw.get("quality"),
                "winner_symbol": raw.get("chordSymbol"),
                "winner_bass": winner_bass,
                "winner_score": winner_score,
                "dcml_root": wir_r.root_pc,
                "dcml_symbol": wir_r.chord_symbol,
                "prev_bass": prev_bass,
                "next_bass": next_bass,
                "step_in": step_in,
                "step_out": step_out,
                "applied_bonus": applied_bonus,
                "dcml_alt_score": alt_score,
                "dcml_alt_bass": dcml_alt.get("bassPitchClass") if dcml_alt else None,
                "dcml_alt_quality": dcml_alt.get("quality") if dcml_alt else None,
                "margin": margin,
                "flips_if_bonus_removed": flips_if_bonus_removed,
                "step_interval_in": ((winner_root - prev_bass + 12) % 12
                                      if prev_bass is not None and winner_bass == winner_root else None),
                "step_interval_out": ((next_bass - winner_root + 12) % 12
                                       if next_bass is not None and winner_bass == winner_root else None),
            }
            rows.append(row)

            # Cluster keys
            sig = ""
            if step_in and step_out: sig = "BOTH"
            elif step_in:            sig = "IN"
            elif step_out:           sig = "OUT"
            else:                    sig = "NEITHER"
            cluster_counts[sig] += 1
            quality_step_pattern[(row["winner_quality"], sig,
                                   "flip" if flips_if_bonus_removed else "noflip")] += 1

    # ── Report ────────────────────────────────────────────────────────────
    print(f"Total Jazz BIR=true (current corpus, post-Iter-94): {len(rows)}")
    print()

    print("=" * 80)
    print("Step-bonus-fires distribution over ALL 137 BIR=true winners:")
    print("=" * 80)
    for sig, cnt in cluster_counts.most_common():
        print(f"  {sig:<8}  {cnt:>4}")
    print()

    flips = [r for r in rows if r["flips_if_bonus_removed"]]
    print("=" * 80)
    print(f"Cases where removing the Iter 94 bonus would FLIP winner to a")
    print(f"DCML-matching alternative (these are very likely NEW Iter-94 regressions):")
    print(f"   total: {len(flips)}")
    print("=" * 80)
    print()
    print(f"{'stem':<28} {'m':>3} {'b':>5} {'tick':>6}  "
          f"{'winner':>12} {'dcml':>10}  "
          f"{'pb':>3} {'nb':>3}  {'in':>2} {'out':>3}  "
          f"{'altScore':>8} {'gap':>6} {'altBass':>7} {'altQ':>10}")
    for r in flips:
        winner = f"{pc_str(r['winner_root'])} {r['winner_quality'][:3]}"
        if r["winner_bass"] != r["winner_root"]:
            winner += f"/{pc_str(r['winner_bass'])}"
        dcml_s = f"{pc_str(r['dcml_root'])} {r['dcml_symbol'][:6]}"
        pb = pc_str(r["prev_bass"]) if r["prev_bass"] is not None else "-"
        nb = pc_str(r["next_bass"]) if r["next_bass"] is not None else "-"
        print(f"{r['stem']:<28} {r['measure']:>3} {r['beat']:>5.2f} "
              f"{r['start_tick']:>6}  "
              f"{winner:>12} {dcml_s:>10}  "
              f"{pb:>3} {nb:>3}  "
              f"{'Y' if r['step_in'] else '.':>2} "
              f"{'Y' if r['step_out'] else '.':>3}  "
              f"{r['dcml_alt_score']:>8.4f} {r['margin']:>6.4f} "
              f"{pc_str(r['dcml_alt_bass']):>7} "
              f"{(r['dcml_alt_quality'] or '?')[:10]:>10}")

    print()
    print("=" * 80)
    print("Cluster: (winner_quality, step_fire, flip_status)")
    print("=" * 80)
    for k, v in quality_step_pattern.most_common():
        q, sig, flip = k
        print(f"  {v:>4}  quality={q:<14} step={sig:<8} {flip}")

    # Detailed interval breakdown for FLIP cases
    print()
    print("=" * 80)
    print("Interval breakdown for FLIP cases (winner_root - prev_bass / next_bass - winner_root):")
    print("=" * 80)
    interval_counts = Counter()
    for r in flips:
        if r["step_in"]:
            interval_counts[("in", r["step_interval_in"])] += 1
        if r["step_out"]:
            interval_counts[("out", r["step_interval_out"])] += 1
    for k, v in interval_counts.most_common():
        direction, iv = k
        sign = "+" if iv <= 6 else "-"
        magnitude = iv if iv <= 6 else 12 - iv
        print(f"  {v:>4}  step{direction:<3}  delta={iv}  ({sign}{magnitude} semitones)")

    # Quality cluster of FLIP cases (the actionable subset)
    print()
    print("=" * 80)
    print(f"Quality distribution of FLIP cases (n={len(flips)}):")
    print("=" * 80)
    qc = Counter(r["winner_quality"] for r in flips)
    for q, c in qc.most_common():
        print(f"  {c:>4}  {q}")

    # distinctPcs and triad-complete breakdown for FLIP cases (does
    # combining with the distinctPcs==3 + complete-triad gate help?)
    print()
    print("=" * 80)
    print("distinctPcs and triad-complete for FLIP cases:")
    print("  (these are the same conditions the existing w_complete gate uses)")
    print("=" * 80)
    # Recompute from tones
    QUALITY_INTERVALS = {
        "Major":          (0, 4, 7),  "Minor":          (0, 3, 7),
        "Diminished":     (0, 3, 6),  "Augmented":      (0, 4, 8),
        "HalfDiminished": (0, 3, 6),  "Dominant7":      (0, 4, 7),
        "Major7":         (0, 4, 7),  "Minor7":         (0, 3, 7),
        "MinorMajor7":    (0, 3, 7),  "Diminished7":    (0, 3, 6),
        "Suspended2":     (0, 2, 7),  "Suspended4":     (0, 5, 7),
        "Power":          (0, 7),
    }
    EXT = 0.20
    complete_dpcs3 = 0
    for r in flips:
        # We need to reload raw tones; reread the file
        try:
            with open(_CORPUS_DIR / f"{r['stem']}.ours.json", encoding="utf-8") as fh:
                rraw = json.load(fh)
        except Exception:
            continue
        # Find region by start_tick
        region = None
        for rg in rraw.get("regions", []):
            if rg.get("startTick") == r["start_tick"]:
                region = rg
                break
        if region is None:
            continue
        pcw = [0.0] * 12
        for t in region.get("tones", []):
            pc = t.get("pitch", 0) % 12
            pcw[pc] += max(0.1, float(t.get("weight", 0.0)))
        dpcs = sum(1 for w in pcw if w > 0.0)
        ivs = QUALITY_INTERVALS.get(r["winner_quality"], ())
        triad_complete = all(pcw[(r["winner_root"] + iv) % 12] > EXT
                             for iv in ivs) if len(ivs) >= 3 else False
        r["_dpcs"] = dpcs
        r["_triad_complete"] = triad_complete
        if dpcs == 3 and triad_complete:
            complete_dpcs3 += 1
    distrib = Counter((r.get("_dpcs"), r.get("_triad_complete")) for r in flips)
    for k, v in sorted(distrib.items()):
        dpcs, comp = k
        print(f"  {v:>4}  distinctPcs={dpcs}  triadComplete={comp}")

    # Bass-PC of DCML alt relative to winner root
    print()
    print("=" * 80)
    print("DCML alt bass-relationship for FLIP cases:")
    print("=" * 80)
    bass_rel = Counter()
    for r in flips:
        if r["dcml_alt_bass"] is None:
            bass_rel["alt_bass_unknown"] += 1
            continue
        if r["dcml_alt_bass"] == r["dcml_root"]:
            bass_rel["alt_root_position"] += 1
        elif r["dcml_alt_bass"] == r["winner_root"]:
            bass_rel["alt_bass==our_root_(slash)"] += 1
        else:
            bass_rel["alt_other_inversion"] += 1
    for k, v in bass_rel.most_common():
        print(f"  {v:>4}  {k}")


if __name__ == "__main__":
    main()
