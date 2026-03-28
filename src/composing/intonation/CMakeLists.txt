# SPDX-License-Identifier: GPL-3.0-only
# MuseScore Studio — Intonation module CMake configuration

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
