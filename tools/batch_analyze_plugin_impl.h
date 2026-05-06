// SPDX-License-Identifier: GPL-3.0-only
// MuseScore-Studio-CLA-applies
//
// batch_analyze_plugin_impl.h
//
// Public API for batch_analyze_plugin_impl.cpp.
// Include this from any translation unit that needs to invoke the plugin
// reimplementation (currently: llm_triage.cpp).

#pragma once

#include <string>
#include <vector>
#include <ostream>

namespace mu::engraving { class Score; }

// ─────────────────────────────────────────────────────────────────────────────
// Note data collected at one tick position
// ─────────────────────────────────────────────────────────────────────────────
struct PluginNoteData {
    int pitch;    // absolute MIDI pitch
    int tpc;      // tonal pitch class
    int endTick;  // tick at which this note stops sounding
};

// ─────────────────────────────────────────────────────────────────────────────
// One chord-identification event
// ─────────────────────────────────────────────────────────────────────────────
struct PluginRegion {
    int         tickStart;
    int         tickEnd;
    int         measureNumber;
    double      beatStart;      // 1-based beat onset within the measure
    double      durationBeats;
    std::string chordLabel;     // actual label (empty = not identified)
    bool        matchAllNotes;  // all note PCs accounted for by the template
    bool        suppressed;     // duplicate — excluded from JSON output
    std::vector<PluginNoteData> chord;       // full sounding note set (sorted asc)
    std::vector<int>            tonesPcSet;  // sorted unique pitch classes
};

// ─────────────────────────────────────────────────────────────────────────────
// Run the plugin algorithm over the whole score.
// Returns one PluginRegion per chord-onset tick (including suppressed entries).
// Post-processing fills tickEnd and durationBeats on non-suppressed entries.
// ─────────────────────────────────────────────────────────────────────────────
std::vector<PluginRegion> runPluginAnalysis(const mu::engraving::Score* score);

// ─────────────────────────────────────────────────────────────────────────────
// Write the unified triage response JSON to @p out.
// Suppressed entries are omitted; the preceding entry's tickEnd covers them.
// scoreContentHash: SHA-256 hex string (or "" if unavailable).
// timestampUtc:     ISO-8601 UTC string (or "").
// ─────────────────────────────────────────────────────────────────────────────
void writePluginResponseJson(
    const std::vector<PluginRegion>& regions,
    const std::string& scoreBasename,
    const std::string& scorePath,
    const std::string& scoreContentHash,
    const std::string& timestampUtc,
    std::ostream& out);
