/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2026 MuseScore Limited
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#pragma once

#include <cstddef>
#include <string>
#include <vector>

// ── Stage-5 fitter — the parameter-override mechanism (design D-6 / A-6) ──────────
//
// An OPTIONAL, flag-gated external override of the scoring pipeline's numeric
// constants, read once at analysis-binary startup (tools/batch_analyze
// --param-override <file>). It exists so the Stage-5 fitter can evaluate a candidate
// parameter vector WITHOUT rebuilding the binary per vector (thousands of evaluations).
//
// ★ BYTE-IDENTITY IS THE ACCEPTANCE. When no override file is loaded, the pipeline's
//   behavior and output are byte-identical to before this mechanism existed: every
//   file-level scoring constant that used to be `constexpr` is now a mutable global
//   with the SAME literal initializer, read exactly as before; the override loader is
//   the ONLY writer, and it runs only when a file is passed. See
//   cowork_stage5_fitter_design.md §2 (constraint 7) + §4.3 (1a).
//
// The mechanism reaches the constants on the PRODUCTION fit surface (the measured
// carrier): the chordanalyzer.cpp file constants (G1), the harmonicfunctionlayer.h
// progression constants (G6), the postscoringgates.cpp gate margins (G7), and the
// ChordAnalyzerPreferences fields (G2–G5). It does NOT reach the dormant-chain
// struct-member defaults (G8/G11/G12/G13) — those are consumed only by the default-off
// dormant chain and cannot affect the production output; see the Phase-1 report.

namespace mu::composing::analysis {
struct ChordAnalyzerPreferences;
}

namespace mu::composing::params {

// ── Registration (called at static-init from the constant-owning TUs) ──────────────
// Register the ADDRESS of a mutable global scoring constant under a stable name.
// The registry stores the pointer; loadAndApply()/applyGlobalOverride() is the writer.
void registerDouble(const char* name, double* slot);
void registerInt(const char* name, int* slot);
void registerBool(const char* name, bool* slot);

// ── Apply / load ───────────────────────────────────────────────────────────────────
struct LoadStats {
    int applied = 0;      ///< total name=value pairs applied
    int globals = 0;      ///< applied to registered global constants
    int prefsFields = 0;  ///< applied to ChordAnalyzerPreferences fields
};

/// Apply one override to the registered globals only. Returns true iff @p name is a
/// registered global (of any type); the value is coerced to the slot's type
/// (int = llround, bool = (value != 0)).
bool applyGlobalOverride(const std::string& name, double value);

/// Apply one override to a ChordAnalyzerPreferences field by name. Returns true iff
/// @p name is a known prefs field (int/bool fields are coerced from @p value).
bool applyPrefsOverride(analysis::ChordAnalyzerPreferences& prefs,
                        const std::string& name, double value);

/// Parse a line-based override FILE and apply every pair.
///
/// Format: one `name value` per line; `#` starts a comment (to end of line); blank
/// lines are ignored. @p value is a decimal number (or the tokens `true`/`false`).
///
/// STRICT: throws std::runtime_error on an I/O error, a malformed line/number, or any
/// name that matches neither a registered global nor a prefs field. After applying,
/// derived constants are recomputed (kStepBudget = kWStepIn + kWStepOut + 0.01, unless
/// kStepBudget was set explicitly). Returns per-channel counts.
LoadStats loadAndApply(const std::string& path,
                       analysis::ChordAnalyzerPreferences& prefs);

// ── Introspection (tests / driver) ───────────────────────────────────────────────
bool isRegisteredGlobal(const std::string& name);
double getRegisteredGlobal(const std::string& name);   ///< reads the current slot value; throws if unknown
std::size_t registeredGlobalCount();
std::vector<std::string> registeredGlobalNames();
bool isKnownName(const std::string& name);             ///< registered global OR prefs field
std::vector<std::string> prefsFieldNames();            ///< the settable ChordAnalyzerPreferences field names

}
