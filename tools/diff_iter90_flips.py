#!/usr/bin/env python3
"""Compare pre-fix and post-fix corpus to enumerate all chord-identity flips."""
from __future__ import annotations
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

POST = _ROOT / "tools" / "corpus"  # current (with fix)
PRE  = Path("C:/tmp/pre_corpus")     # snapshot of pre-fix corpus

if not PRE.exists():
    print("PRE not found — copy current corpus first")
    sys.exit(1)

WIR = _ROOT / "tools" / "dcml" / "when_in_rome"

def load_pair(stem):
    o_post = POST / f"{stem}.ours.json"
    o_pre  = PRE / f"{stem}.ours.json"
    m21    = POST / f"{stem}.music21.json"
    if not (o_post.exists() and o_pre.exists() and m21.exists()):
        return None
    try:
        _, post_r = cmp.load_analysis(o_post)
        _, pre_r  = cmp.load_analysis(o_pre)
        _, m_r    = cmp.load_analysis(m21)
        return post_r, pre_r, m_r
    except Exception:
        return None

flip_correct = []      # was correct → still correct (no change in identity)
flip_to_correct = []   # was wrong → now correct
flip_to_wrong = []     # was correct → now wrong (REGRESSION)
flip_wrong_to_wrong = [] # was wrong → still wrong (just different)
n_unchanged_winner = 0
n_winner_changed = 0
n_processed = 0

for stem_path in sorted(POST.glob("*.ours.json")):
    stem = stem_path.stem.replace(".ours", "")
    data = load_pair(stem)
    if not data:
        continue
    post_r, pre_r, m_r = data
    n_processed += 1

    # Get WIR (ground truth)
    wir_path = dcml.find_wir_file(str(WIR), stem)
    wir_regs = []
    if wir_path:
        try: wir_regs = dcml.parse_rntxt_file(wir_path)
        except: pass

    # Align pre and post by tick
    pre_by_start = {r.start_tick: r for r in pre_r}

    # Align m21
    aligned_post = cmp.align_regions(post_r, m_r)
    wir_aligned = cmp.align_dcml_regions(post_r, wir_regs) if wir_regs else [None]*len(post_r)

    for i, (p, m) in enumerate(aligned_post):
        pre = pre_by_start.get(p.start_tick)
        if pre is None:
            continue
        if pre.root_pc == p.root_pc and pre.quality == p.quality:
            n_unchanged_winner += 1
            continue
        n_winner_changed += 1

        # Get ground truth
        m_pc = m.root_pc if m else None
        wir_pc = wir_aligned[i].root_pc if wir_regs and i < len(wir_aligned) and wir_aligned[i] else None

        # Truth: prefer wir, fallback music21
        truth = wir_pc if wir_pc is not None else m_pc
        if truth is None:
            continue

        was_right = (pre.root_pc == truth)
        now_right = (p.root_pc == truth)

        rec = (stem, p.measure_number, p.beat,
               f"{pre.chord_symbol}({pre.root_pc})",
               f"{p.chord_symbol}({p.root_pc})",
               f"truth={truth}")

        if was_right and now_right: flip_correct.append(rec)
        elif (not was_right) and now_right: flip_to_correct.append(rec)
        elif was_right and (not now_right): flip_to_wrong.append(rec)
        else: flip_wrong_to_wrong.append(rec)

print(f"Processed: {n_processed} chorales")
print(f"Total regions with changed winner: {n_winner_changed} (unchanged: {n_unchanged_winner})")
print()
print(f"Was right, still right (alts may differ):   {len(flip_correct)}")
print(f"Was wrong, now right (TARGETED FIXES):      {len(flip_to_correct)}")
print(f"Was right, now wrong (REGRESSIONS):         {len(flip_to_wrong)}")
print(f"Was wrong, still wrong (just different):    {len(flip_wrong_to_wrong)}")
print()
print(f"Net error change: {len(flip_to_wrong) - len(flip_to_correct):+d}")
print()
print("== TARGETED FIXES (was wrong, now right) ==")
for r in flip_to_correct[:30]:
    print(" ", r)
print(f"  ... ({len(flip_to_correct)} total)")
print()
print("== REGRESSIONS (was right, now wrong) ==")
for r in flip_to_wrong[:50]:
    print(" ", r)
print(f"  ... ({len(flip_to_wrong)} total)")
