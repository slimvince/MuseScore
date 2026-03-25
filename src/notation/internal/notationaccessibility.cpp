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
#include "composing/icomposingconfiguration.h"
#include "modularity/ioc.h"

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
    static muse::GlobalInject<mu::composing::IComposingConfiguration> config;
    const auto* prefs = config.get().get();
    if (!prefs) {
        return "";
    }


    int keyFifths = 0;
    bool isMajor = true;
    const auto chordResults = mu::composing::analysis::analyzeNoteHarmonicContext(note, keyFifths, isMajor);

    // Key/mode string (optional)
    std::string keyStr;
    if (prefs->showKeyModeInStatusBar()) {
        keyStr = std::string(keyName(keyFifths, isMajor)) + (isMajor ? " major" : " minor");
    }

    // If both analyzers are off, but key/mode display is on, show only key/mode
    if (!prefs->analyzeForChordSymbols() && !prefs->analyzeForRomanNumerals()) {
        if (!keyStr.empty()) {
            return "[" + keyStr + "]";
        } else {
            return "";
        }
    }

    if (chordResults.empty()) {
        // If no analysis results, but key/mode display is on, show only key/mode
        if (!keyStr.empty()) {
            return "[" + keyStr + "]";
        } else {
            return "";
        }
    }

    // Prepare candidates, respecting limits for chord symbols and Roman numerals
    int maxChordSyms = prefs->statusBarChordSymbolCount();
    int maxRomans   = prefs->statusBarRomanNumeralCount();
    int chordCount = 0, romanCount = 0;
    std::string candidates;
    std::set<std::string> seenSyms, seenRomans;
    for (const auto& result : chordResults) {
        // Chord symbol
        std::string sym;
        if (prefs->analyzeForChordSymbols()) {
            sym = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(result, keyFifths);
        }
        // Roman numeral
        std::string roman;
        if (prefs->analyzeForRomanNumerals()) {
            roman = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(result, isMajor);
        }

        // Skip if both are empty or already shown
        if ((sym.empty() || !seenSyms.insert(sym).second) && (roman.empty() || !seenRomans.insert(roman).second)) {
            continue;
        }

        // Respect per-type limits
        bool showSym = prefs->analyzeForChordSymbols() && !sym.empty() && chordCount < maxChordSyms;
        bool showRoman = prefs->analyzeForRomanNumerals() && !roman.empty() && romanCount < maxRomans;
        if (!showSym && !showRoman) {
            continue;
        }

        if (!candidates.empty()) {
            candidates += " | ";
        }
        char buf[32];
        std::snprintf(buf, sizeof(buf), " (%.2f)", result.score);

        if (showSym && showRoman) {
            candidates += sym + " [" + roman + "]" + buf;
            ++chordCount;
            ++romanCount;
        } else if (showSym) {
            candidates += sym + buf;
            ++chordCount;
        } else if (showRoman) {
            candidates += "[" + roman + "]" + buf;
            ++romanCount;
        }
    }

    if (candidates.empty()) {
        if (!keyStr.empty()) {
            return "[" + keyStr + "]";
        } else {
            return "";
        }
    }

    if (!keyStr.empty()) {
        return "[" + keyStr + "] " + candidates;
    } else {
        return candidates;
    }
}

} // namespace

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
                           bool& outIsMajor)
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

    struct SoundingNote { int ppitch; int tpc; };

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

    auto buildTones = [](const std::vector<SoundingNote>& sounding) {
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
    };

    std::vector<SoundingNote> sounding;
    collectSoundingAt(seg, sounding);
    if (sounding.empty()) {
        return {};
    }

    const KeySigEvent keySig = sc->staff(note->staffIdx())->keySigEvent(tick);
    const int keyFifths = static_cast<int>(keySig.concertKey());
    outKeyFifths = keyFifths;

    bool isMajor = true;
    const mu::engraving::KeyMode mode = keySig.mode();
    if (mode == mu::engraving::KeyMode::MAJOR || mode == mu::engraving::KeyMode::IONIAN) {
        isMajor = true;
    } else if (mode == mu::engraving::KeyMode::MINOR || mode == mu::engraving::KeyMode::AEOLIAN) {
        isMajor = false;
    } else {
        std::vector<KeyModeAnalyzer::PitchContext> ctx;
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
                            KeyModeAnalyzer::PitchContext p;
                            p.pitch = n->ppitch();
                            ctx.push_back(p);
                        }
                    }
                }
            }
        }

        const auto modeResults =
            KeyModeAnalyzer::analyzeKeyMode(ctx, keyFifths);
        if (!modeResults.empty()) {
            isMajor = (modeResults.front().mode == mu::composing::analysis::KeyMode::Ionian);
        }
    }
    outIsMajor = isMajor;

    ChordTemporalContext temporalCtx;
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
                ChordAnalyzer::analyzeChord(prevTones, keyFifths, isMajor);
            if (!prevResults.empty()) {
                temporalCtx.previousRootPc  = prevResults.front().rootPc;
                temporalCtx.previousQuality = prevResults.front().quality;
            }
        }
        break;
    }

    const auto analysisTones = buildTones(sounding);
    return ChordAnalyzer::analyzeChord(analysisTones, keyFifths, isMajor, &temporalCtx);
}

} // namespace mu::composing::analysis

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
