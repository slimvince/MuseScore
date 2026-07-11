#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
"""
gen_inventory.py — the machine-generated audit inventory for the EG-7 layer
certification audits (OI-84). ONE PASS-1 instrument, layer-selected by --layer
(l1l2 default — the original L1/L2 audit; l3 — the Layer-3 key/mode audit). One path
per concern (#6): the same enumeration + extraction serves every layer; --layer picks
the deep-audited tag set, the output dir, and the per-layer tag refinement.

WHAT THIS IS (protocol P1, cowork_audit_protocol.md; #17(f) applied to audit SCOPE):
  The audit domain is generated MECHANICALLY from the code, never chosen by hand.
  For the ENTIRE src/composing/ tree (tracked files at HEAD) it produces:
    (1) a FILE TABLE — every tracked file tagged L1 / L2 / L3+ / RETIRES with a
        one-line reason. The tag map is authored (a classification, verified against
        ARCHITECTURE.md + the roadmap layer definitions — see TAG_RULES below), but
        the ENUMERATION is total: the script EXITS NONZERO if any tracked file lacks
        a disposition (P1 totality — nothing silently skipped).
    (2) for every L1/L2-tagged file, the complete row lists:
          (a) functions/methods       -> l1l2_functions.csv
          (b) numeric literals         -> l1l2_literals.csv   (trivial 0/1 excluded)
          (c) struct/class fields on   -> l1l2_fields.csv     (header-declared = visible
              types visible outside                              outside the file)
          (d) branches (if/switch/?:)  -> l1l2_branches.csv
          (e) cross-layer calls/deps   -> l1l2_crosslayer.csv (includes crossing a
                                                                 layer/dir boundary)
    (3) a stamped manifest.json (HEAD commit, this script's blob sha, corpus hash,
        per-table row counts) — #16 reproducibility.

EXTRACTION METHOD (stated so the instrument is ESTABLISHED, #19 — not a black box):
  C++ is scanned, not compiled. Comments (// and /* */), string/char literal bodies,
  and preprocessor lines are blanked (line numbers preserved) before pattern matching,
  so nothing inside a comment or string is ever counted. Function DEFINITIONS are
  found by a brace-depth walk (an identifier '(' ... ')' [qualifiers/init-list] '{'
  that opens a body), which also yields each function's [start,end) line span so
  literals/branches can be attributed to their enclosing function. Header function
  DECLARATIONS (ending ';') are found by regex. The method is HEURISTIC and biased to
  OVER-capture (a false extra row gets a 'no issue' disposition; a missed row is the
  real risk) — known limits: macro-generated code, function-pointer typedefs, and
  deeply-nested lambdas may be mis-attributed. --self-check prints per-file counts for
  the establish-the-instrument cross-check (#19).

RUN:
  python tools/audit/gen_inventory.py                    # L1/L2 audit → tools/audit/l1l2/
  python tools/audit/gen_inventory.py --layer l3         # L3 audit    → tools/audit/l3/
  python tools/audit/gen_inventory.py --self-check       # + per-file extraction counts
  python tools/audit/gen_inventory.py --out-dir <scratch># override the artifact dir (byte-id check)
  (exit 0 iff every tracked file received a tag; nonzero on any untagged file — P1.)
"""

import csv
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCOPE_DIR = "src/composing"
CORPUS_HASH = "c50002fee1"   # the pinned corpus for these audits (instruction Task 1.3)

# ── Which layer's audit this run generates (P1 scope selector) ────────────────
# The SAME instrument serves every EG-7 layer audit (one path per concern, #6). A
# --layer flag selects (a) which tag set is "deep-audited", (b) the output dir, and
# (c) an optional per-layer tag REFINEMENT applied over the base TAG_RULES below.
#
#   --layer l1l2 (default): the original L1/L2 certification inventory. The base
#     TAG_RULES are used verbatim, DEEP_TAGS = (L1, L2), artifacts under
#     tools/audit/l1l2/. Byte-identical to the committed L1/L2 run — the L3_REFINE
#     step is NOT applied, so this file's L1/L2 output is unchanged.
#   --layer l3: the Layer-3 (key/mode) certification inventory (this instruction).
#     The L3_REFINE overrides below refine the base L3+ tags on the key/mode files
#     into L3 / L3-MIXED (and correct the mis-tags this audit found), DEEP_TAGS =
#     (L3, L3-MIXED), artifacts under tools/audit/l3/. Everything else is unchanged.
def _selected_layer(argv):
    if "--layer" in argv:
        i = argv.index("--layer")
        if i + 1 < len(argv):
            return argv[i + 1]
    return "l1l2"

