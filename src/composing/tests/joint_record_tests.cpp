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

// Joint estimator — the NOTATION OUTPUT-SURFACE RECORD (contract §3.1–§3.3) coverage tests for
// joint::assembleNotationRecord and its derived-fact primitives. Every derived fact is checked against
// INDEPENDENTLY-STATED expectations (a test-local recomputation, never the code under test), the
// provenance block against the compiled-in embedded constants, and the augmented-sixth sub-type on
// constructed sounding-content cases. The decode uses the compiled-in EMBEDDED tables (the production
// source). The module stays DORMANT — nothing in src/ reads the record.

#include <gtest/gtest.h>

#include <array>
#include <memory>
#include <optional>
#include <string>
#include <vector>

#include "composing/analysis/joint/jointnotationrecord.h"
#include "composing/analysis/joint/jointembeddedartifacts.h"
#include "composing/analysis/joint/jointweights.h"

#ifndef JOINT_ARTIFACT_DIR
#define JOINT_ARTIFACT_DIR "."
#endif

namespace joint = mu::composing::analysis::joint;

namespace {
// INDEPENDENT test oracles (deliberately NOT the code-under-test's primitives).

// pc -> fewest-accidental spelling (an independent copy for the chord-symbol expectation).
const char* const kPcName[12] = { "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B" };

// Independent (tonic, major/minor) -> signature-fifths, reference-nearest enharmonic. Hand table.
int expectFifths(int tonicPc, bool isMajor, int ref)
{
    // relative-major Ionian pc: major -> tonic; minor -> tonic + 3.
    const int ip = (((isMajor ? tonicPc : tonicPc + 3) % 12) + 12) % 12;
    static const int prim[12] = { 0, 7, 2, -3, 4, -1, 6, 1, -4, 3, -2, 5 };
    static const int alt[12]  = { 0, -5, 2, -3, 4, -1, -6, 1, -4, 3, -2, -7 };
    return (std::abs(prim[ip] - ref) <= std::abs(alt[ip] - ref)) ? prim[ip] : alt[ip];
}

// Independent diatonicToKey rule.
bool expectDiatonic(const joint::LabelClass& c)
{
    if (!c.target().empty()) {
        return false;
    }
    if (c.quality() == "AugSixth" || c.quality() == "Neapolitan") {
        return false;
    }
    const std::string& d = c.degreeBase();
    if (!d.empty() && (d[0] == 'b' || d[0] == '#')) {
        return false;
    }
    return true;
}

struct Fixture {
    joint::LoadedCorpus corpus;
    joint::FittedAdapter adapter;       // embedded tables + the SELECTED (production) weights
    std::unique_ptr<joint::Vocabulary> vocab;
    joint::ChordCache cache;
    bool ok = false;
};

Fixture load()
{
    Fixture f;
    const std::string dir = JOINT_ARTIFACT_DIR;
    f.corpus = joint::loadPiecesFromNoteEvents(dir + "/note_events/note_events.json");
    if (!f.corpus.ok) {
        return f;
    }
    f.adapter = joint::FittedAdapter::loadEmbedded(joint::selectedWeights());
    if (!f.adapter.loaded()) {
        return f;
    }
    f.vocab = std::make_unique<joint::Vocabulary>(f.adapter.tables());
    f.ok = true;
    return f;
}

// Build a one-event Piece whose notes sound exactly `pcs` (each pc a note over [0, dur)); `midis`
// gives the midi of each note so the bass is well-defined. measure=1 (non-anacrusis).
joint::Piece onEventPiece(const std::vector<int>& pcs, const std::vector<int>& midis, int dur = 480)
{
    joint::Piece p;
    p.stem = "synthetic";
    p.nQuarter = 4;
    joint::EventRec ev;
    ev.start = 0;
    ev.end = dur;
    ev.measure = 1;
    ev.beat = 1.0;
    p.events.push_back(ev);
    for (size_t k = 0; k < pcs.size(); ++k) {
        joint::NoteRec n;
        n.onset = 0;
        n.dur = dur;
        n.pc = pcs[k];
        n.midi = midis[k];
        n.measure = 1;
        p.notes.push_back(n);
    }
    p.prepare();
    return p;
}
} // namespace

