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
        c.add(d)                  // real-parent FIRST
        d.dynamicType = dynType   // THEN set properties
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

    try {
        s.startCmd(cmdLabel)
        s.selection.selectRange(startTick, endTick, s0, s1)
        api.engraving.cmd(cmdStr)
        s.endCmd()
        return { ok: true }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
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

    try {
        s.startCmd("insert measures")
        if (tick >= 0) {
            var c = s.newCursor()
            c.track = 0
            c.rewindToTick(tick)
        }
        for (var i = 0; i < count; i++) {
            api.engraving.cmd("insert-measure")
        }
        s.endCmd()
        return { ok: true, inserted: count, afterMeasure: afterMeasure }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
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
    var endTick
    if (m.nextMeasure) {
        endTick = _getTickInt(m.nextMeasure.firstSegment.tick) - 1
    } else {
        endTick = _getTickInt(m.lastSegment.tick) + 1
    }

    try {
        s.startCmd("delete measure")
        s.selection.selectRange(startTick, endTick, 0, s.nstaves)
        api.engraving.cmd("time-delete")
        s.endCmd()
        return { ok: true, deletedMeasure: measureNo }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: "deleteMeasure failed: " + e }
    }
}

// Helper for breaks: select the full measure across all staves, then cmd().
function _measureBreakCmd(cmdLabel, cmdStr, measureNo) {
    var s = _score()
    if (!s) return { error: "No score open" }
    var m = _findMeasure(measureNo)
    if (!m) return { error: "Measure " + measureNo + " not found" }
    var startTick = _getTickInt(m.firstSegment.tick)
    var endTick = m.nextMeasure
        ? _getTickInt(m.nextMeasure.firstSegment.tick) - 1
        : _getTickInt(m.lastSegment.tick) + 1

    try {
        s.startCmd(cmdLabel)
        s.selection.selectRange(startTick, endTick, 0, s.nstaves)
        api.engraving.cmd(cmdStr)
        s.endCmd()
        return { ok: true, measure: measureNo }
    } catch(e) {
        try { s.endCmd(true) } catch(ee) {}
        return { error: cmdLabel + " failed: " + e }
    }
}

// Section break at end of a measure.
function addSectionBreak(measureNo) {
    return _measureBreakCmd("add section break", "section-break", measureNo)
}

// System break at end of a measure.
function addSystemBreak(measureNo) {
    return _measureBreakCmd("add system break", "system-break", measureNo)
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
