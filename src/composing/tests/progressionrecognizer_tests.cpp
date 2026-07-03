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

// progressionrecognizer_tests.cpp — THE PROGRESSION-RECOGNITION CONSUMER (dormant).
//
// Oracle-asserted against the consumer design cowork_progression_schema_design.md
// §4 (NOT echoes of any analyzer): recognition (§4.1), substitutions (§4.2), the
// idiom-mixture three-phase weighting (§4.5), the annotation (§4.4/D6/D7), the
// evidence contribution (§4.3), and the always-emitted harmonic sequences (§4.6),
// over hand-built committed progressions + the real Harmonic Vocabulary catalog.
//
// PLUS the Task-2.1 D5 CONSISTENCY TEST (see the block above that test): every
// adjacent chord pair of every catalog entry is EITHER licensed by
// isLicensedProgression (the Layer-5 grammar) OR on the explicit ruled known-gap
// list. A pin plus a tripwire — any 7th failure turns this suite red.

#include <gtest/gtest.h>

#include <set>
#include <string>
#include <utility>

#include "composing/analysis/progression/progressionrecognizer.h"
#include "composing/analysis/vocabulary/harmonicvocabulary.h"
#include "composing/analysis/function/functionprogression.h"  // isLicensedProgression, ProgressionChord (D5 test)
#include "composing/analysis/chord/chordanalyzer.h"            // Extension (seventh bits)

using namespace mu::composing::analysis;
using namespace mu::composing::analysis::progression;

namespace {

// Pitch classes / qualities for readability.
constexpr int C = 0, Db = 1, D = 2, E = 4, Fs = 6, G = 7, A = 9, B = 11;
constexpr ChordQuality Maj = ChordQuality::Major;
constexpr ChordQuality Min = ChordQuality::Minor;

uint32_t ext(Extension e) { return static_cast<uint32_t>(e); }

// One committed-progression position. `committed` defaults true; an abstained
// position sets it false and supplies rankedCandidates.
CommittedChord cc(int rootPc, ChordQuality q, int tonicPc, bool minor = false,
                  uint32_t extensions = 0, int startTick = 0, int endTick = 0,
                  int bassPc = -1)
{
    CommittedChord c;
    c.chord.rootPc = rootPc;
    c.chord.bassPc = (bassPc < 0) ? rootPc : bassPc;
    c.chord.quality = q;
    c.chord.extensions = extensions;
    c.chord.localTonicPc = tonicPc;
    c.chord.localMinorMode = minor;
    c.startTick = startTick;
    c.endTick = endTick;
    return c;
}

const ProgressionSchemaSpan* findSpan(const ProgressionRecognitionOutput& out, const std::string& name)
{
    for (const ProgressionSchemaSpan& s : out.schemaSpans) {
        if (s.name == name) {
            return &s;
        }
    }
    return nullptr;
}

const std::string kIiVITriads = "ii–V–I (common-practice, triads)";
const std::string kIncompleteIiV = "Incomplete ii–V (no resolution)";
const std::string kPrinner = "Prinner (bass 4̂–3̂–2̂–1̂)";

} // namespace

// ── §4.1 recognition — a plain ii–V–I ─────────────────────────────────────────

TEST(ProgressionRecognizer, RecognisesPlainIiVITriads)
{
    HarmonicVocabulary vocab;
    // ii–V–I in C major: Dm, G, C — all committed triads.
    CommittedProgression prog = {
        cc(D, Min, C, false, 0, 0, 480),
        cc(G, Maj, C, false, 0, 480, 960),
        cc(C, Maj, C, false, 0, 960, 1440),
    };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);

    const ProgressionSchemaSpan* s = findSpan(out, kIiVITriads);
    ASSERT_NE(s, nullptr);
    EXPECT_EQ(s->startIndex, 0);
    EXPECT_EQ(s->endIndex, 3);
    EXPECT_EQ(s->startTick, 0);
    EXPECT_EQ(s->endTick, 1440);
    EXPECT_DOUBLE_EQ(s->matchScore, 1.0);   // an exact realisation
    EXPECT_FALSE(s->chordsOnly);            // not a voice-leading-defined entry
    EXPECT_TRUE(s->substitutedMembers.empty());
    EXPECT_GT(s->priorStrength, 0.0);       // admitted

    // §4.1 overlap ordering: the 3-chord ii–V–I is longer than the 2-chord authentic
    // cadence it contains, so it sorts FIRST (longer-then-more-specific).
    ASSERT_FALSE(out.schemaSpans.empty());
    EXPECT_EQ(out.schemaSpans.front().name, kIiVITriads);
}

