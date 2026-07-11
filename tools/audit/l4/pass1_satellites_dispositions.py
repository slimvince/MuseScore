#!/usr/bin/env python3
"""
EG-7 Layer-4 (chord) certification audit — PASS 1 (blind enumerative), session 3
of 3: the satellites (formatter, path decoder, sparse refinement, layer-4 types).

Instrument for OI-102 / OI-84 / EG-7. READ-ONLY over the frozen raw inventory
(tools/audit/l4/{l4_functions,l4_literals,l4_fields,l4_branches,l4_decls,
l4_crosslayer}.csv, stamped in manifest.json at corpus c50002fee1). It produces a
disposition for EVERY in-scope inventory row (protocol P1/P2) — "no issue" is a
recorded verdict with a stated reason, findings are flagged in a plain-language
column (no self-invented IDs; register rows carry OI-### assigned at unblind).

Scope (deep-audited files for this session):
  - src/composing/analysis/chord/chordsymbolformatter.cpp     (LIVE formatter)
  - src/composing/analysis/decode/chordpathdecoder.h          (LIVE beam-1 path)
  - src/composing/analysis/region/sparsechordrefinement.cpp   (LIVE refinement)
  - src/composing/analysis/region/sparsechordrefinement.h
  - src/composing/analysis/types/analysistypes.h  (L4-type rows only: lines < 546;
    KeySigMode onward are L3 types, covered by the L3 audit — excluded here)

Verdict rubric (cowork_audit_protocol.md P2):
  premises:      FACT / THEORY / ASSUMPTION
  derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED
  constants:     ESTABLISHED / UNFIT / DEAD  (+ in param_manifest)
  code:          SURVIVES  (population re-affirmed per row)
"""
import csv, json, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

FORMATTER = "src/composing/analysis/chord/chordsymbolformatter.cpp"
DECODER   = "src/composing/analysis/decode/chordpathdecoder.h"
SPARSE_C  = "src/composing/analysis/region/sparsechordrefinement.cpp"
SPARSE_H  = "src/composing/analysis/region/sparsechordrefinement.h"
TYPES     = "src/composing/analysis/types/analysistypes.h"
TYPES_L4_MAX_LINE = 545   # ChordTemporalContext ends 537; KeySigMode begins 546 (L3, out)

SCOPE = {FORMATTER, DECODER, SPARSE_C, SPARSE_H, TYPES}

TABLES = [
    ("l4_functions.csv", "function"),
    ("l4_literals.csv",  "literal"),
    ("l4_fields.csv",    "field"),
    ("l4_branches.csv",  "branch"),
    ("l4_decls.csv",     "decl"),
    ("l4_crosslayer.csv","crosslayer"),
]

# ── param_manifest presence (substring test over the whole manifest text) ──────
PM_TEXT = open(os.path.join(ROOT, "tools", "param_manifest.json"), encoding="utf-8").read()
def in_param_manifest(name):
    if not name:
        return "n/a"
    if ('"' + name + '"') in PM_TEXT:
        return "yes-row"
    if name in PM_TEXT:
        return "notes-only"
    return "no"

# ── ChordAnalyzerPreferences fields that carry a tunable scoring default ───────
PREF_FIELDS = [
    "bassNoteRootBonus","bassRootThirdOnlyMultiplier","bassRootAloneMultiplier",
    "diatonicRootBonus","tpcConsistencyBonusPerTone","rootContinuityBonus",
    "resolutionBonus","stepwiseBassInversionBonus","stepwiseBassLookaheadBonus",
    "completeTriadInversionBonus","sameRootInversionBonus","maxTotalInversionContextBonus",
    "inversionSuspicionMargin","inversionBonusReduction","preferMinorOverMajorAdd6",
    "harmonicBoundaryJaccardThreshold","pedalTailWeightMultiplier",
    "bassPassingToneMinWeightFraction","extensionThreshold","minDistinctPcsForCandidate",
    "pedalConfidenceThreshold","decodeQualityLevel","scoringPhase",
]

