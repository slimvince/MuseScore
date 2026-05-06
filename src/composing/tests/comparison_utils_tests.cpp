/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 */

#include <gtest/gtest.h>
#include "comparison_utils.h"

using namespace mu::composing::testing;

// ── stripSymbol — edge cases ─────────────────────────────────────────────────

TEST(ComparisonUtils_StripSymbol, EmptyStringReturnsEmpty)
{
    EXPECT_EQ(stripSymbol(QString(), 7, false), QString());
    EXPECT_EQ(stripSymbol(QString(), 9, true),  QString());
}

TEST(ComparisonUtils_StripSymbol, ChordsWithNoExtensionsReturnUnchanged)
{
    // Plain triad / 7th chord already at base — nothing to strip
    EXPECT_EQ(stripSymbol("I",    7, false), "I");
    EXPECT_EQ(stripSymbol("i",    7, false), "i");
    EXPECT_EQ(stripSymbol("IM7",  7, false), "IM7");
    EXPECT_EQ(stripSymbol("I7",   7, false), "I7");
    EXPECT_EQ(stripSymbol("iø7",  7, false), "iø7");
    EXPECT_EQ(stripSymbol("I+7",  7, false), "I+7");
    EXPECT_EQ(stripSymbol("Isus4",7, false), "Isus4");
    EXPECT_EQ(stripSymbol("i7",   7, false), "i7");
    EXPECT_EQ(stripSymbol("C7",   7, false), "C7");
    EXPECT_EQ(stripSymbol("Cm7",  7, false), "Cm7");
    EXPECT_EQ(stripSymbol("CMaj7",7, false), "CMaj7");
}

// ── stripSymbol — degree 7, alterations dropped (false) ─────────────────────

