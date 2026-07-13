#!/usr/bin/env python3
"""cc_oi125_extrapolation_probe.py — the OI-125 measurement, reproducible on demand.

READ-ONLY. Writes nothing (no --out, no artifact, no committed file touched); it prints.

WHAT IT MEASURES. compare_analyses._dcml_tick_for resolves a DCML (measure, beat) onset to a
tick. When the onset lies BEYOND the outermost measure our regions anchor -- overwhelmingly the
pickup measure, which DCML numbers 0 while our regions start at 1 -- it must EXTRAPOLATE. It
used to do so on a hard-coded 4 beats per measure; since OI-125 it uses the measure length
DERIVED from each stem's own anchors (_derive_ticks_per_measure).

This probe enumerates every extrapolation firing over the committed corpus (all three presets,
via the same loaders the a8 driver uses -- no second tick matcher, #6) and answers the two
questions the OI-125 ruling rests on:

  1. Is the branch LOAD-BEARING?          -> how many firings, on how many stems
  2. Was the superseded 4/4 CORRECT here? -> is the derived measure length 4 * tpb on every
                                             firing, i.e. does the fix change any resolved tick?

The figures it reproduces (committed corpus c50002fee1, 2026-07-13; see
cc_wave1_finalize_report.md and the OI-125 register row):

    extrapolation firings           162
    stems that fire                  15
    derived measure length          4.0 beats on every firing stem
    resolved ticks that CHANGE        0 of 162      <- the byte-identity of the OI-125 fix
    stems with < 2 anchors            0 of 352      <- the last-resort constant never fires

Run:  python tools/cc_oi125_extrapolation_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import compare_analyses as cmp          # noqa: E402
import dcml_parser as dcml              # noqa: E402
import a8_rebaseline_measure as a8      # noqa: E402  (the corpus + WiR locations the a8 path uses)

PRESETS = ["baroque", "jazz", "default"]


def main() -> int:
    firings = 0
    fire_stems: set[str] = set()
    tick_changes = []            # firings where derived != the superseded 4/4 constant
    thin_anchor_stems = []       # stems with < 2 anchors (no measure length derivable)
    derived_beats: dict[str, float] = {}

    for preset in PRESETS:
        corpus_dir = _ROOT / "tools" / "corpus" / preset
        for ours_path in sorted(corpus_dir.glob("*.ours.json")):
            stem = ours_path.stem.replace(".ours", "")
            try:
                _, ours_regions = cmp.load_analysis(ours_path)
            except (OSError, ValueError, KeyError, TypeError):
                continue
            if not ours_regions:
                continue
            if dcml.find_wir_file(str(a8.WIR_DIR), stem) is None:
                continue                      # no human ground truth for this stem
            try:
                wir_regions = dcml.load_wir_regions(str(a8.WIR_DIR), stem)
            except Exception:
                continue
            if not wir_regions:
                continue

            tpb = cmp._infer_ticks_per_beat(ours_regions)
            anchors = cmp._build_measure_anchors(ours_regions, tpb)
            if len(anchors) < 2:
                thin_anchor_stems.append((preset, stem, len(anchors)))
            derived = cmp._derive_ticks_per_measure(anchors)

            for dr in wir_regions:
                if getattr(dr, "abs_tick", None) is not None:
                    continue                  # the TSV path carries an absolute tick; no resolver
                m = dr.measure_number
                if not anchors or m in anchors:
                    continue                  # exact anchor
                prev_m = max((x for x in anchors if x < m), default=None)
                next_m = min((x for x in anchors if x > m), default=None)
                if prev_m is not None and next_m is not None and next_m > prev_m:
                    continue                  # the interpolation branch, not extrapolation
                if prev_m is None and next_m is None:
                    continue                  # unresolvable either way

                firings += 1
                fire_stems.add(stem)
                if derived is not None:
                    derived_beats[stem] = derived / tpb

                superseded = cmp.EXTRAPOLATION_BEATS_PER_MEASURE * tpb
                in_force = derived if derived is not None else superseded
                anchor_m = prev_m if prev_m is not None else next_m
                sign = 1 if prev_m is not None else -1
                span = (m - prev_m) if prev_m is not None else (next_m - m)
                old_t = int(round(anchors[anchor_m] + sign * span * superseded + (dr.beat - 1) * tpb))
                new_t = int(round(anchors[anchor_m] + sign * span * in_force + (dr.beat - 1) * tpb))
                if old_t != new_t:
                    tick_changes.append((preset, stem, m, dr.beat, old_t, new_t))

    beats = sorted({round(v, 6) for v in derived_beats.values()})
    print(f"extrapolation firings                 : {firings}")
    print(f"stems that fire                       : {len(fire_stems)}  {sorted(fire_stems)}")
    print(f"derived measure length (beats), firing: {beats}")
    print(f"stems with < 2 anchors (underivable)  : {len(thin_anchor_stems)}  {thin_anchor_stems}")
    print(f"resolved ticks CHANGED by the fix     : {len(tick_changes)}")
    for row in tick_changes[:20]:
        print("    ", row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
