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
#include "progressionrecognizer.h"

#include <algorithm>

namespace mu::composing::analysis::progression {

// ── §0 idiom indexing + the max-over-IdiomSet rule ─────────────────────────────

std::size_t idiomIndex(Idiom idiom)
{
    const uint8_t bit = static_cast<uint8_t>(idiom);
    for (std::size_t i = 0; i < kIdiomCount; ++i) {
        if (bit == (1u << i)) {
            return i;
        }
    }
    return kIdiomCount;  // not a single-bit Idiom value — skipped by callers
}

double maxWeightOverIdioms(const IdiomWeights& w, IdiomSet idioms)
{
    double best = 0.0;
    bool any = false;
    for (std::size_t i = 0; i < kIdiomCount; ++i) {
        if ((idioms & static_cast<IdiomSet>(1u << i)) != 0) {
            if (!any || w[i] > best) {
                best = w[i];
                any = true;
            }
        }
    }
    return any ? best : 0.0;  // §4.5: the MAX over the set, never the sum; empty set → 0
}

// ── §4.5 phase 2 — the discovered mixture ──────────────────────────────────────

namespace {

/// Normalise a five-vector to sum 1; a zero vector falls back to the equal seed.
IdiomWeights normaliseToUnit(const std::array<double, kIdiomCount>& v)
{
    double sum = 0.0;
    for (double x : v) {
        sum += x;
    }
    if (sum <= 0.0) {
        return kEqualSeed;
    }
    IdiomWeights out{};
    for (std::size_t i = 0; i < kIdiomCount; ++i) {
        out[i] = v[i] / sum;
    }
    return out;
}

} // namespace

IdiomWeights blendIdiomWeights(const IdiomWeights& seed,
                               const IdiomEvidenceHistogram& histogram,
                               double blendRate)
{
    const IdiomWeights seedNorm = normaliseToUnit(seed);

    double evidence = 0.0;  // E — the total idiom-evidence mass (raw, pre-normalisation)
    for (double x : histogram) {
        evidence += x;
    }
    if (evidence <= 0.0) {
        return seedNorm;  // §4.5: no recognised evidence ⇒ w = seed
    }

    // α = E / (E + blendRate): 0 at E = 0, → 1 as E → ∞ (the §4.5 direction). blendRate
    // is the declared-default rate; a non-positive rate degenerates to α = 1 (histogram).
    const double alpha = (blendRate > 0.0) ? evidence / (evidence + blendRate) : 1.0;
    const IdiomWeights histNorm = normaliseToUnit(histogram);

    IdiomWeights w{};
    for (std::size_t i = 0; i < kIdiomCount; ++i) {
        w[i] = (1.0 - alpha) * seedNorm[i] + alpha * histNorm[i];
    }
    return w;
}

// ── §4.5 phase 3 — the prior strength ──────────────────────────────────────────

double recognitionPriorStrength(double matchScore, const IdiomWeights& w, IdiomSet idioms,
                                bool modeContradicts, bool chordsOnly,
                                const RecognitionParams& params)
{
    double prior = matchScore * maxWeightOverIdioms(w, idioms);  // §4.5: match × MAX(w over IdiomSet)
    if (modeContradicts) {
        prior *= params.modeCueFactor;   // §4.5 mode cue (< 1, never 0)
    }
    if (chordsOnly) {
        prior *= params.chordsOnlyFactor;  // §4.5 D7 chords-only (< 1)
    }
    return prior;
}

// ── §4.3 the F-B contradiction predicate + contribution assembler ──────────────

bool memberContradictsCommittedReading(int memberRootPc, ChordQuality memberQuality,
                                       int committedRootPc, ChordQuality committedQuality)
{
    return memberRootPc != committedRootPc || memberQuality != committedQuality;
}

CommittedOverrideContribution
overrideContributionFor(int position, int committedRootPc, ChordQuality committedQuality,
                        int memberRootPc, ChordQuality memberQuality,
                        double priorStrength, double compositeConfidence,
                        const std::string& schemaName)
{
    CommittedOverrideContribution c;
    c.position = position;
    c.committedRootPc = committedRootPc;
    c.committedQuality = committedQuality;
    c.memberRootPc = memberRootPc;         // the member's realisation — the SELECTION (an existing reading)
    c.memberQuality = memberQuality;
    c.priorStrength = priorStrength;       // enters the F-B contradiction quantity
    c.compositeConfidence = compositeConfidence;  // the §8 threshold-scaling input (Layer 5 decides firing)
    c.schemaName = schemaName;
    return c;
}

int selectCandidateFillingMember(const std::vector<CandidateReading>& candidates,
                                 int memberRootPc, ChordQuality memberQuality)
{
    for (std::size_t i = 0; i < candidates.size(); ++i) {
        if (candidates[i].rootPc == memberRootPc && candidates[i].quality == memberQuality) {
            return static_cast<int>(i);  // the first candidate that fills the member
        }
    }
    return -1;
}

// ── The §4 recognition ─────────────────────────────────────────────────────────

namespace {

int pcMod12(int pc)
{
    return ((pc % 12) + 12) % 12;
}

/// Does the entry's Mode tag contradict the local key's mode at the recognised span?
/// (§4.5 mode cue — Mode::Both never contradicts; "modes mix", the factor is < 1.)
bool modeContradictsLocalKey(Mode entryMode, bool localMinorMode)
{
    if (entryMode == Mode::Major) {
        return localMinorMode;
    }
    if (entryMode == Mode::Minor) {
        return !localMinorMode;
    }
    return false;  // Mode::Both
}

/// One admitted recognition, paired with its §4.5 prior strength.
struct Admitted {
    const VocabularyCandidate* cand = nullptr;
    double prior = 0.0;
};

/// The anchor pitch class of a recognition — the root of its first covered chord.
/// The §4.6 transposition step is the difference of successive anchors.
int anchorRootPc(const CommittedProgression& progression, const VocabularyCandidate& c)
{
    if (c.spanStart < 0 || c.spanStart >= static_cast<int>(progression.size())) {
        return -1;
    }
    return progression[static_cast<size_t>(c.spanStart)].chord.rootPc;
}

} // namespace

ProgressionRecognitionOutput
recognizeProgressions(const CommittedProgression& progression,
                      const HarmonicVocabulary& vocabulary,
                      const IdiomWeights& seed,
                      IdiomSet idiomSubset,
                      const RecognitionParams& params)
{
    ProgressionRecognitionOutput out;
    out.weights = seed;
    if (progression.empty()) {
        return out;  // §3: nothing in, nothing out
    }

    // ── §4.5 phase 1: weight-free recognition over the committed progression ────
    // Reuse the Vocabulary's recognise (the one matcher). Build its span from each
    // position's recognise-query chord — the committed reading, or the caller's
    // top-ranked candidate at an abstained position.
    VocabularySpan span;
    span.reserve(progression.size());
    for (const CommittedChord& cc : progression) {
        span.push_back(cc.chord);
    }
    const std::vector<VocabularyCandidate> recognitions = vocabulary.recognise(span, idiomSubset);

    // ── §4.5 phase 2: estimate the mixture from the idiom-evidence histogram ────
    // Phase 2's input is phase-1 output ONLY (never phase-3's) — forward-only.
    IdiomEvidenceHistogram histogram{};
    for (const VocabularyCandidate& c : recognitions) {
        if (!c.entry) {
            continue;
        }
        for (std::size_t i = 0; i < kIdiomCount; ++i) {
            if ((c.entry->idioms & static_cast<IdiomSet>(1u << i)) != 0) {
                histogram[i] += c.matchScore;  // contribute the match score to every idiom in the set
            }
        }
    }
    out.weights = blendIdiomWeights(seed, histogram, params.blendRate);

    // ── §4.5 phase 3: weight, admit, and emit ──────────────────────────────────
    std::vector<Admitted> admitted;
    admitted.reserve(recognitions.size());
    for (const VocabularyCandidate& c : recognitions) {
        if (!c.entry) {
            continue;
        }
        const int spanStart = c.spanStart;
        const bool localMinor = progression[static_cast<size_t>(spanStart)].chord.localMinorMode;
        const bool modeContra = modeContradictsLocalKey(c.entry->mode, localMinor);
        const bool chordsOnly = c.entry->voiceLeadingDefined;  // D7
        const double prior = recognitionPriorStrength(c.matchScore, out.weights, c.entry->idioms,
                                                      modeContra, chordsOnly, params);
        if (prior <= params.admissionThreshold) {
            continue;  // §4.5 admission: STRICTLY above the floor; carry all that pass
        }
        admitted.push_back(Admitted{ &c, prior });
    }

    // ── §4.4 the annotation: one progression-schema-span per admitted recognition ─
    for (const Admitted& a : admitted) {
        const VocabularyCandidate& c = *a.cand;
        ProgressionSchemaSpan s;
        s.name = c.entry->name;
        s.idioms = c.entry->idioms;
        s.startIndex = c.spanStart;
        s.endIndex = c.spanEnd;
        s.startTick = progression[static_cast<size_t>(c.spanStart)].startTick;
        s.endTick = progression[static_cast<size_t>(c.spanEnd - 1)].endTick;
        s.matchScore = c.matchScore;
        s.priorStrength = a.prior;
        s.chordsOnly = c.entry->voiceLeadingDefined;  // D7 mark
        for (const SubstitutedMember& m : c.substitutedMembers) {
            SchemaSubstitution ss;
            ss.position = m.spanIndex;
            ss.substitution = m.substitution;
            ss.readOut = m.mapping;
            s.substitutedMembers.push_back(ss);
        }
        out.schemaSpans.push_back(std::move(s));
    }
    // §4.1 overlap preference: prefer the longer span, then the more specific entry
    // (carry ALL — a recognition is evidence, not an exclusive claim; this only orders).
    std::stable_sort(out.schemaSpans.begin(), out.schemaSpans.end(),
        [&](const ProgressionSchemaSpan& x, const ProgressionSchemaSpan& y) {
            const int lx = x.endIndex - x.startIndex;
            const int ly = y.endIndex - y.startIndex;
            if (lx != ly) {
                return lx > ly;  // longer first
            }
            // specificity comes from the entry; recover it via the admitted list order is
            // unnecessary — length ties break by start index (a stable, span-local order).
            return x.startIndex < y.startIndex;
        });

    // ── §4.3 the evidence contribution (both conditions, SELECTION-only) ─────────
    for (const Admitted& a : admitted) {
        const VocabularyCandidate& c = *a.cand;
        // Chord-quality members exist only for a chord-degree skeleton; a bass/melody
        // line member is a line degree, not a chord — no §4.3 chord evidence (declared).
        if (c.entry->skeleton.kind != SkeletonKind::ChordDegrees) {
            continue;
        }
        const std::vector<ChordDegreeStep>& steps = c.entry->skeleton.chordSteps;
        for (int p = c.spanStart; p < c.spanEnd; ++p) {
            const std::size_t stepIdx = static_cast<std::size_t>(p - c.spanStart);
            if (stepIdx >= steps.size()) {
                break;
            }
            const CommittedChord& pos = progression[static_cast<size_t>(p)];

            // Is this covered position a substituted member? (§4.2: the sub is recorded,
            // NOT overridden — excluded from the F-B override path.)
            bool substituted = false;
            for (const SubstitutedMember& m : c.substitutedMembers) {
                if (m.spanIndex == p) {
                    substituted = true;
                    break;
                }
            }

            if (pos.committed) {
                // §4.3 committed path — the F-B override contribution. The LITERAL member
                // demand comes from the entry step; a substituted member is §4.2-excluded.
                if (substituted) {
                    continue;
                }
                const int memberRootPc = pcMod12(pos.chord.localTonicPc + steps[stepIdx].degreeOffset);
                const ChordQuality memberQuality = steps[stepIdx].triadQuality;
                if (memberContradictsCommittedReading(memberRootPc, memberQuality,
                                                      pos.chord.rootPc, pos.chord.quality)) {
                    out.overrides.push_back(
                        overrideContributionFor(p, pos.chord.rootPc, pos.chord.quality,
                                                memberRootPc, memberQuality,
                                                a.prior, pos.compositeConfidence, c.entry->name));
                }
            } else {
                // §4.3 abstained path — the §5.5 functional-plausibility feature. The
                // reading that fills the member is the reading that matched (the surface —
                // the committed-query chord at this position). SELECTION-only: name the
                // ranked candidate that fills it, weight by the prior.
                AbstainedFeature f;
                f.position = p;
                f.memberRootPc = pos.chord.rootPc;
                f.memberQuality = pos.chord.quality;
                f.weight = a.prior;
                f.selectedCandidateIndex =
                    selectCandidateFillingMember(pos.rankedCandidates, pos.chord.rootPc, pos.chord.quality);
                f.schemaName = c.entry->name;
                out.abstainedFeatures.push_back(std::move(f));
            }
        }
    }

    // ── §4.6 harmonic sequences (ALWAYS emitted — evidence never discarded) ──────
    // A sequence = a run of ≥2 non-overlapping recognitions of the SAME entry at a
    // constant nonzero transposition of the anchor root (the pattern repeated
    // transposed — a Monte/Fonte/descending-fifths chain). Detected over the ADMITTED
    // recognitions (a below-threshold recognition is not evidence). Declared shape;
    // a single recognition of an internally-sequential entry is NOT a repeat (report).
    {
        // Group admitted by entry, ordered by covered start; scan each group for runs.
        std::vector<const Admitted*> byEntry;
        byEntry.reserve(admitted.size());
        for (const Admitted& a : admitted) {
            byEntry.push_back(&a);
        }
        std::stable_sort(byEntry.begin(), byEntry.end(),
            [](const Admitted* x, const Admitted* y) {
                if (x->cand->entry != y->cand->entry) {
                    return x->cand->entry < y->cand->entry;  // group by entry (stable)
                }
                return x->cand->spanStart < y->cand->spanStart;  // then by covered start
            });

        std::size_t i = 0;
        while (i < byEntry.size()) {
            std::size_t j = i + 1;
            // Grow a same-entry, non-overlapping, constant-step run starting at i.
            int runStep = 0;
            std::size_t runEnd = i;  // last index in the current run
            double runPrior = byEntry[i]->prior;
            while (j < byEntry.size() && byEntry[j]->cand->entry == byEntry[runEnd]->cand->entry) {
                const VocabularyCandidate& prev = *byEntry[runEnd]->cand;
                const VocabularyCandidate& next = *byEntry[j]->cand;
                if (next.spanStart < prev.spanEnd) {
                    break;  // overlaps the previous member of the run — not successive
                }
                const int ap = anchorRootPc(progression, prev);
                const int an = anchorRootPc(progression, next);
                if (ap < 0 || an < 0) {
                    break;
                }
                const int step = pcMod12(an - ap);
                if (step == 0) {
                    break;  // no transposition — not a sequence
                }
                if (runEnd == i) {
                    runStep = step;  // the run's constant step is set by its first gap
                } else if (step != runStep) {
                    break;  // the step changed — the run ends here
                }
                runPrior = std::max(runPrior, byEntry[j]->prior);
                runEnd = j;
                ++j;
            }

            if (runEnd > i) {  // ≥2 recognitions with a constant nonzero step
                const VocabularyCandidate& first = *byEntry[i]->cand;
                const VocabularyCandidate& last = *byEntry[runEnd]->cand;
                HarmonicSequence hs;
                hs.name = first.entry->name;
                hs.transpositionStep = runStep;
                hs.startIndex = first.spanStart;
                hs.endIndex = last.spanEnd;
                hs.startTick = progression[static_cast<size_t>(first.spanStart)].startTick;
                hs.endTick = progression[static_cast<size_t>(last.spanEnd - 1)].endTick;
                hs.repetitions = static_cast<int>(runEnd - i) + 1;  // matched windows in the run (≥2)
                hs.priorStrength = runPrior;
                out.sequences.push_back(std::move(hs));
                i = runEnd + 1;
            } else {
                ++i;
            }
        }
    }

    return out;
}

} // namespace mu::composing::analysis::progression