// ── §4.2 a substituted ii–(subV)–I: the tritone sub is RECOGNISED, not overridden ─

TEST(ProgressionRecognizer, RecognisesTritoneSubstitutedIiVI)
{
    HarmonicVocabulary vocab;
    // ii–subV–I in C: Dm, D♭7 (subV7 standing for G7), C — position 1 is the sub.
    CommittedProgression prog = {
        cc(D, Min, C),
        cc(Db, Maj, C, false, ext(Extension::MinorSeventh)),   // D♭7 = subV7/I
        cc(C, Maj, C),
    };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);

    const ProgressionSchemaSpan* s = findSpan(out, kIiVITriads);
    ASSERT_NE(s, nullptr);
    ASSERT_EQ(s->substitutedMembers.size(), 1u);
    EXPECT_EQ(s->substitutedMembers[0].position, 1);
    EXPECT_EQ(s->substitutedMembers[0].substitution, SubstitutionType::TritoneSub);
    EXPECT_FALSE(s->substitutedMembers[0].readOut.empty());
    // §4.2/D4: the literal skeleton is unchanged — this build changes no Roman
    // numeral; the substitution is recorded ONLY as the read-out above.
}

// ── §4.6 a Monte chain — the same ii–V repeated ascending by whole step ─────────

TEST(ProgressionRecognizer, EmitsHarmonicSequenceForMonteChain)
{
    HarmonicVocabulary vocab;
    // Three "Incomplete ii–V" units, keys ascending by whole step (C, D, E):
    //   ii–V in C (Dm7, G7) · in D (Em7, A7) · in E (F♯m7, B7).
    const uint32_t m7 = ext(Extension::MinorSeventh);
    CommittedProgression prog = {
        cc(D,  Min, C, false, m7, 0,    480),
        cc(G,  Maj, C, false, m7, 480,  960),
        cc(E,  Min, D, false, m7, 960,  1440),
        cc(A,  Maj, D, false, m7, 1440, 1920),
        cc(Fs, Min, E, false, m7, 1920, 2400),
        cc(B,  Maj, E, false, m7, 2400, 2880),
    };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);

    // §4.6 ALWAYS emits: exactly one sequence, the ii–V repeated ×3 up a whole step.
    ASSERT_EQ(out.sequences.size(), 1u);
    const HarmonicSequence& hs = out.sequences[0];
    EXPECT_EQ(hs.name, kIncompleteIiV);
    EXPECT_EQ(hs.transpositionStep, 2);    // up a whole step
    EXPECT_EQ(hs.repetitions, 3);          // three matched windows
    EXPECT_EQ(hs.startIndex, 0);
    EXPECT_EQ(hs.endIndex, 6);
    EXPECT_GT(hs.priorStrength, 0.0);
}

TEST(ProgressionRecognizer, LoneRecognitionEmitsNoSequence)
{
    HarmonicVocabulary vocab;
    // A single ii–V–I — a recognition, but not a REPEATED (transposed) one.
    CommittedProgression prog = { cc(D, Min, C), cc(G, Maj, C), cc(C, Maj, C) };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);
    EXPECT_TRUE(out.sequences.empty());    // §4.6: a lone recognition is not a sequence
}

// ── §4.5 the three-phase mixture (pure rules, in isolation) ────────────────────

TEST(ProgressionRecognizer, MixtureNoEvidenceReturnsSeed)
{
    // Phase 2 with an empty histogram ⇒ w = the (normalised) seed.
    const IdiomWeights seed = { 0.6, 0.1, 0.1, 0.1, 0.1 };   // already sums to 1
    const IdiomEvidenceHistogram none = { 0, 0, 0, 0, 0 };
    IdiomWeights w = blendIdiomWeights(seed, none, kDefaultRecognitionParams.blendRate);
    for (std::size_t i = 0; i < kIdiomCount; ++i) {
        EXPECT_NEAR(w[i], seed[i], 1e-9);
    }
}

