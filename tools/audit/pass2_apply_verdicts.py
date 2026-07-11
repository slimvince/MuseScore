#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# pass2_apply_verdicts.py — merge the PASS-2 blind auditor's hand-authored
# verdicts into the sample manifest produced by gen_pass2_sample.py.
#
# The VERDICTS table below is the auditor's own judgment, formed from the code
# (all 13 L1/L2 files read in full) BEFORE any pass-1 disposition was opened
# (protocol P5, instruction Task 1). Each entry is keyed by the stable
# process_order and carries an (expected file basename, expected line) pair so a
# mis-key against a re-drawn sample fails LOUDLY rather than silently attaching a
# verdict to the wrong row.
#
# Verdict vocabulary (cowork_audit_protocol.md P2), applied per row kind:
#   function / branch  -> SURVIVES | RETIRES(R#)
#   literal (constant) -> ESTABLISHED | UNFIT | DEAD
#   field (derived)    -> PUBLISHED | SILOED | TRAPPED | DUPLICATED
#   crosslayer (dep)   -> LAYER-OK | LAYER-UPWARD
# flag: CLEAN | FLAG-MINOR | FLAG  ("no issue" is a recorded claim, P2).
#
# Run gen_pass2_sample.py first (writes empty verdict columns), THEN this.

import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1L2 = os.path.join(HERE, "l1l2")

