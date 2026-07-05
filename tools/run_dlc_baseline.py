#!/usr/bin/env python3
"""
run_dlc_baseline.py — generic per-corpus baseline driver for the Distant
Listening Corpus (DLC) sub-corpora onboarded in corpus wave 1.

Replaces the ~30-copied-scripts pattern (run_<corpus>_validation.py) with ONE
config-driven driver (per the census unification rule).  For each requested
sub-corpus it:

  1. runs batch_analyze (DEFAULT config — the user-run configuration) over every
     tools/dcml/<repo>/MS3/*.mscx into a gitignored per-corpus output dir under
     tools/corpus_dlc_wave1/<repo>/ (regenerable; never committed);
  2. scores the outputs against tools/dcml/<repo>/harmonies/<stem>.harmonies.tsv
     with compare_rn.score_corpus (root_agree + rn_agree) and, when --grid,
     grid_score_corpus_tsv (granularity-robust beat-grid view).

The DLC members all share the MS3/ + harmonies/ layout, so the config table is
just the list of repo names; nothing per-corpus is hand-written.  Results are
DESCRIPTIVE research-tier baselines — no target, no tuning, no gate.

Output baselines are written incrementally to
tools/corpus_dlc_wave1/results.json after EACH corpus so a killed run keeps
partial progress.

Usage:
    python tools/run_dlc_baseline.py --all-new [--grid] [--timeout 90] [--limit N]
    python tools/run_dlc_baseline.py --corpora beethoven_piano_sonatas,wagner_overtures
"""
from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT / "tools"))
import compare_rn as crn  # noqa: E402

_DCML = _REPO_ROOT / "tools" / "dcml"
_OUT_ROOT = _REPO_ROOT / "tools" / "corpus_dlc_wave1"

# DLC members already onboarded before wave 1 (their run_*_validation.py exist);
# --all-new skips these.
_PREWAVE1 = {
    "ABC", "bach_en_fr_suites", "chopin_mazurkas", "corelli", "cpe_bach_keyboard",
    "dvorak_silhouettes", "grieg_lyric_pieces", "mozart_piano_sonatas",
    "schumann_kinderszenen", "tchaikovsky_seasons",
}
_NOT_DLC = {"bach_chorales", "when_in_rome"}


def _all_new() -> list[str]:
    repos = []
    for d in sorted(_DCML.iterdir()):
        if not d.is_dir() or d.name in _NOT_DLC or d.name in _PREWAVE1:
            continue
        if (d / "MS3").is_dir() and (d / "harmonies").is_dir():
            repos.append(d.name)
    return repos


def _find_batch_analyze() -> Path | None:
    for p in (_REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
              _REPO_ROOT / "ninja_build" / "batch_analyze.exe",
              _REPO_ROOT / "ninja_build_rel" / "batch_analyze"):
        if p.exists():
            return p
    return None


def _find_git_bash() -> Path | None:
    for p in (Path("C:/Program Files/Git/usr/bin/bash.exe"),
              Path("C:/Program Files (x86)/Git/usr/bin/bash.exe")):
        if p.exists():
            return p
    return None


def _to_unix(p: Path) -> str:
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ":":
        s = "/" + s[0].lower() + s[2:]
    return s.replace("\\", "/")


def _run_one(exe: Path, mscx: Path, out: Path, bash: Path | None, timeout: int,
             param_override: str | None = None) -> bool:
    # --param-override (Stage-5 S-5 candidate scoring, O-8): additive and OPTIONAL. When
    # absent the batch_analyze invocation is byte-identical to before; when a file is
    # passed it flows to batch_analyze --param-override (byte-identical for an identity
    # file, live for a perturbed one).
    try:
        if platform.system() == "Windows" and bash:
            cmd = f'{_to_unix(exe)} "{_to_unix(mscx)}" "{_to_unix(out)}"'
            if param_override:
                cmd += f' --param-override "{_to_unix(Path(param_override))}"'
            r = subprocess.run([str(bash), "-c", cmd], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=timeout)
        else:
            base = [str(exe), str(mscx), str(out)]
            if param_override:
                base += ["--param-override", str(param_override)]
            r = subprocess.run(base, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=timeout)
        return r.returncode == 0 and out.exists()
    except Exception:
        return False


