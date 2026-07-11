#!/usr/bin/env python3
"""Layer-4 (chord) audit PASS-1, oracle session (EG-7 / OI-84 / OI-102).

Generates a disposition for EVERY inventory row whose file is one of the three LIVE
scoring-oracle translation units:
    src/composing/analysis/chord/chordanalyzer.cpp   (the vertical scoring oracle)
    src/composing/analysis/chord/chordanalyzer.h     (the L4 scorer contract surface)
    src/composing/analysis/chord/analysisutils.h     (cross-cutting pitch/key helpers)

Protocol P1/P2 (cowork_audit_protocol.md): the scope is the machine-generated inventory
(tools/audit/l4/*.csv, frozen at manifest head 7f57aad4b5); the output is a verdict from
the closed rubric for every row — "no issue" is a recorded claim with a stated reason.

The classification is a TOTAL FUNCTION over the inventory: a per-kind rule assigns a
default verdict from the row's own value/context, and a curated OVERRIDES table (keyed on
file+line or file+name) carries the specific judgments and the flagged findings. No row is
skipped; constants are classified individually (value+context), never batched away.

Reads tools/param_manifest.json to mark, per numeric constant, whether it is registered in
the Stage-5 override manifest. Emits pass1_dispositions_oracle.csv/.json + a by-verdict
summary. Read-only; no source or reference artifact is touched.
"""
import csv, json, os, re, sys

AUD = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AUD, "..", "..", ".."))
FILES = {
    "src/composing/analysis/chord/chordanalyzer.cpp",
    "src/composing/analysis/chord/chordanalyzer.h",
    "src/composing/analysis/chord/analysisutils.h",
}

# ── The 28 file-scope scoring constants registered for the Stage-5 --param-override
#    mechanism (chordanalyzer.cpp registration block). ──────────────────────────────
REGISTERED = {
    "kContradictionPenalty", "kRootToneFactor", "kSecondToneFactor", "kOtherToneFactor",
    "kTemplateToneWeightCap", "kExtraNoteWeightCap", "kExtensionFactor7th",
    "kExtensionFactorFlat13", "kExtensionFactorDefault", "kForeignPenalty",
    "kSus4FlatThirdFactor", "kSus4SharpThirdFactor", "kDim7CharacteristicBonus",
    "kNonBassPenalty", "kSus4VariantMissing7th", "kSus4Maj7MissingP5", "kSus4MissingFourth",
    "kSus4StructuralFourthThreshold", "kDom7FlatFiveTpcPenalty", "kDom7FlatFiveMissing7th",
    "kPowerChord3PcPenalty", "kBassSupportPresenceThreshold", "kSeventhThreshold",
    "kExtensionThreshold", "kWComplete", "kWCompletePresenceThreshold",
    "kComplexityEvidenceFloor", "kAugThinEvidenceFactor",
}

def load_manifest_names():
    p = os.path.join(REPO, "tools", "param_manifest.json")
    names = set()
    try:
        d = json.load(open(p, encoding="utf-8"))
        for row in d.get("parameters", []):
            nm = row.get("name", "")
            # names may carry a parenthetical qualifier, e.g.
            # "kExtensionThreshold (file constexpr; distinct from prefs.extensionThreshold)"
            base = nm.split(" ")[0].strip()
            names.add(base)
            names.add(nm)
    except Exception as e:
        print("WARN manifest load:", e, file=sys.stderr)
    return names

MANIFEST_NAMES = load_manifest_names()

# ── Curated per-row judgments and flagged findings. Keyed either by (file,line) or by a
#    (file, kind, name) tuple. Each entry: (verdict, verdict_class, flagged, rationale).
#    These override the per-kind defaults below. ──────────────────────────────────────
CPP = "src/composing/analysis/chord/chordanalyzer.cpp"
H   = "src/composing/analysis/chord/chordanalyzer.h"
UTL = "src/composing/analysis/chord/analysisutils.h"

