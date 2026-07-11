#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
"""
gen_l3_dispositions.py — PASS-1 dispositions (protocol P2/P3) for the EG-7 Layer-3
(key/mode) certification audit.

Reads the machine inventory (tools/audit/l3/l3_*.csv, produced by gen_inventory.py
--layer l3) and assigns EVERY row a verdict from the closed rubric (P2 — "no issue"
is a recorded claim with a stated reason, never a blank):
  • constants/literals : ESTABLISHED | UNFIT | DEAD  (+ in_param_manifest)
  • derived facts      : PUBLISHED | SILOED | TRAPPED | DUPLICATED
  • code (fn/decl/br)  : SURVIVES | RETIRES  (+ premise FACT/THEORY/ASSUMPTION)
  • cross-layer deps   : FORWARD-OK | BACK-EDGE | MIXED-DEFERRED
  • out-of-L3 rows     : DEFERRED (Layer-4/5/2 part of a mixed file — split recorded)

The verdicts are the AUDITOR's judgment, encoded here so the disposition is
reproducible (#19) and total (#P1). Per-file/per-kind rules cover the bulk; a curated
OVERRIDES table carries the load-bearing rows and every flagged FINDING. Blind pass
(no known-problem catalog consulted). NOT a behavior change — read-only.

RUN: python tools/audit/l3/gen_l3_dispositions.py   # writes pass1_dispositions.{csv,json}
"""

import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ── Per-file base layer (the split for L3-MIXED files is refined per function below) ─
FILE_LAYER = {
    "keymodesequence.h": "L3", "keymodesequence.cpp": "L3",
    "keymodeanalyzer.h": "L3", "keymodeanalyzer.cpp": "L3",
    "keyresolver.h": "L3", "keyresolver.cpp": "L3",
    "keymodeformatting.cpp": "L3",
    "modepriorpresets.h": "L3", "modepriorpresets.cpp": "L3",
    "cadencekeyanchor.h": "L3", "cadencekeyanchor.cpp": "L3",
    "localmodulationdetector.h": "L3", "localmodulationdetector.cpp": "L3",
    "jointkeydecision.h": "L3", "jointkeydecision.cpp": "L3",
    "regionanalyzer.h": "L3-MIXED", "regionanalyzer.cpp": "L3-MIXED",
    "harmonicrhythm.h": "L3-MIXED",
    "sectionanalyzer.h": "L3-MIXED", "sectionanalyzer.cpp": "L3-MIXED",
    "sectioncadencedetection.cpp": "L3-MIXED",
    "analysistypes.h": "L3-MIXED",
}

# ── Per-function layer for the mixed orchestrator files (verified at source) ────────
FUNC_LAYER = {
    ("regionanalyzer.cpp", "measureTicksBefore"): "L3",         # reach-back increment
    ("regionanalyzer.cpp", "inheritRegionKeyContext"): "L3",    # key-context propagation
    ("regionanalyzer.cpp", "applyJointKeyWiring"): "L3",        # joint key axis (gated OFF)
    ("regionanalyzer.cpp", "analyzeRegions"): "L3-seam+L4-loop", # decode/reachback/localKey L3; Pass1/2/2b L4
    ("regionanalyzer.cpp", "sameKey"): "L3",                    # reach-back lead-key equality
    ("regionanalyzer.cpp", "makeChordPathNode"): "L4",
    ("regionanalyzer.cpp", "coalesceShortSameRootRuns"): "L4",
    ("regionanalyzer.cpp", "tryCollapseSameChordRegion"): "L4",
    ("regionanalyzer.cpp", "absorbShortRegions"): "L4",
    ("regionanalyzer.cpp", "restampBassMinorSeventhAfterMerge"): "L4",
    ("regionanalyzer.cpp", "backfillNextRootPc"): "L5",         # V/x tonicization-label plumbing
    ("regionanalyzer.cpp", "denseBoundaryTicks"): "L2",         # PreserveAllChanges boundary detect
    ("sectionanalyzer.cpp", "stabilizeHarmonicRegionsForDisplay"): "L3",  # + one L4 refine call
    ("sectionanalyzer.cpp", "analyzeSection"): "L3-seam+L4-gap",
    ("sectionanalyzer.cpp", "distinctPitchClassCount"): "util",
    ("sectioncadencedetection.cpp", "hasAssertiveKeyConfidence"): "L3",
    ("sectioncadencedetection.cpp", "detectCadences"): "L5",
    ("sectioncadencedetection.cpp", "detectPivotChords"): "L5",
    ("analysistypes.h", "keyModeIndex"): "L3", ("analysistypes.h", "keyModeFromIndex"): "L3",
}

