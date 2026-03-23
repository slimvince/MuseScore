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
#include "notationaccessibility.h"

#include "translation.h"

#include "igetscore.h"
#include "notation.h"

#include "engraving/accessibility/accessibleroot.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/key.h"
#include "engraving/dom/masterscore.h"
#include "engraving/dom/measure.h"
#include "engraving/dom/note.h"
#include "engraving/dom/part.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/staff.h"

#include "composing/analysis/chordanalyzer.h"
#include "composing/analysis/keymodeanalyzer.h"

#include <set>

using namespace mu::notation;

namespace {

const char* keyName(int fifths, bool isMajor)
{
    static constexpr const char* MAJOR_NAMES[15] = {
        "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F",
        "C", "G", "D", "A", "E", "B", "F#", "C#"
    };
    static constexpr const char* MINOR_NAMES[15] = {
        "Ab", "Eb", "Bb", "F", "C", "G", "D",
        "A", "E", "B", "F#", "C#", "G#", "D#", "A#"
    };
    const int idx = std::clamp(fifths + 7, 0, 14);
    return isMajor ? MAJOR_NAMES[idx] : MINOR_NAMES[idx];
}

// Computes the harmonic annotation string appended to the status bar when a
// note is selected.  Returns "[Key] Sym [Roman] (score) | ..." or "" if no
// analysis is possible.  Separated from singleElementAccessibilityInfo() to
// keep that function's control flow readable.
std::string harmonicAnnotation(const Note* note)
{
    const Score*    sc   = note->score();
    const Fraction  tick = note->tick();

    const Segment* seg = sc->tick2segment(tick, true, SegmentType::ChordRest);
    if (!seg) {
        return "";
    }

    struct SoundingNote { int ppitch; int tpc; };

    // Staff eligibility: visible and pitched (not a drumset instrument).
    auto staffIsEligible = [&](size_t si) -> bool {
        const Staff* st = sc->staff(si);
        if (!st->show()) {
            return false;
        }
        if (st->part()->instrument(tick)->useDrumset()) {
            return false;
        }
        return true;
    };

    // Collect all notes sounding at anchorSeg->tick().
    // "Sounding": attacked at anchorSeg, or started earlier and still sustained.
    // Excludes grace notes, drum staves, hidden staves, silenced notes.
    auto collectSoundingAt = [&](const Segment* anchorSeg,
                                 std::vector<SoundingNote>& out) {
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
                if (!n->play()) {
                    continue;
                }
                out.push_back({ n->ppitch(), n->tpc() });
            }
        };

