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

#include "composing/analysis/section/jointkeydecision.h"

#include <algorithm>
#include <array>
#include <cstdlib>
#include <limits>

namespace mu::composing::analysis {

namespace {

// File-local helpers carry a jkd* prefix: the Unity/jumbo build concatenates every
// composing/analysis TU into one translation unit, so an unprefixed
// anonymous-namespace name (e.g. pcMod12) would ODR-clash with the same name in a
// sibling file (cadencekeyanchor.cpp / localmodulationdetector.cpp).
inline int jkdPcMod12(int x) noexcept
{
    return ((x % 12) + 12) % 12;
}

/// 12-bit diatonic-collection mask of a key (tonic + major/minor).  Major: the
/// major scale.  Minor: natural minor PLUS the raised leading tone (harmonic
/// minor), so a genuine minor V→i's raised LT is in-collection — identical to the
/// modulation detector's lmdCollectionMask, kept local for the same key-agnostic
/// reason.  Built from (tonic, mode) alone, never a resolved key.
inline uint16_t jkdCollectionMask(int tonicPc, bool isMajor) noexcept
{
    static constexpr int kMajor[]     = { 0, 2, 4, 5, 7, 9, 11 };
    static constexpr int kMinorHarm[] = { 0, 2, 3, 5, 7, 8, 10, 11 }; // natural minor + raised 7
    uint16_t m = 0;
    if (isMajor) {
        for (int d : kMajor) {
            m |= static_cast<uint16_t>(1u << jkdPcMod12(tonicPc + d));
        }
    } else {
        for (int d : kMinorHarm) {
            m |= static_cast<uint16_t>(1u << jkdPcMod12(tonicPc + d));
        }
    }
    return m;
}

/// Fraction of the sounding pitch classes in `mask` that lie INSIDE the key's
/// collection (0..1).  Empty mask ⇒ 0.  The scale/collection prior (design §3.3).
inline double jkdInCollectionFraction(uint16_t mask, int tonicPc, bool isMajor) noexcept
{
    const uint16_t coll = jkdCollectionMask(tonicPc, isMajor);
    int total = 0, inside = 0;
    for (int p = 0; p < 12; ++p) {
        if ((mask >> p) & 1u) {
            ++total;
            if ((coll >> p) & 1u) {
                ++inside;
            }
        }
    }
    return total > 0 ? static_cast<double>(inside) / total : 0.0;
}

/// Is `pc` a diatonic degree of the key (member of its collection)?
inline bool jkdRootDiatonic(int pc, int tonicPc, bool isMajor) noexcept
{
    if (pc < 0) {
        return false;
    }
    return (jkdCollectionMask(tonicPc, isMajor) >> jkdPcMod12(pc)) & 1u;
}

// The standard tertian chord vocabulary, root-relative interval sets — IDENTICAL to
// tools/cc_joint_residual_probe.py TEMPLATES, so the structural CHORD-PINNED test
// here reproduces the probe's PINNED class exactly (a complete, clear, unique
// triad/seventh/sixth ⇒ chord hard-pinned; everything else is chord-ambiguous).
struct JkdTemplate { std::array<int, 4> iv; int n; };
constexpr std::array<JkdTemplate, 14> kJkdTemplates = { {
    { { 0, 4, 7, 0 }, 3 },  // Major
    { { 0, 3, 7, 0 }, 3 },  // Minor
    { { 0, 3, 6, 0 }, 3 },  // Dim
    { { 0, 4, 8, 0 }, 3 },  // Aug (symmetric)
    { { 0, 2, 7, 0 }, 3 },  // Sus2
    { { 0, 5, 7, 0 }, 3 },  // Sus4
    { { 0, 4, 7, 10 }, 4 }, // Dom7
    { { 0, 4, 7, 11 }, 4 }, // Maj7
    { { 0, 3, 7, 10 }, 4 }, // Min7
    { { 0, 3, 7, 11 }, 4 }, // MinMaj7
    { { 0, 3, 6, 10 }, 4 }, // HalfDim7
    { { 0, 3, 6, 9 }, 4 },  // Dim7 (symmetric)
    { { 0, 4, 7, 9 }, 4 },  // Maj6
    { { 0, 3, 7, 9 }, 4 },  // Min6
} };

/// CHORD-PINNED ⇔ the sounding pc-set exactly equals exactly ONE (root, template)
/// — a complete, clear, unique vertical sonority (the residual-probe PINNED class).
/// Symmetric dim7/aug (≥2 equal roots), share-tone collisions (≥2 templates),
/// sparse (<3 pcs) and foreign (no template) sets are all chord-AMBIGUOUS.
bool jkdChordPinned(uint16_t mask) noexcept
{
    int popcount = 0;
    for (int p = 0; p < 12; ++p) {
        if ((mask >> p) & 1u) {
            ++popcount;
        }
    }
    if (popcount < 3) {
        return false;   // sparse — cannot determine a triad
    }
    int matches = 0;
    for (const JkdTemplate& t : kJkdTemplates) {
        for (int root = 0; root < 12; ++root) {
            uint16_t tm = 0;
            for (int k = 0; k < t.n; ++k) {
                tm |= static_cast<uint16_t>(1u << jkdPcMod12(root + t.iv[static_cast<size_t>(k)]));
            }
            if (tm == mask) {
                if (++matches > 1) {
                    return false;
                }
            }
        }
    }
    return matches == 1;
}

/// A key/mode state in the global key-path lattice.
struct KeyState {
    int tonicPc = 0;
    bool isMajor = true;
    bool operator==(const KeyState& o) const noexcept
    {
        return tonicPc == o.tonicPc && isMajor == o.isMajor;
    }
};

// J-key-iii production wiring flag.  Default OFF ⇒ byte-identical baseline.  The
// default is seeded from the MUSE_JOINT_KEY_WIRING env var at static-init so a test
// binary (pipeline_snapshot_tests / notation_tests) can exercise the wired bridge
// path WITHOUT a src/notation test-harness edit; setJointKeyWiringEnabled (called by
// batch_analyze's explicit --joint-key-wiring flag) overrides it per process.
bool g_jkdWiringEnabled = []() {
    const char* e = std::getenv("MUSE_JOINT_KEY_WIRING");
    return e && (*e == '1' || *e == 't' || *e == 'T' || *e == 'y' || *e == 'Y');
}();

} // namespace

void setJointKeyWiringEnabled(bool enabled) { g_jkdWiringEnabled = enabled; }
bool jointKeyWiringEnabled() { return g_jkdWiringEnabled; }

JointKeyResult
decideJointKey(const std::vector<JointKeyRegionInput>& regions,
               int keySignatureFifths,
               const JointKeyWeights& w)
{
    JointKeyResult result;
    const int n = static_cast<int>(regions.size());
    if (n == 0) {
        return result;
    }

    // ── Committed key-agnostic evidence: anchor + modulation spans ──────────────
    // Reuse the SAME instruments the cadence/modulation diagnostics use, built from
    // the SAME key-agnostic CadenceRegionInput stream.  The decision integrates them
    // as SOFT evidence; it never reads the production resolved key.
    std::vector<CadenceRegionInput> cad;
    cad.reserve(regions.size());
    for (const JointKeyRegionInput& r : regions) {
        CadenceRegionInput ci;
        ci.startTick = r.startTick;
        ci.endTick = r.endTick;
        ci.rootPc = r.rootPc;
        ci.quality = r.quality;
        ci.pitchClassMask = r.pitchClassMask;
        ci.endsPhrase = r.endsPhrase;
        cad.push_back(ci);
    }
    const ModulationDetectionResult mod = detectLocalModulations(cad, keySignatureFifths);
    result.anchor = mod.anchor;
    result.modulationSpanCount = static_cast<int>(mod.spans.size());

    // ── Signature relative pair = the HARD home backbone (J-key-i strong-signature-
    // backbone).  major tonic pc = (fifths·7) mod 12; relative minor = +9 (a minor
    // third below).  These two states are the ONLY non-modulation-span key states the
    // producer emits: the home pair is hard-pruned from the NOTATED signature.  Its
    // safety ceiling — partial/Dorian signatures whose fifths ≠ the DCML key
    // (~17%/56 stems, bwv254/265) — is structurally excluded and is the documented,
    // ratified residual that MATCHES production, not recovered here (J-key-i §6a/§7).
    // (The J-key-ii global-soften — note-inferred collection-fit/local-aggregate
    // candidates ∪ a 0.30 signature prior — is SUPERSEDED: it shrank the soft win
    // and regressed Default/Baroque S2; restoring this strong backbone is what
    // reproduces the ratified +3.80/+3.50/+12.24 pp profile.) ─────────────────────
    const int homeMajorTonic = jkdPcMod12(keySignatureFifths * 7);
    const int homeMinorTonic = jkdPcMod12(homeMajorTonic + 9);

    // ── Key-state lattice: the signature home pair ∪ committed modulation-span
    // states (the few keys the piece actually visits — NOT all 24).  The home pair is
    // first so ties resolve to the home reading (the J-key-i hard-fifths tie-break).
    // The committed cadence ANCHOR stays a SOFT emission bonus only (never a standalone
    // candidate state — its V→IV/subdominant over-detection would inject a phantom
    // subdominant key; J-key-i §10.5). ────────────────────────────────────────────
    std::vector<KeyState> states;
    auto addState = [&](const KeyState& ks) {
        KeyState n{ jkdPcMod12(ks.tonicPc), ks.isMajor };
        if (std::find(states.begin(), states.end(), n) == states.end()) {
            states.push_back(n);
        }
    };
    addState({ homeMajorTonic, true });    // index 0 — preferred on exact ties
    addState({ homeMinorTonic, false });   // index 1
    for (const LocalKeySpan& s : mod.spans) {
        addState({ jkdPcMod12(s.tonicPc), !s.minorMode });
    }
    const int S = static_cast<int>(states.size());

    // Echo the lattice for the safety instrument (DCML-key representability).  Under
    // the J-key-i strong backbone this is the signature home pair (index 0/1) ∪ the
    // committed modulation-span states.
    result.latticeStates.reserve(states.size());
    for (const KeyState& ks : states) {
        result.latticeStates.push_back({ ks.tonicPc, ks.isMajor });
    }

    // ── Per-region structural flags + coverage (for scope + coupling). ───────────
    std::vector<char> coveredBySpan(n, 0);
    for (int i = 0; i < n; ++i) {
        for (const LocalKeySpan& s : mod.spans) {
            if (s.startTick <= regions[i].startTick && regions[i].startTick < s.endTick) {
                coveredBySpan[i] = 1;
                break;
            }
        }
    }

    // ── Soft per-region emission for a key state (config A: steps 1-3). ───────────
    // ADDITIVE re-rank of the hard survivors — there is no early-out / disqualify on
    // any soft term, so no soft score can veto a hard fact (the −7-wall-in-reverse
    // safety property; design §3/§4/§7).
    auto emissionA = [&](int i, const KeyState& k) -> double {
        const JointKeyRegionInput& r = regions[i];
        double s = 0.0;
        // scale / collection prior
        s += w.scalePrior * jkdInCollectionFraction(r.pitchClassMask, k.tonicPc, k.isMajor);
        // existing analyzeKeyMode local candidate (SOFT prior)
        for (const JointKeyLocalCandidate& lc : r.localCandidates) {
            if (jkdPcMod12(lc.tonicPc) == k.tonicPc && lc.isMajor == k.isMajor) {
                s += w.localPrior * lc.confidence;
                break;
            }
        }
        // cadence anchor (SOFT)
        if (mod.anchor.detected
            && jkdPcMod12(mod.anchor.tonicPc) == k.tonicPc
            && (!mod.anchor.minorMode) == k.isMajor) {
            s += w.cadenceAnchor;
        }
        // local-modulation hypothesis (SOFT) — a committed span covering region i
        for (const LocalKeySpan& sp : mod.spans) {
            if (sp.startTick <= r.startTick && r.startTick < sp.endTick
                && jkdPcMod12(sp.tonicPc) == k.tonicPc && (!sp.minorMode) == k.isMajor) {
                s += w.modulation;
                break;
            }
        }
        // bass-is-root tonic cue (SOFT)
        if (r.bassPc >= 0 && jkdPcMod12(r.bassPc) == k.tonicPc) {
            s += w.bassIsRootTonic;
        }
        // declared-mode hint (SOFT) — applies to the signature relative pair only
        if (r.declaredModeKnown
            && ((k.tonicPc == homeMajorTonic && k.isMajor)
                || (k.tonicPc == homeMinorTonic && !k.isMajor))
            && (k.isMajor == !r.declaredModeMinor)) {
            s += w.declaredHint;
        }
        return s;
    };

    // ── Scoped-joint coupling (config B): on coupled regions, reward the key under
    // which the highest-ranked chord candidate is diatonic (chord×key co-decided). ─
    auto couplingScore = [&](int i, const KeyState& k) -> double {
        const JointKeyRegionInput& r = regions[i];
        for (size_t idx = 0; idx < r.chordAlts.size(); ++idx) {
            if (jkdRootDiatonic(r.chordAlts[idx].rootPc, k.tonicPc, k.isMajor)) {
                // winner full, then a mild rank decay (2nd 0.7, 3rd 0.4, floor 0.1)
                const double decay = std::max(0.1, 1.0 - 0.3 * static_cast<double>(idx));
                return w.couplingBonus * decay;
            }
        }
        return 0.0;
    };

    // Per-region coupled flag (chord-ambiguous AND key-modulation-ambiguous).
    std::vector<char> chordPinnedV(n, 0), keyAmbiguousV(n, 0), coupledV(n, 0);
    for (int i = 0; i < n; ++i) {
        chordPinnedV[i] = jkdChordPinned(regions[i].pitchClassMask) ? 1 : 0;
        const bool nearSpan = coveredBySpan[i]
                              || (i > 0 && coveredBySpan[i - 1])
                              || (i + 1 < n && coveredBySpan[i + 1]);
        keyAmbiguousV[i] = nearSpan ? 1 : 0;
        coupledV[i] = (!chordPinnedV[i] && keyAmbiguousV[i]) ? 1 : 0;
    }

    // ── Viterbi over the key-state lattice (the global key path). ────────────────
    // Transition cost = 0 to stay, −transitionPenalty to switch keys (the modulation
    // penalty across regions; design §3.3).  `withJoint` selects emission A vs B.
    const double NEG_INF = -std::numeric_limits<double>::infinity();
    auto decode = [&](bool withJoint, std::vector<KeyState>& out) {
        out.assign(n, KeyState{});
        std::vector<std::vector<double>> dp(n, std::vector<double>(S, NEG_INF));
        std::vector<std::vector<int>> back(n, std::vector<int>(S, -1));
        // NB: 'emit' is a Qt macro (expands to nothing) — name this 'emitScore'.
        auto emitScore = [&](int i, int sIdx) -> double {
            double e = emissionA(i, states[static_cast<size_t>(sIdx)]);
            if (withJoint && coupledV[i]) {
                e += couplingScore(i, states[static_cast<size_t>(sIdx)]);
            }
            return e;
        };
        for (int s = 0; s < S; ++s) {
            dp[0][s] = emitScore(0, s);
        }
        for (int i = 1; i < n; ++i) {
            for (int s = 0; s < S; ++s) {
                double best = NEG_INF;
                int bestPrev = -1;
                for (int p = 0; p < S; ++p) {
                    const double cand = dp[i - 1][p] + (p == s ? 0.0 : -w.transitionPenalty);
                    if (cand > best) {           // strict > ⇒ lower-index prev wins ties
                        best = cand;
                        bestPrev = p;
                    }
                }
                dp[i][s] = emitScore(i, s) + best;
                back[i][s] = bestPrev;
            }
        }
        // terminal argmax (strict > ⇒ home-major(0)/home-minor(1) preferred on ties)
        int bestS = 0;
        double bestV = dp[n - 1][0];
        for (int s = 1; s < S; ++s) {
            if (dp[n - 1][s] > bestV) {
                bestV = dp[n - 1][s];
                bestS = s;
            }
        }
        for (int i = n - 1; i >= 0; --i) {
            out[static_cast<size_t>(i)] = states[static_cast<size_t>(bestS)];
            if (i > 0) {
                bestS = back[i][bestS];
            }
        }
    };

    std::vector<KeyState> softPath, jointPath;
    decode(/*withJoint=*/false, softPath);
    decode(/*withJoint=*/true, jointPath);

    // ── Assemble the per-region decisions + provenance. ──────────────────────────
    result.decisions.resize(static_cast<size_t>(n));
    for (int i = 0; i < n; ++i) {
        JointKeyDecision& d = result.decisions[static_cast<size_t>(i)];
        d.startTick = regions[i].startTick;
        d.endTick = regions[i].endTick;
        d.softTonicPc = softPath[i].tonicPc;
        d.softIsMajor = softPath[i].isMajor;
        d.jointTonicPc = jointPath[i].tonicPc;
        d.jointIsMajor = jointPath[i].isMajor;
        d.prodTonicPc = regions[i].prodTonicPc;
        d.prodIsMajor = regions[i].prodIsMajor;
        d.chordPinned = chordPinnedV[i] != 0;
        d.keyAmbiguous = keyAmbiguousV[i] != 0;
        d.keyHardPinned = !coveredBySpan[i];
        d.coupled = coupledV[i] != 0;
        d.jointChanged = !(softPath[i] == jointPath[i]);
        d.homeMajorTonicPc = homeMajorTonic;
        d.homeMinorTonicPc = homeMinorTonic;

        // provenance: did the config-A winner draw the anchor / modulation bonus?
        const KeyState& kw = softPath[i];
        d.anchorContributed = mod.anchor.detected
                              && jkdPcMod12(mod.anchor.tonicPc) == kw.tonicPc
                              && (!mod.anchor.minorMode) == kw.isMajor;
        for (const LocalKeySpan& sp : mod.spans) {
            if (sp.startTick <= regions[i].startTick && regions[i].startTick < sp.endTick
                && jkdPcMod12(sp.tonicPc) == kw.tonicPc && (!sp.minorMode) == kw.isMajor) {
                d.modulationContributed = true;
                break;
            }
        }

        if (d.coupled) {
            ++result.coupledCount;
        }
        if (d.keyHardPinned) {
            ++result.hardPinnedCount;
        }
    }

    return result;
}

} // namespace mu::composing::analysis
