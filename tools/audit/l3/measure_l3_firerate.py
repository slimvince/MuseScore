#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
"""
measure_l3_firerate.py — behavioral characterization (protocol P4) for the EG-7
Layer-3 (key/mode) certification audit, PASS 1.

READ-ONLY. Runs the EXISTING default-OFF batch_analyze --decode-keymode diagnostic
(the least-invasive route — no new instrumentation, production byte-identical) over
the pinned Baroque corpus (git_hash c50002fee1, 352 stems) and aggregates the LIVE
Layer-3 decoder's fire rates:

  • slice count + "uncertain"-slice rate (the decoder's low-margin flag),
  • per-region key-CHANGE rate (how often the whole-sequence decode commits a
    key switch vs staying — the changeCost>0 transition),
  • distinct keys per piece + pieces that modulate (>1 distinct key).

NOT MEASURED HERE — partialSignatureCorrection fire-rate: the --decode-keymode dump
surfaces the NOTATED keySigFifths, not the CORRECTED one (verified 2026-07-11 on the
documented Corelli op01n08d partial-signature case: keySigFifths reads -2 with AND
without --ignore-declared-mode). So a notated-vs-corrected diff cannot see the fire.
Characterizing it needs a diagnostic that exposes KeyResolveDump.correctedFifths or a
counter — flagged, deferred. By construction the mechanism targets partial/Dorian
signatures (Corelli-class), which the Bach-chorale Baroque corpus does not contain.

Dormant mechanisms (reach-back, joint-key wiring, the section key-evidence
detectors) fire 0× on the production path BY CONSTRUCTION (gated OFF / diagnostic-
only) — that is derived from the code+wiring in the report, not measured here.

RUN (Git Bash on Windows — see feedback_batch_analyze_windows):
  python tools/audit/l3/measure_l3_firerate.py --out <summary.json> [--limit N]
"""

import glob
import json
import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BIN = os.path.join(REPO, "ninja_build_rel", "batch_analyze.exe")
CORPUS_OURS = os.path.join(REPO, "tools", "corpus", "baroque")
# The pinned source inputs are the committed tools/corpus/*.xml (REPRODUCIBILITY.md
# §"music21 version pin" — the exact BWV-named inputs the c50002fee1 corpus was built
# from); the per-preset baroque/ dir carries only the .ours/.music21 outputs.
SRC_DIR = os.path.join(REPO, "tools", "corpus")
SRC_EXT = ".xml"


def out_path():
    if "--out" in sys.argv:
        return sys.argv[sys.argv.index("--out") + 1]
    return os.path.join(os.path.dirname(__file__), "firerate.json")


def limit():
    if "--limit" in sys.argv:
        return int(sys.argv[sys.argv.index("--limit") + 1])
    return None


def run_decode(src, extra=()):
    try:
        p = subprocess.run([BIN, src, "--preset", "Baroque", "--decode-keymode", *extra],
                           capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0 or not p.stdout.strip():
        return None
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        return None


def main():
    stems = sorted(os.path.basename(f)[:-len(".ours.json")]
                   for f in glob.glob(os.path.join(CORPUS_OURS, "*.ours.json")))
    n = limit()
    if n:
        stems = stems[:n]

    agg = {
        "corpus": "tools/corpus/baroque (git_hash c50002fee1)",
        "diagnostic": "batch_analyze --preset Baroque --decode-keymode (default-OFF, read-only)",
        "stems_requested": len(stems),
        "stems_measured": 0,
        "stems_failed": [],
        "slices_total": 0,
        "uncertain_slices": 0,
        "regions_total": 0,
        "region_key_changes": 0,       # region key != previous region key
        "region_uncertain": 0,
        "pieces_modulating": 0,        # > 1 distinct key across the piece
    }

    for stem in stems:
        src = os.path.join(SRC_DIR, stem + SRC_EXT)
        if not os.path.exists(src):
            agg["stems_failed"].append(stem + " (no source xml)")
            continue
        d = run_decode(src)
        if d is None:
            agg["stems_failed"].append(stem + " (decode failed)")
            continue
        agg["stems_measured"] += 1
        agg["slices_total"] += int(d.get("slicesTotal", 0))
        agg["uncertain_slices"] += int(d.get("uncertainSlices", 0))
        regions = d.get("regions", [])
        agg["regions_total"] += len(regions)
        keys = []
        prev = None
        for r in regions:
            k = r.get("key")
            keys.append(k)
            if r.get("uncertain"):
                agg["region_uncertain"] += 1
            if prev is not None and k != prev:
                agg["region_key_changes"] += 1
            prev = k
        if len(set(keys)) > 1:
            agg["pieces_modulating"] += 1

    # rates
    st = agg["slices_total"] or 1
    rt = agg["regions_total"] or 1
    agg["rate_uncertain_slices_pct"] = round(100.0 * agg["uncertain_slices"] / st, 3)
    agg["rate_region_key_change_pct"] = round(100.0 * agg["region_key_changes"] / rt, 3)
    agg["rate_region_uncertain_pct"] = round(100.0 * agg["region_uncertain"] / rt, 3)

    with open(out_path(), "w", encoding="utf-8") as f:
        json.dump(agg, f, indent=1)
    print("measured %d/%d stems; slices=%d uncertain=%d (%.2f%%); regions=%d key-changes=%d (%.2f%%); "
          "modulating pieces=%d"
          % (agg["stems_measured"], agg["stems_requested"], agg["slices_total"],
             agg["uncertain_slices"], agg["rate_uncertain_slices_pct"], agg["regions_total"],
             agg["region_key_changes"], agg["rate_region_key_change_pct"],
             agg["pieces_modulating"]))


if __name__ == "__main__":
    main()