AUDIT_LAYER = _selected_layer(sys.argv)
if AUDIT_LAYER not in ("l1l2", "l3"):
    sys.stderr.write("unknown --layer %r (expected l1l2 | l3)\n" % AUDIT_LAYER)
    sys.exit(2)


def _selected_out_dir(argv, default):
    # --out-dir <dir> overrides the artifact directory (used to re-generate into a
    # scratch dir for a byte-identity check without touching the committed artifacts).
    if "--out-dir" in argv:
        i = argv.index("--out-dir")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return default

OUT_DIR = _selected_out_dir(sys.argv, os.path.join(REPO_ROOT, "tools", "audit", AUDIT_LAYER))
PREFIX = AUDIT_LAYER   # row-list CSV filename prefix (l1l2_* / l3_*)

# ── The tag map (P1 file table) ──────────────────────────────────────────────
# Ordered rules; FIRST match wins. Each rule: (matcher, tag, reason).
#   matcher: a path (exact, repo-relative, forward-slash) OR a "dir/" prefix.
# Tags: L1 / L2 (deep-audited here) ; L3+ (out of THIS audit's scope, own layer
# audit later) ; RETIRES (on the R1-R10 retirement map — #12 interpretation-check at
# deletion only, per EG-7/OI-84, NOT deep-audited).
# Authority: ARCHITECTURE.md §"Layer 1/2"; cowork_layer1_note_model_design.md §3/§5;
# cowork_layer2_slicing_design.md §3; roadmap retirement map R1-R10 (docs/
# implementation_roadmap.md:138-145); the instruction's L1/L2 definition.
TAG_RULES = [
    # ---- L1: the fact layer (note model + L1.5 notation-derived views) ----
    ("src/composing/analysis/notemodel/note_model.h",  "L1",
     "Note-model core (NoteModel/NoteQueryIndex) — Architectural Layer 1 fact layer (layer1 design §3/§5)"),
    ("src/composing/analysis/notemodel/note_model.cpp", "L1",
     "Note-model core impl (build/tie-resolve/eligibility/query index) — Architectural Layer 1 (layer1 design §4/§6)"),
    ("src/composing/analysis/engravingbridge/regiontonecollector.h", "L1",
     "Derived summary views over the note model (weightedPcView/soundingAt) — L1 §3/§5; check for legacy collectRegionTones residue"),
    ("src/composing/analysis/engravingbridge/regiontonecollector.cpp", "L1",
     "Derived summary views impl — L1 §3/§5; check for legacy collectRegionTones residue (R-note)"),
    ("src/composing/analysis/engravingbridge/regiontoneprimitives.cpp", "L1",
     "weightedPcView/soundingAt primitive impl — L1 derived views (layer1 design §3)"),
    ("src/composing/analysis/engravingbridge/spellingview.h", "L1",
     "Spelling view — L1.5 notation-derived reader (instruction L1 def; R4 shared-spelling-view survivor)"),
    ("src/composing/analysis/engravingbridge/spellingview.cpp", "L1",
     "Spelling view impl — L1.5 notation-derived reader (R4 survivor)"),
    ("src/composing/analysis/engravingbridge/phraseboundaryview.h", "L1",
     "Phrase-boundary primitive — L1.5 notation-derived view (cowork_phrase_boundary_design.md)"),
    ("src/composing/analysis/engravingbridge/phraseboundaryview.cpp", "L1",
     "Phrase-boundary primitive impl — L1.5 notation-derived view"),
    ("src/composing/analysis/scoreharvest/metricweights.h", "L1",
     "Metric-weight primitive (regionMetricWeightForOnsetTick) — L1.5 (layer2 design §8 metric-weight contract)"),
    ("src/composing/analysis/scoreharvest/metricweights.cpp", "L1",
     "Metric-weight primitive impl — L1.5 notation-derived value (layer2 design §8)"),

    # ---- L2: segmentation (the SURVIVING change-point slicer) ----
    ("src/composing/analysis/slicing/slicer.h", "L2",
     "Change-point slicer (changePointSlices/Slice) — Architectural Layer 2 survivor (layer2 design §3)"),
    ("src/composing/analysis/slicing/slicer.cpp", "L2",
     "Change-point slicer impl — Architectural Layer 2 survivor (layer2 design §4/§5)"),

    # ---- RETIRES: the L2-legacy segmenter (segment-first spine) ----
    ("src/composing/analysis/harmony/harmonicsegmenter.h", "RETIRES",
     "L2-LEGACY greedy-expand segmenter — retires R6 (segment-first spine), superseded by the change-point slicer; #12-check the anchor thresholds"),
    ("src/composing/analysis/harmony/harmonicsegmenter.cpp", "RETIRES",
     "L2-LEGACY greedy-expand segmenter impl — retires R6; #12-check kAnchorMinScore/kRound2MinScore + greedy-expand interpretation"),

    # ---- RETIRES: R1 legacy chord competition + Gates A-L (+ R9 file split) ----
    ("src/composing/analysis/chord/chordanalyzer.cpp", "RETIRES",
     "R1 legacy chord competition + Gates A-L; R9 file-split — retires at E4 (roadmap R1/R9)"),
    ("src/composing/analysis/chord/postscoringgates.cpp", "RETIRES",
     "R1 legacy post-scoring Gates I/K/L — retires with the legacy competition at E4"),

    # ---- L3+ : out of THIS audit's scope, deferred to the owning layer's audit ----
    # chord/decode (L4)
    ("src/composing/analysis/chord/", "L3+",
     "chord/decode layer (L4) — deferred to the L4 certification audit (chordslicedecoder is the L4 survivor; chordanalyzer.h types consumed cross-layer)"),
    ("src/composing/analysis/decode/", "L3+",
     "L3 key-mode decoder scaffolding — deferred to the L3 audit"),
    ("src/composing/analysis/function/", "L3+",
     "function layer (L5) — deferred to the L5 audit (harmonicfunctionlayer rename R7; forwardoverride/resolver are Tier-1 armed traps)"),
    ("src/composing/analysis/grouping/", "L3+",
     "grouping for display (L6) — deferred to the L6 audit"),
    ("src/composing/analysis/key/", "L3+",
     "key/mode layer (L3) — deferred to the L3 audit (keyresolver shrinks R5; keymodesequence is the L3 survivor)"),
    ("src/composing/analysis/param/", "L3+",
     "param-override infrastructure — deferred (cross-cutting, not L1/L2)"),
    ("src/composing/analysis/progression/", "L3+",
     "progression recognizer (L5 input) — deferred to the L5 audit"),
    ("src/composing/analysis/region/", "L3+",
     "region orchestration (L3 seam); regionanalyzer.cpp EMBEDS the legacy greedy-expand segmenter retiring R6 — deferred to the L3 audit"),
    ("src/composing/analysis/section/", "L3+",
     "section / cadence / joint-key (L3-L5); cadencekeyanchor R3 diagnostic — deferred"),
    ("src/composing/analysis/types/", "L3+",
     "shared analysis types (cross-layer) — deferred; note: carries metric/spelling/tone type decls consumed by L1"),
    ("src/composing/analysis/vocabulary/", "L3+",
     "harmonic vocabulary (L4) — deferred to the L4 audit"),
    ("src/composing/analysis/voiceleading/", "L3+",
     "voice-leading analysis (L4/L5); voicelinearview is a derived view but serves L4+ selection — deferred (boundary note in report P3)"),
    ("src/composing/intonation/", "L3+",
     "tuning subsystem — outside the harmonic-analysis layer stack (separate concern), not L1/L2"),
    # module wiring / config / interfaces / top-level
    ("src/composing/composingmodule.h", "L3+", "module registration/wiring — not L1/L2 analysis"),
    ("src/composing/composingmodule.cpp", "L3+", "module registration/wiring — not L1/L2 analysis"),
    ("src/composing/composingconfiguration.h", "L3+", "module configuration — not L1/L2 analysis"),
    ("src/composing/composingconfiguration.cpp", "L3+", "module configuration — not L1/L2 analysis"),
    ("src/composing/analyzed_section.h", "L3+", "public output DTO — not L1/L2 analysis"),
    ("src/composing/icomposinganalysisconfiguration.h", "L3+", "config interface — not L1/L2 analysis"),
    ("src/composing/icomposingchordstaffconfiguration.h", "L3+", "config interface — not L1/L2 analysis"),
    ("src/composing/icomposingconfiguration.h", "L3+", "config interface — not L1/L2 analysis"),

    # tests + build + fixtures (out of L1/L2 SOURCE scope; L1/L2 test coverage noted in report P3)
    ("src/composing/tests/", "L3+", "test / fixture / test-data — out of L1/L2 source scope (L1/L2 regression tests noted in report P3)"),
    ("src/composing/CMakeLists.txt", "L3+", "build file — non-source"),
    ("src/composing/analysis/CMakeLists.txt", "L3+", "build file — non-source"),
    ("src/composing/intonation/CMakeLists.txt", "L3+", "build file — non-source"),
]

