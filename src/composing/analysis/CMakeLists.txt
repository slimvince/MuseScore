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

    # function/ — Phase E harmonic function layer (post-analysis pass between
    # analyzeChord() output and the final chord label). E1 is a pass-through
    # shell; E2/E3/E4 migrate progression signals, post-scoring gates, and
    # cadence detection out of chordanalyzer.cpp. See docs/scoring_model.md §10.
    ${CMAKE_CURRENT_LIST_DIR}/function/harmonicfunctionlayer.h
    ${CMAKE_CURRENT_LIST_DIR}/function/harmonicfunctionlayer.cpp

    # key/ — key and mode analysis
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.h
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.h

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
