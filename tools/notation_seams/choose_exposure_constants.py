#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# P1 (seams part 2): choose the §4.1 presentation-gate gap-scale constants.
#
# Reads tools/notation_seams/gap_measurement.json (emitted by the
# pipeline_snapshot_tests DISABLED_SeamsGapMeasurement measurement) and, for each
# legacy normalizedConfidence threshold the exposure gates use today
# (0.35 mode-suffix, 0.5 tentative, 0.8 assertive), chooses the RECORD-path
# key-axis content-score gap constant (nats) whose firing set most nearly
# PRESERVES the legacy EXPOSURE RATE over the snapshot corpus.
#
# The rate is DURATION-WEIGHTED (segmentation-invariant — the legacy and record
# arms segment the same tick span differently, so a per-region/per-segment count
# rate is not comparable across arms; duration weighting is the only fair
# cross-arm measure, the same principle as CLAUDE.md's robust unit). The count
# rate is reported beside it for transparency but does NOT drive the choice.
#
# This is a documented, measured correspondence — NOT a fit and NOT a guess
# (contract §4.1). The chosen constants are declared at their emitter sites in a
# later partition unit (P2/P4), each carrying value + legacy rate + record rate +
# residual + this rationale. No [0,1] remap of the gap is performed anywhere.
#
# Usage:
#   python tools/notation_seams/choose_exposure_constants.py
#   (reads .../gap_measurement.json, writes .../exposure_constants.json)

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEASUREMENT = os.path.join(HERE, "gap_measurement.json")
OUT = os.path.join(HERE, "exposure_constants.json")

# The three legacy normalizedConfidence thresholds and the gate family each governs.
LEGACY_THRESHOLDS = [
    (0.35, "modeNameConfidenceThreshold (mode-suffix vs fallback-suffix)"),
    (0.50, "kTentativeKeyExposureThreshold / supportsTentativeKeyExposure / exposure bucket lower"),
    (0.80, "kAssertiveKeyExposureThreshold / kAnnotateKeyConfidenceThreshold / hasAssertiveExposure / bucket upper"),
]


def duration_weighted_rate(spans, predicate):
    """Fraction of total duration among `spans` (list of (dur, value)) where predicate(value) is true."""
    total = sum(d for d, _ in spans)
    if total <= 0:
        return 0.0
    fired = sum(d for d, v in spans if predicate(v))
    return fired / total


def count_rate(spans, predicate):
    if not spans:
        return 0.0
    return sum(1 for _, v in spans if predicate(v)) / len(spans)


def main():
    if not os.path.exists(MEASUREMENT):
        sys.stderr.write("missing measurement artifact: %s\n"
                         "  run: pipeline_snapshot_tests.exe --gtest_also_run_disabled_tests "
                         "--gtest_filter='*SeamsGapMeasurement*'\n" % MEASUREMENT)
        return 1

    with open(MEASUREMENT, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Pool spans across the corpus.
    legacy_spans = []   # (dur, normalizedConfidence)
    record_spans = []   # (dur, keyAxisGap)  — only segments with a defined gap
    record_null = 0     # segments whose gap was null (no committed / <2 candidates)
    record_errors = []
    for score in data["corpus"]:
        if score.get("recordError"):
            record_errors.append({"id": score["id"], "error": score["recordError"]})
        for r in score["legacyRegions"]:
            dur = r["endTick"] - r["startTick"]
            if dur > 0:
                legacy_spans.append((dur, r["normalizedConfidence"]))
        for s in score["recordSegments"]:
            dur = s["endTick"] - s["startTick"]
            gap = s["keyAxisGap"]
            if gap is None:
                record_null += 1
                continue
            if dur > 0:
                record_spans.append((dur, gap))

    # Candidate thresholds: the observed gap values (a threshold equal to an
    # observed gap includes that segment under the ">= g" rule).
    gap_values = sorted({v for _, v in record_spans}, reverse=True)

    results = []
    for thr, gate in LEGACY_THRESHOLDS:
        legacy_rate_dur = duration_weighted_rate(legacy_spans, lambda c, t=thr: c >= t)
        legacy_rate_cnt = count_rate(legacy_spans, lambda c, t=thr: c >= t)

        # Pick the gap constant g whose duration-weighted record firing rate
        # (fraction of duration with gap >= g) is closest to the legacy rate.
        best = None
        for g in gap_values:
            rate = duration_weighted_rate(record_spans, lambda v, gg=g: v >= gg)
            resid = abs(rate - legacy_rate_dur)
            if best is None or resid < best["residual_dur"] \
               or (resid == best["residual_dur"] and g > best["chosen_gap_nats"]):
                best = {
                    "chosen_gap_nats": g,
                    "record_rate_dur": rate,
                    "residual_dur": resid,
                }
        # count rate achieved at the chosen constant (reported, not selected on)
        record_rate_cnt = count_rate(record_spans, lambda v, gg=best["chosen_gap_nats"]: v >= gg) \
            if best else 0.0

        results.append({
            "legacy_threshold": thr,
            "gate_family": gate,
            "legacy_rate_dur": round(legacy_rate_dur, 6),
            "legacy_rate_count": round(legacy_rate_cnt, 6),
            "chosen_gap_nats": round(best["chosen_gap_nats"], 6) if best else None,
            "record_rate_dur": round(best["record_rate_dur"], 6) if best else None,
            "record_rate_count": round(record_rate_cnt, 6),
            "residual_dur": round(best["residual_dur"], 6) if best else None,
        })

    out = {
        "provenance": {
            "measurement": os.path.relpath(MEASUREMENT, os.path.join(HERE, "..", "..")).replace("\\", "/"),
            "window": data.get("window"),
            "legacy_field": data.get("legacyConfidenceField"),
            "record_field": data.get("recordGapField"),
            "rate_basis": "duration-weighted (segmentation-invariant); count rate reported beside, not selected on",
            "selection": "for each legacy threshold, the observed gap value g minimizing "
                         "|record duration-rate(gap>=g) - legacy duration-rate(conf>=threshold)|",
        },
        "pool": {
            "legacy_regions": len(legacy_spans),
            "record_segments_with_gap": len(record_spans),
            "record_segments_null_gap": record_null,
            "record_errors": record_errors,
        },
        "constants": results,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
        f.write("\n")

    # human-readable summary to stdout
    print("§4.1 gap-scale constant selection (duration-weighted rate preservation)")
    print("  pool: %d legacy regions, %d record segments (+%d null-gap)"
          % (len(legacy_spans), len(record_spans), record_null))
    if record_errors:
        print("  RECORD ERRORS: %s" % record_errors)
    print("  %-8s %-14s %-14s %-12s %-14s %-10s"
          % ("thr", "legacy_dur", "record_dur", "gap_nats", "legacy_cnt", "resid_dur"))
    for r in results:
        print("  %-8.2f %-14.4f %-14.4f %-12s %-14.4f %-10.4f"
              % (r["legacy_threshold"], r["legacy_rate_dur"], r["record_rate_dur"],
                 ("%.4f" % r["chosen_gap_nats"]) if r["chosen_gap_nats"] is not None else "none",
                 r["legacy_rate_count"], r["residual_dur"]))
    print("  wrote %s" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
