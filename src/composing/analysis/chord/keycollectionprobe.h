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

// ── OI-168 / OI-170 measurement scaffolding — DEFAULT-OFF, read-only ───────────────────
//
// Two switches, read once from the environment at static init and both default-OFF, so an
// unset environment leaves the production path untouched:
//
//   MU_KEY_COLLECTION_PROBE            counting on; batch_analyze writes <output>.probe.json
//   MU_KEY_COLLECTION_SIGMASK_VARIANT  the A/B: the THREE remaining collection-membership sites
//                                      (OI-170) test the key SIGNATURE's collection instead of
//                                      the mode-tonic-anchored set
//
// The counters are plain integers that NO scoring path ever reads, and the variant flag is false
// unless set, so production output is byte-identical either way. The whole scaffold is removable
// in one revert (the OI-110 pattern).
//
// WHAT IS MEASURED HERE
//
//   OI-168 (the adopted fix — `cc_oi168_fix_report.md`; the two key-consuming SCORING terms now
//   take the signature collection and no tonic):
//   * the population the chord scorer runs under (calls per key mode, split by call site) —
//     the counters that established that `Altered` is Jazz-only, `AlteredDomBB7` is 0-firing,
//     and the `ChordSliceDecoder` is NOT on the production path;
//   * the `sparsechordrefinement` Aeolian lone-tonic/dominant guard's fire count — the
//     evidence for OI-167 / OI-102's still-open disposition of that file.
//
//   OI-170 (the three sites the OI-168 fix did NOT reach — all on the live region path, all
//   asking a pure COLLECTION-membership question through the TONIC, all carrying the identical
//   δ≠0 corruption on Altered / AlteredDomBB7):
//   * `buildChordResult`'s `diatonicToKey` flag (a PUBLISHED fact);
//   * Gate I's `invRootIsDiatonic` and Gate L's `invRootIsDiatonic` (both SWAP the committed
//     winner when they fire — decision-bearing, not cosmetic).
//   Each site evaluates BOTH predicates whenever counting is on and reports how often they
//   differ; the SIGMASK_VARIANT switch decides which one the code actually uses. The two
//   decision-bearing gates additionally count the cases where the differing predicate would
//   change the gate's swap decision (every other conjunct of the gate passing) — that is the
//   per-gate attribution of any committed-chord flip.
//
//   The two LIVE class-(b) (genuine-tonic) sites' magnitude, which the fix design must account
//   for because the signature mask cannot replace them: Gate G-E's degree test, and
//   `applyTonicPriorToSparseChord`'s degree→triad-quality overwrite on the commit path.
//
// The `…MembershipTests` / `…MembershipDiffers` counters of the OI-168 A/B are gone with the
// terms they measured (the fix deleted the mode-transposed branch, so a "differs" counter there
// would compare a set against itself and report a structural zero — a false instrument, #19).
// The counters below measure the sites where the two forms still genuinely differ.

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

    // ── OI-170 site 1: buildChordResult's diatonicToKey flag ──
    /// buildChordResult reached the diatonic check (both predicates evaluated).
    unsigned long long diatonicFlagTests = 0;
    /// The mode-transposed verdict and the signature-collection verdict DIFFER for this chord.
    unsigned long long diatonicFlagDiffers = 0;

    // ── OI-170 site 2: Gate I's invRootIsDiatonic ──
    /// The membership test was reached (a candidate passed every earlier conjunct).
    unsigned long long gateIDiatonicTests = 0;
    /// The two predicates disagree on this candidate.
    unsigned long long gateIDiatonicDiffers = 0;
    /// They disagree AND every remaining conjunct passes — i.e. the SWAP decision itself differs.
    unsigned long long gateISwapDiffers = 0;

    // ── OI-170 site 3: Gate L's invRootIsDiatonic ──
    unsigned long long gateLDiatonicTests = 0;
    unsigned long long gateLDiatonicDiffers = 0;
    unsigned long long gateLSwapDiffers = 0;

    // ── The live class-(b) (genuine-tonic) sites, for magnitude ──
    /// Gate G-E's key-context degree test fired (the winner was swapped to the HalfDim reading).
    unsigned long long gateGEFires = 0;
    /// applyTonicPriorToSparseChord was entered with a thin (Power/Sus2/Sus4) chord.
    unsigned long long tonicPriorEntries = 0;
    /// …and it overwrote the committed quality with the degree's diatonic triad quality.
    unsigned long long tonicPriorApplied = 0;
};

/// True when MU_KEY_COLLECTION_PROBE is set and non-empty. Read once at static init; the
/// counters do nothing at all when it is false.
extern const bool countingEnabled;

/// True when MU_KEY_COLLECTION_SIGMASK_VARIANT is set and non-empty. Read once at static init.
/// The three OI-170 sites take the key signature's collection instead of the mode-transposed
/// set when this is true. FALSE in production — the default path is unchanged.
extern const bool signatureMaskVariant;

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