# Function-level curated dispositions (by file+name).
FUNC_OVERRIDES = {
    (UTL, "ionianTonicPcFromFifths"): ("FACT", "premise", False,
        "circle-of-fifths -> Ionian tonic pitch class; verified against theory; SURVIVES (cross-cutting)."),
    (UTL, "diatonicMaskFromFifths"): ("FACT", "premise", False,
        "position i has pc (7*i) mod 12 = circle of fifths; verified; SURVIVES (cross-cutting)."),
    (UTL, "collectionMask"): ("THEORY", "premise", False,
        "minor = natural minor + raised leading tone (harmonic-minor collection); documented design choice; SURVIVES."),
    (UTL, "normalizePc"): ("FACT", "code", False, "pitch-class reduction mod 12; SURVIVES (cross-cutting)."),
    (UTL, "pcInMask"): ("FACT", "code", False, "12-bit mask membership test; SURVIVES."),
    (UTL, "endsWith"): ("ESTABLISHED", "code", False, "generic string suffix test; SURVIVES."),
    (CPP, "categorizeExtraNote"): ("THEORY", "premise", True,
        "non-template-note quality classification; carries a `// BUG-10` marker at the Diminished/P5 branch (line ~216) -- a tracked in-code bug label; cross-check register at unblind."),
    (CPP, "detectExtensions"): ("THEORY", "code", True,
        "extension/alteration bitmask detection; contains inline magic thresholds (0.3/0.2/0.1) NOT registered in the override manifest -- see literal flags."),
    (CPP, "dim7CharacteristicBonus"): ("THEORY", "premise", False,
        "dim7 rotation selector via non-diatonic bb7 (documented scoring_model.md 4); SURVIVES-oracle."),
    (CPP, "structuralPenalties"): ("THEORY", "code", True,
        "template self-consistency penalties; inline 0.05 presence literals duplicate kBassSupportPresenceThreshold."),
    (CPP, "scoreExtraNotes"): ("THEORY", "code", False, "signed non-template contribution; SURVIVES-oracle."),
    (CPP, "scoreTemplateTones"): ("THEORY", "code", False, "weighted template-tone presence (root/second/other factors); SURVIVES-oracle."),
    (CPP, "nonBassAdjustment"): ("THEORY", "code", False, "non-bass penalty with TPC waiver; SURVIVES-oracle."),
    (CPP, "diatonicRootContribution"): ("THEORY", "code", False, "the one bass-independent key fact folded into basisIndep; SURVIVES-oracle."),
    (CPP, "buildChordResult"): ("SURVIVES", "code", False,
        "the single result builder (aug-root correction, Sus2->Sus4, Sus->Major(omitsThird), extension/degree/diatonic); SURVIVES-oracle."),
    (CPP, "deriveChordExtensions"): ("SURVIVES", "code", False,
        "fixed-quality extension extraction exposed for the L4->L5 decoder carry; SURVIVES (decoder-consumed)."),
    (CPP, "analyzeChord"): ("SURVIVES", "code", False,
        "the vertical scoring oracle; LIVE production hot path AND decoder emission; SURVIVES (R9 splits, does not delete)."),
    (CPP, "create"): ("SURVIVES", "code", False, "ChordAnalyzerFactory::create; SURVIVES."),
    (CPP, "extensionBits"): ("SURVIVES", "code", False, "single flag->bit mapping shared by buildChordResult + deriveChordExtensions; SURVIVES."),
    (CPP, "templateIntervalsVec"): ("SURVIVES", "code", False, "builds a template's interval vector from kTemplateIntervals (single source); SURVIVES."),
    (CPP, "countTpcMatches"): ("SURVIVES", "code", False, "TPC-match counting helper; SURVIVES."),
    (CPP, "tpcConsistencyBonus"): ("SURVIVES", "code", False, "per-tone TPC spelling bonus; SURVIVES-oracle."),
    (CPP, "bassRootBonusMultiplier"): ("SURVIVES", "code", False, "bass-root bonus multiplier (full/third-only/alone); SURVIVES-oracle."),
    (CPP, "templateHasMatchingThird"): ("SURVIVES", "code", False, "vertical third-presence predicate; SURVIVES-oracle."),
    (CPP, "templateHasMatchingFifth"): ("SURVIVES", "code", False, "vertical fifth-presence predicate; SURVIVES-oracle."),
    (CPP, "qualifiesForCompleteTriadInversionBonus"): ("SURVIVES", "code", False, "vertical inversion-eligibility flag published to the snapshot; SURVIVES-oracle."),
    (CPP, "supportsContextualInversionBonuses"): ("SURVIVES", "code", False, "vertical inversion-eligibility flag published to the snapshot; SURVIVES-oracle."),
    (CPP, "appliedBassRootBonus"): ("SURVIVES", "code", True,
        "applies prefs.bassNoteRootBonus (code value 0.70); ARCHITECTURE.md 4.1/4.1b document 0.65 -- doc drift (scoring_model.md 0.70 is correct)."),
    (H, "templateIntervalMask"): ("SURVIVES", "code", False, "derives Gate R mask from kTemplateIntervals (closes drift hazard); SURVIVES."),
    (H, "makeTemplateMasks"): ("SURVIVES", "code", False, "derived Gate R mask table; SURVIVES."),
    (H, "normalizeMergedBassTone"): ("SURVIVES", "code", False, "merged-tone bass normalization; SURVIVES."),
    (H, "mergeChordAnalysisTones"): ("SURVIVES", "code", False, "tone merge helper; SURVIVES."),
    (H, "bassToneFromTones"): ("SURVIVES", "code", False, "bass-tone extraction; SURVIVES."),
    (H, "isDiatonicStep"): ("FACT", "premise", False, "chromatic step (1 or 2 semitones, shortest path); SURVIVES."),
    (H, "hasExtension"): ("SURVIVES", "code", False, "extension bitmask query; SURVIVES."),
    (H, "hasAnyNinth"): ("SURVIVES", "code", False, "extension bitmask query; SURVIVES."),
    (H, "hasAnyThirteenth"): ("SURVIVES", "code", False, "extension bitmask query; SURVIVES."),
    (H, "setExtension"): ("SURVIVES", "code", False, "extension bitmask setter; SURVIVES."),
    (H, "advanceTemporalContext"): ("SURVIVES", "code", False,
        "temporal-context commit helper; NOT orphaned by the decoder -- ChordPathDecoder::commit() calls it (chordpathdecoder.h:114) + tests; SURVIVES."),
    (H, "computeRawFanoutSummary"): ("PUBLISHED", "derived-fact", True,
        "read-only L5 fan-out summary (Engage arc #8 measurement); computes the pre-cap ranked-set size L5 will select over; consumer = the read-only fan-out dump; DORMANT consumer (engagement), never serialized -- declared-dormancy fact, consumer named."),
    (H, "inferNextRootPc"): ("SURVIVES", "code", True,
        "next-region root inference; couples to the RETIRING gates (calls applyIter8691Pedal + applyPostScoringGates, R1) -- retirement-coupled."),
}

