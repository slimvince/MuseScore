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

#include <gtest/gtest.h>

#include "composing/analysis/chordanalyzer.h"

using namespace mu::composing::analysis;

namespace {

std::vector<ChordAnalysisTone> tones(std::initializer_list<int> pitches)
{
    std::vector<ChordAnalysisTone> out;
    out.reserve(pitches.size());

    bool first = true;
    for (int p : pitches) {
        ChordAnalysisTone t;
        t.pitch = p;
        t.weight = 1.0;
        t.isBass = first;
        out.push_back(t);
        first = false;
    }

    return out;
}

} // namespace

TEST(Composing_ChordAnalyzerTests, DetectsMajorTriadInCMajor)
{
    const auto result = ChordAnalyzer::analyzeChord(tones({60, 64, 67}), true);

    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(result, 0), "CMaj");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(result, true), "I");
}

TEST(Composing_ChordAnalyzerTests, DetectsMinorTriadInCMinor)
{
    const auto result = ChordAnalyzer::analyzeChord(tones({60, 63, 67}), false);

    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(result, -3), "Cm");
    EXPECT_EQ(ChordSymbolFormatter::formatRomanNumeral(result, false), "i");
}

TEST(Composing_ChordAnalyzerTests, DetectsMinorSeventhQuality)
{
    const auto result = ChordAnalyzer::analyzeChord(tones({64, 67, 71, 74}), true);

    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(result, 0), "Em7");
    EXPECT_EQ(result.quality, ChordQuality::Minor);
    EXPECT_TRUE(result.hasMinorSeventh);
}

TEST(Composing_ChordAnalyzerTests, KeepsFlatBassSpellingInFlatKey)
{
    const auto result = ChordAnalyzer::analyzeChord(tones({70, 75, 79}), false);

    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(ChordSymbolFormatter::formatSymbol(result, -3), "EbMaj/Bb");
}