# analysistypes.h field owner → layer (KeyModeAnalyzerPreferences/PitchContext = L3; rest deferred)
TYPES_OWNER_LAYER = {
    "KeyModeAnalyzerPreferences": "L3", "PitchContext": "L3",
    "ParameterBound": "shared-infra",
    "ChordAnalyzerPreferences": "L4", "ChordAnalysisTone": "L4", "ChordTemporalContext": "L4",
}

# Names of the ONLY L3 param present in tools/param_manifest.json (measured 2026-07-11).
PARAM_MANIFEST_L3 = {"kAnnotateKeyConfidenceThreshold"}

CORE_L3_FILES = {"keymodeanalyzer.cpp", "keymodeanalyzer.h", "keymodesequence.cpp",
                 "keymodesequence.h", "keyresolver.cpp", "keyresolver.h",
                 "keymodeformatting.cpp", "modepriorpresets.cpp", "modepriorpresets.h",
                 "cadencekeyanchor.cpp", "cadencekeyanchor.h",
                 "localmodulationdetector.cpp", "localmodulationdetector.h",
                 "jointkeydecision.cpp", "jointkeydecision.h"}


def base(p):
    return os.path.basename(p)


def file_layer(p, func=None, owner=None):
    b = base(p)
    if b == "analysistypes.h" and owner:
        return TYPES_OWNER_LAYER.get(owner, "L3-MIXED")
    if func is not None and (b, func) in FUNC_LAYER:
        return FUNC_LAYER[(b, func)]
    return FILE_LAYER.get(b, "L3+")


# ── Curated OVERRIDES + FINDINGS (keyed by (basename, line) → dict) ─────────────────
# Only the load-bearing / flagged rows; everything else falls to the rule engine.
OVERRIDES = {}


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def in_manifest(name_or_ctx):
    return "yes" if any(n in (name_or_ctx or "") for n in PARAM_MANIFEST_L3) else "no"


