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

#include <initializer_list>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"

namespace mu::composing::analysis {

// ── Chord tone builders ───────────────────────────────────────────────────────

template<typename Range>
std::vector<ChordAnalysisTone> tonesFromRange(const Range& pitches)
{
    std::vector<ChordAnalysisTone> out;
    out.reserve(std::distance(std::begin(pitches), std::end(pitches)));
    bool first = true;
    for (int p : pitches) {
        ChordAnalysisTone t;
        t.pitch  = p;
        t.weight = 1.0;
        t.isBass = first;
        out.push_back(t);
        first = false;
    }
    return out;
}

inline std::vector<ChordAnalysisTone> tones(std::initializer_list<int> pitches)
{
    return tonesFromRange(pitches);
}

// ── Key mode pitch builders ───────────────────────────────────────────────────

inline KeyModeAnalyzer::PitchContext makePitch(int pitch, double durationWeight,
                                               double beatWeight, bool isBass)
{
    KeyModeAnalyzer::PitchContext p;
    p.pitch          = pitch;
    p.durationWeight = durationWeight;
    p.beatWeight     = beatWeight;
    p.isBass         = isBass;
    return p;
}

inline std::vector<KeyModeAnalyzer::PitchContext> flatPitches(std::initializer_list<int> midiPitches)
{
    std::vector<KeyModeAnalyzer::PitchContext> out;
    out.reserve(midiPitches.size());
    bool first = true;
    for (int p : midiPitches) {
        out.push_back(makePitch(p, 1.0, 1.0, first));
        first = false;
    }
    return out;
}

// ── Result construction ───────────────────────────────────────────────────────

inline ChordAnalysisResult makeRomanResult(int degree, ChordQuality quality,
                                           int rootPc = 0, int bassPc = 0,
                                           bool hasMin7 = false, bool hasMaj7 = false,
                                           bool hasDim7 = false, bool hasAdd6 = false,
                                           int keyTonicPc = 0,
                                           KeySigMode keyMode = KeySigMode::Ionian)
{
    ChordAnalysisResult r;
    r.function.degree               = degree;
    r.identity.quality              = quality;
    r.identity.rootPc               = rootPc;
    r.identity.bassPc               = bassPc;
    if (hasMin7) { setExtension(r.identity.extensions, Extension::MinorSeventh); }
    if (hasMaj7) { setExtension(r.identity.extensions, Extension::MajorSeventh); }
    if (hasDim7) { setExtension(r.identity.extensions, Extension::DiminishedSeventh); }
    if (hasAdd6) { setExtension(r.identity.extensions, Extension::AddedSixth); }
    r.function.keyTonicPc           = keyTonicPc;
    r.function.keyMode              = keyMode;
    return r;
}

inline const ChordAnalysisResult* findCandidate(const std::vector<ChordAnalysisResult>& results,
                                                int rootPc,
                                                ChordQuality quality,
                                                bool hasMin7 = false)
{
    for (const auto& result : results) {
        if (result.identity.rootPc != rootPc || result.identity.quality != quality) {
            continue;
        }
        if (hasMin7 && !hasExtension(result.identity.extensions, Extension::MinorSeventh)) {
            continue;
        }
        return &result;
    }
    return nullptr;
}

} // namespace mu::composing::analysis
