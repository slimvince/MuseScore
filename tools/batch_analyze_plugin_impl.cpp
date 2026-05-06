// SPDX-License-Identifier: GPL-3.0-only
// MuseScore-Studio-CLA-applies
//
// batch_analyze_plugin_impl.cpp
//
// Faithful C++ reimplementation of chordIdentifierPopJazz-MS4_6_v1.qml for
// headless execution.  Designed as a fourth triage source alongside the
// musescore_analyzer, LLM, and music21_ground_truth providers.
//
// Outputs the unified LLM-triage response schema:
//   { "metadata": {...}, "tool_input": { "judgments": [...] } }
// Output file naming convention: <basename>.chordIdentifierPopJazz_response.json
//
// Settings hardcoded to plugin defaults:
//   displayChordMode     = 0  (Normal A-G, not Roman)
//   display_bass_note    = 1  (append /bass for inversions)
//   inversion_notation   = 0  (no figured-bass superscripts)
//   entire_note_duration = 1  (carry forward sustained notes)
//   hidePartialChords    = 1  (score shows "??" for partials; JSON records the actual label)
//   displayChordColor    = 0  (irrelevant for analysis)
//
// Integration into batch_analyze.cpp:
//   1. Add #include "batch_analyze_plugin_impl.h" (or forward-declare the two public
//      functions below).
//   2. Add a --plugin flag to argument parsing.
//   3. In the analysis dispatch, after loading the score:
//        if (usePlugin) {
//            auto regions = runPluginAnalysis(score);
//            writePluginResponseJson(regions, sourceBasename, scorePath,
//                                   scoreContentHash, out);
//            return 0;
//        }
//
// Algorithm correspondence to plugin source (chordIdentifierPopJazz-MS4_6_v1.qml):
//
//   Plugin symbol          C++ equivalent
//   ─────────────────────  ──────────────────────────────
//   tpc_name[]             TPC_NAMES[]
//   all_chords[]           ALL_CHORDS[]
//   find_intervals()       findIntervals()
//   compare_arr()          compareArr()
//   remove_dup_mod12()     removeDupMod12()
//   areNotesEqual()        areNotesEqual()
//   getChordName()         getChordName()
//   getAllCurrentNotes()   note-collection block in runPluginAnalysis()
//   setToClosestNextElement() seg->next1(ChordRest) loop in runPluginAnalysis()
//   runsheet()             runPluginAnalysis()
//
// Divergences intentionally corrected from prior draft (see comparison document):
//   1. Bass note: plugin scans chord ascending and takes the first chord-tone
//      (root/3rd/5th/7th/ext), skipping non-chord-tones.  Prior draft used
//      chord[0] unconditionally.  Fixed here.
//   2. Root TPC: plugin overwrites regular_chord[0] for every root note in the
//      ascending loop → last (highest-pitched) root determines the TPC used for
//      the chord name.  Prior draft used the first/lowest.  Fixed here.
//   3. Grace notes: plugin collects all Element.CHORD elements without filtering
//      for grace status.  Prior draft skipped chord->isGrace().  Removed here.
//   4. Note play/visible filter: plugin has no such filter.  Prior draft checked
//      n->play() && n->visible().  Removed here.

#include <algorithm>
#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#include "engraving/dom/score.h"
#include "engraving/dom/segment.h"
#include "engraving/dom/chord.h"
#include "engraving/dom/note.h"
#include "engraving/dom/measure.h"
#include "engraving/types/constants.h"

#include "../batch_analyze_plugin_impl.h"

using namespace mu::engraving;

// ─────────────────────────────────────────────────────────────────────────────
// JSON escape helper (shared convention with batch_analyze.cpp)
// ─────────────────────────────────────────────────────────────────────────────
static std::string pluginJsonEscape(const std::string& s)
{
    std::string r;
    r.reserve(s.size() + 8);
    for (unsigned char c : s) {
        switch (c) {
        case '"':  r += "\\\""; break;
        case '\\': r += "\\\\"; break;
        case '\n': r += "\\n";  break;
        case '\r': r += "\\r";  break;
        case '\t': r += "\\t";  break;
        default:
            if (c < 0x20) {
                char buf[8];
                std::snprintf(buf, sizeof(buf), "\\u%04x", c);
                r += buf;
            } else {
                r += static_cast<char>(c);
            }
        }
    }
    return r;
}

