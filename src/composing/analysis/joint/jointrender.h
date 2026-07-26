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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTRENDER_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTRENDER_H

#include <optional>
#include <string>

#include "labelclass.h"

// The joint estimator's PRESENTATION-DERIVATION primitives — the display strings derived from the
// module's own decode output (the ratified derived-published-fact family: computed once here,
// consumers read; #6 one path per concern). These are the C++ port of the fit-layer's own
// rendering functions:
//   jointOursQuality  = probe_run._QUAL_STR   (joint quality -> the coarse grading quality string)
//   jointChordSymbol  = jointprimitives::pcKeyName + the class quality (the chord-symbol string)
//   jointRenderRn     = probe_run.render_rn    (a When-in-Rome-style Roman numeral)
// They are pure functions of their arguments (no score, no table read). SINGLE SOURCE: both the
// batch render (tools/batch_analyze --joint-inference) and the notation record (§3.2 derived chord
// facts) read them — there is no second copy (the notation output-surface contract §5.6 formatter
// continuity requires the record's chord-symbol/Roman strings reproduce the batch render's forms
// by being the same derivation). The pc->spelling map itself lives once in jointprimitives::pcKeyName.
//
// Spec: cowork_notation_output_contract.md §3.2 (derived chord facts) + §5.6 (formatter continuity);
// probe_run.py / probe_decoder.py.

namespace mu::composing::analysis::joint {

/// probe_run._QUAL_STR: the joint chord quality -> the coarse .ours.json quality string a8/compare_rn
/// grades ("Major"/"Minor"/"Diminished"/"HalfDiminished"/"Augmented"). An unknown quality -> "Unknown".
std::string jointOursQuality(const std::string& quality);

/// The chord-symbol string: the root's canonical pc name (jointPcKeyName) followed by the class's own
/// (fine-grained) quality string — e.g. root pc 7 + "Maj7" -> "GMaj7". Empty when the class has no
/// defined root (a chromatic AugSixth/Neapolitan class whose chordFactorPcs leaves it rootless).
std::string jointChordSymbol(std::optional<int> rootPc, const std::string& quality);

/// probe_run.render_rn: a When-in-Rome-style Roman numeral from the (inversion-free) class + the
/// derived bass role and a hasSeventh flag. `bassRole` is empty when the bass is not a chord factor
/// (Python .get default ""); an empty role leaves the figured-bass suffix empty. Lower-cases the
/// degree for minor-colored qualities, adds the quality sigil (o/ø/+), the figured-bass figure from
/// (bassRole, hasSeventh), and the applied "/target" suffix.
std::string jointRenderRn(const LabelClass& cls, const std::string& bassRole, bool hasSeventh);

} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTRENDER_H
