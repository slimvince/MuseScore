/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2021 MuseScore Limited
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
#include "notationcomposingbridge.h"

#include <optional>

#include "engraving/dom/chord.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"

#include "composing/analysis/analysisutils.h"
#include "composing/analysis/chordanalyzer.h"
#include "composing/analysis/harmonicrhythm.h"
#include "composing/analysis/keymodeanalyzer.h"
#include "composing/intonation/tuning_utils.h"
#include "composing/intonation/just_intonation.h"
#include "composing/intonation/tuning_system.h"
#include "composing/icomposingconfiguration.h"
#include "modularity/ioc.h"

#include "engraving/dom/durationtype.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/factory.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/pitchspelling.h"
#include "engraving/editing/editkeysig.h"
#include "engraving/dom/property.h"
#include "engraving/dom/slur.h"
#include "engraving/dom/stafftext.h"
#include "engraving/dom/tie.h"

#include <cmath>
#include <set>

using namespace mu::engraving;

namespace {

// Returns the TuningSystem selected in user preferences, falling back to
// JustIntonation if the preference is unset or refers to an unknown key.
static const mu::composing::intonation::TuningSystem& preferredTuningSystem()
{
    using namespace mu::composing::intonation;
    static muse::GlobalInject<mu::composing::IComposingConfiguration> config;
    static const JustIntonation jiFallback;

    const auto* prefs = config.get().get();
    if (prefs) {
        const TuningSystem* sys = TuningRegistry::byKey(prefs->tuningSystemKey());
        if (sys) {
            return *sys;
        }
    }
    return jiFallback;
}

} // namespace

// ── harmonicAnnotation ──────────────────────────────────────────────────────
// Declared in notationcomposingbridge.h.

namespace mu::notation {

std::string harmonicAnnotation(const Note* note)
{
    static muse::GlobalInject<mu::composing::IComposingConfiguration> config;
    const auto* prefs = config.get().get();
    if (!prefs) {
        return "";
    }


    int keyFifths = 0;
    mu::composing::analysis::KeyMode keyMode = mu::composing::analysis::KeyMode::Ionian;
    const auto chordResults = mu::composing::analysis::analyzeNoteHarmonicContext(note, keyFifths, keyMode);

    // Key/mode string (optional)
    std::string keyStr;
    if (prefs->showKeyModeInStatusBar()) {
        using mu::composing::analysis::keyModeTonicName;
        using mu::composing::analysis::keyModeSuffix;
        keyStr = std::string(keyModeTonicName(keyFifths, keyMode)) + " " + keyModeSuffix(keyMode);
    }

    // If no chord-level analysis is requested, show only key/mode (no "in" prefix)
    if (!prefs->analyzeForChordSymbols() && !prefs->analyzeForChordFunction()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    if (chordResults.empty()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    // Determine which display formats are active
    const bool wantSym      = prefs->analyzeForChordSymbols()   && prefs->showChordSymbolsInStatusBar();
    const bool wantRoman    = prefs->analyzeForChordFunction()  && prefs->showRomanNumeralsInStatusBar();
    const bool wantNashville = prefs->analyzeForChordFunction() && prefs->showNashvilleNumbersInStatusBar();

    // Build candidate strings: each entry is the parts for one analysis result,
    // separated by " / " (e.g. "Bmaj / II / 2"). Candidates separated by " | ".
    int shown = 0;
    const int maxShown = prefs->analysisAlternatives();
    std::string candidates;
    std::set<std::string> seenKeys;

    for (const auto& result : chordResults) {
        if (shown >= maxShown) {
            break;
        }

        std::string sym, roman, nashville;
        if (wantSym) {
            sym = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(result, keyFifths);
        }
        if (wantRoman) {
            roman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(result);
        }
        if (wantNashville) {
            nashville = mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(result, keyFifths);
        }

        // Skip result if nothing would be shown or if we have already shown this combination
        if (sym.empty() && roman.empty() && nashville.empty()) {
            continue;
        }
        std::string key = sym + "|" + roman + "|" + nashville;
        if (!seenKeys.insert(key).second) {
            continue;
        }

        // Assemble the parts for this candidate, then append the score
        std::string entry;
        for (const std::string& part : { sym, roman, nashville }) {
            if (part.empty()) {
                continue;
            }
            if (!entry.empty()) {
                entry += " / ";
            }
            entry += part;
        }

        if (!entry.empty()) {
            char scoreBuf[16];
            std::snprintf(scoreBuf, sizeof(scoreBuf), " (%.2f)", result.score);
            entry += scoreBuf;

            if (!candidates.empty()) {
                candidates += " | ";
            }
            candidates += entry;
            ++shown;
        }
    }

    if (candidates.empty()) {
        return keyStr.empty() ? "" : "key: " + keyStr;
    }

    const std::string headed = "Chord: " + candidates;
    if (!keyStr.empty()) {
        return headed + " in key: " + keyStr;
    }
    return headed;
}

} // namespace mu::notation

// ── Shared bridge helpers ────────────────────────────────────────────────────
// File-local utilities used by both analyzeNoteHarmonicContext() and
// analyzeHarmonicRhythm().  Extracted from the original lambda-based
// implementation so that the harmonic rhythm scanner can reuse them.

namespace {

struct SoundingNote { int ppitch; int tpc; };

/// Temporary name-based chord track detection.
/// TODO: replace with a proper Part-level flag (see backlog).
static const muse::String CHORD_TRACK_MARKER = u"Chord Track";

bool isChordTrackStaff(const mu::engraving::Score* sc, size_t si)
{
    using namespace mu::engraving;
    if (si >= sc->nstaves()) {
        return false;
    }
    const Part* part = sc->staff(si)->part();
    return part && part->partName().contains(CHORD_TRACK_MARKER);
}

/// Is this staff eligible for harmonic analysis at the given tick?
/// Excludes hidden staves, percussion instruments, and chord track staves.
bool staffIsEligible(const mu::engraving::Score* sc, size_t si,
                     const mu::engraving::Fraction& tick)
{
    using namespace mu::engraving;
    const Staff* st = sc->staff(si);
    if (!st->show()) {
        return false;
    }
    if (st->part()->instrument(tick)->useDrumset()) {
        return false;
    }
    if (isChordTrackStaff(sc, si)) {
        return false;
    }
    return true;
}

/// Collect all notes sounding at anchorSeg's tick across eligible staves.
/// Walks backward up to 4 quarter notes to catch sustained notes.
/// Staves whose index appears in excludeStaves are skipped.
void collectSoundingAt(const mu::engraving::Score* sc,
                       const mu::engraving::Segment* anchorSeg,
                       const std::set<size_t>& excludeStaves,
                       std::vector<SoundingNote>& out)
{
    using namespace mu::engraving;

    const Fraction anchorTick = anchorSeg->tick();

    auto collectCr = [&](const Segment* s, const ChordRest* cr) {
        if (!cr || !cr->isChord() || cr->isGrace()) {
            return;
        }
        if (s->tick() < anchorTick) {
            const Fraction noteEnd = s->tick() + toChord(cr)->actualTicks();
            if (noteEnd <= anchorTick) {
                return;
            }
        }
        for (const Note* n : toChord(cr)->notes()) {
            if (!n->play() || !n->visible()) {
                continue;  // skip silent notes and invisible tuning artifacts
            }
            out.push_back({ n->ppitch(), n->tpc() });
        }
    };

    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (excludeStaves.count(si) || !staffIsEligible(sc, si, anchorTick)) {
            continue;
        }
        for (int v = 0; v < VOICES; ++v) {
            collectCr(anchorSeg,
                      anchorSeg->cr(static_cast<track_idx_t>(si) * VOICES + v));
        }
    }

    const Fraction backLimit = anchorTick - Fraction(4, 1);
    for (const Segment* s = anchorSeg->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {
        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, anchorTick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                collectCr(s, s->cr(static_cast<track_idx_t>(si) * VOICES + v));
            }
        }
    }
}

/// Convert raw sounding notes to analysis tones.  Marks the lowest pitch as bass.
std::vector<mu::composing::analysis::ChordAnalysisTone>
buildTones(const std::vector<SoundingNote>& sounding)
{
    using mu::composing::analysis::ChordAnalysisTone;

    int lowestPpitch = std::numeric_limits<int>::max();
    for (const SoundingNote& sn : sounding) {
        if (sn.ppitch < lowestPpitch) {
            lowestPpitch = sn.ppitch;
        }
    }
    std::vector<ChordAnalysisTone> tones;
    tones.reserve(sounding.size());
    for (const SoundingNote& sn : sounding) {
        ChordAnalysisTone t;
        t.pitch  = sn.ppitch;
        t.tpc    = sn.tpc;
        t.isBass = (sn.ppitch == lowestPpitch);
        tones.push_back(t);
    }
    return tones;
}

/// Map MuseScore's BeatType enum to a weight for key/mode analysis.
double beatTypeToWeight(mu::engraving::BeatType bt,
                        const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs)
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

/// Exponential time decay: notes further from the analysis tick carry less weight.
/// decayRate is the multiplier per measure (4 quarter notes).
double timeDecay(double beatsAgo, double decayRate = 0.7)
{
    return std::pow(decayRate, beatsAgo / 4.0);
}

/// Count distinct pitch classes in a PitchContext vector.
int distinctPitchClasses(const std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    bool seen[12] = {};
    int count = 0;
    for (const auto& p : ctx) {
        int pc = p.pitch % 12;
        if (!seen[pc]) {
            seen[pc] = true;
            ++count;
        }
    }
    return count;
}

/// Collect pitch context into @p ctx for the window [windowStart, windowEnd].
/// Appends to whatever is already in @p ctx (so callers can pre-fill lookback
/// and incrementally extend the lookahead).
static void collectPitchContext(const mu::engraving::Score* sc,
                                const mu::engraving::Fraction& tick,
                                const mu::engraving::Fraction& windowStart,
                                const mu::engraving::Fraction& windowEnd,
                                const std::set<size_t>& excludeStaves,
                                const mu::composing::analysis::KeyModeAnalyzerPreferences& prefs,
                                std::vector<mu::composing::analysis::KeyModeAnalyzer::PitchContext>& ctx)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    static constexpr double LOOKAHEAD_WEIGHT = 0.5;

    const Measure* startMeasure = sc->tick2measure(windowStart);
    if (!startMeasure) {
        startMeasure = sc->firstMeasure();
    }
    if (!startMeasure) {
        return;
    }

    for (const Segment* s = startMeasure->first(SegmentType::ChordRest);
         s && s->tick() <= windowEnd;
         s = s->next1(SegmentType::ChordRest)) {
        const Fraction segTick = s->tick();
        if (segTick < windowStart) {
            continue;
        }

        const Measure* m = s->measure();
        const TimeSigFrac tsig(m->timesig().numerator(),
                               m->timesig().denominator());
        const BeatType bt = tsig.rtick2beatType(s->rtick().ticks());
        const double bw = beatTypeToWeight(bt, prefs);

        const double beatsFromTick =
            std::abs((segTick - tick).ticks())
            / static_cast<double>(Constants::DIVISION);
        const double decay = timeDecay(beatsFromTick);

        const bool isLookahead = (segTick > tick);
        const double lookaheadMul = isLookahead ? LOOKAHEAD_WEIGHT : 1.0;

        struct NoteInfo { int ppitch; double durationQn; };
        std::vector<NoteInfo> segNotes;
        int lowestPitch = std::numeric_limits<int>::max();

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, tick)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const double durQn = cr->actualTicks().ticks()
                                     / static_cast<double>(Constants::DIVISION);
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    const int pp = n->ppitch();
                    segNotes.push_back({ pp, durQn });
                    if (pp < lowestPitch) {
                        lowestPitch = pp;
                    }
                }
            }
        }

        for (const auto& ni : segNotes) {
            KeyModeAnalyzer::PitchContext p;
            p.pitch          = ni.ppitch;
            p.durationWeight = ni.durationQn * decay * lookaheadMul;
            p.beatWeight     = bw;
            p.isBass         = (ni.ppitch == lowestPitch);
            ctx.push_back(p);
        }
    }
}

