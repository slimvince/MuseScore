/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#include <gtest/gtest.h>

#include <QFile>
#include <QXmlStreamReader>

#include <cctype>
#include <fstream>
#include <optional>
#include <sstream>
#include <set>
#include <string>
#include <vector>

#include "composing/analysis/chordanalyzer.h"
#include "engraving/dom/chordlist.h"

using namespace mu::composing::analysis;

namespace {

struct ExpectedHarmony {
    int rootPc = -1;
    std::optional<int> bassPc;
    ChordQuality quality = ChordQuality::Unknown;
    bool hasMinorSeventh = false;
    bool hasMajorSeventh = false;
    std::string symbolText;
};

struct FixtureEvent {
    int measureNumber = -1;
    std::vector<int> pitches;
    int keyFifths = 0;
    bool keyIsMajor = true;
    ExpectedHarmony expected;
    std::string expectedRoman;
};

struct SymbolRomanMismatch {
    int measureNumber = -1;
    std::string expectedSymbol;
    std::string actualSymbol;
    std::string expectedRoman;
    std::string actualRoman;
    int expectedRootPc = -1;
    int actualRootPc = -1;
    ChordQuality expectedQuality = ChordQuality::Unknown;
    ChordQuality actualQuality = ChordQuality::Unknown;
};

int normalizePc(int pitch)
{
    int pc = pitch % 12;
    return pc < 0 ? pc + 12 : pc;
}

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

ChordQuality kindToQuality(const QString& kind)
{
    if (kind == "major" || kind == "major-sixth"
        || kind == "major-seventh" || kind == "major-ninth"
        || kind == "major-11th" || kind == "major-13th"
        || kind == "dominant" || kind == "dominant-ninth"
        || kind == "dominant-11th" || kind == "dominant-13th"
        || kind == "augmented-seventh" || kind == "augmented-ninth") {
        return ChordQuality::Major;
    }
    if (kind == "minor" || kind == "minor-sixth"
        || kind == "minor-seventh" || kind == "minor-ninth"
        || kind == "minor-11th" || kind == "minor-13th"
        || kind == "major-minor") {
        return ChordQuality::Minor;
    }
    if (kind == "diminished" || kind == "diminished-seventh") {
        return ChordQuality::Diminished;
    }
    if (kind == "half-diminished") {
        return ChordQuality::HalfDiminished;
    }
    if (kind == "augmented") {
        return ChordQuality::Augmented;
    }
    if (kind == "suspended-second") {
        return ChordQuality::Suspended2;
    }
    if (kind == "suspended-fourth") {
        return ChordQuality::Suspended4;
    }
    if (kind == "power" || kind == "pedal") {
        return ChordQuality::Power;
    }
    return ChordQuality::Unknown;
}

const char* chordQualityToString(ChordQuality quality)
{
    switch (quality) {
    case ChordQuality::Major: return "Major";
    case ChordQuality::Minor: return "Minor";
    case ChordQuality::Diminished: return "Diminished";
    case ChordQuality::Augmented: return "Augmented";
    case ChordQuality::HalfDiminished: return "HalfDiminished";
    case ChordQuality::Suspended2: return "Suspended2";
    case ChordQuality::Suspended4: return "Suspended4";
    case ChordQuality::Power: return "Power";
    case ChordQuality::Unknown:
    default: return "Unknown";
    }
}

struct SplitChordSymbol {
    std::string root;
    std::string body;
    std::string bass;
    bool valid = false;
};

SplitChordSymbol splitChordSymbol(const std::string& symbol)
{
    SplitChordSymbol out;
    if (symbol.empty()) {
        return out;
    }

    const unsigned char first = static_cast<unsigned char>(symbol[0]);
    if (first < 'A' || first > 'G') {
        return out;
    }

    size_t pos = 1;
    while (pos < symbol.size() && (symbol[pos] == '#' || symbol[pos] == 'b')) {
        ++pos;
    }

    out.root = symbol.substr(0, pos);

    const std::string remainder = symbol.substr(pos);
    const size_t slash = remainder.find('/');
    if (slash == std::string::npos) {
        out.body = remainder;
    } else {
        out.body = remainder.substr(0, slash);
        out.bass = remainder.substr(slash + 1);
    }

    out.valid = true;
    return out;
}

bool equivalentParsedBodies(const std::string& lhsBody, const std::string& rhsBody)
{
    if (lhsBody == rhsBody) {
        return true;
    }

    static mu::engraving::ChordList chordList;
    mu::engraving::ParsedChord lhsParsed;
    mu::engraving::ParsedChord rhsParsed;

    const bool lhsOk = lhsParsed.parse(muse::String::fromUtf8(lhsBody.c_str()), &chordList, true, false)
                       && lhsParsed.parseable();
    const bool rhsOk = rhsParsed.parse(muse::String::fromUtf8(rhsBody.c_str()), &chordList, true, false)
                       && rhsParsed.parseable();

    return lhsOk && rhsOk && lhsParsed == rhsParsed;
}

bool equivalentSymbolSpelling(const std::string& lhs, const std::string& rhs)
{
    if (lhs == rhs) {
        return true;
    }

    const SplitChordSymbol lhsParts = splitChordSymbol(lhs);
    const SplitChordSymbol rhsParts = splitChordSymbol(rhs);
    if (!lhsParts.valid || !rhsParts.valid) {
        return false;
    }

    if (lhsParts.root != rhsParts.root || lhsParts.bass != rhsParts.bass) {
        return false;
    }

    return equivalentParsedBodies(lhsParts.body, rhsParts.body);
}

ExpectedHarmony parseHarmony(QXmlStreamReader& xml)
{
    ExpectedHarmony out;

    const QString analysisKindAttr = xml.attributes().value("analysisKind").toString().trimmed();

    QString rootStep;
    int rootAlter = 0;
    QString bassStep;
    int bassAlter = 0;
    QString kind;

    while (!(xml.isEndElement() && xml.name() == "harmony") && !xml.atEnd()) {
        xml.readNext();

        if (!xml.isStartElement()) {
            continue;
        }

        if (xml.name() == "root-step") {
            rootStep = xml.readElementText().trimmed();
        } else if (xml.name() == "root-alter") {
            rootAlter = xml.readElementText().trimmed().toInt();
        } else if (xml.name() == "kind") {
            const QString symbolText = xml.attributes().value("text").toString().trimmed();
            kind = xml.readElementText().trimmed();
            if (!symbolText.isEmpty()) {
                out.symbolText = symbolText.toStdString();
            }
        } else if (xml.name() == "bass-step") {
            bassStep = xml.readElementText().trimmed();
        } else if (xml.name() == "bass-alter") {
            bassAlter = xml.readElementText().trimmed().toInt();
        }
    }

    const int rootPc = stepToPc(rootStep);
    if (rootPc >= 0) {
        out.rootPc = normalizePc(rootPc + rootAlter);
    }

    if (!bassStep.isEmpty()) {
        const int bassPc = stepToPc(bassStep);
        if (bassPc >= 0) {
            out.bassPc = normalizePc(bassPc + bassAlter);
        }
    }

    const QString effectiveKind = (kind == "none" && !analysisKindAttr.isEmpty()) ? analysisKindAttr : kind;

    // Treat as Augmented if:
    // - symbolText contains '#5', 'aug', or '+'
    // - kind value is 'augmented', 'augmented-seventh', or 'augmented-ninth'
    // - analysisKind attribute is 'augmented'
    const std::string kindStr = kind.toStdString();
    const std::string analysisKindStr = analysisKindAttr.toStdString();
    if (out.symbolText.find("#5") != std::string::npos ||
        out.symbolText.find("aug") != std::string::npos ||
        out.symbolText.find("+") != std::string::npos ||
        kindStr == "augmented" || kindStr == "augmented-seventh" || kindStr == "augmented-ninth" ||
        analysisKindStr == "augmented") {
        out.quality = ChordQuality::Augmented;
    } else {
        out.quality = kindToQuality(effectiveKind);
    }
    out.hasMinorSeventh = (effectiveKind == "minor-seventh" || effectiveKind == "minor-ninth"
                           || effectiveKind == "minor-11th" || effectiveKind == "minor-13th"
                           || effectiveKind == "dominant" || effectiveKind == "dominant-ninth"
                           || effectiveKind == "dominant-11th" || effectiveKind == "dominant-13th"
                           || effectiveKind == "augmented-seventh" || effectiveKind == "augmented-ninth");
    out.hasMajorSeventh = (effectiveKind == "major-seventh" || effectiveKind == "major-ninth"
                           || effectiveKind == "major-11th" || effectiveKind == "major-13th"
                           || effectiveKind == "major-minor");

    return out;
}

std::string parseRomanHarmony(QXmlStreamReader& xml)
{
    std::string roman;

    while (!(xml.isEndElement() && xml.name() == "harmony") && !xml.atEnd()) {
        xml.readNext();

        if (!xml.isStartElement()) {
            continue;
        }

        if (xml.name() == "numeral-root") {
            const QString text = xml.attributes().value("text").toString().trimmed();
            if (!text.isEmpty()) {
                roman = text.toStdString();
            }
            xml.readElementText();
        }
    }

    return roman;
}

std::optional<int> parseNotePitch(QXmlStreamReader& xml)
{
    QString step;
    int alter = 0;
    int octave = -100;
    bool isRest = false;

    while (!(xml.isEndElement() && xml.name() == "note") && !xml.atEnd()) {
        xml.readNext();

        if (!xml.isStartElement()) {
            continue;
        }

        if (xml.name() == "rest") {
            isRest = true;
        } else if (xml.name() == "step") {
            step = xml.readElementText().trimmed();
        } else if (xml.name() == "alter") {
            alter = xml.readElementText().trimmed().toInt();
        } else if (xml.name() == "octave") {
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

    return pitch;
}

std::vector<FixtureEvent> loadCatalogFixtureEvents(const QString& filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return {};
    }

    QXmlStreamReader xml(&file);

    std::vector<FixtureEvent> events;

    int currentKeyFifths = 0;
    bool currentKeyIsMajor = true;

    bool inMeasure = false;
    int currentMeasureNumber = -1;
    bool haveHarmony = false;
    ExpectedHarmony currentExpected;
    std::string currentExpectedRoman;
    std::vector<int> currentPitches;

    while (!xml.atEnd()) {
        xml.readNext();

        if (xml.isStartElement()) {
            if (xml.name() == "measure") {
                inMeasure = true;
                currentMeasureNumber = xml.attributes().value("number").toInt();
                haveHarmony = false;
                currentExpectedRoman.clear();
                currentPitches.clear();
            } else if (xml.name() == "fifths") {
                currentKeyFifths = xml.readElementText().trimmed().toInt();
            } else if (xml.name() == "mode") {
                currentKeyIsMajor = (xml.readElementText().trimmed().toLower() != "minor");
            } else if (xml.name() == "harmony" && inMeasure
                       && xml.attributes().hasAttribute("analysisKind")) {
                currentExpected = parseHarmony(xml);
                haveHarmony = true;
            } else if (xml.name() == "harmony" && inMeasure) {
                currentExpectedRoman = parseRomanHarmony(xml);
            } else if (xml.name() == "note" && inMeasure) {
                const std::optional<int> pitch = parseNotePitch(xml);
                if (pitch.has_value()) {
                    currentPitches.push_back(*pitch);
                }
            }
        } else if (xml.isEndElement() && xml.name() == "measure") {
            if (haveHarmony && !currentPitches.empty()) {
                FixtureEvent event;
                event.measureNumber = currentMeasureNumber;
                event.keyFifths = currentKeyFifths;
                event.keyIsMajor = currentKeyIsMajor;
                event.expected = currentExpected;
                event.expectedRoman = currentExpectedRoman;
                event.pitches = currentPitches;
                events.push_back(event);
            }
            inMeasure = false;
        }
    }

    return events;
}

std::vector<ChordAnalysisTone> toAnalysisTones(const std::vector<int>& pitches)
{
    std::vector<ChordAnalysisTone> tones;
    tones.reserve(pitches.size());

    bool first = true;
    for (int pitch : pitches) {
        ChordAnalysisTone tone;
        tone.pitch = pitch;
        tone.weight = 1.0;
        tone.isBass = first;
        tones.push_back(tone);
        first = false;
    }

    return tones;
}

std::set<std::string> loadMusicXmlCatalogSuffixes(const QString& filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return {};
    }

    QXmlStreamReader xml(&file);
    std::set<std::string> suffixes;

    while (!xml.atEnd()) {
        xml.readNext();
        if (!xml.isStartElement() || xml.name() != "harmony") {
            continue;
        }

        QString symbolText;
        bool isVisibleChord = false;
        while (!(xml.isEndElement() && xml.name() == "harmony") && !xml.atEnd()) {
            xml.readNext();
            if (xml.isStartElement() && xml.name() == "kind") {
                symbolText = xml.attributes().value("text").toString().trimmed();
                const QString kindVal = xml.readElementText().trimmed();
                isVisibleChord = (kindVal == "none");
                break;
            }
        }

        if (!isVisibleChord) {
            continue;
        }

        if (symbolText.startsWith("C")) {
            symbolText = symbolText.mid(1);
        }
        if (!symbolText.isEmpty()) {
            suffixes.insert(symbolText.toStdString());
        }
    }

    return suffixes;
}

size_t countVisibleChordHarmonies(const QString& filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return 0;
    }

