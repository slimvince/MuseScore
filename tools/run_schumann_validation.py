#!/usr/bin/env python3
"""
run_schumann_validation.py — Two-way comparison of our harmonic analysis against
the DCMLab Schumann Kinderszenen corpus (DCML annotations).

Usage:
    python tools/run_schumann_validation.py [OPTIONS]

    --batch-analyze PATH    Path to batch_analyze executable
    --output DIR            Output directory root (default: tools/reports/)
    --skip-cpp              Skip batch_analyze step
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

_REPO_ROOT       = Path(__file__).resolve().parent.parent
_SCHUMANN_MSCX   = _REPO_ROOT / "tools" / "dcml" / "schumann_kinderszenen" / "MS3"
_SCHUMANN_TSV    = _REPO_ROOT / "tools" / "dcml" / "schumann_kinderszenen" / "harmonies"

_SUFFIX_MAP = [
    ('Lyd', 'lydian'), ('Dor', 'dorian'), ('Mix', 'mixolydian'),
    ('Phr', 'phrygian'), ('Loc', 'locrian'), ('harm', 'harmonic_minor'),
    ('min', 'minor'), ('Maj', 'major'), ('maj', 'major'),
]

def _find_batch_analyze(hint):
    candidates = []
    if hint:
        candidates.append(Path(hint))
    candidates += [
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze",
        _REPO_ROOT / "ninja_build" / "batch_analyze",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None

def _to_unix_path(p):
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')

def _find_git_bash():
    for p in [Path("C:/Program Files/Git/usr/bin/bash.exe"),
              Path("C:/Program Files (x86)/Git/usr/bin/bash.exe")]:
        if p.exists():
            return p
    return None

def _run_batch_analyze(exe, mscx, out):
    try:
        import platform
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = f'{_to_unix_path(exe)} "{_to_unix_path(mscx)}" "{_to_unix_path(out)}"'
                result = subprocess.run([str(bash), '-c', cmd],
                    stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=120)
                if result.returncode != 0:
                    print(f"    failed (rc={result.returncode}): "
                          f"{result.stderr.decode('utf-8','replace').strip()[:200]}", file=sys.stderr)
                    return False
                return True
        result = subprocess.run([str(exe), str(mscx), str(out)],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=120)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("    timed out", file=sys.stderr); return False
    except Exception as exc:
        print(f"    error: {exc}", file=sys.stderr); return False

def _get_git_hash():
    try:
        r = subprocess.run(['git','rev-parse','--short','HEAD'],
            capture_output=True, text=True, cwd=str(_REPO_ROOT))
        return r.stdout.strip() if r.returncode == 0 else 'unknown'
    except Exception:
        return 'unknown'

def _modal_distribution(ours_dir):
    counts: Counter = Counter()
    for f in ours_dir.glob('*.ours.json'):
        try:
            d = json.loads(f.read_text(encoding='utf-8'))
            for r in d.get('regions', []):
                key = r.get('key', '')
                for suf, label in _SUFFIX_MAP:
                    if suf in key:
                        counts[label] += 1
                        break
                else:
                    counts['other'] += 1
        except Exception:
            pass
    return dict(counts.most_common())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-analyze", metavar="PATH")
    parser.add_argument("--output", metavar="DIR", default="tools/reports/")
    parser.add_argument("--skip-cpp", action="store_true")
    args = parser.parse_args()

    output_root = Path(args.output)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    schumann_dir = output_root / f"schumann_{timestamp}"
    schumann_dir.mkdir(parents=True, exist_ok=True)

    exe = _find_batch_analyze(args.batch_analyze)
    if exe is None and not args.skip_cpp:
        print("ERROR: batch_analyze not found.", file=sys.stderr); sys.exit(1)
    if exe:
        print(f"Using batch_analyze: {exe}")

    mscx_files = sorted(_SCHUMANN_MSCX.glob("*.mscx"))
    total = len(mscx_files)
    if total == 0:
        print(f"ERROR: no .mscx files in {_SCHUMANN_MSCX}", file=sys.stderr); sys.exit(1)

    print(f"\nSchumann Kinderszenen corpus: {total} movements\n")

    agg_total = agg_aligned = agg_agree = agg_disagree = agg_unaligned = agg_bir = 0
    all_results = []

    for idx, mscx in enumerate(mscx_files, 1):
        stem      = mscx.stem
        ours_path = schumann_dir / f"{stem}.ours.json"
        tsv_path  = _SCHUMANN_TSV / f"{stem}.harmonies.tsv"

        if not tsv_path.exists():
            print(f"  [{idx:3d}/{total}] {stem}  -- no .harmonies.tsv, skipping")
            continue

        if not args.skip_cpp or not ours_path.exists():
            if exe is None:
                print(f"  [{idx:3d}/{total}] {stem}  -- SKIP (no executable)"); continue
            if not _run_batch_analyze(exe, mscx, ours_path):
                print(f"  [{idx:3d}/{total}] {stem}  -- batch_analyze failed, skipping"); continue

        if not ours_path.exists():
            print(f"  [{idx:3d}/{total}] {stem}  -- no output JSON, skipping"); continue

        try:
            dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
        except Exception as exc:
            print(f"  [{idx:3d}/{total}] {stem}  -- DCML parse error: {exc}"); continue

        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except Exception as exc:
            print(f"  [{idx:3d}/{total}] {stem}  -- JSON load error: {exc}"); continue

        direct = cmp.compare_ours_vs_dcml_direct(ours_regions, dcml_regions)
        stats  = cmp.dcml_direct_summarize(direct)

        agg_total     += stats['total']
        agg_aligned   += stats['aligned']
        agg_agree     += stats['agree']
        agg_disagree  += stats['disagree']
        agg_unaligned += stats['unaligned']
        agg_bir       += stats['bass_is_root_in_disagree']

        agree_pct = f"{stats['agree_pct']:.1f}%" if stats['aligned'] else "n/a"
        print(f"  [{idx:3d}/{total}] {stem:<38}  "
              f"ours: {stats['total']:4d}  "
              f"aligned: {stats['aligned']:4d}  "
              f"agree: {stats['agree']:4d} ({agree_pct})  "
              f"disagree: {stats['disagree']:3d}  "
              f"bir_err: {stats['bass_is_root_in_disagree']}")

        all_results.append({'stem': stem, **stats})

    print(f"\n{'='*70}")
    print(f"Schumann Kinderszenen -- aggregate results")
    print(f"{'='*70}")
    print(f"Movements processed : {len(all_results)}/{total}")
    print(f"Total our regions   : {agg_total}")
    if agg_total:
        print(f"DCML-aligned        : {agg_aligned} ({100*agg_aligned/agg_total:.1f}% of ours)")
    if agg_aligned:
        print(f"Root agreement      : {agg_agree}/{agg_aligned} ({100*agg_agree/agg_aligned:.1f}%)")
        print(f"Root disagreement   : {agg_disagree}/{agg_aligned} ({100*agg_disagree/agg_aligned:.1f}%)")
    if agg_disagree:
        print(f"  bassIsRoot=true   : {agg_bir}/{agg_disagree} ({100*agg_bir/agg_disagree:.1f}% of disagreements)")

    modal = _modal_distribution(schumann_dir)
    modal_total = sum(modal.values())
    if modal_total:
        print(f"\nModal distribution ({modal_total} total regions):")
        for mode, count in sorted(modal.items(), key=lambda x: -x[1]):
            print(f"  {mode:<20}: {count:5d}  ({100*count/modal_total:.1f}%)")

    summary_path = output_root / "reports" / f"schumann_{timestamp}.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary = {
        'corpus': 'Schumann Kinderszenen',
        'timestamp': timestamp,
        'git_hash': _get_git_hash(),
        'movements': len(all_results),
        'ours_dir': str(schumann_dir),
        'aggregate': {
            'total': agg_total, 'aligned': agg_aligned,
            'agree': agg_agree, 'disagree': agg_disagree, 'unaligned': agg_unaligned,
            'agree_pct': round(100*agg_agree/agg_aligned, 2) if agg_aligned else 0,
            'bass_is_root_in_disagree': agg_bir,
            'bass_is_root_pct_of_disagree': round(100*agg_bir/agg_disagree, 2) if agg_disagree else 0,
        },
        'modal_distribution': modal,
        'movements_detail': all_results,
    }
    summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f"\nSummary written to {summary_path}")
    print(f"ours JSON written to {schumann_dir}")

if __name__ == "__main__":
    main()
