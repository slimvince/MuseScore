#!/usr/bin/env python3
# Python interpreter: C:\s\MS\.venv\Scripts\python.exe
"""corpus_comparison.py — Aggregate plugin-vs-analyzer statistics across all scores.

Reads every *.triage_queue.json in the outputs tree and computes corpus-wide
and per-genre summaries comparing chordIdentifierPopJazz against musescore_analyzer.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_WORKTREE  = Path(__file__).resolve().parents[2]
_OUTPUTS   = _WORKTREE / "outputs"
_MS_ROOT   = Path(r"C:\s\MS")


# ---------------------------------------------------------------------------
# Corpus label from path
# ---------------------------------------------------------------------------

def corpus_label(tq_path: Path, score_path: str) -> str:
    """Assign a short corpus tag using the score's original path."""
    sp = score_path.replace("\\", "/").lower()
    parts = tq_path.parts

    # when_in_rome outputs landed under outputs/Corpus/ (no when_in_rome prefix)
    if "Corpus" in parts and tq_path.stem == "score.triage_queue":
        idx = parts.index("Corpus")
        style = parts[idx + 1] if len(parts) > idx + 1 else "when_in_rome"
        return f"wir/{style}"

    # Derive from the score_path recorded in the response JSON
    if "/dcml/bach_chorales/"   in sp: return "dcml/bach_chorales"
    if "/dcml/corelli/"         in sp: return "dcml/corelli"
    if "/dcml/bach_en_fr_suites/" in sp: return "dcml/bach_suites"
    if "/dcml/abc/"             in sp: return "dcml/beethoven_sq"
    if "/dcml/cpe_bach"         in sp: return "dcml/cpe_bach"
    if "/dcml/grieg"            in sp: return "dcml/grieg"
    if "/dcml/mozart"           in sp: return "dcml/mozart"
    if "/dcml/chopin"           in sp: return "dcml/chopin"
    if "/dcml/schumann"         in sp: return "dcml/schumann"
    if "/dcml/dvorak"           in sp: return "dcml/dvorak"
    if "/dcml/tchaikovsky"      in sp: return "dcml/tchaikovsky"
    if "/corpus_effendi"        in sp: return "jazz/effendi"
    if "/corpus_omnibook"       in sp: return "jazz/omnibook"
    if "/corpus_rampageswing"   in sp: return "jazz/rampageswing"
    if "/pdmx/"                 in sp: return "jazz/pdmx"
    if "/tools/corpus/"         in sp: return "bach_m21"
    if "/extra scores/hiromi/"  in sp: return "extra/hiromi"
    if "/extra scores/steely"   in sp: return "extra/steelydan"
    if "/extra scores/piazzolla" in sp: return "extra/piazzolla"
    if "/extra scores/"         in sp: return "extra/jazz_mix"
    return "other"


# ---------------------------------------------------------------------------
# Load region counts from response files
# ---------------------------------------------------------------------------

def region_counts(tq_path: Path, basename: str) -> tuple[int, int]:
    """Return (analyzer_regions, plugin_regions) from response JSON files."""
    out_dir = tq_path.parent
    a_path = out_dir / f"{basename}.analyzer_response.json"
    p_path = out_dir / f"{basename}.chordIdentifierPopJazz_response.json"
    a_n = p_n = 0
    for path, var in [(a_path, "a_n"), (p_path, "p_n")]:
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
            n = len(d.get("tool_input", {}).get("judgments", []))
            if var == "a_n":
                a_n = n
            else:
                p_n = n
        except Exception:
            pass
    return a_n, p_n


# ---------------------------------------------------------------------------
# Main aggregation
# ---------------------------------------------------------------------------