DEEP_TAGS = ("L1", "L2") if AUDIT_LAYER == "l1l2" else ("L3", "L3-MIXED")

# ── L3 (key/mode) tag refinement (applied over the base TAG_RULES iff --layer l3) ─
# The base map coarsely tags the key/mode files L3+ ("deferred to the L3 audit").
# THIS audit refines them. Verified at the code (instruction Task 1.1 — a mis-tag is
# a finding, not inherited): each file was read and its layer(s) confirmed at source.
# Tags:
#   L3        — whole file is Layer-3 key/mode inference.
#   L3-MIXED  — file mixes layers; its Layer-3 parts are in scope, the rest deferred
#               to the owning layer's audit (the split is recorded per row in Task 2).
#   L4        — a mis-tag correction: the file is Layer-4 (chord), NOT L3 (finding).
# Ordered; FIRST match wins; exact repo-relative paths (forward slash).
L3_REFINE = [
    # ---- Core L3: key/mode inference proper (whole file) ----
    ("src/composing/analysis/key/keymodesequence.h", "L3",
     "L3 key/mode SEQUENCE DECODER public surface (survivor, LIVE production region key path)"),
    ("src/composing/analysis/key/keymodesequence.cpp", "L3",
     "L3 key/mode sequence decoder impl (Viterbi + change cost + confidence over the lattice)"),
    ("src/composing/analysis/key/keymodeanalyzer.h", "L3",
     "L3 key/mode EMISSION scorer surface (analyzeKeyMode, 21-mode table helpers, KeyCandidateScore)"),
    ("src/composing/analysis/key/keymodeanalyzer.cpp", "L3",
     "L3 emission scorer impl (six scoring terms + pairwise disambiguation + family selection)"),
    ("src/composing/analysis/key/keyresolver.h", "L3",
     "L3 windowed resolver surface (resolveKeyAndModeRanked + shared resolveKeySignatureContext) — R5 shrink target"),
    ("src/composing/analysis/key/keyresolver.cpp", "L3",
     "L3 windowed resolver impl (dynamic lookahead, hysteresis, partial-signature correction) — serves S2 seed + P4 + diagnostic"),
    ("src/composing/analysis/key/keymodeformatting.cpp", "L3",
     "L3 key/mode label formatting (tonic-name tables + mode suffix)"),
    ("src/composing/analysis/key/modepriorpresets.h", "L3",
     "L3 mode-prior presets surface (5 named presets over 21 modes)"),
    ("src/composing/analysis/key/modepriorpresets.cpp", "L3",
     "L3 mode-prior preset table impl (duplicates KeyModeAnalyzerPreferences mode-prior defaults — sync-test-guarded)"),
    # ---- L3 key-evidence detectors (section/, key-agnostic + the joint key axis) ----
    ("src/composing/analysis/section/cadencekeyanchor.h", "L3",
     "L3 key-evidence: key-agnostic authentic-cadence anchor surface (R3 diagnostic; retire post-E5)"),
    ("src/composing/analysis/section/cadencekeyanchor.cpp", "L3",
     "L3 key-evidence impl: key-agnostic cadence detection + salience-weighted global tonic anchor"),
    ("src/composing/analysis/section/localmodulationdetector.h", "L3",
     "L3 key-evidence: key-agnostic local-modulation detector surface (4d-i diagnostic; not wired)"),
    ("src/composing/analysis/section/localmodulationdetector.cpp", "L3",
     "L3 key-evidence impl: establishment + cadence-confirmation local-key span commit"),
    ("src/composing/analysis/section/jointkeydecision.h", "L3",
     "L3 key-axis joint decision surface + the J-key-iii production wiring flag (gated OFF)"),
    ("src/composing/analysis/section/jointkeydecision.cpp", "L3",
     "L3 key-axis joint decision impl (home-pair backbone + soft re-rank Viterbi + scoped joint)"),
    # ---- Mixed: L3 parts in scope, the rest deferred (split recorded per row) ----
    ("src/composing/analysis/region/regionanalyzer.h", "L3-MIXED",
     "L3 seam surface (analyzeRegions + ReachBackOptions) mixed with L4 chord orchestration options"),
    ("src/composing/analysis/region/regionanalyzer.cpp", "L3-MIXED",
     "L3 seam (whole-score decode wiring / reach-back loop / localKeyForRegion / applyJointKeyWiring) + L4 chord orchestration + L2-legacy greedyExpand call — split recorded"),
    ("src/composing/analysis/region/harmonicrhythm.h", "L3-MIXED",
     "region DTO — carries L3 published key facts (keyModeResult/keyConfidence/keyAlternatives) alongside L4 chord fields — split recorded"),
    ("src/composing/analysis/section/sectionanalyzer.h", "L3-MIXED",
     "L3 key/mode stabilization surface mixed with L5 cadence/pivot labeling surface — split recorded"),
    ("src/composing/analysis/section/sectionanalyzer.cpp", "L3-MIXED",
     "L3 key/mode stabilization + gap-region key context + L5 cadence/pivot labeling — split recorded"),
    ("src/composing/analysis/section/sectioncadencedetection.cpp", "L3-MIXED",
     "L5 cadence/pivot labeling impl (reads L3 key confidence via the 0.8 gate) — L5-deferred, split recorded"),
    ("src/composing/analysis/types/analysistypes.h", "L3-MIXED",
     "cross-layer types leaf — holds L3 KeyModeAnalyzerPreferences/PitchContext/KeySigMode (in scope) + L4 ChordAnalyzerPreferences and other types (deferred to L4) — split recorded"),
    # ---- Mis-tag corrections found by this audit (Task 1.1) ----
    ("src/composing/analysis/decode/chordpathdecoder.h", "L4",
     "MIS-TAG (L1/L2 file table said 'L3 key-mode decoder scaffolding') — it is the beam-1 CHORD-path decoder (Stage 3.1), Layer 4; deferred to the L4 audit (pass-1 finding)"),
    ("src/composing/analysis/region/sparsechordrefinement.h", "L4",
     "L4 chord-quality refinement surface (consumes the L3 key as a prior) — deferred to the L4 audit"),
    ("src/composing/analysis/region/sparsechordrefinement.cpp", "L4",
     "L4 chord-quality refinement impl (diatonic-triad promotion from key context) — deferred to the L4 audit"),
]