/// Resolve key signature and mode at a tick.
///
/// Always runs the key/mode inferrer — the key signature is used as a scoring
/// prior inside the analyzer, not as a hard bypass.  Falls back to the notated
/// key signature only when pitch context is genuinely insufficient (< 3 distinct
/// pitch classes).
///
/// @param prevResult  Previous inference at a nearby earlier tick.  When
///                    supplied and the new inferred mode differs, the new mode
///                    must exceed the previous score by prefs.hysteresisMargin
///                    to cause a switch.  Pass nullptr to disable hysteresis
///                    (e.g. at the first region of a piece).
void resolveKeyAndMode(const mu::engraving::Score* sc,
                       const mu::engraving::Fraction& tick,
                       mu::engraving::staff_idx_t staffIdx,
                       const std::set<size_t>& excludeStaves,
                       int& outKeyFifths,
                       mu::composing::analysis::KeyMode& outMode,
                       double& outConfidence,
                       const mu::composing::analysis::KeyModeAnalysisResult* prevResult = nullptr,
                       double* outScore = nullptr)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    const KeySigEvent keySig = sc->staff(staffIdx)->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());
    outKeyFifths = keyFifths;

    // ── Analyzer preferences ──────────────────────────────────────────────
    // Populate from user settings (mode tier weights); all other fields keep
    // their compile-time defaults.
    KeyModeAnalyzerPreferences prefs;
    {
        static muse::GlobalInject<mu::composing::IComposingConfiguration> config;
        const auto* cfg = config.get().get();
        if (cfg) {
            const double t1 = cfg->modeTierWeight1();
            const double t2 = cfg->modeTierWeight2();
            const double t3 = cfg->modeTierWeight3();
            const double t4 = cfg->modeTierWeight4();

            prefs.modePriorIonian     = t1 + 0.2;
            prefs.modePriorAeolian    = t1;
            prefs.modePriorDorian     = t2;
            prefs.modePriorMixolydian = t2;
            prefs.modePriorLydian     = t3;
            prefs.modePriorPhrygian   = t3;
            prefs.modePriorLocrian    = t4;
        }
    }

    // ── Declared mode from key signature ─────────────────────────────────
    std::optional<mu::composing::analysis::KeyMode> declaredMode;
    {
        using EMode = mu::engraving::KeyMode;
        using AMode = mu::composing::analysis::KeyMode;
        switch (keySig.mode()) {
        case EMode::MAJOR:
        case EMode::IONIAN:      declaredMode = AMode::Ionian;     break;
        case EMode::MINOR:
        case EMode::AEOLIAN:     declaredMode = AMode::Aeolian;    break;
        case EMode::DORIAN:      declaredMode = AMode::Dorian;     break;
        case EMode::PHRYGIAN:    declaredMode = AMode::Phrygian;   break;
        case EMode::LYDIAN:      declaredMode = AMode::Lydian;     break;
        case EMode::MIXOLYDIAN:  declaredMode = AMode::Mixolydian; break;
        case EMode::LOCRIAN:     declaredMode = AMode::Locrian;    break;
        default:                 declaredMode = std::nullopt;      break;
        }
    }

    // ── Fixed lookback window (never changes across lookahead expansions) ──
    static constexpr int LOOKBACK_BEATS  = 16;
    static constexpr int INITIAL_LOOKAHEAD_BEATS = 8;

    const Fraction lookbackDuration = Fraction(LOOKBACK_BEATS, 4);
    const Fraction windowStart = (tick > lookbackDuration)
                                 ? tick - lookbackDuration
                                 : Fraction(0, 1);

    // ── Piece-start shortcut ──────────────────────────────────────────────
    //
    // When there is no lookback (the analysis tick is before one full lookback
    // window from the start) and no previous result has been established yet,
    // there is insufficient evidence to override the declared key signature.
    // Return the declared mode directly rather than risking a spurious mode
    // reading from lookahead-only evidence (which is half-weighted and thin).
    // The next region will have lookback context and will correct any error.
    if (prevResult == nullptr && declaredMode.has_value()
        && windowStart == Fraction(0, 1) && tick < lookbackDuration) {
        const int ionianTonic = ionianTonicPcFromFifths(keyFifths);
        const int tonicPc = (ionianTonic + keyModeTonicOffset(*declaredMode)) % 12;
        outMode       = *declaredMode;
        outConfidence = 0.5;
        if (outScore) *outScore = 0.0;
        // outKeyFifths already set above
        (void)tonicPc;  // available for future use
        return;
    }

    // ── Dynamic lookahead loop ────────────────────────────────────────────
    //
    // Start with INITIAL_LOOKAHEAD_BEATS.  If confidence is below the
    // threshold, extend the lookahead by prefs.dynamicLookaheadStepBeats per
    // iteration up to prefs.dynamicLookaheadMaxBeats.  This ensures the
    // opening region (pure lookahead, no lookback) accumulates enough evidence
    // before committing to a mode.
    std::vector<KeyModeAnalyzer::PitchContext> ctx;
    std::vector<KeyModeAnalysisResult> modeResults;

    int lookaheadBeats = INITIAL_LOOKAHEAD_BEATS;
    while (true) {
        ctx.clear();
        const Fraction windowEnd = tick + Fraction(lookaheadBeats, 4);
        collectPitchContext(sc, tick, windowStart, windowEnd,
                            excludeStaves, prefs, ctx);

        modeResults = KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths,
                                                      prefs, declaredMode);

        const bool confident = !modeResults.empty()
            && modeResults.front().normalizedConfidence
               >= prefs.dynamicLookaheadConfidenceThreshold;
        const bool atMax = lookaheadBeats >= prefs.dynamicLookaheadMaxBeats;

        if (confident || atMax) {
            break;
        }
        lookaheadBeats += prefs.dynamicLookaheadStepBeats;
    }

    // Fall back to notated key signature only when pitch data is insufficient
    if (modeResults.empty() || distinctPitchClasses(ctx) < 3) {
        const mu::engraving::KeyMode mode = keySig.mode();
        using CKeyMode = mu::composing::analysis::KeyMode;
        switch (mode) {
        case mu::engraving::KeyMode::MINOR:
        case mu::engraving::KeyMode::AEOLIAN:    outMode = CKeyMode::Aeolian;    break;
        case mu::engraving::KeyMode::DORIAN:     outMode = CKeyMode::Dorian;     break;
        case mu::engraving::KeyMode::PHRYGIAN:   outMode = CKeyMode::Phrygian;   break;
        case mu::engraving::KeyMode::LYDIAN:     outMode = CKeyMode::Lydian;     break;
        case mu::engraving::KeyMode::MIXOLYDIAN: outMode = CKeyMode::Mixolydian; break;
        case mu::engraving::KeyMode::LOCRIAN:    outMode = CKeyMode::Locrian;    break;
        default:                                 outMode = CKeyMode::Ionian;     break;
        }
        outConfidence = 0.0;  // no pitch data — zero confidence
        if (outScore) *outScore = 0.0;
        return;
    }

    // ── Hysteresis ───────────────────────────────────────────────────────
    //
    // If a previous inference is supplied and the new top mode differs, the
    // challenger must exceed the incumbent's score by a margin before a switch
    // is accepted.  Two tiers:
    //   • Same key signature (relative major/minor pair, e.g. D minor ↔ F major):
    //     use relativeKeyHysteresisMargin.  All diatonic notes are shared, so
    //     passing chords easily tip the balance — a higher bar is required.
    //   • Different key signature (genuine modulation):
    //     use hysteresisMargin.  Accidental evidence is more discriminating, so
    //     a lower bar is appropriate.
    const KeyModeAnalysisResult& top = modeResults.front();
    if (prevResult != nullptr && top.mode != prevResult->mode) {
        const double hysteresis = (top.keySignatureFifths == prevResult->keySignatureFifths)
                                  ? prefs.relativeKeyHysteresisMargin
                                  : prefs.hysteresisMargin;
        if (top.score < prevResult->score + hysteresis) {
            // Find the incumbent in the candidate list (it may have ranked lower).
            const KeyModeAnalysisResult* incumbent = nullptr;
            for (const auto& r : modeResults) {
                if (r.mode == prevResult->mode
                    && r.keySignatureFifths == prevResult->keySignatureFifths) {
                    incumbent = &r;
                    break;
                }
            }
            if (incumbent) {
                outKeyFifths  = incumbent->keySignatureFifths;
                outMode       = incumbent->mode;
                outConfidence = incumbent->normalizedConfidence;
                if (outScore) *outScore = incumbent->score;
                return;
            }
            // Incumbent not in candidate list — fall through and accept new mode.
        }
    }

    // Notes win — use inferred result (key signature in Ionian convention so
    // that downstream degree computation is relative to the modal tonic, not
    // the notated key signature).
    outKeyFifths  = top.keySignatureFifths;
    outMode       = top.mode;
    outConfidence = top.normalizedConfidence;
    if (outScore) *outScore = top.score;
}

/// Find the previous chord's temporal context by walking backward from seg.
mu::composing::analysis::ChordTemporalContext
findTemporalContext(const mu::engraving::Score* sc,
                    const mu::engraving::Segment* seg,
                    const std::set<size_t>& excludeStaves,
                    int keyFifths, mu::composing::analysis::KeyMode keyMode)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    ChordTemporalContext temporalCtx;
    const Fraction tick = seg->tick();

    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s != nullptr;
         s = s->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (size_t si = 0; si < sc->nstaves() && !hasAttacks; ++si) {
            if (excludeStaves.count(si) || !staffIsEligible(sc, si, tick)) {
                continue;
            }
            for (int v = 0; v < VOICES && !hasAttacks; ++v) {
                const ChordRest* cr
                    = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (cr && cr->isChord() && !cr->isGrace()) {
                    hasAttacks = true;
                }
            }
        }
        if (!hasAttacks) {
            continue;
        }

        std::vector<SoundingNote> prevSounding;
        collectSoundingAt(sc, s, excludeStaves, prevSounding);
        if (!prevSounding.empty()) {
            const auto prevTones = buildTones(prevSounding);
            const auto prevResults =
                ChordAnalyzer::analyzeChord(prevTones, keyFifths, keyMode);
            if (!prevResults.empty()) {
                temporalCtx.previousRootPc  = prevResults.front().rootPc;
                temporalCtx.previousQuality = prevResults.front().quality;
            }
        }
        break;
    }

    return temporalCtx;
}

/// Find an existing tuplet at @p tick in any track other than @p excludeTrack
/// within the given segment.  Returns nullptr if none found.
mu::engraving::Tuplet* findTupletAtTick(
    mu::engraving::Segment* seg,
    mu::engraving::track_idx_t excludeTrack)
{
    using namespace mu::engraving;
    if (!seg) {
        return nullptr;
    }
    const size_t ntracks = seg->score()->ntracks();
    for (track_idx_t t = 0; t < static_cast<track_idx_t>(ntracks); ++t) {
        if (t == excludeTrack) {
            continue;
        }
        EngravingItem* el = seg->element(t);
        if (!el || !el->isChordRest()) {
            continue;
        }
        Tuplet* tup = toChordRest(el)->tuplet();
        if (tup) {
            return tup;
        }
    }
    return nullptr;
}