def _pct(n: int, d: int) -> float:
    return round(100.0 * n / d, 2) if d else 0.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all-new", action="store_true")
    ap.add_argument("--corpora", default="", help="comma-separated repo names")
    ap.add_argument("--grid", action="store_true", help="also compute granularity-robust grid stats")
    ap.add_argument("--timeout", type=int, default=90, help="per-movement batch_analyze timeout (s)")
    ap.add_argument("--limit", type=int, default=0, help="cap movements per corpus (0 = all)")
    ap.add_argument("--skip-cpp", action="store_true", help="reuse existing .ours.json")
    ap.add_argument("--param-override", default=None, metavar="FILE",
                    help="Stage-5 S-5 (O-8): pass a scoring-parameter override FILE to "
                         "batch_analyze so a candidate vector can be scored per style. "
                         "Additive; absent = byte-identical to the committed baseline.")
    args = ap.parse_args()

    if args.corpora:
        corpora = [c.strip() for c in args.corpora.split(",") if c.strip()]
    elif args.all_new:
        corpora = _all_new()
    else:
        ap.error("pass --all-new or --corpora")

    exe = _find_batch_analyze()
    if exe is None and not args.skip_cpp:
        print("ERROR: batch_analyze not found", file=sys.stderr)
        sys.exit(1)
    bash = _find_git_bash()
    _OUT_ROOT.mkdir(parents=True, exist_ok=True)
    results_path = _OUT_ROOT / "results.json"
    results: dict = {}
    if results_path.exists():
        try:
            results = json.loads(results_path.read_text(encoding="utf-8"))
        except Exception:
            results = {}

    print(f"Corpora ({len(corpora)}): {', '.join(corpora)}")
    for ci, repo in enumerate(corpora, 1):
        t0 = time.time()
        ms3 = _DCML / repo / "MS3"
        hdir = _DCML / repo / "harmonies"
        out_dir = _OUT_ROOT / repo
        out_dir.mkdir(parents=True, exist_ok=True)
        mscx_files = sorted(ms3.glob("*.mscx"))
        if args.limit:
            mscx_files = mscx_files[: args.limit]
        n_ok = n_fail = 0
        for mi, mscx in enumerate(mscx_files, 1):
            out = out_dir / f"{mscx.stem}.ours.json"
            if args.skip_cpp and out.exists():
                n_ok += 1
                continue
            if _run_one(exe, mscx, out, bash, args.timeout, args.param_override):
                n_ok += 1
            else:
                n_fail += 1
        # score
        ps = crn.score_corpus(out_dir, hdir)
        rec: dict = {
            "movements_mscx": len(list(ms3.glob("*.mscx"))),
            "movements_run": len(mscx_files),
            "analyze_ok": n_ok, "analyze_fail": n_fail,
        }
        if ps is not None:
            rn_matched = ps.matched
            rec.update({
                "root_aligned": ps.root_aligned, "root_agree": ps.root_agree,
                "root_agree_pct": _pct(ps.root_agree, ps.root_aligned),
                "rn_matched": rn_matched, "rn_exact": ps.exact, "rn_partial": ps.partial,
                "rn_agree_pct": _pct(ps.exact + ps.partial, rn_matched),
                "key_disagree": ps.key_disagree, "quality_disagree": ps.quality_disagree,
                "root_err": ps.root_err, "movements_scored": ps.movements,
            })
        else:
            rec["score"] = "no_scoreable_pairs"
        if args.grid:
            try:
                gs = crn.grid_score_corpus_tsv(out_dir, hdir)
                if gs:
                    g = {k: v for k, v in vars(gs).items() if isinstance(v, (int, float))}
                    bd = dict(getattr(gs, "bucket_dur", {}) or {})
                    g["bucket_dur"] = bd
                    scored = gs.scored_dur or 0
                    agree_dur = bd.get("exact", 0) + bd.get("partial", 0)
                    g["grid_rn_agree_pct"] = _pct(agree_dur, scored)
                    rootok = agree_dur + bd.get("key_disagree", 0) + bd.get("quality_disagree", 0)
                    g["grid_root_agree_pct"] = _pct(rootok, scored)
                    rec["grid"] = g
                else:
                    rec["grid"] = None
            except Exception as exc:
                rec["grid_error"] = f"{type(exc).__name__}: {exc}"
        rec["elapsed_s"] = round(time.time() - t0, 1)
        results[repo] = rec
        results_path.write_text(json.dumps(results, indent=1), encoding="utf-8")
        ra = rec.get("root_agree_pct", "n/a")
        rn = rec.get("rn_agree_pct", "n/a")
        print(f"[{ci:2d}/{len(corpora)}] {repo:32} ok={n_ok:3d} fail={n_fail:2d} "
              f"root_agree={ra}% rn_agree={rn}% ({rec['elapsed_s']}s)", flush=True)

    print(f"\nDONE. results -> {results_path}")


if __name__ == "__main__":
    main()
