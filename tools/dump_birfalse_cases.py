"""Dump three-way genuine BIR=false cases for diff against a baseline.

Same accumulation logic as analyze_inversion_errors.py but emits a stable, sorted
list of identifying tuples (score, start_tick, our_root, our_quality, their_root,
their_quality) so two runs can be diff'd to isolate regressions.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import compare_analyses as cmp  # noqa: E402
import dcml_parser as dcml  # noqa: E402

_CORPUS_DIR = Path(__file__).resolve().parent / "corpus"
_WIR_DIR    = Path(__file__).resolve().parent / "dcml" / "when_in_rome"


def main() -> None:
    rows = []
    for ours_path in sorted(_CORPUS_DIR.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        music21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not music21_path.exists():
            continue
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions  = cmp.load_analysis(music21_path)
        except Exception:
            continue
        if not ours_regions:
            continue

        aligned = cmp.align_regions(ours_regions, m21_regions)
        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        if not wir_path:
            continue
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions)

        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != "chord_disagree":
                continue
            if our_r.bass_is_root:
                continue
            if i >= len(wir_aligned):
                continue
            wir_r = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat = cmp.three_way_classify(
                our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
            if cat != "music21_dcml_agree":
                continue

            their_root_pc = their_r.root_pc if their_r else None
            their_q = their_r.quality if their_r else "?"
            rows.append((
                stem,
                getattr(our_r, "start_tick", -1),
                our_r.root_pc,
                our_r.quality,
                getattr(our_r, "bass_pc", -1),
                their_root_pc,
                their_q,
                wir_pc,
            ))

    rows.sort()
    for r in rows:
        print("\t".join(str(x) for x in r))
    print(f"# total={len(rows)}")


if __name__ == "__main__":
    main()