// ─────────────────────────────────────────────────────────────────────────────
// TPC → note name
// Plugin: getNoteName(note_tpc) using tpc_name[].
// Index range 0-33 direct; index 34 = tpc -1 (Fbb).
// ─────────────────────────────────────────────────────────────────────────────
static const char* TPC_NAMES[] = {
    "Cbb","Gbb","Dbb","Abb","Ebb","Bbb",        //  0–5
    "Fb","Cb","Gb","Db","Ab","Eb","Bb","F",      //  6–13
    "C","G","D","A","E","B",                      // 14–19
    "F#","C#","G#","D#","A#","E#","B#",          // 20–26
    "F##","C##","G##","D##","A##","E##","B##",   // 27–33
    "Fbb"                                         // 34 (tpc == -1)
};

static std::string getNoteName(int tpc)
{
    if (tpc == -1) return TPC_NAMES[34];
    if (tpc >= 0 && tpc <= 33) return TPC_NAMES[tpc];
    return "";
}

// ─────────────────────────────────────────────────────────────────────────────
// Chord templates
// Plugin: all_chords[] — 34 entries in exact order with exact intervals.
// Intervals are cumulative semitones from root (as produced by findIntervals).
// ─────────────────────────────────────────────────────────────────────────────
struct ChordTemplate {
    const char*      str;
    std::vector<int> intervals;
};

static const ChordTemplate ALL_CHORDS[] = {
    { "",           {4,7}         },   //  0: M (Major triad)
    { "m",          {3,7}         },   //  1: m (minor triad)
    { "dim",        {3,6}         },   //  2: dim (diminished triad)
    { "sus4",       {5,7}         },   //  3: sus4
    { "7sus4",      {5,7,10}      },   //  4: dominant 7sus4
    { "Maj7",       {4,7,11}      },   //  5: major 7th
    { "m(Maj7)",    {3,7,11}      },   //  6: minor/major 7th
    { "m7",         {3,7,10}      },   //  7: minor 7th
    { "7",          {4,7,10}      },   //  8: dominant 7th
    { "o7",         {3,6,9}       },   //  9: diminished 7th
    { "Maj7(#5)",   {4,8,11}      },   // 10: major 7th #5
    { "7(#5)",      {4,8,10}      },   // 11: dominant 7th #5
    { "aug",        {4,8}         },   // 12: augmented triad
    { "0",          {3,6,10}      },   // 13: half-diminished (m7b5)
    { "7(b5)",      {4,6,10}      },   // 14: dominant 7th b5
    { "(add9)",     {4,7,2}       },   // 15: major add9
    { "Maj9",       {4,7,11,2}    },   // 16: major 9th
    { "9",          {4,7,10,2}    },   // 17: dominant 9th
    { "m(add9)",    {3,7,2}       },   // 18: minor add9
    { "m9(Maj7)",   {3,7,11,2}    },   // 19: minor/major 9th
    { "m9",         {3,7,10,2}    },   // 20: minor 9th
    { "Maj7(#11)",  {4,7,11,6}    },   // 21: major 7th #11
    { "Maj9(#11)",  {4,7,11,2,6}  },   // 22: major 9th #11
    { "7(#11)",     {4,7,10,6}    },   // 23: dominant 7th #11
    { "9(#11)",     {4,7,10,2,6}  },   // 24: dominant 9th #11
    { "7(13)",      {4,7,10,9}    },   // 25: dominant 7th 13th
    { "9(13)",      {4,7,10,2,9}  },   // 26: dominant 9th 13th
    { "7(b9)",      {4,7,10,1}    },   // 27: dominant 7th b9
    { "7(b13)",     {4,7,10,8}    },   // 28: dominant 7th b13
    { "7(b9/b13)",  {4,7,10,1,8}  },   // 29: dominant 7th b9 b13
    { "11(b9/b13)", {4,7,10,1,5,8}},   // 30: 11th b9 b13
    { "7(#9)",      {4,7,10,3}    },   // 31: dominant 7th #9
    { "m7(11)",     {3,7,10,5}    },   // 32: minor 7th 11th
    { "m11",        {3,7,10,2,5}  },   // 33: minor 11th
};
static const int N_CHORDS = 34;