/// Create a chain of tied chords from startTick to endTick in the given track,
/// with notes at the specified MIDI pitches.  TPCs are derived from the key
/// signature.  If the region aligns with an existing tuplet in another track,
/// a matching tuplet is created (or reused) in the target track.
/// Returns the first Chord created, or nullptr on failure.
mu::engraving::Chord* addChordChainFromPitches(
    mu::engraving::Score* sc,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::track_idx_t track,
    const std::vector<int>& midiPitches,
    int keySignatureFifths)
{
    using namespace mu::engraving;

    if (endTick <= startTick || midiPitches.empty()) {
        return nullptr;
    }

    Segment* seg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) {
        return nullptr;
    }

    const Key key = Key(keySignatureFifths);
    const Fraction totalDur = endTick - startTick;

    // ── Tuplet path ─────────────────────────────────────────────────────
    // If a source track has a tuplet at this tick and our region duration
    // matches one tuplet element, write a single note inside a matching
    // target tuplet (creating it on first encounter, reusing it for
    // subsequent regions within the same tuplet).
    Tuplet* srcTuplet = findTupletAtTick(seg, track);
    if (srcTuplet) {
        const Fraction elemDur = srcTuplet->baseLen().fraction()
                                 * srcTuplet->ratio().denominator()
                                 / srcTuplet->ratio().numerator();
        if (totalDur == elemDur) {
            Measure* m = sc->tick2measure(startTick);
            if (!m) {
                return nullptr;
            }

            // Check if our track already has a tuplet here (from a prior call).
            Tuplet* dstTuplet = nullptr;
            ChordRest* existingCR = toChordRest(seg->element(track));
            if (existingCR && existingCR->tuplet()) {
                dstTuplet = existingCR->tuplet();
            }

            if (!dstTuplet) {
                // First region in this tuplet — create it and fill with rests.
                // Clear space for the full tuplet duration.
                Segment* tupSeg = sc->tick2segment(srcTuplet->tick(), true,
                                                   SegmentType::ChordRest);
                if (tupSeg) {
                    sc->makeGap(tupSeg, track, srcTuplet->ticks(), nullptr);
                }

                dstTuplet = Factory::createTuplet(m);
                dstTuplet->setRatio(srcTuplet->ratio());
                dstTuplet->setBaseLen(srcTuplet->baseLen());
                dstTuplet->setTicks(srcTuplet->ticks());
                dstTuplet->setTrack(track);
                dstTuplet->setTick(srcTuplet->tick());
                dstTuplet->setParent(m);

                // Fill every slot with rests first.
                Fraction slotTick = srcTuplet->tick();
                const int nSlots = srcTuplet->ratio().numerator();
                for (int i = 0; i < nSlots; ++i) {
                    Rest* r = Factory::createRest(sc->dummy()->segment());
                    r->setTrack(track);
                    r->setDurationType(dstTuplet->baseLen());
                    r->setTicks(dstTuplet->baseLen().fraction());
                    r->setTuplet(dstTuplet);
                    sc->undoAddCR(r, m, slotTick);
                    slotTick += elemDur;
                }

                // Re-fetch segment after rest creation.
                seg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
                if (!seg) {
                    return nullptr;
                }
                existingCR = toChordRest(seg->element(track));
            }

            // Remove whatever is at our slot (rest or previous note).
            if (existingCR && existingCR->tuplet() == dstTuplet) {
                sc->undoRemoveElement(existingCR);
            }

            // Write the note.
            Chord* chord = Factory::createChord(sc->dummy()->segment());
            chord->setTrack(track);
            chord->setDurationType(dstTuplet->baseLen());
            chord->setTicks(dstTuplet->baseLen().fraction());
            chord->setTuplet(dstTuplet);

            for (int pitch : midiPitches) {
                Note* note = Factory::createNote(chord);
                note->setPitch(pitch);
                const int tpc = pitch2tpc(pitch, key, Prefer::NEAREST);
                note->setTpc1(tpc);
                note->setTpc2(tpc);
                chord->add(note);
            }

            sc->undoAddCR(chord, m, startTick);
            return chord;
        }
    }

    // ── Normal (non-tuplet) path ────────────────────────────────────────
    Fraction remaining  = totalDur;
    Fraction tick       = startTick;
    Chord*   firstChord = nullptr;
    Note*    prevNote0   = nullptr;

    while (remaining > Fraction(0, 1)) {
        if (track % VOICES != 0) {
            sc->expandVoice(seg, track);
        }

        const Fraction segCapacity = seg->measure()->endTick() - tick;
        const Fraction chunkDur    = std::min(remaining, segCapacity);
        const Fraction gapped      = sc->makeGap(seg, track, chunkDur, nullptr);
        if (gapped.isZero()) {
            break;
        }

        const std::vector<TDuration> durations = toDurationList(gapped, true);
        Fraction chunkTick    = tick;
        Note*    prevNoteLocal = prevNote0;

        for (const TDuration& d : durations) {
            Measure* measure = sc->tick2measure(chunkTick);
            if (!measure) {
                break;
            }

            Chord* chord = Factory::createChord(sc->dummy()->segment());
            chord->setTrack(track);
            chord->setDurationType(d);
            chord->setTicks(d.fraction());

            for (int pitch : midiPitches) {
                Note* note = Factory::createNote(chord);
                note->setPitch(pitch);
                const int tpc = pitch2tpc(pitch, key, Prefer::NEAREST);
                note->setTpc1(tpc);
                note->setTpc2(tpc);
                chord->add(note);
            }

            sc->undoAddCR(chord, measure, chunkTick);

            if (!firstChord) {
                firstChord = chord;
            }

            if (prevNoteLocal) {
                const Chord* prevChord = prevNoteLocal->chord();
                for (size_t i = 0; i < std::min(prevChord->notes().size(),
                                                 chord->notes().size()); ++i) {
                    Note* n1 = prevChord->notes()[i];
                    Note* n2 = chord->notes()[i];
                    Tie* tie = Factory::createTie(sc->dummy());
                    tie->setStartNote(n1);
                    tie->setEndNote(n2);
                    tie->setTick(n1->tick());
                    tie->setTick2(n2->tick());
                    tie->setTrack(track);
                    n1->setTieFor(tie);
                    n2->setTieBack(tie);
                    sc->undoAddElement(tie);
                }
            }

            prevNoteLocal = chord->notes().empty() ? nullptr : chord->notes().front();
            chunkTick    += d.fraction();
        }

        prevNote0  = prevNoteLocal;
        remaining -= gapped;
        tick       = chunkTick;

        if (remaining > Fraction(0, 1)) {
            seg = sc->tick2segment(tick, true, SegmentType::ChordRest);
            if (!seg) {
                break;
            }
        }
    }

    return firstChord;
}

} // anonymous namespace — shared bridge helpers

// ── analyzeNoteHarmonicContext ────────────────────────────────────────────────
// Implements the free function declared in composing/analysis/chordanalyzer.h.
//
// The implementation lives in the notation module rather than in composing/ because
// extracting pitch context from a selected note requires engraving types (Note,
// Chord, Segment, Staff, KeySig, …) that the composing module intentionally does
// not depend on.  This file acts as the bridge: notation knows how to walk the
// engraving model, composing knows how to analyse pitches.  The two concerns are
// kept separate — this function is the only place they meet.
namespace mu::composing::analysis {

std::vector<ChordAnalysisResult>
analyzeNoteHarmonicContext(const mu::engraving::Note* note,
                           int& outKeyFifths,
                           KeyMode& outKeyMode)
{
    using namespace mu::engraving;

    if (!note) {
        return {};
    }

    const Score*   sc   = note->score();
    const Fraction tick = note->tick();
    const Segment* seg = sc->tick2segment(tick, true, SegmentType::ChordRest);
    if (!seg) {
        return {};
    }

    // Exclude chord-track staves so their notes don't pollute the analysis.
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (isChordTrackStaff(sc, si)) {
            excludeStaves.insert(si);
        }
    }

    // If the selected note is itself on a chord-track staff, fall back to the
    // first eligible staff for key-signature lookup (same as analyzeHarmonicRhythm).
    staff_idx_t refStaff = note->staffIdx();
    if (excludeStaves.count(static_cast<size_t>(refStaff))) {
        refStaff = 0;
        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (!excludeStaves.count(si) && staffIsEligible(sc, si, tick)) {
                refStaff = static_cast<staff_idx_t>(si);
                break;
            }
        }
    }

    std::vector<SoundingNote> sounding;
    collectSoundingAt(sc, seg, excludeStaves, sounding);
    if (sounding.empty()) {
        return {};
    }

    double unusedConfidence = 0.0;
    resolveKeyAndMode(sc, tick, refStaff, excludeStaves,
                      outKeyFifths, outKeyMode, unusedConfidence);

    ChordTemporalContext temporalCtx
        = findTemporalContext(sc, seg, excludeStaves, outKeyFifths, outKeyMode);

    const auto analysisTones = buildTones(sounding);
    return ChordAnalyzer::analyzeChord(analysisTones, outKeyFifths, outKeyMode,
                                       &temporalCtx);
}

} // namespace mu::composing::analysis

