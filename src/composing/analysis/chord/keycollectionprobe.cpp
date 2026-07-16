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

#include "keycollectionprobe.h"

#include <cstdio>
#include <cstdlib>

namespace mu::composing::analysis::keycollectionprobe {

namespace {

bool envFlagSet(const char* name)
{
    const char* v = std::getenv(name);
    return v != nullptr && *v != '\0';
}

bool s_written = false;

} // namespace

const bool countingEnabled    = envFlagSet("MU_KEY_COLLECTION_PROBE");
const bool signatureMaskVariant = envFlagSet("MU_KEY_COLLECTION_SIGMASK_VARIANT");

Counters& counters()
{
    static Counters block;
    return block;
}

void writeCounters(const std::string& path)
{
    if (!countingEnabled || path.empty() || s_written) {
        return;
    }
    s_written = true;

    std::FILE* f = std::fopen(path.c_str(), "w");
    if (!f) {
        return;
    }
    const Counters& c = counters();
    std::fprintf(f,
                 "{\n"
                 "  \"sparseRefineEntries\": %llu,\n"
                 "  \"sparseGuardShapeMatched\": %llu,\n"
                 "  \"sparseAeolianGuardFires\": %llu,\n"
                 "  \"analyzeChordCalls\": %llu,\n"
                 "  \"analyzeChordCallsAltered\": %llu,\n"
                 "  \"analyzeChordCallsAlteredDomBB7\": %llu,\n"
                 "  \"regionCommitCalls\": %llu,\n"
                 "  \"regionCommitCallsAltered\": %llu,\n"
                 "  \"regionCommitCallsAlteredDomBB7\": %llu,\n"
                 "  \"decoderWindowCalls\": %llu,\n"
                 "  \"decoderWindowCallsAltered\": %llu,\n"
                 "  \"decoderWindowCallsAlteredDomBB7\": %llu,\n"
                 "  \"diatonicFlagTests\": %llu,\n"
                 "  \"diatonicFlagDiffers\": %llu,\n"
                 "  \"gateIDiatonicTests\": %llu,\n"
                 "  \"gateIDiatonicDiffers\": %llu,\n"
                 "  \"gateISwapDiffers\": %llu,\n"
                 "  \"gateLDiatonicTests\": %llu,\n"
                 "  \"gateLDiatonicDiffers\": %llu,\n"
                 "  \"gateLSwapDiffers\": %llu,\n"
                 "  \"gateGEFires\": %llu,\n"
                 "  \"tonicPriorEntries\": %llu,\n"
                 "  \"tonicPriorApplied\": %llu,\n"
                 "  \"signatureMaskVariant\": %s\n"
                 "}\n",
                 c.sparseRefineEntries, c.sparseGuardShapeMatched, c.sparseAeolianGuardFires,
                 c.analyzeChordCalls, c.analyzeChordCallsAltered, c.analyzeChordCallsAlteredDomBB7,
                 c.regionCommitCalls, c.regionCommitCallsAltered, c.regionCommitCallsAlteredDomBB7,
                 c.decoderWindowCalls, c.decoderWindowCallsAltered, c.decoderWindowCallsAlteredDomBB7,
                 c.diatonicFlagTests, c.diatonicFlagDiffers,
                 c.gateIDiatonicTests, c.gateIDiatonicDiffers, c.gateISwapDiffers,
                 c.gateLDiatonicTests, c.gateLDiatonicDiffers, c.gateLSwapDiffers,
                 c.gateGEFires, c.tonicPriorEntries, c.tonicPriorApplied,
                 signatureMaskVariant ? "true" : "false");
    std::fclose(f);
}

} // namespace mu::composing::analysis::keycollectionprobe
