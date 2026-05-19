// ScoreAccess.js — MuseScore-facing read/write helpers for the AI Assistant.
//
// This module is the MuseScore layer. It speaks plain MuseScore: api.engraving,
// curScore, Cursor, Segment, EngravingItem. It has no awareness of LLMs, JSON
// schemas, tool names, or dispatching. A MuseScore developer who has never
// heard of an LLM should be able to read this file and recognise standard
// extension-API code.
//
// All exported functions return either:
//   { ok: true, ... } / a value-shaped object on success
//   { error: "<human-readable reason>" } on failure (including "No score open")
//
// Write functions are wrapped in startCmd / endCmd so each tool call lands as
// a single user-visible undo step.
//
// NOTE: this file deliberately omits `.pragma library`. A library JS file
// cannot access QML context properties like `api` (Qt docs: "Shared libraries
// can access the global object, but not the QML scope"), and we need
// `api.engraving.curScore` everywhere.

// ── ElementType integer map (MuseScore 4.7.0) ─────────────────────────────
//
// On 4.7.0 (apiversion=2), api.engraving.Element.XXXX returns a string name
// instead of an integer. newElement() only accepts integers. These values were
// verified by probing newElement(0..200) on the actual 4.7.0 release binary —
// do NOT replace them with source-derived estimates.
var _EL = {
    TEXT:             5,
    LAYOUT_BREAK:     6,
    ACCIDENTAL:       20,
    NOTE:             24,
    CLEF:             25,   // source position 26
    KEYSIG:           26,   // source position 27
    TIMESIG:          28,   // source position 29 (AMBITUS=28 sits between KEYSIG and TIMESIG in source)
    REST:             29,
    TIE:              35,
    ARTICULATION:     38,
    FERMATA:          40,
    DYNAMIC:          42,
    EXPRESSION:       43,
    LYRICS:           45,
    FINGERING:        50,
    TEMPO_TEXT:       52,
    STAFF_TEXT:       53,
    SYSTEM_TEXT:      54,
    REHEARSAL_MARK:   61,
    HARMONY:          65,
    HAIRPIN:          102,
    OTTAVA:           103,
    CHORD:            123,
    SLUR:             124,
    // TREMOLO_SINGLECHORD: 139 is derived from src/engraving/types/types.h line 209
    // (ElementType::TREMOLO_SINGLECHORD), following the established line−70 offset
    // that every other _EL entry matches exactly. NOT runtime-probed yet — verify
    // with newElement(139) on a 4.7.0 binary before relying on it. The Batch D1
    // instruction proposed 459 (derived from apitypes.h line 460−1); that derivation
    // is wrong — apitypes.h line numbers are NOT the enum integer values.
    TREMOLO_SINGLECHORD: 139
}

// ── TextStyleType integer values ──────────────────────────────────────────
//
// Note-level text annotations (FINGERING, STRING_NUMBER, LH_GUITAR_FINGERING,
// RH_GUITAR_FINGERING) are NOT separate ElementTypes — they are all
// ElementType::FINGERING with a different TextStyleType, distinguished via
// Pid::TEXT_STYLE. The QML surface exposes Pid::TEXT_STYLE through the
// writable `subStyle` property on EngravingItem (see API_PROPERTY(subStyle,
// TEXT_STYLE) in src/engraving/api/v1/elements.h).
//
// Values are source-derived from the TextStyleType enum in
// src/engraving/types/types.h. STRING_NUMBER's position in the enum is 45
// (DEFAULT=0, then 44 entries before STRING_NUMBER).
var _TS = {
    STRING_NUMBER:    45
}

// ── ClefType integer map ──────────────────────────────────────────────────
//
// From the ClefType enum in src/engraving/types/types.h. These are literal
// enum values — NOT subject to the source_position−1 offset used for
// ElementType. Set via both el.concertClefType (Pid::CLEF_TYPE_CONCERT)
// and el.transposingClefType (Pid::CLEF_TYPE_TRANSPOSING).
var _CLEF = {
    "treble":     0,   // G
    "treble8vb":  2,   // G8_VB (guitar treble, sounds 8vb)
    "treble8va":  3,   // G8_VA
    "tenor":      11,  // C4 (viola/cello tenor position)
    "alto":       10,  // C3
    "bass":       20,  // F  (was 21 = F15_MB sub-bass — off by one, now fixed)
    "bass8vb":    22,  // F8_VB
    "percussion": 29,  // PERC
    "tab":        31,  // TAB
    "tab4":       32   // TAB4
}

// Reverse lookup: ClefType integer → string name used in the _CLEF map.
// Returns the string key if found, or "unknown(" + clefInt + ")" if not.
function _clefIntToName(clefInt) {
    var keys = Object.keys(_CLEF)
    for (var i = 0; i < keys.length; i++) {
        if (_CLEF[keys[i]] === clefInt) return keys[i]
    }
    return "unknown(" + clefInt + ")"
}

// ── Internal helpers ──────────────────────────────────────────────────────

// Return curScore or null. Callers should check before continuing.
function _score() {
    try {
        if (typeof api === "undefined" || !api || !api.engraving) return null
        return api.engraving.curScore || null
    } catch(e) {
        return null
    }
}

// Sharps-count → "<tonic> major" / "<tonic> minor" string.
// MuseScore's curScore.keysig is the signature only, not the mode, so we always
// label it as major. (Mode disambiguation would require analysing the music.)
function _keysigToString(fifths) {
    if (typeof fifths !== "number") return ""
    var majors = {
        "-7": "Cb major", "-6": "Gb major", "-5": "Db major", "-4": "Ab major",
        "-3": "Eb major", "-2": "Bb major", "-1": "F major",   "0": "C major",
        "1": "G major",   "2": "D major",   "3": "A major",    "4": "E major",
        "5": "B major",   "6": "F# major",  "7": "C# major"
    }
    return majors[String(fifths)] || ("fifths=" + fifths)
}

// Walk segment annotations and return the first element of the requested type.
function _findAnnotation(segment, elementType) {
    if (!segment || !segment.annotations) return null
    var ann = segment.annotations
    for (var i = 0; i < ann.length; i++) {
        if (ann[i] && ann[i].type === elementType) return ann[i]
    }
    return null
}

// Find the first TempoText anywhere in a measure's segments.
function _firstTempoInMeasure(measure) {
    if (!measure) return null
    // Hoist: api.engraving.Element.X rebuilds the full enum on every access on 4.7.0.
    var TEMPO_TEXT = api.engraving.Element.TEMPO_TEXT
    var s = measure.firstSegment
    while (s) {
        var t = _findAnnotation(s, TEMPO_TEXT)
        if (t) return t
        s = s.nextInMeasure
    }
    return null
}

// Find the first RehearsalMark anywhere in a measure's segments.
function _firstRehearsalMarkInMeasure(measure) {
    if (!measure) return null
    var REHEARSAL_MARK = api.engraving.Element.REHEARSAL_MARK
    var s = measure.firstSegment
    while (s) {
        var r = _findAnnotation(s, REHEARSAL_MARK)
        if (r) return r
        s = s.nextInMeasure
    }
    return null
}

// Find measure by 1-based number. Returns null if out of range.
function _findMeasureByNumber(score, n) {
    if (!score || typeof n !== "number" || n < 1) return null
    var m = score.firstMeasure
    var idx = 1
    while (m) {
        if (idx === n) return m
        idx++
        m = m.nextMeasure
    }
    return null
}

// Read style by Sid name, swallowing exceptions.
function _styleValue(score, key, fallback) {
    try {
        if (!score || !score.style) return fallback
        var v = score.style.value(key)
        return (v === undefined || v === null) ? fallback : v
    } catch(e) {
        return fallback
    }
}

// Normalise a tick value that may be a plain int or a MuseScore Fraction.
function _getTickInt(tick) {
    if (typeof tick === "number") return tick
    if (tick && typeof tick.ticks === "number") return tick.ticks
    return 0
}

// Greatest-common-divisor (Euclidean), used for beat-fraction simplification.
function _gcd(a, b) {
    while (b > 0) { var t = b; b = a % b; a = t }
    return a
}

// Convert a segment tick position into a Beat object { beat, fraction }.
// Quarter-note based; correct for 4/4, 3/4, etc. Simplification for compound meters.
function _tickToBeat(segTick, measureTick) {
    var QUARTER = 480
    var offset = segTick - measureTick
    if (offset < 0) offset = 0
    var beatN = Math.floor(offset / QUARTER) + 1
    var rem   = offset % QUARTER
    var frac  = "0"
    if (rem > 0) {
        var g = _gcd(rem, QUARTER)
        frac = (rem / g) + "/" + (QUARTER / g)
    }
    return { beat: beatN, fraction: frac }
}

