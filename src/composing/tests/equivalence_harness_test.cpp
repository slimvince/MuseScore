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

// equivalence_harness_test.cpp
//
// Measurement harness — NOT an assertion test.
//
// History: this harness was built to measure the gap between the old
// suppress-then-recompute replica (Pipeline B) and the baseline analyzeChord
// (Pipeline A). The redesign removed the replica: winner selection now lives in
// exactly one place -- applyHarmonicFunction(), the competition pipeline, which
// analyzeChord() calls internally -- so there is a single winner-selection
// pipeline and the divergence class this harness measured is eliminated by
// construction.
//
// Post-redesign role: a corpus-wide consistency / smoke check. For every region
// in the composing-test corpus (catalog + context MusicXML fixtures) the unified
// pipeline is run and its winner recorded; running it twice must agree (the
// pipeline is deterministic), so the divergence count is 0. The authoritative
// proof that the redesign preserved behaviour is the unchanged pipeline-snapshot
// goldens, the catalog assertions in composing_tests, and the BIR corpus -- this
// harness simply confirms the single pipeline is stable across every fixture.
//
//   Unified pipeline (the only pipeline):
//     analyzeChord()        -> builds the ScoringSnapshot, runs the competition
//                              via applyHarmonicFunction(), returns results[]
//     applyIter8691Pedal()
//     applyPostScoringGates()
//
//   The execution order mirrors regionanalyzer.cpp's Pass-1 call site exactly.
//
// The harness is a yardstick, not a gate: it always SUCCEED()s and never fails
// the suite. Zero divergences = the unified pipeline is consistent.
//
// Output: src/composing/tests/equivalence_harness_report.txt

#include <gtest/gtest.h>

#include <QFile>
#include <QString>
#include <QXmlStreamReader>

#include <cstdio>
#include <ctime>
#include <fstream>
#include <optional>
#include <sstream>
#include <string>
#include <vector>

#include "composing/analysis/chord/chordanalyzer.h"

using namespace mu::composing::analysis;