TEST(ComparisonUtils_StripSymbol, Degree7DropsAlterationsAndExtensions)
{
    // Natural extensions stripped and level replaced with 7
    EXPECT_EQ(stripSymbol("IM9",      7, false), "IM7");
    EXPECT_EQ(stripSymbol("IM11",     7, false), "IM7");
    EXPECT_EQ(stripSymbol("IM13",     7, false), "IM7");
    EXPECT_EQ(stripSymbol("I9",       7, false), "I7");
    EXPECT_EQ(stripSymbol("I11",      7, false), "I7");
    EXPECT_EQ(stripSymbol("I13",      7, false), "I7");
    EXPECT_EQ(stripSymbol("i9",       7, false), "i7");
    EXPECT_EQ(stripSymbol("i11",      7, false), "i7");
    EXPECT_EQ(stripSymbol("i13",      7, false), "i7");
    EXPECT_EQ(stripSymbol("I+9",      7, false), "I+7");
    EXPECT_EQ(stripSymbol("I+13",     7, false), "I+7");
    EXPECT_EQ(stripSymbol("iø9",      7, false), "iø7");
    EXPECT_EQ(stripSymbol("iM9",      7, false), "iM7");
    EXPECT_EQ(stripSymbol("I+M9",     7, false), "I+M7");

    // Alteration-only (no natural extension above 7th)
    EXPECT_EQ(stripSymbol("I7b9",     7, false), "I7");
    EXPECT_EQ(stripSymbol("I7#9",     7, false), "I7");
    EXPECT_EQ(stripSymbol("I7#11",    7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b13",    7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b5",     7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b9#11",  7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b9b13",  7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b5b9b13",7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b5#9b13",7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b9#9",   7, false), "I7");   // both b9 and #9
    EXPECT_EQ(stripSymbol("IM7b5",    7, false), "IM7");
    EXPECT_EQ(stripSymbol("IM7b13",   7, false), "IM7");
    EXPECT_EQ(stripSymbol("IM7#11",   7, false), "IM7");
    EXPECT_EQ(stripSymbol("i7b13",    7, false), "i7");
    EXPECT_EQ(stripSymbol("i7#5",     7, false), "i7");

    // Extension + alterations
    EXPECT_EQ(stripSymbol("I9b13",    7, false), "I7");
    EXPECT_EQ(stripSymbol("I9#11",    7, false), "I7");
    EXPECT_EQ(stripSymbol("I13b9",    7, false), "I7");
    EXPECT_EQ(stripSymbol("I13b9#11", 7, false), "I7");
    EXPECT_EQ(stripSymbol("I13#9#11", 7, false), "I7");
    EXPECT_EQ(stripSymbol("IM9#11",   7, false), "IM7");
    EXPECT_EQ(stripSymbol("IM13#11",  7, false), "IM7");
    EXPECT_EQ(stripSymbol("I+9",      7, false), "I+7");
    EXPECT_EQ(stripSymbol("I+13#11",  7, false), "I+7");
    EXPECT_EQ(stripSymbol("iø9#11",   7, false), "iø7");
    EXPECT_EQ(stripSymbol("iø7#11",   7, false), "iø7");
    EXPECT_EQ(stripSymbol("I13b5",    7, false), "I7");
    EXPECT_EQ(stripSymbol("I9b5b13",  7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b5b9",   7, false), "I7");
    EXPECT_EQ(stripSymbol("I7b5#9b13",7, false), "I7");
}

TEST(ComparisonUtils_StripSymbol, Degree7Sus4StripsLevelEntirelyToBaseSus4)
{
    EXPECT_EQ(stripSymbol("I7sus4",          7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I11sus4",         7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I13sus4",         7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I11b9sus4",       7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I11b5sus4",       7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I13b9#11sus4",    7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I13#5#9#11sus4",  7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I11b9b13sus4",    7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I11b5b9b13sus4",  7, false), "Isus4");
    EXPECT_EQ(stripSymbol("I13#5b9#11sus4",  7, false), "Isus4");
    // Already at base — unchanged
    EXPECT_EQ(stripSymbol("Isus4",           7, false), "Isus4");
}

TEST(ComparisonUtils_StripSymbol, Degree7AddsNotation)
{
    EXPECT_EQ(stripSymbol("I(add9)",    7, false), "I");
    EXPECT_EQ(stripSymbol("I(add11)",   7, false), "I");
    EXPECT_EQ(stripSymbol("I(add#11)",  7, false), "I");
    EXPECT_EQ(stripSymbol("I(add13)",   7, false), "I");
    EXPECT_EQ(stripSymbol("i(add9)",    7, false), "i");
    EXPECT_EQ(stripSymbol("I(addb9)",   7, false), "I");
}

// ── stripSymbol — degree 7, alterations preserved (true) ────────────────────

TEST(ComparisonUtils_StripSymbol, Degree7PreservesAlterationsWhenFlagTrue)
{
    // Natural extensions stripped, but b9/#9/#11/b13 survive
    EXPECT_EQ(stripSymbol("I7b9",      7, true), "I7b9");
    EXPECT_EQ(stripSymbol("I7#11",     7, true), "I7#11");
    EXPECT_EQ(stripSymbol("I7b13",     7, true), "I7b13");
    EXPECT_EQ(stripSymbol("I7b9#11",   7, true), "I7b9#11");
    EXPECT_EQ(stripSymbol("I13b9",     7, true), "I7b9");   // 13→7, b9 preserved
    EXPECT_EQ(stripSymbol("I13b9#11",  7, true), "I7b9#11");
    EXPECT_EQ(stripSymbol("I9#11b13",  7, true), "I7#11b13"); // 9→7, #11+b13 preserved
    EXPECT_EQ(stripSymbol("IM9#11",    7, true), "IM7#11");

    // b5/#5 always dropped regardless of flag
    EXPECT_EQ(stripSymbol("I7b5b9",    7, true), "I7b9");
    EXPECT_EQ(stripSymbol("I7b5#9b13", 7, true), "I7#9b13");
}

// ── stripSymbol — degree 9 ───────────────────────────────────────────────────

TEST(ComparisonUtils_StripSymbol, Degree9DropsFalse)
{
    // 9th stays; 11th/13th stripped
    EXPECT_EQ(stripSymbol("I9",       9, false), "I9");
    EXPECT_EQ(stripSymbol("I11",      9, false), "I9");
    EXPECT_EQ(stripSymbol("I13",      9, false), "I9");
    EXPECT_EQ(stripSymbol("I9#11",    9, false), "I9");
    EXPECT_EQ(stripSymbol("I9b13",    9, false), "I9");
    EXPECT_EQ(stripSymbol("I13#11",   9, false), "I9");
    EXPECT_EQ(stripSymbol("I13b9",    9, false), "I9b9");   // b9 degree 9 ≤ 9, keep
    EXPECT_EQ(stripSymbol("I7b9",     9, false), "I7b9");   // b9 degree 9 ≤ 9, keep
    EXPECT_EQ(stripSymbol("I9b5",     9, false), "I9");     // b5 always dropped
    EXPECT_EQ(stripSymbol("IM13#11",  9, false), "IM9");
    EXPECT_EQ(stripSymbol("I11sus4",  9, false), "I9sus4");
    EXPECT_EQ(stripSymbol("I13sus4",  9, false), "I9sus4");
}

TEST(ComparisonUtils_StripSymbol, Degree9PreserveTrue)
{
    // 11/#11 above 9 but preserved by flag
    EXPECT_EQ(stripSymbol("I11",      9, true), "I9");       // natural 11 → not alteration
    EXPECT_EQ(stripSymbol("I9#11",    9, true), "I9#11");    // #11 above 9, preserved
    EXPECT_EQ(stripSymbol("I13b13",   9, true), "I9b13");    // 13→9, b13 preserved
    EXPECT_EQ(stripSymbol("I13#11b13",9, true), "I9#11b13");
}

// ── stripSymbol — degree 11 ──────────────────────────────────────────────────

TEST(ComparisonUtils_StripSymbol, Degree11DropsFalse)
{
    EXPECT_EQ(stripSymbol("I11",      11, false), "I11");
    EXPECT_EQ(stripSymbol("I13",      11, false), "I11");
    EXPECT_EQ(stripSymbol("I13b13",   11, false), "I11");    // b13 stripped
    EXPECT_EQ(stripSymbol("I13#11",   11, false), "I11#11"); // 13→11, #11 ≤ 11 keep
    EXPECT_EQ(stripSymbol("I9b13",    11, false), "I9");     // b13 stripped
    EXPECT_EQ(stripSymbol("I9#11",    11, false), "I9#11");  // #11 ≤ 11 keep
    EXPECT_EQ(stripSymbol("I13sus4",  11, false), "I11sus4");
}

TEST(ComparisonUtils_StripSymbol, Degree11PreserveTrue)
{
    EXPECT_EQ(stripSymbol("I13b13",   11, true), "I11b13");  // b13 above 11 preserved
}

// ── stripSymbol — degree 13 (no stripping except b5/#5) ─────────────────────

TEST(ComparisonUtils_StripSymbol, Degree13OnlyStripsB5SharpFive)
{
    EXPECT_EQ(stripSymbol("I13#11b9", 13, false), "I13#11b9");
    EXPECT_EQ(stripSymbol("I13b5",    13, false), "I13");    // b5 always dropped
    EXPECT_EQ(stripSymbol("I9#5",     13, false), "I9");     // #5 always dropped
    EXPECT_EQ(stripSymbol("I7b9#11b13", 13, true), "I7b9#11b13");
}

// ── stripSymbol — chord symbols (not Roman numerals) ────────────────────────

TEST(ComparisonUtils_StripSymbol, ChordSymbolSuffix)
{
    EXPECT_EQ(stripSymbol("C13b9#11", 7, false), "C7");
    EXPECT_EQ(stripSymbol("C13#11b9", 7, false), "C7");   // ordering variant
    EXPECT_EQ(stripSymbol("C9b5b13",  7, false), "C7");
    EXPECT_EQ(stripSymbol("C7b5b9",   7, false), "C7");
    EXPECT_EQ(stripSymbol("Cm7b9",    7, false), "Cm7");
    EXPECT_EQ(stripSymbol("CMaj7#11", 7, false), "CMaj7");
    EXPECT_EQ(stripSymbol("C13#5",    7, false), "C7");
    EXPECT_EQ(stripSymbol("C9+",      9, false), "C9+");  // '+' not a b5/#5 token
}

// ── classifyComparison ───────────────────────────────────────────────────────

TEST(ComparisonUtils_ClassifyComparison, DirectMatch)
{
    const auto r = classifyComparison("I7", "I7");
    EXPECT_EQ(r.kind, ComparisonResult::DirectMatch);
}

TEST(ComparisonUtils_ClassifyComparison, DirectMatchEmpty)
{
    const auto r = classifyComparison("", "");
    EXPECT_EQ(r.kind, ComparisonResult::DirectMatch);
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree7AltsDropped)
{
    // Cases that require alteration tokens to be dropped at degree 7.
    // b9/#9 only drop at deg 7 (not earlier); #11 with a 9th-level base also
    // needs deg 7 for the level reduction.
    auto check = [](const char* analyzer, const char* catalog) {
        const auto r = classifyComparison(analyzer, catalog);
        EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff) << analyzer;
        EXPECT_EQ(r.matchedAtDegree, 7) << analyzer;
        EXPECT_FALSE(r.matchedWithAlterationsPreserved) << analyzer;
    };

    check("I7b9",       "I7");   // b9 needs deg 7 false
    check("I7b9#11",    "I7");   // b9+#11 — b9 forces deg 7
    check("I7b5b9b13",  "I7");   // b5 always stripped; b9+b13 force deg 7
    check("I7b9#9",     "I7");   // b9+#9 at deg 7
    check("IM13#11",    "IM7");  // level 13→7 + #11 dropped
    check("I+13#11",    "I+7");  // level 13→7 + #11 dropped
    check("iø9#11",     "iø7");  // level 9→7 + #11 (need deg 7 for level)
    check("I11b9sus4",  "Isus4");// sus4 level + b9
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree7LevelOnly)
{
    // Pure level reduction or always-stripped tokens — flag-independent.
    // Protocol returns the first match in the inner loop: preserveAlts=true.
    auto check = [](const char* analyzer, const char* catalog) {
        const auto r = classifyComparison(analyzer, catalog);
        EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff) << analyzer;
        EXPECT_EQ(r.matchedAtDegree, 7) << analyzer;
        EXPECT_TRUE(r.matchedWithAlterationsPreserved) << analyzer;
    };

    check("IM9",       "IM7");
    check("I9",        "I7");
    check("I13",       "I7");
    check("I+9",       "I+7");
    check("i9",        "i7");
    check("iM9",       "iM7");
    check("I+M9",      "I+M7");
    check("I11sus4",   "Isus4");  // sus4 level stripped
    check("I13sus4",   "Isus4");
    check("I11b5sus4", "Isus4");  // b5 always stripped + sus4 level
    check("I(add9)",   "I");      // add-token stripped at deg 7
    check("i(add9)",   "i");
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree9AltsDropped)
{
    // #11 drops at deg 9 (11 > 9); no level change needed.
    auto check = [](const char* analyzer, const char* catalog) {
        const auto r = classifyComparison(analyzer, catalog);
        EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff) << analyzer;
        EXPECT_EQ(r.matchedAtDegree, 9) << analyzer;
        EXPECT_FALSE(r.matchedWithAlterationsPreserved) << analyzer;
    };

    check("iø7#11", "iø7"); // #11 dropped at deg 9 (no level change)
    check("IM7#11", "IM7"); // #11 dropped at deg 9
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree9LevelOnly)
{
    // add-token degree 11 > 9 — flag-independent; returns (9, true).
    auto check = [](const char* analyzer, const char* catalog) {
        const auto r = classifyComparison(analyzer, catalog);
        EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff) << analyzer;
        EXPECT_EQ(r.matchedAtDegree, 9) << analyzer;
        EXPECT_TRUE(r.matchedWithAlterationsPreserved) << analyzer;
    };

    check("I(add11)",  "I");   // add-degree 11 > 9 stripped
    check("I(add#11)", "I");
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree11AltsDropped)
{
    // b13 drops at deg 11 (13 > 11); no level change needed.
    auto check = [](const char* analyzer, const char* catalog) {
        const auto r = classifyComparison(analyzer, catalog);
        EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff) << analyzer;
        EXPECT_EQ(r.matchedAtDegree, 11) << analyzer;
        EXPECT_FALSE(r.matchedWithAlterationsPreserved) << analyzer;
    };

    check("i7b13",  "i7");   // b13 dropped at deg 11
    check("IM7b13", "IM7");
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree13AlwaysStripped)
{
    // b5/#5 are always stripped regardless of degree or flag.
    // First match in the loop: (13, true) — most conservative.
    auto check = [](const char* analyzer, const char* catalog) {
        const auto r = classifyComparison(analyzer, catalog);
        EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff) << analyzer;
        EXPECT_EQ(r.matchedAtDegree, 13) << analyzer;
        EXPECT_TRUE(r.matchedWithAlterationsPreserved) << analyzer;
    };

    check("I7b5",  "I7");
    check("IM7b5", "IM7");
    check("i7#5",  "i7");
    check("I13b5", "I13");
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree7AltsPreserved)
{
    // Catalog has base 7th + some alterations; analyzer has extra natural extensions
    // stripped but same alterations → matches at deg 7, alts=true.
    const auto r = classifyComparison("I13b9", "I7b9");
    EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff);
    EXPECT_EQ(r.matchedAtDegree, 7);
    EXPECT_TRUE(r.matchedWithAlterationsPreserved);
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree9)
{
    // Level reduction 13→9 is flag-independent; protocol returns (9, true).
    const auto r = classifyComparison("I13", "I9");
    EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff);
    EXPECT_EQ(r.matchedAtDegree, 9);
    EXPECT_TRUE(r.matchedWithAlterationsPreserved);
}

