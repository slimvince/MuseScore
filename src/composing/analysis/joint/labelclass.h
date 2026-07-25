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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_LABELCLASS_H
#define MU_COMPOSING_ANALYSIS_JOINT_LABELCLASS_H

#include <string>

// The joint estimator's chord-class value type — the C++ decode-side port of
// normalize.LabelClass (tools/joint_estimator/normalize.py). The estimator's chord STATE
// and every table key is this class, serialized by key(). It reproduces key(),
// inversionFree(), family(), the isSeventhQuality() predicate, and the classFromKey()
// inverse (probe_decoder.class_from_key). It does NOT re-derive a class from a raw
// When-in-Rome label — that fit-time normalization (normalize.normalize_label, which
// parses WiR figures) stays in Python; the committed tables are already keyed with
// normalized class-key strings, and this module only PARSES those keys back and RENDERS
// them, never fits them.
//
// Dispatch: the joint-estimator C++ module build (OI-180 sanction). This module is
// DORMANT — no production path reads it. Spec: cowork_joint_estimator_factorization.md §1.

namespace mu::composing::analysis::joint {
class LabelClass
{
public:
    LabelClass() = default;
    LabelClass(std::string degreeBase, std::string quality, std::string inversion,
               std::string target, bool rawUnnormalized = false);

    const std::string& degreeBase() const { return m_degreeBase; }
    const std::string& quality() const { return m_quality; }
    const std::string& inversion() const { return m_inversion; }
    const std::string& target() const { return m_target; }
    bool rawUnnormalized() const { return m_rawUnnormalized; }

    /// "degree | quality | inversion | target"  (LabelClass.key()) — the table-key form.
    std::string key() const;

    /// The class with the inversion figure dropped (LabelClass.inversion_free()): the
    /// declared parent for the entry / transition back-off chains.
    LabelClass inversionFree() const;

    /// The class with quality reduced to the triad/seventh FAMILY, inversion dropped
    /// (LabelClass.family()): the coarser transition back-off level.
    LabelClass family() const;

    bool operator==(const LabelClass& o) const;
    bool operator!=(const LabelClass& o) const { return !(*this == o); }

private:
    std::string m_degreeBase;
    std::string m_quality;
    std::string m_inversion;
    std::string m_target;
    bool m_rawUnnormalized = false;
};

/// True iff a quality string is one of the eight seventh qualities
/// (normalize._SEVENTH_QUALITIES).
bool isSeventhQuality(const std::string& quality);

/// Parse a stored class KEY back to a LabelClass (probe_decoder.class_from_key): split on
/// " | ", padding to four fields (key() is the inverse). Matches the Python constructor,
/// which leaves rawUnnormalized at its default (false).
LabelClass classFromKey(const std::string& key);
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_LABELCLASS_H
