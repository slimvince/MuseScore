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

// ── Implode-to-chord-staff bridge ────────────────────────────────────────────
//
// Implements populateChordTrack() (declared in composing/analysis/region/harmonicrhythm.h).
//
// This file is intentionally separate from notationcomposingbridge.cpp so that
// a clean-branch submission of the chord-symbol annotation feature does not need
// to carry the chord-staff implode machinery.

#include <set>

#include "engraving/dom/chord.h"
#include "engraving/dom/durationtype.h"
#include "engraving/dom/factory.h"
#include "engraving/dom/harmony.h"
#include "engraving/dom/key.h"
#include "engraving/dom/keysig.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/rest.h"
#include "engraving/dom/pitchspelling.h"
#include "engraving/dom/property.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/sig.h"
#include "engraving/dom/staff.h"
#include "engraving/dom/stafftext.h"
#include "engraving/dom/tie.h"
#include "engraving/dom/tuplet.h"
#include "engraving/editing/editkeysig.h"

#include "composing/analysis/chord/analysisutils.h"
#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/region/harmonicrhythm.h"
#include "composing/analysis/key/keymodeanalyzer.h"
#include "composing/icomposingchordstaffconfiguration.h"
#include "modularity/ioc.h"

#include "notationcomposingbridge.h"   // analyzeHarmonicRhythm (mu::notation)
#include "notationimplodebridge.h"

using namespace mu::engraving;

namespace {

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

    Measure* startMeasure = sc->tick2measure(startTick);
    if (!startMeasure) {
        return nullptr;
    }

    Segment* seg = startMeasure->undoGetSegment(SegmentType::ChordRest, startTick);
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
                seg = m->undoGetSegment(SegmentType::ChordRest, startTick);
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
            Measure* nextMeasure = sc->tick2measure(tick);
            seg = nextMeasure ? nextMeasure->undoGetSegment(SegmentType::ChordRest, tick) : nullptr;
            if (!seg) {
                break;
            }
        }
    }

    return firstChord;
}

} // anonymous namespace

// ── populateChordTrack ───────────────────────────────────────────────────────
// Implements the free function declared in notationimplodebridge.h.

namespace mu::notation {

bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones)
{
    using namespace mu::engraving;
    using namespace mu::composing::analysis;
    using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode

    if (!score || endTick <= startTick) {
        return false;
    }

    static muse::GlobalInject<mu::composing::IComposingChordStaffConfiguration> composingConfig;
    const mu::composing::IComposingChordStaffConfiguration* prefs = composingConfig.get().get();

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
                                         excludeStaves,
                                         HarmonicRegionGranularity::PreserveAllChanges);
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
        KeySigMode stableMode  = regions.front().keyModeResult.mode;

        for (size_t i = 1; i < regions.size(); ++i) {
            const int rk = regions[i].keyModeResult.keySignatureFifths;
            const KeySigMode rm = regions[i].keyModeResult.mode;
            if (rk != stableKeyFifths || rm != stableMode) {
                // Check if the next region also shares this new key/mode
                // (persistence check), or if this is the last region.
                bool persistent = (i + 1 >= regions.size());
                if (!persistent) {
                    const int nk = regions[i + 1].keyModeResult.keySignatureFifths;
                    const KeySigMode nm = regions[i + 1].keyModeResult.mode;
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
                if ((tonicPc + scale[i]) % 12 == region.chordResult.identity.rootPc) {
                    degree = static_cast<int>(i);
                    break;
                }
            }
            region.chordResult.function.degree = degree;

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
            region.chordResult.function.diatonicToKey = diatonic;
        }
    }

    // ── Populate ─────────────────────────────────────────────────────────────
    bool anyWritten = false;

    // Track key/mode across regions to insert annotations only at boundaries.
    int prevKeyFifths = std::numeric_limits<int>::min();
    KeySigMode prevMode  = static_cast<KeySigMode>(-1);
    size_t prevRegionIdx = 0;

    for (size_t regionIdx = 0; regionIdx < regions.size(); ++regionIdx) {
        const auto& region = regions[regionIdx];
        const Fraction rStart = Fraction::fromTicks(region.startTick);
        const Fraction rEnd   = Fraction::fromTicks(region.endTick);

        const auto& chord = region.chordResult;
        const int localKeyFifths = region.keyModeResult.keySignatureFifths;
        const KeySigMode localMode  = region.keyModeResult.mode;

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
                    auto tonicPcFromKey = [](int fifths, KeySigMode mode) -> int {
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
                        if (prev.function.degree < 0) {
                            continue;  // non-diatonic in old key
                        }
                        if (!newScalePcs[prev.identity.rootPc]) {
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
                            ((prev.identity.rootPc - newTonicPc) % 12 + 12) % 12;
                        pivotInNew.function.degree = -1;
                        for (int d = 0; d < 7; ++d) {
                            if (SCALES[modeIdx][d] == semisFromNewTonic) {
                                pivotInNew.function.degree = d;
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
        Measure* regionMeasure = score->tick2measure(rStart);
        Segment* seg = regionMeasure ? regionMeasure->undoGetSegment(SegmentType::ChordRest, rStart) : nullptr;
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
            h->setPlainText(muse::String::fromStdString(symText));
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
                h->setPlainText(muse::String::fromStdString(fnText));
                score->undoAddElement(h);
            }
        }

        // Non-diatonic chord marker (borrowed chord / secondary dominant).
        // Only annotate when we can identify the source key; purely chromatic
        // chords that fit no diatonic scale are left without a marker.
        const bool highlightNonDiatonic = !prefs || prefs->chordStaffHighlightNonDiatonic();
        if (highlightNonDiatonic && !chord.function.diatonicToKey) {
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
            KeySigMode bestMode = localMode;
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
        if (a.identity.rootPc == b.identity.rootPc) {
            continue;  // same root (e.g. F#m → F#7) — not a cadence
        }

        const char* label = nullptr;

        // PAC: V → I (major dominant) or viio → I (leading-tone diminished).
        if (b.function.degree == 0
            && ((a.function.degree == 4 && a.identity.quality != ChordQuality::Minor)
                || (a.function.degree == 6 && a.identity.quality == ChordQuality::Diminished))) {
            label = "PAC";        // Authentic: V → I  or  viio → I
        } else if (a.function.degree == 3 && b.function.degree == 0) {
            label = "PC";         // Plagal: IV → I
        } else if (a.function.degree == 4 && b.function.degree == 5
                   && a.identity.quality != ChordQuality::Minor
                   && b.identity.quality == ChordQuality::Minor) {
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
    if (writeCadenceMarkers && !regions.empty() && regions.back().chordResult.function.degree == 4) {
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

} // namespace mu::notation