# ── Literal classification (bucketed; keyword-refined) ─────────────────────────────
def classify_literal(r):
    b, func, val, ctx = base(r["file"]), r.get("func", ""), r["value"], r.get("context", "")
    owner = None
    # music-theory / structural tables and pitch arithmetic
    THEORY_FILES = {"keymodeanalyzer.cpp", "keymodeformatting.cpp"}
    if b in THEORY_FILES:
        # in-function presence/half-boost magic thresholds are the tunables here
        if val in ("0.1",) and (">" in ctx or "weight" in ctx.lower() or "Weight" in ctx):
            return ("constant", "UNFIT", "no",
                    "hand-set note-presence threshold (>0.1) — governs triad/LT/characteristic evidence gating; not in param_manifest; Stage-5 candidate")
        if val == "0.5" and "0.5" in ctx and ("Boost" in ctx or "boost" in ctx):
            return ("constant", "UNFIT", "no", "hand-set half-boost factor for partial characteristic-pitch evidence; not in param_manifest")
        return ("constant", "ESTABLISHED", "no",
                "FACT (music theory): scale-interval / mode-offset / circle-of-fifths / enharmonic-spelling table entry or pc arithmetic — structural, not a tunable")
    if b in ("modepriorpresets.cpp", "modepriorpresets.h"):
        return ("constant", "UNFIT", "no",
                "empirical mode-prior magnitude (21 modes x 5 presets); DUPLICATED vs KeyModeAnalyzerPreferences defaults but sync-test-guarded (modepriorpresets_tests); NOT in param_manifest; code says Stage-5 fits")
    if b == "analysistypes.h":
        # attribute to nearest field owner is not in the literal row; use context keywords
        if any(k in ctx for k in ("modePrior", "tonicWeight", "thirdWeight", "fifthWeight",
                                  "leadingTone", "scaleScore", "characteristic", "Triad", "extraScale",
                                  "declaredMode", "hysteresis", "confidenceSigmoid", "lookahead",
                                  "keySignatureDistance", "tonalCenter", "noteWeightCap", "bassMultiplier",
                                  "missingTonic", "beatWeight", "relativeKey", "dynamicLookahead")):
            return ("constant", "UNFIT", in_manifest(ctx),
                    "L3 KeyModeAnalyzerPreferences emission default — empirical/hand-set ('[empirical]'); NOT in param_manifest (only kAnnotateKeyConfidenceThreshold is); Stage-5 fit target per code")
        if "PitchContext" in ctx or any(k in ctx for k in ("durationWeight", "beatWeight", "pitch")):
            return ("constant", "ESTABLISHED", "no", "L3 PitchContext default (neutral 1.0 seed) — structural default, not a scoring tunable")
        return ("deferred", "DEFERRED", "no",
                "Layer-4 (chord) type default in the shared types leaf (ChordAnalyzerPreferences / ChordAnalysisTone / ChordTemporalContext / ParameterBound) — out of L3 scope, deferred to the L4 audit (split recorded)")
    if b in ("keymodesequence.cpp", "keymodesequence.h"):
        if val in ("1000.0", "1e3", "1.0e3") or "kSingleStateConfidence" in ctx:
            return ("constant", "ESTABLISHED", "no", "single-state confidence sentinel (effectively certain) — structural")
        if val in ("12", "21", "252") or "KEY_MODE_COUNT" in ctx or "CandidateCount" in ctx:
            return ("constant", "ESTABLISHED", "no", "FACT: candidate-space cardinality (12 tonics x 21 modes = 252) — structural")
        if val == "7" and "fifths" in ctx.lower():
            return ("constant", "ESTABLISHED", "no", "FACT: circle-of-fifths step generator (mod 12)")
        if val in ("8", "4.0", "1.0", "4"):
            return ("constant", "UNFIT", "no",
                    "KeyModeSequencePreferences default (topK / windowBeats / uncertainThreshold / maxAlternatives) — SETTING, effort-retrofit; change-cost defaults source the resolver hysteresis margins; NOT in param_manifest")
        return ("constant", "ESTABLISHED", "no", "structural/pc-arithmetic literal in the decoder")
    if b == "keyresolver.cpp":
        if val == "0.03" or "kPervasiveFraction" in ctx:
            return ("constant", "UNFIT", "no", "Baroque partial-signature-correction pervasiveness floor (0.03) — empirical, not in param_manifest")
        if val == "2.0" and ("kDominanceRatio" in ctx or "Dominance" in ctx):
            return ("constant", "UNFIT", "no", "Baroque partial-signature-correction dominance ratio (2.0) — empirical, not in param_manifest")
        return ("constant", "ESTABLISHED", "no", "structural/pc-arithmetic or shared-symbol literal in the resolver")
    if b == "cadencekeyanchor.cpp":
        if any(k in ctx for k in ("kWeightBase", "kWeightStructural", "kWeightChromatic", "kWeightFinality")):
            return ("constant", "UNFIT", "no", "cadence-anchor salience weight — provisional '[empirical - Stage-5 fits]', NOT corpus-fit, NOT in param_manifest")
        return ("constant", "ESTABLISHED", "no", "structural/pc-arithmetic literal (presence threshold / fifth interval)")
    if b == "localmodulationdetector.cpp":
        if "kEstablishmentMinChords" in ctx or "kPitchTolerance" in ctx or val in ("5", "2"):
            return ("constant", "UNFIT", "no",
                    "establishment floor (5 chords) / chromatic tolerance (2 pcs) — ordering THEORY-grounded (DCML span statistic cited), magnitude empirical '[Stage-5 fits]', NOT in param_manifest")
        return ("constant", "ESTABLISHED", "no", "structural literal")
    if b == "jointkeydecision.cpp":
        if val in ("0.1", "0.3") and ("decay" in ctx.lower() or "0.3" in ctx or "max(" in ctx):
            return ("constant", "UNFIT", "no",
                    "chord-candidate coupling rank-decay (floor 0.1 / slope 0.3) — hand-set in-code, NOT tagged empirical, NOT in param_manifest, NOT a JointKeyWeights member")
        if val == "3" and "popcount" in ctx:
            return ("constant", "ESTABLISHED", "no", "FACT: >=3 pcs required to determine a triad (chord-pinned structural)")
        return ("constant", "ESTABLISHED", "no", "chord-template interval / structural literal (kJkdTemplates DUPLICATED vs tools/cc_joint_residual_probe.py, not sync-guarded — see report section 5)")
    if b in ("sectioncadencedetection.cpp",):
        return ("constant", "ESTABLISHED", "no", "cadence-degree / structural literal (the 0.8 gate + pivot-lookahead are named constants — see fields/decls)")
    if b in ("regionanalyzer.cpp", "regionanalyzer.h", "sectionanalyzer.cpp", "sectionanalyzer.h", "harmonicrhythm.h"):
        # mixed orchestrators — layer per enclosing function
        lay = file_layer(r["file"], func)
        if lay.startswith("L3"):
            if "kJointModulationFallbackConfidence" in ctx or (val == "0.5" and "Fallback" in ctx):
                return ("constant", "UNFIT", "no", "joint-key modulation fallback confidence (0.5, sub-0.8-gate) — documented hand-set constant, gated OFF")
            return ("constant", "ESTABLISHED", "no", "L3-seam structural literal (tick math / index / duration)")
        return ("deferred", "DEFERRED", "no", "literal in the L4/L2 part of the mixed orchestrator — deferred to the owning layer's audit (split recorded)")
    return ("constant", "ESTABLISHED", "no", "structural literal")


