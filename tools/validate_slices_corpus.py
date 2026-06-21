#!/usr/bin/env python3
"""Layer-2 corpus property-validation driver (DIAGNOSTIC, re-runnable).

Runs the REAL C++ slicer (`batch_analyze --validate-slices`) over the canonical
353-stem music21 Bach-chorale corpus (`tools/corpus/*.xml`) and proves the §2
slice invariants hold on every stem, then aggregates the §3 stats and reconciles
them against the music21 proxy (`C:\\tmp\\l2_slice_probe.py`).

This is a VALIDATION harness only: `--validate-slices` returns before any
analysis runs (the analysis pipeline is never invoked), so real analysis output
is unchanged. The slicer is NOT wired into analysis.

Per-stem invariant checking + stats live in the C++ tool (an INDEPENDENT oracle
recomputed from the note model, not the slicer's internal boundary vector). This
driver only iterates the corpus, collects the per-stem JSON, and aggregates.

On Windows, batch_analyze MUST be launched via Git Bash (a direct Python
subprocess of the Qt headless exe triggers an access violation) — mirrors
run_bach_preset.py.

Usage:
    python tools/validate_slices_corpus.py
        [--batch-analyze PATH] [--corpus-dir tools/corpus]
        [--jobs N] [--out tools/corpus/slice_validation_summary.json]

Exit 0 iff all stems were found AND every stem passed every invariant; nonzero
otherwise (the §5 gate).
"""
import argparse
import json
import platform
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent

# Proxy envelope (music21 proxy, NON-EMPTY slices only — the proxy excluded
# all-rest spans). Used for a sanity reconciliation, NOT an exact gate.
PROXY_MEAN_SLICES_PER_MEASURE = 5.2
PROXY_PER_STEM_MIN = 49
PROXY_PER_STEM_MAX = 391
PROXY_RELEASE_OPENED_NONEMPTY_STEMS = {"bwv375", "bwv392"}


def _find_batch_analyze(hint):
    candidates = ([Path(hint)] if hint else []) + [
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze",
        _REPO_ROOT / "ninja_build" / "batch_analyze",
    ]
    return next((p for p in candidates if p.exists()), None)


def _find_git_bash():
    return next((p for p in [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ] if p.exists()), None)


