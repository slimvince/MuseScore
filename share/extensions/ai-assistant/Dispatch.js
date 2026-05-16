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
        return { error: "Unknown tool: " + name }
    } catch(e) {
        return { error: "dispatchTool exception: " + e }
    }
}
