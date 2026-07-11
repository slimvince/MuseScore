#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# pass2_apply_errorrate.py — Task 4 (protocol P6): record the deep verification
# of pass 1's verdict on each of the 40 uniform-random error-rate rows. For every
# row the auditor read the code, its callers, and the data that settles the
# question; the CHECK column is CORRECT / WRONG and AGREE is Y / N. The measured
# error rate = (# WRONG) / 40.
#
# Keyed by process_order with a (basename,line) integrity check (a re-drawn sample
# would fail loudly rather than mis-attach a check).

import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1L2 = os.path.join(HERE, "l1l2")

# process_order -> (expect_basename, expect_line, pass1_verdict, check, agree, note)
CHECKS = {
 1:  ("phraseboundaryview.cpp","123","SURVIVES","CORRECT","Y","breath-mark branch in the dormant phrase primitive; correct control flow"),
 2:  ("phraseboundaryview.cpp","237","SURVIVES","CORRECT","Y","localChangeProfile ternary; pure helper; correct"),
 3:  ("regiontonecollector.cpp","157","SURVIVES","CORRECT","Y","weightedPcView no-segment fallback (return 0.75); live spine; correct branch"),
 4:  ("regiontoneprimitives.cpp","261","SURVIVES-MIXED","CORRECT","Y","pitchContextOverSpan look-back branch; correct code, in the mixed-layer engravingbridge file (module-level MIXED tag)"),
 5:  ("note_model.cpp","82","SURVIVES","CORRECT","Y","scoreSpan no-first-measure guard; correct"),
 6:  ("note_model.cpp","168","SURVIVES","CORRECT","Y","rebuildForLoadedSpan rest/empty-slot skip; correct"),
 7:  ("note_model.cpp","292","SURVIVES","CORRECT","Y","segment-tree prune (maxRel<=t0); correct"),
 8:  ("metricweights.cpp","49","SURVIVES-MIXED","CORRECT","Y","beatTypeToWeight COMPOUND_SUBBEAT case; correct, in the grab-bag metricweights file"),
 9:  ("metricweights.cpp","173","SURVIVES-MIXED","CORRECT","Y","buildPedalWindowIndex sort tiebreak; correct, in the grab-bag file"),
 10: ("phraseboundaryview.cpp","43","FACT","CORRECT","Y","downward include engraving/dom/staff.h; layer-respecting"),
 11: ("regiontonecollector.cpp","30","FACT","CORRECT","Y","downward include engraving/dom/chord.h"),
 12: ("regiontonecollector.cpp","31","FACT","CORRECT","Y","downward include engraving/dom/chordrest.h"),
 13: ("spellingview.cpp","25","FACT","CORRECT","Y","downward include engraving/dom/pitchspelling.h"),
 14: ("note_model.cpp","35","FACT","CORRECT","Y","downward include engraving/dom/staff.h"),
 15: ("note_model.h","194","SURVIVES","CORRECT","Y","extend() declaration; mirrors its (dormant-on-production) definition verdict; consistent"),
 16: ("note_model.h","86","PUBLISHED","CORRECT","Y","NoteEvent::release published L1 fact; consumed by makeEvent/overlap; correct"),
 17: ("CMakeLists.txt","","L3+","CORRECT","Y","build file, non-source; out of L1/L2 scope"),
 18: ("functionmodulation.cpp","","L3+","CORRECT","Y","function layer (L5); deferred to the L5 audit; not L1/L2"),
 19: ("functionrelationallabel.cpp","","L3+","CORRECT","Y","function layer (L5); not L1/L2"),
 20: ("sparsechordrefinement.cpp","","L3+","CORRECT","Y","region orchestration at the L3 seam; not a fact/segmentation file"),
 21: ("metricweights.h","","SURVIVES-MIXED","CORRECT","Y","L1-tagged metric primitive but a grab-bag (hosts L3 window constants + the upward key include); MIXED is correct (OI-86)"),
 22: ("composingconfiguration.cpp","","L3+","CORRECT","Y","module configuration; not L1/L2 analysis"),
 23: ("tuning_system.h","","L3+","CORRECT","Y","tuning subsystem; outside the harmonic-analysis stack"),
 24: ("chordanalyzer_musicxml_tests.cpp","","L3+","CORRECT","Y","test file; out of L1/L2 source scope"),
 25: ("chordanalyzer_tests.cpp","","L3+","CORRECT","Y","test file; out of scope"),
 26: ("mono_smoke_test.mscx","","L3+","CORRECT","Y","test fixture; out of scope"),
 27: ("nm_long_sustain.musicxml","","L3+","CORRECT","Y","test fixture; out of scope"),
 28: ("s1c_c_major.mscx","","L3+","CORRECT","Y","test fixture; out of scope"),
 29: ("functionmodulation_tests.cpp","","L3+","CORRECT","Y","test file; out of scope"),
 30: ("gater_tests.cpp","","L3+","CORRECT","Y","test file; out of scope"),
 31: ("regionanalysis_tests.cpp","","L3+","CORRECT","Y","test file; out of scope"),
 32: ("test_helpers.h","","L3+","CORRECT","Y","test helper; out of scope"),
 33: ("regiontoneprimitives.cpp","124","RETIRES","CORRECT","Y","collectPitchContext IS the legacy DOM-walk key builder superseded by pitchContextOverSpan; RETIRES(R5) is correct (this is exactly where the blind pass under-classified its branches as clean)"),
 34: ("regiontoneprimitives.cpp","218","SURVIVES-MIXED","CORRECT","Y","pitchContextOverSpan is the live L3 view but lives in the mixed-layer engravingbridge file; MIXED is the module-level tag; correct"),
 35: ("note_model.cpp","47","SURVIVES","CORRECT","Y","makeEvent note-model builder helper (the note model IS the DOM-reading layer); correct"),
 36: ("note_model.cpp","286","SURVIVES","CORRECT","Y","collect() segment-tree recursion; correct"),
 37: ("metricweights.cpp","55","SURVIVES-MIXED","CORRECT","Y","safeBeatType live helper in the grab-bag metricweights file; MIXED module tag; correct"),
 38: ("phraseboundaryview.h","86","UNFIT","CORRECT","Y","wInterOnset 0.30: in the manifest but precision-phase / not-yet-fit, so UNFIT (not-established) is defensible-and-correct. NB pass-1 report prose (§3c) loosely calls it 'ESTABLISHED-as-tracked' while the disposition says UNFIT — a minor internal prose/disposition drift, not a wrong verdict"),
 39: ("metricweights.h","57","UNFIT","CORRECT","Y","LOOKBACK_BEATS 16: hand-set, not in the manifest; UNFIT correct"),
 40: ("metricweights.h","59","UNFIT","CORRECT","Y","LOOKAHEAD_WEIGHT 0.5: hand-set, not in the manifest; UNFIT correct"),
}


