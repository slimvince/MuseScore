#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
"""
gen_dispositions.py — the PASS-1 disposition emitter for the L1/L2 certification
audit (OI-84, protocol P2). Reads the machine inventory (tools/audit/l1l2/
inventory.json) and applies an AUTHORED verdict map to emit a TOTAL disposition:
one closed-set verdict for EVERY inventory row (P2 — "no issue" is a recorded claim,
never a blank). Exits nonzero if any inventory row is left without a verdict.

Separation of concerns (#17(f)): the INVENTORY is machine-generated (gen_inventory.py);
the VERDICTS are the auditor's judgement, authored below at the meaningful granularity
(file / function / constant / cross-layer dep) and EXPANDED to every fine-grained row
(branches, trivial literals, decls) by stated blanket rules, so the artifact is total
AND reproducible (no hand-transcribed per-row table that could drift).

Closed verdict sets (protocol P2):
  premises  : FACT / THEORY / ASSUMPTION
  derived   : PUBLISHED / SILOED / TRAPPED / DUPLICATED   (+ dormancy: DECLARED/WASTE)
  constants : ESTABLISHED / UNFIT / DEAD                  (+ in_manifest bool)
  code      : SURVIVES / RETIRES                          (+ fire: LIVE/DORMANT/COND/NA)

RUN: python tools/audit/gen_dispositions.py   (writes pass1_dispositions.{csv,json})
"""
import csv
import json
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "l1l2")
INV = os.path.join(OUT_DIR, "inventory.json")

F_NM_H = "src/composing/analysis/notemodel/note_model.h"
F_NM_C = "src/composing/analysis/notemodel/note_model.cpp"
F_RTC_H = "src/composing/analysis/engravingbridge/regiontonecollector.h"
F_RTC_C = "src/composing/analysis/engravingbridge/regiontonecollector.cpp"
F_RTP_C = "src/composing/analysis/engravingbridge/regiontoneprimitives.cpp"
F_SV_H = "src/composing/analysis/engravingbridge/spellingview.h"
F_SV_C = "src/composing/analysis/engravingbridge/spellingview.cpp"
F_PBV_H = "src/composing/analysis/engravingbridge/phraseboundaryview.h"
F_PBV_C = "src/composing/analysis/engravingbridge/phraseboundaryview.cpp"
F_MW_H = "src/composing/analysis/scoreharvest/metricweights.h"
F_MW_C = "src/composing/analysis/scoreharvest/metricweights.cpp"
F_SL_H = "src/composing/analysis/slicing/slicer.h"
F_SL_C = "src/composing/analysis/slicing/slicer.cpp"