# ── Targeted overlays: (basename, lo, hi, kind|None, verdict, vclass, finding, note, anchor_only)
# Applied to any row whose file basename matches and line in [lo,hi] (and kind matches
# if given). Later overlays win. finding != "" flags the row; when anchor_only is True the
# FINDING flag is stamped only on the lowest line in the range (the table/block head) while
# every row in the range still receives the verdict + note (totality preserved).
OV = [
 # ---------------- chordsymbolformatter.cpp ----------------
 # Duplicated music-theory tables: each literal is an ESTABLISHED constant that happens to be
 # part of a table duplicated elsewhere; the #6 duplication FINDING is anchored at the head row.
 ("chordsymbolformatter.cpp", 46, 66, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): SHARP/FLAT/GERMAN note-name tables",
  "The four static note-name arrays are duplicated verbatim in csfPitchClassNameFromTpc (88-99). "
  "ARCHITECTURE.md already flags this (a latent mis-spelling risk if one copy is edited without the "
  "other) and proposes a shared helper. Music-theory constant tables (ESTABLISHED values); the second "
  "copy is a #6 duplication.", True),
 ("chordsymbolformatter.cpp", 88, 99, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): SHARP/FLAT/GERMAN note-name tables (2nd copy)",
  "Second verbatim copy of the 46-58 note-name tables. Same ARCHITECTURE-known duplication.", True),
 ("chordsymbolformatter.cpp", 108, 193, "branch", "ASSUMPTION", "premise",
  "FINDING premise-provenance (#17f): enharmonic-spelling normalization thresholds",
  "The pc=3/pc=8/pc=10 and Cb/Fb spelling-normalization branches are notation-convention ASSUMPTIONS "
  "justified in comments by hand-transcribed corpus-survey counts (Iter 78/84/89: '533 sharp-authored "
  "pc=8', '155/277', '95/256') that are not generated artifacts (#17f). Display-layer only (does not "
  "affect chord identity/inference). Load-bearing for display spelling correctness.", True),
 ("chordsymbolformatter.cpp", 457, 465, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): diatonic scale-interval table (csfChromaticRoman SCALES)",
  "The 7-mode diatonic interval table is repeated at csfTonicizationScales (788-796) in the same file, "
  "and the shared key-layer primitive keyModeScaleIntervals already holds it (used by "
  "sparsechordrefinement). Three copies of the same music-theory table.", True),
 ("chordsymbolformatter.cpp", 466, 467, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): UPPER/LOWER Roman-numeral arrays",
  "The UPPER/LOWER numeral literal arrays recur at 492-493 (csfDiatonicRoman) and 937-938 "
  "(formatRomanNumeral tonicization). Three copies.", True),
 ("chordsymbolformatter.cpp", 788, 796, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): diatonic scale-interval table (csfTonicizationScales)",
  "Second in-file copy of the 457-465 scale table; also duplicates the shared keyModeScaleIntervals.", True),
 ("chordsymbolformatter.cpp", 799, 803, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): KeySigMode->diatonic-parent mapping (csfTonicizationParent)",
  "Byte-identical to CHR_DIATONIC_PARENT declared inside formatRomanNumeral (840-844). Two copies of "
  "the same 21-entry mode->parent table.", True),
 ("chordsymbolformatter.cpp", 840, 844, None, "ESTABLISHED", "constant",
  "FINDING duplication (#6): KeySigMode->diatonic-parent mapping (CHR_DIATONIC_PARENT)",
  "Byte-identical to csfTonicizationParent (799-803).", True),
 ("chordsymbolformatter.cpp", 486, 618, "function", "SURVIVES", "code",
  "boundary note: csfDiatonicRoman emits L5-flavored functional Roman labels",
  "csfDiatonicRoman/formatRomanNumeral read result.function.degree/keyTonicPc/keyMode/nextRootPc "
  "(functional/L5 facts) to build Roman numerals on an L4 translation unit. File-table FLAG; "
  "L4/L5 layer home is an open register question (not decided here).", True),
 ("chordsymbolformatter.cpp", 539, 545, "branch", "SURVIVES", "code",
  "FINDING doc-sync (#10): RN extension levels 9/11/13 ARE emitted",
  "csfDiatonicRoman sets level=13/11/9 and appends the numeral (and (add9/11/13)); the corpus shows "
  "~130 such Roman numerals per preset. ARCHITECTURE.md #4.3 states 'extensions beyond the 7th are not "
  "yet emitted' — stale/contradicted by code and data (#15).", True),
 ("chordsymbolformatter.cpp", 884, 899, None, "SURVIVES", "code",
  "FINDING contract-mismatch (#10): aug6 label preset-gating asserted by doc, deferred in code",
  "The It+6/Fr+6/Ger+6 block fires unconditionally; its own comment says 'Preset gating "
  "(Standard/Baroque only): deferred — formatRomanNumeral() has no preset context'. ARCHITECTURE #5.11 "
  "claims aug6 is 'Gated to Standard and Baroque presets only'. Corpus: Baroque 8 / Default 7 / Jazz 0 "
  "aug6 labels — the Jazz 0 is an upstream-analysis coincidence (SharpThirteenth not set), not the "
  "documented gate. Any effective gating is at the call site (out of scope) — note the dependency. "
  "Also an L5-flavored functional label on an L4 TU (boundary).", True),
 ("chordsymbolformatter.cpp", 901, 962, None, "SURVIVES", "code",
  "boundary note: tonicization label (V7/x, viio/x) is L5-flavored functional labeling",
  "Fires when function.nextRootPc>=0 (chord-staff two-pass). Corpus: ~440 tonicization Roman labels "
  "per preset. Universal across presets by design (ARCHITECTURE #5.10). L4/L5 boundary; not decided.", True),
 ("chordsymbolformatter.cpp", 971, 1050, None, "SURVIVES", "code",
  "FINDING contract-gap (P3): Nashville renders chromatic roots as '?' and bass via crude mod-7",
  "formatNashvilleNumber returns '?' for a non-diatonic (chromatic) root (1029-1032, 'refine as "
  "needed') and nashvilleBassSuffix maps any bass via (bassDegree%7)+1 (1013-1020, 'refine as needed'), "
  "which mislabels a chromatic bass degree. LIVE via the notation bridge/imploder/context-menu, so the "
  "gap is user-reachable, not test-only. Not every committed identity has a defined Nashville rendering.", True),
 ("chordsymbolformatter.cpp", 711, 725, "function", "SURVIVES", "code",
  "no issue: slash-bass name guard (the /p fix)",
  "csfIsValidBassNoteName guards the slash-bass suffix against invalid TPC-derived names (the '/p' bug, "
  "fixed 2026-04-13). Present and correct.", True),
 # ---------------- chordpathdecoder.h ----------------
 ("chordpathdecoder.h", 1, 999, None, "SURVIVES", "code",
  "boundary note: retire-vs-survive at the engagement is OPEN",
  "LIVE beam-1 commit-chain re-expression. Callers: regionanalyzer.cpp only (Pass-1 + two Pass-2/2b "
  "sub-loops) plus decode_tests.cpp. commit() re-expresses advanceTemporalContext (the retiring "
  "region-competition path's hand-threaded state); the forward members path()/recordNode()/alternatives/"
  "winnerScore/winnerMargin are inert staging for the SURVIVING Stage-6 consumer and wider-beam "
  "(Stage 3.2). Coupled to the retiring competition via advanceTemporalContext, shaped for the surviving "
  "consumer — facts recorded; the retire/survive decision is not made here (open register question).", True),
 ("chordpathdecoder.h", 118, 133, None, "SURVIVES", "code",
  "declared-dormant, consumer named: path()/recordNode()/alternatives/margins",
  "Inert at beam 1 (nothing reads path() yet). Declared dormancy with a named future consumer (Stage 6 "
  "functional labeling; Stage 3.1b decode-once/query-many) — satisfies the fact-publication corollary "
  "(declared dormancy, future consumer named), not waste.", True),
 # ---------------- sparsechordrefinement.{h,cpp} ----------------
 ("sparsechordrefinement.h", 1, 999, None, "SURVIVES", "code",
  "boundary note (#1): overwrites committed L4 identity.quality from the resolved key",
  "LIVE diatonic-quality refinement on the region path (regionanalyzer 1003/1005/1221/1411; bridge 640; "
  "section 158). Consumes the resolved key (keyFifths/keyMode) as a prior and overwrites the committed "
  "identity.quality AFTER analyzeChord commit. L4/L5 layer home is an open register question — declared "
  "to Cowork, not decided here.", True),
 ("sparsechordrefinement.cpp", 106, 117, "function", "PUBLISHED", "derived-fact",
  "note: diatonicDegreeForRootPc is a widely-consumed pure primitive in a narrow-purpose file",
  "Single published copy (no #6 duplication), consumed layer-wide: L5 function modules "
  "(functionresolver/functionromannumeral/functionrelationallabel), section, bridge, batch. Its HOME "
  "(region/sparsechordrefinement) is narrower than its consumer set — a possible-misplacement note "
  "(shared music-theory primitive), not a duplication.", True),
 ("sparsechordrefinement.cpp", 168, 201, "function", "SURVIVES", "code",
  "boundary note (#1): applyTonicPriorToSparseChord overrides a committed NON-Unknown thin quality",
  "Unlike refineSparseChordQualityFromKeyContext (Unknown-only), this overwrites a committed "
  "Power/Suspended2/Suspended4 quality on <=2-PC regions with the key's diatonic triad quality. The most "
  "aggressive post-commit key-conditioned overwrite of an L4 field. Boundary-ownership open.", True),
 # ---------------- types/analysistypes.h ----------------
 ("analysistypes.h", 388, 414, None, "DEAD", "constant",
  "declared placeholder (not waste): useExistingChordSymbols/useRomanNumeral/useNashvilleAnnotations + StylePrior",
  "Default-false, unwired 'TODO: implement' toggles. ARCHITECTURE 'Do not remove' lists them as "
  "placeholders for named planned features (LLM integration; Authoritative Chord Symbol Mode #4.1f). "
  "DEAD-but-reserved with named future consumer — declared, not silent dead code.", True),
 ("analysistypes.h", 254, 268, None, "ESTABLISHED", "constant",
  "note: maxTotalInversionContextBonus is a documented-inert cap (never clamps at current values)",
  "Default 2.0; the four feeding bonuses sum to <=1.85 (Baroque/Default) or 0.75 (Jazz), so std::min "
  "never binds. Documented-inert safety cap; consumer is fn::inversionContextBonus (oracle session). "
  "In param_manifest. Not a finding (documented).", True),
]

