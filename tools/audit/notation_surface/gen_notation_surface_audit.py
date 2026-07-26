#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# gen_notation_surface_audit.py — the READ-ONLY notation consumption-surface audit
# generator (dispatch cc_instruction_notation_consumption_audit.md, §8.1 of
# cowork_notation_adoption_increment.md, user-ratified 2026-07-26).
#
# It emits the two audit artifacts from ONE embedded, code-verified enumeration so the
# report's figures are DERIVED, never hand-typed (#17f):
#   • consumption_fields.csv  — one row per (live consumer file, consumed surface field)
#   • summary.json            — roster, disposition-class counts, the Task 2/3/4 lists
#
# The enumeration below was verified at the code this session (file:line anchors; four
# read-only extraction passes over the eight live consumers + the section/function layer).
# It records READS of the notation harmonic-analysis output surface only — the legacy
# region/section record types (HarmonicRegion / AnalyzedRegion / KeyArea / AnalyzedSection /
# NoteHarmonicContext and their nested ChordAnalysisResult / KeyModeAnalysisResult /
# ChordAnalysisTone / ChordTemporalExtensions). Dispositions are PROPOSALS (input to the
# Cowork/user rulings), never decisions.
#
# NO src/ is read or written; this is a data generator. Re-run: python
# tools/audit/notation_surface/gen_notation_surface_audit.py

import csv
import json
import os
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))

# ── Disposition-class vocabulary (dispatch Task 1) ───────────────────────────
#   A-SOURCED       : a declared A-surface source exists (DecodeResult/SegmentSummary
#                     field OR a ratified planned publication: full posterior OI-193,
#                     un-rounded modal reading C1, ornament labels OI-194, derived chord facts)
#   DERIVABLE       : recomputable from A-published facts (derivation named)
#   RETIRE-CANDIDATE: no live consumer reads it (or its concern dissolves under A)
#   UNRESOLVED      : cannot be dispositioned from A's surface + the ratified publications
ROLES = {"decision", "presentation", "diagnostic", "carried"}
CLASSES = {"A-SOURCED", "DERIVABLE", "RETIRE-CANDIDATE", "UNRESOLVED"}

# A's published surface, for the source column (jointdecoder.h DecodeResult/SegmentSummary
# + jointfactadapter.h L1 facts + the ratified planned publications).
A_SEG = "SegmentSummary"           # per-segment MAP record (startTick,endTick,tonicPc,isMajor,key,classKey,rootPc,degree,quality,inversion,target)
A_POST = "posterior(OI-193)"       # full forward-backward marginals + ranked alternatives + model probabilities
A_MODAL = "modal-reading(C1)"      # un-rounded modal color, published beside the two-mode key
A_CHORD = "derived-chord-facts"    # chord symbol / root spelling / bass / extensions, derived from (tonic,mode,class,inversion)
A_L1 = "L1-note-surface"           # the sounding notes A's fact adapter already consumes (notatedNotes)

