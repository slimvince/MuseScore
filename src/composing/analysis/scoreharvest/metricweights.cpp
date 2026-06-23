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

#include "metricweights.h"

#include <algorithm>
#include <cmath>

#include "engraving/dom/measure.h"
#include "engraving/dom/pedal.h"
#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/spanner.h"
#include "engraving/types/fraction.h"
#include "engraving/types/types.h"

namespace mu::composing::analysis::scoreharvest {

double beatTypeToWeight(mu::engraving::BeatType bt,
                        const KeyModeAnalyzerPreferences& prefs)
{
    using mu::engraving::BeatType;
    switch (bt) {
    case BeatType::DOWNBEAT:              return prefs.beatWeightDownbeat;
    case BeatType::COMPOUND_STRESSED:     return prefs.beatWeightCompoundStressed;
    case BeatType::SIMPLE_STRESSED:       return prefs.beatWeightSimpleStressed;
    case BeatType::COMPOUND_UNSTRESSED:   return prefs.beatWeightCompoundUnstressed;
    case BeatType::SIMPLE_UNSTRESSED:     return prefs.beatWeightSimpleUnstressed;
    case BeatType::COMPOUND_SUBBEAT:      return prefs.beatWeightCompoundSubbeat;
    case BeatType::SUBBEAT:               return prefs.beatWeightSubbeat;
    }
    return prefs.beatWeightSubbeat;
}

mu::engraving::BeatType safeBeatType(const mu::engraving::Measure* measure,
                                     const mu::engraving::Segment* segment)
{
    using namespace mu::engraving;

    if (!measure || !segment) {
        return BeatType::SUBBEAT;
    }

    const int numerator = measure->timesig().numerator();
    const int denominator = measure->timesig().denominator();
    if (numerator <= 0 || denominator <= 0) {
        return BeatType::SUBBEAT;
    }

    return TimeSigFrac(numerator, denominator).rtick2beatType(segment->rtick().ticks());
}

double regionMetricWeightForBeatType(mu::engraving::BeatType bt)
{
    using mu::engraving::BeatType;
    switch (bt) {
    case BeatType::DOWNBEAT:            return 1.0;
    case BeatType::SIMPLE_STRESSED:
    case BeatType::COMPOUND_STRESSED:   return 0.85;
    case BeatType::SIMPLE_UNSTRESSED:
    case BeatType::COMPOUND_UNSTRESSED: return 0.75;
    default:                            return 0.5;
    }
}

mu::engraving::BeatType beatTypeForOnsetTick(const mu::engraving::Score* sc, int onsetTick)
{
    using namespace mu::engraving;
    if (!sc) {
        return BeatType::SUBBEAT;
    }
    const Measure* m = sc->tick2measure(Fraction::fromTicks(onsetTick));
    if (!m) {
        return BeatType::SUBBEAT;
    }
    const int num = m->timesig().numerator();
    const int den = m->timesig().denominator();
    if (num <= 0 || den <= 0) {
        return BeatType::SUBBEAT;
    }
    const int rtick = onsetTick - m->tick().ticks();
    return TimeSigFrac(num, den).rtick2beatType(rtick);
}

double regionMetricWeightForOnsetTick(const mu::engraving::Score* sc, int onsetTick)
{
    return regionMetricWeightForBeatType(beatTypeForOnsetTick(sc, onsetTick));
}

double timeDecay(double beatsAgo, double decayRate, double beatsPerUnit)
{
    return std::pow(decayRate, beatsAgo / beatsPerUnit);
}

int distinctPitchClasses(const std::vector<KeyModeAnalyzer::PitchContext>& ctx)
{
    bool seen[12] = {};
    int count = 0;
    for (const auto& p : ctx) {
        // PitchContext.pitch is a non-negative ppitch value (note->ppitch()).
        const int pc = p.pitch % 12;
        if (!seen[pc]) {
            seen[pc] = true;
            ++count;
        }
    }
    return count;
}

std::map<std::size_t, std::vector<PedalWindow>>
buildPedalWindowIndex(const mu::engraving::Score* sc,
                      int startTickInt,
                      int endTickInt,
                      const std::set<std::size_t>& excludeStaves,
                      const StaffEligibilityPredicate& isStaffEligible)
{
    using namespace mu::engraving;

    std::map<std::size_t, std::vector<PedalWindow>> result;
    for (const auto& spannerEntry : sc->spanner()) {
        const Spanner* spanner = spannerEntry.second;
        if (!spanner || spanner->type() != ElementType::PEDAL) {
            continue;
        }

        const Pedal* pedal = toPedal(spanner);
        if (!pedal) {
            continue;
        }

        const auto& beginText = pedal->beginText();
        if (beginText == u"<sym>keyboardPedalSost</sym>" || beginText == u"<sym>keyboardPedalS</sym>") {
            continue;
        }

        const int pedalStartTick = pedal->tick().ticks();
        const int pedalEndTick = pedal->tick2().ticks();
        if (pedalEndTick <= pedalStartTick || pedalEndTick <= startTickInt || pedalStartTick >= endTickInt) {
            continue;
        }

        const std::size_t staffIdx = static_cast<std::size_t>(pedal->track() / VOICES);
        if (staffIdx >= sc->nstaves() || excludeStaves.count(staffIdx) || !isStaffEligible(staffIdx)) {
            continue;
        }

        result[staffIdx].push_back({ pedalStartTick, pedalEndTick });
    }

    for (auto& entry : result) {
        auto& windows = entry.second;
        std::sort(windows.begin(), windows.end(), [](const PedalWindow& lhs, const PedalWindow& rhs) {
            if (lhs.startTick != rhs.startTick) {
                return lhs.startTick < rhs.startTick;
            }
            return lhs.endTick < rhs.endTick;
        });
    }

    return result;
}

} // namespace mu::composing::analysis::scoreharvest
