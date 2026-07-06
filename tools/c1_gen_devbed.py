#!/usr/bin/env python3
"""c1_gen_devbed.py — parallel dev-bed fullspine regen for Stage-5 Phase 3 (Task B + rows 4/5).

compare_l6_oracle regenerates the dev-bed fullspine dumps SEQUENTIALLY (~718 movements, one
batch_analyze at a time). This driver does the same dumps in PARALLEL, reusing that module's
primitives verbatim (DEV_BEDS, _corpus_pieces, _run_fullspine via Git Bash — the Qt-safe
launch). Writes {corpus}/{stem}.fullspine.json in place under tools/corpus_l6_oracle (the
default --l6-root c1_reliability + l15_split read), with the current binary (phraseNumVoices).
Read-only diagnostic; no tracked corpus write (tools/corpus_l6_oracle is gitignored).
"""
from __future__ import annotations

import argparse
import concurrent.futures
import multiprocessing
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_l6_oracle as l6

_ROOT = Path(__file__).resolve().parent.parent
L6_ROOT = _ROOT / "tools" / "corpus_l6_oracle"


def _worker(args_tuple):
    exe_s, mscx_s, out_s, bash_s, corpus, stem = args_tuple
    exe, mscx, out = Path(exe_s), Path(mscx_s), Path(out_s)
    bash = Path(bash_s) if bash_s else None
    try:
        ok = l6._run_fullspine(exe, mscx, out, bash, 180, "--dump-fullspine")
    except Exception:
        ok = False
    return (corpus, stem, ok)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=0)
    ap.add_argument("--l6-root", default=str(L6_ROOT))
    args = ap.parse_args()

    exe = l6._find_batch_analyze()
    if exe is None:
        print("ERROR: batch_analyze not found", file=sys.stderr); return 1
    bash = l6._find_git_bash()
    l6_root = Path(args.l6_root)

    work = []
    for corpus in l6.DEV_BEDS:
        cdir = l6_root / corpus
        cdir.mkdir(parents=True, exist_ok=True)
        for stem, mscx, tsv in l6._corpus_pieces(corpus):
            out = cdir / f"{stem}.fullspine.json"
            work.append((str(exe), str(mscx), str(out), str(bash) if bash else "", corpus, stem))

    print(f"Using batch_analyze: {exe}")
    print(f"Dev-bed movements: {len(work)} across {len(l6.DEV_BEDS)} corpora")
    workers = args.workers or min(multiprocessing.cpu_count(), 24)
    print(f"Parallelising over {workers} workers...\n")

    fail = []
    done = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futs = [pool.submit(_worker, w) for w in work]
        for fut in concurrent.futures.as_completed(futs):
            corpus, stem, ok = fut.result()
            done += 1
            if not ok:
                fail.append(f"{corpus}/{stem}")
            if done % 150 == 0:
                print(f"  {done}/{len(work)} done...")

    print(f"\nTOTAL: {len(work)}  FAIL: {len(fail)}")
    if fail:
        print("  fails:", fail[:20])
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
