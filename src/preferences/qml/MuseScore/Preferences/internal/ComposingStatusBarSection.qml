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

    title: qsTrc("preferences", "Status bar")

    property bool showKeyModeInStatusBar
    property int  statusBarChordSymbolCount
    property int  statusBarRomanNumeralCount
    property bool analyzeForChordSymbols
    property bool analyzeForRomanNumerals
    property bool inferKeyMode

    signal showKeyModeInStatusBarChangeRequested(bool value)
    signal statusBarChordSymbolCountChangeRequested(int count)
    signal statusBarRomanNumeralCountChangeRequested(int count)

    Column {
        spacing: root.rowSpacing

        CheckBox {
            id: showKeyModeCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "key/mode")
            checked: root.showKeyModeInStatusBar
            enabled: root.inferKeyMode
            navigation.name: "ShowKeyModeInStatusBarCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.showKeyModeInStatusBarChangeRequested(!checked)
            }
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
                    { text: "0", value: 0 },
                    { text: "1", value: 1 },
                    { text: "2", value: 2 },
                    { text: "3", value: 3 }
                ]
                currentIndex: root.statusBarChordSymbolCount
                controlWidth: 100
                navigationName: "StatusBarChordSymbolCountComboBox"
                navigationPanel: root.navigation
                enabled: root.analyzeForChordSymbols
                onValueEdited: function(newIndex, newValue) {
                    root.statusBarChordSymbolCountChangeRequested(newValue)
                }
            }
        }

        Row {
            spacing: 12
            StyledTextLabel {
                width: root.columnWidth
                anchors.verticalCenter: parent.verticalCenter
                text: qsTrc("preferences", "Number of suggested Roman numerals")
                horizontalAlignment: Text.AlignLeft
            }
            ComboBoxWithTitle {
                title: ""
                model: [
                    { text: "0", value: 0 },
                    { text: "1", value: 1 },
                    { text: "2", value: 2 },
                    { text: "3", value: 3 }
                ]
                currentIndex: root.statusBarRomanNumeralCount
                controlWidth: 100
                navigationName: "StatusBarRomanNumeralCountComboBox"
                navigationPanel: root.navigation
                enabled: root.analyzeForRomanNumerals
                onValueEdited: function(newIndex, newValue) {
                    root.statusBarRomanNumeralCountChangeRequested(newValue)
                }
            }
        }
    }
}
