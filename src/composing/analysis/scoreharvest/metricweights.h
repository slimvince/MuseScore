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

// ── scoreharvest/metricweights ───────────────────────────────────────────────
//
// Shared metric weights, sliding-window constants, and trivial score-walking
// helpers used by both the notation bridge and tools/batch_analyze.cpp.
//
// This module lives inside composing_analysis so tools/batch_analyze.cpp
// (which links against composing but NOT against notation/internal) can call
// the same implementation as the bridge. See docs/duplication_audit.md §5.8.

#include <cstddef>
#include <functional>
#include <map>
#include <set>
#include <vector>

#include "engraving/types/constants.h"
#include "engraving/dom/sig.h"      // for mu::engraving::BeatType

#include "../key/keymodeanalyzer.h"

namespace mu::engraving {
class Score;
class Measure;
class Segment;
}

namespace mu::composing::analysis::scoreharvest {

// ── Sliding-window constants ─────────────────────────────────────────────────
//
// Used by collectPitchContext() and inferLocalKey() / resolveKeyAndMode() to
// build the windowed pitch evidence around an analysis tick.

inline constexpr int    LOOKBACK_BEATS   = 16;
inline constexpr int    LOOKAHEAD_BEATS  = 8;
inline constexpr double LOOKAHEAD_WEIGHT = 0.5;
inline constexpr double DECAY_RATE       = 0.7;   // multiplier per measure (4 quarter notes)

// ── Region-size thresholds ───────────────────────────────────────────────────
//
// kMinRegionTicks         — Pass 3 absorbShortRegions threshold (1 quarter note).
// kPass2bMinRegionTicks   — minimum parent-region duration eligible for
//                           Pass 2b bass-movement sub-boundary detection (4 quarter notes).

inline constexpr int kMinRegionTicks       = mu::engraving::Constants::DIVISION;
inline constexpr int kPass2bMinRegionTicks = 4 * mu::engraving::Constants::DIVISION;

// ── Trivial helpers ──────────────────────────────────────────────────────────

/// Map MuseScore's BeatType enum to a weight for key/mode analysis.
double beatTypeToWeight(mu::engraving::BeatType bt,
                        const KeyModeAnalyzerPreferences& prefs);

/// Return BeatType safely, falling back to SUBBEAT for null or invalid inputs.
mu::engraving::BeatType safeBeatType(const mu::engraving::Measure* measure,
                                     const mu::engraving::Segment* segment);

/// Normalised metric weight [0,1] for a beat type:
///   1.0 = downbeat, 0.85 = stressed, 0.75 = unstressed, 0.5 = subbeat.
double regionMetricWeightForBeatType(mu::engraving::BeatType bt);

/// BeatType at an absolute onset tick, via an INDEXED measure lookup
/// (Score::tick2measure) + the onset's rtick — no segment walk. The index-friendly
/// form (distinct input domain from the segment-taking safeBeatType): the single
/// source for "what beat does this tick fall on" used by both pitchContextOverSpan
/// (key path) and the Layer-4 membership decision (chord path). Falls back to
/// SUBBEAT for null score / no measure / invalid time signature.
mu::engraving::BeatType beatTypeForOnsetTick(const mu::engraving::Score* sc, int onsetTick);

/// Normalised metric weight [0.5,1.0] at an absolute onset tick (indexed) —
/// regionMetricWeightForBeatType(beatTypeForOnsetTick(sc, onsetTick)). The
/// prefs-free per-note metric weight the Layer-4 membership decision reads off the
/// Layer-1 NoteEvent stream (a weak/off-beat note is embellishment-like).
double regionMetricWeightForOnsetTick(const mu::engraving::Score* sc, int onsetTick);

/// Exponential time decay: notes further from the analysis tick carry less weight.
/// `beatsPerUnit` is the length-scale (beats per decay step; one 4/4 measure by
/// default). The default keeps every existing caller byte-identical; the windowed
/// pitch-context view passes it explicitly so the length-scale is a setting, not a
/// magic number.
double timeDecay(double beatsAgo, double decayRate = DECAY_RATE, double beatsPerUnit = 4.0);

/// Count distinct pitch classes in a PitchContext vector.
int distinctPitchClasses(const std::vector<KeyModeAnalyzer::PitchContext>& ctx);

// ── Pedal-window index ───────────────────────────────────────────────────────

/// A sustain-pedal span on a single staff, expressed as absolute tick range.
struct PedalWindow {
    int startTick = 0;
    int endTick   = 0;
};

/// Predicate testing whether a staff is eligible for harmonic analysis at the
/// caller's analysis tick.  The caller's lambda is expected to capture the
/// tick context (the bridge uses the tick-aware staffIsEligible overload from
/// notationanalysisinternal.h; batch_analyze uses its own non-tick overload).
using StaffEligibilityPredicate = std::function<bool(std::size_t staffIdx)>;

/// Collect sustain-pedal spans that overlap [startTickInt, endTickInt), grouped
/// by staff.  Sostenuto and soft pedals are skipped.  Staves in @p excludeStaves
/// or for which @p isStaffEligible returns false are dropped.  Each per-staff
/// vector is sorted by (startTick, endTick).
std::map<std::size_t, std::vector<PedalWindow>>
buildPedalWindowIndex(const mu::engraving::Score* sc,
                      int startTickInt,
                      int endTickInt,
                      const std::set<std::size_t>& excludeStaves,
                      const StaffEligibilityPredicate& isStaffEligible);

} // namespace mu::composing::analysis::scoreharvest