// Convert MuseScore TPC + MIDI pitch to a NoteName string ("C4", "F#3", "Bb5"…).
// TPC ordering: F=13, C=14, G=15, D=16, A=17, E=18, B=19; each sharp +7, each flat -7.
function _tpcToNoteName(tpc, pitch) {
    if (tpc < -1 || tpc > 33) return "?"
    var LETTERS = ["F","C","G","D","A","E","B"]
    var acc
    if      (tpc <  6) acc = "bb"
    else if (tpc < 13) acc = "b"
    else if (tpc < 20) acc = ""
    else if (tpc < 27) acc = "#"
    else               acc = "##"
    var letterIdx = ((tpc - 13) % 7 + 7) % 7
    var letter    = LETTERS[letterIdx]
    var basePc    = { "C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11 }[letter]
    var shift     = acc === "bb" ? -2 : acc === "b" ? -1 : acc === "#" ? 1 : acc === "##" ? 2 : 0
    var writtenPc = ((basePc + shift) % 12 + 12) % 12
    var octave    = Math.round((pitch - writtenPc) / 12) - 1
    return letter + acc + octave
}

// Map a MuseScore duration Fraction string ("1/4", "3/8") to an infomodel
// Duration string. Falls back to the raw fraction if unrecognised.
function _durationStr(fracStr) {
    var map = {
        "8/1": "longa",       "4/1": "breve",
        "1/1": "whole",       "3/2": "dotted whole",
        "1/2": "half",        "3/4": "dotted half",        "7/8":  "double-dotted half",
        "1/4": "quarter",     "3/8": "dotted quarter",     "7/16": "double-dotted quarter",
        "1/8": "eighth",      "3/16": "dotted eighth",     "7/32": "double-dotted eighth",
        "1/16": "16th",       "3/32": "dotted 16th",       "7/64": "double-dotted 16th",
        "1/32": "32nd",       "3/64": "dotted 32nd",
        "1/64": "64th",       "3/128": "dotted 64th",
        "1/128": "128th"
    }
    return map[fracStr] || fracStr
}

// Find measure by 1-based number using curScore. Returns the Measure or null.
// (Wraps _findMeasureByNumber for callers that don't already hold a score ref.)
function _findMeasure(measureNo) {
    var s = _score()
    if (!s) return null
    return _findMeasureByNumber(s, measureNo)
}

// Reverse of _findMeasure: take an absolute tick (int) and return the 1-based
// measure number that contains it. Walks measures in order; returns the last
// measure if tick is past end. Used by getSelection() to map segment ticks
// back to measure numbers for the LLM-facing musical address.
function _tickToMeasureNo(tick) {
    var s = _score()
    if (!s) return null
    var m = s.firstMeasure
    var no = 1
    while (m) {
        var next = m.nextMeasure
        var nextTick = next ? _getTickInt(next.firstSegment.tick) : Number.MAX_VALUE
        if (tick < nextTick) return no
        m = next
        no++
    }
    return no - 1
}

// Convert a NoteName string ("C4", "F#3", "Bb5", "B##4") to a MIDI pitch
// integer. Middle C = "C4" = 60.
function _noteNameToMidi(pitchStr) {
    var classBase = { C:0, D:2, E:4, F:5, G:7, A:9, B:11 }
    var cls = pitchStr[0].toUpperCase()
    var i = 1
    var acc = 0
    while (i < pitchStr.length && (pitchStr[i] === '#' || pitchStr[i] === 'b')) {
        acc += (pitchStr[i] === '#') ? 1 : -1
        i++
    }
    var octave = parseInt(pitchStr.slice(i))
    return (octave + 1) * 12 + (classBase[cls] || 0) + acc
}

// Convert a Duration string to [numerator, denominator] for cursor.setDuration.
// Falls back to quarter-note for unrecognised input.
function _durationToFraction(durationStr) {
    var map = {
        "longa":                   [4, 1],
        "breve":                   [2, 1],
        "whole":                   [1, 1],
        "half":                    [1, 2],
        "quarter":                 [1, 4],
        "eighth":                  [1, 8],
        "16th":                    [1, 16],
        "32nd":                    [1, 32],
        "64th":                    [1, 64],
        "128th":                   [1, 128],
        "dotted half":             [3, 4],
        "dotted quarter":          [3, 8],
        "dotted eighth":           [3, 16],
        "dotted 16th":             [3, 32],
        "dotted 32nd":             [3, 64],
        "double-dotted half":      [7, 8],
        "double-dotted quarter":   [7, 16],
        "double-dotted eighth":    [7, 32]
    }
    return map[durationStr] || [1, 4]
}

// SyllabicType string → integer used by Lyrics.syllabic
// (api.engraving.Lyrics.{SINGLE:0, BEGIN:1, END:2, MIDDLE:3} per runtime probe).
function _syllabicToInt(syllabic) {
    var map = { "single": 0, "begin": 1, "end": 2, "middle": 3 }
    return (map[syllabic] !== undefined) ? map[syllabic] : 0
}

// NoteName string → TPC (Tonal Pitch Class) integer.
// TPC line of fifths: F=13, C=14, G=15, D=16, A=17, E=18, B=19 for naturals.
// Each sharp adds 7; each flat subtracts 7.
function _noteNameToTpc(pitchStr) {
    var baseMap = { C:14, D:16, E:18, F:13, G:15, A:17, B:19 }
    var cls = pitchStr[0].toUpperCase()
    var i = 1
    var acc = 0
    while (i < pitchStr.length && (pitchStr[i] === '#' || pitchStr[i] === 'b')) {
        acc += (pitchStr[i] === '#') ? 7 : -7
        i++
    }
    return (baseMap[cls] !== undefined ? baseMap[cls] : 14) + acc
}

// Key fifths int (-7..+7) → "<tonic> major" label. Mode disambiguation is not
// possible from the signature alone, so we always label as major (same as
// _keysigToString — kept as a separate name for getMeasure clarity).
function _keyIntToString(key) {
    return _keysigToString(key)
}

// BarLine type bit-flag int → human-readable string. BarLineType in
// src/engraving/types/types.h:422 — flag enum, so we test bits in priority
// order (compound flags would otherwise be misreported).
function _barlineTypeStr(typeInt) {
    if (typeInt === 1)      return "normal"          // NORMAL/SINGLE
    if (typeInt === 2)      return "double"          // DOUBLE
    if (typeInt === 4)      return "startRepeat"     // START_REPEAT
    if (typeInt === 8)      return "endRepeat"       // END_REPEAT
    if (typeInt === 16)     return "dashed"          // BROKEN/DASHED
    if (typeInt === 32)     return "end"             // END/FINAL
    if (typeInt === 64)     return "endStartRepeat"  // END_START_REPEAT
    if (typeInt === 128)    return "dotted"          // DOTTED
    if (typeInt === 256)    return "reverseEnd"      // REVERSE_END
    return "type=" + typeInt
}

// Convert a (measure, beat, beatFraction) musical address to an integer tick.
// `beat` is 1-based. `beatFraction` is a string like "0", "1/2", "1/4", "1/3"
// representing the sub-beat offset. Returns -1 if the measure is not found.
//
// Loop terminator is pure tick arithmetic — `seg.tick < measureEndTick`. We
// deliberately do NOT compare segment proxies for identity ("seg.parent === m"
// or similar): in QML non-library JS, two proxy wrappers around the same
// underlying C++ object obtained via different access paths are NOT === equal,
// so an identity-based guard can exit on the first iteration and silently
// return -1 for every valid position.
//
// Ticks-per-beat is derived from the time signature denominator at the start
// of the measure (curScore.division ticks/quarter, beat = whole / denominator).
//
// Returns the exact-match ChordRest segment tick when one exists at the
// requested position. Falls back to the nearest ChordRest segment within
// ticksPerBeat/2 of the computed target — handles small rounding mismatches
// (e.g. beatFraction "1/3" vs actual triplet division) and the common case
// where a long note covers a later beat with no segment at the beat boundary.
// Returns the raw computed tick (no nearby ChordRest) when nothing is close
// enough — callers will then see c.element === null and error appropriately.
function _posToTick(measureNo, beat, beatFraction) {
    var m = _findMeasure(measureNo)
    if (!m) return -1
    var mTick = _getTickInt(m.firstSegment.tick)

    // Measure end tick — preferred path m.ticks (Fraction).ticks, with fallback
    // to nextMeasure.firstSegment.tick or lastSegment.tick+1. Used as the
    // hard upper bound for segment walks below.
    var measureEndTick = -1
    try {
        if (m.ticks && typeof m.ticks.ticks === "number" && m.ticks.ticks > 0) {
            measureEndTick = mTick + m.ticks.ticks
        }
    } catch(e) {}
    if (measureEndTick <= mTick) {
        try {
            var nm = m.nextMeasure
            if (nm && nm.firstSegment) measureEndTick = _getTickInt(nm.firstSegment.tick)
            else if (m.lastSegment)    measureEndTick = _getTickInt(m.lastSegment.tick) + 1
        } catch(e) {}
    }
    if (measureEndTick <= mTick) measureEndTick = mTick + 1920   // emergency: 4/4 @ 480 tpq

    // Detect time-signature denominator for this measure. Walk segments via
    // tick-bound guard so we cannot wander past the measure boundary even if
    // nextInMeasure behaves unexpectedly. SegmentType::TimeSig = 0x20 (32).
    var tsDen = 4
    var seg = m.firstSegment
    while (seg && _getTickInt(seg.tick) < measureEndTick) {
        if (seg.segmentType & 32) {
            try {
                var tsEl = seg.elementAt(0)
                if (tsEl && tsEl.denominator) tsDen = tsEl.denominator
            } catch(e) {}
            break
        }
        seg = seg.nextInMeasure ? seg.nextInMeasure : null
    }

    var tpq = 480
    try {
        var sc = _score()
        if (sc && typeof sc.division === "number" && sc.division > 0) tpq = sc.division
    } catch(e) {}
    var ticksPerBeat = Math.floor(tpq * 4 / tsDen)
    var offset = ((typeof beat === "number" ? beat : 1) - 1) * ticksPerBeat
    var frac = beatFraction || "0"
    if (frac !== "0") {
        var parts = ("" + frac).split("/")
        if (parts.length === 2) {
            var num = parseInt(parts[0], 10)
            var den = parseInt(parts[1], 10)
            if (den > 0) offset += Math.floor(ticksPerBeat * num / den)
        }
    }
    var targetTick = mTick + offset

    // Walk ChordRest segments within this measure; prefer exact match, else
    // return the nearest one within half a beat. SegmentType::ChordRest =
    // 0x2000 (8192). Loop guard is pure tick arithmetic — seg must satisfy
    // mTick <= seg.tick < measureEndTick.
    var bestTick = -1
    var bestDelta = Math.floor(ticksPerBeat / 2) + 1
    var seg2 = m.firstSegment
    while (seg2 && _getTickInt(seg2.tick) < measureEndTick) {
        if (seg2.segmentType & 8192) {
            var segTick = _getTickInt(seg2.tick)
            if (segTick === targetTick) return targetTick
            var d = segTick > targetTick ? segTick - targetTick : targetTick - segTick
            if (d < bestDelta) { bestDelta = d; bestTick = segTick }
        }
        seg2 = seg2.nextInMeasure ? seg2.nextInMeasure : null
    }
    if (bestTick >= 0) return bestTick
    return targetTick
}

// ── Public reads ──────────────────────────────────────────────────────────

// Top-level score metadata. Matches ScoreInfo in infomodel_score.md.
function getScoreInfo() {
    var s = _score()
    if (!s) return { error: "No score open" }

    try {
        var info = {
            title:                  s.title    || "",
            composer:               s.composer || "",
            lyricist:               s.lyricist || null,
            copyright:              null,
            subtitle:               null,
            measureCount:           s.nmeasures,
            durationSeconds:        s.duration,
            parts:                  [],
            initialKeySignature:    _keysigToString(s.keysig),
            initialTimeSignature:   null,
            initialTempo:           null
        }
        try { info.copyright = s.metaTag("copyright") || null } catch(e) {}
        try { info.subtitle  = s.metaTag("subtitle")  || null } catch(e) {}

        var parts = s.parts
        if (parts) {
            var partsList = []
            // Precompute: staffNameMap[globalStaffIndex] = longName (0-based index, so staff 1 → index 0)
            var staffNameMap = []
            for (var pi = 0; pi < parts.length; pi++) {
                var pp    = parts[pi]
                var lName = pp.longName || pp.partName || ""
                var nStv  = Math.floor((pp.endTrack - pp.startTrack) / 4)
                for (var si = 0; si < nStv; si++) staffNameMap.push(lName)
                partsList.push({
                    longName:   lName,
                    shortName:  pp.shortName || "",
                    staves:     nStv,
                    firstStaff: Math.floor(pp.startTrack / 4) + 1, // 1-based global
                    visible:    (pp.show !== false)
                })
            }
            info.parts = partsList
        }

        // Initial time signature: read from the first staff at tick 0.
        try {
            if (s.nstaves > 0 && s.firstMeasure) {
                var st0 = s.staves && s.staves.length > 0 ? s.staves[0] : null
                if (st0 && s.firstMeasure.tick) {
                    var ts = st0.timeSig(s.firstMeasure.tick)
                    if (ts && ts.timesigNominal) {
                        info.initialTimeSignature = {
                            numerator:   ts.timesigNominal.numerator,
                            denominator: ts.timesigNominal.denominator
                        }
                    }
                }
            }
        } catch(e) {}

        // Initial tempo: first TempoText in measure 1, if any.
        try {
            var t = _firstTempoInMeasure(s.firstMeasure)
            if (t) {
                info.initialTempo = {
                    bpm:  t.tempo ? Math.round(t.tempo * 60.0) : null,
                    unit: "quarter",
                    text: t.text || null
                }
            }
        } catch(e) {}

        return info
    } catch(e) {
        return { error: "getScoreInfo failed: " + e }
    }
}

// Per-measure structural snapshot, optionally limited to a 1-based measure range.
// Returns an array of { number, keySignature, timeSignature, tempo, rehearsalMark,
// repeatStart, repeatEnd, jumps[], markers[] }. Repeat/jump/marker fields are
// omitted when absent.
function getStructure(startMeasure, endMeasure) {
    var s = _score()
    if (!s) return { error: "No score open" }

    try {
        var lo = (typeof startMeasure === "number" && startMeasure >= 1) ? startMeasure : 1
        var hi = (typeof endMeasure   === "number" && endMeasure   >= 1) ? endMeasure   : s.nmeasures
        if (hi < lo) { var tmp = lo; lo = hi; hi = tmp }

        var st0 = s.staves && s.staves.length > 0 ? s.staves[0] : null
        var JUMP_TYPE   = (api.engraving.Element && api.engraving.Element.JUMP   !== undefined) ? api.engraving.Element.JUMP   : -1
        var MARKER_TYPE = (api.engraving.Element && api.engraving.Element.MARKER !== undefined) ? api.engraving.Element.MARKER : -1
        var out = []
        var m = s.firstMeasure
        var lastKeyFifths = null
        var lastTsNum = null, lastTsDen = null

        var idx = 1
        while (m) {
            var n = idx
            if (n >= lo && n <= hi) {
                var entry = {
                    number:        n,
                    keySignature:  null,
                    timeSignature: null,
                    tempo:         null,
                    rehearsalMark: null
                }

                // Key signature at this measure (only emit when it changes).
                try {
                    if (st0 && m.tick) {
                        var k = st0.key(m.tick)
                        if (typeof k === "number" && k !== lastKeyFifths) {
                            entry.keySignature = _keysigToString(k)
                            lastKeyFifths = k
                        }
                    }
                } catch(e) {}

                // Time signature at this measure (only emit when it changes).
                try {
                    if (st0 && m.tick) {
                        var ts = st0.timeSig(m.tick)
                        if (ts && ts.timesigNominal) {
                            var num = ts.timesigNominal.numerator
                            var den = ts.timesigNominal.denominator
                            if (num !== lastTsNum || den !== lastTsDen) {
                                entry.timeSignature = { numerator: num, denominator: den }
                                lastTsNum = num; lastTsDen = den
                            }
                        }
                    }
                } catch(e) {}

                // Tempo and rehearsal mark (always emit when present).
                try {
                    var t = _firstTempoInMeasure(m)
                    if (t) {
                        entry.tempo = {
                            bpm:  t.tempo ? Math.round(t.tempo * 60.0) : null,
                            text: t.text || null
                        }
                    }
                } catch(e) {}
                try {
                    var r = _firstRehearsalMarkInMeasure(m)
                    if (r) entry.rehearsalMark = r.text || ""
                } catch(e) {}

                // Repeat barlines — Measure.repeatStart / repeatEnd are bool
                // API_PROPERTYs on MeasureBase (elements.h:1906-1908).
                try {
                    if (m.repeatStart) entry.repeatStart = true
                    if (m.repeatEnd)   entry.repeatEnd   = true
                } catch(e) {}

                // Jump / marker elements — found on Measure.elements, which is
                // the QQmlListProperty<EngravingItem> documented as containing
                // "layout breaks, jump/repeat markings etc." (elements.h:1925).
                try {
                    var els = m.elements
                    var nEls = (els && els.length !== undefined) ? els.length : 0
                    var jumpsList = []
                    var markersList = []
                    for (var ei = 0; ei < nEls; ei++) {
                        var el = els[ei]
                        if (!el) continue
                        var etype = el.type
                        if (JUMP_TYPE !== -1 && etype === JUMP_TYPE) {
                            var jEntry = {}
                            try { jEntry.text       = el.text       || "" } catch(e2) {}
                            try { jEntry.jumpTo     = el.jumpTo     || "" } catch(e2) {}
                            try { jEntry.playUntil  = el.playUntil  || "" } catch(e2) {}
                            try { jEntry.continueAt = el.continueAt || "" } catch(e2) {}
                            jumpsList.push(jEntry)
                        } else if (MARKER_TYPE !== -1 && etype === MARKER_TYPE) {
                            var mkEntry = {}
                            try { mkEntry.text  = el.text  || "" } catch(e2) {}
                            try { mkEntry.label = el.label || "" } catch(e2) {}
                            markersList.push(mkEntry)
                        }
                    }
                    if (jumpsList.length   > 0) entry.jumps   = jumpsList
                    if (markersList.length > 0) entry.markers = markersList
                } catch(e) {}

                out.push(entry)
            }
            if (n > hi) break
            idx++
            m = m.nextMeasure
        }
        return out
    } catch(e) {
        return { error: "getStructure failed: " + e }
    }
}

// Notes and rests in a 1-based measure range, optionally filtered by a global
// 1-based staff range (startStaff..endStaff, from getScoreInfo's firstStaff)
// and voice (1-based, 1..4).
// Returns { ok, notes: [...], rests: [...] } or { error }.
function getNotesInRange(startMeasure, endMeasure, startStaff, endStaff, voice) {
    var score = api.engraving.curScore
    if (!score) return { error: "No score open" }
    if (typeof startMeasure !== "number" || typeof endMeasure !== "number")
        return { error: "startMeasure and endMeasure must be numbers" }
    if (startMeasure > endMeasure)
        return { error: "startMeasure must be <= endMeasure" }

    var totalTracks = score.ntracks

    // --- Resolve track range from optional global staff numbers ---
    var trackLo = 0
    var trackHi = totalTracks - 1
    if (typeof startStaff === "number" && startStaff >= 1)
        trackLo = (startStaff - 1) * 4
    if (typeof endStaff === "number" && endStaff >= 1)
        trackHi = endStaff * 4 - 1
    if (trackLo < 0) trackLo = 0
    if (trackHi >= totalTracks) trackHi = totalTracks - 1

    // --- Voice filter: 1-based in API, 0-based internally (track % 4) ---
    var voiceFilter = -1
    if (typeof voice === "number" && voice >= 1 && voice <= 4)
        voiceFilter = voice - 1

    // --- Precompute globalStaff → instrument longName ---
    var parts = score.parts
    var staffNameMap = []   // staffNameMap[i] = longName of global staff (i+1)
    for (var pi = 0; pi < parts.length; pi++) {
        var pp    = parts[pi]
        var lName = pp.longName || pp.partName || ""
        var nStv  = Math.floor((pp.endTrack - pp.startTrack) / 4)
        for (var si = 0; si < nStv; si++) staffNameMap.push(lName)
    }

    var notes = []
    var rests = []
    // Hoist: api.engraving.Element.X rebuilds the full enum on every access on 4.7.0.
    var CHORD_TYPE = api.engraving.Element.CHORD
    var REST_TYPE  = api.engraving.Element.REST
    var m     = score.firstMeasure
    var idx   = 1
    while (m) {
        if (idx > endMeasure) break
        if (idx >= startMeasure) {
            var measureTick = _getTickInt(m.tick)
            var seg = m.firstSegment
            while (seg) {
                var segTick = _getTickInt(seg.tick)
                var beat    = _tickToBeat(segTick, measureTick)
                for (var track = trackLo; track <= trackHi; track++) {
                    if (voiceFilter >= 0 && (track % 4) !== voiceFilter) continue
                    var el = seg.elementAt(track)
                    if (!el) continue
                    var isChord = (el.type === CHORD_TYPE)
                    var isRest  = (el.type === REST_TYPE)
                    if (!isChord && !isRest) continue

                    var globalStaff  = Math.floor(track / 4) + 1
                    var instrName    = staffNameMap[globalStaff - 1] || ""
                    var location = {
                        measure:    idx,
                        beat:       beat,
                        instrument: instrName,
                        staff:      globalStaff,
                        voice:      (track % 4) + 1
                    }

                    if (isChord) {
                        var chord    = el
                        var duration = _durationStr(chord.duration.str)
                        var isGrace  = false
                        try { isGrace = (chord.noteType !== api.engraving.NoteType.NORMAL) } catch(e) {}
                        var artList  = []
                        try {
                            var arts = chord.articulations
                            for (var ai = 0; ai < arts.length; ai++) {
                                try { var aName = arts[ai].subtypeName(); if (aName) artList.push(aName) } catch(e2) {}
                            }
                        } catch(e) {}
                        var noteArr = chord.notes
                        for (var ni = 0; ni < noteArr.length; ni++) {
                            var note = noteArr[ni]
                            var t    = note.tpc
                            var acc  = null
                            if      (t >= 0  && t <  6) acc = "doubleFlat"
                            else if (t >= 6  && t < 13) acc = "flat"
                            else if (t >= 20 && t < 27) acc = "sharp"
                            else if (t >= 27 && t <= 33) acc = "doubleSharp"
                            notes.push({
                                noteName:      _tpcToNoteName(note.tpc, note.pitch),
                                duration:      duration,
                                location:      location,
                                tiedForward:   !!note.tieForward,
                                tiedBack:      !!note.tieBack,
                                grace:         isGrace,
                                articulations: artList,
                                accidental:    acc,
                                visible:       (note.visible !== false)
                            })
                        }
                    } else {
                        var rest = el
                        var isFullMeasure = false
                        try { isFullMeasure = !!rest.isFullMeasureRest } catch(e) {}
                        rests.push({
                            duration:      _durationStr(rest.duration.str),
                            location:      location,
                            isFullMeasure: isFullMeasure,
                            visible:       (rest.visible !== false)
                        })
                    }
                }
                seg = seg.nextInMeasure
            }
        }
        idx++
        m = m.nextMeasure
    }
    return { ok: true, notes: notes, rests: rests }
}

// Chord symbols (harmony annotations) in a 1-based measure range.
function getHarmonyInRange(startMeasure, endMeasure) {
    var score = _score()
    if (!score) return { error: "No score open" }
    if (typeof startMeasure !== "number" || typeof endMeasure !== "number")
        return { error: "startMeasure and endMeasure must be numbers" }

    var result = []
    // Hoist: api.engraving.Element.X rebuilds the full enum on every access on 4.7.0.
    var HARMONY = api.engraving.Element.HARMONY

    var m   = score.firstMeasure
    var idx = 1
    while (m) {
        if (idx > endMeasure) break
        if (idx >= startMeasure) {
            var measureTick = _getTickInt(m.tick)
            var seg = m.firstSegment
            while (seg) {
                var anns = seg.annotations
                if (anns) {
                    for (var ai = 0; ai < anns.length; ai++) {
                        var el = anns[ai]
                        if (el.type !== HARMONY) continue
                        var text = ""
                        try { text = el.plainText || el.text || "" } catch(e) {
                            try { text = el.text || "" } catch(e2) {}
                        }
                        if (!text) continue
                        var segTick = _getTickInt(seg.tick)
                        result.push({
                            text:    text,
                            measure: idx,
                            beat:    _tickToBeat(segTick, measureTick),
                            visible: (el.visible !== false)
                        })
                    }
                }
                seg = seg.nextInMeasure
            }
        }
        idx++
        m = m.nextMeasure
    }

    return { ok: true, harmonies: result }
}

// Lyrics in a 1-based measure range, optionally filtered by a global 1-based
// staff range (startStaff..endStaff, from getScoreInfo's firstStaff).
// Verse number derived from index in chord.lyrics[] (verse 1 = index 0) since
// lyrics.no is not a Q_PROPERTY in the apiv1 wrapper.
function getLyricsInRange(startMeasure, endMeasure, startStaff, endStaff) {
    var score = api.engraving.curScore
    if (!score) return { error: "No score open" }
    if (typeof startMeasure !== "number" || typeof endMeasure !== "number")
        return { error: "startMeasure and endMeasure must be numbers" }

    var totalTracks = score.ntracks
    var trackLo = 0
    var trackHi = totalTracks - 1
    if (typeof startStaff === "number" && startStaff >= 1)
        trackLo = (startStaff - 1) * 4
    if (typeof endStaff === "number" && endStaff >= 1)
        trackHi = endStaff * 4 - 1
    if (trackLo < 0) trackLo = 0
    if (trackHi >= totalTracks) trackHi = totalTracks - 1

    // Precompute globalStaff → instrument longName
    var parts = score.parts
    var staffNameMap = []
    for (var pi = 0; pi < parts.length; pi++) {
        var pp    = parts[pi]
        var lName = pp.longName || pp.partName || ""
        var nStv  = Math.floor((pp.endTrack - pp.startTrack) / 4)
        for (var si = 0; si < nStv; si++) staffNameMap.push(lName)
    }

    var SYLLABIC_STR = ["single", "begin", "end", "middle"]
    var result  = []
    // Hoist: api.engraving.Element.X rebuilds the full enum on every access on 4.7.0.
    var CHORD_TYPE = api.engraving.Element.CHORD
    var REST_TYPE  = api.engraving.Element.REST
    var m       = score.firstMeasure
    var idx     = 1
    while (m) {
        if (idx > endMeasure) break
        if (idx >= startMeasure) {
            var measureTick = _getTickInt(m.tick)
            var seg = m.firstSegment
            while (seg) {
                var segTick = _getTickInt(seg.tick)
                var beat    = _tickToBeat(segTick, measureTick)
                // Iterate voice-1 tracks only (trackLo is always 4-aligned)
                for (var track = trackLo; track <= trackHi; track += 4) {
                    var el = seg.elementAt(track)
                    if (!el) continue
                    if (el.type !== CHORD_TYPE &&
                        el.type !== REST_TYPE) continue
                    var lyricsList
                    try { lyricsList = el.lyrics } catch(e) { continue }
                    if (!lyricsList || lyricsList.length === 0) continue
                    var globalStaff = Math.floor(track / 4) + 1
                    var instrName   = staffNameMap[globalStaff - 1] || ""
                    for (var li = 0; li < lyricsList.length; li++) {
                        var lyr  = lyricsList[li]
                        var text = ""
                        try { text = lyr.plainText || lyr.text || "" } catch(e) {
                            try { text = lyr.text || "" } catch(e2) {}
                        }
                        var syllabic = "single"
                        try { syllabic = SYLLABIC_STR[lyr.syllabic] || "single" } catch(e) {}
                        result.push({
                            text:     text,
                            syllabic: syllabic,
                            verse:    li + 1,
                            location: {
                                measure:    idx,
                                beat:       beat,
                                instrument: instrName,
                                staff:      globalStaff,
                                voice:      1
                            },
                            visible:  (lyr.visible !== false)
                        })
                    }
                }
                seg = seg.nextInMeasure
            }
        }
        idx++
        m = m.nextMeasure
    }
    return { ok: true, lyrics: result }
}

// ── Public writes ─────────────────────────────────────────────────────────

// Add a rehearsal mark at the start of the given 1-based measure.
// Uses the confirmed add-first-then-set pattern from runtime_probe.md.
function addRehearsalMark(measureNo, text) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof measureNo !== "number" || measureNo < 1)
        return { error: "Invalid measure number: " + measureNo }
    if (typeof text !== "string" || text.length === 0)
        return { error: "Rehearsal mark text must be a non-empty string" }

    var m = _findMeasureByNumber(s, measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found (score has " + s.nmeasures + " measures)" }

    try {
        s.startCmd("add rehearsal mark")
        var c = s.newCursor()
        c.track = 0
        // m.tick is a Fraction; use _getTickInt helper. Fall back to first
        // segment's tick if m.tick is somehow neither int nor Fraction.
        var tickInt = _getTickInt(m.tick)
        if (tickInt === 0 && m.tick === undefined) {
            try { tickInt = _getTickInt(m.firstSegment.tick) } catch(e) {}
        }
        c.rewindToTick(tickInt)

        var rm = api.engraving.newElement(_EL.REHEARSAL_MARK)
        c.add(rm)          // real-parent FIRST
        rm.text = text     // THEN set properties
        s.endCmd()
        return { ok: true, measure: measureNo, text: text }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addRehearsalMark failed: " + e }
    }
}