// ── §3.2 derived: the key-signature-fifths mapping (hand cases) ───────────────────────────────────
TEST(JointRecordTests, KeySignatureFifthsMapping)
{
    // unambiguous majors/minors (reference 0)
    EXPECT_EQ(joint::recordKeySignatureFifths(0, true, 0), 0);    // C major
    EXPECT_EQ(joint::recordKeySignatureFifths(7, true, 0), 1);    // G major
    EXPECT_EQ(joint::recordKeySignatureFifths(5, true, 0), -1);   // F major
    EXPECT_EQ(joint::recordKeySignatureFifths(2, true, 0), 2);    // D major
    EXPECT_EQ(joint::recordKeySignatureFifths(9, false, 0), 0);   // A minor -> C major sig 0
    EXPECT_EQ(joint::recordKeySignatureFifths(2, false, 0), -1);  // D minor -> F major sig -1
    EXPECT_EQ(joint::recordKeySignatureFifths(4, false, 0), 1);   // E minor -> G major sig 1
    // enharmonic pairs resolved by the reference
    EXPECT_EQ(joint::recordKeySignatureFifths(6, true, 6), 6);    // F# major (sharp ref)
    EXPECT_EQ(joint::recordKeySignatureFifths(6, true, -6), -6);  // Gb major (flat ref)
    EXPECT_EQ(joint::recordKeySignatureFifths(1, true, 7), 7);    // C# major (sharp ref)
    EXPECT_EQ(joint::recordKeySignatureFifths(1, true, -5), -5);  // Db major (flat ref)
    EXPECT_EQ(joint::recordKeySignatureFifths(11, true, 5), 5);   // B major (sharp ref)
    EXPECT_EQ(joint::recordKeySignatureFifths(11, true, -7), -7); // Cb major (flat ref)
}

// ── §3.2 derived: the class-native diatonicToKey rule (hand cases) ────────────────────────────────
TEST(JointRecordTests, DiatonicToKeyRule)
{
    EXPECT_TRUE(joint::recordDiatonicToKey(joint::classFromKey("I | Maj |  | ")));
    EXPECT_TRUE(joint::recordDiatonicToKey(joint::classFromKey("V | Dom7 |  | ")));
    EXPECT_TRUE(joint::recordDiatonicToKey(joint::classFromKey("VII | Dim7 |  | ")));  // minor leading-tone dim
    EXPECT_TRUE(joint::recordDiatonicToKey(joint::classFromKey("II | Min7 |  | ")));
    // applied / secondary -> chromatic
    EXPECT_FALSE(joint::recordDiatonicToKey(joint::classFromKey("V | Dom7 |  | V")));  // V/V
    EXPECT_FALSE(joint::recordDiatonicToKey(joint::classFromKey("VII | Dim7 |  | ii")));
    // chromatically-altered degree
    EXPECT_FALSE(joint::recordDiatonicToKey(joint::classFromKey("bVII | Maj7 |  | ")));
    // chromatic predefined families
    EXPECT_FALSE(joint::recordDiatonicToKey(joint::classFromKey("It | AugSixth |  | ")));
    EXPECT_FALSE(joint::recordDiatonicToKey(joint::classFromKey("N | Neapolitan |  | ")));
}

// ── §3.2 derived: the augmented-sixth sub-type from the sounding content (constructed cases) ──────
TEST(JointRecordTests, AugSixthSubTypeFromSoundingContent)
{
    // tonic C (pc 0). ♭6̂=8 (Ab), ♯4̂=6 (F#), 1̂=0. German adds ♭3̂=3 (Eb); French adds 2̂=2 (D).
    const joint::Piece it = onEventPiece({ 8, 0, 6 }, { 56, 60, 66 });          // Italian
    EXPECT_EQ(joint::recordAugSixthSubType(it, 0, 1, 0), "Italian");
    const joint::Piece ger = onEventPiece({ 8, 0, 3, 6 }, { 56, 60, 63, 66 });  // German (adds Eb)
    EXPECT_EQ(joint::recordAugSixthSubType(ger, 0, 1, 0), "German");
    const joint::Piece fr = onEventPiece({ 8, 0, 2, 6 }, { 56, 60, 62, 66 });   // French (adds D)
    EXPECT_EQ(joint::recordAugSixthSubType(fr, 0, 1, 0), "French");
    // a different tonic (D=2): ♭6̂=10 (Bb), ♯4̂=8 (Ab/G#), 1̂=2; German ♭3̂=5 (F); French 2̂=4 (E).
    const joint::Piece gerD = onEventPiece({ 10, 2, 5, 8 }, { 58, 62, 65, 68 });
    EXPECT_EQ(joint::recordAugSixthSubType(gerD, 0, 1, 2), "German");
    const joint::Piece frD = onEventPiece({ 10, 2, 4, 8 }, { 58, 62, 64, 68 });
    EXPECT_EQ(joint::recordAugSixthSubType(frD, 0, 1, 2), "French");
}

