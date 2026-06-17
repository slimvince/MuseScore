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
#include <cstdint>
#include <set>
#include <utility>
#include <vector>

namespace mu::composing::analysis {
namespace {

/// Returns true if bassPc is a chord tone of the chord identified by (rootPc, quality,
/// extensions).  Used by the two-pass pedal detection to decide whether the bass note
/// belongs to the upper-voice chord or is a structural pedal point.
///
/// Checks: (1) quality-defined triad intervals, (2) 7th/9th extensions that are
/// explicitly detected in the extension bitmask.  This correctly handles F13/Eb
/// (Eb = m7 of F, MinorSeventh set → true → no pedal detected) and HalfDiminished
/// (m7 is implicit in that quality → true for interval 10).
static bool cptIsBassChordTone(int bassPc, int rootPc, ChordQuality quality, uint32_t extensions)
{
    const int interval = (bassPc - rootPc + 12) % 12;
    if (interval == 0) {
        return true; // root is always a chord tone
    }

    // Quality-defined triad intervals
    switch (quality) {
    case ChordQuality::Major:
        if (interval == 4 || interval == 7) { return true; }
        break;
    case ChordQuality::Minor:
        if (interval == 3 || interval == 7) { return true; }
        break;
    case ChordQuality::Diminished:
        if (interval == 3 || interval == 6) { return true; }
        break;
    case ChordQuality::HalfDiminished:
        if (interval == 3 || interval == 6 || interval == 10) { return true; }
        break;
    case ChordQuality::Augmented:
        if (interval == 4 || interval == 8) { return true; }
        break;
    case ChordQuality::Suspended2:
        if (interval == 2 || interval == 7) { return true; }
        break;
    case ChordQuality::Suspended4:
        if (interval == 5 || interval == 7) { return true; }
        break;
    case ChordQuality::Power:
        if (interval == 7) { return true; }
        break;
    default:
        break;
    }

    // 7th/9th/11th/13th extensions explicitly detected in the bitmask.
    // A bass note that matches any detected extension is a chord tone — the chord
    // should be labelled as a slash chord (Cm7/F) rather than a pedal point.
    if (interval == 10 && hasExtension(extensions, Extension::MinorSeventh))      { return true; }
    if (interval == 11 && hasExtension(extensions, Extension::MajorSeventh))      { return true; }
    if (interval == 9  && hasExtension(extensions, Extension::DiminishedSeventh)) { return true; }
    if (interval == 1  && hasExtension(extensions, Extension::FlatNinth))         { return true; }
    if (interval == 2  && hasExtension(extensions, Extension::NaturalNinth))      { return true; }
    if (interval == 3  && hasExtension(extensions, Extension::SharpNinth))        { return true; }
    if (interval == 5  && hasExtension(extensions, Extension::NaturalEleventh))   { return true; }
    if (interval == 6  && hasExtension(extensions, Extension::SharpEleventh))     { return true; }
    if (interval == 8  && hasExtension(extensions, Extension::FlatThirteenth))    { return true; }
    if (interval == 9  && hasExtension(extensions, Extension::NaturalThirteenth)) { return true; }

    // If the chord carries any 7th, the perfect 4th above the root (interval 5,
    // natural 11th) is a valid chord tone even when it sits exactly at the
    // extension-detection threshold (detectExtensions uses strict '>').
    // This correctly handles Cm7/F where F's pcWeight equals kExtensionThreshold
    // and NaturalEleventh is therefore not formally detected, but the chord still
    // qualifies as a slash chord rather than a pedal point.
    // A bare triad (no 7th detected) still triggers pedal detection normally.
    const bool hasAnySeventh = hasExtension(extensions, Extension::MinorSeventh)
                            || hasExtension(extensions, Extension::MajorSeventh)
                            || hasExtension(extensions, Extension::DiminishedSeventh);
    if (interval == 5 && hasAnySeventh) { return true; }

    return false;
}

} // namespace

// ── Iter 86 / Iter 91 / pedal-point tail (extracted from analyzeChord) ──────
//
// See the declaration in chordanalyzer.h for the rationale.  All inputs come from
// the PostScoringGateContext captured by analyzeChord(); the temporal context (for
// Iter 91's nextRootPc) is passed separately.  The pedal Pass-2 sub-analysis
// re-invokes analyzeChord() and then re-applies this same tail to its result —
// replicating the recursive behaviour the inline version had (the nested
// analyzeChord() previously ran its own Iter 86/91/pedal tail).
void applyIter8691Pedal(
    std::vector<ChordAnalysisResult>&  results,
    const PostScoringGateContext&      gateCtx,
    const ChordTemporalContext*        context,
    const ChordAnalyzerPreferences&    prefs)
{
    const int bassPc = gateCtx.bassPc;

    // Build a ChordAnalysisResult from a RawCandidate using the captured context
    // (mirrors the buildResult lambda in applyPostScoringGates / analyzeChord).
    const auto buildResult = [&](const RawCandidate& rc) -> ChordAnalysisResult {
        return buildChordResult(rc,
            BuildChordResultContext{ gateCtx.pcWeight, gateCtx.tpcForPc,
                                     gateCtx.bassPc, gateCtx.bassTpc,
                                     gateCtx.keyTonicPc, gateCtx.keyMode,
                                     gateCtx.scale },
            prefs);
    };

    // ── Iter 86 — bass-b7 promotion ──────────────────────────────────────────
    // If the winner is a Major or Minor triad whose bass is the b7 of the
    // root (interval 10) and that b7 is genuinely present in the score, stamp
    // the MinorSeventh extension so the chord symbol (Am7/G) and Roman numeral
    // (i65 / V42) match the literal slash-bass that the symbol formatter
    // already emits.  Also suppresses spurious pedal-point classification on
    // these cases — once MinorSeventh is stamped, cptIsBassChordTone() treats
    // interval 10 as a chord tone and the pedal check below is skipped.
    if (!results.empty() && bassPc >= 0) {
        ChordAnalysisResult& winner = results.front();
        const ChordQuality q = winner.identity.quality;
        const int rPc        = winner.identity.rootPc;
        const bool bassIsB7  = (bassPc != rPc)
                               && ((bassPc - rPc + 12) % 12) == 10;
        const bool isPlainTriad = (q == ChordQuality::Major || q == ChordQuality::Minor)
                                  && !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                                  && !hasExtension(winner.identity.extensions, Extension::MajorSeventh);
        if (bassIsB7
            && isPlainTriad
            && gateCtx.pcWeight[static_cast<size_t>(bassPc)] > prefs.extensionThreshold) {
            setExtension(winner.identity.extensions, Extension::MinorSeventh);
        }
    }

    // ── Iter 91 — bass-as-root promotion (forward-context gated) ─────────────
    // When the winner is a Major/Minor plain-triad slash chord and the bass
    // sits a third (m3 or M3) above the root — Patterns A and B from the
    // iii/III ambiguity study (docs/iter90_bass_as_root_promotion_shelved.md):
    //   Pattern A: bassPc - rootPc ≡ 8 (mod 12), winner Minor — e.g. Em/C → C
    //   Pattern B: bassPc - rootPc ≡ 9 (mod 12), winner Major — e.g. C/A  → Am
    // promote the bass-rooted reading IF the following region's inferred
    // root equals the current bass (context->nextRootPc == bassPc).  That
    // forward resolution is the structural signal that the current bass is
    // the chord root, not the third of an iii/III triad.  previousRootPc was
    // deliberately omitted — it fired too broadly on genuine I → I6
    // progressions where the previous chord shares the iii/III root.
    if (!results.empty()
        && bassPc >= 0
        && context != nullptr
        && context->nextRootPc != -1
        && context->nextRootPc == bassPc) {
        ChordAnalysisResult& winner = results.front();
        const ChordQuality q = winner.identity.quality;
        const int rPc        = winner.identity.rootPc;
        const int delta      = (bassPc - rPc + 12) % 12;
        const bool patternA  = (delta == 8) && (q == ChordQuality::Minor);
        const bool patternB  = (delta == 9) && (q == ChordQuality::Major);
        const bool isPlainTriad = !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                                  && !hasExtension(winner.identity.extensions, Extension::MajorSeventh);
        if ((patternA || patternB) && (bassPc != rPc) && isPlainTriad) {
            // Find the bass-rooted candidate in rawCandidates (the top-3 results[]
            // cap is routinely exhausted by same-rootPc variants of the iii/III
            // reading; the bass-rooted target often lives only in rawCandidates).
            for (const RawCandidate& rc : gateCtx.rawCandidates) {
                if (rc.rootPc != bassPc) continue;
                // Append a built result for the bass-rooted candidate and swap
                // it into the winner slot (same swap pattern as the FM2 fallback
                // at the start of the inversion-correction block, line ~2189).
                results.push_back(buildResult(rc));
                std::swap(results[0], results.back());
                break;
            }
        }
    }

    // ── Two-pass pedal point detection ────────────────────────────────────────
    //
    // Definition: a structural pedal point is a sustained bass note that is NOT
    // a chord tone of the upper-voice harmony.  This two-pass check identifies
    // it when:
    //   (1) Pass 1 (all voices) produces a confident winner R1 with bassPc X.
    //   (2) X is not a chord tone of R1 (triad + detected 7th extensions).
    //   (3) Pass 2 (upper voices only, X removed) produces a chord R2 with
    //       confidence ≥ pedalConfidenceThreshold and ≥ 2 distinct pitch classes.
    //
    // When confirmed, the Pass 2 chord replaces the Pass 1 result: the label
    // describes the upper-voice harmony and isPedalPoint / pedalBassPc are set.
    //
    // Safety checks:
    //   - Bass IS a chord tone of R1 → no check (common-tone progressions, slash
    //     chords, jazz ostinati like F13/Eb where Eb is the minor 7th).
    //   - Upper voices have < 2 distinct pitch classes → insufficient evidence.
    //   - Pass 2 confidence < pedalConfidenceThreshold → ambiguous; keep R1.
    //   - bassPc < 0 → no valid bass (sparse region); skip.
    if (!results.empty() && bassPc >= 0 && prefs.pedalConfidenceThreshold > 0.0) {
        const ChordAnalysisResult& r1 = results.front();
        const bool bassIsChordTone = cptIsBassChordTone(bassPc,
                                                     r1.identity.rootPc,
                                                     r1.identity.quality,
                                                     r1.identity.extensions);
        if (!bassIsChordTone) {
            // Remove all tones with the pedal pitch class and re-analyze.
            std::vector<ChordAnalysisTone> upperTones;
            upperTones.reserve(gateCtx.tones.size());
            for (const ChordAnalysisTone& t : gateCtx.tones) {
                if ((t.pitch % 12 + 12) % 12 != bassPc) {
                    upperTones.push_back(t);
                }
            }

            // Require at least 2 distinct pitch classes in the upper voices.
            std::set<int> upperPcs;
            for (const ChordAnalysisTone& t : upperTones) {
                upperPcs.insert((t.pitch % 12 + 12) % 12);
            }

            if (upperPcs.size() >= 2) {
                // Run Pass 2 — re-use the same key context and preferences.
                // Do not pass temporal context to Pass 2: the context bonuses
                // (rootContinuityBonus, stepwiseBass*) are anchored to the bass
                // note and would distort the upper-voice-only result.
                // Disable the inversion correction and guaranteed-alt append for
                // Pass 2: in the upper-voice-only analysis there is no sustained
                // bass to correct against, and those blocks distort the confidence
                // gap used to confirm the pedal.
                ChordAnalyzerPreferences pass2Prefs = prefs;
                pass2Prefs.inversionSuspicionMargin = 0.0;
                // Capture a gate context for Pass 2 and re-apply this tail to it,
                // matching the inline version where the nested analyzeChord() ran
                // its own Iter 86/91/pedal tail (context = nullptr ⇒ Iter 91 skips).
                PostScoringGateContext pass2GateCtx;
                auto pass2 = RuleBasedChordAnalyzer{}.analyzeChord(
                    upperTones, gateCtx.keySigFifths, gateCtx.keyMode, nullptr,
                    pass2Prefs, &pass2GateCtx);
                applyIter8691Pedal(pass2, pass2GateCtx, nullptr, pass2Prefs);

                if (!pass2.empty()) {
                    // Confidence is measured against the first competitor with a
                    // DIFFERENT root.  Multiple templates for the same chord quality
                    // (triad / maj7 / dom7) can score identically when their extended
                    // tones are absent, filling all three result slots with the same
                    // root — making a gap-to-next-in-list metric artificially low.
                    // Comparing the winner's score against the best genuine alternative
                    // (different rootPc) gives a meaningful pedal-confirmation signal.
                    // Sigmoid constants (midpoint=2.0, steepness=1.5) are the empirical
                    // defaults from ChordAnalyzerPreferences, inlined here after the
                    // chord-level normalizedConfidence field was removed as dead code.
                    double pass2AltScore = 0.0;
                    const int p2Root = pass2.front().identity.rootPc;
                    for (size_t i = 1; i < pass2.size(); ++i) {
                        if (pass2[i].identity.rootPc != p2Root) {
                            pass2AltScore = pass2[i].identity.score;
                            break;
                        }
                    }
                    const double gap = pass2.front().identity.score - pass2AltScore;
                    const double c2  = 1.0 / (1.0 + std::exp(-1.5 * (gap - 2.0)));
                    if (c2 >= prefs.pedalConfidenceThreshold) {
                        // Confirmed pedal — replace results with Pass 2.
                        results = pass2;
                        results.front().identity.isPedalPoint = true;
                        results.front().identity.pedalBassPc  = bassPc;
                    }
                }
            }
        }
    }
}

} // namespace mu::composing::analysis
