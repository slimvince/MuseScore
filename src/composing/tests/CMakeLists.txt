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
    ${CMAKE_CURRENT_LIST_DIR}/cadencekeyanchor_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordanalyzer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordanalyzer_musicxml_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/comparison_utils_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/decode_chord_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/decode_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/decode_keymode_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/diagnose_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/functionlayer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/gater_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/jointkeydecision_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/keymodeanalyzer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/localmodulationdetector_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/note_model_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/postscoringgates_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/reachback_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/regionanalysis_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/slicer_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/spellingview_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/synthetic_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/tonicizationlabeler_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/tuning_tests.cpp
)

set(MODULE_TEST_LINK
    composing_analysis
    intonation
    engraving
)

set(MODULE_TEST_DATA_ROOT ${CMAKE_CURRENT_LIST_DIR})

include(SetupGTest)