// ─────────────────────────────────────────────────────────────────────────────
// removeDupMod12
// Plugin: remove_dup_mod12(chord) — sorted unique pitch classes (mod 12).
// ─────────────────────────────────────────────────────────────────────────────
static std::vector<int> removeDupMod12(const std::vector<PluginNoteData>& chord)
{
    std::vector<int> pcs;
    pcs.reserve(chord.size());
    for (const auto& n : chord) pcs.push_back(n.pitch % 12);
    std::sort(pcs.begin(), pcs.end());
    pcs.erase(std::unique(pcs.begin(), pcs.end()), pcs.end());
    return pcs;
}

// ─────────────────────────────────────────────────────────────────────────────
// findIntervals
// Plugin: find_intervals(sorted_chord_uniq).
// For each root position: cumulative intervals between consecutive pitch classes,
// wrapping around the circle.  Zero intervals skipped.
// ─────────────────────────────────────────────────────────────────────────────
static std::vector<std::vector<int>> findIntervals(const std::vector<int>& uniq)
{
    int n = static_cast<int>(uniq.size());
    std::vector<std::vector<int>> intervals(n);
    for (int root = 0; root < n; root++) {
        int idx = -1;
        for (int i = 0; i < n - 1; i++) {
            int cur = (uniq[(root + i + 1) % n] - uniq[(root + i) % n]) % 12;
            while (cur < 0) cur += 12;
            if (cur != 0) {
                idx++;
                int val = cur;
                if (idx > 0) val += intervals[root][idx - 1];
                intervals[root].push_back(val);
            }
        }
    }
    return intervals;
}

// ─────────────────────────────────────────────────────────────────────────────
// compareArr
// Plugin: compare_arr(ref_arr, search_elt).
// Returns how many elements of ref appear in search, plus a per-element flag.
// ─────────────────────────────────────────────────────────────────────────────
struct CmpResult {
    int              nbFound;
    std::vector<int> cmpArr;   // 1 = found, 0 = not (same length as ref)
};

static CmpResult compareArr(const std::vector<int>& ref,
                             const std::vector<int>& search)
{
    CmpResult r{ 0, {} };
    r.cmpArr.reserve(ref.size());
    for (int v : ref) {
        bool found = (std::find(search.begin(), search.end(), v) != search.end());
        r.cmpArr.push_back(found ? 1 : 0);
        if (found) r.nbFound++;
    }
    return r;
}

// ─────────────────────────────────────────────────────────────────────────────
// areNotesEqual
// Plugin: areNotesEqual(chord1, chord2) using remove_dup(mod=10000) — i.e.,
// sorted unique original MIDI pitches (not mod-12).
// ─────────────────────────────────────────────────────────────────────────────
static bool areNotesEqual(const std::vector<PluginNoteData>& a,
                           const std::vector<PluginNoteData>& b)
{
    auto pitches = [](const std::vector<PluginNoteData>& c) {
        std::vector<int> v;
        v.reserve(c.size());
        for (const auto& n : c) v.push_back(n.pitch);
        std::sort(v.begin(), v.end());
        v.erase(std::unique(v.begin(), v.end()), v.end());
        return v;
    };
    return pitches(a) == pitches(b);
}

// ─────────────────────────────────────────────────────────────────────────────
// ChordResult
// ─────────────────────────────────────────────────────────────────────────────
struct PluginChordResult {
    std::string      chordLabel;     // actual label, e.g. "Cm7/G"; empty = not found
    bool             matchAllNotes;  // all note PCs accounted for by template
    std::vector<int> tonesPcSet;     // sorted unique pitch classes of the full chord
};

