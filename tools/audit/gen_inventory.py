#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
"""
gen_inventory.py — the machine-generated audit inventory for the EG-7 layer
certification audits (OI-84). ONE PASS-1 instrument, layer-selected by --layer
(l1l2 default — the original L1/L2 audit; l3 — the Layer-3 key/mode audit; l4 — the
Layer-4 chord audit; l5 — the Layer-5 function + measurement-instruments audit).
One path per concern (#6): the same enumeration + extraction serves every layer;
--layer picks the deep-audited tag set, the output dir, and the per-layer tag
refinement.

  --layer l5 adds a SECOND scope root beside src/composing: the measurement
  INSTRUMENTS under tools/ (the regression-stop chain, the corpus generators/
  validators, the ground-truth parser, the comparison/grading tools, the fit
  manifest, and batch_analyze as the shared harness). Because most instruments are
  PYTHON, l5 extraction routes each deep file by extension — the C++ scan (below)
  for .cpp/.h, and a Python `ast` scan for .py (functions/literals/branches/class
  fields/internal-imports/file-IO). One instrument, two language front-ends; the
  row schema is shared. See L5_REFINE (the L5-source population tags) and
  INSTRUMENT_RULES (the tools/ instrument enumeration).

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
  python tools/audit/gen_inventory.py --layer l4         # L4 audit    → tools/audit/l4/
  python tools/audit/gen_inventory.py --layer l5         # L5+instr    → tools/audit/l5/
  python tools/audit/gen_inventory.py --self-check       # + per-file extraction counts
  python tools/audit/gen_inventory.py --out-dir <scratch># override the artifact dir (byte-id check)
  (exit 0 iff every tracked file in scope received a tag; nonzero on any untagged file — P1.)
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
#   --layer l3: the Layer-3 (key/mode) certification inventory. The L3_REFINE
#     overrides below refine the base L3+ tags on the key/mode files into L3 /
#     L3-MIXED (and correct the mis-tags that audit found), DEEP_TAGS = (L3, L3-MIXED),
#     artifacts under tools/audit/l3/. Everything else is unchanged.
#   --layer l4: the Layer-4 (chord) certification inventory (this instruction). The
#     L4_REFINE overrides below refine the base L3+/RETIRES tags on the chord/decode
#     files into the THREE populations the instruction names — L4-SCORER (c, the LIVE
#     surviving scorer core the dormant decoder reuses), L4-DECODER (b, the DORMANT
#     ChordSliceDecoder), L4-RETIRES (a, the legacy competition tail + Gates A-L that
#     retire at engagement) — plus L4-MIXED (in-scope L4 content beside other-layer
#     types) and DEFERRED (verified NOT L4). DEEP_TAGS = (L4-SCORER, L4-DECODER,
#     L4-MIXED); L4-RETIRES gets a file-level interpretation-check note only (NO deep
#     rows); DEFERRED and non-chord files are out of scope. Artifacts under
#     tools/audit/l4/. Every tag re-verified at the code + call sites (a mis-tag is a
#     finding, not inherited) — see L4_REFINE.
def _selected_layer(argv):
    if "--layer" in argv:
        i = argv.index("--layer")
        if i + 1 < len(argv):
            return argv[i + 1]
    return "l1l2"

AUDIT_LAYER = _selected_layer(sys.argv)
if AUDIT_LAYER not in ("l1l2", "l3", "l4", "l5"):
    sys.stderr.write("unknown --layer %r (expected l1l2 | l3 | l4 | l5)\n" % AUDIT_LAYER)
    sys.exit(2)

# ── The instruments scope (l5 only): a SECOND enumeration root beside src/composing ─
# The measurement chain lives under tools/. The enumeration DOMAIN is mechanical and
# total: TOP-LEVEL tracked tools/*.{py,cpp,json} + tools/tests/*.py. Subtrees that are
# the audit's OWN artifacts or committed reference/fitted DATA (tools/audit/,
# tools/robust_stop/, tools/calibration_maps/, tools/reports/, tools/refresh_divergence_*/,
# tools/fonttools/, tools/jsdoc/, gitignored corpus dirs) are EXCLUDED — they are
# instrument OUTPUTS or unrelated build tooling, not instruments under audit. The
# exclusion is documented here so the boundary is auditable (nothing silently dropped).
# NOTE: git pathspec `*` spans `/`, so the depth filter is applied in Python, not the glob.
INSTRUMENT_SCOPE_EXTS = (".py", ".cpp", ".json")


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

if AUDIT_LAYER == "l1l2":
    DEEP_TAGS = ("L1", "L2")
elif AUDIT_LAYER == "l3":
    DEEP_TAGS = ("L3", "L3-MIXED")
elif AUDIT_LAYER == "l4":
    DEEP_TAGS = ("L4-SCORER", "L4-DECODER", "L4-MIXED")
else:  # l5
    # L5-DORMANT = the dormant-but-surviving resolver pipeline (deep, C++);
    # INSTRUMENT = the Python measurement chain (deep, Python);
    # INSTRUMENT-HARNESS = batch_analyze.cpp (deep, C++).
    # L5-RETIRES / DEFERRED / NON-INSTRUMENT / INSTRUMENT-MANIFEST / INSTRUMENT-TEST
    # get file-level rows only (see L5_REFINE + INSTRUMENT_RULES for the reasons).
    DEEP_TAGS = ("L5-DORMANT", "INSTRUMENT", "INSTRUMENT-HARNESS")

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


# ── L4 (chord) tag refinement (applied over the base TAG_RULES iff --layer l4) ─
# The base map coarsely tags the chord/decode files L3+ / RETIRES. THIS audit refines
# them into the THREE populations the instruction names — each RE-VERIFIED at the code
# with call sites traced (a mis-tag is a finding, not inherited):
#   L4-SCORER  — (c) the LIVE surviving scorer core + its live in-scope satellites: the
#                vertical oracle analyzeChord the dormant decoder REUSES, its stable
#                contract header, the shared symbol formatter, the shared utility
#                header, the live beam-1 commit-chain, the live sparse-quality
#                refinement. Deep-audited. Any open survive/retire OR layer-boundary
#                question is FLAGGED in the reason (a pass-1 finding).
#   L4-DECODER — (b) the DORMANT-but-surviving per-slice ChordSliceDecoder (the
#                engagement's clean target; runs only under --decode-chords). Deep.
#   L4-MIXED   — a file whose L4-in-scope content sits beside other-layer content; the
#                split is recorded per row in Task 2. Deep.
#   L4-RETIRES — (a) code that RETIRES at the decoder engagement (roadmap R1: the legacy
#                competition tail + Gates A-L). File-level interpretation-check note
#                only; NO deep rows.
#   DEFERRED   — verified NOT Layer 4 (belongs to another layer's audit); NOT deep.
# Ordered; FIRST match wins; exact repo-relative paths (forward slash). Authority:
# ARCHITECTURE.md §"Layer 4"/§4.1/§7; docs/scoring_model.md §"File layout after refactor
# #1"/§11; roadmap retirement map R1/R9 (docs/implementation_roadmap.md:138-145); the
# chordslicedecoder.h header (decoder REUSES analyzeChord: chordslicedecoder.cpp:453).
L4_REFINE = [
    # ---- (c) LIVE surviving scorer core + live in-scope satellites (deep) ----
    ("src/composing/analysis/chord/chordanalyzer.cpp", "L4-SCORER",
     "MIS-TAG (inherited RETIRES) — the LIVE surviving vertical scoring ORACLE (analyzeChord @regionanalyzer.cpp:987, buildChordResult/detectExtensions, TemplateDef/templates/score matrices, factory) that the DORMANT decoder REUSES (chordslicedecoder.cpp:453); only the competition (function/) + Gates A-L retire (R1); R9 file-SPLITS this file, does not delete it (pass-1 finding)"),
    ("src/composing/analysis/chord/chordanalyzer.h", "L4-SCORER",
     "L4 scorer CONTRACT surface (stable integration boundary): kTemplateCount/kTemplateIntervals, ChordIdentity/ChordAnalysisResult/RawCandidate, IChordAnalyzer/RuleBasedChordAnalyzer/factory; also declares PostScoringGateContext/PromotionTarget consumed by the retiring gates (split recorded in Task 2)"),
    ("src/composing/analysis/chord/chordsymbolformatter.cpp", "L4-SCORER",
     "LIVE shared chord-symbol formatter (formatSymbol/formatRomanNumeral/formatNashvilleNumber) — production notation render (notationcomposingbridge.cpp:490..); survives the engagement. FLAG: formatRomanNumeral is L5-flavored output on an L4 TU (boundary note)"),
    ("src/composing/analysis/chord/analysisutils.h", "L4-SCORER",
     "LIVE cross-cutting chord helper header (normalizePc/diatonicMaskFromFifths/collectionMask/ionianTonicPcFromFifths) reused by the surviving oracle+formatter; survives. FLAG: cross-cutting (also serves L3/L5)"),
    ("src/composing/analysis/decode/chordpathdecoder.h", "L4-SCORER",
     "LIVE beam-1 chord-path commit-chain re-expression (Stage 3.1, byte-identical; replaces advanceTemporalContext on the production region path). FLAG: retire-vs-survive at engagement is OPEN (Stage-3.2 wider-beam scaffolding vs legacy plumbing) — pass-1"),
    ("src/composing/analysis/region/sparsechordrefinement.h", "L4-SCORER",
     "LIVE L4 diatonic chord-QUALITY refinement surface on the region path (regionanalyzer.cpp:1003/1005; consumes the L3 key as a prior). FLAG: L4/L5 BOUNDARY — overwrites identity.quality (L4) from resolved-key (L5-flavored) post-commit; layer home OPEN, declare to Cowork (pass-1)"),
    ("src/composing/analysis/region/sparsechordrefinement.cpp", "L4-SCORER",
     "LIVE L4 diatonic chord-QUALITY refinement impl (refineSparseChordQualityFromKeyContext/applyTonicPriorToSparseChord/forceChordTrackQualityFromKeyContext). FLAG: L4/L5 boundary (see .h) — layer home OPEN"),
    # ---- (b) DORMANT-but-surviving decoder — the engagement's clean target (deep) ----
    ("src/composing/analysis/chord/chordslicedecoder.h", "L4-DECODER",
     "DORMANT per-slice chord-symbol decoder surface (ChordSliceDecoder + preferences/DTOs) — the Layer-4 rebuild target; runs analyzeChord over each L2 slice; NOT wired (batch_analyze --decode-chords diagnostic only)"),
    ("src/composing/analysis/chord/chordslicedecoder.cpp", "L4-DECODER",
     "DORMANT per-slice chord-symbol decoder impl (decideSlice/classifyMembership/applyCommitDecision/spellingPinnedRoot/computeConfidence/nameOpenQuestion + decode/redecodeRange/decodeSelection)"),
    # ---- L4-MIXED — L4-in-scope content beside other-layer types (deep, split recorded) ----
    ("src/composing/analysis/types/analysistypes.h", "L4-MIXED",
     "cross-layer types leaf — the L4 chord types are IN SCOPE (ChordAnalyzerPreferences, ChordAnalysisTone, ChordTemporalContext, DecodeQualityLevel, ChordQuality) beside L3/L5 types (KeyModeAnalyzerPreferences/PitchContext/KeySigMode) covered by the L3 audit; only the L4-type rows are dispositioned here — split recorded per row in Task 2"),
    # ---- (a) RETIRES at engagement — file-level interpretation-check note only (NO deep rows) ----
    ("src/composing/analysis/chord/postscoringgates.cpp", "L4-RETIRES",
     "RETIRES — literally roadmap R1 (Gates A-L / applyPostScoringGates; LIVE now @regionanalyzer.cpp:1000). #12 interpretation-check on deletion: Gate J (viio->V7), Gate L (Major-over-aug), Gate I (first-inv-Major-over-Minor), the enharmonic Maj-add6<->m7 flip/FM2, and the bias correction are the ONLY site of several key-function chord RESELECTIONS — L5 must consciously re-home or reject EACH before deletion"),
    ("src/composing/analysis/chord/chordpostpasses.cpp", "L4-RETIRES",
     "RETIRES — legacy competition late-promotion tail (applyIter8691Pedal: Iter-86 bass-b7 + Iter-91 bass-as-root promotions + two-pass pedal-point; LIVE now @regionanalyzer.cpp:999 but NOT reused by the dormant decoder). #12 interpretation-check on deletion: the pedal-point detection + bass-root late promotions are legacy-winner corrections the decoder must be confirmed to cover/reject before deletion"),
    # ---- DEFERRED — verified NOT Layer 4 (belongs to another layer's audit; NOT deep) ----
    ("src/composing/analysis/chord/chordvoicing.cpp", "DEFERRED",
     "MIS-IMPLIED-L4 — chord-tone/voicing utility (chordTonePitchClasses/closePositionVoicing) serving notation IMPLODE + display stabilization (arrangement concern, ARCHITECTURE §voicing), NOT chord decoding; no decode/competition caller — deferred to the arrangement/notation concern (pass-1 finding)"),
    ("src/composing/analysis/chord/chorddiagnose.cpp", "DEFERRED",
     "DIAGNOSTIC satellite (diagnoseChord replays analyzeChord+applyIter8691Pedal+applyPostScoringGates) reached only via batch_analyze --diagnose-measures; NOT production, NOT the decoder. FLAG: coupled to R1 (rewrites/retires WITH Gates A-L) — deferred to the instruments audit (pass-1)"),
    ("src/composing/analysis/vocabulary/harmonicvocabulary.h", "DEFERRED",
     "NOT L4 (inherited '(L4)' imprecise) — ARCHITECTURE §7 Harmonic Vocabulary, a queried reference catalog consumed by the L5 progression/function machinery (progressionrecognizer/functionresolver); DORMANT (no production consumer) — deferred to the L5-consumer/progression-schema audit (pass-1 finding)"),
    ("src/composing/analysis/vocabulary/harmonicvocabulary.cpp", "DEFERRED",
     "NOT L4 (see .h) — ARCHITECTURE §7 Harmonic Vocabulary impl; DORMANT L5-consumer catalog — deferred"),
    ("src/composing/analysis/voiceleading/textureclassifier.h", "DEFERRED",
     "NOT L4 (inherited '(L4/L5)' imprecise) — voice-leading AXIS 2 (orthogonal to the harmonic spine), VL-C texture classifier; DORMANT (no production consumer) — deferred to the voice-leading-axis audit"),
    ("src/composing/analysis/voiceleading/textureclassifier.cpp", "DEFERRED",
     "NOT L4 — voice-leading axis-2 VL-C impl; DORMANT — deferred to the voice-leading-axis audit"),
    ("src/composing/analysis/voiceleading/textureclassifierreference.h", "DEFERRED",
     "NOT L4 — voice-leading axis-2 generated reference set (VL-C centroids); deferred to the voice-leading-axis audit"),
    ("src/composing/analysis/voiceleading/voicelinearview.h", "DEFERRED",
     "NOT L4 — voice-leading axis-2 VL-A per-voice linear FACT view over the L1 note model; deferred to the voice-leading-axis audit"),
    ("src/composing/analysis/voiceleading/voicelinearview.cpp", "DEFERRED",
     "NOT L4 — voice-leading axis-2 VL-A impl; deferred to the voice-leading-axis audit"),
    ("src/composing/analysis/voiceleading/voiceleadingprofiles.h", "DEFERRED",
     "NOT L4 — voice-leading axis-2 VL-B motion/interval profiles; DORMANT — deferred to the voice-leading-axis audit"),
    ("src/composing/analysis/voiceleading/voiceleadingprofiles.cpp", "DEFERRED",
     "NOT L4 — voice-leading axis-2 VL-B impl; DORMANT — deferred to the voice-leading-axis audit"),
]


def refine_l4(path, tag, reason):
    """In --layer l4 mode, override the base tag for the chord/decode files into the
    three populations (a/b/c) + L4-MIXED + DEFERRED. Returns the (possibly refined)
    (tag, reason); base tag unchanged for files L4_REFINE omits."""
    for matcher, l4tag, l4reason in L4_REFINE:
        if path == matcher:
            return l4tag, l4reason
    return tag, reason


# ── L5 (function) tag refinement (applied over the base TAG_RULES iff --layer l5) ─
# The base map coarsely tags the function/, progression/, section/ files L3+ ("deferred
# to the L5 audit"). THIS audit refines them into the instruction's three populations —
# each RE-VERIFIED at the code with call sites traced (a mis-tag is a finding, not
# inherited):
#   L5-DORMANT — (b) the DORMANT-but-surviving resolver pipeline (Phase-5c, built +
#                unit-tested, NOT wired to production: no non-test .cpp/.h includes it;
#                its only non-test reference is the batch_analyze --decode diagnostic).
#                The engagement's clean target. Deep-audited.
#   L5-RETIRES — (a) LIVE-now-and-retiring function machinery on the roadmap retirement
#                map. File-level interpretation-check note only (NO deep rows), per the
#                L4-RETIRES precedent.
#   L5-MIXED   — a file whose L5-in-scope content sits beside another layer's (already
#                audited) content; the L5 part is a RETIRES note, the rest is elsewhere.
#                File-level note only.
#   DEFERRED   — verified NOT in L5's deep scope: already deep-audited by the L3 audit
#                (do not duplicate, #6), or belongs to the L6 audit.
# Ordered; FIRST match wins; exact repo-relative paths (forward slash). Authority:
# cowork_layer5_function_design.md (SIGNED) §1/§13; ARCHITECTURE.md §"Layer 5"/§"Layer 6";
# roadmap retirement map R1/R2/R7 (docs/implementation_roadmap.md:138-145); the file
# headers themselves (harmonicfunctionlayer.h:25 "Competition pipeline"); call-site trace
# (detectCadences reached from src/notation/internal/notationcomposingbridge.cpp — LIVE).
L5_REFINE = [
    # ---- (a) RETIRES — legacy competition pipeline mis-named "function" (R1/R7) ----
    ("src/composing/analysis/function/harmonicfunctionlayer.h", "L5-RETIRES",
     "MIS-TAG (inherited 'function layer (L5)') — this is the LEGACY L4 CHORD-COMPETITION pipeline "
     "(harmonicfunctionlayer.h:25 'Competition pipeline — the SINGLE owner of winner selection'; "
     "applyHarmonicFunction runs the per-bass competition + winner selection, LIVE via chordanalyzer/"
     "regionanalyzer), NOT the Layer-5 function machinery; its functional labeling is 'E4 (planned)'. "
     "Retires R1 (legacy competition) + R7 (rename). #12-check on deletion: it is the SOLE owner of "
     "winner selection + progression-signal application (pass-1 finding)"),
    ("src/composing/analysis/function/harmonicfunctionlayer.cpp", "L5-RETIRES",
     "MIS-TAG (see .h) — legacy L4 competition pipeline impl (applyHarmonicFunction winner selection); "
     "retires R1/R7; #12-check the winner-selection + progression-signal ownership on deletion"),
    ("src/composing/analysis/section/sectioncadencedetection.cpp", "L5-RETIRES",
     "LIVE-and-retiring — the legacy KEY-DEPENDENT (circular) cadence + pivot detection "
     "(detectCadences/detectPivotChords), reached from the notation bridge (notationcomposingbridge.cpp) "
     "= production; roadmap R2 (legacy circular cadence detector) + the L6 rebuild target. The dormant "
     "key-agnostic replacement is function/functioncadence. #12-check on deletion: the cadence-type + "
     "pivot interpretations L5/L6 must consciously re-home (pass-1)"),
    # ---- (a) MIXED — L3-audited file whose L5 cadence/pivot part is LIVE-and-retiring ----
    ("src/composing/analysis/section/sectionanalyzer.h", "L5-MIXED",
     "L3-audited (L3-MIXED) — its L5 content (detectCadences/detectPivotChords surface, LIVE via the "
     "notation bridge) is the R2 legacy circular detector; file-level RETIRES note only, deep rows NOT "
     "re-generated (the L3 audit already inventoried this file — #6 no-duplication)"),
    ("src/composing/analysis/section/sectionanalyzer.cpp", "L5-MIXED",
     "L3-audited (L3-MIXED) — its L5 cadence/pivot labeling (LIVE, R2-retiring) noted at file level; "
     "deep rows NOT re-generated (#6; the L3 inventory holds this file's rows)"),
    # ---- (b) DORMANT-but-surviving resolver pipeline — the engagement target (deep) ----
    ("src/composing/analysis/function/forwardoverride.h", "L5-DORMANT",
     "DORMANT §8/§9-D7 confidence-weighted forward-override mechanism surface (the ONE reusable "
     "override the resolver + modulation recompute reuse); not wired"),
    ("src/composing/analysis/function/forwardoverride.cpp", "L5-DORMANT",
     "DORMANT forward-override impl (localized/forward/convergence-bounded recompute; one-pass closure)"),
    ("src/composing/analysis/function/functioncadence.h", "L5-DORMANT",
     "DORMANT §5.2 key-agnostic event-pair cadence DETECTOR surface (replaces the retiring "
     "sectioncadencedetection); not wired"),
    ("src/composing/analysis/function/functioncadence.cpp", "L5-DORMANT",
     "DORMANT §5.2 cadence detector impl (cadential-6/4 collapse, family gate, phrase gate, tonic-vote)"),
    ("src/composing/analysis/function/functionmodulation.h", "L5-DORMANT",
     "DORMANT §5.3/§5.4 tonicization-vs-modulation + cadence-confirmed modulation recompute surface "
     "(reuses the L3-audited localmodulationdetector substrate); not wired"),
    ("src/composing/analysis/function/functionmodulation.cpp", "L5-DORMANT",
     "DORMANT §5.3/§5.4 impl (persistence hysteresis over committed spans; §8 case-4 channel #1)"),
    ("src/composing/analysis/function/functionoutput.h", "L5-DORMANT",
     "DORMANT §7 output-assembly surface (Roman numeral + cadence + local-key markers + open marks); not wired"),
    ("src/composing/analysis/function/functionoutput.cpp", "L5-DORMANT",
     "DORMANT §7 output-assembly impl (additive over the L4 result; verbatim carried-identity emit)"),
    ("src/composing/analysis/function/functionprogression.h", "L5-DORMANT",
     "DORMANT §5.0 progression MODEL surface — the GRAMMAR owner isLicensedProgression (D5); not wired"),
    ("src/composing/analysis/function/functionprogression.cpp", "L5-DORMANT",
     "DORMANT §5.0 progression impl (licensed-motion test; §15-12 grammar-completion is spec-ahead-of-code)"),
    ("src/composing/analysis/function/functionrelationallabel.h", "L5-DORMANT",
     "DORMANT §5.6 relational labels (aug6/Neapolitan/applied/mixture precedence) + unified tonicization "
     "emitter surface; not wired"),
    ("src/composing/analysis/function/functionrelationallabel.cpp", "L5-DORMANT",
     "DORMANT §5.6 relational-label impl (chromaticism trigger + false-positive guard; V/iv over-trigger is inference-deferred)"),
    ("src/composing/analysis/function/functionresolver.h", "L5-DORMANT",
     "DORMANT §5.5 RESOLVER surface (select-among-carried-readings by ambiguity kind) + §5.5/§10 "
     "fine-grain override (§8 channel #2); not wired"),
    ("src/composing/analysis/function/functionresolver.cpp", "L5-DORMANT",
     "DORMANT §5.5 resolver impl (six ambiguity kinds; verbatim carried-identity selection; soft bass prior)"),
    ("src/composing/analysis/function/functionromannumeral.h", "L5-DORMANT",
     "DORMANT §5.1 base Roman-numeral derivation surface (degree/quality/inversion/chromatic alteration); not wired"),
    ("src/composing/analysis/function/functionromannumeral.cpp", "L5-DORMANT",
     "DORMANT §5.1 base Roman-numeral derivation impl (deterministic reading from key + committed chord)"),
    ("src/composing/analysis/function/tonicizationlabeler.h", "L5-DORMANT",
     "DORMANT applied-chord labeler (§13 the dormant tonicizationlabeler; Stage-6-tonic-i narrow slice; "
     "the reused labeler §5.6 references); not wired"),
    ("src/composing/analysis/function/tonicizationlabeler.cpp", "L5-DORMANT",
     "DORMANT applied-chord labeler impl (secondary-dominant / applied-leading-tone recognition)"),
    ("src/composing/analysis/progression/progressionrecognizer.h", "L5-DORMANT",
     "DORMANT L5-consumer progression-schema recognizer surface (reads the Harmonic Vocabulary catalog; "
     "one-way consistency test with the D5 grammar); batch_analyze --diagnostic only, no production consumer"),
    ("src/composing/analysis/progression/progressionrecognizer.cpp", "L5-DORMANT",
     "DORMANT progression-schema recognizer impl (multi-chord pattern/substitution recognition over the committed progression)"),
    # ---- DEFERRED — already deep-audited elsewhere, or another layer's audit (NOT deep here) ----
    ("src/composing/analysis/section/localmodulationdetector.h", "DEFERRED",
     "ALREADY L3-AUDITED (L3 file table: 'L3 key-evidence: local-modulation detector') — it is ALSO the "
     "dormant modulation-span substrate the L5 functionmodulation reuses (§13); the L5 SEAM (what "
     "functionmodulation reads from it) is audited via functionmodulation's rows, the file internals NOT "
     "re-audited here (#6 no-duplication)"),
    ("src/composing/analysis/section/localmodulationdetector.cpp", "DEFERRED",
     "ALREADY L3-AUDITED — L5-reused substrate; seam checked via functionmodulation (#6)"),
    ("src/composing/analysis/grouping/groupinglayer.h", "DEFERRED",
     "Layer 6 (grouping) — the design-only rebuild of the live cadence/pivot/KeyArea machinery; deferred to the L6 audit"),
    ("src/composing/analysis/grouping/groupinglayer.cpp", "DEFERRED",
     "Layer 6 (grouping) — deferred to the L6 audit"),
]


def refine_l5_source(path, tag, reason):
    """In --layer l5 mode, override the base tag for the src/composing function/,
    progression/, section/, grouping/ files. Returns the (possibly refined)
    (tag, reason); base tag unchanged for files L5_REFINE omits."""
    for matcher, l5tag, l5reason in L5_REFINE:
        if path == matcher:
            return l5tag, l5reason
    return tag, reason


# ── The INSTRUMENTS enumeration (l5 only; over the tools/ scope) ──────────────
# The measurement chain the project's regression stops, corpus generation, ground-truth
# parsing, and fitting depend on (guiding principle 19: what does each instrument measure,
# what validates it, what would silently break it). The INSTRUMENT set is the IMPORT
# CLOSURE of the named entry points (verified: `grep '^import' + import-chase`), plus
# batch_analyze (the shared harness) and param_manifest.json (the fit manifest). Every
# other tracked file in the INSTRUMENT_SCOPE_GLOBS domain is tagged NON-INSTRUMENT (a
# one-off diagnostic / injection helper / registry / config) with a reason, so the domain
# is TOTAL (P1) and the instrument boundary is auditable. Ordered; FIRST match wins.
INSTRUMENT_RULES = [
    # ---- the deep-audited measurement chain (Python) ----
    ("tools/compare_analyses.py", "INSTRUMENT",
     "base COMPARISON module — three-level batch_analyze-vs-music21 region compare; imported by ~all "
     "the stops. Reads .ours.json + .music21.json; writes nothing (library)"),
    ("tools/dcml_parser.py", "INSTRUMENT",
     "the GROUND-TRUTH PARSER — DCML TSV + RomanText → WiR roots (the corrected-parser, 2026-06-13). "
     "Reads .harmonies.tsv / DCML; writes nothing (library)"),
    ("tools/compare_rn.py", "INSTRUMENT",
     "the robust-unit ROMAN-NUMERAL grid compare (grid_score_regions; a8 self-validates variant-(b) "
     "decomposition byte-identical to this). Reads .ours.json + DCML GT"),
    ("tools/characterise_bir_false.py", "INSTRUMENT",
     "the BATCH-STOP diagnostic + validate_corpus_dir (the corpus-integrity guard the a8 instrument "
     "imports). Reads a per-preset corpus dir + its manifest; writes stdout characterization"),
    ("tools/a8_rebaseline_measure.py", "INSTRUMENT",
     "the ROBUST-STOP measurement instrument (variant-(b) root-fail enumerations; self-validates "
     "grid==oracle per piece). Reads the corpus; writes tools/robust_stop/<preset>/* + summary/manifest"),
    ("tools/robust_stop_diff.py", "INSTRUMENT",
     "the ROBUST-STOP GATE (exit 0 iff every preset's class-(b) duration non-increases vs the committed "
     "reference). Reads a candidate a8 dir + tools/robust_stop/ reference; writes the explained diff"),
    ("tools/run_bach_preset.py", "INSTRUMENT",
     "the CORPUS GENERATOR/VALIDATOR — clean-slates + regenerates a per-preset dir, stamps "
     "corpus_manifest.json, exits nonzero unless complete. Runs batch_analyze; writes .ours.json + manifest"),
    ("tools/analyze_inversion_errors.py", "INSTRUMENT",
     "the SECONDARY bassIsRoot metric (three-way music21_dcml_agree split). Reads a validated per-preset dir"),
    ("tools/music21_batch.py", "INSTRUMENT",
     "the music21 GROUND-TRUTH GENERATOR — exports the corpus to MusicXML + .music21.json (v9.9.1 pin). "
     "Reads music21 corpus; writes tools/corpus/*.xml + *.music21.json"),
    ("tools/oracle_root_metric.py", "INSTRUMENT",
     "the STANDING per-event tiered ORACLE-ROOT metric (reuses compare_analyses + dcml_parser + "
     "validate_corpus_dir). Reads a validated per-preset dir + DCML GT"),
    ("tools/calibration_fit.py", "INSTRUMENT",
     "the FITTING instrument — Stage-5 Class-M→Class-P reliability maps (isotonic/logistic). Reads the "
     "corpus + c1 substrate; writes tools/calibration_maps/*.json"),
    ("tools/c1_reliability.py", "INSTRUMENT",
     "the C1 reliability instrumentation primitives (cell-join + squash + PRESETS) reused by the fitter"),
    ("tools/stage5_fit_driver.py", "INSTRUMENT",
     "the Stage-5 FITTER HARNESS (fitter design §4.3/§7). Reads DCML GT; drives the calibration fit"),
    # ---- the shared harness (C++) ----
    ("tools/batch_analyze.cpp", "INSTRUMENT-HARNESS",
     "the SHARED HARNESS — the standalone score→analysis driver every corpus run + diagnostic path uses "
     "(--decode-chords, --section-level, --diagnose-measures, --dump-regions). Reads a score; writes .ours.json"),
    # ---- the fit manifest (JSON; file-level, establishment-checked in Task 2) ----
    ("tools/param_manifest.json", "INSTRUMENT-MANIFEST",
     "the FIT MANIFEST — the param provenance ledger the constants ESTABLISHED/UNFIT/DEAD check reads "
     "(CLAUDE.md). File-level row; its coverage of L5 + scorer constants is a Task-2 establishment check"),
]

# NON-INSTRUMENT sub-classification (reasons for the file-table; first prefix match wins).
# Applied to any INSTRUMENT_SCOPE_GLOBS file NOT matched by INSTRUMENT_RULES, so the tools/
# domain is totally tagged. These get file-level rows only.
NONINSTRUMENT_PREFIX_REASONS = [
    ("tools/tests/", "INSTRUMENT-TEST",
     "regression test for a measurement instrument (dcml_parser / metric primitives / oracle_root_metric "
     "/ snapshot sources) — the establishment cross-check; file-level"),
    ("tools/diag_", "NON-INSTRUMENT", "one-off diagnostic script (per-iteration/gate triage) — not the standing measurement chain"),
    ("tools/iter", "NON-INSTRUMENT", "one-off per-iteration diagnostic script — not the standing measurement chain"),
    ("tools/analyze_", "NON-INSTRUMENT", "one-off analysis/triage script — not the standing measurement chain"),
    ("tools/check_", "NON-INSTRUMENT", "one-off score/tick check script — not the standing measurement chain"),
    ("tools/diff_", "NON-INSTRUMENT", "one-off classification-diff script — not the standing measurement chain"),
    ("tools/compare_", "NON-INSTRUMENT", "corpus/oracle comparison helper — not in the core regression-stop import closure (own audit if promoted)"),
    ("tools/cc_", "NON-INSTRUMENT", "a specific measurement-run driver (baseline / sweep / full-spine / step-M) — a run, not the standing chain"),
    ("tools/decode_", "NON-INSTRUMENT", "dormant-decoder corpus run driver — a run, not the standing chain"),
    ("tools/run_", "NON-INSTRUMENT", "per-corpus validation runner (composer-specific) — wraps the chain; not itself the stop"),
    ("tools/inject_", "NON-INSTRUMENT", "ground-truth-injection helper (writes RN into scores for QA) — not a measurement instrument"),
    ("tools/pdmx_", "NON-INSTRUMENT", "PDMX dataset candidate/spot-check helper — corpus acquisition, not measurement"),
    ("tools/", "NON-INSTRUMENT", "tools/ script/registry/config NOT in the measurement-chain import closure — file-level, out of instrument deep scope"),
]


def resolve_instrument_tag(path):
    for matcher, tag, reason in INSTRUMENT_RULES:
        if path == matcher:
            return tag, reason
    for prefix, tag, reason in NONINSTRUMENT_PREFIX_REASONS:
        if path.startswith(prefix):
            return tag, reason
    return "NON-INSTRUMENT", "tools/ file — out of instrument deep scope (file-level)"

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


def list_instrument_scope():
    """The tools/ instruments enumeration domain (l5 only): TOP-LEVEL tracked
    tools/*.{py,cpp,json} + tools/tests/*.py. Mechanical + total over that domain (P1).
    Depth is filtered in Python because a git pathspec `*` spans `/`."""
    out = sh(["git", "ls-files", "tools/"])
    files = []
    for l in out.splitlines():
        p = l.replace("\\", "/").strip()
        if not p:
            continue
        rest = p[len("tools/"):]
        ext = os.path.splitext(p)[1]
        top_level = ("/" not in rest) and ext in INSTRUMENT_SCOPE_EXTS
        tests_py = rest.startswith("tests/") and rest.count("/") == 1 and ext == ".py"
        if top_level or tests_py:
            files.append(p)
    return sorted(set(files))


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


# ── Python extraction (l5 instruments): an `ast` scan, parallel to the C++ scan ──
# Row schema shared with the C++ path: functions, literals (trivial 0/1 excluded),
# branches, fields (class-body attributes = the Python analogue of visible struct
# fields), crosslayer (internal-module imports = the instrument's dependency edges),
# and — instrument-specific, per the instruction — an IO list (open()/json.load/
# json.dump/glob/read_text/write_text calls = what each instrument reads and writes).
# decls is C++-only (empty for Python). ESTABLISHED (#19): Python is PARSED (ast), not
# regex-scanned, so the extraction is exact, not heuristic.
import ast as _ast

_PY_STDLIB_MODS = {
    "os", "sys", "json", "re", "csv", "glob", "subprocess", "argparse", "collections",
    "math", "pathlib", "typing", "itertools", "functools", "dataclasses", "io", "shutil",
    "hashlib", "time", "random", "copy", "xml", "statistics", "struct", "tempfile",
    "warnings", "abc", "enum", "fractions", "datetime", "traceback", "concurrent",
    "multiprocessing", "__future__", "numpy", "np", "sklearn", "music21", "unittest",
    "pytest", "textwrap", "operator", "bisect", "heapq", "decimal", "contextlib",
}
_PY_IO_CALLS = {"open", "load", "loads", "dump", "dumps", "glob", "iglob",
                "read_text", "write_text", "read_bytes", "write_bytes",
                "read_csv", "to_csv", "makedirs", "mkdir", "walk", "listdir"}


def _py_enclosing(func_spans, ln):
    best = None
    for name, sl, el in func_spans:
        if sl <= ln <= el:
            if best is None or (el - sl) < (best[2] - best[1]):
                best = (name, sl, el)
    return best[0] if best else "<module-scope>"


def extract_python(orig, path):
    """ast scan of a Python instrument. Returns (funcs, lits, branches, fields, cross, io)."""
    funcs, lits, branches, fields, cross, io = [], [], [], [], [], []
    orig_lines = orig.split("\n")
    try:
        tree = _ast.parse(orig)
    except SyntaxError as e:
        sys.stderr.write("  PY-PARSE-FAIL %s: %s\n" % (path, e))
        return funcs, lits, branches, fields, cross, io

    func_spans = []
    for node in _ast.walk(tree):
        if isinstance(node, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
            el = getattr(node, "end_lineno", node.lineno)
            func_spans.append((node.name, node.lineno, el))
            funcs.append({"name": node.name, "start_line": node.lineno, "end_line": el})

    def ctx(ln):
        return orig_lines[ln - 1].strip()[:160] if 0 < ln <= len(orig_lines) else ""

    # class-body attributes (visible fields) — track the enclosing class per node
    for node in _ast.walk(tree):
        if isinstance(node, _ast.ClassDef):
            for stmt in node.body:
                if isinstance(stmt, _ast.AnnAssign) and isinstance(stmt.target, _ast.Name):
                    fields.append({"line": stmt.lineno, "type_owner": node.name,
                                   "field_type": _ast.unparse(stmt.annotation)[:60]
                                   if hasattr(_ast, "unparse") else "",
                                   "name": stmt.target.id, "context": ctx(stmt.lineno)})
                elif isinstance(stmt, _ast.Assign):
                    for t in stmt.targets:
                        if isinstance(t, _ast.Name):
                            fields.append({"line": stmt.lineno, "type_owner": node.name,
                                           "field_type": "", "name": t.id,
                                           "context": ctx(stmt.lineno)})

    for node in _ast.walk(tree):
        # literals (exclude trivial 0/1 and booleans)
        if isinstance(node, _ast.Constant) and isinstance(node.value, (int, float)) \
                and not isinstance(node.value, bool):
            if node.value in (0, 1):
                continue
            ln = getattr(node, "lineno", 0)
            lits.append({"line": ln, "value": repr(node.value),
                         "func": _py_enclosing(func_spans, ln), "context": ctx(ln)})
        # branches
        kind = None
        if isinstance(node, _ast.If):
            kind = "if"
        elif isinstance(node, (_ast.For, _ast.AsyncFor)):
            kind = "for"
        elif isinstance(node, _ast.While):
            kind = "while"
        elif isinstance(node, _ast.IfExp):
            kind = "ternary"
        elif isinstance(node, _ast.Try):
            kind = "try"
        elif hasattr(_ast, "match_case") and isinstance(node, _ast.match_case):
            kind = "case"
        if kind:
            ln = getattr(node, "lineno", 0)
            branches.append({"line": ln, "kind": kind,
                             "func": _py_enclosing(func_spans, ln), "context": ctx(ln)})
        # internal-module imports (dependency edges = the instrument's crosslayer)
        if isinstance(node, _ast.Import):
            for a in node.names:
                top = a.name.split(".")[0]
                if top not in _PY_STDLIB_MODS:
                    cross.append({"line": node.lineno, "include": a.name,
                                  "resolved": "tools/%s.py" % top, "target_area": "instrument"})
        elif isinstance(node, _ast.ImportFrom):
            top = (node.module or "").split(".")[0]
            if top and top not in _PY_STDLIB_MODS:
                cross.append({"line": node.lineno, "include": node.module,
                              "resolved": "tools/%s.py" % top, "target_area": "instrument"})
        # file IO (reads/writes — the instrument's surface)
        if isinstance(node, _ast.Call):
            fname = None
            if isinstance(node.func, _ast.Name):
                fname = node.func.id
            elif isinstance(node.func, _ast.Attribute):
                fname = node.func.attr
            if fname in _PY_IO_CALLS:
                ln = getattr(node, "lineno", 0)
                io.append({"line": ln, "call": fname,
                           "func": _py_enclosing(func_spans, ln), "context": ctx(ln)})
    return funcs, lits, branches, fields, cross, io


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
        elif AUDIT_LAYER == "l4":
            tag, reason = refine_l4(p, tag, reason)
        elif AUDIT_LAYER == "l5":
            tag, reason = refine_l5_source(p, tag, reason)
        file_rows.append({"file": p, "tag": tag or "UNTAGGED", "reason": reason or ""})
    # l5: the SECOND scope root — the tools/ instruments domain (mechanically total)
    if AUDIT_LAYER == "l5":
        for p in list_instrument_scope():
            tag, reason = resolve_instrument_tag(p)
            file_rows.append({"file": p, "tag": tag, "reason": reason})
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
    all_io = []   # l5-instruments: what each Python instrument reads/writes
    per_file = {}
    for p in deep:
        with open(os.path.join(REPO_ROOT, p), encoding="utf-8") as f:
            orig = f.read()
        orig_lines = orig.split("\n")
        io = []
        if p.endswith(".py"):
            # Python instrument — exact ast scan (no C++ blanking/brace walk)
            funcs, lits, branches, fields, cross, io = extract_python(orig, p)
            decls = []
        else:
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
        for r in io:
            all_io.append({"file": p, **r})
        per_file[p] = {"functions": len(funcs), "literals": len(lits),
                       "branches": len(branches), "fields": len(fields),
                       "decls": len(decls), "crosslayer": len(cross), "io": len(io)}

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
    if AUDIT_LAYER == "l5":
        write_csv(os.path.join(OUT_DIR, PREFIX + "_io.csv"), all_io,
                  ["file", "line", "call", "func", "context"])

    inventory = {
        "file_table": file_rows,
        "functions": all_funcs, "literals": all_lits, "branches": all_branches,
        "fields": all_fields, "decls": all_decls, "crosslayer": all_cross,
    }
    if AUDIT_LAYER == "l5":
        inventory["io"] = all_io
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
        "audit": {
            "l1l2": "EG-7 L1/L2 certification, PASS 1 (blind enumerative)",
            "l3": "EG-7 Layer-3 (key/mode) certification, PASS 1 (blind enumerative)",
            "l4": "EG-7 Layer-4 (chord) certification, PASS 1 (blind enumerative)",
            "l5": "EG-7 Layer-5 (function) + instruments certification, PASS 1 (blind enumerative)",
        }[AUDIT_LAYER],
        "audit_layer": AUDIT_LAYER,
        "head_commit": head,
        "script_blob_sha": script_sha,
        "corpus_hash": CORPUS_HASH,
        "scope_dir": SCOPE_DIR if AUDIT_LAYER != "l5" else (SCOPE_DIR + " + tools/ (instruments)"),
        # extraction_method + the io total are l5-conditional so prior-layer manifests
        # regenerate byte-identically (only the self-referential script_blob_sha evolves).
        "extraction_method": (
            "regex/brace-depth scan over comment/string/preproc-blanked C++; heuristic, over-capture-biased; see module docstring"
            if AUDIT_LAYER != "l5" else
            "C++ (.cpp/.h): regex/brace-depth scan over comment/string/preproc-blanked source (heuristic, over-capture-biased). Python instruments (.py): exact `ast` scan (functions/literals/branches/class-fields/internal-imports/file-IO). See module docstring."
        ),
        "totals": {
            "tracked_files": len(files) + (len(list_instrument_scope()) if AUDIT_LAYER == "l5" else 0),
            "file_table_rows": len(file_rows),
            "tag_counts": tag_counts,
            "deep_audited_files": len(deep),
            "functions": len(all_funcs),
            "literals": len(all_lits),
            "branches": len(all_branches),
            "fields": len(all_fields),
            "decls": len(all_decls),
            "crosslayer": len(all_cross),
            **({"io": len(all_io)} if AUDIT_LAYER == "l5" else {}),
        },
        "deep_audited_file_list": deep,
    }
    with open(os.path.join(OUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)

    n_tracked = len(files) + (len(list_instrument_scope()) if AUDIT_LAYER == "l5" else 0)
    print("gen_inventory OK — %d tracked files in scope, %d deep-audited (%s)" %
          (n_tracked, len(deep), "/".join(DEEP_TAGS)))
    print("  tag counts:", tag_counts)
    print("  rows: funcs=%d lits=%d branches=%d fields=%d decls=%d cross=%d io=%d" %
          (len(all_funcs), len(all_lits), len(all_branches), len(all_fields),
           len(all_decls), len(all_cross), len(all_io)))
    if self_check:
        print("\n-- per-file extraction counts (establish-the-instrument cross-check) --")
        for p in deep:
            c = per_file[p]
            print("  %-62s f=%2d lit=%3d br=%3d fld=%2d dcl=%2d x=%2d io=%2d" %
                  (p, c["functions"], c["literals"], c["branches"], c["fields"],
                   c["decls"], c["crosslayer"], c.get("io", 0)))


if __name__ == "__main__":
    main()
