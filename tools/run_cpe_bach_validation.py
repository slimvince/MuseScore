#!/usr/bin/env python3
"""
run_cpe_bach_validation.py — Two-way comparison against the DCMLab
C.P.E. Bach Keyboard corpus (DCML annotations).

Usage:
    python tools/run_cpe_bach_validation.py [OPTIONS]
    --batch-analyze PATH    --output DIR    --skip-cpp
"""

from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import dcml_parser as dcml

_REPO_ROOT   = Path(__file__).resolve().parent.parent
_MSCX_DIR    = _REPO_ROOT / "tools" / "dcml" / "cpe_bach_keyboard" / "MS3"
_TSV_DIR     = _REPO_ROOT / "tools" / "dcml" / "cpe_bach_keyboard" / "harmonies"

_SUFFIX_MAP = [
    ('Lyd','lydian'),('Dor','dorian'),('Mix','mixolydian'),('Phr','phrygian'),
    ('Loc','locrian'),('harm','harmonic_minor'),('min','minor'),('Maj','major'),('maj','major'),
]

def _find_batch_analyze(hint):
    candidates = ([Path(hint)] if hint else []) + [
        _REPO_ROOT/"ninja_build_rel"/"batch_analyze.exe",
        _REPO_ROOT/"ninja_build"/"batch_analyze.exe",
        _REPO_ROOT/"ninja_build_rel"/"batch_analyze",
        _REPO_ROOT/"ninja_build"/"batch_analyze",
    ]
    return next((p for p in candidates if p.exists()), None)

def _to_unix_path(p):
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')

def _find_git_bash():
    return next((p for p in [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ] if p.exists()), None)

def _run_batch_analyze(exe, mscx, out):
    try:
        import platform
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = f'{_to_unix_path(exe)} "{_to_unix_path(mscx)}" "{_to_unix_path(out)}"'
                r = subprocess.run([str(bash),'-c',cmd], stdout=subprocess.DEVNULL,
                                   stderr=subprocess.PIPE, timeout=120)
                if r.returncode != 0:
                    print(f"    failed: {r.stderr.decode('utf-8','replace').strip()[:200]}", file=sys.stderr)
                    return False
                return True
        r = subprocess.run([str(exe),str(mscx),str(out)], stdout=subprocess.DEVNULL,
                           stderr=subprocess.PIPE, timeout=120)
        return r.returncode == 0
    except subprocess.TimeoutExpired:
        print("    timed out", file=sys.stderr); return False
    except Exception as e:
        print(f"    error: {e}", file=sys.stderr); return False

def _get_git_hash():
    try:
        r = subprocess.run(['git','rev-parse','--short','HEAD'],
            capture_output=True, text=True, cwd=str(_REPO_ROOT))
        return r.stdout.strip() if r.returncode == 0 else 'unknown'
    except Exception: return 'unknown'

