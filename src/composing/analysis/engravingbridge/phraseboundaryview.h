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

// ── composing/analysis/engravingbridge — the owned phrase-boundary primitive ──
//
// Architectural Layer 1.5 (the notation-derived views): the SINGLE place that
// reads, from the notated surface alone, where a musical phrase ends. It lives
// beside the other Layer-1.5 views (spellingview / soundingAt / weightedPcView /
// pitchContextOverSpan), NOT inside an analysis layer, so every consumer of the
// per-region "ends a phrase" signal reads one owned primitive — never a per-site
// copy (the unification rule). Notation-only: key-, chord-, and function-agnostic
// by construction (the function layer's cadence detection CONSUMES phrase
// boundaries, so a boundary that depended on cadence would be circular).
//
// Spec: cowork_phrase_boundary_design.md (SIGNED). Build: the two-step plan in
// cc_instruction_phrase_boundary_build.md.
//
//   • STEP A (this revision) — DE-DUPLICATION, byte-identical. This primitive
//     retires the two hand-synchronised fermata scans that existed before it
//     (regionanalyzer.cpp jkdPhraseBoundaryTicks + tools/batch_analyze.cpp
//     collectPhraseBoundaryTicks) into one owner. The DEFINITION is unchanged
//     here (fermata-only), so every consumer's output is byte-identical.
//   • STEP B (next) — replaces the fermata-only definition with the graded
//     surface-cue + notated-marker model (design §4: per-voice gap/inter-onset/
//     pitch-interval local-change cues, aggregated to a texture profile, plus
//     deterministic marker spikes, then peak-picking) WITHOUT changing this
//     signature or its consumers.
//
// CONSUMER STATUS (build §1 enumeration): every "ends a phrase" consumer is
// dormant or gated-off on the production path today — the joint-key re-key pass
// (regionanalyzer applyJointKeyWiring, gated on jointKeyWiringEnabled(), default
// OFF) and the batch_analyze --dump-cadence-anchor/--dump-modulation/
// --dump-joint-key diagnostics. So the graded Step-B definition is byte-identical
// on production; the strength becomes load-bearing only when the function layer
// (Layer 5) engages.

#include <set>

namespace mu::engraving {
class Score;
}

namespace mu::composing::analysis::engravingbridge {

/// The picked phrase-boundary ticks of @p score — the onset ticks at which a
/// phrase's sounding ends. The single owned source the (currently dormant/gated)
/// "ends a phrase" consumers read.
///
/// STEP A — fermata-only: the tick of every chord-rest segment carrying a
/// fermata on any annotation, read off the engraved notation (no key/function).
/// Byte-identical to the two retired hand-synced scans. Returns an empty set for
/// a null score.
std::set<int> phraseBoundaryTicks(const mu::engraving::Score* score);

} // namespace mu::composing::analysis::engravingbridge