# ── FILE-level P2 four-questions + verdict ───────────────────────────────────
FILE_DISPO = {
    F_NM_H: dict(layer="L1", verdict="SURVIVES",
        assumes="MuseScore DOM tie/play/visible flags are authoritative (FACT: DOM API); one onset per tied group (THEORY: Pardo&Birmingham / music21 chordify lineage)",
        publishes="NoteEvent{11 fields}, NoteModel query API, NoteQueryIndex — the single source of 'what sounds'",
        consumers="L2 slicer, L1.5 views, L3 key path, L4 decoder (all downstream)",
        edges="empty/backwards/silent span → no notes; grace/muted/invisible/non-tonal KEPT+flagged; N==0 index safe",
        flags=[]),
    F_NM_C: dict(layer="L1", verdict="SURVIVES",
        assumes="playTicksFraction() is the authoritative tie-resolved span (FACT: DOM); staffIsEligible at onset tick is the eligibility fact",
        publishes="build/extend/overlapping/onsetIn impls; NoteQueryIndex (max-release segment tree)",
        consumers="same as note_model.h",
        edges="null score / no firstMeasure → empty model; extend clamps at score bounds, no-op on non-positive/covered; INT_MIN padded leaves pruned",
        flags=["extend() DORMANT on production (only the dormant L4 decoder reach-back calls it) — declared dormancy, consumer named (Phase-3 reach-back)",
               "interim Phase-1a: extend() re-walks the WHOLE score (byte-identical but O(score) per step) — self-declared debt, Phase-1b deferred"]),
    F_SL_H: dict(layer="L2", verdict="SURVIVES",
        assumes="a chord can change ONLY at a boundary tick (THEORY: change-point/salami-slice, Pardo&Birmingham); eligibility is L1's fact, not re-decided",
        publishes="Slice{start,end}, changePointSlices() — the exhaustive constant-sonority grid",
        consumers="L3 decoder (regionanalyzer seam), L4, L6",
        edges="<2 boundaries → empty; zero-width note dedups away; clip inert on whole-score; single-tick loaded span → empty",
        flags=[]),
    F_SL_C: dict(layer="L2", verdict="SURVIVES",
        assumes="union of eligible onsets+releases, clipped to loaded span, tiles the domain (FACT, provable)",
        publishes="changePointSlices impl",
        consumers="regionanalyzer:632/704 (LIVE), batch_analyze ×5, chordslicedecoder(dormant), phraseboundaryview(dormant)",
        edges="all handled explicitly in-code (see header); clip documented byte-identical on whole-score live path",
        flags=[]),
    F_MW_H: dict(layer="L1", verdict="SURVIVES-MIXED",
        assumes="beat-strength from the notated time signature is preference-free metric evidence (FACT: engraving TimeSigFrac); metric weight in [0.5,1.0]",
        publishes="beat-weight table, sliding-window constants, pedal-window index, timeDecay, distinctPitchClasses",
        consumers="L4 membership (regionMetricWeightForOnsetTick), L3 key window (LOOKBACK/DECAY, beatTypeToWeight), pedal reader",
        edges="null score / no measure / timesig num|den<=0 → SUBBEAT fallback (0.5)",
        flags=["MIXED LAYER: an L1.5 metric primitive that ALSO hosts L3 key-window constants (LOOKBACK_BEATS/LOOKAHEAD/DECAY_RATE) and prefs-driven key beat weights — #7 layering",
               "UPWARD DEP: metricweights.h:42 includes ../key/keymodeanalyzer.h (L1.5 -> L3 KeyModeAnalyzer types) — #7 back-edge",
               "TWO metric-weight tables: regionMetricWeightForBeatType (hard-coded prefs-free) vs beatTypeToWeight (prefs-driven) — potential #6 duplication of the same concept"]),
    F_MW_C: dict(layer="L1", verdict="SURVIVES-MIXED",
        assumes="the hard-coded 1.0/0.85/0.75/0.5 beat table IS the metric-salience fact (ASSUMPTION: hand-set, no fit record)",
        publishes="beat-weight impls, buildPedalWindowIndex",
        consumers="see metricweights.h",
        edges="pedal: skips sostenuto/soft (magic strings); staff bounds + eligibility guarded; empty windows sorted",
        flags=["beat-weight table 1.0/0.85/0.75/0.5 NOT in param_manifest.json (T3-1/EG-5 gap) — UNFIT",
               "distinctPitchClasses takes KeyModeAnalyzer::PitchContext (L3 type) — the upward-dep surface"]),
    F_SV_H: dict(layer="L1", verdict="SURVIVES",
        assumes="tpc is a line-of-fifths spelling carried losslessly by L1 (FACT: engraving Tpc); tpcIsValid (not >=0) is the correct presence test (FACT: flat side is negative)",
        publishes="lineOfFifths/sharpFlatSense/spanSpelling — the SINGLE tpc-spelling interpreter",
        consumers="dormant L4 spelling-pin (lineOfFifths); Phase-B L3 key-spelling term (spanSpelling/sharpFlatSense — ZERO consumers today)",
        edges="invalid tpc → kNoLineOfFifths sentinel (-23, cannot collide); empty span → count 0, centroid 0.0",
        flags=["DORMANT: no production consumer — lineOfFifths only feeds the dormant L4 pin; spanSpelling/sharpFlatSense have ZERO consumers (Phase-B). Declared dormancy, consumers named (fact-publication corollary)",
               "DUPLICATED (R4): the fold of chordanalyzer.cpp's inline tpc cluster (tpcForPc/tpcSpellsAsSharp/tpcConsistencyBonus/countTpcMatches) into this primitive HAS NOT happened — a SECOND live tpc reader coexists (self-declared; retires R4 with the decoder)"]),
    F_SV_C: dict(layer="L1", verdict="SURVIVES",
        assumes="line-of-fifths = tpc - TPC_C (FACT)",
        publishes="lineOfFifths/sharpFlatSense/spanSpelling impls",
        consumers="see spellingview.h",
        edges="tpcIsValid skips invalid; centroid 0.0 on empty",
        flags=[]),
    F_PBV_H: dict(layer="L1", verdict="SURVIVES",
        assumes="phrase ends are readable from the notated surface alone, key/chord/function-agnostic (THEORY: local-change surface cues; design cowork_phrase_boundary_design.md §4) — MUST be cadence-agnostic (cadence CONSUMES it — circularity guard)",
        publishes="PhraseBoundaryParams, VoiceBoundaryProfile, PhraseBoundaryProfile, phraseBoundaryTicks()",
        consumers="DORMANT/gated-off on production (joint-key re-key pass gated OFF; batch diagnostics) — becomes load-bearing at L5 engage",
        edges="null score → empty set; all-zero profile → no picks; one-sided change-ratio at ends",
        flags=["DORMANT on production: every 'ends a phrase' consumer is gated-off/diagnostic — declared dormancy, consumer named (L5 cadence engage)",
               "PRECISION-PHASE constants (k, tauTicks, coincidenceWeight, minSilenceTicks) NOT in param_manifest.json (wGap/wInterOnset/wPitch/spikeCeilingFactor ARE) — partial manifest coverage, EG-5 gap; declared precision-phase (honest)"]),
    F_PBV_C: dict(layer="L1", verdict="SURVIVES",
        assumes="peak = local max above mean+k*SD (THEORY: Simple-Picker); marker spikes strictly exceed max surface strength (by spikeCeilingFactor>1)",
        publishes="computePhraseBoundaryProfile/phraseBoundaryTicks + pure helpers (changeRatio/localChangeProfile/maxNormalizeInPlace/pickPeaks)",
        consumers="see phraseboundaryview.h (dormant)",
        edges="changeRatio 0 when a+b==0; maxNormalize no-op on non-positive max; empty profile safe",
        flags=[]),
    F_RTC_H: dict(layer="L1", verdict="SURVIVES-MIXED",
        assumes="eligibility = show && !drumset && !chordTrack (FACT: matches notation predicate); weightedPcView reproduces legacy collectRegionTones EXCEPT tie + no-cap corrections",
        publishes="staffIsEligible/isChordTrackStaff, soundingAt/collectSoundingAt/buildTones, weightedPcView/collectRegionTones",
        consumers="L2(via note_model eligibility), L4 chord scoring (weightedPcView/buildTones), notation bridge, batch",
        edges="see impl; excludeStaves/grace/non-playing filtered by passes()",
        flags=["MIXED LAYER GRAB-BAG: this L1.5 header ALSO declares L2-legacy sub-boundary detectors (detectOnsetSubBoundaries/detectBassMovementSubBoundaries, Pass-2/2b — retire R6), an L4 helper (findTemporalContext — FQ-3/OI-12, live on the bridge, moves to E4), and L3 key-context builders (collectPitchContext legacy + pitchContextOverSpan L3-survivor). #7 layering / #6 owner-drift",
               "UPWARD DEP: regiontonecollector.cpp:37 includes chord/analysisutils.h (L4)"]),
    F_RTC_C: dict(layer="L1", verdict="SURVIVES",
        assumes="the 0.3 repetition boost, 1.5 cross-voice boost, and the >=3-pc dense-start look-ahead exclusion reproduce the legacy analysis weighting (ASSUMPTION: hand-set; kept byte-identical to legacy on purpose)",
        publishes="weightedPcView impl (the real derived view)",
        consumers="batch_analyze:2706, notation bridge collectRegionTones wrapper",
        edges="regionDuration<=0 guarded; durInRegion<=0 skipped; totalWeight==0 skipped; pedal pass only when pedals present",
        flags=["UNFIT inference weights in the L1.5 view NOT in param_manifest: repetition-boost 0.3 (line 297), cross-voice-boost 1.5 (line 312) — hand-set, inference-affecting",
               "the Fraction(4,1) 4-whole-note backLimit (line 151) is the PEDAL-TAIL lookback window ONLY (verified) — NOT the removed sustain cap; but it is a hand-set magic window matching 'legacy coverage'"]),
    F_RTP_C: dict(layer="L1", verdict="SURVIVES-MIXED",
        assumes="pitchContextOverSpan weighting (durationQn x timeDecay x lookahead x beatWeight) is the L3 key-window evidence model (THEORY: windowed pitch salience); Jaccard sub-boundary distance detects onset change (L2-legacy)",
        publishes="soundingAt/buildTones/weightedPcView helpers, collectPitchContext(legacy)/pitchContextOverSpan(L3), detectOnset/BassMovementSubBoundaries(L2-legacy)",
        consumers="keymodesequence:89 (pitchContextOverSpan, LIVE L3), keyresolver seed (collectPitchContext, retires R5), bridge (sub-boundary pass-throughs)",
        edges="onsets<2 → no sub-boundary; empty context safe; lookahead multiplier applied by flag",
        flags=["UPWARD DEP: regiontoneprimitives.cpp:38 includes chord/chordanalyzer.h (L4) — the audit-Q2 back-edge is killed in the HEADER but the L1.5 IMPLEMENTATION still depends on L4",
               "MIXED: hosts L2-legacy sub-boundary detectors (retire R6) + L3 key-context builders in one L1.5 .cpp"]),
}

