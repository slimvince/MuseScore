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

#include "composing/analysis/keymodeguesser.h"

using namespace mu::composing::analysis;

namespace {

KeyModeGuesser::PitchContext makePitch(int pitch, double durationWeight, double beatWeight, bool isBass)
{
    KeyModeGuesser::PitchContext p;
    p.pitch = pitch;
    p.durationWeight = durationWeight;
    p.beatWeight = beatWeight;
    p.isBass = isBass;
    return p;
}

} // namespace

TEST(Composing_KeyModeGuesserTests, PrefersCMajorForCMajorPitchSet)
{
    const std::vector<KeyModeGuesser::PitchContext> pitches = {
        makePitch(60, 2.0, 1.0, true),
        makePitch(64, 1.0, 1.0, false),
        makePitch(67, 1.0, 1.0, false),
        makePitch(71, 1.0, 0.8, false)
    };

    const KeyModeGuessResult result = KeyModeGuesser::guessKeyMode(pitches, 0);

    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(result.keySignatureFifths, 0);
    EXPECT_TRUE(result.isMajor);
}

TEST(Composing_KeyModeGuesserTests, PrefersAminorWhenAeolianEvidenceIsStrong)
{
    const std::vector<KeyModeGuesser::PitchContext> pitches = {
        makePitch(57, 2.0, 1.0, true),
        makePitch(60, 1.0, 1.0, false),
        makePitch(64, 1.0, 1.0, false),
        makePitch(67, 1.0, 0.8, false)
    };

    const KeyModeGuessResult result = KeyModeGuesser::guessKeyMode(pitches, 0);

    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(result.keySignatureFifths, 0);
    EXPECT_FALSE(result.isMajor);
}
