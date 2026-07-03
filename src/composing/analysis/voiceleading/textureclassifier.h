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

// ── composing/analysis/voiceleading — VL-C: TEXTURE CLASSIFICATION (axis 2) ────
//
// The SECOND analysis axis (voice leading), foundation component VL-C — the FIRST
// judgment component of the axis. Spec: cowork_voiceleading_axis_design.md (SIGNED
// 2026-07-03) §5.3, §7, §8. It owns the measured-motion evidence contribution to the
// one question "what texture is this span?" — and only that (no era/composer/genre
// claim; no harmonic decision).
//
// FEATURE SPACE = z-SCORED CONCATENATION (ABz) — a STRUCTURAL declaration DECIDED BY
// MEASUREMENT (§5.3, knowledge-based coding). The build ran the three named candidates
// (motion-only / two-stage / z-scored concatenation; raw concatenation rejected a
// priori for the measured motion dilution) and measured how well NEAREST-CENTROID in
// each space reproduces the ratified AB K=4 partition. WINNER: z-scored concatenation,
// nearest-centroid ARI 0.791 / accuracy 0.918 (two-stage 0.716, motion-only 0.258).
// Provenance + the shipped reference set (mean/std + 4 z-space centroids): the GENERATED
// header textureclassifierreference.h (run_vl_feature_space.py). The 20-d feature is
// the interval profile (16) then the motion profile (4), in the reference's declared
// order.
//
// OUTPUT (§5.3 as signed) — the committed class PLUS the FULL RANKED LIST of ALL class
// fits with weights (zero information loss; the ARCH §2.15 carried-alternatives
// contract). The committed class is the TOP of the ranked list; nothing below is
// discarded. The Class-M `texture-of-span` confidence (cowork_confidence_contract.md
// §2/§3 row) is the best-vs-second-best FIT margin, squashed to [0,1]: fit is
// exp(-distance/fitScale) of the z-space euclidean distance to a centroid, so the
// margin is already in [0,1) (R5 squash: monotone in the distance margin; fitScale is
// the precision-phase constant). The ranked-list `weight` is the normalized fit.
//
// THE THREE DECLARED FLOORS (spec §5.3, used by these names): the EVIDENTIAL FLOOR
// (min motion-sample count for a profile to support a decision), the MARGIN FLOOR (min
// best-vs-second margin), the FIT FLOOR (min absolute fit of the best class). Abstention
// (contract U5) fires when the margin is below the margin floor OR the best fit is below
// the fit floor — the fit-floor clause is what makes a span resembling NO reference class
// abstain rather than be forced to its nearest. A single-voice selection has no voice
// pairs -> the motion profile is undefined -> NO-PAIR abstention (never interval-only,
// v1). All floors are PRECISION-PHASE (documented defaults, NOT tuned).
//
// v1 GRANULARITY: the whole analysed selection is ONE VoiceLeadingSpan (§5.3, §D4). The
// per-span refinement (voice-leading-spans plural within a selection) is gated on the
// §15-1 measurement — NOT this build. The output TYPE is already a span, so the
// refinement changes cardinality, not shape.
//
// DORMANT: no production consumer (see voicelinearview.h).

#include <array>
#include <vector>

#include "composing/analysis/notemodel/note_model.h"
#include "composing/analysis/voiceleading/textureclassifierreference.h"
#include "composing/analysis/voiceleading/voiceleadingprofiles.h"

namespace mu::composing::analysis::voiceleading {

/// The four data-derived voice-leading idioms (findings v2.0; spec §0). Enum order
/// MATCHES the centroid order in textureclassifierreference.h — TextureClass(k) is the
/// class of kVlRefCentroidZ[k]. Names are post-hoc readings of cluster signatures,
/// provisional like the harmonic-idiom names.
enum class TextureClass {
    Contrapuntal = 0,        ///< contrapuntal part-writing (stepwise, contrary/similar; low oblique/leap)
    HomophonicClassical = 1, ///< homophonic melody+accompaniment, classical keyboard figuration
    HomophonicPianistic = 2, ///< homophonic, romantic/virtuosic pianistic (leap-elevated)
    ModerateMixed = 3        ///< the moderate/mixed early-music cluster
};

/// Why a classification abstained (contract U5 semantics). None = committed.
enum class AbstentionReason {
    None,
    NoPair,        ///< < 2 profile-eligible voices — no voice pairs, motion undefined (v1)
    TooFewSamples, ///< motion below the evidential floor, or interval profile undefined
    LowMargin,     ///< best-vs-second margin below the margin floor
    LowFit         ///< best absolute fit below the fit floor (resembles no reference class)
};

/// One class's fit — carried for ALL classes in the ranked list (zero information loss).
struct ClassFit {
    TextureClass cls = TextureClass::ModerateMixed;
    double distance = 0.0;   ///< z-space euclidean distance to this class's centroid
    double fit = 0.0;        ///< exp(-distance/fitScale) — absolute fit in (0,1]
    double weight = 0.0;     ///< normalized fit (sum to 1 over classes) — the ranked-list weight
};

/// One voice-leading-span: the range, the committed idiom + the full ranked list of ALL
/// class fits with weights, the Class-M confidence, and the honest marks (§7).
struct VoiceLeadingSpan {
    int startTick = 0;
    int endTick = 0;

