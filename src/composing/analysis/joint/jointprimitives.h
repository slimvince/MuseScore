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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTPRIMITIVES_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTPRIMITIVES_H

#include <cmath>
#include <cstddef>
#include <cstdint>
#include <optional>
#include <string>
#include <vector>

#include "labelclass.h"

// The joint estimator's shared pitch/chord/label PRIMITIVES — the C++ port of the fit-layer
// generators' own functions (TOTAL UNIFICATION #6: the Python decode reuses them, so does
// this port), namely:
//   gen_note_tables:  member_pcs, chord_factor_pcs, note_category, spelling_bin,
//                     _spelling_parent, _framework_and_root, _chord_root, _split_degree,
//                     _emit_display, _emit_context_chain, the collections and templates.
//   gen_label_tables: _collection_fifths, _fold_fifths_diff, _cof_distance, _key_change_kind,
//                     _beat_class, _t1_ctx_chain, _t1_outcome_parent, _t3_entry_parent,
//                     _t4_ctx_chain, _relation_cell, _applied_rel_parent, _target_head_rest,
//                     _family_key_of, _PC_TO_FIFTHS, the pooling sigils.
// These are pure functions of their arguments; every value is established byte-for-byte against
// the pinned Python by the primitive unit tests. Reuses the sanctioned dependency-free pitch
// primitive normalizePc (chord/analysisutils.h); no legacy L2/L3/L4/L5 analysis is touched.
//
// Spec: cowork_joint_estimator_factorization.md §3; probe_decoder.py / gen_note_tables.py /
// gen_label_tables.py.