TEST(ProgressionRecognizer, MixtureEvidenceMovesWeightTowardHistogram)
{
    // Evidence all on idiom 1 (ChromaticFunctional) ⇒ w[1] rises above the equal seed.
    const IdiomEvidenceHistogram hist = { 0, 3, 0, 0, 0 };
    IdiomWeights w = blendIdiomWeights(kEqualSeed, hist, /*blendRate*/ 1.0);
    EXPECT_GT(w[1], kEqualSeed[1]);        // moved toward the histogram
    EXPECT_GT(w[1], w[0]);                 // and above the un-evidenced idioms
    // α = E/(E+rate) = 3/4; w[1] = 0.25·0.2 + 0.75·1.0 = 0.8.
    EXPECT_NEAR(w[1], 0.8, 1e-9);
}

TEST(ProgressionRecognizer, PriorStrengthUsesMaxNotSumOverIdioms)
{
    const IdiomWeights w = { 0.5, 0.1, 0.3, 0.1, 0.1 };
    // An entry tagged {DiatonicFunctional(0), SeventhFunctional(2)} — the prior uses the
    // MAX (0.5), never the sum (0.8): a multi-idiom entry is not thereby advantaged.
    const IdiomSet twoIdioms = idiomSet(Idiom::DiatonicFunctional, Idiom::SeventhFunctional);
    double prior = recognitionPriorStrength(1.0, w, twoIdioms, /*modeContra*/ false, /*chordsOnly*/ false);
    EXPECT_NEAR(prior, 0.5, 1e-9);
    EXPECT_NE(prior, 0.8);
}

// ── §4.5 admission + the two soft-cue factors ──────────────────────────────────

TEST(ProgressionRecognizer, AdmissionThresholdGatesEmission)
{
    HarmonicVocabulary vocab;
    CommittedProgression prog = { cc(D, Min, C), cc(G, Maj, C), cc(C, Maj, C) };

    // Default threshold (0.0, inert) admits.
    EXPECT_FALSE(recognizeProgressions(prog, vocab).schemaSpans.empty());

    // A threshold above any achievable prior (≤ 1) admits nothing.
    RecognitionParams strict = kDefaultRecognitionParams;
    strict.admissionThreshold = 2.0;
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab, kEqualSeed, kAllIdioms, strict);
    EXPECT_TRUE(out.schemaSpans.empty());
    EXPECT_TRUE(out.abstainedFeatures.empty());
    EXPECT_TRUE(out.sequences.empty());
}

TEST(ProgressionRecognizer, ModeCueAndChordsOnlyFactorsScaleThePrior)
{
    const IdiomWeights w = { 0.4, 0.4, 0.4, 0.4, 0.4 };
    const IdiomSet one = idiomSet(Idiom::DiatonicFunctional);
    RecognitionParams p = kDefaultRecognitionParams;   // modeCueFactor = chordsOnlyFactor = 0.5

    const double base = recognitionPriorStrength(1.0, w, one, false, false, p);
    EXPECT_NEAR(base, 0.4, 1e-9);
    // Mode cue: a contradicting entry mode multiplies by the factor (< 1, never 0).
    EXPECT_NEAR(recognitionPriorStrength(1.0, w, one, /*modeContra*/ true, false, p),
                base * p.modeCueFactor, 1e-9);
    // Chords-only (D7): a voice-leading-defined entry multiplies by the factor (< 1).
    EXPECT_NEAR(recognitionPriorStrength(1.0, w, one, false, /*chordsOnly*/ true, p),
                base * p.chordsOnlyFactor, 1e-9);
    // Both cues compound.
    EXPECT_NEAR(recognitionPriorStrength(1.0, w, one, true, true, p),
                base * p.modeCueFactor * p.chordsOnlyFactor, 1e-9);
}

// ── §4.4/D7 the chords-only mark on a voice-leading-defined entry ───────────────

