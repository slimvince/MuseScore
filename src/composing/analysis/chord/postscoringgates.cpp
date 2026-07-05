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
#include "../param/paramoverride.h"   // Stage-5 fitter: optional constant override (D-6)

#include <algorithm>
#include <cstdint>
#include <utility>
#include <vector>

namespace mu::composing::analysis {

// ── Stage-5 fitter: §6-block gate margins (G7) relocated to file scope ───────────
// Moved here (from applyPostScoringGates locals / a nested block) with unchanged
// values so the parameter-override mechanism can register their addresses at
// static-init (a function-local static is not initialized until its function first
// runs — too late for the startup-time override loader). Byte-identical when no
// override is loaded: same literals, read exactly as before; the loader is the only
// writer. applyPostScoringGates is production-only and odr-used, so registration runs.
// See cowork_stage5_fitter_design.md D-6 (§6-block dissolution is Phase-2 family 2).
namespace {
double kGateIMargin = 0.45;              ///< Gate I: first-inversion Min→Maj
double kGateKMargin = 0.20;              ///< Gate K: first-inversion Aug
double kGateLMargin = 0.35;              ///< Gate L: same-root Aug→Maj
double kHalfDimFirstInversionBonus = 0.55; ///< Iter-61 Option B: HalfDim first-inversion bonus (under preferMinorOverMajorAdd6)

const bool s_registerGateMarginParams = [] {
    namespace P = mu::composing::params;
    P::registerDouble("kGateIMargin",              &kGateIMargin);
    P::registerDouble("kGateKMargin",              &kGateKMargin);
    P::registerDouble("kGateLMargin",              &kGateLMargin);
    P::registerDouble("kHalfDimFirstInversionBonus", &kHalfDimFirstInversionBonus);
    return true;
}();
} // namespace

void applyPostScoringGates(
    std::vector<ChordAnalysisResult>& results,
    const ChordAnalyzerPreferences&   prefs,
    const ChordTemporalContext*       context,
    const PostScoringGateContext&     gateCtx)
{
    // Local convenience: build a ChordAnalysisResult from a RawCandidate using
    // the captured gate context. Mirrors the buildResult lambda the gate block
    // used to call when it lived inside analyzeChord().
    const auto buildResult = [&](const RawCandidate& rc) -> ChordAnalysisResult {
        return buildChordResult(rc,
            BuildChordResultContext{ gateCtx.pcWeight, gateCtx.tpcForPc,
                                     gateCtx.bassPc, gateCtx.bassTpc,
                                     gateCtx.keyTonicPc, gateCtx.keyMode,
                                     gateCtx.scale },
            prefs);
    };

    // ── §6-block dissolution audit (Phase 2.2): per-rule disable hook ────────────
    // ruleOff(X) is true only when a `disable_rule X` override line was loaded; with no
    // override every call returns false, so each guard `!ruleOff(X) && <cond>` collapses
    // to `<cond>` — byte-identical to the pre-audit code. Measurement-only (design D-7).
    namespace P = ::mu::composing::params;
    const auto ruleOff = [](P::PostScoringRule r) { return P::isRuleDisabled(r); };

    // Gate margin guards (corpus-tuned).  All reachable corpus targets have
    // margins well within these bounds.
    // (kGateIMargin/kGateKMargin/kGateLMargin relocated to file scope for the Stage-5
    //  parameter-override mechanism — same values.)

    // ── Inversion / bass-root bias correction ────────────────────────────────
    //
    // If the winner's bass-root bonus is the sole reason it beat the best
    // non-bass alternative (margin < inversionSuspicionMargin), and a clean
    // triadic/seventh alternative exists, and the chord has ≥ 3 distinct PCs
    // (not an arpeggio artifact), remove the bonus contribution and re-sort.
    //
    // This corrects the systematic bias where inverted chords are labelled with
    // the bass note as root instead of the actual chord root.
    if (prefs.inversionSuspicionMargin > 0.0
        && prefs.inversionBonusReduction < 1.0
        && results.size() >= 2
        && gateCtx.distinctPcs >= 3)
    {
        // CAPTURE BEFORE stable_sort — Sub-9a bug (fixed in Gate G-E by commit
        // f3e0f5f72c).  winner is a live reference to results[0].  The
        // stable_sort below may promote Am7b5/C (rootPc=9) to results[0], making
        // winner.identity.rootPc=9.  Gate G-E uses originalWinnerRootPc to
        // compute gExpectedAltRoot — if it read winner.identity.rootPc after the
        // sort it would compute the wrong leading tone (e.g. (9+9)%12=6 instead
        // of (0+9)%12=9) and pull in a spurious candidate (the dormant F#m7b5
        // case).  Capture all three originalWinner* fields here for any gate
        // that needs the pre-correction winner.  See docs/scoring_model.md §7.
        //
        // Live reference — winner tracks results[0] through any swap or re-sort.
        // Use originalWinnerQuality, originalWinnerRootPc, and
        // originalWinnerHasAddedSixth (captured below) when you need the
        // pre-swap state in gates that run after A–F.
        const ChordAnalysisResult& winner = results[0];
        const ChordQuality originalWinnerQuality = winner.identity.quality;
        const int originalWinnerRootPc = winner.identity.rootPc;
        const bool originalWinnerHasAddedSixth =
            hasExtension(winner.identity.extensions, Extension::AddedSixth);
        const bool winnerBassIsRoot = (winner.identity.rootPc == winner.identity.bassPc);

        // The correction only targets Major and Minor winners — the typical inversion
        // bias patterns (e.g. Bb6 labelled as root-position when it's really Gm/Bb).
        // Augmented, Diminished, HalfDiminished, Suspended, and Power chords with
        // bassIsRoot=true are far more often correct root-position identifications,
        // and the correction causes regressions when applied to them.
        const bool winnerQualityTargeted = (winner.identity.quality == ChordQuality::Major
                            || winner.identity.quality == ChordQuality::Minor);

        if (winnerBassIsRoot && winnerQualityTargeted) {
            // Find the best alternative that has clean (Major or Minor) quality.
            // Seconds-chord, augmented, diminished, etc. are excluded as described above.
            static constexpr std::array<ChordQuality, 2> kCleanQualities = {
                ChordQuality::Major,
                ChordQuality::Minor,
            };
            size_t bestAltIdx = results.size();
            bool bestAltIsHalfDimInversion = false;
            for (size_t i = 1; i < results.size(); ++i) {
                const auto& alt = results[i];
                // The alternative must have a DIFFERENT root — if it agrees on the
                // root but differs only in extensions (e.g. CMaj9 vs CMaj9(no 3)),
                // there is no inversion to correct.
                if (alt.identity.rootPc == winner.identity.rootPc) {
                    continue;
                }
                const bool isClean = std::find(kCleanQualities.begin(),
                                               kCleanQualities.end(),
                                               alt.identity.quality)
                                     != kCleanQualities.end();
                // HalfDiminished first/second/third-inversion exception:
                // accept a HalfDim alt only when all four chord tones (root, m3,
                // b5, m7) are present in the region and the winner's bass pitch
                // class (= winner root, since this block requires bassIsRoot=true)
                // is the alt's m3, b5, or m7. Targets bwv187.7-style cases where
                // the bass-root bonus on a clean Minor reading is blocking the
                // correct inverted half-diminished seventh.
                bool isHalfDimInversion = false;
                if (!isClean && alt.identity.quality == ChordQuality::HalfDiminished) {
                    const int aR = alt.identity.rootPc;
                    const int thirdPc   = (aR + 3) % 12;
                    const int fifthPc   = (aR + 6) % 12;
                    const int seventhPc = (aR + 10) % 12;
                    const double thr = prefs.extensionThreshold;
                    const int wb = winner.identity.bassPc;
                    // The bass pc is by definition sounding — exempt it from the
                    // weight threshold so a briefly-sounded inversion bass (e.g.
                    // bwv187.7 m=14 G at 0.14 vs thr 0.20) does not block the
                    // inversion reading.  Targets Minor-add6 winners where the
                    // bass=m3 of the HalfDim root has short metric duration.
                    auto tonePresent = [&](int pc) {
                        return pc == wb || gateCtx.pcWeight[static_cast<size_t>(pc)] > thr;
                    };
                    const bool allTonesPresent =
                        tonePresent(aR)
                        && tonePresent(thirdPc)
                        && tonePresent(fifthPc)
                        && tonePresent(seventhPc);
                    const bool bassIsInversion =
                        (wb == thirdPc || wb == fifthPc || wb == seventhPc);
                    isHalfDimInversion = allTonesPresent && bassIsInversion;
                }
                if (isClean || isHalfDimInversion) {
                    bestAltIdx = i;
                    bestAltIsHalfDimInversion = isHalfDimInversion;
                    break;
                }
            }

            if (bestAltIdx < results.size()) {
                // ── Enharmonic equivalence fast path ─────────────────────────
                //
                // Major-add6 and Minor7 chords span identical pitch classes when
                // the Minor7 root is a minor third below the Major root:
                //   altRootPc == (winnerRootPc + 9) % 12
                // In bass-heavy textures the scorer systematically favours the
                // bass-root Major reading; margin comparison cannot reliably
                // distinguish the two.  When preferMinorOverMajorAdd6 is set
                // (Standard/Baroque), prefer the Minor alternative directly.
                bool didEnharmonicFlip = false;
                if (prefs.preferMinorOverMajorAdd6) {
                    const bool winnerIsMajor =
                        (winner.identity.quality == ChordQuality::Major);
                    // The added-sixth guard restricts the fast path to sonorities
                    // where the sixth (e.g. G in Bb-D-F-G) is present with enough
                    // structural weight that the analyzer already labeled it as an
                    // added-sixth chord.  Without this guard the fast path fires on
                    // plain C major triads (C-E-G) just because Am is a candidate,
                    // producing a flood of Am7/C regressions on root-position chords.
                    const bool winnerHasAddedSixth =
                        hasExtension(winner.identity.extensions, Extension::AddedSixth);
                    const int expectedAltRoot = (winner.identity.rootPc + 9) % 12;
                    // Gate A (the direct Major-add6 → relative-Minor enharmonic swap) was
                    // RETIRED in Stage 5 (2026-07-05, design D-7): it fired on ZERO corpus
                    // cells across all three carriers (cc_stage5_phase2_2b_report.md §1.2),
                    // so its removal is corpus-byte-identical. The FM2 fallback below stays
                    // as the enharmonic-partner mechanism (pull the Minor alt from rawCandidates).
                    // FM2 fallback: a higher-scoring different-root alt (e.g. Em/C) may have
                    // blocked the enharmonic partner from entering results[] via the append path.
                    // Scan rawCandidates above threshold for the Minor alt at expectedAltRoot.
                    if (!ruleOff(P::PostScoringRule::FM2)
                        && !didEnharmonicFlip && winnerIsMajor && winnerHasAddedSixth) {
                        for (const RawCandidate& rc : gateCtx.rawCandidates) {
                            if (rc.score < gateCtx.threshold) { break; }
                            if (rc.rootPc == expectedAltRoot
                                && rc.quality == ChordQuality::Minor) {
                                results.push_back(buildResult(rc));
                                std::swap(results[0], results.back());
                                didEnharmonicFlip = true;
                                break;
                            }
                        }
                    }
                    // Gates B/C/D (forward / 3-region-window / consecutive-stepwise temporal
                    // confirmations of the Major-add6 ↔ Minor flip) were removed in Stage 3.4b
                    // as provably unreachable (Stage-1b finding F1): each repeated Gate A's exact
                    // entry conditions plus extra temporal evidence behind `!didEnharmonicFlip`,
                    // but Gate A — which has those same conditions with no temporal requirement —
                    // always fires first and sets the flag. Removal is byte-identical (0/353 × 3
                    // configs, snapshots zero-diff). See docs/scoring_model.md §6/§8.
                }

                // ── Gate E: first-inversion detection ─────────────────────────────────────
                //
                // When the winner is Minor with bassIsRoot=true and the best Major alternative
                // has its root a minor-6th above the winner root (= winner root is the major
                // 3rd of the alt), the scorer has likely identified the bass note (= 3rd of
                // the actual chord) as the root.  E.g., F#m wins when D/F# is correct.
                //
                // Relationship: altRootPc == (winnerRootPc + 8) % 12
                // Gated by preferMinorOverMajorAdd6 (classical presets only) and a stepwise
                // bass signal (temporal context required).
                if (!ruleOff(P::PostScoringRule::GateE)
                    && !didEnharmonicFlip
                    && prefs.preferMinorOverMajorAdd6
                    && context != nullptr
                    && winner.identity.quality == ChordQuality::Minor
                    && results[bestAltIdx].identity.quality == ChordQuality::Major
                    && results[bestAltIdx].identity.rootPc == (winner.identity.rootPc + 8) % 12
                    && gateCtx.pcWeight[static_cast<size_t>(results[bestAltIdx].identity.rootPc)] > prefs.extensionThreshold
                    && (context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext)) {
                    std::swap(results[0], results[bestAltIdx]);
                    didEnharmonicFlip = true;
                }

                // Gate F (second-inversion → root-position Major, alt at (rootPc+5)%12) was
                // RETIRED in Stage 5 (2026-07-05, design D-7): 0 corpus firing sites on all
                // three carriers (cc_stage5_phase2_2b_report.md §1.2) — removal is
                // corpus-byte-identical. didEnharmonicFlip flows unchanged into the bias block.

                if (!didEnharmonicFlip) {
                    const double margin = winner.identity.score - results[bestAltIdx].identity.score;

                    // Seventh-chord exemption: if the winner carries a minor or major
                    // seventh extension that the best alternative lacks, the bass-root
                    // bonus is not the sole structural advantage — the winner is a richer,
                    // more specific reading (e.g. Am7 vs Em triad).  Do not penalise it.
                    const bool winnerHasSeventh =
                        hasExtension(winner.identity.extensions, Extension::MinorSeventh)
                        || hasExtension(winner.identity.extensions, Extension::MajorSeventh);
                    const bool altHasSeventh =
                        hasExtension(results[bestAltIdx].identity.extensions, Extension::MinorSeventh)
                        || hasExtension(results[bestAltIdx].identity.extensions, Extension::MajorSeventh);
                    const bool seventhExempt = winnerHasSeventh && !altHasSeventh;

                    if (!ruleOff(P::PostScoringRule::BiasCorrection)
                        && !seventhExempt && margin < prefs.inversionSuspicionMargin) {
                        // Deduct the bass-bonus contribution from the winner and re-sort.
                        const double deduction = prefs.bassNoteRootBonus
                                                * (1.0 - prefs.inversionBonusReduction);
                        results[0].identity.score -= deduction;
                        // Confirmed first-inversion HalfDim bonus: when the bestAlt
                        // is a HalfDim with all four chord tones present and the
                        // winner's bass is one of those tones (m3/b5/m7), the
                        // deduction alone is not enough to flip — the bass-root
                        // Minor/Major reading carries residual scoring advantages
                        // (e.g. AddedSixth extension fit) that keep it ahead.
                        // Gated by preferMinorOverMajorAdd6 (same gate as the
                        // existing Minor-add6 ↔ HalfDim7 path, Gate G-E below):
                        // Jazz prefs disable this preference because the
                        // genuine Cm6/Cm69 chord vocabulary is idiomatic and
                        // must outrank the enharmonic Aø7/C inversion reading.
                        if (bestAltIsHalfDimInversion && prefs.preferMinorOverMajorAdd6) {
                            // (kHalfDimFirstInversionBonus relocated to file scope for
                            //  the Stage-5 override mechanism — same 0.55 value.)
                            results[bestAltIdx].identity.score += kHalfDimFirstInversionBonus;
                        }
                        std::stable_sort(results.begin(), results.end(),
                                         [](const ChordAnalysisResult& a,
                                            const ChordAnalysisResult& b) {
                                             return a.identity.score > b.identity.score;
                                         });
                    }
                }
            }
        // ── Gates G-E / G-B / G-C / G-D: Minor-add6 ↔ HalfDim7 ─────────────────────
        //
        // MinorAdd6 and HalfDim7 share identical pitch classes.
        // kCleanQualities excludes HalfDiminished, so this block runs independently
        // of the bestAlt path above.
        //
        // Gate G-E (key-context): fires when the HalfDim7 alt is a functional chord
        // of the current key — either the leading-tone seventh (viiø7, alt root at
        // tonicPc+11) or the supertonic seventh (iiø7, alt root at tonicPc+2).
        // No temporal signals required.
        //
        // Gates G-B/C/D: temporal fallbacks for the remaining cases.
        if (prefs.preferMinorOverMajorAdd6
            && originalWinnerQuality == ChordQuality::Minor
            && originalWinnerHasAddedSixth) {
            const int gExpectedAltRoot = (originalWinnerRootPc + 9) % 12;
            // Find the HalfDim7 alt in results[].
            size_t halfDimAltIdx = results.size();
            for (size_t i = 1; i < results.size(); ++i) {
                if (results[i].identity.quality == ChordQuality::HalfDiminished
                    && results[i].identity.rootPc == gExpectedAltRoot) {
                    halfDimAltIdx = i;
                    break;
                }
            }
            // Gate G-E: if HalfDim not in results[], look in rawCandidates (temporal
            // context may have suppressed it via rootContinuityBonus)
            bool halfDimPulledFromRaw = false;
            if (halfDimAltIdx >= results.size()) {
                for (const auto& rc : gateCtx.rawCandidates) {
                    if (rc.quality == ChordQuality::HalfDiminished
                        && rc.rootPc == gExpectedAltRoot) {
                        results.push_back(buildResult(rc));
                        halfDimAltIdx = results.size() - 1;
                        halfDimPulledFromRaw = true;
                        break;
                    }
                }
            }
            if (halfDimAltIdx != results.size()) {
                bool didGFlip = false;
                // Gate G-E: leading-tone key-context gate.
                // The half-diminished seventh is the standard functional reading when
                // it is rooted on the leading tone (viiø7) or supertonic (iiø7) of
                // the current key.  No temporal signals required.
                const int gLeadingTonePc  = (gateCtx.keyTonicPc + 11) % 12;  // viiø7
                const int gSupertonicPc   = (gateCtx.keyTonicPc + 2) % 12;   // iiø7
                const int gMediantPc      = (gateCtx.keyTonicPc + 4) % 12;   // iiiø7 / mediant
                if (!ruleOff(P::PostScoringRule::GateGE)
                    && !didGFlip
                    && (results[halfDimAltIdx].identity.rootPc == gLeadingTonePc
                        || results[halfDimAltIdx].identity.rootPc == gSupertonicPc
                        || results[halfDimAltIdx].identity.rootPc == gMediantPc)) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
                // Gate G-B (Minor-add6 ↔ HalfDim7 forward-evidence temporal fallback) was
                // RETIRED in Stage 5 (2026-07-05, design D-7): 0 corpus firing sites on all
                // three carriers (cc_stage5_phase2_2b_report.md §1.2) — byte-identical removal.
                // Gate G-C (Minor-add6 ↔ HalfDim7 recent-root + stepwise-from-previous
                // fallback) was RETIRED in Stage 5 (2026-07-05, design D-7): 0 corpus firing
                // sites on all three carriers (cc_stage5_phase2_2b_report.md §1.2) — byte-identical.
                // Gate G-D: two or more consecutive stepwise bass moves ending here.
                if (!ruleOff(P::PostScoringRule::GateGD)
                    && !didGFlip
                    && context != nullptr
                    && context->consecutiveBassStepwiseCount >= 2) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
                if (halfDimPulledFromRaw && !didGFlip) {
                    // No sub-gate fired — remove the phantom alternative that was
                    // pulled from rawCandidates so it does not pollute results[].
                    results.pop_back();
                }
            }
        }
        }

        // ── Gate H: Augmented triad root-symmetry resolution ──────────────────────────
        //
        // An augmented triad has three enharmonic roots (±4 semitones mod 12): D+, F#+,
        // and Bb+ are the same chord.  When the analyzer picks root R but the correct
        // root is (R+4)%12 or (R+8)%12, the two candidates represent the same sonority
        // with different root labels.  Temporal evidence resolves the ambiguity.
        //
        // Unlike the main correction block, this gate handles Augmented winners
        // (excluded from winnerQualityTargeted = Major/Minor).  It fires only with
        // temporal context and is gated by preferMinorOverMajorAdd6 (classical presets).
        if (!ruleOff(P::PostScoringRule::GateH)
            && winnerBassIsRoot
            && winner.identity.quality == ChordQuality::Augmented
            && prefs.preferMinorOverMajorAdd6
            && context != nullptr) {
            bool didAugmentedFlip = false;
            for (const int semitones : {4, 8}) {
                if (didAugmentedFlip) break;
                const int altRoot = (winner.identity.rootPc + semitones) % 12;
                // Find an Augmented candidate at this root.
                size_t augAltIdx = results.size();
                for (size_t i = 1; i < results.size(); ++i) {
                    if (results[i].identity.quality == ChordQuality::Augmented
                        && results[i].identity.rootPc == altRoot) {
                        augAltIdx = i;
                        break;
                    }
                }
                if (augAltIdx == results.size()) continue;
                // Gate H-B: next region's inferred root matches the alt augmented root.
                if (!didAugmentedFlip
                    && context->nextRootPc != -1
                    && context->nextRootPc == altRoot
                    && context->bassIsStepwiseToNext) {
                    std::swap(results[0], results[augAltIdx]);
                    didAugmentedFlip = true;
                }
                // Gate H-C: alt root appears in the 3-region window AND bass is stepwise.
                if (!didAugmentedFlip && context->bassIsStepwiseFromPrevious) {
                    const auto& rpc = context->recentRootPcs;
                    if (rpc[0] == altRoot || rpc[1] == altRoot || rpc[2] == altRoot) {
                        std::swap(results[0], results[augAltIdx]);
                        didAugmentedFlip = true;
                    }
                }
                // Gate H-D: two or more consecutive stepwise bass moves.
                if (!didAugmentedFlip
                    && context->consecutiveBassStepwiseCount >= 2) {
                    std::swap(results[0], results[augAltIdx]);
                    didAugmentedFlip = true;
                }
            }
        }

        // ── Gate I: prefer diatonic first-inversion major over root-position minor ──────
        //
        // When the winner is a Minor chord with bassIsRoot=true and a runner-up shares
        // the same bass note but is a first-inversion chord whose root lies a major third
        // below the bass (I4 interval), and that root is diatonic to the current key,
        // prefer the first-inversion reading.  E.g., Em → C/E when C is diatonic.
        //
        // Score margin guard (≤ 0.45) ensures the gate only fires when the two readings
        // are genuinely competitive — not when the Minor winner is strongly confirmed.
        if (!ruleOff(P::PostScoringRule::GateI)
            && winnerBassIsRoot
            && originalWinnerQuality == ChordQuality::Minor
            && results.size() >= 2
            && gateCtx.keyTonicPc >= 0) {
            for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                const ChordAnalysisResult& inv = results[iIdx];
                const int invBassPc = inv.identity.bassPc;
                const int invRootPc = inv.identity.rootPc;
                if (invBassPc != winner.identity.bassPc)                   continue;  // different bass
                if (invBassPc == invRootPc)                                continue;  // root position
                if ((winner.identity.bassPc - invRootPc + 12) % 12 != 4)  continue;  // not I4 interval
                const int invInterval = (invRootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (!invRootIsDiatonic)                                    continue;  // not diatonic
                if (gateCtx.pcWeight[static_cast<size_t>(invRootPc)] <= prefs.extensionThreshold) {
                    continue;  // promoted root absent from the score — do not invent a rootless inversion
                }
                if (winner.identity.score - inv.identity.score > kGateIMargin)   continue;  // margin too wide
                std::swap(results[0], results[iIdx]);
                break;
            }
        }

        // ── Gate K: prefer first-inversion augmented over root-position augmented ──────────
        //
        // When the winner is an Augmented chord with bassIsRoot=true and a runner-up shares
        // the same bass note but is NOT root-position, with its root a major third below
        // the bass (I4 interval), prefer the first-inversion reading.  E.g., D+ → Bb#5/D.
        //
        // Quality condition covers both encoding variants of an augmented-collection chord:
        // Augmented quality directly, or Major with SharpFifth extension.
        //
        // Margin guard (≤ 0.20) keeps the gate narrow; all reachable targets have margin ≤ 0.12.
        if (!ruleOff(P::PostScoringRule::GateK)
            && winnerBassIsRoot
            && originalWinnerQuality == ChordQuality::Augmented
            && results.size() >= 2
            && gateCtx.keyTonicPc >= 0) {
            for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                const ChordAnalysisResult& inv = results[iIdx];
                if (inv.identity.bassPc != winner.identity.bassPc)                   continue;  // different bass
                if (inv.identity.bassPc == inv.identity.rootPc)                      continue;  // root position
                if ((winner.identity.bassPc - inv.identity.rootPc + 12) % 12 != 4)  continue;  // not I4 interval
                const bool isAugmentedCollection =
                    inv.identity.quality == ChordQuality::Augmented
                    || (inv.identity.quality == ChordQuality::Major
                        && hasExtension(inv.identity.extensions, Extension::SharpFifth));
                if (!isAugmentedCollection)                                          continue;  // not augmented quality
                const int invInterval = (inv.identity.rootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (!invRootIsDiatonic)                                              continue;  // not diatonic
                if (winner.identity.score - inv.identity.score > kGateKMargin)             continue;  // margin too wide
                std::swap(results[0], results[iIdx]);
                break;
            }
        }

        // ── Gate L: prefer same-root Major over root-position Augmented (TYPE-A quality fix) ──
        //
        // When the winner is a plain Augmented triad (no 7th extension) at root position
        // and a runner-up shares the exact same root AND same bass (also root-position),
        // has Major quality, and that root is diatonic to the current key, prefer Major.
        // E.g., B+ → B (Bmin), E+ → E (Cmaj), F+ → F (FDor).
        //
        // Seventh exclusion: augmented +7 chords (e.g. C+7 jazz dominant) are intentionally
        // augmented and must not be demoted to plain Major.
        // Margin guard (≤ 0.35) keeps the gate narrow; all corpus targets have margin ≤ 0.30.
        // Diatonic check prevents spurious fires on chromatic passing augmented chords.
        if (!ruleOff(P::PostScoringRule::GateL)
            && originalWinnerQuality == ChordQuality::Augmented
            && winnerBassIsRoot
            && results.size() >= 2
            && gateCtx.keyTonicPc >= 0
            && !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
            && !hasExtension(winner.identity.extensions, Extension::MajorSeventh)) {
            for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                const ChordAnalysisResult& inv = results[iIdx];
                if (inv.identity.quality != ChordQuality::Major)                        continue;  // not Major
                if (inv.identity.rootPc != winner.identity.rootPc)                      continue;  // different root
                if (inv.identity.bassPc != winner.identity.bassPc)                      continue;  // not root-position
                const int invInterval = (inv.identity.rootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (!invRootIsDiatonic)                                                 continue;  // not diatonic
                if (winner.identity.score - inv.identity.score > kGateLMargin)                continue;  // margin too wide
                std::swap(results[0], results[iIdx]);
                break;
            }
        }

        // ── Gate J: prefer inverted dominant-7th over root-position diminished triad ──────
        //
        // A root-position diminished TRIAD whose would-be dominant root (a major third
        // below the dim root) is also sounding is, by construction, the 3rd/5th/7th of
        // that dominant seventh — i.e. an inverted V7, not a root-position vii°.  The
        // four pcs {R-4, R, R+3, R+6} are exactly a dominant seventh rooted at R-4
        // (root, M3, P5, m7).  Promote the dominant reading.
        //   E.g. {C#,E,F#,A#} bass A#:  A#° (vii° of Bm) → F#7/A# (V6/5).
        // A genuine standalone vii° / vii°7 never voices the dominant root, so the
        // present-root guard means this cannot misfire on real leading-tone chords.
        // No diatonic guard — a secondary dominant (V7/x) is just as validly completed.
        if (!ruleOff(P::PostScoringRule::GateJ)
            && originalWinnerQuality == ChordQuality::Diminished
            && results.size() >= 2) {
            const ChordAnalysisResult& dimWinner = results[0];
            if (dimWinner.identity.quality == ChordQuality::Diminished
                && dimWinner.identity.rootPc == dimWinner.identity.bassPc            // root position
                && !hasExtension(dimWinner.identity.extensions, Extension::DiminishedSeventh)) {
                const int domRootPc = (dimWinner.identity.rootPc - 4 + 12) % 12;     // major 3rd below
                if (gateCtx.pcWeight[static_cast<size_t>(domRootPc)] > prefs.extensionThreshold) {
                    for (size_t iIdx = 1; iIdx < results.size(); ++iIdx) {
                        const ChordAnalysisResult& dom = results[iIdx];
                        if (dom.identity.rootPc != domRootPc)                          continue;  // not the V7 root
                        if (dom.identity.quality != ChordQuality::Major)              continue;  // dom7 is Major+m7
                        if (!hasExtension(dom.identity.extensions, Extension::MinorSeventh)) {
                            continue;  // must carry the dominant seventh
                        }
                        std::swap(results[0], results[iIdx]);
                        break;
                    }
                }
            }
        }

    }
}

} // namespace mu::composing::analysis
