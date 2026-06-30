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

// ── composing/analysis/vocabulary/harmonicvocabulary ─────────────────────────
//
// THE HARMONIC VOCABULARY — the curated reference catalog of harmonic conventions
// (named chord PROGRESSIONS and chord SUBSTITUTIONS of tonal music), queried by the
// analysis tool (to RECOGNISE a written progression and disambiguate a chord) and a
// future composition tool (to SUGGEST progressions/substitutions). Spec (the
// contract): cowork_progression_schema_dictionary.md. Consumer design (context, NOT
// built here): cowork_progression_schema_design.md. Architecture placement:
// cowork_target_architecture.md §7 / ARCHITECTURE.md §7.
//
// IT IS KNOWLEDGE, NOT A TOOL THAT ACTS (spec §1/§2). It holds the catalog and answers
// the four §4 queries — browse / recognise / suggest / expand — each returning a RANKED
// LIST of candidate entries carrying a structural match score. It DECIDES nothing: the
// matching threshold, the style weighting, and the choice of what to do with a candidate
// are the CONSUMER's (the firewall, spec §6). It keeps NO information about any piece —
// it returns the same answers regardless of what is being analysed, and remembers nothing
// between queries (the query methods are const).
//
// DORMANT (build §4): this module has NO production consumer — nothing in src/ calls it;
// it is reachable only from its own module + its unit tests (harmonicvocabulary_tests.cpp)
// and tools/CMake registration. So adding it is byte-identical on production by
// construction (the L5-step firewall precedent). The recognition CONSUMER (the L5 prior +
// the L6 annotation) is a LATER step (the ratified order: encyclopedia → L6 → wire the
// consumer); it is NOT built here.
//
// REUSE, NOT A PARALLEL ENCODING (build decision 2, the firewall discipline L5 followed):
//   • CHORD QUALITY — the existing analysis::ChordQuality enum (the triad quality) +
//     analysis::Extension bitmask (the seventh type), composed by SeventhRequirement below.
//     No second quality vocabulary.
//   • PAIRWISE MOTION — the licensed-progression content (descending-fifth / descending-
//     third / ascending-second / applied resolution) is functionprogression's predicate
//     domain; the catalog's named progressions are the MULTI-CHORD extension of it.
//   • DEGREE — the skeleton's scale-degree is the CHROMATIC SEMITONE OFFSET from the local
//     tonic, (rootPc − tonicPc) mod 12 ∈ [0,11] — the pitch-class realization of the
//     Roman-numeral degree. This is the SAME root-relative-to-tonic notion
//     region::diatonicDegreeForRootPc computes, kept CHROMATIC (mod 12) rather than folded
//     to a diatonic 0..6, because the catalog needs chromatic degrees (♭II Neapolitan,
//     ♭VI/♭VII modal interchange, subV) that the diatonic-only fold returns −1 for and
//     cannot express. It is plain pitch-class arithmetic (the same primitive
//     functionprogression uses), NOT a second degree enum. (Declared build-decision.)
//
// NO CONSTANTS (build §4): v1 matching is EXACT, key-relative, structural — no weight,
// threshold, or margin. The match score is a structural-completeness value (1.0 for an
// exact realisation; non-exact entries are EXCLUDED). The FUZZY / partial / metric-
// sensitive scoring is precision-phase, DEFERRED to the consumer (spec §4 / design §4.1) —
// it is NOT built here.

#include <cstdint>
#include <string>
#include <vector>

#include "composing/analysis/types/analysistypes.h"   // ChordQuality, Extension is in chord/, see note