    TextureClass committed = TextureClass::ModerateMixed;   ///< top of `ranked` (meaningful iff !abstained)
    std::vector<ClassFit> ranked;                           ///< ALL classes, fit-descending (empty iff no feature)
    double confidence = 0.0;                                ///< Class-M texture-of-span, squashed [0,1]

    bool abstained = false;
    AbstentionReason reason = AbstentionReason::None;

    ReductionRule reduction = ReductionRule::TopNote;       ///< provenance: the reduction the profiles used
    int motionSampleCount = 0;                              ///< the evidence the decision rested on

    // §7 bounded-context provenance (the evidence span the classification actually saw,
    // and whether it was truncated at a selection edge). For a non-extending classify
    // these mirror [startTick, endTick).
    int evidenceStartTick = 0;
    int evidenceEndTick = 0;
    bool clippedBySelectionEdge = false;   ///< rested on a window truncated at a NON-score loaded edge
    bool cueDenied = false;                ///< a decision-relevant extension request was refused (hard bound)
};

/// Precision-phase classifier constants (documented defaults from the fit distribution;
/// NOT tuned — the firewall). Defaults come from textureclassifierreference.h.
struct TextureClassifierParams {
    double fitScale = kVlFitScaleDefault;       ///< distance -> fit scale (median best-distance)
    double fitFloor = kVlFitFloorDefault;       ///< min absolute best fit (~p05)
    double marginFloor = kVlMarginFloorDefault; ///< min best-vs-second fit margin (~p05)
    int evidentialFloor = kMinMotionEvents;     ///< min motion-sample count (study min_events)
};

/// Build the 20-d raw feature (interval A[0..15] then motion B[16..19]) in the
/// reference's declared order. Exposed for inspection / tests.
std::array<double, kVlFeatureDim> buildFeature(const MotionProfile& motion, const IntervalProfile& interval);

/// Classify ONE span (whole-selection granularity, v1) from its profiles. Emits the
/// full ranked list; abstains per the three floors / no-pair rule. Pure — no note-model
/// dependency — so the oracle tests inject hand-built profiles.
VoiceLeadingSpan classifyTexture(const MotionProfile& motion, const IntervalProfile& interval,
                                 int startTick, int endTick,
                                 const TextureClassifierParams& params = {});

// ── VL-C's bounded-context extension requester (Task D; spec §8) ───────────────
//
// The discovery rule, coded + tested (a component ships with its extension behavior).
// The cue fires iff the profile rests on fewer samples than the evidential floor AND
// the classification margin is below the margin floor. The requester owns the loop —
// it calls NoteModel::extend (later first, then earlier), re-builds the view + profiles
// + classification over the enlarged loaded span each step, and stops when the
// classification and its margin stop changing under further context (convergence), or
// at the hard bound (settings cap) or the score boundary. Whole-score selection => the
// loaded edges ARE the score bounds => no cue fires (inertness).

struct VlExtensionParams {
    bool enableExtension = false;   ///< DORMANT default OFF (no request fires; byte-identical)
    int maxSteps = 4;               ///< hard bound — the §3.7 safety cap (settings)
    int incrementBars = 2;         ///< extension increment in bars (the requester's natural unit)
    int ticksPerBar = 1920;        ///< bars->ticks default (4/4 at 480/quarter); precision-phase
};

/// Classify a SELECTION with bounded-context extension (spec §8; the L4/L5 requester
/// pattern). @p model is taken BY VALUE so the loop extends a private copy (the
/// caller's model is untouched). Output covers the SELECTION (its range is
/// [selectionStart, selectionEnd)); extended context is EVIDENCE, informing the profile,
/// never separately labelled (§2 invariant). The final evidence span + truncation
/// provenance ride the result. With enableExtension OFF, or selection == whole score, NO
/// extension fires. DORMANT: no production consumer.
VoiceLeadingSpan classifySelectionExtending(notemodel::NoteModel model,
                                            int selectionStart, int selectionEnd,
                                            const TextureClassifierParams& params = {},
                                            const VlExtensionParams& ext = {});

} // namespace mu::composing::analysis::voiceleading