// Add a dynamic marking at a (measure, beat) position on a specific staff.
// Voice is hard-coded to 1 (track = (staff-1)*4) — dynamics attach to the
// staff, not a particular voice.
function addDynamic(measureNo, beat, beatFraction, staff, dynamic) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof measureNo !== "number" || measureNo < 1)
        return { error: "Invalid measure number: " + measureNo }
    if (typeof staff !== "number" || staff < 1)
        return { error: "Invalid staff number: " + staff }

    var dynamicMap = {
        ppp: 4, pp: 5, p: 6, mp: 7, mf: 8, f: 9, ff: 10, fff: 11,
        fp: 15, sf: 17, sfz: 18, sfp: 23, rfz: 25, fz: 27
    }
    // SMuFL-marked-up glyph text for each dynamic, sourced from
    // src/engraving/dom/dynamic.cpp DYN_LIST. We need this because the
    // enum overload Dynamic::setDynamicType(DynamicType) (dynamic.cpp:230 vs.
    // 238) sets ONLY the enum — the string overload also calls setXmlText(),
    // and without text the element is added but renders no glyph. v0.5.1
    // smoke test 16/17 reported this: undo entry + layout space + no glyph.
    // We set text AFTER c.add(d) (the dynamicType-determined variant must be
    // committed first, same constraint as the existing set-before-add note).
    var dynamicTextMap = {
        ppp: "<sym>dynamicPiano</sym><sym>dynamicPiano</sym><sym>dynamicPiano</sym>",
        pp:  "<sym>dynamicPiano</sym><sym>dynamicPiano</sym>",
        p:   "<sym>dynamicPiano</sym>",
        mp:  "<sym>dynamicMezzo</sym><sym>dynamicPiano</sym>",
        mf:  "<sym>dynamicMezzo</sym><sym>dynamicForte</sym>",
        f:   "<sym>dynamicForte</sym>",
        ff:  "<sym>dynamicForte</sym><sym>dynamicForte</sym>",
        fff: "<sym>dynamicForte</sym><sym>dynamicForte</sym><sym>dynamicForte</sym>",
        fp:  "<sym>dynamicForte</sym><sym>dynamicPiano</sym>",
        sf:  "<sym>dynamicSforzando</sym><sym>dynamicForte</sym>",
        sfz: "<sym>dynamicSforzando</sym><sym>dynamicForte</sym><sym>dynamicZ</sym>",
        sfp: "<sym>dynamicSforzando</sym><sym>dynamicForte</sym><sym>dynamicPiano</sym>",
        rfz: "<sym>dynamicRinforzando</sym><sym>dynamicForte</sym><sym>dynamicZ</sym>",
        fz:  "<sym>dynamicForte</sym><sym>dynamicZ</sym>"
    }
    // Normalise case — LLM occasionally sends "F" or "MP". Reject unknown
    // values rather than silently substituting (a silent fallback rendered
    // the wrong glyph and looked invisible to the user in earlier smoke tests).
    var dynLc = (typeof dynamic === "string") ? dynamic.toLowerCase() : ""
    var dynType = dynamicMap[dynLc]
    if (dynType === undefined) {
        return {
            error: "Unknown dynamic '" + dynamic + "'. Valid: " + Object.keys(dynamicMap).join(", "),
            _debug: { fn: "addDynamic", input: dynamic, normalized: dynLc }
        }
    }

    var tick = _posToTick(measureNo, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measureNo + " not found",
        _debug: { fn: "addDynamic", measureNo: measureNo, beat: beat, beatFraction: beatFraction || "0", staff: staff, tick: tick }
    }

    // Cursor must land on a ChordRest before c.add(d) — dynamics attach to a
    // ChordRest segment. If c.element is null or wrong type, c.add() either
    // silently no-ops or attaches to a non-ChordRest segment and renders
    // invisibly while still showing "Add dynamic" in the undo stack — the
    // worst possible failure mode for the user. Guard BEFORE startCmd so a
    // bad position never produces a phantom undo entry.
    var probe = s.newCursor()
    probe.track = (staff - 1) * 4
    probe.rewindToTick(tick)
    var probeEl = probe.element
    var CHORD = api.engraving.Element.CHORD
    var REST  = api.engraving.Element.REST
    if (!probeEl || (probeEl.type !== CHORD && probeEl.type !== REST)) {
        return {
            error: "No chord/rest at measure " + measureNo + " beat " + beat + " staff " + staff,
            _debug: { fn: "addDynamic", tick: tick, elementType: probeEl ? probeEl.type : null, CHORD: CHORD, REST: REST }
        }
    }

    // Hoist element type constant — api.engraving.Element.X rebuilds the full
    // enum on every access on 4.7.0; hoist before any call that uses it.
    var DYNAMIC = api.engraving.Element.DYNAMIC

    // Idempotency: if a dynamic already exists at this tick on this staff,
    // update it in-place instead of stacking a duplicate.
    // Walk BEFORE startCmd (and before any cursor) — no rewindToTick yet,
    // so no GC invalidation risk.
    var existingDyn = _findAnnotationAtTickAndStaff(s, measureNo, tick, staff - 1, DYNAMIC)
    if (existingDyn) {
        try {
            s.startCmd("update dynamic")
            existingDyn.dynamicType = dynType
            var glyphTextUpd = dynamicTextMap[dynLc]
            if (glyphTextUpd) existingDyn.text = glyphTextUpd
            s.endCmd()
            return { ok: true, measure: measureNo, beat: beat, dynamic: dynLc, updated: "in-place" }
        } catch(e) {
            try { s.endCmd(true) } catch(ee) {}
            return { error: "updateDynamic failed: " + e }
        }
    }

    try {
        s.startCmd("add dynamic")
        var c = s.newCursor()
        c.track = (staff - 1) * 4
        c.rewindToTick(tick)
        var d = api.engraving.newElement(_EL.DYNAMIC)
        // EXCEPTION to the add-first-then-set pattern: dynamicType determines
        // which element variant the engraving layer commits, so it must be
        // set BEFORE c.add(). Setting it after produces a hairpin pair instead
        // of the requested glyph (and only the first call works).
        d.dynamicType = dynType
        c.add(d)
        // Set the visible glyph text AFTER add. Required because the enum
        // overload Dynamic::setDynamicType(DynamicType) does NOT populate
        // xmlText — without text the element renders as an invisible spacer.
        // See dynamicTextMap above for the SMuFL mapping.
        var glyphText = dynamicTextMap[dynLc]
        if (glyphText) d.text = glyphText
        s.endCmd()
        return { ok: true, measure: measureNo, beat: beat, dynamic: dynLc, _debug: { dynType: dynType, tick: tick } }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addDynamic failed: " + e, _debug: { fn: "addDynamic", dynType: dynType, tick: tick } }
    }
}

// Add a tempo marking at the start of a measure. Sets both displayed text
// and playback tempo (quarters-per-second). tempoFollowText=false so the
// numeric value drives playback regardless of the text.
function addTempoMark(measureNo, bpm, unit, text) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof measureNo !== "number" || measureNo < 1)
        return { error: "Invalid measure number: " + measureNo }
    var hasBpm = (typeof bpm === "number" && bpm > 0)
    var qps, displayText
    if (hasBpm) {
        var unitLower = (unit || "quarter").toLowerCase()
        qps = bpm / 60.0
        if      (unitLower === "half")            qps = bpm / 30.0
        else if (unitLower === "eighth")          qps = bpm / 120.0
        else if (unitLower === "dotted quarter")  qps = bpm * 1.5 / 60.0
        else if (unitLower === "dotted half")     qps = bpm * 1.5 / 30.0

        var noteSymbol = "♩"
        if      (unitLower === "half")            noteSymbol = "𝅝"
        else if (unitLower === "eighth")          noteSymbol = "♪"
        else if (unitLower === "dotted quarter")  noteSymbol = "♩."
        else if (unitLower === "dotted half")     noteSymbol = "𝅝."

        displayText = (text ? text + " " : "") + noteSymbol + " = " + bpm
    } else {
        // Text-only tempo word (e.g. "Allegro") — no metronome mark.
        // tt.tempo is a fallback QPS; tempoFollowText=true lets MuseScore
        // parse playback speed from the Italian word where possible.
        if (!text) return { error: "Either bpm or text is required for a tempo mark" }
        qps = 2.0   // 120 BPM fallback
        displayText = text
    }

    // Anchor to the first ChordRest segment of the measure. Anchoring to the
    // raw m.firstSegment.tick lands the cursor on a TimeSig or KeySig segment
    // for measures that start with one (always true for measure 1, and again
    // wherever a sig change occurs). cursor.add(TEMPO_TEXT) on a non-ChordRest
    // segment shows "Add tempo mark" in the undo stack but renders invisibly
    // — the same failure mode that bit addSystemText before fixes1.
    var mTick = _posToTick(measureNo, 1, "0")
    if (mTick < 0) return {
        error: "Measure " + measureNo + " not found or has no chord/rest segment",
        _debug: { fn: "addTempoMark", measureNo: measureNo, tick: mTick }
    }

    // Duplicate guard: a tempo mark already exists in this measure. Adding
    // another stacks them at the same anchor, with the second silently
    // overriding playback (v0.5.1 smoke test 20 observation). Return ok with
    // a note rather than corrupting the score.
    var measure = _findMeasure(measureNo)
    if (measure && _firstTempoInMeasure(measure)) {
        return {
            ok: true,
            measure: measureNo,
            note: "tempo mark already exists at measure " + measureNo + " — no change made"
        }
    }

    try {
        s.startCmd("add tempo")
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(mTick)
        var tt = api.engraving.newElement(_EL.TEMPO_TEXT)
        c.add(tt)                    // real-parent FIRST
        tt.text = displayText        // THEN set properties
        tt.tempo = qps               // playback fallback if text parse fails
        // tempoFollowText=true matches the toolbar default ("Follow written
        // tempo"). Smoke test v0.5.1 test 20 flagged the previous Override
        // setting as a behavioural mismatch with user-added marks. With
        // follow=true, MuseScore re-parses displayText on edit and keeps
        // playback in sync with the visible mark.
        tt.tempoFollowText = true
        s.endCmd()
        return { ok: true, measure: measureNo, bpm: hasBpm ? bpm : null, tempo: qps, text: displayText }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addTempoMark failed: " + e }
    }
}

// Staff text at a (measure, beat) position, voice 1, single staff.
//
// `textType` is optional: "staff" (default) → STAFF_TEXT, "expression" →
// EXPRESSION element. EXPRESSION uses italic typography and is the correct
// element for performance expressions like dolce, espressivo, cantabile etc.
// If the EXPRESSION element type is not exposed in this build the function
// falls back to STAFF_TEXT and notes it in the response.
function addStaffText(measureNo, beat, beatFraction, staff, text, textType) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof staff !== "number" || staff < 1)
        return { error: "Invalid staff number: " + staff }
    if (typeof text !== "string" || text.length === 0)
        return { error: "Staff text must be a non-empty string" }

    var tick = _posToTick(measureNo, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measureNo + " not found",
        _debug: { fn: "addStaffText", measureNo: measureNo, beat: beat, beatFraction: beatFraction || "0", staff: staff, tick: tick }
    }

    var elemKind = "staff"
    var elemType = _EL.STAFF_TEXT
    var fellBack = false
    if (textType === "expression") {
        if (api.engraving.Element.EXPRESSION !== undefined) {
            elemType = _EL.EXPRESSION
            elemKind = "expression"
        } else {
            fellBack = true   // EXPRESSION not exposed; keep STAFF_TEXT
        }
    }

    try {
        s.startCmd("add " + elemKind + " text")
        var c = s.newCursor()
        c.track = (staff - 1) * 4
        c.rewindToTick(tick)
        var st = api.engraving.newElement(elemType)
        c.add(st)
        st.text = text
        s.endCmd()
        var res = { ok: true, measure: measureNo, beat: beat, staff: staff, textType: elemKind }
        if (fellBack) res.note = "EXPRESSION element type not exposed in this build; rendered as staff text."
        return res
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addStaffText failed: " + e }
    }
}

// System text at the start of a measure, track 0 (applies to all staves).
// Anchors to the first ChordRest segment of the measure — anchoring to
// `m.firstSegment.tick` lands the cursor on a TimeSig/KeySig segment when
// the measure begins with one, and cursor.add(SYSTEM_TEXT) silently fails
// on a non-ChordRest segment.
function addSystemText(measureNo, text) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof text !== "string" || text.length === 0)
        return { error: "System text must be a non-empty string" }

    var mTick = _posToTick(measureNo, 1, "0")
    if (mTick < 0) return {
        error: "Measure " + measureNo + " not found or has no chord/rest segment",
        _debug: { fn: "addSystemText", measureNo: measureNo, tick: mTick }
    }

    try {
        s.startCmd("add system text")
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(mTick)
        var sysT = api.engraving.newElement(_EL.SYSTEM_TEXT)
        c.add(sysT)
        sysT.text = text
        s.endCmd()
        return { ok: true, measure: measureNo }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addSystemText failed: " + e }
    }
}

