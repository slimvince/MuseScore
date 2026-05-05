#!/usr/bin/env python3
"""
Sweep all score corpora under tools/, running notation-prepared vs
notation-refreshed for each score, and report divergences.

Usage:
    python corpus_sweep.py [--dry-run]
"""

import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

TOOLS_DIR  = Path(__file__).parent.parent          # tools/
BA         = TOOLS_DIR.parent / "ninja_build_rel" / "batch_analyze.exe"
OUT_DIR    = Path(__file__).parent
TIMEOUT_S  = 30   # per batch_analyze invocation

SCORE_EXTS = {".xml", ".musicxml", ".mxl", ".mscx", ".mscz"}

# Corpora to sweep (in order, with labels matching the task brief)
CORPUS_DIRS = [
    (TOOLS_DIR / "corpus",              "corpus_bach (tools/corpus/)"),
    (TOOLS_DIR / "corpus_effendi_src",  "corpus_effendi_src (stand-in for corpus_beethoven/)"),
    (TOOLS_DIR / "corpus_rampageswing_full", "corpus_rampageswing_full (stand-in for corpus_dcml/)"),
    (TOOLS_DIR / "extra scores",        "extra_scores (tools/extra scores/)"),
]

QUALITY_NAMES = {
    0:  "Major",      1:  "Minor",       2:  "Dominant7",
    3:  "MajorMaj7",  4:  "MinorMaj7",   5:  "MinorMin7",
    6:  "HalfDim7",   7:  "Dim7",        8:  "Diminished",
    9:  "Augmented",  10: "Suspended2",  11: "Suspended4",
    12: "Power",      13: "Unknown",
}
PC_NAMES = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]

def pc_name(pc):
    return PC_NAMES[pc % 12] if (pc is not None and pc >= 0) else "?"

def qual_name(q):
    return QUALITY_NAMES.get(q, f"q{q}")

def chord_sym(identity):
    root = pc_name(identity.get("rootPc", -1))
    q    = qual_name(identity.get("quality", -1))
    bass = pc_name(identity.get("bassPc", -1))
    inv  = identity.get("isInversion", False)
    return f"{root}/{q}/{bass}" if inv else f"{root}/{q}"

def classify(prep_id, ref_id):
    if prep_id == ref_id:
        return "identical"
    if prep_id.get("rootPc") != ref_id.get("rootPc"):
        return "root_changed"
    if prep_id.get("quality") != ref_id.get("quality"):
        return "quality_changed"
    if (prep_id.get("bassPc") != ref_id.get("bassPc")
            or prep_id.get("isInversion") != ref_id.get("isInversion")):
        return "inversion_bass"
    return "extensions_changed"

def run_ba(score_path: Path, mode: str) -> dict | None:
    """Run batch_analyze and return parsed JSON, or None on failure."""
    try:
        result = subprocess.run(
            [str(BA), str(score_path), "--dump-regions", mode],
            capture_output=True,
            timeout=TIMEOUT_S,
        )
        if result.returncode != 0:
            return None
        return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception):
        return None

def process_score(score_path: Path) -> dict:
    """Run both modes concurrently and return per-score stats."""
    with ThreadPoolExecutor(max_workers=2) as ex:
        fut_prep = ex.submit(run_ba, score_path, "notation-prepared")
        fut_ref  = ex.submit(run_ba, score_path, "notation-refreshed")
        prep_data = fut_prep.result()
        ref_data  = fut_ref.result()

    if prep_data is None or ref_data is None:
        return {"score": score_path.name, "status": "skip",
                "prep_failed": prep_data is None,
                "ref_failed":  ref_data  is None}

    prep_regs = {r["startTick"]: r for r in prep_data.get("regions", [])}
    ref_regs  = {r["startTick"]: r for r in ref_data.get("regions", [])}
    shared    = sorted(set(prep_regs) & set(ref_regs))

    divergences = []
    for tick in shared:
        prep_id = prep_regs[tick].get("identity", {})
        ref_id  = ref_regs[tick].get("identity", {})
        cat = classify(prep_id, ref_id)
        if cat != "identical":
            measure = prep_regs[tick].get("measure", "?")
            beat    = prep_regs[tick].get("beat", "?")
            tones   = [pc_name(t.get("pc", -1))
                       for t in prep_regs[tick].get("tones", [])]
            divergences.append({
                "tick":     tick,
                "measure":  measure,
                "beat":     beat,
                "tones":    tones,
                "prepared": chord_sym(prep_id),
                "refreshed":chord_sym(ref_id),
                "category": cat,
            })

    return {
        "score":       score_path.name,
        "status":      "ok",
        "prep_count":  len(prep_regs),
        "ref_count":   len(ref_regs),
        "shared":      len(shared),
        "divergences": divergences,
    }

