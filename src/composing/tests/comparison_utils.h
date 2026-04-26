/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#pragma once

#include <QString>
#include <QRegularExpression>

namespace mu::composing::testing {

// ── stripSymbol ──────────────────────────────────────────────────────────────
//
// Pure utility for test-infrastructure diff classification.
// Reduces a chord symbol or Roman numeral string to the equivalent form a
// catalog using a simplified notation convention would write.
//
// maxExtensionDegree: 7 / 9 / 11 / 13.  Other values are rejected (assert in
//   debug, input returned unchanged in release) and must not be passed.
//
// preserveAlterationsAboveLimit: when true, altered tones whose interval
//   degree exceeds maxExtensionDegree (b9, #9, #11, b13) survive in the
//   output.  When false, they are dropped along with natural extensions above
//   the limit.
//
// b5 and #5 are always dropped regardless of the flag; they are structural
// fifth alterations that simplified catalog conventions consistently omit.
//
// Never call this from production code (emitters, formatters, analyzers).
// It exists solely for comparison classification in test and tool contexts.
//
// Thread-safe (pure function, no shared state).

inline QString stripSymbol(const QString& symbol, int maxExtensionDegree,
                            bool preserveAlterationsAboveLimit)
{
    Q_ASSERT_X(maxExtensionDegree == 7 || maxExtensionDegree == 9
               || maxExtensionDegree == 11 || maxExtensionDegree == 13,
               "stripSymbol", "maxExtensionDegree must be 7, 9, 11, or 13");

    if (maxExtensionDegree != 7 && maxExtensionDegree != 9
        && maxExtensionDegree != 11 && maxExtensionDegree != 13) {
        return symbol;
    }

    if (symbol.isEmpty()) {
        return symbol;
    }

    QString s = symbol;

    // ── Step 1: (add...) tokens ───────────────────────────────────────────
    // Present in no-7th chords: I(add9), I(add11), I(add#11), i(addb9), etc.
    // Strip if the add-degree > maxExtensionDegree.
    {
        static const QRegularExpression kAddRe(QStringLiteral(R"(\(add[#b]?\d+\))"));
        int offset = 0;
        while (offset < s.length()) {
            const QRegularExpressionMatch m = kAddRe.match(s, offset);
            if (!m.hasMatch()) {
                break;
            }
            // Parse degree from token: everything after "add", skip optional sign
            const QString inner = m.captured(0);            // e.g. "(add#11)"
            int p = inner.indexOf(QLatin1String("add")) + 3;
            if (p < inner.length() && (inner[p] == '#' || inner[p] == 'b')) {
                ++p;
            }
            QString degStr;
            while (p < inner.length() && inner[p].isDigit()) {
                degStr += inner[p++];
            }
            const int deg = degStr.toInt();
            if (deg > maxExtensionDegree) {
                s.remove(m.capturedStart(), m.capturedLength());
                // offset unchanged: string shrank, re-scan from same position
            } else {
                offset = m.capturedEnd();
            }
        }
    }

    // ── Step 2: Alteration tokens ─────────────────────────────────────────
    // Removal order matters to avoid partial-string confusion:
    //   #11 before any "11" handling; b13 before "b1" ambiguity.
    //
    // b5, #5 (interval degree 5): always dropped — below any meaningful
    //   maxExtensionDegree, but simplified catalogs consistently omit them.
    //
    // b9, #9 (degree 9): drop when 9 > maxExtensionDegree and flag is false.
    // #11    (degree 11): drop when 11 > maxExtensionDegree and flag is false.
    // b13    (degree 13): drop when 13 > maxExtensionDegree and flag is false.

    if (11 > maxExtensionDegree && !preserveAlterationsAboveLimit) {
        s.remove(QStringLiteral("#11"));
    }
    if (13 > maxExtensionDegree && !preserveAlterationsAboveLimit) {
        s.remove(QStringLiteral("b13"));
    }
    if (9 > maxExtensionDegree && !preserveAlterationsAboveLimit) {
        s.remove(QStringLiteral("b9"));
        s.remove(QStringLiteral("#9"));
    }
    s.remove(QStringLiteral("b5"));
    s.remove(QStringLiteral("#5"));

    // ── Step 3: Reduce extension level number ─────────────────────────────
    // The extension level (7 / 9 / 11 / 13) appears in the string body NOT
    // preceded by '#' or 'b' (those are alteration-token prefixes).
    //
    // For suspended chords (contains "sus") at maxExtensionDegree == 7:
    //   strip the level number entirely — the base form is "[deg]sus4" with
    //   no explicit level.  This matches the catalog convention of labelling
    //   all sus4 variants simply as "Isus4".
    //
    // For all other chords:
    //   replace a level > maxExtensionDegree with maxExtensionDegree.

    const bool isSus = s.contains(QStringLiteral("sus"));

    // Iterate levels 13→11→9 (descending, stop when level ≤ maxExtensionDegree).
    static const struct { int level; QLatin1String str; } kLevels[] = {
        { 13, QLatin1String("13") },
        { 11, QLatin1String("11") },
        {  9, QLatin1String("9")  },
    };

    for (const auto& entry : kLevels) {
        if (entry.level <= maxExtensionDegree) {
            break;
        }
        int pos = 0;
        while (pos < s.length()) {
            const int idx = s.indexOf(entry.str, pos);
            if (idx < 0) {
                break;
            }
            // Skip if preceded by '#' or 'b' (part of an alteration token).
            const bool isAlt = (idx > 0 && (s[idx - 1] == '#' || s[idx - 1] == 'b'));
            if (!isAlt) {
                if (isSus && maxExtensionDegree == 7) {
                    // Sus4 at degree 7: remove level entirely
                    s.remove(idx, entry.str.size());
                    pos = idx;
                } else {
                    // Replace with maxExtensionDegree
                    const QString replacement = QString::number(maxExtensionDegree);
                    s.replace(idx, entry.str.size(), replacement);
                    pos = idx + replacement.length();
                }
                break; // one level number per chord
            }
            pos = idx + entry.str.size();
        }
        if (entry.level > maxExtensionDegree) {
            // Already handled or not found; continue to next lower level
        }
    }

    // For sus4 at degree 7: also strip a bare "7" level if present (e.g. I7sus4
    // → Isus4).  Guard: not preceded by 'M' (Maj7sus stays as Maj7sus), '#', or 'b'.
    if (isSus && maxExtensionDegree == 7) {
        int pos = 0;
        while (pos < s.length()) {
            const int idx = s.indexOf(QLatin1Char('7'), pos);
            if (idx < 0) {
                break;
            }
            const bool guard = (idx > 0
                                && (s[idx - 1] == 'M' || s[idx - 1] == '#'
                                    || s[idx - 1] == 'b'));
            if (!guard) {
                s.remove(idx, 1);
                pos = idx; // string shrank; re-scan same position
            } else {
                pos = idx + 1;
            }
        }
    }

    return s;
}

// ── classifyComparison ───────────────────────────────────────────────────────
//
// Applies the progressive comparison protocol from extension_stripping_policy.md
// to a single (analyzerOutput, catalogEntry) string pair.
//
// Returns:
//   DirectMatch    — exact strings are equal.
//   ConventionDiff — analyzerOutput matches catalogEntry after stripping at
//                    some degree + alteration-mode; matchedAtDegree and
//                    matchedWithAlterationsPreserved indicate which.
//   RealDiff       — no stripping configuration produces a match.

struct ComparisonResult {
    enum Kind { DirectMatch, ConventionDiff, RealDiff };
    Kind kind = RealDiff;
    int  matchedAtDegree = 0;                  // valid only for ConventionDiff
    bool matchedWithAlterationsPreserved = false; // valid only for ConventionDiff
};

inline ComparisonResult classifyComparison(const QString& analyzerOutput,
                                            const QString& catalogEntry)
{
    ComparisonResult result;

    // Step 1: direct comparison
    if (analyzerOutput == catalogEntry) {
        result.kind = ComparisonResult::DirectMatch;
        return result;
    }

    // Step 2–3: progressive stripping — highest degree first (least stripping).
    // At each degree try preserveAlterationsAboveLimit=true first, then false.
    static const int kDegrees[] = { 13, 11, 9, 7 };

    for (const int deg : kDegrees) {
        for (const bool preserveAlts : { true, false }) {
            if (stripSymbol(analyzerOutput, deg, preserveAlts) == catalogEntry) {
                result.kind = ComparisonResult::ConventionDiff;
                result.matchedAtDegree = deg;
                result.matchedWithAlterationsPreserved = preserveAlts;
                return result;
            }
        }
    }

    // Step 4: no match found
    result.kind = ComparisonResult::RealDiff;
    return result;
}

} // namespace mu::composing::testing
