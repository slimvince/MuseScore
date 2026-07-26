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

// The joint estimator's EMBEDDED-artifact drift guard (ratified Decision D1). These are the
// standing establishment tests (#19) that the compiled-in table/weight data can NEVER silently
// diverge from the committed artifacts under tools/joint_estimator/: each embedded artifact's
// bytes must be byte-identical to (and sha256-equal to) its committed file, and the embedded
// SELECTED weight vector must be value-exact to decode_parity_ref.json's selected_weights. They
// also exercise the embedded-source loaders (JointTables::loadEmbedded / FittedAdapter::loadEmbedded)
// and confirm they produce the same loaded values as the filesystem loaders (#6, one parse path).

#include <fstream>
#include <sstream>
#include <string>

#include <gtest/gtest.h>

#include <QByteArray>
#include <QCryptographicHash>

#include "composing/analysis/joint/jointadapter.h"
#include "composing/analysis/joint/jointembeddedartifacts.h"
#include "composing/analysis/joint/jointtables.h"
#include "composing/analysis/joint/jointweights.h"

#include "serialization/json.h"
#include "types/bytearray.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;
namespace emb = mu::composing::analysis::joint::embedded;

namespace {
std::string readFileBytes(const std::string& path)
{
    std::ifstream f(path, std::ios::binary);
    std::ostringstream ss;
    ss << f.rdbuf();
    return ss.str();
}

// Normalize a checked-out file's bytes to the git-canonical LF form (.gitattributes `* text=auto`:
// CRLF -> LF). The embedded artifacts are stored in this canonical form (OI-195), so the guard
// establishes against the committed OBJECT content and is checkout-configuration-INDEPENDENT: on a
// CRLF checkout the raw working-tree bytes carry `\r\n`, but the canonical LF form does not.
// git converts CRLF only (a lone CR is left as-is), so a plain `\r\n` -> `\n` pass is exact.
std::string toCanonicalLf(const std::string& s)
{
    std::string out;
    out.reserve(s.size());
    for (std::size_t i = 0; i < s.size(); ++i) {
        if (s[i] == '\r' && i + 1 < s.size() && s[i + 1] == '\n') {
            continue;   // drop the CR of a CRLF pair
        }
        out.push_back(s[i]);
    }
    return out;
}

std::string sha256Hex(const std::string& bytes)
{
    const QByteArray in(bytes.data(), static_cast<int>(bytes.size()));
    return QCryptographicHash::hash(in, QCryptographicHash::Sha256).toHex().toStdString();
}

bool isLowerHex64(const std::string& s)
{
    if (s.size() != 64) {
        return false;
    }
    for (char c : s) {
        if (!((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f'))) {
            return false;
        }
    }
    return true;
}
} // namespace

// ── The drift guard: embedded bytes == committed files, and the published sha256 matches ───────

TEST(JointEmbeddedDriftGuard, EmbeddedArtifactsMatchCommittedBytesAndHashes)
{
    ASSERT_EQ(emb::kTableArtifacts.size(), 5u);
    for (const emb::EmbeddedBlob* b : emb::kTableArtifacts) {
        const std::string embedded = b->bytes();
        // The file side is normalized to the git-canonical LF form (OI-195), so the guard compares
        // the committed OBJECT content, not the checkout's line-ending configuration.
        const std::string file =
            toCanonicalLf(readFileBytes(std::string(JOINT_ARTIFACT_DIR) + "/" + b->name));
        ASSERT_FALSE(file.empty()) << "committed artifact not found: " << b->name;

        // byte-equality (strictly stronger than the sha256 the §2 provenance publishes): the
        // embedded data can never silently diverge from the committed artifact.
        EXPECT_EQ(embedded.size(), b->byteLen) << b->name;
        EXPECT_EQ(embedded, file) << b->name;

        // the published sha256 constant matches BOTH the embedded bytes and the committed file
        // (canonical LF form).
        ASSERT_TRUE(isLowerHex64(b->sha256)) << b->name;
        EXPECT_EQ(sha256Hex(embedded), std::string(b->sha256)) << b->name;
        EXPECT_EQ(sha256Hex(file), std::string(b->sha256)) << b->name;
    }
}

TEST(JointEmbeddedDriftGuard, SelectedWeightsValueExactVsParityRef)
{
    // The embedded selected vector's committed source is decode_parity_ref.json's selected_weights.
    const std::string refBytes =
        readFileBytes(std::string(JOINT_ARTIFACT_DIR) + "/decode_parity_ref.json");
    ASSERT_FALSE(refBytes.empty());
    std::string jerr;
    const muse::ByteArray ba(refBytes.data(), refBytes.size());
    const muse::JsonObject ref = muse::JsonDocument::fromJson(ba, &jerr).rootObject();
    ASSERT_TRUE(jerr.empty()) << jerr;
    const muse::JsonObject sel = ref.value("selected_weights").toObject();

    const joint::WeightVector w = joint::selectedWeights();
    for (const std::string& n : joint::kWeightNames) {
        // bit-exact (value-exact): the embedded snippet parses to the same double as the file.
        EXPECT_EQ(w.get(n), sel.value(n).toDouble()) << n;
    }
    EXPECT_EQ(std::string(emb::kWeightVectorIdentity), "random07");
    EXPECT_EQ(std::string(ref.value("provenance").toObject().value("selected_start").toStdString()),
              "random07");
}

// ── The embedded loaders produce the same loaded values as the filesystem loaders (#6) ─────────

TEST(JointEmbeddedLoad, TablesMatchFileLoad)
{
    const joint::JointTables fromFile = joint::JointTables::load(JOINT_ARTIFACT_DIR, "all");
    const joint::JointTables fromEmbed = joint::JointTables::loadEmbedded("all");
    ASSERT_TRUE(fromFile.loaded) << fromFile.error;
    ASSERT_TRUE(fromEmbed.loaded) << fromEmbed.error;

    EXPECT_EQ(fromEmbed.tableSet, "all");
    EXPECT_EQ(fromEmbed.corpusGitHash, fromFile.corpusGitHash);

    // flat distributions compare element-wise (bit-exact doubles).
    EXPECT_EQ(fromEmbed.t2, fromFile.t2);
    EXPECT_EQ(fromEmbed.t3, fromFile.t3);
    EXPECT_EQ(fromEmbed.boundaryProb, fromFile.boundaryProb);
    EXPECT_EQ(fromEmbed.factorAbsent, fromFile.factorAbsent);

    // Katz tables: sizes + a spot cell (no operator== on KatzTable).
    EXPECT_EQ(fromEmbed.t1Major.rows.size(), fromFile.t1Major.rows.size());
    EXPECT_EQ(fromEmbed.t1Minor.rows.size(), fromFile.t1Minor.rows.size());
    ASSERT_TRUE(fromEmbed.t1Major.rows.count("I | Maj |  | "));
    EXPECT_DOUBLE_EQ(fromEmbed.t1Major.rows.at("I | Maj |  | ").dist.at("BASE"),
                     fromFile.t1Major.rows.at("I | Maj |  | ").dist.at("BASE"));
    EXPECT_EQ(fromEmbed.t4.rows.size(), fromFile.t4.rows.size());
    EXPECT_EQ(fromEmbed.spelling.at("major"), fromFile.spelling.at("major"));
}

TEST(JointEmbeddedLoad, AdapterLoadsEmbedded)
{
    const joint::FittedAdapter a = joint::FittedAdapter::loadEmbedded(joint::selectedWeights());
    ASSERT_TRUE(a.loaded()) << a.error();
    EXPECT_EQ(a.corpusGitHash(), "57ed94a6a46571172a351c09ba4f5cb92930674a");
    // the selected vector reached the adapter (declared_mode is 1.0 in the direct-metric fit).
    EXPECT_DOUBLE_EQ(a.weights().get("declared_mode"), 1.0);
}

TEST(JointEmbeddedLoad, LoadEmbeddedRejectsNonAllTableSet)
{
    const joint::JointTables t = joint::JointTables::loadEmbedded("fold0");
    EXPECT_FALSE(t.loaded);
    EXPECT_FALSE(t.error.empty());
}

// ── The §2 provenance constants (declared dormancy — the notation record build consumes them) ──

TEST(JointEmbeddedProvenance, ConstantsWellFormed)
{
    EXPECT_EQ(std::string(emb::kCorpusGitHash), "57ed94a6a46571172a351c09ba4f5cb92930674a");
    EXPECT_FALSE(std::string(emb::kDecoderVersion).empty());
    EXPECT_EQ(std::string(emb::kWeightVectorIdentity), "random07");

    // artifact names + hashes are populated and well-formed.
    EXPECT_EQ(emb::kTablesAll.name, std::string("tables_all.json"));
    EXPECT_EQ(emb::kModeMarginal.name, std::string("mode_marginal.json"));
    for (const emb::EmbeddedBlob* b : emb::kTableArtifacts) {
        EXPECT_TRUE(isLowerHex64(b->sha256)) << b->name;
        EXPECT_GT(b->byteLen, 0u) << b->name;
    }
}