    QXmlStreamReader xml(&file);
    size_t count = 0;

    while (!xml.atEnd()) {
        xml.readNext();
        if (xml.isStartElement() && xml.name() == "harmony"
            && xml.attributes().hasAttribute("analysisKind")) {
            ++count;
        }
    }

    return count;
}

std::vector<std::string> loadCatalogRomanNumerals(const QString& filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return {};
    }

    QXmlStreamReader xml(&file);
    std::vector<std::string> numerals;

    while (!xml.atEnd()) {
        xml.readNext();
        if (!xml.isStartElement() || xml.name() != "numeral-root") {
            continue;
        }

        const QString text = xml.attributes().value("text").toString().trimmed();
        if (!text.isEmpty()) {
            numerals.push_back(text.toStdString());
        }
    }

    return numerals;
}

std::set<std::string> loadMuseScoreCatalogSuffixes(const QString& filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return {};
    }

    QXmlStreamReader xml(&file);
    std::set<std::string> suffixes;

    while (!xml.atEnd()) {
        xml.readNext();
        if (!xml.isStartElement() || xml.name() != "chord") {
            continue;
        }

        while (!(xml.isEndElement() && xml.name() == "chord") && !xml.atEnd()) {
            xml.readNext();
            if (xml.isStartElement() && xml.name() == "name") {
                const QString suffix = xml.readElementText().trimmed();
                if (!suffix.isEmpty()) {
                    suffixes.insert(suffix.toStdString());
                }
                    break;
            }
        }
    }

    return suffixes;
}

} // namespace