# functions whose verdict/fire differ from the file default
FUNC_DISPO = {
    (F_NM_C, "extend"): dict(verdict="SURVIVES", fire="DORMANT",
        note="production fire-rate 0 — only the dormant L4 decoder reach-back + tests call it (declared dormancy, Phase-3 reach-back)"),
    (F_SV_C, "lineOfFifths"): dict(verdict="SURVIVES", fire="DORMANT",
        note="production fire-rate 0 — only the dormant L4 spelling-pin (chordslicedecoder:610) + tests"),
    (F_SV_C, "spanSpelling"): dict(verdict="SURVIVES", fire="DORMANT",
        note="ZERO consumers anywhere (Phase-B L3 key-spelling term) — declared dormancy"),
    (F_SV_C, "sharpFlatSense"): dict(verdict="SURVIVES", fire="DORMANT",
        note="ZERO consumers (Phase-B) — declared dormancy"),
    (F_PBV_C, "computePhraseBoundaryProfile"): dict(verdict="SURVIVES", fire="DORMANT",
        note="production fire-rate 0 — batch diagnostics + gated-off joint-key only"),
    (F_PBV_C, "phraseBoundaryTicks"): dict(verdict="SURVIVES", fire="DORMANT",
        note="production fire-rate 0 — diagnostic/gated consumers only (declared dormancy, L5 engage)"),
    (F_RTP_C, "collectPitchContext"): dict(verdict="RETIRES", fire="LIVE",
        note="legacy DOM-walk key-context builder — retires R5 with the legacy key resolver (seed S2); pitchContextOverSpan is the survivor"),
    (F_RTP_C, "detectOnsetSubBoundaries"): dict(verdict="RETIRES", fire="COND",
        note="L2-legacy Pass-2 Jaccard sub-boundary — retires R6; exposed via bridge pass-through"),
    (F_RTP_C, "detectBassMovementSubBoundaries"): dict(verdict="RETIRES", fire="COND",
        note="L2-legacy Pass-2b bass-movement sub-boundary — retires R6; exposed via bridge pass-through"),
    (F_RTC_H, "findTemporalContext"): dict(verdict="SURVIVES", fire="LIVE",
        note="L4 temporal-context helper — LIVE on the notation bridge (609); ownership moves to E4 (FQ-3/OI-12)"),
}

