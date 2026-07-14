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

#ifndef MU_COMPOSING_ANALYSIS_KEYCOLLECTIONPROBE_H
#define MU_COMPOSING_ANALYSIS_KEYCOLLECTIONPROBE_H

#include <string>

// ── OI-168 measurement scaffolding — DEFAULT-OFF, read-only ────────────────────────────
//
// Measures the magnitude of the OI-168 defect: `analyzeChord`'s two key-consuming terms
// (dim7CharacteristicBonus, diatonicRootContribution) test membership in
// { (keyTonicPc + scale[i]) mod 12 }, which equals the key SIGNATURE's diatonic collection
// only when the mode's tonic offset equals its diatonic parent's — true for 19 of the 21
// KeySigMode values, false for Altered (offset 1) and AlteredDomBB7 (offset 8), whose set is
// the signature's collection transposed up a semitone.
//
// Two independent switches, BOTH read once from the environment at static-init and BOTH
// default-OFF, so an unset environment leaves the production path untouched:
//
//   MU_KEY_COLLECTION_PROBE            counting on; batch_analyze writes <output>.probe.json
//   MU_KEY_COLLECTION_SIGMASK_VARIANT  the A/B: the two membership tests read the signature's
//                                      own diatonic collection instead (the proposed fix's
//                                      form — provably the same set for the 19 delta=0 modes)
//
// The counters are plain integers that NO scoring path ever reads, and the variant flag is
// false unless explicitly set, so production output is byte-identical either way. The whole
// scaffold is removable in one revert (the OI-110 pattern).

namespace mu::composing::analysis::keycollectionprobe {

/// Every counted branch. One block per process; a corpus run writes one file per score.
struct Counters {
    // ── Task A: the sparsechordrefinement Aeolian lone-tonic/dominant guard ──
    /// refineSparseChordQualityFromKeyContext entered with an Unknown-quality chord.
    unsigned long long sparseRefineEntries = 0;
    /// The guard's SHAPE preconditions held (one distinct pitch class, tonic-or-dominant
    /// degree, minor diatonic triad) — evaluated under ANY mode, so a zero here means the
    /// guard is unreachable for reasons other than the Aeolian test.
    unsigned long long sparseGuardShapeMatched = 0;
    /// The guard actually fired (the shape held AND the mode is Aeolian): the chord was left
    /// Unknown instead of hardening to a minor triad.
    unsigned long long sparseAeolianGuardFires = 0;

    // ── Task B: the population the two key-consuming terms are scored under ──
    // Split per call site, because the chord scorer is entered from three places.
    unsigned long long analyzeChordCalls = 0;                ///< every analyzeChord entry
    unsigned long long analyzeChordCallsAltered = 0;
    unsigned long long analyzeChordCallsAlteredDomBB7 = 0;
    unsigned long long regionCommitCalls = 0;                ///< regionanalyzer's committing call
    unsigned long long regionCommitCallsAltered = 0;
    unsigned long long regionCommitCallsAlteredDomBB7 = 0;
    unsigned long long decoderWindowCalls = 0;               ///< ChordSliceDecoder's slice window
    unsigned long long decoderWindowCallsAltered = 0;
    unsigned long long decoderWindowCallsAlteredDomBB7 = 0;

    // ── Task C support: does the corrupted membership give a DIFFERENT verdict? ──
    // Counted per (root, template) cell, at each of the two terms, whether or not the
    // variant is enabled: "tests" is every membership question asked, "differs" is every
    // one the signature collection answers differently from the mode-transposed set.
    unsigned long long dim7MembershipTests = 0;
    unsigned long long dim7MembershipDiffers = 0;
    unsigned long long diatonicRootMembershipTests = 0;
    unsigned long long diatonicRootMembershipDiffers = 0;
};

/// True when MU_KEY_COLLECTION_PROBE is set and non-empty. Read once at static init; the
/// counters do nothing at all when it is false.
extern const bool countingEnabled;

/// True when MU_KEY_COLLECTION_SIGMASK_VARIANT is set and non-empty. Read once at static init.
/// When false (every production run) the two membership tests keep their committed form.
extern const bool signatureMaskVariantEnabled;

/// The process-global counter block.
Counters& counters();

/// Increment \p c, but only while counting is enabled.
inline void bump(unsigned long long& c) noexcept
{
    if (countingEnabled) {
        ++c;
    }
}

/// Write the counters as one JSON object to \p path. A no-op unless counting is enabled, so
/// callers need no guard of their own. Idempotent (writes at most once per process).
void writeCounters(const std::string& path);

} // namespace mu::composing::analysis::keycollectionprobe

#endif // MU_COMPOSING_ANALYSIS_KEYCOLLECTIONPROBE_H
