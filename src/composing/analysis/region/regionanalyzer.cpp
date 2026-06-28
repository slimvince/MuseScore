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

#include "regionanalyzer.h"

#include <algorithm>
#include <array>
#include <optional>
#include <utility>

#include "engraving/dom/chord.h"
#include "engraving/dom/engravingitem.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"
#include "engraving/types/constants.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/decode/chordpathdecoder.h"
#include "composing/analysis/engravingbridge/phraseboundaryview.h"
#include "composing/analysis/engravingbridge/regiontonecollector.h"
#include "composing/analysis/function/harmonicfunctionlayer.h"
#include "composing/analysis/harmony/harmonicsegmenter.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/analysis/key/keymodesequence.h"
#include "composing/analysis/key/keyresolver.h"
#include "composing/analysis/region/sparsechordrefinement.h"
#include "composing/analysis/scoreharvest/metricweights.h"
#include "composing/analysis/section/jointkeydecision.h"   // J-key-iii production wiring
#include "composing/analysis/slicing/slicer.h"

namespace ebr  = mu::composing::analysis::engravingbridge;
namespace kr   = mu::composing::analysis::keyresolver;
namespace kms  = mu::composing::analysis::keymodeseq;
namespace shv  = mu::composing::analysis::scoreharvest;
namespace nmdl = mu::composing::analysis::notemodel;
namespace slc  = mu::composing::analysis::slicing;

