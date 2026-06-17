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

#include "chordanalyzer.h"

#include <algorithm>
#include <cmath>
#include <vector>

namespace mu::composing::analysis {

// ── chordTonePitchClasses ─────────────────────────────────────────────────────

std::vector<int> chordTonePitchClasses(const ChordAnalysisResult& result)
{
    const int r = result.identity.rootPc;
    auto pc = [&](int semitones) { return (r + semitones) % 12; };

    // Start with the triad implied by quality.
    // Third slot:
    int thirdInterval = -1;  // -1 = no third
    switch (result.identity.quality) {
    case ChordQuality::Major:
    case ChordQuality::Augmented:
        thirdInterval = 4;
        break;
    case ChordQuality::Minor:
    case ChordQuality::Diminished:
    case ChordQuality::HalfDiminished:
        thirdInterval = 3;
        break;
    case ChordQuality::Suspended2:
        thirdInterval = 2;
        break;
    case ChordQuality::Suspended4:
        thirdInterval = 5;
        break;
    case ChordQuality::Power:
    case ChordQuality::Unknown:
        thirdInterval = -1;
        break;
    }

    // Fifth slot:
    int fifthInterval = -1;
    switch (result.identity.quality) {
    case ChordQuality::Major:
    case ChordQuality::Minor:
    case ChordQuality::Suspended2:
    case ChordQuality::Suspended4:
    case ChordQuality::Power:
        fifthInterval = 7;
        break;
    case ChordQuality::Diminished:
    case ChordQuality::HalfDiminished:
        fifthInterval = 6;
        break;
    case ChordQuality::Augmented:
        fifthInterval = 8;
        break;
    case ChordQuality::Unknown:
        fifthInterval = -1;
        break;
    }

    // Apply fifth alterations (override the quality's default).
    if (hasExtension(result.identity.extensions, Extension::FlatFifth) && fifthInterval == 7) {
        fifthInterval = 6;
    }
    if (hasExtension(result.identity.extensions, Extension::SharpFifth) && fifthInterval == 7) {
        fifthInterval = 8;
    }

    // Collect: root is always first.
    std::vector<int> pcs;
    pcs.push_back(r);

    // Third (skip if omitted).
    if (thirdInterval >= 0 && !hasExtension(result.identity.extensions, Extension::OmitsThird)) {
        pcs.push_back(pc(thirdInterval));
    }

    // Fifth.
    if (fifthInterval >= 0) {
        pcs.push_back(pc(fifthInterval));
    }

    // Seventh.
    if (hasExtension(result.identity.extensions, Extension::MajorSeventh)) {
        pcs.push_back(pc(11));
    } else if (hasExtension(result.identity.extensions, Extension::MinorSeventh)) {
        pcs.push_back(pc(10));
    } else if (hasExtension(result.identity.extensions, Extension::DiminishedSeventh)) {
        pcs.push_back(pc(9));
    }
    // HalfDiminished has a structural minor 7th not flagged as hasMinorSeventh.
    if (result.identity.quality == ChordQuality::HalfDiminished
        && !hasExtension(result.identity.extensions, Extension::MinorSeventh) && !hasExtension(result.identity.extensions, Extension::MajorSeventh)) {
        pcs.push_back(pc(10));
    }

    // Added sixth (when no seventh — otherwise it's a 13th).
    if (hasExtension(result.identity.extensions, Extension::AddedSixth) && !hasExtension(result.identity.extensions, Extension::MinorSeventh)
        && !hasExtension(result.identity.extensions, Extension::MajorSeventh) && !hasExtension(result.identity.extensions, Extension::DiminishedSeventh)) {
        pcs.push_back(pc(9));
    }

    // Upper extensions.
    if (hasExtension(result.identity.extensions, Extension::FlatNinth)) {
        pcs.push_back(pc(1));
    }
    if (hasExtension(result.identity.extensions, Extension::NaturalNinth)) {
        pcs.push_back(pc(2));
    }
    if (hasExtension(result.identity.extensions, Extension::SharpNinth)) {
        pcs.push_back(pc(3));
    }
    if (hasExtension(result.identity.extensions, Extension::NaturalEleventh)) {
        pcs.push_back(pc(5));
    }
    if (hasExtension(result.identity.extensions, Extension::SharpEleventh)) {
        pcs.push_back(pc(6));
    }
    if (hasExtension(result.identity.extensions, Extension::NaturalThirteenth)) {
        pcs.push_back(pc(9));
    }
    if (hasExtension(result.identity.extensions, Extension::FlatThirteenth)) {
        pcs.push_back(pc(8));
    }
    if (hasExtension(result.identity.extensions, Extension::SharpThirteenth)) {
        pcs.push_back(pc(10));
    }

    // Deduplicate (extensions may overlap with triad tones in pitch-class space).
    std::vector<int> unique;
    unique.push_back(pcs[0]);  // root always first
    for (size_t i = 1; i < pcs.size(); ++i) {
        bool dup = false;
        for (int u : unique) {
            if (u == pcs[i]) { dup = true; break; }
        }
        if (!dup) {
            unique.push_back(pcs[i]);
        }
    }

    // Sort upper tones (everything after root) ascending from root.
    if (unique.size() > 1) {
        std::sort(unique.begin() + 1, unique.end(), [&](int a, int b) {
            int relA = (a - r + 12) % 12;
            int relB = (b - r + 12) % 12;
            return relA < relB;
        });
    }

    return unique;
}

// ── closePositionVoicing ─────────────────────────────────────────────────────

ClosePositionVoicing closePositionVoicing(const ChordAnalysisResult& result)
{
    if (result.identity.quality == ChordQuality::Unknown) {
        return {};
    }

    const std::vector<int> pcs = chordTonePitchClasses(result);
    if (pcs.empty()) {
        return {};
    }

    ClosePositionVoicing v;

    // Bass: root in C2–C3 (MIDI 36–48), nearest to midpoint 42.
    const int rootPc = pcs[0];
    {
        constexpr int kBassLow = 36;   // C2
        constexpr int kBassMid = 42;   // F#2
        // Find the octave placement nearest to midpoint.
        int best = kBassLow + rootPc;
        if (best < kBassLow) {
            best += 12;
        }
        // Check one octave up too, pick closer to midpoint.
        if (best + 12 <= 48 && std::abs(best + 12 - kBassMid) < std::abs(best - kBassMid)) {
            best += 12;
        }
        v.bassPitch = best;
    }

    // Treble: upper tones in close position above C4 (MIDI 60).
    // Each successive tone is placed ascending from the previous, within one octave.
    if (pcs.size() > 1) {
        constexpr int kTrebleFloor = 60;  // C4
        int prev = kTrebleFloor;

        for (size_t i = 1; i < pcs.size(); ++i) {
            // Place this pc at or above prev.
            int pitch = kTrebleFloor + pcs[i];
            // Normalize into the correct octave: at or above prev.
            while (pitch < prev) {
                pitch += 12;
            }
            // If it jumped more than an octave above the floor, bring it down.
            // (Only possible for the first tone; subsequent tones just stack.)
            v.treblePitches.push_back(pitch);
            prev = pitch;
        }
    }

    return v;
}

} // namespace mu::composing::analysis
