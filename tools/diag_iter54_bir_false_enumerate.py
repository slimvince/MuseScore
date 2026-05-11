"""
diag_iter54_bir_false_enumerate.py — Enumerate all three-way genuine BIR=false cases.

Diagnostic only. Run from repo root.
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


def main() -> None:
    cases: list[tuple[str, cmp.Region, int]] = []

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
            if our_r.bass_is_root:
                continue  # only BIR=false
            if not wir_regions or i >= len(wir_aligned):
                continue
            wir_r = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            their_pc = their_r.root_pc if their_r else None
            cat = cmp.three_way_classify(our_r.root_pc, their_pc, wir_pc)
            if cat != "music21_dcml_agree":
                continue
            cases.append((stem, our_r, wir_pc if wir_pc is not None else -1))

    print(f"Genuine BIR=false (three-way) total: {len(cases)}\n")
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


if __name__ == "__main__":
    main()
