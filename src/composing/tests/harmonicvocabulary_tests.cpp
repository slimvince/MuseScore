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

// harmonicvocabulary_tests.cpp — THE HARMONIC VOCABULARY component (v1, dormant).
//
// Oracle-asserted against the spec / known music theory (NOT echoes of any analyzer):
// the four §4 queries — browse / recognise / suggest / expand — over a hand-built
// catalog. Spec (the contract): cowork_progression_schema_dictionary.md.

#include <gtest/gtest.h>

#include "composing/analysis/vocabulary/harmonicvocabulary.h"
#include "composing/analysis/chord/chordanalyzer.h"   // Extension (to set seventh bits on a span chord)

using namespace mu::composing::analysis;

namespace {

// Pitch classes for readability.
constexpr int C = 0, Cs = 1, D = 2, Ds = 3, E = 4, F = 5, G = 7, A = 9, Bb = 10, Db = 1;

uint32_t ext(Extension e) { return static_cast<uint32_t>(e); }

SpanChord chord(int rootPc, ChordQuality q, int tonicPc, bool minor = false,
                uint32_t extensions = 0, int bassPc = -1)
{
    SpanChord c;
    c.rootPc = rootPc;
    c.bassPc = (bassPc < 0) ? rootPc : bassPc;
    c.quality = q;
    c.extensions = extensions;
    c.localTonicPc = tonicPc;
    c.localMinorMode = minor;
    return c;
}

// A bass-line span chord (root/quality irrelevant to a bass-line match; bass is set).
SpanChord bassChord(int bassPc, int tonicPc)
{
    return chord(bassPc, ChordQuality::Major, tonicPc, /*minor*/ false, /*ext*/ 0, bassPc);
}

bool hasEntryNamed(const std::vector<VocabularyCandidate>& cands, const std::string& name)
{
    for (const VocabularyCandidate& c : cands) {
        if (c.entry && c.entry->name == name) {
            return true;
        }
    }
    return false;
}

const VocabularyCandidate* findEntry(const std::vector<VocabularyCandidate>& cands, const std::string& name)
{
    for (const VocabularyCandidate& c : cands) {
        if (c.entry && c.entry->name == name) {
            return &c;
        }
    }
    return nullptr;
}

const std::string kIiVI = "ii–V–I (common-practice, triads)";

} // namespace

// ── §4 expand — the generative spine (§5.1) ───────────────────────────────────

TEST(HarmonicVocabulary, ExpandEmitsTheFourSlotsPlusTheSubsRelatedIi)
{
    HarmonicVocabulary vocab;
    // x = the supertonic degree (offset 2). The five generative slots are functions of x.
    std::vector<GenerativeSlot> slots = vocab.expand(2);
    ASSERT_EQ(slots.size(), 5u);

    // V7/x: a dominant seventh a perfect fifth above x → (2+7)=9, Major + minor 7th.
    EXPECT_EQ(slots[0].name, "V7/x");
    EXPECT_EQ(slots[0].chord.degreeOffset, 9);
    EXPECT_EQ(slots[0].chord.triadQuality, ChordQuality::Major);
    EXPECT_EQ(slots[0].chord.seventh, SeventhRequirement::Minor);

    // viio7/x: a diminished seventh a semitone below x → (2+11)=1.
    EXPECT_EQ(slots[1].name, "viio7/x");
    EXPECT_EQ(slots[1].chord.degreeOffset, 1);
    EXPECT_EQ(slots[1].chord.triadQuality, ChordQuality::Diminished);

    // IIm7/x: the related ii a major second above x → (2+2)=4.
    EXPECT_EQ(slots[2].name, "IIm7/x");
    EXPECT_EQ(slots[2].chord.degreeOffset, 4);
    EXPECT_EQ(slots[2].chord.triadQuality, ChordQuality::Minor);

    // subV7/x: the tritone substitute, a semitone above x → (2+1)=3, Major + minor 7th.
    EXPECT_EQ(slots[3].name, "subV7/x");
    EXPECT_EQ(slots[3].chord.degreeOffset, 3);
    EXPECT_EQ(slots[3].chord.triadQuality, ChordQuality::Major);

    // the sub's related ii, a perfect fifth above subV7/x → (2+8)=10.
    EXPECT_EQ(slots[4].name, "IIm7/subV7/x");
    EXPECT_EQ(slots[4].chord.degreeOffset, 10);
    EXPECT_EQ(slots[4].chord.triadQuality, ChordQuality::Minor);

    // every returned slot carries a structural match score.
    for (const GenerativeSlot& s : slots) {
        EXPECT_DOUBLE_EQ(s.matchScore, 1.0);
    }
}

