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
import QtQuick.Controls

import Muse.UiComponents
import MuseScore.Preferences

import "internal"

PreferencesPage {
    id: root

    Component.onCompleted: {
        preferencesModel.load()
    }

    ComposingPreferencesModel {
        id: preferencesModel
    }

    Column {
        width: parent.width
        spacing: root.sectionsSpacing

        ComposingAnalysisSection {
            analyzeForChordSymbols:  preferencesModel.analyzeForChordSymbols
            analyzeForChordFunction: preferencesModel.analyzeForChordFunction
            inferKeyMode:            preferencesModel.inferKeyMode
            analysisAlternatives:    preferencesModel.analysisAlternatives
            tuningSystemKey:         preferencesModel.tuningSystemKey
            tonicAnchoredTuning:     preferencesModel.tonicAnchoredTuning
            tuningMode:              preferencesModel.tuningMode
            minimizeTuningDeviation: preferencesModel.minimizeTuningDeviation
            annotateTuningOffsets:        preferencesModel.annotateTuningOffsets
            annotateDriftAtBoundaries:    preferencesModel.annotateDriftAtBoundaries
            // Mode priors — diatonic
            modePriorIonian:     preferencesModel.modePriorIonian
            modePriorDorian:     preferencesModel.modePriorDorian
            modePriorPhrygian:   preferencesModel.modePriorPhrygian
            modePriorLydian:     preferencesModel.modePriorLydian
            modePriorMixolydian: preferencesModel.modePriorMixolydian
            modePriorAeolian:    preferencesModel.modePriorAeolian
            modePriorLocrian:    preferencesModel.modePriorLocrian
            // Mode priors — melodic minor family
            modePriorMelodicMinor:  preferencesModel.modePriorMelodicMinor
            modePriorDorianB2:      preferencesModel.modePriorDorianB2
            modePriorLydianAugmented: preferencesModel.modePriorLydianAugmented
            modePriorLydianDominant:  preferencesModel.modePriorLydianDominant
            modePriorMixolydianB6:  preferencesModel.modePriorMixolydianB6
            modePriorAeolianB5:     preferencesModel.modePriorAeolianB5
            modePriorAltered:       preferencesModel.modePriorAltered
            // Mode priors — harmonic minor family
            modePriorHarmonicMinor: preferencesModel.modePriorHarmonicMinor
            modePriorLocrianSharp6: preferencesModel.modePriorLocrianSharp6
            modePriorIonianSharp5:  preferencesModel.modePriorIonianSharp5
            modePriorDorianSharp4:  preferencesModel.modePriorDorianSharp4
            modePriorPhrygianDominant: preferencesModel.modePriorPhrygianDominant
            modePriorLydianSharp2:  preferencesModel.modePriorLydianSharp2
            modePriorAlteredDomBB7: preferencesModel.modePriorAlteredDomBB7
            currentPreset:          preferencesModel.currentModePriorPreset

            navigation.section: root.navigationSection
            navigation.order: root.navigationOrderStart + 1

            onAnalyzeForChordSymbolsChangeRequested:  function(value) { preferencesModel.analyzeForChordSymbols  = value }
            onAnalyzeForChordFunctionChangeRequested: function(value) { preferencesModel.analyzeForChordFunction = value }
            onInferKeyModeChangeRequested:            function(value) { preferencesModel.inferKeyMode            = value }
            onAnalysisAlternativesChangeRequested:    function(count) { preferencesModel.analysisAlternatives    = count }
            onTuningSystemKeyChangeRequested:         function(key)   { preferencesModel.tuningSystemKey         = key   }
            onTonicAnchoredTuningChangeRequested:     function(value) { preferencesModel.tonicAnchoredTuning     = value }
            onTuningModeChangeRequested:              function(mode)  { preferencesModel.tuningMode              = mode  }
            onMinimizeTuningDeviationChangeRequested: function(value) { preferencesModel.minimizeTuningDeviation = value }
            onAnnotateTuningOffsetsChangeRequested:        function(value) { preferencesModel.annotateTuningOffsets        = value }
            onAnnotateDriftAtBoundariesChangeRequested:    function(value) { preferencesModel.annotateDriftAtBoundaries    = value }
            onModePriorIonianChangeRequested:         function(v) { preferencesModel.modePriorIonian     = v }
            onModePriorDorianChangeRequested:         function(v) { preferencesModel.modePriorDorian     = v }
            onModePriorPhrygianChangeRequested:       function(v) { preferencesModel.modePriorPhrygian   = v }
            onModePriorLydianChangeRequested:         function(v) { preferencesModel.modePriorLydian     = v }
            onModePriorMixolydianChangeRequested:     function(v) { preferencesModel.modePriorMixolydian = v }
            onModePriorAeolianChangeRequested:        function(v) { preferencesModel.modePriorAeolian    = v }
            onModePriorLocrianChangeRequested:        function(v) { preferencesModel.modePriorLocrian    = v }
            onModePriorMelodicMinorChangeRequested:   function(v) { preferencesModel.modePriorMelodicMinor  = v }
            onModePriorDorianB2ChangeRequested:       function(v) { preferencesModel.modePriorDorianB2      = v }
            onModePriorLydianAugmentedChangeRequested: function(v) { preferencesModel.modePriorLydianAugmented = v }
            onModePriorLydianDominantChangeRequested:  function(v) { preferencesModel.modePriorLydianDominant  = v }
            onModePriorMixolydianB6ChangeRequested:   function(v) { preferencesModel.modePriorMixolydianB6  = v }
            onModePriorAeolianB5ChangeRequested:      function(v) { preferencesModel.modePriorAeolianB5     = v }
            onModePriorAlteredChangeRequested:        function(v) { preferencesModel.modePriorAltered       = v }
            onModePriorHarmonicMinorChangeRequested:  function(v) { preferencesModel.modePriorHarmonicMinor = v }
            onModePriorLocrianSharp6ChangeRequested:  function(v) { preferencesModel.modePriorLocrianSharp6 = v }
            onModePriorIonianSharp5ChangeRequested:   function(v) { preferencesModel.modePriorIonianSharp5  = v }
            onModePriorDorianSharp4ChangeRequested:   function(v) { preferencesModel.modePriorDorianSharp4  = v }
            onModePriorPhrygianDominantChangeRequested: function(v) { preferencesModel.modePriorPhrygianDominant = v }
            onModePriorLydianSharp2ChangeRequested:   function(v) { preferencesModel.modePriorLydianSharp2  = v }
            onModePriorAlteredDomBB7ChangeRequested:  function(v) { preferencesModel.modePriorAlteredDomBB7 = v }
            onApplyPresetRequested: function(name) { preferencesModel.applyModePriorPreset(name) }
        }

        SeparatorLine { }

        ComposingStatusBarSection {
            showKeyModeInStatusBar:          preferencesModel.showKeyModeInStatusBar
            showChordSymbolsInStatusBar:     preferencesModel.showChordSymbolsInStatusBar
            showRomanNumeralsInStatusBar:    preferencesModel.showRomanNumeralsInStatusBar
            showNashvilleNumbersInStatusBar: preferencesModel.showNashvilleNumbersInStatusBar
            analyzeForChordSymbols:          preferencesModel.analyzeForChordSymbols
            analyzeForChordFunction:         preferencesModel.analyzeForChordFunction
            inferKeyMode:                    preferencesModel.inferKeyMode

            navigation.section: root.navigationSection
            navigation.order: root.navigationOrderStart + 2

            onShowKeyModeInStatusBarChangeRequested:          function(value) { preferencesModel.showKeyModeInStatusBar          = value }
            onShowChordSymbolsInStatusBarChangeRequested:     function(value) { preferencesModel.showChordSymbolsInStatusBar     = value }
            onShowRomanNumeralsInStatusBarChangeRequested:    function(value) { preferencesModel.showRomanNumeralsInStatusBar    = value }
            onShowNashvilleNumbersInStatusBarChangeRequested: function(value) { preferencesModel.showNashvilleNumbersInStatusBar = value }
        }

        SeparatorLine { }

        ComposingChordStaffSection {
            chordStaffWriteChordSymbols:   preferencesModel.chordStaffWriteChordSymbols
            chordStaffFunctionNotation:    preferencesModel.chordStaffFunctionNotation
            chordStaffWriteKeyAnnotations: preferencesModel.chordStaffWriteKeyAnnotations
            chordStaffHighlightNonDiatonic: preferencesModel.chordStaffHighlightNonDiatonic
            chordStaffWriteCadenceMarkers: preferencesModel.chordStaffWriteCadenceMarkers
            analyzeForChordSymbols:        preferencesModel.analyzeForChordSymbols
            analyzeForChordFunction:       preferencesModel.analyzeForChordFunction
            inferKeyMode:                  preferencesModel.inferKeyMode

            navigation.section: root.navigationSection
            navigation.order: root.navigationOrderStart + 3

            onChordStaffWriteChordSymbolsChangeRequested:    function(value) { preferencesModel.chordStaffWriteChordSymbols    = value }
            onChordStaffFunctionNotationChangeRequested:     function(value) { preferencesModel.chordStaffFunctionNotation     = value }
            onChordStaffWriteKeyAnnotationsChangeRequested:  function(value) { preferencesModel.chordStaffWriteKeyAnnotations  = value }
            onChordStaffHighlightNonDiatonicChangeRequested: function(value) { preferencesModel.chordStaffHighlightNonDiatonic = value }
            onChordStaffWriteCadenceMarkersChangeRequested:  function(value) { preferencesModel.chordStaffWriteCadenceMarkers  = value }
        }
    }
}
