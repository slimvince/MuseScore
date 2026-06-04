#!/usr/bin/env python3
"""One-off helper: find Maj→Dom7 quality_disagree cases across cross-corpus
and report the 7th PC weight from the per-region tones list.

Usage: python tools/find_maj_to_dom7.py [--limit N] [--corpora a,b,c]
"""
from __future__ import annotations

import argparse
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import compare_rn as crn
import dcml_parser as dcml


def pc_weight_sum(tones, target_pc: int) -> float:
    """Sum tone weights for tones at the target pitch class."""
    return sum(float(t.get("weight", 0.0)) for t in tones if (int(t.get("pitch", 0)) % 12) == target_pc)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="tools/reports/live_20260603")
    ap.add_argument("--limit-per-corpus", type=int, default=5)
    ap.add_argument("--corpora", default="beethoven,mozart,grieg,chopin,corelli")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    repo_root = Path(__file__).resolve().parent.parent

    wanted = set(args.corpora.split(","))
    corpora = crn.discover_corpora(root)

    print(f"# Maj→Dom7 quality_disagree examples ({args.limit_per_corpus} per corpus)")
    print(f"# Cross-corpus root: {root}")
    print()

    for label, ours_dir in corpora.items():
        if label not in wanted:
            continue
        cfg = crn.CROSS_CORPORA[label]
        tsv_dir = repo_root / cfg["tsv_dir"]
        if not tsv_dir.is_dir():
            continue
        print(f"### {label}")
        found = 0
        for ours_path in sorted(ours_dir.glob("*.ours.json")):
            if found >= args.limit_per_corpus:
                break
            stem = ours_path.name.replace(".ours.json", "")
            tsv = crn._find_tsv(tsv_dir, stem)
            if tsv is None:
                continue
            try:
                _, ours_regions = cmp.load_analysis(ours_path)
            except Exception:
                continue
            try:
                dcml_regions = dcml.parse_abc_harmonies_file(str(tsv))
            except Exception:
                continue
            if not ours_regions or not dcml_regions:
                continue
            matches = cmp.align_dcml_regions(ours_regions, dcml_regions,
                                            mode=cmp.DEFAULT_DCML_MATCH_MODE)
            # raw json for tones
            import json
            raw = json.loads(ours_path.read_text(encoding="utf-8"))
            raw_regions = raw.get("regions", [])
            for idx, (ours_r, dr) in enumerate(zip(ours_regions, matches)):
                if found >= args.limit_per_corpus:
                    break
                if dr is None:
                    continue
                pair = crn.classify_pair(ours_r, dr)
                if pair is None or pair.category != "quality_disagree":
                    continue
                o_q = crn.extract_quality(pair.ours_rn)
                d_q = crn.extract_quality(pair.dcml_rn)
                if not (o_q == "Maj" and d_q == "Dom7"):
                    continue
                # find matching raw region
                rr = raw_regions[idx] if idx < len(raw_regions) else None
                if rr is None:
                    continue
                tones = rr.get("tones", [])
                root_pc = int(rr.get("rootPitchClass", -1))
                seventh_pc = (root_pc + 10) % 12
                w7 = pc_weight_sum(tones, seventh_pc)
                # also report total weight for normalisation context
                total_w = sum(float(t.get("weight", 0.0)) for t in tones)
                # distinct PCs in region
                distinct_pcs = sorted(set(int(t.get("pitch", 0)) % 12 for t in tones))
                print(f"  {stem}  m{rr.get('measureNumber')} b{rr.get('beat')} "
                      f"tick={rr.get('startTick')}-{rr.get('endTick')}  "
                      f"ours={pair.ours_rn} ({rr.get('chordSymbol')})  "
                      f"dcml={pair.dcml_rn}")
                print(f"      rootPc={root_pc} 7thPc={seventh_pc}  "
                      f"w(7th)={w7:.3f}  total_w={total_w:.3f}  "
                      f"w(7th)/total={(w7/total_w if total_w else 0):.3f}  "
                      f"distinct_pcs={distinct_pcs}  "
                      f"above_0.20={'YES' if w7 >= 0.20 else 'no'}  "
                      f"present={'yes' if seventh_pc in distinct_pcs else 'NO'}")
                found += 1
        if found == 0:
            print("  (none found)")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
