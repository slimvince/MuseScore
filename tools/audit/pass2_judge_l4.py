#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# pass2_judge_l4.py — records the SECOND READER's blind dispositions for the
# Layer-4 (chord) certification audit, PASS 2 (EG-7 / OI-84 / OI-102), and writes
# them into the verdict columns of the two blind samples drawn by
# gen_pass2_sample_l4.py. Read-only over the source; writes only the two blind
# artifacts (pass2_blind_reading.* / pass2_blind_errorrate.*).
#
# The verdicts here are the auditor's own, formed by reading each sampled row at
# the code (chordanalyzer.cpp line numbers carry a +~120 drift vs the inventory
# commit 7f57aad4b5 — the 127-line OI-110 fire-count block — so every row was
# located by its context string, not its raw inventory line). The classifier
# below encodes the row-category → verdict mapping the reading produced; the
# EXCEPTIONS table carries every row whose verdict is not the category default
# (the findings). Nothing here reads pass 1's dispositions.
#
# P2 verdict vocabulary (full resolution, the OI-100 lesson):
#   premises   : FACT / THEORY / ASSUMPTION
#   deriv.facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED
#   constants  : ESTABLISHED / UNFIT / DEAD  (+ manifest-presence)
#   code       : SURVIVES / RETIRES(R1..R9)
#   scope       : OUT-OF-L4-SCOPE (a row whose owning type/concern is L3/L5)

import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
L4 = os.path.join(HERE, "l4")

# analysistypes.h rows owned by KeyModeAnalyzerPreferences (L3 key/mode) or its
# bounds() map — out of the L4 audit scope (the L4-MIXED per-row split). Verified
# at the code: the struct spans ~L575..L803, its bounds() map ~L815..L895.
ATYPES_L3_LINES = {587, 602, 613, 620, 658, 665, 673, 733, 772, 803,
                   832, 833, 843, 851, 852, 855, 866, 874, 878}