# constants that are genuinely tunable weights (UNFIT unless fit-established); keyed (file,value)
# in_manifest from the param_manifest grep (Task-2 measurement).
UNFIT_CONSTS = {
    (F_MW_C, "0.85"): (False, "metric weight STRESSED — hand-set, not in manifest (EG-5/T3-1)"),
    (F_MW_C, "0.75"): (False, "metric weight UNSTRESSED — hand-set, not in manifest"),
    (F_MW_C, "0.5"):  (False, "metric weight SUBBEAT/fallback — hand-set, not in manifest"),
    (F_MW_H, "16"):   (False, "LOOKBACK_BEATS — L3 key-window, hand-set, not in manifest"),
    (F_MW_H, "8"):    (False, "LOOKAHEAD_BEATS — L3 key-window, hand-set, not in manifest"),
    (F_MW_H, "0.5"):  (False, "LOOKAHEAD_WEIGHT — hand-set, not in manifest"),
    (F_MW_H, "0.7"):  (False, "DECAY_RATE — hand-set, not in manifest"),
    (F_MW_H, "4.0"):  (False, "timeDecay beatsPerUnit default — hand-set, not in manifest"),
    (F_RTC_C, "0.3"): (False, "repetition-boost magnitude — inference weight, not in manifest"),
    (F_RTC_C, "1.5"): (False, "cross-voice-boost magnitude — inference weight, not in manifest"),
    (F_RTC_H, "0.7"): (False, "SpanWindowWeights.decayRate seed — mirrors DECAY_RATE, not in manifest"),
    (F_RTC_H, "0.5"): (False, "SpanWindowWeights.lookaheadWeight seed — not in manifest"),
    (F_RTC_H, "0.25"): (False, "detectOnsetSubBoundaries Jaccard threshold — L2-legacy, not in manifest (retires R6)"),
    (F_PBV_H, "0.50"): (True,  "wGap — precision-phase, IN param_manifest"),
    (F_PBV_H, "0.30"): (True,  "wInterOnset — precision-phase, IN param_manifest"),
    (F_PBV_H, "0.20"): (True,  "wPitch — precision-phase, IN param_manifest"),
    (F_PBV_H, "1.5"):  (True,  "spikeCeilingFactor — precision-phase, IN param_manifest"),
    (F_PBV_H, "1.0"):  (False, "k (Simple-Picker SD offset) — precision-phase, NOT in manifest"),
    (F_PBV_H, "240"):  (False, "minSilenceTicks — precision-phase, NOT in manifest (and a raw tick, not DIVISION-derived)"),
    (F_PBV_H, "0.0"):  (False, "coincidenceWeight default-off — precision-phase, NOT in manifest"),
}


