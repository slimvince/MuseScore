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

#include "jointprimitives.h"

#include <algorithm>
#include <array>
#include <cctype>
#include <cstdlib>
#include <unordered_map>

#include "composing/analysis/chord/analysisutils.h"   // normalizePc (the sanctioned pitch leaf)

namespace mu::composing::analysis::joint {
using mu::composing::analysis::normalizePc;

// The pooling sigils. Guillemets as « / » (« / ») — under the /utf-8 build the literal
// bytes are UTF-8, identical to the committed table keys and the Python string constants.
const std::string kBase = "BASE";
const std::string kPoolInvfree = "«invfree» ";     // «invfree» + trailing space
const std::string kPoolFamily = "«family» ";       // «family» + trailing space
const std::string kRel = "«rel»";                  // «rel»
const std::string kRelResolve = "«rel»resolve";
const std::string kRelElsewhere = "«rel»elsewhere";

namespace {
// gen_note_tables._DEG
int degreeNum(const std::string& roman)
{
    static const std::unordered_map<std::string, int> deg = {
        { "I", 1 }, { "II", 2 }, { "III", 3 }, { "IV", 4 }, { "V", 5 }, { "VI", 6 }, { "VII", 7 }
    };
    const auto it = deg.find(roman);
    return it != deg.end() ? it->second : -1;
}

// gen_note_tables._MAJ_SCALE / _MIN_SCALE
const std::array<int, 7> kMajScale = { 0, 2, 4, 5, 7, 9, 11 };
const std::array<int, 7> kMinScale = { 0, 2, 3, 5, 7, 8, 10 };

// gen_note_tables._QUAL_TEMPLATE (AugSixth/Neapolitan are NOT here — special content).
const std::unordered_map<std::string, std::vector<int> >& qualTemplates()
{
    static const std::unordered_map<std::string, std::vector<int> > t = {
        { "Maj", { 0, 4, 7 } }, { "Min", { 0, 3, 7 } }, { "Dim", { 0, 3, 6 } }, { "Aug", { 0, 4, 8 } },
        { "Dom7", { 0, 4, 7, 10 } }, { "Maj7", { 0, 4, 7, 11 } }, { "Min7", { 0, 3, 7, 10 } },
        { "MinMaj7", { 0, 3, 7, 11 } }, { "Dim7", { 0, 3, 6, 9 } }, { "HalfDim7", { 0, 3, 6, 10 } },
        { "HalfDim", { 0, 3, 6 } }, { "Aug7", { 0, 4, 8, 10 } }, { "AugMaj7", { 0, 4, 8, 11 } }
    };
    return t;
}

bool isDimQuality(const std::string& q)
{
    return q == "Dim" || q == "Dim7" || q == "HalfDim7" || q == "HalfDim";
}

PcMask maskOf(std::initializer_list<int> pcs)
{
    PcMask m = 0;
    for (int pc : pcs) {
        m |= static_cast<PcMask>(1u << normalizePc(pc));
    }
    return m;
}

// gen_note_tables._MAJ_COLLECTION / _MIN_COLLECTION (tonic-RELATIVE offsets).
PcMask majRelColl() { static const PcMask m = maskOf({ 0, 2, 4, 5, 7, 9, 11 }); return m; }
PcMask minRelColl() { static const PcMask m = maskOf({ 0, 2, 3, 5, 7, 8, 10, 9, 11 }); return m; }

int pythonMod(int a, int m) { int r = a % m; return r < 0 ? r + m : r; }

// gen_note_tables._split_degree
void splitDegree(const std::string& base, int& num, int& acc)
{
    acc = 0;
    size_t i = 0;
    for (; i < base.size(); ++i) {
        if (base[i] == 'b') {
            --acc;
        } else if (base[i] == '#') {
            ++acc;
        } else {
            break;
        }
    }
    num = degreeNum(base.substr(i));   // leading accidentals stripped (base.lstrip("b#"))
}

// gen_note_tables._chord_root; returns -1 for an unmappable degree (Python None).
int chordRoot(const std::string& base, const std::string& quality, int tonic, bool isMajor)
{
    int num, acc;
    splitDegree(base, num, acc);
    if (num < 0) {
        return -1;
    }
    int semi = (isMajor ? kMajScale : kMinScale)[num - 1] + acc;
    if (!isMajor && acc == 0 && isDimQuality(quality)) {
        if (num == 7) {
            semi = 11;
        } else if (num == 6) {
            semi = 9;
        }
    }
    return normalizePc(tonic + semi);
}

std::vector<std::string> splitByPipe(const std::string& s)
{
    // Split on " | " (the LabelClass.key() separator).
    static const std::string sep = " | ";
    std::vector<std::string> out;
    size_t pos = 0;
    while (true) {
        const size_t next = s.find(sep, pos);
        if (next == std::string::npos) {
            out.push_back(s.substr(pos));
            break;
        }
        out.push_back(s.substr(pos, next - pos));
        pos = next + sep.size();
    }
    return out;
}

// gen_label_tables._family_key_of
std::string familyKeyOf(const std::string& invfreeKey)
{
    const std::vector<std::string> parts = splitByPipe(invfreeKey);
    const std::string deg = parts.size() > 0 ? parts[0] : "";
    const std::string qual = parts.size() > 1 ? parts[1] : "";
    const std::string tgt = parts.size() > 3 ? parts[3] : "";
    const std::string fam = isSeventhQuality(qual) ? "seventh" : "triad";
    return deg + " | " + fam + " |  | " + tgt;
}

} // namespace

bool startsWith(const std::string& s, const std::string& prefix)
{
    return s.size() >= prefix.size() && s.compare(0, prefix.size(), prefix) == 0;
}

int pcToFifths(int pc)
{
    static const std::array<int, 12> f = { 0, -5, 2, -3, 4, -1, 6, 1, -4, 3, -2, 5 };
    return f[normalizePc(pc)];
}

Framework frameworkAndRoot(const LabelClass& cls, int tonic, bool isMajor)
{
    Framework f;
    if (cls.rawUnnormalized()) {
        return f;
    }
    const std::string& q = cls.quality();
    int fwTonic = tonic;
    bool fwMajor = isMajor;
    const std::string& target = cls.target();
    if (!target.empty()) {
        if (target.find('/') != std::string::npos) {
            return f;                       // multi-level applied — unmappable
        }
        // tbase = target.lstrip("b#"); tnum = _DEG[tbase.upper()]
        size_t i = 0;
        while (i < target.size() && (target[i] == 'b' || target[i] == '#')) {
            ++i;
        }
        std::string tbase = target.substr(i);
        std::string tbaseUpper = tbase;
        for (char& c : tbaseUpper) {
            c = static_cast<char>(std::toupper(static_cast<unsigned char>(c)));
        }
        const int tnum = degreeNum(tbaseUpper);
        if (tnum < 0) {
            return f;
        }
        int tacc = 0;                       // sum over ALL '#'/'b' in the target
        for (char c : target) {
            if (c == '#') {
                ++tacc;
            } else if (c == 'b') {
                --tacc;
            }
        }
        fwTonic = normalizePc(tonic + (isMajor ? kMajScale : kMinScale)[tnum - 1] + tacc);
        fwMajor = !tbase.empty() && std::isupper(static_cast<unsigned char>(tbase[0]));
    }
    if (q == "AugSixth" || q == "Neapolitan") {
        f.valid = true;
        f.fwTonic = fwTonic;
        f.fwMajor = fwMajor;
        f.hasRoot = false;
        return f;
    }
    if (qualTemplates().find(q) == qualTemplates().end()) {
        return f;
    }
    const int root = chordRoot(cls.degreeBase(), q, fwTonic, fwMajor);
    if (root < 0) {
        return f;
    }
    f.valid = true;
    f.fwTonic = fwTonic;
    f.fwMajor = fwMajor;
    f.hasRoot = true;
    f.root = root;
    return f;
}

std::optional<PcMask> memberPcs(const LabelClass& cls, int tonic, bool isMajor)
{
    const Framework f = frameworkAndRoot(cls, tonic, isMajor);
    if (!f.valid) {
        return std::nullopt;
    }
    const std::string& q = cls.quality();
    if (q == "AugSixth") {
        return maskOf({ f.fwTonic + 8, f.fwTonic + 0, f.fwTonic + 6 });
    }
    if (q == "Neapolitan") {
        return maskOf({ f.fwTonic + 1, f.fwTonic + 5, f.fwTonic + 8 });
    }
    PcMask m = 0;
    for (int iv : qualTemplates().at(q)) {
        m |= static_cast<PcMask>(1u << normalizePc(f.root + iv));
    }
    const std::string& inv = cls.inversion();
    if (!inv.empty() && inv[0] == '9') {
        const int ninth = (inv.find("b9") != std::string::npos) ? 1 : 2;
        m |= static_cast<PcMask>(1u << normalizePc(f.root + ninth));
    }
    return m;
}

std::optional<std::vector<ChordFactor> > chordFactorPcs(const LabelClass& cls, int tonic, bool isMajor)
{
    const Framework f = frameworkAndRoot(cls, tonic, isMajor);
    if (!f.valid || !f.hasRoot) {
        return std::nullopt;
    }
    static const std::array<const char*, 4> roles = { "root", "third", "fifth", "seventh" };
    const std::vector<int>& tmpl = qualTemplates().at(cls.quality());
    std::vector<ChordFactor> out;
    out.reserve(tmpl.size());
    for (size_t i = 0; i < tmpl.size(); ++i) {
        out.push_back({ roles[i], normalizePc(f.root + tmpl[i]) });
    }
    return out;
}

std::string noteCategory(int pc, PcMask mem, int tonic, bool isMajor)
{
    if ((mem >> normalizePc(pc)) & 1u) {
        return "member";
    }
    const PcMask coll = isMajor ? majRelColl() : minRelColl();
    return ((coll >> normalizePc(pc - tonic)) & 1u) ? "within" : "outside";
}

PcMask keyCollectionMask(int tonic, bool isMajor)
{
    const std::array<int, 7>& scale = isMajor ? kMajScale : kMinScale;
    PcMask m = 0;
    if (isMajor) {
        for (int s : scale) {
            m |= static_cast<PcMask>(1u << normalizePc(tonic + s));
        }
    } else {
        // _MIN_COLLECTION = natural minor + raised 6th (+9) and raised 7th (+11)
        for (int s : kMinScale) {
            m |= static_cast<PcMask>(1u << normalizePc(tonic + s));
        }
        m |= static_cast<PcMask>(1u << normalizePc(tonic + 9));
        m |= static_cast<PcMask>(1u << normalizePc(tonic + 11));
    }
    return m;
}

std::string spellingBin(int rel, bool isMajor)
{
    if (isMajor) {
        if (rel >= -1 && rel <= 5) {
            return "dia:" + std::to_string(rel);
        }
        return rel < -1 ? "chr_flat" : "chr_sharp";
    }
    if (rel >= -4 && rel <= 2) {
        return "dia:" + std::to_string(rel);
    }
    if (rel == 3) {
        return "raised6";
    }
    if (rel == 5) {
        return "raised7";
    }
    return rel < -4 ? "chr_flat" : "chr_sharp";
}

std::optional<std::string> spellingParent(const std::string& cell)
{
    if (cell == "BASE") {
        return std::nullopt;
    }
    if (startsWith(cell, "CLASS:")) {
        return std::string("BASE");
    }
    if (startsWith(cell, "dia:")) {
        return std::string("CLASS:diatonic");
    }
    // _SPELL_CLASS: raised6/raised7 -> raised; chr_flat/chr_sharp -> chromatic; else chromatic
    if (cell == "raised6" || cell == "raised7") {
        return std::string("CLASS:raised");
    }
    return std::string("CLASS:chromatic");
}

std::string emitDisplay(const std::string& mc, const std::string& ap, const std::string& dp, bool tied)
{
    return mc + " | " + ap + " | " + dp + " | " + (tied ? "1" : "0");
}

std::vector<std::string> emitContextChain(const std::string& mc, const std::string& ap,
                                           const std::string& dp, bool tied)
{
    const bool cs = (ap == "step") || (dp == "step") || (mc == "sub_tactus") || tied;
    return { "L0:" + mc + "|" + ap + "|" + dp + "|" + (tied ? "1" : "0"),
             "L1:" + ap + "|" + dp,
             std::string("L2:") + (cs ? "1" : "0"),
             "BASE" };
}

int collectionFifths(int tonic, bool isMajor)
{
    const int base = isMajor ? tonic : normalizePc(tonic + 3);
    return pcToFifths(base);
}

int foldFifthsDiff(int d)
{
    d = pythonMod(d, 12);
    return d > 6 ? d - 12 : d;
}

int cofDistance(int a, int b)
{
    const int ca = pythonMod(a * 7, 12);
    const int cb = pythonMod(b * 7, 12);
    const int d = std::abs(ca - cb);
    return std::min(d, 12 - d);
}

std::string keyChangeKind(int ta, bool ma, int tb, bool mb)
{
    if (ta == tb && ma != mb) {
        return "parallel";
    }
    if (ma && !mb && tb == normalizePc(ta + 9)) {
        return "relative";
    }
    if (!ma && mb && tb == normalizePc(ta + 3)) {
        return "relative";
    }
    return "other";
}

std::vector<std::string> t1CtxChain(const LabelClass& fromCls)
{
    return { "L0:" + fromCls.key(),
             "L1:" + fromCls.inversionFree().key(),
             "L2:" + fromCls.family().key(),
             kBase };
}

std::vector<std::string> t4CtxChain(const std::string& deg, const std::string& qual, const std::string& mode)
{
    return { "L0:" + deg + "|" + qual + "|" + mode,
             "L1:*|" + qual + "|" + mode,
             "L2:*|*|" + mode };
}

std::optional<std::string> t1OutcomeParent(const Node& node)
{
    if (node.isClass) {
        const LabelClass& to = node.cls;
        if (!to.inversion().empty()) {
            return kPoolInvfree + to.inversionFree().key();
        }
        if (to.quality() != "triad" && to.quality() != "seventh") {
            return kPoolFamily + to.family().key();
        }
        return kBase;
    }
    const std::string& s = node.str;
    if (startsWith(s, kPoolInvfree)) {
        return kPoolFamily + familyKeyOf(s.substr(kPoolInvfree.size()));
    }
    if (startsWith(s, kPoolFamily)) {
        return kBase;
    }
    return kBase;                          // BASE (terminal: parent == self, caught by the seen set)
}

std::optional<std::string> t3EntryParent(const Node& node)
{
    if (node.isClass) {
        const LabelClass& cls = node.cls;
        if (!cls.inversion().empty()) {
            return kPoolInvfree + cls.inversionFree().key();
        }
        return kBase;
    }
    if (startsWith(node.str, kPoolInvfree)) {
        return kBase;
    }
    return kBase;
}

std::optional<std::string> appliedRelParent(const Node& node)
{
    const std::string s = node.keyStr();
    if (s == kRelElsewhere || s == kRelResolve) {
        return std::nullopt;
    }
    const std::string prefix = kRelResolve + "|";
    if (startsWith(s, prefix)) {
        const std::string body = s.substr(prefix.size());
        const size_t bar = body.find('|');
        if (bar != std::string::npos) {
            return kRelResolve + "|" + body.substr(0, bar);
        }
        return kRelResolve;
    }
    return std::nullopt;
}

std::string relationCell(const LabelClass& a, const LabelClass& b)
{
    // _target_head_rest(a.target)
    std::string head = a.target();
    std::string rest;
    const size_t slash = head.find('/');
    if (slash != std::string::npos) {
        rest = head.substr(slash + 1);
        head = head.substr(0, slash);
    }
    auto upper = [](std::string x) {
        for (char& c : x) {
            c = static_cast<char>(std::toupper(static_cast<unsigned char>(c)));
        }
        return x;
    };
    const bool resolves = (upper(b.degreeBase()) == upper(head)) && (b.target() == rest);
    if (!resolves) {
        return kRelElsewhere;
    }
    const std::string qf = isSeventhQuality(b.quality()) ? "seventh" : "triad";
    const std::string pos = b.inversion().empty() ? "root" : "inv";
    return kRelResolve + "|" + qf + "|" + pos;
}
} // namespace mu::composing::analysis::joint