# ── The enumeration ──────────────────────────────────────────────────────────
# Columns: consumer, entry_point, carrier, field_path, sites, fact, role, disposition, a_source
# `consumer` uses the short file key; `sites` are representative file:line anchors (READS).
ROWS = [
    # ============ sectionanalyzer.cpp (analyzeSection: HarmonicRegion -> AnalyzedRegion + KeyArea) ============
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "startTick",
     "212, 476-717", "region start tick (raw->analyzed translate; measure layout, trim, merge, gap-fill)",
     "decision", "A-SOURCED", A_SEG + ".startTick"),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "endTick",
     "213, 476-717", "region end tick (translate; layout/trim/merge/gap boundaries)",
     "decision", "A-SOURCED", A_SEG + ".endTick"),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "chordResult",
     "214", "chord identity+function, carried into AnalyzedRegion + merge/gap logic",
     "decision", "A-SOURCED", A_SEG + " + " + A_CHORD),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "alternatives",
     "214, 441", "ranked chord candidates, carried into AnalyzedRegion (never re-read here)",
     "carried", "A-SOURCED", A_POST + " (ranked alternatives)"),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "hasAnalyzedChord",
     "215", "sparse-region flag, carried into AnalyzedRegion; never read by any consumer",
     "carried", "RETIRE-CANDIDATE", "no live reader; A always decodes a segment"),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "keyModeResult",
     "216", "key/mode context, carried + stabilized",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor,key)"),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "tones",
     "217, 671, 708-709", "sounding tones, carried + recomputed for gap/trim regions",
     "decision", "DERIVABLE", A_L1 + " (re-collect over [startTick,endTick))"),
    ("sectionanalyzer.cpp", "analyzeSection", "HarmonicRegion", "temporalExtensions",
     "218", "temporal-context snapshot copied to AnalyzedRegion; no member ever field-read (comment L443)",
     "carried", "RETIRE-CANDIDATE", "no live reader on any consumer; decode-time-internal"),
    ("sectionanalyzer.cpp", "analyzeSection", "chordResult.identity", "rootPc",
     "133, 227, 251, 514", "committed root: degree derivation, adjacent-merge, gap/carry tests",
     "decision", "A-SOURCED", A_SEG + ".rootPc"),
    ("sectionanalyzer.cpp", "analyzeSection", "chordResult.identity", "bassPc",
     "252", "region bass, gap-tone-matches-bass test",
     "decision", "DERIVABLE", A_SEG + ".inversion + class members"),
    ("sectionanalyzer.cpp", "analyzeSection", "chordResult.identity", "quality",
     "227, 232", "quality: adjacent-merge equality, Sus gap-tone block",
     "decision", "A-SOURCED", A_SEG + ".quality (" + A_CHORD + ")"),
    ("sectionanalyzer.cpp", "analyzeSection", "chordResult.function", "degree",
     "140, 275", "diatonic-degree gate (degree>=0) for diatonicToKey",
     "decision", "A-SOURCED", A_SEG + ".degree"),
    ("sectionanalyzer.cpp", "analyzeSection", "keyModeResult", "keySignatureFifths",
     "105, 109, 129, 135, 751", "island key-stabilization compare + tonicPc + key-area grouping",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor)->fifths (keySignatureFifthsForKey)"),
    ("sectionanalyzer.cpp", "analyzeSection", "keyModeResult", "mode",
     "106, 110, 130-131, 752", "stabilization compare + keyModeTonicOffset/ScaleIntervals + key-area mode",
     "decision", "A-SOURCED", A_SEG + ".isMajor + " + A_MODAL),
    ("sectionanalyzer.cpp", "analyzeSection", "keyModeResult", "normalizedConfidence",
     "753, 760", "key-area grouping: confidence >= 0.8 opens a new area, keeps area max",
     "decision", "A-SOURCED", A_POST + " (key-marginal mass)"),
    ("sectionanalyzer.cpp", "analyzeSection", "ChordAnalysisTone", "pitch",
     "80, 100, 142, 245, 494, 708", "distinct-PC count, scale-membership (diatonicToKey), gap-tone PC sets",
     "decision", "DERIVABLE", A_L1 + " (sounding note pcs)"),
    ("sectionanalyzer.cpp", "analyzeSection", "ChordAnalysisTone", "tpc",
     "330, 400", "bass spelling of an inferred sparse/gap chord",
     "decision", "DERIVABLE", A_L1 + " (note tpc)"),

    # ============ sectioncadencedetection.cpp (detectCadences / detectPivotChords over AnalyzedRegion) ============
    ("sectioncadencedetection.cpp", "analyzeSection", "keyModeResult", "normalizedConfidence",
     "56, 78-79, 174, 203", "hasAssertiveKeyConfidence (>=0.8) gates cadence + pivot labels",
     "decision", "A-SOURCED", A_POST + " (key-marginal mass)"),
    ("sectioncadencedetection.cpp", "analyzeSection", "keyModeResult", "keySignatureFifths",
     "87-88, 180-187, 203", "cadence requires same key; pivot key-change detection",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor)->fifths"),
    ("sectioncadencedetection.cpp", "analyzeSection", "keyModeResult", "mode",
     "89-90, 184-205", "cadence requires same mode; pivot key-change; tonicPc via keyModeTonicOffset",
     "decision", "A-SOURCED", A_SEG + ".isMajor"),
    ("sectioncadencedetection.cpp", "analyzeSection", "chordResult.identity", "rootPc",
     "94, 230", "cadence roots must differ; pivot root in incoming scale",
     "decision", "A-SOURCED", A_SEG + ".rootPc"),
    ("sectioncadencedetection.cpp", "analyzeSection", "chordResult.identity", "quality",
     "102-109", "PAC dominant non-minor; DC major->minor deceptive test",
     "decision", "A-SOURCED", A_SEG + ".quality"),
    ("sectioncadencedetection.cpp", "analyzeSection", "chordResult.function", "degree",
     "101-131, 227", "cadence class (PAC/PC/DC/HC) + pivot diatonic-to-outgoing-key from degree",
     "decision", "A-SOURCED", A_SEG + ".degree (A's native cadence factor, OI-166)"),
    ("sectioncadencedetection.cpp", "analyzeSection", "AnalyzedRegion", "startTick",
     "121-132, 249", "cadence/pivot label write-tick placement",
     "decision", "A-SOURCED", A_SEG + ".startTick"),

    # ============ notationcomposingbridge.cpp (+helpers): single-note + region-emit + status-bar ============
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedSection", "regions",
     "249, 254, 1006, 1015, 1379", "region list: note-containment lookup + emission set",
     "decision", "A-SOURCED", A_SEG + " sequence"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedSection", "keyAreas",
     "1016, 1086-1102, 1130", "key-area list: bracket markers + effective Roman key",
     "decision", "DERIVABLE", "collapse " + A_SEG + " key sequence into areas"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "startTick",
     "256, 1021, 1071, 1111", "region containment + selection split + min-duration gate + annotation segment",
     "decision", "A-SOURCED", A_SEG + ".startTick"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "endTick",
     "256, 271, 1072, 1113", "containment + boundary tie-break + min-duration gate",
     "decision", "A-SOURCED", A_SEG + ".endTick"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "chordResult",
     "298, 1136", "primary decoded chord -> chordResults[0] / annotationResult",
     "decision", "A-SOURCED", A_SEG + " + " + A_CHORD),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "alternatives",
     "297, 301-302", "candidates [1..] -> NoteHarmonicContext.chordResults[1..] (context menu / status bar)",
     "decision", "A-SOURCED", A_POST + " (ranked alternatives)"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "keyModeResult",
     "278-279, 1118-1119", "per-region key -> context.keyFifths/keyMode + chord-symbol spelling key",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor,fifths)"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "keyAreaId",
     "285, 1081", "enclosing key-area index (bracket markers, enclosingKeyArea)",
     "decision", "DERIVABLE", "key-area index from collapsed " + A_SEG + " sequence"),
    ("notationcomposingbridge.cpp", "analyzeSection", "AnalyzedRegion", "temporalExtensions",
     "281", "whole-struct copy into NoteHarmonicContext.temporalExtensions; no sub-field read",
     "carried", "RETIRE-CANDIDATE", "no live reader downstream"),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "chordResult.identity", "rootPc",
     "95, 1142, 1206", "sparse-chord degree; annotation degree; pedal-name chord root",
     "decision", "A-SOURCED", A_SEG + ".rootPc"),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "chordResult.identity", "quality",
     "1153, 1158", "Unknown-gate for chord-track roman-quality refinement",
     "decision", "A-SOURCED", A_SEG + ".quality"),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "chordResult.identity", "score",
     "836", "status-bar candidate '(%.2f)' score suffix",
     "presentation", "A-SOURCED", A_POST + " (candidate model probability)"),
    ("notationcomposingbridge.cpp", "analyzeSection", "chordResult.identity", "isPedalPoint",
     "1202", "gate: emit 'X ped.' pedal-point StaffText annotation",
     "decision", "UNRESOLVED", "A DecodeResult/SegmentSummary carries no pedal-point concept -> user (decision-doc §3)"),
    ("notationcomposingbridge.cpp", "analyzeSection", "chordResult.identity", "pedalBassPc",
     "1203, 1206-1207", "pedal bass note for the 'X ped.' annotation",
     "decision", "UNRESOLVED", "A carries no pedal-bass concept -> user (decision-doc §3)"),
    ("notationcomposingbridge.cpp", "analyzeSection", "chordResult.function", "degree",
     "97, 1144, 1154-1155", "diatonic-degree gate for sparse/annotation Roman refinement",
     "decision", "A-SOURCED", A_SEG + ".degree"),
    ("notationcomposingbridge.cpp", "analyzeSection", "keyModeResult", "keySignatureFifths",
     "278, 1118", "context.keyFifths + per-region chord-symbol spelling key",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor)->fifths"),
    ("notationcomposingbridge.cpp", "analyzeSection", "keyModeResult", "mode",
     "279, 771, 863, 1119", "context.keyMode + status-bar/area key-string suffix (keyModeSuffix)",
     "decision", "A-SOURCED", A_SEG + ".isMajor + " + A_MODAL),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "keyModeResult", "normalizedConfidence",
     "280 (helpers.cpp:192)", "-> NoteHarmonicContext.keyConfidence (carried; no in-tree reader)",
     "carried", "A-SOURCED", A_POST + " (key-marginal mass)"),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "keyModeResult", "score",
     "helpers.cpp:194", "written to *outScore; the only caller passes no ptr (dead)",
     "diagnostic", "RETIRE-CANDIDATE", "dead path; no live reader"),
    ("notationcomposingbridge.cpp", "analyzeSection", "KeyArea", "keyFifths",
     "859, 862, 1045, 1130", "status-bar area string + bracket-marker tonic + effective Roman key",
     "decision", "DERIVABLE", "= area key from collapsed " + A_SEG + " sequence"),
    ("notationcomposingbridge.cpp", "analyzeSection", "KeyArea", "mode",
     "859, 863, 1047-1059, 1131", "bracket-marker case/suffix branches on exotic mode; area Roman key",
     "decision", "A-SOURCED", A_SEG + ".isMajor + " + A_MODAL),
    ("notationcomposingbridge.cpp", "analyzeSection", "KeyArea", "startTick",
     "1087-1088", "prev/new area starts for bracket-marker placement + pivot suppression",
     "decision", "DERIVABLE", "area span bound from collapsed " + A_SEG + " sequence"),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "ChordAnalysisTone", "pitch",
     "100, 133, 143, 155-166", "sparse-chord inference: bass/root/PC-set of a thin region",
     "decision", "DERIVABLE", A_L1 + " (sounding note pcs)"),
    ("notationcomposingbridge.cpp", "analyzeNoteHarmonicContext", "ChordAnalysisTone", "tpc",
     "157", "bass spelling (bassTpc) of the inferred sparse chord",
     "decision", "DERIVABLE", A_L1 + " (note tpc)"),

    # ============ notationimplodebridge.cpp (analyzeHarmonicRhythm -> analyzeSection -> chord track) ============
    ("notationimplodebridge.cpp", "analyzeSection", "AnalyzedRegion", "startTick",
     "251, 577, 634, 666, 857", "key-run duration, display-region lookup, tone window, merge gap, note placement",
     "decision", "A-SOURCED", A_SEG + ".startTick"),
    ("notationimplodebridge.cpp", "analyzeSection", "AnalyzedRegion", "endTick",
     "251, 595, 669, 858-859", "key-run stability, merge extend, min-display-duration gate",
     "decision", "A-SOURCED", A_SEG + ".endTick"),
    ("notationimplodebridge.cpp", "analyzeSection", "AnalyzedRegion", "chordResult",
     "303, 862, 1100, 1153-1174", "coalescing key + voicing + chord-symbol/roman/nashville formatting",
     "decision", "A-SOURCED", A_SEG + " + " + A_CHORD),
    ("notationimplodebridge.cpp", "analyzeSection", "AnalyzedRegion", "keyModeResult",
     "185-256, 863-864", "key-run label + KeySig write (fifths) + spelling key + coalescing",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor,fifths)"),
    ("notationimplodebridge.cpp", "analyzeSection", "AnalyzedRegion", "tones",
     "671, 1074, 1096-1108", "voicing pitches for the imploded chord-track chord",
     "decision", "DERIVABLE", A_L1 + " (re-collect over segment span)"),
    ("notationimplodebridge.cpp", "analyzeSection", "AnalyzedRegion", "hasAssertiveExposure",
     "195, 253, 867", "gates KeySig exposure, '?' mark, relationship/pivot, non-diatonic marker",
     "decision", "A-SOURCED", A_POST + " (key-marginal mass >= threshold)"),
    ("notationimplodebridge.cpp", "analyzeSection", "chordResult.identity", "rootPc",
     "303, 1015-1027", "coalescing equality + pivot root-in-scale",
     "decision", "A-SOURCED", A_SEG + ".rootPc"),
    ("notationimplodebridge.cpp", "analyzeSection", "chordResult.identity", "quality",
     "304, 1183", "coalescing equality + fallback-refined roman-quality emit gate",
     "decision", "A-SOURCED", A_SEG + ".quality"),
    ("notationimplodebridge.cpp", "analyzeSection", "chordResult.function", "degree",
     "1012, 1180", "pivot diatonic (degree>=0) + roman-numeral fallback gate",
     "decision", "A-SOURCED", A_SEG + ".degree"),
    ("notationimplodebridge.cpp", "analyzeSection", "chordResult.function", "diatonicToKey",
     "1205", "gates the non-diatonic (borrowed/secondary) marker",
     "decision", "DERIVABLE", "from " + A_SEG + ".degree/classKey (diatonic vs chromatic/applied class)"),
    ("notationimplodebridge.cpp", "analyzeSection", "keyModeResult", "keySignatureFifths",
     "185-243, 863", "key-run label + KeySig element fifths + spelling/formatter key",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor)->fifths"),
    ("notationimplodebridge.cpp", "analyzeSection", "keyModeResult", "mode",
     "186-256, 864", "key-label suffix + coalescing + relationship/pivot/borrowed-key (exotic branches)",
     "decision", "A-SOURCED", A_SEG + ".isMajor + " + A_MODAL),
    ("notationimplodebridge.cpp", "analyzeSection", "keyModeResult", "normalizedConfidence",
     "84, 189-235, 307-308", "OI-182 exposure gates + mode-suffix threshold + coalescing bucket",
     "decision", "A-SOURCED", A_POST + " (key-marginal mass/gap)"),
    ("notationimplodebridge.cpp", "analyzeSection", "ChordAnalysisTone", "pitch",
     "1075-1076", "voicing dedup by MIDI pitch (bass/treble split)",
     "decision", "DERIVABLE", A_L1 + " (sounding note pitches)"),

    # ============ notationtuningbridge.cpp (analyzeHarmonicRhythm region tuning + single-note tuning) ============
    ("notationtuningbridge.cpp", "analyzeHarmonicRhythm", "HarmonicRegion", "startTick",
     "787", "region tuning-loop start (which notes are retuned)",
     "decision", "A-SOURCED", A_SEG + ".startTick"),
    ("notationtuningbridge.cpp", "analyzeHarmonicRhythm", "HarmonicRegion", "endTick",
     "788", "region tuning-loop end bound",
     "decision", "A-SOURCED", A_SEG + ".endTick"),
    ("notationtuningbridge.cpp", "analyzeHarmonicRhythm", "chordResult.identity", "rootPc",
     "792, 794, 796", "tuning-offset lookup (semitoneFromPitches, tuningOffset, rootOffset)",
     "decision", "A-SOURCED", A_SEG + ".rootPc"),
    ("notationtuningbridge.cpp", "analyzeHarmonicRhythm", "chordResult.identity", "quality",
     "793", "tuningSystem.tuningOffset(quality,...) argument",
     "decision", "A-SOURCED", A_SEG + ".quality"),
    ("notationtuningbridge.cpp", "analyzeHarmonicRhythm", "HarmonicRegion", "keyModeResult",
     "793, 796", "whole key/mode struct passed to tuningOffset/rootOffset (tonic-anchored tuning)",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor,fifths)"),

    # ============ notationinteraction.cpp (analyzeNoteHarmonicContext -> write chord symbol/RN/Nashville) — OUT OF EXPECTED ROSTER ============
    ("notationinteraction.cpp", "analyzeNoteHarmonicContext", "ChordAnalysisResult", "results[0]",
     "8316-8318", "top candidate -> formatChordResultForStatusBar -> Harmony element written to score",
     "decision", "A-SOURCED", A_SEG + " + " + A_CHORD),
    ("notationinteraction.cpp", "analyzeNoteHarmonicContext", "(out-param)", "keyFifths",
     "8309-8318", "spelling key for the written chord symbol / Roman numeral",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor)->fifths"),

    # ============ notationcontextmenumodel.cpp (analyzeNoteHarmonicContextDetails -> right-click menu) — OUT OF EXPECTED ROSTER ============
    ("notationcontextmenumodel.cpp", "analyzeNoteHarmonicContextDetails", "NoteHarmonicContext", "keyFifths",
     "58, 86-88", "spelling key for menu chord-symbol/roman/nashville formatting",
     "decision", "A-SOURCED", A_SEG + " (tonic,isMajor)->fifths"),
    ("notationcontextmenumodel.cpp", "analyzeNoteHarmonicContextDetails", "NoteHarmonicContext", "chordResults",
     "85-88", "each candidate -> formatSymbol/formatRomanNumeral/formatNashvilleNumber menu items",
     "decision", "A-SOURCED", A_SEG + " + " + A_POST + " + " + A_CHORD),
    ("notationcontextmenumodel.cpp", "analyzeNoteHarmonicContextDetails", "chordResults[].identity", "score",
     "91", "menu-label '(%.2f)' score suffix",
     "presentation", "A-SOURCED", A_POST + " (candidate model probability)"),
    ("notationcontextmenumodel.cpp", "analyzeNoteHarmonicContextDetails", "chordResults[].identity", "rootPc",
     "124", "'tune as' menu entry root",
     "decision", "A-SOURCED", A_SEG + ".rootPc"),
    ("notationcontextmenumodel.cpp", "analyzeNoteHarmonicContextDetails", "chordResults[].identity", "quality",
     "124", "'tune as' menu entry quality",
     "decision", "A-SOURCED", A_SEG + ".quality"),

    # ============ notationaccessibility.cpp — STRING consumer only (no struct field) ============
    ("notationaccessibility.cpp", "harmonicAnnotation", "(std::string)", "harmonicAnnotation(note)",
     "204, 206", "pre-formatted status-bar annotation string appended to accessibility text; NO struct read",
     "presentation", "A-SOURCED", "downstream of the composingbridge status-bar formatter (no direct surface read)"),
]