# process_order -> (expect_basename, expect_line, verdict, flag, reason)
VERDICTS = {
 1:  ("phraseboundaryview.cpp","44","LAYER-OK","CLEAN","downward include to engraving types; layer-respecting"),
 2:  ("note_model.cpp","330","SURVIVES","CLEAN","empty/degenerate-range guard in L1 onsetIn query; correct"),
 3:  ("note_model.cpp","168","SURVIVES","CLEAN","rest/empty-slot skip in the L1 score walk; correct"),
 4:  ("regiontonecollector.h","57","LAYER-OK","CLEAN","downward include to engraving constants; layer-respecting"),
 5:  ("phraseboundaryview.cpp","264","ESTABLISHED","CLEAN","accumulator initializer (sum=0.0); not a tunable"),
 6:  ("note_model.cpp","204","SURVIVES","FLAG-MINOR","L1 bounded-context extend(): correct+idempotent, BUT the note_model.h docstring says 'no layer calls it yet' while regionanalyzer.cpp:702 (live reach-back), chordslicedecoder.cpp:1387/1393 and textureclassifier.cpp:183/187 DO call it (#10 doc-sync)"),
 7:  ("regiontoneprimitives.cpp","356","ESTABLISHED","CLEAN","Jaccard-distance complement (1.0 - inter/uni); structural"),
 8:  ("metricweights.cpp","173","SURVIVES","CLEAN","stable-sort tiebreak on pedal windows; correct"),
 9:  ("phraseboundaryview.cpp","435","SURVIVES","CLEAN","marker-spike add in the (dormant) phrase primitive; correct"),
 10: ("spellingview.cpp","38","SURVIVES","CLEAN","tpc-validity guard, the single presence test; correct (dormant primitive)"),
 11: ("regiontoneprimitives.cpp","33","LAYER-OK","CLEAN","downward include to engraving DOM note.h"),
 12: ("phraseboundaryview.cpp","249","ESTABLISHED","CLEAN","non-positive-max guard; not a tunable"),
 13: ("regiontoneprimitives.cpp","35","LAYER-OK","CLEAN","downward include to engraving DOM sig.h"),
 14: ("regiontonecollector.h","92","SURVIVES","CLEAN","L1 staff-eligibility predicate; live, consumed by note model+slicer+views"),
 15: ("phraseboundaryview.h","91","UNFIT","FLAG-MINOR","phrase peak-pick threshold offset k=1.0; hand-set precision-phase default, not established / not in a fit manifest"),
 16: ("metricweights.h","104","ESTABLISHED","CLEAN","beats-per-decay-unit length-scale (one 4/4 measure = 4.0); structural default"),
 17: ("phraseboundaryview.cpp","295","SURVIVES","CLEAN","empty-voice-lines early return; correct (dormant)"),
 18: ("regiontonecollector.cpp","317","ESTABLISHED","CLEAN","pedal-tail enable guard (>0.0); the multiplier is the pref, not this literal"),
 19: ("phraseboundaryview.cpp","141","SURVIVES","CLEAN","key-sig element test in marker scan; correct (dormant)"),
 20: ("note_model.cpp","89","SURVIVES","CLEAN","whole-score L1 build delegate; live spine; byte-identical degenerate case"),
 21: ("metricweights.cpp","23","LAYER-OK","CLEAN","self header include"),
 22: ("slicer.cpp","59","ESTABLISHED","CLEAN","need >=2 boundaries to form a slice; structural"),
 23: ("spellingview.h","102","PUBLISHED","FLAG-MINOR","SpanSpelling::sharpCount output field; the primitive has ZERO production consumers (spellingview appears only in itself + tests) - dormant, declared Phase B"),
 24: ("regiontoneprimitives.cpp","510","SURVIVES","FLAG","control flow inside findTemporalContext, which constructs+runs the full Layer-4 chord analyzer (analyzeChord/applyPostScoringGates) from an L1-tagged file - upward L1->L4 dependency (#7)"),
 25: ("note_model.cpp","268","ESTABLISHED","CLEAN","binary-tree child index (2*v); structural"),
 26: ("regiontonecollector.cpp","297","ESTABLISHED","CLEAN","base multiplier identity 1.0 in (1.0 + 0.3*(distinct-1)); the 0.3 co-located is the knob"),
 27: ("note_model.cpp","31","LAYER-OK","CLEAN","downward include to engraving DOM measure.h"),
 28: ("metricweights.cpp","142","SURVIVES","CLEAN","pedal-spanner type filter; correct"),
 29: ("phraseboundaryview.h","126","PUBLISHED","FLAG-MINOR","VoiceBoundaryProfile::strength output field; dormant primitive (consumers gated-off/dormant per header), load-bearing only at L5 engage"),
 30: ("metricweights.h","60","UNFIT","FLAG-MINOR","DECAY_RATE=0.7 windowed-evidence decay; hand-set inference magnitude, not in a fit manifest"),
 31: ("regiontonecollector.cpp","212","SURVIVES","CLEAN","view eligibility filter (staff/play/visible/grace); live spine; correct"),
 32: ("metricweights.cpp","46","SURVIVES","CLEAN","prefs-driven beat-type case (COMPOUND_UNSTRESSED); correct"),
 33: ("regiontoneprimitives.cpp","38","LAYER-UPWARD","FLAG","an L1-tagged file includes the Layer-4 chord analyzer header - the upward include enabling findTemporalContext's L4 call (#7)"),
 34: ("metricweights.cpp","35","LAYER-OK","CLEAN","downward include to engraving types.h"),
 35: ("note_model.h","82","PUBLISHED","CLEAN","NoteEvent::tpc - L1 published spelling fact; consumed by views + spelling-pin; correct"),
 36: ("phraseboundaryview.cpp","183","SURVIVES","CLEAN","ritardando marker case in the (dormant) phrase scan; correct"),
 37: ("regiontoneprimitives.cpp","586","SURVIVES","FLAG","control flow inside findTemporalContext (L1 file running the full Layer-4 analyzer - upward L1->L4 dependency)"),
 38: ("regiontonecollector.cpp","242","SURVIVES","CLEAN","onset-at-region-start flag set; correct"),
 39: ("regiontonecollector.cpp","35","LAYER-OK","CLEAN","downward include to engraving DOM sig.h"),
 40: ("regiontoneprimitives.cpp","244","SURVIVES","CLEAN","per-onset lowest-pitch (bass) tracking; live L3 view; correct"),
 41: ("metricweights.cpp","77","SURVIVES","FLAG-MINOR","hardcoded DOWNBEAT->1.0 in regionMetricWeightForBeatType; a SECOND BeatType->weight mapping coexists with the prefs-driven beatTypeToWeight (duplication question, #6)"),
 42: ("regiontonecollector.cpp","320","SURVIVES","CLEAN","pedal-release-absence guard in Pass 4; correct"),
 43: ("note_model.cpp","134","SURVIVES","CLEAN","no-first-measure early return, builds empty index; correct"),
 44: ("phraseboundaryview.cpp","264","ESTABLISHED","CLEAN","accumulator initializer (sumSq=0.0); not a tunable"),
 45: ("phraseboundaryview.cpp","315","ESTABLISHED","CLEAN","vector zero-init; not a tunable"),
 46: ("regiontonecollector.cpp","355","SURVIVES","CLEAN","bass selection with the passing-tone min-weight floor; correct"),
 47: ("metricweights.h","58","UNFIT","FLAG-MINOR","LOOKAHEAD_BEATS=8 look-ahead window length; hand-set hyperparameter, not established / not in a fit manifest"),
 48: ("regiontoneprimitives.cpp","180","SURVIVES","CLEAN","play/visible eligibility filter in the legacy key builder; correct"),
 49: ("regiontonecollector.cpp","277","SURVIVES","CLEAN","eligibility filter in the pedal-candidate pass; correct"),
 50: ("note_model.cpp","278","SURVIVES","CLEAN","segment-tree overlap query; live; correct (padded leaves pruned, ascending order preserved)"),
 51: ("spellingview.h","60","LAYER-OK","CLEAN","downward include to engraving DOM pitchspelling.h"),
 52: ("metricweights.h","57","UNFIT","FLAG-MINOR","LOOKBACK_BEATS=16 look-back window length; hand-set hyperparameter, not in a fit manifest"),
 53: ("spellingview.cpp","47","SURVIVES","FLAG-MINOR","absent-spelling guard in sharpFlatSense, which has ZERO consumers (dormant, declared Phase B)"),
 54: ("regiontonecollector.cpp","336","SURVIVES","CLEAN","pedal-tail bass update in Pass 4; correct"),
 55: ("regiontoneprimitives.cpp","147","SURVIVES","CLEAN","window lower-bound skip in the legacy key builder; correct"),
 56: ("note_model.cpp","75","SURVIVES","CLEAN","structural score-bounds helper; returns [0,0) on null/no-measures; correct"),
 57: ("phraseboundaryview.cpp","39","LAYER-OK","CLEAN","downward include to engraving DOM measure.h"),
 58: ("regiontonecollector.cpp","275","SURVIVES","CLEAN","pedal-index-present guard for the Pass 4 candidate gather; correct"),
 59: ("phraseboundaryview.cpp","257","SURVIVES","CLEAN","Simple-Picker peak-picking (mean + k*SD); pure, correct; (dormant primitive)"),
 60: ("phraseboundaryview.cpp","41","LAYER-OK","CLEAN","downward include to engraving DOM segment.h"),
 61: ("phraseboundaryview.cpp","345","ESTABLISHED","CLEAN","non-positive-max guard; not a tunable"),
 62: ("regiontoneprimitives.cpp","240","SURVIVES","CLEAN","eligibility filter (bass-map pass) in pitchContextOverSpan; live L3 view"),
 63: ("metricweights.cpp","39","SURVIVES","FLAG-MINOR","prefs-driven BeatType->weight (key path); a second BeatType->weight mapping (regionMetricWeightForBeatType, hardcoded) coexists - duplication question (#6)"),
 64: ("phraseboundaryview.h","103","UNFIT","FLAG-MINOR","coincidenceWeight default 0.0 = off; precision-phase knob, currently behaviorally inert"),
 65: ("regiontoneprimitives.cpp","356","SURVIVES","FLAG-MINOR","Jaccard div-by-zero guard in detectOnsetSubBoundaries - a legacy Layer-2 segmentation detector residing in an L1-derived-views file, feeding greedyExpandSegmentation (retires R6)"),
 66: ("spellingview.cpp","59","SURVIVES","FLAG-MINOR","skip-invalid-spelling in spanSpelling, which has zero consumers (dormant Phase B)"),
 67: ("phraseboundaryview.cpp","200","SURVIVES","CLEAN","min-silence filter for the all-rest spike; correct (dormant primitive)"),
 68: ("regiontonecollector.cpp","254","SURVIVES","CLEAN","non-positive-duration skip (backward-sustain branch); correct"),
 69: ("slicer.h","86","PUBLISHED","CLEAN","Slice::end - L2 published slice-boundary fact; consumed by the decoder; correct"),
 70: ("phraseboundaryview.cpp","319","SURVIVES","CLEAN","last-event boundary guard for the cue diffs; correct"),
 71: ("note_model.h","90","PUBLISHED","CLEAN","NoteEvent::visible - L1 eligibility fact; consumed by passes()/slicer; correct"),
 72: ("regiontonecollector.cpp","367","ESTABLISHED","CLEAN","pitch-class modulus (%12); structural"),
 73: ("note_model.cpp","268","ESTABLISHED","CLEAN","binary-tree child index (2*v); structural"),
 74: ("regiontonecollector.cpp","361","ESTABLISHED","CLEAN","positive-weight guard in the fallback bass; not a tunable"),
 75: ("regiontoneprimitives.cpp","34","LAYER-OK","CLEAN","downward include to engraving DOM segment.h"),
 76: ("metricweights.cpp","44","SURVIVES","CLEAN","prefs-driven beat-type case (DOWNBEAT); correct"),
 77: ("regiontonecollector.cpp","361","SURVIVES","CLEAN","fallback bass selection when no pc clears the min-weight floor; correct"),
 78: ("regiontoneprimitives.cpp","64","SURVIVES","CLEAN","eligibility filter in the point-in-time soundingAt view; live"),
 79: ("regiontonecollector.h","250","PUBLISHED","FLAG-MINOR","SpanWindowWeights::lookaheadWeight config field, default 0.5; the L3 decoder passes its own, but the default is an unestablished inference magnitude"),
 80: ("regiontoneprimitives.cpp","544","SURVIVES","FLAG","eligibility skip inside findTemporalContext (L1 file running the full Layer-4 analyzer - upward L1->L4 dependency)"),
 81: ("note_model.h","200","SURVIVES","CLEAN","loadedEnd() accessor; correct"),
 82: ("regiontoneprimitives.cpp","320","SURVIVES","FLAG-MINOR","grace/rest skip in detectOnsetSubBoundaries - legacy L2 segmentation logic in an L1 file (retires R6 with greedy-expand)"),
 83: ("spellingview.cpp","64","SURVIVES","FLAG-MINOR","sharp-side tally branch in spanSpelling (zero consumers, dormant Phase B)"),
 84: ("metricweights.cpp","45","SURVIVES","CLEAN","prefs-driven beat-type case (SIMPLE_STRESSED); correct"),
 85: ("metricweights.cpp","131","SURVIVES","CLEAN","buildPedalWindowIndex; live (Pass 4 of weightedPcView); correct; skips sostenuto/soft pedal"),
 86: ("regiontonecollector.cpp","30","LAYER-OK","CLEAN","downward include to engraving DOM chord.h"),
 87: ("phraseboundaryview.cpp","78","SURVIVES","CLEAN","same-onset chord-collapse merge in collectVoiceLines; correct (dormant primitive)"),
 88: ("regiontonecollector.cpp","311","SURVIVES","CLEAN","cross-voice boost gate (maxVoices>1, Pass 3); live spine; correct"),
 89: ("regiontonecollector.cpp","184","SURVIVES","CLEAN","dense-start backward-pc counting filter; reproduces legacy exactly; correct"),
 90: ("slicer.h","75","LAYER-OK","CLEAN","L2 slicer includes the L1 note model - downward (correct direction)"),
 91: ("regiontoneprimitives.cpp","425","SURVIVES","FLAG-MINOR","bass-present guard in detectBassMovementSubBoundaries - legacy L2 detector in an L1 file (retires R6)"),
 92: ("spellingview.cpp","44","SURVIVES","FLAG-MINOR","sharpFlatSense() has ZERO production consumers (only self + tests) - dormant, declared Phase B (the L3 key-spelling term)"),
 93: ("regiontonecollector.cpp","31","LAYER-OK","CLEAN","downward include to engraving DOM chordrest.h"),
 94: ("regiontoneprimitives.cpp","252","SURVIVES","CLEAN","eligibility filter (weighting pass) in pitchContextOverSpan; live L3 view"),
 95: ("phraseboundaryview.h","114","PUBLISHED","FLAG-MINOR","PhraseBoundaryParams::spikeCeilingFactor default 1.5; unestablished inference magnitude (declared precision-phase)"),
 96: ("regiontonecollector.cpp","215","ESTABLISHED","CLEAN","pitch-class modulus (%12); structural"),
 97: ("spellingview.cpp","72","SURVIVES","FLAG-MINOR","centroid divide guard (count>0) in spanSpelling (zero consumers, dormant Phase B)"),
 98: ("metricweights.cpp","55","SURVIVES","CLEAN","safeBeatType null/invalid-safe lookup; live; correct fallback to SUBBEAT"),
 99: ("note_model.h","207","SURVIVES","CLEAN","scoreStart() accessor; correct"),
 100:("note_model.h","84","PUBLISHED","CLEAN","NoteEvent::voice - L1 published fact; consumed by phrase grouping/views; correct"),
 101:("phraseboundaryview.cpp","285","SURVIVES","FLAG-MINOR","computePhraseBoundaryProfile: correct+pure, BUT dormant on production (consumers gated-off/dormant per header) - declared, load-bearing at L5 engage"),
 102:("note_model.h","197","SURVIVES","CLEAN","notes() accessor returning the note vector; correct"),
 103:("regiontoneprimitives.cpp","263","SURVIVES","CLEAN","look-ahead distance else-if branch in pitchContextOverSpan; live L3 view; correct"),
 104:("spellingview.h","100","PUBLISHED","FLAG-MINOR","SpanSpelling::count output field; dormant primitive, zero consumers (declared Phase B)"),
 105:("phraseboundaryview.cpp","146","SURVIVES","CLEAN","no-keysig-element skip in marker scan; correct (dormant primitive)"),
 106:("note_model.h","85","PUBLISHED","CLEAN","NoteEvent::onset - L1 core published fact; consumed everywhere; correct"),
 107:("regiontonecollector.cpp","188","SURVIVES","CLEAN","distinct-pc dedup in the dense-start count; reproduces legacy; correct"),
 108:("phraseboundaryview.cpp","366","ESTABLISHED","CLEAN","vector zero-init (strength.resize); not a tunable"),
 109:("phraseboundaryview.cpp","315","ESTABLISHED","CLEAN","vector zero-init; not a tunable"),
 110:("phraseboundaryview.cpp","225","ESTABLISHED","CLEAN","denominator guard (denom<=0.0); not a tunable"),
}


