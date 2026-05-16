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
    var s = measure.firstSegment
    while (s) {
        var t = _findAnnotation(s, api.engraving.Element.TEMPO_TEXT)
        if (t) return t
        s = s.nextInMeasure
    }
    return null
}

// Find the first RehearsalMark anywhere in a measure's segments.
function _firstRehearsalMarkInMeasure(measure) {
    if (!measure) return null
    var s = measure.firstSegment
    while (s) {
        var r = _findAnnotation(s, api.engraving.Element.REHEARSAL_MARK)
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
// Ticks-per-beat is derived from the time signature denominator at the start
// of the measure (480 ticks/quarter, beat = whole / denominator).
function _posToTick(measureNo, beat, beatFraction) {
    var m = _findMeasure(measureNo)
    if (!m) return -1
    var mTick = _getTickInt(m.firstSegment.tick)
    var tsDen = 4
    var seg = m.firstSegment
    while (seg) {
        // SegmentType::TimeSig = 0x20 (32) — see src/engraving/dom/segment.h
        if (seg.segmentType & 32) {
            try {
                var tsEl = seg.elementAt(0)
                if (tsEl && tsEl.denominator) tsDen = tsEl.denominator
            } catch(e) {}
            break
        }
        seg = seg.nextInMeasure ? seg.nextInMeasure : seg.next
        if (!seg) break
    }
    var tpq = 480
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
    return mTick + offset
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
// Returns an array of { number, keySignature, timeSignature, tempo, rehearsalMark }.
function getStructure(startMeasure, endMeasure) {
    var s = _score()
    if (!s) return { error: "No score open" }

    try {
        var lo = (typeof startMeasure === "number" && startMeasure >= 1) ? startMeasure : 1
        var hi = (typeof endMeasure   === "number" && endMeasure   >= 1) ? endMeasure   : s.nmeasures
        if (hi < lo) { var tmp = lo; lo = hi; hi = tmp }

        var st0 = s.staves && s.staves.length > 0 ? s.staves[0] : null
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
                    var isChord = (el.type === api.engraving.Element.CHORD)
                    var isRest  = (el.type === api.engraving.Element.REST)
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
                        if (el.type !== api.engraving.Element.HARMONY) continue
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
                    if (el.type !== api.engraving.Element.CHORD &&
                        el.type !== api.engraving.Element.REST) continue
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

        var rm = api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)
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
    var dynType = dynamicMap[dynamic]
    var fellBack = false
    if (dynType === undefined) { dynType = 8; fellBack = true }

    var tick = _posToTick(measureNo, beat, beatFraction)
    if (tick < 0) return { error: "Measure " + measureNo + " not found" }

    try {
        s.startCmd("add dynamic")
        var c = s.newCursor()
        c.track = (staff - 1) * 4
        c.rewindToTick(tick)
        var d = api.engraving.newElement(api.engraving.Element.DYNAMIC)
        // EXCEPTION to the add-first-then-set pattern: dynamicType determines
        // which element variant the engraving layer commits, so it must be
        // set BEFORE c.add(). Setting it after produces a hairpin pair instead
        // of the requested glyph (and only the first call works).
        d.dynamicType = dynType
        c.add(d)
        s.endCmd()
        var res = { ok: true, measure: measureNo, beat: beat, dynamic: dynamic }
        if (fellBack) res.note = "Unknown dynamic '" + dynamic + "'; fell back to mf"
        return res
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addDynamic failed: " + e }
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
    if (typeof bpm !== "number" || bpm <= 0)
        return { error: "Invalid bpm: " + bpm }

    var unitLower = (unit || "quarter").toLowerCase()
    var qps = bpm / 60.0
    if      (unitLower === "half")            qps = bpm / 30.0
    else if (unitLower === "eighth")          qps = bpm / 120.0
    else if (unitLower === "dotted quarter")  qps = bpm * 1.5 / 60.0
    else if (unitLower === "dotted half")     qps = bpm * 1.5 / 30.0

    var noteSymbol = "♩"  // ♩
    if      (unitLower === "half")            noteSymbol = "𝅝"        // 𝅝
    else if (unitLower === "eighth")          noteSymbol = "♪"              // ♪
    else if (unitLower === "dotted quarter")  noteSymbol = "♩."
    else if (unitLower === "dotted half")     noteSymbol = "𝅝."

    var displayText = (text ? text + " " : "") + noteSymbol + " = " + bpm

    var m = _findMeasure(measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }
    var mTick = _getTickInt(m.firstSegment.tick)

    try {
        s.startCmd("add tempo")
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(mTick)
        var tt = api.engraving.newElement(api.engraving.Element.TEMPO_TEXT)
        c.add(tt)                    // real-parent FIRST
        tt.text = displayText        // THEN set properties
        tt.tempo = qps
        tt.tempoFollowText = false   // honor .tempo, not text-parse
        s.endCmd()
        return { ok: true, measure: measureNo, bpm: bpm, tempo: qps, text: displayText }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addTempoMark failed: " + e }
    }
}

// Staff text at a (measure, beat) position, voice 1, single staff.
function addStaffText(measureNo, beat, beatFraction, staff, text) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof staff !== "number" || staff < 1)
        return { error: "Invalid staff number: " + staff }
    if (typeof text !== "string" || text.length === 0)
        return { error: "Staff text must be a non-empty string" }

    var tick = _posToTick(measureNo, beat, beatFraction)
    if (tick < 0) return { error: "Measure " + measureNo + " not found" }

    try {
        s.startCmd("add staff text")
        var c = s.newCursor()
        c.track = (staff - 1) * 4
        c.rewindToTick(tick)
        var st = api.engraving.newElement(api.engraving.Element.STAFF_TEXT)
        c.add(st)
        st.text = text
        s.endCmd()
        return { ok: true, measure: measureNo, beat: beat, staff: staff }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addStaffText failed: " + e }
    }
}

// System text at the start of a measure, track 0 (applies to all staves).
function addSystemText(measureNo, text) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof text !== "string" || text.length === 0)
        return { error: "System text must be a non-empty string" }

    var m = _findMeasure(measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }
    var mTick = _getTickInt(m.firstSegment.tick)

    try {
        s.startCmd("add system text")
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(mTick)
        var sysT = api.engraving.newElement(api.engraving.Element.SYSTEM_TEXT)
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
    if (tick < 0) return { error: "Measure " + measureNo + " not found" }

    try {
        s.startCmd("add chord symbol")
        var c = s.newCursor()
        c.track = (staff - 1) * 4
        c.rewindToTick(tick)
        var h = api.engraving.newElement(api.engraving.Element.HARMONY)
        c.add(h)
        h.text = text
        s.endCmd()
        return { ok: true, measure: measureNo, beat: beat, text: text }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "addHarmony failed: " + e }
    }
}

