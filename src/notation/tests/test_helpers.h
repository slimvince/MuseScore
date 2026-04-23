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

#pragma once

#include <memory>

#include "modularity/ioc.h"

#include "composing/icomposinganalysisconfiguration.h"
#include "composing/icomposingchordstaffconfiguration.h"

#include "composing/analysis/chord/chordanalyzer.h"
#include "composing/analysis/key/keymodeanalyzer.h"

// ── IoC config accessors ──────────────────────────────────────────────────────

inline std::shared_ptr<mu::composing::IComposingAnalysisConfiguration> analysisConfig()
{
    return muse::modularity::globalIoc()->resolve<mu::composing::IComposingAnalysisConfiguration>("composing");
}

inline std::shared_ptr<mu::composing::IComposingChordStaffConfiguration> chordStaffConfig()
{
    return muse::modularity::globalIoc()->resolve<mu::composing::IComposingChordStaffConfiguration>("composing");
}

// ── Result construction ───────────────────────────────────────────────────────

/// Build a ChordAnalysisResult for a diatonic chord in C major (keyFifths=0,
/// Ionian).  degree: 0=I, 1=ii, 2=iii, 3=IV, 4=V, 5=vi, 6=viio.
inline mu::composing::analysis::ChordAnalysisResult diatonicResult(
    int degree, mu::composing::analysis::ChordQuality quality)
{
    static const int kIonianIntervals[7] = { 0, 2, 4, 5, 7, 9, 11 };
    mu::composing::analysis::ChordAnalysisResult r;
    r.identity.rootPc   = (kIonianIntervals[degree] + 0) % 12; // C major tonic = 0
    r.identity.bassPc   = r.identity.rootPc;
    r.identity.quality  = quality;
    r.function.degree   = degree;
    r.function.diatonicToKey = true;
    r.function.keyTonicPc   = 0;   // C
    r.function.keyMode  = mu::composing::analysis::KeySigMode::Ionian;
    return r;
}
