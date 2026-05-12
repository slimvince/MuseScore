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

add_subdirectory(analysis)

# Add intonation module

# Add intonation module
add_subdirectory(intonation)

muse_create_module(composing)

target_sources(composing PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/composingmodule.cpp
    ${CMAKE_CURRENT_LIST_DIR}/composingmodule.h
    ${CMAKE_CURRENT_LIST_DIR}/composingconfiguration.cpp
    ${CMAKE_CURRENT_LIST_DIR}/composingconfiguration.h
    ${CMAKE_CURRENT_LIST_DIR}/icomposinganalysisconfiguration.h
    ${CMAKE_CURRENT_LIST_DIR}/icomposingchordstaffconfiguration.h
    ${CMAKE_CURRENT_LIST_DIR}/icomposingconfiguration.h

    # Phase 2 — shared unified-pipeline output types.  See
    # docs/unified_analysis_pipeline.md.  Phase 4 will retire the bridge-side
    # analyzeSection() delegate and move the entry point into composing/.
    ${CMAKE_CURRENT_LIST_DIR}/analyzed_section.h
)

target_include_directories(composing_analysis INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/..
    ${CMAKE_CURRENT_BINARY_DIR}/..
)

# Iter 67: harmonicsegmenter.cpp uses engraving Score/Segment/Chord/Note types,
# so composing_analysis now depends on engraving for compilation and linkage.
target_link_libraries(composing_analysis PUBLIC engraving)

target_link_libraries(composing PRIVATE
    composing_analysis
    muse_global
    intonation
)

if (MUE_BUILD_COMPOSING_TESTS)
    add_subdirectory(tests)
endif()