# ── The consumer roster (live production consumers of the surface) ────────────
# expected = the decision-doc §1 named roster; found = what the tree-wide sweep decided.
EXPECTED_ROSTER = [
    "notationcomposingbridge", "notationimplodebridge", "notationtuningbridge",
    "sectionanalyzer(+downstream function-labeling)", "accessibility",
]
ROSTER = OrderedDict([
    ("notationharmonicrhythmbridge.cpp", "SEAM/producer: reads config + plumbs 21 mode priors; returns HarmonicRegion vector (no region field read)"),
    ("notationcomposingbridge.cpp(+helpers.cpp)", "main analysis: single-note context + region-emit annotations + status-bar string"),
    ("notationimplodebridge.cpp", "chord-track implode: key runs, voicing, chord-symbol/roman/nashville, OI-182 constants, cadence"),
    ("notationtuningbridge.cpp", "region + single-note intonation (tuning offsets)"),
    ("sectionanalyzer.cpp", "HarmonicRegion->AnalyzedRegion translation + key stabilization + gap-fill + key-area grouping"),
    ("sectioncadencedetection.cpp", "detectCadences / detectPivotChords (cadence + pivot staff-text labels)"),
    ("notationinteraction.cpp", "OUT-OF-ROSTER (found by sweep): analyzeNoteHarmonicContext -> writes Harmony elements to score"),
    ("notationscene/notationcontextmenumodel.cpp", "OUT-OF-ROSTER (found by sweep): analyzeNoteHarmonicContextDetails -> right-click analysis menu"),
    ("notationaccessibility.cpp", "STRING consumer only (harmonicAnnotation string); reads no struct field"),
])
DORMANT = OrderedDict([
    ("functionresolver.{h,cpp}", "DORMANT (no production consumer): internal L4->L5 FunctionSlice/FunctionalCadence types"),
    ("functionprogression.{h,cpp}", "DORMANT: internal ProgressionChord/ProgressionSlice licensing predicates"),
    ("functionromannumeral.{h,cpp}", "DORMANT: BaseRomanNumeralInput wrapper -> shared formatRomanNumeral"),
])

