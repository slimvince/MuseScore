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

// ── Intonation/tuning bridge ─────────────────────────────────────────────────
//
// Implements:
//   applyTuningAtNote()  (mu::composing::intonation)  — single-note tuning
//   applyRegionTuning()  (mu::composing::intonation)  — region tuning
//
// Both declared in composing/intonation/tuning_system.h.
//
// Kept separate from notationcomposingbridge.cpp (analysis) so that a
// clean-branch submission of the chord-symbol annotation feature does not need
// to carry the tuning machinery.

#include "notationanalysisinternal.h"

#include <cmath>
#include <set>

#include "engraving/dom/chord.h"
#include "engraving/dom/expression.h"
#include "engraving/dom/factory.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/note.h"
#include "engraving/dom/property.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/slur.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/stafftext.h"
#include "engraving/dom/tie.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/intonation/just_intonation.h"
#include "composing/intonation/tuning_system.h"
#include "composing/intonation/tuning_utils.h"
#include "composing/icomposinganalysisconfiguration.h"
#include "modularity/ioc.h"

#include "notationcomposingbridge.h"   // analyzeNoteHarmonicContext, analyzeHarmonicRhythm (mu::notation)
#include "notationtuningbridge.h"

using namespace mu::engraving;
using mu::notation::internal::isChordTrackStaff;
using mu::notation::internal::staffIsEligible;
using mu::notation::internal::chordTrackExcludeStaves;

