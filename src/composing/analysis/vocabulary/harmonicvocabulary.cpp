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
#include "harmonicvocabulary.h"

#include <algorithm>

#include "composing/analysis/chord/chordanalyzer.h"   // Extension, hasExtension — the seventh bits

namespace mu::composing::analysis {

// ── Style-family helpers (the §12.1 leaves; expand the §5 bracket labels) ─────

// The §5 style bracket labels map COARSELY onto the small preset-aligned tag set
// {Baroque, Jazz, Default}: common-practice (incl. galant/Romantic) → {Baroque, Default};
// jazz → {Jazz}; vernacular/pop → {Default} (the general config).
std::vector<StyleTag> commonPracticeStyles()
{
    return { StyleTag::Baroque, StyleTag::Default };
}

std::vector<StyleTag> jazzStyles()
{
    return { StyleTag::Jazz };
}

std::vector<StyleTag> vernacularStyles()
{
    return { StyleTag::Default };
}

std::vector<StyleTag> allStyleTags()
{
    return { StyleTag::Baroque, StyleTag::Jazz, StyleTag::Default };
}

// ── FunctionalSkeleton ────────────────────────────────────────────────────────

int FunctionalSkeleton::length() const
{
    return kind == SkeletonKind::ChordDegrees
           ? static_cast<int>(chordSteps.size())
           : static_cast<int>(lineSteps.size());
}

int FunctionalSkeleton::specificity() const
{
    if (kind == SkeletonKind::ChordDegrees) {
        int s = 0;
        for (const ChordDegreeStep& step : chordSteps) {
            s += 2;  // degree + triad quality, always constrained
            if (step.seventh != SeventhRequirement::Unspecified) {
                s += 1;  // a specified seventh is an extra constraint
            }
        }
        return s;
    }
    // a line step constrains only its degree
    return static_cast<int>(lineSteps.size());
}

namespace {

// ── Authoring helpers (readability of the in-code catalog, build decision 1) ──

// The §5 bracket labels, expanded to the §12.1 leaves. "[all styles]".
std::vector<StyleTag> allStyles()        { return allStyleTags(); }
// "[common-practice + jazz]".
std::vector<StyleTag> commonAndJazz()
{
    std::vector<StyleTag> v = commonPracticeStyles();
    for (StyleTag t : jazzStyles()) { v.push_back(t); }
    return v;
}

ChordDegreeStep cd(int degreeOffset, ChordQuality q,
                   SeventhRequirement s = SeventhRequirement::Unspecified)
{
    return ChordDegreeStep{ degreeOffset, q, s };
}

LineDegreeStep ld(int degreeOffset) { return LineDegreeStep{ degreeOffset }; }

FunctionalSkeleton chordSkeleton(std::vector<ChordDegreeStep> steps)
{
    FunctionalSkeleton sk;
    sk.kind = SkeletonKind::ChordDegrees;
    sk.chordSteps = std::move(steps);
    return sk;
}

FunctionalSkeleton lineSkeleton(SkeletonKind kind, std::vector<LineDegreeStep> steps)
{
    FunctionalSkeleton sk;
    sk.kind = kind;  // BassLine or MelodyLine
    sk.lineSteps = std::move(steps);
    return sk;
}

Entry progression(std::string name, std::vector<StyleTag> tags,
                  FunctionalSkeleton sk, std::string provenance)
{
    Entry e;
    e.name = std::move(name);
    e.styleTags = std::move(tags);
    e.kind = EntryKind::Progression;
    e.skeleton = std::move(sk);
    e.provenance = std::move(provenance);
    return e;
}

Entry substitution(std::string name, std::vector<StyleTag> tags,
                    SubstitutionType type, std::string rule,
                    std::string underlying, std::string provenance)
{
    Entry e;
    e.name = std::move(name);
    e.styleTags = std::move(tags);
    e.kind = EntryKind::Substitution;
    e.substitution = SubstitutionMapping{ type, std::move(rule), std::move(underlying) };
    e.provenance = std::move(provenance);
    return e;
}

// Quality shorthands for the catalog.
constexpr ChordQuality Maj = ChordQuality::Major;
constexpr ChordQuality Min = ChordQuality::Minor;
constexpr ChordQuality Dim = ChordQuality::Diminished;
constexpr ChordQuality Aug = ChordQuality::Augmented;
constexpr ChordQuality HD  = ChordQuality::HalfDiminished;
constexpr SeventhRequirement S7min = SeventhRequirement::Minor;
constexpr SeventhRequirement S7maj = SeventhRequirement::Major;
constexpr SeventhRequirement S7dim = SeventhRequirement::Diminished;

// ── Matching primitives ───────────────────────────────────────────────────────

int pcOffset(int pc, int tonicPc)
{
    if (pc < 0) {
        return -1;
    }
    return ((pc - tonicPc) % 12 + 12) % 12;
}

bool hasAnySeventh(uint32_t ext)
{
    return hasExtension(ext, Extension::MinorSeventh)
           || hasExtension(ext, Extension::MajorSeventh)
           || hasExtension(ext, Extension::DiminishedSeventh);
}

bool seventhSatisfied(uint32_t ext, SeventhRequirement req)
{
    switch (req) {
    case SeventhRequirement::Unspecified: return true;
    case SeventhRequirement::None:        return !hasAnySeventh(ext);
    case SeventhRequirement::Minor:       return hasExtension(ext, Extension::MinorSeventh);
    case SeventhRequirement::Major:       return hasExtension(ext, Extension::MajorSeventh);
    case SeventhRequirement::Diminished:  return hasExtension(ext, Extension::DiminishedSeventh);
    }
    return false;
}

// Does a span chord LITERALLY realise a chord-degree step (key-relative, exact)?
bool literalChordMatch(const SpanChord& c, const ChordDegreeStep& step)
{
    return pcOffset(c.rootPc, c.localTonicPc) == step.degreeOffset
           && c.quality == step.triadQuality
           && seventhSatisfied(c.extensions, step.seventh);
}

// Is the span chord a dominant-seventh a TRITONE from the step's dominant — i.e. the
// tritone substitution of a Major-triad (dominant) step? (subV7 for V7, spec §5.3.) This
// is the ONE substitution operation v1 drives recognise's substitution-awareness with (a
// concrete, exact, key-relative degree transform — no fuzzy threshold). The surface root
// sits a tritone (+6) from the underlying dominant and carries a minor seventh.
bool tritoneSubMatch(const SpanChord& c, const ChordDegreeStep& step)
{
    if (step.triadQuality != ChordQuality::Major) {
        return false;  // tritone sub replaces a DOMINANT (Major-triad) step only
    }
    const int surfaceOffset = (step.degreeOffset + 6) % 12;
    return pcOffset(c.rootPc, c.localTonicPc) == surfaceOffset
           && c.quality == ChordQuality::Major
           && hasExtension(c.extensions, Extension::MinorSeventh);
}

// The diatonic scale-degree set (semitone offsets) for a local mode.
bool isDiatonicDegree(int offset, bool minorMode)
{
    if (offset < 0) {
        return false;
    }
    if (minorMode) {
        // natural minor + the harmonic-minor raised leading tone (11)
        switch (offset) {
        case 0: case 2: case 3: case 5: case 7: case 8: case 10: case 11: return true;
        default: return false;
        }
    }
    switch (offset) {  // major
    case 0: case 2: case 4: case 5: case 7: case 9: case 11: return true;
    default: return false;
    }
}

} // namespace

// ── The seed catalog (the §5 first-pass content, in-code) ─────────────────────
//
// Degree offsets are semitones above the local tonic. Major-key entries use the major
// degrees (I=0 ii=2 iii=4 IV=5 V=7 vi=9 viio=11; ♭II=1 ♭III=3 ♭VI=8 ♭VII=10); minor-key
// entries use the minor degrees (i=0 ii°=2 III=3 iv=5 V=7 VI=8 VII=10 viio=11). Encoded
// faithfully from the spec; not invented beyond it (provenance discipline, spec §8). Where
// a schema is conventionally defined by voice-leading/melody, only the HARMONIC or BASS
// pattern is held (spec §2/§5.2); the voice-leading dimension lives elsewhere.

HarmonicVocabulary::HarmonicVocabulary()
{
    auto& E = m_entries;

    const std::string ramos =
        "Ramos, Mapping Tonal Harmony (mDecks) — the function map / secondary & substitute apparatus";
    const std::string caplin = "Common-practice cadence theory (Caplin); reused by L5 §5.2";
    const std::string jazzReharm = "Jazz reharmonization literature (tritone sub, modal interchange, related ii–V)";
    const std::string gjerdingen = "Gjerdingen, Music in the Galant Style; Katsiavalos (ISMIR 2019)";
    const std::string popLoops = "Common-practice & pop bass-line / loop conventions";

    // ── §5.2 Cadential [common-practice + jazz] (overlap L5 §5.2 — listed for completeness) ──
    E.push_back(progression("Authentic cadence (V–I)", commonAndJazz(),
        chordSkeleton({ cd(7, Maj), cd(0, Maj) }), caplin));
    E.push_back(progression("Authentic cadence, minor (V–i)", commonAndJazz(),
        chordSkeleton({ cd(7, Maj), cd(0, Min) }), caplin));
    E.push_back(progression("Deceptive cadence (V–vi)", commonAndJazz(),
        chordSkeleton({ cd(7, Maj), cd(9, Min) }), caplin));
    E.push_back(progression("Deceptive cadence, minor (V–♭VI)", commonAndJazz(),
        chordSkeleton({ cd(7, Maj), cd(8, Maj) }), caplin));
    E.push_back(progression("Plagal cadence (IV–I)", commonAndJazz(),
        chordSkeleton({ cd(5, Maj), cd(0, Maj) }), caplin));
    E.push_back(progression("Phrygian half cadence, minor (iv6–V)", commonPracticeStyles(),
        chordSkeleton({ cd(5, Min), cd(7, Maj) }), caplin));

    // ── §5.2 The ii–V family [jazz + common-practice] ──
    E.push_back(progression("ii–V–I (common-practice, triads)", commonAndJazz(),
        chordSkeleton({ cd(2, Min), cd(7, Maj), cd(0, Maj) }), caplin));
    E.push_back(progression("IIm7–V7–Imaj7 (major ii–V–I)", commonAndJazz(),
        chordSkeleton({ cd(2, Min, S7min), cd(7, Maj, S7min), cd(0, Maj, S7maj) }), ramos));
    E.push_back(progression("iiø7–V7–i (minor ii–V–i)", commonAndJazz(),
        chordSkeleton({ cd(2, HD), cd(7, Maj, S7min), cd(0, Min) }), ramos));
    E.push_back(progression("Incomplete ii–V (no resolution)", jazzStyles(),
        chordSkeleton({ cd(2, Min, S7min), cd(7, Maj, S7min) }), jazzReharm));

    // ── §5.2 Turnarounds [jazz] ──
    E.push_back(progression("Turnaround I–vi–ii–V", jazzStyles(),
        chordSkeleton({ cd(0, Maj), cd(9, Min), cd(2, Min), cd(7, Maj) }), jazzReharm));
    E.push_back(progression("Turnaround I–VI7–ii–V", jazzStyles(),
        chordSkeleton({ cd(0, Maj), cd(9, Maj, S7min), cd(2, Min), cd(7, Maj) }), jazzReharm));
    E.push_back(progression("Turnaround iii–vi–ii–V", jazzStyles(),
        chordSkeleton({ cd(4, Min), cd(9, Min), cd(2, Min), cd(7, Maj) }), jazzReharm));
    E.push_back(progression("Rhythm-changes A-section (I–VI7–IIm7–V7)", jazzStyles(),
        chordSkeleton({ cd(0, Maj, S7maj), cd(9, Maj, S7min), cd(2, Min, S7min), cd(7, Maj, S7min) }),
        jazzReharm));

    // ── §5.2 Sequences [common-practice + jazz] ──
    E.push_back(progression("Circle-of-fifths (full, I–IV–viio–iii–vi–ii–V–I)", commonAndJazz(),
        chordSkeleton({ cd(0, Maj), cd(5, Maj), cd(11, Dim), cd(4, Min),
                        cd(9, Min), cd(2, Min), cd(7, Maj), cd(0, Maj) }), ramos));
    E.push_back(progression("Circle-of-fifths (iii–vi–ii–V–I)", commonAndJazz(),
        chordSkeleton({ cd(4, Min), cd(9, Min), cd(2, Min), cd(7, Maj), cd(0, Maj) }), ramos));
    E.push_back(progression("Descending-thirds (I–vi–IV–ii)", commonAndJazz(),
        chordSkeleton({ cd(0, Maj), cd(9, Min), cd(5, Maj), cd(2, Min) }), ramos));

    // ── §5.2 Bass-line and pop loops [common-practice + pop] ──
    // Lament bass / descending tetrachord (minor): held as the BASS line 1̂–♭7̂–♭6̂–5̂.
    // (The chromatic 5-note variant is a voice-leading elaboration — declared, not a
    // distinct v1 skeleton.)
    E.push_back(progression("Lament bass (descending tetrachord, minor)", commonPracticeStyles(),
        lineSkeleton(SkeletonKind::BassLine, { ld(0), ld(10), ld(8), ld(7) }), popLoops));
    E.push_back(progression("Andalusian cadence (i–♭VII–♭VI–V)", commonPracticeStyles(),
        chordSkeleton({ cd(0, Min), cd(10, Maj), cd(8, Maj), cd(7, Maj) }), popLoops));
    E.push_back(progression("Doo-wop (I–vi–IV–V)", vernacularStyles(),
        chordSkeleton({ cd(0, Maj), cd(9, Min), cd(5, Maj), cd(7, Maj) }), popLoops));
    E.push_back(progression("Axis (I–V–vi–IV)", vernacularStyles(),
        chordSkeleton({ cd(0, Maj), cd(7, Maj), cd(9, Min), cd(5, Maj) }), popLoops));
    E.push_back(progression("Pachelbel (I–V–vi–iii–IV–I–IV–V)", commonPracticeStyles(),
        chordSkeleton({ cd(0, Maj), cd(7, Maj), cd(9, Min), cd(4, Min),
                        cd(5, Maj), cd(0, Maj), cd(5, Maj), cd(7, Maj) }), popLoops));

    // ── §5.2 Galant schemata — harmonic / bass pattern only [galant] ──
    // Prinner: melody 6̂–5̂–4̂–3̂ OVER bass 4̂–3̂–2̂–1̂ — held by its BASS line (the melody is
    // voice-leading, held elsewhere; the bass is the matchable harmonic pattern, decision 3).
    E.push_back(progression("Prinner (bass 4̂–3̂–2̂–1̂)", commonPracticeStyles(),
        lineSkeleton(SkeletonKind::BassLine, { ld(5), ld(4), ld(2), ld(0) }), gjerdingen));
    E.push_back(progression("Romanesca (I–V–vi–iii)", commonPracticeStyles(),
        chordSkeleton({ cd(0, Maj), cd(7, Maj), cd(9, Min), cd(4, Min) }), gjerdingen));
    // Do-Re-Mi: an OPENING defined by the melody 1̂–2̂–3̂ — held as a MELODY line (carried for
    // completeness; v1 cannot match a melody against a committed-chord span — declared).
    E.push_back(progression("Do-Re-Mi (melody 1̂–2̂–3̂)", commonPracticeStyles(),
        lineSkeleton(SkeletonKind::MelodyLine, { ld(0), ld(2), ld(4) }), gjerdingen));
    // Monte (ascending) / Fonte (descending) — sequences of applied-resolution pairs; the
    // harmonic pattern (an approximation of the voice-leading schema, spec §5.2).
    E.push_back(progression("Monte (ascending, V7/IV–IV–V7/V–V)", commonPracticeStyles(),
        chordSkeleton({ cd(0, Maj, S7min), cd(5, Maj), cd(2, Maj, S7min), cd(7, Maj) }), gjerdingen));
    E.push_back(progression("Fonte (descending, V7/ii–ii–V7/I–I)", commonPracticeStyles(),
        chordSkeleton({ cd(9, Maj, S7min), cd(2, Min), cd(7, Maj, S7min), cd(0, Maj) }), gjerdingen));

    // ── §5.2 Advanced jazz cycles [jazz] ──
    E.push_back(progression("Backdoor (♭VII7–I)", jazzStyles(),
        chordSkeleton({ cd(10, Maj, S7min), cd(0, Maj, S7maj) }), jazzReharm));
    // Coltrane changes — a major-thirds KEY cycle; held as the three M3-related tonics
    // (I–♭VI–III as key centres). The full ii–V realisation spans modulations — encoded as
    // the defining tonic cycle (declared as a representative, modulation-spanning entry).
    E.push_back(progression("Coltrane changes (major-thirds tonic cycle)", jazzStyles(),
        chordSkeleton({ cd(0, Maj, S7maj), cd(8, Maj, S7maj), cd(4, Maj, S7maj) }), jazzReharm));

    // ── §5.3 Substitution operations ──
    E.push_back(substitution("Secondary dominant / tonicization", commonAndJazz(),
        SubstitutionType::SecondaryDominant,
        "Tonicize any diatonic x with V7/x or viio7/x.", "V7/x or viio7/x of x", ramos));
    E.push_back(substitution("Related ii–V", jazzStyles(),
        SubstitutionType::RelatedIiV,
        "Precede any V7/x (or subV7/x) with its IIm7.", "IIm7 of x's dominant", jazzReharm));
    E.push_back(substitution("Tritone substitution (subV)", jazzStyles(),
        SubstitutionType::TritoneSub,
        "Replace any dominant V7/x with subV7/x (a tritone away).",
        "subV7/x stands for V7/x", jazzReharm));
    E.push_back(substitution("Diatonic (functional) substitution", commonAndJazz(),
        SubstitutionType::DiatonicFunctional,
        "Replace a chord with a same-function diatonic chord sharing tones (I↔iii↔vi, IV↔ii, V↔viio).",
        "a same-function diatonic chord", ramos));
    E.push_back(substitution("Modal interchange", allStyles(),
        SubstitutionType::ModalInterchange,
        "Substitute a parallel-mode chord (in major borrow iv, iiø7, ♭VI, ♭VII, ♭III, ♭II, v, viio7).",
        "the parallel-mode counterpart", ramos));
    E.push_back(substitution("Diminished approach", commonAndJazz(),
        SubstitutionType::DiminishedApproach,
        "Insert a passing/auxiliary diminished seventh between diatonic chords (I–#io7–ii).",
        "a passing diminished seventh", jazzReharm));
    E.push_back(substitution("Deceptive resolution", commonAndJazz(),
        SubstitutionType::DeceptiveResolution,
        "Resolve a dominant to a non-tonic (V→vi, V→♭VI).", "a non-tonic resolution of V", caplin));
    E.push_back(substitution("Line cliché", commonAndJazz(),
        SubstitutionType::LineCliche,
        "A chromatic inner line over a held chord (i–i(maj7)–i7–i6); the line is voice-leading, held elsewhere.",
        "a held chord with a chromatic inner line", jazzReharm));
    // NOTE: upper-structure / voicing substitution is explicitly OUT (spec §5.3) — a
    // voicing, not a function — so it is intentionally NOT a catalog entry.
}

// ── Style filtering ───────────────────────────────────────────────────────────

namespace {

bool inActiveStyles(const Entry& e, const std::vector<StyleTag>& subset)
{
    for (StyleTag tag : e.styleTags) {
        if (std::find(subset.begin(), subset.end(), tag) != subset.end()) {
            return true;
        }
    }
    return false;
}

void rankCandidates(std::vector<VocabularyCandidate>& cands)
{
    std::stable_sort(cands.begin(), cands.end(),
        [](const VocabularyCandidate& a, const VocabularyCandidate& b) {
            if (a.matchScore != b.matchScore) {
                return a.matchScore > b.matchScore;
            }
            const int sa = a.entry ? a.entry->skeleton.specificity() : 0;
            const int sb = b.entry ? b.entry->skeleton.specificity() : 0;
            if (sa != sb) {
                return sa > sb;  // more specific first
            }
            const int la = a.entry ? a.entry->skeleton.length() : 0;
            const int lb = b.entry ? b.entry->skeleton.length() : 0;
            return la > lb;      // then longer first
        });
}

} // namespace

// ── §4 browse ─────────────────────────────────────────────────────────────────

std::vector<VocabularyCandidate>
HarmonicVocabulary::browse(const std::vector<StyleTag>& styleSubset) const
{
    std::vector<VocabularyCandidate> out;
    for (const Entry& e : m_entries) {
        if (!inActiveStyles(e, styleSubset)) {
            continue;
        }
        VocabularyCandidate c;
        c.entry = &e;
        c.matchScore = 1.0;  // structural completeness — an enumerated entry
        out.push_back(c);
    }
    rankCandidates(out);
    return out;
}

// ── §4 recognise ──────────────────────────────────────────────────────────────

namespace {

// Try to match a chord-degree skeleton against the span window starting at `start`. On a
// full match, fills `subs` with any substituted members and returns true.
bool matchChordWindow(const VocabularySpan& span, int start,
                      const FunctionalSkeleton& sk, std::vector<SubstitutedMember>& subs)
{
    const int n = static_cast<int>(sk.chordSteps.size());
    for (int i = 0; i < n; ++i) {
        const SpanChord& c = span[static_cast<size_t>(start + i)];
        const ChordDegreeStep& step = sk.chordSteps[static_cast<size_t>(i)];
        if (literalChordMatch(c, step)) {
            continue;
        }
        // Substitution-aware (v1: the tritone substitution — an exact, key-relative
        // degree transform). The LITERAL skeleton is unchanged; the substitution is only
        // recorded as the underlying-function read-out (design §4.2).
        if (tritoneSubMatch(c, step)) {
            SubstitutedMember m;
            m.spanIndex = start + i;
            m.substitution = SubstitutionType::TritoneSub;
            m.mapping = "subV7 here stands for the dominant V7 (tritone substitution)";
            subs.push_back(m);
            continue;
        }
        return false;  // this step neither literal- nor substitution-matched
    }
    return true;
}

// Match a bass-line skeleton against the span window's bass scale-degrees.
bool matchBassWindow(const VocabularySpan& span, int start, const FunctionalSkeleton& sk)
{
    const int n = static_cast<int>(sk.lineSteps.size());
    for (int i = 0; i < n; ++i) {
        const SpanChord& c = span[static_cast<size_t>(start + i)];
        const int bassOffset = pcOffset(c.bassPc, c.localTonicPc);
        if (bassOffset != sk.lineSteps[static_cast<size_t>(i)].degreeOffset) {
            return false;
        }
    }
    return true;
}

} // namespace

std::vector<VocabularyCandidate>
HarmonicVocabulary::recognise(const VocabularySpan& span,
                              const std::vector<StyleTag>& styleSubset) const
{
    std::vector<VocabularyCandidate> out;
    const int spanLen = static_cast<int>(span.size());

    for (const Entry& e : m_entries) {
        if (e.kind != EntryKind::Progression || !inActiveStyles(e, styleSubset)) {
            continue;
        }
        const FunctionalSkeleton& sk = e.skeleton;
        const int len = sk.length();
        if (len == 0 || len > spanLen) {
            continue;
        }
        // MelodyLine skeletons cannot be matched against a committed-chord span (no melody
        // pc) — carried in the catalog, not matchable in v1 (declared).
        if (sk.kind == SkeletonKind::MelodyLine) {
            continue;
        }
        // Every contiguous window of the span of equal length (a schema may be recognised
        // inside a longer span). All plausible matches are carried (a schema is evidence,
        // not an exclusive claim — design §4.1).
        for (int start = 0; start + len <= spanLen; ++start) {
            std::vector<SubstitutedMember> subs;
            bool matched = false;
            if (sk.kind == SkeletonKind::ChordDegrees) {
                matched = matchChordWindow(span, start, sk, subs);
            } else { // BassLine
                matched = matchBassWindow(span, start, sk);
            }
            if (!matched) {
                continue;
            }
            VocabularyCandidate c;
            c.entry = &e;
            c.matchScore = 1.0;  // an exact realisation (structural completeness)
            c.spanStart = start;
            c.spanEnd = start + len;
            c.substitutedMembers = std::move(subs);
            out.push_back(c);
        }
    }
    rankCandidates(out);
    return out;
}

// ── §4 suggest ────────────────────────────────────────────────────────────────

namespace {

// Does the span chord-sequence equal the chord skeleton's prefix [0, spanLen)?
bool spanIsChordPrefix(const VocabularySpan& span, const FunctionalSkeleton& sk)
{
    const int spanLen = static_cast<int>(span.size());
    if (sk.kind != SkeletonKind::ChordDegrees || spanLen >= sk.length()) {
        return false;  // need the entry to be strictly longer (a real continuation)
    }
    for (int i = 0; i < spanLen; ++i) {
        if (!literalChordMatch(span[static_cast<size_t>(i)], sk.chordSteps[static_cast<size_t>(i)])) {
            return false;
        }
    }
    return true;
}

// Does the span chord-sequence equal the chord skeleton's SUFFIX (the last spanLen steps)?
bool spanIsChordSuffix(const VocabularySpan& span, const FunctionalSkeleton& sk)
{
    const int spanLen = static_cast<int>(span.size());
    const int len = sk.length();
    if (sk.kind != SkeletonKind::ChordDegrees || spanLen >= len) {
        return false;
    }
    const int off = len - spanLen;
    for (int i = 0; i < spanLen; ++i) {
        if (!literalChordMatch(span[static_cast<size_t>(i)], sk.chordSteps[static_cast<size_t>(off + i)])) {
            return false;
        }
    }
    return true;
}

// Is a substitution OPERATION structurally applicable to some chord in the span? Structural
// (no threshold), so a span with nothing applicable yields an empty replace (spec §4).
bool substitutionApplies(const Entry& e, const VocabularySpan& span)
{
    for (const SpanChord& c : span) {
        const int off = pcOffset(c.rootPc, c.localTonicPc);
        const bool diatonic = isDiatonicDegree(off, c.localMinorMode);
        const bool isMajorTriad = (c.quality == ChordQuality::Major);
        const bool isTriadMajMin = (c.quality == ChordQuality::Major || c.quality == ChordQuality::Minor);
        switch (e.substitution.type) {
        case SubstitutionType::TritoneSub:
        case SubstitutionType::RelatedIiV:
        case SubstitutionType::DeceptiveResolution:
            if (isMajorTriad) { return true; }       // a dominant-capable chord
            break;
        case SubstitutionType::SecondaryDominant:
            if (diatonic && off != 0) { return true; } // a tonicizable non-tonic degree
            break;
        case SubstitutionType::DiatonicFunctional:
        case SubstitutionType::ModalInterchange:
        case SubstitutionType::DiminishedApproach:
            if (diatonic) { return true; }
            break;
        case SubstitutionType::LineCliche:
            if (isTriadMajMin) { return true; }
            break;
        }
    }
    return false;
}

} // namespace

std::vector<VocabularyCandidate>
HarmonicVocabulary::suggest(const VocabularySpan& span, SuggestDirection direction,
                            const std::vector<StyleTag>& styleSubset) const
{
    std::vector<VocabularyCandidate> out;
    if (span.empty()) {
        return out;
    }

    for (const Entry& e : m_entries) {
        if (!inActiveStyles(e, styleSubset)) {
            continue;
        }
        bool take = false;
        if (direction == SuggestDirection::Replace) {
            take = (e.kind == EntryKind::Substitution) && substitutionApplies(e, span);
        } else if (e.kind == EntryKind::Progression) {
            take = (direction == SuggestDirection::Follow)
                   ? spanIsChordPrefix(span, e.skeleton)
                   : spanIsChordSuffix(span, e.skeleton);
        }
        if (!take) {
            continue;
        }
        VocabularyCandidate c;
        c.entry = &e;
        c.matchScore = 1.0;
        out.push_back(c);
    }
    rankCandidates(out);
    return out;
}

// ── §4 expand — the generative spine (§5.1) ───────────────────────────────────

std::vector<GenerativeSlot>
HarmonicVocabulary::expand(int targetDegreeOffset) const
{
    const int x = ((targetDegreeOffset % 12) + 12) % 12;
    // NB: do NOT name this `slots` — Qt force-includes a `#define slots` keyword macro
    // through the PCH, which would mangle the declaration.
    std::vector<GenerativeSlot> genSlots;

    // V7/x — the secondary dominant: a dominant seventh a perfect fifth above x.
    genSlots.push_back({ "V7/x", cd((x + 7) % 12, ChordQuality::Major, SeventhRequirement::Minor), 1.0 });
    // viio7/x — the secondary leading-tone: a diminished seventh a semitone below x.
    genSlots.push_back({ "viio7/x", cd((x + 11) % 12, ChordQuality::Diminished, SeventhRequirement::Diminished), 1.0 });
    // IIm7/x — the related ii: a minor seventh a major second above x (the applied ii–V).
    genSlots.push_back({ "IIm7/x", cd((x + 2) % 12, ChordQuality::Minor, SeventhRequirement::Minor), 1.0 });
    // subV7/x — the tritone substitute dominant: a dominant seventh a semitone above x.
    genSlots.push_back({ "subV7/x", cd((x + 1) % 12, ChordQuality::Major, SeventhRequirement::Minor), 1.0 });
    // IIm7 of subV7/x — the sub's related ii: a minor seventh a perfect fifth above subV7/x.
    genSlots.push_back({ "IIm7/subV7/x", cd((x + 8) % 12, ChordQuality::Minor, SeventhRequirement::Minor), 1.0 });

    return genSlots;
}

} // namespace mu::composing::analysis