        for (size_t si = 0; si < sc->nstaves(); ++si) {
            if (!staffIsEligible(si)) {
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
                if (!staffIsEligible(si)) {
                    continue;
                }
                for (int v = 0; v < VOICES; ++v) {
                    collectCr(s, s->cr(static_cast<track_idx_t>(si) * VOICES + v));
                }
            }
        }
    };

    // Build a ChordAnalysisTone vector from a sounding-note list.
    auto buildTones = [](const std::vector<SoundingNote>& sounding) {
        int lowestPpitch = std::numeric_limits<int>::max();
        for (const SoundingNote& sn : sounding) {
            if (sn.ppitch < lowestPpitch) {
                lowestPpitch = sn.ppitch;
            }
        }
        std::vector<composing::analysis::ChordAnalysisTone> tones;
        tones.reserve(sounding.size());
        for (const SoundingNote& sn : sounding) {
            composing::analysis::ChordAnalysisTone t;
            t.pitch  = sn.ppitch;
            t.tpc    = sn.tpc;
            t.isBass = (sn.ppitch == lowestPpitch);
            tones.push_back(t);
        }
        return tones;
    };

    // Collect notes sounding at the selected tick.
    std::vector<SoundingNote> sounding;
    collectSoundingAt(seg, sounding);
    if (sounding.empty()) {
        return "";
    }

    // Key signature at this tick from the selected note's staff.
    const KeySigEvent keySig = sc->staff(note->staffIdx())->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());

    // Determine major/minor. If UNKNOWN, run KeyModeAnalyzer on a
    // look-back window covering the current and previous measure.
    bool isMajor = true;
    const KeyMode mode = keySig.mode();
    if (mode == KeyMode::MAJOR || mode == KeyMode::IONIAN) {
        isMajor = true;
    } else if (mode == KeyMode::MINOR || mode == KeyMode::AEOLIAN) {
        isMajor = false;
    } else {
        std::vector<composing::analysis::KeyModeAnalyzer::PitchContext> ctx;
        const Measure* currentMeasure = sc->tick2measure(tick);
        const Measure* startMeasure   = currentMeasure
                                        ? currentMeasure->prevMeasure()
                                        : nullptr;
        if (!startMeasure) {
            startMeasure = currentMeasure;
        }
        if (startMeasure) {
            for (const Segment* s = startMeasure->first(SegmentType::ChordRest);
                 s && s->tick() <= tick;
                 s = s->next1(SegmentType::ChordRest)) {
                for (size_t si = 0; si < sc->nstaves(); ++si) {
                    if (!staffIsEligible(si)) {
                        continue;
                    }
                    for (int v = 0; v < VOICES; ++v) {
                        const ChordRest* cr
                            = s->cr(static_cast<track_idx_t>(si) * VOICES + v);
                        if (!cr || !cr->isChord() || cr->isGrace()) {
                            continue;
                        }
                        for (const Note* n : toChord(cr)->notes()) {
                            composing::analysis::KeyModeAnalyzer::PitchContext p;
                            p.pitch = n->ppitch();
                            ctx.push_back(p);
                        }
                    }
                }
            }
        }

        const auto modeResults =
            composing::analysis::KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths);
        if (!modeResults.empty()) {
            isMajor = (modeResults.front().mode
                       == composing::analysis::KeyMode::Ionian);
        }
    }

    // Look back to populate temporal context (root-continuity scoring).
    // Walk backward from seg; find the first segment with freshly attacked
    // notes; cold-analyze it; store the result as the previous chord.
    composing::analysis::ChordTemporalContext temporalCtx;
    for (const Segment* s = seg->prev1(SegmentType::ChordRest);
         s != nullptr;
         s = s->prev1(SegmentType::ChordRest)) {
        bool hasAttacks = false;
        for (size_t si = 0; si < sc->nstaves() && !hasAttacks; ++si) {
            if (!staffIsEligible(si)) {
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
        collectSoundingAt(s, prevSounding);
        if (!prevSounding.empty()) {
            const auto prevTones = buildTones(prevSounding);
            const auto prevResults =
                composing::analysis::ChordAnalyzer::analyzeChord(
                    prevTones, keyFifths, isMajor);
            if (!prevResults.empty()) {
                temporalCtx.previousRootPc  = prevResults.front().rootPc;
                temporalCtx.previousQuality = prevResults.front().quality;
            }
        }
        break;
    }

    const std::string keyStr = std::string(keyName(keyFifths, isMajor))
                               + (isMajor ? " major" : " minor");

    const auto analysisTones = buildTones(sounding);
    const auto chordResults =
        composing::analysis::ChordAnalyzer::analyzeChord(
            analysisTones, keyFifths, isMajor, &temporalCtx);

    if (chordResults.empty()) {
        return "";
    }

    std::string candidates;
    std::set<std::string> seen;
    for (const auto& result : chordResults) {
        const std::string sym =
            composing::analysis::ChordSymbolFormatter::formatSymbol(
                result, keyFifths);
        if (sym.empty() || !seen.insert(sym).second) {
            continue;
        }
        if (!candidates.empty()) {
            candidates += " | ";
        }
        char buf[32];
        std::snprintf(buf, sizeof(buf), " (%.2f)", result.score);
        const std::string roman =
            composing::analysis::ChordSymbolFormatter::formatRomanNumeral(result, isMajor);
        if (!roman.empty()) {
            candidates += sym + " [" + roman + "]" + buf;
        } else {
            candidates += sym + buf;
        }
    }

    if (candidates.empty()) {
        return "";
    }

    return "[" + keyStr + "] " + candidates;
}

} // namespace
using namespace muse::async;
using namespace mu::engraving;
using namespace muse::accessibility;

NotationAccessibility::NotationAccessibility(const Notation* notation)
    : m_getScore(notation)
{
    notation->interaction()->selectionChanged().onNotify(this, [this]() {
        updateAccessibilityInfo();
    });

    notation->notationChanged().onReceive(this, [this](const muse::RectF&) {
        updateAccessibilityInfo();
    });
}

const mu::engraving::Score* NotationAccessibility::score() const
{
    return m_getScore->score();
}

const mu::engraving::Selection* NotationAccessibility::selection() const
{
    return &score()->selection();
}

muse::ValCh<std::string> NotationAccessibility::accessibilityInfo() const
{
    return m_accessibilityInfo;
}

void NotationAccessibility::setMapToScreenFunc(const AccessibleMapToScreenFunc& func)
{
#ifndef ENGRAVING_NO_ACCESSIBILITY
    score()->rootItem()->accessible()->accessibleRoot()->setMapToScreenFunc(func);
    score()->dummy()->rootItem()->accessible()->accessibleRoot()->setMapToScreenFunc(func);
#else
    UNUSED(func)
#endif
}