namespace {

// ── A single region to test (one harmony-bearing catalog measure) ───────────
struct HarnessRegion {
    std::string scoreLabel;
    int         measureNumber = -1;
    std::vector<int> pitches;   ///< MIDI pitches; first entry is the bass.
    std::vector<int> tpcs;      ///< parallel to pitches; -1 = not available.
    int         keyFifths = 0;
    KeySigMode  keyMode = KeySigMode::Ionian;
};

// ── MusicXML helpers (a minimal subset of chordanalyzer_musicxml_tests.cpp) ──
//
// We only need note pitches/TPCs and the running key context per measure —
// the harness compares Pipeline A vs Pipeline B, not against ground truth, so
// the full expected-harmony parser is unnecessary.

int stepToPc(const QString& step)
{
    if (step == "C") return 0;
    if (step == "D") return 2;
    if (step == "E") return 4;
    if (step == "F") return 5;
    if (step == "G") return 7;
    if (step == "A") return 9;
    if (step == "B") return 11;
    return -1;
}

int parsePitch(const QString& step, int alter, int octave)
{
    const int base = stepToPc(step);
    if (base < 0) {
        return -1;
    }
    return (octave + 1) * 12 + base + alter;
}

/// TPC (tonal pitch class) from MusicXML step + alter — same encoding as the
/// existing catalog loader: F=14, C=15, G=16, D=17, A=18, E=19, B=20;
/// each sharp adds 7, each flat subtracts 7. Returns -1 if step is unrecognised.
int tpcFromStepAlter(const QString& step, int alter)
{
    if (step.isEmpty()) {
        return -1;
    }
    static constexpr struct { char s; int base; } TABLE[] = {
        { 'F', 14 }, { 'C', 15 }, { 'G', 16 }, { 'D', 17 },
        { 'A', 18 }, { 'E', 19 }, { 'B', 20 }
    };
    for (const auto& entry : TABLE) {
        if (step[0].toLatin1() == entry.s) {
            return entry.base + 7 * alter;
        }
    }
    return -1;
}

struct NotePitchTpc {
    int pitch = -1;
    int tpc   = -1;
};

std::optional<NotePitchTpc> parseNote(QXmlStreamReader& xml)
{
    QString step;
    int alter = 0;
    int octave = -100;
    bool isRest = false;

    while (!(xml.isEndElement() && xml.name() == QLatin1String("note")) && !xml.atEnd()) {
        xml.readNext();
        if (!xml.isStartElement()) {
            continue;
        }
        if (xml.name() == QLatin1String("rest")) {
            isRest = true;
        } else if (xml.name() == QLatin1String("step")) {
            step = xml.readElementText().trimmed();
        } else if (xml.name() == QLatin1String("alter")) {
            alter = xml.readElementText().trimmed().toInt();
        } else if (xml.name() == QLatin1String("octave")) {
            octave = xml.readElementText().trimmed().toInt();
        }
    }

    if (isRest || step.isEmpty() || octave == -100) {
        return std::nullopt;
    }
    const int pitch = parsePitch(step, alter, octave);
    if (pitch < 0) {
        return std::nullopt;
    }
    return NotePitchTpc{ pitch, tpcFromStepAlter(step, alter) };
}

KeySigMode modeFromString(const QString& raw)
{
    const QString m = raw.trimmed().toLower();
    if (m == "minor")          return KeySigMode::Aeolian;
    if (m == "dorian")         return KeySigMode::Dorian;
    if (m == "phrygian")       return KeySigMode::Phrygian;
    if (m == "lydian")         return KeySigMode::Lydian;
    if (m == "mixolydian")     return KeySigMode::Mixolydian;
    if (m == "aeolian")        return KeySigMode::Aeolian;
    if (m == "locrian")        return KeySigMode::Locrian;
    return KeySigMode::Ionian;
}

/// Load every harmony-bearing measure from a catalog/context fixture as a
/// region. Mirrors loadCatalogFixtureEvents()'s gate exactly: a region is
/// emitted only when the measure carries a non-"other" analysisKind harmony
/// annotation AND has at least one sounding note. This makes the harness's
/// region set identical to the events the existing composing tests analyse.
std::vector<HarnessRegion> loadRegions(const QString& filePath, const std::string& label)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return {};
    }

    QXmlStreamReader xml(&file);
    std::vector<HarnessRegion> regions;

    int currentKeyFifths = 0;
    KeySigMode currentKeyMode = KeySigMode::Ionian;

    bool inMeasure = false;
    int currentMeasureNumber = -1;
    bool haveHarmony = false;
    std::vector<int> currentPitches;
    std::vector<int> currentTpcs;

    while (!xml.atEnd()) {
        xml.readNext();

        if (xml.isStartElement()) {
            if (xml.name() == QLatin1String("measure")) {
                inMeasure = true;
                currentMeasureNumber = xml.attributes().value("number").toInt();
                haveHarmony = false;
                currentPitches.clear();
                currentTpcs.clear();
            } else if (xml.name() == QLatin1String("fifths")) {
                currentKeyFifths = xml.readElementText().trimmed().toInt();
            } else if (xml.name() == QLatin1String("mode")) {
                currentKeyMode = modeFromString(xml.readElementText());
            } else if (xml.name() == QLatin1String("harmony") && inMeasure
                       && xml.attributes().hasAttribute("analysisKind")) {
                // "other" entries are suffix-coverage annotations only; skip them.
                const QString ak = xml.attributes().value("analysisKind").toString().trimmed();
                if (ak != "other") {
                    haveHarmony = true;
                }
            } else if (xml.name() == QLatin1String("note") && inMeasure) {
                const std::optional<NotePitchTpc> pt = parseNote(xml);
                if (pt.has_value()) {
                    currentPitches.push_back(pt->pitch);
                    currentTpcs.push_back(pt->tpc);
                }
            }
        } else if (xml.isEndElement() && xml.name() == QLatin1String("measure")) {
            if (haveHarmony && !currentPitches.empty()) {
                HarnessRegion r;
                r.scoreLabel    = label;
                r.measureNumber = currentMeasureNumber;
                r.keyFifths     = currentKeyFifths;
                r.keyMode       = currentKeyMode;
                r.pitches       = currentPitches;
                r.tpcs          = currentTpcs;
                regions.push_back(std::move(r));
            }
            inMeasure = false;
        }
    }

    return regions;
}