def refine_l3(path, tag, reason):
    """In --layer l3 mode, override the base tag for the key/mode files. Returns the
    (possibly refined) (tag, reason); base tag unchanged for files L3_REFINE omits."""
    for matcher, l3tag, l3reason in L3_REFINE:
        if path == matcher:
            return l3tag, l3reason
    return tag, reason

# control keywords that precede '(' but are NOT function names
CTRL_KW = {"if", "for", "while", "switch", "catch", "return", "sizeof", "and", "or",
           "not", "do", "else", "case", "constexpr", "static_assert", "decltype",
           "alignof", "noexcept", "throw"}
QUAL_KW = ("const", "noexcept", "override", "final", "mutable", "volatile", "&", "&&")


def sh(args):
    return subprocess.check_output(args, cwd=REPO_ROOT, text=True).strip()


def list_tracked():
    out = sh(["git", "ls-files", SCOPE_DIR])
    return [l.replace("\\", "/") for l in out.splitlines() if l.strip()]


def resolve_tag(path):
    for matcher, tag, reason in TAG_RULES:
        if matcher.endswith("/"):
            if path.startswith(matcher):
                return tag, reason
        elif path == matcher:
            return tag, reason
    return None, None


# ── C++ blanking: kill comments / string bodies / preprocessor, keep line count ──
def blank_code(text):
    """Return text with // and /* */ comments, string/char literal BODIES, and
    preprocessor lines replaced by spaces. Newlines preserved (line numbers intact)."""
    out = []
    i, n = 0, len(text)
    state = "code"   # code | line_comment | block_comment | string | char
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if state == "code":
            if c == "/" and nxt == "/":
                state = "line_comment"; out.append("  "); i += 2; continue
            if c == "/" and nxt == "*":
                state = "block_comment"; out.append("  "); i += 2; continue
            if c == '"':
                state = "string"; out.append('"'); i += 1; continue
            if c == "'":
                state = "char"; out.append("'"); i += 1; continue
            out.append(c); i += 1; continue
        if state == "line_comment":
            if c == "\n":
                state = "code"; out.append("\n")
            else:
                out.append(" ")
            i += 1; continue
        if state == "block_comment":
            if c == "*" and nxt == "/":
                state = "code"; out.append("  "); i += 2; continue
            out.append("\n" if c == "\n" else " "); i += 1; continue
        if state == "string":
            if c == "\\":
                out.append("  "); i += 2; continue
            if c == '"':
                state = "code"; out.append('"'); i += 1; continue
            out.append("\n" if c == "\n" else " "); i += 1; continue
        if state == "char":
            if c == "\\":
                out.append("  "); i += 2; continue
            if c == "'":
                state = "code"; out.append("'"); i += 1; continue
            out.append("\n" if c == "\n" else " "); i += 1; continue
    blanked = "".join(out)
    # blank preprocessor lines (keep the newline)
    lines = blanked.split("\n")
    for k, ln in enumerate(lines):
        if ln.lstrip().startswith("#"):
            lines[k] = " " * len(ln)
    return "\n".join(lines)


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


