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
#include "analysisutils.h"            // pcInMask, diatonicMaskFromFifths (the signature collection)
#include "keycollectionprobe.h"       // OI-170 counters + signature-mask variant (default-OFF)

#include <algorithm>
#include <cstdint>
#include <utility>
#include <vector>

namespace kcp = mu::composing::analysis::keycollectionprobe;

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
double kGateLMargin = 0.35;              ///< Gate L: same-root Aug→Maj
double kHalfDimFirstInversionBonus = 0.55; ///< Iter-61 Option B: HalfDim first-inversion bonus (under preferMinorOverMajorAdd6)
// (kGateKMargin retired with Gate K — Stage 5, 2026-07-05, D-7.)

const bool s_registerGateMarginParams = [] {
    namespace P = mu::composing::params;
    P::registerDouble("kGateIMargin",              &kGateIMargin);
    P::registerDouble("kGateLMargin",              &kGateLMargin);
    P::registerDouble("kHalfDimFirstInversionBonus", &kHalfDimFirstInversionBonus);
    return true;
}();

// The single builder wrapper: adapt a scored RawCandidate through the one normalizing builder
// (buildChordResult) using the captured post-scoring gate context. This collapses the two
// byte-identical gateCtx builder lambdas that applyPostScoringGates() and applyIter8691Pedal()
// previously duplicated; promoteToWinner() is its only caller.
ChordAnalysisResult buildResultFromGateCtx(const RawCandidate&              rc,
                                           const PostScoringGateContext&   gateCtx,
                                           const ChordAnalyzerPreferences& prefs)
{
    return buildChordResult(rc,
        BuildChordResultContext{ gateCtx.pcWeight, gateCtx.tpcForPc,
                                 gateCtx.bassPc, gateCtx.bassTpc,
                                 gateCtx.keyTonicPc, gateCtx.keyMode,
                                 gateCtx.scale, gateCtx.keySigFifths },
        prefs);
}
} // namespace

// ── Unified post-scoring promotion primitive (Layer 4) ────────────────────────────────
// See chordanalyzer.h for the contract. The two promotion idioms — swap an already-carried
// reading (Idiom A) and build-then-append a reading pulled from rawCandidates (Idiom B) — are
// the two branches of this one primitive; every post-scoring promotion site routes through it.
bool promoteToWinner(std::vector<ChordAnalysisResult>& results,
                     const PostScoringGateContext&      gateCtx,
                     const ChordAnalyzerPreferences&    prefs,
                     const PromotionTarget&             target,
                     std::size_t                        presentHint,
                     bool                               stopBelowThreshold)
{
    const auto matches = [&](int rootPc, ChordQuality quality) {
        return rootPc == target.rootPc
            && (target.quality == ChordQuality::Unknown || quality == target.quality);
    };

    // ── Idiom A — present-first: swap an already-carried match to the front ────────────
    if (presentHint != kPromoteAppendOnly) {
        std::size_t j = results.size();
        if (presentHint == kPromotePresentScan) {
            for (std::size_t i = 1; i < results.size(); ++i) {
                if (matches(results[i].identity.rootPc, results[i].identity.quality)) {
                    j = i;
                    break;
                }
            }
        } else if (presentHint < results.size()
                   && matches(results[presentHint].identity.rootPc,
                              results[presentHint].identity.quality)) {
            j = presentHint;
        }
        if (j < results.size()) {
            std::swap(results[0], results[j]);
            return true;
        }
    }

    // ── Idiom B — append-built: build the target once from rawCandidates ───────────────
    for (const RawCandidate& rc : gateCtx.rawCandidates) {
        if (stopBelowThreshold && rc.score < gateCtx.threshold) {
            break;
        }
        if (matches(rc.rootPc, rc.quality)) {
            results.push_back(buildResultFromGateCtx(rc, gateCtx, prefs));
            std::swap(results[0], results.back());
            return true;
        }
    }
    return false;
}