// Helper: range-select + cmd() write — shared by hairpin, slur, ottava.
function _rangeCmdWrite(cmdLabel, cmdStr,
                        startMeasure, startBeat, startBeatFraction, startStaff,
                        endMeasure,   endBeat,   endBeatFraction,   endStaff) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof startStaff !== "number" || startStaff < 1)
        return { error: "Invalid startStaff: " + startStaff }
    if (typeof endStaff !== "number" || endStaff < 1)
        return { error: "Invalid endStaff: " + endStaff }

    var startTick = _posToTick(startMeasure, startBeat, startBeatFraction)
    if (startTick < 0) return { error: "Start measure " + startMeasure + " not found" }
    var endTick   = _posToTick(endMeasure,   endBeat,   endBeatFraction)
    if (endTick < 0)   return { error: "End measure " + endMeasure + " not found" }

    var s0 = startStaff - 1   // inclusive, 0-based
    var s1 = endStaff         // exclusive, 0-based

    // NO startCmd/endCmd here: api.engraving.cmd() handlers run
    // prepareChanges/commitChanges internally, and those become no-ops while
    // the undo stack is locked by an outer startCmd — the cmd silently drops.
    try {
        s.selection.selectRange(startTick, endTick, s0, s1)
        api.engraving.cmd(cmdStr)
        return { ok: true }
    } catch(e) {
        return { error: cmdLabel + " failed: " + e }
    }
}