std::vector<ChordAnalysisTone> toAnalysisTones(const std::vector<int>& pitches,
                                               const std::vector<int>& tpcs)
{
    std::vector<ChordAnalysisTone> tones;
    tones.reserve(pitches.size());
    bool first = true;
    for (size_t i = 0; i < pitches.size(); ++i) {
        ChordAnalysisTone tone;
        tone.pitch  = pitches[i];
        tone.tpc    = (i < tpcs.size()) ? tpcs[i] : -1;
        tone.weight = 1.0;
        tone.isBass = first;
        tones.push_back(tone);
        first = false;
    }
    return tones;
}

const char* qualityName(ChordQuality q)
{
    switch (q) {
    case ChordQuality::Major:          return "Major";
    case ChordQuality::Minor:          return "Minor";
    case ChordQuality::Diminished:     return "Diminished";
    case ChordQuality::Augmented:      return "Augmented";
    case ChordQuality::HalfDiminished: return "HalfDiminished";
    case ChordQuality::Suspended2:     return "Suspended2";
    case ChordQuality::Suspended4:     return "Suspended4";
    case ChordQuality::Power:          return "Power";
    case ChordQuality::Unknown:
    default:                           return "Unknown";
    }
}

// ── Winner of one pipeline (the comparison key) ─────────────────────────────
struct Winner {
    bool        present = false;
    int         bassPc = -1;
    int         rootPc = -1;
    ChordQuality quality = ChordQuality::Unknown;
    int         tiePriority = -1;
};

bool winnersMatch(const Winner& a, const Winner& b)
{
    if (a.present != b.present) {
        return false;
    }
    if (!a.present) {
        return true; // both absent
    }
    return a.bassPc == b.bassPc
           && a.rootPc == b.rootPc
           && a.quality == b.quality
           && a.tiePriority == b.tiePriority;
}

std::string formatWinner(const Winner& w)
{
    if (!w.present) {
        return "(none)";
    }
    std::ostringstream oss;
    oss << w.bassPc << "/" << w.rootPc << "/" << qualityName(w.quality)
        << "(tie=" << w.tiePriority << ")";
    return oss.str();
}

// ── Best-effort git HEAD and ISO-8601 timestamp for the report header ───────

std::string repoRootFromDataRoot()
{
    // composing_tests_DATA_ROOT is "<repo>/src/composing/tests" (forward slashes
    // from CMAKE_CURRENT_LIST_DIR). Strip the known suffix to recover <repo>.
    std::string dataRoot = composing_tests_DATA_ROOT;
    const std::string suffix = "/src/composing/tests";
    if (dataRoot.size() >= suffix.size()
        && dataRoot.compare(dataRoot.size() - suffix.size(), suffix.size(), suffix) == 0) {
        return dataRoot.substr(0, dataRoot.size() - suffix.size());
    }
    return dataRoot;
}

std::string trimWhitespace(const std::string& s)
{
    const auto first = s.find_first_not_of(" \t\r\n");
    if (first == std::string::npos) {
        return "";
    }
    const auto last = s.find_last_not_of(" \t\r\n");
    return s.substr(first, last - first + 1);
}

std::string readFileTrimmed(const std::string& path)
{
    std::ifstream f(path);
    if (!f.is_open()) {
        return "";
    }
    std::ostringstream oss;
    oss << f.rdbuf();
    return trimWhitespace(oss.str());
}

