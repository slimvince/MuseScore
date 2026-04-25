# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# tools/llm_triage/CMakeLists.txt
#
# LLM-Triage v0: plain-text format emitter for hand-evaluation against frontier LLMs.
# Loads one score, runs the harmonic analyzer, emits three .txt artifacts.
# See docs/llm_triage_design.md for design rationale.

add_executable(llm_triage
    llm_triage.cpp
)

set_target_properties(llm_triage PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)

target_include_directories(llm_triage PRIVATE
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/framework
    ${CMAKE_SOURCE_DIR}/src/framework/global
    ${CMAKE_BINARY_DIR}/tools/llm_triage
)

target_link_libraries(llm_triage
    PRIVATE
    muse_global
    muse_draw
    engraving
    notation
    composing_analysis
    iex_musicxml
)