void applyPostScoringGates(
    std::vector<ChordAnalysisResult>& results,
    const ChordAnalyzerPreferences&   prefs,
    const ChordTemporalContext*       context,
    const PostScoringGateContext&     gateCtx)
{
    // ── §6-block dissolution audit (Phase 2.2): per-rule disable hook ────────────
    // ruleOff(X) is true only when a `disable_rule X` override line was loaded; with no
    // override every call returns false, so each guard `!ruleOff(X) && <cond>` collapses
    // to `<cond>` — byte-identical to the pre-audit code. Measurement-only (design D-7).
    namespace P = ::mu::composing::params;
    const auto ruleOff = [](P::PostScoringRule r) { return P::isRuleDisabled(r); };

    // Gate margin guards (corpus-tuned).  All reachable corpus targets have
    // margins well within these bounds.
    // (kGateIMargin/kGateLMargin relocated to file scope for the Stage-5
    //  parameter-override mechanism — same values. kGateKMargin retired with Gate K.)

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
                // The former Gate A (swap the enharmonic Minor7 partner already carried at
                // bestAltIdx) and FM2 (build+append the partner from rawCandidates when a
                // higher-scoring different-root alt blocked it from results[]) are the two halves
                // of ONE flip — the present and absent branches of the single promoteToWinner()
                // primitive. Passing presentHint = bestAltIdx reproduces Gate A's exact swap
                // (the primitive swaps that index iff it is the Minor at (root+9)%12), and the
                // append branch (stopBelowThreshold = true) reproduces FM2's above-threshold
                // rawCandidate pull — byte-identical to HEAD, winner AND alternatives.
                //
                // The added-sixth guard restricts the flip to sonorities already labelled
                // added-sixth (so it does not fire on plain triads just because a relative minor
                // is a candidate). The surviving rule name for the whole flip is FM2 (Gate A was
                // retired at the promotion unification — cowork_gateA_unification_design.md; the
                // provably-unreachable Gates B/C/D were removed earlier in Stage 3.4b).
                if (prefs.preferMinorOverMajorAdd6
                    && !ruleOff(P::PostScoringRule::FM2)
                    && winner.identity.quality == ChordQuality::Major
                    && hasExtension(winner.identity.extensions, Extension::AddedSixth)) {
                    const int expectedAltRoot = (winner.identity.rootPc + 9) % 12;
                    didEnharmonicFlip = promoteToWinner(
                        results, gateCtx, prefs,
                        PromotionTarget{ expectedAltRoot, ChordQuality::Minor },
                        /*presentHint=*/ bestAltIdx,
                        /*stopBelowThreshold=*/ true);
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
                    // Pure Idiom-A swap: the target (Major at winnerRoot+8) is results[bestAltIdx]
                    // by the guard above, so promoteToWinner swaps that exact index — its append
                    // branch is unreachable here (the reading is always present).
                    promoteToWinner(results, gateCtx, prefs,
                                    PromotionTarget{ (winner.identity.rootPc + 8) % 12, ChordQuality::Major },
                                    /*presentHint=*/ bestAltIdx,
                                    /*stopBelowThreshold=*/ true);
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
        // ── Gates G-E / G-D: Minor-add6 ↔ HalfDim7 ─────────────────────────────────
        //
        // MinorAdd6 and HalfDim7 share identical pitch classes; the HalfDim7 reading is rooted
        // a minor third above the Minor-add6 winner (gExpectedAltRoot). Promote that HalfDim7
        // reading when the key context confirms it — Gate G-E: its root is the leading-tone
        // seventh (viiø7, tonic+11), supertonic seventh (iiø7, tonic+2), or mediant (iiiø7,
        // tonic+4), no temporal signal required — or Gate G-D: two or more consecutive stepwise
        // bass moves end here (only when G-E does not fire, the former !didGFlip ordering).
        //
        // Because the HalfDim7 reading is at gExpectedAltRoot, the Gate G-E key-context test
        // needs only that root, not the carried object. The former "scan results[]; else pull
        // from rawCandidates; else pop the phantom if no sub-gate fires" dance is exactly
        // promoteToWinner()'s present-first-else-append with the no-promotion (return-false)
        // path — so it is invoked only when a flip should occur, and the transient pull+pop is
        // gone. Byte-identical to HEAD (winner AND alternatives). Gates G-B/G-C were retired in
        // Stage 5 (D-7) as 0-firing.
        if (prefs.preferMinorOverMajorAdd6
            && originalWinnerQuality == ChordQuality::Minor
            && originalWinnerHasAddedSixth) {
            const int gExpectedAltRoot = (originalWinnerRootPc + 9) % 12;
            const int gLeadingTonePc   = (gateCtx.keyTonicPc + 11) % 12;  // viiø7
            const int gSupertonicPc    = (gateCtx.keyTonicPc + 2) % 12;   // iiø7
            const int gMediantPc       = (gateCtx.keyTonicPc + 4) % 12;   // iiiø7 / mediant
            const bool geKeyContext = (gExpectedAltRoot == gLeadingTonePc
                                       || gExpectedAltRoot == gSupertonicPc
                                       || gExpectedAltRoot == gMediantPc);
            const bool geFires = !ruleOff(P::PostScoringRule::GateGE) && geKeyContext;
            if (geFires) {
                // OI-170 (default-OFF): Gate G-E is a genuine TONIC use — it asks whether the
                // alternative root is the key's ii / iii / vii DEGREE, which the signature's
                // collection cannot answer. Counted, not changed: this is the magnitude of a
                // class-(b) site the signature-mask primitive cannot replace.
                kcp::bump(kcp::counters().gateGEFires);
            }
            const bool gdFires = !ruleOff(P::PostScoringRule::GateGD)
                                 && !geFires
                                 && context != nullptr
                                 && context->consecutiveBassStepwiseCount >= 2;
            if (geFires || gdFires) {
                promoteToWinner(results, gateCtx, prefs,
                                PromotionTarget{ gExpectedAltRoot, ChordQuality::HalfDiminished },
                                /*presentHint=*/ kPromotePresentScan,
                                /*stopBelowThreshold=*/ false);
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
                // OI-170 — "is that root diatonic to the current key?" is a COLLECTION-membership
                // question, and this asks it through the TONIC (the mode-transposed set). The
                // default-OFF variant asks the key SIGNATURE's own collection instead; the
                // counters report how often the two verdicts differ, and how often that
                // difference would change this gate's SWAP decision.
                const int invInterval = (invRootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (kcp::countingEnabled || kcp::signatureMaskVariant) {
                    const bool bySignature =
                        pcInMask(diatonicMaskFromFifths(gateCtx.keySigFifths), invRootPc);
                    kcp::bump(kcp::counters().gateIDiatonicTests);
                    if (bySignature != invRootIsDiatonic) {
                        kcp::bump(kcp::counters().gateIDiatonicDiffers);
                        const bool restPasses =
                            gateCtx.pcWeight[static_cast<size_t>(invRootPc)] > prefs.extensionThreshold
                            && (winner.identity.score - inv.identity.score) <= kGateIMargin;
                        if (restPasses) {
                            kcp::bump(kcp::counters().gateISwapDiffers);
                        }
                    }
                    if (kcp::signatureMaskVariant) {
                        invRootIsDiatonic = bySignature;
                    }
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

        // ── Gate K RETIRED (Stage 5, 2026-07-05, design D-7) ──────────────────────────────
        // The first-inversion-Augmented-over-root-position-Augmented swap (D+ → Bb#5/D,
        // margin ≤ kGateKMargin) fired on ZERO corpus cells across all three carriers
        // (cc_stage5_phase2_2b_report.md §1.2); its founding case bwv40.6 is no longer
        // touched (superseded upstream, §1.3). Removal is corpus-byte-identical. The margin
        // constant kGateKMargin was retired with it (file-scope block above).

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
                // OI-170 — the same collection-membership-through-the-tonic question as Gate I,
                // and the same default-OFF signature-collection variant + counters.
                const int invInterval = (inv.identity.rootPc - gateCtx.keyTonicPc + 12) % 12;
                bool invRootIsDiatonic = false;
                for (int d = 0; d < 7; ++d) {
                    if (gateCtx.scale[d] == invInterval) { invRootIsDiatonic = true; break; }
                }
                if (kcp::countingEnabled || kcp::signatureMaskVariant) {
                    const bool bySignature =
                        pcInMask(diatonicMaskFromFifths(gateCtx.keySigFifths), inv.identity.rootPc);
                    kcp::bump(kcp::counters().gateLDiatonicTests);
                    if (bySignature != invRootIsDiatonic) {
                        kcp::bump(kcp::counters().gateLDiatonicDiffers);
                        if ((winner.identity.score - inv.identity.score) <= kGateLMargin) {
                            kcp::bump(kcp::counters().gateLSwapDiffers);
                        }
                    }
                    if (kcp::signatureMaskVariant) {
                        invRootIsDiatonic = bySignature;
                    }
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