// Crescendo or decrescendo hairpin spanning two positions on the same staff.
function addHairpin(startMeasure, startBeat, startBeatFraction, startStaff,
                    endMeasure, endBeat, endBeatFraction, endStaff, type) {
    var cmdStr = (type === "decresc") ? "add-hairpin-reverse" : "add-hairpin"
    var res = _rangeCmdWrite("add hairpin", cmdStr,
                             startMeasure, startBeat, startBeatFraction, startStaff,
                             endMeasure, endBeat, endBeatFraction, endStaff)
    if (res.ok) res.type = (type === "decresc") ? "decresc" : "cresc"
    return res
}

// Slur spanning two positions on the same staff.
function addSlur(startMeasure, startBeat, startBeatFraction, startStaff,
                 endMeasure, endBeat, endBeatFraction, endStaff) {
    return _rangeCmdWrite("add slur", "add-slur",
                          startMeasure, startBeat, startBeatFraction, startStaff,
                          endMeasure, endBeat, endBeatFraction, endStaff)
}

// Ottava line (8va or 8vb) spanning two positions on the same staff.
function addOttava(startMeasure, startBeat, startBeatFraction, startStaff,
                   endMeasure, endBeat, endBeatFraction, endStaff, type) {
    var cmdStr = (type === "8vb") ? "add-8vb" : "add-8va"
    var res = _rangeCmdWrite("add ottava", cmdStr,
                             startMeasure, startBeat, startBeatFraction, startStaff,
                             endMeasure, endBeat, endBeatFraction, endStaff)
    if (res.ok) res.type = (type === "8vb") ? "8vb" : "8va"
    return res
}

// Insert `count` empty measures after `afterMeasure`. Pass afterMeasure=0 to
// insert before measure 1. Each iteration calls cmd("insert-measure"), which
// inserts a single measure at the cursor's current measure (pushing subsequent
// measures to the right).
function insertMeasures(afterMeasure, count) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof afterMeasure !== "number" || afterMeasure < 0)
        return { error: "Invalid afterMeasure: " + afterMeasure }
    if (typeof count !== "number" || count < 1)
        return { error: "count must be >= 1" }

    var m
    if (afterMeasure === 0) {
        m = s.firstMeasure
    } else {
        var mAfter = _findMeasure(afterMeasure)
        if (!mAfter) return { error: "Measure " + afterMeasure + " not found" }
        m = mAfter.nextMeasure
    }
    var tick = m ? _getTickInt(m.firstSegment.tick) : -1

    // NO startCmd/endCmd: each cmd("insert-measure") manages its own undo
    // entry. Wrapping locks the stack and makes the inner commits no-op.
    // Trade-off: count>1 produces N undo steps instead of one.
    try {
        if (tick >= 0) {
            var c = s.newCursor()
            c.track = 0
            c.rewindToTick(tick)
        }
        for (var i = 0; i < count; i++) {
            api.engraving.cmd("insert-measure")
        }
        return { ok: true, inserted: count, afterMeasure: afterMeasure }
    } catch(e) {
        return { error: "insertMeasures failed: " + e }
    }
}