TEST(Composing_ChordAnalyzerMusicXmlTests, DetectsExpectedAbstractHarmonyFromCatalog)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT) + "/data/chordanalyzer_catalog.musicxml";
    const std::vector<FixtureEvent> events = loadCatalogFixtureEvents(fixturePath);

    ASSERT_FALSE(events.empty());

    std::vector<SymbolRomanMismatch> symbolOrRomanMismatches;

    for (const FixtureEvent& event : events) {
        const ChordAnalysisResult result = ChordAnalyzer::analyzeChord(
            toAnalysisTones(event.pitches),
            event.keyIsMajor);

        EXPECT_TRUE(result.isValid);

        if (event.expected.rootPc >= 0) {
            EXPECT_EQ(result.rootPc, event.expected.rootPc);
        }

        if (event.expected.quality != ChordQuality::Unknown) {
            EXPECT_EQ(result.quality, event.expected.quality);
        }

        if (event.expected.bassPc.has_value()) {
            EXPECT_EQ(result.bassPc, *event.expected.bassPc);
        }

        EXPECT_EQ(result.hasMinorSeventh, event.expected.hasMinorSeventh);
        EXPECT_EQ(result.hasMajorSeventh, event.expected.hasMajorSeventh);

        std::string actualSymbol;
        if (!event.expected.symbolText.empty()) {
            actualSymbol = ChordSymbolFormatter::formatSymbol(result, event.keyFifths);
            EXPECT_TRUE(equivalentSymbolSpelling(actualSymbol, event.expected.symbolText));
        }

        std::string actualRoman;
        if (!event.expectedRoman.empty()) {
            actualRoman = ChordSymbolFormatter::formatRomanNumeral(result, event.keyIsMajor);
            EXPECT_EQ(actualRoman, event.expectedRoman);
        }

        const bool symbolMismatch = !event.expected.symbolText.empty()
                        && !equivalentSymbolSpelling(actualSymbol, event.expected.symbolText);
        const bool romanMismatch = !event.expectedRoman.empty() && actualRoman != event.expectedRoman;
        if (symbolMismatch || romanMismatch) {
            SymbolRomanMismatch mm;
            mm.measureNumber = event.measureNumber;
            mm.expectedSymbol = event.expected.symbolText;
            mm.actualSymbol = actualSymbol;
            mm.expectedRoman = event.expectedRoman;
            mm.actualRoman = actualRoman;
            mm.expectedRootPc = event.expected.rootPc;
            mm.actualRootPc = result.rootPc;
            mm.expectedQuality = event.expected.quality;
            mm.actualQuality = result.quality;
            symbolOrRomanMismatches.push_back(std::move(mm));
        }
    }

    if (!symbolOrRomanMismatches.empty()) {
        std::ostringstream oss;
        oss << "Symbol/Roman mismatches (measure, category, XML vs Analyzer):\n";
        for (const SymbolRomanMismatch& mm : symbolOrRomanMismatches) {
            const bool symbolMismatch = !mm.expectedSymbol.empty() && mm.expectedSymbol != mm.actualSymbol;
            const bool romanMismatch = !mm.expectedRoman.empty() && mm.expectedRoman != mm.actualRoman;
            const char* category = (symbolMismatch && romanMismatch) ? "symbol+roman"
                                : (symbolMismatch ? "symbol" : "roman");

            oss << "measure " << mm.measureNumber << ": " << category;
            if (symbolMismatch) {
                oss << " | symbol XML='" << mm.expectedSymbol
                    << "' Analyzer='" << mm.actualSymbol << "'";
            }
            if (romanMismatch) {
                oss << " | roman XML='" << mm.expectedRoman
                    << "' Analyzer='" << mm.actualRoman << "'";
            }
            oss << "\n";
        }
        ADD_FAILURE() << oss.str();
    }
}

