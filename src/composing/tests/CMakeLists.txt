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

set(MODULE_TEST composing_tests)

set(MODULE_TEST_SRC
    # Stage 1c — score-driven tests (regionanalysis_tests.cpp) need the engraving +
    # draw modules initialised and a key/instrument/config environment, so the
    # composing test binary supplies its own SuiteEnvironment (environment.cpp)
    # plus the engraving ScoreRW utility and config mock. Mirrors engraving_tests.
    ${CMAKE_CURRENT_LIST_DIR}/environment.cpp
    ${PROJECT_SOURCE_DIR}/src/engraving/tests/utils/scorerw.cpp
    ${PROJECT_SOURCE_DIR}/src/engraving/tests/utils/scorerw.h
    ${PROJECT_SOURCE_DIR}/src/engraving/tests/mocks/engravingconfigurationmock.h

    ${CMAKE_CURRENT_LIST_DIR}/test_helpers.h
    ${CMAKE_CURRENT_LIST_DIR}/comparison_utils.h
    ${CMAKE_CURRENT_LIST_DIR}/analyzechord_robustness_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/cadencekeyanchor_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord_branch_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordanalyzer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordanalyzer_musicxml_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordsymbolformatter_branch_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordvoicing_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/comparison_utils_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/decode_chord_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/decode_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/decode_keymode_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/diagnose_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge_branch_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/forwardoverride_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functioncadence_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionlayer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionmodulation_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionoutput_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionprogression_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionrelationallabel_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionresolver_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionromannumeral_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/gater_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/grouping_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/harmonicvocabulary_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint_adapter_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint_decoder_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint_embedded_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint_primitives_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint_tables_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/jointkeydecision_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/keymodeanalyzer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/keymode_branch_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/l3_coverage_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/localmodulationdetector_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/modepriorpresets_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/nashville_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/note_model_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/note_notated_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/paramoverride_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/phraseboundaryview_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/postscoringgates_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/progressionrecognizer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/reachback_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/regionanalysis_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/slicer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/spellingview_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/synthetic_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/tonicizationlabeler_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/tuning_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading_tests.cpp
)

set(MODULE_TEST_LINK
    composing_analysis
    intonation
    engraving
)

set(MODULE_TEST_DATA_ROOT ${CMAKE_CURRENT_LIST_DIR})

include(SetupGTest)

# The joint-estimator table-loading tests read the committed runtime artifacts under
# tools/joint_estimator/ (loaded from disk, not a Qt resource); pass the absolute source
# path as a compile definition so the test locates them regardless of the run directory.
target_compile_definitions(${MODULE_TEST} PRIVATE
    JOINT_ARTIFACT_DIR="${PROJECT_SOURCE_DIR}/tools/joint_estimator")