IDENT = re.compile(r"[A-Za-z_]\w*")


def extract_functions(blanked):
    """Brace-depth walk. Returns list of dicts {name, start_line, end_line}.
    A '{' opens a function body when, scanning back over whitespace / a member-init
    list / trailing qualifiers, we reach a ')' whose matching '(' is preceded by an
    identifier that is not a control keyword and not 'namespace/struct/class/enum/union'."""
    funcs = []
    n = len(blanked)
    depth = 0
    stack = []   # frames: (name, start_line, depth_before)
    i = 0
    while i < n:
        c = blanked[i]
        if c == "{":
            name, sl = _funcname_before(blanked, i)
            if name is not None:
                stack.append((name, sl, depth))
            else:
                stack.append((None, None, depth))
            depth += 1
            i += 1
            continue
        if c == "}":
            depth -= 1
            if stack:
                fr = stack.pop()
                if fr[0] is not None and fr[2] == depth:
                    funcs.append({"name": fr[0], "start_line": fr[1],
                                  "end_line": line_of(blanked, i)})
            i += 1
            continue
        i += 1
    return funcs


def _funcname_before(blanked, brace_idx):
    """Given index of a '{', decide if it opens a function body and return (name, line)."""
    j = brace_idx - 1
    # skip whitespace
    while j >= 0 and blanked[j] in " \t\r\n":
        j -= 1
    # skip a member-init list ": a(b), c{d}" or trailing qualifiers, back to ')'
    # heuristic: if we don't land on ')' directly, walk back over init-list chars
    if j < 0:
        return None, None
    if blanked[j] != ")":
        # try to skip an init list / qualifiers: scan back to the matching ')' that
        # is followed (ignoring init-list) by this '{'. Look back for ')' before a ';' or '{' or '}'.
        k = j
        while k >= 0 and blanked[k] not in ";{}":
            if blanked[k] == ")":
                j = k
                break
            k -= 1
        if j < 0 or blanked[j] != ")":
            return None, None
    # match the ')' back to its '('
    pd = 0
    k = j
    while k >= 0:
        if blanked[k] == ")":
            pd += 1
        elif blanked[k] == "(":
            pd -= 1
            if pd == 0:
                break
        k -= 1
    if k < 0:
        return None, None
    # identifier immediately before '('
    m = k - 1
    while m >= 0 and blanked[m] in " \t\r\n":
        m -= 1
    end = m + 1
    while m >= 0 and (blanked[m].isalnum() or blanked[m] == "_"):
        m -= 1
    name = blanked[m + 1:end]
    if not name or name in CTRL_KW:
        return None, None
    if name in ("namespace", "struct", "class", "enum", "union"):
        return None, None
    # reject macro-ish ALLCAPS with no lowercase that are likely control macros? keep — over-capture ok
    return name, line_of(blanked, k)