# ── Task 2 — exotic-mode (KeySigMode beyond Ionian/Aeolian) consumer sites ────
EXOTIC_MODE_SITES = [
    {"site": "notationharmonicrhythmbridge.cpp:92-113", "what": "plumbs all 21 mode priors from IComposingAnalysisConfiguration into keyPrefs.modePrior* (the 19 exotic priors + Ionian/Aeolian)",
     "disposition": "RETIRE under C1 (two-mode key): the 19 exotic-mode priors go dead; the whole 21-prior stack retires (retirement-map item 2)"},
    {"site": "icomposinganalysisconfiguration.h:157-252", "what": "21 mode-prior getters/setters/notifications + applyModePriorPreset/currentModePriorPreset",
     "disposition": "RETIRE under C1 (the interface's 21-prior block); modeNameConfidenceThreshold(:117) retires with the suffix-vs-fallback gate"},
    {"site": "composingconfiguration.cpp:62-.. (+ MODE_NAME_CONFIDENCE_THRESHOLD:48)", "what": "21 MODE_PRIOR settings keys + impls + MODE_NAME_CONFIDENCE_THRESHOLD",
     "disposition": "RETIRE under C1 (the persisted settings + registration)"},
    {"site": "composingpreferencesmodel.{h,cpp} (88 modePrior refs)", "what": "the 21 mode-prior UI-model properties (Q_PROPERTY + getters/setters/signals)",
     "disposition": "RETIRE under C1 (the preferences-model surface)"},
    {"site": "preferences/qml/.../ComposingAnalysisSection.qml (105 modePrior refs) + ComposingPreferencesPage.qml", "what": "the 21 mode-prior UI sliders + bindings",
     "disposition": "RETIRE under C1 (the UI panel exposing the exotic-mode priors)"},
    {"site": "notationcomposingbridge.cpp:1047-1049", "what": "makeBracketMarker: isMajorLike branch on Ionian/Lydian/Mixolydian -> bracket tonic letter case",
     "disposition": "C1: two-mode isMajor suffices for the case decision; exotic branch retires"},
    {"site": "notationcomposingbridge.cpp:1053-1059", "what": "makeBracketMarker: Ionian/Aeolian/HarmonicMinor/MelodicMinor -> bare-colon vs keyModeSuffix marker form",
     "disposition": "C1: the exotic-mode bracket-suffix forms retire; the modal reading is published beside the two-mode key"},
    {"site": "notationcomposingbridge.cpp:771, 863", "what": "status-bar + enclosing-area key string via keyModeSuffix(mode) for all 21 modes",
     "disposition": "C1: two-mode suffix (major/minor) + published un-rounded modal reading replaces the 21-value suffix"},
    {"site": "notationcomposingbridge.cpp:91 (helper), 1140", "what": "keyModeScaleIntervals(mode) degree lookup — per-mode scale (branches implicitly on all 21)",
     "disposition": "A-SOURCED: A's degree state is native scale-degree relative to (tonic, major/minor); the per-mode scale table is not needed"},
    {"site": "notationimplodebridge.cpp:103-119", "what": "fallbackModeSuffix + keyAnnotationBaseLabel: keyModeIsMajor collapse to Ionian/Aeolian below modeNameConfidenceThreshold, else keyModeSuffix(all 21)",
     "disposition": "C1: the confidence-gated exotic-vs-broad suffix machinery retires; two-mode label + modal reading"},
    {"site": "notationimplodebridge.cpp:941-1004, 1233-1269", "what": "relationship arrows, modulation-pivot, borrowed-key search over all KEY_MODE_COUNT modes (Ionian/Aeolian tie-break at :1233-1252)",
     "disposition": "C1: the exotic-mode relationship/borrowed-key machinery retires; the two-mode key + posterior alternatives replace it"},
    {"site": "keymodeformatting.cpp:82-134 (keyModeSuffix/keyModeTonicName)", "what": "the 21-mode display-name + suffix tables the notation path routes through",
     "disposition": "The shared formatter the notation path calls; under C1 the exotic-name tables become unreachable from the notation surface (retire with the 21-value mode)"},
]

