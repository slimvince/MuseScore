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

// ── Section-level cadence and pivot detection ────────────────────────────────
//
// detectCadences() / detectPivotChords() / hasAssertiveKeyConfidence().
// Lifted verbatim out of section/sectionanalyzer.cpp (byte-identical pure code
// movement) — these three functions are independent of analyzeSection and are
// driven directly by the notation bridge.  Declarations stay in the unchanged
// sectionanalyzer.h.

#include "composing/analysis/section/sectionanalyzer.h"

#include <algorithm>
#include <limits>
#include <string>
#include <vector>

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/region/sparsechordrefinement.h"

namespace cra = mu::composing::analysis::region;

namespace mu::composing::analysis {

// ── Cadence and pivot detection ───────────────────────────────────────────────

bool hasAssertiveKeyConfidence(
    const mu::composing::analysis::KeyModeAnalysisResult& kmr)
{
    // Gates on the emission sigmoid (normalizedConfidence) as an INTERNAL 0.8 threshold
    // — the sigmoid's declared production role (confidence contract §3 / D-L3a: it is a
    // gate input, not the Layer-3 boundary confidence, which is the sequence margin).
    // Input + constant left UNCHANGED by the D-L3a close-out (declaration only).
    return kmr.normalizedConfidence >= kAnnotateKeyConfidenceThreshold;
}

std::vector<CadenceMarker> detectCadences(
    const std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
    size_t selectionCount)
{
    using namespace mu::composing::analysis;

    std::vector<CadenceMarker> markers;

    const size_t total = regions.size();
    if (total == 0 || selectionCount == 0) {
        return markers;
    }

    // Clamp: selectionCount may equal total (no lookahead), that is fine.
    const size_t n = std::min(selectionCount, total);

    // ── PAC / PC / DC ───────────────────────────────────────────────────────
    // Examine consecutive pairs (i, i+1) where i is inside the selection.
    for (size_t i = 0; i + 1 < total && i < n; ++i) {
        if (!hasAssertiveKeyConfidence(regions[i].keyModeResult)
            || !hasAssertiveKeyConfidence(regions[i + 1].keyModeResult)) {
            continue;
        }

        const auto& a = regions[i].chordResult;
        const auto& b = regions[i + 1].chordResult;

        // Cadence requires same key / mode context.
        if (regions[i].keyModeResult.keySignatureFifths
            != regions[i + 1].keyModeResult.keySignatureFifths
            || regions[i].keyModeResult.mode
               != regions[i + 1].keyModeResult.mode) {
            continue;  // key change — not a cadence
        }
        // And different chord roots.
        if (a.identity.rootPc == b.identity.rootPc) {
            continue;
        }

        const char* label = nullptr;

        // PAC: V → I (non-minor dominant) or viio → I (leading-tone diminished).
        if (b.function.degree == 0
            && ((a.function.degree == 4 && a.identity.quality != ChordQuality::Minor)
                || (a.function.degree == 6 && a.identity.quality == ChordQuality::Diminished))) {
            label = "PAC";
        } else if (a.function.degree == 3 && b.function.degree == 0) {
            label = "PC";   // Plagal: IV → I
        } else if (a.function.degree == 4 && b.function.degree == 5
                   && a.identity.quality != ChordQuality::Minor
                   && b.identity.quality == ChordQuality::Minor) {
            label = "DC";   // Deceptive: V → vi
        }

        if (!label) {
            continue;
        }

        // Place the label at the resolution chord tick (b / regions[i+1]).
        // If that chord is in the lookahead region (outside the selection)
        // place it at the preparatory chord instead so the annotation stays
        // within the selection boundary.
        const int writeTick = (i + 1 < n)
            ? regions[i + 1].startTick
            : regions[i].startTick;

        markers.push_back({ writeTick, std::string(label) });
    }

    // ── Half cadence ────────────────────────────────────────────────────────
    // Last in-selection region is degree 4 (dominant arrival).
    if (hasAssertiveKeyConfidence(regions[n - 1].keyModeResult)
        && regions[n - 1].chordResult.function.degree == 4) {
        const int hcTick = regions[n - 1].startTick;
        // Do not emit HC if another cadence label already occupies this tick.
        const bool alreadyLabelled = std::any_of(markers.begin(), markers.end(),
            [hcTick](const CadenceMarker& m) { return m.tick == hcTick; });
        if (!alreadyLabelled) {
            markers.push_back({ hcTick, "HC" });
        }
    }

    return markers;
}

std::vector<PivotLabel> detectPivotChords(
    const std::vector<mu::composing::analysis::AnalyzedRegion>& regions,
    size_t selectionCount)
{
    using namespace mu::composing::analysis;

    std::vector<PivotLabel> labels;

    if (regions.empty() || selectionCount == 0) {
        return labels;
    }

    const size_t total = regions.size();
    const size_t n = std::min(selectionCount, total);

    // Walk all regions (including lookahead) to find assertive key transitions.
    // A transition occurs when consecutive assertive regions disagree on key/mode.
    struct KeyTransition {
        size_t boundaryIdx;  // index of first region in the new (incoming) key
        int oldFifths;
        KeySigMode oldMode;
        int newFifths;
        KeySigMode newMode;
    };

    std::vector<KeyTransition> transitions;
    int prevFifths  = std::numeric_limits<int>::min();
    KeySigMode prevMode = KeySigMode::Ionian;

    for (size_t i = 0; i < total; ++i) {
        const auto& km = regions[i].keyModeResult;
        if (!hasAssertiveKeyConfidence(km)) {
            continue;
        }
        if (prevFifths == std::numeric_limits<int>::min()) {
            // First assertive region establishes the baseline key.
            prevFifths = km.keySignatureFifths;
            prevMode   = km.mode;
            continue;
        }
        if (km.keySignatureFifths != prevFifths || km.mode != prevMode) {
            // Key has changed — record the transition.
            transitions.push_back({ i, prevFifths, prevMode,
                                     km.keySignatureFifths, km.mode });
            prevFifths = km.keySignatureFifths;
            prevMode   = km.mode;
        }
    }

    for (const auto& tr : transitions) {
        // Confirm that the new key is stable by finding at least one more
        // assertive region beyond the boundary that agrees with it.
        // Limit the search to kMaxPivotLookaheadRegions past the boundary.
        bool confirmed = false;
        const size_t searchEnd = std::min(tr.boundaryIdx + 1
                                          + static_cast<size_t>(kMaxPivotLookaheadRegions),
                                          total);
        for (size_t k = tr.boundaryIdx + 1; k < searchEnd; ++k) {
            const auto& km = regions[k].keyModeResult;
            if (hasAssertiveKeyConfidence(km)
                && km.keySignatureFifths == tr.newFifths
                && km.mode == tr.newMode) {
                confirmed = true;
                break;
            }
        }
        if (!confirmed) {
            continue;  // new key not confirmed — suppress pivot to avoid false positive
        }

        // Build the incoming key's tonic pitch class (still needed for keyTonicPc).
        const int newIonianPc = ionianTonicPcFromFifths(tr.newFifths);
        const int newTonicPc  = (newIonianPc + keyModeTonicOffset(tr.newMode)) % 12;

        // Walk backward from the boundary through the in-selection regions,
        // looking for the first chord that is:
        //   (a) diatonic to the outgoing key  (function.degree >= 0), AND
        //   (b) its root pitch class is in the incoming key's scale.
        const size_t searchBack = std::min(tr.boundaryIdx, n);  // stay in selection
        for (size_t j = searchBack; j > 0; --j) {
            const size_t idx = j - 1;
            const auto& prev = regions[idx].chordResult;

            if (prev.function.degree < 0) {
                continue;  // not diatonic to outgoing key
            }
            if (cra::diatonicDegreeForRootPc(prev.identity.rootPc, tr.newFifths, tr.newMode) < 0) {
                continue;  // root not in incoming scale
            }

            // Found the pivot chord.  Format in both keys.
            const std::string oldRoman = ChordSymbolFormatter::formatRomanNumeral(prev);

            // Compute the degree in the incoming key.
            ChordAnalysisResult pivotInNew = prev;
            pivotInNew.function.degree = cra::diatonicDegreeForRootPc(
                prev.identity.rootPc, tr.newFifths, tr.newMode);
            pivotInNew.function.diatonicToKey = (pivotInNew.function.degree >= 0);
            pivotInNew.function.keyTonicPc = newTonicPc;
            pivotInNew.function.keyMode    = tr.newMode;
            const std::string newRoman = ChordSymbolFormatter::formatRomanNumeral(pivotInNew);

            if (!oldRoman.empty() && !newRoman.empty()) {
                // U+2192 RIGHT ARROW — pivot chord separator (same encoding
                // used in the chord staff path).
                labels.push_back({ regions[idx].startTick,
                                   oldRoman + " \u2192 " + newRoman });
            }
            break;  // one pivot per key transition
        }
    }

    return labels;
}

} // namespace mu::composing::analysis
