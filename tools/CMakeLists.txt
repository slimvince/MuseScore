# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# tools/CMakeLists.txt
#
# Development tools — not part of the shipping product.
# Compiled only when MUE_BUILD_ENGRAVING_DEVTOOLS is ON (the default for
# development builds).  Release packages built with -DMUE_BUILD_ENGRAVING_DEVTOOLS=OFF
# will skip this directory entirely.

if (NOT MUE_BUILD_ENGRAVING_DEVTOOLS)
    return()
endif()

# ── batch_analyze ─────────────────────────────────────────────────────────
# Headless harmonic analysis tool.  Loads a MusicXML (or MSCZ/MSCX) file and
# writes our ChordAnalyzer + KeyModeAnalyzer results as JSON.
# See tools/batch_analyze.cpp for usage.

add_executable(batch_analyze
    batch_analyze.cpp
)

set_target_properties(batch_analyze PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)

# Include paths: src/ (for engraving/, composing/, importexport/) and
# src/framework/ (for global/, draw/).
target_include_directories(batch_analyze PRIVATE
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/framework
    ${CMAKE_SOURCE_DIR}/src/framework/global
    ${CMAKE_BINARY_DIR}/tools
)

target_link_libraries(batch_analyze
    PRIVATE
    muse_global         # IoC container, String, Ret, IO types, GlobalModule
    muse_draw           # DrawModule (fonts, vector rendering)
    engraving           # Score model, layout, compat loaders
    notation            # Live notation bridge path for parity checks
    composing_analysis  # ChordAnalyzer, KeyModeAnalyzer, ChordSymbolFormatter
    iex_musicxml        # importMusicXml(), MusicXmlModule
)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

add_test(
    NAME batch_analyze_regressions
    COMMAND ${Python3_EXECUTABLE}
            ${CMAKE_SOURCE_DIR}/tools/test_batch_analyze_regressions.py
            --batch-analyze $<TARGET_FILE:batch_analyze>
            --repo-root ${CMAKE_SOURCE_DIR}
)

set_tests_properties(batch_analyze_regressions PROPERTIES
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

# ── llm_triage ────────────────────────────────────────────────────────────
# Format-emitter for LLM-assisted triage. See docs/llm_triage_design.md.
add_subdirectory(llm_triage)
