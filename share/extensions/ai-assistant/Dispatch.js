// Dispatch.js — maps an LLM tool-call (name + args) to a ScoreAccess function.
//
// `scoreAccess` is injected by the caller (Main.qml) — passing it explicitly
// avoids JS-resource scoping issues: this file is NOT `.pragma library`
// (and so cannot `.import` other JS files), because ScoreAccess.js itself
// cannot be `.pragma library` (it needs the QML scope to reach `api`).
//
// Returns the ScoreAccess result object directly: `{ ok: true, ... }` or a
// value-shaped object on success, `{ error: "..." }` on failure. Unknown
// tools and uncaught exceptions both surface as `{ error: "..." }` so the
// conversation never dies on a bad tool call.

function dispatchTool(scoreAccess, name, args) {
    try {
        var a = args || {}
        if (name === "get_score_info")       return scoreAccess.getScoreInfo()
        if (name === "get_structure")        return scoreAccess.getStructure(a.startMeasure, a.endMeasure)
        if (name === "add_rehearsal_mark")   return scoreAccess.addRehearsalMark(a.measure, a.text)
        if (name === "get_notes_in_range")   return scoreAccess.getNotesInRange(a.startMeasure, a.endMeasure, a.startStaff, a.endStaff, a.voice)
        if (name === "get_harmony_in_range") return scoreAccess.getHarmonyInRange(a.startMeasure, a.endMeasure)
        if (name === "get_lyrics_in_range")  return scoreAccess.getLyricsInRange(a.startMeasure, a.endMeasure, a.startStaff, a.endStaff)

        // ── Batch 3 write tools ──
        if (name === "add_dynamic")          return scoreAccess.addDynamic(a.measure, a.beat, a.beatFraction || "0", a.staff, a.dynamic)
        if (name === "add_tempo_mark")       return scoreAccess.addTempoMark(a.measure, a.bpm, a.unit || "quarter", a.text || "")
        if (name === "add_staff_text")       return scoreAccess.addStaffText(a.measure, a.beat, a.beatFraction || "0", a.staff, a.text, a.textType || "staff")
        if (name === "add_system_text")      return scoreAccess.addSystemText(a.measure, a.text)
        if (name === "add_harmony")          return scoreAccess.addHarmony(a.measure, a.beat, a.beatFraction || "0", a.staff, a.text)
        // endStaff defaults to startStaff: LLMs frequently omit it on single-staff
        // spans ("hairpin on staff 1"), and a missing endStaff propagated as
        // undefined into selectRange silently dropped the cmd.
        if (name === "add_hairpin")          return scoreAccess.addHairpin(a.startMeasure, a.startBeat, a.startBeatFraction || "0", a.startStaff, a.endMeasure, a.endBeat, a.endBeatFraction || "0", a.endStaff || a.startStaff, a.type)
        if (name === "add_slur")             return scoreAccess.addSlur(a.startMeasure, a.startBeat, a.startBeatFraction || "0", a.startStaff, a.endMeasure, a.endBeat, a.endBeatFraction || "0", a.endStaff || a.startStaff)
        if (name === "add_ottava")           return scoreAccess.addOttava(a.startMeasure, a.startBeat, a.startBeatFraction || "0", a.startStaff, a.endMeasure, a.endBeat, a.endBeatFraction || "0", a.endStaff || a.startStaff, a.type)
        if (name === "insert_measures")      return scoreAccess.insertMeasures(a.afterMeasure, a.count)
        if (name === "append_measures")      return scoreAccess.appendMeasures(a.count)
        if (name === "delete_measure")       return scoreAccess.deleteMeasure(a.measure)
        if (name === "add_section_break")    return scoreAccess.addSectionBreak(a.measure)
        if (name === "add_system_break")     return scoreAccess.addSystemBreak(a.measure)
        if (name === "add_page_break")       return scoreAccess.addPageBreak(a.measure)
        if (name === "add_key_signature")    return scoreAccess.addKeySignature(a.measure, a.key)
        if (name === "add_time_signature")   return scoreAccess.addTimeSignature(a.measure, a.numerator, a.denominator)
        if (name === "add_clef")             return scoreAccess.addClef(a.measure, a.beat || 1, a.beatFraction || "0", a.staff || 1, a.clefType)
        if (name === "add_fingering")        return scoreAccess.addFingering(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice || 1, a.finger, a.pitch || null)
        if (name === "add_string_number")    return scoreAccess.addStringNumber(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice || 1, a.stringNumber, a.pitch || null)
        if (name === "set_score_metadata")   return scoreAccess.setScoreMetadata(a.title || "", a.composer || "", a.lyricist || "", a.copyright || "", a.subtitle || "")

        // ── Diagnostic ──
        if (name === "get_debug_info")       return scoreAccess.getDebugInfo()
        if (name === "probe_clef_type_enum") return scoreAccess.probeClefTypeEnum()

        // ── Batch 4 tools ──
        if (name === "get_score_metadata")   return scoreAccess.getScoreMetadata()
        if (name === "get_key_at")           return scoreAccess.getKeyAt(a.measure)
        if (name === "get_time_sig_at")      return scoreAccess.getTimeSigAt(a.measure)
        if (name === "add_note")             return scoreAccess.addNote(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.pitch, a.duration)
        if (name === "add_note_to_chord")    return scoreAccess.addNoteToChord(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.pitch)
        if (name === "add_rest")             return scoreAccess.addRest(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.duration)
        if (name === "add_lyric")            return scoreAccess.addLyric(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.text, a.syllabic || "single", a.verse || 1)
        if (name === "add_tie")              return scoreAccess.addTie(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice)
        if (name === "add_articulation")     return scoreAccess.addArticulation(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.articulation)

        // ── Batch 5 tools ──
        if (name === "get_measure")          return scoreAccess.getMeasure(a.measure)
        if (name === "set_note_pitch")       return scoreAccess.setNotePitch(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.oldPitch || null, a.newPitch)
        if (name === "set_note_duration")    return scoreAccess.setNoteDuration(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice, a.duration)
        if (name === "add_fermata")          return scoreAccess.addFermata(a.measure, a.beat, a.beatFraction || "0", a.staff, a.type || "normal")

        // ── Batch 6 tools ──
        if (name === "get_selection")              return scoreAccess.getSelection()
        if (name === "get_view_settings")          return scoreAccess.getViewSettings()
        if (name === "get_midi_channel_settings")  return scoreAccess.getMidiChannelSettings(a.instrument || null)
        // set_view_settings: LLM may nest under `settings` or pass top-level fields; accept both.
        if (name === "set_view_settings")          return scoreAccess.setViewSettings(a.settings || a)
        if (name === "set_note_accidental")        return scoreAccess.setNoteAccidental(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice || 1, a.pitch || null, a.accidental)
        if (name === "set_note_velocity")          return scoreAccess.setNoteVelocity(a.measure, a.beat, a.beatFraction || "0", a.staff, a.voice || 1, a.pitch || null, a.velocity)

        // ── Batch 7 tools ──
        if (name === "get_spanners_in_range")      return scoreAccess.getSpannersInRange(a.startMeasure, a.endMeasure, a.instrument || null)
        if (name === "get_clef_at")                return scoreAccess.getClefAt(a.measure, a.staff || 1)
        if (name === "get_chord_symbol_spelling")  return scoreAccess.getChordSymbolSpelling()
        if (name === "get_concert_pitch")          return scoreAccess.getConcertPitch()

        // ── Batch 8 tools ──
        if (name === "set_midi_channel_settings")  return scoreAccess.setMidiChannelSettings(a.instrument, a.channelName || "normal", a)

        return { error: "Unknown tool: " + name }
    } catch(e) {
        return { error: "dispatchTool exception: " + e }
    }
}