// ─────────────────────────────────────────────────────────────────────────────
// getChordName
// Plugin: getChordName(chord, keysig) with settings hardcoded as above.
//
// Divergence fixes applied here:
//   FIX-1  Bass: scan ascending-sorted chord for first chord-tone, skipping NCTs.
//   FIX-2  Root TPC: iterate without break → last (highest) root note wins.
// ─────────────────────────────────────────────────────────────────────────────
static PluginChordResult getChordName(std::vector<PluginNoteData>& chord,
                                       int /*keysig*/)
{
    // Sort ascending — required for bass determination (FIX-1) and root TPC
    // (FIX-2).  Plugin: chord.sort(function(a,b){ return a.pitch - b.pitch; })
    std::sort(chord.begin(), chord.end(),
              [](const PluginNoteData& a, const PluginNoteData& b){
                  return a.pitch < b.pitch;
              });

    auto uniq = removeDupMod12(chord);
    if (uniq.empty()) return { "", false, {} };

    auto intervals = findIntervals(uniq);

    // Build tonesPcSet from the sorted unique PCs.
    std::vector<int> tonesPcSet = uniq;

    // ── Template matching ──────────────────────────────────────────────────
    // Plugin: nested loop idx_chtype_ / idx_rootpos_; keep best full match.
    int  idx_chtype = -1, idx_rootpos = -1, nb_found = 0;
    bool all_found  = false;

    std::vector<int>              idx_chtype_arr, idx_rootpos_arr, nb_found_arr;
    std::vector<std::vector<int>> cmp_result_arr;

    for (int ct = 0; ct < N_CHORDS; ct++) {
        for (int rp = 0; rp < static_cast<int>(intervals.size()); rp++) {
            auto cmp = compareArr(ALL_CHORDS[ct].intervals, intervals[rp]);
            if (cmp.nbFound > 0) {
                if (cmp.nbFound == static_cast<int>(ALL_CHORDS[ct].intervals.size())) {
                    // Full match: keep the one with the most intervals matched.
                    if (cmp.nbFound > nb_found) {
                        nb_found    = cmp.nbFound;
                        idx_rootpos = rp;
                        idx_chtype  = ct;
                        if (nb_found == static_cast<int>(intervals[rp].size()))
                            all_found = true;
                    }
                }
                // Save every partial candidate for fallback.
                idx_chtype_arr.push_back(ct);
                idx_rootpos_arr.push_back(rp);
                cmp_result_arr.push_back(cmp.cmpArr);
                nb_found_arr.push_back(cmp.nbFound);
            }
        }
    }

    // ── Partial-chord fallback ─────────────────────────────────────────────
    // Plugin: if no full match found, try (1) 3rd+7th present, then (2) 3rd only.
    // The nb_found max computation is debug-only in the plugin and does NOT
    // pre-filter the candidate list; we faithfully omit that filter here.
    if (idx_chtype < 0 && !idx_chtype_arr.empty()) {
        // Pass 1: third (cmpArr[0]==1) AND 7th (cmpArr[2]==1).
        // Plugin accesses cmpArr[2] directly; JS undefined===1 is false, so this
        // is a no-op for 2-element arrays.  Guard with size()>=3 to match.
        for (int i = 0; i < static_cast<int>(cmp_result_arr.size()); i++) {
            const auto& c = cmp_result_arr[i];
            if (c.size() >= 3 && c[0] == 1 && c[2] == 1) {
                idx_chtype  = idx_chtype_arr[i];
                idx_rootpos = idx_rootpos_arr[i];
                break;
            }
        }
        // Pass 2: third only (cmpArr[0]==1).
        if (idx_chtype < 0) {
            for (int i = 0; i < static_cast<int>(cmp_result_arr.size()); i++) {
                const auto& c = cmp_result_arr[i];
                if (!c.empty() && c[0] == 1) {
                    idx_chtype  = idx_chtype_arr[i];
                    idx_rootpos = idx_rootpos_arr[i];
                    break;
                }
            }
        }
    }

    if (idx_chtype < 0)
        return { "", false, tonesPcSet };

    int rootNote = uniq[idx_rootpos];  // pitch class of identified root

    // ── FIX-2: Root TPC — last (highest-pitched) root note ────────────────
    // Plugin: regular_chord[0] = chord[i] inside ascending loop, no break →
    // overwritten on each root note found → final value is the highest root.
    int rootTpc = 14;  // default C
    for (const auto& n : chord) {
        if ((n.pitch % 12) == (rootNote % 12))
            rootTpc = n.tpc;  // intentional: no break
    }

    // ── FIX-1: Bass note — first chord-tone in ascending pitch order ───────
    // Plugin: iterates chord (sorted ascending), checks root/3rd/5th/7th/ext
    // in order and sets bass=chord[i] on first match; NCTs fall through to
    // the color-reset else-branch and do not update bass.
    int bassPitch12 = -1;
    int bassTpc     = 14;
    for (const auto& n : chord) {
        int  pc           = n.pitch % 12;
        bool isChordTone  = (pc == (rootNote % 12));
        if (!isChordTone) {
            for (int iv : ALL_CHORDS[idx_chtype].intervals) {
                if (pc == ((rootNote + iv) % 12)) { isChordTone = true; break; }
            }
        }
        if (isChordTone) {
            bassPitch12 = pc;
            bassTpc     = n.tpc;
            break;
        }
    }
    // Fallback: all notes are NCTs (shouldn't occur in practice).
    if (bassPitch12 < 0) {
        bassPitch12 = chord[0].pitch % 12;
        bassTpc     = chord[0].tpc;
    }

    // ── Build chord name ───────────────────────────────────────────────────
    std::string chordName = getNoteName(rootTpc) + ALL_CHORDS[idx_chtype].str;

    // ── Inversion ─────────────────────────────────────────────────────────
    // inversion_notation=0: no superscripts/figured-bass appended.
    int inv = -1;
    if (bassPitch12 == (rootNote % 12)) {
        inv = 0;
    } else {
        for (int i = 0; i < static_cast<int>(ALL_CHORDS[idx_chtype].intervals.size()); i++) {
            if (bassPitch12 == ((rootNote + ALL_CHORDS[idx_chtype].intervals[i]) % 12)) {
                inv = i + 1;
                break;
            }
        }
    }

    // display_bass_note=1: append /bassNote when not root position.
    if (inv > 0)
        chordName += "/" + getNoteName(bassTpc);

    return { chordName, all_found, tonesPcSet };
}

