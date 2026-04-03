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
    property bool showChordSymbolsInStatusBar
    property bool showRomanNumeralsInStatusBar
    property bool showNashvilleNumbersInStatusBar
    property bool analyzeForChordSymbols
    property bool analyzeForChordFunction
    property bool inferKeyMode

    signal showKeyModeInStatusBarChangeRequested(bool value)
    signal showChordSymbolsInStatusBarChangeRequested(bool value)
    signal showRomanNumeralsInStatusBarChangeRequested(bool value)
    signal showNashvilleNumbersInStatusBarChangeRequested(bool value)

    Column {
        spacing: root.rowSpacing

        CheckBox {
            id: showChordSymbolsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Chord symbols")
            checked: root.showChordSymbolsInStatusBar
            enabled: root.analyzeForChordSymbols
            navigation.name: "ShowChordSymbolsInStatusBarCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.showChordSymbolsInStatusBarChangeRequested(!checked)
            }
        }

        CheckBox {
            id: showRomanNumeralsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Roman numerals")
            checked: root.showRomanNumeralsInStatusBar
            enabled: root.analyzeForChordFunction
            navigation.name: "ShowRomanNumeralsInStatusBarCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.showRomanNumeralsInStatusBarChangeRequested(!checked)
            }
        }

        CheckBox {
            id: showNashvilleNumbersCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Nashville numbers")
            checked: root.showNashvilleNumbersInStatusBar
            enabled: root.analyzeForChordFunction
            navigation.name: "ShowNashvilleNumbersInStatusBarCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.showNashvilleNumbersInStatusBarChangeRequested(!checked)
            }
        }

        CheckBox {
            id: showKeyModeCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Key/mode")
            checked: root.showKeyModeInStatusBar
            enabled: root.inferKeyMode
            navigation.name: "ShowKeyModeInStatusBarCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.showKeyModeInStatusBarChangeRequested(!checked)
            }
        }
    }
}
