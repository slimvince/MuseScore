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

// ── Test-backfill (criteria 1-4): modepriorpresets (L3 key) ──────────────────
//
// modePriorPresets() was 0% covered (cc_tree_repair_and_coverage_report.md C1
// §C3). The DECIDABLE oracle here is the DOCUMENTED CONTRACT in modepriorpresets.h:
//   • exactly five built-in presets,
//   • returned in the display order Standard, Jazz, Modal, Baroque, Contemporary,
//   • "the 'Standard' preset matches the compile-time defaults in
//     KeyModeAnalyzerPreferences" — and, by construction, the ModePriorPreset
//     struct's own default member initializers.
// Those contract assertions are independent oracles. The individual per-mode
// magnitudes (e.g. Jazz dorian = 0.80) are EMPIRICALLY TUNED constants — a handful
// are pinned below only as explicitly-labelled REGRESSION GUARDS (change detectors),
// not correctness proofs, and only where they assert a documented design intent
// (Jazz embraces Dorian/Mixolydian; Baroque favours the harmonic-minor leading tone).

#include <gtest/gtest.h>

#include <vector>

#include "composing/analysis/key/modepriorpresets.h"

using mu::composing::ModePriorPreset;
using mu::composing::modePriorAppDefaults;
using mu::composing::modePriorPresets;

namespace {

// Compare every numeric prior of two presets (name excluded). Oracle helper for
// the "Standard == struct defaults" contract.
void expectSamePriors(const ModePriorPreset& a, const ModePriorPreset& b)
{
    EXPECT_DOUBLE_EQ(a.ionian, b.ionian);
    EXPECT_DOUBLE_EQ(a.dorian, b.dorian);
    EXPECT_DOUBLE_EQ(a.phrygian, b.phrygian);
    EXPECT_DOUBLE_EQ(a.lydian, b.lydian);
    EXPECT_DOUBLE_EQ(a.mixolydian, b.mixolydian);
    EXPECT_DOUBLE_EQ(a.aeolian, b.aeolian);
    EXPECT_DOUBLE_EQ(a.locrian, b.locrian);
    EXPECT_DOUBLE_EQ(a.melodicMinor, b.melodicMinor);
    EXPECT_DOUBLE_EQ(a.dorianB2, b.dorianB2);
    EXPECT_DOUBLE_EQ(a.lydianAugmented, b.lydianAugmented);
    EXPECT_DOUBLE_EQ(a.lydianDominant, b.lydianDominant);
    EXPECT_DOUBLE_EQ(a.mixolydianB6, b.mixolydianB6);
    EXPECT_DOUBLE_EQ(a.aeolianB5, b.aeolianB5);
    EXPECT_DOUBLE_EQ(a.altered, b.altered);
    EXPECT_DOUBLE_EQ(a.harmonicMinor, b.harmonicMinor);
    EXPECT_DOUBLE_EQ(a.locrianSharp6, b.locrianSharp6);
    EXPECT_DOUBLE_EQ(a.ionianSharp5, b.ionianSharp5);
    EXPECT_DOUBLE_EQ(a.dorianSharp4, b.dorianSharp4);
    EXPECT_DOUBLE_EQ(a.phrygianDominant, b.phrygianDominant);
    EXPECT_DOUBLE_EQ(a.lydianSharp2, b.lydianSharp2);
    EXPECT_DOUBLE_EQ(a.alteredDomBB7, b.alteredDomBB7);
}

bool samePriors(const ModePriorPreset& a, const ModePriorPreset& b)
{
    return a.ionian == b.ionian && a.dorian == b.dorian && a.phrygian == b.phrygian
        && a.lydian == b.lydian && a.mixolydian == b.mixolydian && a.aeolian == b.aeolian
        && a.locrian == b.locrian && a.melodicMinor == b.melodicMinor && a.dorianB2 == b.dorianB2
        && a.lydianAugmented == b.lydianAugmented && a.lydianDominant == b.lydianDominant
        && a.mixolydianB6 == b.mixolydianB6 && a.aeolianB5 == b.aeolianB5 && a.altered == b.altered
        && a.harmonicMinor == b.harmonicMinor && a.locrianSharp6 == b.locrianSharp6
        && a.ionianSharp5 == b.ionianSharp5 && a.dorianSharp4 == b.dorianSharp4
        && a.phrygianDominant == b.phrygianDominant && a.lydianSharp2 == b.lydianSharp2
        && a.alteredDomBB7 == b.alteredDomBB7;
}

} // namespace