# ── Task 3 — OI-182 exposure-bucket + related confidence constants ────────────
OI182 = [
    {"const": "kTentativeKeyExposureThreshold = 0.5", "loc": "notationimplodebridge.cpp:79",
     "fed_by": "keyModeResult.normalizedConfidence (the emission sigmoid)",
     "controls": "supportsTentativeKeyExposure(:84) -> run.hasTentativeExposure -> finishRun emission gate (:205, discards key run if untrue); keyExposureBucket lower bound",
     "disposition": "confidence-mapping: replace with the B-full posterior key-marginal mass/gap threshold (contract's confidence-mapping ruling)"},
    {"const": "kAssertiveKeyExposureThreshold = 0.8", "loc": "notationimplodebridge.cpp:80",
     "fed_by": "keyModeResult.normalizedConfidence",
     "controls": "keyExposureBucket(:92) bucket 1<->2 boundary -> sameUserFacingInference region coalescing (:307-308). (Actual KeySig exposure uses AnalyzedRegion.hasAssertiveExposure, set by analyzeSection at the same 0.8 on normalizedConfidence.)",
     "disposition": "confidence-mapping: replace with posterior key-marginal mass threshold; shares its fate with hasAssertiveExposure"},
    {"const": "keyExposureBucket(confidence)->{0,1,2}", "loc": "notationimplodebridge.cpp:87-96",
     "fed_by": "keyModeResult.normalizedConfidence (:307-308)",
     "controls": "sameUserFacingInference region-coalescing equality -> chord-track segmentation (merge loop :665-677)",
     "disposition": "confidence-mapping: the bucketed confidence-equality re-expresses as a posterior-mass band; retires with normalizedConfidence"},
    {"const": "kSameChordReannotationGap = 2*480 = 960 ticks", "loc": "notationimplodebridge.cpp:661",
     "fed_by": "gapFromLastAnnotation = r.startTick - merged.back().startTick (:666) + sameUserFacingInference (:665)",
     "controls": "merge condition (:667): consecutive same-chord sub-regions merge (<960) vs separate re-annotations (>=960) -> chord-track segmentation",
     "disposition": "presentation-timing constant (not a confidence value); survives the switch as an emitter-side option over A's segment stream (re-home to the notation emitter, not the inference layer)"},
    {"const": "fallbackModeSuffix()", "loc": "notationimplodebridge.cpp:103-108",
     "fed_by": "KeySigMode mode (via keyModeIsMajor) + modeNameConfidenceThreshold=0.35 gate (:115-117)",
     "controls": "under low confidence, collapse the exotic mode suffix to plain major/minor (Ionian/Aeolian)",
     "disposition": "RETIRE under C1: the two-mode label is the default; the un-rounded modal reading is published beside it (no rounded exotic label to fall back from)"},
    {"const": "modeNameConfidenceThreshold = 0.35 (Gate L)", "loc": "icomposinganalysisconfiguration.h:117; composingconfiguration.cpp:48",
     "fed_by": "keyModeResult.normalizedConfidence",
     "controls": "picks the true per-mode suffix vs fallbackModeSuffix in keyAnnotationBaseLabel (:115-117)",
     "disposition": "RETIRE under C1 (no exotic suffix to gate); its confidence role folds into the posterior-mass mapping"},
    {"const": "kAnnotateKeyConfidenceThreshold = 0.8", "loc": "sectionanalyzer.h:91 (hasAssertiveKeyConfidence, key-area open at :760)",
     "fed_by": "keyModeResult.normalizedConfidence",
     "controls": "cadence/pivot gate (sectioncadencedetection.cpp:56) + key-area opening (sectionanalyzer.cpp:760) + AnalyzedRegion.hasAssertiveExposure",
     "disposition": "confidence-mapping: the 0.8 assertive bar maps to a posterior key-marginal mass threshold (B-full)"},
]

