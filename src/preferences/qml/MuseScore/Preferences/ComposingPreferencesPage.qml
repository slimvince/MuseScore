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
            analyzeForRomanNumerals: preferencesModel.analyzeForRomanNumerals
            inferKeyMode:            preferencesModel.inferKeyMode
            analysisAlternatives:    preferencesModel.analysisAlternatives
            tuningSystemKey:         preferencesModel.tuningSystemKey

            navigation.section: root.navigationSection
            navigation.order: root.navigationOrderStart + 1

            onAnalyzeForChordSymbolsChangeRequested:  function(value) { preferencesModel.analyzeForChordSymbols  = value }
            onAnalyzeForRomanNumeralsChangeRequested: function(value) { preferencesModel.analyzeForRomanNumerals = value }
            onInferKeyModeChangeRequested:            function(value) { preferencesModel.inferKeyMode            = value }
            onAnalysisAlternativesChangeRequested:    function(count) { preferencesModel.analysisAlternatives    = count }
            onTuningSystemKeyChangeRequested:         function(key)   { preferencesModel.tuningSystemKey         = key   }
        }

        SeparatorLine { }

        ComposingStatusBarSection {
            showKeyModeInStatusBar:     preferencesModel.showKeyModeInStatusBar
            statusBarChordSymbolCount:  preferencesModel.statusBarChordSymbolCount
            statusBarRomanNumeralCount: preferencesModel.statusBarRomanNumeralCount
            analyzeForChordSymbols:     preferencesModel.analyzeForChordSymbols
            analyzeForRomanNumerals:    preferencesModel.analyzeForRomanNumerals
            inferKeyMode:               preferencesModel.inferKeyMode

            navigation.section: root.navigationSection
            navigation.order: root.navigationOrderStart + 2

            onShowKeyModeInStatusBarChangeRequested:      function(value) { preferencesModel.showKeyModeInStatusBar     = value }
            onStatusBarChordSymbolCountChangeRequested:   function(count) { preferencesModel.statusBarChordSymbolCount  = count }
            onStatusBarRomanNumeralCountChangeRequested:  function(count) { preferencesModel.statusBarRomanNumeralCount = count }
        }
    }
}