namespace mu::composing::analysis::region {

namespace {

constexpr int kPass2MinRegionTicks    = 4 * mu::engraving::Constants::DIVISION;
constexpr int kMaxBassMovementPasses  = 8;

/// One reach-back increment in ticks: the duration of the measure ending at `tick`
/// (the measure just before the loaded-span edge), read from the score's time
/// signature — Architectural Layer 3's natural unit (design §2). Falls back to a 4/4
/// measure when no measure precedes `tick` (e.g. tick at/below the score start); the
/// extend() that consumes it clamps at the score boundary regardless.
int measureTicksBefore(const mu::engraving::Score* score, int tick)
{
    using namespace mu::engraving;
    const Measure* m = score->tick2measure(Fraction::fromTicks(tick > 0 ? tick - 1 : 0));
    if (m) {
        const int t = m->ticks().ticks();
        if (t > 0) {
            return t;
        }
    }
    return 4 * Constants::DIVISION;
}

/// Coalesce runs of consecutive contiguous short regions that share a common
/// root into a single region. A 960-tick harmony broken by upper-voice motion
/// into Cm → Csus2 → Cm → C7 (each 240 ticks, all rooted on C) is one real
/// harmonic change, not four. Without this pass each short slice gets absorbed
/// individually into a differently-rooted predecessor and the change is lost.
/// Corelli op01n08d m18 b1 (vi/III = Cm spanning b1–b2 then viio/III = Ddim at
/// b3): the four C-rooted sub-regions at b1, b1.5, b2, b2.5 (240 ticks each)
/// previously vanished into the m17 Gm region; coalescing them yields a single
/// 960-tick Cm region that clears kMinRegionTicks. The combined region inherits
/// the chord identity of the longest sub-region (the Cm variants dominate over
/// the Csus2 / C7 passing-tone misreads).
void coalesceShortSameRootRuns(std::vector<HarmonicRegion>& regions)
{
    if (regions.size() <= 1) {
        return;
    }
    constexpr int kMinRegionTicks = shv::kMinRegionTicks;
    std::vector<HarmonicRegion> coalesced;
    coalesced.reserve(regions.size());
    size_t i = 0;
    while (i < regions.size()) {
        const int dur = regions[i].endTick - regions[i].startTick;
        if (dur >= kMinRegionTicks) {
            coalesced.push_back(std::move(regions[i]));
            ++i;
            continue;
        }
        const int runRoot = regions[i].chordResult.identity.rootPc;
        // Skip coalescing when the predecessor shares the run's root: the
        // existing absorb-into-predecessor step already produces the same
        // outcome (extended predecessor of identical chord identity), so
        // running the coalesce would either be a no-op or could subtly
        // re-identify the merged region from one of the short slices.
        if (!coalesced.empty()
            && coalesced.back().chordResult.identity.rootPc == runRoot) {
            coalesced.push_back(std::move(regions[i]));
            ++i;
            continue;
        }
        size_t j = i + 1;
        int totalDur = dur;
        while (j < regions.size()) {
            const int nextDur = regions[j].endTick - regions[j].startTick;
            if (nextDur >= kMinRegionTicks) { break; }
            if (regions[j].chordResult.identity.rootPc != runRoot) { break; }
            if (regions[j].startTick != regions[j - 1].endTick) { break; }
            totalDur += nextDur;
            ++j;
        }
        // Conservative thresholds. Two filters together avoid disturbing
        // existing snapshot goldens while still rescuing the Corelli
        // op01n08d m18 b1 case (vi/III = Cm spanning b1 → b3 = 960 ticks,
        // realised as four 240-tick Cm/Csus2/Cm/C7 sub-regions after
        // Pass 2b's bass-movement splitting):
        //   • runLen ≥ 3 sub-regions — a true intervening harmony broken
        //     by upper-voice motion produces multiple sub-regions; a
        //     2-sub-region run is more often a single misread split by
        //     one passing tone and is safer to leave to absorbShortRegions.
        //   • totalDur ≥ 1.5 beats — guards against rescuing transient
        //     two-eighth-note same-root coincidences that happen to share
        //     a root with the previous region's chord.
        constexpr int kCoalesceMinRunTicks   = 3 * shv::kMinRegionTicks / 2; // 720
        constexpr size_t kCoalesceMinRunCount = 3;
        const size_t runLen = j - i;
        if (runLen >= kCoalesceMinRunCount && totalDur >= kCoalesceMinRunTicks) {
            size_t longestIdx = i;
            int longestDur = dur;
            for (size_t k = i + 1; k < j; ++k) {
                const int d = regions[k].endTick - regions[k].startTick;
                if (d > longestDur) { longestIdx = k; longestDur = d; }
            }
            HarmonicRegion combined = std::move(regions[longestIdx]);
            combined.startTick = regions[i].startTick;
            combined.endTick   = regions[j - 1].endTick;
            for (size_t k = i; k < j; ++k) {
                if (k == longestIdx) { continue; }
                mergeChordAnalysisTones(combined.tones, regions[k].tones);
            }
            if (const auto* bassTone = bassToneFromTones(combined.tones)) {
                combined.chordResult.identity.bassPc  = bassTone->pitch % 12;
                combined.chordResult.identity.bassTpc = bassTone->tpc;
            }
            coalesced.push_back(std::move(combined));
            i = j;
        } else {
            coalesced.push_back(std::move(regions[i]));
            ++i;
        }
    }
    regions = std::move(coalesced);
}

/// Collapse a candidate chord into the previous region when the two are truly
/// adjacent and carry the same root pitch-class and quality (same predicate +
/// merge body formerly inlined at the Pass-1 main-loop and Pass-2 sites). On a
/// merge the previous region's endTick is extended, its tones are merged, and
/// its bass is recomputed from the merged tones; returns true and the caller
/// skips constructing a new region. Returns false (no mutation) when the vector
/// is empty, the candidate is not contiguous with the back region, or root/
/// quality differ — the caller then builds its own region (the two call-sites
/// construct different HarmonicRegion shapes, so that else-branch stays at the
/// call-site). Takes the vector (not back()) so the original `!empty() && ...`
/// short-circuit is preserved: back() is never evaluated on an empty vector.
/// See docs/implementation_roadmap.md 0.6.
bool tryCollapseSameChordRegion(std::vector<HarmonicRegion>& regions,
                                const ChordAnalysisResult& candidate,
                                int newStartTick,
                                int newEndTick,
                                const std::vector<ChordAnalysisTone>& newTones)
{
    const bool isContiguousWithPreviousRegion = !regions.empty()
                                            && regions.back().endTick == newStartTick;
    if (!(isContiguousWithPreviousRegion
          && regions.back().chordResult.identity.rootPc == candidate.identity.rootPc
          && regions.back().chordResult.identity.quality == candidate.identity.quality)) {
        return false;
    }
    regions.back().endTick = newEndTick;
    mergeChordAnalysisTones(regions.back().tones, newTones);
    if (const auto* bassTone = bassToneFromTones(regions.back().tones)) {
        regions.back().chordResult.identity.bassPc  = bassTone->pitch % 12;
        regions.back().chordResult.identity.bassTpc = bassTone->tpc;
    }
    return true;
}

/// Pass 3 — absorb every region shorter than kMinRegionTicks into the previous
/// region, regardless of root. Greedy-expand routinely emits sub-beat slices on
/// passing tones and embellishments; analyzed in isolation they produce exotic
/// low-confidence readings (sus / add11 / non-root-bass dim) that are not real
/// harmonic changes. Merging them back into the host chord keeps the region
/// stream at chord-rhythm granularity (the granularity DCML/music21 annotate
/// at). A long genuine intervening harmony survives because it clears the
/// duration threshold; a short different-rooted slice does not.
void absorbShortRegions(std::vector<HarmonicRegion>& regions)
{
    if (regions.size() <= 1) {
        return;
    }
    constexpr int kMinRegionTicks = shv::kMinRegionTicks;
    std::vector<HarmonicRegion> filtered;
    filtered.push_back(std::move(regions[0]));
    for (size_t i = 1; i < regions.size(); ++i) {
        const int duration = regions[i].endTick - regions[i].startTick;
        if (duration < kMinRegionTicks) {
            filtered.back().endTick = regions[i].endTick;
        } else {
            filtered.push_back(std::move(regions[i]));
        }
    }
    regions = std::move(filtered);
}

/// The slice→region key reduction result (the Layer-5 override-readiness forward-carry):
/// the chosen key PLUS the representative slice's already-computed ranked alternative keys
/// and sequence-margin confidence. One clearly-named reduction so the later precise pin
/// (the L5-modulation step, cowork_layer5_function_design.md §15-3) is a single-site change.
struct RegionKeyReduction {
    KeyModeAnalysisResult chosen;                       ///< the region's chosen key (== old localKeyForRegion return)
    std::vector<KeyModeAnalysisResult> alternatives;    ///< the repSlice's ranked alt keys (excl. chosen)
    double confidence = 0.0;                            ///< the repSlice's sequence-margin confidence
};

/// Propagate the region key CONTEXT — the chosen key AND its override-readiness
/// forward-carry (alt keys + confidence) — from a parent region to a sub-region, so the
/// carried key menu travels with keyModeResult and stays consistent with it. Used at every
/// Pass-2 / Pass-2b sub-region that inherits its parent's key.
inline void inheritRegionKeyContext(HarmonicRegion& child, const HarmonicRegion& parent)
{
    child.keyModeResult   = parent.keyModeResult;
    child.keyAlternatives = parent.keyAlternatives;
    child.keyConfidence   = parent.keyConfidence;
}

/// Populate nextRootPc in each region's ChordFunction so that
/// ChordSymbolFormatter::formatRomanNumeral() can emit V/x and vii°/x labels.
/// Called after all merge/absorb passes, before returning the regions vector.
void backfillNextRootPc(std::vector<HarmonicRegion>& regions)
{
    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        regions[i].chordResult.function.nextRootPc
            = regions[i + 1].chordResult.identity.rootPc;
    }
    // The last region has no successor — nextRootPc remains -1.
}

/// Iter 87 — post-merge bass-b7 promotion. The same-root same-quality merge in
/// the main loop keeps the earlier sub-region's chord identity but updates
/// bassPc/bassTpc. When a late-entering b7 in the bass promotes a later
/// sub-region to MinorSeventh (Iter 86 stamp inside analyzeChord), the merge
/// discards that candidate identity in favour of the earlier sub-region's
/// plain triad reading. Re-apply the b7 promotion on the merged region using
/// the merged tones and final bass so the chord symbol (Am7/G, Em7/D)
/// reflects the slash bass that the analyzer already emits via formatSymbol.
///
/// This used to live in tools/batch_analyze.cpp only (the bridge relied on
/// Iter 86's intra-call stamp surviving the merge). Phase 4 moves it inside
/// the shared orchestrator so both paths get the same post-merge guarantee.
void restampBassMinorSeventhAfterMerge(
    std::vector<HarmonicRegion>& regions,
    const ChordAnalyzerPreferences& prefs)
{
    for (HarmonicRegion& r : regions) {
        if (!r.hasAnalyzedChord) { continue; }
        const int rPc = r.chordResult.identity.rootPc;
        const int bPc = r.chordResult.identity.bassPc;
        if (bPc < 0 || bPc == rPc) { continue; }
        if (((bPc - rPc + 12) % 12) != 10) { continue; }
        const ChordQuality q = r.chordResult.identity.quality;
        if (q != ChordQuality::Major && q != ChordQuality::Minor) { continue; }
        if (hasExtension(r.chordResult.identity.extensions, Extension::MinorSeventh)) { continue; }
        if (hasExtension(r.chordResult.identity.extensions, Extension::MajorSeventh)) { continue; }

        double bassPcWeight = 0.0;
        for (const auto& t : r.tones) {
            const int tonePc = ((t.pitch % 12) + 12) % 12;
            if (tonePc == bPc) {
                bassPcWeight += std::max(0.1, t.weight);
            }
        }
        if (bassPcWeight > prefs.extensionThreshold) {
            setExtension(r.chordResult.identity.extensions, Extension::MinorSeventh);
        }
    }
}

/// Dense-boundary detector for PreserveAllChanges granularity. Emits a
/// boundary every time the pitch-class set changes between adjacent ChordRest
/// segments.
std::vector<mu::engraving::Fraction> denseBoundaryTicks(
    const nmdl::NoteModel& noteModel,
    const mu::engraving::Segment* firstSeg,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;
    std::vector<Fraction> boundaries;
    boundaries.push_back(startTick);

    uint16_t prevBits = 0;
    bool havePrevious = false;

    for (const Segment* s = firstSeg; s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        std::vector<ebr::SoundingNote> sounding;
        ebr::soundingAt(noteModel, s->tick().ticks(), excludeStaves, sounding);
        if (sounding.empty()) {
            continue;
        }
        uint16_t bits = 0;
        for (const ebr::SoundingNote& sn : sounding) {
            bits |= static_cast<uint16_t>(1u << (sn.ppitch % 12));
        }
        if (!havePrevious) {
            prevBits = bits;
            havePrevious = true;
            continue;
        }
        if (bits == prevBits) {
            continue;
        }
        boundaries.push_back(s->tick());
        prevBits = bits;
    }

    return boundaries;
}

// ── J-key-iii — the joint re-key pass (the FIRST intentional production behavior
// change on the key axis; gated on jointKeyWiringEnabled(), default OFF) ─────────
//
// KEY-ONLY (J-key-iii §6/§7 decision). Pass-1 (the forward loop above) produced the
// FINAL regions with the production key K0 + chord R0.  This pass:
//   (a) re-resolves the local key candidates per FINAL region (threading prevKey —
//       IDENTICAL to the batch_analyze --dump-joint-key construction, so the soft
//       decision reproduces the measured diagnostic byte-for-byte), builds the
//       JointKeyRegionInput stream, and calls decideJointKey ONCE (frozen — no
//       fixpoint; dossier §4);
//   (b) maps the SOFT (config-A) per-region decision (tonicPc,isMajor) to a
//       KeyModeAnalysisResult and overrides region.keyModeResult.
// The CHORD is left as the production chord R0 (NOT re-emitted): a faithful per-region
// chord re-emission under the joint key cannot reproduce the multi-pass pipeline chord
// (the production chord is emitted mid-pipeline, before Pass-3 tone merging; J-key-iii
// §6/§7 measured ~6% same-key root-flip noise, i.e. the re-emission injected more
// artifact than genuine key-driven movement), so the chord-axis side-effect (the
// diatonic-root re-rank, dossier §6) is DEFERRED to a faithful mechanism.  The key axis
// alone therefore moves; BIR/chord output is byte-identical to production.  Caller
// re-runs backfillNextRootPc afterwards so V/x tonicization labels reflect the new key.
void applyJointKeyWiring(const mu::engraving::Score* score,
                         std::vector<HarmonicRegion>& regions,
                         mu::engraving::staff_idx_t refStaff,
                         const std::set<size_t>& excludeStaves,
                         const KeyModeAnalyzerPreferences& keyPrefs)
{
    using namespace mu::engraving;
    if (regions.empty() || !score) {
        return;
    }

    // Documented constant: confidence for a joint pick that is NOT among the region's
    // local candidates (a modulation-span state the Viterbi committed).  Conservative
    // and SUB-threshold (< kAnnotateKeyConfidenceThreshold 0.8) so such a region does
    // NOT spuriously open a KeyArea / fire a cadence; the matched-candidate path
    // (the common case) carries the real calibrated normalizedConfidence.  [empirical]
    constexpr double kJointModulationFallbackConfidence = 0.5;

    // (a) notation-derived inputs — IDENTICAL to the diagnostic (batch_analyze main()).
    int notatedFifths = 0;
    int declaredModeOrdinal = -1;   // -1 unknown, 0 major, 1 minor
    if (refStaff < score->nstaves() && score->staff(refStaff)) {
        const KeySigEvent kse = score->staff(refStaff)->keySigEvent(Fraction(0, 1));
        notatedFifths = static_cast<int>(kse.concertKey());
        const KeyMode km = kse.mode();
        if (km == KeyMode::MAJOR || km == KeyMode::IONIAN) {
            declaredModeOrdinal = 0;
        } else if (km == KeyMode::MINOR || km == KeyMode::AEOLIAN) {
            declaredModeOrdinal = 1;
        }
    }
    // Phrase boundaries from the single owned Layer-1.5 primitive (de-dup of the
    // former jkdPhraseBoundaryTicks; same fermata-only definition at Step A).
    const std::set<int> phraseBoundaryTicks = ebr::phraseBoundaryTicks(score);

    // (b) re-resolve local candidates per FINAL region + build the joint input stream.
    std::vector<analysis::JointKeyRegionInput> input;
    std::vector<std::vector<KeyModeAnalysisResult>> perRegionRanked;
    input.reserve(regions.size());
    perRegionRanked.reserve(regions.size());
    std::optional<KeyModeAnalysisResult> prevKey;
    for (const HarmonicRegion& hr : regions) {
        const Fraction regionStart = Fraction::fromTicks(hr.startTick);
        const auto keyRanked = kr::resolveKeyAndModeRanked(
            score, regionStart, refStaff, excludeStaves, keyPrefs,
            prevKey.has_value() ? &prevKey.value() : nullptr);
        prevKey = keyRanked.empty() ? prevKey : std::optional<KeyModeAnalysisResult>(keyRanked.front());

        analysis::JointKeyRegionInput ji;
        ji.startTick = hr.startTick;
        ji.endTick   = hr.endTick;
        ji.rootPc    = hr.hasAnalyzedChord ? hr.chordResult.identity.rootPc : -1;
        ji.quality   = hr.chordResult.identity.quality;
        uint16_t mask = 0;
        for (const auto& t : hr.tones) {
            mask |= static_cast<uint16_t>(1u << (t.pitch % 12));
        }
        ji.pitchClassMask = mask;
        bool endsPhrase = (&hr == &regions.back());
        if (!endsPhrase) {
            auto it = phraseBoundaryTicks.lower_bound(hr.startTick);
            if (it != phraseBoundaryTicks.end() && *it < hr.endTick) {
                endsPhrase = true;
            }
        }
        ji.endsPhrase = endsPhrase;
        int bassPc = hr.chordResult.identity.bassPc;
        if (bassPc < 0) {
            if (const auto* bt = bassToneFromTones(hr.tones)) {
                bassPc = bt->pitch % 12;
            }
        }
        ji.bassPc = bassPc;
        for (const auto& kc : keyRanked) {
            analysis::JointKeyLocalCandidate lc;
            lc.tonicPc    = kc.tonicPc;
            lc.isMajor    = kc.isMajor();
            lc.confidence = kc.normalizedConfidence;
            ji.localCandidates.push_back(lc);
        }
        if (hr.hasAnalyzedChord) {
            ji.chordAlts.push_back({ hr.chordResult.identity.rootPc, hr.chordResult.identity.quality });
        }
        for (const auto& alt : hr.alternatives) {
            ji.chordAlts.push_back({ alt.identity.rootPc, alt.identity.quality });
        }
        ji.prodTonicPc      = hr.keyModeResult.tonicPc;   // ECHO only (never read by the decision)
        ji.prodIsMajor      = hr.keyModeResult.isMajor();
        ji.declaredModeKnown = (declaredModeOrdinal == 0 || declaredModeOrdinal == 1);
        ji.declaredModeMinor = (declaredModeOrdinal == 1);
        input.push_back(std::move(ji));
        perRegionRanked.push_back(keyRanked);
    }

    // (c) decide ONCE (frozen) over all regions.
    const analysis::JointKeyResult jk = analysis::decideJointKey(input, notatedFifths);
    if (jk.decisions.size() != regions.size()) {
        return;   // defensive — shapes must match; leave production untouched
    }

    // (d) per-region: map the SOFT decision → keyModeResult (KEY-ONLY; chord untouched).
    for (size_t i = 0; i < regions.size(); ++i) {
        HarmonicRegion& region = regions[i];
        const analysis::JointKeyDecision& d = jk.decisions[i];
        const int  jt = d.softTonicPc;     // §5: the SOFT (config-A) decision is wired
        const bool jm = d.softIsMajor;
        if (jt < 0) {
            continue;
        }

        // §3 representation mapping (tonicPc,isMajor) → KeyModeAnalysisResult.
        KeyModeAnalysisResult km;
        km.tonicPc            = jt;
        km.mode               = jm ? KeySigMode::Ionian : KeySigMode::Aeolian;   // binary collapse (measured, §6)
        km.keySignatureFifths = keySignatureFifthsForKey(jt, jm, notatedFifths);  // home pair → notated fifths
        double conf = kJointModulationFallbackConfidence;
        double raw  = 0.0;
        for (const KeyModeAnalysisResult& lc : perRegionRanked[i]) {
            if ((((lc.tonicPc % 12) + 12) % 12) == jt && lc.isMajor() == jm) {
                conf = lc.normalizedConfidence;   // option (b): carry the matching local candidate
                raw  = lc.score;
                break;
            }
        }
        km.normalizedConfidence = conf;
        km.score                = raw;
        region.keyModeResult    = km;
        // CHORD intentionally left as the production R0 (key-only; J-key-iii §6/§7).
    }
}

} // anonymous namespace

