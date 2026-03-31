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
    std::vector<int> tpcs;   // parallel to pitches; -1 = not available
    int keyFifths = 0;
    KeyMode keyMode = KeyMode::Ionian;
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
    // Exception: when analysisKind explicitly specifies a non-augmented quality (e.g.
    // 'suspended-fourth', 'minor'), that takes priority over the symbol-text inference
    // so that e.g. C7sus#5 is classified as Suspended4, not Augmented.
    const std::string kindStr = kind.toStdString();
    const std::string analysisKindStr = analysisKindAttr.toStdString();
    const bool analysisKindOverridesAugmented = analysisKindStr == "suspended-fourth"
                                                || analysisKindStr == "suspended-second"
                                                || analysisKindStr == "minor"
                                                || analysisKindStr == "minor-seventh";
    if (!analysisKindOverridesAugmented
        && (out.symbolText.find("#5") != std::string::npos ||
            out.symbolText.find("aug") != std::string::npos ||
            out.symbolText.find("+") != std::string::npos ||
            kindStr == "augmented" || kindStr == "augmented-seventh" || kindStr == "augmented-ninth" ||
            analysisKindStr == "augmented")) {
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

    // For suspended chords, derive hasMinorSeventh from the chord symbol text.
    // "C7sus", "C9sus", "C13sus#11" all imply a minor 7th is present.
    // "Csusb9" does NOT — a flat-9 alone does not imply a 7th.
    if (!out.hasMinorSeventh && !out.hasMajorSeventh
        && (out.quality == ChordQuality::Suspended2 || out.quality == ChordQuality::Suspended4)) {
        const std::string& s = out.symbolText;
        if (s.find("Maj") == std::string::npos) {
            // Plain "7" → minor 7th directly.
            const bool has7 = s.find("7") != std::string::npos;
            // "9" implies 7th only when unmodified (not "b9" or "#9" standing alone).
            const bool has9 = [&]() {
                const auto pos = s.find("9");
                return pos != std::string::npos && pos > 0
                       && s[pos - 1] != 'b' && s[pos - 1] != '#';
            }();
            // 11th and 13th always imply 7th in jazz chord nomenclature.
            const bool has11or13 = s.find("11") != std::string::npos
                                   || s.find("13") != std::string::npos;
            out.hasMinorSeventh = has7 || has9 || has11or13;
        }
    }

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

/// TPC (tonal pitch class) from MusicXML step + alter.
/// Encoding: F=14, C=15, G=16, D=17, A=18, E=19, B=20; each sharp adds 7, each flat subtracts 7.
/// Returns -1 if step is unrecognised.
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

std::optional<NotePitchTpc> parseNotePitch(QXmlStreamReader& xml)
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

    return NotePitchTpc{ pitch, tpcFromStepAlter(step, alter) };
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
    KeyMode currentKeyMode = KeyMode::Ionian;

    bool inMeasure = false;
    int currentMeasureNumber = -1;
    bool haveHarmony = false;
    ExpectedHarmony currentExpected;
    std::string currentExpectedRoman;
    std::vector<int> currentPitches;
    std::vector<int> currentTpcs;

    while (!xml.atEnd()) {
        xml.readNext();

        if (xml.isStartElement()) {
            if (xml.name() == "measure") {
                inMeasure = true;
                currentMeasureNumber = xml.attributes().value("number").toInt();
                haveHarmony = false;
                currentExpectedRoman.clear();
                currentPitches.clear();
                currentTpcs.clear();
            } else if (xml.name() == "fifths") {
                currentKeyFifths = xml.readElementText().trimmed().toInt();
            } else if (xml.name() == "mode") {
                {
                    const QString modeStr = xml.readElementText().trimmed().toLower();
                    if (modeStr == "minor")          currentKeyMode = KeyMode::Aeolian;
                    else if (modeStr == "dorian")     currentKeyMode = KeyMode::Dorian;
                    else if (modeStr == "phrygian")   currentKeyMode = KeyMode::Phrygian;
                    else if (modeStr == "lydian")     currentKeyMode = KeyMode::Lydian;
                    else if (modeStr == "mixolydian") currentKeyMode = KeyMode::Mixolydian;
                    else if (modeStr == "aeolian")    currentKeyMode = KeyMode::Aeolian;
                    else if (modeStr == "locrian")    currentKeyMode = KeyMode::Locrian;
                    else                              currentKeyMode = KeyMode::Ionian;
                }
            } else if (xml.name() == "harmony" && inMeasure
                       && xml.attributes().hasAttribute("analysisKind")) {
                // "other" entries are suffix-coverage annotations only; skip them.
                const QString ak = xml.attributes().value("analysisKind").toString().trimmed();
                ExpectedHarmony parsed = parseHarmony(xml);
                if (ak != "other") {
                    currentExpected = std::move(parsed);
                    haveHarmony = true;
                }
            } else if (xml.name() == "harmony" && inMeasure) {
                currentExpectedRoman = parseRomanHarmony(xml);
            } else if (xml.name() == "note" && inMeasure) {
                const std::optional<NotePitchTpc> pt = parseNotePitch(xml);
                if (pt.has_value()) {
                    currentPitches.push_back(pt->pitch);
                    currentTpcs.push_back(pt->tpc);
                }
            }
        } else if (xml.isEndElement() && xml.name() == "measure") {
            if (haveHarmony && !currentPitches.empty()) {
                FixtureEvent event;
                event.measureNumber = currentMeasureNumber;
                event.keyFifths = currentKeyFifths;
                event.keyMode = currentKeyMode;
                event.expected = currentExpected;
                event.expectedRoman = currentExpectedRoman;
                event.pitches = currentPitches;
                event.tpcs = currentTpcs;
                events.push_back(event);
            }
            inMeasure = false;
        }
    }

    return events;
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

    // Named / modal chord exceptions: these catalog entries use informal labels
    // that go beyond pitch-content analysis.  Abstract detection (root/quality/7th)
    // is correct; only the symbol or Roman numeral string differs because the
    // catalog annotation encodes information the analyzer cannot derive from pitches.
    //   m60  Cm9b5: analyzer returns Cm7b5 — 9th extension not tracked separately.
    //   m164 C7alt: informal alt label; analyzer returns the specific alteration spelling.
    //   m285 CTristan: non-standard pitch set, no matching template.
    //   m333 CPhryg: modal label for Cm11 — Phrygian flat-2 is not a chord quality.
    //   m340 Csus#4: catalog Roman numeral is "I" (tonic, no quality suffix);
    //        analyzer correctly returns "Isus4" — annotation style difference.
    static const std::set<int> kSymbolExceptions = { 60, 164, 285, 333, 340 };

    // Thread temporal context between successive catalog entries so the
    // root-continuity bonus can resolve ambiguous chords (e.g. m264 {C,Eb,Ab}).
    int previousRootPc = -1;

    for (const FixtureEvent& event : events) {
        ChordTemporalContext temporalCtx;
        temporalCtx.previousRootPc = previousRootPc;
        const auto results = ChordAnalyzer::analyzeChord(
            toAnalysisTones(event.pitches, event.tpcs),
            event.keyFifths,
            event.keyMode,
            &temporalCtx);

        if (event.expected.quality != ChordQuality::Unknown
            && event.expected.quality != ChordQuality::Power) {
            EXPECT_FALSE(results.empty());
        }
        if (results.empty()) {
            previousRootPc = -1;
            continue;
        }
        const ChordAnalysisResult& result = results.front();
        previousRootPc = result.rootPc;

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
        if (!event.expected.symbolText.empty()
                && !kSymbolExceptions.count(event.measureNumber)) {
            actualSymbol = ChordSymbolFormatter::formatSymbol(result, event.keyFifths);
            EXPECT_TRUE(equivalentSymbolSpelling(actualSymbol, event.expected.symbolText));
        }

        std::string actualRoman;
        if (!event.expectedRoman.empty()
                && !kSymbolExceptions.count(event.measureNumber)) {
            actualRoman = ChordSymbolFormatter::formatRomanNumeral(result);
            EXPECT_EQ(actualRoman, event.expectedRoman);
        }

        const bool symbolMismatch = !event.expected.symbolText.empty()
                        && !kSymbolExceptions.count(event.measureNumber)
                        && !equivalentSymbolSpelling(actualSymbol, event.expected.symbolText);
        const bool romanMismatch = !event.expectedRoman.empty()
                        && !kSymbolExceptions.count(event.measureNumber)
                        && actualRoman != event.expectedRoman;
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

// Writes a debug context block (pitches, pitch classes, TPCs, key) to a stream.
static void writeMismatchDebugContext(std::ostringstream& oss,
                                      const std::vector<int>& pitches,
                                      const std::vector<int>& tpcs,
                                      int keyFifths,
                                      KeyMode keyMode)
{
    oss << "  key=" << keyFifths << (keyModeIsMajor(keyMode) ? "maj" : "min");
    oss << "  pitches=[";
    for (size_t i = 0; i < pitches.size(); ++i) {
        oss << pitches[i];
        if (i + 1 < pitches.size()) { oss << ","; }
    }
    oss << "]  pcs=[";
    for (size_t i = 0; i < pitches.size(); ++i) {
        oss << normalizePc(pitches[i]);
        if (i + 1 < pitches.size()) { oss << ","; }
    }
    oss << "]  tpcs=[";
    for (size_t i = 0; i < tpcs.size(); ++i) {
        oss << tpcs[i];
        if (i + 1 < tpcs.size()) { oss << ","; }
    }
    oss << "]\n";
}

/// Writes two-section mismatch report to chord_mismatch_report.txt:
///   Section 1 — Abstract mismatches (root / quality / 7th flags wrong).
///                These are real analyzer bugs; the test FAILs when any are present.
///   Section 2 — Symbol / Roman-numeral mismatches (abstract correct but text differs).
///                Informational only — lets you distinguish formatter bugs from
///                catalog annotation inconsistencies by inspecting the pitch content.
TEST(Composing_ChordAnalyzerMusicXmlTests, ReportsCatalogSymbolAndRomanMismatches)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT) + "/data/chordanalyzer_catalog.musicxml";
    const std::vector<FixtureEvent> events = loadCatalogFixtureEvents(fixturePath);

    ASSERT_FALSE(events.empty());

    struct MismatchEntry {
        int measureNumber = -1;
        // Abstract fields
        int expectedRootPc = -1;
        int actualRootPc   = -1;
        ChordQuality expectedQuality = ChordQuality::Unknown;
        ChordQuality actualQuality   = ChordQuality::Unknown;
        std::string abstractDetail;   // human-readable description of what mismatched
        // Symbol / Roman fields
        std::string expectedSymbol;
        std::string actualSymbol;
        std::string expectedRoman;
        std::string actualRoman;
        // Debug context
        std::vector<int> pitches;
        std::vector<int> tpcs;
        int keyFifths  = 0;
        KeyMode keyMode = KeyMode::Ionian;
    };

    std::vector<MismatchEntry> abstractMismatches;
    std::vector<MismatchEntry> symbolMismatches;

    int previousRootPcReport = -1;

    for (const FixtureEvent& event : events) {
        // Skip events that produce insufficient pitch classes for analysis.
        // This happens when the catalog measure has fewer than 3 distinct sounding PCs
        // (e.g. a dyad or single note used as a section separator).
        ChordTemporalContext temporalCtx;
        temporalCtx.previousRootPc = previousRootPcReport;
        const auto results = ChordAnalyzer::analyzeChord(
            toAnalysisTones(event.pitches, event.tpcs),
            event.keyFifths,
            event.keyMode,
            &temporalCtx);

        if (results.empty()) {
            previousRootPcReport = -1;
            continue;
        }
        const ChordAnalysisResult& result = results.front();
        previousRootPcReport = result.rootPc;

        // ── Abstract mismatch detection ──────────────────────────────────────
        std::ostringstream abstractDetail;
        bool hasAbstractMismatch = false;

        if (event.expected.rootPc >= 0 && result.rootPc != event.expected.rootPc) {
            hasAbstractMismatch = true;
            abstractDetail << "root(xml=" << event.expected.rootPc << ",ana=" << result.rootPc << ") ";
        }
        if (event.expected.bassPc.has_value() && result.bassPc != *event.expected.bassPc) {
            hasAbstractMismatch = true;
            abstractDetail << "bass(xml=" << *event.expected.bassPc << ",ana=" << result.bassPc << ") ";
        }
        if (event.expected.quality != ChordQuality::Unknown && result.quality != event.expected.quality) {
            hasAbstractMismatch = true;
            abstractDetail << "quality(xml=" << chordQualityToString(event.expected.quality)
                           << ",ana=" << chordQualityToString(result.quality) << ") ";
        }
        if (result.hasMinorSeventh != event.expected.hasMinorSeventh) {
            hasAbstractMismatch = true;
            abstractDetail << "minor7(xml=" << event.expected.hasMinorSeventh
                           << ",ana=" << result.hasMinorSeventh << ") ";
        }
        if (result.hasMajorSeventh != event.expected.hasMajorSeventh) {
            hasAbstractMismatch = true;
            abstractDetail << "major7(xml=" << event.expected.hasMajorSeventh
                           << ",ana=" << result.hasMajorSeventh << ") ";
        }

        if (hasAbstractMismatch) {
            MismatchEntry mm;
            mm.measureNumber   = event.measureNumber;
            mm.expectedRootPc  = event.expected.rootPc;
            mm.actualRootPc    = result.rootPc;
            mm.expectedQuality = event.expected.quality;
            mm.actualQuality   = result.quality;
            mm.abstractDetail  = abstractDetail.str();
            mm.pitches         = event.pitches;
            mm.tpcs            = event.tpcs;
            mm.keyFifths       = event.keyFifths;
            mm.keyMode      = event.keyMode;
            abstractMismatches.push_back(std::move(mm));
        }

        // ── Symbol / Roman mismatch detection ────────────────────────────────
        // Checked independently of abstract — a symbol mismatch on an abstractly
        // correct chord signals a formatter bug or a catalog annotation inconsistency.
        // Skip symbol check when catalog quality is Unknown (blues, non-standard kinds).
        const std::string actualSymbol =
            (!event.expected.symbolText.empty() && event.expected.quality != ChordQuality::Unknown)
            ? ChordSymbolFormatter::formatSymbol(result, event.keyFifths) : "";
        const std::string actualRoman =
            !event.expectedRoman.empty()
            ? ChordSymbolFormatter::formatRomanNumeral(result) : "";

        const bool symbolMismatch = !actualSymbol.empty()
                                    && !equivalentSymbolSpelling(actualSymbol, event.expected.symbolText);
        const bool romanMismatch  = !actualRoman.empty() && actualRoman != event.expectedRoman;

        if (symbolMismatch || romanMismatch) {
            MismatchEntry mm;
            mm.measureNumber   = event.measureNumber;
            mm.expectedRootPc  = event.expected.rootPc;
            mm.actualRootPc    = result.rootPc;
            mm.expectedQuality = event.expected.quality;
            mm.actualQuality   = result.quality;
            mm.expectedSymbol  = event.expected.symbolText;
            mm.actualSymbol    = actualSymbol;
            mm.expectedRoman   = event.expectedRoman;
            mm.actualRoman     = actualRoman;
            mm.pitches         = event.pitches;
            mm.tpcs            = event.tpcs;
            mm.keyFifths       = event.keyFifths;
            mm.keyMode      = event.keyMode;
            symbolMismatches.push_back(std::move(mm));
        }
    }

    // ── Build report ─────────────────────────────────────────────────────────
    std::ostringstream report;

    report << "=== Abstract chord mismatch summary: total=" << abstractMismatches.size() << " ===\n";
    report << "Per-measure abstract mismatches (root/quality wrong — real analyzer bugs):\n";
    for (const MismatchEntry& mm : abstractMismatches) {
        report << "measure " << mm.measureNumber << ": " << mm.abstractDetail << "\n";
        writeMismatchDebugContext(report, mm.pitches, mm.tpcs, mm.keyFifths, mm.keyMode);
    }

    report << "\n=== Symbol/Roman mismatch summary: total=" << symbolMismatches.size() << " ===\n";
    report << "Per-measure symbol mismatches (abstract correct; inspect pitches to determine\n"
           << "  whether this is a formatter bug or a catalog annotation inconsistency):\n";
    for (const MismatchEntry& mm : symbolMismatches) {
        const bool sym = !mm.expectedSymbol.empty() && mm.expectedSymbol != mm.actualSymbol;
        const bool rom = !mm.expectedRoman.empty()  && mm.expectedRoman  != mm.actualRoman;
        const char* cat = (sym && rom) ? "symbol+roman" : (sym ? "symbol" : "roman");
        report << "measure " << mm.measureNumber << " [" << cat << "]";
        if (sym) {
            report << "  xml='" << mm.expectedSymbol << "'  analyzer='" << mm.actualSymbol << "'";
        }
        if (rom) {
            report << "  roman xml='" << mm.expectedRoman << "'  analyzer='" << mm.actualRoman << "'";
        }
        report << "\n";
        writeMismatchDebugContext(report, mm.pitches, mm.tpcs, mm.keyFifths, mm.keyMode);
    }

    const std::string reportPath = (QString::fromUtf8(composing_tests_DATA_ROOT)
                                    + "/chord_mismatch_report.txt").toStdString();
    std::ofstream reportFile(reportPath);
    if (reportFile.is_open()) {
        reportFile << report.str();
    }

    // Only hard-fail on abstract mismatches; symbol mismatches are informational.
    if (!abstractMismatches.empty()) {
        std::ostringstream failMsg;
        failMsg << "Abstract chord mismatch summary: total=" << abstractMismatches.size() << "\n";
        failMsg << "Per-measure mismatches:\n";
        for (const MismatchEntry& mm : abstractMismatches) {
            failMsg << "measure " << mm.measureNumber << ": " << mm.abstractDetail << "\n";
            writeMismatchDebugContext(failMsg, mm.pitches, mm.tpcs, mm.keyFifths, mm.keyMode);
        }
        FAIL() << failMsg.str();
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

/// Runs the context-progressions fixture, threading both previousRootPc AND
/// previousQuality between measures.  Each measure must resolve to the expected
/// root and quality; the quality-guided resolution biases should fire on the
/// designated resolution chords (M3, M6, M9, M12).
TEST(Composing_ChordAnalyzerMusicXmlTests, DetectsExpectedHarmonyWithTemporalContext)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT)
                                + "/data/chordanalyzer_context.musicxml";
    const std::vector<FixtureEvent> events = loadCatalogFixtureEvents(fixturePath);

    ASSERT_EQ(events.size(), 13u);

    int previousRootPc = -1;
    ChordQuality previousQuality = ChordQuality::Unknown;

    for (const FixtureEvent& event : events) {
        ChordTemporalContext ctx;
        ctx.previousRootPc  = previousRootPc;
        ctx.previousQuality = previousQuality;

        const auto results = ChordAnalyzer::analyzeChord(
            toAnalysisTones(event.pitches, event.tpcs),
            event.keyFifths,
            event.keyMode,
            &ctx);

        ASSERT_FALSE(results.empty()) << "measure " << event.measureNumber;
        const ChordAnalysisResult& result = results.front();

        if (event.expected.rootPc >= 0) {
            EXPECT_EQ(result.rootPc, event.expected.rootPc) << "measure " << event.measureNumber;
        }
        if (event.expected.quality != ChordQuality::Unknown) {
            EXPECT_EQ(result.quality, event.expected.quality) << "measure " << event.measureNumber;
        }
        if (!event.expected.symbolText.empty()) {
            const std::string actualSym = ChordSymbolFormatter::formatSymbol(result, event.keyFifths);
            EXPECT_TRUE(equivalentSymbolSpelling(actualSym, event.expected.symbolText))
                << "measure " << event.measureNumber
                << ": expected '" << event.expected.symbolText << "' got '" << actualSym << "'";
        }

        previousRootPc  = result.rootPc;
        previousQuality = result.quality;
    }
}

