"""
diag_iter54_alts_full.py — Dump full alternatives list for each genuine-14 case.

Checks whether HalfDim/Diminished alts at correct (agreed) root are present
or absent in results[].
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import compare_analyses as cmp
import dcml_parser as dcml

_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"

_PC = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def main() -> None:
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
                continue
            if not wir_regions or i >= len(wir_aligned):
                continue
            wir_r = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            their_pc = their_r.root_pc if their_r else None
            cat = cmp.three_way_classify(our_r.root_pc, their_pc, wir_pc)
            if cat != "music21_dcml_agree":
                continue

            agreed = _PC[wir_pc] if wir_pc is not None else "?"
            print(f"\n=== {stem}  m={our_r.measure_number}  b={our_r.beat}  "
                  f"agreed_root={agreed} (pc={wir_pc}) ===")
            print(f"  winner: {our_r.quality} root={_PC[our_r.root_pc]} "
                  f"bass={_PC[our_r.bass_pc]} score={our_r.chord_score:.4f}")
            for ai, alt in enumerate(our_r.alternatives or []):
                ar = alt.get("rootPitchClass", -1)
                ab = alt.get("bassPitchClass", -1)
                tag = " <- AGREED ROOT" if ar == wir_pc else ""
                print(f"  alt[{ai}]: {alt.get('quality')} "
                      f"root={_PC[ar] if 0 <= ar < 12 else '?'} "
                      f"bass={_PC[ab] if 0 <= ab < 12 else '?'} "
                      f"BIR={alt.get('bassIsRoot')} "
                      f"score={alt.get('score', 0):.4f}{tag}")


if __name__ == "__main__":
    main()