def _modal_dist(ours_dir):
    counts: Counter = Counter()
    for f in ours_dir.glob('*.ours.json'):
        try:
            for r in json.loads(f.read_text(encoding='utf-8')).get('regions', []):
                key = r.get('key', '')
                for suf, lbl in _SUFFIX_MAP:
                    if suf in key: counts[lbl] += 1; break
                else: counts['other'] += 1
        except Exception: pass
    return dict(counts.most_common())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-analyze", metavar="PATH")
    parser.add_argument("--output", metavar="DIR", default="tools/reports/")
    parser.add_argument("--skip-cpp", action="store_true")
    args = parser.parse_args()

    output_root = Path(args.output)
    timestamp   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir     = output_root / f"cpe_bach_{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    exe = _find_batch_analyze(args.batch_analyze)
    if exe is None and not args.skip_cpp:
        print("ERROR: batch_analyze not found.", file=sys.stderr); sys.exit(1)
    if exe: print(f"Using batch_analyze: {exe}")

    mscx_files = sorted(_MSCX_DIR.glob("*.mscx"))
    total = len(mscx_files)
    if total == 0:
        print(f"ERROR: no .mscx in {_MSCX_DIR}", file=sys.stderr); sys.exit(1)
    print(f"\nC.P.E. Bach Keyboard corpus: {total} movements\n")

    agg_total=agg_aligned=agg_agree=agg_disagree=agg_unaligned=agg_bir=0
    all_results=[]

    for idx, mscx in enumerate(mscx_files, 1):
        stem      = mscx.stem
        ours_path = out_dir / f"{stem}.ours.json"
        tsv_path  = _TSV_DIR / f"{stem}.harmonies.tsv"

        if not tsv_path.exists():
            print(f"  [{idx:3d}/{total}] {stem}  -- no TSV, skipping"); continue
        if not args.skip_cpp or not ours_path.exists():
            if exe is None: print(f"  [{idx:3d}/{total}] {stem}  -- SKIP"); continue
            if not _run_batch_analyze(exe, mscx, ours_path):
                print(f"  [{idx:3d}/{total}] {stem}  -- failed, skipping"); continue
        if not ours_path.exists():
            print(f"  [{idx:3d}/{total}] {stem}  -- no JSON, skipping"); continue

        try: dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
        except Exception as e: print(f"  [{idx:3d}/{total}] {stem}  -- DCML error: {e}"); continue
        try: _, ours_regions = cmp.load_analysis(ours_path)
        except Exception as e: print(f"  [{idx:3d}/{total}] {stem}  -- JSON error: {e}"); continue

        direct = cmp.compare_ours_vs_dcml_direct(ours_regions, dcml_regions)
        stats  = cmp.dcml_direct_summarize(direct)
        agg_total+=stats['total']; agg_aligned+=stats['aligned']
        agg_agree+=stats['agree']; agg_disagree+=stats['disagree']
        agg_unaligned+=stats['unaligned']; agg_bir+=stats['bass_is_root_in_disagree']

        pct = f"{stats['agree_pct']:.1f}%" if stats['aligned'] else "n/a"
        print(f"  [{idx:3d}/{total}] {stem:<38}  ours:{stats['total']:4d}  "
              f"aligned:{stats['aligned']:4d}  agree:{stats['agree']:4d} ({pct})  "
              f"disagree:{stats['disagree']:3d}  bir:{stats['bass_is_root_in_disagree']}")
        all_results.append({'stem': stem, **stats})

    print(f"\n{'='*70}\nC.P.E. Bach Keyboard -- aggregate results\n{'='*70}")
    print(f"Movements processed : {len(all_results)}/{total}")
    print(f"Total our regions   : {agg_total}")
    if agg_total:   print(f"DCML-aligned        : {agg_aligned} ({100*agg_aligned/agg_total:.1f}%)")
    if agg_aligned: print(f"Root agreement      : {agg_agree}/{agg_aligned} ({100*agg_agree/agg_aligned:.1f}%)")
    if agg_disagree:print(f"  bassIsRoot=true   : {agg_bir}/{agg_disagree} ({100*agg_bir/agg_disagree:.1f}%)")

    modal = _modal_dist(out_dir)
    mt    = sum(modal.values())
    if mt:
        print(f"\nModal distribution ({mt} regions):")
        for m,c in sorted(modal.items(), key=lambda x:-x[1]):
            print(f"  {m:<20}: {c:5d}  ({100*c/mt:.1f}%)")

    sp = output_root/"reports"/f"cpe_bach_{timestamp}.json"
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps({
        'corpus':'C.P.E. Bach Keyboard','timestamp':timestamp,'git_hash':_get_git_hash(),
        'movements':len(all_results),'ours_dir':str(out_dir),
        'aggregate':{'total':agg_total,'aligned':agg_aligned,'agree':agg_agree,
            'disagree':agg_disagree,'unaligned':agg_unaligned,
            'agree_pct':round(100*agg_agree/agg_aligned,2) if agg_aligned else 0,
            'bass_is_root_in_disagree':agg_bir,
            'bass_is_root_pct_of_disagree':round(100*agg_bir/agg_disagree,2) if agg_disagree else 0},
        'modal_distribution':modal,'movements_detail':all_results,
    }, indent=2), encoding='utf-8')
    print(f"\nSummary written to {sp}\nours JSON written to {out_dir}")

if __name__ == "__main__":
    main()
