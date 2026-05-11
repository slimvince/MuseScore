"""
diag_iter63_genuine6_enumerate.py — Enumerate and characterize the
current BIR=true genuine cases (three-way music21+DCML agreement).

Diagnostic only. Reads tools/corpus/*.ours.json + dcml WiR.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import compare_analyses as cmp
import dcml_parser as dcml

_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"


def _find_region(data, meas, beat):
    for r in data.get("regions", []):
        if r.get("measureNumber") == meas and abs(r.get("beat", 0) - beat) < 0.05:
            return r
    return None


def main() -> None:
    cases = []  # list of (stem, our_r, agreed_pc)

    for ours_path in sorted(_CORPUS_DIR.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        m21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not m21_path.exists():
            continue
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions = cmp.load_analysis(m21_path)
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
            if not our_r.bass_is_root:
                continue  # only BIR=true
            if not wir_regions or i >= len(wir_aligned):
                continue
            wir_r = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            their_pc = their_r.root_pc if their_r else None
            cat = cmp.three_way_classify(our_r.root_pc, their_pc, wir_pc)
            if cat != "music21_dcml_agree":
                continue
            cases.append((stem, our_r, wir_pc if wir_pc is not None else -1))

    print(f"Genuine BIR=true (three-way) total: {len(cases)}\n")
    print(f"{'#':>3}  {'stem':<14} {'m':>3} {'b':>5}  {'q':<14} "
          f"{'r':>3} {'b_pc':>4} {'BIR':>5} {'agreed':>6} "
          f"{'score':>7} {'margin':>7}")
    print("-" * 90)
    for idx, (stem, r, agreed_pc) in enumerate(cases, 1):
        score = f"{r.chord_score:.4f}" if r.chord_score is not None else "?"
        margin = f"{r.chord_score_margin:.4f}" if r.chord_score_margin is not None else "?"
        print(f"{idx:>3}  {stem:<14} {r.measure_number:>3} {r.beat:>5.2f}  "
              f"{r.quality:<14} {r.root_pc:>3} {r.bass_pc:>4} "
              f"{str(r.bass_is_root):>5} {agreed_pc:>6} {score:>7} {margin:>7}")

    # Detailed dump per case
    print("\n" + "=" * 90)
    print("Detailed per-case dump")
    print("=" * 90)
    for idx, (stem, our_r, agreed_pc) in enumerate(cases, 1):
        fpath = _CORPUS_DIR / f"{stem}.ours.json"
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"\n[{idx}] {stem}: failed to read ours.json: {e}")
            continue
        meas, beat = our_r.measure_number, our_r.beat
        r = _find_region(data, meas, beat)
        if not r:
            print(f"\n[{idx}] {stem} m={meas} b={beat}: region not found in JSON")
            continue
        print(f"\n[{idx}] === {stem} m={meas} b={beat:.2f} ===")
        print(f"  agreed root pc: {agreed_pc}")
        print(f"  winner: root={r.get('rootPitchClass')} qual={r.get('quality')!r} "
              f"score={r.get('chordScore', 0):.4f} "
              f"bass={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')}")
        print(f"  pcSet: {r.get('pitchClassSet')}  "
              f"noteCount={r.get('noteCount')}  "
              f"dur={r.get('endTick', 0) - r.get('startTick', 0)} ticks  "
              f"sym={r.get('chordSymbol')!r}")
        print(f"  pcMaskBitfield: {r.get('pitchClassMaskBitfield')}")
        alts = r.get("alternatives", []) or []
        for j, a in enumerate(alts[:3]):
            print(f"  alt[{j}]: root={a.get('rootPitchClass')} "
                  f"qual={a.get('quality')!r} score={a.get('score', 0):.4f} "
                  f"bass={a.get('bassPitchClass')} bassIsRoot={a.get('bassIsRoot')} "
                  f"sym={a.get('chordSymbol')!r}")
        # Find any alt with root == agreed_pc
        agreed_alt = next((a for a in alts if a.get("rootPitchClass") == agreed_pc), None)
        if agreed_alt:
            print(f"  agreed-root alt FOUND: qual={agreed_alt.get('quality')!r} "
                  f"score={agreed_alt.get('score', 0):.4f} "
                  f"bass={agreed_alt.get('bassPitchClass')} "
                  f"bassIsRoot={agreed_alt.get('bassIsRoot')}")
        else:
            print(f"  agreed-root alt: NOT in alternatives")
        # Neighbours
        regions = data.get("regions", [])
        try:
            ridx = next(k for k, rr in enumerate(regions)
                        if rr.get("measureNumber") == meas
                        and abs(rr.get("beat", 0) - beat) < 0.05)
        except StopIteration:
            ridx = -1
        if ridx >= 0:
            for nb in regions[max(0, ridx - 2):ridx + 3]:
                if nb is r:
                    continue
                print(f"  nb: m={nb.get('measureNumber')} b={nb.get('beat', 0):.2f} "
                      f"root={nb.get('rootPitchClass')} qual={nb.get('quality')!r} "
                      f"dur={nb.get('endTick', 0) - nb.get('startTick', 0)} "
                      f"pcs={nb.get('pitchClassSet')}")


if __name__ == "__main__":
    main()
