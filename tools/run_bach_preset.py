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
import concurrent.futures
import datetime
import io
import json
import multiprocessing
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


def _run_batch_analyze(exe, xml_path, out_path, preset, diag_fh=None):
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
                if diag_fh is not None and r.stderr:
                    diag_fh.write(r.stderr.decode('utf-8', 'replace'))
                    diag_fh.flush()
                if r.returncode != 0:
                    print(f"    failed: {r.stderr.decode('utf-8','replace').strip()[:200]}",
                          file=sys.stderr)
                    return False
                return True
        r = subprocess.run([str(exe), str(xml_path), str(out_path), '--preset', preset],
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=120)
        if diag_fh is not None and r.stderr:
            diag_fh.write(r.stderr.decode('utf-8', 'replace'))
            diag_fh.flush()
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


def _process_one(args_tuple):
    """Process a single chorale in a worker process.

    Returns (idx, stem, status, stats_or_None, diag_text, error_msg) where
    status is one of 'OK', 'SKIP_NO_M21', 'SKIP_NO_EXE', 'FAILED',
    'SKIP_NO_OURS', 'ERROR'.
    """
    idx, exe, xml_path, ours_path, m21_path, preset, skip_cpp = args_tuple
    stem = xml_path.stem

    if not m21_path.exists():
        return (idx, stem, 'SKIP_NO_M21', None, '', None)

    diag_buf = io.StringIO()

    if not skip_cpp or not ours_path.exists():
        if exe is None:
            return (idx, stem, 'SKIP_NO_EXE', None, '', None)
        diag_buf.write(f"[PROCESSING] {stem}\n")
        ok = _run_batch_analyze(exe, xml_path, ours_path, preset, diag_buf)
        if not ok:
            return (idx, stem, 'FAILED', None, diag_buf.getvalue(), None)

    if not ours_path.exists():
        return (idx, stem, 'SKIP_NO_OURS', None, diag_buf.getvalue(), None)

    try:
        ours_meta, m21_meta, compared = cmp.compare_files(ours_path, m21_path)
    except Exception as exc:
        return (idx, stem, 'ERROR', None, diag_buf.getvalue(), str(exc))

    counts = cmp.summarize(compared)
    ci_n, ci_rate = cmp.chord_identity_agreement(counts)
    total_r = sum(counts.values())
    m21_n = len(m21_meta.get("regions", []))
    unaligned = counts.get('unaligned', 0)

    stats = {
        'ci_n': ci_n,
        'ci_rate': ci_rate,
        'total_r': total_r,
        'm21_n': m21_n,
        'unaligned': unaligned,
    }
    return (idx, stem, 'OK', stats, diag_buf.getvalue(), None)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preset", default="Baroque",
                        choices=["Standard", "Baroque", "Modal", "Jazz", "Contemporary"])
    parser.add_argument("--batch-analyze", metavar="PATH")
    parser.add_argument("--corpus-dir", metavar="DIR", default="tools/corpus")
    parser.add_argument("--output-dir", metavar="DIR")
    parser.add_argument("--skip-cpp", action="store_true")
    parser.add_argument("--diag-out", metavar="FILE",
                        help="Append batch_analyze stderr to this file (for diagnostics)")
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

    diag_fh = None
    if args.diag_out:
        diag_fh = open(args.diag_out, 'w', encoding='utf-8')
        print(f"Diagnostic stderr → {args.diag_out}")

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

    work_items = [
        (idx, exe, xml_path,
         out_dir / f"{xml_path.stem}.ours.json",
         corpus_dir / f"{xml_path.stem}.music21.json",
         args.preset, args.skip_cpp)
        for idx, xml_path in enumerate(xml_files, 1)
    ]

    workers = min(multiprocessing.cpu_count(), len(xml_files))
    print(f"  Parallelising over {workers} workers ({total} chorales)...\n")

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_process_one, item): item[0] for item in work_items}
        for future in concurrent.futures.as_completed(futures):
            try:
                idx, stem, status, stats, diag_text, err = future.result()
            except Exception as exc:
                print(f"  worker crashed: {exc}", file=sys.stderr)
                continue

            if diag_text and diag_fh is not None:
                diag_fh.write(diag_text)
                diag_fh.flush()

            if status == 'SKIP_NO_M21':
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no music21.json)")
                continue
            if status == 'SKIP_NO_EXE':
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no exe)")
                continue
            if status == 'FAILED':
                print(f"  [{idx:>3}/{total}] {stem:<30}  FAILED")
                continue
            if status == 'SKIP_NO_OURS':
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no ours.json)")
                continue
            if status == 'ERROR':
                print(f"  [{idx:>3}/{total}] {stem:<30}  ERROR: {err}", file=sys.stderr)
                continue

            print(f"  [{idx:>3}/{total}] {stem:<30}  m21:{stats['m21_n']:>3}"
                  f"  ours:{stats['total_r']:>3}  chord_id:{stats['ci_n']:>3}"
                  f"  {stats['ci_rate']:.0%}")

            agree_sum += stats['ci_rate']
            compared_n += 1
            total_regions += stats['total_r']
            total_agree += stats['ci_n']
            total_chord += stats['total_r'] - stats['unaligned']

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

    if diag_fh is not None:
        diag_fh.close()
        print(f"Diagnostic stderr written to {args.diag_out}")


if __name__ == "__main__":
    main()
