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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTADAPTER_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTADAPTER_H

#include <cmath>
#include <optional>
#include <string>
#include <unordered_map>
#include <utility>

#include "jointprimitives.h"
#include "jointtables.h"
#include "jointweights.h"

// The joint estimator's factor log-probability provider — the C++ port of
// probe_decoder.FittedAdapter. It answers every factor query the decoder makes over the loaded
// generative tables (jointtables) plus the per-mode class marginal (mode_marginal.json), applying
// the ratified below-threshold (Katz leftover) apportionment rule (§5 option 2a). It holds the
// 13-weight vector; the weights are applied at the DECODER's call sites (as in Python), so the
// adapter methods always return the RAW factor log-probability. DORMANT (no production consumer).
//
// Spec: cowork_joint_estimator_factorization.md §3/§5; probe_decoder.FittedAdapter.

namespace mu::composing::analysis::joint {
inline double log0Floor() { return std::log(1e-9); }         // LOG0_FLOOR
double safeLog(double p);                                     // _safe_log

class FittedAdapter
{
public:
    /// Load the tables for `tableSet` ("all"/"fold{i}") and the mode marginal from `artifactDir`;
    /// `weights` defaults to the identity (generative-baseline) setting. Check `loaded()`.
    static FittedAdapter load(const std::string& artifactDir, const std::string& tableSet = "all",
                              WeightVector weights = identityWeights(),
                              const std::string& leftoverMode = "freq");

    bool loaded() const { return m_loaded; }
    const std::string& error() const { return m_error; }
    const std::string& corpusGitHash() const { return m_tables.corpusGitHash; }
    const WeightVector& weights() const { return m_weights; }
    const JointTables& tables() const { return m_tables; }

    // Per-feature cadence weights (a nat per firing) read off the weight vector.
    double cadenceWeight(const std::string& feature) const { return m_weights.get("cad_" + feature); }
    bool anyCadenceWeight() const;

    // ── the factors (each returns a raw log-probability, a nat) ─────────────────────────────
    double priorLogp(int tonic, bool isMajor, std::optional<int> sigFifths, const std::string& declaredMode) const;
    /// The prior split into (signature-only component, declared-mode increment) — the two fitted
    /// features whose identity-weighted sum is priorLogp (★R2).
    std::pair<double, double> priorTerms(int tonic, bool isMajor, std::optional<int> sigFifths,
                                         const std::string& declaredMode) const;
    double entryLogp(const LabelClass& cls, bool isMajor) const;
    double keyTransLogp(int tonicPrev, bool majorPrev, int tonic, bool isMajor) const;
    double chordTransLogp(const LabelClass& prev, const LabelClass& cls, bool isMajor) const;
    double emissionLogp(const std::string& category, const std::string& mc, const std::string& ap,
                        const std::string& dp, bool tied) const;
    double spellingLogp(const std::string& sbin, bool isMajor) const;
    double bassLogp(const std::string* role, const std::string& family, const std::string& degreeBase,
                    const std::string& quality, bool isMajor) const;
    double factorAbsentLogp(const std::string& role, const std::string& family) const;
    double boundaryLogp(const std::string& beatClass, bool isBoundary, bool fermCtx) const;

private:
    using ParentFn = std::optional<std::string> (*)(const Node&);

    static const std::string& modeName(bool isMajor);
    const std::unordered_map<std::string, double>& modeMarginal(bool isMajor) const;

    // firstBucket / katz leftover (the ratified §5 below-threshold rule)
    std::optional<std::string> firstBucket(const Dist& dist, Node start, ParentFn parentFn) const;
    std::optional<double> katzQuery(const Dist& dist, const Node& outcome, ParentFn parentFn,
                                    bool isMajor, bool isClass) const;
    std::pair<double, int> apportion(const Dist& dist, const std::string& bucket, ParentFn parentFn,
                                     bool isMajor) const;

    static const Dist* firstPresentDist(const std::vector<std::string>& chain,
                                        const std::unordered_map<std::string, Dist>& levels);

    JointTables m_tables;
    WeightVector m_weights;
    std::string m_leftoverMode = "freq";
    std::unordered_map<std::string, double> m_margMajor;
    std::unordered_map<std::string, double> m_margMinor;
    bool m_loaded = false;
    std::string m_error;

    // apportion cache: key = distPtr + '\x1f' + bucket + '\x1f' + mode -> (denomMass, count)
    mutable std::unordered_map<std::string, std::pair<double, int> > m_apportionCache;
};
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTADAPTER_H
