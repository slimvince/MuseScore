#!/usr/bin/env python3
"""
analyze_wrong_root_iter90.py — R5 Group (b) characterization.

Reconstruct wrong-root patterns in the genuine BIR=false=118 baseline.
Group cases by:
  - root offset (semitones: theirs_root - ours_root, mod 12)
  - our quality / their quality
  - bass relation to true root
  - whether true root is present in our pcWeight

Goal: identify dominant failure patterns and suggest the highest-yield
safe targeted fix.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

PC_NAMES = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]


def _infer_quality(sym: str) -> str:
    if not sym:
        return ""
    s = sym.split('/')[0]
    m = re.match(r'^[A-G][#b]?', s)
    if not m:
        return ""
    body = s[m.end():]
    if 'dim7' in body or '°7' in body:
        return "Diminished7"
    if body.startswith('ø') or 'm7b5' in body.lower():
        return "HalfDiminished"
    if 'maj7' in body.lower() or body.startswith('M7'):
        return "Major7"
    if body.startswith('m7') or body.startswith('min7'):
        return "Minor7"
    if body.startswith('7'):
        return "Dominant7"
    if 'dim' in body.lower() or '°' in body:
        return "Diminished"
    if body.startswith('m') or body.startswith('min'):
        return "Minor"
    if 'sus' in body.lower():
        return "Suspended"
    return "Major"


def _root_present_in_alts(alts, target_root_pc):
    """Check whether the target root_pc appears as the root of any alternative."""
    for alt in alts or []:
        sym = alt.get("chordSymbol", "")
        # Try structured fields first
        rp = alt.get("rootPitchClass")
        if rp is not None and rp == target_root_pc:
            return True
    return False


def _parse_pc_set(pc_set_int):
    """Decode bitmap pcSet into a set of PCs."""
    if pc_set_int is None:
        return set()
    return {i for i in range(12) if pc_set_int & (1 << i)}


def main():
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))
    print(f"Found {len(ours_files)} corpus files")

    # Collect genuine wrong-root cases (BIR=false dominant)
    cases = []
    processed = 0

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

        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        wir_regions = []
        if wir_path:
            try:
                wir_regions = dcml.parse_rntxt_file(wir_path)
            except Exception:
                pass

        aligned     = cmp.align_regions(ours_regions, m21_regions)
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None]*len(ours_regions)
        processed  += 1

        for i, (our_r, their_r) in enumerate(aligned):
            res = cmp.classify(our_r, their_r)
            if res.category != "chord_disagree":
                continue
            if not wir_regions or i >= len(wir_aligned):
                continue
            wir_r  = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat    = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
            if cat != "music21_dcml_agree":
                continue

            true_root = their_r.root_pc  # = wir_pc, both agree
            our_root  = our_r.root_pc
            our_bass  = our_r.bass_pc if our_r.bass_pc is not None else our_root

            offset = (true_root - our_root) % 12
            bass_to_true = (our_bass - true_root) % 12
            true_in_pcs = (true_root in _parse_pc_set(our_r.pitch_class_set))
            true_in_alts = _root_present_in_alts(our_r.alternatives, true_root)

            their_q = _infer_quality(their_r.chord_symbol)

            cases.append({
                "stem": stem,
                "m": our_r.measure_number,
                "b": our_r.beat,
                "our_root": our_root,
                "our_quality": our_r.quality,
                "our_bass": our_bass,
                "our_sym": our_r.chord_symbol,
                "true_root": true_root,
                "their_q": their_q,
                "their_sym": their_r.chord_symbol,
                "offset": offset,
                "bass_to_true": bass_to_true,
                "true_in_pcs": true_in_pcs,
                "true_in_alts": true_in_alts,
                "margin": our_r.chord_score_margin or 0.0,
                "score": our_r.chord_score or 0.0,
                "noteCount": our_r.note_count or 0,
                "pcSet": our_r.pitch_class_set,
                "bir": our_r.bass_is_root,
                "alts": our_r.alternatives,
            })

    n = len(cases)
    print(f"\nProcessed {processed} chorales -> {n} genuine wrong-root cases (chord_disagree, music21+DCML agree)")

    # ── 1. Root-offset distribution ──
    offset_counts = Counter(c["offset"] for c in cases)
    print("\n── Root-offset distribution (true_root - our_root mod 12) ──")
    interval_names = {
        0: "same root (quality-only diff)",
        1: "true=our+1 (semitone up)",
        2: "true=our+2 (whole-tone up)",
        3: "true=our+3 (m3 up)",
        4: "true=our+4 (M3 up)  [our root could be 3rd of true]",
        5: "true=our+5 (P4 up)  [our root could be 5th of true]",
        6: "true=our+6 (tritone)",
        7: "true=our+7 (P5 up)  [our root could be 4th of true]",
        8: "true=our+8 (m6 up)  [our root could be 3rd above true root - i.e. true is m3 below us]",
        9: "true=our+9 (M6 up)  [our root could be 3rd of true (true is m3 below)]",
        10: "true=our+10 (m7 up) [our root could be b7 of true]",
        11: "true=our+11 (M7 up) [our root could be 7th of true]",
    }
    for off in range(12):
        cnt = offset_counts.get(off, 0)
        if cnt == 0:
            continue
        bar = "█" * (cnt * 40 // max(1, n))
        print(f"  +{off:2d}  {cnt:4d}  {bar}  {interval_names[off]}")

    # ── 2. Our-quality / their-quality combinations ──
    qq = Counter((c["our_quality"], c["their_q"]) for c in cases)
    print("\n── (our_quality, their_quality) combinations (top 20) ──")
    for (oq, tq), cnt in qq.most_common(20):
        print(f"  {oq:<18} -> {tq:<18}  {cnt:4d}")

    # ── 3. By offset, show top quality combinations ──
    print("\n── Per-offset quality combinations ──")
    for off in sorted(offset_counts.keys(), key=lambda o: -offset_counts[o]):
        if offset_counts[off] < 3:
            continue
        sub = [c for c in cases if c["offset"] == off]
        qcomb = Counter((c["our_quality"], c["their_q"]) for c in sub)
        print(f"\n  offset=+{off}  (n={len(sub)})")
        for (oq, tq), cnt in qcomb.most_common(8):
            print(f"    {oq:<18} -> {tq:<18}  {cnt:4d}")

    # ── 4. True-root presence in our pcWeight (key for any bonus gate) ──
    in_pcs = sum(1 for c in cases if c["true_in_pcs"])
    in_alts = sum(1 for c in cases if c["true_in_alts"])
    print(f"\n── True-root visibility ──")
    print(f"  True root present in our pcSet:           {in_pcs}/{n} ({100*in_pcs/n:.1f}%)")
    print(f"  True root present in our alternatives[]:  {in_alts}/{n} ({100*in_alts/n:.1f}%)")

    # ── 5. Bass relationship to true root ──
    btt = Counter(c["bass_to_true"] for c in cases)
    print("\n── (our_bass - true_root) mod 12 ──")
    bass_relation_names = {
        0:  "bass IS true root (P1)",
        2:  "bass is 9th/2nd of true",
        3:  "bass is m3 of true",
        4:  "bass is M3 of true",
        5:  "bass is 4th of true",
        6:  "bass is tritone of true",
        7:  "bass is 5th of true",
        8:  "bass is #5/b6 of true",
        9:  "bass is 6th of true",
        10: "bass is b7 of true",
        11: "bass is 7th of true",
        1:  "bass is b9 of true",
    }
    for off in range(12):
        cnt = btt.get(off, 0)
        if cnt == 0:
            continue
        bar = "█" * (cnt * 40 // max(1, n))
        print(f"  bass-to-true=+{off:2d}  {cnt:4d}  {bar}  {bass_relation_names.get(off,'?')}")

    # ── 6. The "true root is the bass" pattern — mis-rooted slash chord ──
    # For these cases, our root_pc != true_root, but the bass IS the true root.
    # If the true_root is present in pcSet but we still mis-rooted the chord,
    # this is a strong fix candidate (a slash-chord upgrade).
    bass_is_true = [c for c in cases if c["bass_to_true"] == 0]
    print(f"\n── 'Bass is true root' subset: {len(bass_is_true)}/{n} ──")
    bs_qcomb = Counter((c["our_quality"], c["their_q"]) for c in bass_is_true)
    for (oq, tq), cnt in bs_qcomb.most_common(15):
        print(f"  {oq:<18} -> {tq:<18}  {cnt:4d}")
    bs_with_alt = sum(1 for c in bass_is_true if c["true_in_alts"])
    print(f"  Of these, true root appears in our alternatives[]:  {bs_with_alt}/{len(bass_is_true)}")

    # ── 7. Margin distribution by group ──
    print("\n── Margin distribution overall ──")
    m_lt_010 = sum(1 for c in cases if c["margin"] < 0.10)
    m_lt_025 = sum(1 for c in cases if c["margin"] < 0.25)
    m_lt_050 = sum(1 for c in cases if c["margin"] < 0.50)
    m_lt_100 = sum(1 for c in cases if c["margin"] < 1.00)
    print(f"  margin < 0.10:  {m_lt_010}/{n}  ({100*m_lt_010/n:.1f}%)")
    print(f"  margin < 0.25:  {m_lt_025}/{n}  ({100*m_lt_025/n:.1f}%)")
    print(f"  margin < 0.50:  {m_lt_050}/{n}  ({100*m_lt_050/n:.1f}%)")
    print(f"  margin < 1.00:  {m_lt_100}/{n}  ({100*m_lt_100/n:.1f}%)")

    # ── 8. Save full enumeration ──
    out_path = _ROOT / "tools" / "iter90_wrong_root_characterization.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"=== Iter 90 — wrong-root characterization (R5 Group (b)) ===\n")
        fh.write(f"Baseline: BIR=false={n}\n\n")
        fh.write(f"  #  stem             m     b   our                         true                       offset  bass-to-true  margin   alts_have_true\n")
        fh.write("-" * 130 + "\n")
        for i, c in enumerate(cases, 1):
            fh.write(f"  {i:3d}  {c['stem']:<14}  {c['m']:3d}  {c['b']:5.2f}  "
                     f"{c['our_sym']:<22} ({c['our_quality']:<14})  "
                     f"-> {c['their_sym']:<18} ({c['their_q']:<14})  "
                     f"+{c['offset']:2d}  +{c['bass_to_true']:2d}  "
                     f"{c['margin']:6.3f}  {'Y' if c['true_in_alts'] else 'N'}\n")
    print(f"\nFull enumeration written to {out_path}")

    # ── 9. The "offset+5 / bass=true_root" subset — almost surely a missed inversion ──
    # If true_root = our_root + 5 AND bass IS true_root, our root is the 5th and the bass
    # is the actual root. That's a confused root-position-vs-1st-inversion case where the
    # winner has the wrong root entirely.
    off5_bass_true = [c for c in cases if c["offset"] == 5 and c["bass_to_true"] == 0]
    print(f"\n── 'offset=+5 AND bass IS true root' subset: {len(off5_bass_true)} ──")
    for c in off5_bass_true[:10]:
        print(f"  {c['stem']} m={c['m']} b={c['b']}  {c['our_sym']} -> {c['their_sym']}  margin={c['margin']:.3f}")

    # ── 10. The "offset+9 / bass=true_root" subset (true is m3 below; our root is the 3rd) ──
    off9_bass_true = [c for c in cases if c["offset"] == 9 and c["bass_to_true"] == 0]
    print(f"\n── 'offset=+9 AND bass IS true root' subset: {len(off9_bass_true)} ──")
    for c in off9_bass_true[:10]:
        print(f"  {c['stem']} m={c['m']} b={c['b']}  {c['our_sym']} -> {c['their_sym']}  margin={c['margin']:.3f}")

    # ── 11. Note count distribution by group (sparse vs dense) ──
    print("\n── Note count distribution overall ──")
    nc = Counter(c["noteCount"] for c in cases)
    for k in sorted(nc.keys()):
        print(f"  noteCount={k}: {nc[k]}")


if __name__ == "__main__":
    main()
