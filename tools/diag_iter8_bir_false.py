#!/usr/bin/env python3
"""
diag_iter8_bir_false.py — Temporal signal analysis for BIR=false regressions.

For each genuine three-way BIR=false error (we say inversion, music21 + WiR
both say root-position), reconstructs the temporal context from the region
sequence in the .ours.json file and records:

  (a) winner quality  — quality of the chord we picked (an inversion)
  (b) alt quality     — quality of our first alternative (typically root-pos)
  (c) bassIsStepwiseFromPrevious
  (d) bassIsStepwiseToNext
  (e) recentRootPcs[0/1/2] contains winner rootPc
  (f) consecutiveBassStepwiseCount
  (g) nextRootPc vs winnerRootPc

Then groups errors by which temporal-signal pattern fired and reports the
top patterns.  Output only — no files are modified.
"""
from __future__ import annotations

import json, sys, re
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT       = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "tools" / "corpus"
WIR_DIR    = ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


# ── Helpers ───────────────────────────────────────────────────────────────────

def is_step(pc1: int, pc2: int) -> bool:
    """Chromatic step (1 or 2 semitones), matching batch_analyze isDiatonicStep."""
    if pc1 < 0 or pc2 < 0:
        return False
    d = abs(pc1 - pc2)
    d = min(d, 12 - d)
    return d in (1, 2)


def quality_from_symbol(sym: str) -> str:
    s = sym.split("/")[0]
    m = re.match(r"^[A-G][#b]?", s)
    if not m:
        return "?"
    body = s[m.end():]
    if "dim7" in body or "°7" in body:      return "Diminished7"
    if body.startswith("ø") or "m7b5" in body.lower(): return "HalfDiminished"
    if "maj7" in body.lower() or body.startswith("M7"): return "Major7"
    if body.startswith("m7") or body.startswith("min7"): return "Minor7"
    if body.startswith("7"):                return "Dominant7"
    if "dim" in body.lower() or "°" in body: return "Diminished"
    if body.startswith("m") or body.startswith("min"): return "Minor"
    return "Major"


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
        _, ours_regions = cmp.load_analysis(ours_path)
        _, m21_regions  = cmp.load_analysis(music21_path)
        wir_regions     = dcml.parse_rntxt_file(wir_path)
    except Exception:
        return []

    if not ours_regions:
        return []

    aligned     = cmp.align_regions(ours_regions, m21_regions)
    wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions)

    # Raw JSON for alternatives + bassPitchClass
    raw_regions = json.loads(ours_path.read_text(encoding="utf-8")).get("regions", [])
    raw_by_tick = {r["startTick"]: r for r in raw_regions}

    # Rolling temporal state (mirrors analyzeScore loop)
    prev_bass       = -1       # ctx.previousBassPc before loop; -1 = no prior region
    running_stepwise = 0       # runningStepwiseCount
    recent_roots    = [-1, -1, -1]  # recentRootsBuf, most-recent-first

    results = []

    for i, (our_r, their_r) in enumerate(aligned):
        raw = raw_by_tick.get(str(our_r.start_tick), {})

        curr_bass = int(raw["bassPitchClass"]) if raw else -1
        curr_root = our_r.root_pc if our_r.root_pc is not None else -1

        # ── Reconstruct temporal context at analysis time for this region ──

        sf = is_step(prev_bass, curr_bass)
        if sf:
            running_stepwise += 1
        else:
            running_stepwise = 0

        # look-ahead (next region in aligned sequence)
        next_bass = -1
        next_root = -1
        if i + 1 < len(aligned):
            next_our = aligned[i + 1][0]
            next_raw = raw_by_tick.get(str(next_our.start_tick), {})
            next_bass = int(next_raw["bassPitchClass"]) if next_raw else -1
            next_root = next_our.root_pc if next_our.root_pc is not None else -1

        st  = is_step(curr_bass, next_bass)
        cc  = running_stepwise           # consecutiveBassStepwiseCount
        rcw = (curr_root != -1 and curr_root in recent_roots)
        nrm = (next_root != -1 and next_root == curr_root)

        # ── Check three-way BIR=false ──────────────────────────────────────
        cresult = cmp.classify(our_r, their_r)
        if cresult.category == "chord_disagree" and not our_r.bass_is_root:
            wir_r  = wir_aligned[i] if i < len(wir_aligned) else None
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat3   = cmp.three_way_classify(our_r.root_pc,
                                            their_r.root_pc if their_r else None,
                                            wir_pc)
            if cat3 == "music21_dcml_agree":
                # alt quality: first alternative in our list
                alts = raw.get("alternatives", []) if raw else our_r.alternatives or []
                alt_q = quality_from_symbol(alts[0]["chordSymbol"]) if alts else "?"

                results.append({
                    "stem":             stem,
                    "measure":          our_r.measure_number,
                    "beat":             our_r.beat,
                    "winner_quality":   our_r.quality or "?",
                    "alt_quality":      alt_q,
                    "sf":               sf,    # (c) bassIsStepwiseFromPrevious
                    "st":               st,    # (d) bassIsStepwiseToNext
                    "rcw":              rcw,   # (e) recentRootPcs contains winner root
                    "cc":               cc,    # (f) consecutiveBassStepwiseCount
                    "nrm":              nrm,   # (g) nextRootPc == winnerRootPc
                    "next_root":        next_root,
                    "winner_root":      curr_root,
                    "recent_roots":     list(recent_roots),
                    "prev_bass":        prev_bass,
                    "curr_bass":        curr_bass,
                    "next_bass":        next_bass,
                })

        # ── Advance rolling state ──────────────────────────────────────────
        recent_roots = [curr_root, recent_roots[0], recent_roots[1]]
        prev_bass    = curr_bass

    return results