TEST(Composing_ChordAnalyzerMusicXmlTests, CatalogMusicXmlHasRomanNumeralPerChord)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT) + "/data/chordanalyzer_catalog.musicxml";

    const std::vector<FixtureEvent> events = loadCatalogFixtureEvents(fixturePath);
    ASSERT_FALSE(events.empty());

    std::vector<int> unexpectedlyMissing;
    for (const FixtureEvent& event : events) {
        if (event.expectedRoman.empty()) {
            unexpectedlyMissing.push_back(event.measureNumber);
        }
    }

    if (!unexpectedlyMissing.empty()) {
        std::ostringstream oss;
        oss << unexpectedlyMissing.size() << " chord event(s) lack Roman numeral annotation:";
        for (int m : unexpectedlyMissing) { oss << " m" << m; }
        FAIL() << oss.str();
    }
}

/// Diagnostic dump: prints every ranked candidate for every chord in the
/// catalog fixture.  Not a pass/fail test — used for manual evaluation.
TEST(Composing_ChordAnalyzerMusicXmlTests, DumpAllCandidatesForContextFile)
{
    const QString fixturePath = QString::fromUtf8(composing_tests_DATA_ROOT)
                                + "/data/chordanalyzer_catalog.musicxml";
    const std::vector<FixtureEvent> events = loadCatalogFixtureEvents(fixturePath);

    const char* pcNames[12] = { "C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B" };

    for (const FixtureEvent& event : events) {
        const auto results = ChordAnalyzer::analyzeChord(
            toAnalysisTones(event.pitches, event.tpcs),
            event.keyFifths,
            event.keyMode);

        // Pitch-class set for display
        std::string pcs;
        for (int p : event.pitches) {
            if (!pcs.empty()) pcs += ",";
            pcs += pcNames[((p % 12) + 12) % 12];
        }

        std::printf("\nm%-4d key=%dmaj  pcs={%s}\n",
                    event.measureNumber, event.keyFifths, pcs.c_str());

        if (results.empty()) {
            std::printf("  (no candidates)\n");
            continue;
        }
        std::set<std::string> seen;
        size_t rank = 0;
        for (const auto& r : results) {
            if (rank >= 8) break;
            const std::string sym = ChordSymbolFormatter::formatSymbol(r, event.keyFifths);
            if (sym.empty() || !seen.insert(sym).second) {
                continue;
            }
            ++rank;
            std::printf("  #%-2zu  score=%.2f  root=%-3s quality=%-14s  sym=%s\n",
                        rank, r.score,
                        pcNames[r.rootPc],
                        chordQualityToString(r.quality),
                        sym.c_str());
        }
    }
    std::fflush(stdout);
    // Always passes — output is for manual inspection.
    SUCCEED();
}
