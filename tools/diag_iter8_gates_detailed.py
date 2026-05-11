#!/usr/bin/env python3
"""
diag_iter8_gates_detailed.py — Per-gate condition analysis for BIR=false errors.

For each of the 1222 genuine BIR=false errors, reconstructs temporal context
from the region sequence and checks whether each temporal gate's FULL condition
is currently satisfied (given the post-fix code).

Identity-bass note:
  identity.bassPc (weight-thresholded in the analyser) is reconstructed from
  the tones field using bassPT = 0.05 * totalWeight.  It diverges from the raw
  bassPitchClass in only 17/11535 regions (0.15%), so bassPitchClass is an
  accurate proxy; we use the reconstructed value for correctness.

Gate full conditions checked:
  Families B/C/D   — MajorAdd6 ↔ Minor  (winner quality = Minor, rootPc = (bass+9)%12)
  Families G-B/C/D — MinorAdd6 ↔ HalfDim (winner quality = HalfDiminished, rootPc = (bass+9)%12)
  Families H-B/C/D — Augmented symmetry  (winner quality = Augmented, rootPc = (bass+4|8)%12)

  Gate B   : quality_B AND nrm AND st
  Gate C   : quality_B AND sf AND rcw
  Gate D   : quality_B AND cc >= 2
  Gate G-B : quality_G AND nrm AND st
  Gate G-C : quality_G AND sf AND rcw
  Gate G-D : quality_G AND cc >= 2
  Gate H-B : quality_H AND nrm AND st
  Gate H-C : quality_H AND sf AND rcw
  Gate H-D : quality_H AND cc >= 2

  where:
    nrm = nextRootPc  == winnerRootPc  (nextRoot matches the promoted inversion root)
    rcw = winnerRootPc in recentRootPcs  (inversion root appeared in last 3 regions)
    sf  = bassIsStepwiseFromPrevious  (identity-bass step from prev region)
    st  = bassIsStepwiseToNext        (isBass step to next region)
    cc  = consecutiveBassStepwiseCount

Score margin: chordScoreMargin = winner.score - alt[0].score (from JSON).
  Negative  → gate promoted a lower-scoring chord (gate-caused inversion).
  Positive  → inversion already outscored the root-position alternative.
"""
from __future__ import annotations

import json, sys, re
from pathlib import Path
from collections import Counter, defaultdict
from statistics import mean, median

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT       = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "tools" / "corpus"
WIR_DIR    = ROOT / "tools" / "dcml" / "when_in_rome"
BASS_PT    = 0.05   # bassPassingToneMinWeightFraction default