// Append `count` empty measures at the end of the score. Wrapped in startCmd/
// endCmd for consistent undo even if curScore.appendMeasures handles undo
// internally — extra wrap is harmless.
function appendMeasures(count) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (typeof count !== "number" || count < 1)
        return { error: "count must be >= 1" }

    try {
        s.startCmd("append measures")
        s.appendMeasures(count)
        s.endCmd()
        return { ok: true, appended: count }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "appendMeasures failed: " + e }
    }
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

    // NO startCmd/endCmd: cmd("time-delete") owns its undo entry.
    try {
        s.selection.selectRange(startTick, endTick, 0, s.nstaves)
        api.engraving.cmd("time-delete")
        return { ok: true, deletedMeasure: measureNo }
    } catch(e) {
        return { error: "deleteMeasure failed: " + e }
    }
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
function _addLayoutBreak(cmdLabel, layoutBreakType, measureNo) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var m = _findMeasure(measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }
    var tickInt = _getTickInt(m.firstSegment.tick)

    try {
        s.startCmd(cmdLabel)
        var c = s.newCursor()
        c.track = 0
        c.rewindToTick(tickInt)
        var lb = api.engraving.newElement(api.engraving.Element.LAYOUT_BREAK)
        lb.layoutBreakType = layoutBreakType
        c.add(lb)
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

// Set score metadata. Empty/null fields are skipped.
function setScoreMetadata(title, composer, lyricist, copyright, subtitle) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var updates = []
    try {
        s.startCmd("set score metadata")
        if (title)     { s.setMetaTag("workTitle",  title);     updates.push("title") }
        if (composer)  { s.setMetaTag("composer",   composer);  updates.push("composer") }
        if (lyricist)  { s.setMetaTag("lyricist",   lyricist);  updates.push("lyricist") }
        if (copyright) { s.setMetaTag("copyright",  copyright); updates.push("copyright") }
        if (subtitle)  { s.setMetaTag("workNumber", subtitle);  updates.push("subtitle") }
        s.endCmd()
        return { ok: true, updated: updates }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "setScoreMetadata failed: " + e }
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
        subtitle:   s.metaTag("workNumber")  || "",
        composer:   s.metaTag("composer")    || "",
        lyricist:   s.metaTag("lyricist")    || "",
        copyright:  s.metaTag("copyright")   || "",
        arranger:   s.metaTag("arranger")    || "",
        translator: s.metaTag("translator")  || ""
    }
}

