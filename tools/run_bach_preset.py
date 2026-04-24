#!/usr/bin/env python3
"""
run_bach_preset.py — Run Bach chorale corpus with a specific preset and compare
against existing music21.json files (which serve as ground truth).

Usage:
    python tools/run_bach_preset.py [OPTIONS]
    --preset NAME         Preset name (Standard, Baroque, Modal, Jazz, Contemporary)
    --batch-analyze PATH  Path to batch_analyze executable
    --corpus-dir DIR      Directory containing *.xml and *.music21.json (default: tools/corpus)
    --output-dir DIR      Where to write *.ours.json output (default: tools/corpus_<preset>)
    --skip-cpp            Skip batch_analyze, re-use existing .ours.json files
"""

from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp

_REPO_ROOT = Path(__file__).resolve().parent.parent


def _find_batch_analyze(hint):
    candidates = ([Path(hint)] if hint else []) + [
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze",
        _REPO_ROOT / "ninja_build" / "batch_analyze",
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


def _run_batch_analyze(exe, xml_path, out_path, preset):
    try:
        import platform
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = (f'{_to_unix_path(exe)} "{_to_unix_path(xml_path)}"'
                       f' "{_to_unix_path(out_path)}" --preset {preset}')
                r = subprocess.run([str(bash), '-c', cmd],
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.PIPE, timeout=120)
                if r.returncode != 0:
                    print(f"    failed: {r.stderr.decode('utf-8','replace').strip()[:200]}",
                          file=sys.stderr)
                    return False
                return True
        r = subprocess.run([str(exe), str(xml_path), str(out_path), '--preset', preset],
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=120)
        return r.returncode == 0
    except subprocess.TimeoutExpired:
        print("    timed out", file=sys.stderr); return False
    except Exception as e:
        print(f"    error: {e}", file=sys.stderr); return False


def _get_git_hash():
    try:
        r = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                           capture_output=True, text=True, cwd=str(_REPO_ROOT))
        return r.stdout.strip() if r.returncode == 0 else 'unknown'
    except Exception:
        return 'unknown'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preset", default="Baroque",
                        choices=["Standard", "Baroque", "Modal", "Jazz", "Contemporary"])
    parser.add_argument("--batch-analyze", metavar="PATH")
    parser.add_argument("--corpus-dir", metavar="DIR", default="tools/corpus")
    parser.add_argument("--output-dir", metavar="DIR")
    parser.add_argument("--skip-cpp", action="store_true")
    args = parser.parse_args()

    corpus_dir = Path(args.corpus_dir)
    if args.output_dir:
        out_dir = Path(args.output_dir)
    else:
        out_dir = _REPO_ROOT / "tools" / f"corpus_{args.preset.lower()}"
    out_dir.mkdir(parents=True, exist_ok=True)

    exe = _find_batch_analyze(args.batch_analyze)
    if exe is None and not args.skip_cpp:
        print("ERROR: batch_analyze not found.", file=sys.stderr); sys.exit(1)
    if exe:
        print(f"Using batch_analyze: {exe}")

    xml_files = sorted(f for f in corpus_dir.glob("*.xml")
                       if not f.stem.endswith("_m21"))
    total = len(xml_files)
    if total == 0:
        print(f"ERROR: no .xml files in {corpus_dir}", file=sys.stderr); sys.exit(1)

    print(f"\nBach chorales — preset={args.preset}  ({total} files)\n")

    agree_sum = 0.0
    compared_n = 0
    total_regions = 0
    total_agree = 0
    total_chord = 0

    for idx, xml_path in enumerate(xml_files, 1):
        stem = xml_path.stem
        ours_path = out_dir / f"{stem}.ours.json"
        m21_path = corpus_dir / f"{stem}.music21.json"

        if not m21_path.exists():
            print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no music21.json)")
            continue

        if not args.skip_cpp or not ours_path.exists():
            if exe is None:
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no exe)")
                continue
            ok = _run_batch_analyze(exe, xml_path, ours_path, args.preset)
            if not ok:
                print(f"  [{idx:>3}/{total}] {stem:<30}  FAILED")
                continue

        if not ours_path.exists():
            print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no ours.json)")
            continue

        try:
            ours_meta, m21_meta, compared = cmp.compare_files(ours_path, m21_path)
        except Exception as exc:
            print(f"  [{idx:>3}/{total}] {stem:<30}  ERROR: {exc}", file=sys.stderr)
            continue

        counts = cmp.summarize(compared)
        ci_n, ci_rate = cmp.chord_identity_agreement(counts)
        total_r = sum(counts.values())
        m21_n = len(m21_meta.get("regions", []))

        print(f"  [{idx:>3}/{total}] {stem:<30}  m21:{m21_n:>3}  ours:{total_r:>3}"
              f"  chord_id:{ci_n:>3}  {ci_rate:.0%}")

        agree_sum += ci_rate
        compared_n += 1
        total_regions += total_r
        total_agree += ci_n
        total_chord += total_r - counts.get('unaligned', 0)

    print(f"\n{'='*65}")
    print(f"Bach chorales — preset={args.preset} — aggregate results")
    print(f"{'='*65}")
    print(f"Chorales compared   : {compared_n}/{total}")
    if total_chord:
        print(f"Total aligned regions: {total_chord}")
        print(f"Chord identity agree : {total_agree} ({100*total_agree/total_chord:.1f}%)")
    if compared_n:
        print(f"Mean per-chorale    : {agree_sum/compared_n:.1%}")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = _REPO_ROOT / "tools" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    sp = report_dir / f"bach_{args.preset.lower()}_{timestamp}.json"
    sp.write_text(json.dumps({
        'corpus': 'Bach chorales',
        'preset': args.preset,
        'timestamp': timestamp,
        'git_hash': _get_git_hash(),
        'chorales_compared': compared_n,
        'chorales_total': total,
        'aggregate': {
            'total_aligned': total_chord,
            'chord_identity_agree': total_agree,
            'chord_identity_pct': round(100*total_agree/total_chord, 2) if total_chord else 0,
            'mean_per_chorale_pct': round(100*agree_sum/compared_n, 2) if compared_n else 0,
        },
        'out_dir': str(out_dir),
    }, indent=2), encoding='utf-8')
    print(f"\nReport written to {sp}")
    print(f"ours JSON written to {out_dir}")


if __name__ == "__main__":
    main()