// Chord symbol (Harmony annotation) at a (measure, beat) position on a staff.
function addHarmony(measureNo, beat, beatFraction, staff, text) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof staff !== "number" || staff < 1)
        return { error: "Invalid staff number: " + staff }
    if (typeof text !== "string" || text.length === 0)
        return { error: "Chord symbol text must be a non-empty string" }

    var tick = _posToTick(measureNo, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measureNo + " not found",
        _debug: { fn: "addHarmony", measureNo: measureNo, beat: beat, beatFraction: beatFraction || "0", staff: staff, tick: tick }
    }

    try {
        s.startCmd("add chord symbol")
        var c = s.newCursor()
        c.track = (staff - 1) * 4
        c.rewindToTick(tick)
        var h = api.engraving.newElement(_EL.HARMONY)
        c.add(h)
        h.text = text
        s.endCmd()
        return { ok: true, measure: measureNo, beat: beat, text: text }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addHarmony failed: " + e }
    }
}

// Count spanners on the given staff (0-based) whose start tick lies within
// [startTick, endTick]. Used as a before/after probe to detect silent no-ops
// in slur/ottava cmd handlers — the cmd returns no error when its selection
// preconditions aren't met (e.g. selection has < 2 distinct chord-rests for a
// slur), and the only way to know nothing happened is to count.
function _countSpannersAt(score, startTick, endTick, staff0) {
    try {
        var sps = score.spanners
        if (!sps || sps.length === undefined) return 0
        var n = 0
        for (var i = 0; i < sps.length; i++) {
            var sp = sps[i]
            if (!sp) continue
            var spTick = -1, spStaff = -1
            try { spTick  = _getTickInt(sp.spannerTick) } catch (e) {}
            try { spStaff = sp.staffIdx } catch (e) {}
            if (spTick < startTick || spTick > endTick) continue
            if (staff0 >= 0 && spStaff !== staff0) continue
            n++
        }
        return n
    } catch (e) { return 0 }
}

// Helper: range-select + cmd() write — shared by hairpin, slur, ottava.
//
// `verifyKind` is "spanner" for slur/ottava — we count score-level spanners on
// the target staff before and after, and return an error if the count didn't
// increase (cmd silently no-op'd). Hairpin doesn't need verification: the cmd
// handler has a `noteOrRestSelected` guard that produces no entry only when
// the selection is genuinely empty, and our probe ensures it isn't.
function _rangeCmdWrite(cmdLabel, cmdStr, verifyKind,
                        startMeasure, startBeat, startBeatFraction, startStaff,
                        endMeasure,   endBeat,   endBeatFraction,   endStaff) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof startStaff !== "number" || startStaff < 1)
        return { error: "Invalid startStaff: " + startStaff }
    // Defense in depth — Dispatch.js already defaults endStaff to startStaff
    // when the LLM omits it, but a missing/invalid value here would silently
    // propagate as undefined into selectRange and drop the cmd.
    if (typeof endStaff !== "number" || endStaff < 1) endStaff = startStaff

    var startTick = _posToTick(startMeasure, startBeat, startBeatFraction)
    if (startTick < 0) return {
        error: "Start measure " + startMeasure + " not found",
        _debug: { fn: cmdLabel, side: "start", measureNo: startMeasure, beat: startBeat, beatFraction: startBeatFraction || "0", staff: startStaff, tick: startTick }
    }
    var endTick   = _posToTick(endMeasure,   endBeat,   endBeatFraction)
    if (endTick < 0)   return {
        error: "End measure " + endMeasure + " not found",
        _debug: { fn: cmdLabel, side: "end", measureNo: endMeasure, beat: endBeat, beatFraction: endBeatFraction || "0", staff: endStaff, tick: endTick }
    }

    var s0 = startStaff - 1   // inclusive, 0-based
    var s1 = endStaff         // exclusive, 0-based

    // KNOWN BROKEN — MuseScore upstream bug #24673.
    // api.engraving.cmd("add-slur") / "add-8va" / "add-8vb" are silently
    // discarded from form-extension context. NotationActionController rejects
    // them via isNotationPage() because the extension dialog has UI focus
    // (resolveCurrentUiContext returns UiCtxUnknown). Confirmed on MS 4.7 and
    // master as of May 2026. Fix is tracked at:
    // https://github.com/musescore/MuseScore/issues/24673
    if (cmdStr === "add-slur" || cmdStr === "add-8va" || cmdStr === "add-8vb") {
        return {
            error: cmdLabel + " is not available due to a known MuseScore bug that affects form-extensions. "
                   + "See https://github.com/musescore/MuseScore/issues/24673 — upvoting the issue helps prioritize a fix."
        }
    }

    // Hairpin and other range cmds: selectRange approach.
    var selEndTick = endTick + 1

    var before = (verifyKind === "spanner") ? _countSpannersAt(s, startTick, endTick, s0) : 0

    // NO startCmd/endCmd here: api.engraving.cmd() handlers run
    // prepareChanges/commitChanges internally, and those become no-ops while
    // the undo stack is locked by an outer startCmd — the cmd silently drops.
    try {
        s.selection.selectRange(startTick, selEndTick, s0, s1)
        api.engraving.cmd(cmdStr)
        if (verifyKind === "spanner") {
            var after = _countSpannersAt(s, startTick, endTick, s0)
            if (after <= before) {
                return {
                    error: cmdLabel + " had no effect — selection may contain too few notes or no compatible target",
                    _debug: { fn: cmdLabel, cmd: cmdStr, startTick: startTick, selEndTick: selEndTick, staff0: s0, before: before, after: after }
                }
            }
        }
        return { ok: true }
    } catch(e) {
        return { error: cmdLabel + " failed: " + e }
    }
}

// Crescendo or decrescendo hairpin spanning two positions on the same staff.
function addHairpin(startMeasure, startBeat, startBeatFraction, startStaff,
                    endMeasure, endBeat, endBeatFraction, endStaff, type) {
    var cmdStr = (type === "decresc") ? "add-hairpin-reverse" : "add-hairpin"
    var res = _rangeCmdWrite("add hairpin", cmdStr, "spanner",
                             startMeasure, startBeat, startBeatFraction, startStaff,
                             endMeasure, endBeat, endBeatFraction, endStaff)
    if (res.ok) res.type = (type === "decresc") ? "decresc" : "cresc"
    return res
}

// Slur spanning two positions on the same staff.
function addSlur(startMeasure, startBeat, startBeatFraction, startStaff,
                 endMeasure, endBeat, endBeatFraction, endStaff) {
    return _rangeCmdWrite("add slur", "add-slur", "spanner",
                          startMeasure, startBeat, startBeatFraction, startStaff,
                          endMeasure, endBeat, endBeatFraction, endStaff)
}

// Ottava line (8va or 8vb) spanning two positions on the same staff.
function addOttava(startMeasure, startBeat, startBeatFraction, startStaff,
                   endMeasure, endBeat, endBeatFraction, endStaff, type) {
    var cmdStr = (type === "8vb") ? "add-8vb" : "add-8va"
    var res = _rangeCmdWrite("add ottava", cmdStr, "spanner",
                             startMeasure, startBeat, startBeatFraction, startStaff,
                             endMeasure, endBeat, endBeatFraction, endStaff)
    if (res.ok) res.type = (type === "8vb") ? "8vb" : "8va"
    return res
}

// Insert `count` empty measures after `afterMeasure`. Pass afterMeasure=0 to
// insert before measure 1.
//
// cmd("insert-measure") routes to NotationActionController which requires
// hasSelection — a cursor position alone is NOT a selection. Earlier code
// positioned a cursor and called the cmd, which silently no-op'd. The fix
// selectRange's the target measure (the measure we want to insert BEFORE),
// then fires the cmd. Each iteration re-finds the target by 1-based number;
// after each insert, the just-inserted empty measure occupies that number
// and the next iteration inserts before IT.
function insertMeasures(afterMeasure, count) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof afterMeasure !== "number" || afterMeasure < 0)
        return { error: "Invalid afterMeasure: " + afterMeasure }
    if (typeof count !== "number" || count < 1)
        return { error: "count must be >= 1" }

    var targetNo = afterMeasure + 1   // 1-based number of measure to insert BEFORE

    var before = s.nmeasures
    try {
        for (var i = 0; i < count; i++) {
            var target = _findMeasure(targetNo)
            if (!target) {
                // No measure at position N — fall through to append.
                api.engraving.cmd("append-measure")
            } else {
                var st = _getTickInt(target.firstSegment.tick)
                var et = target.nextMeasure
                    ? _getTickInt(target.nextMeasure.firstSegment.tick)
                    : _getTickInt(target.lastSegment.tick) + 1
                s.selection.selectRange(st, et, 0, s.nstaves)
                api.engraving.cmd("insert-measure")
            }
        }
    } catch(e) {
        return { error: "insertMeasures failed: " + e }
    }
    var after = s.nmeasures
    if (after - before < count) {
        return {
            error: "insert_measures had no effect — this is likely caused by a known MuseScore bug that prevents certain commands from dispatching in form-extension context. "
                   + "See https://github.com/musescore/MuseScore/issues/24673",
            _debug: { fn: "insertMeasures", before: before, after: after, requested: count }
        }
    }
    return { ok: true, inserted: after - before, afterMeasure: afterMeasure }
}

// Append `count` empty measures at the end of the score.
//
// Uses cmd("append-measure") in a loop instead of curScore.appendMeasures(n).
// Reason: Score::appendMeasures creates measures with createMeasureRests=false
// (engraving/dom/score.cpp:4407-4415), which leaves the staves of the new
// measure empty — no full-measure rest is laid out, so the measure looks
// invisible in the editor. The cmd("append-measure") path goes through
// NotationActionController::addBoxes which properly populates rests.
function appendMeasures(count) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof count !== "number" || count < 1)
        return { error: "count must be >= 1" }

    // NO startCmd/endCmd — cmd owns its own undo entry. Verify against
    // s.nmeasures before/after — cmd("append-measure") will silently no-op
    // if the action dispatcher rejects it (e.g. score-locked state), and the
    // bare ok:true would otherwise mislead.
    var before = s.nmeasures
    try {
        for (var i = 0; i < count; i++) api.engraving.cmd("append-measure")
    } catch(e) {
        return { error: "appendMeasures failed: " + e }
    }
    var after = s.nmeasures
    var added = after - before
    if (added <= 0) {
        return {
            error: "append_measures had no effect — this is likely caused by a known MuseScore bug that prevents certain commands from dispatching in form-extension context. "
                   + "See https://github.com/musescore/MuseScore/issues/24673",
            _debug: { fn: "appendMeasures", before: before, after: after, requested: count }
        }
    }
    return { ok: true, appended: added }
}

// Delete one measure across all staves and shift later measures left.
function deleteMeasure(measureNo) {
    var s = _score()
    if (!s) return { error: "No score open" }

    var m = _findMeasure(measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }

    var startTick = _getTickInt(m.firstSegment.tick)
    var endTick = m.nextMeasure
        ? _getTickInt(m.nextMeasure.firstSegment.tick)
        : _getTickInt(m.lastSegment.tick) + 1

    // NO startCmd/endCmd: cmd("time-delete") owns its undo entry. Verify
    // against s.nmeasures before/after — see appendMeasures for rationale.
    var before = s.nmeasures
    try {
        s.selection.selectRange(startTick, endTick, 0, s.nstaves)
        api.engraving.cmd("time-delete")
    } catch(e) {
        return { error: "deleteMeasure failed: " + e }
    }
    var after = s.nmeasures
    if (after >= before) {
        return {
            error: "delete_measure had no effect — this is likely caused by a known MuseScore bug that prevents certain commands from dispatching in form-extension context. "
                   + "See https://github.com/musescore/MuseScore/issues/24673",
            _debug: { fn: "deleteMeasure", measureNo: measureNo, before: before, after: after, startTick: startTick, endTick: endTick }
        }
    }
    return { ok: true, deletedMeasure: measureNo }
}

// Helper for breaks: construct a LayoutBreak element directly and attach it
// to the measure via Cursor::add. The cursor's add() routes LAYOUT_BREAK to
// MeasureBase::addInternal(_segment->measure(), ...), so any segment within
// the measure works. layoutBreakType MUST be set BEFORE c.add() — the engraving
// layer uses it to determine the element's identity at insertion time (same
// constraint as Dynamic::dynamicType).
//
// Replaces the previous selectRange+cmd("section-break")/cmd("system-break")
// approach, which crashed MuseScore. Cmd strings "section-break" and
// "system-break" ARE registered (notationactioncontroller.cpp:268,272) but the
// handler path interacts badly with plugin-side startCmd/endCmd wrapping.
// Walk Measure.elements looking for an existing LayoutBreak of the given type.
// Returns true if one is already attached. Used to suppress duplicate adds —
// otherwise calling add_system_break twice on the same measure produces two
// stacked LayoutBreak elements at the same position (visible in v0.5.1 smoke
// test 14).
function _hasLayoutBreak(measure, layoutBreakType) {
    if (!measure) return false
    try {
        var els = measure.elements
        var nE = (els && els.length !== undefined) ? els.length : 0
        var LB = api.engraving.Element ? api.engraving.Element.LAYOUT_BREAK : -1
        for (var i = 0; i < nE; i++) {
            var el = els[i]
            if (!el) continue
            if (el.type !== LB) continue
            var t = -1
            try { t = el.layoutBreakType } catch (e) {}
            if (t === layoutBreakType) return true
        }
    } catch (e) {}
    return false
}

// Find a segment-resident element (stored in segment._elist[track], NOT annotations)
// at an exact tick on a given track, in segments matching segTypeMask.
// Examples: Clef (segTypeMask=0x400), KeySig (0x40), TimeSig (0x20).
// Returns the element if found, null otherwise.
//
// ALWAYS call this BEFORE c.rewindToTick(tick). Accessing m.firstSegment and
// seg.nextInMeasure creates QML wrapper objects; if called after rewindToTick,
// GC of those wrappers invalidates the cursor's internal segment pointer and
// c.add() silently no-ops.
function _findSegmentElAtTick(s, measure, tick, track, segTypeMask) {
    var m = _findMeasureByNumber(s, measure)
    if (!m) return null
    try {
        var seg = m.firstSegment
        while (seg) {
            var segTick = _getTickInt(seg.tick)
            if (segTick > tick) break
            if (segTick === tick && (seg.segmentType & segTypeMask)) {
                return seg.elementAt(track)
            }
            seg = seg.nextInMeasure ? seg.nextInMeasure : null
        }
    } catch (e) {}
    return null
}

// Find a segment annotation at an exact tick on a given 0-based staffIdx.
// Annotations include DYNAMIC, TEMPO_TEXT, STAFF_TEXT, SYSTEM_TEXT, etc.
// elType: pass a pre-hoisted api.engraving.Element.XXX value (string on 4.7.0).
// Returns the matching annotation if found, null otherwise.
//
// ALWAYS call this BEFORE c.rewindToTick(tick). Same GC invalidation risk as above.
function _findAnnotationAtTickAndStaff(s, measure, tick, staffIdx, elType) {
    var m = _findMeasureByNumber(s, measure)
    if (!m) return null
    try {
        var seg = m.firstSegment
        while (seg) {
            var segTick = _getTickInt(seg.tick)
            if (segTick > tick) break
            if (segTick === tick) {
                var ann = seg.annotations
                for (var i = 0; i < ann.length; i++) {
                    if (ann[i] && ann[i].type === elType && ann[i].staffIdx === staffIdx) return ann[i]
                }
            }
            seg = seg.nextInMeasure ? seg.nextInMeasure : null
        }
    } catch (e) {}
    return null
}

function _addLayoutBreak(cmdLabel, layoutBreakType, measureNo) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var m = _findMeasure(measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }
    var tickInt = _getTickInt(m.firstSegment.tick)

    if (_hasLayoutBreak(m, layoutBreakType)) {
        return {
            ok: true,
            measure: measureNo,
            note: cmdLabel + " already exists at measure " + measureNo + " — no change made"
        }
    }

    try {
        s.startCmd(cmdLabel)
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(tickInt)
        var lb = api.engraving.newElement(_EL.LAYOUT_BREAK)
        // Set type both BEFORE and AFTER add: empirically system break (LINE=1)
        // works either way because LINE is the constructor default, but
        // section break (SECTION=2) was silently dropped when set only BEFORE
        // — the engraving layer initialises the LayoutBreak with the default
        // LINE type at add() and only honours a post-add type assignment.
        lb.layoutBreakType = layoutBreakType
        c.add(lb)
        lb.layoutBreakType = layoutBreakType
        s.endCmd()
        return { ok: true, measure: measureNo }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: cmdLabel + " failed: " + e }
    }
}

// LayoutBreakType integer values from src/engraving/types/types.h:412
// PAGE=0, LINE=1, SECTION=2, NOBREAK=3.

// Section break at end of a measure.
function addSectionBreak(measureNo) {
    return _addLayoutBreak("add section break", 2 /* SECTION */, measureNo)
}

// System break at end of a measure.
function addSystemBreak(measureNo) {
    return _addLayoutBreak("add system break", 1 /* LINE */, measureNo)
}

// Page break at end of a measure.
function addPageBreak(measureNo) {
    return _addLayoutBreak("add page break", 0 /* PAGE */, measureNo)
}

