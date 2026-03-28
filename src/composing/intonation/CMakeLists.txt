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

# Add all source files in this directory
muse_create_module(intonation NO_QT)

target_sources(intonation PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/tuning_system.h
    ${CMAKE_CURRENT_LIST_DIR}/just_intonation.h
    ${CMAKE_CURRENT_LIST_DIR}/equal_temperament.h
    ${CMAKE_CURRENT_LIST_DIR}/pythagorean.h
    ${CMAKE_CURRENT_LIST_DIR}/quarter_comma_meantone.h
    ${CMAKE_CURRENT_LIST_DIR}/werckmeister.h
    ${CMAKE_CURRENT_LIST_DIR}/kirnberger.h
    ${CMAKE_CURRENT_LIST_DIR}/tuning_registry.cpp
    ${CMAKE_CURRENT_LIST_DIR}/tuning_utils.h
)

target_link_libraries(intonation PRIVATE composing_analysis)
