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

// ── The record-path variant of analyzeSection ────────────────────────────────
//
// analyzeSectionFromRecord: NotationRecord -> AnalyzedSection. See sectionrecordadapter.h for the
// contract, the isolation rules, and the provenance. DORMANT — no src/ caller yet.

#include "composing/analysis/section/sectionrecordadapter.h"

#include <algorithm>
#include <array>
#include <limits>
#include <optional>
#include <string>
#include <vector>

#include "engraving/dom/pitchspelling.h"      // Tpc::TPC_C (line-of-fifths origin: lof = tpc - TPC_C)

#include "composing/analysis/section/sectionanalyzer.h"           // groupKeyAreas + the section types
#include "composing/analysis/engravingbridge/regiontonecollector.h"   // weightedPcView (the L1 tone view)
#include "composing/analysis/notemodel/note_model.h"               // NoteModel (Layer 1)
#include "composing/analysis/joint/jointnotationrecord.h"          // NotationRecord / RecordSegment / recordDiatonicToKey
#include "composing/analysis/joint/jointdecoder.h"                 // ChordCache / SegmentSlice / PosteriorAxis
#include "composing/analysis/joint/jointprimitives.h"              // frameworkAndRoot / rootSpellingLof / Framework
#include "composing/analysis/joint/jointrender.h"                  // jointOursQuality
#include "composing/analysis/joint/labelclass.h"                   // classFromKey / LabelClass

namespace ebr = mu::composing::analysis::engravingbridge;

