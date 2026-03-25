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
import QtQuick

import Muse.Ui
import Muse.UiComponents

BaseSection {
    id: root

    title: qsTrc("preferences", "Analysis")

    property bool analyzeForChordSymbols
    property bool analyzeForRomanNumerals
    property bool inferKeyMode
    property int  analysisAlternatives

    signal analyzeForChordSymbolsChangeRequested(bool value)
    signal analyzeForRomanNumeralsChangeRequested(bool value)
    signal inferKeyModeChangeRequested(bool value)
    signal analysisAlternativesChangeRequested(int count)

    Column {
        spacing: root.rowSpacing

        // --- Analysis checkboxes ---
        CheckBox {
            id: chordSymbolsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Analyse for chord symbols")
            checked: root.analyzeForChordSymbols
            navigation.name: "AnalyzeForChordSymbolsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.analyzeForChordSymbolsChangeRequested(!checked)
            }
        }
        CheckBox {
            id: romanNumeralsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Analyse for Roman numerals")
            checked: root.analyzeForRomanNumerals
            navigation.name: "AnalyzeForRomanNumeralsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.analyzeForRomanNumeralsChangeRequested(!checked)
            }
        }
        CheckBox {
            id: inferKeyModeCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Analyse for key/mode")
            checked: root.inferKeyMode
            // Force-on when either analysis is active; user can only disable
            // when both chord-symbol and Roman-numeral analysis are off.
            enabled: !root.analyzeForChordSymbols && !root.analyzeForRomanNumerals
            navigation.name: "InferKeyModeCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.inferKeyModeChangeRequested(!checked)
            }
        }

        // --- Section break ---
        SeparatorLine { }

        // --- Context menu section ---
        StyledTextLabel {
            text: qsTrc("preferences", "Context menu")
            width: root.columnWidth
            font: ui.theme.bodyBoldFont
            horizontalAlignment: Text.AlignLeft
            wrapMode: Text.WordWrap
            padding: 0
            leftPadding: 0
            rightPadding: 0
            topPadding: root.rowSpacing
            bottomPadding: root.rowSpacing / 2
        }
        Row {
            spacing: 12
            StyledTextLabel {
                width: root.columnWidth
                anchors.verticalCenter: parent.verticalCenter
                text: qsTrc("preferences", "Number of suggested chords")
                horizontalAlignment: Text.AlignLeft
            }
            ComboBoxWithTitle {
                title: ""
                model: [
                    { text: "1", value: 1 },
                    { text: "2", value: 2 },
                    { text: "3", value: 3 },
                    { text: "4", value: 4 },
                    { text: "5", value: 5 }
                ]
                currentIndex: root.analysisAlternatives - 1
                controlWidth: 100
                navigationName: "AnalysisAlternativesComboBox"
                navigationPanel: root.navigation
                enabled: root.analyzeForChordSymbols || root.analyzeForRomanNumerals
                onValueEdited: function(newIndex, newValue) {
                    root.analysisAlternativesChangeRequested(newValue)
                }
            }
        }
    }
}