// Add or change a key signature at the start of a measure, applied to ALL staves.
// key: integer -7 (7 flats) to +7 (7 sharps), 0 = C major / A minor.
function addKeySignature(measure, key) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof key !== "number" || key < -7 || key > 7)
        return { error: "key must be an integer from -7 (7 flats) to +7 (7 sharps)" }

    var tick = _posToTick(measure, 1, "0")
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    try {
        s.startCmd("add key signature")
        var nStaves = s.nstaves
        for (var st = 0; st < nStaves; st++) {
            var track = st * 4

            // Walk FIRST (before rewindToTick) to avoid QML GC cursor invalidation.
            // SegmentType::KeySig = 0x40.
            var existingEl = _findSegmentElAtTick(s, measure, tick, track, 0x40)
            if (existingEl) {
                // Update in-place: property write calls undoPropertyChanged — fully undo-tracked.
                existingEl.concertKey = key
                continue
            }

            // No existing element — position cursor NOW (after walk) and add.
            var c = s.newCursor()
            c.track = track
            c.rewindToTick(tick)
            var el = api.engraving.newElement(_EL.KEYSIG)
            el.concertKey = key
            c.add(el)
        }
        s.endCmd()
        return { ok: true, measure: measure, key: key, keySignature: _keysigToString(key), stavesUpdated: nStaves }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addKeySignature failed: " + e }
    }
}

// Add or change a time signature at a measure.
// denominator must be a power of 2 (1, 2, 4, 8, 16, 32).
// NOTE: cursor.add() for TIMESIG calls score->cmdAddTimeSig() which manages
// its own startCmd/endCmd — do NOT wrap in an outer transaction.
function addTimeSignature(measure, numerator, denominator) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (!numerator || !denominator || numerator < 1 || denominator < 1)
        return { error: "numerator and denominator are required and must be positive integers" }

    var tick = _posToTick(measure, 1, "0")
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    try {
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(tick)
        var el = api.engraving.newElement(_EL.TIMESIG)
        el.timesig = api.engraving.fraction(numerator, denominator)
        c.add(el)
        return { ok: true, measure: measure, numerator: numerator, denominator: denominator }
    } catch(e) {
        return { error: "addTimeSignature failed: " + e }
    }
}

// Add or change a clef at a position in the score.
// clefType: "treble", "treble8vb", "treble8va", "tenor", "alto", "bass",
//           "bass8vb", "percussion", "tab", "tab4"
function addClef(measure, beat, beatFraction, staff, clefType) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var clefInt = _CLEF[clefType]
    if (clefInt === undefined)
        return { error: "Unknown clefType '" + clefType + "'. Valid values: " + Object.keys(_CLEF).join(", ") }

    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    try {
        s.startCmd("add clef")
        var c = s.newCursor()
        var track = (staff - 1) * 4
        c.track = track

        // Walk FIRST (before rewindToTick) to avoid QML GC cursor invalidation.
        // SegmentType::Clef = 0x400 — user-added mid-measure clef changes.
        // HeaderClef (0x2) segments are system-generated; _findSegmentElAtTick
        // only targets 0x400 so they are never touched.
        var existingEl = _findSegmentElAtTick(s, measure, tick, track, 0x400)

        if (existingEl) {
            // Update in-place: property writes call undoPropertyChanged — fully undo-tracked.
            // No cursor.add() needed for this path.
            existingEl.concertClefType    = clefInt   // Pid::CLEF_TYPE_CONCERT
            existingEl.transposingClefType = clefInt  // Pid::CLEF_TYPE_TRANSPOSING
            s.endCmd()
            return { ok: true, measure: measure, beat: beat, staff: staff, clefType: clefType,
                     updated: "in-place" }
        }

        // No existing element — position cursor NOW (after walk) and add.
        c.rewindToTick(tick)
        var el = api.engraving.newElement(_EL.CLEF)
        el.concertClefType     = clefInt   // Pid::CLEF_TYPE_CONCERT
        el.transposingClefType = clefInt   // Pid::CLEF_TYPE_TRANSPOSING
        c.add(el)
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, staff: staff, clefType: clefType }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addClef failed: " + e }
    }
}

// Diagnostic: probe whether api.engraving.ClefType QML enum is accessible
// and what values it reports for common clef types.
function probeClefTypeEnum() {
    try {
        var ct = api.engraving.ClefType
        if (!ct) return { error: "api.engraving.ClefType is null or undefined" }
        return {
            ok: true,
            G:       ct.G       !== undefined ? ct.G       : "missing",
            F:       ct.F       !== undefined ? ct.F       : "missing",
            C3:      ct.C3      !== undefined ? ct.C3      : "missing",
            C4:      ct.C4      !== undefined ? ct.C4      : "missing",
            G8_VB:   ct.G8_VB   !== undefined ? ct.G8_VB   : "missing",
            PERC:    ct.PERC    !== undefined ? ct.PERC    : "missing",
            TAB:     ct.TAB     !== undefined ? ct.TAB     : "missing",
            INVALID: ct.INVALID !== undefined ? ct.INVALID : "missing"
        }
    } catch(e) {
        return { error: "probeClefTypeEnum failed: " + e }
    }
}

// Add a fingering annotation to a note. `finger` is the fingering digit or
// symbol as a string or integer (e.g. 1, 2, 3, 4, 5, 0, "p", "i", "m", "a").
// `pitch` is optional (e.g. "C4") — if provided, targets the matching note in
// the chord; if omitted, targets chord.notes[0] (lowest note).
function addFingering(measure, beat, beatFraction, staff, voice, finger, pitch) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (finger === undefined || finger === null || finger === "")
        return { error: "finger is required" }

    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addFingering", measureNo: measure, beat: beat, staff: staff }
    }

    var c = s.newCursor()
    c.track = (staff - 1) * 4 + ((voice || 1) - 1)
    c.rewindToTick(tick)
    var chord = c.element
    var CHORD = api.engraving.Element.CHORD
    if (!chord || chord.type !== CHORD) {
        return {
            error: "No chord at measure " + measure + " beat " + beat + " staff " + staff,
            _debug: { fn: "addFingering", tick: tick, elementType: chord ? chord.type : null }
        }
    }

    var targetNote = null
    if (pitch !== null && pitch !== undefined) {
        var targetMidi = _noteNameToMidi(pitch)
        if (targetMidi < 0) return { error: "Unrecognised pitch: " + pitch }
        for (var i = 0; i < chord.notes.length; i++) {
            if (parseInt(chord.notes[i].pitch) === targetMidi) { targetNote = chord.notes[i]; break }
        }
        if (!targetNote) return {
            error: "No note with pitch " + pitch + " found at measure " + measure + " beat " + beat,
            _debug: { fn: "addFingering", tick: tick, targetMidi: targetMidi }
        }
    } else {
        if (!chord.notes || chord.notes.length === 0)
            return { error: "Chord at measure " + measure + " beat " + beat + " has no notes" }
        targetNote = chord.notes[0]
    }

    try {
        s.startCmd("add fingering")
        var el = api.engraving.newElement(_EL.FINGERING)
        el.text = String(finger)
        targetNote.add(el)
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, staff: staff, finger: String(finger) }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addFingering failed: " + e }
    }
}

// Add a string number annotation to a note. `stringNumber` is 1–6 (or 0 for
// open string). `pitch` is optional — same semantics as addFingering.
//
// String numbers share ElementType::FINGERING with regular fingerings; the
// distinction is the TextStyleType (Pid::TEXT_STYLE = STRING_NUMBER), set
// via the writable `subStyle` property after construction.
function addStringNumber(measure, beat, beatFraction, staff, voice, stringNumber, pitch) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (stringNumber === undefined || stringNumber === null || stringNumber === "")
        return { error: "stringNumber is required" }

    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addStringNumber", measureNo: measure, beat: beat, staff: staff }
    }

    var c = s.newCursor()
    c.track = (staff - 1) * 4 + ((voice || 1) - 1)
    c.rewindToTick(tick)
    var chord = c.element
    var CHORD = api.engraving.Element.CHORD
    if (!chord || chord.type !== CHORD) {
        return {
            error: "No chord at measure " + measure + " beat " + beat + " staff " + staff,
            _debug: { fn: "addStringNumber", tick: tick, elementType: chord ? chord.type : null }
        }
    }

    var targetNote = null
    if (pitch !== null && pitch !== undefined) {
        var targetMidi = _noteNameToMidi(pitch)
        if (targetMidi < 0) return { error: "Unrecognised pitch: " + pitch }
        for (var i = 0; i < chord.notes.length; i++) {
            if (parseInt(chord.notes[i].pitch) === targetMidi) { targetNote = chord.notes[i]; break }
        }
        if (!targetNote) return {
            error: "No note with pitch " + pitch + " found at measure " + measure + " beat " + beat,
            _debug: { fn: "addStringNumber", tick: tick, targetMidi: targetMidi }
        }
    } else {
        if (!chord.notes || chord.notes.length === 0)
            return { error: "Chord at measure " + measure + " beat " + beat + " has no notes" }
        targetNote = chord.notes[0]
    }

    try {
        s.startCmd("add string number")
        var el = api.engraving.newElement(_EL.FINGERING)
        el.subStyle = _TS.STRING_NUMBER
        el.text = String(stringNumber)
        targetNote.add(el)
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, staff: staff, stringNumber: String(stringNumber) }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addStringNumber failed: " + e }
    }
}

// Set score metadata. Empty/null fields are skipped.
//
// NOTE: Score::setMetaTag (engraving/dom/score.cpp:2002) writes directly to
// m_metaTags WITHOUT pushing an undo entry. So the change persists with the
// score (and round-trips through save/load) but no Undo entry appears in
// MuseScore's stack — the previous startCmd/endCmd wrap registered as an
// empty command. Visible title/composer text frames rendered from these
// tags are also NOT auto-refreshed; the user has to re-open the score or
// trigger a redraw to see the updated header.
function setScoreMetadata(title, composer, lyricist, copyright, subtitle) {
    var s = _score()
    if (!s) return { error: "No score open" }
    // Readiness guard. Score::setMetaTag is non-undoable and writes directly
    // to m_metaTags; in v0.5.1 smoke test 22 the first call silently failed
    // and the second worked. Best hypothesis is the score wasn't fully in a
    // writable state on the first call (e.g. mid-layout or before
    // post-load init). Refusing to attempt the write when nmeasures is 0 or
    // firstMeasure is null gives a clean error instead of a phantom ok.
    if (!s.firstMeasure || !s.nmeasures || s.nmeasures < 1) {
        return { error: "Score not ready (no measures available) — try again after the score is fully loaded" }
    }

    // Write + read-back verify each tag. If the read-back disagrees with the
    // write, try once more before reporting failure. Avoids the silent-fail
    // mode without making the function block indefinitely.
    var pairs = []
    if (title)     pairs.push(["workTitle", title,     "title"])
    if (composer)  pairs.push(["composer",  composer,  "composer"])
    if (lyricist)  pairs.push(["lyricist",  lyricist,  "lyricist"])
    if (copyright) pairs.push(["copyright", copyright, "copyright"])
    // The subtitle field in MuseScore Score Properties is keyed by the
    // tag "subtitle". An earlier implementation used "workNumber", which
    // landed the value in the "Work number" field instead.
    if (subtitle)  pairs.push(["subtitle",  subtitle,  "subtitle"])

    var updates = []
    var stillFailed = []
    try {
        for (var i = 0; i < pairs.length; i++) {
            var key = pairs[i][0], val = pairs[i][1], label = pairs[i][2]
            s.setMetaTag(key, val)
            var got = ""
            try { got = s.metaTag(key) || "" } catch (e) {}
            if (got !== val) {
                // Retry once — covers the timing-sensitive case observed
                // in smoke test 22 where the second call worked.
                s.setMetaTag(key, val)
                try { got = s.metaTag(key) || "" } catch (e) {}
            }
            if (got === val) updates.push(label)
            else             stillFailed.push(label)
        }
    } catch(e) {
        return { error: "setScoreMetadata failed: " + e }
    }
    var subtitleNote = subtitle
        ? " Subtitle tag saved. Visual title-frame display refreshes on save — to verify, call get_score_metadata."
        : ""
    if (stillFailed.length > 0) {
        return {
            ok: true,
            updated: updates,
            failed: stillFailed,
            titleFrameUpdated: false,
            note: "Some tags could not be persisted after retry: " + stillFailed.join(", ") + ". Tag writes are non-undoable; visible title-frame text may also need a save+reopen to refresh." + subtitleNote
        }
    }
    return {
        ok: true,
        updated: updates,
        titleFrameUpdated: false,
        note: "Tags saved with score. Not undoable; the visible title-frame text may not refresh until the score is saved and re-opened." + subtitleNote
    }
}

// ── BATCH 4: note entry, lyrics, articulations, tie, metadata read ───────

// Read-only writable-metadata tags. Complement to getScoreInfo (which reports
// structural data). Call before setScoreMetadata to see existing values.
function getScoreMetadata() {
    var s = _score()
    if (!s) return { error: "No score open" }
    return {
        title:      s.metaTag("workTitle")   || "",
        subtitle:   s.metaTag("subtitle")    || "",
        composer:   s.metaTag("composer")    || "",
        lyricist:   s.metaTag("lyricist")    || "",
        copyright:  s.metaTag("copyright")   || "",
        arranger:   s.metaTag("arranger")    || "",
        translator: s.metaTag("translator")  || "",
        workNumber: s.metaTag("workNumber")  || ""
    }
}

// Key signature active at a given 1-based measure number.
// Returns { measure, keySignature, fifths } where keySignature is a string
// ("C major", "G major", "D minor" etc.) and fifths is the raw integer
// (-7..+7, negative = flats, positive = sharps).
function getKeyAt(measure) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var st0 = s.staves && s.staves.length > 0 ? s.staves[0] : null
    if (!st0) return { error: "No staves found" }
    var tick = _posToTick(measure, 1, "0")
    if (tick < 0) return { error: "Measure " + measure + " not found" }
    try {
        var k = st0.key(tick)
        return {
            measure:       measure,
            keySignature:  _keysigToString(k),
            fifths:        k
        }
    } catch(e) {
        return { error: "getKeyAt failed: " + e }
    }
}

// Time signature active at a given 1-based measure number.
// Returns { measure, numerator, denominator, display } where display is e.g. "4/4", "3/8".
function getTimeSigAt(measure) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var st0 = s.staves && s.staves.length > 0 ? s.staves[0] : null
    if (!st0) return { error: "No staves found" }
    var tick = _posToTick(measure, 1, "0")
    if (tick < 0) return { error: "Measure " + measure + " not found" }
    try {
        var ts = st0.timeSig(tick)
        if (!ts || !ts.timesigNominal) return { error: "No time signature found at measure " + measure }
        var num = ts.timesigNominal.numerator
        var den = ts.timesigNominal.denominator
        return {
            measure:     measure,
            numerator:   num,
            denominator: den,
            display:     num + "/" + den
        }
    } catch(e) {
        return { error: "getTimeSigAt failed: " + e }
    }
}

// Clef type active at a given 1-based measure number on a given 1-based staff.
// Returns { measure, staff, clefType, clefInt } where clefType is the string
// name from the _CLEF map (e.g. "bass", "treble") and clefInt is the raw integer.
function getClefAt(measure, staff) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var staffIdx = (staff || 1) - 1
    if (!s.staves || staffIdx < 0 || staffIdx >= s.staves.length)
        return { error: "Staff " + staff + " not found (score has " + (s.staves ? s.staves.length : 0) + " staves)" }
    var tick = _posToTick(measure, 1, "0")
    if (tick < 0) return { error: "Measure " + measure + " not found" }
    try {
        var clefInt = s.staves[staffIdx].clefType(tick)
        return {
            measure:  measure,
            staff:    staff,
            clefType: _clefIntToName(clefInt),
            clefInt:  clefInt
        }
    } catch(e) {
        return { error: "getClefAt failed: " + e }
    }
}

// Add a note at (measure, beat, beatFraction) on (staff, voice), overwriting
// whatever is there (note or rest). Uses cursor.addNote(midi, false) so the
// cursor does not advance.
function addNote(measure, beat, beatFraction, staff, voice, pitch, duration) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addNote", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }
    var midiPitch = _noteNameToMidi(pitch)
    var frac = _durationToFraction(duration)
    try {
        s.startCmd("add note")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        c.setDuration(frac[0], frac[1])
        c.addNote(midiPitch, false)
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, pitch: pitch, duration: duration }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "addNote failed: " + e }
    }
}

// Add a pitch to an existing chord without changing its duration. Fails if
// there is no chord at the given position.
function addNoteToChord(measure, beat, beatFraction, staff, voice, pitch) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addNoteToChord", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }
    var midiPitch = _noteNameToMidi(pitch)

    // Cursor must land on a CHORD before c.addNote(p, true) — the "add to
    // chord" path requires an existing chord; on a rest or empty position
    // it silently fails (the user sees "Add note" in the undo stack but
    // nothing happens to their pitch set). Probe before startCmd.
    var probe = s.newCursor()
    probe.track = (staff - 1) * 4 + (voice - 1)
    probe.rewindToTick(tick)
    var probeEl = probe.element
    var CHORD = api.engraving.Element.CHORD
    if (!probeEl || probeEl.type !== CHORD) {
        return {
            error: "No chord at measure " + measure + " beat " + beat + " — use add_note to create the first note",
            _debug: { fn: "addNoteToChord", tick: tick, elementType: probeEl ? probeEl.type : null, CHORD: CHORD }
        }
    }

    try {
        s.startCmd("add note to chord")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        c.addNote(midiPitch, true)
        s.endCmd()
        return { ok: true, pitch: pitch }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "addNoteToChord failed: " + e }
    }
}

