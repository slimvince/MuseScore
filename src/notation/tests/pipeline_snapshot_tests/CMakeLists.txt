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

# ── pipeline_snapshot_tests ────────────────────────────────────────────────────
#
# Phase 1b of the unified-pipeline refactor (docs/unified_analysis_pipeline.md).
# Pins current user-facing output of the four analysis paths (P1 Implode,
# P2 Annotation, P3 Tick-regional, P4 Tick-local) against a fixed corpus so
# that the Phase 2+ refactor can prove behavior preservation.
#
# Binary is modelled on the notation_tests target: full IoC + ScoreRW + the
# shared gmain.cpp harness.
#
# Snapshots live alongside the sources under ./snapshots/ and are loaded at
# runtime using the PIPELINE_SNAPSHOT_SNAPSHOTS_DIR compile definition below.

set(MODULE_TEST pipeline_snapshot_tests)

set(MODULE_TEST_SRC
    ${CMAKE_CURRENT_LIST_DIR}/pipeline_snapshot_tests.cpp
    ${CMAKE_CURRENT_LIST_DIR}/environment.cpp

    ${PROJECT_SOURCE_DIR}/src/engraving/tests/utils/scorerw.cpp
    ${PROJECT_SOURCE_DIR}/src/engraving/tests/utils/scorerw.h
    ${PROJECT_SOURCE_DIR}/src/engraving/tests/mocks/engravingconfigurationmock.h
)

# Source root for the test corpus (DCML scores we do not copy in).
set(MODULE_TEST_DATA_ROOT "${PROJECT_SOURCE_DIR}")

set(MODULE_TEST_DEF
    PIPELINE_SNAPSHOT_SNAPSHOTS_DIR="${CMAKE_CURRENT_LIST_DIR}/snapshots"
    PIPELINE_SNAPSHOT_CORPUS_ROOT="${PROJECT_SOURCE_DIR}"
)

set(MODULE_TEST_LINK
    notation
    composing
    engraving
)

include(SetupGTest)
