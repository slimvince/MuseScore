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

#include "paramoverride.h"

#include "../types/analysistypes.h"

#include <array>
#include <cmath>
#include <fstream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <set>
#include <utility>

namespace mu::composing::params {

namespace {

// Meyers-singleton registries — construct-before-first-use, so the static-init-time
// registerXxx() calls from the constant-owning TUs are always safe regardless of the
// cross-TU initialization order.
std::map<std::string, double*>& doubleRegistry()
{
    static std::map<std::string, double*> m;
    return m;
}
std::map<std::string, int*>& intRegistry()
{
    static std::map<std::string, int*> m;
    return m;
}
std::map<std::string, bool*>& boolRegistry()
{
    static std::map<std::string, bool*> m;
    return m;
}

// Trim leading/trailing ASCII whitespace.
std::string trim(const std::string& s)
{
    const auto b = s.find_first_not_of(" \t\r\n\f\v");
    if (b == std::string::npos) {
        return {};
    }
    const auto e = s.find_last_not_of(" \t\r\n\f\v");
    return s.substr(b, e - b + 1);
}

// Parse a numeric token, accepting the literal words true/false.
double parseValueToken(const std::string& tok, const std::string& lineForError)
{
    if (tok == "true") {
        return 1.0;
    }
    if (tok == "false") {
        return 0.0;
    }
    try {
        size_t consumed = 0;
        const double v = std::stod(tok, &consumed);
        if (consumed != tok.size()) {
            throw std::invalid_argument("trailing characters");
        }
        return v;
    } catch (const std::exception&) {
        throw std::runtime_error("param-override: malformed value '" + tok
                                 + "' in line: " + lineForError);
    }
}

// ── §6-block rule-disable state (measurement-only) ─────────────────────────────────
// Process-global, value-initialized to all-false = every §6 rule ENABLED. Written only
// by disableRuleByName()/setRuleDisabled(); disableRuleByName() runs only from a
// `disable_rule` line in a loaded file. So with no override file the array is all-false
// and applyPostScoringGates() runs byte-identically. isRuleDisabled() is the only reader
// on the hot path.
std::array<bool, static_cast<std::size_t>(PostScoringRule::Count)>& ruleDisabledState()
{
    static std::array<bool, static_cast<std::size_t>(PostScoringRule::Count)> s{};
    return s;
}

// Canonical §6 rule names, indexed by PostScoringRule (execution order). The
// `disable_rule <Name>` file tokens and the introspection list are both this table.
const std::array<const char*, static_cast<std::size_t>(PostScoringRule::Count)>&
ruleNameTable()
{
    static const std::array<const char*, static_cast<std::size_t>(PostScoringRule::Count)>
        kNames = {
            "BiasCorrection", "FM2", "GateE",
            "GateGE", "GateGB", "GateGC", "GateGD",
            "GateH", "GateI", "GateK", "GateL", "GateJ",
        };
    return kNames;
}

} // namespace

std::vector<std::string> postScoringRuleNames()
{
    std::vector<std::string> out;
    for (const char* n : ruleNameTable()) {
        out.emplace_back(n);
    }
    return out;
}

bool postScoringRuleId(const std::string& name, PostScoringRule& out)
{
    const auto& names = ruleNameTable();
    for (std::size_t i = 0; i < names.size(); ++i) {
        if (name == names[i]) {
            out = static_cast<PostScoringRule>(i);
            return true;
        }
    }
    return false;
}

bool isKnownRuleName(const std::string& name)
{
    PostScoringRule r{};
    return postScoringRuleId(name, r);
}

void setRuleDisabled(PostScoringRule rule, bool disabled)
{
    ruleDisabledState()[static_cast<std::size_t>(rule)] = disabled;
}

bool disableRuleByName(const std::string& name)
{
    PostScoringRule r{};
    if (!postScoringRuleId(name, r)) {
        return false;
    }
    setRuleDisabled(r, true);
    return true;
}

void resetPostScoringRules()
{
    ruleDisabledState().fill(false);
}

bool isRuleDisabled(PostScoringRule rule)
{
    return ruleDisabledState()[static_cast<std::size_t>(rule)];
}

void registerDouble(const char* name, double* slot)
{
    doubleRegistry()[name] = slot;
}
void registerInt(const char* name, int* slot)
{
    intRegistry()[name] = slot;
}
void registerBool(const char* name, bool* slot)
{
    boolRegistry()[name] = slot;
}

bool applyGlobalOverride(const std::string& name, double value)
{
    if (auto it = doubleRegistry().find(name); it != doubleRegistry().end()) {
        *(it->second) = value;
        return true;
    }
    if (auto it = intRegistry().find(name); it != intRegistry().end()) {
        *(it->second) = static_cast<int>(std::llround(value));
        return true;
    }
    if (auto it = boolRegistry().find(name); it != boolRegistry().end()) {
        *(it->second) = (value != 0.0);
        return true;
    }
    return false;
}

bool applyPrefsOverride(analysis::ChordAnalyzerPreferences& prefs,
                        const std::string& name, double value)
{
    // ── double-valued fields ──────────────────────────────────────────────────
    if (name == "bassNoteRootBonus")             { prefs.bassNoteRootBonus = value; return true; }
    if (name == "bassRootThirdOnlyMultiplier")   { prefs.bassRootThirdOnlyMultiplier = value; return true; }
    if (name == "bassRootAloneMultiplier")       { prefs.bassRootAloneMultiplier = value; return true; }
    if (name == "diatonicRootBonus")             { prefs.diatonicRootBonus = value; return true; }
    if (name == "tpcConsistencyBonusPerTone")    { prefs.tpcConsistencyBonusPerTone = value; return true; }
    if (name == "rootContinuityBonus")           { prefs.rootContinuityBonus = value; return true; }
    if (name == "resolutionBonus")               { prefs.resolutionBonus = value; return true; }
    if (name == "stepwiseBassInversionBonus")    { prefs.stepwiseBassInversionBonus = value; return true; }
    if (name == "stepwiseBassLookaheadBonus")    { prefs.stepwiseBassLookaheadBonus = value; return true; }
    if (name == "completeTriadInversionBonus")   { prefs.completeTriadInversionBonus = value; return true; }
    if (name == "sameRootInversionBonus")        { prefs.sameRootInversionBonus = value; return true; }
    if (name == "maxTotalInversionContextBonus") { prefs.maxTotalInversionContextBonus = value; return true; }
    if (name == "inversionSuspicionMargin")      { prefs.inversionSuspicionMargin = value; return true; }
    if (name == "inversionBonusReduction")       { prefs.inversionBonusReduction = value; return true; }
    if (name == "harmonicBoundaryJaccardThreshold") { prefs.harmonicBoundaryJaccardThreshold = value; return true; }
    if (name == "pedalTailWeightMultiplier")     { prefs.pedalTailWeightMultiplier = value; return true; }
    if (name == "bassPassingToneMinWeightFraction") { prefs.bassPassingToneMinWeightFraction = value; return true; }
    if (name == "pedalConfidenceThreshold")      { prefs.pedalConfidenceThreshold = value; return true; }
    if (name == "extensionThreshold")            { prefs.extensionThreshold = value; return true; }
    // ── int-valued field (frozen; read-only rider only) ───────────────────────
    if (name == "minDistinctPcsForCandidate")    { prefs.minDistinctPcsForCandidate = static_cast<int>(std::llround(value)); return true; }
    // ── bool-valued field (frozen; read-only rider only) ──────────────────────
    if (name == "preferMinorOverMajorAdd6")      { prefs.preferMinorOverMajorAdd6 = (value != 0.0); return true; }
    return false;
}

std::vector<std::string> prefsFieldNames()
{
    return {
        "bassNoteRootBonus", "bassRootThirdOnlyMultiplier", "bassRootAloneMultiplier",
        "diatonicRootBonus", "tpcConsistencyBonusPerTone", "rootContinuityBonus",
        "resolutionBonus", "stepwiseBassInversionBonus", "stepwiseBassLookaheadBonus",
        "completeTriadInversionBonus", "sameRootInversionBonus",
        "maxTotalInversionContextBonus", "inversionSuspicionMargin",
        "inversionBonusReduction", "harmonicBoundaryJaccardThreshold",
        "pedalTailWeightMultiplier", "bassPassingToneMinWeightFraction",
        "pedalConfidenceThreshold", "extensionThreshold",
        "minDistinctPcsForCandidate", "preferMinorOverMajorAdd6",
    };
}

bool isRegisteredGlobal(const std::string& name)
{
    return doubleRegistry().count(name) || intRegistry().count(name) || boolRegistry().count(name);
}

double getRegisteredGlobal(const std::string& name)
{
    if (auto it = doubleRegistry().find(name); it != doubleRegistry().end()) {
        return *(it->second);
    }
    if (auto it = intRegistry().find(name); it != intRegistry().end()) {
        return static_cast<double>(*(it->second));
    }
    if (auto it = boolRegistry().find(name); it != boolRegistry().end()) {
        return *(it->second) ? 1.0 : 0.0;
    }
    throw std::runtime_error("param-override: getRegisteredGlobal on unknown name: " + name);
}

std::size_t registeredGlobalCount()
{
    return doubleRegistry().size() + intRegistry().size() + boolRegistry().size();
}

std::vector<std::string> registeredGlobalNames()
{
    std::vector<std::string> names;
    for (const auto& [k, v] : doubleRegistry()) { (void)v; names.push_back(k); }
    for (const auto& [k, v] : intRegistry())    { (void)v; names.push_back(k); }
    for (const auto& [k, v] : boolRegistry())   { (void)v; names.push_back(k); }
    return names;
}

bool isKnownName(const std::string& name)
{
    if (isRegisteredGlobal(name)) {
        return true;
    }
    for (const auto& f : prefsFieldNames()) {
        if (f == name) {
            return true;
        }
    }
    return false;
}

LoadStats loadAndApply(const std::string& path,
                       analysis::ChordAnalyzerPreferences& prefs)
{
    std::ifstream ifs(path, std::ios::binary);
    if (!ifs) {
        throw std::runtime_error("param-override: cannot open file: " + path);
    }

    LoadStats stats;
    std::set<std::string> seen;
    std::string rawLine;
    int lineNo = 0;
    while (std::getline(ifs, rawLine)) {
        ++lineNo;
        // strip comment
        std::string line = rawLine;
        if (const auto hash = line.find('#'); hash != std::string::npos) {
            line = line.substr(0, hash);
        }
        line = trim(line);
        if (line.empty()) {
            continue;
        }
        std::istringstream iss(line);
        std::string name, valueTok, extra;
        iss >> name >> valueTok;
        if (name.empty() || valueTok.empty()) {
            throw std::runtime_error("param-override: malformed line " + std::to_string(lineNo)
                                     + " (expected 'name value'): " + line);
        }
        if (iss >> extra) {
            throw std::runtime_error("param-override: extra token '" + extra + "' on line "
                                     + std::to_string(lineNo) + ": " + line);
        }

        // ── `disable_rule <Name>`: §6-block dissolution audit (measurement-only) ──
        // A reserved keyword line, distinct from the numeric `name value` grammar; its
        // second token is a §6 rule name, not a number, so it is intercepted before
        // parseValueToken(). Does not participate in the kStepBudget derivation (seen).
        if (name == "disable_rule") {
            if (!disableRuleByName(valueTok)) {
                throw std::runtime_error("param-override: unknown §6 rule name '" + valueTok
                                         + "' on line " + std::to_string(lineNo));
            }
            ++stats.rulesDisabled;
            ++stats.applied;
            continue;
        }

        const double value = parseValueToken(valueTok, line);

        bool applied = false;
        if (applyGlobalOverride(name, value)) {
            ++stats.globals;
            applied = true;
        } else if (applyPrefsOverride(prefs, name, value)) {
            ++stats.prefsFields;
            applied = true;
        }
        if (!applied) {
            throw std::runtime_error("param-override: unknown parameter name '" + name
                                     + "' on line " + std::to_string(lineNo));
        }
        ++stats.applied;
        seen.insert(name);
    }

    // ── Recompute derived constants ──────────────────────────────────────────────
    // kStepBudget = kWStepIn + kWStepOut + 0.01 (the m7-family surgical-guard tolerance;
    // frozen, but DERIVED from two fittable step bonuses). If the file moved kWStepIn or
    // kWStepOut without explicitly pinning kStepBudget, keep the derivation faithful so a
    // step-bonus perturbation is measured as the pre-override code would have seen it.
    if (!seen.count("kStepBudget")
        && (seen.count("kWStepIn") || seen.count("kWStepOut"))
        && isRegisteredGlobal("kWStepIn") && isRegisteredGlobal("kWStepOut")
        && isRegisteredGlobal("kStepBudget")) {
        const double derived = getRegisteredGlobal("kWStepIn") + getRegisteredGlobal("kWStepOut") + 0.01;
        applyGlobalOverride("kStepBudget", derived);
    }

    return stats;
}

} // namespace mu::composing::params