# ── Task 4 — the in-memory-only fields (confirm no production consumer) ───────
TASK4 = {
    "keyAlternatives": {
        "definition": "harmonicrhythm.h:118",
        "population": "regionanalyzer.cpp:279,552,1043,1062",
        "readers_found": ["regionanalysis_tests.cpp:510,518-525 (TEST ONLY)"],
        "production_consumer": False,
        "note": "No production consumer; a composing-layer regression test is the only reader. Not carried into AnalyzedRegion at all. Confirmed at code — unchanged vs decision-doc §1.",
    },
    "fanout": {
        "definition": "harmonicrhythm.h:130",
        "population": "regionanalyzer.cpp:1066,1262,1454 (computeRawFanoutSummary)",
        "readers_found": ["tools/batch_analyze.cpp:699,1419-1422 (--dump-fanout diagnostic, batch surface, read-only)"],
        "production_consumer": False,
        "note": "No reader anywhere in src/; only the batch --dump-fanout diagnostic (tools/) reads it. Not on the notation path. Confirmed at code — unchanged vs decision-doc §1.",
    },
}

# ── Emit ──────────────────────────────────────────────────────────────────────
def write_csv():
    path = os.path.join(HERE, "consumption_fields.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["consumer", "entry_point", "carrier", "field_path", "read_sites",
                    "fact", "role", "disposition_class", "a_surface_source_or_derivation"])
        for r in ROWS:
            assert r[6] in ROLES, "bad role: " + r[6]
            assert r[7] in CLASSES, "bad class: " + r[7]
            w.writerow(r)
    return path, len(ROWS)