// ── analyzeHarmonicRhythm ────────────────────────────────────────────────────
// Implements the free function declared in composing/analysis/harmonicrhythm.h.
//
// Scans a time range across all eligible staves, detects harmonic boundaries
// (ticks where the sounding pitch-class set changes), runs chord analysis at
// each boundary, and collapses consecutive same-chord regions into a sequence
// of HarmonicRegion structs.  Reuses the same file-local helpers as
// analyzeNoteHarmonicContext() above.
namespace mu::composing::analysis {

std::vector<HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves)
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

    // Resolve key/mode at the start of the range.  Use staff 0 as the reference
    // for the key signature (all concert-pitch staves share the same key sig).
    // If staff 0 is excluded or ineligible, find the first eligible one.
    staff_idx_t refStaff = 0;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (!excludeStaves.count(si) && staffIsEligible(score, si, startTick)) {
            refStaff = static_cast<staff_idx_t>(si);
            break;
        }
    }

    int keyFifths = 0;
    KeyMode keyMode = KeyMode::Ionian;
    double keyConfidence = 0.0;
    resolveKeyAndMode(score, startTick, refStaff, excludeStaves,
                      keyFifths, keyMode, keyConfidence);

    // ── Pass 1: detect boundaries and analyze ────────────────────────────────
    // At each ChordRest segment, collect the sounding pitch-class set (as a
    // 12-bit bitset).  When it differs from the previous set, we have a new
    // harmonic boundary.  Run chord analysis at each boundary.

    struct BoundaryAnalysis {
        Fraction tick;
        ChordAnalysisResult chordResult;
        KeyModeAnalysisResult keyModeResult;
        std::vector<ChordAnalysisTone> tones;
    };

    std::vector<BoundaryAnalysis> boundaries;

    auto pcBitset = [](const std::vector<ChordAnalysisTone>& tones) -> uint16_t {
        uint16_t bits = 0;
        for (const auto& t : tones) {
            bits |= static_cast<uint16_t>(1u << (t.pitch % 12));
        }
        return bits;
    };

    uint16_t prevBits = 0;
    ChordTemporalContext temporalCtx
        = findTemporalContext(score, seg, excludeStaves, keyFifths, keyMode);

    // Hysteresis: track the previous key/mode result so that a mode switch
    // requires a score advantage of prefs.hysteresisMargin.
    std::optional<KeyModeAnalysisResult> prevKeyResult;

    for (const Segment* s = seg;
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {

        std::vector<SoundingNote> sounding;
        collectSoundingAt(score, s, excludeStaves, sounding);
        if (sounding.empty()) {
            continue;
        }

        auto tones = buildTones(sounding);
        const uint16_t bits = pcBitset(tones);

        if (bits == prevBits && !boundaries.empty()) {
            continue;  // same pitch-class set — same region
        }
        prevBits = bits;

        // Resolve key/mode at this tick (it may change across the range).
        // Pass the previous result for hysteresis; nullptr on the first boundary.
        int localKeyFifths = keyFifths;
        KeyMode localKeyMode = keyMode;
        double localKeyConfidence = 0.0;
        double localKeyScore = 0.0;
        resolveKeyAndMode(score, s->tick(), refStaff, excludeStaves,
                          localKeyFifths, localKeyMode, localKeyConfidence,
                          prevKeyResult.has_value() ? &prevKeyResult.value() : nullptr,
                          &localKeyScore);

        const auto results = ChordAnalyzer::analyzeChord(
            tones, localKeyFifths, localKeyMode, &temporalCtx);

        if (results.empty()) {
            continue;  // < 3 distinct pitch classes — skip
        }

        // Chain temporal context forward.
        temporalCtx.previousRootPc  = results.front().rootPc;
        temporalCtx.previousQuality = results.front().quality;

        KeyModeAnalysisResult kmResult;
        kmResult.keySignatureFifths   = localKeyFifths;
        kmResult.mode                 = localKeyMode;
        kmResult.normalizedConfidence = localKeyConfidence;
        kmResult.score                = localKeyScore;

        // Update hysteresis state with the committed key result.
        prevKeyResult = kmResult;

        boundaries.push_back({ s->tick(), results.front(), kmResult,
                               std::move(tones) });
    }

    if (boundaries.empty()) {
        return {};
    }

    // ── Pass 2: build regions and collapse same-chord neighbors ──────────────
    std::vector<HarmonicRegion> regions;
    regions.reserve(boundaries.size());

    for (size_t i = 0; i < boundaries.size(); ++i) {
        const Fraction regionEnd = (i + 1 < boundaries.size())
                                   ? boundaries[i + 1].tick
                                   : endTick;

        // Collapse: if previous region has the same root and quality, extend it.
        if (!regions.empty()
            && regions.back().chordResult.rootPc == boundaries[i].chordResult.rootPc
            && regions.back().chordResult.quality == boundaries[i].chordResult.quality) {
            regions.back().endTick = regionEnd.ticks();
            continue;
        }

        HarmonicRegion region;
        region.startTick    = boundaries[i].tick.ticks();
        region.endTick      = regionEnd.ticks();
        region.chordResult  = boundaries[i].chordResult;
        region.keyModeResult = boundaries[i].keyModeResult;
        region.tones        = std::move(boundaries[i].tones);
        regions.push_back(std::move(region));
    }

    // ── Pass 3: absorb short regions (passing tones, ornaments) ──────────
    // Regions shorter than a quarter note are likely caused by passing tones
    // or brief melodic ornaments rather than genuine harmonic changes.
    // Absorb them into the preceding region.
    static constexpr int kMinRegionTicks = Constants::DIVISION;  // 1 quarter note

    if (regions.size() > 1) {
        std::vector<HarmonicRegion> filtered;
        filtered.push_back(std::move(regions[0]));

        for (size_t i = 1; i < regions.size(); ++i) {
            const int duration = regions[i].endTick - regions[i].startTick;
            if (duration < kMinRegionTicks) {
                // Absorb: extend previous region to cover this one.
                filtered.back().endTick = regions[i].endTick;
            } else {
                filtered.push_back(std::move(regions[i]));
            }
        }

        regions = std::move(filtered);
    }

    return regions;
}

// ── populateChordTrack ───────────────────────────────────────────────────────
// Implements the free function declared in composing/analysis/harmonicrhythm.h.

bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones)
{
    using namespace mu::engraving;

    if (!score || endTick <= startTick) {
        return false;
    }

    static muse::GlobalInject<mu::composing::IComposingConfiguration> composingConfig;
    const mu::composing::IComposingConfiguration* prefs = composingConfig.get().get();

    const staff_idx_t bassStaffIdx = trebleStaffIdx + 1;
    if (bassStaffIdx >= score->nstaves()) {
        return false;
    }

    // The target staves are excluded from the analysis input.
    const std::set<size_t> excludeStaves = {
        static_cast<size_t>(trebleStaffIdx),
        static_cast<size_t>(bassStaffIdx)
    };

    // ── Analyze ──────────────────────────────────────────────────────────────
    auto regions = analyzeHarmonicRhythm(score, startTick, endTick,
                                         excludeStaves);
    if (regions.empty()) {
        return false;
    }

    // ── Clear target region ──────────────────────────────────────────────────
    // Remove all existing content (notes, rests, annotations) from both staves
    // in voice 0 within the time range.  Measure rests that extend beyond the
    // target range are split: portions outside the range become proper rests.
    const track_idx_t trebleTrack = trebleStaffIdx * VOICES;
    const track_idx_t bassTrack   = bassStaffIdx * VOICES;

    for (track_idx_t track : { trebleTrack, bassTrack }) {
        // Walk each measure overlapping the target range.
        for (Measure* m = score->tick2measure(startTick);
             m && m->tick() < endTick;
             m = m->nextMeasure()) {
            const Fraction mStart = m->tick();
            const Fraction mEnd   = m->endTick();
            const Fraction clearFrom = std::max(mStart, startTick);
            const Fraction clearTo   = std::min(mEnd, endTick);

            // ── Tuplet-aware clearing ───────────────────────────────────
            // If source tracks have a tuplet at this position, we must
            // clear the full tuplet span (not just the single-element
            // range) and avoid calling setRest for the tuplet zone — the
            // tuplet path in addChordChainFromPitches handles it.
            Segment* chkSeg = score->tick2segment(clearFrom, true,
                                                   SegmentType::ChordRest);
            Tuplet* srcTup = chkSeg ? findTupletAtTick(chkSeg, track)
                                    : nullptr;
            if (srcTup) {
                const Fraction tupFrom = srcTup->tick();
                const Fraction tupTo   = tupFrom + srcTup->ticks();

                // Remove non-tuplet ChordRests that overlap the full
                // tuplet span.  Split them outside the tuplet range.
                std::vector<ChordRest*> toRemove;
                for (Segment* seg = m->first(SegmentType::ChordRest);
                     seg; seg = seg->next(SegmentType::ChordRest)) {
                    ChordRest* cr = toChordRest(seg->element(track));
                    if (!cr || cr->tuplet()) {
                        continue;
                    }
                    const Fraction crStart = cr->tick();
                    const Fraction crEnd   = crStart + cr->actualTicks();
                    if (crStart < tupTo && crEnd > tupFrom) {
                        toRemove.push_back(cr);
                    }
                }

                for (ChordRest* cr : toRemove) {
                    const Fraction crStart = cr->tick();
                    const Fraction crEnd   = crStart + cr->actualTicks();

                    // Extract pitches before removal (for chord cloning).
                    std::vector<int> pitches;
                    int crKeyFifths = 0;
                    if (cr->isChord()) {
                        for (const Note* n : toChord(cr)->notes()) {
                            pitches.push_back(n->pitch());
                        }
                        // Get key context for TPC derivation.
                        crKeyFifths = static_cast<int>(
                            cr->staff()->keySigEvent(crStart).key());
                    }

                    score->undoRemoveElement(cr);

                    // Recreate content outside the tuplet range.
                    // If it was a chord, clone as tied notes; if rest,
                    // create rests.
                    if (crStart < tupFrom) {
                        if (!pitches.empty()) {
                            addChordChainFromPitches(
                                score, crStart, tupFrom, track,
                                pitches, crKeyFifths);
                        } else {
                            score->setRest(crStart, track,
                                           tupFrom - crStart,
                                           false, nullptr);
                        }
                    }
                    if (crEnd > tupTo) {
                        if (!pitches.empty()) {
                            addChordChainFromPitches(
                                score, tupTo, crEnd, track,
                                pitches, crKeyFifths);
                        } else {
                            score->setRest(tupTo, track,
                                           crEnd - tupTo,
                                           false, nullptr);
                        }
                    }
                }
                // No setRest inside the tuplet range — tuplet path will
                // call makeGap + create tuplet + fill with rests/notes.
                continue;
            }

            // ── Normal (non-tuplet) clearing ────────────────────────────
            std::vector<ChordRest*> toRemove;
            for (Segment* seg = m->first(SegmentType::ChordRest);
                 seg; seg = seg->next(SegmentType::ChordRest)) {
                ChordRest* cr = toChordRest(seg->element(track));
                if (!cr) {
                    continue;
                }
                const Fraction crStart = cr->tick();
                const Fraction crEnd   = crStart + cr->actualTicks();
                if (crStart < clearTo && crEnd > clearFrom) {
                    toRemove.push_back(cr);
                }
            }

            for (ChordRest* cr : toRemove) {
                const Fraction crStart = cr->tick();
                const Fraction crEnd   = crStart + cr->actualTicks();

                score->undoRemoveElement(cr);

                // Re-fill portions outside [clearFrom, clearTo) with rests.
                if (crStart < clearFrom) {
                    score->setRest(crStart, track,
                                   clearFrom - crStart, false, nullptr);
                }
                if (crEnd > clearTo) {
                    score->setRest(clearTo, track,
                                   crEnd - clearTo, false, nullptr);
                }
            }

            // Fill the cleared range with rests (overwritten by notes later).
            if (!toRemove.empty()) {
                score->setRest(clearFrom, track,
                               clearTo - clearFrom, false, nullptr);
            }
        }
    }

    // Remove existing annotations (Harmony + StaffText) on the target staves.
    for (Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        std::vector<EngravingItem*> toRemove;
        for (EngravingItem* ann : s->annotations()) {
            if (!ann->isHarmony() && !ann->isStaffText()) {
                continue;
            }
            const track_idx_t t = ann->track();
            if (t / VOICES == trebleStaffIdx || t / VOICES == bassStaffIdx) {
                toRemove.push_back(ann);
            }
        }
        for (EngravingItem* ann : toRemove) {
            score->undoRemoveElement(ann);
        }
    }

    // Note: KeySig clearing is not needed here — undoChangeKeySig() in the
    // populate loop handles creating or updating key sigs at each boundary.

    // ── Stabilize key/mode and recompute degrees ─────────────────────────
    // Mode detection can flicker between ticks within the same harmonic
    // section.  We detect genuine key/mode boundaries (where the first region
    // in a new section differs from the previous section's key/mode) and force
    // all subsequent regions to use that key/mode until the next genuine
    // boundary.  Then recompute degree and diatonicToKey from the stabilized
    // key/mode so Roman numerals match the displayed mode label.
    {
        static constexpr std::array<int, 7> IONIAN_SCALE     = { 0, 2, 4, 5, 7, 9, 11 };
        static constexpr std::array<int, 7> DORIAN_SCALE      = { 0, 2, 3, 5, 7, 9, 10 };
        static constexpr std::array<int, 7> PHRYGIAN_SCALE    = { 0, 1, 3, 5, 7, 8, 10 };
        static constexpr std::array<int, 7> LYDIAN_SCALE      = { 0, 2, 4, 6, 7, 9, 11 };
        static constexpr std::array<int, 7> MIXOLYDIAN_SCALE  = { 0, 2, 4, 5, 7, 9, 10 };
        static constexpr std::array<int, 7> AEOLIAN_SCALE     = { 0, 2, 3, 5, 7, 8, 10 };
        static constexpr std::array<int, 7> LOCRIAN_SCALE     = { 0, 1, 3, 5, 6, 8, 10 };
        static constexpr std::array<const std::array<int, 7>*, 7> MODE_SCALES = {
            &IONIAN_SCALE, &DORIAN_SCALE, &PHRYGIAN_SCALE, &LYDIAN_SCALE,
            &MIXOLYDIAN_SCALE, &AEOLIAN_SCALE, &LOCRIAN_SCALE
        };

        // Pass A: find genuine boundaries and propagate forward.
        // A boundary is where the region's key/mode differs from the stable
        // (i.e., the last boundary's) key/mode.  Single-region flickers that
        // revert back are suppressed by only updating stable on transitions
        // that persist for at least 2 consecutive regions.
        int stableKeyFifths = regions.front().keyModeResult.keySignatureFifths;
        KeyMode stableMode  = regions.front().keyModeResult.mode;

        for (size_t i = 1; i < regions.size(); ++i) {
            const int rk = regions[i].keyModeResult.keySignatureFifths;
            const KeyMode rm = regions[i].keyModeResult.mode;
            if (rk != stableKeyFifths || rm != stableMode) {
                // Check if the next region also shares this new key/mode
                // (persistence check), or if this is the last region.
                bool persistent = (i + 1 >= regions.size());
                if (!persistent) {
                    const int nk = regions[i + 1].keyModeResult.keySignatureFifths;
                    const KeyMode nm = regions[i + 1].keyModeResult.mode;
                    persistent = (nk == rk && nm == rm);
                }
                if (persistent) {
                    stableKeyFifths = rk;
                    stableMode = rm;
                }
            }
            // Force this region to use the stable key/mode.
            regions[i].keyModeResult.keySignatureFifths = stableKeyFifths;
            regions[i].keyModeResult.mode = stableMode;
        }

        // Pass B: recompute degree and diatonicToKey from stabilized key/mode.
        for (auto& region : regions) {
            const int ionianPc = ionianTonicPcFromFifths(
                region.keyModeResult.keySignatureFifths);
            const int tonicPc = (ionianPc
                + keyModeTonicOffset(region.keyModeResult.mode)) % 12;
            const auto& scale =
                *MODE_SCALES[keyModeIndex(region.keyModeResult.mode)];

            int degree = -1;
            for (size_t i = 0; i < scale.size(); ++i) {
                if ((tonicPc + scale[i]) % 12 == region.chordResult.rootPc) {
                    degree = static_cast<int>(i);
                    break;
                }
            }
            region.chordResult.degree = degree;

            bool diatonic = (degree >= 0);
            if (diatonic) {
                for (const auto& tone : region.tones) {
                    const int pc = tone.pitch % 12;
                    bool inScale = false;
                    for (int interval : scale) {
                        if ((tonicPc + interval) % 12 == pc) {
                            inScale = true;
                            break;
                        }
                    }
                    if (!inScale) {
                        diatonic = false;
                        break;
                    }
                }
            }
            region.chordResult.diatonicToKey = diatonic;
        }
    }

    // ── Populate ─────────────────────────────────────────────────────────────
    bool anyWritten = false;

    // Track key/mode across regions to insert annotations only at boundaries.
    int prevKeyFifths = std::numeric_limits<int>::min();
    KeyMode prevMode  = static_cast<KeyMode>(-1);
    size_t prevRegionIdx = 0;

    for (size_t regionIdx = 0; regionIdx < regions.size(); ++regionIdx) {
        const auto& region = regions[regionIdx];
        const Fraction rStart = Fraction::fromTicks(region.startTick);
        const Fraction rEnd   = Fraction::fromTicks(region.endTick);

        const auto& chord = region.chordResult;
        const int localKeyFifths = region.keyModeResult.keySignatureFifths;
        const KeyMode localMode  = region.keyModeResult.mode;

        // ── Key signature + mode annotation at key/mode boundaries ───────
        const bool writeKeyAnnotations = !prefs || prefs->chordStaffWriteKeyAnnotations();
        if (writeKeyAnnotations && (localKeyFifths != prevKeyFifths || localMode != prevMode)) {
            // Insert a key signature only when the inferred key differs from
            // what is already notated on the chord track staves at this tick.
            // This avoids redundant key sigs while still annotating mode changes
            // (which key signatures alone cannot express).
            const int notatedFifths = static_cast<int>(
                score->staff(trebleStaffIdx)->keySigEvent(rStart).concertKey());

            if (localKeyFifths != notatedFifths) {
                Measure* m = score->tick2measure(rStart);
                if (m) {
                    KeySigEvent kse;
                    kse.setConcertKey(Key(localKeyFifths));
                    kse.setKey(Key(localKeyFifths));

                    // Staff-local key sig: create the element on each chord
                    // staff individually, without propagating to other staves.
                    for (staff_idx_t si : { trebleStaffIdx, bassStaffIdx }) {
                        Segment* ksSeg = m->undoGetSegment(
                            SegmentType::KeySig, rStart);
                        if (!ksSeg) {
                            continue;
                        }
                        const track_idx_t track = si * VOICES;
                        KeySig* existing = toKeySig(ksSeg->element(track));
                        if (existing) {
                            existing->undoChangeProperty(
                                Pid::GENERATED, false);
                            score->undo(new ChangeKeySig(
                                existing, kse, existing->showCourtesy()));
                        } else {
                            KeySig* ks = Factory::createKeySig(ksSeg);
                            ks->setParent(ksSeg);
                            ks->setTrack(track);
                            ks->setKeySigEvent(kse);
                            score->undoAddElement(ks);
                        }
                        score->staff(si)->setKey(rStart, kse);
                    }
                }
            }

            // Mode staff text above treble (e.g. "C major", "D Dorian").
            // Always written at key/mode boundaries — key sigs can't express
            // mode (keySig=0 could be C major, D Dorian, E Phrygian, …).
            Segment* textSeg = score->tick2segment(rStart, true,
                                                    SegmentType::ChordRest);
            if (textSeg) {
                using mu::composing::analysis::keyModeTonicName;
                using mu::composing::analysis::keyModeSuffix;
                using mu::composing::analysis::keyModeTonicOffset;
                using mu::composing::analysis::keyModeIsMajor;

                std::string modeLabel =
                    std::string(keyModeTonicName(localKeyFifths, localMode))
                    + " " + keyModeSuffix(localMode);

                // Key stability indicator: flag uncertain key/mode detections.
                //   confidence > 0.8  → no annotation (high confidence)
                //   0.5 – 0.8        → append "?"
                //   < 0.5            → wrap as "(X mode?)"
                const double conf = region.keyModeResult.normalizedConfidence;
                if (conf < 0.5) {
                    modeLabel = "(" + modeLabel + "?)";
                } else if (conf < 0.8) {
                    modeLabel += "?";
                }

                // Key relationship annotation (skip for the first region).
                // Written separately below the first stave.
                std::string relationLabel;
                if (prevKeyFifths != std::numeric_limits<int>::min()) {
                    auto tonicPcFromKey = [](int fifths, KeyMode mode) -> int {
                        const int ionianPc = ((fifths * 7) % 12 + 12) % 12;
                        return (ionianPc + keyModeTonicOffset(mode)) % 12;
                    };

                    const int prevTonicPc  = tonicPcFromKey(prevKeyFifths, prevMode);
                    const int localTonicPc = tonicPcFromKey(localKeyFifths, localMode);
                    const bool prevMajor   = keyModeIsMajor(prevMode);
                    const bool localMajor  = keyModeIsMajor(localMode);
                    const int fifthsDelta  = localKeyFifths - prevKeyFifths;

                    if (prevKeyFifths == localKeyFifths
                        && prevMajor != localMajor) {
                        relationLabel = localMajor
                            ? "(\u2192 relative maj)"
                            : "(\u2192 relative min)";
                    } else if (prevTonicPc == localTonicPc
                               && prevMajor != localMajor) {
                        relationLabel = localMajor
                            ? "(\u2192 parallel maj)"
                            : "(\u2192 parallel min)";
                    } else if (fifthsDelta == 1) {
                        relationLabel = "(\u2192 dominant key)";
                    } else if (fifthsDelta == -1) {
                        relationLabel = "(\u2192 subdominant key)";
                    } else if (fifthsDelta != 0) {
                        relationLabel = "(\u2192 "
                            + std::to_string(std::abs(fifthsDelta))
                            + (fifthsDelta > 0 ? "\u266f" : "\u266d")
                            + ")";
                    }
                }

                // Key/mode label above first stave.
                StaffText* st = Factory::createStaffText(textSeg);
                st->setTrack(trebleTrack);
                st->setParent(textSeg);
                st->setPlainText(muse::String::fromStdString(modeLabel));
                score->undoAddElement(st);

                // Key relationship annotation below first stave.
                if (!relationLabel.empty()) {
                    StaffText* rt = Factory::createStaffText(textSeg);
                    rt->setTrack(trebleTrack);
                    rt->setParent(textSeg);
                    rt->setPlacement(mu::engraving::PlacementV::BELOW);
                    rt->setPlainText(muse::String::fromStdString(relationLabel));
                    score->undoAddElement(rt);
                }

                // Modulation path: find the pivot chord (diatonic to both
                // old and new keys) by walking backward from the boundary.
                if (prevKeyFifths != std::numeric_limits<int>::min()
                    && (localKeyFifths != prevKeyFifths
                        || localMode != prevMode)) {
                    // Build the new key's scale pitch class set.
                    const int newIonianPc = ((localKeyFifths * 7) % 12 + 12) % 12;
                    const int newTonicOffset = keyModeTonicOffset(localMode);
                    const int modeIdx = static_cast<int>(localMode);
                    // Scale intervals for each mode
                    static constexpr int SCALES[7][7] = {
                        {0,2,4,5,7,9,11}, // Ionian
                        {0,2,3,5,7,9,10}, // Dorian
                        {0,1,3,5,7,8,10}, // Phrygian
                        {0,2,4,6,7,9,11}, // Lydian
                        {0,2,4,5,7,9,10}, // Mixolydian
                        {0,2,3,5,7,8,10}, // Aeolian
                        {0,1,3,5,6,8,10}, // Locrian
                    };
                    bool newScalePcs[12] = {};
                    const int newTonicPc = (newIonianPc + newTonicOffset) % 12;
                    for (int iv : SCALES[modeIdx]) {
                        newScalePcs[(newTonicPc + iv) % 12] = true;
                    }

                    // Walk backward from the boundary looking for a chord
                    // that is diatonic to the OLD key (degree >= 0) AND whose
                    // root falls in the NEW key's scale.
                    std::string pivotText;
                    for (size_t j = regionIdx; j > prevRegionIdx; --j) {
                        const auto& prev = regions[j - 1].chordResult;
                        if (prev.degree < 0) {
                            continue;  // non-diatonic in old key
                        }
                        if (!newScalePcs[prev.rootPc]) {
                            continue;  // not in new scale
                        }
                        // Found the pivot — format in both keys.
                        const std::string oldRoman =
                            ChordSymbolFormatter::formatRomanNumeral(prev);

                        // Re-derive degree in the new key for the roman
                        // numeral label.  Copy the chord result and override
                        // only the degree field.
                        ChordAnalysisResult pivotInNew = prev;
                        const int semisFromNewTonic =
                            ((prev.rootPc - newTonicPc) % 12 + 12) % 12;
                        pivotInNew.degree = -1;
                        for (int d = 0; d < 7; ++d) {
                            if (SCALES[modeIdx][d] == semisFromNewTonic) {
                                pivotInNew.degree = d;
                                break;
                            }
                        }
                        const std::string newRoman =
                            ChordSymbolFormatter::formatRomanNumeral(pivotInNew);

                        if (!oldRoman.empty() && !newRoman.empty()) {
                            using mu::composing::analysis::keyModeSuffix;
                            pivotText = "pivot: " + oldRoman + " in "
                                + keyModeTonicName(prevKeyFifths, prevMode)
                                + " " + keyModeSuffix(prevMode)
                                + " \u2192 " + newRoman + " in "
                                + keyModeTonicName(localKeyFifths, localMode)
                                + " " + keyModeSuffix(localMode);
                        } else {
                            pivotText = "pivot: " + oldRoman + " \u2192 "
                                + newRoman;
                        }
                        break;
                    }

                    if (pivotText.empty()) {
                        pivotText = "direct modulation";
                    }

                    StaffText* pt = Factory::createStaffText(textSeg);
                    pt->setTrack(bassTrack);
                    pt->setParent(textSeg);
                    pt->setPlainText(
                        muse::String::fromStdString(pivotText));
                    score->undoAddElement(pt);
                }
            }

            prevKeyFifths = localKeyFifths;
            prevMode      = localMode;
            prevRegionIdx = regionIdx;
        }

        // ── Voicing ──────────────────────────────────────────────────────
        int bassPitch = -1;
        std::vector<int> treblePitches;

        if (useCollectedTones && !region.tones.empty()) {
            // Use the actual sounding tones from the score at their original
            // pitches, deduplicated by exact MIDI pitch.  The lowest pitch
            // goes to the bass staff; the rest go to treble.
            std::set<int> seen;
            std::vector<int> uniquePitches;
            for (const auto& tone : region.tones) {
                if (seen.insert(tone.pitch).second) {
                    uniquePitches.push_back(tone.pitch);
                }
            }

            std::sort(uniquePitches.begin(), uniquePitches.end());

            bassPitch = uniquePitches.front();
            for (size_t i = 1; i < uniquePitches.size(); ++i) {
                treblePitches.push_back(uniquePitches[i]);
            }
        } else {
            // Canonical close-position voicing from the analysis result.
            const ClosePositionVoicing voicing = closePositionVoicing(chord);
            bassPitch = voicing.bassPitch;
            treblePitches = voicing.treblePitches;
        }

        if (bassPitch < 0) {
            continue;
        }

        // ── Notes ────────────────────────────────────────────────────────
        // Bass: root only.
        addChordChainFromPitches(score, rStart, rEnd, bassTrack,
                                 { bassPitch }, localKeyFifths);

        // Treble: upper-structure chord tones.
        if (!treblePitches.empty()) {
            addChordChainFromPitches(score, rStart, rEnd, trebleTrack,
                                     treblePitches, localKeyFifths);
        }

        // Chord-staff notes are annotation-only — silence them so they don't
        // double the playback of the source staff.
        for (Segment* ps = score->tick2segment(rStart, true, SegmentType::ChordRest);
             ps && ps->tick() < rEnd;
             ps = ps->next1(SegmentType::ChordRest)) {
            for (track_idx_t tr : { trebleTrack, bassTrack }) {
                ChordRest* cr = ps->cr(tr);
                if (!cr || !cr->isChord()) {
                    continue;
                }
                for (Note* n : toChord(cr)->notes()) {
                    n->undoChangeProperty(Pid::PLAY, false);
                }
            }
        }

        // ── Harmony elements ─────────────────────────────────────────────
        Segment* seg = score->tick2segment(rStart, true, SegmentType::ChordRest);
        if (!seg) {
            continue;
        }

        // Chord symbol above treble.
        const bool writeChordSymbols = !prefs || prefs->chordStaffWriteChordSymbols();
        const std::string symText = writeChordSymbols
            ? ChordSymbolFormatter::formatSymbol(chord, localKeyFifths) : "";
        if (!symText.empty()) {
            Harmony* h = Factory::createHarmony(seg);
            h->setTrack(trebleTrack);
            h->setParent(seg);
            h->setHarmonyType(HarmonyType::STANDARD);
            h->setHarmony(muse::String::fromStdString(symText));
            h->setPlainText(h->harmonyName());
            score->undoAddElement(h);
        }

        // Chord function notation below second stave (Roman or Nashville, per preference).
        const std::string fnKey = prefs ? prefs->chordStaffFunctionNotation() : "roman";
        if (fnKey != "none") {
            const bool useNashville = (fnKey == "nashville");
            const std::string fnText = useNashville
                ? ChordSymbolFormatter::formatNashvilleNumber(chord, localKeyFifths)
                : ChordSymbolFormatter::formatRomanNumeral(chord);
            if (!fnText.empty()) {
                Harmony* h = Factory::createHarmony(seg);
                h->setTrack(bassTrack);
                h->setParent(seg);
                h->setHarmonyType(useNashville ? HarmonyType::NASHVILLE : HarmonyType::ROMAN);
                h->setHarmony(muse::String::fromStdString(fnText));
                h->setPlainText(h->harmonyName());
                score->undoAddElement(h);
            }
        }

        // Non-diatonic chord marker (borrowed chord / secondary dominant).
        // Only annotate when we can identify the source key; purely chromatic
        // chords that fit no diatonic scale are left without a marker.
        const bool highlightNonDiatonic = !prefs || prefs->chordStaffHighlightNonDiatonic();
        if (highlightNonDiatonic && !chord.diatonicToKey) {
            // Borrowed chord source key: find the nearest key (by circle-of-
            // fifths distance) in which all of this chord's quality tones are
            // diatonic.  Check all 7 modes × 15 keys (84 candidates).
            using mu::composing::analysis::keyModeTonicName;
            using mu::composing::analysis::keyModeSuffix;
            using mu::composing::analysis::keyModeTonicOffset;
            using mu::composing::analysis::KEY_MODE_COUNT;
            using mu::composing::analysis::keyModeFromIndex;

            static constexpr int SCALES[7][7] = {
                {0,2,4,5,7,9,11}, // Ionian
                {0,2,3,5,7,9,10}, // Dorian
                {0,1,3,5,7,8,10}, // Phrygian
                {0,2,4,6,7,9,11}, // Lydian
                {0,2,4,5,7,9,10}, // Mixolydian
                {0,2,3,5,7,8,10}, // Aeolian
                {0,1,3,5,6,8,10}, // Locrian
            };

            bool chordPcs[12] = {};
            for (int pc : mu::composing::analysis::chordTonePitchClasses(chord)) {
                chordPcs[pc % 12] = true;
            }

            int bestFifths = localKeyFifths;
            KeyMode bestMode = localMode;
            int bestDist = std::numeric_limits<int>::max();

            for (int candidateFifths = -7; candidateFifths <= 7; ++candidateFifths) {
                if (candidateFifths == localKeyFifths) {
                    continue;
                }
                const int dist = std::abs(candidateFifths - localKeyFifths);
                if (dist >= bestDist) {
                    continue;
                }
                const int ionianPc = ((candidateFifths * 7) % 12 + 12) % 12;
                for (size_t mi = 0; mi < KEY_MODE_COUNT; ++mi) {
                    const int tonicPc = (ionianPc + keyModeTonicOffset(keyModeFromIndex(mi))) % 12;
                    bool scalePcs[12] = {};
                    for (int iv : SCALES[mi]) {
                        scalePcs[(tonicPc + iv) % 12] = true;
                    }
                    bool allIn = true;
                    for (int pc = 0; pc < 12; ++pc) {
                        if (chordPcs[pc] && !scalePcs[pc]) { allIn = false; break; }
                    }
                    if (!allIn) {
                        continue;
                    }
                    if (dist < bestDist
                        || (dist == bestDist && (mi == 0 || mi == 5))) {
                        bestDist = dist;
                        bestFifths = candidateFifths;
                        bestMode = keyModeFromIndex(mi);
                    }
                }
            }

            // Only write the marker when a source key was found.
            if (bestDist < std::numeric_limits<int>::max()) {
                // Star above second stave.
                StaffText* ndt = Factory::createStaffText(seg);
                ndt->setTrack(bassTrack);
                ndt->setParent(seg);
                ndt->setPlainText(muse::String(u"\u2605"));  // ★
                score->undoAddElement(ndt);

                // Source key label above second stave (no "from" prefix).
                std::string borrowLabel =
                    std::string(keyModeTonicName(bestFifths, bestMode))
                    + " " + keyModeSuffix(bestMode);
                StaffText* bt = Factory::createStaffText(seg);
                bt->setTrack(bassTrack);
                bt->setParent(seg);
                bt->setPlainText(muse::String::fromStdString(borrowLabel));
                score->undoAddElement(bt);
            }
        }

        anyWritten = true;
    }

    // ── Cadence markers ─────────────────────────────────────────────────────
    // Detect standard cadence patterns from consecutive region pairs and
    // annotate the resolution chord with a staff text label on the bass staff.
    //   Authentic  (PAC): V → I
    //   Plagal     (PC):  IV → I
    //   Deceptive  (DC):  V → vi
    //   Half       (HC):  → V  (last region, or followed by key change)
    const bool writeCadenceMarkers = !prefs || prefs->chordStaffWriteCadenceMarkers();
    if (writeCadenceMarkers)
    for (size_t i = 0; i + 1 < regions.size(); ++i) {
        const auto& a = regions[i].chordResult;
        const auto& b = regions[i + 1].chordResult;

        // Cadences require same key context and different chord roots.
        if (regions[i].keyModeResult.keySignatureFifths
            != regions[i + 1].keyModeResult.keySignatureFifths
            || regions[i].keyModeResult.mode
               != regions[i + 1].keyModeResult.mode) {
            continue;  // key change — not a cadence
        }
        if (a.rootPc == b.rootPc) {
            continue;  // same root (e.g. F#m → F#7) — not a cadence
        }

        const char* label = nullptr;

        // PAC: V → I (major dominant) or viio → I (leading-tone diminished).
        if (b.degree == 0
            && ((a.degree == 4 && a.quality != ChordQuality::Minor)
                || (a.degree == 6 && a.quality == ChordQuality::Diminished))) {
            label = "PAC";        // Authentic: V → I  or  viio → I
        } else if (a.degree == 3 && b.degree == 0) {
            label = "PC";         // Plagal: IV → I
        } else if (a.degree == 4 && b.degree == 5
                   && a.quality != ChordQuality::Minor
                   && b.quality == ChordQuality::Minor) {
            label = "DC";         // Deceptive: V → vi
        }

        if (label) {
            const Fraction bStart = Fraction::fromTicks(regions[i + 1].startTick);
            Segment* cSeg = score->tick2segment(bStart, true,
                                                 SegmentType::ChordRest);
            if (cSeg) {
                StaffText* ct = Factory::createStaffText(cSeg);
                ct->setTrack(bassTrack);
                ct->setParent(cSeg);
                ct->setPlainText(muse::String::fromStdString(label));
                score->undoAddElement(ct);
            }
        }
    }

    // Half cadence: last region is V (dominant arrival at end of range).
    if (writeCadenceMarkers && !regions.empty() && regions.back().chordResult.degree == 4) {
        const Fraction hStart = Fraction::fromTicks(regions.back().startTick);
        Segment* hSeg = score->tick2segment(hStart, true,
                                             SegmentType::ChordRest);
        if (hSeg) {
            StaffText* hc = Factory::createStaffText(hSeg);
            hc->setTrack(bassTrack);
            hc->setParent(hSeg);
            hc->setPlainText(muse::String(u"HC"));
            score->undoAddElement(hc);
        }
    }

    return anyWritten;
}

} // namespace mu::composing::analysis