def main():
    csv_path = os.path.join(L1L2, "pass2_errorrate_sample.csv")
    json_path = os.path.join(L1L2, "pass2_errorrate_sample.json")
    rows = list(csv.DictReader(open(csv_path, newline="", encoding="utf-8")))
    if len(rows) != 40:
        sys.stderr.write("FATAL: expected 40 error-rate rows, got %d\n" % len(rows))
        sys.exit(2)
    if set(int(r["process_order"]) for r in rows) != set(CHECKS):
        sys.stderr.write("FATAL: process_order set mismatch vs CHECKS\n")
        sys.exit(2)

    wrong = 0
    for r in rows:
        po = int(r["process_order"])
        base, line, p1v, check, agree, note = CHECKS[po]
        got = os.path.basename(r["file"])
        if got != base or r["line"] != line:
            sys.stderr.write("FATAL: row %d is %s:%s but table expects %s:%s\n"
                             % (po, got, r["line"], base, line))
            sys.exit(2)
        r["pass1_verdict"], r["pass2_check"], r["agree"], r["note"] = p1v, check, agree, note
        if check == "WRONG":
            wrong += 1

    cols = ["process_order", "row_id", "kind", "file", "line", "label",
            "pass1_verdict", "pass2_check", "agree", "note"]
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: int(x["process_order"])):
            w.writerow(r)

    with open(json_path, encoding="utf-8") as fh:
        blob = json.load(fh)
    by_po = {int(r["process_order"]): r for r in rows}
    for jr in blob["rows"]:
        r = by_po[int(jr["process_order"])]
        for k in ("pass1_verdict", "pass2_check", "agree", "note"):
            jr[k] = r[k]
    blob["meta"]["error_rate"] = {"wrong": wrong, "n": 40, "rate": wrong / 40.0}
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(blob, fh, indent=1, sort_keys=True)

    print("error-rate check: %d WRONG of 40 (rate %.3f)" % (wrong, wrong / 40.0))


if __name__ == "__main__":
    main()