// ─────────────────────────────────────────────────────────────────────────────
// runPluginAnalysis
// Plugin: runsheet() main loop + getAllCurrentNotes() + setToClosestNextElement().
//
// Divergence fixes applied here:
//   FIX-3  Grace notes: plugin never filters by grace status (cursor lands on
//          grace-note ChordRest segments if they have a Chord element); isGrace()
//          check from prior draft removed.
//   FIX-4  Note filter: plugin pushes all notes[i] without play/visible checks;
//          n->play() && n->visible() check from prior draft removed.
// ─────────────────────────────────────────────────────────────────────────────
std::vector<PluginRegion> runPluginAnalysis(const Score* score)
{
    std::vector<PluginRegion> results;

    std::vector<PluginNoteData> prevChord;
    std::string                 prevChordLabel;
    bool                        prevMatchedAll = false;

    const int nstaves = static_cast<int>(score->nstaves());

    // Start from first ChordRest segment.
    const Segment* seg = score->firstSegment(SegmentType::ChordRest);

    while (seg) {
        const int tick = seg->tick().ticks();

        // ── Collect notes at this segment ─────────────────────────────────
        // Plugin: getAllCurrentNotes iterates staff endStaff→0, voice 3→0,
        // pushes cursor.element.notes without any play/visible or grace filter.
        std::vector<PluginNoteData> currentNotes;

        for (int si = nstaves - 1; si >= 0; si--) {
            for (int v = 3; v >= 0; v--) {
                const EngravingItem* el = seg->element(
                    static_cast<track_idx_t>(si) * VOICES + v);
                if (!el || !el->isChord()) continue;
                const Chord* chord = toChord(el);
                // FIX-3: no isGrace() skip — plugin does not filter grace chords.
                // Only collect notes whose chord onset == seg tick; the cursor
                // in the plugin lands at a specific tick position and sees only
                // the chord onset there.
                if (chord->tick().ticks() != tick) continue;
                const int chordEnd = tick + chord->actualTicks().ticks();
                for (const Note* n : chord->notes()) {
                    // FIX-4: no play/visible filter — plugin pushes all notes[i].
                    currentNotes.push_back({ n->ppitch(), n->tpc(), chordEnd });
                }
            }
        }

        // ── entire_note_duration=1: carry forward sustained notes ──────────
        // Plugin: for each note in prev_chord, if
        //   note.parent.parent.tick + chordDuration(note.parent) > cursor.tick
        // then push into full_chord.  Equivalent to endTick > currentTick.
        for (const auto& n : prevChord) {
            if (n.endTick > tick)
                currentNotes.push_back(n);
        }

        if (!currentNotes.empty()) {
            // ── Identify chord ─────────────────────────────────────────────
            auto res = getChordName(currentNotes, 0);

            // ── Duplicate suppression ──────────────────────────────────────
            // Plugin: suppress (harmony.text='') when
            //   (prev_chordName == chordName && prev_matched_all && curr_matched_all)
            //   OR areNotesEqual(prev_full_chord, full_chord)
            bool suppress = false;
            if (!results.empty()) {
                if ((prevChordLabel == res.chordLabel
                     && prevMatchedAll
                     && res.matchAllNotes)
                    || areNotesEqual(prevChord, currentNotes)) {
                    suppress = true;
                }
            }

            // Compute measure number and beat onset.
            const Measure* m        = seg->measure();
            const int measureNum    = m ? m->measureNumber() + 1 : 0;
            const int measureTick   = m ? m->tick().ticks() : 0;
            const double beatStart  = 1.0 + static_cast<double>(tick - measureTick)
                                           / Constants::DIVISION;

            results.push_back({
                tick,
                tick,               // tickEnd: placeholder, filled below
                measureNum,
                beatStart,
                0.0,                // durationBeats: placeholder
                res.chordLabel,
                res.matchAllNotes,
                suppress,
                currentNotes,
                res.tonesPcSet
            });

            prevChordLabel = res.chordLabel;
            prevMatchedAll = res.matchAllNotes;
            prevChord      = currentNotes;
        }

        // ── Advance to next segment with any Chord element ─────────────────
        // Plugin: setToClosestNextElement scans seg.next (all segment types)
        // until it finds one with Element.CHORD.  Using next1(ChordRest) is
        // functionally equivalent because Chord elements only exist inside
        // ChordRest segments.
        const Segment* next = seg->next1(SegmentType::ChordRest);
        while (next) {
            bool hasChord = false;
            for (track_idx_t tr = 0; tr < score->ntracks(); tr++) {
                const EngravingItem* el = next->element(tr);
                if (el && el->isChord()) { hasChord = true; break; }
            }
            if (hasChord) break;
            next = next->next1(SegmentType::ChordRest);
        }
        seg = next;
    }

    // ── Post-processing: fill tickEnd and durationBeats ───────────────────
    // Each non-suppressed entry's tickEnd = next non-suppressed entry's tickStart
    // (or score end tick).  Suppressed entries are excluded from the JSON output
    // so the previous entry's tick range implicitly covers them.
    const int scoreLast = score->lastMeasure()
                        ? score->lastMeasure()->endTick().ticks()
                        : (results.empty() ? 0 : results.back().tickStart);

    // Build index of non-suppressed entries for tickEnd propagation.
    std::vector<size_t> activeIdx;
    for (size_t i = 0; i < results.size(); i++) {
        if (!results[i].suppressed)
            activeIdx.push_back(i);
    }
    for (size_t k = 0; k < activeIdx.size(); k++) {
        PluginRegion& r = results[activeIdx[k]];
        const int endTick = (k + 1 < activeIdx.size())
                          ? results[activeIdx[k + 1]].tickStart
                          : scoreLast;
        r.tickEnd        = endTick;
        r.durationBeats  = static_cast<double>(endTick - r.tickStart)
                          / Constants::DIVISION;
    }

    return results;
}

// ─────────────────────────────────────────────────────────────────────────────
// beatRangeStr
// Mimics convert_music21_ground_truth.py beat_range_str(beat, duration):
//   "1-2" = beats 1 through 2 inclusive (duration 2), "3" = 1-beat region at 3.
// ─────────────────────────────────────────────────────────────────────────────
static std::string beatRangeStr(double beatStart, double durationBeats)
{
    auto fmt = [](double v) -> std::string {
        // Show as integer when integral; otherwise up to 3 significant digits.
        double iv;
        if (std::modf(v, &iv) == 0.0) {
            return std::to_string(static_cast<int>(iv));
        }
        char buf[32];
        std::snprintf(buf, sizeof(buf), "%.3g", v);
        return buf;
    };
    const double endVal = beatStart + durationBeats - 1.0;
    if (durationBeats <= 1.0 + 1e-6)
        return fmt(beatStart);
    return fmt(beatStart) + "-" + fmt(endVal);
}

// ─────────────────────────────────────────────────────────────────────────────
// tonesPcSetStr
// Format the sounding notes as "C4 E4 G4" etc. for the tones_pc_set field.
// One entry per unique pitch class (lowest-pitched instance), sorted ascending.
// Uses TPC for note name and MIDI pitch for octave (C4 = MIDI 60).
// ─────────────────────────────────────────────────────────────────────────────
static std::string tonesPcSetStr(const std::vector<PluginNoteData>& chord,
                                  const std::vector<int>& tonesPcSet)
{
    if (chord.empty() || tonesPcSet.empty()) return "";

    // Map each unique PC to the lowest-pitched note instance.
    std::vector<PluginNoteData> sorted = chord;
    std::sort(sorted.begin(), sorted.end(),
              [](const PluginNoteData& a, const PluginNoteData& b){
                  return a.pitch < b.pitch;
              });

    std::vector<PluginNoteData> repNotes;
    repNotes.reserve(tonesPcSet.size());
    for (int pc : tonesPcSet) {
        for (const auto& n : sorted) {
            if ((n.pitch % 12) == pc) {
                repNotes.push_back(n);
                break;
            }
        }
    }
    // Sort by pitch ascending so the output order matches the analyzer convention.
    std::sort(repNotes.begin(), repNotes.end(),
              [](const PluginNoteData& a, const PluginNoteData& b){
                  return a.pitch < b.pitch;
              });

    std::ostringstream oss;
    for (size_t i = 0; i < repNotes.size(); i++) {
        if (i) oss << " ";
        const int octave = repNotes[i].pitch / 12 - 1;
        oss << getNoteName(repNotes[i].tpc) << octave;
    }
    return oss.str();
}