// ── applyTuningAtNote ─────────────────────────────────────────────────────────
// Implements the free function declared in composing/intonation/tuning_system.h.
//
// Phase 2: applies tuning to notes that attack at the selected note's tick.
// Phase 3: handles sustained notes via split-and-tie score mutation.
namespace mu::composing::intonation {

namespace {

// Walk the tieFor chain starting at @p root, calling @p fn on each Chord.
template<typename Fn>
void forEachChordInChain(mu::engraving::Chord* root, Fn fn)
{
    mu::engraving::Chord* c = root;
    while (c) {
        fn(c);
        mu::engraving::Chord* next = nullptr;
        if (!c->notes().empty()) {
            mu::engraving::Tie* t = c->notes().front()->tieFor();
            next = (t && t->endNote()) ? t->endNote()->chord() : nullptr;
        }
        c = next;
    }
}


// Create a chain of tied chords from @p startTick to @p endTick in @p track,
// copying note pitches/TPCs from @p srcChord.  Returns the first Chord
// created, or nullptr on failure.  The caller is responsible for setting
// visibility and tuning on the resulting chain.
//
// Follows the same pattern as the internal setChord() function used by
// Score::cmdRealizeChordSymbols().
mu::engraving::Chord* addChordChain(mu::engraving::Score*          sc,
                                     const mu::engraving::Fraction&  startTick,
                                     const mu::engraving::Fraction&  endTick,
                                     mu::engraving::track_idx_t       track,
                                     const mu::engraving::Chord*      srcChord)
{
    using namespace mu::engraving;

    if (endTick <= startTick || !srcChord || srcChord->notes().empty()) {
        return nullptr;
    }

    Segment* seg = sc->tick2segment(startTick, true, SegmentType::ChordRest);
    if (!seg) {
        return nullptr;
    }

    Fraction    remaining  = endTick - startTick;
    Fraction    tick       = startTick;
    Chord*      firstChord = nullptr;
    Note*       prevNote0  = nullptr;   // first-note of previous chord, for tying

    while (remaining > Fraction(0, 1)) {
        // Expand secondary voice with rests if it has no content yet.
        if (track % VOICES != 0) {
            sc->expandVoice(seg, track);
        }

        // Clip this chunk to the current measure boundary.
        const Fraction segCapacity = seg->measure()->endTick() - tick;
        const Fraction chunkDur    = std::min(remaining, segCapacity);

        const Fraction gapped = sc->makeGap(seg, track, chunkDur, nullptr);
        if (gapped.isZero()) {
            break;
        }

        // Decompose gapped duration into standard note values (may need dots/ties).
        const std::vector<TDuration> durations = toDurationList(gapped, /*useDots=*/true);
        Fraction chunkTick = tick;

        // Track the previous note for internal ties within this chunk.
        Note* prevNoteLocal = prevNote0;

        for (const TDuration& d : durations) {
            Measure* measure = sc->tick2measure(chunkTick);
            if (!measure) {
                break;
            }

            // Build a new chord with all notes copied from srcChord.
            Chord* chord = Factory::createChord(sc->dummy()->segment());
            chord->setTrack(track);
            chord->setDurationType(d);
            chord->setTicks(d.fraction());

            for (const Note* srcNote : srcChord->notes()) {
                Note* note = Factory::createNote(chord);
                note->setPitch(srcNote->pitch());
                note->setTpc1(srcNote->tpc1());
                note->setTpc2(srcNote->tpc2());
                chord->add(note);
            }

            sc->undoAddCR(chord, measure, chunkTick);

            if (!firstChord) {
                firstChord = chord;
            }

            // Tie previous chord's notes to this chord's notes (same order).
            if (prevNoteLocal) {
                const Chord* prevChord = prevNoteLocal->chord();
                for (size_t i = 0; i < std::min(prevChord->notes().size(),
                                                  chord->notes().size()); ++i) {
                    Note* n1 = prevChord->notes()[i];
                    Note* n2 = chord->notes()[i];
                    Tie* tie = Factory::createTie(sc->dummy());
                    tie->setStartNote(n1);
                    tie->setEndNote(n2);
                    tie->setTick(n1->tick());
                    tie->setTick2(n2->tick());
                    tie->setTrack(track);
                    n1->setTieFor(tie);
                    n2->setTieBack(tie);
                    sc->undoAddElement(tie);
                }
            }

            prevNoteLocal = chord->notes().empty() ? nullptr : chord->notes().front();
            chunkTick    += d.fraction();
        }

        prevNote0  = prevNoteLocal;
        remaining -= gapped;
        tick       = chunkTick;

        if (remaining > Fraction(0, 1)) {
            seg = sc->tick2segment(tick, true, SegmentType::ChordRest);
            if (!seg) {
                break;
            }
        }
    }

    return firstChord;
}

// Connect the last chord of @p chainA to the first chord of @p chainB via
// a slur.  A slur (rather than a tie) is used because ties make the playback
// engine treat both halves as one sustained sound, ignoring note_B's tuning.
// A slur keeps them as independent playback events with legato articulation.
void bridgeChains(mu::engraving::Score*  sc,
                  mu::engraving::Chord*  chainA,
                  mu::engraving::Chord*  chainB)
{
    using namespace mu::engraving;

    // Walk to the last chord in A.
    Chord* lastA = chainA;
    forEachChordInChain(chainA, [&](Chord* c) { lastA = c; });

    Slur* slur = Factory::createSlur(sc->dummy());
    slur->setScore(sc);
    slur->setTick(lastA->tick());
    slur->setTick2(chainB->tick());
    slur->setTrack(lastA->track());
    slur->setTrack2(chainB->track());
    slur->setStartElement(lastA);
    slur->setEndElement(chainB);
    sc->undoAddElement(slur);
}

/// Split a sustained chord at @p splitTick and apply tuning to the new portion.
///
/// Shortens the original chord to end at splitTick, creates a continuation
/// chain from splitTick to the original end, bridges them with a slur, applies
/// @p tuningFn to every note in the new chain, and transfers forward slurs.
///
/// @param tuningFn  Called for each Note* in the new chain to set its tuning.
/// @return true if a split was performed.
template<typename TuningFn>
bool splitAndTuneChord(mu::engraving::Score* sc,
                       mu::engraving::Chord* chordMut,
                       const mu::engraving::Fraction& splitTick,
                       TuningFn tuningFn)
{
    using namespace mu::engraving;

    const Fraction noteTick    = chordMut->tick();
    const Fraction noteEndTick = noteTick + chordMut->actualTicks();
    const track_idx_t track    = chordMut->track();

    if (splitTick <= noteTick || splitTick >= noteEndTick) {
        return false;
    }

    // Shorten the original chord to end at the split tick.
    sc->changeCRlen(chordMut, splitTick - noteTick);

    // Create continuation chain from splitTick to the original end.
    Chord* noteB = addChordChain(sc, splitTick, noteEndTick, track, chordMut);
    if (!noteB) {
        return false;
    }

    // Apply tuning to every note in the new chain.
    forEachChordInChain(noteB, [&](Chord* c) {
        for (Note* n : c->notes()) {
            tuningFn(n);
        }
    });

    // Slur the (now-shortened) original to the new chain.
    bridgeChains(sc, chordMut, noteB);

    // Transfer any existing forward slurs from the original chord to noteB
    // so that successive splits produce a chain (1→2→3→4) rather than a
    // fan (1→2, 1→3, 1→4).
    Chord* lastB = noteB;
    forEachChordInChain(noteB, [&](Chord* c) { lastB = c; });
    for (auto& [tick_, sp] : sc->spanner()) {
        if (!sp->isSlur()) {
            continue;
        }
        if (sp->startElement() == chordMut && sp->endElement() != noteB) {
            sp->setStartElement(lastB);
            sp->setTick(lastB->tick());
        }
    }

    return true;
}

} // anonymous namespace

// ─────────────────────────────────────────────────────────────────────────────

bool applyTuningAtNote(const mu::engraving::Note* selectedNote,
                       const TuningSystem& system)
{
    using namespace mu::engraving;

    if (!selectedNote || !selectedNote->visible()) {
        return false;
    }

    int keyFifths = 0;
    mu::composing::analysis::KeyMode keyMode = mu::composing::analysis::KeyMode::Ionian;
    const auto results = mu::composing::analysis::analyzeNoteHarmonicContext(
        selectedNote, keyFifths, keyMode);

    if (results.empty()) {
        return false;
    }

    const auto& chordResult = results.front();

    // Populate keyModeResult so rootOffset() can locate the mode tonic.
    mu::composing::analysis::KeyModeAnalysisResult keyModeResult;
    keyModeResult.keySignatureFifths = keyFifths;
    keyModeResult.mode = keyMode;
    {
        using mu::composing::analysis::keyModeTonicOffset;
        const int ionianPc = ((keyFifths * 7) % 12 + 12) % 12;
        keyModeResult.tonicPc = (ionianPc + keyModeTonicOffset(keyMode)) % 12;
    }

    static muse::GlobalInject<mu::composing::IComposingConfiguration> cfg;
    const bool tonicAnchored  = cfg.get() && cfg.get()->tonicAnchoredTuning();
    const bool minimizeRetune = cfg.get() && cfg.get()->minimizeTuningDeviation();
    const bool annotateTuning = cfg.get() && cfg.get()->annotateTuningOffsets();

    static constexpr double kEpsilonCents = 0.5;

    auto desiredOffset = [&](int ppitch) -> double {
        const int semitones = semitoneFromPitches(ppitch % 12, chordResult.rootPc);
        double offset = system.tuningOffset(keyModeResult, chordResult.quality,
                                            chordResult.rootPc, semitones);
        if (tonicAnchored) {
            offset += system.rootOffset(keyModeResult, chordResult.rootPc);
        }
        return offset;
    };

    auto staffEligible = [&](size_t si) -> bool {
        const Score* sc = selectedNote->score();
        const Staff* st = sc->staff(si);
        return st->show()
               && !st->part()->instrument(selectedNote->tick())->useDrumset()
               && !isChordTrackStaff(sc, si);
    };

    Score*         sc   = selectedNote->score();
    const Fraction tick = selectedNote->tick();
    Segment*       seg  = sc->tick2segment(tick, true, SegmentType::ChordRest);
    if (!seg) {
        return false;
    }

    // ── "Minimize retune": subtract mean offset so chord hovers near 0 ¢ ────────
    double meanShift = 0.0;
    if (minimizeRetune && seg) {
        double sum = 0.0;
        int    cnt = 0;
        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (!staffEligible(si)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const ChordRest* cr = seg->cr(static_cast<track_idx_t>(si) * VOICES + v);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                for (const Note* n : toChord(cr)->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    sum += desiredOffset(n->ppitch());
                    ++cnt;
                }
            }
        }
        if (cnt > 0) {
            meanShift = sum / cnt;
        }
    }
    auto finalOffset = [&](int ppitch) { return desiredOffset(ppitch) - meanShift; };

