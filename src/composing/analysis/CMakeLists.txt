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
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.h
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.h

    # section/ — unified section-level analysis: the analyzeSection() entry
    # point, key/mode stabilization, and cadence / pivot detection. Moved here
    # from notation/internal/notationcomposingbridgehelpers.cpp in Stage 2.1
    # (Phase 4c — Dependency Rule §3.3; docs/implementation_roadmap.md Stage 2.1).
    ${CMAKE_CURRENT_LIST_DIR}/section/sectionanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/section/sectionanalyzer.cpp
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
    # key is an echoed reference, never read). Built + MEASURED only; invoked solely
    # from tools/batch_analyze --dump-joint-key, never the production resolver
    # (wiring is J-key-ii).
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

    # engravingbridge/ — single source of truth for the score-walking helpers
    # shared by the notation bridge and tools/batch_analyze.cpp. Replaces the
    # Step-3 using-declaration plumbing in batch_analyze.cpp. See
    # docs/duplication_audit.md §§2.1-2.13 and §5.1.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontonecollector.h
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontonecollector.cpp
)