def overlays_matching(basename, line, kind):
    """Yield the OV entries (with index) matching a row, in file order (later wins)."""
    for idx, ov in enumerate(OV):
        (bn, lo, hi, k, verdict, vclass, finding, note, anchor_only) = ov
        if bn != basename:
            continue
        if k is not None and k != kind:
            continue
        if lo <= line <= hi:
            yield idx, ov

# ── Class defaults per (basename, kind) ───────────────────────────────────────
def base_disposition(basename, kind, value, func, line):
    """Return (verdict, vclass, population, assumes, publishes, consumes, edge, note)."""
    pop = "LIVE"
    if basename == "chordpathdecoder.h":
        pop = "LIVE (retire/survive at engagement OPEN)"
    # ---- constants / literals ----
    if kind == "literal":
        if basename == "chordsymbolformatter.cpp":
            return ("ESTABLISHED", "constant", pop,
                    "a committed ChordAnalysisResult + key-signature fifths",
                    "a display substring", "notation render / batch output / status bar",
                    "handled per rendering branch",
                    "music-theory / TPC-encoding / notation-catalog integer (pitch class, scale "
                    "interval, TPC code, key-fifths threshold, figured-bass index). Not tunable; "
                    "not in param_manifest.")
        if basename == "analysistypes.h":
            nm = func or ""
            pm = in_param_manifest(func) if func in PREF_FIELDS else "n/a"
            return ("ESTABLISHED", "constant", pop,
                    "n/a (a default value / optimizer bound in a value type)",
                    "the compile-time default consumed by the analyzer/competition pipeline",
                    "analyzeChord + the competition pipeline (use-site dispositioned in the oracle session)",
                    "default member-initializer; bounds() supplies optimizer range",
                    "ChordAnalyzerPreferences scoring default or bounds() optimizer range; fit-status "
                    "per parameter is recorded in param_manifest.json; the USE-site disposition belongs "
                    "to the oracle session.")
        # sparsechordrefinement / decoder literals
        return ("ESTABLISHED", "constant", pop,
                "n/a", "n/a", "the enclosing function",
                "scale-degree / pitch-class / interval bound",
                "music-theory bound (scale degree 0..6, pitch-class %12, triad interval). Not tunable; "
                "not in param_manifest.")
    # ---- functions ----
    if kind == "function":
        if basename == "chordsymbolformatter.cpp":
            return ("SURVIVES", "code", pop,
                    "a committed ChordAnalysisResult (identity + function + key context)",
                    "a display string (chord symbol / Roman numeral / Nashville number)",
                    "notation render bridge, batch_analyze output, status bar / context menu",
                    "empty/sparse identity, Unknown quality, slash bass, enharmonic spelling, "
                    "chromatic root, symmetric chord",
                    "LIVE display formatter function; analysis-is-display-agnostic separation (#2.3).")
        if basename == "sparsechordrefinement.cpp":
            return ("SURVIVES", "code", pop,
                    "a committed ChordAnalysisResult + region tones + resolved key",
                    "a possibly-overwritten identity.quality (and function.degree/keyTonicPc/keyMode)",
                    "regionanalyzer Pass-1/2/2b, section analyzer, notation bridge",
                    "Unknown quality, <=2-PC region, Aeolian lone tonic/dominant, non-diatonic root",
                    "LIVE post-commit diatonic-quality refinement (region path).")
        # decoder methods
        return ("SURVIVES", "code", pop,
                "the seed temporal context + per-region inputs written on context()",
                "the threaded temporal context + (inert) decoded path",
                "regionanalyzer.cpp (3 sites) + decode_tests.cpp",
                "beam-1 single path; levels>FastBeam1 behave as FastBeam1 (no-op)",
                "byte-identical re-expression of advanceTemporalContext at beam 1.")
    # ---- fields ----
    if kind == "field":
        if basename == "analysistypes.h":
            pm = in_param_manifest(value) if value in PREF_FIELDS else "n/a"
            return ("PUBLISHED", "derived-fact", pop,
                    "n/a (a value-type member)",
                    "a value that crosses the L1.5/L3/L4 boundaries (pure-relocation leaf)",
                    "chord analyzer, key analyzer, engraving bridge, region/section pipeline",
                    "default member-initializer stated in-struct",
                    "cross-layer value-type field in the pure-relocation types leaf.")
        # chordpathdecoder.h private members
        return ("SURVIVES", "code", pop,
                "n/a (decoder path state)",
                "the threaded path state / decoded path",
                "the decoder's own commit()/recordNode()",
                "initialized to the loop-local defaults it replaces",
                "beam-1 decoder path-state member.")
    # ---- branches ----
    if kind == "branch":
        if basename == "chordsymbolformatter.cpp":
            return ("SURVIVES", "code", pop,
                    "a committed identity's quality/extensions/bass",
                    "a display substring for that case",
                    "the formatter's output string",
                    "the per-case notation convention it encodes",
                    "notation-convention rendering branch.")
        return ("SURVIVES", "code", pop,
                "the refinement guard inputs (quality, PC count, degree, key)",
                "whether the committed quality is overwritten",
                "the caller's committed ChordAnalysisResult",
                "Unknown/thin quality, <=2-PC, non-diatonic root, Aeolian exclusion",
                "refinement guard/branch.")
    # ---- decls ----
    if kind == "decl":
        return ("SURVIVES", "code", pop, "n/a", "the declared surface", "callers of the module",
                "n/a", "public declaration.")
    # ---- crosslayer ----
    if kind == "crosslayer":
        note = "cross-layer include/call."
        vclass = "code"
        verdict = "SURVIVES"
        if basename in ("sparsechordrefinement.cpp", "sparsechordrefinement.h") and "key" in (value or ""):
            note = ("consumes the L3 key (keymodeanalyzer.h) as a prior — the L4/L5 boundary "
                    "consumption; expected/declared.")
        return (verdict, vclass, pop, "n/a", "n/a", "n/a", "n/a", note)
    return ("SURVIVES", "code", pop, "n/a", "n/a", "n/a", "n/a", "row.")