def const_class(file, value, func, context):
    """ESTABLISHED / UNFIT / DEAD + in_manifest, with a stated reason."""
    key = (file, value)
    if key in UNFIT_CONSTS:
        inman, reason = UNFIT_CONSTS[key]
        return "UNFIT", inman, reason
    # structural / music-fact constants (not tunable):
    if value in ("12",):
        return "ESTABLISHED", False, "12 = pitch-class count (music FACT, not tunable)"
    if value in ("2",):
        return "ESTABLISHED", False, "structural 2 (binary tree / boundary-pair / *2 reserve) — FACT, not tunable"
    if value in ("4", "4.0"):
        return "ESTABLISHED", False, "4 = quarters-per-whole / 4-whole-note window (metric FACT)"
    if value in ("3",):
        return "ESTABLISHED", False, "dense-start threshold 3 distinct pcs — legacy structural (batch-only path)"
    if value in ("0.0", "1.0"):
        return "ESTABLISHED", False, "init/identity literal (accumulator seed / multiplicative identity) — not a tunable weight"
    if value in ("0.75",) and file == F_RTC_C:
        return "ESTABLISHED", False, "bwAtRegionStart fallback = UNSTRESSED metric weight (reuse of the established table value)"
    # any remaining numeric — record explicitly as UNFIT-review (never silently 'fine')
    return "UNFIT", False, "unclassified numeric literal — review (default UNFIT, not silently accepted)"


def cross_class(file, target_area, resolved):
    if target_area in ("chord", "key"):
        return ("ASSUMPTION", "UPWARD cross-layer dep: an L1/L2 file includes a %s (higher-layer) header — #7 layering finding" % target_area)
    if target_area == "types":
        return ("FACT", "shared leaf types header (analysistypes.h) or engraving types — the designed unification, downward/lateral")
    if target_area in ("notemodel", "slicing", "engravingbridge", "scoreharvest"):
        return ("FACT", "intra-L1/L2 dependency (lateral, within the fact/segmentation layers) — legitimate reuse (#6)")
    return ("FACT", "engraving/std external dependency — downward, legitimate")


