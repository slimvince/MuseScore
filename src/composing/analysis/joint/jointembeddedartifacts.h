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

// ★ GENERATED FILE — DO NOT EDIT BY HAND.
// Produced by tools/joint_estimator/gen_embedded_tables.py from the committed fitted
// artifacts under tools/joint_estimator/ (ratified Decision D1). Regenerate with:
//     python tools/joint_estimator/gen_embedded_tables.py
//
// The five table artifacts + the SELECTED weight vector are embedded VERBATIM (JSON
// bytes, not a parsed-structure codegen) and parsed at load through the SAME parser as
// the filesystem path (#6). The embedded bytes are the GIT-CANONICAL LF form
// (.gitattributes `* text=auto`; CRLF -> LF), so the generated source and the drift
// guard are checkout-configuration-INDEPENDENT (OI-195): the guard normalizes the
// checked-out file's line endings to LF before comparing. Establishment = byte equality
// vs the committed artifacts (the joint_embedded_tests drift guard). Source corpus: 57ed94a6a46571172a351c09ba4f5cb92930674a.

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTEMBEDDEDARTIFACTS_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTEMBEDDEDARTIFACTS_H

#include <array>
#include <cstddef>
#include <string>

namespace mu::composing::analysis::joint::embedded {
/// One embedded artifact: the committed file's bytes stored VERBATIM as compiled-in
/// C-string chunks (JSON text carries no NUL byte, so each chunk is NUL-terminated and
/// its length is strlen; bytes() concatenates them into the exact file bytes). `sha256`
/// is the lowercase-hex digest of those verbatim bytes (== the committed file's
/// git-canonical LF digest, OI-195).
struct EmbeddedBlob {
    const char* const* chunks;
    std::size_t chunkCount;
    std::size_t byteLen;   ///< total verbatim byte length
    const char* sha256;    ///< lowercase-hex sha256 of the verbatim bytes
    const char* name;      ///< source artifact name

    std::string bytes() const;   ///< reconstruct the verbatim file bytes
};

// ── the five committed table artifacts (verbatim) ────────────────────────────────────
extern const EmbeddedBlob kTablesAll;
extern const EmbeddedBlob kNoteTablesAll;
extern const EmbeddedBlob kFactorPresenceAll;
extern const EmbeddedBlob kFermataBoundaryAddendum;
extern const EmbeddedBlob kModeMarginal;

/// The five table artifacts, for the drift guard.
extern const std::array<const EmbeddedBlob*, 5> kTableArtifacts;

/// The direct-metric SELECTED weight vector (probe_decoder selected_start 'random07'),
/// extracted from decode_parity_ref.json's selected_weights and embedded VERBATIM as a
/// JSON snippet in WEIGHT_NAMES order; parsed at load by joint::selectedWeights().
extern const EmbeddedBlob kSelectedWeightsJson;

// ── §2 provenance constants (published on the notation output-surface record). ────────
// DECLARED DORMANCY (fact-publication corollary): their named consumer is the notation
// record build (a later dispatch); nothing reads them yet.
extern const char* const kWeightVectorIdentity;   ///< "random07"
extern const char* const kDecoderVersion;         ///< the joint decoder's own version
extern const char* const kCorpusGitHash;          ///< source corpus (tables_all provenance)
extern const char* const kGeneratedBy;            ///< the generating instrument
} // namespace mu::composing::analysis::joint::embedded

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTEMBEDDEDARTIFACTS_H
