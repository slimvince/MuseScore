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

#include "jointfactadapter.h"

#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <tuple>
#include <unordered_map>
#include <utility>

// L1 published fact surface — the ONLY note-fact source (OI-180: no module-private raw-note walk).
#include "composing/analysis/notemodel/note_model.h"

// The score's STRUCTURAL facts (measure layout, initial key signature/mode, meter). No note read.
#include "engraving/dom/measure.h"
#include "engraving/dom/part.h"
#include "engraving/dom/score.h"
#include "engraving/dom/staff.h"
#include "engraving/types/fraction.h"
#include "engraving/dom/pitchspelling.h"     // Tpc::TPC_C (line-of-fifths origin)
#include "engraving/types/types.h"           // Key, KeyMode

namespace mu::composing::analysis::joint {

namespace {
using namespace mu::engraving;
namespace nm = mu::composing::analysis::notemodel;

// The pinned corpus tick convention (music21_batch.py / note_events.json ticks_per_quarter; the ★R1
// four-beat window and the whole module assume it — load_pieces STOPs if note_events disagrees).
constexpr int kTicksPerQuarter = 480;

// metric-class codes (gen_note_events._MC): downbeat / mid_strong / other_tactus / sub_tactus.
enum { MC_DOWNBEAT = 0, MC_MID_STRONG = 1, MC_OTHER_TACTUS = 2, MC_SUB_TACTUS = 3 };
// melodic codes (gen_note_events._MV): none / step / leap.
enum { MV_NONE = 0, MV_STEP = 1, MV_LEAP = 2 };

double round4(double x)
{
    return std::round(x * 10000.0) / 10000.0;   // == Python round(x, 4)
}

// gen_label_tables._beat_class over a (round-4'd) 1-indexed quarter-beat. When n_quarter is falsy
// (no meter) gen_note_events forces sub_tactus.
int beatClass(double pos, int nQuarter)
{
    if (nQuarter <= 0) {
        return MC_SUB_TACTUS;
    }
    if (pos != std::trunc(pos)) {          // Python: pos != int(pos)
        return MC_SUB_TACTUS;
    }
    const int ib = static_cast<int>(pos);
    if (ib == 1) {
        return MC_DOWNBEAT;
    }
    if (ib == 3 && nQuarter == 4) {
        return MC_MID_STRONG;
    }
    return MC_OTHER_TACTUS;
}

// ── the METRICAL GRID (music21's measure/beat model) ─────────────────────────────────────────────
// music21's .measureNumber and .beat follow the TIME-SIGNATURE metrical grid — downbeats every
// nominal-measure length, offset by the anacrusis — NOT MuseScore's Measure objects. MuseScore creates
// an extra Measure at each chorale PHRASE-SPLIT barline (a partial measure ending a phrase mid-bar),
// which music21 folds back into the metrical measure. So a MuseScore-measure walk (numbering, boundary)
// diverges from music21 from the first phrase-split on. We reconstruct the metrical grid instead:
//   * anacrusis A = the leading pickup's actual length (firstMeasure->ticks() when it is < nominal);
//     the pickup is metrical measure 0 spanning [0, A); measure k>=1 downbeats at A + (k-1)*L.
//   * a note's music21 .beat is (tick - downbeat)/quarter + 1, PADDED for the pickup (paddingLeft =
//     nominal - A) so a pickup note lands on its would-be full-measure beat.
//   * the event lattice's beat (_tick_to_measure_beat) is the SAME grid but UNPADDED.
// The note .beat uses the time-signature BEAT UNIT (half-note for X/2, dotted-quarter for compound X/8),
// not the quarter. The measure NUMBER: a leading pickup is metrical measure 0 (excluded from the decode)
// and real measures are 1,2,3,... — matching music21 for the common convention (the xml numbers the
// pickup 0). Two number-only divergence classes are NOT mechanically recoverable from MuseScore (which
// does not preserve the xml <measure number>): editorial pickup-numbered-1 (bwv113.8) and repeat/reset
// or misnumbered xml numbers (bwv324 repeats numbers 1..9; bwv261 misnumbers). Both are cosmetic EXCEPT
// the pickup-numbered-1 ==0 case (reported).
struct GridMeas { int downbeat; int number; int beatDur; };

struct Grid {
    std::vector<GridMeas> meas;   // downbeats in ascending order (metrical measures)
    int anacrusis = 0;            // A: pickup length (0 if no pickup)
    bool hasPickup = false;
    int pickupNominal = 0;        // the pickup measure's nominal length (for the paddingLeft)
};

// music21 beatDuration in ticks: compound meters (denominator 8, numerator a multiple of 3 > 3) beat in
// dotted-quarter units (720t); simple meters beat in the denominator note value ((4/den)*480t).
int beatDurTicks(int numerator, int denominator)
{
    if (denominator <= 0) {
        return kTicksPerQuarter;
    }
    if (denominator == 8 && numerator > 3 && numerator % 3 == 0) {
        return 3 * (4 * kTicksPerQuarter / 8);   // dotted quarter = 720
    }
    return 4 * kTicksPerQuarter / denominator;   // 4/4->480, 3/2->960, 3/8->240
}

// Build the metrical grid: downbeats every nominal-measure length, offset by the anacrusis (music21's
// time-signature grid, which its native .beat follows and which folds chorale phrase-split half-measures
// back into one metrical measure). Meter changes (the multi-meter stems) shift the nominal length + beat
// unit per segment. The pickup is metrical measure 0. Pieces whose xml measure structure is pathological
// (misnumbered/repeat-reset numbers, irregular non-split measures) drift — the reported note-mc class.
Grid buildGrid(const Score* sc)
{
    Grid g;
    const Measure* first = sc->firstMeasure();
    if (!first) {
        g.meas.push_back({ 0, 1, kTicksPerQuarter });
        return g;
    }
    // meter segments: (startTick, nominalLen, beatDur), recorded at each meter change
    struct Seg { int start; int nominal; int beatDur; };
    std::vector<Seg> segs;
    for (const Measure* m = first; m; m = m->nextMeasure()) {
        const Fraction ts = m->timesig();
        const int nl = ts.ticks();
        if (nl <= 0) {
            continue;
        }
        const int bd = beatDurTicks(ts.numerator(), ts.denominator());
        if (segs.empty() || segs.back().nominal != nl || segs.back().beatDur != bd) {
            segs.push_back({ m->tick().ticks(), nl, bd });
        }
    }
    const auto lenAt = [&](int pos) {
        int v = 0;
        for (const Seg& s : segs) { if (s.start <= pos) { v = s.nominal; } else { break; } }
        return v;
    };
    const auto beatDurAtPos = [&](int pos) {
        int v = 0;
        for (const Seg& s : segs) { if (s.start <= pos) { v = s.beatDur; } else { break; } }
        return v > 0 ? v : kTicksPerQuarter;
    };
    const int scoreEnd = sc->endTick().ticks();
    const int firstNominal = first->timesig().ticks();
    const int firstActual = first->ticks().ticks();
    if (firstNominal > 0 && firstActual > 0 && firstActual < firstNominal) {
        g.hasPickup = true;
        g.anacrusis = firstActual;
        g.pickupNominal = firstNominal;
    }
    int number = 1;
    int pos = 0;
    if (g.hasPickup) {
        g.meas.push_back({ 0, 0, beatDurAtPos(0) });   // pickup = metrical measure 0
        pos = g.anacrusis;
    }
    for (int guard = 0; pos < scoreEnd && guard < 1000000; ++guard) {
        const int L = lenAt(pos);
        if (L <= 0) {
            break;
        }
        g.meas.push_back({ pos, number, beatDurAtPos(pos) });
        pos += L;
        ++number;
    }
    if (g.meas.empty()) {
        g.meas.push_back({ 0, 1, kTicksPerQuarter });
    }
    return g;
}

int gridIndexOf(const Grid& g, int tick)
{
    int lo = 0, hi = static_cast<int>(g.meas.size());
    while (lo < hi) {                          // first downbeat > tick
        const int mid = (lo + hi) / 2;
        if (g.meas[mid].downbeat <= tick) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return std::max(0, lo - 1);
}

int measureNumberOf(const Grid& g, int tick)
{
    return g.meas.empty() ? 0 : g.meas[gridIndexOf(g, tick)].number;
}

// music21 native .beat of a note at `onset`: metrical-grid position in the time-signature BEAT UNIT,
// PADDED for the leading pickup (paddingLeft = the pickup's nominal - actual, in ticks).
double notePaddedBeat(const Grid& g, int onset)
{
    if (g.meas.empty()) {
        return 1.0;
    }
    const int i = gridIndexOf(g, onset);
    const int bd = (g.meas[i].beatDur > 0) ? g.meas[i].beatDur : kTicksPerQuarter;
    double offset = static_cast<double>(onset - g.meas[i].downbeat);
    if (i == 0 && g.hasPickup) {
        offset += static_cast<double>(g.pickupNominal - g.anacrusis);
    }
    return round4(offset / bd + 1.0);
}

// ── the EVENT lattice's measure/beat (music21 gen_note_events._tick_to_measure_beat over _measure_map) ──
// gen_note_events computes the EVENT measure/beat NOT from native .beat but from
// _measure_map(score.parts[0]) = {measure.number: start_tick}. For a suffix-split pair "N"/"Na"
// music21's .number returns the SAME base int N for both, so the dict OVERWRITES and keeps the LATER
// ("Na") start — a real music21-extraction quirk (the event grid then differs from the note grid on
// split-measure pieces: 209/326 stems). We reproduce it EXACTLY: each MuseScore measure's music21 base
// number IS its start's metrical-grid measure number (a suffix continuation shares the grid measure of
// its partner), so {base_number -> last MuseScore-measure start} == music21's _measure_map. The beat is
// then (tick - the-last-start-<=-tick) / quarter + 1, and the measure is that entry's base number.
struct EventMeasMap {
    std::vector<std::pair<int, int> > byStart;   // (start_tick, base_number), ascending by start
};

EventMeasMap buildEventMeasMap(const Score* sc, const Grid& g)
{
    std::map<int, int> numToStart;               // base_number -> LAST measure start (dict overwrite)
    for (const Measure* m = sc->firstMeasure(); m; m = m->nextMeasure()) {
        const int st = m->tick().ticks();
        numToStart[measureNumberOf(g, st)] = st;
    }
    EventMeasMap em;
    em.byStart.reserve(numToStart.size());
    for (const auto& kv : numToStart) {
        em.byStart.push_back({ kv.second, kv.first });
    }
    std::sort(em.byStart.begin(), em.byStart.end());   // by start_tick (music21 sorts m1_map by value)
    return em;
}

// _tick_to_measure_beat: the LAST map entry whose start <= tick gives (measure number, beat).
std::pair<int, double> eventMeasureBeat(const EventMeasMap& em, int tick)
{
    if (em.byStart.empty()) {
        return { 0, 1.0 };
    }
    int lo = 0, hi = static_cast<int>(em.byStart.size());
    while (lo < hi) {                            // first entry with start > tick
        const int mid = (lo + hi) / 2;
        if (em.byStart[mid].first <= tick) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    const int i = std::max(0, lo - 1);
    return { em.byStart[i].second,
             round4(static_cast<double>(tick - em.byStart[i].first) / kTicksPerQuarter + 1.0) };
}

// gen_note_events._melodic: step (<=2 semitones) / leap (>2) / none, against the temporally-adjacent
// same-PART note. `pn` is the part's notes as (onset, dur, midi), SORTED by (onset, midi). `dir` -1 =
// approach (previous distinct onset), +1 = departure (next distinct onset). The adjacent note is the
// min-|Δmidi| member of that onset group; "none" unless it is temporally contiguous (no rest gap).
int melodic(const std::vector<std::tuple<int, int, int> >& pn, size_t i, int dir)
{
    const int curOnset = std::get<0>(pn[i]);
    const int curDur = std::get<1>(pn[i]);
    const int curMidi = std::get<2>(pn[i]);

    // the adjacent distinct onset (max earlier for approach, min later for departure)
    bool have = false;
    int adjOnset = 0;
    for (const auto& nd : pn) {
        const int o = std::get<0>(nd);
        if (dir < 0 ? (o < curOnset) : (o > curOnset)) {
            if (!have || (dir < 0 ? (o > adjOnset) : (o < adjOnset))) {
                adjOnset = o;
                have = true;
            }
        }
    }
    if (!have) {
        return MV_NONE;
    }
    // among the group at adjOnset, the min-|Δmidi| note
    bool picked = false;
    int otherDur = 0, otherMidi = 0;
    for (const auto& nd : pn) {
        if (std::get<0>(nd) != adjOnset) {
            continue;
        }
        const int md = std::get<2>(nd);
        if (!picked || std::abs(md - curMidi) < std::abs(otherMidi - curMidi)) {
            otherDur = std::get<1>(nd);
            otherMidi = md;
            picked = true;
        }
    }
    const bool contiguous = (dir < 0) ? (adjOnset + otherDur == curOnset)
                                      : (curOnset + curDur == adjOnset);
    if (!contiguous) {
        return MV_NONE;
    }
    return (std::abs(otherMidi - curMidi) <= 2) ? MV_STEP : MV_LEAP;
}
} // namespace

AdapterFacts buildAdapterFacts(const mu::engraving::Score* score, const std::string& stem,
                               const std::set<size_t>& excludeStaves)
{
    using namespace mu::engraving;

    AdapterFacts fx;
    if (!score) {
        fx.error = "null score";
        return fx;
    }

    // ── structural facts: metrical grid, meter, initial key signature / declared mode ────────────
    const Grid grid = buildGrid(score);
    const EventMeasMap eventMap = buildEventMeasMap(score, grid);

    // meter / n_quarter / multi-meter (gen_note_events._time_signature): first time signature; distinct
    // (numerator, denominator) across measures. n_quarter = numerator*4/denominator (quarter-beats).
    int nQuarter = 0;
    std::set<std::pair<int, int> > sigs;
    for (const Measure* m = score->firstMeasure(); m; m = m->nextMeasure()) {
        const Fraction ts = m->timesig();
        if (ts.numerator() > 0 && ts.denominator() > 0) {
            sigs.insert({ ts.numerator(), ts.denominator() });
        }
    }
    if (!sigs.empty()) {
        const Fraction ts0 = score->firstMeasure()->timesig();
        fx.meterBeats = ts0.numerator();
        fx.meterBeatType = ts0.denominator();
        nQuarter = ts0.numerator() * 4 / ts0.denominator();
    }
    fx.multiMeter = sigs.size() > 1;

    // signature fifths + declared mode — the initial KeySigEvent (regionanalyzer.cpp pattern; the
    // Stage-4a <mode> import). read_xml_header reads the FIRST <fifths>/<mode>; staff 0 at tick 0.
    if (score->nstaves() > 0 && score->staff(0)) {
        const KeySigEvent kse = score->staff(0)->keySigEvent(Fraction(0, 1));
        fx.sigFifths = static_cast<int>(kse.concertKey());
        const KeyMode km = kse.mode();
        if (km == KeyMode::MAJOR || km == KeyMode::IONIAN) {
            fx.declaredMode = "major";
        } else if (km == KeyMode::MINOR || km == KeyMode::AEOLIAN) {
            fx.declaredMode = "minor";
        }
    }

    // staff -> Part index (== music21 part index). For this SATB corpus each Part is one staff, so
    // part == staff; using the Part index is the general music21-part-grouping rule (a multi-staff
    // part would group all its staves, as music21's part.recurse().notes does).
    std::unordered_map<int, int> staffToPart;
    {
        std::unordered_map<const Part*, int> partIndex;
        const std::vector<Part*>& parts = score->parts();
        for (size_t pi = 0; pi < parts.size(); ++pi) {
            partIndex[parts[pi]] = static_cast<int>(pi);
        }
        for (size_t s = 0; s < score->nstaves(); ++s) {
            const Staff* st = score->staff(s);
            const Part* pt = st ? st->part() : nullptr;
            const auto it = pt ? partIndex.find(pt) : partIndex.end();
            staffToPart[static_cast<int>(s)] = (it != partIndex.end()) ? it->second : static_cast<int>(s);
        }
    }

    // ── notes from the L1 published surface (notatedNotes — tie-UNRESOLVED atoms) ─────────────────
    const nm::NoteModel model = nm::NoteModel::build(score);

    std::vector<NoteRec> notes;
    notes.reserve(model.notatedNotes().size());
    for (const nm::NotatedNote& nn : model.notatedNotes()) {
        if (nn.isGrace) {
            continue;                       // music21 skips grace (duration.quarterLength == 0 => dur<=0)
        }
        if (nn.duration <= 0) {
            continue;                       // music21: if dur <= 0: continue
        }
        if (excludeStaves.count(static_cast<size_t>(nn.staff))) {
            continue;                       // OI-204 input-scoping: an excluded (chord-track) staff's
                                            // notes never enter the fact surface — no self-feedback on
                                            // a populated chord track. Empty set skips nothing.
        }
        NoteRec n;
        n.onset = nn.onset;
        n.dur = nn.duration;
        n.pc = ((nn.pitch % 12) + 12) % 12;
        n.midi = nn.pitch;
        n.lof = nn.tpc - static_cast<int>(Tpc::TPC_C);
        const auto pit = staffToPart.find(nn.staff);
        n.part = (pit != staffToPart.end()) ? pit->second : nn.staff;
        n.measure = measureNumberOf(grid, nn.onset);
        n.beat = notePaddedBeat(grid, nn.onset);
        n.mc = beatClass(n.beat, nQuarter);
        n.ap = MV_NONE;                     // filled per-part below
        n.dp = MV_NONE;
        n.tied = nn.tieContinuation ? 1 : 0;
        n.ferm = nn.hasFermata ? 1 : 0;
        notes.push_back(n);
    }

    // melodic approach/departure — computed WITHIN each part (gen_note_events computes ap/dp on the
    // per-part note list sorted by (onset, midi), BEFORE the global sort).
    std::unordered_map<int, std::vector<size_t> > byPart;
    for (size_t k = 0; k < notes.size(); ++k) {
        byPart[notes[k].part].push_back(k);
    }
    for (auto& kv : byPart) {
        std::vector<size_t>& idxs = kv.second;
        std::sort(idxs.begin(), idxs.end(), [&](size_t a, size_t b) {
            return notes[a].onset != notes[b].onset ? notes[a].onset < notes[b].onset
                                                    : notes[a].midi < notes[b].midi;
        });
        std::vector<std::tuple<int, int, int> > pn;
        pn.reserve(idxs.size());
        for (size_t gi : idxs) {
            pn.emplace_back(notes[gi].onset, notes[gi].dur, notes[gi].midi);
        }
        for (size_t i = 0; i < idxs.size(); ++i) {
            notes[idxs[i]].ap = melodic(pn, i, -1);
            notes[idxs[i]].dp = melodic(pn, i, +1);
        }
    }

    // final global order: (onset, part, midi) — gen_note_events.notes.sort.
    std::sort(notes.begin(), notes.end(), [](const NoteRec& a, const NoteRec& b) {
        if (a.onset != b.onset) {
            return a.onset < b.onset;
        }
        if (a.part != b.part) {
            return a.part < b.part;
        }
        return a.midi < b.midi;
    });

    // ── the event lattice (gen_note_events.extract_stem): minimal segments between consecutive
    // notated onsets/offsets with >=1 sounding note (the Pardo & Birmingham partition) ────────────
    std::set<int> boundSet;
    for (const NoteRec& n : notes) {
        boundSet.insert(n.onset);
        boundSet.insert(n.onset + n.dur);
    }
    const std::vector<int> bounds(boundSet.begin(), boundSet.end());

    std::vector<EventRec> events;
    for (size_t bi = 0; bi + 1 < bounds.size(); ++bi) {
        const int a = bounds[bi];
        const int b = bounds[bi + 1];
        bool anySounding = false;
        bool anyFerm = false;
        for (const NoteRec& n : notes) {
            if (n.onset <= a && n.onset + n.dur >= b) {
                anySounding = true;
                if (n.ferm != 0) {
                    anyFerm = true;
                }
            }
        }
        if (!anySounding) {
            continue;                       // a silent gap is not a harmonic event
        }
        EventRec ev;
        ev.start = a;
        ev.end = b;
        const std::pair<int, double> mb = eventMeasureBeat(eventMap, a);
        ev.measure = mb.first;
        ev.beat = mb.second;
        ev.mc = beatClass(ev.beat, nQuarter);
        ev.ferm = anyFerm ? 1 : 0;
        events.push_back(ev);
    }

    // ── assemble the Piece ────────────────────────────────────────────────────────────────────────
    fx.piece.stem = stem;
    fx.piece.nQuarter = nQuarter;
    fx.piece.notes = std::move(notes);
    fx.piece.events = std::move(events);
    fx.piece.prepare();
    fx.ok = true;
    return fx;
}

} // namespace mu::composing::analysis::joint
