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

#include <string>
#include "modularity/imoduleinterface.h"
#include "async/notification.h"

namespace mu::composing {

/// Settings used only by the chord-staff implode feature (populateChordTrack).
/// Not needed for the clean-branch chord-symbol annotation submission.
class IComposingChordStaffConfiguration : MODULE_GLOBAL_INTERFACE
{
    INTERFACE_ID(IComposingChordStaffConfiguration)

public:
    virtual ~IComposingChordStaffConfiguration() = default;

    /// Whether to write chord symbol annotations (HarmonyType::STANDARD) to the
    /// chord staff when imploding.
    virtual bool chordStaffWriteChordSymbols() const = 0;
    virtual void setChordStaffWriteChordSymbols(bool value) = 0;
    virtual muse::async::Notification chordStaffWriteChordSymbolsChanged() const = 0;

    /// Which chord-function notation to write below the treble staff when imploding.
    /// "none" — nothing; "roman" — Roman; "nashville" — Nashville.
    virtual std::string chordStaffFunctionNotation() const = 0;
    virtual void setChordStaffFunctionNotation(const std::string& value) = 0;
    virtual muse::async::Notification chordStaffFunctionNotationChanged() const = 0;

    /// Whether to write key/mode staff-text annotations at region boundaries.
    virtual bool chordStaffWriteKeyAnnotations() const = 0;
    virtual void setChordStaffWriteKeyAnnotations(bool value) = 0;
    virtual muse::async::Notification chordStaffWriteKeyAnnotationsChanged() const = 0;

    /// Whether to write the non-diatonic chord marker (★ + source key).
    virtual bool chordStaffHighlightNonDiatonic() const = 0;
    virtual void setChordStaffHighlightNonDiatonic(bool value) = 0;
    virtual muse::async::Notification chordStaffHighlightNonDiatonicChanged() const = 0;

    /// Whether to write cadence markers (PAC, PC, DC, HC).
    virtual bool chordStaffWriteCadenceMarkers() const = 0;
    virtual void setChordStaffWriteCadenceMarkers(bool value) = 0;
    virtual muse::async::Notification chordStaffWriteCadenceMarkersChanged() const = 0;
};

} // namespace mu::composing