// Add a rest at the given position, overwriting whatever is there.
function addRest(measure, beat, beatFraction, staff, voice, duration) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addRest", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }
    var frac = _durationToFraction(duration)
    try {
        s.startCmd("add rest")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        c.setDuration(frac[0], frac[1])
        c.addRest()
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, duration: duration }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "addRest failed: " + e }
    }
}

// Add a lyric syllable to the chord at the given position. Attaches with
// chord.add(ly), NOT cursor.add(ly) — that distinction is load-bearing.
// `verse` is 1-based externally, 0-based internally (Lyrics.verse).
function addLyric(measure, beat, beatFraction, staff, voice, text, syllabic, verse) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addLyric", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }
    try {
        s.startCmd("add lyric")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        var chord = c.element
        if (!chord) {
            try { s.endCmd(true) } catch (ee) {}
            return {
                error: "No element at measure " + measure + " beat " + beat,
                _debug: { fn: "addLyric", tick: tick, elementType: null }
            }
        }
        var ly = api.engraving.newElement(_EL.LYRICS)
        chord.add(ly)                       // chord.add, NOT cursor.add
        ly.text = text
        ly.syllabic = _syllabicToInt(syllabic)
        ly.verse = (verse || 1) - 1         // 0-based internally
        s.endCmd()
        return { ok: true, text: text, syllabic: syllabic, verse: verse || 1 }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "addLyric failed: " + e }
    }
}

// Tie the note at the given position to the next note of the same pitch.
// cmd("tie") — NOT "add-tie" (the registered action ID is just "tie",
// notationactioncontroller.cpp:240). cmd-based, so NO startCmd wrapper.
//
// The cmd silently no-ops when its selection has no note (e.g. selectRange
// was too tight to include the chord segment) or when the chord has no
// next-position note of matching pitch to tie to. We probe the chord first
// and then verify that some note's tieForward flipped — otherwise we return
// an error rather than a misleading ok:true.
function addTie(measure, beat, beatFraction, staff, voice) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addTie", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }

    var s0 = staff - 1
    var probe = s.newCursor()
    probe.track = s0 * 4 + ((voice || 1) - 1)
    probe.rewindToTick(tick)
    var chord = probe.element
    var CHORD = api.engraving.Element.CHORD
    if (!chord || chord.type !== CHORD) {
        return {
            error: "No chord at measure " + measure + " beat " + beat + " staff " + staff + " — nothing to tie",
            _debug: { fn: "addTie", tick: tick, elementType: chord ? chord.type : null }
        }
    }

    // Snapshot tieForward flags so we can detect a no-op.
    var before = []
    var nNotes = chord.notes ? chord.notes.length : 0
    for (var i = 0; i < nNotes; i++) before.push(!!chord.notes[i].tieForward)

    // Selection range must cover the chord segment. The chord's duration in
    // ticks tells us where the next chord-rest segment starts; selecting up
    // to (but not including) that boundary covers exactly this chord.
    var dTicks = 1
    try { if (chord.duration && typeof chord.duration.ticks === "number") dTicks = chord.duration.ticks } catch (e) {}
    if (dTicks < 1) dTicks = 1

    try {
        s.selection.selectRange(tick, tick + dTicks, s0, s0 + 1)
        api.engraving.cmd("tie")

        // Verify: re-fetch chord via fresh cursor — old `chord` ref is stale
        // after cmd() replaces the engraving objects in the model.
        var recheck = s.newCursor()
        recheck.track = s0 * 4 + ((voice || 1) - 1)
        recheck.rewindToTick(tick)
        var freshChord = recheck.element
        var changed = false
        if (freshChord && freshChord.type === CHORD && freshChord.notes) {
            for (var j = 0; j < Math.min(freshChord.notes.length, before.length); j++) {
                if (!!freshChord.notes[j].tieForward && !before[j]) { changed = true; break }
            }
        }
        if (!changed) {
            return {
                error: "tie cmd had no effect — the next position likely has no note of matching pitch",
                _debug: { fn: "addTie", tick: tick, durationTicks: dTicks, noteCount: nNotes }
            }
        }
        return { ok: true }
    } catch (e) {
        return { error: "addTie failed: " + e }
    }
}

// Add an articulation to the chord at the given position. cmd-based, so NO
// startCmd wrapper. Only articulations with a verified registered cmd string
// are included — others return an "unsupported" error rather than guessing.
//
// Sources (notationactioncontroller.cpp / notationuiactions.cpp):
//   add-staccato   (controller:181, uiactions:2526)
//   add-tenuto     (controller:180, uiactions:2519)
//   add-sforzato   (controller:179, uiactions:2512) ← maps "accent"
//   add-marcato    (controller:178, uiactions:2505)
//   add-trill      (controller:503, uiactions:1972)
//   add-mordent    (controller:505, uiactions:1984)
//   add-turn       (controller:498, uiactions:1942)
//   add-up-bow     (controller:513, uiactions:2026)
//   add-down-bow   (controller:514, uiactions:2032)
//
// Direct-construction articulations (no registered cmd path): staccatissimo,
// snapPizzicato, harmonic, stress, unstress. These use `newElement(ARTICULATION)`
// + `art.symbol = SymId.<...>` BEFORE `chord.add(art)` — same set-before-add
// discipline as Fermata. The SYMBOL property is defined on the base EngravingItem
// (elements.h:828) and is documented as valid for symbols, articulation,
// fermatas and breaths.
//
// Still NOT covered: shortFermata/longFermata/veryLongFermata (use add_fermata
// instead), leftHandPizzicato, tremolo (own element type).
function addArticulation(measure, beat, beatFraction, staff, voice, articulation) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addArticulation", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, articulation: articulation, tick: tick }
    }

    // ── Direct-construction branch (SymId-keyed) ──
    // SymId names verified in src/engraving/api/v1/apitypes.h.
    // `staccato` originally went through the cmd("add-staccato") path, but in
    // smoke-test v0.5.1 that path silently no-op'd (ok:true returned in ~8ms,
    // no undo entry, no glyph). Moving it to direct construction matches the
    // proven-working staccatissimo / snapPizzicato path and bypasses whatever
    // selection-state requirement the cmd handler was failing on.
    var directSymIds = {
        "staccato":      "articStaccatoAbove",
        "staccatissimo": "articStaccatissimoAbove",
        "snapPizzicato": "pluckedSnapPizzicatoAbove",
        "harmonic":      "stringsHarmonic",
        "stress":        "articStressAbove",
        "unstress":      "articUnstressAbove"
    }
    if (directSymIds[articulation] !== undefined) {
        var symIdName = directSymIds[articulation]
        var SymId = api.engraving.SymId
        if (!SymId) return { error: "api.engraving.SymId not exposed" }
        var symValue = SymId[symIdName]
        if (symValue === undefined) return { error: "SymId not found: " + symIdName }

        var c = s.newCursor()
        c.track = (staff - 1) * 4 + ((voice || 1) - 1)
        c.rewindToTick(tick)
        var chord = c.element
        if (!chord || chord.type !== api.engraving.Element.CHORD)
            return {
                error: "No chord at measure " + measure + " beat " + beat,
                _debug: { fn: "addArticulation", tick: tick, elementType: chord ? chord.type : null, CHORD_TYPE: api.engraving.Element.CHORD }
            }

        try {
            s.startCmd("add articulation")
            var art = api.engraving.newElement(_EL.ARTICULATION)
            art.symbol = symValue       // SET BEFORE add — Pid::SYMBOL keys the variant (same as Fermata)
            chord.add(art)              // chord.add, NOT cursor.add — same pattern as add_lyric
            s.endCmd()
            return { ok: true, articulation: articulation }
        } catch (e) {
            try { s.endCmd(true) } catch (ee) {}
            return { error: "addArticulation (direct) failed: " + e }
        }
    }

    // ── Cmd-based branch (registered action handlers) ──
    // `staccato` is intentionally absent here — it lives in directSymIds now
    // (see Fix 1 in this version). Other cmd-based articulations still go
    // through toggleArticulation; we probe the chord first and verify the
    // articulation count actually increased to detect silent no-ops.
    var articulationCmdMap = {
        "tenuto":   "add-tenuto",
        "accent":   "add-sforzato",
        "marcato":  "add-marcato",
        "trill":    "add-trill",
        "mordent":  "add-mordent",
        "turn":     "add-turn",
        "upBow":    "add-up-bow",
        "downBow":  "add-down-bow"
    }
    var cmdStr = articulationCmdMap[articulation]
    if (!cmdStr) return { error: "Articulation '" + articulation + "' not yet implemented" }

    var s0 = staff - 1
    var probeC = s.newCursor()
    probeC.track = s0 * 4 + ((voice || 1) - 1)
    probeC.rewindToTick(tick)
    var probeChord = probeC.element
    if (!probeChord || probeChord.type !== api.engraving.Element.CHORD) {
        return {
            error: "No chord at measure " + measure + " beat " + beat + " staff " + staff,
            _debug: { fn: "addArticulation", tick: tick, elementType: probeChord ? probeChord.type : null }
        }
    }
    var beforeArts = (probeChord.articulations && probeChord.articulations.length) || 0

    var dTicks = 1
    try { if (probeChord.duration && typeof probeChord.duration.ticks === "number") dTicks = probeChord.duration.ticks } catch (e) {}
    if (dTicks < 1) dTicks = 1

    try {
        s.selection.selectRange(tick, tick + dTicks, s0, s0 + 1)
        api.engraving.cmd(cmdStr)
        var afterArts = (probeChord.articulations && probeChord.articulations.length) || 0
        if (afterArts <= beforeArts) {
            return {
                error: "Articulation cmd had no effect — selection may have missed the chord",
                _debug: { fn: "addArticulation", cmd: cmdStr, tick: tick, before: beforeArts, after: afterArts }
            }
        }
        return { ok: true, articulation: articulation }
    } catch (e) {
        return { error: "addArticulation failed: " + e }
    }
}

// ── Diagnostic ───────────────────────────────────────────────────────────
//
// console.log() is silently swallowed in MS4 extensions, so returning enum
// integers as tool output is the only way to inspect API surface from inside
// the extension. Originally specified in CC_INSTRUCTION_batch3_fixes.md Fix 4
// but not previously landed.
function getDebugInfo() {
    var el  = api.engraving.Element
    var dt  = api.engraving.DynamicType
    var lbt = api.engraving.LayoutBreakType
    return {
        elementTypes: {
            DYNAMIC:        el ? el.DYNAMIC        : "undefined",
            LAYOUT_BREAK:   el ? el.LAYOUT_BREAK   : "undefined",
            HAIRPIN:        el ? el.HAIRPIN        : "undefined",
            SLUR:           el ? el.SLUR           : "undefined",
            OTTAVA:         el ? el.OTTAVA         : "undefined",
            TEMPO_TEXT:     el ? el.TEMPO_TEXT     : "undefined",
            STAFF_TEXT:     el ? el.STAFF_TEXT     : "undefined",
            SYSTEM_TEXT:    el ? el.SYSTEM_TEXT    : "undefined",
            REHEARSAL_MARK: el ? el.REHEARSAL_MARK : "undefined",
            HARMONY:        el ? el.HARMONY        : "undefined",
            LYRICS:         el ? el.LYRICS         : "undefined"
        },
        dynamicTypes: {
            PPP: dt ? dt.PPP : "undefined",
            PP:  dt ? dt.PP  : "undefined",
            P:   dt ? dt.P   : "undefined",
            MP:  dt ? dt.MP  : "undefined",
            MF:  dt ? dt.MF  : "undefined",
            F:   dt ? dt.F   : "undefined",
            FF:  dt ? dt.FF  : "undefined",
            FFF: dt ? dt.FFF : "undefined",
            FP:  dt ? dt.FP  : "undefined",
            SFZ: dt ? dt.SFZ : "undefined"
        },
        layoutBreakTypes: {
            LINE:    lbt ? lbt.LINE    : "undefined",
            PAGE:    lbt ? lbt.PAGE    : "undefined",
            SECTION: lbt ? lbt.SECTION : "undefined",
            NOBREAK: lbt ? lbt.NOBREAK : "undefined"
        },
        score: (function() {
            var sc = _score()
            return sc ? { nstaves: sc.nstaves, nmeasures: sc.nmeasures } : null
        })()
    }
}

// ── Settings exposure (read-only) ─────────────────────────────────────────
//
// Used by Main.qml's buildSystemPrompt(). These are score-side settings, not
// app preferences (which are not reachable from a v2 extension).

// "STANDARD" | "GERMAN" | "GERMAN_PURE" | "SOLFEGGIO" | "FRENCH" | null
function getChordSymbolSpelling() {
    var s = _score()
    if (!s) return null
    var v = _styleValue(s, "chordSymbolSpelling", null)
    if (v === null || v === undefined) return null
    // The MStyle.value() return is the underlying enum integer.
    var map = { 0: "STANDARD", 1: "GERMAN", 2: "GERMAN_PURE", 3: "SOLFEGGIO", 4: "FRENCH" }
    if (typeof v === "number" && map[v]) return map[v]
    // Some builds may return a string already.
    if (typeof v === "string") return v.toUpperCase()
    return null
}

// true | false | null
function getConcertPitch() {
    var s = _score()
    if (!s) return null
    var v = _styleValue(s, "concertPitch", null)
    if (typeof v === "boolean") return v
    if (typeof v === "number")  return v !== 0
    return null
}

// ── BATCH 5: get_measure, set_note_pitch, set_note_duration, add_fermata ──

// Structural metadata for ONE measure: time/key signature, tempo, rehearsal
// mark, end-barline type, and chord symbols. Notes/rests/lyrics intentionally
// omitted — callers should use getNotesInRange / getLyricsInRange for content.
function getMeasure(measureNo) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var m = _findMeasureByNumber(s, measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }

    var result = { number: measureNo }

    // Active key/time signature at this measure (via Staff API, same path as
    // getStructure — segment-walking misses changes carried from prior measures).
    var st0 = s.staves && s.staves.length > 0 ? s.staves[0] : null
    try {
        if (st0 && m.tick) {
            var ts = st0.timeSig(m.tick)
            if (ts && ts.timesigNominal) {
                result.timeSignature = {
                    numerator:   ts.timesigNominal.numerator,
                    denominator: ts.timesigNominal.denominator
                }
            }
        }
    } catch(e) {}
    try {
        if (st0 && m.tick) {
            var k = st0.key(m.tick)
            if (typeof k === "number") result.keySignature = _keyIntToString(k)
        }
    } catch(e) {}

    // Tempo + rehearsal mark in this measure (reuse existing helpers).
    try {
        var t = _firstTempoInMeasure(m)
        if (t) {
            result.tempo = {
                text: t.text || null,
                bpm:  t.tempo ? Math.round(t.tempo * 60.0) : null
            }
        }
    } catch(e) {}
    try {
        var r = _firstRehearsalMarkInMeasure(m)
        if (r) result.rehearsalMark = r.text || ""
    } catch(e) {}

    // End barline — look for the EndBarLine segment (SegmentType 0x20000),
    // falling back to the last segment if absent.
    try {
        var seg = m.firstSegment
        var blSeg = null
        while (seg) {
            if (seg.segmentType & 0x20000) { blSeg = seg; break }
            seg = seg.next
        }
        if (!blSeg) blSeg = m.lastSegment
        if (blSeg) {
            var bl = blSeg.elementAt(0)
            if (bl && typeof bl.barlineType === "number")
                result.barlineEnd = _barlineTypeStr(bl.barlineType)
        }
    } catch(e) {}

    // Chord symbols in this measure (reuse existing reader).
    try {
        var harm = getHarmonyInRange(measureNo, measureNo)
        if (harm && harm.harmonies) result.harmonies = harm.harmonies
        else result.harmonies = []
    } catch(e) {
        result.harmonies = []
    }

    return result
}

// Change the pitch of a specific note within the chord at the given position.
// `oldPitch` (NoteName) identifies which note to change (by MIDI pitch match);
// if null/omitted, changes the first (lowest) note.
function setNotePitch(measure, beat, beatFraction, staff, voice, oldPitch, newPitch) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "setNotePitch", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }
    var newMidi = _noteNameToMidi(newPitch)
    var newTpc  = _noteNameToTpc(newPitch)
    var oldMidi = oldPitch ? _noteNameToMidi(oldPitch) : null

    try {
        s.startCmd("set note pitch")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        var chord = c.element
        if (!chord || !chord.notes) {
            try { s.endCmd(true) } catch (ee) {}
            return {
                error: "No chord at measure " + measure + " beat " + beat,
                _debug: { fn: "setNotePitch", tick: tick, elementType: chord ? chord.type : null, CHORD_TYPE: api.engraving.Element.CHORD }
            }
        }
        var target = null
        for (var i = 0; i < chord.notes.length; i++) {
            if (oldMidi === null || chord.notes[i].pitch === oldMidi) {
                target = chord.notes[i]
                break
            }
        }
        if (!target) {
            try { s.endCmd(true) } catch (ee) {}
            return { error: "Note " + oldPitch + " not found at that position" }
        }
        target.pitch = newMidi
        target.tpc   = newTpc
        s.endCmd()
        return { ok: true, from: oldPitch, to: newPitch }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "setNotePitch failed: " + e }
    }
}