// ── Contract: count + display order (criterion 1, 3 — oracle) ────────────────

TEST(Composing_ModePriorPresetsTests, ReturnsExactlyFivePresetsInDocumentedOrder)
{
    const std::vector<ModePriorPreset> presets = modePriorPresets();
    ASSERT_EQ(presets.size(), 5u);
    EXPECT_EQ(presets[0].name, "Standard");
    EXPECT_EQ(presets[1].name, "Jazz");
    EXPECT_EQ(presets[2].name, "Modal");
    EXPECT_EQ(presets[3].name, "Baroque");
    EXPECT_EQ(presets[4].name, "Contemporary");
}

// ── Contract: Standard == compile-time defaults (criterion 3 — oracle) ───────

TEST(Composing_ModePriorPresetsTests, StandardMatchesStructDefaultInitializers)
{
    // modepriorpresets.h documents: "The 'Standard' preset matches the compile-time
    // defaults in KeyModeAnalyzerPreferences." The ModePriorPreset struct carries
    // those same defaults as its member initializers, so a default-constructed
    // ModePriorPreset must equal the returned Standard preset field-for-field.
    const ModePriorPreset defaults;   // default member initializers
    expectSamePriors(modePriorPresets()[0], defaults);
}

// ── Contract: presets are distinct (criterion 1) ────────────────────────────

TEST(Composing_ModePriorPresetsTests, AllFivePresetsAreDistinct)
{
    const std::vector<ModePriorPreset> p = modePriorPresets();
    for (size_t i = 0; i < p.size(); ++i) {
        for (size_t j = i + 1; j < p.size(); ++j) {
            EXPECT_FALSE(samePriors(p[i], p[j]))
                << "presets " << p[i].name << " and " << p[j].name
                << " must differ in at least one prior";
        }
    }
}

// ── Contract: the app out-of-box defaults (criterion 3 — oracle) ─────────────

TEST(Composing_ModePriorPresetsTests, AppDefaultsAreNotOneOfTheNamedPresets)
{
    // modepriorpresets.h documents modePriorAppDefaults() as the app's registered
    // settings defaults — NOT a sixth tuning preset. The named-preset list is the
    // user-visible one and must stay at five; a caller asking for "Default" is served
    // by modePriorAppDefaults(), not by a lookup in modePriorPresets().
    const std::vector<ModePriorPreset> p = modePriorPresets();
    ASSERT_EQ(p.size(), 5u);
    for (const ModePriorPreset& preset : p) {
        EXPECT_NE(preset.name, "Default");
    }
    EXPECT_EQ(modePriorAppDefaults().name, "Default");
}