void NotationAccessibility::setEnabled(bool enabled)
{
#ifndef ENGRAVING_NO_ACCESSIBILITY
    std::vector<AccessibleRoot*> roots {
        score()->rootItem()->accessible()->accessibleRoot(),
        score()->dummy()->rootItem()->accessible()->accessibleRoot()
    };

    EngravingItem* selectedElement = selection()->element();
    AccessibleItemPtr selectedElementAccItem = selectedElement ? selectedElement->accessible() : nullptr;

    for (AccessibleRoot* root : roots) {
        root->setEnabled(enabled);

        if (!enabled) {
            root->setFocusedElement(nullptr);
            continue;
        }

        if (!selectedElementAccItem) {
            continue;
        }

        if (selectedElementAccItem->accessibleRoot() == root) {
            root->setFocusedElement(selectedElementAccItem);
        }
    }
#else
    UNUSED(enabled)
#endif
}

void NotationAccessibility::updateAccessibilityInfo()
{
    if (!score()) {
        return;
    }

    QString newAccessibilityInfo;

    if (selection()->isSingle()) {
        newAccessibilityInfo = singleElementAccessibilityInfo();
    } else if (selection()->isRange()) {
        newAccessibilityInfo = rangeAccessibilityInfo();
    } else if (selection()->isList()) {
        newAccessibilityInfo = muse::qtrc("notation", "List selection");
    }

    // Simplify whitespace and remove newlines
    newAccessibilityInfo = newAccessibilityInfo.simplified();

    setAccessibilityInfo(newAccessibilityInfo);
}

void NotationAccessibility::setAccessibilityInfo(const QString& info)
{
    std::string infoStd = info.toStdString();

    if (m_accessibilityInfo.val == infoStd) {
        return;
    }

    m_accessibilityInfo.set(infoStd);
}

QString NotationAccessibility::rangeAccessibilityInfo() const
{
    const mu::engraving::Segment* endSegment = selection()->endSegment();

    if (!endSegment) {
        endSegment = score()->lastSegment();
    } else {
        endSegment = endSegment->prev1MM();
    }

    EngravingItem::BarBeat startBarbeat = selection()->startSegment()->barbeat();

    QString start = muse::qtrc("engraving", "Start measure: %1").arg(String::number(startBarbeat.bar));
    if (startBarbeat.displayedBar != startBarbeat.bar) {
        start += "; " + muse::qtrc("engraving", "Start displayed measure: %1").arg(startBarbeat.displayedBar);
    }
    start += "; " + muse::qtrc("engraving", "Start beat: %1").arg(startBarbeat.beat);

    EngravingItem::BarBeat endBarbeat = endSegment->barbeat();
    QString end = muse::qtrc("engraving", "End measure: %1").arg(String::number(endBarbeat.bar));
    if (endBarbeat.displayedBar != endBarbeat.bar) {
        end += "; " + muse::qtrc("engraving", "End displayed measure: %1").arg(endBarbeat.displayedBar);
    }
    end += "; " + muse::qtrc("engraving", "End beat: %1").arg(endBarbeat.beat);

    return muse::qtrc("notation", "Range selection; %1; %2")
           .arg(start)
           .arg(end);
}

QString NotationAccessibility::singleElementAccessibilityInfo() const
{
    const EngravingItem* element = selection()->element();
    if (!element) {
        return QString();
    }

    QString accessibilityInfo = element->accessibleInfo();
    QString barsAndBeats = element->formatBarsAndBeats();

    if (!barsAndBeats.isEmpty()) {
        accessibilityInfo += "; " + barsAndBeats;
    }

    if (element->hasStaff()) {
        QString staff = muse::qtrc("notation", "Staff %1").arg(QString::number(element->staffIdx() + 1));

        QString staffName = element->staff()->part()->longName(element->tick());
        if (staffName.isEmpty()) {
            staffName = element->staff()->partName();
        }

        if (staffName.isEmpty()) {
            accessibilityInfo = QString("%1; %2").arg(accessibilityInfo).arg(staff);
        } else {
            accessibilityInfo = QString("%1; %2 (%3)").arg(accessibilityInfo).arg(staff).arg(staffName);
        }
    }

    // When a single note is selected, append harmonic analysis to the status bar.
    if (element->isNote()) {
        const std::string annotation = harmonicAnnotation(toNote(element));
        if (!annotation.empty()) {
            accessibilityInfo += "; " + QString::fromStdString(annotation);
        }
    }

    return accessibilityInfo;
}
