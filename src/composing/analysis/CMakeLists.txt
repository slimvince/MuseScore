# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

muse_create_module(composing_analysis NO_QT)

target_sources(composing_analysis PRIVATE
    # chord/ — chord analysis, formatting, voicing
    ${CMAKE_CURRENT_LIST_DIR}/chord/analysisutils.h
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordanalyzer.h
    # Refactor #1 — single-responsibility layer TUs split out of chordanalyzer.cpp
    # (byte-identical pure code movement). See cc_refactor1_split_design_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordsymbolformatter.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordvoicing.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chorddiagnose.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordpostpasses.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/postscoringgates.cpp
    # LAYER 4 (Increment A) — the per-slice CHORD-SYMBOL decoder: runs the existing
    # chord scorer over each Layer-2 slice's window and reads the complete candidate
    # cube it surfaces (the L3 pattern), producing one chord + ranked alternatives +
    # confidence + uncertain per slice. ISOLATED this increment: built + unit-tested
    # + graded against the held-out chord GT, NOT wired into the live pipeline —
    # production output byte-identical; it runs only under batch_analyze
    # --decode-chords. Membership / spelling-pin / new types are later increments.
    # See cowork_layer4_chordsymbol_design.md + cc_layer4_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordslicedecoder.h
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordslicedecoder.cpp

    # function/ — Phase E harmonic function layer (post-analysis pass between
    # analyzeChord() output and the final chord label). E1 is a pass-through
    # shell; E2/E3/E4 migrate progression signals, post-scoring gates, and
    # cadence detection out of chordanalyzer.cpp. See docs/scoring_model.md §10.
    ${CMAKE_CURRENT_LIST_DIR}/function/harmonicfunctionlayer.h
    ${CMAKE_CURRENT_LIST_DIR}/function/harmonicfunctionlayer.cpp

    # tonicizationlabeler — the functional layer's narrow first slice (Stage
    # 6-tonic-i; docs/stage6_functional_layer_design.md §3): a secondary-dominant
    # / applied-leading-tone labeling pass over the decoded chord+key path,
    # distinct from harmonicfunctionlayer (the chord-competition layer). Built +
    # MEASURED only; it PRODUCES a label and does NOT mutate chord/key or feed the
    # production RN output (wiring is 6-tonic-ii).
    ${CMAKE_CURRENT_LIST_DIR}/function/tonicizationlabeler.h
    ${CMAKE_CURRENT_LIST_DIR}/function/tonicizationlabeler.cpp

    # decode/ — chord-path decoder (Stage 3.1). Beam-1 re-expression of the greedy
    # left-to-right commit chain that analyzeRegions() threads by hand; lands behind
    # the quality-level knob with beam-1 (level 0) as the byte-identical default.
    # Header-only at 3.1. See docs/decoder_design.md and docs/scoring_model.md §11.
    ${CMAKE_CURRENT_LIST_DIR}/decode/chordpathdecoder.h

    # key/ — key and mode analysis
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeanalyzer.h
    # Refactor — display formatters lifted out of keymodeanalyzer.cpp
    # (byte-identical pure code movement): keyModeTonicName / keyModeSuffix.
    # Both are header-declared (external linkage) and depend only on the
    # KeySigMode enum — no coupling to the anon-ns MODES/scorer cluster, which
    # stays in keymodeanalyzer.cpp. Declarations stay in the unchanged
    # keymodeanalyzer.h. See cc_refactor_keymodeanalyzer_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeformatting.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.h
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.h
    # LAYER 3 — the key/mode SEQUENCE decoder (dedicated key-path Viterbi over the
    # Layer-2 slices; emission = KeyModeAnalyzer through the Layer-1 indexed query).
    # WIRED into the live pipeline (regionanalyzer.cpp:581): the whole-score decode
    # replaces the per-region key argmax at the Pass-1 seam. Still also runs as a
    # graded diagnostic under batch_analyze --decode-keymode. See
    # cowork_layer3_keymode_design.md + cc_layer3_decoder_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodesequence.h
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodesequence.cpp

    # section/ — unified section-level analysis: the analyzeSection() entry
    # point, key/mode stabilization, and cadence / pivot detection. Moved here
    # from notation/internal/notationcomposingbridgehelpers.cpp in Stage 2.1
    # (Phase 4c — Dependency Rule §3.3; docs/implementation_roadmap.md Stage 2.1).
    ${CMAKE_CURRENT_LIST_DIR}/section/sectionanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/section/sectionanalyzer.cpp
    # Refactor — cadence/pivot detection lifted out of sectionanalyzer.cpp
    # (byte-identical pure code movement): detectCadences / detectPivotChords /
    # hasAssertiveKeyConfidence — independent of analyzeSection, driven by the
    # notation bridge. Declarations stay in the unchanged sectionanalyzer.h.
    ${CMAKE_CURRENT_LIST_DIR}/section/sectioncadencedetection.cpp
    # cadencekeyanchor — key-agnostic authentic-cadence → global tonic anchor
    # (Stage 4c-i; docs/stage4c_cadence_key_design.md §2). Built + measured only;
    # not yet wired into key scoring (that is 4c-ii).
    ${CMAKE_CURRENT_LIST_DIR}/section/cadencekeyanchor.h
    ${CMAKE_CURRENT_LIST_DIR}/section/cadencekeyanchor.cpp
    # localmodulationdetector — key-agnostic local-modulation detector (Stage
    # 4d-i; docs/stage4d_local_modulation_design.md §2): commits a candidate
    # local-key span when it is ESTABLISHED (sustained consistent run) AND
    # CONFIRMED (a V→I cadence inside it), consuming ONLY the key-agnostic cadence
    # instrument + raw region structure (no resolved key / KeyArea — the
    # no-circularity rule, design §3). Built + MEASURED only; not wired (4d-ii).
    ${CMAKE_CURRENT_LIST_DIR}/section/localmodulationdetector.h
    ${CMAKE_CURRENT_LIST_DIR}/section/localmodulationdetector.cpp
    # jointkeydecision — the scoped constrained-joint KEY decision (J-key-i;
    # docs/scoped_joint_design.md §6, the key-axis-first build): hard-fifths prune +
    # soft re-rank (cadence anchor / modulation / bass-is-root / declared-mode hint
    # / global key-path, all SOFT) + a scoped joint on the coupled core. Emits a
    # soft-only AND a soft+joint decision per region (the attribution toggle).
    # Consumes ONLY key-agnostic + local-candidate evidence (the production resolved
    # key is an echoed reference, never read). WIRED into the production resolver via
    # applyJointKeyWiring (J-key-iii, regionanalyzer.cpp:1369) but gated on
    # jointKeyWiringEnabled() (default OFF) — so production output is byte-identical by
    # default; also invoked from tools/batch_analyze --dump-joint-key.
    ${CMAKE_CURRENT_LIST_DIR}/section/jointkeydecision.h
    ${CMAKE_CURRENT_LIST_DIR}/section/jointkeydecision.cpp

    # region/ — harmonic region types and the shared analyzeRegions orchestrator.
    # Phase 4 of the duplication remediation (docs/duplication_audit.md §§2.14, 5.4)
    # moved the per-region pipeline body out of the notation bridge and
    # tools/batch_analyze.cpp into this module.
    ${CMAKE_CURRENT_LIST_DIR}/region/harmonicrhythm.h
    ${CMAKE_CURRENT_LIST_DIR}/region/regionanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/region/regionanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/region/sparsechordrefinement.h
    ${CMAKE_CURRENT_LIST_DIR}/region/sparsechordrefinement.cpp

    # harmony/ — region-level harmonic segmentation (greedy-expand, Iter 67)
    ${CMAKE_CURRENT_LIST_DIR}/harmony/harmonicsegmenter.h
    ${CMAKE_CURRENT_LIST_DIR}/harmony/harmonicsegmenter.cpp

    # scoreharvest/ — shared score-walking helpers used by both the notation
    # bridge and tools/batch_analyze.cpp. See docs/duplication_audit.md §5.8.
    ${CMAKE_CURRENT_LIST_DIR}/scoreharvest/metricweights.h
    ${CMAKE_CURRENT_LIST_DIR}/scoreharvest/metricweights.cpp

    # notemodel/ — LAYER 1: the lossless, annotated, tie-resolved note model
    # (the single source of truth for "what sounds"). Read once per score,
    # queryable by tick range via true-span overlap (no horizon). The
    # engravingbridge tone views derive over it. See
    # cowork_layer1_note_model_design.md + cc_layer1_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/notemodel/note_model.h
    ${CMAKE_CURRENT_LIST_DIR}/notemodel/note_model.cpp

    # engravingbridge/ — single source of truth for the score-walking helpers
    # shared by the notation bridge and tools/batch_analyze.cpp. Replaces the
    # Step-3 using-declaration plumbing in batch_analyze.cpp. See
    # docs/duplication_audit.md §§2.1-2.13 and §5.1.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontonecollector.h
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontonecollector.cpp
    # Refactor — tone/context primitives split out of regiontonecollector.cpp
    # (byte-identical pure code movement): collectSoundingAt, buildTones,
    # collectPitchContext, the two sub-boundary detectors, and findTemporalContext.
    # Residual regiontonecollector.cpp holds the collectRegionTones orchestrator.
    # Declarations stay in the unchanged regiontonecollector.h. See
    # cc_module_layering_assessment_dossier.md §5.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontoneprimitives.cpp
    # spellingview — the single shared tpc → line-of-fifths/sharp-flat spelling
    # primitive (Phase 4, the maximal-information capability). Interprets the
    # notated spelling Layer 1 carries (NoteEvent.tpc) into per-note line-of-fifths
    # + sharp/flat sense (the Layer-4 spelling-pin's input) and a signature-agnostic
    # span centroid/distribution (the Layer-3 key-spelling term's input, Phase B).
    # CAPABILITY ONLY — no production consumer yet, so output is byte-identical;
    # unit-tested as a pure function (spellingview_tests.cpp). See
    # cowork_tpc_capability_design.md + cc_tpc_capability_build_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/spellingview.h
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/spellingview.cpp

    # slicing/ — LAYER 2: the deterministic CHANGE-POINT SLICER. Enumerates the
    # constant-tonal-sonority slices over the layer-1 note model as a covering,
    # lossless, zero-interpretation FACT (boundaries at every eligible onset AND
    # release; all-rest interior spans are explicit empty slices). WIRED into the live
    # analysis pipeline (changePointSlices @ regionanalyzer.cpp:579), consumed at
    # layer 3 by the key/mode sequence decoder. See
    # cowork_layer2_slicing_design.md + cc_layer2_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/slicing/slicer.h
    ${CMAKE_CURRENT_LIST_DIR}/slicing/slicer.cpp
)
