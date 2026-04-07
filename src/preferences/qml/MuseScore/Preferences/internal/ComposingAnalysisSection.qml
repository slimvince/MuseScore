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
    property int  tuningMode          ///< 0 = TonicAnchored, 1 = FreeDrift
    property bool allowSplitSlurOfSustainedEvents
    property bool minimizeTuningDeviation
    property bool annotateTuningOffsets
    property bool annotateDriftAtBoundaries
    // Mode priors — diatonic
    property real modePriorIonian
    property real modePriorDorian
    property real modePriorPhrygian
    property real modePriorLydian
    property real modePriorMixolydian
    property real modePriorAeolian
    property real modePriorLocrian
    // Mode priors — melodic minor family
    property real modePriorMelodicMinor
    property real modePriorDorianB2
    property real modePriorLydianAugmented
    property real modePriorLydianDominant
    property real modePriorMixolydianB6
    property real modePriorAeolianB5
    property real modePriorAltered
    // Mode priors — harmonic minor family
    property real modePriorHarmonicMinor
    property real modePriorLocrianSharp6
    property real modePriorIonianSharp5
    property real modePriorDorianSharp4
    property real modePriorPhrygianDominant
    property real modePriorLydianSharp2
    property real modePriorAlteredDomBB7
    property string currentPreset     ///< Name of matching preset, or "" for custom

    signal analyzeForChordSymbolsChangeRequested(bool value)
    signal analyzeForChordFunctionChangeRequested(bool value)
    signal inferKeyModeChangeRequested(bool value)
    signal analysisAlternativesChangeRequested(int count)
    signal tuningSystemKeyChangeRequested(string key)
    signal tonicAnchoredTuningChangeRequested(bool value)
    signal tuningModeChangeRequested(int mode)
    signal allowSplitSlurOfSustainedEventsChangeRequested(bool value)
    signal minimizeTuningDeviationChangeRequested(bool value)
    signal annotateTuningOffsetsChangeRequested(bool value)
    signal annotateDriftAtBoundariesChangeRequested(bool value)
    signal modePriorIonianChangeRequested(real value)
    signal modePriorDorianChangeRequested(real value)
    signal modePriorPhrygianChangeRequested(real value)
    signal modePriorLydianChangeRequested(real value)
    signal modePriorMixolydianChangeRequested(real value)
    signal modePriorAeolianChangeRequested(real value)
    signal modePriorLocrianChangeRequested(real value)
    signal modePriorMelodicMinorChangeRequested(real value)
    signal modePriorDorianB2ChangeRequested(real value)
    signal modePriorLydianAugmentedChangeRequested(real value)
    signal modePriorLydianDominantChangeRequested(real value)
    signal modePriorMixolydianB6ChangeRequested(real value)
    signal modePriorAeolianB5ChangeRequested(real value)
    signal modePriorAlteredChangeRequested(real value)
    signal modePriorHarmonicMinorChangeRequested(real value)
    signal modePriorLocrianSharp6ChangeRequested(real value)
    signal modePriorIonianSharp5ChangeRequested(real value)
    signal modePriorDorianSharp4ChangeRequested(real value)
    signal modePriorPhrygianDominantChangeRequested(real value)
    signal modePriorLydianSharp2ChangeRequested(real value)
    signal modePriorAlteredDomBB7ChangeRequested(real value)
    signal applyPresetRequested(string name)

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
        Row {
            spacing: 12
            enabled: root.analyzeForChordFunction

            StyledTextLabel {
                anchors.verticalCenter: parent.verticalCenter
                text: qsTrc("preferences", "Drift mode")
                horizontalAlignment: Text.AlignLeft
            }

            Row {
                spacing: 4

                FlatButton {
                    text: qsTrc("preferences", "Tonic-anchored")
                    accentButton: root.tuningMode === 0
                    navigation.name: "TuningModeTonicAnchoredButton"
                    navigation.panel: root.navigation
                    onClicked: root.tuningModeChangeRequested(0)
                }
                FlatButton {
                    text: qsTrc("preferences", "Free drift")
                    accentButton: root.tuningMode === 1
                    navigation.name: "TuningModeFreeDriftButton"
                    navigation.panel: root.navigation
                    onClicked: root.tuningModeChangeRequested(1)
                }
            }
        }
        CheckBox {
            id: splitSlurSustainedEventsCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Allow split/slurring of sustained events for retuning")
            checked: root.allowSplitSlurOfSustainedEvents
            enabled: root.analyzeForChordFunction
            navigation.name: "AllowSplitSlurOfSustainedEventsCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.allowSplitSlurOfSustainedEventsChangeRequested(!checked)
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
        CheckBox {
            id: annotateDriftBoundariesCheckBox
            width: root.columnWidth
            text: qsTrc("preferences", "Annotate pitch drift at region boundaries (Free drift only)")
            checked: root.annotateDriftAtBoundaries
            enabled: root.analyzeForChordFunction && root.tuningMode === 1
            navigation.name: "AnnotateDriftAtBoundariesCheckBox"
            navigation.panel: root.navigation
            onClicked: {
                root.annotateDriftAtBoundariesChangeRequested(!checked)
            }
        }

        // --- Section break ---
        SeparatorLine { }

        // --- Mode prior section ---
        StyledTextLabel {
            text: qsTrc("preferences", "Mode detection priors")
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

        // Preset buttons
        Row {
            spacing: 6
            enabled: root.inferKeyMode

            Repeater {
                model: ["Standard", "Jazz", "Modal", "Baroque", "Contemporary"]

                FlatButton {
                    text: modelData
                    accentButton: root.currentPreset === modelData
                    onClicked: root.applyPresetRequested(modelData)
                }
            }
        }

        // Diatonic modes
        StyledTextLabel {
            text: qsTrc("preferences", "Diatonic")
            width: root.columnWidth
            font: ui.theme.bodyFont
            horizontalAlignment: Text.AlignLeft
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Ionian (major)")
            columnWidth: root.columnWidth
            currentValue: root.modePriorIonian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorIonianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorIonianChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Dorian")
            columnWidth: root.columnWidth
            currentValue: root.modePriorDorian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorDorianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorDorianChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Phrygian")
            columnWidth: root.columnWidth
            currentValue: root.modePriorPhrygian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorPhrygianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorPhrygianChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Lydian")
            columnWidth: root.columnWidth
            currentValue: root.modePriorLydian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorLydianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorLydianChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Mixolydian")
            columnWidth: root.columnWidth
            currentValue: root.modePriorMixolydian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorMixolydianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorMixolydianChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Aeolian (natural minor)")
            columnWidth: root.columnWidth
            currentValue: root.modePriorAeolian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorAeolianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorAeolianChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Locrian")
            columnWidth: root.columnWidth
            currentValue: root.modePriorLocrian
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorLocrianControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorLocrianChangeRequested(v) }
        }

        // Melodic minor family
        StyledTextLabel {
            text: qsTrc("preferences", "Melodic minor family")
            width: root.columnWidth
            font: ui.theme.bodyFont
            horizontalAlignment: Text.AlignLeft
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Melodic minor")
            columnWidth: root.columnWidth
            currentValue: root.modePriorMelodicMinor
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorMelodicMinorControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorMelodicMinorChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Dorian ♭2")
            columnWidth: root.columnWidth
            currentValue: root.modePriorDorianB2
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorDorianB2Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorDorianB2ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Lydian augmented")
            columnWidth: root.columnWidth
            currentValue: root.modePriorLydianAugmented
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorLydianAugmentedControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorLydianAugmentedChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Lydian dominant")
            columnWidth: root.columnWidth
            currentValue: root.modePriorLydianDominant
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorLydianDominantControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorLydianDominantChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Mixolydian ♭6")
            columnWidth: root.columnWidth
            currentValue: root.modePriorMixolydianB6
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorMixolydianB6Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorMixolydianB6ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Aeolian ♭5 (half-diminished)")
            columnWidth: root.columnWidth
            currentValue: root.modePriorAeolianB5
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorAeolianB5Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorAeolianB5ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Altered (super-Locrian)")
            columnWidth: root.columnWidth
            currentValue: root.modePriorAltered
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorAlteredControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorAlteredChangeRequested(v) }
        }

        // Harmonic minor family
        StyledTextLabel {
            text: qsTrc("preferences", "Harmonic minor family")
            width: root.columnWidth
            font: ui.theme.bodyFont
            horizontalAlignment: Text.AlignLeft
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Harmonic minor")
            columnWidth: root.columnWidth
            currentValue: root.modePriorHarmonicMinor
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorHarmonicMinorControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorHarmonicMinorChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Locrian ♯6")
            columnWidth: root.columnWidth
            currentValue: root.modePriorLocrianSharp6
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorLocrianSharp6Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorLocrianSharp6ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Ionian ♯5")
            columnWidth: root.columnWidth
            currentValue: root.modePriorIonianSharp5
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorIonianSharp5Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorIonianSharp5ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Dorian ♯4")
            columnWidth: root.columnWidth
            currentValue: root.modePriorDorianSharp4
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorDorianSharp4Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorDorianSharp4ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Phrygian dominant")
            columnWidth: root.columnWidth
            currentValue: root.modePriorPhrygianDominant
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorPhrygianDominantControl"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorPhrygianDominantChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Lydian ♯2")
            columnWidth: root.columnWidth
            currentValue: root.modePriorLydianSharp2
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorLydianSharp2Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorLydianSharp2ChangeRequested(v) }
        }
        IncrementalPropertyControlWithTitle {
            title: qsTrc("preferences", "Altered dominant ♭♭7")
            columnWidth: root.columnWidth
            currentValue: root.modePriorAlteredDomBB7
            minValue: -5.0; maxValue: 5.0
            control.decimals: 2; control.step: 0.1
            navigation.name: "ModePriorAlteredDomBB7Control"
            navigation.panel: root.navigation
            enabled: root.inferKeyMode
            onValueEdited: function(v) { root.modePriorAlteredDomBB7ChangeRequested(v) }
        }
    }
}
