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
    property bool analyzeForChordFunction
    property bool inferKeyMode
    property int  analysisAlternatives
    property string tuningSystemKey
    property bool tonicAnchoredTuning
    property bool minimizeTuningDeviation
    property bool annotateTuningOffsets
    property real modeTierWeight1
    property real modeTierWeight2
    property real modeTierWeight3
    property real modeTierWeight4

    signal analyzeForChordSymbolsChangeRequested(bool value)
    signal analyzeForChordFunctionChangeRequested(bool value)
    signal inferKeyModeChangeRequested(bool value)
    signal analysisAlternativesChangeRequested(int count)
    signal tuningSystemKeyChangeRequested(string key)
    signal tonicAnchoredTuningChangeRequested(bool value)
    signal minimizeTuningDeviationChangeRequested(bool value)
    signal annotateTuningOffsetsChangeRequested(bool value)
    signal modeTierWeight1ChangeRequested(real value)
    signal modeTierWeight2ChangeRequested(real value)
    signal modeTierWeight3ChangeRequested(real value)
    signal modeTierWeight4ChangeRequested(real value)

    Column {
        spacing: root.rowSpacing

        // --- Analysis checkboxes ---
        CheckBox {
            id: chordSymbolsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Analyse chord symbols")
            checked: root.analyzeForChordSymbols
            navigation.name: "AnalyzeForChordSymbolsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.analyzeForChordSymbolsChangeRequested(!checked)
            }
        }
        CheckBox {
            id: chordFunctionCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Analyse chord function")
            checked: root.analyzeForChordFunction
            navigation.name: "AnalyzeForChordFunctionCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.analyzeForChordFunctionChangeRequested(!checked)
            }
        }
        CheckBox {
            id: inferKeyModeCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Analyse for key/mode")
            checked: root.inferKeyMode
            // Force-on when chord-function analysis is active; user can only
            // disable it when chord-function analysis is off.
            enabled: !root.analyzeForChordFunction
            navigation.name: "InferKeyModeCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.inferKeyModeChangeRequested(!checked)
            }
        }

        // --- Section break ---
        SeparatorLine { }

        // --- Context menu / general ---
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
                text: qsTrc("preferences", "Number of alternatives")
                horizontalAlignment: Text.AlignLeft
            }
            ComboBoxWithTitle {
                title: ""
                model: [
                    { text: "1", value: 1 },
                    { text: "2", value: 2 },
                    { text: "3", value: 3 }
                ]
                currentIndex: root.analysisAlternatives - 1
                controlWidth: 100
                navigationName: "AnalysisAlternativesComboBox"
                navigationPanel: root.navigation
                enabled: root.analyzeForChordSymbols || root.analyzeForChordFunction
                onValueEdited: function(newIndex, newValue) {
                    root.analysisAlternativesChangeRequested(newValue)
                }
            }
        }

        // --- Section break ---
        SeparatorLine { }

        // --- Intonation ---
        StyledTextLabel {
            text: qsTrc("preferences", "Intonation")
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
                text: qsTrc("preferences", "Tuning system")
                horizontalAlignment: Text.AlignLeft
                enabled: root.analyzeForChordFunction
            }

            property var tuningSystemModel: [
                { text: qsTrc("preferences", "Equal Temperament"),      value: "equal" },
                { text: qsTrc("preferences", "Just Intonation"),        value: "just" },
                { text: qsTrc("preferences", "Pythagorean"),            value: "pythagorean" },
                { text: qsTrc("preferences", "Quarter-Comma Meantone"), value: "quarter_comma_meantone" }
            ]

            ComboBoxWithTitle {
                title: ""
                model: parent.tuningSystemModel
                currentIndex: {
                    var key = root.tuningSystemKey
                    for (var i = 0; i < parent.tuningSystemModel.length; i++) {
                        if (parent.tuningSystemModel[i].value === key) { return i }
                    }
                    return 0
                }
                controlWidth: 200
                navigationName: "TuningSystemComboBox"
                navigationPanel: root.navigation
                enabled: root.analyzeForChordFunction
                onValueEdited: function(newIndex, newValue) {
                    root.tuningSystemKeyChangeRequested(newValue)
                }
            }
        }

        CheckBox {
            id: tonicAnchoredCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Anchor tuning to mode tonic")
            checked: root.tonicAnchoredTuning
            enabled: root.analyzeForChordFunction
            navigation.name: "TonicAnchoredTuningCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.tonicAnchoredTuningChangeRequested(!checked)
            }
        }
        CheckBox {
            id: minimizeRetuneCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Minimize average retune amount")
            checked: root.minimizeTuningDeviation
            enabled: root.analyzeForChordFunction
            navigation.name: "MinimizeTuningDeviationCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.minimizeTuningDeviationChangeRequested(!checked)
            }
        }
        CheckBox {
            id: annotateOffsetsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Annotate tuning offsets in score (¢)")
            checked: root.annotateTuningOffsets
            enabled: root.analyzeForChordFunction
            navigation.name: "AnnotateTuningOffsetsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.annotateTuningOffsetsChangeRequested(!checked)
            }
        }

        // --- Section break ---
        SeparatorLine { }

        // --- Mode weight section ---
        StyledTextLabel {
            text: qsTrc("preferences", "Mode detection weights")
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
                text: qsTrc("preferences", "Preset")
                horizontalAlignment: Text.AlignLeft
            }

            property var presetModel: [
                { text: qsTrc("preferences", "Standard"),  value: "standard" },
                { text: qsTrc("preferences", "Jazz"),      value: "jazz" },
                { text: qsTrc("preferences", "Modal"),     value: "modal" },
                { text: qsTrc("preferences", "Equal"),     value: "equal" }
            ]

            property var presetValues: ({
                "standard": { t1:  1.0, t2: -0.5, t3: -1.5, t4: -3.0 },
                "jazz":     { t1:  1.0, t2:  0.5, t3: -0.5, t4: -2.0 },
                "modal":    { t1:  0.5, t2:  0.5, t3:  0.0, t4: -1.5 },
                "equal":    { t1:  0.0, t2:  0.0, t3:  0.0, t4:  0.0 }
            })

            function currentPresetIndex() {
                var m = presetModel
                var pv = presetValues
                for (var i = 0; i < m.length; i++) {
                    var v = pv[m[i].value]
                    if (Math.abs(root.modeTierWeight1 - v.t1) < 0.01
                        && Math.abs(root.modeTierWeight2 - v.t2) < 0.01
                        && Math.abs(root.modeTierWeight3 - v.t3) < 0.01
                        && Math.abs(root.modeTierWeight4 - v.t4) < 0.01) {
                        return i
                    }
                }
                return -1  // custom values — no preset matches
            }

            ComboBoxWithTitle {
                title: ""
                model: parent.presetModel
                currentIndex: parent.currentPresetIndex()
                controlWidth: 200
                navigationName: "ModeWeightPresetComboBox"
                navigationPanel: root.navigation
                enabled: root.inferKeyMode
                onValueEdited: function(newIndex, newValue) {
                    var v = parent.presetValues[newValue]
                    if (v) {
                        root.modeTierWeight1ChangeRequested(v.t1)
                        root.modeTierWeight2ChangeRequested(v.t2)
                        root.modeTierWeight3ChangeRequested(v.t3)
                        root.modeTierWeight4ChangeRequested(v.t4)
                    }
                }
            }
        }

        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Tier 1 — Ionian (major) / Aeolian (minor)")
            columnWidth: root.columnWidth
            currentValue: root.modeTierWeight1
            minValue: -5.0
            maxValue: 5.0
            control.decimals: 1
            control.step: 0.5
            navigation.name: "ModeTierWeight1Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(newValue) {
                root.modeTierWeight1ChangeRequested(newValue)
            }
        }

        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Tier 2 — Dorian / Mixolydian")
            columnWidth: root.columnWidth
            currentValue: root.modeTierWeight2
            minValue: -5.0
            maxValue: 5.0
            control.decimals: 1
            control.step: 0.5
            navigation.name: "ModeTierWeight2Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(newValue) {
                root.modeTierWeight2ChangeRequested(newValue)
            }
        }

        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Tier 3 — Lydian / Phrygian")
            columnWidth: root.columnWidth
            currentValue: root.modeTierWeight3
            minValue: -5.0
            maxValue: 5.0
            control.decimals: 1
            control.step: 0.5
            navigation.name: "ModeTierWeight3Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(newValue) {
                root.modeTierWeight3ChangeRequested(newValue)
            }
        }

        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Tier 4 — Locrian")
            columnWidth: root.columnWidth
            currentValue: root.modeTierWeight4
            minValue: -5.0
            maxValue: 5.0
            control.decimals: 1
            control.step: 0.5
            navigation.name: "ModeTierWeight4Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(newValue) {
                root.modeTierWeight4ChangeRequested(newValue)
            }
        }
    }
}
