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

#include "jointweights.h"

namespace mu::composing::analysis::joint {
const std::array<std::string, 13> kWeightNames = {
    "prior", "declared_mode", "emission", "spelling", "bass", "boundary",
    "chord_trans", "key_trans", "entry",
    "cad_leading_tone", "cad_tritone_pair", "cad_dominant_tonic_bass", "cad_fermata_location"
};

const std::array<std::string, 9> kGenerativeWeightNames = {
    "prior", "declared_mode", "emission", "spelling", "bass", "boundary",
    "chord_trans", "key_trans", "entry"
};

double WeightVector::get(const std::string& name) const
{
    const auto it = w.find(name);
    return it != w.end() ? it->second : 0.0;
}

WeightVector identityWeights()
{
    WeightVector wv;
    for (const std::string& n : kGenerativeWeightNames) {
        wv.w[n] = 1.0;
    }
    // The four cadence feature weights are 0.0 at the generative baseline. They are the
    // difference between kWeightNames and kGenerativeWeightNames; set them explicitly so
    // the vector carries every name.
    for (const std::string& n : kWeightNames) {
        if (wv.w.find(n) == wv.w.end()) {
            wv.w[n] = 0.0;
        }
    }
    return wv;
}
} // namespace mu::composing::analysis::joint