TEST(ProgressionRecognizer, VoiceLeadingDefinedEntryCarriesTheChordsOnlyMark)
{
    HarmonicVocabulary vocab;
    // The Prinner — a BASS-line schema (4̂–3̂–2̂–1̂), voiceLeadingDefined. Match its bass
    // degrees over C: bass F, E, D, C (roots/qualities irrelevant to a bass-line match).
    CommittedProgression prog = {
        cc(0, Maj, C, false, 0, 0,    480,  /*bass*/ 5),   // 4̂ = F
        cc(0, Maj, C, false, 0, 480,  960,  /*bass*/ 4),   // 3̂ = E
        cc(0, Maj, C, false, 0, 960,  1440, /*bass*/ 2),   // 2̂ = D
        cc(0, Maj, C, false, 0, 1440, 1920, /*bass*/ 0),   // 1̂ = C
    };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);

    const ProgressionSchemaSpan* s = findSpan(out, kPrinner);
    ASSERT_NE(s, nullptr);
    EXPECT_TRUE(s->chordsOnly);   // D7 — recognised by its chord/bass skeleton alone
    // §4.3: a line-defined entry has no chord-quality member, so it contributes no
    // abstained/override chord evidence (declared) — verified indirectly: all four
    // positions are committed, so no abstained features regardless.
}

// ── §4.3 the abstained-feature path (selection-only) ───────────────────────────

TEST(ProgressionRecognizer, AbstainedPositionEmitsSelectionOnlyFeature)
{
    HarmonicVocabulary vocab;
    // ii–V–I where Layer 4 ABSTAINED on the V (position 1): the query chord is the
    // top candidate (G major); the ranked candidates are [G major (fills the member),
    // E minor (does not)].
    CommittedProgression prog = {
        cc(D, Min, C),
        cc(G, Maj, C),   // .chord = the top candidate used for recognition
        cc(C, Maj, C),
    };
    prog[1].committed = false;
    prog[1].rankedCandidates = {
        CandidateReading{ G, Maj, 0, 0.7 },   // index 0 — fills the V member
        CandidateReading{ E, Min, 0, 0.3 },   // index 1 — does not
    };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);

    // The committed-override path is inert here (see the F-B test); only the abstained
    // feature fires, at position 1, SELECTING an existing candidate (index 0).
    EXPECT_TRUE(out.overrides.empty());
    bool found = false;
    for (const AbstainedFeature& f : out.abstainedFeatures) {
        if (f.position == 1) {
            EXPECT_EQ(f.memberRootPc, G);
            EXPECT_EQ(f.memberQuality, Maj);
            EXPECT_EQ(f.selectedCandidateIndex, 0);   // selection-only — an existing candidate
            EXPECT_GT(f.weight, 0.0);                 // weighted by the recognition's prior
            found = true;
        }
    }
    EXPECT_TRUE(found);
}

// ── §4.3 the committed-override path — F-B semantics, selection-only ────────────

TEST(ProgressionRecognizer, CommittedOverrideContributionCarriesFBSemantics)
{
    // The contradiction predicate: a member demands a different root OR quality.
    EXPECT_TRUE(memberContradictsCommittedReading(G, Maj, C, Maj));    // different root
    EXPECT_TRUE(memberContradictsCommittedReading(G, Maj, G, Min));    // different quality
    EXPECT_FALSE(memberContradictsCommittedReading(G, Maj, G, Maj));   // identical → no contradiction

    // The contribution is SELECTION-only: the replacement it names is the member's
    // realisation (an existing reading, G major), NOT a reading built from notes; the
    // prior enters the F-B quantity; the composite confidence is the §8-scaling input.
    CommittedOverrideContribution c =
        overrideContributionFor(/*pos*/ 3, /*committed*/ C, Maj, /*member*/ G, Maj,
                                /*prior*/ 0.5, /*conf*/ 0.8, "ii–V–I");
    EXPECT_EQ(c.position, 3);
    EXPECT_EQ(c.committedRootPc, C);
    EXPECT_EQ(c.memberRootPc, G);        // the selection = the member realisation
    EXPECT_EQ(c.memberQuality, Maj);
    EXPECT_DOUBLE_EQ(c.priorStrength, 0.5);       // enters the F-B contradiction quantity
    EXPECT_DOUBLE_EQ(c.compositeConfidence, 0.8); // the §8 threshold-scaling input (L5 fires, not here)
}

