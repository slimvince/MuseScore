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

// Joint estimator — the ROOT/BASS TONAL SPELLING derivation (notation output-surface contract §3.2 /
// §5.2) coverage tests for joint::rootSpellingLof / joint::factorSpellingLof. Hand-derived cases
// across modes, applied (secondary) classes, and the chromatic families (Neapolitan / augmented-sixth),
// plus a corpus PC-CONSISTENCY check: every derived root spelling's pitch class equals the decoder's
// committed root pc (the internal-consistency half of the §5.2 establishment; the corpus-vs-notation
// half is tools/joint_estimator/gen_spelling_establishment.py). Line-of-fifths convention: C=0.

#include <gtest/gtest.h>

#include <memory>
#include <optional>
#include <string>

#include "composing/analysis/joint/jointprimitives.h"
#include "composing/analysis/joint/jointdecoder.h"
#include "composing/analysis/joint/jointadapter.h"
#include "composing/analysis/joint/jointweights.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

namespace {
std::optional<int> rootLof(const std::string& classKey, int tonic, bool isMajor, int ref)
{
    return joint::rootSpellingLof(joint::classFromKey(classKey), tonic, isMajor, ref);
}
int pcOf(int lof) { return ((7 * lof) % 12 + 12) % 12; }
} // namespace

// ── root spelling: diatonic degrees across both modes ─────────────────────────────────────────────
TEST(JointSpellingTests, RootDiatonicDegrees)
{
    // C major (tonic 0, ref 0)
    EXPECT_EQ(rootLof("I | Maj |  | ", 0, true, 0), 0);     // C
    EXPECT_EQ(rootLof("V | Dom7 |  | ", 0, true, 0), 1);    // G
    EXPECT_EQ(rootLof("IV | Maj |  | ", 0, true, 0), -1);   // F
    EXPECT_EQ(rootLof("VI | Min |  | ", 0, true, 0), 3);    // A
    EXPECT_EQ(rootLof("II | Min7 |  | ", 0, true, 0), 2);   // D
    // A minor (tonic 9, ref 0)
    EXPECT_EQ(rootLof("I | Min |  | ", 9, false, 0), 3);    // A
    EXPECT_EQ(rootLof("V | Maj |  | ", 9, false, 0), 4);    // E
    EXPECT_EQ(rootLof("III | Maj |  | ", 9, false, 0), 0);  // C (♭3 mediant)
    EXPECT_EQ(rootLof("VII | Maj |  | ", 9, false, 0), 1);  // G (natural subtonic ♭7)
    // A minor diminished degrees take the RAISED 6th/7th (harmonic/melodic minor), not the naturals
    EXPECT_EQ(rootLof("VII | Dim7 |  | ", 9, false, 0), 8); // G# (raised leading tone)
    EXPECT_EQ(rootLof("VI | Dim |  | ", 9, false, 0), 6);   // F# (raised submediant)
}

// ── root spelling: chromatically-altered + chromatic-family classes ───────────────────────────────
TEST(JointSpellingTests, RootChromaticClasses)
{
    // ♭VII major-seventh in C major -> Bb (lof -2), a borrowed lowered seventh
    EXPECT_EQ(rootLof("bVII | Maj7 |  | ", 0, true, 0), -2);   // Bb
    // Neapolitan in C major -> Db (♭2 spelling, lof -5)
    EXPECT_EQ(rootLof("N | Neapolitan |  | ", 0, true, 0), -5);   // Db
    // augmented-sixth in C major -> the framework tonic C (lof 0)
    EXPECT_EQ(rootLof("It | AugSixth |  | ", 0, true, 0), 0);     // C
    // in A minor the Neapolitan -> Bb (♭2 of A, lof -2... A lof 3, ♭2 = Bb lof -2)
    EXPECT_EQ(rootLof("N | Neapolitan |  | ", 9, false, 0), -2);  // Bb
}

// ── root spelling: applied (secondary) classes tonicize their target ──────────────────────────────
TEST(JointSpellingTests, RootAppliedClasses)
{
    // V/V in C major -> D major, root D (lof +2)
    EXPECT_EQ(rootLof("V | Dom7 |  | V", 0, true, 0), 2);   // D
    // V/vi in C major -> E major, root E (lof +4)
    EXPECT_EQ(rootLof("V | Dom7 |  | vi", 0, true, 0), 4);  // E
    // vii°7/V in C major -> leading tone of G = F# (lof +6)
    EXPECT_EQ(rootLof("VII | Dim7 |  | V", 0, true, 0), 6); // F#
    // V/ii in C major -> A major, root A (lof +3)
    EXPECT_EQ(rootLof("V | Dom7 |  | ii", 0, true, 0), 3);  // A
}