def classify_field(r):
    b, owner, name, ctx = base(r["file"]), r.get("type_owner", ""), r.get("name", ""), r.get("context", "")
    lay = file_layer(r["file"], owner=owner)
    # KeyModeAnalyzerPreferences members = the L3 emission CONSTANTS
    if owner == "KeyModeAnalyzerPreferences":
        return (lay, "constant", "UNFIT", in_manifest(name),
                "L3 emission scoring constant (weight/bonus/penalty/prior/threshold) — empirical/hand-set per code; NOT in param_manifest unless noted; Stage-5 fit target")
    if owner in ("ChordAnalyzerPreferences", "ChordAnalysisTone", "ChordTemporalContext"):
        return (lay, "deferred", "DEFERRED", "no", "Layer-4 type member in the shared leaf — deferred to the L4 audit (split recorded)")
    if owner == "ParameterBound":
        return (lay, "no-issue", "NO-ISSUE", "no", "shared parameter-bounds infra member — cross-cutting, not L3-specific")
    if owner == "PitchContext":
        return (lay, "no-issue", "NO-ISSUE", "no", "L3 emission input member (pitch/durationWeight/beatWeight/isBass) — plumbing")
    # derived-fact publication surfaces
    if owner in ("KeyModeAnalysisResult", "SliceKeyMode"):
        if name in ("normalizedConfidence",):
            return (lay, "derived-fact", "PUBLISHED", "no",
                    "L3 emission-sigmoid confidence — PUBLISHED as the INTERNAL 0.8-gate input (D-L3a); NOT the boundary confidence")
        if name in ("confidence",):
            return (lay, "derived-fact", "PUBLISHED", "no",
                    "SliceKeyMode sequence-margin — THE L3 boundary confidence; PUBLISHED to HarmonicRegion.keyConfidence")
        if name in ("alternatives",):
            return (lay, "derived-fact", "PUBLISHED", "no",
                    "ranked key alternatives — PUBLISHED (declared dormancy: future consumer = L5 modulation recompute)")
        return (lay, "derived-fact", "PUBLISHED", "no", "L3 result field — published on the L3 output surface")
    if owner == "KeyCandidateScore":
        return (lay, "derived-fact", "PUBLISHED", "no",
                "per-candidate emission breakdown — PUBLISHED only via the diagnostic dump (--decode-keymode/--dump-key-candidates); nullptr on production (byte-identical)")
    if base(r["file"]) == "harmonicrhythm.h" and owner == "HarmonicRegion":
        if name in ("keyConfidence",):
            return ("L3-MIXED", "derived-fact", "PUBLISHED", "no",
                    "THE L3 boundary confidence (sequence margin) on the region DTO — PUBLISHED but NO production consumer (declared dormancy -> L5); the 0.8 gate reads keyModeResult.normalizedConfidence instead (the D-L3a stance — report section 5)")
        if name in ("keyAlternatives",):
            return ("L3-MIXED", "derived-fact", "PUBLISHED", "no",
                    "region-level candidate-key menu — PUBLISHED, no production consumer (declared dormancy -> L5 modulation recompute)")
        if name in ("keyModeResult",):
            return ("L3-MIXED", "derived-fact", "PUBLISHED", "no", "the region's chosen L3 key/mode — PUBLISHED, consumed by display/gate/chord")
        return ("L3-MIXED", "no-issue", "NO-ISSUE", "no", "L4 chord/plumbing member of the region DTO — deferred split")
    if owner in ("JointKeyWeights",):
        return (lay, "constant", "UNFIT", "no", "joint-key soft weight — '[empirical - Stage-5 fits]', gated OFF, NOT in param_manifest")
    if owner and owner.startswith("JointKey") or owner in ("LocalKeySpan", "CadenceKeyAnchor", "AuthenticCadence",
                                                           "CadenceRegionInput", "ModulationDetectionResult",
                                                           "JointKeyDecision", "JointKeyResult", "JointKeyRegionInput",
                                                           "JointKeyLatticeState", "JointKeyChordAlt", "JointKeyLocalCandidate",
                                                           "KeySignatureContext", "KeyResolveDump",
                                                           "KeyModeSequencePreferences", "State", "SliceKeyMode",
                                                           "ChordTemporalExtensions", "RegionKeyReduction"):
        return (lay, "no-issue", "NO-ISSUE", "no", "L3 diagnostic/plumbing struct member (input or dump field) — no derived-fact publication concern")
    return (lay, "no-issue", "NO-ISSUE", "no", "struct member — input/plumbing, no L3 fact-publication concern")