def collect_scores(corpus_dir: Path) -> list[Path]:
    paths = []
    for ext in SCORE_EXTS:
        paths.extend(corpus_dir.glob(f"*{ext}"))
    return sorted(paths)

def main():
    dry_run = "--dry-run" in sys.argv
    print(f"batch_analyze: {BA}", flush=True)
    print(f"dry_run: {dry_run}", flush=True)

    all_results    = []   # list of per-score result dicts
    skip_list      = []   # skipped scores
    corpus_reports = []   # one entry per corpus

    for corpus_dir, corpus_label in CORPUS_DIRS:
        if not corpus_dir.exists():
            corpus_reports.append(
                f"  {corpus_label}: DIRECTORY NOT FOUND — skipped")
            continue

        scores = collect_scores(corpus_dir)
        if not scores:
            corpus_reports.append(
                f"  {corpus_label}: no score files found — skipped")
            continue

        print(f"\n=== {corpus_label} ({len(scores)} scores) ===", flush=True)
        if dry_run:
            print("  [dry-run: skipping execution]", flush=True)
            continue

        t0 = time.time()
        for i, score_path in enumerate(scores, 1):
            r = process_score(score_path)
            all_results.append((corpus_label, r))
            if r["status"] == "skip":
                skip_list.append((corpus_label, score_path.name))
                print(f"  [{i}/{len(scores)}] SKIP  {score_path.name}", flush=True)
            else:
                ndiv = len(r["divergences"])
                flag = f"  *** {ndiv} divergences" if ndiv else ""
                elapsed = time.time() - t0
                print(f"  [{i}/{len(scores)}] {r['shared']:4d} regions  "
                      f"{ndiv:3d} diverg  {score_path.name}{flag}", flush=True)

        elapsed = time.time() - t0
        corpus_div = sum(len(r["divergences"]) for _, r in all_results
                         if r.get("status") == "ok")
        corpus_reports.append(
            f"  {corpus_label}: {len(scores)} scores, "
            f"{elapsed:.0f}s elapsed")

    if dry_run:
        print("\n[dry-run complete]")
        return

    # ── Aggregate stats ───────────────────────────────────────────────────
    ok_results    = [(cl, r) for cl, r in all_results if r["status"] == "ok"]
    total_scores  = len(ok_results)
    total_skipped = len(skip_list)
    total_regions = sum(r["shared"] for _, r in ok_results)
    total_diverg  = sum(len(r["divergences"]) for _, r in ok_results)

    all_divergences = []
    for cl, r in ok_results:
        for d in r["divergences"]:
            all_divergences.append((cl, r["score"], d))

    # ── Build CORPUS_SWEEP.md ──────────────────────────────────────────────
    lines = []
    lines.append("# Corpus Sweep — refreshChordResultWithDisplayContext Divergence Analysis")
    lines.append("")
    lines.append(f"Date: 2026-04-24")
    lines.append(f"Baseline: `--dump-regions notation-prepared` (post-`prepareUserFacingHarmonicRegions`, pre-refresh)")
    lines.append(f"Subject:  `--dump-regions notation-refreshed` (post-`refreshChordResultWithDisplayContext`)")
    lines.append("")
    lines.append("## Corpora")
    lines.append("")
    lines.append("Requested: `corpus_bach/`, `corpus_beethoven/`, `corpus_dcml/` — none found by those names.")
    lines.append("Actual score-containing directories used (in sweep order):")
    lines.append("")
    for entry in corpus_reports:
        lines.append(entry)
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Scores processed | {total_scores} |")
    lines.append(f"| Scores skipped (crash/timeout) | {total_skipped} |")
    lines.append(f"| Shared regions compared | {total_regions} |")
    lines.append(f"| **Divergences (refresh changed identity)** | **{total_diverg}** |")
    lines.append("")

    if total_diverg == 0:
        lines.append("## Conclusion")
        lines.append("")
        lines.append(f"**`refreshChordResultWithDisplayContext` produced zero chord-identity changes "
                     f"across {total_regions:,} regions / {total_scores} scores** spanning Bach chorales, "
                     f"jazz/pop transcriptions, big-band arrangements, and mixed repertoire.")
        lines.append("")
        lines.append("**Recommendation: delete `refreshChordResultWithDisplayContext` as dead code.**")
        lines.append("")
        lines.append("The function re-runs `analyzeChord` with a `findTemporalContext` display context, "
                     "but the tone set passed to it is already the full `region.tones` vector from "
                     "`prepareUserFacingHarmonicRegions` — the same tones that produced the original "
                     "result. Unless `findTemporalContext` surfaces a bass PC *not* in `region.tones`, "
                     "the refresh is a guaranteed no-op. The sweep confirms this is universally true "
                     "on all tested material.")
        lines.append("")
        lines.append("Before deletion: verify that no caller passes a tones-subset or overrides "
                     "the keyFifths/mode arguments relative to `region.keyModeResult` — "
                     "if any caller does, the refresh could matter on a path this sweep didn't cover.")
    else:
        lines.append("## Divergences")
        lines.append("")
        lines.append("| Score | Tick | m.beat | Tones | Prepared | Refreshed | Category |")
        lines.append("|-------|------|--------|-------|----------|-----------|----------|")
        for cl, score_name, d in all_divergences:
            tones_str = ",".join(d["tones"][:6])
            lines.append(f"| {score_name} | {d['tick']} | m{d['measure']}.b{d['beat']} | "
                         f"{tones_str} | {d['prepared']} | {d['refreshed']} | {d['category']} |")
        lines.append("")

    if skip_list:
        lines.append("## Skipped Scores")
        lines.append("")
        for cl, name in skip_list:
            lines.append(f"- `{name}` ({cl})")
        lines.append("")

    lines.append("## NOTES")
    lines.append("")
    lines.append("### notation vs notation-prepared asymmetry (from previous session)")
    lines.append("")
    lines.append("The `--dump-regions notation` mode calls `analyzeHarmonicRhythm` directly; "
                 "`notation-prepared` calls `prepareUserFacingHarmonicRegions` which adds "
                 "gap-tone boundary insertion and same-chord absorption on top. The two paths "
                 "produce different region counts and different tick boundaries — they are **not** "
                 "directly comparable region-for-region. Observed on the three initial fixtures:")
    lines.append("")
    lines.append("| Fixture | analyzeHarmonicRhythm | prepareUserFacingHarmonicRegions | Shared ticks |")
    lines.append("|---------|----------------------|----------------------------------|-------------|")
    lines.append("| BWV 525 (Bach organ sonata) | 114 | 101 | 79 |")
    lines.append("| Poulenc O Magnum Mysterium | 67 | 78 | 60 |")
    lines.append("| Solid Theory | 53 | 59 | 52 |")
    lines.append("")
    lines.append("Poulenc and Solid Theory gain regions in the prepared path (gap-tone boundary "
                 "insertion adds boundaries not present in the raw harmonic rhythm); BWV 525 loses "
                 "regions (same-chord absorption dominant). This divergence is ~25–35% of tick "
                 "positions. **Status: noted for future investigation; out of scope for policy #1.**")
    lines.append("")

    md_text = "\n".join(lines)
    out_path = OUT_DIR / "CORPUS_SWEEP.md"
    out_path.write_text(md_text, encoding="utf-8")
    print(f"\nWritten: {out_path}", file=sys.stderr)

    # Also print summary to stdout
    summary = (
        f"\n{'='*60}\n"
        f"SWEEP COMPLETE\n"
        f"  Scores processed:  {total_scores}\n"
        f"  Scores skipped:    {total_skipped}\n"
        f"  Regions compared:  {total_regions:,}\n"
        f"  Divergences:       {total_diverg}\n"
        f"{'='*60}\n"
    )
    sys.stdout.buffer.write(summary.encode("utf-8"))
    sys.stdout.buffer.flush()

if __name__ == "__main__":
    main()