def enclosing(funcs, ln):
    best = None
    for f in funcs:
        if f["start_line"] <= ln <= f["end_line"]:
            if best is None or (f["end_line"] - f["start_line"]) < (best["end_line"] - best["start_line"]):
                best = f
    return best["name"] if best else "<file-scope>"


NUM = re.compile(
    r"(?<![\w.])(?:0[xX][0-9a-fA-F]+|\d+\.\d+(?:[eE][+-]?\d+)?|\.\d+|\d+(?:[eE][+-]?\d+)?)(?![\w.])")


def extract_literals(blanked, orig_lines, funcs):
    rows = []
    for k, bl in enumerate(blanked.split("\n")):
        ln = k + 1
        for m in NUM.finditer(bl):
            tok = m.group(0)
            if tok in ("0", "1"):    # trivial 0/1 excluded (P1 rule, in-script)
                continue
            rows.append({"line": ln, "value": tok, "func": enclosing(funcs, ln),
                         "context": orig_lines[k].strip()[:160]})
    return rows


BRANCH_PATTERNS = [
    ("if", re.compile(r"\bif\s*\(")),
    ("else-if", re.compile(r"\belse\s+if\s*\(")),
    ("switch", re.compile(r"\bswitch\s*\(")),
    ("case", re.compile(r"\bcase\b")),
    ("ternary", re.compile(r"\?")),
]


def extract_branches(blanked, orig_lines, funcs):
    rows = []
    for k, bl in enumerate(blanked.split("\n")):
        ln = k + 1
        for kind, pat in BRANCH_PATTERNS:
            for _ in pat.finditer(bl):
                # avoid double-counting 'else if' as both else-if and if
                if kind == "if" and re.search(r"\belse\s+if\s*\(", bl):
                    continue
                rows.append({"line": ln, "kind": kind, "func": enclosing(funcs, ln),
                             "context": orig_lines[k].strip()[:160]})
    return rows


# a field declaration inside a struct/class body in a header
FIELD = re.compile(
    r"^\s*(?:mutable\s+|static\s+|constexpr\s+|inline\s+)*"
    r"(?P<type>[A-Za-z_][\w:<>,\s\*&]*?)\s+"
    r"(?P<name>[A-Za-z_]\w*)\s*(?:=[^;]+)?;\s*$")
DECL_FUNC = re.compile(r"\b[A-Za-z_]\w*\s*\([^;{]*\)\s*(?:const|noexcept|override|final|=\s*0|=\s*default|=\s*delete)?\s*;")