# ── Pattern classification ────────────────────────────────────────────────────

def pattern_key(e: dict) -> str:
    """
    Assign each error a canonical pattern label based on which temporal signals
    are active.  Signals are listed in descending specificity so that the label
    captures the richest context first.
    """
    parts = []

    # Stepwise context
    if e["sf"] and e["st"]:
        parts.append("sf+st")
    elif e["sf"]:
        parts.append("sf_only")
    elif e["st"]:
        parts.append("st_only")

    # Consecutive count (only noteworthy if >= 2)
    if e["cc"] >= 3:
        parts.append("cc>=3")
    elif e["cc"] == 2:
        parts.append("cc=2")

    # Root signals
    if e["nrm"]:
        parts.append("next_root=winner")
    if e["rcw"]:
        parts.append("recent_root=winner")

    return "+".join(parts) if parts else "no_signal"


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    ours_files = sorted(CORPUS_DIR.glob("*.ours.json"))
    print(f"Scanning {len(ours_files)} .ours.json files …")

    all_errors: list[dict] = []
    for f in ours_files:
        all_errors.extend(analyze_file(f))

    n_total = len(all_errors)
    print(f"Total genuine BIR=false errors found: {n_total}\n")

    # Split: errors with vs. without any active temporal signal
    with_signal    = [e for e in all_errors if pattern_key(e) != "no_signal"]
    without_signal = [e for e in all_errors if pattern_key(e) == "no_signal"]

    print(f"Errors with active temporal signals  : {len(with_signal)}"
          f"  (estimate of Iter-8-introduced errors)")
    print(f"Errors with NO temporal signal       : {len(without_signal)}"
          f"  (pre-existing errors unchanged by Iter 8)")
    print()

    # ── Pattern distribution across ALL errors ────────────────────────────
    all_counts = Counter(pattern_key(e) for e in all_errors)
    print("=" * 70)
    print(f"PATTERN DISTRIBUTION — all {n_total} genuine BIR=false errors")
    print("=" * 70)
    print(f"{'Pattern':<45}  {'Count':>5}  {'%':>6}")
    print("-" * 60)
    for pat, cnt in all_counts.most_common():
        pct = 100.0 * cnt / max(1, n_total)
        print(f"  {pat:<43}  {cnt:>5}  {pct:>6.1f}%")
    print()

    # ── Pattern distribution for temporally-active subset ────────────────
    n_ws = len(with_signal)
    ws_counts = Counter(pattern_key(e) for e in with_signal)
    print("=" * 70)
    print(f"PATTERN DISTRIBUTION — {n_ws} temporally-active errors")
    print("(most likely new from Iter 8 — at least one non-default signal)")
    print("=" * 70)
    print(f"{'Pattern':<45}  {'Count':>5}  {'%':>6}")
    print("-" * 60)
    for pat, cnt in ws_counts.most_common():
        pct = 100.0 * cnt / max(1, n_ws)
        print(f"  {pat:<43}  {cnt:>5}  {pct:>6.1f}%")
    print()

    # ── Top-3 pattern deep-dive ───────────────────────────────────────────
    top3_pats = [p for p, _ in ws_counts.most_common(3)]
    for rank, pat in enumerate(top3_pats, 1):
        subset = [e for e in with_signal if pattern_key(e) == pat]
        n_s    = len(subset)

        wq_ctr = Counter(e["winner_quality"] for e in subset)
        aq_ctr = Counter(e["alt_quality"]    for e in subset)
        cc_ctr = Counter(e["cc"]             for e in subset)
        sf_cnt = sum(1 for e in subset if e["sf"])
        st_cnt = sum(1 for e in subset if e["st"])
        nrm_cnt= sum(1 for e in subset if e["nrm"])
        rcw_cnt= sum(1 for e in subset if e["rcw"])

        print("=" * 70)
        print(f"RANK {rank}: Pattern '{pat}'  (n={n_s})")
        print("=" * 70)
        print(f"  (c) bassIsStepwiseFromPrevious = True : {sf_cnt:>4}  ({100*sf_cnt/n_s:.0f}%)")
        print(f"  (d) bassIsStepwiseToNext       = True : {st_cnt:>4}  ({100*st_cnt/n_s:.0f}%)")
        print(f"  (e) recentRootPcs has winner root     : {rcw_cnt:>4}  ({100*rcw_cnt/n_s:.0f}%)")
        print(f"  (f) consecutiveBassStepwiseCount dist : {dict(sorted(cc_ctr.items()))}")
        print(f"  (g) nextRootPc == winnerRootPc        : {nrm_cnt:>4}  ({100*nrm_cnt/n_s:.0f}%)")
        print()
        print(f"  (a) Winner quality (inversion we picked):")
        for q, c in wq_ctr.most_common(8):
            print(f"        {q:<20}  {c:>4}  ({100*c/n_s:.1f}%)")
        print(f"  (b) Alt quality (first alternative, typically root-pos):")
        for q, c in aq_ctr.most_common(8):
            print(f"        {q:<20}  {c:>4}  ({100*c/n_s:.1f}%)")
        print()


if __name__ == "__main__":
    main()