// Remove a note from a chord at the given position.
// If pitch is provided, removes only the note matching that pitch.
// If pitch is omitted and the chord has exactly one note, removes it.
// If pitch is omitted and the chord has multiple notes, returns an error.
// When the last note is removed, the engine atomically replaces the chord
// with a rest of equal duration (Score::deleteItem handles this).
function deleteNote(measure, beat, beatFraction, staff, voice, pitch) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "deleteNote", measureNo: measure, beat: beat, beatFraction: beatFraction || "0" }
    }
    var targetMidi = pitch ? _noteNameToMidi(pitch) : null

    try {
        s.startCmd("delete note")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        var chord = c.element
        if (!chord || !chord.notes) {
            try { s.endCmd(true) } catch (ee) {}
            return {
                error: "No chord at measure " + measure + " beat " + beat,
                _debug: { fn: "deleteNote", tick: tick, elementType: chord ? chord.type : null }
            }
        }
        if (!targetMidi && chord.notes.length > 1) {
            try { s.endCmd(true) } catch (ee) {}
            return { error: "Multiple notes at this position — specify pitch to delete (e.g. 'C4')" }
        }
        var target = null
        for (var i = 0; i < chord.notes.length; i++) {
            if (targetMidi === null || parseInt(chord.notes[i].pitch) === targetMidi) {
                target = chord.notes[i]
                break
            }
        }
        if (!target) {
            try { s.endCmd(true) } catch (ee) {}
            return { error: "Note " + pitch + " not found at that position" }
        }
        api.engraving.removeElement(target)
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, staff: staff, voice: voice, deleted: pitch || "note" }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "deleteNote failed: " + e }
    }
}

// Adds a single-note tremolo to the chord at the given position.
// type: "buzz" (buzz roll), "8th", "16th", "32nd", "64th".
// Two-note tremolo is not implemented — requires C++ API additions
// (TremoloTwoChord::setChord1/setChord2 are not Q_INVOKABLE).
//
// On 4.7.0, api.engraving.TremoloType.X may return either an integer or a
// string name (same enum-string issue as api.engraving.Element.X). Either way
// the assignment `tr.tremoloType = val` should work — EngravingItem::setProperty
// for Pid::TREMOLO_TYPE accepts both forms via QVariant coercion. If this
// proves wrong at runtime, fall back to literal string names (e.g. "R16").
function addTremolo(measure, beat, beatFraction, staff, voice, type) {
    var s = _score()
    if (!s) return { error: "No score open" }

    var _TREMOLO_TYPE = {
        "buzz":  "BUZZ_ROLL",
        "8th":   "R8",
        "16th":  "R16",
        "32nd":  "R32",
        "64th":  "R64"
    }
    var typeName = _TREMOLO_TYPE[type]
    if (!typeName) return { error: "Unknown tremolo type '" + type + "'. Valid: buzz, 8th, 16th, 32nd, 64th" }

    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addTremolo", measureNo: measure, beat: beat }
    }

    var TremoloType = api.engraving.TremoloType
    if (!TremoloType) return { error: "api.engraving.TremoloType not exposed" }
    var tremoloTypeVal = TremoloType[typeName]
    if (tremoloTypeVal === undefined) return { error: "TremoloType." + typeName + " not found" }

    try {
        s.startCmd("add tremolo")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + ((voice || 1) - 1)
        c.rewindToTick(tick)
        var chord = c.element
        if (!chord || chord.type !== api.engraving.Element.CHORD) {
            try { s.endCmd(true) } catch (ee) {}
            return {
                error: "No chord at measure " + measure + " beat " + beat + " — tremolo requires a note, not a rest",
                _debug: { fn: "addTremolo", tick: tick, elementType: chord ? chord.type : null }
            }
        }
        var tr = api.engraving.newElement(_EL.TREMOLO_SINGLECHORD)
        c.add(tr)                          // cursor.add routes through Chord::addInternal
        tr.tremoloType = tremoloTypeVal    // set AFTER add (element must be parented first)
        s.endCmd()
        return { ok: true, measure: measure, beat: beat, staff: staff, voice: voice, type: type }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "addTremolo failed: " + e }
    }
}

// Change the duration of the chord/rest at the given position. Pitches are
// preserved; only duration changes. Overwrites the position — trailing
// content past the new duration may be overwritten if the new duration is
// longer than the old.
function setNoteDuration(measure, beat, beatFraction, staff, voice, duration) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "setNoteDuration", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }
    var frac = _durationToFraction(duration)

    try {
        s.startCmd("set note duration")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        var chord = c.element

        var pitches = []
        var isRest = (!chord || !chord.notes || chord.notes.length === 0)
        if (!isRest) {
            for (var i = 0; i < chord.notes.length; i++)
                pitches.push(chord.notes[i].pitch)
        }

        c.setDuration(frac[0], frac[1])
        if (isRest || pitches.length === 0) {
            c.addRest()
        } else {
            c.addNote(pitches[0], false)          // replaces with new duration + first pitch
            for (var j = 1; j < pitches.length; j++)
                c.addNote(pitches[j], true)       // restore remaining chord notes
        }
        s.endCmd()
        return { ok: true, duration: duration, pitchCount: pitches.length }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "setNoteDuration failed: " + e }
    }
}

// Add a fermata above the note/rest at the given position.
//
// Fermata variants are keyed by SymId, not by a separate FermataType property:
// Fermata::setProperty only handles Pid::SYMBOL (engraving/dom/fermata.cpp:151).
// FermataType is a read-only derived value — see Fermata::fermataType() at
// fermata.cpp:254 which maps SymId → FermataType via a lookup table.
//
// So we set `f.symbol = api.engraving.SymId.fermata{Type}Above` BEFORE c.add()
// — same set-before-add discipline as Dynamic.dynamicType / LayoutBreak.layoutBreakType.
// SymId values exposed in apiv1 at src/engraving/api/v1/apitypes.h:2721,2723,2727,2731.
function addFermata(measure, beat, beatFraction, staff, type) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof staff !== "number" || staff < 1)
        return { error: "Invalid staff number: " + staff }

    var symId = api.engraving.SymId
    if (!symId) return { error: "FERMATA: api.engraving.SymId not exposed" }

    var symMap = {
        "normal":   symId.fermataAbove,
        "short":    symId.fermataShortAbove,
        "long":     symId.fermataLongAbove,
        "veryLong": symId.fermataVeryLongAbove
    }
    var typeKey = type || "normal"
    var symValue = symMap[typeKey]
    if (symValue === undefined) symValue = symMap["normal"]

    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "addFermata", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, tick: tick }
    }

    try {
        s.startCmd("add fermata")
        var c = s.newCursor()
        c.track = (staff - 1) * 4       // fermatas attach to the staff, not a voice
        c.rewindToTick(tick)
        var f = api.engraving.newElement(_EL.FERMATA)
        f.symbol = symValue              // SET BEFORE add — Pid::SYMBOL keys the variant
        c.add(f)
        s.endCmd()
        return { ok: true, type: typeKey }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "addFermata failed: " + e }
    }
}

// ── BATCH 6: selection, view settings, accidental, velocity, MIDI read ───

// Return the current MuseScore selection — either a range (with extent) or a
// list of individually-selected elements. Read-only, no startCmd needed.
//
// Track→staff conversion: track = (staff-1)*4 + (voice-1), with global 1-based
// staff. C++ Selection.startStaff/endStaff are 0-based — convert by +1.
function getSelection() {
    var s = _score()
    if (!s) return { error: "No score open" }
    var sel = s.selection
    if (!sel) return { error: "No selection" }

    // sel.isRange may be either a boolean property or a callable in different
    // MS4 builds — normalise.
    var isRange = sel.isRange
    if (typeof isRange === "function") {
        try { isRange = sel.isRange() } catch (e) { isRange = false }
    }
    isRange = !!isRange

    // Read segment / staff bounds regardless of isRange — they're populated
    // for any non-list selection and let us infer rangeness when isRange is
    // false but the user has actually selected a range. Smoke test v0.5.1
    // observed isRange:false for what was clearly a range; segments
    // disagreed and were the truthful indicator.
    var ss = null, es = null
    try { ss = sel.startSegment } catch (e) {}
    try { es = sel.endSegment } catch (e) {}

    var ssTick = -1, esTick = -1
    try { if (ss && ss.tick !== undefined) ssTick = _getTickInt(ss.tick) } catch (e) {}
    try { if (es && es.tick !== undefined) esTick = _getTickInt(es.tick) } catch (e) {}

    var startStaffRaw = null, endStaffRaw = null
    try { if (sel.startStaff !== undefined && sel.startStaff !== null) startStaffRaw = sel.startStaff } catch (e) {}
    try { if (sel.endStaff   !== undefined && sel.endStaff   !== null) endStaffRaw   = sel.endStaff } catch (e) {}

    // Promote to range if segments span more than a point OR staves span > 1.
    var segmentSpan = (ssTick >= 0 && esTick >= 0 && esTick !== ssTick)
    var staffSpan   = (startStaffRaw !== null && endStaffRaw !== null && (endStaffRaw - startStaffRaw) > 1)
    if (!isRange && (segmentSpan || staffSpan)) isRange = true

    var result = {
        isRange:      isRange,
        elements:     [],
        startMeasure: null,
        endMeasure:   null,
        startStaff:   null,
        endStaff:     null
    }

    if (isRange) {
        if (ssTick >= 0) result.startMeasure = _tickToMeasureNo(ssTick)
        // endSegment is one segment PAST the selection end (it's the segment
        // the selection stops at, exclusive). Report the measure containing
        // the last included tick — esTick - 1 covers the typical range end.
        if (esTick >= 0) result.endMeasure   = _tickToMeasureNo(esTick > ssTick ? esTick - 1 : esTick)
        if (startStaffRaw !== null) result.startStaff = startStaffRaw + 1
        if (endStaffRaw   !== null) result.endStaff   = endStaffRaw   + 1   // already 1-past
    }

    // Precompute globalStaff → instrument longName (matches getNotesInRange).
    var parts = s.parts
    var staffNameMap = []
    for (var pi = 0; pi < parts.length; pi++) {
        var pp    = parts[pi]
        var lName = pp.longName || pp.partName || ""
        var nStv  = Math.floor((pp.endTrack - pp.startTrack) / 4)
        for (var si = 0; si < nStv; si++) staffNameMap.push(lName)
    }

    // sel.elements for a range selection enumerates every element inside the
    // range (notes, rests, beams, ties, articulations...). Order and count
    // vary between calls because some intermediate elements are layout-derived
    // and rebuilt on demand. Range bounds are the stable answer; populate
    // elements only for non-range selections.
    var els = null
    if (!isRange) {
        try { els = sel.elements } catch (e) {}
    }
    if (els && els.length > 0) {
        for (var i = 0; i < els.length; i++) {
            var e = els[i]
            if (!e) continue
            var track = (e.track !== undefined && e.track !== null) ? e.track : 0
            var staff = Math.floor(track / 4) + 1
            var voice = (track % 4) + 1
            // Walk parent chain to find a tick — leaf elements (notes,
            // articulations, accidentals) often don't carry a tick directly;
            // their containing chord or segment does. Previous code stopped
            // at e.parent.tick, which left tick = -1 (and measure = null) for
            // anything one extra hop deep, e.g. articulations on chord notes.
            var tick = -1
            try { if (e.tick !== undefined && e.tick !== null) tick = _getTickInt(e.tick) } catch (e2) {}
            if (tick < 0) {
                var anc = e.parent
                var hops = 0
                while (anc && hops < 4) {
                    try {
                        if (anc.tick !== undefined && anc.tick !== null) {
                            tick = _getTickInt(anc.tick)
                            if (tick >= 0) break
                        }
                    } catch (e3) {}
                    anc = anc.parent
                    hops++
                }
            }
            var mno = tick >= 0 ? _tickToMeasureNo(tick) : null
            var instrName = staffNameMap[staff - 1] || ""
            var typeStr = ""
            try { typeStr = String(e.name || e.type || "") } catch (e3) {}
            var elemObj = {
                type:       typeStr,
                measure:    mno,
                staff:      staff,
                voice:      voice,
                instrument: instrName
            }
            // For Note elements, add pitch and beat position.
            var NOTE = api.engraving.Element.NOTE
            if (typeStr === "Note" || typeStr === String(NOTE)) {
                try {
                    elemObj.pitch = _tpcToNoteName(e.tpc, e.pitch)
                } catch(e2) {}
                if (tick >= 0 && mno !== null) {
                    try {
                        var measureStartTick = _posToTick(mno, 1, "0")
                        var beatObj = _tickToBeat(tick, measureStartTick)
                        elemObj.beat         = beatObj.beat
                        elemObj.beatFraction = beatObj.fraction
                    } catch(e3) {}
                }
            }
            result.elements.push(elemObj)
        }
    }

    return result
}

// Return current score-level display settings. Read-only.
function getViewSettings() {
    var s = _score()
    if (!s) return { error: "No score open" }

    // LayoutMode enum (engraving/rendering/layoutoptions.h): PAGE=0, FLOAT=1,
    // LINE=2 (continuous), SYSTEM=3 (single), HORIZONTAL_FIXED=4.
    var lmMap = { 0: "page", 1: "float", 2: "continuous", 3: "single", 4: "horizontal" }
    var lmInt = s.layoutMode
    var layoutMode = (lmMap[lmInt] !== undefined) ? lmMap[lmInt] : String(lmInt)

    var getBool = function(prop, dflt) {
        try {
            var v = s[prop]
            if (v === undefined || v === null) return dflt
            return !!v
        } catch (e) { return dflt }
    }

    // NOTE: the underlying Q_PROPERTY is `showPageborders` (lowercase b) —
    // engraving/api/v1/score.h:325. Read from that, expose as the more
    // conventional `showPageBorders` in the result so the schema is consistent.
    return {
        layoutMode:            layoutMode,
        showInvisible:         getBool("showInvisible", false),
        showUnprintable:       getBool("showUnprintable", false),
        showFrames:            getBool("showFrames", false),
        showPageBorders:       getBool("showPageborders", false),
        showSoundFlags:        getBool("showSoundFlags", false),
        showVerticalFrames:    getBool("showVerticalFrames", false),
        showInstrumentNames:   getBool("showInstrumentNames", false),
        markIrregularMeasures: getBool("markIrregularMeasures", false),
        concertPitch:          !!_styleValue(s, "concertPitch", false)
    }
}

// Read MIDI channel parameters per instrument. `instrument` is an optional
// case-insensitive substring filter against the part long/short name.
// Channels are byte-valued (0–127), not audio mixer dB.
function getMidiChannelSettings(instrument) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var results = []
    var filterName = instrument ? String(instrument).toLowerCase() : null

    var parts = s.parts
    for (var pi = 0; pi < parts.length; pi++) {
        var part = parts[pi]
        var partName = part.longName || part.shortName || ""
        if (filterName && partName.toLowerCase().indexOf(filterName) < 0) continue

        // part.instruments — try direct indexing first, fall back to .get(i)
        var insts = part.instruments
        if (!insts) continue
        var nInsts = insts.length !== undefined ? insts.length : 0
        for (var ii = 0; ii < nInsts; ii++) {
            var inst = insts[ii]
            if (!inst && typeof insts.get === "function") {
                try { inst = insts.get(ii) } catch (e) {}
            }
            if (!inst) continue
            var channels = inst.channels
            if (!channels) continue
            var nChan = channels.length !== undefined ? channels.length : 0
            for (var ci = 0; ci < nChan; ci++) {
                var ch = channels[ci]
                if (!ch && typeof channels.get === "function") {
                    try { ch = channels.get(ci) } catch (e) {}
                }
                if (!ch) continue
                results.push({
                    instrument:  partName,
                    channelName: ch.name || "normal",
                    volume:      ch.volume,
                    pan:         ch.pan,
                    chorus:      ch.chorus,
                    reverb:      ch.reverb,
                    mute:        !!ch.mute,
                    midiProgram: ch.midiProgram,
                    midiBank:    (ch.midiBank !== undefined) ? ch.midiBank : 0
                })
            }
        }
    }
    return results
}