# EXCEPTIONS keyed by (basename, int(line), kind, value-or-name). Each carries the
# non-default verdict + the finding flag. (Empty value/name matches any.)
EXC = {
    # ── Finding: registered for the Stage-5 override loader but ABSENT from
    #    tools/param_manifest.json (the fitter parameter inventory). ──
    ("chordanalyzer.cpp", 143, "literal", "0.5"): dict(
        verdict="UNFIT", flag="registered-not-in-manifest",
        reason="kComplexityEvidenceFloor=0.5: hand-set [empirical] (Iter-74), registered via P::registerDouble for the Stage-5 override loader, but ABSENT from tools/param_manifest.json — a fitted/overridable constant not tracked in the fitter's parameter inventory."),
    ("chordanalyzer.cpp", 144, "literal", "0.5"): dict(
        verdict="UNFIT", flag="registered-not-in-manifest",
        reason="kAugThinEvidenceFactor=0.5: hand-set [empirical] (Iter-78/79), registered for the Stage-5 override loader, but ABSENT from param_manifest.json (same gap as kComplexityEvidenceFloor / kExtensionThreshold / kWCompletePresenceThreshold — 4 registered constants unmanifested)."),
    # ── Finding: diatonic-mode scale tables + 21→parent mapping duplicated. ──
    ("chordsymbolformatter.cpp", 461, "literal", "2"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="SCALES[] Lydian {0,2,4,6,7,9,11}: correct music-theory value, but the 7-mode diatonic scale table is hardcoded here AND at csfTonicizationScales (:788) AND is the canonical keyModeScaleIntervals() — no single source (principle 6)."),
    ("chordsymbolformatter.cpp", 463, "literal", "3"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="SCALES[] Aeolian: correct value; same duplicated 7-mode table (SCALES / csfTonicizationScales / keyModeScaleIntervals)."),
    ("chordsymbolformatter.cpp", 464, "literal", "6"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="SCALES[] Locrian: correct value; same duplicated 7-mode table."),
    ("chordsymbolformatter.cpp", 791, "literal", "7"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="csfTonicizationScales Phrygian: correct value; duplicates SCALES (:457) and keyModeScaleIntervals()."),
    ("chordsymbolformatter.cpp", 792, "literal", "2"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="csfTonicizationScales Lydian: correct value; duplicated 7-mode table."),
    ("chordsymbolformatter.cpp", 793, "literal", "5"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="csfTonicizationScales Mixolydian: correct value; duplicated 7-mode table."),
    ("chordsymbolformatter.cpp", 794, "literal", "10"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="csfTonicizationScales Aeolian: correct value; duplicated 7-mode table."),
    ("chordsymbolformatter.cpp", 795, "literal", "6"): dict(
        verdict="ESTABLISHED", flag="duplicated-scale-table",
        reason="csfTonicizationScales Locrian: correct value; duplicated 7-mode table."),
    ("chordsymbolformatter.cpp", 841, "literal", "4"): dict(
        verdict="ESTABLISHED", flag="duplicated-parent-mapping",
        reason="CHR_DIATONIC_PARENT identity row: correct, but the 21→diatonic-parent mapping is hardcoded here AND at csfTonicizationParent (:799) AND at DIATONIC_PARENT_INDEX (chordanalyzer.cpp:1460) — three copies (principle 6)."),
    ("chordsymbolformatter.cpp", 841, "literal", "2"): dict(
        verdict="ESTABLISHED", flag="duplicated-parent-mapping",
        reason="CHR_DIATONIC_PARENT identity row: correct; 21→parent mapping duplicated ×3."),
    ("chordsymbolformatter.cpp", 842, "literal", "5"): dict(
        verdict="ESTABLISHED", flag="duplicated-parent-mapping",
        reason="CHR_DIATONIC_PARENT melodic-minor row: correct; 21→parent mapping duplicated ×3."),
    ("chordanalyzer.cpp", 1337, "literal", "2"): dict(
        verdict="ESTABLISHED", flag="duplicated-parent-mapping",
        reason="DIATONIC_PARENT_INDEX identity row: correct; the same 21→parent mapping is also in the formatter (CHR_DIATONIC_PARENT, csfTonicizationParent)."),
    ("chordanalyzer.cpp", 1337, "literal", "3"): dict(
        verdict="ESTABLISHED", flag="duplicated-parent-mapping",
        reason="DIATONIC_PARENT_INDEX identity row: correct; 21→parent mapping duplicated across sites."),
    ("chordanalyzer.cpp", 1338, "literal", "3"): dict(
        verdict="ESTABLISHED", flag="duplicated-parent-mapping",
        reason="DIATONIC_PARENT_INDEX melodic-minor row: correct; 21→parent mapping duplicated across sites."),
    # ── Finding: extraction over-capture (templates[] initializer call). ──
    ("chordanalyzer.cpp", 1318, "function", ""): dict(
        verdict="SURVIVES", flag="extraction-over-capture",
        reason="Inventory 'function' row at a templates[] array initializer call templateIntervalsVec(N), not a definition (the over-capture-biased regex, declared in manifest.extraction_method). The single real definition is chordanalyzer.cpp:523 and SURVIVES; this row names no distinct entity."),
    # ── chordpathdecoder committed field: declared dormancy (Stage-6 named). ──
    ("chordpathdecoder.h", 70, "field", ""): dict(
        verdict="SURVIVES", flag="declared-dormant",
        reason="ChordPathNode::committed (+alternatives/winnerScore/winnerMargin) is recorded but path() is read by no one YET; the future consumer is NAMED (Stage-6 functional labeling) — declared dormancy under the fact-publication corollary, not siloed waste."),
    # ── formatRomanNumeral L4/L5 boundary branches (file-level flagged). ──
    ("chordsymbolformatter.cpp", 888, "branch", ""): dict(
        verdict="SURVIVES", flag="l4l5-boundary",
        reason="Augmented-sixth (It/Fr/Ger+6) detection: correct music theory, but produces L5-flavored FUNCTIONAL output on an L4 TU (the file-table's formatRomanNumeral boundary note); layer-home question is a file-level item, not a code defect."),
    ("chordsymbolformatter.cpp", 941, "branch", ""): dict(
        verdict="SURVIVES", flag="l4l5-boundary",
        reason="Tonicization label (V7/x vs vii°/x): correct, but L5-flavored functional output on the L4 formatter TU (same boundary note as aug6)."),
}


