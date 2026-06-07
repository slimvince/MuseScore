#!/usr/bin/env python3
"""
analyze_iter90_regressions.py — characterize NEW BIR=true regressions
introduced by the Iter 90 bass-as-root gate.

Compares current BIR=true=23 against the prior 4-case baseline; the 19 new
cases are the ones the gate flipped incorrectly. For each, dump enough
detail to find a structural discriminator.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _ROOT / "tools" / "corpus"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

PC = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]

# Prior 4 BIR=true cases from iter63_genuine6_characterization (deduced from baseline)
# Actually only 4 in current pre-Iter-90 baseline; we'll just dump all 23 now.

def main():
    ours_files = sorted(_CORPUS_DIR.glob("*.ours.json"))
    cases = []
    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        m21_path = _CORPUS_DIR / f"{stem}.music21.json"
        if not m21_path.exists():
            continue
        try:
            _, ours = cmp.load_analysis(ours_path)
            _, m21  = cmp.load_analysis(m21_path)
        except Exception:
            continue
        if not ours:
            continue
        wir_path = dcml.find_wir_file(str(_WIR_DIR), stem)
        wir_regs = []
        if wir_path:
            try: wir_regs = dcml.parse_rntxt_file(wir_path)
            except Exception: pass

        aligned = cmp.align_regions(ours, m21)
        wir_aligned = cmp.align_dcml_regions(ours, wir_regs) if wir_regs else [None]*len(ours)
        for i, (our_r, their_r) in enumerate(aligned):
            res = cmp.classify(our_r, their_r)
            if res.category != "chord_disagree":
                continue
            if not wir_regs or i >= len(wir_aligned):
                continue
            wir_r = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
            if cat != "music21_dcml_agree":
                continue
            if not our_r.bass_is_root:
                continue  # only BIR=true cases (the regressions)
            cases.append((stem, our_r, their_r, wir_r))

    print(f"BIR=true=  {len(cases)}  (was 4 pre-Iter-90, so ~19 new)\n")

    pcset_decode = lambda x: sorted([i for i in range(12) if x and x & (1<<i)])

    for idx, (stem, o, t, w) in enumerate(cases, 1):
        true_root = t.root_pc
        pcs_in = pcset_decode(o.pitch_class_set)
        pcs_str = "{" + ",".join(PC[p] for p in pcs_in) + "}"
        # Extract per-PC weights from tones if present in the JSON
        ours_path = _CORPUS_DIR / f"{stem}.ours.json"
        d = json.load(open(ours_path))
        region_data = None
        for r in d.get('regions', []):
            if r.get('startTick') == o.start_tick:
                region_data = r
                break
        weights = {}
        if region_data:
            for tn in region_data.get('tones', []):
                pc = tn['pitch'] % 12
                weights[pc] = weights.get(pc, 0) + tn.get('weight', 0)
        bass_w = weights.get(o.bass_pc or -1, 0.0)
        bass_pc_name = PC[o.bass_pc] if o.bass_pc is not None else "?"
        true_root_name = PC[true_root]
        our_root_name  = PC[o.root_pc]
        # Identify the gate's pattern: A (Minor, delta=4) or B (Major, delta=3)?
        # Pre-flip winner was different (we don't know it without prior data).
        # Just dump the post-flip winner here.
        print(f"[{idx:2d}] {stem:<14} m={o.measure_number:3d} b={o.beat:.2f}  "
              f"winner={o.chord_symbol:<14} (root={our_root_name} bass={bass_pc_name} q={o.quality})  "
              f"true_root={true_root_name}  pcs={pcs_str}")
        print(f"     bassWeight={bass_w:.2f}  noteCount={o.note_count}  margin={o.chord_score_margin or 0:.3f}  "
              f"key={o.key} keyConf={o.key_confidence:.2f}  diatonic={o.diatonic_to_key}")
        # Show bass:root pcWeights ratio — useful for guard design
        root_w = weights.get(o.root_pc, 0.0)
        true_w = weights.get(true_root, 0.0)
        print(f"     pcWeights: ourRoot({our_root_name})={root_w:.2f}  bass({bass_pc_name})={bass_w:.2f}  "
              f"trueRoot({true_root_name})={true_w:.2f}")
        # Alts
        alts = o.alternatives or []
        print(f"     alts ({len(alts)}):")
        for a in alts[:3]:
            print(f"       {a.get('chordSymbol','?'):<14} root={a.get('rootPitchClass','?')} "
                  f"bass={a.get('bassPitchClass','?')} q={a.get('quality','?')} "
                  f"score={a.get('score','?')}")
        print()

if __name__ == "__main__":
    main()