TEST(ProgressionRecognizer, ExactMatchProducesNoCommittedOverride)
{
    HarmonicVocabulary vocab;
    // A fully-committed exact ii–V–I: every literal member matches the committed
    // reading by construction, so the override path is structurally inert (design §8).
    CommittedProgression prog = { cc(D, Min, C), cc(G, Maj, C), cc(C, Maj, C) };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);
    EXPECT_TRUE(out.overrides.empty());
}

// ── §3 nothing recognised → nothing emitted ────────────────────────────────────

TEST(ProgressionRecognizer, NothingRecognisedEmitsNothing)
{
    HarmonicVocabulary vocab;
    // A single chord and a static repeat realise no named progression.
    CommittedProgression prog = { cc(C, Maj, C), cc(C, Maj, C) };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);
    EXPECT_TRUE(out.schemaSpans.empty());
    EXPECT_TRUE(out.abstainedFeatures.empty());
    EXPECT_TRUE(out.overrides.empty());
    EXPECT_TRUE(out.sequences.empty());
    // No recognised evidence ⇒ the mixture stays at the (normalised) seed.
    for (std::size_t i = 0; i < kIdiomCount; ++i) {
        EXPECT_NEAR(out.weights[i], kEqualSeed[i], 1e-9);
    }

    // The empty input is also handled.
    EXPECT_TRUE(recognizeProgressions({}, vocab).schemaSpans.empty());
}

TEST(ProgressionRecognizer, RecognisedEvidenceMovesTheMixtureWeights)
{
    HarmonicVocabulary vocab;
    // A plain ii–V–I is Diatonic-functional; recognising it moves the mixture toward
    // idiom 0 (DiatonicFunctional) above the equal-seed 0.2 (§4.5 phases 1→2).
    CommittedProgression prog = { cc(D, Min, C), cc(G, Maj, C), cc(C, Maj, C) };
    ProgressionRecognitionOutput out = recognizeProgressions(prog, vocab);
    EXPECT_GT(out.weights[0], kEqualSeed[0]);
}

// ══════════════════════════════════════════════════════════════════════════════
// Task 2.1 — THE D5 CONSISTENCY TEST (the one-way catalog → grammar coupling).
//
// D5 (cowork_progression_schema_design.md §6, user-ratified 2026-07-02) asserts the
// containment: every adjacent chord pair inside every catalog progression should
// satisfy the Layer-5 licensing grammar (isLicensedProgression). This test enforces
// it — a FAILURE names the entry and states BOTH possible readings:
//   (a) the entry is MIS-ENCODED (a catalog typo — fix the Vocabulary), OR
//   (b) a genuine GRAMMAR GAP was found (a motion §5.0 does not yet license — extend
//       functionprogression, an L5-owned change; L5 spec §15-12).
//
// RULING (2026-07-02): the six entries / eleven motions below were found at this
// build and ruled reading (b) — GRAMMAR GAPS, not mis-encodings (each entry is
// musically correct; the §5.0 grammar descends from the old scoring-bonus signals
// and omits plagal / ascending-fifth (delta 7), descending-second (delta 10/11), and
// the diatonic diminished-fifth (delta 6)). They are pinned on the explicit known-gap
// list below so the suite stays honest WITHOUT tagging around them: any SEVENTH
// failure (a new entry, or a mis-encoding) is NOT on the list ⇒ the suite turns RED;
// and if the §15-12 grammar completion later licenses one of these, its list entry no
// longer fails ⇒ the suite turns RED, forcing the list to shrink and the test to
// tighten. (Cowork's addendum cites "12 motions"; the measured count is 11 — the exact
// pairs are enumerated below and reconciled in cc_consumer_build_report.md.)
// ══════════════════════════════════════════════════════════════════════════════