// ── §2 provenance: the block equals the compiled-in embedded constants ────────────────────────────
TEST(JointRecordTests, ProvenanceBlockMatchesEmbeddedConstants)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok) << "corpus/adapter load failed";
    ASSERT_TRUE(f.corpus.pieces.count("bwv324"));
    joint::Piece& piece = f.corpus.pieces.at("bwv324");
    const joint::DecodeResult r = joint::decodePiece(piece, f.adapter, *f.vocab, f.cache, 4,
                                                     std::optional<int>(0), "");
    const joint::NotationRecord rec = joint::assembleNotationRecord(
        piece, r, std::optional<int>(0), "", f.adapter, *f.vocab, f.cache);

    ASSERT_EQ(rec.provenance.tableArtifacts.size(), joint::embedded::kTableArtifacts.size());
    for (size_t k = 0; k < rec.provenance.tableArtifacts.size(); ++k) {
        EXPECT_EQ(rec.provenance.tableArtifacts[k].first, joint::embedded::kTableArtifacts[k]->name);
        EXPECT_EQ(rec.provenance.tableArtifacts[k].second, joint::embedded::kTableArtifacts[k]->sha256);
    }
    EXPECT_EQ(rec.provenance.weightVectorIdentity, joint::embedded::kWeightVectorIdentity);
    EXPECT_EQ(rec.provenance.decoderVersion, joint::embedded::kDecoderVersion);
    EXPECT_EQ(rec.provenance.corpusGitHash, joint::embedded::kCorpusGitHash);
    // input echo + span
    EXPECT_EQ(rec.sigFifths, std::optional<int>(0));
    EXPECT_EQ(rec.declaredMode, "");
    EXPECT_EQ(rec.spanStartTick, piece.events.front().start);
    EXPECT_EQ(rec.spanEndTick, piece.events.back().end);
}

// ── §3.1/§3.2/§3.3: derived facts of two real corpus pieces vs independent expectations ────────────
TEST(JointRecordTests, RealCorpusDerivedFactsAgainstIndependentExpectations)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok);
    for (const std::string& stem : { std::string("bwv324"), std::string("bwv362") }) {
        ASSERT_TRUE(f.corpus.pieces.count(stem)) << stem;
        joint::Piece& piece = f.corpus.pieces.at(stem);
        const joint::DecodeResult r = joint::decodePiece(piece, f.adapter, *f.vocab, f.cache, 4,
                                                         std::optional<int>(0), "");
        ASSERT_FALSE(r.segments.empty()) << stem;
        const joint::NotationRecord rec = joint::assembleNotationRecord(
            piece, r, std::optional<int>(0), "", f.adapter, *f.vocab, f.cache);

        ASSERT_EQ(rec.segments.size(), r.segments.size()) << stem;
        ASSERT_EQ(rec.slices.size(), r.segments.size()) << stem;   // §3.3 one slice per segment

        for (size_t i = 0; i < rec.segments.size(); ++i) {
            const joint::SegmentSummary& seg = r.segments[i];
            const joint::RecordSegment& rs = rec.segments[i];
            const joint::LabelClass cls = joint::classFromKey(seg.classKey);

            // committed reading, verbatim
            EXPECT_EQ(rs.startTick, seg.startTick) << stem << " seg " << i;
            EXPECT_EQ(rs.endTick, seg.endTick) << stem << " seg " << i;
            EXPECT_EQ(rs.tonicPc, seg.tonicPc) << stem << " seg " << i;
            EXPECT_EQ(rs.isMajor, seg.isMajor) << stem << " seg " << i;
            EXPECT_EQ(rs.classKey, seg.classKey) << stem << " seg " << i;
            EXPECT_EQ(rs.rootPc, seg.rootPc) << stem << " seg " << i;

            // derived: key-signature fifths (independent)
            EXPECT_EQ(rs.keySignatureFifths, expectFifths(seg.tonicPc, seg.isMajor, 0))
                << stem << " seg " << i;
            // derived: diatonicToKey (independent)
            EXPECT_EQ(rs.diatonicToKey, expectDiatonic(cls)) << stem << " seg " << i;
            // derived: chord symbol (independent) — pc name + class quality, or "" when rootless
            if (rs.rootPc.has_value()) {
                const std::string expSym =
                    std::string(kPcName[((*rs.rootPc) % 12 + 12) % 12]) + cls.quality();
                EXPECT_EQ(rs.chordSymbol, expSym) << stem << " seg " << i;
            } else {
                EXPECT_EQ(rs.chordSymbol, "") << stem << " seg " << i;
            }
            // derived: member factors — first factor is the root at rootPc (non-chromatic classes)
            if (!rs.members.empty()) {
                EXPECT_EQ(rs.members.front().role, "root") << stem << " seg " << i;
                ASSERT_TRUE(rs.rootPc.has_value()) << stem << " seg " << i;
                EXPECT_EQ(rs.members.front().pc, *rs.rootPc) << stem << " seg " << i;
            }
            // derived: per-event bass facts cover exactly events [i, j)
            EXPECT_EQ(static_cast<int>(rs.bassPerEvent.size()), seg.j - seg.i) << stem << " seg " << i;
            // aug-sixth sub-type present iff the class is AugSixth
            if (cls.quality() == "AugSixth") {
                EXPECT_FALSE(rs.augSixthSubType.empty()) << stem << " seg " << i;
            } else {
                EXPECT_TRUE(rs.augSixthSubType.empty()) << stem << " seg " << i;
            }
        }
    }
}