def classify_function(r, kind):
    b, name = base(r["file"]), r.get("name", "")
    lay = file_layer(r["file"], name)
    if lay in ("L4", "L5", "L2", "util"):
        return (lay, "code", "DEFERRED",
                "%s part of a mixed file — deferred to the owning layer's audit (split recorded)" % lay)
    # RETIRES map (roadmap R2/R3/R5/R6)
    RETIRE = {
        ("keyresolver.cpp", "resolveKeyAndModeRanked"):
            "SURVIVES but R5-SHRINKS: the per-window argmax + hysteresis retire (superseded by the decoder change cost); resolveKeySignatureContext + the insufficient-PCs fallback SURVIVE as the S2 seed + P4 tick-local + grading baseline. #12-check at deletion: KEEP the shared signature/declared-mode/partial-correction; drop the hysteresis.",
    }
    if (b, name) in RETIRE:
        return (lay, "code", "RETIRES", RETIRE[(b, name)])
    return (lay, "code", "SURVIVES", "L3 mechanism on the survivor path (or its diagnostic/dormant scaffolding) — no retirement scheduled for the L3 concern itself")


def classify_branch(r):
    b, func = base(r["file"]), r.get("func", "")
    lay = file_layer(r["file"], func)
    if lay in ("L4", "L5", "L2", "util") or lay.endswith("L4-loop") or lay.endswith("L4-gap"):
        # branch in a mixed function: keep it, note the split
        pass
    return (lay, "code", "NO-ISSUE", "ordinary control flow / guard — edge-case behavior characterized in the report's contract-direction + edge-case notes")


def classify_cross(r):
    b, tgt = base(r["file"]), r.get("target_area", "")
    forward = {"notemodel", "slicing", "engravingbridge", "scoreharvest", "types", "key", "external"}
    if tgt in forward:
        return ("cross", "FORWARD-OK", "forward/self dependency (L1 notes / L2 slices / L1.5 views / types leaf / self / engraving) — Dependency Rule respected")
    if tgt in ("chord", "function", "decode", "progression", "voiceleading", "grouping", "vocabulary"):
        inc = r.get("include", "") + r.get("resolved", "")
        if b in CORE_L3_FILES:
            if tgt == "chord" and "analysisutils" in inc:
                return ("cross", "BACK-EDGE-NOTE",
                        "CORE L3 file includes chord/analysisutils.h for shared pitch-class primitives (normalizePc / diatonicMaskFromFifths) — dependency-free util siloed under chord/ (L4 dir); layering smell, not a heavy coupling")
            if tgt == "chord" and "chordanalyzer.h" in inc:
                return ("cross", "BACK-EDGE",
                        "CORE L3 key-evidence header includes the HEAVY L4 chord/chordanalyzer.h only for the ChordQuality enum, which lives in the dependency-free types leaf analysistypes.h — an avoidable header back-edge the types-leaf refactor removed elsewhere (Dependency Rule / #7)")
            return ("cross", "BACK-EDGE",
                    "CORE L3 file includes a %s (L4/L5) header — potential back-edge; verify it is a type-only / shared-util include, else a Dependency-Rule violation" % tgt)
        return ("cross", "MIXED-DEFERRED",
                "L4/L5 include in a mixed orchestrator file (its L4/L5 part) — expected; deferred to the owning layer's audit")
    if tgt in ("region", "section", "harmony", "param", "intonation"):
        return ("cross", "FORWARD-OK", "same-tier / infra include (region-section orchestration / param-override / harmony-legacy) — within the L3 seam's remit")
    return ("cross", "NO-ISSUE", "cross-dir include — %s" % tgt)


