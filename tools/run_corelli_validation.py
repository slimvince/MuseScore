#!/usr/bin/env python3
"""
run_corelli_validation.py — Two-way comparison of our harmonic analysis against
the DCMLab Corelli Trio Sonatas corpus (DCML annotations).

Steps:
  1. For each .mscx file in tools/dcml/corelli/MS3/, run batch_analyze to get
     our analysis as JSON (written to a timestamped subdirectory).
  2. Parse the corresponding .harmonies.tsv from tools/dcml/corelli/harmonies/.
  3. Align by measure + beat and compare root pitch classes.
  4. Report per-movement and aggregate stats, including bassIsRoot breakdown.

Usage:
    python tools/run_corelli_validation.py [OPTIONS]

    --batch-analyze PATH    Path to batch_analyze executable
                            (default: ninja_build_rel/batch_analyze.exe on Windows)
    --output DIR            Output directory root (default: tools/reports/)
    --skip-cpp              Skip step 1 (re-use existing .ours.json files)
    --help
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
import dcml_parser as dcml


# ══════════════════════════════════════════════════════════════════════════
# Paths
# ══════════════════════════════════════════════════════════════════════════

_REPO_ROOT      = Path(__file__).resolve().parent.parent
_CORELLI_MSCX   = _REPO_ROOT / "tools" / "dcml" / "corelli" / "MS3"
_CORELLI_TSV    = _REPO_ROOT / "tools" / "dcml" / "corelli" / "harmonies"


# ══════════════════════════════════════════════════════════════════════════
# Helpers
# ══════════════════════════════════════════════════════════════════════════

def _find_batch_analyze(hint: str | None) -> Path | None:
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


def _to_unix_path(p: Path) -> str:
    """Convert Windows path to /drive/... form for use as bash executable path."""
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')


def _to_win_path(p: Path) -> str:
    """Convert path to C:/... form for file arguments to native Windows binaries."""
    return str(p.resolve()).replace('\\', '/')


def _find_git_bash() -> Path | None:
    candidates = [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def _run_batch_analyze(exe: Path, mscx: Path, out: Path, preset: str = "Standard") -> bool:
    preset_arg = f'--preset {preset}'
    try:
        import platform
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = f'{_to_unix_path(exe)} "{_to_win_path(mscx)}" "{_to_win_path(out)}" {preset_arg}'
                result = subprocess.run(
                    [str(bash), '-c', cmd],
                    stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                    timeout=120,
                )
                if result.returncode != 0:
                    stderr_text = result.stderr.decode('utf-8', errors='replace').strip()
                    print(f"    batch_analyze failed (rc={result.returncode}): "
                          f"{stderr_text[:200]}", file=sys.stderr)
                    return False
                return True

        result = subprocess.run(
            [str(exe), str(mscx), str(out), '--preset', preset],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
            timeout=120,
        )
        if result.returncode != 0:
            stderr_text = result.stderr.decode('utf-8', errors='replace').strip()
            print(f"    batch_analyze failed (rc={result.returncode}): "
                  f"{stderr_text[:200]}", file=sys.stderr)
            return False
        return True
    except subprocess.TimeoutExpired:
        print("    batch_analyze timed out", file=sys.stderr)
        return False
    except Exception as exc:
        print(f"    batch_analyze error: {exc}", file=sys.stderr)
        return False


# ══════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare our harmonic analysis against Corelli trio sonatas DCML annotations."
    )
    parser.add_argument("--batch-analyze", metavar="PATH",
                        help="Path to batch_analyze executable")
    parser.add_argument("--output", metavar="DIR", default="tools/reports/",
                        help="Output directory root (default: tools/reports/)")
    parser.add_argument("--skip-cpp", action="store_true",
                        help="Skip batch_analyze step (re-use existing JSON)")
    parser.add_argument("--preset", metavar="NAME", default="Standard",
                        help="Preset to pass to batch_analyze (default: Standard)")
    args = parser.parse_args()

    output_root = Path(args.output)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    preset_suffix = f"_{args.preset.lower()}" if args.preset.lower() != "standard" else ""
    corelli_dir = output_root / f"corelli{preset_suffix}_{timestamp}"
    corelli_dir.mkdir(parents=True, exist_ok=True)

    exe = _find_batch_analyze(args.batch_analyze)
    if exe is None and not args.skip_cpp:
        print("ERROR: batch_analyze not found. Build it first.", file=sys.stderr)
        sys.exit(1)
    if exe:
        print(f"Using batch_analyze: {exe} (preset: {args.preset})")

    mscx_files = sorted(_CORELLI_MSCX.glob("*.mscx"))
    total = len(mscx_files)
    if total == 0:
        print(f"ERROR: no .mscx files found in {_CORELLI_MSCX}", file=sys.stderr)
        sys.exit(1)

    print(f"\nCorelli trio sonatas corpus: {total} movements\n")

    agg_total = agg_aligned = agg_agree = agg_disagree = agg_unaligned = 0
    agg_bir = 0
    all_results: list[dict] = []

    for idx, mscx in enumerate(mscx_files, 1):
        stem      = mscx.stem
        ours_path = corelli_dir / f"{stem}.ours.json"
        tsv_path  = _CORELLI_TSV / f"{stem}.harmonies.tsv"

        if not tsv_path.exists():
            print(f"  [{idx:3d}/{total}] {stem}  — no .harmonies.tsv, skipping")
            continue

        # Step 1 — batch_analyze
        if not args.skip_cpp or not ours_path.exists():
            if exe is None:
                print(f"  [{idx:3d}/{total}] {stem}  — SKIP (no executable)")
                continue
            ok = _run_batch_analyze(exe, mscx, ours_path, preset=args.preset)
            if not ok:
                print(f"  [{idx:3d}/{total}] {stem}  — batch_analyze failed, skipping")
                continue

        if not ours_path.exists():
            print(f"  [{idx:3d}/{total}] {stem}  — no output JSON, skipping")
            continue

        # Step 2 — parse DCML
        try:
            dcml_regions = dcml.parse_abc_harmonies_file(str(tsv_path))
        except Exception as exc:
            print(f"  [{idx:3d}/{total}] {stem}  — DCML parse error: {exc}")
            continue

        # Step 3 — load our analysis and compare
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except Exception as exc:
            print(f"  [{idx:3d}/{total}] {stem}  — JSON load error: {exc}")
            continue

        direct = cmp.compare_ours_vs_dcml_direct(ours_regions, dcml_regions)
        stats  = cmp.dcml_direct_summarize(direct)

        agg_total     += stats['total']
        agg_aligned   += stats['aligned']
        agg_agree     += stats['agree']
        agg_disagree  += stats['disagree']
        agg_unaligned += stats['unaligned']
        agg_bir       += stats['bass_is_root_in_disagree']

        agree_pct = f"{stats['agree_pct']:.1f}%" if stats['aligned'] else "n/a"
        print(f"  [{idx:3d}/{total}] {stem:<30}  "
              f"ours: {stats['total']:4d}  "
              f"aligned: {stats['aligned']:4d}  "
              f"agree: {stats['agree']:4d} ({agree_pct})  "
              f"disagree: {stats['disagree']:3d}  "
              f"bir_err: {stats['bass_is_root_in_disagree']}")

        all_results.append({'stem': stem, **stats})

    # ── Aggregate summary ─────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"Corelli trio sonatas -- aggregate results")
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

    # ── Write JSON summary ────────────────────────────────────────────────
    summary_path = output_root / "reports" / f"corelli_{timestamp}.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary = {
        'corpus': 'Corelli trio sonatas',
        'timestamp': timestamp,
        'git_hash': _get_git_hash(),
        'movements': len(all_results),
        'ours_dir': str(corelli_dir),
        'aggregate': {
            'total': agg_total,
            'aligned': agg_aligned,
            'agree': agg_agree,
            'disagree': agg_disagree,
            'unaligned': agg_unaligned,
            'agree_pct': round(100*agg_agree/agg_aligned, 2) if agg_aligned else 0,
            'bass_is_root_in_disagree': agg_bir,
            'bass_is_root_pct_of_disagree': round(100*agg_bir/agg_disagree, 2) if agg_disagree else 0,
        },
        'movements_detail': all_results,
    }
    summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f"\nSummary written to {summary_path}")
    print(f"ours JSON written to {corelli_dir}")


def _get_git_hash() -> str:
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            capture_output=True, text=True,
            cwd=str(_REPO_ROOT), timeout=10,
        )
        return result.stdout.strip() if result.returncode == 0 else 'unknown'
    except Exception:
        return 'unknown'


if __name__ == "__main__":
    main()
