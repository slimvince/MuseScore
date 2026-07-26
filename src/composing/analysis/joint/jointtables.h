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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTTABLES_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTTABLES_H

#include <string>
#include <unordered_map>

// Runtime loader for the joint estimator's committed generative tables. The frozen tables
// (fit once from ground-truth counts, per the ratified staged fitting) are LOADED AT
// RUNTIME from the committed JSON artifacts under tools/joint_estimator/ — production
// packaging is an adoption-time question, not this build's. This module holds ONLY the
// loaded values; the factor log-probability queries over them (the decoder's Adapter) are
// a separate component.
//
// The four committed artifacts read here (the "all-326" publishable set; the fold sets
// share the schema, selected by tableSet = "fold{i}"):
//   tables_all.json               table1..table5 (chord/key/entry/bass transition + prior)
//   note_tables_all.json          emission / spelling / boundary
//   factor_presence_all.json      the missing-template-tone (absence) table
//   fermata_boundary_addendum.json the boundary factor's fermata-crossed cells
//
// Source of truth for the schema and every query: probe_decoder.FittedAdapter
// (tools/joint_estimator/probe_decoder.py). This module is DORMANT — no production path
// reads it. Spec: cowork_joint_estimator_factorization.md §2/§3.

namespace mu::composing::analysis::joint {
/// A distribution over outcome-key strings (an outcome class-key, a figure, or a pooled
/// bucket sigil such as BASE / «invfree» / mode:M).
using Dist = std::unordered_map<std::string, double>;

/// One fitted transition-table row: the back-off level it was fit at, and its
/// distribution over outcomes.
struct KatzRow {
    std::string contextUsed;
    Dist dist;
};

/// A Katz-backed table (table1 per mode, table4, emission): a display-key -> row map plus
/// the derived context_used -> dist back-off map (probe_decoder builds it with setdefault,
/// first-wins; every context_used maps to a unique dist, so the map is order-independent).
struct KatzTable {
    std::unordered_map<std::string, KatzRow> rows;
    std::unordered_map<std::string, Dist> levels;
};

/// A boundary-factor cell (fermata-crossed): its probability and whether its own training
/// count cleared the reliability threshold. `present` is false when the cell is absent.
struct BoundaryCell {
    bool present = false;
    bool reliable = false;
    double prob = 0.0;
};

class JointTables
{
public:
    /// Load the committed tables from `artifactDir` for the given table set ("all" or
    /// "fold0".."fold4"). On any failure `loaded` is false and `error` describes it; the
    /// caller must check `loaded` before use.
    static JointTables load(const std::string& artifactDir, const std::string& tableSet = "all");

    /// Load the tables from the compiled-in embedded artifacts (ratified Decision D1) — the
    /// PRODUCTION source, provenance-locked at build time (#16/#19). Only the "all" table set
    /// is embedded; any other `tableSet` sets `error` and leaves `loaded` false. Parses the
    /// SAME bytes through the SAME parser as load() (#6, one parse path).
    static JointTables loadEmbedded(const std::string& tableSet = "all");

    bool loaded = false;
    std::string error;

    // provenance
    std::string corpusGitHash;      ///< tables_all.json provenance.corpus_git_hash
    std::string tableSet;

    // table 1 — same-key chord transition, per mode
    KatzTable t1Major;
    KatzTable t1Minor;
    // table 2 — key transition (flat cell -> prob)
    Dist t2;
    // table 3 — entry chord at a key change / initial segment (flat cell -> prob)
    Dist t3;
    // table 4 — bass / inversion
    KatzTable t4;
    // table 5 — signature / declared-mode prior, keyed by declared mode "major"/"minor"/"none"
    std::unordered_map<std::string, Dist> t5;

    // note tables
    KatzTable emission;                                   ///< emission_category_by_covariate
    std::unordered_map<std::string, Dist> spelling;       ///< "major"/"minor" -> spelling dist
    std::unordered_map<std::string, double> boundaryProb; ///< beat_class -> P(boundary)

    // factor presence (the PRIMARY 'overlap' mode): "role|family" -> P(absent) smoothed
    std::unordered_map<std::string, double> factorAbsent;

    // fermata-crossed boundary cells: beat_class -> cell, split by fermata context
    std::unordered_map<std::string, BoundaryCell> fermBoundaryFerm;
    std::unordered_map<std::string, BoundaryCell> fermBoundaryNoFerm;
};
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTTABLES_H
