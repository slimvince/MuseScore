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

#include "jointtables.h"

#include <fstream>
#include <iterator>
#include <utility>
#include <vector>

#include "serialization/json.h"
#include "types/bytearray.h"

namespace mu::composing::analysis::joint {
namespace {
// Read a JSON file from disk (std::ifstream — no filesystem-injection dependency, so this
// loads identically in the NO_QT composing library and in both consumer binaries) and
// parse it with the muse JSON facility.
bool readRoot(const std::string& path, muse::JsonObject& out, std::string& err)
{
    std::ifstream f(path, std::ios::binary);
    if (!f) {
        err = "cannot open " + path;
        return false;
    }
    const std::string s((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
    std::string jerr;
    const muse::ByteArray ba(s.data(), s.size());
    const muse::JsonDocument doc = muse::JsonDocument::fromJson(ba, &jerr);
    if (!jerr.empty()) {
        err = "JSON parse error in " + path + ": " + jerr;
        return false;
    }
    if (!doc.isObject()) {
        err = "not a JSON object: " + path;
        return false;
    }
    out = doc.rootObject();
    return true;
}

// A flat distribution: every value is a number.
Dist parseDist(const muse::JsonObject& o)
{
    Dist d;
    const std::vector<std::string> ks = o.keys();
    d.reserve(ks.size());
    for (const std::string& k : ks) {
        d[k] = o.value(k).toDouble();
    }
    return d;
}

// A Katz-backed table: display-key -> {context_used, dist}, plus the derived
// context_used -> dist back-off map (setdefault first-wins, matching probe_decoder; every
// context_used maps to a unique dist in the committed tables, so first-wins is
// order-independent).
KatzTable parseKatz(const muse::JsonObject& tableObj)
{
    KatzTable t;
    for (const std::string& dk : tableObj.keys()) {
        const muse::JsonObject rowObj = tableObj.value(dk).toObject();
        KatzRow row;
        row.contextUsed = rowObj.value("context_used").toStdString();
        row.dist = parseDist(rowObj.value("dist").toObject());
        if (t.levels.find(row.contextUsed) == t.levels.end()) {
            t.levels.emplace(row.contextUsed, row.dist);
        }
        t.rows.emplace(dk, std::move(row));
    }
    return t;
}

// A boundary cell (fermata-crossed). `present` is true only when the cell exists AND
// carries a numeric probability — collapsing the two fall-back triggers Python's
// boundary_logp applies (an absent cell, and a cell whose prob is null); the decoder then
// uses the cell iff (present && reliable), exactly as the Python rule
// `cell.reliable and cell.prob is not None`.
BoundaryCell parseBoundaryCell(const muse::JsonObject& parent, const std::string& key)
{
    BoundaryCell c;
    if (!parent.contains(key)) {
        return c;
    }
    const muse::JsonObject o = parent.value(key).toObject();
    const muse::JsonValue pv = o.value("prob");
    if (!pv.isNumber()) {
        return c;
    }
    c.present = true;
    c.reliable = o.contains("reliable") && o.value("reliable").toBool();
    c.prob = pv.toDouble();
    return c;
}
} // namespace

JointTables JointTables::load(const std::string& artifactDir, const std::string& tableSet)
{
    JointTables jt;
    jt.tableSet = tableSet;
    const std::string suffix = tableSet;
    const std::string dir = artifactDir + "/";

    // ── tables_{suffix}.json ── table1..table5
    muse::JsonObject tables;
    if (!readRoot(dir + "tables_" + suffix + ".json", tables, jt.error)) {
        return jt;
    }
    jt.corpusGitHash = tables.value("provenance").toObject().value("corpus_git_hash").toStdString();

    const muse::JsonObject t1 = tables.value("table1_chord_transition").toObject();
    jt.t1Major = parseKatz(t1.value("major").toObject());
    jt.t1Minor = parseKatz(t1.value("minor").toObject());
    jt.t2 = parseDist(tables.value("table2_key_transition").toObject());
    jt.t3 = parseDist(tables.value("table3_entry_chord").toObject());
    jt.t4 = parseKatz(tables.value("table4_bass_inversion").toObject());

    const muse::JsonObject t5 = tables.value("table5_signature_prior").toObject();
    for (const std::string& dmode : t5.keys()) {
        jt.t5.emplace(dmode, parseDist(t5.value(dmode).toObject()));
    }

    // ── note_tables_{suffix}.json ── emission / spelling / boundary
    muse::JsonObject ntab;
    if (!readRoot(dir + "note_tables_" + suffix + ".json", ntab, jt.error)) {
        return jt;
    }
    jt.emission = parseKatz(ntab.value("emission_category_by_covariate").toObject());

    const muse::JsonObject spell = ntab.value("spelling_position_by_mode").toObject();
    for (const std::string& mode : spell.keys()) {
        jt.spelling.emplace(mode, parseDist(spell.value(mode).toObject().value("dist").toObject()));
    }

    const muse::JsonObject bnd = ntab.value("event_boundary_by_beat_class").toObject();
    for (const std::string& bc : bnd.keys()) {
        jt.boundaryProb[bc] = bnd.value(bc).toObject().value("prob").toDouble();
    }

    // ── factor_presence_{suffix}.json ── the missing-template-tone (absence) table
    muse::JsonObject fpres;
    if (!readRoot(dir + "factor_presence_" + suffix + ".json", fpres, jt.error)) {
        return jt;
    }
    const std::string primary = fpres.value("primary_mode").toStdString();
    const muse::JsonObject fpTable = fpres.value("factor_presence_table").toObject().value(primary).toObject();
    for (const std::string& cell : fpTable.keys()) {
        jt.factorAbsent[cell] = fpTable.value(cell).toObject().value("p_absent_smoothed").toDouble();
    }

    // ── fermata_boundary_addendum.json ── the boundary factor's fermata-crossed cells
    muse::JsonObject ferm;
    if (!readRoot(dir + "fermata_boundary_addendum.json", ferm, jt.error)) {
        return jt;
    }
    const muse::JsonObject byBc = ferm.value("fits").toObject().value(suffix).toObject()
                                  .value("exact_tick_by_beat_class").toObject();
    for (const std::string& bc : byBc.keys()) {
        const muse::JsonObject cell = byBc.value(bc).toObject();
        jt.fermBoundaryFerm.emplace(bc, parseBoundaryCell(cell, "fermata_at_or_adjacent"));
        jt.fermBoundaryNoFerm.emplace(bc, parseBoundaryCell(cell, "no_fermata_context"));
    }

    jt.error.clear();
    jt.loaded = true;
    return jt;
}
} // namespace mu::composing::analysis::joint
