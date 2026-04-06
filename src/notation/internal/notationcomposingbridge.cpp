/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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

// ── Single-note bridge: harmonicAnnotation + analyzeNoteHarmonicContext ──────
//
// Implements the two single-note bridge functions declared in
// notationcomposingbridge.h.  Shared engraving helpers live in
// notationcomposingbridgehelpers.cpp; the bulk time-range scanner lives in
// notationharmonicrhythmbridge.cpp.

#include "notationcomposingbridge.h"
#include "notationanalysisinternal.h"
#include "notationcomposingbridgehelpers.h"

#include <set>
#include <string>

#include "engraving/dom/note.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

using namespace mu::engraving;
using mu::notation::internal::isChordTrackStaff;
using mu::notation::internal::staffIsEligible;
using mu::notation::internal::SoundingNote;
using mu::notation::internal::collectSoundingAt;
using mu::notation::internal::buildTones;
using mu::notation::internal::resolveKeyAndMode;
using mu::notation::internal::findTemporalContext;

// ── harmonicAnnotation ──────────────────────────────────────────────────────

namespace mu::notation {

std::string harmonicAnnotation(const Note* note)
{
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> config;
    const auto* prefs = config.get().get();
    if (!prefs) {
        return "";
    }

    int keyFifths = 0;
    mu::composing::analysis::KeySigMode keyMode = mu::composing::analysis::KeySigMode::Ionian;
    const auto chordResults = analyzeNoteHarmonicContext(note, keyFifths, keyMode);

    // Key/mode string (optional)
    std::string keyStr;
    if (prefs->showKeyModeInStatusBar()) {
        using mu::composing::analysis::keyModeTonicName;
        using mu::composing::analysis::keyModeSuffix;
        keyStr = std::string(keyModeTonicName(keyFifths, keyMode)) + " " + keyModeSuffix(keyMode);
    }

    // If no chord-level analysis is requested, show only key/mode (no "in" prefix)
    if (!prefs->analyzeForChordSymbols() && !prefs->analyzeForChordFunction()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    if (chordResults.empty()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    // Determine which display formats are active
    const bool wantSym      = prefs->analyzeForChordSymbols()   && prefs->showChordSymbolsInStatusBar();
    const bool wantRoman    = prefs->analyzeForChordFunction()  && prefs->showRomanNumeralsInStatusBar();
    const bool wantNashville = prefs->analyzeForChordFunction() && prefs->showNashvilleNumbersInStatusBar();

    int shown = 0;
    const int maxShown = prefs->analysisAlternatives();
    std::string candidates;
    std::set<std::string> seenKeys;

    for (const auto& result : chordResults) {
        if (shown >= maxShown) {
            break;
        }

        std::string sym, roman, nashville;
        if (wantSym) {
            sym = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(result, keyFifths);
        }
        if (wantRoman) {
            roman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(result);
        }
        if (wantNashville) {
            nashville = mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(result, keyFifths);
        }

        if (sym.empty() && roman.empty() && nashville.empty()) {
            continue;
        }
        std::string key = sym + "|" + roman + "|" + nashville;
        if (!seenKeys.insert(key).second) {
            continue;
        }

        std::string entry;
        for (const std::string& part : { sym, roman, nashville }) {
            if (part.empty()) {
                continue;
            }
            if (!entry.empty()) {
                entry += " / ";
            }
            entry += part;
        }

        if (!entry.empty()) {
            char scoreBuf[16];
            std::snprintf(scoreBuf, sizeof(scoreBuf), " (%.2f)", result.identity.score);
            entry += scoreBuf;

            if (!candidates.empty()) {
                candidates += " | ";
            }
            candidates += entry;
            ++shown;
        }
    }

    if (candidates.empty()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    const std::string headed = "Chord: " + candidates;
    if (!keyStr.empty()) {
        return headed + " in key: " + keyStr;
    }
    return headed;
}

} // namespace mu::notation

// ── analyzeNoteHarmonicContext ────────────────────────────────────────────────

namespace mu::notation {

std::vector<mu::composing::analysis::ChordAnalysisResult>
analyzeNoteHarmonicContext(const mu::engraving::Note* note,
                           int& outKeyFifths,
                           mu::composing::analysis::KeySigMode& outKeyMode)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;
    using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode

    if (!note) {
        return {};
    }

    const Score*   sc   = note->score();
    const Fraction tick = note->tick();
    const Segment* seg = sc->tick2segment(tick, true, SegmentType::ChordRest);
    if (!seg) {
        return {};
    }

    // Exclude chord-staff staves so their notes don't pollute the analysis.
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (isChordTrackStaff(sc, si)) {
            excludeStaves.insert(si);
        }
    }

    // If the selected note is itself on a chord-staff, fall back to the
    // first eligible staff for key-signature lookup.
    staff_idx_t refStaff = note->staffIdx();
    if (excludeStaves.count(static_cast<size_t>(refStaff))) {
        refStaff = 0;
        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (!excludeStaves.count(si) && staffIsEligible(sc, si, tick)) {
                refStaff = static_cast<staff_idx_t>(si);
                break;
            }
        }
    }

    std::vector<SoundingNote> sounding;
    collectSoundingAt(sc, seg, excludeStaves, sounding);
    if (sounding.empty()) {
        return {};
    }

    double unusedConfidence = 0.0;
    resolveKeyAndMode(sc, tick, refStaff, excludeStaves,
                      outKeyFifths, outKeyMode, unusedConfidence);

    // Derive current bass pc from the lowest sounding pitch (same logic as buildTones).
    int currentBassPc = -1;
    {
        int lo = std::numeric_limits<int>::max();
        for (const SoundingNote& sn : sounding) { lo = std::min(lo, sn.ppitch); }
        if (lo != std::numeric_limits<int>::max()) { currentBassPc = lo % 12; }
    }

    ChordTemporalContext temporalCtx
        = findTemporalContext(sc, seg, excludeStaves, outKeyFifths, outKeyMode, currentBassPc);

    const auto analysisTones = buildTones(sounding);
    return ChordAnalyzerFactory::create()->analyzeChord(analysisTones, outKeyFifths, outKeyMode,
                                                        &temporalCtx);
}

} // namespace mu::notation