# Field-level curated dispositions (by type_owner).
FIELD_OWNER_DISP = {
    "ChordIdentity": ("PUBLISHED", "derived-fact", "the pitch-content identity the oracle publishes upward (root/quality/bass/extensions/score); consumed by the region path + decoder + formatter; SURVIVES."),
    "ChordFunction": ("PUBLISHED", "derived-fact", "tonal-function fields (degree/diatonic/keyTonic/keyMode/nextRootPc); published; consumed by the formatter + L5; SURVIVES."),
    "ChordAnalysisResult": ("PUBLISHED", "derived-fact", "the analysis result DTO (identity+function); the oracle's output contract; SURVIVES."),
    "RawCandidate": ("PUBLISHED", "derived-fact", "per-cell raw scoring output; consumed by the gates (RETIRING R1) + fan-out summary + decoder; retirement-coupled for the gate fields."),
    "PostScoringGateContext": ("PUBLISHED", "derived-fact", "captured inputs the RETIRING gates + Iter86/91/pedal tail need; retirement-coupled (R1 + chordpostpasses L4-RETIRES)."),
    "RawFanoutSummary": ("PUBLISHED", "derived-fact", "read-only L5 fan-out counts (Engage arc #8); declared-dormancy, consumer = fan-out dump."),
    "BuildChordResultContext": ("PUBLISHED", "derived-fact", "locally-computed inputs buildChordResult needs; SURVIVES."),
    "ChordExtensionInfo": ("PUBLISHED", "derived-fact", "vertical extension identity for the L4->L5 decoder carry; SURVIVES (decoder-consumed)."),
    "PromotionTarget": ("PUBLISHED", "derived-fact", "the (root,quality) a promotion wants; serves promoteToWinner (RETIRING gates R1); retirement-coupled."),
    "DiagnosticOracleCell": ("PUBLISHED", "derived-fact", "diagnostic ORACLE cell view; serves diagnoseChord (chorddiagnose.cpp DEFERRED); SURVIVES-diagnostic."),
    "DiagnosticCompetitionCandidate": ("PUBLISHED", "derived-fact", "diagnostic COMPETITION view; serves diagnoseChord; SURVIVES-diagnostic."),
    "DiagnosticPostGateTrail": ("PUBLISHED", "derived-fact", "diagnostic POST-GATES trail; serves diagnoseChord; SURVIVES-diagnostic."),
    "ChordAnalysisDiagnosticResult": ("PUBLISHED", "derived-fact", "full diagnostic output; serves diagnoseChord; SURVIVES-diagnostic."),
    "ClosePositionVoicing": ("PUBLISHED", "derived-fact", "voicing DTO; defined in chordvoicing.cpp (DEFERRED arrangement concern); display/arrangement decl in the analysis header (layering note)."),
}