def extract_fields_and_decls(blanked, orig_lines, path):
    """Header-only: struct/class fields (visible outside the file) + function declarations.
    Tracks a simple class/struct stack so a field row carries its enclosing type."""
    fields = []
    decls = []
    if not path.endswith(".h"):
        return fields, decls
    type_stack = []   # (kind_name, brace_depth_at_open)
    depth = 0
    lines = blanked.split("\n")
    # precompute struct/class open lines by scanning tokens
    # simple line walk with brace tracking; detect 'struct X {' / 'class X {'
    for k, bl in enumerate(lines):
        ln = k + 1
        stripped = bl.strip()
        m = re.match(r"^(struct|class)\s+([A-Za-z_]\w*)", stripped)
        opens_here = bl.count("{")
        closes_here = bl.count("}")
        cur_type = type_stack[-1][0] if type_stack else None
        # field / decl detection inside a type body
        if cur_type is not None:
            fm = FIELD.match(bl)
            if fm and "(" not in bl and ")" not in bl:
                fields.append({"line": ln, "type_owner": cur_type,
                               "field_type": fm.group("type").strip(),
                               "name": fm.group("name"),
                               "context": orig_lines[k].strip()[:160]})
            if DECL_FUNC.search(bl):
                dm = re.search(r"([A-Za-z_]\w*)\s*\(", bl)
                if dm and dm.group(1) not in CTRL_KW:
                    decls.append({"line": ln, "type_owner": cur_type or "<free>",
                                  "name": dm.group(1),
                                  "context": orig_lines[k].strip()[:160]})
        else:
            # free function declaration in a header (namespace scope)
            if DECL_FUNC.search(bl):
                dm = re.search(r"([A-Za-z_]\w*)\s*\(", bl)
                if dm and dm.group(1) not in CTRL_KW:
                    decls.append({"line": ln, "type_owner": "<namespace>",
                                  "name": dm.group(1),
                                  "context": orig_lines[k].strip()[:160]})
        # update stack AFTER processing the line
        if m and "{" in bl:
            type_stack.append((m.group(2), depth))
        depth += opens_here - closes_here
        while type_stack and depth <= type_stack[-1][1]:
            type_stack.pop()
    return fields, decls


# cross-layer include: an include of a header outside this file's own directory
def extract_crosslayer(orig_text, path):
    rows = []
    own_dir = os.path.dirname(path)
    for k, ln in enumerate(orig_text.split("\n")):
        m = re.match(r'\s*#\s*include\s*"([^"]+)"', ln)
        if not m:
            continue
        inc = m.group(1)
        # resolve relative includes to compare layer/dir
        target = os.path.normpath(os.path.join(own_dir, inc)).replace("\\", "/") if inc.startswith(".") \
            else inc.replace("\\", "/")
        # a cross-layer dep = include that resolves outside the file's own analysis subdir
        tdir = os.path.dirname(target)
        crosses = tdir != own_dir
        # classify the target layer heuristically by its path segment
        seg = None
        for key in ("notemodel", "slicing", "engravingbridge", "scoreharvest", "harmony",
                    "chord", "decode", "function", "grouping", "key", "param",
                    "progression", "region", "section", "types", "vocabulary", "voiceleading"):
            if "/" + key + "/" in "/" + target or target.endswith("/" + key) or ("/" + key + "/") in target:
                seg = key
                break
        if crosses:
            rows.append({"line": k + 1, "include": inc, "resolved": target,
                         "target_area": seg or "external"})
    return rows