namespace mu::composing::analysis::joint {
// A 12-bit pitch-class set (bit pc set) — the C++ form of a Python frozenset of pcs.
using PcMask = uint16_t;

// NEUMAIER (Kahan-Babuska) compensated summation over `n` doubles in the given order — the C++ mirror
// of Python's builtin sum() on floats (CPython 3.12+ uses exactly this compensated algorithm). Every
// place the pinned Python decoder sums floats with sum() (weighted_content; the emission-floor
// denominator) MUST use this, not a naive accumulation, or the C++ result drifts ~1 ULP and breaks
// decode parity with the reference (#16). /fp:precise (the build default) preserves the compensation.
// REPRODUCIBILITY COUPLING (recorded in the parity artifacts' provenance too): the C++ decode's
// bit-identity to the Python reference RESTS on CPython's sum() staying Neumaier-compensated. If a
// future Python version changes sum()'s algorithm, this mirror would no longer match and the decode
// parity would break — which is exactly how such a change should surface (a loud parity failure, not a
// silent drift). Re-mirror this function against the new sum() and re-stamp the parity references then.
inline double neumaierSum(const double* xs, std::size_t n)
{
    double s = 0.0, c = 0.0;
    for (std::size_t i = 0; i < n; ++i) {
        const double x = xs[i];
        const double t = s + x;
        if (std::fabs(s) >= std::fabs(x)) {
            c += (s - t) + x;
        } else {
            c += (x - t) + s;
        }
        s = t;
    }
    return s + c;
}

// The ordered chord factor: role ("root"/"third"/"fifth"/"seventh") and its pitch class.
struct ChordFactor {
    std::string role;
    int pc;
};

// The tonicized framework a class is read in, plus its chord root (gen_note_tables.
// _framework_and_root). `hasRoot` is false for a chromatic class (AugSixth/Neapolitan — special
// member content, no standard root/third/fifth); `valid` is false for an unmappable class.
struct Framework {
    bool valid = false;
    int fwTonic = 0;
    bool fwMajor = true;
    bool hasRoot = false;
    int root = 0;
};

// ── shared string helper (one definition — the joint module's TUs share a Unity build) ──
bool startsWith(const std::string& s, const std::string& prefix);

// ── constants ─────────────────────────────────────────────────────────────────────────
// gen_label_tables._PC_TO_FIFTHS: pc -> signed circle-of-fifths position.
int pcToFifths(int pc);

// probe_decoder._PC_KEYNAME: pc -> canonical fewest-accidental spelling (C, Db, D, ...). The ONE
// source of this map in the module (#6): consumed by the decoder's key string (jointdecoder.keyString)
// AND the presentation chord symbol (jointrender.jointChordSymbol). `pc` is normalized to 0..11.
const std::string& pcKeyName(int pc);

// The pooling sigils (gen_label_tables); guillemets are UTF-8, matching the committed table keys.
extern const std::string kBase;          // "BASE"
extern const std::string kPoolInvfree;   // "«invfree» "
extern const std::string kPoolFamily;    // "«family» "
extern const std::string kRel;           // "«rel»"
extern const std::string kRelResolve;    // "«rel»resolve"
extern const std::string kRelElsewhere;  // "«rel»elsewhere"

// ── chord content (gen_note_tables) ─────────────────────────────────────────────────────
Framework frameworkAndRoot(const LabelClass& cls, int tonic, bool isMajor);
/// member_pcs: the realized chord-member pc set, or nullopt if unmappable.
std::optional<PcMask> memberPcs(const LabelClass& cls, int tonic, bool isMajor);
/// chord_factor_pcs: ordered (role, pc), or nullopt for a chromatic/unmappable class.
std::optional<std::vector<ChordFactor> > chordFactorPcs(const LabelClass& cls, int tonic, bool isMajor);
/// note_category: "member" / "within" / "outside".
std::string noteCategory(int pc, PcMask mem, int tonic, bool isMajor);
/// The local key's diatonic collection as a pc mask (major scale / composite minor).
PcMask keyCollectionMask(int tonic, bool isMajor);

// ── notated key-signature fifths + tonal spelling (notation output-surface contract §3.2) ──────
// (tonic, mode) -> the notated key-signature fifths, enharmonic spelling nearest `referenceFifths`.
// A MODULE-LOCAL reimplementation that duplicates keymodeanalyzer::keySignatureFifthsForKey (the
// legacy key analyzer) — it cannot be reused without including keymodeanalyzer.h and breaking the
// joint module's L1-only isolation (#7/OI-180); the two unify when the legacy key analyzer retires.
int keySignatureFifths(int tonicPc, bool isMajor, int referenceFifths);

// The chord ROOT's line-of-fifths tonal spelling (C=0, +1 = a perfect fifth up — == note_events'
// `lof` = tpc - Tpc::TPC_C), derived from (key, degree/class); std::nullopt for an unmappable class.
// The chromatic classes (applied targets, Neapolitan, augmented-sixth) follow their standard
// theory spellings. See the definition for the full per-degree/per-mode derivation. Its pitch class
// (7*lof mod 12) equals the decoder's root pc by construction (chordRoot).
std::optional<int> rootSpellingLof(const LabelClass& cls, int tonicPc, bool isMajor, int referenceFifths);

// A chord FACTOR's line-of-fifths spelling given the root's lof and the factor/root pitch classes:
// rootLof + the canonical spelling of the tertian interval (factorPc - rootPc). std::nullopt when
// that interval is not a tertian chord-factor interval (unison/third/fifth/seventh).
std::optional<int> factorSpellingLof(int rootLof, int rootPc, int factorPc);

// ── spelling (gen_note_tables) ──────────────────────────────────────────────────────────
std::string spellingBin(int rel, bool isMajor);
/// _spelling_parent: the back-off parent of a spelling cell, or nullopt for BASE (terminal).
std::optional<std::string> spellingParent(const std::string& cell);

// ── emission covariate keying (gen_note_tables) ─────────────────────────────────────────
/// _emit_display of (metricClass, approach, departure, tied).
std::string emitDisplay(const std::string& mc, const std::string& ap, const std::string& dp, bool tied);
/// _emit_context_chain of the same covariate combo (the back-off level keys).
std::vector<std::string> emitContextChain(const std::string& mc, const std::string& ap,
                                           const std::string& dp, bool tied);

// ── key arithmetic (gen_label_tables) ───────────────────────────────────────────────────
int collectionFifths(int tonic, bool isMajor);
int foldFifthsDiff(int d);
int cofDistance(int a, int b);
std::string keyChangeKind(int ta, bool ma, int tb, bool mb);

// ── table-key back-off chains (gen_label_tables) ────────────────────────────────────────
std::vector<std::string> t1CtxChain(const LabelClass& fromCls);
std::vector<std::string> t4CtxChain(const std::string& deg, const std::string& qual, const std::string& mode);

// A back-off "node": either a class (the first outcome) or a pooled-bucket string (its parents).
struct Node {
    bool isClass = false;
    LabelClass cls;
    std::string str;
    std::string keyStr() const { return isClass ? cls.key() : str; }
    static Node ofClass(const LabelClass& c) { Node n; n.isClass = true; n.cls = c; return n; }
    static Node ofStr(const std::string& s) { Node n; n.isClass = false; n.str = s; return n; }
};

/// _t1_outcome_parent / _t3_entry_parent / _applied_rel_parent: the pooled parent of a node, or
/// nullopt when there is no proper parent (a self-referential BASE, or a terminal relation cell).
std::optional<std::string> t1OutcomeParent(const Node& node);
std::optional<std::string> t3EntryParent(const Node& node);
std::optional<std::string> appliedRelParent(const Node& node);

/// _relation_cell: continuation `b`'s relation to applied chord `a`'s target.
std::string relationCell(const LabelClass& a, const LabelClass& b);
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTPRIMITIVES_H
