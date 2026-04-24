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

// Mirror of src/notation/tests/environment.cpp — shared by the pipeline
// snapshot harness so ScoreRW + IoC are available to load DCML corpus
// scores and drive the notation/composing bridges.

#include "testing/environment.h"

#include "draw/drawmodule.h"
#include "engraving/engravingmodule.h"
#include "composing/composingmodule.h"

#include "engraving/dom/instrtemplate.h"
#include "engraving/dom/mscore.h"

#include "engraving/tests/mocks/engravingconfigurationmock.h"
#include "engraving/tests/utils/scorerw.h"

#include "log.h"

static const mu::engraving::IEngravingConfiguration::DebuggingOptions debugOpt {};

static muse::testing::SuiteEnvironment pipeline_snapshot_se(
{
    new muse::draw::DrawModule(),
    new mu::engraving::EngravingModule(),
    new mu::composing::ComposingModule()
},
nullptr,
[]() {
    LOGI() << "pipeline snapshot tests suite post init";

    mu::engraving::ScoreRW::setRootPath(muse::String::fromUtf8(pipeline_snapshot_tests_DATA_ROOT));

    mu::engraving::MScore::testMode = true;
    mu::engraving::MScore::noGui = true;

    mu::engraving::loadInstrumentTemplates(":/engraving/instruments/instruments.xml");

    using ECMock = ::testing::NiceMock<mu::engraving::EngravingConfigurationMock>;

    std::shared_ptr<ECMock> configurator(new ECMock(), [](ECMock*) {});
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

    mu::engraving::IEngravingConfiguration* ecptr = mock.get();
    delete ecptr;
});