TEST(Composing_ChordAnalyzerMusicXmlTests, ReportsCatalogSymbolAndRomanMismatches)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT) + "/data/chordanalyzer_catalog.musicxml";
    const std::vector<FixtureEvent> events = loadCatalogFixtureEvents(fixturePath);

    ASSERT_FALSE(events.empty());

    std::vector<SymbolRomanMismatch> mismatches;

    for (const FixtureEvent& event : events) {
        const ChordAnalysisResult result = ChordAnalyzer::analyzeChord(
            toAnalysisTones(event.pitches),
            event.keyIsMajor);

        // Compare abstract properties only
        bool abstractMismatch = false;
        std::ostringstream oss;
        oss << "measure " << event.measureNumber << ": ";

        if (event.expected.rootPc >= 0 && result.rootPc != event.expected.rootPc) {
            abstractMismatch = true;
            oss << "root mismatch (expected=" << event.expected.rootPc << ", actual=" << result.rootPc << ") ";
        }
        if (event.expected.bassPc.has_value() && result.bassPc != *event.expected.bassPc) {
            abstractMismatch = true;
            oss << "bass mismatch (expected=" << *event.expected.bassPc << ", actual=" << result.bassPc << ") ";
        }
        if (event.expected.quality != ChordQuality::Unknown && result.quality != event.expected.quality) {
            abstractMismatch = true;
            oss << "quality mismatch (expected=" << chordQualityToString(event.expected.quality) << ", actual=" << chordQualityToString(result.quality) << ") ";
        }
        if (result.hasMinorSeventh != event.expected.hasMinorSeventh) {
            abstractMismatch = true;
            oss << "minor7 mismatch (expected=" << event.expected.hasMinorSeventh << ", actual=" << result.hasMinorSeventh << ") ";
        }
        if (result.hasMajorSeventh != event.expected.hasMajorSeventh) {
            abstractMismatch = true;
            oss << "major7 mismatch (expected=" << event.expected.hasMajorSeventh << ", actual=" << result.hasMajorSeventh << ") ";
        }

        if (!abstractMismatch) {
            continue;
        }

        SymbolRomanMismatch mm;
        mm.measureNumber = event.measureNumber;
        mm.expectedSymbol = event.expected.symbolText;
        mm.actualSymbol = "";
        mm.expectedRoman = event.expectedRoman;
        mm.actualRoman = "";
        mm.expectedRootPc = event.expected.rootPc;
        mm.actualRootPc = result.rootPc;
        mm.expectedQuality = event.expected.quality;
        mm.actualQuality = result.quality;
        mismatches.push_back(std::move(mm));
        oss << "\n";
        // Optionally, print details for debugging
        // std::cout << oss.str();
    }

    if (!mismatches.empty()) {
        std::ostringstream oss;
        oss << "Abstract chord mismatch summary: total=" << mismatches.size() << "\n";
        oss << "Per-measure mismatches:\n";
        for (const SymbolRomanMismatch& mm : mismatches) {
            oss << "measure " << mm.measureNumber << ": ";
            oss << "root (xml=" << mm.expectedRootPc << ", analyser=" << mm.actualRootPc << ") ";
            oss << "quality (xml=" << chordQualityToString(mm.expectedQuality) << ", analyser=" << chordQualityToString(mm.actualQuality) << ") ";
            oss << "\n";

            // Debug info: input pitches and pitch classes
            const FixtureEvent* eventPtr = nullptr;
            for (const auto& ev : events) {
                if (ev.measureNumber == mm.measureNumber) {
                    eventPtr = &ev;
                    break;
                }
            }
            if (eventPtr) {
                oss << "  Debug: input pitches = [";
                for (size_t i = 0; i < eventPtr->pitches.size(); ++i) {
                    oss << eventPtr->pitches[i];
                    if (i + 1 < eventPtr->pitches.size()) oss << ", ";
                }
                oss << "]  pitch classes = [";
                for (size_t i = 0; i < eventPtr->pitches.size(); ++i) {
                    oss << normalizePc(eventPtr->pitches[i]);
                    if (i + 1 < eventPtr->pitches.size()) oss << ", ";
                }
                oss << "]\n";
            }
        }
        // Write the report to a file in composing/tests
        const std::string reportPath = (QString::fromUtf8(composing_tests_DATA_ROOT) + "/chord_mismatch_report.txt").toStdString();
        std::ofstream report(reportPath);
        if (report.is_open()) {
            report << oss.str();
            report.close();
        }
        FAIL() << oss.str();
    }
}