std::string gitHead()
{
    const std::string repoRoot = repoRootFromDataRoot();
    const std::string headContent = readFileTrimmed(repoRoot + "/.git/HEAD");
    if (headContent.empty()) {
        return "(unknown)";
    }
    const std::string refPrefix = "ref:";
    if (headContent.rfind(refPrefix, 0) == 0) {
        const std::string ref = trimWhitespace(headContent.substr(refPrefix.size()));
        const std::string sha = readFileTrimmed(repoRoot + "/.git/" + ref);
        if (!sha.empty()) {
            return sha;
        }
        return "(unknown — loose ref absent; run: git rev-parse HEAD)";
    }
    // Detached HEAD: content is the SHA itself.
    return headContent;
}

std::string isoNowUtc()
{
    const std::time_t t = std::time(nullptr);
    const std::tm* tmv = std::gmtime(&t);
    if (!tmv) {
        return "(unknown)";
    }
    char buf[32];
    std::strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%SZ", tmv);
    return std::string(buf);
}

// ── One pipeline execution (mirrors regionanalyzer.cpp Pass-1 call site) ─────
//
// analyzeChord() builds the ScoringSnapshot and runs the competition
// (applyHarmonicFunction) internally, so the call site is simply
// analyzeChord -> applyIter8691Pedal -> applyPostScoringGates.
Winner runPipeline(const RuleBasedChordAnalyzer& analyzer,
                   const std::vector<ChordAnalysisTone>& tones,
                   int keyFifths,
                   KeySigMode keyMode,
                   const ChordTemporalContext& temporalCtx,
                   const ChordAnalyzerPreferences& prefs)
{
    PostScoringGateContext gateCtx;
    auto results = analyzer.analyzeChord(
        tones, keyFifths, keyMode, &temporalCtx, prefs, &gateCtx);

    if (results.empty()) {
        return Winner{}; // present = false
    }

    applyIter8691Pedal(results, gateCtx, &temporalCtx, prefs);
    applyPostScoringGates(results, prefs, &temporalCtx, gateCtx);

    if (results.empty()) {
        return Winner{};
    }

    const ChordIdentity& id = results.front().identity;
    Winner w;
    w.present     = true;
    w.bassPc      = id.bassPc;
    w.rootPc      = id.rootPc;
    w.quality     = id.quality;
    w.tiePriority = id.tiePriority;
    return w;
}

struct Divergence {
    std::string scoreLabel;
    int         measureNumber = -1;
    Winner      a;
    Winner      b;
};

} // namespace