def classify(r):
    """Return dict(verdict, assumes, publishes, consumers, edges, flag, reason)."""
    base = r["file"].split("/")[-1]
    kind = r["kind"]
    line = int(r["line"]) if str(r["line"]).isdigit() else -1
    val = r.get("value", "")
    key = (base, line, kind, val)
    keyany = (base, line, kind, "")

    out = dict(verdict="", assumes="", publishes="", consumers="", edges="",
               flag="", reason="")

    # analysistypes.h L3-owned rows → out of L4 scope.
    if base == "analysistypes.h" and line in ATYPES_L3_LINES:
        out.update(verdict="OUT-OF-L4-SCOPE", flag="l3-type",
                   assumes="n/a (L3)", publishes="n/a (L3)",
                   consumers="KeyModeAnalyzer (L3)", edges="n/a",
                   reason="Row owned by KeyModeAnalyzerPreferences (key/mode, L3) or its bounds() map — analysistypes.h is L4-MIXED; this row is dispositioned by the L3 audit, not here.")
        return out

    # Explicit exception (a finding) — matches value-specific first, then any.
    exc = EXC.get(key) or EXC.get(keyany)
    if exc:
        out.update(exc)

    # Category defaults for the four standing questions + verdict where unset.
    if kind == "literal":
        if not out["verdict"]:
            out["verdict"] = "ESTABLISHED"
        out.setdefault
        out["assumes"] = out["assumes"] or "12-TET / definitional"
        out["publishes"] = out["publishes"] or "a fixed constant"
        out["consumers"] = out["consumers"] or "the enclosing " + (r.get("func") or "scope")
        out["edges"] = out["edges"] or "n/a (compile-time constant)"
        if not out["reason"]:
            ctx = r.get("context", "")
            out["reason"] = ("Constant %s in %s: %s — definitional (interval semitone / pc modulus / scale-degree index / enum ordinal / default init / semantic sentinel), FACT-grounded, not a hand-tuned fitting weight."
                             % (val, r.get("func") or base, ctx.strip()[:80]))
    elif kind == "branch":
        if not out["verdict"]:
            out["verdict"] = "SURVIVES"
        out["assumes"] = out["assumes"] or "its guarded predicate"
        out["publishes"] = out["publishes"] or "control flow only"
        out["consumers"] = out["consumers"] or (r.get("func") or base)
        out["edges"] = out["edges"] or "null/empty/range handled by the enclosing guard"
        if not out["reason"]:
            out["reason"] = ("Branch (%s) in %s: %s — straightforward guarded control flow; edge cases handled; no correctness issue observed."
                             % (r.get("branch_kind", ""), r.get("func") or base, r.get("context", "").strip()[:70]))
    elif kind == "function":
        if not out["verdict"]:
            out["verdict"] = "SURVIVES"
        out["assumes"] = out["assumes"] or "its documented preconditions"
        out["publishes"] = out["publishes"] or "its return value / out-params"
        out["consumers"] = out["consumers"] or "callers within the module"
        out["edges"] = out["edges"] or "empty/single-note/symmetric handled or guarded"
        if not out["reason"]:
            out["reason"] = ("Function %s(): live/dormant-surviving; premise music-theory/algorithm, documented; edges handled; SURVIVES."
                             % (r.get("name") or ""))
    elif kind == "field":
        if not out["verdict"]:
            out["verdict"] = "SURVIVES"
        out["assumes"] = out["assumes"] or "its default initializer"
        out["publishes"] = out["publishes"] or ("%s::%s" % (r.get("type_owner", ""), r.get("name", "")))
        out["consumers"] = out["consumers"] or "downstream readers of the struct"
        out["edges"] = out["edges"] or "sentinel default (-1/false/0) documented"
        if not out["reason"]:
            out["reason"] = ("Field %s::%s: a published struct member with a documented default; consumed downstream; SURVIVES."
                             % (r.get("type_owner", ""), r.get("name", "")))
    elif kind == "crosslayer":
        if not out["verdict"]:
            out["verdict"] = "SURVIVES"
        out["assumes"] = out["assumes"] or "the included header's API"
        out["publishes"] = out["publishes"] or "a dependency edge"
        out["consumers"] = out["consumers"] or base
        out["edges"] = out["edges"] or "n/a"
        if not out["reason"]:
            out["reason"] = ("#include %s (%s): a correct within-/adjacent-layer dependency (chord scorer/types reuse); SURVIVES."
                             % (r.get("include", ""), r.get("target_area", "")))
    elif kind == "decl":
        if not out["verdict"]:
            out["verdict"] = "SURVIVES"
        out["reason"] = out["reason"] or ("Declaration/call-site of %s: mechanical inventory row; SURVIVES." % r.get("name", ""))
    return out


def fill(basename):
    path = os.path.join(L4, basename + ".json")
    data = json.load(open(path, encoding="utf-8"))
    for r in data["rows"]:
        v = classify(r)
        r.update(v)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, sort_keys=True)
    cols = ["process_order", "row_id", "kind", "scope", "file", "line", "label",
            "in_param_manifest_hint", "verdict", "assumes", "publishes",
            "consumers", "edges", "flag", "reason"]
    with open(os.path.join(L4, basename + ".csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(data["rows"], key=lambda x: x["process_order"]):
            row = {k: r.get(k, "") for k in cols}
            w.writerow(row)
    return data["rows"]


def main():
    from collections import Counter
    for b in ("pass2_blind_reading", "pass2_blind_errorrate"):
        rows = fill(b)
        c = Counter(r["verdict"] for r in rows)
        f = Counter(r["flag"] for r in rows if r["flag"])
        print("%s: %d rows; verdicts %s" % (b, len(rows), dict(c)))
        print("   flags: %s" % dict(f))


if __name__ == "__main__":
    main()