TEST(Composing_ModePriorPresetsTests, AppDefaultsDivergeFromStandardOnElevenModes)
{
    // The documented contract (modepriorpresets.h, and the applyPreset() comment in
    // tools/batch_analyze.cpp): the app's out-of-box priors are NOT the struct defaults,
    // i.e. NOT "Standard" — they diverge on 11 of the 21 modes, and agree on the other 10.
    // This is the reason "Default" cannot simply be served as the Standard preset, so it
    // is a genuine oracle rather than a pinned magnitude. Since the harness's "Default"
    // preset and ComposingConfiguration::init() now read this ONE table (OI-135), the
    // divergence is stated in exactly one place and checked here.
    const ModePriorPreset standard;          // == modePriorPresets()[0], by the test above
    const ModePriorPreset app = modePriorAppDefaults();

    // The 11 documented divergences.
    EXPECT_NE(app.lydian, standard.lydian);
    EXPECT_NE(app.mixolydian, standard.mixolydian);
    EXPECT_NE(app.locrian, standard.locrian);
    EXPECT_NE(app.lydianAugmented, standard.lydianAugmented);
    EXPECT_NE(app.lydianDominant, standard.lydianDominant);
    EXPECT_NE(app.mixolydianB6, standard.mixolydianB6);
    EXPECT_NE(app.aeolianB5, standard.aeolianB5);
    EXPECT_NE(app.locrianSharp6, standard.locrianSharp6);
    EXPECT_NE(app.ionianSharp5, standard.ionianSharp5);
    EXPECT_NE(app.dorianSharp4, standard.dorianSharp4);
    EXPECT_NE(app.lydianSharp2, standard.lydianSharp2);

    // The other 10 agree.
    EXPECT_DOUBLE_EQ(app.ionian, standard.ionian);
    EXPECT_DOUBLE_EQ(app.dorian, standard.dorian);
    EXPECT_DOUBLE_EQ(app.phrygian, standard.phrygian);
    EXPECT_DOUBLE_EQ(app.aeolian, standard.aeolian);
    EXPECT_DOUBLE_EQ(app.melodicMinor, standard.melodicMinor);
    EXPECT_DOUBLE_EQ(app.dorianB2, standard.dorianB2);
    EXPECT_DOUBLE_EQ(app.altered, standard.altered);
    EXPECT_DOUBLE_EQ(app.harmonicMinor, standard.harmonicMinor);
    EXPECT_DOUBLE_EQ(app.phrygianDominant, standard.phrygianDominant);
    EXPECT_DOUBLE_EQ(app.alteredDomBB7, standard.alteredDomBB7);
}

// ── Design intent (semi-oracle): Jazz embraces the modal colours ─────────────

TEST(Composing_ModePriorPresetsTests, JazzFavoursDorianAndMixolydianRelativeToStandard)
{
    // Documented design intent (modepriorpresets.cpp): the Jazz preset embraces the
    // modal sounds that classical Standard treats as rare. This is a behavioural
    // contract, not just a tuned magnitude: Jazz Dorian/Mixolydian are positive and
    // strictly above their (negative) Standard counterparts.
    const std::vector<ModePriorPreset> p = modePriorPresets();
    const ModePriorPreset& standard = p[0];
    const ModePriorPreset& jazz = p[1];
    EXPECT_GT(jazz.dorian, 0.0);
    EXPECT_GT(jazz.mixolydian, 0.0);
    EXPECT_GT(jazz.dorian, standard.dorian);
    EXPECT_GT(jazz.mixolydian, standard.mixolydian);
}

// ── Regression guards (labelled): tuned magnitudes are change-detectors only ─

TEST(Composing_ModePriorPresetsTests, RegressionGuard_DistinguishingTunedMagnitudes)
{
    // REGRESSION GUARD, not a correctness proof: these are empirically tuned
    // constants. Pinned so an accidental edit to the preset table is caught. Each
    // reflects a documented stylistic lean.
    const std::vector<ModePriorPreset> p = modePriorPresets();
    // Baroque favours the harmonic-minor leading tone (positive harmonicMinor),
    // unlike every other preset (which keeps it <= 0.2).
    EXPECT_DOUBLE_EQ(p[3].harmonicMinor, 0.50);   // Baroque
    EXPECT_LE(p[0].harmonicMinor, 0.0);           // Standard
    // Modal flattens the seven diatonic modes toward parity (all at +0.50).
    EXPECT_DOUBLE_EQ(p[2].dorian, 0.50);
    EXPECT_DOUBLE_EQ(p[2].phrygian, 0.50);
    EXPECT_DOUBLE_EQ(p[2].lydian, 0.50);
}