TEST(Composing_EquivalenceHarness, SuppressedPlusFunctionMatchesBaseline)
{
    const RuleBasedChordAnalyzer analyzer{};

    // Per-fixture preferences. Both pipelines use the identical preferences and
    // the identical unified analyzeChord path, so the two winners must match.
    ChordAnalyzerPreferences jazzPrefs;
    jazzPrefs.extensionThreshold = 0.12;

    ChordAnalyzerPreferences standardPrefs;
    standardPrefs.preferMinorOverMajorAdd6 = true;

    ChordAnalyzerPreferences defaultPrefs; // context fixture uses defaults

    struct Fixture {
        QString relativePath;
        const ChordAnalyzerPreferences* prefs;
        std::string label;
    };
    const std::vector<Fixture> fixtures = {
        { "/data/chordanalyzer_catalog_jazz.musicxml",     &jazzPrefs,     "catalog_jazz" },
        { "/data/chordanalyzer_catalog_standard.musicxml", &standardPrefs, "catalog_standard" },
        { "/data/chordanalyzer_context.musicxml",          &defaultPrefs,  "context" },
    };

    int totalRegions = 0;
    int matchCount   = 0;
    int divergeCount = 0;
    int skippedBothEmpty = 0; // both pipelines returned no candidate
    std::vector<Divergence> divergences;

    for (const Fixture& fixture : fixtures) {
        const QString path = QString::fromUtf8(composing_tests_DATA_ROOT) + fixture.relativePath;
        const std::vector<HarnessRegion> regions = loadRegions(path, fixture.label);

        // Temporal context is threaded across regions from Pipeline A's winner —
        // the baseline is the reference both pipelines are measured against, and
        // both see the identical context for each region.
        int previousRootPc = -1;
        ChordQuality previousQuality = ChordQuality::Unknown;

        for (const HarnessRegion& region : regions) {
            const std::vector<ChordAnalysisTone> tones =
                toAnalysisTones(region.pitches, region.tpcs);

            ChordTemporalContext temporalCtx;
            temporalCtx.previousRootPc  = previousRootPc;
            temporalCtx.previousQuality = previousQuality;

            // Pipeline A and B both run the single unified pipeline. After the
            // redesign there is no second winner-selection path to compare
            // against; running twice confirms the pipeline is deterministic and
            // stable across the whole fixture set (divergences must be 0).
            const Winner a = runPipeline(
                analyzer, tones, region.keyFifths, region.keyMode, temporalCtx,
                *fixture.prefs);
            const Winner b = runPipeline(
                analyzer, tones, region.keyFifths, region.keyMode, temporalCtx,
                *fixture.prefs);

            // Advance temporal context from the baseline winner.
            if (a.present) {
                previousRootPc  = a.rootPc;
                previousQuality = a.quality;
            } else {
                previousRootPc  = -1;
                previousQuality = ChordQuality::Unknown;
            }

            if (!a.present && !b.present) {
                ++skippedBothEmpty;
                continue;
            }

            ++totalRegions;
            if (winnersMatch(a, b)) {
                ++matchCount;
            } else {
                ++divergeCount;
                divergences.push_back(Divergence{ region.scoreLabel, region.measureNumber, a, b });
            }
        }
    }

    // ── Write the report ────────────────────────────────────────────────────
    std::ostringstream report;
    report << "Equivalence Harness Report\n";
    report << "HEAD: " << gitHead() << "\n";
    report << "Date: " << isoNowUtc() << "\n";
    report << "\n";

    const double pct = (totalRegions > 0)
                       ? (100.0 * static_cast<double>(divergeCount) / static_cast<double>(totalRegions))
                       : 0.0;
    char pctBuf[32];
    std::snprintf(pctBuf, sizeof(pctBuf), "%.1f", pct);

    report << "Total regions tested : " << totalRegions << "\n";
    report << "Match                : " << matchCount << "\n";
    report << "Diverge              : " << divergeCount << "  (" << pctBuf << "%)\n";
    report << "Skipped (both empty) : " << skippedBothEmpty << "\n";
    report << "\n";

    report << "--- Divergences (first 40) ---\n";
    const size_t kMaxListed = 40;
    for (size_t i = 0; i < divergences.size() && i < kMaxListed; ++i) {
        const Divergence& d = divergences[i];
        report << d.scoreLabel << "  tick=" << d.measureNumber
               << "  A=" << formatWinner(d.a)
               << "  B=" << formatWinner(d.b) << "\n";
    }
    if (divergences.size() > kMaxListed) {
        report << "... (" << (divergences.size() - kMaxListed)
               << " more divergence(s) not listed)\n";
    }

    const std::string reportPath = (QString::fromUtf8(composing_tests_DATA_ROOT)
                                    + "/equivalence_harness_report.txt").toStdString();
    std::ofstream reportFile(reportPath);
    if (reportFile.is_open()) {
        reportFile << report.str();
    }

    // Echo a compact summary to the test log so the run output is self-describing.
    std::printf("[EquivalenceHarness] regions=%d match=%d diverge=%d (%s%%) skipped=%d\n",
                totalRegions, matchCount, divergeCount, pctBuf, skippedBothEmpty);
    std::fflush(stdout);

    // Measurement only — never fail the suite regardless of divergence count.
    SUCCEED();
}