def main():
    csv_path = os.path.join(L1L2, "pass2_blind_sample.csv")
    json_path = os.path.join(L1L2, "pass2_blind_sample.json")
    rows = list(csv.DictReader(open(csv_path, newline="", encoding="utf-8")))
    if len(rows) != 110:
        sys.stderr.write("FATAL: expected 110 blind rows, got {}\n".format(len(rows)))
        sys.exit(2)
    if set(int(r["process_order"]) for r in rows) != set(VERDICTS):
        sys.stderr.write("FATAL: process_order set mismatch vs VERDICTS table\n")
        sys.exit(2)

    for r in rows:
        po = int(r["process_order"])
        exp_base, exp_line, verdict, flag, reason = VERDICTS[po]
        base = os.path.basename(r["file"])
        if base != exp_base or r["line"] != exp_line:
            sys.stderr.write(
                "FATAL: row {} is {}:{} but verdict table expects {}:{} - "
                "sample drifted, refusing to mis-key.\n".format(
                    po, base, r["line"], exp_base, exp_line))
            sys.exit(2)
        r["verdict"], r["flag"], r["reason"] = verdict, flag, reason

    cols = ["process_order", "row_id", "kind", "file", "line", "label",
            "verdict", "flag", "reason"]
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: int(x["process_order"])):
            w.writerow(r)

    # Rewrite the JSON with verdicts + a flag summary.
    with open(json_path, encoding="utf-8") as fh:
        blob = json.load(fh)
    by_po = {int(r["process_order"]): r for r in rows}
    for jr in blob["rows"]:
        r = by_po[int(jr["process_order"])]
        jr["verdict"], jr["flag"], jr["reason"] = r["verdict"], r["flag"], r["reason"]
    summary = {"CLEAN": 0, "FLAG-MINOR": 0, "FLAG": 0}
    for r in rows:
        summary[r["flag"]] = summary.get(r["flag"], 0) + 1
    blob["meta"]["flag_summary"] = summary
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(blob, fh, indent=1, sort_keys=True)

    print("verdicts applied to 110 rows. flag summary: {}".format(summary))
    flagged = [(int(r["process_order"]), os.path.basename(r["file"]), r["line"], r["flag"])
               for r in rows if r["flag"] != "CLEAN"]
    for po, base, line, flag in sorted(flagged):
        print("  [{}] {} {}:{}".format(flag, po, base, line))


if __name__ == "__main__":
    main()
