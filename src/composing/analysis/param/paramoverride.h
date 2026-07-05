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

// ── §6-block dissolution AUDIT — per-rule disable (measurement-only, Phase 2.2) ─────
//
// The docs/scoring_model.md §6 post-scoring correction block, addressable rule by rule
// so the Stage-5 dissolution audit can measure each rule's marginal contribution at
// current weights. Each id maps to ONE clean skip in applyPostScoringGates() — disabling
// it removes only that rule's rank mutation, nothing else. Default = every rule ENABLED
// (all-false), so with no `disable_rule` line the pipeline is byte-identical. This is the
// SAME safety class as the constant override (A-6): flag-gated, byte-identical absent.
// The audit is measurement-only; the fit that decides any retirement is Phase 2.2b (D-7).
enum class PostScoringRule : int {
    BiasCorrection = 0,  ///< bass-root bias deduction + re-sort (incl. kHalfDimFirstInversionBonus)
    FM2,                 ///< Minor-partner pull from rawCandidates in the enharmonic fast path
    GateE,               ///< first-inversion Minor → Major (+8)
    GateF,               ///< second-inversion → root-position Major (+5)
    GateGE,              ///< Minor-add6 ↔ HalfDim7 key-function flip (viiø7/iiø7/iiiø7)
    GateGB,              ///< Minor-add6 ↔ HalfDim7 forward-evidence temporal fallback
    GateGC,              ///< Minor-add6 ↔ HalfDim7 recent-root + stepwise temporal fallback
    GateGD,              ///< Minor-add6 ↔ HalfDim7 consecutive-stepwise temporal fallback
    GateH,               ///< augmented rotation resolution
    GateI,               ///< first-inversion Major over root-position Minor
    GateK,               ///< first-inversion Augmented over root-position Augmented
    GateL,               ///< same-root Major over root-position Augmented (TYPE-A)
    GateJ,               ///< vii° → V7 completion (runs last)
    Count
};

/// Canonical §6 rule names (execution order); the `disable_rule <Name>` file tokens.
std::vector<std::string> postScoringRuleNames();
/// Map a canonical §6 rule name to its id. Returns true iff @p name is a known rule.
bool postScoringRuleId(const std::string& name, PostScoringRule& out);
/// True iff @p name is a known §6 rule name.
bool isKnownRuleName(const std::string& name);
/// Disable one §6 rule by canonical name (the file-grammar path). Returns true iff known.
bool disableRuleByName(const std::string& name);
/// Programmatic set (tests). resetPostScoringRules() re-enables ALL — the process default.
void setRuleDisabled(PostScoringRule rule, bool disabled);
void resetPostScoringRules();
/// Hot-path query, read by applyPostScoringGates(). Default (nothing disabled) = false.
bool isRuleDisabled(PostScoringRule rule);

// ── Apply / load ───────────────────────────────────────────────────────────────────
struct LoadStats {
    int applied = 0;        ///< total override entries applied (name=value pairs + disable_rule lines)
    int globals = 0;        ///< applied to registered global constants
    int prefsFields = 0;    ///< applied to ChordAnalyzerPreferences fields
    int rulesDisabled = 0;  ///< §6 rules disabled via `disable_rule <Name>` (measurement-only)
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
/// A line `disable_rule <Name>` disables one §6 post-scoring rule (measurement-only,
/// Phase 2.2) — <Name> is one of postScoringRuleNames(); the `disable_rule` keyword is
/// reserved and never a parameter name.
///
/// STRICT: throws std::runtime_error on an I/O error, a malformed line/number, an
/// unknown §6 rule name, or any name that matches neither a registered global nor a
/// prefs field. After applying,
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
