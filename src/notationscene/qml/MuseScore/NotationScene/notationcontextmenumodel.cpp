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

// The context menu calls mu::notation::analyzeNoteHarmonicContext() from the
// notation bridge rather than calling the composing module directly.  This
// keeps the dependency direction correct: notationscene → notation → composing.

#include "notationcontextmenumodel.h"
#include "types/translatablestring.h"
#include "ui/view/iconcodes.h"
#include "widgets/editstyleutils.h"
#include "engraving/dom/gradualtempochange.h"
#include "engraving/dom/fret.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/note.h"

#include "notation/internal/notationcomposingbridge.h"  // analyzeNoteHarmonicContext (mu::notation)
#include "composing/analysis/chord/chordanalyzer.h"           // ChordSymbolFormatter, ChordAnalysisResult
#include "composing/intonation/tuning_system.h"         // TuningRegistry, TuningSystem

#include <set>

using namespace mu::notation;
using namespace muse;
using namespace muse::uicomponents;
using namespace muse::actions;

// Minimal implementation to resolve linker error
muse::uicomponents::MenuItem* NotationContextMenuModel::makeEditStyle(const mu::engraving::EngravingItem* element)
{
    // TODO: Implement actual style editing logic if needed
    return nullptr;
}

void NotationContextMenuModel::appendNoteAnalysisItems(MenuItemList& items, const mu::engraving::Note* note)
{
    if (!note) {
        return;
    }

    const auto context = mu::notation::analyzeNoteHarmonicContextDetails(note);
    const int keyFifths = context.keyFifths;
    const bool wantChordSymbols = m_composingConfig()->analyzeForChordSymbols();
    const bool wantRomanNumerals = m_composingConfig()->analyzeForChordFunction();
    const bool wantNashvilleNumbers = m_composingConfig()->analyzeForChordFunction();

    if (!wantChordSymbols && !wantRomanNumerals && !wantNashvilleNumbers) {
        return;
    }

    // Sort a working copy by descending score so the highest-scoring candidate
    // appears first in the submenu.  The chordResults vector may have a
    // region-winner prepended at position 0 (potentially lower-scoring than the
    // fresh display analysis); sorting ensures the user always sees the best
    // candidate at the top, regardless of that prepend ordering.
    auto analysisResults = context.chordResults;
    std::sort(analysisResults.begin(), analysisResults.end(),
              [](const mu::composing::analysis::ChordAnalysisResult& a,
                 const mu::composing::analysis::ChordAnalysisResult& b) {
                  return a.identity.score > b.identity.score;
              });

    int maxAlternatives = m_composingConfig()->analysisAlternatives();

    struct TuneAsEntry {
        std::string label;
        int rootPc;
        int quality;
    };

    MenuItemList chordMenuItems, romanMenuItems, nashvilleMenuItems;
    std::vector<TuneAsEntry> tuneAsEntries;
    std::set<std::string> seenChordSymbols, seenNumerals, seenNashville;
    int chordCount = 0, romanCount = 0, nashvilleCount = 0;

    for (const auto& res : analysisResults) {
        std::string symbol    = mu::composing::analysis::ChordSymbolFormatter::formatSymbol(res, keyFifths);
        std::string numeral   = mu::composing::analysis::ChordSymbolFormatter::formatRomanNumeral(res);
        std::string nashville = mu::composing::analysis::ChordSymbolFormatter::formatNashvilleNumber(res, keyFifths);

        char buf[32];
        std::snprintf(buf, sizeof(buf), " (%.2f)", res.identity.score);

        if (wantChordSymbols && chordCount < maxAlternatives && !symbol.empty()
            && seenChordSymbols.insert(symbol).second) {
            std::string label = symbol + buf;
            MenuItem* item = new MenuItem(this);
            item->setId(QString("compose:add-chord-symbol:%1").arg(chordCount));
            ui::UiAction action;
            action.title = TranslatableString::untranslatable(QString::fromStdString(label));
            action.code = "add-chord-symbol-from-analysis";
            item->setAction(action);
            ui::UiActionState state;
            state.enabled = true;
            item->setState(state);
            item->setArgs(ActionData::make_arg1<QString>(QString::fromStdString(symbol)));
            chordMenuItems << item;
            ++chordCount;
        }

        if (wantRomanNumerals && romanCount < maxAlternatives && !numeral.empty()
            && seenNumerals.insert(numeral).second) {
            std::string label = numeral + buf;
            MenuItem* item = new MenuItem(this);
            item->setId(QString("compose:add-roman-numeral:%1").arg(romanCount));
            ui::UiAction action;
            action.title = TranslatableString::untranslatable(QString::fromStdString(label));
            action.code = "add-roman-numeral-from-analysis";
            item->setAction(action);
            ui::UiActionState state;
            state.enabled = true;
            item->setState(state);
            item->setArgs(ActionData::make_arg1<QString>(QString::fromStdString(numeral)));
            romanMenuItems << item;
            tuneAsEntries.push_back({ label, res.identity.rootPc, static_cast<int>(res.identity.quality) });
            ++romanCount;
        }

        if (wantNashvilleNumbers && nashvilleCount < maxAlternatives && !nashville.empty()
            && seenNashville.insert(nashville).second) {
            std::string label = nashville + buf;
            MenuItem* item = new MenuItem(this);
            item->setId(QString("compose:add-nashville-number:%1").arg(nashvilleCount));
            ui::UiAction action;
            action.title = TranslatableString::untranslatable(QString::fromStdString(label));
            action.code = "add-nashville-number-from-analysis";
            item->setAction(action);
            ui::UiActionState state;
            state.enabled = true;
            item->setState(state);
            item->setArgs(ActionData::make_arg1<QString>(QString::fromStdString(nashville)));
            nashvilleMenuItems << item;
            ++nashvilleCount;
        }
    }

    if (!chordMenuItems.isEmpty() || !romanMenuItems.isEmpty() || !nashvilleMenuItems.isEmpty()) {
        items << makeSeparator();
    }
    if (!chordMenuItems.isEmpty()) {
        items << makeMenu(TranslatableString("notation", "Add chord symbol"), chordMenuItems);
    }
    if (!romanMenuItems.isEmpty()) {
        items << makeMenu(TranslatableString("notation", "Add Roman numeral"), romanMenuItems);
    }
    if (!nashvilleMenuItems.isEmpty()) {
        items << makeMenu(TranslatableString("notation", "Add Nashville number"), nashvilleMenuItems);
    }

    // "Tune as [system name]" nested submenu — one leaf per unique Roman numeral result.
    if (wantRomanNumerals && !tuneAsEntries.empty()) {
        const std::string tuningKey = m_composingConfig()->tuningSystemKey();
        const composing::intonation::TuningSystem* sys
            = composing::intonation::TuningRegistry::byKey(tuningKey);
        const std::string displayName = sys ? sys->displayName() : tuningKey;

        const QString submenuTitle = QString("Tune as %1").arg(QString::fromStdString(displayName));
        MenuItemList tuneAsItems;
        int tuneIdx = 0;
        for (const TuneAsEntry& entry : tuneAsEntries) {
            MenuItem* item = new MenuItem(this);
            item->setId(QString("compose:tune-as:%1").arg(tuneIdx++));
            ui::UiAction action;
            action.title = TranslatableString::untranslatable(QString::fromStdString(entry.label));
            action.code = "compose-tune-as";
            item->setAction(action);
            ui::UiActionState state;
            state.enabled = true;
            item->setState(state);
            item->setArgs(ActionData::make_arg3<int, int, QString>(
                              entry.rootPc,
                              entry.quality,
                              QString::fromStdString(tuningKey)));
            tuneAsItems << item;
        }
        items << makeMenu(TranslatableString::untranslatable(submenuTitle), tuneAsItems);
    }
}