std::vector<HarmonicRegion>
analyzeRegions(const mu::engraving::Score* score,
               const mu::engraving::Fraction& startTick,
               const mu::engraving::Fraction& endTick,
               const std::set<size_t>& excludeStaves,
               const ChordAnalyzerPreferences& prefs,
               const KeyModeAnalyzerPreferences& keyPrefs,
               const AnalyzeRegionsOptions& opts)
{
    using namespace mu::engraving;

    if (!score || endTick <= startTick) {
        return {};
    }

    // Find the first ChordRest segment at or after startTick.
    const Segment* seg = score->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) {
        return {};
    }

    // LAYER 1 — build the lossless, tie-resolved note model ONCE for this score.
    // Every tone read below derives a view over it (weightedPcView / soundingAt /
    // findTemporalContext), so the tie de-inflation and uncapped-overlap fixes
    // apply uniformly and the score is read only once per analysis.
    //
    // Production (opts.reachBack.enabled == false) builds the WHOLE score — the
    // degenerate "selection = score" — so the live path is byte-identical to before
    // the bounded-context API existed. The selection-aware reach-back capability
    // (default OFF) instead builds over the selection [startTick, endTick); the loop
    // after the decode below may then grow it earlier (cowork_layer3_reachback_design.md).
    nmdl::NoteModel noteModel = opts.reachBack.enabled
        ? nmdl::NoteModel::build(score, startTick.ticks(), endTick.ticks())
        : nmdl::NoteModel::build(score);

    // Resolve key/mode at the start of the range. Use staff 0 as the reference
    // for the key signature (all concert-pitch staves share the same key sig).
    // If staff 0 is excluded or ineligible, find the first eligible one.
    staff_idx_t refStaff = 0;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!excludeStaves.count(si) && ebr::staffIsEligible(score, si, startTick)) {
            refStaff = static_cast<staff_idx_t>(si);
            break;
        }
    }

    const auto initialRanked = kr::resolveKeyAndModeRanked(
        score, startTick, refStaff, excludeStaves, keyPrefs, nullptr);
    int keyFifths = initialRanked.front().keySignatureFifths;
    KeySigMode keyMode = initialRanked.front().mode;

    // ── LAYER 3 — whole-score key/mode SEQUENCE DECODE (replaces the per-region
    // key resolver at the Pass-1 seam) ───────────────────────────────────────
    //
    // One Viterbi decode over the Layer-2 change-point slice grid decides the
    // key/mode as a SINGLE time-consistent sequence; each Pass-1 coarse region
    // then takes its duration-majority decoder key over the slice run it spans
    // (the whole-sequence change cost replaces the resolver's per-region
    // hysteresis). The seed above (resolver @startTick) is kept ONLY to keep the
    // segmentation grid byte-stable (S2) — greedyExpandSegmentation/findTemporalContext
    // still consume keyFifths/keyMode; only the per-region key path is replaced.
    //
    // Three fidelity ties to the resolver-as-graded decoder:
    //  (1) the decode excludes the SAME staves production excludes (excludeStaves),
    //  (2) it anchors on the SAME Baroque partial-signature-corrected fifths +
    //      declared mode the resolver computes (resolveKeySignatureContext),
    //  (3) per-region confidence is the emission-scale C1 sigmoid the 0.8
    //      downstream key-confidence gates expect (set inside decode()).
    // Single-signature anchor (read at startTick) is the accepted baseline; a
    // notated mid-piece key-signature change is tracked from the notes by the
    // change cost rather than re-anchored (a deferred refinement).
    const KeyModeAnalysisResult seedKey = initialRanked.front();
    const kr::KeySignatureContext keySigCtx =
        kr::resolveKeySignatureContext(score, startTick, refStaff, excludeStaves, keyPrefs);
    std::vector<slc::Slice> slices = slc::changePointSlices(noteModel);
    std::vector<kms::SliceKeyMode> sliceKeys =
        kms::KeyModeSequenceDecoder::decode(
            slices, noteModel, keySigCtx.correctedFifths, keySigCtx.declaredMode,
            keyPrefs, kms::kDefaultKeyModeSequencePreferences, excludeStaves);

    // ── Architectural Layer 3 reach-back (selection-aware capability; default OFF) ──
    // Production builds the whole score (opts.reachBack.enabled == false), so this
    // loop never runs on the live path and the corpus stays byte-identical. On a
    // partial selection whose opening has no settled key, ask Architectural Layer 1
    // to extend EARLIER one increment at a time, re-slice (Layer 2) and re-decode
    // (Layer 3) the enlarged span, until the leading-edge key stops changing (the
    // principled convergence criterion — design §3), the hard bound is hit, or the
    // score start is reached (extend reports boundaryReached). The decoder stays a
    // pure function of the slices it is given; the loop lives here, never inside
    // decode(). A whole-score model has nothing earlier to reach, so extend() clamps
    // on the first request and the loop exits with no extension — reach-back cannot
    // fire on the corpus (design §4).
    //
    // Convergence note (measured, cc_layer3_phase3_report.md): the design's cheaper
    // proxy "a settled key is in view in the reached-back context" was found to stop
    // PREMATURELY — a single settled context measure does not anchor the leading edge
    // (the leading-edge key flips only once a confident earlier key is established
    // over a run, e.g. a V–I). So the headline criterion is implemented directly:
    // track the leading-edge SETTLED key across iterations and stop when it repeats —
    // more earlier context then cannot move it.
    if (opts.reachBack.enabled) {
        const int selStartTick = startTick.ticks();
        const double minConf = opts.reachBack.minOpeningConfidence;

        // Leading-edge slice = the first slice whose end exceeds the selection start
        // (the same upper_bound idiom as the region→slice lookup below).
        auto leadIndex = [&]() -> int {
            for (size_t i = 0; i < slices.size() && i < sliceKeys.size(); ++i) {
                if (slices[i].end > selStartTick) {
                    return static_cast<int>(i);
                }
            }
            return -1;
        };
        // The leading edge's key + whether the decoder is SETTLED on it: not marked
        // uncertain AND (when a low-confidence trigger is configured) its sequence-
        // margin confidence is at or above it.
        struct LeadKey {
            int tonic = -1; int mode = -1; bool settled = false; bool valid = false;
            bool sameKey(const LeadKey& o) const { return tonic == o.tonic && mode == o.mode; }
        };
        auto leadKey = [&]() -> LeadKey {
            const int i = leadIndex();
            if (i < 0) {
                return {};
            }
            const kms::SliceKeyMode& sk = sliceKeys[static_cast<size_t>(i)];
            return { sk.chosen.tonicPc, static_cast<int>(sk.chosen.mode),
                     !sk.uncertain && sk.confidence >= minConf, true };
        };

        // Trigger: enter the loop only when the selection's opening is UNSETTLED.
        const LeadKey opening = leadKey();
        if (opening.valid && !opening.settled) {
            LeadKey lastSettled {};   // the last settled leading-edge key seen
            int reachedSteps = 0;
            while (!noteModel.boundaryReached()
                   && reachedSteps < opts.reachBack.maxReachSteps) {
                const int incTicks = opts.reachBack.incrementTicks > 0
                    ? opts.reachBack.incrementTicks
                    : measureTicksBefore(score, noteModel.loadedStart());
                if (incTicks <= 0) {
                    break;
                }
                noteModel.extend(nmdl::NoteModel::Direction::Earlier, incTicks);
                ++reachedSteps;
                slices = slc::changePointSlices(noteModel);
                sliceKeys = kms::KeyModeSequenceDecoder::decode(
                    slices, noteModel, keySigCtx.correctedFifths, keySigCtx.declaredMode,
                    keyPrefs, kms::kDefaultKeyModeSequencePreferences, excludeStaves);

                // Converged once the leading edge is SETTLED on a key that the prior
                // settled iteration already had — more earlier context cannot move it.
                const LeadKey cur = leadKey();
                if (cur.valid && cur.settled) {
                    if (lastSettled.valid && cur.sameKey(lastSettled)) {
                        break;
                    }
                    lastSettled = cur;
                }
            }
        }
    }

    // Per-slice end ticks (slices are ordered, contiguous and covering) for an
    // O(log N) region→slice-run lookup.
    std::vector<int> sliceEnds;
    sliceEnds.reserve(slices.size());
    for (const slc::Slice& s : slices) {
        sliceEnds.push_back(s.end);
    }

    // Duration-majority decoder key for a coarse region [rs, re): the (tonic, mode)
    // holding the most ticks across the region's slice run; the representative slice
    // (the longest run-member carrying that key) supplies the labelled result and
    // its emission-scale confidence. Ties (equal total duration) resolve to the key
    // whose representative slice has the lower index — deterministic. Falls back to
    // the segmentation seed when the region overlaps no decoded slice (e.g. a region
    // outside the eligible-note span, or a degenerate all-rest model).
    auto localKeyForRegion = [&](int rs, int re) -> RegionKeyReduction {
        if (sliceKeys.empty() || re <= rs) {
            return { seedKey, {}, 0.0 };
        }
        // First slice whose end > rs (covers or follows rs).
        const auto it = std::upper_bound(sliceEnds.begin(), sliceEnds.end(), rs);
        size_t i = static_cast<size_t>(it - sliceEnds.begin());

        struct Vote { long long total = 0; int repSlice = -1; int repDur = 0; };
        std::vector<std::pair<std::pair<int, int>, Vote>> votes;   // ((tonicPc,modeIdx), Vote)
        auto voteFor = [&](int tonicPc, int modeIdx, int dur, int sliceIdx) {
            const std::pair<int, int> key{ tonicPc, modeIdx };
            for (auto& v : votes) {
                if (v.first == key) {
                    v.second.total += dur;
                    if (dur > v.second.repDur) { v.second.repDur = dur; v.second.repSlice = sliceIdx; }
                    return;
                }
            }
            votes.push_back({ key, Vote{ dur, sliceIdx, dur } });
        };

        for (; i < slices.size() && slices[i].start < re; ++i) {
            if (i >= sliceKeys.size()) {
                break;
            }
            const int ov = std::min(slices[i].end, re) - std::max(slices[i].start, rs);
            if (ov <= 0) {
                continue;
            }
            const KeyModeAnalysisResult& ck = sliceKeys[i].chosen;
            voteFor(ck.tonicPc, static_cast<int>(keyModeIndex(ck.mode)), ov, static_cast<int>(i));
        }

        if (votes.empty()) {
            return { seedKey, {}, 0.0 };
        }
        const Vote* best = nullptr;
        for (const auto& v : votes) {
            if (!best
                || v.second.total > best->total
                || (v.second.total == best->total && v.second.repSlice < best->repSlice)) {
                best = &v.second;
            }
        }
        // v1 reduction (§15-3): carry the representative slice's already-computed ranked
        // alternative keys + sequence-margin confidence alongside the chosen key.
        const kms::SliceKeyMode& rep = sliceKeys[static_cast<size_t>(best->repSlice)];
        return { rep.chosen, rep.alternatives, rep.confidence };
    };

    // Pass 1 chord-analyzer preferences. Bridge supplies pass1MinDistinctPcsForCandidate=1
    // (Iter 75 sparse-texture admission); batch leaves it at -1 (use the
    // caller's prefs.minDistinctPcsForCandidate unchanged).
    ChordAnalyzerPreferences pass1Prefs = prefs;
    if (opts.pass1MinDistinctPcsForCandidate >= 0) {
        pass1Prefs.minDistinctPcsForCandidate = opts.pass1MinDistinctPcsForCandidate;
    }

    const auto chordAnalyzer = ChordAnalyzerFactory::create();

    std::vector<HarmonicRegion> preMergeRegions;

    // ── Pass 1 — coarse boundary detection ───────────────────────────────────
    std::vector<Fraction> boundaryTicks;
    if (opts.granularity == HarmonicRegionGranularity::PreserveAllChanges) {
        boundaryTicks = denseBoundaryTicks(noteModel, seg, startTick, endTick, excludeStaves);
    } else {
        mu::composing::HarmonicSegmenterCallbacks segCallbacks;
        segCallbacks.staffIsEligible = [&](size_t s) {
            return ebr::staffIsEligible(score, s, startTick);
        };
        const bool excludeLookAhead = opts.excludeLookAheadOnDenseStart;
        segCallbacks.collectRegionTones = [&noteModel, &excludeStaves, excludeLookAhead](int s, int e) {
            return ebr::weightedPcView(noteModel, s, e, excludeStaves, -1, excludeLookAhead);
        };
        const auto placedRegions = mu::composing::greedyExpandSegmentation(
            score, startTick, endTick, excludeStaves,
            mu::composing::analysis::kDefaultChordAnalyzerPreferences,
            chordAnalyzer.get(), keyFifths, keyMode, segCallbacks);

        // Iter 77 Fix B — emit both START and END ticks of placed regions so
        // a confident anchor followed by an unplaced gap keeps its own region.
        std::set<int> boundaryTickSet;
        for (const auto& pr : placedRegions) {
            if (pr.round >= 1) {
                boundaryTickSet.insert(pr.startTick);
                boundaryTickSet.insert(pr.endTick);
            }
        }
        for (int t : boundaryTickSet) {
            if (t >= startTick.ticks() && t < endTick.ticks()) {
                boundaryTicks.push_back(Fraction::fromTicks(t));
            }
        }
        if (boundaryTicks.empty()) {
            boundaryTicks.push_back(startTick);
        }
    }

    // Pass 1 — analyze each coarse boundary region into a HarmonicRegion stream.
    // Factored into a lambda so it can be retried under a relaxed admission
    // threshold. On thin / homophonic textures greedy-expand sometimes emits a
    // single whole-score boundary; with the batch options
    // (excludeLookAheadOnDenseStart=true) that lone coarse region collapses to
    // its sparse opening, falls below minDistinctPcsForCandidate, and Pass 1
    // returns empty — at which point Pass 2/2b (gated on a non-empty Pass 1)
    // never run and the orchestrator returns nothing. The retry below rescues
    // exactly that case by re-running Pass 1 with sparse admission (=1, the
    // value the bridge already uses), letting the coarse region survive so
    // Pass 2/2b can subdivide it. The retry fires only when Pass 1 would
    // otherwise be empty, so it is a no-op for every score that already
    // produces regions (provably zero BIR impact).
    auto runPass1 = [&](int minDistinctOverride) -> std::vector<HarmonicRegion> {
        ChordAnalyzerPreferences attemptPrefs = pass1Prefs;
        attemptPrefs.minDistinctPcsForCandidate = minDistinctOverride;

        // Beam-1 chord-path decoder (Stage 3.1). It owns the path state the greedy
        // commit chain threaded by hand — the ChordTemporalContext, the rolling
        // stepwise counter and the recent-roots window — and replaces the
        // advanceTemporalContext() commit below with decoder.commit(). `temporalCtx`
        // is a live reference to that state, so every per-region input write below is
        // unchanged. Byte-identical: the decoder computes no score (analyzeChord +
        // applyHarmonicFunction run upstream of commit). See docs/decoder_design.md §§4–5.
        decode::ChordPathDecoder decoder(
            ebr::findTemporalContext(noteModel, seg, excludeStaves, keyFifths, keyMode, -1),
            attemptPrefs.decodeQualityLevel);
        ChordTemporalContext& temporalCtx = decoder.context();

        if (opts.hooks && opts.hooks->preMergeRegions) {
            preMergeRegions.clear();
        }

        std::vector<HarmonicRegion> regions;
        regions.reserve(boundaryTicks.size());

        for (size_t i = 0; i < boundaryTicks.size(); ++i) {
            const Fraction regionStart = boundaryTicks[i];
            const Fraction regionEnd   = (i + 1 < boundaryTicks.size())
                                         ? boundaryTicks[i + 1] : endTick;

            auto tones = ebr::weightedPcView(
                noteModel, regionStart.ticks(), regionEnd.ticks(), excludeStaves, -1,
                opts.excludeLookAheadOnDenseStart);
            if (tones.empty()) {
                continue;
            }

            int currentBassPc = -1;
            for (const auto& t : tones) {
                if (t.isBass) { currentBassPc = t.pitch % 12; break; }
            }
            temporalCtx.bassIsStepwiseFromPrevious =
                (temporalCtx.previousBassPc != -1 && currentBassPc != -1)
                && isDiatonicStep(temporalCtx.previousBassPc, currentBassPc);

            // Per-region key = the Layer-3 decoder's duration-majority key over the
            // region's slice run (replaces the per-region resolver + its hysteresis;
            // the whole-sequence change cost is the smoothing). See the decode above.
            const RegionKeyReduction localKeyRed =
                localKeyForRegion(regionStart.ticks(), regionEnd.ticks());
            const KeyModeAnalysisResult localKey = localKeyRed.chosen;
            const int localKeyFifths = localKey.keySignatureFifths;
            const KeySigMode localKeyMode = localKey.mode;

            // Next-region lookahead (bass + root) for joint scoring.
            int nextBassPc = -1;
            temporalCtx.nextRootPc = -1;
            if (currentBassPc != -1 && i + 1 < boundaryTicks.size()) {
                const Fraction nextRegionStart = boundaryTicks[i + 1];
                const Fraction nextRegionEnd = (i + 2 < boundaryTicks.size())
                                               ? boundaryTicks[i + 2] : endTick;
                const auto nextTones = ebr::weightedPcView(
                    noteModel, nextRegionStart.ticks(), nextRegionEnd.ticks(), excludeStaves, -1,
                    opts.excludeLookAheadOnDenseStart);
                for (const auto& nextTone : nextTones) {
                    if (nextTone.isBass) { nextBassPc = nextTone.pitch % 12; break; }
                }
                temporalCtx.nextRootPc = inferNextRootPc(
                    chordAnalyzer.get(), nextTones, localKeyFifths, localKeyMode);
            }
            temporalCtx.bassIsStepwiseToNext =
                (currentBassPc != -1 && nextBassPc != -1)
                && isDiatonicStep(currentBassPc, nextBassPc);
            temporalCtx.nextBassPc = nextBassPc;

            const Segment* regionStartSeg = score->tick2segment(
                regionStart, false, SegmentType::ChordRest);
            const Measure* currentMeasure = regionStartSeg ? regionStartSeg->measure() : nullptr;
            temporalCtx.regionMetricWeight = shv::regionMetricWeightForBeatType(
                shv::safeBeatType(currentMeasure, regionStartSeg));

            analysis::PostScoringGateContext gateCtx;
            auto results = chordAnalyzer->analyzeChord(
                tones, localKeyFifths, localKeyMode, &temporalCtx, attemptPrefs, &gateCtx);

            if (results.empty()) {
                continue;
            }

            ChordAnalysisResult chosenResult = results.front();

            // Winner selection (applyHarmonicFunction, the competition pipeline)
            // now runs inside analyzeChord(); no explicit call here.

            analysis::applyIter8691Pedal(results, gateCtx, &temporalCtx, attemptPrefs);
            analysis::applyPostScoringGates(results, attemptPrefs, &temporalCtx, gateCtx);
            chosenResult = results.empty() ? chosenResult : results.front();

            refineSparseChordQualityFromKeyContext(
                chosenResult, tones, localKeyFifths, localKeyMode);
            applyTonicPriorToSparseChord(
                chosenResult, tones, localKeyFifths, localKeyMode);

            const ChordTemporalExtensions extensionsSnapshot = toExtensionsSnapshot(temporalCtx);
            std::vector<ChordAnalysisResult> alternativesSnapshot;
            if (results.size() > 1) {
                alternativesSnapshot.assign(results.begin() + 1, results.end());
            }

            decoder.commit(chosenResult.identity, gateCtx);
            temporalCtx.nextRootPc = -1;
            temporalCtx.nextBassPc = -1;

            // Cache-ready path accumulation (Stage 3.1; inert — nothing reads
            // decoder.path() yet). winnerScore / margin mirror the predecessor-
            // confidence fields advanceTemporalContext() captures from gateCtx.
            {
                decode::ChordPathNode node;
                node.committed    = chosenResult;
                node.alternatives = alternativesSnapshot;
                node.winnerScore  = gateCtx.rawCandidates.empty()
                                    ? 0.0 : gateCtx.rawCandidates[0].score;
                node.winnerMargin = (gateCtx.rawCandidates.size() >= 2)
                                    ? gateCtx.rawCandidates[0].score - gateCtx.rawCandidates[1].score
                                    : -1.0;
                decoder.recordNode(std::move(node));
            }

            if (opts.hooks && opts.hooks->preMergeRegions) {
                HarmonicRegion preMergeRegion;
                preMergeRegion.startTick = regionStart.ticks();
                preMergeRegion.endTick = regionEnd.ticks();
                preMergeRegion.chordResult = chosenResult;
                preMergeRegion.alternatives = alternativesSnapshot;
                preMergeRegion.hasAnalyzedChord = true;
                preMergeRegion.keyModeResult = localKey;
                preMergeRegion.keyAlternatives = localKeyRed.alternatives;
                preMergeRegion.keyConfidence = localKeyRed.confidence;
                preMergeRegion.tones = tones;
                preMergeRegion.temporalExtensions = extensionsSnapshot;
                preMergeRegions.push_back(std::move(preMergeRegion));
            }

            // Collapse same-chord consecutive regions only when truly adjacent.
            // Shared with the Pass 2 site via tryCollapseSameChordRegion(); only this
            // else-branch (region construction) differs. See docs/implementation_roadmap.md 0.6.
            if (!tryCollapseSameChordRegion(regions, chosenResult,
                                            regionStart.ticks(), regionEnd.ticks(), tones)) {
                HarmonicRegion region;
                region.startTick     = regionStart.ticks();
                region.endTick       = regionEnd.ticks();
                region.chordResult   = chosenResult;
                region.alternatives  = std::move(alternativesSnapshot);
                region.hasAnalyzedChord = true;
                region.keyModeResult = localKey;
                region.keyAlternatives = localKeyRed.alternatives;
                region.keyConfidence = localKeyRed.confidence;
                region.tones         = std::move(tones);
                region.temporalExtensions = extensionsSnapshot;
                regions.push_back(std::move(region));
            }
        }

        return regions;
    };

    std::vector<HarmonicRegion> regions = runPass1(pass1Prefs.minDistinctPcsForCandidate);
    if (regions.empty() && pass1Prefs.minDistinctPcsForCandidate > 1) {
        // Sparse-admission fallback (thin-texture rescue; see runPass1 comment).
        regions = runPass1(1);
    }

    // ── Pass 2 — onset-Jaccard sub-boundary detection ────────────────────────
    if (opts.granularity != HarmonicRegionGranularity::PreserveAllChanges && !regions.empty()) {
        std::vector<HarmonicRegion> pass2Regions;
        pass2Regions.reserve(regions.size() * 2);

        for (size_t parentIdx = 0; parentIdx < regions.size(); ++parentIdx) {
            const HarmonicRegion& parentRegion = regions[parentIdx];
            const int parentDuration = parentRegion.endTick - parentRegion.startTick;
            if (parentDuration < kPass2MinRegionTicks) {
                pass2Regions.push_back(parentRegion);
                continue;
            }

            const Fraction parentStart = Fraction::fromTicks(parentRegion.startTick);
            const Fraction parentEnd   = Fraction::fromTicks(parentRegion.endTick);
            const auto subs = ebr::detectOnsetSubBoundaries(
                score, parentStart, parentEnd, excludeStaves, opts.onsetBoundaryThreshold);

            if (subs.empty()) {
                pass2Regions.push_back(parentRegion);
                continue;
            }

            std::vector<Fraction> subBounds;
            subBounds.reserve(subs.size() + 2);
            subBounds.push_back(parentStart);
            subBounds.insert(subBounds.end(), subs.begin(), subs.end());
            subBounds.push_back(parentEnd);

            const int subKeyFifths      = parentRegion.keyModeResult.keySignatureFifths;
            const KeySigMode subKeyMode = parentRegion.keyModeResult.mode;

            // Iter 94 — parent-scope previousBassPc / nextBassPc.
            const int parentPredBassPc = (parentIdx > 0)
                ? regions[parentIdx - 1].chordResult.identity.bassPc : -1;
            const int parentSuccBassPc = (parentIdx + 1 < regions.size())
                ? regions[parentIdx + 1].chordResult.identity.bassPc : -1;

            // Per-parent beam-1 decoder (Stage 3.1). Owns this parent's sub-region
            // path state (sub temporal context + rolling stepwise counter + recent-
            // roots window) and replaces the advanceTemporalContext() sub-commit with
            // subDecoder.commit(). `subCtx` is a live reference; the seeding below and
            // every per-sub input write are unchanged. The rolling counter / recent-
            // roots window start fresh per parent (the old subRunningStepwiseCount = 0
            // / subRecentRootsBuf = {-1,-1,-1}); the first sub still sees the parent-
            // seeded consecutiveBassStepwiseCount / recentRootPcs set below.
            decode::ChordPathDecoder subDecoder(ChordTemporalContext{}, prefs.decodeQualityLevel);
            ChordTemporalContext& subCtx = subDecoder.context();
            if (!pass2Regions.empty()
                && pass2Regions.back().endTick == parentRegion.startTick) {
                subCtx.previousRootPc  = pass2Regions.back().chordResult.identity.rootPc;
                subCtx.previousQuality = pass2Regions.back().chordResult.identity.quality;
                subCtx.previousBassPc  = pass2Regions.back().chordResult.identity.bassPc;
            }
            subCtx.consecutiveBassStepwiseCount
                = parentRegion.temporalExtensions.consecutiveBassStepwiseCount;
            subCtx.recentRootPcs = parentRegion.temporalExtensions.recentRootPcs;

            for (size_t si = 0; si + 1 < subBounds.size(); ++si) {
                const Fraction subStart = subBounds[si];
                const Fraction subEnd   = subBounds[si + 1];

                // Iter 93 — pass parent.startTick so onsetAtRegionStart is
                // computed at full-region scope.
                auto subTones = ebr::weightedPcView(
                    noteModel, subStart.ticks(), subEnd.ticks(), excludeStaves,
                    parentRegion.startTick, opts.excludeLookAheadOnDenseStart);

                if (subTones.empty()) {
                    HarmonicRegion gap;
                    gap.startTick        = subStart.ticks();
                    gap.endTick          = subEnd.ticks();
                    gap.chordResult      = parentRegion.chordResult;
                    gap.alternatives     = parentRegion.alternatives;
                    gap.hasAnalyzedChord = true;
                    inheritRegionKeyContext(gap, parentRegion);
                    gap.temporalExtensions = parentRegion.temporalExtensions;
                    pass2Regions.push_back(std::move(gap));
                    continue;
                }

                int subBassPc = -1;
                for (const auto& t : subTones) {
                    if (t.isBass) { subBassPc = t.pitch % 12; break; }
                }
                subCtx.bassIsStepwiseFromPrevious =
                    (subCtx.previousBassPc != -1 && subBassPc != -1)
                    && isDiatonicStep(subCtx.previousBassPc, subBassPc);
                subCtx.bassIsStepwiseToNext = false;
                {
                    const Segment* subSeg = score->tick2segment(
                        subStart, false, SegmentType::ChordRest);
                    subCtx.regionMetricWeight = shv::regionMetricWeightForBeatType(
                        shv::safeBeatType(subSeg ? subSeg->measure() : nullptr, subSeg));
                }

                // Iter 94 — parent-scope override (after stepwise booleans, before analyzeChord).
                subCtx.previousBassPc = parentPredBassPc;
                subCtx.nextBassPc     = parentSuccBassPc;

                // Iter 95 Step 2 (fine-grained) — nextRootPc from the next
                // sub-region's tones within this parent's subBounds; for the
                // last sub of the parent, fall back to the next parent's
                // whole span. Matches the old batch's per-sub lookahead that
                // w_seq / w_dim were tuned against (coarse parent-identity
                // lookup blunted the signal — see Phase 4 prompt).
                {
                    int nextStartT = -1;
                    int nextEndT   = -1;
                    if (si + 2 < subBounds.size()) {
                        nextStartT = subBounds[si + 1].ticks();
                        nextEndT   = subBounds[si + 2].ticks();
                    } else if (parentIdx + 1 < regions.size()) {
                        nextStartT = regions[parentIdx + 1].startTick;
                        nextEndT   = regions[parentIdx + 1].endTick;
                    }
                    int subNextRootPc = -1;
                    if (nextStartT >= 0 && nextEndT > nextStartT) {
                        const auto nextTones = ebr::weightedPcView(
                            noteModel, nextStartT, nextEndT, excludeStaves, -1,
                            opts.excludeLookAheadOnDenseStart);
                        subNextRootPc = inferNextRootPc(
                            chordAnalyzer.get(), nextTones, subKeyFifths, subKeyMode);
                    }
                    subCtx.nextRootPc = subNextRootPc;
                }

                analysis::PostScoringGateContext subGateCtx;
                auto subResults = chordAnalyzer->analyzeChord(
                    subTones, subKeyFifths, subKeyMode, &subCtx, prefs, &subGateCtx);

                if (subResults.empty()) {
                    HarmonicRegion fallback;
                    fallback.startTick        = subStart.ticks();
                    fallback.endTick          = subEnd.ticks();
                    fallback.chordResult      = parentRegion.chordResult;
                    fallback.hasAnalyzedChord = true;
                    inheritRegionKeyContext(fallback, parentRegion);
                    fallback.tones            = std::move(subTones);
                    fallback.temporalExtensions = toExtensionsSnapshot(subCtx);
                    pass2Regions.push_back(std::move(fallback));
                    continue;
                }

                ChordAnalysisResult chosenSub = subResults.front();

                // Winner selection (applyHarmonicFunction, the competition pipeline)
                // now runs inside analyzeChord(); no explicit call here.

                analysis::applyIter8691Pedal(subResults, subGateCtx, &subCtx, prefs);
                analysis::applyPostScoringGates(subResults, prefs, &subCtx, subGateCtx);
                chosenSub = subResults.empty() ? chosenSub : subResults.front();

                refineSparseChordQualityFromKeyContext(
                    chosenSub, subTones, subKeyFifths, subKeyMode);

                const ChordTemporalExtensions subExtSnap = toExtensionsSnapshot(subCtx);
                std::vector<ChordAnalysisResult> subAltsSnap;
                if (subResults.size() > 1) {
                    subAltsSnap.assign(subResults.begin() + 1, subResults.end());
                }

                subDecoder.commit(chosenSub.identity, subGateCtx);
                {
                    decode::ChordPathNode node;
                    node.committed    = chosenSub;
                    node.alternatives = subAltsSnap;
                    node.winnerScore  = subGateCtx.rawCandidates.empty()
                                        ? 0.0 : subGateCtx.rawCandidates[0].score;
                    node.winnerMargin = (subGateCtx.rawCandidates.size() >= 2)
                                        ? subGateCtx.rawCandidates[0].score - subGateCtx.rawCandidates[1].score
                                        : -1.0;
                    subDecoder.recordNode(std::move(node));
                }

                // Collapse same-chord consecutive regions only when truly adjacent.
                // Shared with the Pass-1 main-loop site via tryCollapseSameChordRegion();
                // only this else-branch (region construction) differs. See
                // docs/implementation_roadmap.md 0.6.
                if (!tryCollapseSameChordRegion(pass2Regions, chosenSub,
                                                subStart.ticks(), subEnd.ticks(), subTones)) {
                    HarmonicRegion subRegion;
                    subRegion.startTick        = subStart.ticks();
                    subRegion.endTick          = subEnd.ticks();
                    subRegion.chordResult      = chosenSub;
                    subRegion.alternatives     = std::move(subAltsSnap);
                    subRegion.hasAnalyzedChord = true;
                    inheritRegionKeyContext(subRegion, parentRegion);
                    subRegion.tones            = std::move(subTones);
                    subRegion.temporalExtensions = subExtSnap;
                    pass2Regions.push_back(std::move(subRegion));
                }
            }
        }

        regions = std::move(pass2Regions);
    }

    // ── Pass 2b — iterative bass-movement sub-boundaries ────────────────────
    if (opts.granularity != HarmonicRegionGranularity::PreserveAllChanges && !regions.empty()) {
        constexpr int kPass2bMinRegionTicks = shv::kPass2bMinRegionTicks;

        bool anyNewSplit = true;
        int passCount = 0;
        while (anyNewSplit && passCount < kMaxBassMovementPasses) {
            anyNewSplit = false;
            ++passCount;

            std::vector<HarmonicRegion> pass2bRegions;
            pass2bRegions.reserve(regions.size() * 2);

            for (size_t parentIdx = 0; parentIdx < regions.size(); ++parentIdx) {
                const HarmonicRegion& parentRegion = regions[parentIdx];
                const int parentDuration = parentRegion.endTick - parentRegion.startTick;
                if (parentDuration < kPass2bMinRegionTicks) {
                    pass2bRegions.push_back(parentRegion);
                    continue;
                }

                const Fraction parentStart = Fraction::fromTicks(parentRegion.startTick);
                const Fraction parentEnd   = Fraction::fromTicks(parentRegion.endTick);
                const auto subs = ebr::detectBassMovementSubBoundaries(
                    score, parentStart, parentEnd, excludeStaves);

                if (subs.empty()) {
                    pass2bRegions.push_back(parentRegion);
                    continue;
                }

                anyNewSplit = true;

                std::vector<Fraction> bounds;
                bounds.push_back(parentStart);
                for (const Fraction& t : subs) {
                    bounds.push_back(t);
                }
                bounds.push_back(parentEnd);

                const int subKeyFifths      = parentRegion.keyModeResult.keySignatureFifths;
                const KeySigMode subKeyMode = parentRegion.keyModeResult.mode;

                const int parentPredBassPc = (parentIdx > 0)
                    ? regions[parentIdx - 1].chordResult.identity.bassPc : -1;
                const int parentSuccBassPc = (parentIdx + 1 < regions.size())
                    ? regions[parentIdx + 1].chordResult.identity.bassPc : -1;

                // Per-parent beam-1 decoder (Stage 3.1) — see the Pass 2 site above.
                // Owns this parent's sub-region path state and replaces the
                // advanceTemporalContext() sub-commit with subDecoder.commit().
                // Rolling counter / recent-roots window start fresh per parent; the
                // first sub still sees the parent-seeded consecutiveBassStepwiseCount /
                // recentRootPcs set below.
                decode::ChordPathDecoder subDecoder(ChordTemporalContext{}, prefs.decodeQualityLevel);
                ChordTemporalContext& subCtx = subDecoder.context();
                if (!pass2bRegions.empty()
                    && pass2bRegions.back().endTick == parentRegion.startTick) {
                    subCtx.previousRootPc  = pass2bRegions.back().chordResult.identity.rootPc;
                    subCtx.previousQuality = pass2bRegions.back().chordResult.identity.quality;
                    subCtx.previousBassPc  = pass2bRegions.back().chordResult.identity.bassPc;
                }
                subCtx.consecutiveBassStepwiseCount
                    = parentRegion.temporalExtensions.consecutiveBassStepwiseCount;
                subCtx.recentRootPcs = parentRegion.temporalExtensions.recentRootPcs;

                for (size_t bi = 0; bi + 1 < bounds.size(); ++bi) {
                    const Fraction subStart = bounds[bi];
                    const Fraction subEnd   = bounds[bi + 1];

                    auto subTones = ebr::weightedPcView(
                        noteModel, subStart.ticks(), subEnd.ticks(), excludeStaves,
                        parentRegion.startTick, opts.excludeLookAheadOnDenseStart);

                    if (subTones.empty()) {
                        HarmonicRegion subRegion;
                        subRegion.startTick        = subStart.ticks();
                        subRegion.endTick          = subEnd.ticks();
                        subRegion.chordResult      = parentRegion.chordResult;
                        subRegion.hasAnalyzedChord = parentRegion.hasAnalyzedChord;
                        inheritRegionKeyContext(subRegion, parentRegion);
                        pass2bRegions.push_back(std::move(subRegion));
                        continue;
                    }

                    int subBassPc = -1;
                    for (const auto& t : subTones) {
                        if (t.isBass) { subBassPc = t.pitch % 12; break; }
                    }
                    subCtx.bassIsStepwiseFromPrevious =
                        (subCtx.previousBassPc != -1 && subBassPc != -1)
                        && isDiatonicStep(subCtx.previousBassPc, subBassPc);
                    subCtx.bassIsStepwiseToNext = false;
                    {
                        const Segment* subSeg = score->tick2segment(
                            subStart, false, SegmentType::ChordRest);
                        subCtx.regionMetricWeight = shv::regionMetricWeightForBeatType(
                            shv::safeBeatType(subSeg ? subSeg->measure() : nullptr, subSeg));
                    }

                    subCtx.previousBassPc = parentPredBassPc;
                    subCtx.nextBassPc     = parentSuccBassPc;

                    // Iter 95 Step 2 (fine-grained) — see Pass 2 comment above.
                    {
                        int nextStartT = -1;
                        int nextEndT   = -1;
                        if (bi + 2 < bounds.size()) {
                            nextStartT = bounds[bi + 1].ticks();
                            nextEndT   = bounds[bi + 2].ticks();
                        } else if (parentIdx + 1 < regions.size()) {
                            nextStartT = regions[parentIdx + 1].startTick;
                            nextEndT   = regions[parentIdx + 1].endTick;
                        }
                        int subNextRootPc = -1;
                        if (nextStartT >= 0 && nextEndT > nextStartT) {
                            const auto nextTones = ebr::weightedPcView(
                                noteModel, nextStartT, nextEndT, excludeStaves, -1,
                                opts.excludeLookAheadOnDenseStart);
                            subNextRootPc = inferNextRootPc(
                                chordAnalyzer.get(), nextTones, subKeyFifths, subKeyMode);
                        }
                        subCtx.nextRootPc = subNextRootPc;
                    }

                    analysis::PostScoringGateContext subGateCtx;
                    auto subResults = chordAnalyzer->analyzeChord(
                        subTones, subKeyFifths, subKeyMode, &subCtx, prefs, &subGateCtx);

                    if (subResults.empty()) {
                        HarmonicRegion subRegion;
                        subRegion.startTick        = subStart.ticks();
                        subRegion.endTick          = subEnd.ticks();
                        subRegion.chordResult      = parentRegion.chordResult;
                        subRegion.alternatives     = parentRegion.alternatives;
                        subRegion.hasAnalyzedChord = parentRegion.hasAnalyzedChord;
                        inheritRegionKeyContext(subRegion, parentRegion);
                        subRegion.tones            = std::move(subTones);
                        subRegion.temporalExtensions = toExtensionsSnapshot(subCtx);
                        pass2bRegions.push_back(std::move(subRegion));
                        continue;
                    }

                    ChordAnalysisResult chosenSub = subResults.front();

                    // Winner selection (applyHarmonicFunction, the competition
                    // pipeline) now runs inside analyzeChord(); no explicit call here.

                    analysis::applyIter8691Pedal(subResults, subGateCtx, &subCtx, prefs);
                    analysis::applyPostScoringGates(subResults, prefs, &subCtx, subGateCtx);
                    chosenSub = subResults.empty() ? chosenSub : subResults.front();

                    refineSparseChordQualityFromKeyContext(
                        chosenSub, subTones, subKeyFifths, subKeyMode);

                    const ChordTemporalExtensions subExtSnap = toExtensionsSnapshot(subCtx);
                    std::vector<ChordAnalysisResult> subAltsSnap;
                    if (subResults.size() > 1) {
                        subAltsSnap.assign(subResults.begin() + 1, subResults.end());
                    }

                    subDecoder.commit(chosenSub.identity, subGateCtx);
                    {
                        decode::ChordPathNode node;
                        node.committed    = chosenSub;
                        node.alternatives = subAltsSnap;
                        node.winnerScore  = subGateCtx.rawCandidates.empty()
                                            ? 0.0 : subGateCtx.rawCandidates[0].score;
                        node.winnerMargin = (subGateCtx.rawCandidates.size() >= 2)
                                            ? subGateCtx.rawCandidates[0].score - subGateCtx.rawCandidates[1].score
                                            : -1.0;
                        subDecoder.recordNode(std::move(node));
                    }

                    HarmonicRegion subRegion;
                    subRegion.startTick        = subStart.ticks();
                    subRegion.endTick          = subEnd.ticks();
                    subRegion.chordResult      = chosenSub;
                    subRegion.alternatives     = std::move(subAltsSnap);
                    subRegion.hasAnalyzedChord = true;
                    inheritRegionKeyContext(subRegion, parentRegion);
                    subRegion.tones            = std::move(subTones);
                    subRegion.temporalExtensions = subExtSnap;
                    pass2bRegions.push_back(std::move(subRegion));
                }
            }

            regions = std::move(pass2bRegions);
        } // end while
    }

    if (regions.empty()) {
        return {};
    }

    // ── Pass 3 — absorb short regions ────────────────────────────────────────
    if (opts.granularity == HarmonicRegionGranularity::Smoothed) {
        coalesceShortSameRootRuns(regions);
        absorbShortRegions(regions);
    }

    // Iter 87 post-merge MinorSeventh re-stamp (now on both paths).
    restampBassMinorSeventhAfterMerge(regions, prefs);

    // V/x and vii°/x tonicization labels.
    backfillNextRootPc(regions);

    // ── J-key-iii — joint re-key 2-pass (the FIRST intentional production behavior
    // change on the key axis).  Gated on jointKeyWiringEnabled(), default OFF ⇒ the
    // committed baseline is byte-identical; ON ⇒ override the per-region key with
    // decideJointKey's SOFT decision + re-emit the chord under it, then re-run the
    // tonicization backfill so V/x labels reflect the joint key. ─────────────────────
    if (analysis::jointKeyWiringEnabled()) {
        applyJointKeyWiring(score, regions, refStaff, excludeStaves, keyPrefs);
        backfillNextRootPc(regions);
    }

    // ── Output-filter (design §2 step 7): emit results only for the selection ────
    // Under reach-back the reached-back context slices anchor the carried-in key but
    // are evidence, never output. The Pass loops already scope every region to
    // [startTick, endTick), so this drops nothing in practice; it makes the
    // selection-only contract explicit and robust against any future context-span
    // leakage. Inert on the production path (reach-back disabled).
    if (opts.reachBack.enabled) {
        const int selStartTick = startTick.ticks();
        regions.erase(
            std::remove_if(regions.begin(), regions.end(),
                           [selStartTick](const HarmonicRegion& r) {
                               return r.endTick <= selStartTick;
                           }),
            regions.end());
    }

    if (opts.hooks) {
        if (opts.hooks->preMergeRegions) {
            *opts.hooks->preMergeRegions = std::move(preMergeRegions);
        }
        if (opts.hooks->postMergeRegions) {
            *opts.hooks->postMergeRegions = regions;
        }
    }

    return regions;
}

} // namespace mu::composing::analysis::region