namespace mu::composing::analysis {

// ── Style taxonomy — provisional placeholders (build decision 6) ──────────────
//
// A SMALL, REPLACEABLE preset-aligned tag set — the same {Baroque, Jazz, Default} the
// preset system already selects on (Default = the user-run / general config). Entries tag
// MULTI-VALUED (a convention can belong to several presets). The §5 style bracket labels
// ("[all styles]", "[common-practice + jazz]", "[galant]", …) map COARSELY onto these
// three via the family helpers below. The FORMAL hierarchical taxonomy (the §12.1 proposed
// family→style leaves) is a SEPARATE joint decision with the preset system (spec §6/§12.1)
// — this component only carries the labels and is deliberately kept small so the tag type
// is trivially replaced when that taxonomy is ratified; style BEHAVIOR is the consumer's.
enum class StyleTag : uint8_t {
    Baroque,   ///< the common-practice / Baroque preset
    Jazz,      ///< the jazz preset
    Default,   ///< the user-run / general (Standard) config
};

/// The common-practice bracket label, coarsely → {Baroque, Default}.
std::vector<StyleTag> commonPracticeStyles();
/// The jazz bracket label → {Jazz}.
std::vector<StyleTag> jazzStyles();
/// The vernacular/popular bracket label, coarsely → {Default}.
std::vector<StyleTag> vernacularStyles();
/// Every tag — the "[all styles]" bracket label and the default query subset.
std::vector<StyleTag> allStyleTags();

// ── The functional skeleton — a tagged union (build decision 3) ───────────────
//
// A progression entry's skeleton is EITHER a chord-degree sequence (key-relative
// (scale-degree, quality) pairs) OR a bass/melody-line-degree sequence (for the bass-line
// and galant entries — e.g. Prinner's bass 4̂–3̂–2̂–1̂). One representation holds both.

/// The seventh requirement on a chord-degree step. Composes ChordQuality (the triad) with
/// the Extension seventh bits — NOT a parallel quality enum. Most common-practice steps
/// leave it Unspecified (the step constrains only the triad); the jazz entries specify it
/// (IIm7 = Minor triad + Minor seventh; V7 = Major + Minor; Imaj7 = Major + Major;
/// viio7 = Diminished + Diminished). A step that specifies a seventh requires it; an
/// Unspecified step matches a span chord regardless of any seventh it carries (the
/// seventh is then a surface detail the skeleton does not speak to — still EXACT, not fuzzy).
enum class SeventhRequirement : uint8_t {
    Unspecified,   ///< the step constrains only the triad quality
    None,          ///< a bare triad — no seventh present
    Minor,         ///< a minor seventh (dominant seventh on a Major triad; m7 on a Minor triad)
    Major,         ///< a major seventh
    Diminished,    ///< a diminished seventh (Diminished triad + dim7)
};

/// One step of a chord-degree skeleton: a key-relative (scale-degree, quality) pair.
struct ChordDegreeStep {
    int degreeOffset = 0;                              ///< semitones above the tonic, [0,11] (♭II=1, V=7, ♭VII=10)
    ChordQuality triadQuality = ChordQuality::Major;   ///< the triad quality (reused enum)
    SeventhRequirement seventh = SeventhRequirement::Unspecified;
};

/// One step of a bass/melody-LINE skeleton (decision 3): a key-relative scale-degree of
/// the bass (or melody) line, as a chromatic semitone offset from the local tonic. A line
/// is a melodic skeleton — no chord quality. `melodyLine` records whether the line is the
/// MELODY (top) or the BASS (bottom). v1 MATCHES bass lines against the span's bass pitch
/// classes; a melody line is carried for completeness/browse but is NOT chord-span-
/// matchable in v1 (the committed-chord span carries no melody pc — declared build-decision).
struct LineDegreeStep {
    int degreeOffset = 0;   ///< semitones above the tonic, [0,11]
};

enum class SkeletonKind : uint8_t { ChordDegrees, BassLine, MelodyLine };

/// The functional skeleton (the tagged union, decision 3).
struct FunctionalSkeleton {
    SkeletonKind kind = SkeletonKind::ChordDegrees;
    std::vector<ChordDegreeStep> chordSteps;  ///< valid when kind == ChordDegrees
    std::vector<LineDegreeStep>  lineSteps;   ///< valid when kind == BassLine / MelodyLine

    int length() const;
    /// The structural specificity used for ranking (more-constrained → higher): each
    /// chord step counts its degree + triad (+1 if a seventh is specified); each line
    /// step counts its degree. Length is the secondary key.
    int specificity() const;
};

// ── The substitution mapping (substitution entries) ───────────────────────────
//
// A substitution entry is a named OPERATION mapping a substituted SURFACE chord to the
// underlying FUNCTION it replaces (spec §3/§5.3). v1 carries the rule descriptively and,
// for the operations with a concrete key-relative degree transform (tritone sub, diatonic
// functional sub), drives recognise's substitution-aware matching. Upper-structure /
// voicing substitution is explicitly OUT (spec §5.3) — a voicing, not a function.
enum class SubstitutionType : uint8_t {
    SecondaryDominant,   ///< tonicize any diatonic x with V7/x or viio7/x
    RelatedIiV,          ///< precede any V7/x (or subV7/x) with its IIm7
    TritoneSub,          ///< replace any dominant V7/x with subV7/x (a tritone away)
    DiatonicFunctional,  ///< same-function diatonic chord sharing tones (I↔iii↔vi, IV↔ii, V↔viio)
    ModalInterchange,    ///< substitute a parallel-mode chord
    DiminishedApproach,  ///< insert a passing/auxiliary dim7 between diatonic chords
    DeceptiveResolution, ///< resolve a dominant to a non-tonic (V→vi, V→♭VI)
    LineCliche,          ///< a chromatic inner line over a held chord (the line is voice-leading, held elsewhere)
};

struct SubstitutionMapping {
    SubstitutionType type = SubstitutionType::DiatonicFunctional;
    std::string rule;                ///< the surface→underlying rule, human-readable (§3/§5.3)
    std::string underlyingFunction;  ///< the function the surface stands for (e.g. "V7/x")
};

// ── The entry (spec §3) — one catalog record ──────────────────────────────────
enum class EntryKind : uint8_t { Progression, Substitution };

struct Entry {
    std::string name;                  ///< the conventional name
    std::vector<StyleTag> styleTags;   ///< one or more §12.1 leaves (multi-valued)
    EntryKind kind = EntryKind::Progression;
    std::string provenance;            ///< the established source (§11)