MenuItemList NotationContextMenuModel::makeNoteItems()
{
    MenuItemList items = makeElementItems();

    if (!m_composingConfig()->analyzeForChordSymbols() && !m_composingConfig()->analyzeForChordFunction()) {
        return items;
    }

    const EngravingItem* element = currentElement();
    const mu::engraving::Note* note = nullptr;

    if (element && element->isNote()) {
        note = engraving::toNote(element);
    } else if (element && element->isChord()) {
        const auto* chord = engraving::toChord(element);
        if (chord && !chord->notes().empty()) {
            note = chord->notes().front();
        }
    }

    appendNoteAnalysisItems(items, note);
    return items;
}

void NotationContextMenuModel::loadItems(int elementType)
{
    AbstractMenuModel::load();
    MenuItemList items = makeItemsByElementType(static_cast<ElementType>(elementType));
    setItems(items);
}

MenuItemList NotationContextMenuModel::makeItemsByElementType(ElementType elementType)
{
    switch (elementType) {
    case ElementType::MEASURE:
        return makeMeasureItems();
    case ElementType::PAGE:
        return makePageItems();
    case ElementType::STAFF_TEXT:
        return makeStaffTextItems();
    case ElementType::SYSTEM_TEXT:
    case ElementType::TRIPLET_FEEL:
        return makeSystemTextItems();
    case ElementType::TIMESIG:
        return makeTimeSignatureItems();
    case ElementType::INSTRUMENT_NAME:
        return makeInstrumentNameItems();
    case ElementType::HARMONY:
        return makeHarmonyItems();
    case ElementType::FRET_DIAGRAM:
        return makeFretboardDiagramItems();
    case ElementType::INSTRUMENT_CHANGE:
        return makeChangeInstrumentItems();
    case ElementType::VBOX:
        return makeVerticalBoxItems();
    case ElementType::HBOX:
        return makeHorizontalBoxItems();
    case ElementType::HAIRPIN_SEGMENT:
        return makeHairpinItems();
    case ElementType::GRADUAL_TEMPO_CHANGE_SEGMENT:
        return makeGradualTempoChangeItems();
    case ElementType::TEXT:
        return makeTextItems();
    case ElementType::NOTE:
    case ElementType::CHORD:
        return makeNoteItems();
    default:
        break;
    }

    return makeElementItems();
}