// ── §3.1/§3.2: a small SYNTHETIC piece with a hand-stated exact record ────────────────────────────
TEST(JointRecordTests, SyntheticPieceExactRecord)
{
    Fixture f = load();
    ASSERT_TRUE(f.ok);

    // one event: a C-major triad (C4/E4/G4), bass C.
    joint::Piece piece = onEventPiece({ 0, 4, 7 }, { 60, 64, 67 });

    // hand-built committed segment: C major, tonic 0, class "I | Maj".
    joint::SegmentSummary s;
    s.i = 0;
    s.j = 1;
    s.startTick = 0;
    s.endTick = 480;
    s.tonicPc = 0;
    s.isMajor = true;
    s.key = "Cmaj";
    s.classKey = "I | Maj |  | ";
    s.rootPc = 0;
    s.degree = "I";
    s.quality = "Maj";
    joint::DecodeResult r;
    r.stem = piece.stem;
    r.segments.push_back(s);

    const joint::NotationRecord rec = joint::assembleNotationRecord(
        piece, r, std::optional<int>(0), "major", f.adapter, *f.vocab, f.cache);

    // §3.1
    EXPECT_EQ(rec.stem, "synthetic");
    EXPECT_EQ(rec.spanStartTick, 0);
    EXPECT_EQ(rec.spanEndTick, 480);
    EXPECT_EQ(rec.sigFifths, std::optional<int>(0));
    EXPECT_EQ(rec.declaredMode, "major");
    EXPECT_EQ(rec.provenance.tableArtifacts.size(), 5u);

    // §3.2 exact hand-stated facts
    ASSERT_EQ(rec.segments.size(), 1u);
    const joint::RecordSegment& rs = rec.segments[0];
    EXPECT_EQ(rs.chordSymbol, "CMaj");
    EXPECT_EQ(rs.romanNumeral, "I");
    EXPECT_TRUE(rs.diatonicToKey);
    EXPECT_EQ(rs.keySignatureFifths, 0);
    EXPECT_EQ(rs.augSixthSubType, "");
    ASSERT_EQ(rs.members.size(), 3u);
    EXPECT_EQ(rs.members[0].role, "root");   EXPECT_EQ(rs.members[0].pc, 0);
    EXPECT_EQ(rs.members[1].role, "third");  EXPECT_EQ(rs.members[1].pc, 4);
    EXPECT_EQ(rs.members[2].role, "fifth");  EXPECT_EQ(rs.members[2].pc, 7);
    ASSERT_EQ(rs.bassPerEvent.size(), 1u);
    EXPECT_EQ(rs.bassPerEvent[0].eventIndex, 0);
    EXPECT_EQ(rs.bassPerEvent[0].bassPc, std::optional<int>(0));
    EXPECT_EQ(rs.bassPerEvent[0].role, "root");

    // §3.3 one slice for the one segment
    ASSERT_EQ(rec.slices.size(), 1u);
    EXPECT_FALSE(rec.slices[0].keyAxis.labels.empty());
    EXPECT_FALSE(rec.slices[0].chordAxis.labels.empty());
}