    FunctionalSkeleton skeleton;       ///< valid when kind == Progression
    SubstitutionMapping substitution;  ///< valid when kind == Substitution
};

// ── The query span (spec §4) — a contiguous run of committed chords ───────────
//
// "A span ... a contiguous run of one or more committed chords, each chord with its
// decided function and key — the form the analysis tool produces" (spec §4). Each SpanChord
// maps from a Layer-5 FunctionLayerOutput unit (committedIdentity → root/bass/quality/
// extensions) + its region key (localTonicPc / localMinorMode); hand-constructible in tests.
struct SpanChord {
    int rootPc = -1;                                ///< committed root pitch class (0–11)
    int bassPc = -1;                                ///< committed bass pitch class (0–11); for bass-line matching
    ChordQuality quality = ChordQuality::Unknown;   ///< committed triad quality
    uint32_t extensions = 0;                        ///< committed Extension bitmask (the seventh type)
    int localTonicPc = 0;                           ///< the chord's local key tonic pitch class
    bool localMinorMode = false;                    ///< the chord's local key mode (minor vs major)
};
using VocabularySpan = std::vector<SpanChord>;

// ── The query results ─────────────────────────────────────────────────────────

/// A substituted member of a recognised progression (spec §4 recognise: "each with the
/// substitution mapping for any substituted member"; design §4.2: the literal skeleton is
/// unchanged — the substitution is recorded only as the underlying-function read-out).
struct SubstitutedMember {
    int spanIndex = -1;                                    ///< position in the span
    SubstitutionType substitution = SubstitutionType::TritoneSub;
    std::string mapping;                                   ///< e.g. "D♭7 = subV7/I (tritone sub of V)"
};

/// One ranked candidate (browse / recognise / suggest). Carries a match score; the list is
/// ranked by it (then specificity, then length). NEVER a binary match, NEVER a decision
/// (spec §2/§6 — the firewall).
struct VocabularyCandidate {
    const Entry* entry = nullptr;   ///< the matched/offered entry (non-owning; points into the catalog)
    double matchScore = 0.0;        ///< v1: 1.0 for an exact realisation (structural completeness)

    int spanStart = 0;              ///< recognise: the covered span range [start, end)
    int spanEnd = 0;

    std::vector<SubstitutedMember> substitutedMembers;  ///< recognise: the substituted members (may be empty)
};

/// A generative slot produced by expand (spec §4/§5.1) — a secondary/substitute function
/// of a target degree x, instantiated on demand rather than enumerated.
struct GenerativeSlot {
    std::string name;        ///< "V7/x", "viio7/x", "IIm7/x", "subV7/x", "IIm7 of subV7/x"
    ChordDegreeStep chord;   ///< the slot's chord, as a degree offset relative to the home tonic given x
    double matchScore = 1.0; ///< structural completeness — a fully-specified generated slot
};

enum class SuggestDirection : uint8_t { Follow, Precede, Replace };

// ── The component ─────────────────────────────────────────────────────────────
class HarmonicVocabulary
{
public:
    /// Builds the seed catalog (the §5 first-pass content) in-code (build decision 1 — a
    /// plain in-code catalog, no external data file).
    HarmonicVocabulary();

    /// §4 browse — every enumerated entry in the active styles (used to load the active
    /// catalog), ranked by specificity then length.
    std::vector<VocabularyCandidate>
    browse(const std::vector<StyleTag>& styleSubset = allStyleTags()) const;

    /// §4 recognise (the analysis direction) — the progression entries whose functional
    /// skeleton `span` exactly realises (key-relative, substitution-aware), each with the
    /// substitution mapping for any substituted member; ranked. May be empty.
    std::vector<VocabularyCandidate>
    recognise(const VocabularySpan& span,
              const std::vector<StyleTag>& styleSubset = allStyleTags()) const;

    /// §4 suggest (the composition direction) — by direction:
    ///   • Follow  → progression entries that could continue FROM the span (span = a prefix);
    ///   • Precede → progression entries that could lead INTO the span (span = a suffix);
    ///   • Replace → substitution entries applicable to the span, plus same-function
    ///     diatonic alternatives (the DiatonicFunctional entry).
    /// Ranked. May be empty.
    std::vector<VocabularyCandidate>
    suggest(const VocabularySpan& span, SuggestDirection direction,
            const std::vector<StyleTag>& styleSubset = allStyleTags()) const;

    /// §4 expand — the generative slots for target degree `x` (a semitone offset [0,11]):
    /// V7/x, viio7/x, IIm7/x, subV7/x, and the sub's related ii (§5.1). The generative
    /// spine as a function, not enumerated rows.
    std::vector<GenerativeSlot> expand(int targetDegreeOffset) const;

    /// Direct read access to the catalog (for tests / inspection).
    const std::vector<Entry>& entries() const { return m_entries; }

private:
    std::vector<Entry> m_entries;
};

} // namespace mu::composing::analysis