    bool anyApplied = false;

    // ── Phase 2: notes that attack at the anchor tick ─────────────────────────
    for (size_t si = 0; si < sc->nstaves(); ++si) {
        if (!staffEligible(si)) {
            continue;
        }
        for (int v = 0; v < VOICES; ++v) {
            ChordRest* cr = seg->cr(static_cast<track_idx_t>(si) * VOICES + v);
            if (!cr || !cr->isChord() || cr->isGrace()) {
                continue;
            }
            std::string tuningAnnotation;
            for (Note* n : toChord(cr)->notes()) {
                if (!n->play() || !n->visible()) {
                    continue;
                }
                const double desired = finalOffset(n->ppitch());
                if (annotateTuning) {
                    const int cents = static_cast<int>(std::round(desired));
                    if (!tuningAnnotation.empty()) tuningAnnotation += ' ';
                    tuningAnnotation += (cents >= 0 ? "+" : "") + std::to_string(cents);
                }
                if (std::abs(n->tuning() - desired) < kEpsilonCents) {
                    continue;
                }
                n->undoChangeProperty(Pid::TUNING, desired);
                anyApplied = true;
            }
            if (annotateTuning && !tuningAnnotation.empty()) {
                StaffText* at = Factory::createStaffText(seg);
                at->setTrack(static_cast<track_idx_t>(si) * VOICES + v);
                at->setParent(seg);
                at->setPlacement(PlacementV::BELOW);
                at->setPlainText(muse::String::fromStdString(tuningAnnotation));
                sc->undoAddElement(at);
                anyApplied = true;
            }
        }
    }

