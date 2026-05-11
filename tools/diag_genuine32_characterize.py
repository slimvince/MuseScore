"""
diag_genuine32_characterize.py — Cross-reference the genuine-32 BIR=true set
against known investigation groups.

Diagnostic only. Run from the repo root.
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

GROUPS = {
    "Gate M":          {"bwv187.7", "bwv227.11", "bwv278", "bwv301", "bwv302",
                        "bwv40.6", "bwv423", "bwv85.6"},
    "Gate N":          {"bwv123.6", "bwv322", "bwv337", "bwv392", "bwv417",
                        "bwv425"},
    "TYPE-B residual": {"bwv288", "bwv309", "bwv331"},
    "MinMaj7":         {"bwv20.11", "bwv40.3", "bwv64.8"},
}


def classify_stem(stem: str) -> str:
    for label, members in GROUPS.items():
        if stem in members:
            return label
    return "UNCHARACTERIZED"


def main() -> None:
    genuine: list[tuple[str, cmp.Region]] = []

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
            genuine.append((stem, our_r))

    print(f"Genuine BIR=true (three-way) total: {len(genuine)}\n")

    # ── Summary table ────────────────────────────────────────────────────
    by_group: dict[str, list[tuple[str, cmp.Region]]] = {
        "Gate M": [], "Gate N": [], "TYPE-B residual": [], "MinMaj7": [],
        "UNCHARACTERIZED": [],
    }
    print(f"{'#':>3}  {'stem':<14} {'m':>3} {'b':>5}  {'q':<14} "
          f"{'root':>4} {'bass':>4} {'BIR':>5} {'score':>7} {'margin':>7}  group")
    print("-" * 96)
    for idx, (stem, r) in enumerate(genuine, 1):
        group = classify_stem(stem)
        by_group[group].append((stem, r))
        score = f"{r.chord_score:.4f}" if r.chord_score is not None else "?"
        margin = f"{r.chord_score_margin:.4f}" if r.chord_score_margin is not None else "?"
        print(f"{idx:>3}  {stem:<14} {r.measure_number:>3} {r.beat:>5.2f}  "
              f"{r.quality:<14} {r.root_pc:>4} {r.bass_pc:>4} "
              f"{str(r.bass_is_root):>5} {score:>7} {margin:>7}  {group}")

    print()
    for group, items in by_group.items():
        print(f"  {group:<20} {len(items)}")
    print()

    # ── Detail dump for UNCHARACTERIZED ─────────────────────────────────
    unchar = by_group["UNCHARACTERIZED"]
    if not unchar:
        print("All entries accounted for — no UNCHARACTERIZED cases.")
        return

    print("=" * 96)
    print(f"UNCHARACTERIZED cases ({len(unchar)}):")
    print("=" * 96)
    for stem, r in unchar:
        score = r.chord_score if r.chord_score is not None else float("nan")
        margin = r.chord_score_margin if r.chord_score_margin is not None else float("nan")
        print(f"\n--- {stem}  m={r.measure_number} b={r.beat}  ---")
        print(f"  winner: quality={r.quality} rootPc={r.root_pc} "
              f"bassPc={r.bass_pc} bassIsRoot={r.bass_is_root} "
              f"score={score:.4f} margin={margin:.4f}")
        print(f"  symbol={r.chord_symbol!r}  noteCount={r.note_count}")
        for ai, alt in enumerate(r.alternatives[:2]):
            alt_score = alt.get("score", 0.0)
            print(f"  alt[{ai}]: quality={alt.get('quality')} "
                  f"rootPc={alt.get('rootPitchClass')} "
                  f"bassPc={alt.get('bassPitchClass')} "
                  f"bassIsRoot={alt.get('bassIsRoot')} "
                  f"score={alt_score:.4f} "
                  f"chordSymbol={alt.get('chordSymbol', '')!r}")


if __name__ == "__main__":
    main()
