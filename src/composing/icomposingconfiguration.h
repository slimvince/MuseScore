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
#pragma once

#include "icomposinganalysisconfiguration.h"
#include "icomposingchordstaffconfiguration.h"

namespace mu::composing {

/// Full composing configuration: analysis + chord-staff output settings.
///
/// Code that only needs analysis settings should inject the narrower
/// IComposingAnalysisConfiguration interface rather than this one.
/// Code that needs chord-staff (implode) output settings should inject
/// IComposingChordStaffConfiguration.
///
/// IComposingConfiguration itself is NOT registered in the IoC container;
/// only the two sub-interfaces are.  ComposingConfiguration inherits from
/// both sub-interfaces and is registered under both.
class IComposingConfiguration
    : public IComposingAnalysisConfiguration
    , public IComposingChordStaffConfiguration
{
public:
    virtual ~IComposingConfiguration() = default;
};

} // namespace mu::composing