// ...remaining code...

MenuItemList NotationContextMenuModel::makeDefaultCopyPasteItems()
{
    MenuItemList items {
        makeMenuItem("action://notation/cut"),
        makeMenuItem("action://notation/copy"),
        makeMenuItem("action://notation/paste"),
        makeMenuItem("notation-swap"),
        makeMenuItem("action://notation/delete"),
    };

    return items;
}

MenuItemList NotationContextMenuModel::makeMeasureItems()
{
    MenuItemList items = {
        makeMenuItem("action://notation/cut"),
        makeMenuItem("action://notation/copy"),
        makeMenuItem("action://notation/paste"),
        makeMenuItem("notation-swap"),
    };

    items << makeSeparator();

    MenuItem* clearItem = makeMenuItem("action://notation/delete");
    clearItem->setTitle(TranslatableString("notation", "Clear measures"));
    MenuItem* deleteItem = makeMenuItem("time-delete");
    deleteItem->setTitle(TranslatableString("notation", "Delete measures"));
    items << clearItem;
    items << deleteItem;

    items << makeSeparator();

    if (isDrumsetStaff()) {
        items << makeMenuItem("customize-kit");
    }

    items << makeMenuItem("staff-properties");
    items << makeSeparator();
    items << makeMenu(TranslatableString("notation", "Insert measures"), makeInsertMeasuresItems());
    if (globalContext()->currentNotation()->viewMode() == mu::notation::ViewMode::PAGE) {
        items << makeMenu(TranslatableString("notation", "Move measures"), makeMoveMeasureItems());
    }
    items << makeMenuItem("make-into-system", TranslatableString("notation", "Create system from selection"));
    items << makeSeparator();
    items << makeMenuItem("measure-properties");

    // Append chord analysis items for the first selected note, if any.
    auto sel = selection();
    if (sel) {
        auto selNotes = sel->notes();
        if (!selNotes.empty()) {
            appendNoteAnalysisItems(items, selNotes.front());
        }
    }

    return items;
}

MenuItemList NotationContextMenuModel::makeStaffTextItems()
{
    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenuItem("staff-text-properties");

    return items;
}

MenuItemList NotationContextMenuModel::makeSystemTextItems()
{
    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenuItem("system-text-properties");

    return items;
}

MenuItemList NotationContextMenuModel::makeTimeSignatureItems()
{
    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenuItem("time-signature-properties");

    return items;
}

MenuItemList NotationContextMenuModel::makeInstrumentNameItems()
{
    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenuItem("staff-properties");

    return items;
}

MenuItemList NotationContextMenuModel::makeHarmonyItems()
{
    const EngravingItem* element = currentElement();
    if (element && engraving::toHarmony(element)->isInFretBox()) {
        return makeElementInFretBoxItems();
    }

    MenuItemList items = makeElementItems();
    items << makeSeparator();

    if (element) {
        engraving::EngravingObject* parent = element->isHarmony() ? element->explicitParent() : nullptr;
        bool hasLinkedFretboardDiagram = parent && parent->isFretDiagram();
        if (!hasLinkedFretboardDiagram) {
            items << makeMenuItem("add-fretboard-diagram");
        }
    }

    items << makeMenuItem("realize-chord-symbols");

    return items;
}