TEST(ProgressionRecognizerD5Consistency, EveryCatalogPairIsLicensedOrARuledGrammarGap)
{
    // The ruled known-gap list: (entry name, adjacent-pair start index). Exactly the
    // 6 entries / 11 motions found 2026-07-02, each verdict "musically correct; §5.0
    // grammar gap (L5-owned, L5 §15-12)".
    const std::set<std::pair<std::string, int>> knownGaps = {
        { "Plagal cadence (IV–I)", 0 },                                   // IV→I  delta 7 (plagal / ascending 5th)
        { "Axis (I–V–vi–IV)", 0 },                                        // I→V   delta 7
        { "Pachelbel (I–V–vi–iii–IV–I–IV–V)", 0 },                        // I→V   delta 7
        { "Pachelbel (I–V–vi–iii–IV–I–IV–V)", 2 },                        // vi→iii delta 7
        { "Pachelbel (I–V–vi–iii–IV–I–IV–V)", 4 },                        // IV→I  delta 7
        { "Romanesca (I–V–vi–iii)", 0 },                                  // I→V   delta 7
        { "Romanesca (I–V–vi–iii)", 2 },                                  // vi→iii delta 7
        { "Andalusian cadence (i–♭VII–♭VI–V)", 0 },                       // i→♭VII delta 10 (descending 2nd)
        { "Andalusian cadence (i–♭VII–♭VI–V)", 1 },                       // ♭VII→♭VI delta 10
        { "Andalusian cadence (i–♭VII–♭VI–V)", 2 },                       // ♭VI→V  delta 11 (descending semitone)
        { "Circle-of-fifths (full, I–IV–viio–iii–vi–ii–V–I)", 1 },        // IV→viio delta 6 (diminished 5th)
    };

    HarmonicVocabulary vocab;

    // Scan: every adjacent chord pair of every chord-degree PROGRESSION entry. (Bass-
    // and melody-line skeletons are LINE degrees, not chord-root sequences, so they
    // are outside isLicensedProgression's domain — declared; substitution entries have
    // no skeleton.)
    std::set<std::pair<std::string, int>> failing;
    for (const Entry& e : vocab.entries()) {
        if (e.kind != EntryKind::Progression || e.skeleton.kind != SkeletonKind::ChordDegrees) {
            continue;
        }
        const std::vector<ChordDegreeStep>& steps = e.skeleton.chordSteps;
        for (std::size_t i = 0; i + 1 < steps.size(); ++i) {
            // Realise the key-relative degrees at tonic = C (0); quality carried for the
            // applied-resolution sub-predicate.
            ProgressionChord from{ steps[i].degreeOffset,     steps[i].triadQuality };
            ProgressionChord to{   steps[i + 1].degreeOffset, steps[i + 1].triadQuality };
            if (!isLicensedProgression(from, to)) {
                failing.insert({ e.name, static_cast<int>(i) });
            }
        }
    }

    // (1) Every failure must be a RULED known gap. A failure that is NOT on the list is
    //     a mis-encoded entry OR a new grammar gap — either way, investigate; do NOT
    //     tag around it (D5 stop condition).
    for (const std::pair<std::string, int>& f : failing) {
        EXPECT_TRUE(knownGaps.count(f) == 1)
            << "UNEXPECTED consistency failure at entry \"" << f.first << "\" pair #" << f.second
            << " — either the entry is MIS-ENCODED (fix the Vocabulary) OR a NEW grammar gap "
               "was found (extend functionprogression / L5 §5.0). Do not tag around it.";
    }
    // (2) Every ruled known gap must still be a real failure. If the §15-12 grammar
    //     completion licenses one, it stops failing ⇒ shrink this list + tighten.
    for (const std::pair<std::string, int>& k : knownGaps) {
        EXPECT_TRUE(failing.count(k) == 1)
            << "STALE known-gap: entry \"" << k.first << "\" pair #" << k.second
            << " now PASSES the grammar — remove it from the known-gap list (the §15-12 "
               "grammar completion has landed) and tighten the test.";
    }
    // (3) The measured counts, pinned.
    EXPECT_EQ(failing.size(), 11u);
    EXPECT_EQ(knownGaps.size(), 11u);
}