// Add a note at (measure, beat, beatFraction) on (staff, voice), overwriting
// whatever is there (note or rest). Uses cursor.addNote(midi, false) so the
// cursor does not advance.
function addNote(measure, beat, beatFraction, staff, voice, pitch, duration) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return { error: "Measure " + measure + " not found" }
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }
    var midiPitch = _noteNameToMidi(pitch)
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }
    try {
        s.startCmd("add lyric")
        var c = s.newCursor()
        c.track = (staff - 1) * 4 + (voice - 1)
        c.rewindToTick(tick)
        var chord = c.element
        if (!chord) {
            try { s.endCmd(true) } catch (ee) {}
            return { error: "No element at measure " + measure + " beat " + beat }
        }
        var ly = api.engraving.newElement(api.engraving.Element.LYRICS)
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
function addTie(measure, beat, beatFraction, staff, voice) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return { error: "Measure " + measure + " not found" }
    try {
        var s0 = staff - 1
        s.selection.selectRange(tick, tick + 1, s0, s0 + 1)
        api.engraving.cmd("tie")
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    // ── Direct-construction branch (SymId-keyed; no cmd path exists) ──
    // SymId names verified in src/engraving/api/v1/apitypes.h:
    //   articStaccatissimoAbove   (2369)
    //   pluckedSnapPizzicatoAbove (4267)
    //   stringsHarmonic           (4411)  — no Above variant; bare name
    //   articStressAbove          (2377)
    //   articUnstressAbove        (2385)
    var directSymIds = {
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
            return { error: "No chord at measure " + measure + " beat " + beat }

        try {
            s.startCmd("add articulation")
            var art = api.engraving.newElement(api.engraving.Element.ARTICULATION)
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
    var articulationCmdMap = {
        "staccato": "add-staccato",
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
    try {
        var s0 = staff - 1
        s.selection.selectRange(tick, tick + 1, s0, s0 + 1)
        api.engraving.cmd(cmdStr)
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
        score: curScore ? {
            nstaves:   curScore.nstaves,
            nmeasures: curScore.nmeasures
        } : null
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }
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
            return { error: "No chord at measure " + measure + " beat " + beat }
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

// Change the duration of the chord/rest at the given position. Pitches are
// preserved; only duration changes. Overwrites the position — trailing
// content past the new duration may be overwritten if the new duration is
// longer than the old.
function setNoteDuration(measure, beat, beatFraction, staff, voice, duration) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var tick = _posToTick(measure, beat, beatFraction)
    if (tick < 0) return { error: "Measure " + measure + " not found" }
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    try {
        s.startCmd("add fermata")
        var c = s.newCursor()
        c.track = (staff - 1) * 4       // fermatas attach to the staff, not a voice
        c.rewindToTick(tick)
        var f = api.engraving.newElement(api.engraving.Element.FERMATA)
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

    var result = {
        isRange:      !!isRange,
        elements:     [],
        startMeasure: null,
        endMeasure:   null,
        startStaff:   null,
        endStaff:     null
    }

    if (isRange) {
        try {
            var ss = sel.startSegment
            var es = sel.endSegment
            if (ss) result.startMeasure = _tickToMeasureNo(_getTickInt(ss.tick))
            if (es) result.endMeasure   = _tickToMeasureNo(_getTickInt(es.tick))
        } catch (e) {}
        try {
            if (sel.startStaff !== undefined && sel.startStaff !== null)
                result.startStaff = sel.startStaff + 1
            if (sel.endStaff !== undefined && sel.endStaff !== null)
                result.endStaff = sel.endStaff + 1
        } catch (e) {}
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

    var els = null
    try { els = sel.elements } catch (e) {}
    if (els && els.length > 0) {
        for (var i = 0; i < els.length; i++) {
            var e = els[i]
            if (!e) continue
            var track = (e.track !== undefined && e.track !== null) ? e.track : 0
            var staff = Math.floor(track / 4) + 1
            var voice = (track % 4) + 1
            var tick = -1
            try {
                if (e.tick !== undefined && e.tick !== null) tick = _getTickInt(e.tick)
                else if (e.parent && e.parent.tick !== undefined) tick = _getTickInt(e.parent.tick)
            } catch (e2) {}
            var mno = tick >= 0 ? _tickToMeasureNo(tick) : null
            var instrName = staffNameMap[staff - 1] || ""
            var typeStr = ""
            try { typeStr = String(e.name || e.type || "") } catch (e3) {}
            result.elements.push({
                type:       typeStr,
                measure:    mno,
                staff:      staff,
                voice:      voice,
                instrument: instrName
            })
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

    return {
        layoutMode:            layoutMode,
        showInvisible:         getBool("showInvisible", false),
        showUnprintable:       getBool("showUnprintable", false),
        showFrames:            getBool("showFrames", false),
        showPageBorders:       getBool("showPageBorders", false),
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

// Write score-level display toggles. Two-phase because direct property writes
// need startCmd/endCmd; cmd()-based writes (concertPitch toggle, layoutMode)
// must NOT be wrapped — those handlers own their own undo entry and become
// no-ops when the stack is locked.
function setViewSettings(settings) {
    var s = _score()
    if (!s) return { error: "No score open" }
    if (!settings) return { error: "settings object required" }

    var updated = []
    var anyDirect = (settings.showInvisible       !== undefined) ||
                    (settings.showUnprintable     !== undefined) ||
                    (settings.showFrames          !== undefined) ||
                    (settings.showPageBorders     !== undefined) ||
                    (settings.showSoundFlags      !== undefined) ||
                    (settings.showVerticalFrames  !== undefined) ||
                    (settings.showInstrumentNames !== undefined) ||
                    (settings.markIrregularMeasures !== undefined)

    if (anyDirect) {
        var trySet = function(prop, key) {
            if (settings[key] === undefined) return
            try { s[prop] = !!settings[key]; updated.push(key) } catch (e) {}
        }
        try {
            s.startCmd("set view settings")
            trySet("showInvisible",         "showInvisible")
            trySet("showUnprintable",       "showUnprintable")
            trySet("showFrames",            "showFrames")
            trySet("showPageBorders",       "showPageBorders")
            trySet("showSoundFlags",        "showSoundFlags")
            trySet("showVerticalFrames",    "showVerticalFrames")
            trySet("showInstrumentNames",   "showInstrumentNames")
            trySet("markIrregularMeasures", "markIrregularMeasures")
            s.endCmd()
        } catch (e) {
            try { s.endCmd(true) } catch (ee) {}
            return { error: "setViewSettings phase 1 failed: " + e }
        }
    }

    // Phase 2: cmd()-based writes — NO startCmd wrapper.
    try {
        if (settings.concertPitch !== undefined) {
            var current = !!_styleValue(s, "concertPitch", false)
            if (current !== !!settings.concertPitch) {
                api.engraving.cmd("concert-pitch")
                updated.push("concertPitch")
            }
        }
        if (settings.layoutMode !== undefined) {
            // Registered cmd strings (notationuiactions.cpp:547+):
            //   view-mode-page, view-mode-float, view-mode-continuous, view-mode-single
            // HORIZONTAL_FIXED has no registered cmd path.
            var lmCmds = {
                "page":       "view-mode-page",
                "float":      "view-mode-float",
                "continuous": "view-mode-continuous",
                "single":     "view-mode-single"
            }
            var c = lmCmds[settings.layoutMode]
            if (c) {
                api.engraving.cmd(c)
                updated.push("layoutMode")
            }
        }
    } catch (e) {
        return { error: "setViewSettings phase 2 failed: " + e }
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
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    var c = s.newCursor()
    c.track = (staff - 1) * 4 + ((voice || 1) - 1)
    c.rewindToTick(tick)
    var chord = c.element
    if (!chord || chord.type !== api.engraving.Element.CHORD)
        return { error: "No chord at measure " + measure + " beat " + beat }

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
    if (tick < 0) return { error: "Measure " + measure + " not found" }

    var c = s.newCursor()
    c.track = (staff - 1) * 4 + ((voice || 1) - 1)
    c.rewindToTick(tick)
    var chord = c.element
    if (!chord || chord.type !== api.engraving.Element.CHORD)
        return { error: "No chord at measure " + measure + " beat " + beat }

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

    var spanners = null
    try { spanners = s.spanners } catch (e) { return { error: "curScore.spanners not readable: " + e } }
    if (!spanners) return { ok: true, spanners: [] }
    var nSpanners = (spanners.length !== undefined) ? spanners.length : 0

    var results = []
    for (var i = 0; i < nSpanners; i++) {
        var sp = spanners[i]
        if (!sp) continue

        var spStart = -1, spDur = 0
        try { spStart = _getTickInt(sp.spannerTick) } catch (e) {}
        try { spDur   = _getTickInt(sp.spannerTicks) } catch (e) {}
        if (spStart < 0) continue
        var spEnd = spStart + spDur

        // Range overlap test: spanner intersects [startTick, endTick)
        if (spEnd <= startTick || spStart >= endTick) continue

        var spStaffIdx = 0
        try { spStaffIdx = sp.staffIdx } catch (e) {}
        var globalStaff = spStaffIdx + 1
        var instrName = staffNameMap[globalStaff - 1] || ""

        if (filterName && instrName.toLowerCase().indexOf(filterName) < 0) continue

        var spType = ""
        try { spType = String(sp.subtypeName() || "") } catch (e) {}
        if (!spType) {
            try { spType = "type=" + String(sp.type) } catch (e) {}
        }

        results.push({
            type:         spType,
            startMeasure: _tickToMeasureNo(spStart),
            endMeasure:   _tickToMeasureNo(spEnd > spStart ? spEnd - 1 : spStart),
            staff:        globalStaff,
            instrument:   instrName,
            visible:      (sp.visible !== false)
        })
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