def _to_unix_path(p):
    s = str(Path(p).resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')


def _run_one(exe, xml_path):
    """Run batch_analyze --validate-slices on one stem; return (rc, parsed_json_or_None, err)."""
    try:
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = (f'{_to_unix_path(exe)} "{_to_unix_path(xml_path)}" --validate-slices')
                r = subprocess.run([str(bash), '-c', cmd],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=180)
            else:
                r = subprocess.run([str(exe), str(xml_path), '--validate-slices'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=180)
        else:
            r = subprocess.run([str(exe), str(xml_path), '--validate-slices'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               timeout=180)
        out = r.stdout.decode('utf-8', 'replace').strip()
        parsed = None
        if out:
            try:
                parsed = json.loads(out)
            except Exception as e:
                return (r.returncode, None,
                        f"unparseable JSON: {e}; raw[:200]={out[:200]!r}")
        return (r.returncode, parsed,
                r.stderr.decode('utf-8', 'replace').strip())
    except subprocess.TimeoutExpired:
        return (-1, None, "timeout")
    except Exception as e:
        return (-1, None, f"exception: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-analyze", default=None)
    ap.add_argument("--corpus-dir", default=str(_REPO_ROOT / "tools" / "corpus"))
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--out", default=str(_REPO_ROOT / "tools" / "corpus"
                                         / "slice_validation_summary.json"))
    args = ap.parse_args()

    # Windows consoles/redirects default to cp1252; this script prints box-drawing
    # and section characters. Force UTF-8 so the run never dies on an encode error.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    exe = _find_batch_analyze(args.batch_analyze)
    if not exe:
        print("ERROR: batch_analyze not found.", file=sys.stderr)
        sys.exit(1)
    print(f"Using batch_analyze: {exe}")

    corpus = Path(args.corpus_dir)
    stems = sorted(corpus.glob("*.xml"))
    print(f"Corpus: {corpus}  ({len(stems)} stems)")
    if not stems:
        print("ERROR: no *.xml stems found in corpus dir.", file=sys.stderr)
        sys.exit(1)

    results = {}      # stem -> parsed json
    load_failures = []  # (stem, rc, err)
    invariant_failures = []  # parsed json with ok=false

    def work(xml):
        rc, parsed, err = _run_one(exe, xml)
        return (xml.stem, rc, parsed, err)

    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for i, (stem, rc, parsed, err) in enumerate(ex.map(work, stems), 1):
            if parsed is None:
                load_failures.append((stem, rc, err))
            else:
                results[stem] = parsed
                if not parsed.get("ok", False):
                    invariant_failures.append(parsed)
            if i % 50 == 0:
                print(f"  ... {i}/{len(stems)}")

    # ── §5 gate: every stem found + every invariant passed. ──────────────────
    n_ok = sum(1 for r in results.values() if r.get("ok"))
    print("\n" + "=" * 70)
    print(f"Stems run: {len(results)}/{len(stems)}   invariant-pass: {n_ok}/{len(stems)}")

    if load_failures:
        print(f"\n!! {len(load_failures)} stem(s) failed to load / produce JSON:")
        for stem, rc, err in load_failures[:20]:
            print(f"   {stem}: rc={rc} {err[:160]}")

    if invariant_failures:
        print(f"\n!! {len(invariant_failures)} stem(s) FAILED an invariant (STOP):")
        for r in invariant_failures[:50]:
            for v in r.get("violations", []):
                print(f"   {r['stem']}: [{v['invariant']}] {v['detail']} "
                      f"(tickA={v['tickA']}, tickB={v['tickB']})")

    # ── §3 stats (over the stems that produced JSON). ────────────────────────
    def agg(key):
        return sum(r.get(key, 0) for r in results.values())

    total_measures = agg("measures")
    total_slices = agg("slicesTotal")
    total_nonempty = agg("slicesNonEmpty")
    total_empty = agg("slicesEmpty")
    total_eligible = agg("eligibleNotes")
    total_relonly_b = agg("releaseOnlyBoundaries")
    total_relopen_ne = agg("releaseOpenedNonEmptySlices")

    per_stem_nonempty = {s: r.get("slicesNonEmpty", 0) for s, r in results.items()}
    stems_with_empty = sorted(s for s, r in results.items() if r.get("slicesEmpty", 0) > 0)
    stems_relopen_ne = sorted(s for s, r in results.items()
                              if r.get("releaseOpenedNonEmptySlices", 0) > 0)

    mean_ne_per_measure = (total_nonempty / total_measures) if total_measures else 0.0

    # performance: pure slicer cost (sliceMs is measured inside the process,
    # parallelism does not distort it).
    slice_ms = {s: r.get("sliceMs", 0.0) for s, r in results.items()}
    worst_stem = max(slice_ms, key=slice_ms.get) if slice_ms else None
    sum_slice_ms = sum(slice_ms.values())

    non_det = sorted(s for s, r in results.items() if not r.get("deterministic", True))

    if per_stem_nonempty:
        mn_s = min(per_stem_nonempty, key=per_stem_nonempty.get)
        mx_s = max(per_stem_nonempty, key=per_stem_nonempty.get)
    else:
        mn_s = mx_s = None

    print("\n── §3 stats (REAL slicer) ──────────────────────────────────────────")
    print(f"  total measures            : {total_measures}")
    print(f"  total eligible notes      : {total_eligible}")
    print(f"  total slices (incl. empty): {total_slices}")
    print(f"  total NON-EMPTY slices    : {total_nonempty}")
    print(f"  total EMPTY slices        : {total_empty}  "
          f"(in {len(stems_with_empty)} stems)")
    print(f"  mean NON-EMPTY / measure  : {mean_ne_per_measure:.2f}   "
          f"(proxy ~{PROXY_MEAN_SLICES_PER_MEASURE})")
    if mn_s:
        print(f"  per-stem NON-EMPTY range  : {per_stem_nonempty[mn_s]} ({mn_s}) .. "
              f"{per_stem_nonempty[mx_s]} ({mx_s})   "
              f"(proxy ~{PROXY_PER_STEM_MIN}..{PROXY_PER_STEM_MAX})")
    print(f"  release-only boundaries   : {total_relonly_b}")
    print(f"  release-opened NON-EMPTY  : {total_relopen_ne}  in stems {stems_relopen_ne}  "
          f"(proxy: 2 in {sorted(PROXY_RELEASE_OPENED_NONEMPTY_STEMS)})")
    print(f"  determinism failures      : {len(non_det)} {non_det if non_det else ''}")
    print(f"  pure slicer time (sum)    : {sum_slice_ms:.2f} ms")
    if worst_stem:
        print(f"  worst single-stem slicer  : {slice_ms[worst_stem]:.3f} ms ({worst_stem})")

    # ── proxy reconciliation flags (order-of-magnitude outliers). ────────────
    outliers = []
    for s, ne in per_stem_nonempty.items():
        if ne and (ne < PROXY_PER_STEM_MIN / 10 or ne > PROXY_PER_STEM_MAX * 10):
            outliers.append((s, ne))
    if outliers:
        print(f"\n  !! {len(outliers)} stem(s) an ORDER OF MAGNITUDE outside the proxy "
              f"envelope (surface):")
        for s, ne in sorted(outliers, key=lambda x: x[1]):
            print(f"     {s}: {ne} non-empty slices")

    summary = {
        "stems_total": len(stems),
        "stems_run": len(results),
        "invariant_pass": n_ok,
        "load_failures": [{"stem": s, "rc": rc, "err": e} for s, rc, e in load_failures],
        "invariant_failures": invariant_failures,
        "totals": {
            "measures": total_measures,
            "eligibleNotes": total_eligible,
            "slicesTotal": total_slices,
            "slicesNonEmpty": total_nonempty,
            "slicesEmpty": total_empty,
            "releaseOnlyBoundaries": total_relonly_b,
            "releaseOpenedNonEmptySlices": total_relopen_ne,
        },
        "meanNonEmptyPerMeasure": round(mean_ne_per_measure, 3),
        "perStemNonEmptyMin": (per_stem_nonempty[mn_s] if mn_s else None),
        "perStemNonEmptyMinStem": mn_s,
        "perStemNonEmptyMax": (per_stem_nonempty[mx_s] if mx_s else None),
        "perStemNonEmptyMaxStem": mx_s,
        "stemsWithEmpty": stems_with_empty,
        "stemsReleaseOpenedNonEmpty": stems_relopen_ne,
        "determinismFailures": non_det,
        "sumSliceMs": round(sum_slice_ms, 3),
        "worstStem": worst_stem,
        "worstStemMs": (round(slice_ms[worst_stem], 4) if worst_stem else None),
        "proxyOutliers": [{"stem": s, "nonEmpty": ne} for s, ne in outliers],
    }
    Path(args.out).write_text(json.dumps(summary, indent=2, sort_keys=True),
                              encoding="utf-8")
    print(f"\nSummary written to {args.out}")

    gate_ok = (len(results) == len(stems)
               and n_ok == len(stems)
               and not load_failures
               and not invariant_failures
               and not non_det)
    print("\nGATE:", "PASS" if gate_ok else "FAIL")
    sys.exit(0 if gate_ok else 1)


if __name__ == "__main__":
    main()