def build_summary():
    by_class = Counter(r[7] for r in ROWS)
    by_role = Counter(r[6] for r in ROWS)
    by_consumer = Counter(r[0] for r in ROWS)
    # decision-bearing fields that are UNRESOLVED (the findings that return to the user)
    unresolved = [
        {"consumer": r[0], "field": r[2] + "." + r[3], "sites": r[4], "fact": r[5], "why": r[8]}
        for r in ROWS if r[7] == "UNRESOLVED"
    ]
    retire = [
        {"consumer": r[0], "field": r[2] + "." + r[3], "sites": r[4], "note": r[8]}
        for r in ROWS if r[7] == "RETIRE-CANDIDATE"
    ]
    entry_points = sorted({r[1] for r in ROWS})
    carriers = sorted({r[2] for r in ROWS})
    summary = OrderedDict()
    summary["dispatch"] = "cc_instruction_notation_consumption_audit.md (READ-ONLY)"
    summary["decision_surface"] = "cowork_notation_adoption_increment.md §8.1 (user-ratified 2026-07-26)"
    summary["scope"] = "READS of the notation harmonic-analysis output surface by live production consumers"
    summary["total_field_rows"] = len(ROWS)
    summary["disposition_class_counts"] = OrderedDict(sorted(by_class.items()))
    summary["role_counts"] = OrderedDict(sorted(by_role.items()))
    summary["rows_per_consumer"] = OrderedDict(sorted(by_consumer.items()))
    summary["entry_points"] = entry_points
    summary["carrier_types"] = carriers
    summary["roster_expected"] = EXPECTED_ROSTER
    summary["roster_found"] = OrderedDict(ROSTER)
    summary["roster_found_beyond_expected"] = [
        "notationinteraction.cpp (harmony-writing; via single-note entry analyzeNoteHarmonicContext)",
        "notationscene/notationcontextmenumodel.cpp (right-click analysis menu; via analyzeNoteHarmonicContextDetails)",
        "sectioncadencedetection.cpp (part of the section layer; cadence/pivot labels)",
        "notationcomposingbridgehelpers.cpp (part of the composingbridge)",
    ]
    summary["second_entry_point"] = "analyzeNoteHarmonicContext / analyzeNoteHarmonicContextDetails (single-note; returns ChordAnalysisResult / NoteHarmonicContext) — a SECOND surface beyond analyzeHarmonicRhythm, not named in decision-doc §1"
    summary["dormant_no_consumer"] = OrderedDict(DORMANT)
    summary["accessibility_is_string_only"] = "notationaccessibility.cpp reads NO struct field; consumes only the pre-formatted harmonicAnnotation(Note*) string (singleElementAccessibilityInfo :173/:204/:206)"
    summary["task2_exotic_mode_sites"] = EXOTIC_MODE_SITES
    summary["task2_site_count"] = len(EXOTIC_MODE_SITES)
    summary["task3_oi182_constants"] = OI182
    summary["task4_in_memory_only_fields"] = TASK4
    summary["unresolved_findings"] = unresolved
    summary["unresolved_count"] = len(unresolved)
    summary["retire_candidates"] = retire
    path = os.path.join(HERE, "summary.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    return path, summary


def main():
    csv_path, n = write_csv()
    json_path, summary = build_summary()
    print("wrote {} ({} field rows)".format(csv_path, n))
    print("wrote {}".format(json_path))
    print("disposition classes:", dict(summary["disposition_class_counts"]))
    print("unresolved findings:", summary["unresolved_count"])
    print("task2 exotic-mode sites:", summary["task2_site_count"])
    print("live consumers in roster:", len(summary["roster_found"]))


if __name__ == "__main__":
    main()
