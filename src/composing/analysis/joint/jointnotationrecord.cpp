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

#include "jointnotationrecord.h"

#include <array>

#include "jointembeddedartifacts.h"   // §2 provenance constants (Decision D1 — dormancy discharged)
#include "jointrender.h"              // the §3.2/§5.6 presentation derivations (single-sourced, Task 1)

namespace mu::composing::analysis::joint {

// ── §3.2 derived: (tonic, mode) -> notated key-signature fifths ───────────────────────────────────
// MODULE-LOCAL reimplementation of keymodeanalyzer::keySignatureFifthsForKey (the legacy key
// analyzer). It is duplicated, not reused, because keymodeanalyzer.h drags in the legacy L3/L4 key
// machinery and the joint module reads ONLY the L1/L1.5 fact surface + the sanctioned dependency-free
// primitives (#7/OI-180). The two unify when the legacy key analyzer retires (the OI-180 map).
//
// Derivation (the circle-of-fifths key signatures):
//   * a MAJOR key's signature is the circle-of-fifths position of its tonic (Ionian);
//   * a MINOR key shares its RELATIVE MAJOR's signature — Aeolian's parent Ionian is tonic + 3
//     semitones (A minor -> C major, +3 = 0 mod 12);
//   * the three enharmonic tonics (Db/C#, Gb/F#, Cb/B) have TWO valid signatures (±); the spelling
//     nearest the notated reference signature is chosen (|opt - ref| minimized, ties -> the first).
// The per-Ionian-pc table below is the standard key-signature accidental count (sharps +, flats -).
int recordKeySignatureFifths(int tonicPc, bool isMajor, int referenceFifths)
{
    const int ionianPc = isMajor ? (((tonicPc % 12) + 12) % 12)
                                 : ((((tonicPc + 3) % 12) + 12) % 12);   // minor -> relative-major Ionian
    // (Ionian pc) -> {primary, enharmonic-alternate} signature fifths.
    static const std::array<std::array<int, 2>, 12> kOpts = { {
        { {  0,  0 } },   // 0  C
        { {  7, -5 } },   // 1  C# / Db
        { {  2,  2 } },   // 2  D
        { { -3, -3 } },   // 3  Eb
        { {  4,  4 } },   // 4  E
        { { -1, -1 } },   // 5  F
        { {  6, -6 } },   // 6  F# / Gb
        { {  1,  1 } },   // 7  G
        { { -4, -4 } },   // 8  Ab
        { {  3,  3 } },   // 9  A
        { { -2, -2 } },   // 10 Bb
        { {  5, -7 } },   // 11 B / Cb
    } };
    const std::array<int, 2>& o = kOpts[static_cast<size_t>(ionianPc)];
    const int d0 = o[0] - referenceFifths, d1 = o[1] - referenceFifths;
    return (std::abs(d0) <= std::abs(d1)) ? o[0] : o[1];
}

// ── §3.2 derived: the class-native diatonicToKey answer ───────────────────────────────────────────
// TRUE iff the class is a plain diatonic-degree chord of the key's mode. A purely STRUCTURAL read of
// the class — never a pitch-collection recomputation (the OI-173 lesson: that had four inequivalent
// definitions). The joint state's degree is expressed relative to (tonic, mode), so:
//   * an applied/secondary chord (target non-empty) is chromatic to the home key -> false;
//   * the augmented-sixth and Neapolitan families are chromatic predefined sonorities -> false;
//   * a degree carrying an explicit ♭/♯ accidental (e.g. "bVII") is a chromatic inflection of the
//     mode's own diatonic degree -> false;
//   * an UNaltered degree ("I".."VII") sits on the mode's own diatonic scale (major or minor, incl.
//     the harmonic/melodic-minor leading-tone forms the decoder resolves) -> true.
bool recordDiatonicToKey(const LabelClass& cls)
{
    if (!cls.target().empty()) {
        return false;                                   // applied / secondary
    }
    const std::string& q = cls.quality();
    if (q == "AugSixth" || q == "Neapolitan") {
        return false;                                   // chromatic predefined family
    }
    const std::string& d = cls.degreeBase();
    if (!d.empty() && (d[0] == 'b' || d[0] == '#')) {
        return false;                                   // chromatically-altered degree
    }
    return true;
}

// ── §3.2 derived: the augmented-sixth display sub-type from the SOUNDING content ──────────────────
// The fitted vocabulary collapsed the augmented-sixth family to Italian pitch content (2 corpus
// tokens), so the class cannot carry Italian/German/French — it is read from the pitch classes
// SOUNDING over the segment. All three share the ♭6̂ bass and the ♯4̂; the DISTINGUISHING added tone is
// the fourth voice (relative to the local tonic t):
//   * German adds ♭3̂ = (t + 3) — the perfect fifth above the ♭6̂ bass  -> "German"
//   * French adds  2̂ = (t + 2)                                          -> "French"
//   * neither -> "Italian" (only ♭6̂, 1̂, ♯4̂)
// German is tested first (its added tone is the more common and the ♭3̂/2̂ distinction is exclusive in
// the standard chord). Empty for a non-AugSixth segment; the caller only invokes it for AugSixth.
std::string recordAugSixthSubType(const Piece& piece, int i, int j, int tonicPc)
{
    if (i < 0 || j <= i || j > static_cast<int>(piece.events.size())) {
        return std::string();
    }
    const PcMask sounding = piece.overlapPcs(i, j);
    const int t = ((tonicPc % 12) + 12) % 12;
    const bool hasFlat3 = (sounding >> (((t + 3) % 12))) & 1u;
    const bool has2 = (sounding >> (((t + 2) % 12))) & 1u;
    if (hasFlat3) {
        return "German";
    }
    if (has2) {
        return "French";
    }
    return "Italian";
}

// ── the assembly ──────────────────────────────────────────────────────────────────────────────────
namespace {
// The factor role of `bassPc` among the ordered chord factors, or "" when it is not a member (or the
// class carries no standard factors — a chromatic AugSixth/Neapolitan whose chordFactorPcs is null).
std::string bassFactorRole(const ChordInfo& info, std::optional<int> bassPc)
{
    if (!bassPc.has_value() || !info.fac.has_value()) {
        return std::string();
    }
    for (const ChordFactor& f : *info.fac) {
        if (f.pc == *bassPc) {
            return f.role;
        }
    }
    return std::string();
}
} // namespace

NotationRecord assembleNotationRecord(const Piece& piece, const DecodeResult& result,
                                      std::optional<int> sigFifths, const std::string& declaredMode,
                                      const FittedAdapter& adapter, const Vocabulary& vocab,
                                      ChordCache& cache)
{
    NotationRecord rec;
    rec.stem = piece.stem;

    // §3.1 piece block ────────────────────────────────────────────────────────────────────────────
    if (!piece.events.empty()) {
        rec.spanStartTick = piece.events.front().start;
        rec.spanEndTick = piece.events.back().end;
    }
    rec.sigFifths = sigFifths;
    rec.declaredMode = declaredMode;
    // §2 provenance — the compiled-in D1 embedded constants (discharges their declared dormancy).
    for (const embedded::EmbeddedBlob* b : embedded::kTableArtifacts) {
        rec.provenance.tableArtifacts.emplace_back(std::string(b->name), std::string(b->sha256));
    }
    rec.provenance.weightVectorIdentity = embedded::kWeightVectorIdentity;
    rec.provenance.decoderVersion = embedded::kDecoderVersion;
    rec.provenance.corpusGitHash = embedded::kCorpusGitHash;

    // the reference for the enharmonic key-signature spelling: the notated initial signature (0 when
    // no signature is notated — C major / A minor).
    const int sigRef = sigFifths.has_value() ? *sigFifths : 0;

    // §3.2 committed segments + derived chord facts ───────────────────────────────────────────────
    rec.segments.reserve(result.segments.size());
    for (const SegmentSummary& s : result.segments) {
        RecordSegment rs;
        // committed reading, verbatim
        rs.startTick = s.startTick;
        rs.endTick = s.endTick;
        rs.tonicPc = s.tonicPc;
        rs.isMajor = s.isMajor;
        rs.key = s.key;
        rs.classKey = s.classKey;
        rs.degree = s.degree;
        rs.quality = s.quality;
        rs.inversion = s.inversion;
        rs.target = s.target;
        rs.rootPc = s.rootPc;

        const LabelClass* cls = vocab.find(s.classKey);
        const LabelClass resolved = cls ? *cls : classFromKey(s.classKey);
        const ChordInfo& info = cache.get(resolved, s.tonicPc, s.isMajor);

        // derived facts
        rs.keySignatureFifths = recordKeySignatureFifths(s.tonicPc, s.isMajor, sigRef);
        rs.memberPcs = info.mem;
        if (info.fac.has_value()) {
            rs.members = *info.fac;
        }
        rs.chordSymbol = jointChordSymbol(info.root, resolved.quality());
        rs.diatonicToKey = recordDiatonicToKey(resolved);

        // per-event bass facts over [i, j)
        const bool hasSeventh = info.fac.has_value() && info.fac->size() == 4;
        for (int e = s.i; e < s.j && e >= 0 && e < static_cast<int>(piece.evBass.size()); ++e) {
            EventBassFact bf;
            bf.eventIndex = e;
            bf.bassPc = piece.evBass[e];
            bf.role = bassFactorRole(info, piece.evBass[e]);
            rs.bassPerEvent.push_back(std::move(bf));
        }
        // the Roman numeral uses the FIRST event's bass role (the batch-render form, §5.6 continuity).
        const std::optional<int> firstBass =
            (s.i >= 0 && s.i < static_cast<int>(piece.evBass.size())) ? piece.evBass[s.i] : std::nullopt;
        rs.romanNumeral = jointRenderRn(resolved, bassFactorRole(info, firstBass), hasSeventh);

        if (resolved.quality() == "AugSixth") {
            rs.augSixthSubType = recordAugSixthSubType(piece, s.i, s.j, s.tonicPc);
        }

        rec.segments.push_back(std::move(rs));
    }

    // §3.3 group (i) — the established posterior slice (attached, NOT recomputed inline).
    rec.slices = computePosteriorSlice(piece, result.segments, adapter, vocab, cache);

    return rec;
}

} // namespace mu::composing::analysis::joint