TEST(HarmonicVocabulary, ExpandWrapsTheTargetDegree)
{
    HarmonicVocabulary vocab;
    // x = the leading tone (offset 11): V7/x root = (11+7)=18 mod 12 = 6.
    std::vector<GenerativeSlot> slots = vocab.expand(11);
    ASSERT_EQ(slots.size(), 5u);
    EXPECT_EQ(slots[0].chord.degreeOffset, 6);
}

// ── §4 recognise — exact, key-relative, structural ────────────────────────────

TEST(HarmonicVocabulary, RecognisesMajorIiVI)
{
    HarmonicVocabulary vocab;
    // Dm – G – C in C major.
    VocabularySpan span = {
        chord(D, ChordQuality::Minor, C),
        chord(G, ChordQuality::Major, C),
        chord(C, ChordQuality::Major, C),
    };
    std::vector<VocabularyCandidate> r = vocab.recognise(span);
    ASSERT_FALSE(r.empty());
    const VocabularyCandidate* iivi = findEntry(r, kIiVI);
    ASSERT_NE(iivi, nullptr);
    EXPECT_EQ(iivi->spanStart, 0);
    EXPECT_EQ(iivi->spanEnd, 3);
    EXPECT_TRUE(iivi->substitutedMembers.empty());   // a literal realisation
    EXPECT_DOUBLE_EQ(iivi->matchScore, 1.0);
    // The longest / most specific match (ii–V–I, len 3) ranks ahead of the embedded
    // authentic V–I (len 2).
    EXPECT_EQ(r.front().entry->name, kIiVI);
}

TEST(HarmonicVocabulary, RecognisesMinorIiVI)
{
    HarmonicVocabulary vocab;
    // Dø7 – G7 – Cm in C minor.
    VocabularySpan span = {
        chord(D, ChordQuality::HalfDiminished, C, /*minor*/ true),
        chord(G, ChordQuality::Major, C, /*minor*/ true, ext(Extension::MinorSeventh)),
        chord(C, ChordQuality::Minor, C, /*minor*/ true),
    };
    std::vector<VocabularyCandidate> r = vocab.recognise(span);
    EXPECT_TRUE(hasEntryNamed(r, "iiø7–V7–i (minor ii–V–i)"));
}

TEST(HarmonicVocabulary, RecogniseIsKeyRelativeAcrossKeys)
{
    HarmonicVocabulary vocab;
    // The same ii–V–I transposed to D major (tonic 2): Em – A – D.
    VocabularySpan span = {
        chord(E, ChordQuality::Minor, D),
        chord(A, ChordQuality::Major, D),
        chord(D, ChordQuality::Major, D),
    };
    std::vector<VocabularyCandidate> r = vocab.recognise(span);
    const VocabularyCandidate* iivi = findEntry(r, kIiVI);
    ASSERT_NE(iivi, nullptr);
    EXPECT_EQ(iivi->spanStart, 0);
    EXPECT_EQ(iivi->spanEnd, 3);
}

TEST(HarmonicVocabulary, RecogniseReturnsEmptyOnAnUnrecognisedSpan)
{
    HarmonicVocabulary vocab;
    // C – C♯ (offsets 0,1, both major) realises no schema.
    VocabularySpan span = {
        chord(C, ChordQuality::Major, C),
        chord(Cs, ChordQuality::Major, C),
    };
    EXPECT_TRUE(vocab.recognise(span).empty());
}