    // ── Phase 3: sustained notes (started before anchor tick) ─────────────────
    const Fraction backLimit = tick - Fraction(4, 1);

    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s && s->tick() >= backLimit;
         s = s->prev1(SegmentType::ChordRest)) {

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (!staffEligible(si)) {
                continue;
            }
            for (int v = 0; v < VOICES; ++v) {
                const track_idx_t origTrack = static_cast<track_idx_t>(si) * VOICES + v;
                const ChordRest*  cr        = s->cr(origTrack);
                if (!cr || !cr->isChord() || cr->isGrace()) {
                    continue;
                }
                const Chord*   ch          = toChord(cr);
                const Fraction noteTick    = s->tick();
                const Fraction noteEndTick = noteTick + ch->actualTicks();
                if (noteEndTick <= tick) {
                    continue;
                }

                bool anyNeedsTuning = false;
                for (const Note* n : ch->notes()) {
                    if (!n->play() || !n->visible()) {
                        continue;
                    }
                    if (std::abs(n->tuning() - finalOffset(n->ppitch())) >= kEpsilonCents) {
                        anyNeedsTuning = true;
                        break;
                    }
                }
                if (!anyNeedsTuning) {
                    continue;
                }

                Segment* noteSeg  = sc->tick2segment(noteTick, true, SegmentType::ChordRest);
                Chord*   chordMut = noteSeg
                                    ? toChord(noteSeg->cr(origTrack))
                                    : nullptr;
                if (!chordMut) {
                    continue;
                }

                if (splitAndTuneChord(sc, chordMut, tick,
                                      [&](Note* n) { n->setTuning(finalOffset(n->ppitch())); })) {
                    anyApplied = true;
                    if (annotateTuning && seg) {
                        const ChordRest* splitCr = seg->cr(origTrack);
                        if (splitCr && splitCr->isChord()) {
                            std::string tuningAnnotation;
                            for (const Note* n : toChord(splitCr)->notes()) {
                                if (!n->play() || !n->visible()) {
                                    continue;
                                }
                                const int cents = static_cast<int>(std::round(finalOffset(n->ppitch())));
                                if (!tuningAnnotation.empty()) tuningAnnotation += ' ';
                                tuningAnnotation += (cents >= 0 ? "+" : "") + std::to_string(cents);
                            }
                            if (!tuningAnnotation.empty()) {
                                StaffText* at = Factory::createStaffText(seg);
                                at->setTrack(origTrack);
                                at->setParent(seg);
                                at->setPlacement(PlacementV::BELOW);
                                at->setPlainText(muse::String::fromStdString(tuningAnnotation));
                                sc->undoAddElement(at);
                            }
                        }
                    }
                }
            }
        }
    }

    return anyApplied;
}

// ── applyRegionTuning ─────────────────────────────────────────────────────────

bool applyRegionTuning(mu::engraving::Score* score,
                       const mu::engraving::Fraction& startTick,
                       const mu::engraving::Fraction& endTick)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;

    if (!score || endTick <= startTick) {
        return false;
    }

    // Exclude chord track staves from both analysis and tuning.
    std::set<size_t> excludeStaves;
    for (size_t si = 0; si < score->nstaves(); ++si) {
        if (isChordTrackStaff(score, si)) {
            excludeStaves.insert(si);
        }
    }

    // ── Harmonic analysis ────────────────────────────────────────────────────
    const auto regions = analyzeHarmonicRhythm(score, startTick, endTick,
                                               excludeStaves);
    if (regions.empty()) {
        return false;
    }

    const auto& tuningSystem = preferredTuningSystem();

    static muse::GlobalInject<mu::composing::IComposingConfiguration> cfg;
    const bool tonicAnchored  = cfg.get() && cfg.get()->tonicAnchoredTuning();
    const bool minimizeRetune = cfg.get() && cfg.get()->minimizeTuningDeviation();
    const bool annotateTuning = cfg.get() && cfg.get()->annotateTuningOffsets();

    static constexpr double kEpsilonCents = 0.5;

    bool anyApplied = false;

    for (const auto& region : regions) {
        const Fraction rStart = Fraction::fromTicks(region.startTick);
        const Fraction rEnd   = Fraction::fromTicks(region.endTick);
        const auto& chord     = region.chordResult;

        auto desiredOffset = [&](int ppitch) -> double {
            const int semitones = semitoneFromPitches(ppitch % 12, chord.rootPc);
            double offset = tuningSystem.tuningOffset(region.keyModeResult, chord.quality,
                                                      chord.rootPc, semitones);
            if (tonicAnchored) {
                offset += tuningSystem.rootOffset(region.keyModeResult, chord.rootPc);
            }
            return offset;
        };

        // ── "Minimize retune": subtract mean offset so chord hovers near 0 ¢ ──
        double meanShift = 0.0;
        if (minimizeRetune) {
            double sum = 0.0;
            int    cnt = 0;
            for (Segment* mseg = score->tick2segment(rStart, true, SegmentType::ChordRest);
                 mseg && mseg->tick() < rEnd;
                 mseg = mseg->next1(SegmentType::ChordRest)) {
                for (size_t si = 0; si < score->nstaves(); ++si) {
                    if (excludeStaves.count(si)
                        || !staffIsEligible(score, si, mseg->tick())) {
                        continue;
                    }
                    for (int v = 0; v < VOICES; ++v) {
                        const ChordRest* cr = mseg->cr(
                            static_cast<track_idx_t>(si) * VOICES + v);
                        if (!cr || !cr->isChord() || cr->isGrace()) {
                            continue;
                        }
                        for (const Note* n : toChord(cr)->notes()) {
                            if (!n->play() || !n->visible()) {
                                continue;
                            }
                            sum += desiredOffset(n->ppitch());
                            ++cnt;
                        }
                    }
                }
            }
            if (cnt > 0) {
                meanShift = sum / cnt;
            }
        }
        auto finalOffset = [&](int ppitch) { return desiredOffset(ppitch) - meanShift; };

        // ── Phase 2: notes attacking within this region ──────────────────
        for (Segment* seg = score->tick2segment(rStart, true, SegmentType::ChordRest);
             seg && seg->tick() < rEnd;
             seg = seg->next1(SegmentType::ChordRest)) {

            for (size_t si = 0; si < score->nstaves(); ++si) {
                if (excludeStaves.count(si)
                    || !staffIsEligible(score, si, seg->tick())) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    ChordRest* cr = seg->cr(
                        static_cast<track_idx_t>(si) * VOICES + v);
                    if (!cr || !cr->isChord() || cr->isGrace()) {
                        continue;
                    }
                    std::string tuningAnnotation;
                    for (Note* n : toChord(cr)->notes()) {
                        if (!n->play() || !n->visible()) {
                            continue;
                        }
                        const double desired = finalOffset(n->ppitch());
                        if (annotateTuning) {
                            const int cents = static_cast<int>(std::round(desired));
                            if (!tuningAnnotation.empty()) tuningAnnotation += ' ';
                            tuningAnnotation += (cents >= 0 ? "+" : "") + std::to_string(cents);
                        }
                        if (std::abs(n->tuning() - desired) < kEpsilonCents) {
                            continue;
                        }
                        n->undoChangeProperty(Pid::TUNING, desired);
                        anyApplied = true;
                    }
                    if (annotateTuning && !tuningAnnotation.empty()) {
                        StaffText* at = Factory::createStaffText(seg);
                        at->setTrack(static_cast<track_idx_t>(si) * VOICES + v);
                        at->setParent(seg);
                        at->setPlacement(PlacementV::BELOW);
                        at->setPlainText(muse::String::fromStdString(tuningAnnotation));
                        score->undoAddElement(at);
                        anyApplied = true;
                    }
                }
            }
        }

        // ── Phase 3: sustained notes (started before this region) ────────
        // Walk backward from rStart to find chords that are still sounding.
        const Fraction backLimit = rStart - Fraction(4, 1);
        Segment* rStartSeg = score->tick2segment(rStart, true,
                                                  SegmentType::ChordRest);
        if (!rStartSeg) {
            continue;
        }

        for (const Segment* s = rStartSeg->prev1(SegmentType::ChordRest);
             s && s->tick() >= backLimit;
             s = s->prev1(SegmentType::ChordRest)) {

            for (size_t si = 0; si < score->nstaves(); ++si) {
                if (excludeStaves.count(si)
                    || !staffIsEligible(score, si, s->tick())) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    const track_idx_t origTrack
                        = static_cast<track_idx_t>(si) * VOICES + v;
                    const ChordRest* cr = s->cr(origTrack);
                    if (!cr || !cr->isChord() || cr->isGrace()) {
                        continue;
                    }
                    const Chord*   ch          = toChord(cr);
                    const Fraction noteTick    = s->tick();
                    const Fraction noteEndTick = noteTick + ch->actualTicks();
                    if (noteEndTick <= rStart) {
                        continue;   // ended before region
                    }

                    // Check if any note needs different tuning.
                    bool anyNeedsTuning = false;
                    for (const Note* n : ch->notes()) {
                        if (!n->play() || !n->visible()) {
                            continue;
                        }
                        if (std::abs(n->tuning() - finalOffset(n->ppitch()))
                            >= kEpsilonCents) {
                            anyNeedsTuning = true;
                            break;
                        }
                    }
                    if (!anyNeedsTuning) {
                        continue;
                    }

                    Segment* noteSeg = score->tick2segment(
                        noteTick, true, SegmentType::ChordRest);
                    Chord* chordMut = noteSeg
                        ? toChord(noteSeg->cr(origTrack))
                        : nullptr;
                    if (!chordMut) {
                        continue;
                    }

                    if (splitAndTuneChord(score, chordMut, rStart,
                            [&](Note* n) {
                                n->setTuning(finalOffset(n->ppitch()));
                            })) {
                        anyApplied = true;
                        if (annotateTuning) {
                            Segment* splitSeg = score->tick2segment(
                                rStart, true, SegmentType::ChordRest);
                            if (splitSeg) {
                                const ChordRest* splitCr = splitSeg->cr(origTrack);
                                if (splitCr && splitCr->isChord()) {
                                    std::string tuningAnnotation;
                                    for (const Note* n : toChord(splitCr)->notes()) {
                                        if (!n->play() || !n->visible()) {
                                            continue;
                                        }
                                        const int cents = static_cast<int>(std::round(finalOffset(n->ppitch())));
                                        if (!tuningAnnotation.empty()) tuningAnnotation += ' ';
                                        tuningAnnotation += (cents >= 0 ? "+" : "") + std::to_string(cents);
                                    }
                                    if (!tuningAnnotation.empty()) {
                                        StaffText* at = Factory::createStaffText(splitSeg);
                                        at->setTrack(origTrack);
                                        at->setParent(splitSeg);
                                        at->setPlacement(PlacementV::BELOW);
                                        at->setPlainText(muse::String::fromStdString(tuningAnnotation));
                                        score->undoAddElement(at);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return anyApplied;
}

} // namespace mu::composing::intonation