namespace mu::composing::analysis {

namespace {

// `joint::` below resolves to the nested namespace mu::composing::analysis::joint (this TU is inside
// mu::composing::analysis), so no alias is needed.

// The line-of-fifths origin: note_events' `lof` == tpc - TPC_C (jointfactadapter), so tpc = lof + TPC_C.
constexpr int kTpcC = static_cast<int>(mu::engraving::Tpc::TPC_C);

// The record-path assertive-exposure gate constant: the §3.3 KEY-AXIS content-score GAP (nats) whose
// duration-weighted record firing rate matches the legacy 0.8 normalizedConfidence gate's rate. From
// the P1 measurement (tools/notation_seams/exposure_constants.json, gate_family
// "kAssertiveKeyExposureThreshold / kAnnotateKeyConfidenceThreshold / hasAssertiveExposure / bucket
// upper"): legacy dur-rate 0.273902, record dur-rate 0.272871, residual 0.001031. A PRESENTATION
// constant declared on the record's gap scale — NOT a fit and NOT a [0,1] remap (the record-path
// analogue of kAnnotateKeyConfidenceThreshold = 0.8). The tentative (0.5) and mode-suffix (0.35)
// constants of the same family are declared at their consumers in P4 (OI-182); this arm needs only
// the assertive gate to set hasAssertiveExposure.
constexpr double kAssertiveKeyExposureGap = 1.055757;

// A's native scale-degree (RecordSegment.degree == LabelClass.degreeBase, an uppercase Roman or a
// chromatic token; `target` is the applied tonicization) -> the legacy 0-based diatonic degree index
// (0 = I .. 6 = VII) the cadence/pivot detectors and the Roman formatter read. Only an UNALTERED
// diatonic Roman with no applied target is a home-key scale degree; an accidental-prefixed degree
// ("bVII"), an applied/secondary chord (target non-empty), or a chromatic-family token ("It"/"Ger"/
// "Fr"/"N"/"raw:...") -> -1 (exactly as diatonicDegreeForRootPc returns -1 for an off-scale root).
// This READS A's published degree fact — it never recomputes a degree from root+key (the OI-173
// four-definitions lesson).
int recordFunctionDegree(const std::string& degreeBase, const std::string& target)
{
    if (!target.empty()) {
        return -1;
    }
    static const std::array<std::pair<const char*, int>, 7> kRoman = { {
        { "I", 0 }, { "II", 1 }, { "III", 2 }, { "IV", 3 }, { "V", 4 }, { "VI", 5 }, { "VII", 6 }
    } };
    for (const auto& r : kRoman) {
        if (degreeBase == r.first) {
            return r.second;
        }
    }
    return -1;
}

// The coarse .ours.json quality string (jointOursQuality output) -> the ChordQuality enum. The joint
// coarse quality is one of {Major, Minor, Diminished, HalfDiminished, Augmented}; anything else ->
// Unknown. (Suspended2/Suspended4/Power never arise from the joint coarse quality.)
ChordQuality qualityFromOursString(const std::string& q)
{
    if (q == "Major") {
        return ChordQuality::Major;
    }
    if (q == "Minor") {
        return ChordQuality::Minor;
    }
    if (q == "Diminished") {
        return ChordQuality::Diminished;
    }
    if (q == "HalfDiminished") {
        return ChordQuality::HalfDiminished;
    }
    if (q == "Augmented") {
        return ChordQuality::Augmented;
    }
    return ChordQuality::Unknown;
}

KeySigMode twoModeOf(bool isMajor)
{
    return isMajor ? KeySigMode::Ionian : KeySigMode::Aeolian;   // C1: the published mode axis is {major, minor}
}

// The §3.3 KEY-AXIS content-score gap the record-path exposure gates read:
//   keyAxis.scores[committed] - max(other keyAxis.scores)   (nats)
// nullopt when there is no committed reading or fewer than two scoreable candidate keys (the P1
// null-gap case; measured to be 0 segments over the snapshot corpus). Definition verbatim from
// tools/notation_seams/exposure_constants.json's `record_field`.
std::optional<double> keyAxisGap(const joint::SegmentSlice* slice)
{
    if (!slice) {
        return std::nullopt;
    }
    const joint::PosteriorAxis& ax = slice->keyAxis;
    if (ax.committed < 0 || ax.committed >= static_cast<int>(ax.scores.size()) || ax.scores.size() < 2) {
        return std::nullopt;
    }
    double best = -std::numeric_limits<double>::infinity();
    for (size_t k = 0; k < ax.scores.size(); ++k) {
        if (static_cast<int>(k) == ax.committed) {
            continue;
        }
        best = std::max(best, ax.scores[k]);
    }
    return ax.scores[static_cast<size_t>(ax.committed)] - best;
}

// The committed reading -> chordResult (identity + function), read from the record's published facts
// (§3.2). `committedContentScore` is the committed chord-axis slice score (the status-bar '(%.2f)'
// suffix carries the model probability, CSV row 37) or 0 when the slice is absent.
ChordAnalysisResult recordChordResult(const joint::RecordSegment& seg, double committedContentScore)
{
    ChordAnalysisResult res;

    ChordIdentity& id = res.identity;
    id.score = committedContentScore;
    id.rootPc = seg.rootPc.value_or(-1);
    id.rootTpc = seg.rootSpellingLof.has_value() ? *seg.rootSpellingLof + kTpcC : -1;

    // bass: the FIRST event's sounding bass (evBass[i]; the batch-render form), which the record
    // publishes as bassPerEvent.front(). The bass is a property of the sounding notes, not the class.
    std::optional<int> bassPc;
    std::optional<int> bassLof;
    if (!seg.bassPerEvent.empty()) {
        bassPc = seg.bassPerEvent.front().bassPc;
        bassLof = seg.bassPerEvent.front().spellingLof;
    }
    id.bassPc = bassPc.value_or(id.rootPc);              // fall back to the root when the event is empty
    id.bassTpc = bassLof.has_value() ? *bassLof + kTpcC : -1;
    id.quality = qualityFromOursString(joint::jointOursQuality(seg.quality));
    // id.isPedalPoint stays false — the pedal-point class suspends on the record path (the P1 ruling,
    // OI-194: the "X ped." annotation re-expresses from the voice-independent ornament class later).

    ChordFunction& fn = res.function;
    fn.degree = recordFunctionDegree(seg.degree, seg.target);
    fn.diatonicToKey = seg.diatonicToKey;
    fn.keyTonicPc = seg.tonicPc;
    fn.keyMode = twoModeOf(seg.isMajor);
    return res;
}

// The alternatives: the §3.3 chord-axis slice (every scoreable vocabulary class re-scored under the
// committed key), each resolved to identity+function under the committed key, ranked by content score
// descending, with the committed reading dropped (it is the region's chordResult). The content-score
// ordering differing from the legacy template-score ordering is an EXPECTED inference-driven
// difference (dispatch Gap-1) — classified in P6, never re-ordered toward the legacy ranking.
std::vector<ChordAnalysisResult> recordAlternatives(const joint::RecordSegment& seg,
                                                    const joint::SegmentSlice* slice,
                                                    int referenceFifths, joint::ChordCache& cache)
{
    std::vector<ChordAnalysisResult> alts;
    if (!slice) {
        return alts;
    }
    const joint::PosteriorAxis& ax = slice->chordAxis;
    // every candidate reads the SAME committed sounding bass (the notes do not change with the reading)
    const std::optional<int> bassPc =
        seg.bassPerEvent.empty() ? std::nullopt : seg.bassPerEvent.front().bassPc;

    alts.reserve(ax.labels.size());
    for (size_t k = 0; k < ax.labels.size(); ++k) {
        if (static_cast<int>(k) == ax.committed) {
            continue;                                    // the committed reading is the region's chordResult
        }
        const joint::LabelClass cls = joint::classFromKey(ax.labels[k]);
        const joint::ChordInfo& info = cache.get(cls, seg.tonicPc, seg.isMajor);

        ChordAnalysisResult alt;
        alt.identity.score = ax.scores[k];
        alt.identity.rootPc = info.root.value_or(-1);    // same root convention as the decoder/slice
        const std::optional<int> lof = joint::rootSpellingLof(cls, seg.tonicPc, seg.isMajor, referenceFifths);
        alt.identity.rootTpc = lof.has_value() ? *lof + kTpcC : -1;
        alt.identity.bassPc = bassPc.value_or(alt.identity.rootPc);
        alt.identity.quality = qualityFromOursString(joint::jointOursQuality(cls.quality()));

        alt.function.degree = recordFunctionDegree(cls.degreeBase(), cls.target());
        alt.function.diatonicToKey = joint::recordDiatonicToKey(cls);
        alt.function.keyTonicPc = seg.tonicPc;
        alt.function.keyMode = twoModeOf(seg.isMajor);
        alts.push_back(std::move(alt));
    }

    std::stable_sort(alts.begin(), alts.end(),
                     [](const ChordAnalysisResult& a, const ChordAnalysisResult& b) {
                         return a.identity.score > b.identity.score;
                     });
    return alts;
}

} // namespace

AnalyzedSection analyzeSectionFromRecord(const mu::engraving::Score* sc,
                                         const mu::engraving::Fraction& from,
                                         const mu::engraving::Fraction& to,
                                         const std::set<size_t>& excludeStaves,
                                         const joint::NotationRecord& rec)
{
    AnalyzedSection out;
    out.startTick = from.ticks();
    out.endTick   = to.ticks();

    if (!sc || to <= from) {
        return out;
    }

    // LAYER 1 — the tie-resolved note model, built once; the per-segment tone view derives over it.
    // This is the SAME composing-side L1 surface the legacy analyzeSection uses (weightedPcView), NOT
    // the notation-side collector (#7, amendment 3). The record carries no per-segment raw tones.
    const notemodel::NoteModel noteModel = notemodel::NoteModel::build(sc);

    // Resolve alternative candidate classes to roots/spellings with the decoder's own root convention
    // (chordFactorPcs[0] or chromaticRootPc). One cache for the whole section.
    joint::ChordCache cache;
    const int referenceFifths = rec.sigFifths.value_or(0);   // the notated signature (spelling reference)

    // A's decode is CONTIGUOUS by construction — the legacy gap-fill / trim / measure-layout /
    // key-stabilization machinery repairs the Pass-0 stream's holes and the record has none, so it is
    // NOT ported. One record segment overlapping [from, to) -> one AnalyzedRegion, 1:1. Segments are
    // included by span OVERLAP (the same rule as the §1 span view) and are NOT clipped — the committed
    // segmentation is preserved verbatim (clipping would fragment A's decode).
    const int fromTick = from.ticks();
    const int toTick   = to.ticks();
    out.regions.reserve(rec.segments.size());
    for (size_t si = 0; si < rec.segments.size(); ++si) {
        const joint::RecordSegment& seg = rec.segments[si];
        if (seg.endTick <= fromTick || seg.startTick >= toTick) {
            continue;                                    // segment does not overlap the window
        }
        const joint::SegmentSlice* slice = (si < rec.slices.size()) ? &rec.slices[si] : nullptr;

        const double committedContentScore =
            (slice && slice->chordAxis.committed >= 0
             && slice->chordAxis.committed < static_cast<int>(slice->chordAxis.scores.size()))
                ? slice->chordAxis.scores[static_cast<size_t>(slice->chordAxis.committed)]
                : 0.0;

        AnalyzedRegion r;
        r.startTick        = seg.startTick;
        r.endTick          = seg.endTick;
        r.hasAnalyzedChord = true;                        // A decodes every segment
        r.chordResult      = recordChordResult(seg, committedContentScore);

        // key/mode context — the C1 two-mode key; normalizedConfidence carries the RAW §3.3 key-axis
        // gap (nats), NO [0,1] remap (amendment 1); hasAssertiveExposure = gap >= the P1 constant.
        KeyModeAnalysisResult& kmr = r.keyModeResult;
        kmr.keySignatureFifths   = seg.keySignatureFifths;
        kmr.mode                 = twoModeOf(seg.isMajor);
        kmr.tonicPc              = seg.tonicPc;
        const std::optional<double> gap = keyAxisGap(slice);
        kmr.normalizedConfidence = gap.value_or(0.0);
        r.hasAssertiveExposure   = gap.has_value() && *gap >= kAssertiveKeyExposureGap;

        // tones: re-collect over the segment span from the L1 note surface (DERIVABLE; the record does
        // not carry raw tones).
        r.tones = ebr::weightedPcView(noteModel, seg.startTick, seg.endTick, excludeStaves);

        // alternatives: the §3.3 chord-axis slice, content-score ranked, committed dropped.
        r.alternatives = recordAlternatives(seg, slice, referenceFifths, cache);

        out.regions.push_back(std::move(r));
    }

    // Key-areas: the shared confidence-gated grouping (reads the stored hasAssertiveExposure).
    groupKeyAreas(out.regions, out.keyAreas);
    return out;
}

} // namespace mu::composing::analysis