TEST(HarmonicVocabulary, RecogniseSurfacesATritoneSubstitutedMember)
{
    HarmonicVocabulary vocab;
    // Dm – D♭7 – C in C major: a ii–subV–I. The literal skeleton (ii–V–I) is unchanged;
    // the V member is read as a tritone-substituted dominant via the substitution mapping.
    VocabularySpan span = {
        chord(D, ChordQuality::Minor, C),
        chord(Db, ChordQuality::Major, C, /*minor*/ false, ext(Extension::MinorSeventh)),
        chord(C, ChordQuality::Major, C),
    };
    std::vector<VocabularyCandidate> r = vocab.recognise(span);
    const VocabularyCandidate* iivi = findEntry(r, kIiVI);
    ASSERT_NE(iivi, nullptr);
    // the entry's literal skeleton is unchanged (still ii–V–I, three chord steps).
    EXPECT_EQ(iivi->entry->skeleton.length(), 3);
    // the substituted member is recorded at the V position (span index 1).
    ASSERT_EQ(iivi->substitutedMembers.size(), 1u);
    EXPECT_EQ(iivi->substitutedMembers[0].spanIndex, 1);
    EXPECT_EQ(iivi->substitutedMembers[0].substitution, SubstitutionType::TritoneSub);
    EXPECT_FALSE(iivi->substitutedMembers[0].mapping.empty());
}

TEST(HarmonicVocabulary, RecognisesAGalantBassLineSchema)
{
    HarmonicVocabulary vocab;
    // The Prinner bass 4̂–3̂–2̂–1̂ in C major → bass F – E – D – C (offsets 5,4,2,0).
    VocabularySpan span = {
        bassChord(F, C),
        bassChord(E, C),
        bassChord(D, C),
        bassChord(C, C),
    };
    std::vector<VocabularyCandidate> r = vocab.recognise(span);
    EXPECT_TRUE(hasEntryNamed(r, "Prinner (bass 4̂–3̂–2̂–1̂)"));
}

// ── §4 suggest — follow / precede / replace ───────────────────────────────────

TEST(HarmonicVocabulary, SuggestFollowReturnsAPrefixContinuation)
{
    HarmonicVocabulary vocab;
    // ii–V → could continue to I (ii–V–I).
    VocabularySpan span = {
        chord(D, ChordQuality::Minor, C),
        chord(G, ChordQuality::Major, C),
    };
    std::vector<VocabularyCandidate> f = vocab.suggest(span, SuggestDirection::Follow);
    EXPECT_TRUE(hasEntryNamed(f, kIiVI));
    for (const VocabularyCandidate& c : f) {
        EXPECT_DOUBLE_EQ(c.matchScore, 1.0);
    }
}

TEST(HarmonicVocabulary, SuggestPrecedeReturnsASuffixLeadIn)
{
    HarmonicVocabulary vocab;
    // V–I → could be led into by ii (ii–V–I).
    VocabularySpan span = {
        chord(G, ChordQuality::Major, C),
        chord(C, ChordQuality::Major, C),
    };
    std::vector<VocabularyCandidate> p = vocab.suggest(span, SuggestDirection::Precede);
    EXPECT_TRUE(hasEntryNamed(p, kIiVI));
}

TEST(HarmonicVocabulary, SuggestFollowIsEmptyWhenNothingContinues)
{
    HarmonicVocabulary vocab;
    // C – C♯ is no entry's prefix.
    VocabularySpan span = {
        chord(C, ChordQuality::Major, C),
        chord(Cs, ChordQuality::Major, C),
    };
    EXPECT_TRUE(vocab.suggest(span, SuggestDirection::Follow).empty());
}