// ── the derived root pc equals the committed root pc (internal consistency, all hand cases) ───────
TEST(JointSpellingTests, RootPcMatchesDecoderRoot)
{
    joint::ChordCache cache;
    struct Case { const char* ck; int tonic; bool major; };
    const Case cases[] = {
        { "I | Maj |  | ", 0, true }, { "V | Dom7 |  | ", 0, true }, { "bVII | Maj7 |  | ", 0, true },
        { "VII | Dim7 |  | ", 9, false }, { "V | Dom7 |  | V", 0, true }, { "N | Neapolitan |  | ", 0, true },
        { "It | AugSixth |  | ", 0, true }, { "III | Maj |  | ", 9, false },
    };
    for (const Case& c : cases) {
        const joint::LabelClass cls = joint::classFromKey(c.ck);
        const std::optional<int> lof = joint::rootSpellingLof(cls, c.tonic, c.major, 0);
        const joint::ChordInfo& info = cache.get(cls, c.tonic, c.major);
        ASSERT_TRUE(lof.has_value()) << c.ck;
        ASSERT_TRUE(info.root.has_value()) << c.ck;
        EXPECT_EQ(pcOf(*lof), *info.root) << c.ck << " derived-spelling pc != decoder root pc";
    }
}

// ── factor spelling: the tertian intervals per quality ────────────────────────────────────────────
TEST(JointSpellingTests, FactorSpellings)
{
    // root C (lof 0, pc 0)
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 0), 0);    // root (unison)  -> C
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 4), 4);    // M3  -> E
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 3), -3);   // m3  -> Eb
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 7), 1);    // P5  -> G
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 6), -6);   // d5  -> Gb
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 8), 8);    // A5  -> G#
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 10), -2);  // m7  -> Bb
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 11), 5);   // M7  -> B
    EXPECT_EQ(joint::factorSpellingLof(0, 0, 9), -9);   // d7  -> Bbb
    // a non-tertian interval (major second) is not a chord factor -> none
    EXPECT_FALSE(joint::factorSpellingLof(0, 0, 2).has_value());
    // relative to a non-C root: D dim triad, fifth Ab (d5) -> Ab (lof -4)
    EXPECT_EQ(joint::factorSpellingLof(2, 2, 8), -4);   // rootLof 2 (D), fifth pc 8 -> Ab
}

// ── corpus pc-consistency: every decoded segment's derived root spelling pc == committed root pc ──
TEST(JointSpellingTests, CorpusRootPcConsistency)
{
    const std::string dir = JOINT_ARTIFACT_DIR;
    joint::LoadedCorpus corpus = joint::loadPiecesFromNoteEvents(dir + "/note_events/note_events.json");
    ASSERT_TRUE(corpus.ok);
    joint::FittedAdapter adapter = joint::FittedAdapter::loadEmbedded(joint::selectedWeights());
    ASSERT_TRUE(adapter.loaded());
    joint::Vocabulary vocab(adapter.tables());
    joint::ChordCache cache;

    int checked = 0;
    for (const std::string& stem : { std::string("bwv324"), std::string("bwv362"),
                                     std::string("bwv10.7") }) {
        ASSERT_TRUE(corpus.pieces.count(stem)) << stem;
        joint::Piece& piece = corpus.pieces.at(stem);
        const joint::DecodeResult r = joint::decodePiece(piece, adapter, vocab, cache, 4,
                                                         std::optional<int>(0), "");
        for (const joint::SegmentSummary& s : r.segments) {
            const joint::LabelClass cls = joint::classFromKey(s.classKey);
            const std::optional<int> lof = joint::rootSpellingLof(cls, s.tonicPc, s.isMajor, 0);
            if (!lof.has_value() || !s.rootPc.has_value()) {
                continue;
            }
            EXPECT_EQ(pcOf(*lof), *s.rootPc)
                << stem << " @" << s.startTick << " class " << s.classKey;
            ++checked;
        }
    }
    EXPECT_GT(checked, 0);
}
