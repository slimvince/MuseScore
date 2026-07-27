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

// ── The inference<->presentation dependency-direction guard (seams-2 P-strings, Task 3) ──
//
// A PERMANENT, mechanical include-closure test enforcing the boundary the notation output-surface
// contract draws (cowork_notation_output_contract.md §3.3 amendment + the D2 ruling): the display
// strings (chord symbol, Nashville number) are PRESENTATION derivations from the joint estimator's
// PUBLISHED record; the estimator's inference/decode never depends on presentation, and the
// presentation formatter never reaches into the module's inference internals. Both directions fail
// the build on violation. Dispatch: cc_instruction_notation_pstrings.md (the include-closure pattern
// the joint module build established).
//
// Enumeration (documented; the inference side is a GLOB so new module files are auto-covered):
//   INFERENCE side  = every file under src/composing/analysis/joint/ — the joint estimator module:
//                     the decode machinery (jointdecoder / jointtables / jointadapter / jointfactadapter
//                     / jointprimitives / jointweights / jointembeddedartifacts / labelclass), and the
//                     render / record / producer units (jointrender / jointnotationrecord /
//                     jointnotationproducer) plus their headers. It must NOT include the presentation
//                     chord-symbol/Nashville formatter — declared in chordanalyzer.h (the
//                     ChordSymbolFormatter namespace), defined in chordsymbolformatter.cpp. (The module
//                     MAY include the sanctioned shared pitch leaf analysisutils.h — that is a pitch
//                     primitive, NOT presentation.)
//   PRESENTATION side = the chord-symbol/Nashville formatter chordsymbolformatter.cpp. It must NOT
//                     include any joint module header (composing/analysis/joint/...): it consumes only
//                     the published record/adapter output surface (a ChordAnalysisResult), never the
//                     decode internals.

#include <gtest/gtest.h>

#include <filesystem>
#include <fstream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

namespace {

// COMPOSING_SRC_DIR is the compile-time absolute path to src/composing (a compile definition in the
// tests CMakeLists), so the guard reads the real sources regardless of the run directory.
const std::filesystem::path kComposingSrc{ COMPOSING_SRC_DIR };

// The quoted / angled target of every #include directive in `content` (the text between the
// delimiters). A pure string->vector scanner so the negative control can perturb synthetic input.
std::vector<std::string> collectIncludesFromContent(const std::string& content)
{
    std::vector<std::string> out;
    std::istringstream in(content);
    std::string line;
    while (std::getline(in, line)) {
        const size_t hash = line.find_first_not_of(" \t");
        if (hash == std::string::npos || line.compare(hash, 8, "#include") != 0) {
            continue;
        }
        const size_t open = line.find_first_of("\"<", hash + 8);
        if (open == std::string::npos) {
            continue;
        }
        const char close = (line[open] == '"') ? '"' : '>';
        const size_t end = line.find(close, open + 1);
        if (end == std::string::npos) {
            continue;
        }
        out.push_back(line.substr(open + 1, end - open - 1));
    }
    return out;
}

std::vector<std::string> collectIncludes(const std::filesystem::path& file)
{
    std::ifstream in(file);
    const std::string content((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
    return collectIncludesFromContent(content);
}

// The presentation chord-symbol/Nashville formatter: its declaring header (chordanalyzer.h, which
// carries the ChordSymbolFormatter namespace) or its unit (chordsymbolformatter). The sanctioned
// shared pitch leaf analysisutils.h is deliberately NOT matched (a pitch primitive, not presentation).
bool referencesPresentationFormatter(const std::string& inc)
{
    return inc.find("chordanalyzer.h") != std::string::npos
           || inc.find("chordsymbolformatter") != std::string::npos;
}

// Any joint-estimator module header (matched by its path segment).
bool referencesJointModule(const std::string& inc)
{
    return inc.find("analysis/joint/") != std::string::npos;
}

std::vector<std::filesystem::path> jointModuleFiles()
{
    std::vector<std::filesystem::path> files;
    const std::filesystem::path dir = kComposingSrc / "analysis" / "joint";
    for (const auto& entry : std::filesystem::directory_iterator(dir)) {
        if (!entry.is_regular_file()) {
            continue;
        }
        const std::string ext = entry.path().extension().string();
        if (ext == ".h" || ext == ".cpp") {
            files.push_back(entry.path());
        }
    }
    return files;
}

} // namespace

// (a) The joint estimator's inference module never depends on the presentation formatter.
TEST(InferencePresentationBoundary, JointModuleDoesNotIncludePresentationFormatter)
{
    const std::vector<std::filesystem::path> files = jointModuleFiles();
    ASSERT_FALSE(files.empty())
        << "no joint module files found under " << (kComposingSrc / "analysis" / "joint");
    for (const auto& file : files) {
        for (const std::string& inc : collectIncludes(file)) {
            EXPECT_FALSE(referencesPresentationFormatter(inc))
                << file.filename().string() << " includes the presentation formatter (\"" << inc
                << "\") — inference must not depend on presentation";
        }
    }
}

// (b) The presentation formatter never reaches into the joint module's inference internals.
TEST(InferencePresentationBoundary, PresentationFormatterDoesNotIncludeJointModule)
{
    const std::filesystem::path formatter =
        kComposingSrc / "analysis" / "chord" / "chordsymbolformatter.cpp";
    ASSERT_TRUE(std::filesystem::exists(formatter)) << "missing " << formatter;
    for (const std::string& inc : collectIncludes(formatter)) {
        EXPECT_FALSE(referencesJointModule(inc))
            << "chordsymbolformatter.cpp includes a joint inference header (\"" << inc
            << "\") — presentation must consume only the published output surface";
    }
}

// Negative control (the dispatch's discipline): the guard must actually FIRE on a perturbed include,
// in BOTH directions — and must NOT flag the sanctioned shared pitch leaf.
TEST(InferencePresentationBoundary, NegativeControl_GuardFiresOnAViolation)
{
    // a joint file that pulls in the presentation formatter -> flagged (direction a)
    const std::vector<std::string> v1 = collectIncludesFromContent("  #include \"chordanalyzer.h\"\n");
    ASSERT_EQ(v1.size(), 1u);
    EXPECT_TRUE(referencesPresentationFormatter(v1[0]));

    // the formatter pulling in a joint inference header -> flagged (direction b)
    const std::vector<std::string> v2 =
        collectIncludesFromContent("#include \"composing/analysis/joint/jointdecoder.h\"\n");
    ASSERT_EQ(v2.size(), 1u);
    EXPECT_TRUE(referencesJointModule(v2[0]));

    // the sanctioned shared pitch leaf -> NOT flagged either way
    const std::vector<std::string> ok =
        collectIncludesFromContent("#include \"composing/analysis/chord/analysisutils.h\"\n");
    ASSERT_EQ(ok.size(), 1u);
    EXPECT_FALSE(referencesPresentationFormatter(ok[0]));
    EXPECT_FALSE(referencesJointModule(ok[0]));
}