def main() -> None:
    # Find all triage_queue.json files (flat outputs + when_in_rome subdirs)
    all_tq = list(_OUTPUTS.rglob("*.triage_queue.json"))
    print(f"Found {len(all_tq)} triage_queue.json files\n")

    # Counters
    total_scores            = 0
    total_cells             = 0
    total_flagged           = 0
    total_analyzer_regions  = 0
    total_plugin_regions    = 0
    issue_totals: dict[str, int] = defaultdict(int)

    # Two-source only (analyzer + plugin, no LLMs)
    two_src_scores          = 0
    two_src_cells           = 0
    two_src_flagged         = 0
    two_src_issue: dict[str, int] = defaultdict(int)

    # Per-corpus breakdown
    corpus_stats: dict[str, dict] = defaultdict(lambda: {
        "scores": 0, "cells": 0, "flagged": 0,
        "analyzer_regions": 0, "plugin_regions": 0,
        "issue": defaultdict(int),
    })

    # Root/quality agreement among entries where BOTH sources present
    both_present    = 0
    root_agree      = 0
    quality_agree   = 0
    exact_match     = 0

    for tq_path in sorted(all_tq):
        try:
            d = json.loads(tq_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        basename = d.get("score_basename", tq_path.stem.split(".triage_queue")[0])
        sources  = d.get("sources", [])
        summary  = d.get("summary", {})
        entries  = d.get("entries", [])

        cells   = summary.get("total_cells", 0)
        flagged = summary.get("flagged", 0)
        by_type = summary.get("by_issue_type", {})

        a_n, p_n = region_counts(tq_path, basename)

        # Get score_path from analyzer response for corpus labelling
        ap = tq_path.parent / f"{basename}.analyzer_response.json"
        score_path = ""
        try:
            ad = json.loads(ap.read_text(encoding="utf-8"))
            score_path = ad.get("metadata", {}).get("score_path", "")
        except Exception:
            pass
        label = corpus_label(tq_path, score_path)

        total_scores           += 1
        total_cells            += cells
        total_flagged          += flagged
        total_analyzer_regions += a_n
        total_plugin_regions   += p_n
        for k, v in by_type.items():
            issue_totals[k] += v

        cs = corpus_stats[label]
        cs["scores"]           += 1
        cs["cells"]            += cells
        cs["flagged"]          += flagged
        cs["analyzer_regions"] += a_n
        cs["plugin_regions"]   += p_n
        for k, v in by_type.items():
            cs["issue"][k] += v

        # Two-source only (sources is a list of dicts with 'provider' key)
        provider_names = {s.get("provider", "") for s in sources if isinstance(s, dict)}
        has_llm = bool(provider_names & {"claude", "gemini", "openai"})
        if not has_llm:
            two_src_scores  += 1
            two_src_cells   += cells
            two_src_flagged += flagged
            for k, v in by_type.items():
                two_src_issue[k] += v

        # Per-entry agreement (both sources present)
        for e in entries:
            srcs = e.get("sources", {})
            a = srcs.get("musescore_analyzer")
            p = srcs.get("chordIdentifierPopJazz")
            if a is None or p is None:
                continue
            both_present += 1
            ap = (a.get("parsed") or {})
            pp = (p.get("parsed") or {})
            if ap.get("root_pc") == pp.get("root_pc"):
                root_agree += 1
            if ap.get("root_pc") == pp.get("root_pc") and \
               ap.get("quality") == pp.get("quality"):
                quality_agree += 1
            axes = e.get("axes", {})
            if axes.get("exact_match"):
                exact_match += 1

    # ---------------------------------------------------------------------------
    # Print report
    # ---------------------------------------------------------------------------

    pct = lambda n, d: f"{100*n/d:.1f}%" if d else "n/a"

    print("=" * 65)
    print("CORPUS-WIDE SUMMARY (all sources)")
    print("=" * 65)
    print(f"  Scores processed         : {total_scores:,}")
    print(f"  Total comparison cells   : {total_cells:,}")
    print(f"  Flagged cells            : {total_flagged:,}  ({pct(total_flagged, total_cells)})")
    print(f"  All-agree cells          : {issue_totals.get('all_agree', 0):,}  ({pct(issue_totals.get('all_agree', 0), total_cells)})")
    print()
    print(f"  Analyzer regions (total) : {total_analyzer_regions:,}")
    print(f"  Plugin regions  (total)  : {total_plugin_regions:,}")
    ratio = total_plugin_regions / total_analyzer_regions if total_analyzer_regions else 0
    print(f"  Plugin/analyzer ratio    : {ratio:.1f}x")
    print()

    print("Issue-type breakdown (all scores):")
    for k, v in sorted(issue_totals.items(), key=lambda x: -x[1]):
        print(f"  {k:<40} {v:>7,}  ({pct(v, total_cells)})")
    print()

    print("=" * 65)
    print("TWO-SOURCE ONLY (analyzer + plugin, no LLMs)")
    print("=" * 65)
    print(f"  Scores   : {two_src_scores:,}")
    print(f"  Cells    : {two_src_cells:,}  flagged={two_src_flagged:,}  ({pct(two_src_flagged, two_src_cells)})")
    print(f"  All-agree: {two_src_issue.get('all_agree',0):,}  ({pct(two_src_issue.get('all_agree',0), two_src_cells)})")
    print()
    print("  Issue breakdown:")
    for k, v in sorted(two_src_issue.items(), key=lambda x: -x[1]):
        print(f"    {k:<40} {v:>7,}  ({pct(v, two_src_cells)})")
    print()

    print("=" * 65)
    print("CELL-LEVEL AGREEMENT (both sources present, any score)")
    print("=" * 65)
    print(f"  Cells with both sources  : {both_present:,}")
    print(f"  Root agreement           : {root_agree:,}  ({pct(root_agree, both_present)})")
    print(f"  Root+quality agreement   : {quality_agree:,}  ({pct(quality_agree, both_present)})")
    print(f"  Exact match              : {exact_match:,}  ({pct(exact_match, both_present)})")
    print()

    print("=" * 65)
    print("PER-CORPUS BREAKDOWN (top 20 by score count)")
    print("=" * 65)
    sorted_corpora = sorted(corpus_stats.items(), key=lambda x: -x[1]["scores"])
    print(f"  {'Corpus':<40} {'Scores':>6} {'Cells':>7} {'Agree%':>7} {'Ratio':>6}")
    print(f"  {'-'*40} {'-'*6} {'-'*7} {'-'*7} {'-'*6}")
    for label, cs in sorted_corpora[:20]:
        agree_pct = 100 * cs["issue"].get("all_agree", 0) / cs["cells"] if cs["cells"] else 0
        pr = cs["plugin_regions"]
        ar = cs["analyzer_regions"]
        r = pr / ar if ar else 0
        print(f"  {label:<40} {cs['scores']:>6,} {cs['cells']:>7,} {agree_pct:>6.1f}% {r:>5.1f}x")


if __name__ == "__main__":
    main()
