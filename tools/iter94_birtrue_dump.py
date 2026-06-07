#!/usr/bin/env python3
"""Emit a stable list of all Jazz BIR=true cases as tab-separated rows for
diffing across binary versions.  Key = (stem, start_tick).
"""
from __future__ import annotations
import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
_ROOT = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"
sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as _dcml

PC = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]
def pcs(p): return PC[p%12] if p is not None else "?"

def main():
    rows = []
    for ours_path in sorted(_CORPUS_DIR.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours","")
        m21p = _CORPUS_DIR / f"{stem}.music21.json"
        if not m21p.exists(): continue
        try:
            with open(ours_path,encoding="utf-8") as fh:
                raw = json.load(fh)
            if raw.get("preset","").lower() != "jazz": continue
            _, ours = cmp.load_analysis(ours_path)
            _, m21 = cmp.load_analysis(m21p)
        except Exception:
            continue
        if not ours: continue
        aligned = cmp.align_regions(ours, m21)
        wirp = _dcml.find_wir_file(str(_WIR_DIR), stem)
        wir = []
        if wirp:
            try: wir = _dcml.parse_rntxt_file(wirp)
            except Exception: pass
        if not wir: continue
        wal = cmp.align_dcml_regions(ours, wir)
        rgns = raw.get("regions", [])
        for i,(our_r, their_r) in enumerate(aligned):
            res = cmp.classify(our_r, their_r)
            if res.category != "chord_disagree": continue
            if not our_r.bass_is_root: continue
            if i >= len(wal): continue
            wr = wal[i]
            if wr is None or wr.root_pc is None: continue
            cat = cmp.three_way_classify(our_r.root_pc,
                                          their_r.root_pc if their_r else None,
                                          wr.root_pc)
            if cat != "music21_dcml_agree": continue
            if i >= len(rgns): continue
            r = rgns[i]
            prev_bass = rgns[i-1].get("bassPitchClass") if i>0 else -1
            next_bass = rgns[i+1].get("bassPitchClass") if i+1<len(rgns) else -1
            rows.append((
                stem,
                r.get("startTick", -1),
                r.get("measureNumber", -1),
                r.get("beat", 0.0),
                pcs(r.get("rootPitchClass")),
                r.get("quality","?"),
                pcs(r.get("bassPitchClass")),
                r.get("chordSymbol","?"),
                pcs(wr.root_pc),
                wr.chord_symbol or "?",
                pcs(prev_bass) if prev_bass>=0 else "-",
                pcs(next_bass) if next_bass>=0 else "-",
                f"{r.get('chordScore',0):.4f}",
            ))
    rows.sort()
    print("# stem\tstart_tick\tmeasure\tbeat\twinner_root\tquality\tbass\tsymbol\tdcml_root\tdcml_symbol\tprev_bass\tnext_bass\tscore")
    for row in rows:
        print("\t".join(str(c) for c in row))
    print(f"# TOTAL\t{len(rows)}")

if __name__ == "__main__":
    main()
