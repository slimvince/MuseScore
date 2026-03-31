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
    ${CMAKE_CURRENT_LIST_DIR}/analysisutils.h
    ${CMAKE_CURRENT_LIST_DIR}/chordanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chordanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/harmonicrhythm.h
    ${CMAKE_CURRENT_LIST_DIR}/keymodeanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/keymodeanalyzer.h
)
