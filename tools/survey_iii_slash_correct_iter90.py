#!/usr/bin/env python3
"""
Survey iii-slash-chord patterns where our analysis is CORRECT.

For each region in the corpus, find cases where:
  - our quality is Minor and our bass = (our_root - 4) mod 12  (Pattern A: Em/C)
  - our quality is Major and our bass = (our_root - 3) mod 12  (Pattern B: C/A)

Then count:
  (a) ground truth (music21+DCML) AGREES with our root → CORRECT iii-slash
  (b) ground truth disagrees, true root = bass → wrong-root case (the 55 we want to fix)
  (c) ground truth disagrees, true root != bass → some other failure

(a) counts the regressions we'd introduce by flipping all such cases.
(b) counts the targeted fixes.
"""
from __future__ import annotations
import sys, json
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import compare_analyses as cmp
import dcml_parser as dcml

_CORPUS = _ROOT / "tools" / "corpus"
_WIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

def main():
    counts = {
        "A_correct": 0, "A_wrong_root_bass": 0, "A_other": 0,
        "B_correct": 0, "B_wrong_root_bass": 0, "B_other": 0,
        "total_A": 0, "total_B": 0,
    }
    correct_cases_A = []  # (Em/C cases where iii is right per ground truth)
    correct_cases_B = []

    for ours_path in sorted(_CORPUS.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        m21_path = _CORPUS / f"{stem}.music21.json"
        if not m21_path.exists():
            continue
        try:
            _, ours = cmp.load_analysis(ours_path)
            _, m21  = cmp.load_analysis(m21_path)
        except Exception:
            continue
        if not ours:
            continue
        wir_path = dcml.find_wir_file(str(_WIR), stem)
        wir_regs = []
        if wir_path:
            try: wir_regs = dcml.parse_rntxt_file(wir_path)
            except Exception: pass

        aligned = cmp.align_regions(ours, m21)
        wir_aligned = cmp.align_dcml_regions(ours, wir_regs) if wir_regs else [None]*len(ours)

        for i, (our_r, their_r) in enumerate(aligned):
            if our_r.bass_pc is None:
                continue
            if our_r.bass_pc == our_r.root_pc:
                continue  # not a slash chord
            delta = (our_r.root_pc - our_r.bass_pc + 12) % 12
            if our_r.quality == "Minor" and delta == 4:
                pattern = "A"
            elif our_r.quality == "Major" and delta == 3:
                pattern = "B"
            else:
                continue
            counts[f"total_{pattern}"] += 1

            # Ground truth: prefer music21+DCML three-way agreement
            their_pc = their_r.root_pc if their_r else None
            wir_pc = None
            if wir_regs and i < len(wir_aligned) and wir_aligned[i]:
                wir_pc = wir_aligned[i].root_pc

            # CORRECT if either (their_pc agrees with our root) AND (wir agrees with our root or wir_pc is None)
            # For safety, require BOTH music21 and (DCML or no DCML coverage) to agree.
            if their_pc == our_r.root_pc and (wir_pc is None or wir_pc == our_r.root_pc):
                counts[f"{pattern}_correct"] += 1
                correct_cases = correct_cases_A if pattern == "A" else correct_cases_B
                if len(correct_cases) < 30:
                    correct_cases.append((stem, our_r.measure_number, our_r.beat,
                                          our_r.chord_symbol, their_pc, wir_pc))
            elif their_pc is not None and wir_pc is not None and their_pc == wir_pc and their_pc == our_r.bass_pc:
                counts[f"{pattern}_wrong_root_bass"] += 1
            else:
                counts[f"{pattern}_other"] += 1

    print(f"Pattern A (Minor with bass M3 below root, e.g. Em/C):")
    print(f"  Total occurrences:                              {counts['total_A']}")
    print(f"  CORRECT (m21 agrees with our root):             {counts['A_correct']}")
    print(f"  WRONG-ROOT, true root IS bass (Iter 90 target): {counts['A_wrong_root_bass']}")
    print(f"  Other (other disagreement):                     {counts['A_other']}")
    print()
    print(f"Pattern B (Major with bass m3 below root, e.g. C/A):")
    print(f"  Total occurrences:                              {counts['total_B']}")
    print(f"  CORRECT (m21 agrees with our root):             {counts['B_correct']}")
    print(f"  WRONG-ROOT, true root IS bass (Iter 90 target): {counts['B_wrong_root_bass']}")
    print(f"  Other (other disagreement):                     {counts['B_other']}")
    print()
    print(f"Net effect of unconditional flip:")
    print(f"  Pattern A: -{counts['A_wrong_root_bass']} BIR=false errors, +{counts['A_correct']} regressions")
    print(f"  Pattern B: -{counts['B_wrong_root_bass']} BIR=false errors, +{counts['B_correct']} regressions")
    net = (counts['A_wrong_root_bass'] + counts['B_wrong_root_bass'] -
           counts['A_correct'] - counts['B_correct'])
    print(f"  Net: {net:+d} (positive means improvement)")
    print()
    print(f"Sample CORRECT-A cases (would regress if flipped):")
    for c in correct_cases_A[:15]:
        print(f"  {c}")
    print(f"Sample CORRECT-B cases (would regress if flipped):")
    for c in correct_cases_B[:15]:
        print(f"  {c}")

if __name__ == "__main__":
    main()