MenuItemList NotationContextMenuModel::makeFretboardDiagramItems()
{
    const EngravingItem* element = currentElement();
    if (element && engraving::toFretDiagram(element)->isInFretBox()) {
        return makeElementInFretBoxItems();
    }

    MenuItemList items = makeElementItems();

    const engraving::FretDiagram* fretDiagram = engraving::toFretDiagram(element);
    if (!fretDiagram->harmony()) {
        items << makeSeparator();
        items << makeMenuItem("chord-text", TranslatableString("notation", "Add c&hord symbol"));
    }

    return items;
}

MenuItemList NotationContextMenuModel::makeElementInFretBoxItems()
{
    MenuItemList items {
        makeMenuItem("action://notation/copy")
    };

    MenuItem* hideItem = makeMenuItem("action://notation/delete");

    ui::UiAction action = hideItem->action();
    action.iconCode = ui::IconCode::Code::NONE;
    action.title = TranslatableString("notation", "Hide");
    hideItem->setAction(action);

    items << hideItem
          << makeSeparator();

    MenuItemList selectItems = makeSelectItems();

    if (!selectItems.isEmpty()) {
        items << makeMenu(TranslatableString("notation", "Select"), selectItems)
              << makeSeparator();
    }

    const EngravingItem* element = currentElement();
    items << makeEditStyle(element);

    return items;
}

MenuItemList NotationContextMenuModel::makeSelectItems()
{
    if (isSingleSelection()) {
        return MenuItemList { makeMenuItem("select-similar"), makeMenuItem("select-similar-staff"), makeMenuItem("select-dialog") };
    } else if (canSelectSimilarInRange()) {
        return MenuItemList { makeMenuItem("select-similar-range"), makeMenuItem("select-dialog") };
    } else if (canSelectSimilar()) {
        return MenuItemList{ makeMenuItem("select-dialog") };
    }

    return MenuItemList();
}

MenuItemList NotationContextMenuModel::makeElementItems()
{
    MenuItemList items = makeDefaultCopyPasteItems();

    if (interaction()->isTextEditingStarted()) {
        return items;
    }

    MenuItemList selectItems = makeSelectItems();

    if (!selectItems.isEmpty()) {
        items << makeMenu(TranslatableString("notation", "Select"), selectItems);
    }

    const EngravingItem* element = currentElement();

    if (element && element->isEditable()) {
        items << makeSeparator();
        items << makeMenuItem("edit-element");
    }

    MenuItem* editStyleItem = makeEditStyle(element);
    if (editStyleItem) {
        items << makeSeparator();
        items << editStyleItem;
    }

    return items;
}

MenuItemList NotationContextMenuModel::makeInsertMeasuresItems()
{
    MenuItemList items {
        makeMenuItem("insert-measures-after-selection", TranslatableString("notation", "After selection…")),
        makeMenuItem("insert-measures", TranslatableString("notation", "Before selection…")),
        makeSeparator(),
        makeMenuItem("insert-measures-at-start-of-score", TranslatableString("notation", "At start of score…")),
        makeMenuItem("append-measures", TranslatableString("notation", "At end of score…"))
    };

    return items;
}

MenuItemList NotationContextMenuModel::makeMoveMeasureItems()
{
    MenuItemList items {
        makeMenuItem("move-measure-to-prev-system", TranslatableString("notation", "To previous system")),
        makeMenuItem("move-measure-to-next-system", TranslatableString("notation", "To next system"))
    };

    return items;
}

MenuItemList NotationContextMenuModel::makeChangeInstrumentItems()
{
    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenuItem("change-instrument");

    return items;
}

MenuItemList NotationContextMenuModel::makeVerticalBoxItems()
{
    MenuItemList addMenuItems;
    addMenuItems << makeMenuItem("frame-text");
    addMenuItems << makeMenuItem("title-text");
    addMenuItems << makeMenuItem("subtitle-text");
    addMenuItems << makeMenuItem("composer-text");
    addMenuItems << makeMenuItem("poet-text");
    addMenuItems << makeMenuItem("part-text");
    addMenuItems << makeMenuItem("add-image");

    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenu(TranslatableString("notation", "Add"), addMenuItems);

    return items;
}