// Write score-level display toggles.
//
// Two strategies depending on the property:
//
// (a) cmd-based toggle for properties with a registered handler — direct
//     property writes do change the underlying field but the scene/viewport
//     isn't notified, so the score view doesn't repaint. The cmd handlers
//     route through NotationActionController::toggleScoreConfig which fires
//     the proper view-refresh signal. cmd handlers TOGGLE the current value,
//     so we compare current to desired and only fire when they differ.
//
// (b) Direct Q_PROPERTY write for properties with no registered cmd path
//     (showSoundFlags, showInstrumentNames, showVerticalFrames). Not
//     undoable, but the only path available.
//
// (c) Cmd-based for concertPitch (toggle) and layoutMode (per-mode cmd).
//
// No startCmd/endCmd wrappers — cmd-based handlers own their undo entries,
// and direct writes here are not undoable anyway.
function setViewSettings(settings) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (!settings) return { error: "settings object required" }

    var updated = []

    // (a) Toggleable scene flags via registered cmd handlers
    // (notationactioncontroller.cpp:409-414). The underlying Q_PROPERTY
    // name `showPageborders` (lowercase b) differs from the schema key.
    var toggles = [
        { key: "showInvisible",         prop: "showInvisible",         cmd: "show-invisible" },
        { key: "showUnprintable",       prop: "showUnprintable",       cmd: "show-unprintable" },
        { key: "showFrames",            prop: "showFrames",            cmd: "show-frames" },
        { key: "showPageBorders",       prop: "showPageborders",       cmd: "show-pageborders" },
        { key: "markIrregularMeasures", prop: "markIrregularMeasures", cmd: "show-irregular" }
    ]
    for (var i = 0; i < toggles.length; i++) {
        var t = toggles[i]
        if (settings[t.key] === undefined) continue
        var current = false
        try { current = !!s[t.prop] } catch (e) {}
        if (current !== !!settings[t.key]) {
            try { api.engraving.cmd(t.cmd); updated.push(t.key) } catch (e) {}
        }
    }

    // (b) Direct Q_PROPERTY writes — no registered cmd handler for these.
    var directProps = [
        { key: "showSoundFlags",      prop: "showSoundFlags" },
        { key: "showInstrumentNames", prop: "showInstrumentNames" },
        { key: "showVerticalFrames",  prop: "showVerticalFrames" }
    ]
    for (var j = 0; j < directProps.length; j++) {
        var dp = directProps[j]
        if (settings[dp.key] === undefined) continue
        try { s[dp.prop] = !!settings[dp.key]; updated.push(dp.key) } catch (e) {}
    }

    // (c) Concert pitch — toggle cmd compared against the style value.
    //
    // cmd("concert-pitch") routes through Controller::toggleConcertPitch
    // (notationactioncontroller.cpp:416) which is the only path that fires
    // the proper UI refresh signal (the toolbar indicator binds to it). A
    // direct style write changes the value but leaves the indicator stale.
    //
    // We verify the post-cmd style value to detect dispatcher failure — the
    // smoke test v0.5.1 test 40 reported updated:['concertPitch'] returned
    // while the indicator stayed unchanged, which would indicate the cmd
    // didn't actually land. Returning a note in that case is more honest
    // than claiming success.
    if (settings.concertPitch !== undefined) {
        var desiredCP = !!settings.concertPitch
        var curCP     = !!_styleValue(s, "concertPitch", false)
        if (curCP !== desiredCP) {
            try { api.engraving.cmd("concert-pitch") } catch (e) {}
            var afterCP = !!_styleValue(s, "concertPitch", false)
            if (afterCP === desiredCP) {
                updated.push("concertPitch")
            } else {
                return {
                    error: "concert_pitch could not be changed — this is likely caused by a known MuseScore bug that prevents certain commands from dispatching in form-extension context. "
                           + "See https://github.com/musescore/MuseScore/issues/24673",
                    _debug: { fn: "setScoreSettings", curCP: curCP, afterCP: afterCP, desiredCP: desiredCP }
                }
            }
        } else {
            // Already at desired — surface this so the LLM doesn't conclude
            // the cmd failed silently.
            updated.push("concertPitch (already " + desiredCP + ")")
        }
    }

    // (c) Layout mode — one cmd per mode (notationuiactions.cpp:547+).
    // HORIZONTAL_FIXED has no registered cmd path.
    if (settings.layoutMode !== undefined) {
        var lmCmds = {
            "page":       "view-mode-page",
            "float":      "view-mode-float",
            "continuous": "view-mode-continuous",
            "single":     "view-mode-single"
        }
        var lmc = lmCmds[settings.layoutMode]
        if (lmc) {
            try { api.engraving.cmd(lmc); updated.push("layoutMode") } catch (e) {}
        }
    }

    return { ok: true, updated: updated }
}

// Set or remove the accidental on a note. AccidentalType enum (apitypes.h:48):
// NONE=0, FLAT, NATURAL, SHARP, SHARP2 (double sharp), FLAT2 (double flat),
// plus dozens of microtonal variants we don't expose. Use the symbolic form
// `api.engraving.AccidentalType.SHARP` etc. with a defensive fallback.
function setNoteAccidental(measure, beat, beatFraction, staff, voice, pitch, accidental) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "setNoteAccidental", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }

    var c = s.newCursor()
    c.track = (staff - 1) * 4 + ((voice || 1) - 1)
    c.rewindToTick(tick)
    var chord = c.element
    if (!chord || chord.type !== api.engraving.Element.CHORD)
        return {
            error: "No chord at measure " + measure + " beat " + beat,
            _debug: { fn: "setNoteAccidental", tick: tick, elementType: chord ? chord.type : null, CHORD_TYPE: api.engraving.Element.CHORD }
        }

    var pitchInt = pitch ? _noteNameToMidi(pitch) : -1
    var targetNote = null
    for (var i = 0; i < chord.notes.length; i++) {
        var n = chord.notes[i]
        if (pitchInt < 0 || n.pitch === pitchInt) { targetNote = n; break }
    }
    if (!targetNote) return { error: "Note not found at that position" }

    // Map accidental string to AccidentalType enum. Use api.engraving.AccidentalType
    // when available; fall back to integer literals (verified from apitypes.h
    // mu::engraving::AccidentalType order: NONE=0, FLAT, NATURAL, SHARP, SHARP2, FLAT2).
    var AT = api.engraving.AccidentalType
    var accMap
    if (AT && AT.SHARP !== undefined) {
        accMap = {
            "none":        AT.NONE,
            "flat":        AT.FLAT,
            "natural":     AT.NATURAL,
            "sharp":       AT.SHARP,
            "doubleSharp": AT.SHARP2,
            "doubleFlat":  AT.FLAT2
        }
    } else {
        // Fallback integers — apitypes.h declares values by int(mu::engraving::AccidentalType::X).
        // Confirmed enum order: NONE=0, FLAT, NATURAL, SHARP, SHARP2, FLAT2.
        accMap = {
            "none": 0, "flat": 1, "natural": 2, "sharp": 3, "doubleSharp": 4, "doubleFlat": 5
        }
    }
    var accType = accMap[accidental]
    if (accType === undefined) return { error: "Unknown accidental: " + accidental }

    try {
        s.startCmd("set note accidental")
        targetNote.accidentalType = accType
        s.endCmd()
        return { ok: true, accidental: accidental }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "setNoteAccidental failed: " + e }
    }
}

// Per-note playback velocity override (0–127). Sets veloType=USER_VAL so the
// custom userVelocity is honoured (otherwise score-dynamics drive playback).
// VeloType enum (apitypes.h:661): OFFSET_VAL=0, USER_VAL=1.
function setNoteVelocity(measure, beat, beatFraction, staff, voice, pitch, velocity) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return {
        error: "Measure " + measure + " not found",
        _debug: { fn: "setNoteVelocity", measureNo: measure, beat: beat, beatFraction: beatFraction || "0", staff: staff, voice: voice, tick: tick }
    }

    var c = s.newCursor()
    c.track = (staff - 1) * 4 + ((voice || 1) - 1)
    c.rewindToTick(tick)
    var chord = c.element
    if (!chord || chord.type !== api.engraving.Element.CHORD)
        return {
            error: "No chord at measure " + measure + " beat " + beat,
            _debug: { fn: "setNoteVelocity", tick: tick, elementType: chord ? chord.type : null, CHORD_TYPE: api.engraving.Element.CHORD }
        }

    var pitchInt = pitch ? _noteNameToMidi(pitch) : -1
    var targetNote = null
    for (var i = 0; i < chord.notes.length; i++) {
        var n = chord.notes[i]
        if (pitchInt < 0 || n.pitch === pitchInt) { targetNote = n; break }
    }
    if (!targetNote) return { error: "Note not found at that position" }

    var USER_VAL = 1
    try {
        if (api.engraving.VeloType && api.engraving.VeloType.USER_VAL !== undefined)
            USER_VAL = api.engraving.VeloType.USER_VAL
    } catch (e) {}

    var v = velocity
    if (typeof v !== "number") return { error: "velocity must be a number 0–127" }
    if (v < 0)   v = 0
    if (v > 127) v = 127

    try {
        s.startCmd("set note velocity")
        targetNote.veloType     = USER_VAL    // must come before userVelocity takes effect
        targetNote.userVelocity = v
        s.endCmd()
        return { ok: true, velocity: v }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "setNoteVelocity failed: " + e }
    }
}

// ── BATCH 7: get_spanners_in_range ───────────────────────────────────────

// Enumerate spanners (hairpins, slurs, ottavas, etc.) intersecting a measure
// range. curScore.spanners is a QQmlListProperty<apiv1::Spanner> (score.h:203,
// added in 4.7) — iterable via .length / [i] in QML JS.
//
// Spanner inherits from EngravingItem, so its position is exposed as
// `spannerTick` (start) + `spannerTicks` (duration as a Fraction), and the
// usual `track` / `staffIdx` / `visible` / `subtypeName()` come from the base.
// End tick = spannerTick + spannerTicks (NOT a separate tick2 property in
// the apiv1 wrapper).
function getSpannersInRange(startMeasure, endMeasure, instrument) {
    var s = _score()
    if (!s) return { error: "No score open" }

    var startM = _findMeasure(startMeasure)
    var endM   = _findMeasure(endMeasure)
    if (!startM) return { error: "Start measure " + startMeasure + " not found" }
    if (!endM)   return { error: "End measure "   + endMeasure   + " not found" }

    var startTick = _getTickInt(startM.firstSegment.tick)
    var endTick   = endM.nextMeasure
        ? _getTickInt(endM.nextMeasure.firstSegment.tick)
        : _getTickInt(endM.lastSegment.tick) + 1

    var filterName = instrument ? String(instrument).toLowerCase() : null

    // Precompute globalStaff → instrument longName (matches getNotesInRange).
    var parts = s.parts
    var staffNameMap = []
    for (var pi = 0; pi < parts.length; pi++) {
        var pp    = parts[pi]
        var lName = pp.longName || pp.partName || ""
        var nStv  = Math.floor((pp.endTrack - pp.startTrack) / 4)
        for (var si = 0; si < nStv; si++) staffNameMap.push(lName)
    }

    var results = []
    var seen = {}   // dedupe key "startTick:type:staff"
    var pushSpanner = function(spStart, spEnd, spStaffIdx, spType, visibleFlag) {
        if (spStart < 0) return
        if (spEnd <= startTick || spStart >= endTick) return
        var globalStaff = spStaffIdx + 1
        var instrName = staffNameMap[globalStaff - 1] || ""
        if (filterName && instrName.toLowerCase().indexOf(filterName) < 0) return
        var key = spStart + ":" + spType + ":" + globalStaff
        if (seen[key]) return
        seen[key] = true
        results.push({
            type:         spType,
            startMeasure: _tickToMeasureNo(spStart),
            endMeasure:   _tickToMeasureNo(spEnd > spStart ? spEnd - 1 : spStart),
            staff:        globalStaff,
            instrument:   instrName,
            visible:      visibleFlag
        })
    }

    // Primary path: curScore.spanners (QQmlListProperty<Spanner>, MS 4.7+).
    var spanners = null
    try { spanners = s.spanners } catch (e) {}
    var nSpanners = (spanners && spanners.length !== undefined) ? spanners.length : 0
    for (var i = 0; i < nSpanners; i++) {
        var sp = spanners[i]
        if (!sp) continue
        var spStart = -1, spDur = 0, spStaffIdx = 0
        try { spStart = _getTickInt(sp.spannerTick) } catch (e) {}
        try { spDur   = _getTickInt(sp.spannerTicks) } catch (e) {}
        try { spStaffIdx = sp.staffIdx } catch (e) {}
        var spType = ""
        try { spType = String(sp.subtypeName() || "") } catch (e) {}
        if (!spType) { try { spType = "type=" + String(sp.type) } catch (e) {} }
        pushSpanner(spStart, spStart + spDur, spStaffIdx, spType,
                    (sp.visible !== false))
    }

    // Fallback path: walk every note in the range and pull forward spanners
    // off note.spannerForward (apiv1 elements.h:1377). Catches the cases
    // where curScore.spanners returns empty — observed in smoke test v0.5.1
    // where slurs and hairpins were confirmed present but s.spanners.length
    // came back 0. Note-anchored spanners (slurs, ties, glissandi) appear
    // here; chord-rest-anchored spanners (hairpins, ottavas) generally do
    // not — those rely on the primary path above.
    var ELEM = api.engraving.Element
    var CHORD = ELEM ? ELEM.CHORD : -1
    var mIter = s.firstMeasure
    var idx = 1
    while (mIter) {
        var mTick = _getTickInt(mIter.firstSegment.tick)
        if (mTick >= endTick) break
        if (idx >= startMeasure && idx <= endMeasure) {
            var seg = mIter.firstSegment
            while (seg) {
                if (seg.segmentType & 8192) {   // ChordRest
                    for (var t = 0; t < s.ntracks; t++) {
                        var el = seg.elementAt(t)
                        if (!el || el.type !== CHORD) continue
                        var notes = el.notes
                        var nN = notes ? notes.length : 0
                        for (var ni = 0; ni < nN; ni++) {
                            var note = notes[ni]
                            var fwd = null
                            try { fwd = note.spannerForward } catch (e) {}
                            if (!fwd || fwd.length === undefined) continue
                            for (var fi = 0; fi < fwd.length; fi++) {
                                var fsp = fwd[fi]
                                if (!fsp) continue
                                var fStart = -1, fDur = 0, fStaff = Math.floor(t / 4)
                                try { fStart = _getTickInt(fsp.spannerTick) } catch (e) {}
                                try { fDur   = _getTickInt(fsp.spannerTicks) } catch (e) {}
                                if (fStart < 0) {
                                    try { fStart = _getTickInt(seg.tick) } catch (e) {}
                                }
                                var fType = ""
                                try { fType = String(fsp.subtypeName() || "") } catch (e) {}
                                if (!fType) { try { fType = "type=" + String(fsp.type) } catch (e) {} }
                                pushSpanner(fStart, fStart + fDur, fStaff, fType,
                                            (fsp.visible !== false))
                            }
                        }
                    }
                }
                seg = seg.nextInMeasure ? seg.nextInMeasure : null
            }
        }
        idx++
        if (idx > endMeasure) break
        mIter = mIter.nextMeasure
    }

    return { ok: true, spanners: results }
}

// ── BATCH 8: set_midi_channel_settings ───────────────────────────────────

// Write MIDI channel parameters for an instrument channel. Partial update —
// only fields present on `settings` are written. Wrapped in startCmd/endCmd
// since these are direct property writes (no cmd path exists).
//
// Channel lookup mirrors getMidiChannelSettings: walk parts → instruments →
// channels with the Qt-model-vs-plain-array fallback. `chFilter === "normal"`
// also accepts the first channel of an instrument when no channel of that
// name is present (the unnamed primary channel).
function setMidiChannelSettings(instrument, channelName, settings) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (!instrument) return { error: "instrument is required" }
    if (!settings) return { error: "settings is required" }

    var filterName = String(instrument).toLowerCase()
    var chFilter   = String(channelName || "normal").toLowerCase()

    var targetCh = null
    var parts = s.parts
    for (var pi = 0; pi < parts.length && !targetCh; pi++) {
        var part = parts[pi]
        var pName = (part.longName || part.shortName || "").toLowerCase()
        if (pName.indexOf(filterName) < 0) continue

        var insts = part.instruments
        if (!insts) continue
        var nInsts = insts.length !== undefined ? insts.length : 0
        for (var ii = 0; ii < nInsts && !targetCh; ii++) {
            var inst = insts[ii]
            if (!inst && typeof insts.get === "function") {
                try { inst = insts.get(ii) } catch (e) {}
            }
            if (!inst) continue
            var channels = inst.channels
            if (!channels) continue
            var nChan = channels.length !== undefined ? channels.length : 0
            for (var ci = 0; ci < nChan; ci++) {
                var ch = channels[ci]
                if (!ch && typeof channels.get === "function") {
                    try { ch = channels.get(ci) } catch (e) {}
                }
                if (!ch) continue
                var cName = (ch.name || "normal").toLowerCase()
                if (cName === chFilter || (chFilter === "normal" && ci === 0)) {
                    targetCh = ch
                    break
                }
            }
        }
    }
    if (!targetCh) return { error: "Channel not found for instrument '" + instrument + "' channel '" + channelName + "'" }

    var updated = []
    try {
        s.startCmd("set MIDI channel settings")
        if (settings.volume      !== undefined) { targetCh.volume      = settings.volume;      updated.push("volume") }
        if (settings.pan         !== undefined) { targetCh.pan         = settings.pan;         updated.push("pan") }
        if (settings.chorus      !== undefined) { targetCh.chorus      = settings.chorus;      updated.push("chorus") }
        if (settings.reverb      !== undefined) { targetCh.reverb      = settings.reverb;      updated.push("reverb") }
        if (settings.mute        !== undefined) { targetCh.mute        = !!settings.mute;      updated.push("mute") }
        if (settings.midiProgram !== undefined) { targetCh.midiProgram = settings.midiProgram; updated.push("midiProgram") }
        if (settings.midiBank    !== undefined) { targetCh.midiBank    = settings.midiBank;    updated.push("midiBank") }
        s.endCmd()
        return { ok: true, updated: updated }
    } catch (e) {
        try { s.endCmd(true) } catch (ee) {}
        return { error: "setMidiChannelSettings failed: " + e }
    }
}