namespace {

const mu::composing::IComposingAnalysisConfiguration* analysisConfig()
{
    static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> s_cfg;
    return s_cfg.get().get();
}

// Returns the TuningSystem selected in user preferences, falling back to
// JustIntonation if the preference is unset or refers to an unknown key.
static const mu::composing::intonation::TuningSystem& preferredTuningSystem()
{
    using namespace mu::composing::intonation;
    static const JustIntonation jiFallback;

    const auto* prefs = analysisConfig();
    if (prefs) {
        const TuningSystem* sys = TuningRegistry::byKey(prefs->tuningSystemKey());
        if (sys) {
            return *sys;
        }
    }
    return jiFallback;
}

bool noteHasNonPartialTie(const mu::engraving::Note* note)
{
    return note && (note->tieBackNonPartial() || note->tieForNonPartial());
}

const mu::engraving::Note* firstNonPartialTiedNote(const mu::engraving::Note* note)
{
    const mu::engraving::Note* current = note;
    while (current && current->tieBackNonPartial() && current->tieBackNonPartial()->startNote()) {
        current = current->tieBackNonPartial()->startNote();
    }
    return current;
}

const mu::engraving::Note* nextNonPartialTiedNote(const mu::engraving::Note* note)
{
    if (!note || !note->tieForNonPartial() || !note->tieForNonPartial()->endNote()) {
        return nullptr;
    }
    return note->tieForNonPartial()->endNote();
}

const mu::engraving::Note* firstNonPartialTiedNoteInRegion(const mu::engraving::Note* note,
                                                           const mu::engraving::Fraction& regionStart)
{
    const mu::engraving::Note* current = note;
    while (current && current->tieBackNonPartial() && current->tieBackNonPartial()->startNote()) {
        const mu::engraving::Note* previous = current->tieBackNonPartial()->startNote();
        if (!previous->chord() || previous->chord()->tick() < regionStart) {
            break;
        }
        current = previous;
    }
    return current;
}

std::vector<mu::engraving::Note*> collectNonPartialTieChain(mu::engraving::Note* note)
{
    std::vector<mu::engraving::Note*> chain;
    for (mu::engraving::Note* current = const_cast<mu::engraving::Note*>(firstNonPartialTiedNote(note));
         current;
         current = const_cast<mu::engraving::Note*>(nextNonPartialTiedNote(current))) {
        chain.push_back(current);
    }
    return chain;
}

std::vector<mu::engraving::Note*> collectNonPartialTieChainInRegion(mu::engraving::Note* note,
                                                                    const mu::engraving::Fraction& regionStart,
                                                                    const mu::engraving::Fraction& regionEnd)
{
    std::vector<mu::engraving::Note*> chain;
    for (mu::engraving::Note* current = const_cast<mu::engraving::Note*>(firstNonPartialTiedNoteInRegion(note, regionStart));
         current;
         current = const_cast<mu::engraving::Note*>(nextNonPartialTiedNote(current))) {
        if (!current->chord() || current->chord()->tick() >= regionEnd) {
            break;
        }
        chain.push_back(current);
    }
    return chain;
}

const mu::engraving::Note* authorityNoteForTieChain(const mu::engraving::Note* note)
{
    const mu::engraving::Note* first = firstNonPartialTiedNote(note);
    for (const mu::engraving::Note* current = first; current; current = nextNonPartialTiedNote(current)) {
        if (mu::notation::hasTuningAnchorExpression(current)) {
            return current;
        }
    }
    return first;
}

bool computeTieChainOffset(const mu::engraving::Note* authorityNote,
                           const mu::composing::intonation::TuningSystem& tuningSystem,
                           bool tonicAnchored,
                           mu::composing::intonation::TuningMode tuningMode,
                           double& outOffset)
{
    using namespace mu::composing::analysis;
    using namespace mu::composing::intonation;

    if (!authorityNote || !authorityNote->visible() || !authorityNote->play()) {
        return false;
    }

    if (mu::notation::hasTuningAnchorExpression(authorityNote)) {
        outOffset = (tuningMode == TuningMode::FreeDrift) ? authorityNote->tuning() : 0.0;
        return true;
    }

    int keyFifths = 0;
    KeySigMode keyMode = KeySigMode::Ionian;
    const auto results = mu::notation::analyzeNoteHarmonicContext(authorityNote, keyFifths, keyMode);
    if (results.empty()) {
        return false;
    }

    const auto& chordResult = results.front();

    KeyModeAnalysisResult keyModeResult;
    keyModeResult.keySignatureFifths = keyFifths;
    keyModeResult.mode = keyMode;
    {
        const int ionianPc = mu::composing::analysis::ionianTonicPcFromFifths(keyFifths);
        keyModeResult.tonicPc = (ionianPc + keyModeTonicOffset(keyMode)) % 12;
    }

    const int semitones = semitoneFromPitches(authorityNote->ppitch() % 12,
                                              chordResult.identity.rootPc);
    outOffset = tuningSystem.tuningOffset(keyModeResult, chordResult.identity.quality,
                                          chordResult.identity.rootPc, semitones);
    if (tonicAnchored) {
        outOffset += tuningSystem.rootOffset(keyModeResult, chordResult.identity.rootPc);
    }

    return true;
}

std::string formatTuningAnnotation(double offset, bool anchorAuthority)
{
    const int cents = static_cast<int>(std::round(offset));
    std::string annotation = (cents >= 0 ? "+" : "") + std::to_string(cents);
    if (anchorAuthority) {
        annotation += "*";
    }
    return annotation;
}

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

bool retuneAtExistingTieBoundary(mu::engraving::Score* sc,
                                 mu::engraving::Note* regionStartNote)
{
    using namespace mu::engraving;

    if (!sc || !regionStartNote || !regionStartNote->tieBackNonPartial()) {
        return false;
    }

    Note* previousNote = regionStartNote->tieBackNonPartial()->startNote();
    Chord* currentChord = regionStartNote->chord();
    Chord* previousChord = previousNote ? previousNote->chord() : nullptr;
    if (!currentChord || !previousChord) {
        return false;
    }

    bool removedAnyTie = false;
    for (Note* note : currentChord->notes()) {
        Tie* tieBack = note->tieBackNonPartial();
        if (!tieBack || !tieBack->startNote() || tieBack->startNote()->chord() != previousChord) {
            continue;
        }
        sc->undoRemoveElement(tieBack);
        removedAnyTie = true;
    }

    if (!removedAnyTie) {
        return false;
    }

    bridgeChains(sc, previousChord, currentChord);
    return true;
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

// ── hasTuningAnchorExpression / computeSusceptibility ────────────────────────
namespace mu::notation {

bool hasTuningAnchorExpression(const mu::engraving::Note* note)
{
    using namespace mu::composing::intonation;

    if (!note) {
        return false;
    }
    const Chord* ch = note->chord();
    if (!ch) {
        return false;
    }
    const Segment* seg = ch->segment();
    if (!seg) {
        return false;
    }

    for (const EngravingItem* ann : seg->annotations()) {
        if (!ann->isExpression()) {
            continue;
        }
        const auto* expr = toExpression(ann);
        // Check that the expression belongs to the same track (voice) as the note.
        if (expr->track() != ch->track()) {
            continue;
        }
        // Delegate case-insensitive / trimmed comparison to the pure function.
        if (isTuningAnchorText(expr->plainText().toStdString())) {
            return true;
        }
    }
    return false;
}

mu::composing::intonation::RetuningSusceptibility computeSusceptibility(
    const mu::engraving::Note* note)
{
    using namespace mu::composing::intonation;
    if (hasTuningAnchorExpression(note)) {
        return RetuningSusceptibility::AbsolutelyProtected;
    }
    // Duration-based and context-based classification is a future addition
    // (see backlog_tone_weight.md).  All non-anchor notes are Free for now.
    return RetuningSusceptibility::Free;
}

} // namespace mu::notation

// ── applyTuningAtNote ─────────────────────────────────────────────────────────
// Implements the free function declared in notationtuningbridge.h.
//
// Phase 2: applies tuning to notes that attack at the selected note's tick.
// Phase 3: handles sustained notes via split-and-tie score mutation.
namespace mu::notation {

bool applyTuningAtNote(const mu::engraving::Note* selectedNote,
                       const mu::composing::intonation::TuningSystem& system)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;
    using namespace mu::composing::intonation;
    using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode

    if (!selectedNote || !selectedNote->visible()) {
        return false;
    }

    int keyFifths = 0;
    KeySigMode keyMode = KeySigMode::Ionian;
    const auto results = analyzeNoteHarmonicContext(selectedNote, keyFifths, keyMode);

    if (results.empty()) {
        return false;
    }

    const auto& chordResult = results.front();

    // Populate keyModeResult so rootOffset() can locate the mode tonic.
    KeyModeAnalysisResult keyModeResult;
    keyModeResult.keySignatureFifths = keyFifths;
    keyModeResult.mode = keyMode;
    {
        const int ionianPc = mu::composing::analysis::ionianTonicPcFromFifths(keyFifths);
        keyModeResult.tonicPc = (ionianPc + keyModeTonicOffset(keyMode)) % 12;
    }

    const auto* cfg = analysisConfig();
    const bool tonicAnchored  = cfg && cfg->tonicAnchoredTuning();
    const bool minimizeRetune = cfg && cfg->minimizeTuningDeviation();
    const bool annotateTuning = cfg && cfg->annotateTuningOffsets();

    static constexpr double kEpsilonCents = 0.5;

    auto desiredOffset = [&](int ppitch) -> double {
        const int semitones = semitoneFromPitches(ppitch % 12, chordResult.identity.rootPc);
        double offset = system.tuningOffset(keyModeResult, chordResult.identity.quality,
                                            chordResult.identity.rootPc, semitones);
        if (tonicAnchored) {
            offset += system.rootOffset(keyModeResult, chordResult.identity.rootPc);
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
    using namespace mu::composing::intonation;
    using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode

    if (!score || endTick <= startTick) {
        return false;
    }

    // Exclude chord staff staves from both analysis and tuning.
    std::set<size_t> excludeStaves = chordTrackExcludeStaves(score);

    // ── Harmonic analysis ────────────────────────────────────────────────────
    const auto regions = analyzeHarmonicRhythm(score, startTick, endTick,
                                               excludeStaves);
    if (regions.empty()) {
        return false;
    }

    const auto& tuningSystem = preferredTuningSystem();

    const auto* cfg = analysisConfig();
    const bool tonicAnchored       = cfg && cfg->tonicAnchoredTuning();
    const bool minimizeRetune      = cfg && cfg->minimizeTuningDeviation();
    const bool annotateTuning      = cfg && cfg->annotateTuningOffsets();
    const bool annotateDriftBounds = cfg && cfg->annotateDriftAtBoundaries();
    const bool allowSplitSlurOfSustainedEvents = !cfg
        || cfg->allowSplitSlurOfSustainedEvents();
    const auto tuningMode          = cfg
        ? cfg->tuningMode()
        : mu::composing::intonation::TuningMode::TonicAnchored;

    static constexpr double kEpsilonCents = 0.5;

    bool anyApplied = false;
    std::set<const Note*> processedTieRoots;

    for (const auto& region : regions) {
        const Fraction rStart = Fraction::fromTicks(region.startTick);
        const Fraction rEnd   = Fraction::fromTicks(region.endTick);
        const auto& chord     = region.chordResult;

        auto desiredOffset = [&](int ppitch) -> double {
            const int semitones = semitoneFromPitches(ppitch % 12, chord.identity.rootPc);
            double offset = tuningSystem.tuningOffset(region.keyModeResult, chord.identity.quality,
                                                      chord.identity.rootPc, semitones);
            if (tonicAnchored) {
                offset += tuningSystem.rootOffset(region.keyModeResult, chord.identity.rootPc);
            }
            return offset;
        };

        // ── Drift reference hierarchy ─────────────────────────────────────────
        //
        // TonicAnchored mode — P0 (anchor) → P2/P3 (zero drift):
        //   If an alt.rif. note attacks at rStart, shift all other notes so the
        //   anchor lands at exactly 0 ¢.  driftAdjustment = −desiredOffset(anchor).
        //   Octave-equivalent notes then produce a pure octave from the anchor.
        //
        // FreeDrift mode — P1 (held note) → P2/P3 (zero drift):
        //   Drift accumulates from the previous region via a held note (P1).
        //   An anchor note in FreeDrift is pitched AT the current drift level,
        //   not reset to 0 ¢ — it confirms "here is where we have drifted to"
        //   without pulling other notes back to 12-TET.
        //   The P0 driftAdjustment override therefore does NOT apply in FreeDrift.
        //
        // In FreeDrift mode sustained notes are NEVER split (Phase 3 is skipped).
        double driftAdjustment = 0.0;
        bool   foundAnchorRef  = false;

        // P0: TonicAnchored only — anchor as intonation reset reference.
        if (tuningMode == mu::composing::intonation::TuningMode::TonicAnchored) {
            Segment* rStartSeg = score->tick2segment(rStart, true,
                                                      SegmentType::ChordRest);
            if (rStartSeg) {
                for (size_t si = 0; si < score->nstaves() && !foundAnchorRef; ++si) {
                    if (excludeStaves.count(si)
                        || !staffIsEligible(score, si, rStart)) {
                        continue;
                    }
                    for (int v = 0; v < VOICES && !foundAnchorRef; ++v) {
                        const ChordRest* cr = rStartSeg->cr(
                            static_cast<track_idx_t>(si) * VOICES + v);
                        if (!cr || !cr->isChord() || cr->isGrace()) {
                            continue;
                        }
                        for (const Note* n : toChord(cr)->notes()) {
                            if (!n->play() || !n->visible()) {
                                continue;
                            }
                            if (hasTuningAnchorExpression(n)) {
                                driftAdjustment = -desiredOffset(n->ppitch());
                                foundAnchorRef  = true;
                                break;
                            }
                        }
                    }
                }
            }
        }

        // ── P1 (FreeDrift only): held-note as drift reference ────────────────
        if (tuningMode == mu::composing::intonation::TuningMode::FreeDrift) {
            const Fraction backLimit = rStart - Fraction(4, 1);
            Segment* rStartSeg = score->tick2segment(rStart, true,
                                                      SegmentType::ChordRest);
            bool foundHeld = false;
            if (rStartSeg) {
                for (const Segment* s = rStartSeg->prev1(SegmentType::ChordRest);
                     s && s->tick() >= backLimit && !foundHeld;
                     s = s->prev1(SegmentType::ChordRest)) {
                    for (size_t si = 0; si < score->nstaves() && !foundHeld; ++si) {
                        if (excludeStaves.count(si)
                            || !staffIsEligible(score, si, s->tick())) {
                            continue;
                        }
                        for (int v = 0; v < VOICES && !foundHeld; ++v) {
                            const ChordRest* cr = s->cr(
                                static_cast<track_idx_t>(si) * VOICES + v);
                            if (!cr || !cr->isChord() || cr->isGrace()) {
                                continue;
                            }
                            const Chord* ch = toChord(cr);
                            if (s->tick() + ch->actualTicks() <= rStart) {
                                continue;  // ended before this region
                            }
                            for (const Note* n : ch->notes()) {
                                if (!n->play() || !n->visible()) {
                                    continue;
                                }
                                if (hasTuningAnchorExpression(n)) {
                                    continue;  // anchor note: not a valid drift ref
                                }
                                driftAdjustment = n->tuning() - desiredOffset(n->ppitch());
                                foundHeld = true;
                                break;
                            }
                        }
                    }
                }
            }
            // P2/P3: no held note → driftAdjustment remains 0.0.
        }

        // ── Drift boundary annotation (FreeDrift, separate toggle) ────────────
        //
        // When annotateDriftAtBoundaries is enabled and we are in FreeDrift mode,
        // insert a StaffText at the region start showing the accumulated drift,
        // e.g. "d=+3" or "d=-2", on the first eligible non-chord-staff staff.
        // Only emitted when |driftAdjustment| >= kEpsilonCents (meaningful drift).
        if (annotateDriftBounds
            && tuningMode == mu::composing::intonation::TuningMode::FreeDrift
            && std::abs(driftAdjustment) >= kEpsilonCents) {

            Segment* rStartSeg = score->tick2segment(rStart, true,
                                                      SegmentType::ChordRest);
            if (rStartSeg) {
                for (size_t si = 0; si < score->nstaves(); ++si) {
                    if (excludeStaves.count(si)
                        || !staffIsEligible(score, si, rStart)) {
                        continue;
                    }
                    const int cents = static_cast<int>(std::round(driftAdjustment));
                    std::string label = "d=";
                    label += (cents >= 0) ? "+" : "";
                    label += std::to_string(cents);
                    StaffText* dt = Factory::createStaffText(rStartSeg);
                    dt->setTrack(static_cast<track_idx_t>(si) * VOICES);
                    dt->setParent(rStartSeg);
                    dt->setPlacement(PlacementV::ABOVE);
                    dt->setPlainText(muse::String::fromStdString(label));
                    score->undoAddElement(dt);
                    anyApplied = true;
                    break;  // one marker per region boundary is enough
                }
            }
        }

        // ── "Minimize retune": subtract mean offset so chord hovers near 0 ¢ ──
        // Anchor notes are excluded — they always contribute 0 ¢, not desiredOffset.
        // Non-partial tie chains count once, using the chain authority note.
        double meanShift = 0.0;
        if (minimizeRetune) {
            double sum = 0.0;
            int    cnt = 0;
            std::set<const Note*> meanShiftTieRoots;
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
                            if (noteHasNonPartialTie(n)) {
                                const Note* tieRoot = firstNonPartialTiedNote(n);
                                if (meanShiftTieRoots.count(tieRoot)) {
                                    continue;
                                }
                                meanShiftTieRoots.insert(tieRoot);

                                const Note* authorityNote = authorityNoteForTieChain(n);
                                if (hasTuningAnchorExpression(authorityNote)) {
                                    continue;
                                }

                                if (tuningMode == mu::composing::intonation::TuningMode::FreeDrift
                                    && tieRoot->chord()
                                    && tieRoot->chord()->tick() < rStart) {
                                    sum += authorityNote->tuning();
                                    ++cnt;
                                    continue;
                                }

                                const double tieOffset = desiredOffset(authorityNote->ppitch())
                                    + driftAdjustment;
                                sum += tieOffset;
                                ++cnt;
                                continue;
                            }
                            if (hasTuningAnchorExpression(n)) {
                                continue;  // anchor always at 0 ¢; exclude from mean
                            }
                            sum += desiredOffset(n->ppitch()) + driftAdjustment;
                            ++cnt;
                        }
                    }
                }
            }
            if (cnt > 0) {
                meanShift = sum / cnt;
            }
        }

        auto finalOffset = [&](int ppitch) {
            return desiredOffset(ppitch) + driftAdjustment - meanShift;
        };

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
                        if (noteHasNonPartialTie(n)) {
                            const Note* fullTieRoot = firstNonPartialTiedNote(n);
                            const Note* fullAuthorityNote = authorityNoteForTieChain(n);
                            const bool tieChainHasAnchor = hasTuningAnchorExpression(fullAuthorityNote);
                            const Note* regionTieRoot = firstNonPartialTiedNoteInRegion(n, rStart);
                            const bool boundaryCrossesRegion = regionTieRoot->tieBackNonPartial()
                                && regionTieRoot->tieBackNonPartial()->startNote()
                                && regionTieRoot->tieBackNonPartial()->startNote()->chord()
                                && regionTieRoot->tieBackNonPartial()->startNote()->chord()->tick() < rStart;
                            const bool allowTieBoundarySegmentation
                                = boundaryCrossesRegion && allowSplitSlurOfSustainedEvents && !tieChainHasAnchor;
                            const Note* tieRoot = allowTieBoundarySegmentation ? regionTieRoot : fullTieRoot;
                            if (processedTieRoots.count(tieRoot)) {
                                continue;
                            }
                            processedTieRoots.insert(tieRoot);

                            const Note* authorityNote = allowTieBoundarySegmentation
                                ? tieRoot
                                : fullAuthorityNote;

                            double tieOffset = 0.0;
                            if (tuningMode == mu::composing::intonation::TuningMode::FreeDrift) {
                                // In FreeDrift, carried tie chains stay whole unless the
                                // user explicitly allows a boundary rewrite and the
                                // continuation really needs a different tuning.
                                if (boundaryCrossesRegion && !allowTieBoundarySegmentation) {
                                    continue;
                                }
                                tieOffset = finalOffset(authorityNote->ppitch());
                            } else if (!computeTieChainOffset(authorityNote, tuningSystem, tonicAnchored,
                                                              tuningMode, tieOffset)) {
                                continue;
                            }

                            if (allowTieBoundarySegmentation
                                && std::abs(regionTieRoot->tuning() - tieOffset) < kEpsilonCents) {
                                continue;
                            }

                            if (allowTieBoundarySegmentation) {
                                if (retuneAtExistingTieBoundary(score, const_cast<Note*>(regionTieRoot))) {
                                    anyApplied = true;
                                }
                            }

                            std::vector<Note*> tiedNotes = allowTieBoundarySegmentation
                                ? collectNonPartialTieChainInRegion(n, rStart, rEnd)
                                : collectNonPartialTieChain(n);
                            for (Note* tiedNote : tiedNotes) {
                                if (!tiedNote->play() || !tiedNote->visible()) {
                                    continue;
                                }
                                if (std::abs(tiedNote->tuning() - tieOffset) < kEpsilonCents) {
                                    continue;
                                }
                                tiedNote->undoChangeProperty(Pid::TUNING, tieOffset);
                                anyApplied = true;
                            }

                            if (annotateTuning && tieRoot->chord() && tieRoot->chord()->segment()) {
                                StaffText* at = Factory::createStaffText(tieRoot->chord()->segment());
                                at->setTrack(tieRoot->chord()->track());
                                at->setParent(tieRoot->chord()->segment());
                                at->setPlacement(PlacementV::BELOW);
                                at->setPlainText(muse::String::fromStdString(
                                    formatTuningAnnotation(tieOffset,
                                                           hasTuningAnchorExpression(authorityNote))));
                                score->undoAddElement(at);
                                anyApplied = true;
                            }
                            continue;
                        }
                        if (hasTuningAnchorExpression(n)) {
                            // Anchor note handling differs by mode:
                            //
                            // TonicAnchored: forced to 0 ¢ (12-TET fixed reference).
                            //   Other notes are shifted via driftAdjustment so that
                            //   JI intervals are computed relative to this 0 ¢ anchor.
                            //
                            // FreeDrift: pitched at finalOffset (current drift level).
                            //   The anchor "confirms" where we have drifted to without
                            //   resetting other notes back to 12-TET.
                            if (tuningMode == mu::composing::intonation::TuningMode::FreeDrift) {
                                const double desired = finalOffset(n->ppitch());
                                if (annotateTuning) {
                                    const int cents = static_cast<int>(std::round(desired));
                                    if (!tuningAnnotation.empty()) tuningAnnotation += ' ';
                                    tuningAnnotation += (cents >= 0 ? "+" : "")
                                                        + std::to_string(cents) + "*";
                                }
                                if (std::abs(n->tuning() - desired) >= kEpsilonCents) {
                                    n->undoChangeProperty(Pid::TUNING, desired);
                                    anyApplied = true;
                                }
                            } else {
                                if (std::abs(n->tuning()) >= kEpsilonCents) {
                                    n->undoChangeProperty(Pid::TUNING, 0.0);
                                    anyApplied = true;
                                }
                                if (annotateTuning) {
                                    if (!tuningAnnotation.empty()) tuningAnnotation += ' ';
                                    tuningAnnotation += "+0*";
                                }
                            }
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
        //
        // Score mutation for sustained untied notes happens only when the user
        // allows sustained-event rewriting. In both modes, the continuation is
        // rewritten only if its target tuning differs from the carried tuning.
        if (!allowSplitSlurOfSustainedEvents) {
            continue;
        }

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
                    // Anchor notes are protected: zero offset, never split.
                    // Chords containing a non-partial tie are left to Phase 2,
                    // which either keeps the chain whole or segments it at an
                    // existing tie boundary depending on user preference.
                    bool anyNeedsTuning = false;
                    bool hasAnchor = false;
                    bool hasNonPartialTie = false;
                    for (const Note* n : ch->notes()) {
                        if (!n->play() || !n->visible()) {
                            continue;
                        }
                        if (noteHasNonPartialTie(n)) {
                            hasNonPartialTie = true;
                            continue;
                        }
                        if (hasTuningAnchorExpression(n)) {
                            hasAnchor = true;
                            continue;  // anchor note never retuned or split
                        }
                        if (std::abs(n->tuning() - finalOffset(n->ppitch()))
                            >= kEpsilonCents) {
                            anyNeedsTuning = true;
                        }
                    }
                    // If any note in the chord is an anchor, do not split the
                    // chord — splitting would duplicate the anchor note and
                    // corrupt its protection semantics.
                    if (hasAnchor || hasNonPartialTie || !anyNeedsTuning) {
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

} // namespace mu::notation