MenuItemList NotationContextMenuModel::makeHorizontalBoxItems()
{
    MenuItemList addMenuItems;
    addMenuItems << makeMenuItem("frame-text");
    addMenuItems << makeMenuItem("add-image");

    MenuItemList items = makeElementItems();
    items << makeSeparator();
    items << makeMenu(TranslatableString("notation", "Add"), addMenuItems);

    return items;
}

MenuItemList NotationContextMenuModel::makeHairpinItems()
{
    MenuItemList items = makeElementItems();

    const EngravingItem* element = currentElement();
    if (!element || !element->isHairpinSegment() || !isSingleSelection()) {
        return items;
    }

    items << makeSeparator();

    const engraving::Hairpin* h = toHairpinSegment(element)->hairpin();
    ui::UiActionState snapPrevState = { true, h->snapToItemBefore() };
    MenuItem* snapPrev = makeMenuItem("toggle-snap-to-previous");
    snapPrev->setState(snapPrevState);
    items << snapPrev;

    ui::UiActionState snapNextState = { true, h->snapToItemAfter() };
    MenuItem* snapNext = makeMenuItem("toggle-snap-to-next");
    snapNext->setState(snapNextState);
    items << snapNext;

    return items;
}

MenuItemList NotationContextMenuModel::makeGradualTempoChangeItems()
{
    MenuItemList items = makeElementItems();

    const EngravingItem* element = currentElement();
    if (!element || !element->isGradualTempoChangeSegment() || !isSingleSelection()) {
        return items;
    }

    items << makeSeparator();

    const engraving::GradualTempoChange* gtc = toGradualTempoChangeSegment(element)->tempoChange();
    ui::UiActionState snapNextState = { true, gtc->snapToItemAfter() };
    MenuItem* snapNext = makeMenuItem("toggle-snap-to-next");
    snapNext->setState(snapNextState);
    items << snapNext;

    return items;
}

MenuItemList NotationContextMenuModel::makeTextItems()
{
    const EngravingItem* element = currentElement();
    if (!(element->parentItem() && element->parentItem()->isBarLine())) {
        // Regular text
        return makeElementItems();
    }

    // Play count text
    MenuItemList items;

    if (interaction()->isTextEditingStarted()) {
        return items;
    }

    MenuItemList selectItems = makeSelectItems();

    if (!selectItems.isEmpty()) {
        items << makeMenu(TranslatableString("notation", "Select"), selectItems);
    }

    items << makeSeparator()
          << makeEditStyle(element);

    return items;
}

MenuItemList NotationContextMenuModel::makePageItems()
{
    MenuItemList items {
        makeMenuItem("edit-style"),
        makeMenuItem("page-settings"),
        makeMenuItem("load-style"),
    };

    return items;
}

bool NotationContextMenuModel::isSingleSelection() const
{
    INotationSelectionPtr selection = this->selection();
    return selection ? selection->element() != nullptr : false;
}

bool NotationContextMenuModel::canSelectSimilar() const
{
    return currentElement() != nullptr;
}

bool NotationContextMenuModel::canSelectSimilarInRange() const
{
    return canSelectSimilar() && selection()->isRange();
}

bool NotationContextMenuModel::isDrumsetStaff() const
{
    const INotationInteraction::HitElementContext& ctx = hitElementContext();
    if (!ctx.staff) {
        return false;
    }

    Fraction tick = ctx.element ? ctx.element->tick() : Fraction { -1, 1 };
    return ctx.staff->part()->instrument(tick)->drumset() != nullptr;
}

INotationInteractionPtr NotationContextMenuModel::interaction() const
{
    INotationPtr notation = globalContext()->currentNotation();
    return notation ? notation->interaction() : nullptr;
}

INotationSelectionPtr NotationContextMenuModel::selection() const
{
    INotationInteractionPtr interaction = this->interaction();
    return interaction ? interaction->selection() : nullptr;
}

const EngravingItem* NotationContextMenuModel::currentElement() const
{
    const EngravingItem* element = hitElementContext().element;
    if (element) {
        return element;
    }

    auto selection = this->selection();
    return selection && selection->element() ? selection->element() : nullptr;
}

const INotationInteraction::HitElementContext& NotationContextMenuModel::hitElementContext() const
{
    if (INotationInteractionPtr interaction = this->interaction()) {
        return interaction->hitElementContext();
    }

    static INotationInteraction::HitElementContext dummy;
    return dummy;
}