def main():
    with open(INV, encoding="utf-8") as f:
        inv = json.load(f)
    rows = []
    flagged = []

    def add(kind, file, ident, verdict_class, verdict, reason, line=""):
        rows.append(dict(kind=kind, file=file, ident=ident, line=line,
                         verdict_class=verdict_class, verdict=verdict, reason=reason))

    # file table (all 216) — the L3+/RETIRES ones get their tag-reason as the disposition
    for r in inv["file_table"]:
        f = r["file"]
        if f in FILE_DISPO:
            d = FILE_DISPO[f]
            add("file", f, d["layer"], "CODE", d["verdict"],
                "ASSUMES: %s | PUBLISHES: %s | CONSUMERS: %s | EDGES: %s" %
                (d["assumes"], d["publishes"], d["consumers"], d["edges"]))
            for fl in d["flags"]:
                flagged.append(dict(file=f, kind="file-flag", detail=fl))
        else:
            add("file", f, r["tag"], "SCOPE", r["tag"], r["reason"])

    # functions
    for r in inv["functions"]:
        f, name = r["file"], r["name"]
        fd = FUNC_DISPO.get((f, name))
        if fd:
            add("function", f, name, "CODE", fd["verdict"],
                "fire=%s — %s" % (fd["fire"], fd["note"]), r.get("start_line", ""))
            if fd["verdict"] == "RETIRES" or fd["fire"] == "DORMANT":
                flagged.append(dict(file=f, kind="func-%s" % ("retires" if fd["verdict"] == "RETIRES" else "dormant"),
                                    detail="%s(): %s" % (name, fd["note"])))
        else:
            base = FILE_DISPO.get(f, {}).get("verdict", "SURVIVES")
            add("function", f, name, "CODE", base,
                "fire=LIVE (spine/derived-view) — SURVIVES; premise = file-level; no separate premise", r.get("start_line", ""))

    # literals -> constants
    for r in inv["literals"]:
        cls, inman, reason = const_class(r["file"], r["value"], r.get("func", ""), r.get("context", ""))
        add("literal", r["file"], r["value"], "CONST", cls,
            "in_manifest=%s — %s (func=%s)" % (inman, reason, r.get("func", "")), r.get("line", ""))
        if cls == "UNFIT" and not inman:
            flagged.append(dict(file=r["file"], kind="const-unfit-not-in-manifest",
                                detail="%s @L%s (%s): %s" % (r["value"], r.get("line", ""), r.get("func", ""), reason)))

    # fields (header-declared, cross-visible) -> publication axis
    for r in inv["fields"]:
        add("field", r["file"], "%s.%s" % (r.get("type_owner", ""), r.get("name", "")), "DERIVED", "PUBLISHED",
            "cross-visible struct field on %s — published surface; consumer per file disposition" % r.get("type_owner", ""),
            r.get("line", ""))

    # decls mirror function/code
    for r in inv["decls"]:
        add("decl", r["file"], "%s::%s" % (r.get("type_owner", ""), r.get("name", "")), "CODE", "SURVIVES",
            "declaration — verdict mirrors its definition row", r.get("line", ""))

    # branches -> control flow within enclosing function
    for r in inv["branches"]:
        f = r["file"]
        func = r.get("func", "<file-scope>")
        fd = FUNC_DISPO.get((f, func))
        v = fd["verdict"] if fd else FILE_DISPO.get(f, {}).get("verdict", "SURVIVES")
        add("branch", f, "%s@%s:%s" % (r.get("kind", ""), func, r.get("line", "")), "CODE", v,
            "control-flow branch within %s(); disposition inherits the function; edge-behavior audited at file level" % func,
            r.get("line", ""))

    # cross-layer
    for r in inv["crosslayer"]:
        cls, reason = cross_class(r["file"], r.get("target_area", ""), r.get("resolved", ""))
        add("crosslayer", r["file"], r.get("include", ""), "PREMISE", cls, reason, r.get("line", ""))
        if cls == "ASSUMPTION":
            flagged.append(dict(file=r["file"], kind="crosslayer-upward",
                                detail="includes %s (%s) — %s" % (r.get("include", ""), r.get("target_area", ""), reason)))

    # totality check
    missing = [r for r in rows if not r["verdict"] or not r["reason"]]
    if missing:
        raise SystemExit("P2 TOTALITY FAILURE — %d rows without a verdict" % len(missing))

    # write CSV + JSON
    cols = ["kind", "file", "ident", "line", "verdict_class", "verdict", "reason"]
    with open(os.path.join(OUT_DIR, "pass1_dispositions.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    with open(os.path.join(OUT_DIR, "pass1_dispositions.json"), "w", encoding="utf-8") as fh:
        json.dump(dict(rows=rows, flagged=flagged), fh, indent=1)

    # summary
    from collections import Counter
    byv = Counter(r["verdict"] for r in rows)
    byc = Counter(r["verdict_class"] for r in rows)
    print("pass1_dispositions OK — %d rows, ALL with a verdict (P2 total)" % len(rows))
    print("  by class:", dict(byc))
    print("  by verdict:", dict(byv))
    print("  flagged findings: %d" % len(flagged))
    fk = Counter(x["kind"] for x in flagged)
    print("  flagged by kind:", dict(fk))


if __name__ == "__main__":
    main()
