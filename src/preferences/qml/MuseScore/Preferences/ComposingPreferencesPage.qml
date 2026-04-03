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
            minimizeTuningDeviation: preferencesModel.minimizeTuningDeviation
            annotateTuningOffsets:   preferencesModel.annotateTuningOffsets
            modeTierWeight1:         preferencesModel.modeTierWeight1
            modeTierWeight2:         preferencesModel.modeTierWeight2
            modeTierWeight3:         preferencesModel.modeTierWeight3
            modeTierWeight4:         preferencesModel.modeTierWeight4

            navigation.section: root.navigationSection
            navigation.order: root.navigationOrderStart + 1

            onAnalyzeForChordSymbolsChangeRequested:  function(value) { preferencesModel.analyzeForChordSymbols  = value }
            onAnalyzeForChordFunctionChangeRequested: function(value) { preferencesModel.analyzeForChordFunction = value }
            onInferKeyModeChangeRequested:            function(value) { preferencesModel.inferKeyMode            = value }
            onAnalysisAlternativesChangeRequested:    function(count) { preferencesModel.analysisAlternatives    = count }
            onTuningSystemKeyChangeRequested:         function(key)   { preferencesModel.tuningSystemKey         = key   }
            onTonicAnchoredTuningChangeRequested:     function(value) { preferencesModel.tonicAnchoredTuning     = value }
            onMinimizeTuningDeviationChangeRequested: function(value) { preferencesModel.minimizeTuningDeviation = value }
            onAnnotateTuningOffsetsChangeRequested:   function(value) { preferencesModel.annotateTuningOffsets   = value }
            onModeTierWeight1ChangeRequested:         function(value) { preferencesModel.modeTierWeight1         = value }
            onModeTierWeight2ChangeRequested:         function(value) { preferencesModel.modeTierWeight2         = value }
            onModeTierWeight3ChangeRequested:         function(value) { preferencesModel.modeTierWeight3         = value }
            onModeTierWeight4ChangeRequested:         function(value) { preferencesModel.modeTierWeight4         = value }
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
