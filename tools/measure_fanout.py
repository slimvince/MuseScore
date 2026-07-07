#!/usr/bin/env python3
"""measure_fanout.py — Engage arc #8 read-only measurement.

Runs batch_analyze --dump-fanout over the pinned Bach corpus (tools/corpus/*.xml)
for each of the three presets and reports the TRUE untruncated above-threshold
competition fan-out distribution — the ranked-set size Layer 5 will select over,
BEFORE applyHarmonicFunction()'s cap-of-3.

--dump-fanout returns before the standard writeJson, so the standard .ours.json
corpus is untouched; this script writes only throwaway *.fanout.json side files
into a scratch dir. Read-only, no behavior change, no re-baseline.

Reuses run_bach_preset's Git-Bash invocation helpers (no duplication).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import multiprocessing
import statistics
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_bach_preset as rbp

_REPO_ROOT = Path(__file__).resolve().parent.parent
PRESETS = ["Baroque", "Jazz", "Default"]


def _collect_one(args_tuple):
    exe, xml_path, preset, scratch = args_tuple
    stem = xml_path.stem
    out_path = Path(scratch) / f"{preset}_{stem}.fanout.json"
    ok = rbp._run_batch_analyze(exe, xml_path, out_path, preset,
                                diag_fh=None, extra_args="--dump-fanout")
    if not ok or not out_path.exists():
        return (stem, None, "FAILED")
    try:
        data = json.loads(out_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return (stem, None, f"PARSE_ERR:{exc}")
    finally:
        try:
            out_path.unlink()
        except OSError:
            pass
    # Keep only regions that ran a fresh competition (total > 0). total == 0 is an
    # inherited/gap/fallback slice with no independent Layer-5 decision point.
    rows = [(r["fanoutTotal"], r["fanoutAboveThreshold"],
             r["distinctRootsTotal"], r["distinctRootsAbove"])
            for r in data.get("regions", []) if r.get("fanoutTotal", 0) > 0]
    return (stem, rows, "OK")


def _pct(sorted_vals, q):
    if not sorted_vals:
        return 0.0
    idx = min(len(sorted_vals) - 1, int(q * (len(sorted_vals) - 1) + 0.5))
    return sorted_vals[idx]


def _summarize(rows):
    """rows: list of (total, aboveThreshold, distinctRootsTotal, distinctRootsAbove)."""
    n = len(rows)
    total       = [r[0] for r in rows]
    above       = [r[1] for r in rows]
    droots_tot  = [r[2] for r in rows]
    droots_abv  = [r[3] for r in rows]
    above_s     = sorted(above)
    total_s     = sorted(total)
    droots_abv_s = sorted(droots_abv)

    def hist(vals, cap=12):
        h = {}
        for v in vals:
            k = v if v <= cap else f">{cap}"
            h[k] = h.get(k, 0) + 1
        return h

    def frac(vals, thr):
        return sum(1 for v in vals if v > thr) / n if n else 0.0

    return {
        "n_competition_slices": n,
        "above_threshold": {
            "min": min(above) if above else 0,
            "median": statistics.median(above) if above else 0,
            "mean": round(statistics.mean(above), 4) if above else 0,
            "p90": _pct(above_s, 0.90),
            "p99": _pct(above_s, 0.99),
            "max": max(above) if above else 0,
            "histogram": hist(above),
        },
        "total_fanout": {
            "min": min(total) if total else 0,
            "median": statistics.median(total) if total else 0,
            "mean": round(statistics.mean(total), 4) if total else 0,
            "p90": _pct(total_s, 0.90),
            "p99": _pct(total_s, 0.99),
            "max": max(total) if total else 0,
            "histogram": hist(total),
        },
        "truncation_impact_above_threshold": {
            "frac_gt_2": round(frac(above, 2), 4),
            "frac_gt_3": round(frac(above, 3), 4),
            "frac_gt_5": round(frac(above, 5), 4),
            "frac_gt_10": round(frac(above, 10), 4),
            "count_gt_2": sum(1 for v in above if v > 2),
            "count_gt_3": sum(1 for v in above if v > 3),
            "count_gt_5": sum(1 for v in above if v > 5),
            "count_gt_10": sum(1 for v in above if v > 10),
        },
        "distinct_roots_above": {
            "min": min(droots_abv) if droots_abv else 0,
            "median": statistics.median(droots_abv) if droots_abv else 0,
            "mean": round(statistics.mean(droots_abv), 4) if droots_abv else 0,
            "p90": _pct(droots_abv_s, 0.90),
            "max": max(droots_abv) if droots_abv else 0,
            "histogram": hist(droots_abv, cap=6),
            # Fraction of above-threshold slices offering >1 genuinely-different root
            "frac_multiroot": round(
                sum(1 for v in droots_abv if v > 1) / n, 4) if n else 0.0,
        },
        "distinct_roots_total_mean": round(statistics.mean(droots_tot), 4) if droots_tot else 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-analyze", metavar="PATH")
    ap.add_argument("--corpus-dir", default="tools/corpus")
    ap.add_argument("--out", metavar="FILE", help="write the JSON report here")
    args = ap.parse_args()

    exe = rbp._find_batch_analyze(args.batch_analyze)
    if exe is None:
        print("ERROR: batch_analyze not found", file=sys.stderr)
        sys.exit(1)
    print(f"Using batch_analyze: {exe}")

    corpus_dir = Path(args.corpus_dir)
    xml_files = sorted(f for f in corpus_dir.glob("*.xml")
                       if not f.stem.endswith("_m21"))
    if not xml_files:
        print(f"ERROR: no .xml in {corpus_dir}", file=sys.stderr)
        sys.exit(1)
    print(f"Corpus: {len(xml_files)} scores × {len(PRESETS)} presets")

    report = {
        "git_hash": rbp._get_git_hash(),
        "corpus_git_hash": None,
        "n_scores": len(xml_files),
        "presets": {},
    }
    # copy through the pinned corpus hash if a manifest is present
    for d in ("baroque",):
        mp = corpus_dir / d / "corpus_manifest.json"
        if mp.exists():
            report["corpus_git_hash"] = json.loads(mp.read_text())["git_hash"]

    workers = min(multiprocessing.cpu_count(), len(xml_files))
    with tempfile.TemporaryDirectory() as scratch:
        for preset in PRESETS:
            print(f"\n=== preset {preset} ===")
            work = [(exe, xml, preset, scratch) for xml in xml_files]
            all_rows = []
            failed = []
            done = 0
            with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
                futs = {pool.submit(_collect_one, w): w[1].stem for w in work}
                for fut in concurrent.futures.as_completed(futs):
                    stem, rows, status = fut.result()
                    done += 1
                    if status != "OK":
                        failed.append((stem, status))
                    else:
                        all_rows.extend(rows)
                    if done % 50 == 0:
                        print(f"  {done}/{len(work)} ...")
            summ = _summarize(all_rows)
            summ["scores_failed"] = failed
            report["presets"][preset] = summ
            at = summ["above_threshold"]
            ti = summ["truncation_impact_above_threshold"]
            print(f"  competition slices: {summ['n_competition_slices']}")
            print(f"  above-threshold: min={at['min']} median={at['median']} "
                  f"mean={at['mean']} p90={at['p90']} p99={at['p99']} max={at['max']}")
            print(f"  truncation (>2 cap bites): {ti['frac_gt_2']:.1%}  "
                  f">3: {ti['frac_gt_3']:.1%}  >5: {ti['frac_gt_5']:.1%}  "
                  f">10: {ti['frac_gt_10']:.1%}")
            print(f"  distinct-roots-above mean={summ['distinct_roots_above']['mean']} "
                  f"multi-root slices={summ['distinct_roots_above']['frac_multiroot']:.1%}")
            if failed:
                print(f"  FAILED {len(failed)}: {failed[:5]}")

    out = args.out or str(_REPO_ROOT / "tools" / "reports" / "fanout_measure.json")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nReport → {out}")


if __name__ == "__main__":
    main()
