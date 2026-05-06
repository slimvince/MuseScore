#!/usr/bin/env python3
"""
Compare notation-prepared vs notation-refreshed region dumps.

The 'prepared' mode runs prepareUserFacingHarmonicRegions without any refresh.
The 'refreshed' mode applies refreshChordResultWithDisplayContext on top.
Both use the same segmentation, so this comparison isolates the refresh effect.

A secondary note on the 'notation' (analyzeHarmonicRhythm) vs 'refreshed' comparison
is included at the end to document how many region-boundary differences arise from
the merge/absorption step in prepareUserFacingHarmonicRegions.
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent

FIXTURES = [
    {
        "label":    "BWV 525 (Bach organ sonata)",
        "prepared": "bwv525_prepared.json",
        "refreshed":"bwv525_refreshed.json",
        "raw":      "bwv525_raw.json",
    },
    {
        "label":    "Poulenc O Magnum Mysterium",
        "prepared": "poulenc_prepared.json",
        "refreshed":"poulenc_refreshed.json",
        "raw":      "poulenc_raw.json",
    },
    {
        "label":    "Solid Theory (subst. for op01n08d — not found on master)",
        "prepared": "solidtheory_prepared.json",
        "refreshed":"solidtheory_refreshed.json",
        "raw":      "solidtheory_raw.json",
    },
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
    if pc is None or pc < 0:
        return "?"
    return PC_NAMES[pc % 12]

def qual_name(q):
    return QUALITY_NAMES.get(q, f"q{q}")

def chord_sym(identity):
    root = pc_name(identity.get("rootPc", -1))
    q    = qual_name(identity.get("quality", -1))
    bass = pc_name(identity.get("bassPc", -1))
    inv  = identity.get("isInversion", False)
    sym  = f"{root}/{q}"
    if inv:
        sym += f"/{bass}"
    return sym

def classify(prep_id, ref_id):
    if prep_id == ref_id:
        return "identical"
    rr, rq, rb, ri = (prep_id.get("rootPc"), prep_id.get("quality"),
                      prep_id.get("bassPc"), prep_id.get("isInversion", False))
    xr, xq, xb, xi = (ref_id.get("rootPc"),  ref_id.get("quality"),
                      ref_id.get("bassPc"),  ref_id.get("isInversion", False))
    if rr != xr:
        return "root_changed"
    if rq != xq:
        return "quality_changed"
    if rb != xb or ri != xi:
        return "inversion_bass"
    return "extensions_changed"

def load_regions(path):
    with open(path) as f:
        data = json.load(f)
    return {r["startTick"]: r for r in data.get("regions", [])}

def compare_pair(label, prep_path, ref_path, raw_path):
    if not prep_path.exists() or not ref_path.exists():
        return f"=== {label} ===\nFILE NOT FOUND\n", None

    prep_regs = load_regions(prep_path)
    ref_regs  = load_regions(ref_path)
    raw_regs  = load_regions(raw_path) if raw_path.exists() else {}

    shared_ticks = sorted(set(prep_regs) & set(ref_regs))
    prep_only = len(set(prep_regs) - set(ref_regs))
    ref_only  = len(set(ref_regs)  - set(prep_regs))

    counts = {"identical": 0, "inversion_bass": 0, "quality_changed": 0,
              "root_changed": 0, "extensions_changed": 0}
    samples = []

    for tick in shared_ticks:
        prep_r = prep_regs[tick]
        ref_r  = ref_regs[tick]
        prep_id = prep_r.get("identity", {})
        ref_id  = ref_r.get("identity", {})
        cat = classify(prep_id, ref_id)
        counts[cat] += 1
        if cat != "identical":
            measure = prep_r.get("measure", "?")
            beat    = prep_r.get("beat", "?")
            samples.append((measure, beat, tick, prep_id, ref_id, cat))

    total = len(shared_ticks)
    changed = total - counts["identical"]
    pct = lambda n: f"{100*n/total:.1f}" if total else "0.0"

    lines = [f"=== {label} ==="]
    lines.append(f"Regions in prepared path:           {len(prep_regs)}")
    lines.append(f"Regions in refreshed path:          {len(ref_regs)}")
    lines.append(f"Shared ticks (comparable):          {total}")
    lines.append(f"  Prepared-only (absorbed in refreshed): {prep_only}")
    lines.append(f"  Refreshed-only (new in refreshed):     {ref_only}")
    lines.append("")
    lines.append(f"Among shared regions:")
    lines.append(f"  Identical:              {counts['identical']} ({pct(counts['identical'])}%)")
    lines.append(f"  Inversion/bass changed: {counts['inversion_bass']} ({pct(counts['inversion_bass'])}%)")
    lines.append(f"  Quality changed:        {counts['quality_changed']} ({pct(counts['quality_changed'])}%)")
    lines.append(f"  Root changed:           {counts['root_changed']} ({pct(counts['root_changed'])}%)")
    lines.append(f"  Extensions changed:     {counts['extensions_changed']} ({pct(counts['extensions_changed'])}%)")
    lines.append("")

    # analyzeHarmonicRhythm vs prepareUserFacingHarmonicRegions boundary note
    if raw_regs:
        raw_shared = len(set(raw_regs) & set(prep_regs))
        lines.append(f"[Note] analyzeHarmonicRhythm regions: {len(raw_regs)}  "
                     f"vs prepareUserFacingHarmonicRegions: {len(prep_regs)}  "
                     f"(shared ticks: {raw_shared})")
        lines.append("")

    samples.sort(key=lambda x: (int(x[0]) if str(x[0]).isdigit() else 9999,
                                 float(x[1]) if str(x[1]).replace('.','',1).isdigit() else 0))
    n_show = min(5, len(samples))
    if n_show:
        lines.append(f"Sample (first {n_show} non-identical, by measure):")
        for measure, beat, tick, prep_id, ref_id, cat in samples[:n_show]:
            lines.append(f"  m{measure}.b{beat}: "
                         f"prepared {chord_sym(prep_id)} "
                         f"→ refreshed {chord_sym(ref_id)}  [class: {cat}]")
    else:
        lines.append("No identity divergences among shared regions.")
    lines.append("")
    return "\n".join(lines), (counts, total, changed)


def main():
    all_output = []
    aggregate_total   = 0
    aggregate_changed = 0
    class_totals = {"identical": 0, "inversion_bass": 0, "quality_changed": 0,
                    "root_changed": 0, "extensions_changed": 0}

    for fix in FIXTURES:
        label    = fix["label"]
        prep_p   = BASE_DIR / fix["prepared"]
        ref_p    = BASE_DIR / fix["refreshed"]
        raw_p    = BASE_DIR / fix["raw"]
        text, stats = compare_pair(label, prep_p, ref_p, raw_p)
        all_output.append(text)
        if stats:
            counts, total, changed = stats
            aggregate_total   += total
            aggregate_changed += changed
            for k in class_totals:
                class_totals[k] += counts[k]

    # Aggregate
    all_output.append("=== AGGREGATE (prepared → refreshed, shared ticks only) ===")
    all_output.append(f"Total shared regions:               {aggregate_total}")
    if aggregate_total:
        all_output.append(f"Changed by refresh:                 {aggregate_changed} "
                          f"({100*aggregate_changed/aggregate_total:.1f}%)")
    else:
        all_output.append("Changed by refresh:                 0 (0.0%)")
    non_id = {k: v for k, v in class_totals.items() if k != "identical"}
    if any(v > 0 for v in non_id.values()):
        dominant = max(non_id, key=lambda k: non_id[k])
        all_output.append(f"Dominant change class:              {dominant} ({non_id[dominant]} regions)")
    else:
        all_output.append("Dominant change class:              (none — all identical)")
    for k, v in class_totals.items():
        if k != "identical":
            all_output.append(f"  {k:<25} {v}")
    all_output.append("")

    summary = "\n".join(all_output)
    sys.stdout.buffer.write(summary.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")
    out_path = BASE_DIR / "SUMMARY.txt"
    out_path.write_text(summary, encoding="utf-8")
    print(f"Written to {out_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