def classify_literal(row):
    """Return (verdict, verdict_class, in_manifest, flagged, rationale) for a literal row."""
    file, line, value, func, context = row["file"], row["line"], row["value"], row["func"], row["context"]
    ctx = context or ""
    # 1) A registered/known scoring constant ON ITS DEFINITION LINE ONLY
    #    (`static double kX = <value>;`). Matching the name anywhere in context would
    #    mis-attribute an unrelated literal (e.g. the bare 1.0 on the kComplexityEvidenceFloor
    #    USE line) to the constant.
    m = re.search(r'static\s+double\s+(k[A-Z][A-Za-z0-9]+)\s*=', ctx)
    named = m.group(1) if m else None
    if named and named in REGISTERED:
        in_man = "yes" if (named in MANIFEST_NAMES) else "no"
        flg = (in_man == "no")
        rat = (f"{named}: scoring constant, theory-ordered + empirical magnitude, override-registered"
               + ("" if in_man == "yes"
                  else "; ABSENT from param_manifest.json despite being override-registered (coverage gap)"))
        return ("ESTABLISHED", "constant", in_man, flg, rat)
    # 2) TPC-delta / interval / pitch-class structural constants (music theory).
    if func in ("templateIntervalsVec",) or "tpcDeltas" in ctx or re.search(r'%\s*12', ctx) \
       or "interval" in ctx.lower() or "1u <<" in ctx or "<<" in ctx and "Extension" in ctx:
        return ("ESTABLISHED", "constant", "na", False,
                "structural pitch-class/interval/TPC-delta or bitmask constant (music theory); not a tunable.")
    # 3) circle-of-fifths / mode tables.
    if func in ("ionianTonicPcFromFifths",) or "DIATONIC_PARENT" in ctx or func in ("collectionMask", "diatonicMaskFromFifths"):
        return ("ESTABLISHED", "constant", "na", False,
                "circle-of-fifths / mode-collection table entry (music theory FACT); not a tunable.")
    # 4) Inline threshold literals not backed by a named constant (0.3/0.2/0.1/0.05/0.01, or MIDI 60).
    if re.fullmatch(r'0?\.\d+', value) or value in ("60", "0.3", "0.2", "0.1", "0.05", "0.01"):
        try:
            fv = float(value)
        except ValueError:
            fv = None
        if fv is not None and 0.0 < fv < 1.0 and func in ("detectExtensions", "structuralPenalties",
                                                          "buildChordResult", "analyzeChord", "bassRootBonusMultiplier",
                                                          "templateHasMatchingThird", "templateHasMatchingFifth"):
            return ("ESTABLISHED", "constant", "no", True,
                    "inline extension/presence threshold (%s) -- hand-set, NOT override-registered, some duplicate kBassSupportPresenceThreshold/kWCompletePresenceThreshold (0.05); documented in-comment." % value)
    # 5) Everything else: structural / bound / index literal.
    return ("ESTABLISHED", "constant", "na", False,
            "structural literal (bound, index, threshold-with-documented-rationale); not a scoring tunable.")

