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

#include "jointadapter.h"

#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iterator>
#include <set>

#include "serialization/json.h"
#include "types/bytearray.h"

namespace mu::composing::analysis::joint {
static const double kAlpha = 1.0;   // glt.ALPHA

double safeLog(double p)
{
    return (p > 0.0) ? std::log(p) : log0Floor();
}

namespace {
double distSum(const Dist& d)
{
    double s = 0.0;
    for (const auto& kv : d) {
        s += kv.second;
    }
    return s;
}

double distGet(const Dist& d, const std::string& k, double def = 0.0)
{
    const auto it = d.find(k);
    return it != d.end() ? it->second : def;
}

// _ROLE_TO_FIGURES (probe_decoder): the WiR inversion figures that place a chord factor-role in the
// bass, per family. Several figures can denote one role; the bass query sums whichever the row stored.
const std::vector<std::string>& roleFigures(const std::string& family, const std::string& role)
{
    static const std::vector<std::string> empty;
    static const std::unordered_map<std::string, std::vector<std::string> > triad = {
        { "root", { "" } }, { "third", { "6" } }, { "fifth", { "6/4" } }
    };
    static const std::unordered_map<std::string, std::vector<std::string> > seventh = {
        { "root", { "7" } }, { "third", { "6/5" } }, { "fifth", { "4/3" } }, { "seventh", { "2", "4/2" } }
    };
    const auto& m = (family == "seventh") ? seventh : triad;
    const auto it = m.find(role);
    return it != m.end() ? it->second : empty;
}
} // namespace

const std::string& FittedAdapter::modeName(bool isMajor)
{
    static const std::string maj = "major";
    static const std::string min = "minor";
    return isMajor ? maj : min;
}

const std::unordered_map<std::string, double>& FittedAdapter::modeMarginal(bool isMajor) const
{
    return isMajor ? m_margMajor : m_margMinor;
}

bool FittedAdapter::anyCadenceWeight() const
{
    for (const std::string& f : { "leading_tone", "tritone_pair", "dominant_tonic_bass", "fermata_location" }) {
        if (cadenceWeight(f) != 0.0) {
            return true;
        }
    }
    return false;
}

FittedAdapter FittedAdapter::load(const std::string& artifactDir, const std::string& tableSet,
                                  WeightVector weights, const std::string& leftoverMode)
{
    FittedAdapter a;
    a.m_weights = std::move(weights);
    a.m_leftoverMode = leftoverMode;
    a.m_tables = JointTables::load(artifactDir, tableSet);
    if (!a.m_tables.loaded) {
        a.m_error = a.m_tables.error;
        return a;
    }
    // mode_marginal.json
    const std::string path = artifactDir + "/mode_marginal.json";
    std::ifstream f(path, std::ios::binary);
    if (!f) {
        a.m_error = "cannot open " + path;
        return a;
    }
    const std::string s((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
    std::string jerr;
    const muse::ByteArray ba(s.data(), s.size());
    const muse::JsonObject root = muse::JsonDocument::fromJson(ba, &jerr).rootObject();
    if (!jerr.empty()) {
        a.m_error = "JSON parse error in " + path + ": " + jerr;
        return a;
    }
    for (const auto& modePair : { std::make_pair(std::string("major"), &a.m_margMajor),
                                  std::make_pair(std::string("minor"), &a.m_margMinor) }) {
        const muse::JsonObject o = root.value(modePair.first).toObject();
        for (const std::string& k : o.keys()) {
            (*modePair.second)[k] = o.value(k).toDouble();
        }
    }
    a.m_loaded = true;
    return a;
}

// ── the ratified below-threshold (Katz leftover) rule ──────────────────────────────────────

std::optional<std::string> FittedAdapter::firstBucket(const Dist& dist, Node start, ParentFn parentFn) const
{
    Node cur = std::move(start);
    std::set<std::string> seen;
    while (true) {
        const std::string ck = cur.keyStr();
        if (dist.find(ck) != dist.end()) {
            return ck;
        }
        if (seen.find(ck) != seen.end()) {
            return std::nullopt;
        }
        seen.insert(ck);
        const std::optional<std::string> par = parentFn(cur);
        if (!par.has_value()) {
            return std::nullopt;
        }
        cur = Node::ofStr(*par);
    }
}

std::pair<double, int> FittedAdapter::apportion(const Dist& dist, const std::string& bucket,
                                                ParentFn parentFn, bool isMajor) const
{
    const std::string key = std::to_string(reinterpret_cast<uintptr_t>(&dist)) + "\x1f" + bucket
                            + "\x1f" + modeName(isMajor);
    const auto cached = m_apportionCache.find(key);
    if (cached != m_apportionCache.end()) {
        return cached->second;
    }
    const std::unordered_map<std::string, double>& marg = modeMarginal(isMajor);
    double tot = 0.0;
    int cnt = 0;
    for (const auto& kv : marg) {
        if (firstBucket(dist, Node::ofClass(classFromKey(kv.first)), parentFn) == bucket) {
            tot += kv.second + kAlpha;
            ++cnt;
        }
    }
    const std::pair<double, int> v = { tot > 0.0 ? tot : kAlpha, cnt };
    m_apportionCache.emplace(key, v);
    return v;
}

std::optional<double> FittedAdapter::katzQuery(const Dist& dist, const Node& outcome, ParentFn parentFn,
                                               bool isMajor, bool isClass) const
{
    const std::string ck = outcome.keyStr();
    const auto direct = dist.find(ck);
    if (direct != dist.end()) {
        return direct->second;             // stored exact cell
    }
    const std::optional<std::string> bucket = firstBucket(dist, outcome, parentFn);
    if (!bucket.has_value()) {
        return std::nullopt;
    }
    const double mass = distGet(dist, *bucket, 0.0);
    if (mass <= 0.0) {
        return std::nullopt;
    }
    if (!isClass) {
        return mass;                       // the reserved mass for a terminal semantic cell
    }
    const std::pair<double, int> ap = apportion(dist, *bucket, parentFn, isMajor);
    if (m_leftoverMode == "even") {
        return mass / std::max(1, ap.second);
    }
    const std::unordered_map<std::string, double>& marg = modeMarginal(isMajor);
    const auto mIt = marg.find(ck);
    const double margCk = (mIt != marg.end()) ? mIt->second : 0.0;
    return ap.first > 0.0 ? (mass * (margCk + kAlpha) / ap.first) : mass;
}

const Dist* FittedAdapter::firstPresentDist(const std::vector<std::string>& chain,
                                            const std::unordered_map<std::string, Dist>& levels)
{
    for (const std::string& k : chain) {
        const auto it = levels.find(k);
        if (it != levels.end()) {
            return &it->second;
        }
    }
    return nullptr;                          // == levels.get(chain.back(), {}) with an empty dist
}

// ── factor 10: signature / declared-mode prior (initial state only) ─────────────────────────

double FittedAdapter::priorLogp(int tonic, bool isMajor, std::optional<int> sigFifths,
                                const std::string& declaredMode) const
{
    const std::string dmode = (declaredMode == "major" || declaredMode == "minor") ? declaredMode : "none";
    const auto t5it = m_tables.t5.find(dmode);
    static const Dist kFallback = { { "BASE", 1.0 } };
    const Dist* dist = (t5it != m_tables.t5.end()) ? &t5it->second
                       : (m_tables.t5.count("none") ? &m_tables.t5.at("none") : &kFallback);

    if (!sigFifths.has_value()) {
        return safeLog(distGet(*dist, "BASE", 1.0 / 24.0));
    }
    const int coll = collectionFifths(tonic, isMajor);
    const int diff = foldFifthsDiff(coll - *sigFifths);
    const std::string band = (std::abs(diff) <= 1) ? std::to_string(diff) : "far";
    const std::string lm = isMajor ? "M" : "m";
    const std::string cell = band + "|" + lm;
    if (dist->find(cell) != dist->end()) {
        return safeLog(dist->at(cell));
    }
    const std::string mcell = "mode:" + lm;
    if (dist->find(mcell) != dist->end()) {
        return safeLog(dist->at(mcell));
    }
    const double base = distGet(*dist, "BASE", 0.0);
    int concrete = 0;
    for (const auto& kv : *dist) {
        if (kv.first.find('|') != std::string::npos && !startsWith(kv.first, "mode:")
            && !startsWith(kv.first, "mp:")) {
            ++concrete;
        }
    }
    const int residual = std::max(1, 24 - concrete);
    return safeLog(base > 0.0 ? base / residual : 1e-6);
}

std::pair<double, double> FittedAdapter::priorTerms(int tonic, bool isMajor, std::optional<int> sigFifths,
                                                    const std::string& declaredMode) const
{
    const double sigOnly = priorLogp(tonic, isMajor, sigFifths, "");
    const double full = priorLogp(tonic, isMajor, sigFifths, declaredMode);
    return { sigOnly, full - sigOnly };
}

// ── factor 6: entry chord ───────────────────────────────────────────────────────────────────

double FittedAdapter::entryLogp(const LabelClass& cls, bool isMajor) const
{
    const std::optional<double> p = katzQuery(m_tables.t3, Node::ofClass(cls), &t3EntryParent, isMajor, true);
    return p.has_value() ? safeLog(*p) : log0Floor();
}

// ── factor 5: key transition ─────────────────────────────────────────────────────────────────

double FittedAdapter::keyTransLogp(int tonicPrev, bool majorPrev, int tonic, bool isMajor) const
{
    const Dist& t2 = m_tables.t2;
    if (tonicPrev == tonic && majorPrev == isMajor) {
        return safeLog(distGet(t2, "stay", 1e-6));
    }
    const std::string kind = keyChangeKind(tonicPrev, majorPrev, tonic, isMajor);
    std::string cell;
    if (kind == "parallel" || kind == "relative") {
        cell = kind;
    } else {
        const int dist = cofDistance(tonicPrev, tonic);
        const std::string mp = std::string(majorPrev ? "M" : "m") + (isMajor ? "M" : "m");
        const std::string band = (dist <= 2) ? ("cof" + std::to_string(dist)) : "cofFar";
        cell = band + "|" + mp;
    }
    if (t2.find(cell) != t2.end()) {
        return safeLog(t2.at(cell));
    }
    const size_t bar = cell.find('|');
    if (bar != std::string::npos) {
        const std::string mpCell = "mp:" + cell.substr(bar + 1);
        if (t2.find(mpCell) != t2.end()) {
            return safeLog(t2.at(mpCell));
        }
    }
    return safeLog(distGet(t2, "BASE", 1e-6));
}

// ── factor 4: same-key chord transition (with the applied-relation override) ─────────────────

double FittedAdapter::chordTransLogp(const LabelClass& prev, const LabelClass& cls, bool isMajor) const
{
    const KatzTable& t1 = isMajor ? m_tables.t1Major : m_tables.t1Minor;
    const std::string pk = prev.key();
    // `dist` MUST point at the table's OWN dist (the row's, or a shared level dist) — never a local
    // copy: the apportionment cache is keyed by the dist's address, matching Python's id(dist), so a
    // stable, shared object is required (a copied local address would alias across calls).
    const Dist* dist = nullptr;
    std::string contextUsed;
    static const Dist kEmpty;
    const auto rit = t1.rows.find(pk);
    if (rit != t1.rows.end()) {
        dist = &rit->second.dist;
        contextUsed = rit->second.contextUsed;
    } else {
        const std::vector<std::string> chain = t1CtxChain(prev);
        // _first_present returns a level KEY; the row's context_used is that chosen key.
        std::string chosen = chain.back();
        for (const std::string& k : chain) {
            if (t1.levels.find(k) != t1.levels.end()) {
                chosen = k;
                break;
            }
        }
        contextUsed = chosen;
        const auto lit = t1.levels.find(chosen);
        dist = (lit != t1.levels.end()) ? &lit->second : &kEmpty;
    }
    if (startsWith(contextUsed, kRel)) {
        const std::string relCell = relationCell(prev, cls);
        const std::optional<double> p = katzQuery(*dist, Node::ofStr(relCell), &appliedRelParent,
                                                  isMajor, /*isClass=*/false);
        return p.has_value() ? safeLog(*p) : log0Floor();
    }
    const std::optional<double> p = katzQuery(*dist, Node::ofClass(cls), &t1OutcomeParent,
                                              isMajor, /*isClass=*/true);
    return p.has_value() ? safeLog(*p) : log0Floor();
}

// ── factor 1: pitch emission ─────────────────────────────────────────────────────────────────

double FittedAdapter::emissionLogp(const std::string& category, const std::string& mc,
                                   const std::string& ap, const std::string& dp, bool tied) const
{
    const std::string dk = emitDisplay(mc, ap, dp, tied);
    const Dist* dist = nullptr;
    const auto rit = m_tables.emission.rows.find(dk);
    if (rit != m_tables.emission.rows.end()) {
        dist = &rit->second.dist;
    } else {
        dist = firstPresentDist(emitContextChain(mc, ap, dp, tied), m_tables.emission.levels);
    }
    static const Dist kEmpty;
    if (dist == nullptr) {
        dist = &kEmpty;
    }
    const auto it = dist->find(category);
    if (it == dist->end() || it->second <= 0.0) {
        return safeLog(!dist->empty() ? 1.0 / (distSum(*dist) + 3.0) : 1e-4);
    }
    return safeLog(it->second);
}

// ── factor 2: spelling emission ──────────────────────────────────────────────────────────────

double FittedAdapter::spellingLogp(const std::string& sbin, bool isMajor) const
{
    const auto sit = m_tables.spelling.find(modeName(isMajor));
    static const Dist kEmpty;
    const Dist& dist = (sit != m_tables.spelling.end()) ? sit->second : kEmpty;
    if (dist.find(sbin) != dist.end()) {
        return safeLog(dist.at(sbin));
    }
    std::optional<std::string> cur = sbin;
    std::set<std::string> seen;
    while (cur.has_value() && seen.find(*cur) == seen.end()) {
        const auto it = dist.find(*cur);
        if (it != dist.end()) {
            return safeLog(it->second);
        }
        seen.insert(*cur);
        cur = spellingParent(*cur);
    }
    return safeLog(distGet(dist, "BASE", 1e-4));
}

// ── factor 3: bass / inversion ───────────────────────────────────────────────────────────────

double FittedAdapter::bassLogp(const std::string* role, const std::string& family,
                               const std::string& degreeBase, const std::string& quality, bool isMajor) const
{
    if (role == nullptr) {
        return safeLog(0.02);              // a non-chord-factor bass — a floor
    }
    const std::string mode = isMajor ? "M" : "m";
    const std::string dk = degreeBase + "|" + quality + "|" + mode;
    const Dist* dist = nullptr;
    const auto rit = m_tables.t4.rows.find(dk);
    if (rit != m_tables.t4.rows.end()) {
        dist = &rit->second.dist;
    } else {
        dist = firstPresentDist(t4CtxChain(degreeBase, quality, mode), m_tables.t4.levels);
    }
    static const Dist kEmpty;
    if (dist == nullptr) {
        dist = &kEmpty;
    }
    double p = 0.0;
    for (const std::string& fig : roleFigures(family, *role)) {
        p += distGet(*dist, fig, 0.0);
    }
    if (p <= 0.0) {
        return safeLog(0.01);
    }
    return safeLog(p);
}

double FittedAdapter::factorAbsentLogp(const std::string& role, const std::string& family) const
{
    const std::string cell = role + "|" + family;
    const auto it = m_tables.factorAbsent.find(cell);
    if (it == m_tables.factorAbsent.end()) {
        return safeLog(0.05);
    }
    return safeLog(it->second);
}

// ── factor 7 (+8): boundary ──────────────────────────────────────────────────────────────────

double FittedAdapter::boundaryLogp(const std::string& beatClass, bool isBoundary, bool fermCtx) const
{
    const auto& fermMap = fermCtx ? m_tables.fermBoundaryFerm : m_tables.fermBoundaryNoFerm;
    const auto fit = fermMap.find(beatClass);
    bool haveP = false;
    double p = 0.0;
    if (fit != fermMap.end() && fit->second.present && fit->second.reliable) {
        p = fit->second.prob;
        haveP = true;
    }
    if (!haveP) {
        const auto bit = m_tables.boundaryProb.find(beatClass);
        if (bit != m_tables.boundaryProb.end()) {
            p = bit->second;
            haveP = true;
        }
    }
    if (!haveP) {
        return 0.0;
    }
    p = std::min(std::max(p, 1e-6), 1.0 - 1e-6);
    return std::log(isBoundary ? p : (1.0 - p));
}
} // namespace mu::composing::analysis::joint
