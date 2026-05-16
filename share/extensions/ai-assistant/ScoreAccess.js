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
    while (m) {
        if (m.measureNumber === n) return m
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
            for (var i = 0; i < parts.length; i++) {
                var p = parts[i]
                info.parts.push({
                    name:       p.partName  || p.longName || "",
                    shortName:  p.shortName || "",
                    staves:     (p.staves && p.staves.length) ? p.staves.length : 1,
                    startTrack: p.startTrack,
                    endTrack:   p.endTrack
                })
            }
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

        while (m) {
            var n = m.measureNumber
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
            m = m.nextMeasure
        }
        return out
    } catch(e) {
        return { error: "getStructure failed: " + e }
    }
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
        // m.tick is a Fraction; the cursor accepts either rewindToTick(int) or
        // rewindToFraction(Fraction). The Fraction object has a .ticks property
        // exposing the int form. Use rewindToTick for consistency with the
        // documented pattern in api_write.md.
        var tickInt = (m.tick && typeof m.tick.ticks === "number") ? m.tick.ticks : 0
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
