#!/usr/bin/env python3
"""
rerun_dcml_comparison.py — Re-aggregate existing .ours.json files against
their DCML annotations using both the legacy beat-snap matcher and the new
time-overlap matcher, and report deltas side-by-side.

Usage:
    python tools/rerun_dcml_comparison.py [--bach-corpus DIR] [--cross-corpus-root DIR]

Defaults read:
    Bach chorales:  tools/reports/live_20260515_bach/corpus/  (paired .ours.json
                    + .music21.json)  +  rntxt files in tools/dcml/bach_chorales
                    if available.
    Cross-corpus:   tools/reports/live_20260515/<corpus>_<timestamp>/  paired
                    with the matching DCML TSV files under tools/dcml/<corpus>/.

Output: prints a markdown-formatted report to stdout.  No batch_analyze is
invoked — this script only re-aggregates existing analysis JSONs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import dcml_parser as dcml


REPO_ROOT = Path(__file__).resolve().parent.parent


# ── P5 reporting hygiene (audit L1.1/L1.2/L6.1) ─────────────────────────────
# The default cross-corpus root was a stale, pre-Stage-1/2/3 dir (live_20260515,
# ~5pp low); a no-arg invocation silently re-aggregated it (the accidental
# stale-measurement trap).  Default now points at the HEAD-stamped verify dir,
# and `_check_corpus_freshness` reads each corpus's recorded git_hash and warns
# LOUDLY (or hard-fails under --strict-hash) when it does not match HEAD, so a
# reader can never mistake a 24-day-old number for a current one.

def _git_head_short() -> str | None:
    try:
        out = subprocess.run(["git", "rev-parse", "--short=10", "HEAD"],
                             cwd=str(REPO_ROOT), capture_output=True,
                             text=True, timeout=10)
        return out.stdout.strip() or None
    except Exception:
        return None


def _check_corpus_freshness(root: Path, strict: bool) -> None:
    """Read the git_hash stamp of each corpus report under <root>/reports/ and
    compare to HEAD.  Prints a prominent warning on any mismatch; raises
    SystemExit under --strict-hash.  This closes the audit L1.2 trap (a no-arg
    re-aggregation of a stale corpus reads as a current measurement)."""
    head = _git_head_short()
    reports_dir = root / "reports"
    stamps: dict[str, str] = {}
    if reports_dir.is_dir():
        for jf in sorted(reports_dir.glob("*.json")):
            try:
                stamps[jf.name] = json.loads(jf.read_text(encoding="utf-8")).get("git_hash", "?")
            except Exception:
                stamps[jf.name] = "?"
    distinct = sorted(set(stamps.values()))
    if head is None:
        print("  [freshness] WARNING: could not resolve git HEAD — corpus "
              "git_hash not checked.", file=sys.stderr)
        return
    if not stamps:
        print(f"  [freshness] WARNING: no corpus report stamps found under "
              f"{reports_dir} — cannot verify the .ours.json are at HEAD.",
              file=sys.stderr)
        return
    mismatched = [h for h in distinct if h != head and h != "?"]
    if mismatched or "?" in distinct:
        banner = (
            "  " + "=" * 64 + "\n"
            "  == STALE-MEASUREMENT WARNING (audit L1.2)\n"
            f"  ==   HEAD            : {head}\n"
            f"  ==   corpus git_hash : {', '.join(distinct)}\n"
            "  ==   The .ours.json under this root were NOT produced at HEAD.\n"
            "  ==   The precision numbers below may be stale -- regenerate the\n"
            "  ==   corpus at HEAD, or pass --allow-stale-hash to suppress this.\n"
            "  " + "=" * 64
        )
        print(banner, file=sys.stderr)
        if strict:
            raise SystemExit("  [freshness] --strict-hash: corpus git_hash != HEAD; aborting.")
    else:
        print(f"  [freshness] OK: corpus git_hash == HEAD ({head}).")


# Per-corpus configuration for the 10-corpus cross-corpus run.
# Keys are corpus short names; values describe how to locate the matching
# .ours.json directory and the DCML annotation files.
CROSS_CORPORA = OrderedDict([
    ("dvorak",       {"ours_glob": "dvorak_*",       "tsv_dir": "tools/dcml/dvorak_silhouettes/harmonies"}),
    ("chopin",       {"ours_glob": "chopin_*",       "tsv_dir": "tools/dcml/chopin_mazurkas/harmonies"}),
    ("corelli",      {"ours_glob": "corelli_*",      "tsv_dir": "tools/dcml/corelli/harmonies"}),
    ("mozart",       {"ours_glob": "mozart_*",       "tsv_dir": "tools/dcml/mozart_piano_sonatas/harmonies"}),
    ("schumann",     {"ours_glob": "schumann_*",     "tsv_dir": "tools/dcml/schumann_kinderszenen/harmonies"}),
    ("tchaikovsky",  {"ours_glob": "tchaikovsky_*",  "tsv_dir": "tools/dcml/tchaikovsky_seasons/harmonies"}),
    ("grieg",        {"ours_glob": "grieg_*",        "tsv_dir": "tools/dcml/grieg_lyric_pieces/harmonies"}),
    ("beethoven",    {"ours_glob": "beethoven",      "tsv_dir": "tools/dcml/ABC/harmonies"}),
    ("cpe_bach",     {"ours_glob": "cpe_bach_*",     "tsv_dir": "tools/dcml/cpe_bach_keyboard/harmonies"}),
    ("bach_suites",  {"ours_glob": "bach_suites_*",  "tsv_dir": "tools/dcml/bach_en_fr_suites/harmonies"}),
])


def _find_tsv(tsv_dir: Path, stem: str) -> Path | None:
    """Look up a DCML TSV file by stem.  Handles a few common naming variants."""
    for cand in (f"{stem}.harmonies.tsv", f"{stem}.tsv"):
        p = tsv_dir / cand
        if p.exists():
            return p
    return None


def _aggregate_corpus(ours_dir: Path, tsv_dir: Path, label: str
                       ) -> dict | None:
    """Re-aggregate one corpus's .ours.json files against DCML.  Returns a
    dict of aggregates for both match modes, or None if no usable pairs."""
    if not ours_dir.is_dir() or not tsv_dir.is_dir():
        return None
    ours_files = sorted(ours_dir.glob("*.ours.json"))
    if not ours_files:
        return None

    agg = {
        m: {"total": 0, "aligned": 0, "agree": 0, "disagree": 0,
            "bir_in_disagree": 0, "movements": 0,
            "rn_scoreable": 0, "rn_agree": 0, "rn_disagree": 0,
            "rn_agree_in_root_disagree": 0, "rn_disagree_in_root_agree": 0}
        for m in ("beat-snap", "time-overlap")
    }
    # DCML-anchored metric — denominator is DCML annotations, not our regions.
    anchored = {"total_dcml": 0, "scoreable": 0, "agree": 0, "disagree": 0,
                "no_ours_coverage": 0, "bir_in_disagree": 0, "movements": 0,
                "rn_scoreable": 0, "rn_agree": 0, "rn_disagree": 0,
                "rn_agree_in_root_disagree": 0, "rn_disagree_in_root_agree": 0}

    for p in ours_files:
        stem = p.name.replace(".ours.json", "")
        tsv = _find_tsv(tsv_dir, stem)
        if tsv is None:
            continue
        try:
            _, ours_regions = cmp.load_analysis(p)
        except Exception:
            continue
        try:
            dcml_regions = dcml.parse_abc_harmonies_file(str(tsv))
        except Exception:
            continue
        if not ours_regions or not dcml_regions:
            continue

        for mode in ("beat-snap", "time-overlap"):
            direct = cmp.compare_ours_vs_dcml_direct(ours_regions, dcml_regions,
                                                      mode=mode)
            stats = cmp.dcml_direct_summarize(direct)
            agg[mode]["total"]           += stats["total"]
            agg[mode]["aligned"]         += stats["aligned"]
            agg[mode]["agree"]           += stats["agree"]
            agg[mode]["disagree"]        += stats["disagree"]
            agg[mode]["bir_in_disagree"] += stats["bass_is_root_in_disagree"]
            agg[mode]["rn_scoreable"]    += stats["rn_scoreable"]
            agg[mode]["rn_agree"]        += stats["rn_agree"]
            agg[mode]["rn_disagree"]     += stats["rn_disagree"]
            agg[mode]["rn_agree_in_root_disagree"] += stats["rn_agree_in_root_disagree"]
            agg[mode]["rn_disagree_in_root_agree"] += stats["rn_disagree_in_root_agree"]
            agg[mode]["movements"]       += 1

        anch_rows = cmp.compare_dcml_anchored(ours_regions, dcml_regions)
        anch_stats = cmp.dcml_anchored_summarize(anch_rows)
        anchored["total_dcml"]       += anch_stats["total_dcml"]
        anchored["scoreable"]        += anch_stats["scoreable"]
        anchored["agree"]            += anch_stats["agree"]
        anchored["disagree"]         += anch_stats["disagree"]
        anchored["no_ours_coverage"] += anch_stats["no_ours_coverage"]
        anchored["bir_in_disagree"]  += anch_stats["bass_is_root_in_disagree"]
        anchored["rn_scoreable"]     += anch_stats["rn_scoreable"]
        anchored["rn_agree"]         += anch_stats["rn_agree"]
        anchored["rn_disagree"]      += anch_stats["rn_disagree"]
        anchored["rn_agree_in_root_disagree"] += anch_stats["rn_agree_in_root_disagree"]
        anchored["rn_disagree_in_root_agree"] += anch_stats["rn_disagree_in_root_agree"]
        anchored["movements"]        += 1

    if agg["beat-snap"]["total"] == 0:
        return None
    return {"label": label, "anchored": anchored, **agg}


def _pct(num: int, denom: int) -> float:
    return 100.0 * num / denom if denom else 0.0


def _print_corpus_row(label: str, stats: dict) -> None:
    bs = stats["beat-snap"]
    to = stats["time-overlap"]
    an = stats["anchored"]
    print(f"  {label:14s}  movements={bs['movements']:3d}  ours_total={bs['total']:5d}"
          f"  dcml_total={an['total_dcml']:5d}")
    print(f"    beat-snap          (per-ours) : aligned={bs['aligned']:5d} ({_pct(bs['aligned'], bs['total']):5.1f}%)"
          f"  root_agree={bs['agree']:5d}/{bs['aligned']} ({_pct(bs['agree'], bs['aligned']):5.1f}%)"
          f"  rn_agree={bs['rn_agree']:5d}/{bs['rn_scoreable']} ({_pct(bs['rn_agree'], bs['rn_scoreable']):5.1f}%)")
    print(f"    time-overlap raw   (per-ours) : aligned={to['aligned']:5d} ({_pct(to['aligned'], to['total']):5.1f}%)"
          f"  root_agree={to['agree']:5d}/{to['aligned']} ({_pct(to['agree'], to['aligned']):5.1f}%)"
          f"  rn_agree={to['rn_agree']:5d}/{to['rn_scoreable']} ({_pct(to['rn_agree'], to['rn_scoreable']):5.1f}%)")
    print(f"    DCML-anchored (per-DCML, PRIMARY): coverage={an['scoreable']:5d}/{an['total_dcml']} ({_pct(an['scoreable'], an['total_dcml']):5.1f}%)"
          f"  root_agree={an['agree']:5d}/{an['scoreable']} ({_pct(an['agree'], an['scoreable']):5.1f}%)"
          f"  rn_agree={an['rn_agree']:5d}/{an['rn_scoreable']} ({_pct(an['rn_agree'], an['rn_scoreable']):5.1f}%)"
          f"  bir_err={an['bir_in_disagree']:4d}/{an['disagree']}")
    if an['rn_scoreable'] > 0 or bs['rn_scoreable'] > 0:
        print(f"      RN x root cross-tab (DCML-anchored): rn_agree_in_root_disagree={an['rn_agree_in_root_disagree']:4d}"
              f"  rn_disagree_in_root_agree={an['rn_disagree_in_root_agree']:4d}")


def run_cross_corpus(root: Path) -> dict:
    """Walk a live_<timestamp> directory and re-aggregate every corpus
    sub-directory whose name matches one of CROSS_CORPORA."""
    out: dict[str, dict] = OrderedDict()
    print(f"\n=== Cross-corpus re-aggregation from {root} ===")
    for label, cfg in CROSS_CORPORA.items():
        ours_dir = None
        for cand in sorted(root.glob(cfg["ours_glob"])):
            if cand.is_dir():
                ours_dir = cand
                break
        if ours_dir is None:
            print(f"  {label:14s}  — no .ours.json directory found")
            continue
        tsv_dir = REPO_ROOT / cfg["tsv_dir"]
        stats = _aggregate_corpus(ours_dir, tsv_dir, label)
        if stats is None:
            print(f"  {label:14s}  — no usable .ours/DCML pairs in {ours_dir.name}")
            continue
        out[label] = stats
        _print_corpus_row(label, stats)
    return out


def _weighted_summary(per_corpus: dict[str, dict]) -> dict:
    """Roll up per-corpus aggregates into weighted totals for each mode and
    for the DCML-anchored metric."""
    totals = {
        m: {"total": 0, "aligned": 0, "agree": 0, "disagree": 0,
            "bir_in_disagree": 0, "movements": 0,
            "rn_scoreable": 0, "rn_agree": 0, "rn_disagree": 0,
            "rn_agree_in_root_disagree": 0, "rn_disagree_in_root_agree": 0}
        for m in ("beat-snap", "time-overlap")
    }
    anchored = {"total_dcml": 0, "scoreable": 0, "agree": 0, "disagree": 0,
                "no_ours_coverage": 0, "bir_in_disagree": 0, "movements": 0,
                "rn_scoreable": 0, "rn_agree": 0, "rn_disagree": 0,
                "rn_agree_in_root_disagree": 0, "rn_disagree_in_root_agree": 0}
    for stats in per_corpus.values():
        for m in totals:
            for k in totals[m]:
                totals[m][k] += stats[m][k]
        for k in anchored:
            anchored[k] += stats["anchored"][k]
    totals["anchored"] = anchored
    return totals


def run_bach(corpus_dir: Path, dcml_dir: Path | None) -> dict | None:
    """Re-aggregate Bach chorales using the existing music21 + ours pairs.
    music21 alignment uses the standard tick-overlap (unchanged); DCML is
    only included when rntxt annotations are supplied."""
    if not corpus_dir.is_dir():
        return None
    ours_files = sorted(corpus_dir.glob("*.ours.json"))
    if not ours_files:
        return None

    print(f"\n=== Bach chorales re-aggregation from {corpus_dir} ===")

    # music21 alignment is the metric STATUS.md tracks under "region alignment %".
    # Unchanged by this work, but we report it to satisfy the prompt.
    m21_total = 0
    m21_aligned = 0
    m21_full = 0
    m21_near = 0
    m21_rn_diff = 0
    m21_key_diff = 0

    # DCML (rntxt) three-way agreement, computed in both modes.
    dcml_loader = None
    if dcml_dir and dcml_dir.is_dir():
        dcml_loader = dcml_dir

    dcml_agg = {
        m: {"total": 0, "aligned_dcml": 0, "ours_dcml_agree": 0,
            "ours_dcml_disagree": 0, "dcml_with_root": 0,
            "rn_scoreable": 0, "rn_agree": 0, "rn_disagree": 0,
            "movements": 0}
        for m in ("beat-snap", "time-overlap")
    }

    for p in ours_files:
        stem = p.name.replace(".ours.json", "")
        m21_path = p.with_name(stem + ".music21.json")
        if not m21_path.exists():
            continue
        try:
            ours_meta, ours_regions = cmp.load_analysis(p)
            m21_meta, m21_regions = cmp.load_analysis(m21_path)
        except Exception:
            continue

        aligned = cmp.align_regions(ours_regions, m21_regions)
        compared = [cmp.classify(o, t) for o, t in aligned]
        counts = cmp.summarize(compared)
        m21_total   += sum(counts.values())
        m21_aligned += sum(counts.values()) - counts.get("unaligned", 0)
        m21_full    += counts.get("full_agree", 0)
        m21_near    += counts.get("near_agree", 0)
        m21_rn_diff += counts.get("chord_agree_rn_differs", 0)
        m21_key_diff+= counts.get("chord_agree_key_differs", 0)

        # DCML three-way (optional)
        if dcml_loader is not None:
            wir_path = dcml.find_wir_file(str(dcml_loader), stem)
            if wir_path:
                try:
                    dcml_regions = dcml.parse_rntxt_file(wir_path)
                except Exception:
                    dcml_regions = None
                if dcml_regions:
                    for mode in ("beat-snap", "time-overlap"):
                        matches = cmp.align_dcml_regions(ours_regions,
                                                         dcml_regions,
                                                         mode=mode)
                        for our, dr in zip(ours_regions, matches):
                            dcml_agg[mode]["total"] += 1
                            if dr is None:
                                continue
                            dcml_agg[mode]["aligned_dcml"] += 1
                            # Roman numeral comparison (independent of root_pc
                            # resolvability; counts whenever both sides have a
                            # parseable degree base).
                            d_rn = cmp._rn_base_cased(getattr(dr, 'roman_numeral', '') or '')
                            o_rn = cmp._rn_base_cased(our.roman_numeral or '')
                            if d_rn and o_rn:
                                dcml_agg[mode]["rn_scoreable"] += 1
                                if d_rn == o_rn:
                                    dcml_agg[mode]["rn_agree"] += 1
                                else:
                                    dcml_agg[mode]["rn_disagree"] += 1
                            if dr.root_pc is None:
                                continue
                            dcml_agg[mode]["dcml_with_root"] += 1
                            if dr.root_pc == our.root_pc:
                                dcml_agg[mode]["ours_dcml_agree"] += 1
                            else:
                                dcml_agg[mode]["ours_dcml_disagree"] += 1
                    dcml_agg["beat-snap"]["movements"] += 1
                    dcml_agg["time-overlap"]["movements"] += 1

    m21_unaligned = m21_total - m21_aligned
    m21_chord_id = m21_full + m21_rn_diff + m21_key_diff
    overall_agreement = _pct(m21_full + m21_near, m21_total)
    chord_id_on_aligned = _pct(m21_chord_id, m21_aligned)
    region_alignment = _pct(m21_aligned, m21_total)

    print(f"  music21 comparison (tick-overlap, unchanged):")
    print(f"    total regions       : {m21_total}")
    print(f"    aligned             : {m21_aligned} ({region_alignment:.1f}%)")
    print(f"    full+near agreement : {m21_full + m21_near} ({overall_agreement:.1f}%)")
    print(f"    chord-id on aligned : {m21_chord_id}/{m21_aligned} ({chord_id_on_aligned:.1f}%)")

    if dcml_agg["beat-snap"]["movements"] > 0:
        for mode in ("beat-snap", "time-overlap"):
            d = dcml_agg[mode]
            print(f"  DCML rntxt comparison ({mode}):")
            print(f"    movements with DCML : {d['movements']}")
            print(f"    ours regions covered: {d['total']}")
            print(f"    aligned to DCML     : {d['aligned_dcml']} ({_pct(d['aligned_dcml'], d['total']):.1f}%)")
            print(f"    DCML root resolved  : {d['dcml_with_root']}")
            print(f"    ours/DCML root_agree: {d['ours_dcml_agree']}/{d['dcml_with_root']} ({_pct(d['ours_dcml_agree'], d['dcml_with_root']):.1f}%)")
            print(f"    ours/DCML rn_agree  : {d['rn_agree']}/{d['rn_scoreable']} ({_pct(d['rn_agree'], d['rn_scoreable']):.1f}%)  (case-sensitive degree base)")
    else:
        print("  DCML rntxt comparison: no rntxt annotations found (skipped)")

    return {
        "m21_total": m21_total,
        "m21_aligned": m21_aligned,
        "m21_full_plus_near": m21_full + m21_near,
        "m21_chord_id_on_aligned": m21_chord_id,
        "region_alignment_pct": region_alignment,
        "overall_agreement_pct": overall_agreement,
        "chord_id_on_aligned_pct": chord_id_on_aligned,
        "dcml": dcml_agg,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bach-corpus",
                    default="tools/reports/live_head_verify/corpus",
                    help="Bach chorales corpus directory containing paired"
                         " .ours.json + .music21.json files")
    ap.add_argument("--bach-dcml",
                    default=None,
                    help="Optional directory of DCML rntxt files for the"
                         " three-way Bach comparison")
    ap.add_argument("--cross-corpus-root",
                    default="tools/reports/live_head_verify",
                    help="Root directory of cross-corpus .ours.json output"
                         " subdirectories (default: the HEAD-stamped verify dir,"
                         " not the old live_20260515 — audit L1.2).")
    ap.add_argument("--allow-stale-hash", action="store_true",
                    help="Suppress the stale-measurement warning when the corpus"
                         " git_hash differs from HEAD (the numbers may be stale).")
    ap.add_argument("--strict-hash", action="store_true",
                    help="Hard-fail (exit nonzero) if the corpus git_hash differs"
                         " from HEAD, for CI/automated measurement.")
    args = ap.parse_args()

    bach_corpus = (REPO_ROOT / args.bach_corpus).resolve()
    cross_root = (REPO_ROOT / args.cross_corpus_root).resolve()
    bach_dcml = (REPO_ROOT / args.bach_dcml).resolve() if args.bach_dcml else None

    # P5: surface corpus freshness before any number is printed.
    if not args.allow_stale_hash:
        _check_corpus_freshness(cross_root, strict=args.strict_hash)

    print("\n[coverage] DCML-anchored denominators below are the FULL annotation"
          "\n           set (every harmonized onset), NOT the downbeat-only subset"
          "\n           the pre-P0 parser scored -- post-fix GT volume is ~2.4x the"
          "\n           old count (audit P0/L6.1).")

    bach = run_bach(bach_corpus, bach_dcml)
    cross = run_cross_corpus(cross_root)

    if cross:
        print("\n=== Cross-corpus weighted aggregate ===")
        totals = _weighted_summary(cross)
        for mode in ("beat-snap", "time-overlap"):
            t = totals[mode]
            align_pct = _pct(t["aligned"], t["total"])
            agree_pct = _pct(t["agree"], t["aligned"])
            print(f"  {mode:13s}  (per-ours): movements={t['movements']:4d}  total_ours={t['total']:6d}"
                  f"  aligned={t['aligned']:6d} ({align_pct:5.1f}%)"
                  f"  root_agree={t['agree']:6d}/{t['aligned']} ({agree_pct:5.1f}%)"
                  f"  rn_agree={t['rn_agree']:6d}/{t['rn_scoreable']} ({_pct(t['rn_agree'], t['rn_scoreable']):5.1f}%)"
                  f"  bir_err={t['bir_in_disagree']:5d}/{t['disagree']}")
        an = totals["anchored"]
        print(f"  DCML-anchored (per-DCML, PRIMARY): movements={an['movements']:4d}"
              f"  dcml_total={an['total_dcml']:6d}"
              f"  coverage={an['scoreable']:6d} ({_pct(an['scoreable'], an['total_dcml']):5.1f}%)"
              f"  root_agree={an['agree']:6d}/{an['scoreable']} ({_pct(an['agree'], an['scoreable']):5.1f}%)"
              f"  rn_agree={an['rn_agree']:6d}/{an['rn_scoreable']} ({_pct(an['rn_agree'], an['rn_scoreable']):5.1f}%)"
              f"  bir_err={an['bir_in_disagree']:5d}/{an['disagree']}")
        print(f"    RN x root cross-tab (DCML-anchored): rn_agree_in_root_disagree={an['rn_agree_in_root_disagree']:5d}"
              f"  rn_disagree_in_root_agree={an['rn_disagree_in_root_agree']:5d}")


if __name__ == "__main__":
    main()
