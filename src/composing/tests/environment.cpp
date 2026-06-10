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

#include "testing/environment.h"

// ── Score-loading support (Stage 1c) ─────────────────────────────────────────
// The segmentation / harmonicsegmenter / keyresolver unit tests
// (regionanalysis_tests.cpp) drive code that consumes a real
// mu::engraving::Score, so the composing test binary must initialise the
// engraving + draw modules and register an EngravingConfiguration mock exactly
// the way engraving_tests does. This is a faithful copy of
// src/engraving/tests/environment.cpp; the pure-tone tests (chordanalyzer,
// gates, function layer, keymode) are unaffected by the extra module init.
#include "draw/drawmodule.h"
#include "engraving/engravingmodule.h"

#include "engraving/dom/instrtemplate.h"
#include "engraving/dom/mscore.h"

#include "engraving/tests/mocks/engravingconfigurationmock.h"
#include "engraving/tests/utils/scorerw.h"

#include "log.h"

static const mu::engraving::IEngravingConfiguration::DebuggingOptions debugOpt {};

static muse::testing::SuiteEnvironment composing_se(
{
    new muse::draw::DrawModule(),
    new mu::engraving::EngravingModule()
},
    nullptr,
    []() {
    LOGI() << "composing tests suite post init";

    mu::engraving::ScoreRW::setRootPath(muse::String::fromUtf8(composing_tests_DATA_ROOT));

    mu::engraving::MScore::testMode = true;
    mu::engraving::MScore::noGui = true;

    mu::engraving::loadInstrumentTemplates(":/engraving/instruments/instruments.xml");

    using ECMock = ::testing::NiceMock<mu::engraving::EngravingConfigurationMock>;

    std::shared_ptr<ECMock> configurator(new ECMock(), [](ECMock*) {}); // no delete
    ON_CALL(*configurator, defaultColor()).WillByDefault(::testing::Return(muse::draw::Color::BLACK));
    ON_CALL(*configurator, debuggingOptions()).WillByDefault(::testing::ReturnRef(debugOpt));
    ON_CALL(*configurator, allowReadingImagesFromOutsideMscz()).WillByDefault(::testing::Return(true));

    muse::modularity::globalIoc()->unregister<mu::engraving::IEngravingConfiguration>("utests");
    muse::modularity::globalIoc()->registerExport<mu::engraving::IEngravingConfiguration>("utests", configurator);
},
    []() {
    std::shared_ptr<mu::engraving::IEngravingConfiguration> mock
        = muse::modularity::globalIoc()->resolve<mu::engraving::IEngravingConfiguration>("utests");
    muse::modularity::globalIoc()->unregister<mu::engraving::IEngravingConfiguration>("utests");

    //! HACK (carried over from engraving tests): live pointers to the mock
    //! survive teardown, so delete it manually to silence the leak warning.
    mu::engraving::IEngravingConfiguration* ecptr = mock.get();
    delete ecptr;
}
    );