TEST(HarmonicVocabulary, SuggestReplaceReturnsApplicableSubstitutionsAndDiatonicAlternatives)
{
    HarmonicVocabulary vocab;
    // A dominant G in C major: substitutions apply (tritone sub, related ii–V, …) and a
    // same-function diatonic alternative is offered (the diatonic-functional substitution).
    VocabularySpan span = { chord(G, ChordQuality::Major, C) };
    std::vector<VocabularyCandidate> rep = vocab.suggest(span, SuggestDirection::Replace);
    ASSERT_FALSE(rep.empty());
    EXPECT_TRUE(hasEntryNamed(rep, "Tritone substitution (subV)"));
    EXPECT_TRUE(hasEntryNamed(rep, "Diatonic (functional) substitution"));
    for (const VocabularyCandidate& c : rep) {
        ASSERT_NE(c.entry, nullptr);
        EXPECT_EQ(c.entry->kind, EntryKind::Substitution);
    }
}

TEST(HarmonicVocabulary, SuggestReplaceIsEmptyWhenNoSubstitutionApplies)
{
    HarmonicVocabulary vocab;
    // A chromatic augmented chord on ♭II (offset 1, augmented): not a dominant, not
    // diatonic, not a plain triad → no substitution operation applies.
    VocabularySpan span = { chord(Db, ChordQuality::Augmented, C) };
    EXPECT_TRUE(vocab.suggest(span, SuggestDirection::Replace).empty());
}

// ── §4 browse + ranking ───────────────────────────────────────────────────────

TEST(HarmonicVocabulary, BrowseReturnsEntriesInActiveStylesOnly)
{
    HarmonicVocabulary vocab;
    // The jazz subset surfaces a jazz-only entry and excludes a galant-only one.
    std::vector<VocabularyCandidate> jazz = vocab.browse(jazzStyles());
    EXPECT_TRUE(hasEntryNamed(jazz, "Tritone substitution (subV)"));
    EXPECT_FALSE(hasEntryNamed(jazz, "Prinner (bass 4̂–3̂–2̂–1̂)"));

    // The Baroque (common-practice) subset surfaces the Prinner.
    std::vector<VocabularyCandidate> galant = vocab.browse({ StyleTag::Baroque });
    EXPECT_TRUE(hasEntryNamed(galant, "Prinner (bass 4̂–3̂–2̂–1̂)"));

    // every browsed entry carries a match score.
    for (const VocabularyCandidate& c : jazz) {
        EXPECT_DOUBLE_EQ(c.matchScore, 1.0);
    }
}

TEST(HarmonicVocabulary, BrowseRanksMoreSpecificAndLongerFirst)
{
    HarmonicVocabulary vocab;
    std::vector<VocabularyCandidate> all = vocab.browse();
    ASSERT_GE(all.size(), 2u);
    // ranking is specificity-then-length: non-increasing down the list.
    for (size_t i = 1; i < all.size(); ++i) {
        const int prevSpec = all[i - 1].entry->skeleton.specificity();
        const int curSpec = all[i].entry->skeleton.specificity();
        EXPECT_GE(prevSpec, curSpec);
        if (prevSpec == curSpec) {
            EXPECT_GE(all[i - 1].entry->skeleton.length(), all[i].entry->skeleton.length());
        }
    }
}

TEST(HarmonicVocabulary, RecogniseRanksTheLongerMatchFirst)
{
    HarmonicVocabulary vocab;
    // Dm – G – C realises both ii–V–I (len 3) and the embedded authentic V–I (len 2);
    // the longer / more specific ranks first.
    VocabularySpan span = {
        chord(D, ChordQuality::Minor, C),
        chord(G, ChordQuality::Major, C),
        chord(C, ChordQuality::Major, C),
    };
    std::vector<VocabularyCandidate> r = vocab.recognise(span);
    ASSERT_GE(r.size(), 2u);
    EXPECT_GE(r[0].entry->skeleton.specificity(), r[1].entry->skeleton.specificity());
    EXPECT_TRUE(hasEntryNamed(r, "Authentic cadence (V–I)"));
}