TEST(ComparisonUtils_ClassifyComparison, ConventionDiffAtDegree11)
{
    // Level reduction 13→11 is flag-independent; protocol returns (11, true).
    const auto r = classifyComparison("I13", "I11");
    EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff);
    EXPECT_EQ(r.matchedAtDegree, 11);
    EXPECT_TRUE(r.matchedWithAlterationsPreserved);
}

TEST(ComparisonUtils_ClassifyComparison, HighestMatchingDegreeSelected)
{
    // "I13b9#11" vs "I9b9": strips at deg 9 (false) → "I9b9" ✓
    // but also strips at deg 7 → "I7" ≠ "I9b9"
    // Should report deg 9 (least aggressive).
    const auto r = classifyComparison("I13b9#11", "I9b9");
    EXPECT_EQ(r.kind, ComparisonResult::ConventionDiff);
    EXPECT_EQ(r.matchedAtDegree, 9);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffDifferentRoot)
{
    // Different Roman degree — no stripping resolves this
    const auto r = classifyComparison("V7", "I7");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffDifferentQuality)
{
    const auto r = classifyComparison("I7", "i7");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffSus4VsTriad)
{
    // Isus4 cannot be reduced to I
    const auto r = classifyComparison("Isus4", "I");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffAlterationOrdering)
{
    // Symbol ordering difference — no degree of stripping resolves
    // (both sides have the same content but written in different order)
    const auto r = classifyComparison("C13#11b9", "C13b9#11");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffEmptyAnalyzerOutput)
{
    const auto r = classifyComparison("", "CTristan");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffAnalyzerSimplerThanCatalog)
{
    // Analyzer is LESS extended than catalog — stripping can't add extensions
    const auto r = classifyComparison("Cm7b5", "Cm9b5");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}

TEST(ComparisonUtils_ClassifyComparison, RealDiffViiHalfDimInversionWithSpurious11)
{
    // Pattern E: spurious #11 + inversion, after stripping #11 gives "viiø765"
    // not "viiø65" — real diff remains
    const auto r = classifyComparison("viiø7#1165", "viiø65");
    EXPECT_EQ(r.kind, ComparisonResult::RealDiff);
}
