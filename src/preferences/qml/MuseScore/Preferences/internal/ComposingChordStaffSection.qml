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

    title: qsTrc("preferences", "Chord staff")

    property bool   chordStaffWriteChordSymbols
    property string chordStaffFunctionNotation
    property bool   chordStaffWriteKeyAnnotations
    property bool   chordStaffHighlightNonDiatonic
    property bool   chordStaffWriteCadenceMarkers

    property bool analyzeForChordSymbols
    property bool analyzeForChordFunction
    property bool inferKeyMode

    signal chordStaffWriteChordSymbolsChangeRequested(bool value)
    signal chordStaffFunctionNotationChangeRequested(string value)
    signal chordStaffWriteKeyAnnotationsChangeRequested(bool value)
    signal chordStaffHighlightNonDiatonicChangeRequested(bool value)
    signal chordStaffWriteCadenceMarkersChangeRequested(bool value)

    Column {
        spacing: root.rowSpacing

        // --- Chord labels ---
        StyledTextLabel {
            text: qsTrc("preferences", "Chord labels")
            width: root.columnWidth
            font: ui.theme.bodyBoldFont
            horizontalAlignment: Text.AlignLeft
            wrapMode: Text.WordWrap
            padding: 0
            leftPadding: 0
            rightPadding: 0
            bottomPadding: root.rowSpacing / 2
        }

        CheckBox {
            id: writeChordSymbolsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Write chord symbols")
            checked: root.chordStaffWriteChordSymbols
            enabled: root.analyzeForChordSymbols
            navigation.name: "ChordStaffWriteChordSymbolsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.chordStaffWriteChordSymbolsChangeRequested(!checked)
            }
        }

        Row {
            spacing: 12
            StyledTextLabel {
                width: root.columnWidth
                anchors.verticalCenter: parent.verticalCenter
                text: qsTrc("preferences", "Chord function notation")
                horizontalAlignment: Text.AlignLeft
                enabled: root.analyzeForChordFunction
            }

            property var functionNotationModel: [
                { text: qsTrc("preferences", "None"),             value: "none" },
                { text: qsTrc("preferences", "Roman numerals"),   value: "roman" },
                { text: qsTrc("preferences", "Nashville numbers"), value: "nashville" }
            ]

            ComboBoxWithTitle {
                title: ""
                model: parent.functionNotationModel
                currentIndex: {
                    var key = root.chordStaffFunctionNotation
                    for (var i = 0; i < parent.functionNotationModel.length; i++) {
                        if (parent.functionNotationModel[i].value === key) { return i }
                    }
                    return 1 // default: roman
                }
                controlWidth: 200
                navigationName: "ChordStaffFunctionNotationComboBox"
                navigationPanel: root.navigation
                enabled: root.analyzeForChordFunction
                onValueEdited: function(newIndex, newValue) {
                    root.chordStaffFunctionNotationChangeRequested(newValue)
                }
            }
        }

        // --- Section break ---
        SeparatorLine { }

        // --- Key analysis ---
        StyledTextLabel {
            text: qsTrc("preferences", "Key analysis")
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

        CheckBox {
            id: writeKeyAnnotationsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Write key/mode annotations")
            checked: root.chordStaffWriteKeyAnnotations
            enabled: root.inferKeyMode
            navigation.name: "ChordStaffWriteKeyAnnotationsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.chordStaffWriteKeyAnnotationsChangeRequested(!checked)
            }
        }

        CheckBox {
            id: highlightNonDiatonicCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Mark non-diatonic chords")
            checked: root.chordStaffHighlightNonDiatonic
            enabled: root.analyzeForChordFunction
            navigation.name: "ChordStaffHighlightNonDiatonicCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.chordStaffHighlightNonDiatonicChangeRequested(!checked)
            }
        }

        CheckBox {
            id: writeCadenceMarkersCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Write cadence markers (PAC, HC, DC, PC)")
            checked: root.chordStaffWriteCadenceMarkers
            enabled: root.analyzeForChordFunction
            navigation.name: "ChordStaffWriteCadenceMarkersCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.chordStaffWriteCadenceMarkersChangeRequested(!checked)
            }
        }
    }
}