sys.path.insert(0, str(ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


# ── Helpers ───────────────────────────────────────────────────────────────────

def is_step(pc1: int, pc2: int) -> bool:
    if pc1 < 0 or pc2 < 0:
        return False
    d = abs(pc1 - pc2)
    return min(d, 12 - d) in (1, 2)


def identity_bass(tones: list[dict]) -> int:
    """Replicate analyser's weight-thresholded bass note selection."""
    total_w = sum(t["weight"] for t in tones)
    thresh  = BASS_PT * total_w
    qualifying = [t for t in tones if t["weight"] >= thresh]
    pool = qualifying if qualifying else tones
    return min(pool, key=lambda t: t["pitch"])["pitch"] % 12


def isBass_pc(tones: list[dict]) -> int:
    for t in tones:
        if t["isBass"]:
            return t["pitch"] % 12
    return -1


def quality_from_symbol(sym: str) -> str:
    s = sym.split("/")[0]
    m = re.match(r"^[A-G][#b]?", s)
    if not m:
        return "?"
    body = s[m.end():]
    if "dim7" in body or "°7" in body:       return "Diminished7"
    if body.startswith("ø") or "m7b5" in body.lower(): return "HalfDiminished"
    if "maj7" in body.lower() or body.startswith("M7"): return "Major7"
    if body.startswith("m7") or body.startswith("min7"): return "Minor7"
    if body.startswith("7"):                 return "Dominant7"
    if "dim" in body.lower() or "°" in body: return "Diminished"
    if body.startswith("m") or body.startswith("min"): return "Minor"
    return "Major"


# ── Gate condition checks ─────────────────────────────────────────────────────

def gate_conditions(e: dict) -> dict[str, bool]:
    """
    Returns a dict of gate_name → bool indicating whether that gate's
    FULL condition is currently satisfied for this error record.
    """
    sf   = e["sf"]
    st   = e["st"]
    cc   = e["cc"]
    rcw  = e["rcw"]
    nrm  = e["nrm"]
    qB   = e["is_BCD_pattern"]   # Minor at (bass+9)%12
    qG   = e["is_GBD_pattern"]   # HalfDim at (bass+9)%12
    qH   = e["is_HD_pattern"]    # Augmented at (bass+4)%12 or (bass+8)%12

    return {
        "B"   : qB and nrm and st,
        "C"   : qB and sf  and rcw,
        "D"   : qB and cc >= 2,
        "G-B" : qG and nrm and st,
        "G-C" : qG and sf  and rcw,
        "G-D" : qG and cc >= 2,
        "H-B" : qH and nrm and st,
        "H-C" : qH and sf  and rcw,
        "H-D" : qH and cc >= 2,
    }


# ── Per-file analysis ─────────────────────────────────────────────────────────

def analyze_file(ours_path: Path) -> list[dict]:
    stem = ours_path.stem.replace(".ours", "")
    music21_path = CORPUS_DIR / f"{stem}.music21.json"
    if not music21_path.exists():
        return []
    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    if not wir_path:
        return []

    try:
        _, ours_r  = cmp.load_analysis(ours_path)
        _, m21_r   = cmp.load_analysis(music21_path)
        wir_regs   = dcml.parse_rntxt_file(wir_path)
    except Exception:
        return []
    if not ours_r:
        return []

    aligned     = cmp.align_regions(ours_r, m21_r)
    wir_aligned = cmp.align_dcml_regions(ours_r, wir_regs)

    raw_regs    = json.loads(ours_path.read_text(encoding="utf-8")).get("regions", [])
    raw_by_tick = {int(r["startTick"]): r for r in raw_regs}

    # Rolling state — mirrors analyzeScore()
    prev_id_bass  = -1    # identity.bassPc of previous region (weight-thresholded)
    running_sw    = 0     # runningStepwiseCount
    recent_roots  = [-1, -1, -1]

    results: list[dict] = []

    for i, (our_reg, their_reg) in enumerate(aligned):
        raw = raw_by_tick.get(our_reg.start_tick, {})
        tones   = raw.get("tones", [])

        curr_id_bass = identity_bass(tones) if tones else our_reg.bass_pc or -1
        curr_is_bass = isBass_pc(tones)     if tones else (our_reg.bass_pc or -1)
        curr_root    = our_reg.root_pc if our_reg.root_pc is not None else -1

        # sf: isDiatonicStep(prev identity_bass, curr isBass)
        sf = is_step(prev_id_bass, curr_is_bass)
        if sf:
            running_sw += 1
        else:
            running_sw = 0

        # Look-ahead (st uses isBass for both)
        next_is_bass = -1
        next_root    = -1
        if i + 1 < len(aligned):
            next_reg = aligned[i + 1][0]
            next_raw = raw_by_tick.get(next_reg.start_tick, {})
            next_tones = next_raw.get("tones", [])
            next_is_bass = isBass_pc(next_tones) if next_tones else -1
            next_root    = next_reg.root_pc if next_reg.root_pc is not None else -1

        st  = is_step(curr_is_bass, next_is_bass)
        cc  = running_sw
        rcw = (curr_root != -1 and curr_root in recent_roots)
        nrm = (next_root != -1 and next_root == curr_root)

        # Quality patterns
        bass = curr_id_bass
        qBCD = (our_reg.quality == "Minor"
                and curr_root == (bass + 9) % 12)
        qGBD = (our_reg.quality == "HalfDiminished"
                and curr_root == (bass + 9) % 12)
        qHBD = (our_reg.quality == "Augmented"
                and (curr_root == (bass + 4) % 12
                     or curr_root == (bass + 8) % 12))

        # Three-way genuine BIR=false check
        cresult = cmp.classify(our_reg, their_reg)
        if cresult.category == "chord_disagree" and not our_reg.bass_is_root:
            wir_r  = wir_aligned[i] if i < len(wir_aligned) else None
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat3   = cmp.three_way_classify(our_reg.root_pc,
                                            their_reg.root_pc if their_reg else None,
                                            wir_pc)
            if cat3 == "music21_dcml_agree":
                margin = our_reg.chord_score_margin or 0.0

                results.append({
                    "stem":          stem,
                    "measure":       our_reg.measure_number,
                    "beat":          our_reg.beat,
                    "quality":       our_reg.quality or "?",
                    "root":          curr_root,
                    "bass":          bass,
                    "margin":        margin,
                    "sf":            sf,
                    "st":            st,
                    "cc":            cc,
                    "rcw":           rcw,
                    "nrm":           nrm,
                    "is_BCD_pattern": qBCD,
                    "is_GBD_pattern": qGBD,
                    "is_HD_pattern":  qHBD,
                })

        # Advance rolling state
        recent_roots  = [curr_root, recent_roots[0], recent_roots[1]]
        prev_id_bass  = curr_id_bass

    return results


# ── Main ──────────────────────────────────────────────────────────────────────

def margin_stats(margins: list[float]) -> str:
    if not margins:
        return "n/a"
    neg  = sum(1 for m in margins if m < 0)
    zero = sum(1 for m in margins if m == 0)
    pos  = sum(1 for m in margins if m > 0)
    return (f"neg={neg}({100*neg//len(margins)}%)  "
            f"zero={zero}  pos={pos}({100*pos//len(margins)}%)  "
            f"min={min(margins):.2f}  med={median(margins):.2f}  max={max(margins):.2f}")


def margin_hist(margins: list[float], bins=None) -> str:
    if not margins:
        return ""
    if bins is None:
        bins = [(-99, -1.0), (-1.0, -0.5), (-0.5, -0.25), (-0.25, 0.0),
                (0.0, 0.25), (0.25, 0.5), (0.5, 1.0), (1.0, 99)]
    lines = []
    for lo, hi in bins:
        c = sum(1 for m in margins if lo <= m < hi)
        pct = 100 * c // max(1, len(margins))
        bar = "█" * (c * 30 // max(1, len(margins)))
        label = f"[{lo:+.2f},{hi:+.2f})" if hi < 99 else f"[{lo:+.2f},+inf)"
        lines.append(f"  {label}  {c:>4}  {bar}")
    return "\n".join(lines)


def main() -> None:
    ours_files = sorted(CORPUS_DIR.glob("*.ours.json"))
    print(f"Scanning {len(ours_files)} files …")

    all_errors: list[dict] = []
    for f in ours_files:
        all_errors.extend(analyze_file(f))

    n = len(all_errors)
    print(f"Total genuine BIR=false errors: {n}\n")

    # ── Signal summary ────────────────────────────────────────────────────────
    sf_n  = sum(1 for e in all_errors if e["sf"])
    st_n  = sum(1 for e in all_errors if e["st"])
    cc2_n = sum(1 for e in all_errors if e["cc"] >= 2)
    rcw_n = sum(1 for e in all_errors if e["rcw"])
    nrm_n = sum(1 for e in all_errors if e["nrm"])
    qB_n  = sum(1 for e in all_errors if e["is_BCD_pattern"])
    qG_n  = sum(1 for e in all_errors if e["is_GBD_pattern"])
    qH_n  = sum(1 for e in all_errors if e["is_HD_pattern"])

    print("=== Signal prevalence across all BIR=false errors ===")
    print(f"  sf  (bassIsStepwiseFromPrevious) : {sf_n:>4}  ({100*sf_n//n}%)")
    print(f"  st  (bassIsStepwiseToNext)       : {st_n:>4}  ({100*st_n//n}%)")
    print(f"  cc>=2 (consec stepwise count)    : {cc2_n:>4}  ({100*cc2_n//n}%)")
    print(f"  rcw (recent roots contain winner): {rcw_n:>4}  ({100*rcw_n//n}%)")
    print(f"  nrm (next root == winner root)   : {nrm_n:>4}  ({100*nrm_n//n}%)")
    print(f"  quality pattern B (Minor +9)     : {qB_n:>4}  ({100*qB_n//n}%)")
    print(f"  quality pattern G (HalfDim +9)   : {qG_n:>4}  ({100*qG_n//n}%)")
    print(f"  quality pattern H (Aug ±4/8)     : {qH_n:>4}  ({100*qH_n//n}%)")
    print()

    # ── Per-gate analysis ─────────────────────────────────────────────────────
    gate_names = ["B", "C", "D", "G-B", "G-C", "G-D", "H-B", "H-C", "H-D"]

    print("=" * 70)
    print(f"PER-GATE CONDITION COUNTS  (n={n} BIR=false errors)")
    print("=" * 70)
    print(f"{'Gate':<6}  {'Full condition':<52}  {'Count':>5}  {'%':>5}")
    print("-" * 70)

    gate_errors: dict[str, list[dict]] = {}
    for g in gate_names:
        matching = [e for e in all_errors if gate_conditions(e)[g]]
        gate_errors[g] = matching
        pct = 100 * len(matching) // max(1, n)
        cond_desc = {
            "B"  : "Minor+(bass+9) AND nrm AND st",
            "C"  : "Minor+(bass+9) AND sf  AND rcw",
            "D"  : "Minor+(bass+9) AND cc>=2",
            "G-B": "HalfDim+(bass+9) AND nrm AND st",
            "G-C": "HalfDim+(bass+9) AND sf  AND rcw",
            "G-D": "HalfDim+(bass+9) AND cc>=2",
            "H-B": "Aug+(bass+4|8) AND nrm AND st",
            "H-C": "Aug+(bass+4|8) AND sf  AND rcw",
            "H-D": "Aug+(bass+4|8) AND cc>=2",
        }[g]
        print(f"  {g:<4}  {cond_desc:<52}  {len(matching):>5}  {pct:>4}%")

    print()

    # ── Pattern-only counts (temporal ignored) — baseline for scale ───────────
    print("=== Pattern-only counts (ignoring temporal — upper bound per family) ===")
    for pat, label in [("is_BCD_pattern", "B/C/D quality (Minor at bass+9)"),
                        ("is_GBD_pattern", "G-B/C/D quality (HalfDim at bass+9)"),
                        ("is_HD_pattern",  "H-B/C/D quality (Aug at bass+4|8)")]:
        m = sum(1 for e in all_errors if e[pat])
        print(f"  {label:<42}  {m:>4}  ({100*m//n}%)")
    print()

    # ── Per-gate margin detail ────────────────────────────────────────────────
    print("=" * 70)
    print("SCORE MARGIN DETAIL per gate  (winner.score - alt[0].score)")
    print("  neg = gate promoted lower-scoring chord; pos = natural win")
    print("=" * 70)
    for g in gate_names:
        errs = gate_errors[g]
        if not errs:
            print(f"\nGate {g}: 0 matching errors — skip")
            continue
        margins = [e["margin"] for e in errs]
        neg = sum(1 for m in margins if m < 0)
        pos = sum(1 for m in margins if m >= 0)
        print(f"\nGate {g}  (n={len(errs)})")
        print(f"  Margin summary: {margin_stats(margins)}")
        print(f"  Margin histogram:")
        print(margin_hist(margins))
        # Winner quality breakdown for this gate's errors
        qctr = Counter(e["quality"] for e in errs)
        print(f"  Winner quality: {dict(qctr.most_common(5))}")

    # ── Overall margin distribution for all 1222 BIR=false errors ────────────
    print()
    print("=" * 70)
    print(f"OVERALL margin distribution for all {n} BIR=false errors")
    print("=" * 70)
    all_margins = [e["margin"] for e in all_errors]
    print(f"  {margin_stats(all_margins)}")
    print(margin_hist(all_margins))

    # ── sf-breakdown for quality-matching errors ─────────────────────────────
    print()
    print("=" * 70)
    print("SF BREAKDOWN for quality-pattern-matching errors")
    print("(shows how many quality-pattern errors have sf=True — Gate C/G-C/H-C eligibility)")
    print("=" * 70)
    for pat, label in [("is_BCD_pattern", "B/C/D (Minor at bass+9)"),
                        ("is_GBD_pattern", "G-B/C/D (HalfDim at bass+9)"),
                        ("is_HD_pattern",  "H-B/C/D (Aug at bass+4|8)")]:
        subset = [e for e in all_errors if e[pat]]
        sf_yes = [e for e in subset if e["sf"]]
        sf_rcw = [e for e in sf_yes if e["rcw"]]
        print(f"  {label}: total={len(subset)}  sf=True: {len(sf_yes)}  sf+rcw: {len(sf_rcw)}")


if __name__ == "__main__":
    main()