// ─────────────────────────────────────────────────────────────────────────────
// writePluginResponseJson
// Emits the unified LLM-triage response schema.
// Suppressed entries are excluded; their tick range is covered by the preceding
// non-suppressed entry's tickEnd (set in runPluginAnalysis post-processing).
// ─────────────────────────────────────────────────────────────────────────────
void writePluginResponseJson(
    const std::vector<PluginRegion>& regions,
    const std::string& scoreBasename,
    const std::string& scorePath,
    const std::string& scoreContentHash,   // SHA-256 hex or ""
    const std::string& timestampUtc,       // ISO-8601 UTC or ""
    std::ostream& out)
{
    // ── Metadata ──────────────────────────────────────────────────────────
    out << "{\n";
    out << "  \"metadata\": {\n";
    out << "    \"score_basename\": \""   << pluginJsonEscape(scoreBasename)  << "\",\n";
    out << "    \"score_path\": \""       << pluginJsonEscape(scorePath)      << "\",\n";
    out << "    \"score_content_hash\": \""<< pluginJsonEscape(scoreContentHash) << "\",\n";
    out << "    \"requested_model\": \"chordIdentifierPopJazz_MS4_6_v1\",\n";
    out << "    \"provider\": \"chordIdentifierPopJazz\",\n";
    out << "    \"model\": \"chordIdentifierPopJazz_MS4_6_v1\",\n";

    // model_response_id: deterministic from score content hash if available.
    const std::string responseId = scoreContentHash.size() >= 16
                                 ? "deterministic-" + scoreContentHash.substr(0, 16)
                                 : "chordIdentifierPopJazz-" + scoreBasename;
    out << "    \"model_response_id\": \"" << pluginJsonEscape(responseId) << "\",\n";

    out << "    \"prompt_version\": \"v1.3\",\n";
    out << "    \"system_prompt_hash\": \"\",\n";
    out << "    \"tool_definition_hash\": \"\",\n";
    out << "    \"timestamp_utc\": \""    << pluginJsonEscape(timestampUtc) << "\",\n";
    out << "    \"input_tokens\": 0,\n";
    out << "    \"output_tokens\": 0,\n";
    out << "    \"stop_reason\": \"completed\",\n";
    out << "    \"is_authoritative\": false,\n";
    out << "    \"ground_truth_source\": null,\n";
    out << "    \"plugin_settings\": {\n";
    out << "      \"displayChordMode\": 0,\n";
    out << "      \"display_bass_note\": 1,\n";
    out << "      \"inversion_notation\": 0,\n";
    out << "      \"entire_note_duration\": 1,\n";
    out << "      \"hidePartialChords\": 1\n";
    out << "    }\n";
    out << "  },\n";

    // ── Judgments ─────────────────────────────────────────────────────────
    out << "  \"tool_input\": {\n";
    out << "    \"judgments\": [\n";

    bool firstJudgment = true;
    for (const auto& r : regions) {
        if (r.suppressed) continue;

        // Confidence: full match + all notes → high; full match + NCTs → medium;
        // partial match → low; no identification → none.
        const char* confidence;
        double      confidenceRaw;
        if (r.chordLabel.empty()) {
            confidence    = "none";
            confidenceRaw = 0.0;
        } else if (r.matchAllNotes) {
            confidence    = "high";
            confidenceRaw = 1.0;
        } else {
            // Full template match but extra non-chord-tones present
            // (matchAllNotes = false when notes.size() > template.intervals.size()).
            // Also covers partial template matches (3rd+7th / 3rd fallback).
            confidence    = "low";
            confidenceRaw = 0.4;
        }

        const std::string beatRange  = beatRangeStr(r.beatStart, r.durationBeats);
        const std::string tonesStr   = tonesPcSetStr(r.chord, r.tonesPcSet);

        if (!firstJudgment) out << ",\n";
        firstJudgment = false;

        out << "      {\n";
        out << "        \"measure\": "         << r.measureNumber             << ",\n";
        out << "        \"beat_range\": \""    << pluginJsonEscape(beatRange) << "\",\n";
        out << "        \"tick_start\": "      << r.tickStart                 << ",\n";
        out << "        \"tick_end\": "        << r.tickEnd                   << ",\n";
        out << "        \"chord_label\": \""   << pluginJsonEscape(r.chordLabel) << "\",\n";
        out << "        \"chord_label_alternatives\": [],\n";
        out << "        \"key\": \"\",\n";
        out << "        \"mode\": \"\",\n";
        out << "        \"confidence\": \""    << confidence                  << "\",\n";

        // confidence_raw: emit as decimal without scientific notation
        {
            char buf[32];
            std::snprintf(buf, sizeof(buf), "%.4g", confidenceRaw);
            out << "        \"confidence_raw\": " << buf << ",\n";
        }

        out << "        \"reasoning\": \"chordIdentifierPopJazz rule-based match"
            << (r.matchAllNotes ? "" : "; partial or extra NCTs present")
            << "\",\n";
        out << "        \"roman_numeral\": \"\",\n";
        out << "        \"diatonic_to_key\": null,\n";
        out << "        \"tones_pc_set\": \""  << pluginJsonEscape(tonesStr)  << "\"\n";
        out << "      }";
    }

    out << "\n    ],\n";
    out << "    \"key_summary\": \"\",\n";
    out << "    \"ambiguity_flags\": [],\n";
    out << "    \"format_friction\": \"\"\n";
    out << "  }\n";
    out << "}\n";
}