TEST(Composing_ChordAnalyzerMusicXmlTests, CatalogMusicXmlCoversMuseScoreChordSuffixes)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT) + "/data/chordanalyzer_catalog.musicxml";
    const QString museScoreCatalogPath = QString::fromUtf8(composing_tests_DATA_ROOT)
                                         + "/../../engraving/data/chords/chords.xml";

    const std::set<std::string> fixtureSuffixes = loadMusicXmlCatalogSuffixes(fixturePath);
    const std::set<std::string> museScoreSuffixes = loadMuseScoreCatalogSuffixes(museScoreCatalogPath);

    ASSERT_FALSE(fixtureSuffixes.empty());
    ASSERT_FALSE(museScoreSuffixes.empty());

    std::vector<std::string> missing;
    for (const std::string& suffix : museScoreSuffixes) {
        if (fixtureSuffixes.find(suffix) == fixtureSuffixes.end()) {
            missing.push_back(suffix);
        }
    }

    if (!missing.empty()) {
        std::string message = "Missing suffixes in MusicXML fixture:";
        for (const std::string& suffix : missing) {
            message += " ";
            message += suffix;
        }
        FAIL() << message;
    }
}

TEST(Composing_ChordAnalyzerMusicXmlTests, CatalogMusicXmlHasRomanNumeralPerChord)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT) + "/data/chordanalyzer_catalog.musicxml";

    const std::vector<std::string> romans = loadCatalogRomanNumerals(fixturePath);
    const size_t visibleChordCount = countVisibleChordHarmonies(fixturePath);

    ASSERT_GT(visibleChordCount, 0u);
    ASSERT_EQ(romans.size(), visibleChordCount);

    for (const std::string& roman : romans) {
        EXPECT_FALSE(roman.empty());
    }
}