# ── Map analysistypes.h field default-initializer lines to their field name, so a
#    numeric-default literal on that line inherits the field's param_manifest linkage.
TYPES_FIELD_LINE = {}
with open(os.path.join(HERE, "l4_fields.csv"), newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        if row["file"] == TYPES:
            TYPES_FIELD_LINE[int(row.get("line", 0) or 0)] = row.get("name", "")

# ── Build dispositions (pass 1: base + verdict/note overlay) ──────────────────
rows_out = []
for tbl, kind in TABLES:
    path = os.path.join(HERE, tbl)
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            f = row["file"]
            if f not in SCOPE:
                continue
            # l4_functions.csv records start_line/end_line; all other tables use `line`.
            line = int(row.get("line") or row.get("start_line") or 0)
            if f == TYPES and line >= 546:
                continue  # L3 types — reference only, out of this session's scope
            basename = f.split("/")[-1]
            value = row.get("value") or row.get("name") or ""
            func = row.get("func") or ""
            (verdict, vclass, pop, assumes, publishes, consumes, edge, note) = \
                base_disposition(basename, kind, value, func, line)
            ov_idx = None
            for idx, ov in overlays_matching(basename, line, kind):
                verdict, vclass, _flag, note = ov[4], ov[5], ov[6], ov[7]
                ov_idx = idx  # last (later wins) governs verdict/note
            pm = "n/a"
            if kind in ("literal", "field") and basename == "analysistypes.h":
                if kind == "field":
                    cand = value
                else:  # literal: inherit the field declared on the same line, else its func
                    cand = TYPES_FIELD_LINE.get(line) or func
                pm = in_param_manifest(cand) if cand in PREF_FIELDS else "no(structural)"
            rows_out.append({
                "file": f, "line": line, "kind": kind, "value": value, "func": func,
                "population": pop, "verdict_class": vclass, "verdict": verdict,
                "in_param_manifest": pm, "assumes": assumes, "publishes": publishes,
                "consumes": consumes, "edge_cases": edge, "finding": "", "note": note,
                "_basename": basename, "_ov_idx": ov_idx,
            })

# ── Pass 2: stamp each overlay's finding flag on the minimum in-range row line ──
for idx, ov in enumerate(OV):
    (bn, lo, hi, k, verdict, vclass, finding, note, anchor_only) = ov
    matches = [r for r in rows_out
               if r["_basename"] == bn and lo <= r["line"] <= hi
               and (k is None or r["kind"] == k)]
    if not matches:
        # An overlay that matches no inventory row is itself a tooling STOP (surface it).
        print("WARN: overlay matched zero rows:", bn, lo, hi, k, "|", finding)
        continue
    anchors = [min(matches, key=lambda r: r["line"])] if anchor_only else matches
    for r in anchors:
        # Only stamp if THIS overlay governs the row (later-wins), so the flag matches the verdict.
        if r["_ov_idx"] == idx or not anchor_only:
            r["finding"] = finding

for r in rows_out:
    r.pop("_basename", None); r.pop("_ov_idx", None)

rows_out.sort(key=lambda r: (r["file"], r["line"], r["kind"]))

# ── Emit CSV + JSON ───────────────────────────────────────────────────────────
COLS = ["file","line","kind","value","func","population","verdict_class","verdict",
        "in_param_manifest","assumes","publishes","consumes","edge_cases","finding","note"]
with open(os.path.join(HERE, "pass1_dispositions_satellites.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS)
    w.writeheader()
    for r in rows_out:
        w.writerow(r)

summary = {
    "audit": "EG-7 Layer-4 (chord) PASS 1 (blind), session 3 of 3 — satellites",
    "corpus_hash": "c50002fee1",
    "scope_files": sorted(SCOPE),
    "total_rows": len(rows_out),
    "by_file": dict(collections.Counter(r["file"].split("/")[-1] for r in rows_out)),
    "by_kind": dict(collections.Counter(r["kind"] for r in rows_out)),
    "by_verdict": dict(collections.Counter(r["verdict"] for r in rows_out)),
    "by_verdict_class": dict(collections.Counter(r["verdict_class"] for r in rows_out)),
    "flagged_rows": [
        {"file": r["file"], "line": r["line"], "kind": r["kind"], "finding": r["finding"]}
        for r in rows_out if r["finding"].startswith("FINDING")
    ],
    "boundary_note_rows": [
        {"file": r["file"], "line": r["line"], "kind": r["kind"], "note_head": r["finding"]}
        for r in rows_out if r["finding"] and not r["finding"].startswith("FINDING")
    ],
}
with open(os.path.join(HERE, "pass1_dispositions_satellites.json"), "w", encoding="utf-8") as fh:
    json.dump({"summary": summary, "rows": rows_out}, fh, indent=1)

print(json.dumps(summary, indent=1))