def write_csv(path, rows, cols):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    self_check = "--self-check" in sys.argv
    os.makedirs(OUT_DIR, exist_ok=True)
    files = list_tracked()

    # (1) FILE TABLE — total tagging or fail
    file_rows = []
    untagged = []
    for p in files:
        tag, reason = resolve_tag(p)
        if tag is None:
            untagged.append(p)
        elif AUDIT_LAYER == "l3":
            tag, reason = refine_l3(p, tag, reason)
        file_rows.append({"file": p, "tag": tag or "UNTAGGED", "reason": reason or ""})
    if untagged:
        sys.stderr.write("P1 TOTALITY FAILURE — untagged files (add a TAG_RULES entry):\n")
        for u in untagged:
            sys.stderr.write("  " + u + "\n")
        # still write the file table for inspection, then fail
        write_csv(os.path.join(OUT_DIR, "file_table.csv"), file_rows, ["file", "tag", "reason"])
        sys.exit(2)
    write_csv(os.path.join(OUT_DIR, "file_table.csv"), file_rows, ["file", "tag", "reason"])

    deep = [r["file"] for r in file_rows if r["tag"] in DEEP_TAGS]

    all_funcs, all_lits, all_branches, all_fields, all_decls, all_cross = [], [], [], [], [], []
    per_file = {}
    for p in deep:
        with open(os.path.join(REPO_ROOT, p), encoding="utf-8") as f:
            orig = f.read()
        orig_lines = orig.split("\n")
        blanked = blank_code(orig)
        funcs = extract_functions(blanked)
        lits = extract_literals(blanked, orig_lines, funcs)
        branches = extract_branches(blanked, orig_lines, funcs)
        fields, decls = extract_fields_and_decls(blanked, orig_lines, p)
        cross = extract_crosslayer(orig, p)
        for f_ in funcs:
            all_funcs.append({"file": p, **f_})
        for r in lits:
            all_lits.append({"file": p, **r})
        for r in branches:
            all_branches.append({"file": p, **r})
        for r in fields:
            all_fields.append({"file": p, **r})
        for r in decls:
            all_decls.append({"file": p, **r})
        for r in cross:
            all_cross.append({"file": p, **r})
        per_file[p] = {"functions": len(funcs), "literals": len(lits),
                       "branches": len(branches), "fields": len(fields),
                       "decls": len(decls), "crosslayer": len(cross)}

    write_csv(os.path.join(OUT_DIR, PREFIX + "_functions.csv"), all_funcs,
              ["file", "name", "start_line", "end_line"])
    write_csv(os.path.join(OUT_DIR, PREFIX + "_literals.csv"), all_lits,
              ["file", "line", "value", "func", "context"])
    write_csv(os.path.join(OUT_DIR, PREFIX + "_branches.csv"), all_branches,
              ["file", "line", "kind", "func", "context"])
    write_csv(os.path.join(OUT_DIR, PREFIX + "_fields.csv"), all_fields,
              ["file", "line", "type_owner", "field_type", "name", "context"])
    write_csv(os.path.join(OUT_DIR, PREFIX + "_decls.csv"), all_decls,
              ["file", "line", "type_owner", "name", "context"])
    write_csv(os.path.join(OUT_DIR, PREFIX + "_crosslayer.csv"), all_cross,
              ["file", "line", "include", "resolved", "target_area"])

    inventory = {
        "file_table": file_rows,
        "functions": all_funcs, "literals": all_lits, "branches": all_branches,
        "fields": all_fields, "decls": all_decls, "crosslayer": all_cross,
    }
    with open(os.path.join(OUT_DIR, "inventory.json"), "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=1)

    # (3) MANIFEST — stamp (no wall-clock: excluded per byte-identity precedent)
    head = sh(["git", "rev-parse", "HEAD"])
    script_rel = "tools/audit/gen_inventory.py"
    script_sha = sh(["git", "hash-object", script_rel])
    tag_counts = {}
    for r in file_rows:
        tag_counts[r["tag"]] = tag_counts.get(r["tag"], 0) + 1
    manifest = {
        "instrument": "tools/audit/gen_inventory.py",
        "audit": ("EG-7 L1/L2 certification, PASS 1 (blind enumerative)"
                  if AUDIT_LAYER == "l1l2"
                  else "EG-7 Layer-3 (key/mode) certification, PASS 1 (blind enumerative)"),
        "audit_layer": AUDIT_LAYER,
        "head_commit": head,
        "script_blob_sha": script_sha,
        "corpus_hash": CORPUS_HASH,
        "scope_dir": SCOPE_DIR,
        "extraction_method": "regex/brace-depth scan over comment/string/preproc-blanked C++; heuristic, over-capture-biased; see module docstring",
        "totals": {
            "tracked_files": len(files),
            "file_table_rows": len(file_rows),
            "tag_counts": tag_counts,
            "deep_audited_files": len(deep),
            "functions": len(all_funcs),
            "literals": len(all_lits),
            "branches": len(all_branches),
            "fields": len(all_fields),
            "decls": len(all_decls),
            "crosslayer": len(all_cross),
        },
        "deep_audited_file_list": deep,
    }
    with open(os.path.join(OUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)

    print("gen_inventory OK — %d tracked files, %d deep-audited (%s)" %
          (len(files), len(deep), "/".join(DEEP_TAGS)))
    print("  tag counts:", tag_counts)
    print("  rows: funcs=%d lits=%d branches=%d fields=%d decls=%d cross=%d" %
          (len(all_funcs), len(all_lits), len(all_branches), len(all_fields),
           len(all_decls), len(all_cross)))
    if self_check:
        print("\n-- per-file extraction counts (establish-the-instrument cross-check) --")
        for p in deep:
            c = per_file[p]
            print("  %-62s f=%2d lit=%3d br=%3d fld=%2d dcl=%2d x=%2d" %
                  (p, c["functions"], c["literals"], c["branches"], c["fields"],
                   c["decls"], c["crosslayer"]))


if __name__ == "__main__":
    main()