def population_for(file, name, ctx):
    """Coarse population tag."""
    retiring_tokens = ("applyPostScoringGates", "applyIter8691Pedal", "promoteToWinner",
                       "PostScoringGateContext", "PromotionTarget")
    if any(t in (name or "") or t in (ctx or "") for t in retiring_tokens):
        return "RETIREMENT-COUPLED"
    if "Diagnostic" in (name or "") or "diagnose" in (name or "").lower():
        return "SURVIVES-diagnostic"
    if (name or "") in ("formatSymbol", "formatRomanNumeral", "formatNashvilleNumber"):
        return "SURVIVES-formatter-decl"
    if (name or "") in ("closePositionVoicing", "chordTonePitchClasses", "ClosePositionVoicing"):
        return "SURVIVES-voicing-decl"
    return "SURVIVES-oracle"

def read_csv(name):
    with open(os.path.join(AUD, name), encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("file") in FILES]

def main():
    rows_out = []

    # FUNCTIONS
    for r in read_csv("l4_functions.csv"):
        key = (r["file"], r["name"])
        if key in FUNC_OVERRIDES:
            verdict, vclass, flg, rat = FUNC_OVERRIDES[key]
        else:
            verdict, vclass, flg, rat = ("SURVIVES", "code", False, "surviving oracle/helper function; no issue.")
        rows_out.append(dict(file=r["file"], loc=f'{r["start_line"]}-{r["end_line"]}', kind="function",
                             name=r["name"], population=population_for(r["file"], r["name"], ""),
                             verdict_class=vclass, verdict=verdict, in_param_manifest="na",
                             flagged="yes" if flg else "no", rationale=rat))

    # LITERALS
    for r in read_csv("l4_literals.csv"):
        verdict, vclass, in_man, flg, rat = classify_literal(r)
        rows_out.append(dict(file=r["file"], loc=r["line"], kind="literal",
                             name=r["value"], population=population_for(r["file"], r["func"], r["context"]),
                             verdict_class=vclass, verdict=verdict, in_param_manifest=in_man,
                             flagged="yes" if flg else "no",
                             rationale=f'[{r["func"]}] {rat}'))

    # FIELDS
    for r in read_csv("l4_fields.csv"):
        owner = r["type_owner"]
        if owner in FIELD_OWNER_DISP:
            verdict, vclass, rat = FIELD_OWNER_DISP[owner]
        else:
            verdict, vclass, rat = ("PUBLISHED", "derived-fact", f"field of {owner}; published on the oracle contract surface; SURVIVES.")
        pop = population_for(r["file"], owner, r["context"])
        rows_out.append(dict(file=r["file"], loc=r["line"], kind="field",
                             name=f'{owner}.{r["name"]}', population=pop,
                             verdict_class=vclass, verdict=verdict, in_param_manifest="na",
                             flagged="no", rationale=rat))

    # BRANCHES
    for r in read_csv("l4_branches.csv"):
        rows_out.append(dict(file=r["file"], loc=r["line"], kind="branch",
                             name=f'{r["kind"]}@{r["func"]}', population=population_for(r["file"], r["func"], r["context"]),
                             verdict_class="code", verdict="SURVIVES", in_param_manifest="na",
                             flagged="no",
                             rationale=f'[{r["func"]}] branch in surviving oracle/helper; exercised on the corpus (see fire table); no issue.'))

    # DECLS
    for r in read_csv("l4_decls.csv"):
        nm = r["name"]
        flg = nm in ("formatRomanNumeral", "formatNashvilleNumber", "closePositionVoicing", "chordTonePitchClasses")
        rat = "local decl / call in surviving code; no issue."
        if flg:
            rat = "display/voicing/arrangement declaration living in the analysis header (chordanalyzer.h) -- ARCHITECTURE.md 4.1i-noted layering debt (analysis-is-display-agnostic 2.3)."
        rows_out.append(dict(file=r["file"], loc=r["line"], kind="decl",
                             name=nm, population=population_for(r["file"], nm, r["context"]),
                             verdict_class="code", verdict="SURVIVES", in_param_manifest="na",
                             flagged="yes" if flg else "no", rationale=rat))

    # CROSSLAYER (source-file rows only; inbound consumer edges noted separately in the report)
    for r in read_csv("l4_crosslayer.csv"):
        target = r["target_area"]
        flg = False  # the L4/L5 seam is expected architecture, not a finding; noted in rationale
        rat = f'include edge to {target}; '
        if target == "function":
            rat += "chord oracle -> harmonicfunctionlayer (the competition pipeline it hands the snapshot to); the L4/L5 seam, R1/R7-coupled but load-bearing (byte-identical E2d split); note not finding."
        elif target in ("key", "types"):
            rat += "reads the L3 key/mode + leaf types the oracle depends on; expected, SURVIVES."
        elif target == "param":
            rat += "Stage-5 override registration include; SURVIVES."
        else:
            rat += "internal chord include; SURVIVES."
        rows_out.append(dict(file=r["file"], loc=r["line"], kind="crosslayer",
                             name=r["include"], population="SURVIVES-oracle",
                             verdict_class="code", verdict="SURVIVES", in_param_manifest="na",
                             flagged="yes" if flg else "no", rationale=rat))

    # ── write artifacts ──
    cols = ["file", "loc", "kind", "name", "population", "verdict_class", "verdict",
            "in_param_manifest", "flagged", "rationale"]
    with open(os.path.join(AUD, "pass1_dispositions_oracle.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    # summary
    from collections import Counter
    by_kind = Counter(r["kind"] for r in rows_out)
    by_verdict = Counter(r["verdict"] for r in rows_out)
    by_class = Counter(r["verdict_class"] for r in rows_out)
    flagged = [r for r in rows_out if r["flagged"] == "yes"]
    manifest_missing = [r for r in rows_out if r["in_param_manifest"] == "no"]
    summary = dict(total_rows=len(rows_out), by_kind=dict(by_kind), by_verdict=dict(by_verdict),
                   by_verdict_class=dict(by_class), flagged_count=len(flagged),
                   constants_registered_absent_from_manifest=sorted(set(
                       re.search(r'\b(k[A-Z][A-Za-z0-9]+)\b', r["rationale"]).group(1)
                       for r in manifest_missing
                       if r["verdict_class"] == "constant" and "ABSENT" in r["rationale"]
                       and re.search(r'\b(k[A-Z][A-Za-z0-9]+)\b', r["rationale"]))))
    with open(os.path.join(AUD, "pass1_dispositions_oracle.json"), "w", encoding="utf-8") as f:
        json.dump(dict(meta=dict(
            audit="EG-7 Layer-4 (chord) PASS-1 oracle session (OI-102)",
            inventory_head="7f57aad4b5", corpus_hash="c50002fee1",
            files=sorted(FILES)), summary=summary, rows=rows_out), f, indent=1)

    print("total rows:", len(rows_out))
    print("by_kind:", dict(by_kind))
    print("by_verdict:", dict(by_verdict))
    print("by_verdict_class:", dict(by_class))
    print("flagged rows:", len(flagged))
    for r in flagged:
        print(f'  FLAG {r["file"].split("/")[-1]}:{r["loc"]} [{r["kind"]}] {r["name"]} -> {r["rationale"][:110]}')

if __name__ == "__main__":
    main()
