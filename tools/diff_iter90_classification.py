#!/usr/bin/env python3
"""Compare pre-fix vs post-fix region classifications (full + near agree)."""
from __future__ import annotations
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

POST = _ROOT / "tools" / "corpus"
PRE  = Path("C:/tmp/pre_corpus")
WIR  = _ROOT / "tools" / "dcml" / "when_in_rome"

both = []
for stem_path in sorted(POST.glob("*.ours.json")):
    stem = stem_path.stem.replace(".ours", "")
    o_post = POST / f"{stem}.ours.json"
    o_pre  = PRE / f"{stem}.ours.json"
    m21    = POST / f"{stem}.music21.json"
    if not (o_post.exists() and o_pre.exists() and m21.exists()):
        continue
    try:
        _, post_r = cmp.load_analysis(o_post)
        _, pre_r  = cmp.load_analysis(o_pre)
        _, m_r    = cmp.load_analysis(m21)
    except Exception:
        continue

    wir_path = dcml.find_wir_file(str(WIR), stem)
    wir_regs = []
    if wir_path:
        try: wir_regs = dcml.parse_rntxt_file(wir_path)
        except: pass

    aligned_post = cmp.align_regions(post_r, m_r)
    aligned_pre  = cmp.align_regions(pre_r,  m_r)
    wir_post     = cmp.align_dcml_regions(post_r, wir_regs) if wir_regs else [None]*len(post_r)
    wir_pre      = cmp.align_dcml_regions(pre_r,  wir_regs) if wir_regs else [None]*len(pre_r)

    # Index pre by tick
    pre_idx = {r.start_tick: i for i, r in enumerate(pre_r)}

    for i_post, (p, m) in enumerate(aligned_post):
        i_pre = pre_idx.get(p.start_tick)
        if i_pre is None:
            continue
        if i_pre >= len(aligned_pre):
            continue
        pre_p, pre_m = aligned_pre[i_pre]

        post_cat = cmp.classify(p, m).category
        pre_cat  = cmp.classify(pre_p, pre_m).category

        # Three-way category
        wir_post_pc = wir_post[i_post].root_pc if wir_regs and i_post < len(wir_post) and wir_post[i_post] else None
        wir_pre_pc  = wir_pre[i_pre].root_pc   if wir_regs and i_pre  < len(wir_pre)  and wir_pre[i_pre]  else None
        post_3way = cmp.three_way_classify(p.root_pc,    m.root_pc if m else None, wir_post_pc) if wir_regs else None
        pre_3way  = cmp.three_way_classify(pre_p.root_pc, pre_m.root_pc if pre_m else None, wir_pre_pc) if wir_regs else None

        # Genuine wrong-root: chord_disagree AND music21_dcml_agree
        post_genuine_wrong = (post_cat == "chord_disagree" and post_3way == "music21_dcml_agree")
        pre_genuine_wrong  = (pre_cat  == "chord_disagree" and pre_3way  == "music21_dcml_agree")

        if pre_genuine_wrong != post_genuine_wrong:
            both.append((stem, p.measure_number, p.beat,
                         "WRONG" if pre_genuine_wrong else pre_cat[:8],
                         "WRONG" if post_genuine_wrong else post_cat[:8],
                         f"pre={pre_p.chord_symbol}({pre_p.root_pc})",
                         f"post={p.chord_symbol}({p.root_pc})",
                         f"truth_m21={m.root_pc if m else '-'} wir={wir_post_pc}"))

print(f"Total classification flips: {len(both)}")
became_wrong = [r for r in both if r[4] == "WRONG"]
fixed        = [r for r in both if r[3] == "WRONG"]
print(f"  Became wrong (regression):  {len(became_wrong)}")
print(f"  Fixed (improvement):        {len(fixed)}")
print(f"  Net change in errors:       {len(became_wrong) - len(fixed):+d}")
print()
print("Became wrong:")
for r in became_wrong:
    print(" ", r)
print()
print("Fixed:")
for r in fixed:
    print(" ", r)