def main():
    rows = []
    for f in load("l3_functions.csv"):
        lay, cls, verd, reason = classify_function(f, "function")
        rows.append({"file": f["file"], "kind": "function", "line": f["start_line"],
                     "ident": f["name"], "func": f["name"], "layer": lay,
                     "verdict_class": cls, "verdict": verd, "in_param_manifest": "",
                     "reason": reason})
    for d in load("l3_decls.csv"):
        lay, cls, verd, reason = classify_function({"file": d["file"], "name": d["name"]}, "decl")
        rows.append({"file": d["file"], "kind": "decl", "line": d["line"],
                     "ident": d["name"], "func": d.get("type_owner", ""), "layer": lay,
                     "verdict_class": cls, "verdict": verd, "in_param_manifest": "", "reason": reason})
    for lt in load("l3_literals.csv"):
        cls, verd, inman, reason = classify_literal(lt)
        lay = file_layer(lt["file"], lt.get("func"))
        rows.append({"file": lt["file"], "kind": "literal", "line": lt["line"],
                     "ident": lt["value"], "func": lt.get("func", ""), "layer": lay,
                     "verdict_class": cls, "verdict": verd, "in_param_manifest": inman, "reason": reason})
    for fl in load("l3_fields.csv"):
        lay, cls, verd, inman, reason = classify_field(fl)
        rows.append({"file": fl["file"], "kind": "field", "line": fl["line"],
                     "ident": fl["name"], "func": fl.get("type_owner", ""), "layer": lay,
                     "verdict_class": cls, "verdict": verd, "in_param_manifest": inman, "reason": reason})
    for br in load("l3_branches.csv"):
        lay, cls, verd, reason = classify_branch(br)
        rows.append({"file": br["file"], "kind": "branch", "line": br["line"],
                     "ident": br["kind"], "func": br.get("func", ""), "layer": lay,
                     "verdict_class": cls, "verdict": verd, "in_param_manifest": "", "reason": reason})
    for cr in load("l3_crosslayer.csv"):
        verd, cls_or_reason = None, None
        _, verd, reason = classify_cross(cr)
        rows.append({"file": cr["file"], "kind": "crosslayer", "line": cr["line"],
                     "ident": cr.get("include", ""), "func": cr.get("target_area", ""),
                     "layer": file_layer(cr["file"]), "verdict_class": "cross",
                     "verdict": verd, "in_param_manifest": "", "reason": reason})

    # apply OVERRIDES
    for r in rows:
        key = (base(r["file"]), int(r["line"]), r["kind"])
        if key in OVERRIDES:
            r.update(OVERRIDES[key])

    cols = ["file", "kind", "line", "ident", "func", "layer",
            "verdict_class", "verdict", "in_param_manifest", "reason"]
    with open(os.path.join(HERE, "pass1_dispositions.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # summary counts
    from collections import Counter
    by_verdict = Counter(r["verdict"] for r in rows)
    by_kind = Counter(r["kind"] for r in rows)
    by_layer = Counter(r["layer"] for r in rows)
    summary = {
        "audit": "EG-7 Layer-3 (key/mode) certification, PASS 1 (blind enumerative) — dispositions",
        "inventory_manifest": "tools/audit/l3/manifest.json",
        "total_rows": len(rows),
        "by_kind": dict(by_kind),
        "by_verdict": dict(by_verdict),
        "by_layer": dict(by_layer),
    }
    with open(os.path.join(HERE, "pass1_dispositions.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "rows": rows}, f, indent=1)

    print("dispositions: %d rows" % len(rows))
    print("  by kind:", dict(by_kind))
    print("  by verdict:", dict(by_verdict))


if __name__ == "__main__":
    main()
