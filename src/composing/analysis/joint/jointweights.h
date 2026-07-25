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

#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTWEIGHTS_H
#define MU_COMPOSING_ANALYSIS_JOINT_JOINTWEIGHTS_H

#include <array>
#include <string>
#include <unordered_map>

// The joint estimator's log-linear factor weight vector — the C++ port of
// probe_decoder.WEIGHT_NAMES / identity_weights (★R2, user ruling C1). Thirteen weights:
// nine generative-factor weights over frozen table log-probabilities, plus four
// cadence-evidence feature weights. The IDENTITY setting (every generative weight 1.0,
// every cadence weight 0.0 — a cadence feature is an indicator, not a log-probability, so
// its generative-baseline value is zero) reproduces the committed step-1 probe decode and
// is the mandated generative-baseline ablation arm. The weights are applied at the factor
// call sites in the decoder (a later commit); this component only holds and names them.
//
// Spec: cowork_joint_estimator_factorization.md §2; probe_decoder.py.

namespace mu::composing::analysis::joint {
/// The 13 weight names, in probe_decoder.WEIGHT_NAMES order.
extern const std::array<std::string, 13> kWeightNames;
/// The nine generative-factor weight names (WEIGHT_NAMES[:9]).
extern const std::array<std::string, 9> kGenerativeWeightNames;

/// A weight vector keyed by weight name. Missing names read as 0.0 via get().
struct WeightVector {
    std::unordered_map<std::string, double> w;

    /// The weight for `name`, or 0.0 if absent (matching Python's w.get(name, 0.0) at the
    /// cadence call sites; generative call sites always find their name).
    double get(const std::string& name) const;
};

/// The mandated generative-baseline setting: every generative weight 1.0, every cadence
/// weight 0.0 (probe_decoder.identity_weights()).
WeightVector identityWeights();
} // namespace mu::composing::analysis::joint

#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTWEIGHTS_H
