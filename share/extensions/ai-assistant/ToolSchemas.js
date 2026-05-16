// ToolSchemas.js — JSON tool schemas in the three provider formats.
//
// The provider-neutral core (name, description, parameters) is defined once
// and then wrapped per provider. Call getToolSchemas("anthropic" | "openai" |
// "gemini") to get the array shaped for that provider's tool-call API.
//
// Adding a tool: append a CORE entry, then re-deploy. No code in this file
// depends on tool name or argument shape.
//
// NOTE: kept without `.pragma library` for consistency with the other modules
// — none of them are library-mode (see ScoreAccess.js for why).

// Anthropic format: top-level array of { name, description, input_schema }.
function _toAnthropic(t) {
    return { name: t.name, description: t.description, input_schema: t.parameters }
}

// OpenAI / custom format: array of { type: "function", function: {...} }.
function _toOpenAI(t) {
    return {
        type: "function",
        function: { name: t.name, description: t.description, parameters: t.parameters }
    }
}

// Gemini format: nested under tools: [{ functionDeclarations: [...] }].
// Returning the inner declarations only — Main.qml wraps them.
function _toGemini(t) {
    var p = { type: "object", properties: t.parameters.properties || {} }
    if (t.parameters.required && t.parameters.required.length > 0) p.required = t.parameters.required
    var decl = { name: t.name, description: t.description }
    if (Object.keys(p.properties).length > 0) decl.parameters = p
    return decl
}

function getToolSchemas(providerFormat) {
    // CORE lives inside this function (not at module level) because QML's JS
    // import scope does not reliably initialise module-level `var` arrays
    // before the first call site — moving it in here forces evaluation at
    // call time, which is when `api`/`curScore` are also reachable.
    var CORE = [
        {
            name: "get_score_info",
            description:
                "Returns basic metadata about the open score: title, composer, lyricist, " +
                "copyright, subtitle, measure count, duration (seconds), initial key/time/tempo, " +
                "and the list of parts (instruments). Use this when the user asks about the score " +
                "in general terms (\"what is this piece?\", \"who composed it?\", \"how long is it?\"). " +
                "Each part includes firstStaff (global 1-based staff number from the top of the score) " +
                "— use this value with get_notes_in_range and get_lyrics_in_range to target a specific staff.",
            parameters: {
                type: "object",
                properties: {},
                required: []
            }
        },
        {
            name: "get_structure",
            description:
                "Returns a per-measure structural snapshot covering the requested range. For each " +
                "measure, reports any change in key signature, time signature, tempo marking, or " +
                "rehearsal mark. Use this to find a specific section (\"where does the B section start?\"), " +
                "to list rehearsal letters, or to detect tempo/key changes. Measures are 1-based. " +
                "Both bounds are optional — default is the whole score.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure: { type: "integer", description: "First measure (1-based, inclusive). Default: 1." },
                    endMeasure:   { type: "integer", description: "Last measure (1-based, inclusive). Default: last measure." }
                },
                required: []
            }
        },
        {
            name: "add_rehearsal_mark",
            description:
                "Inserts a rehearsal mark at the start of the given measure. The change is undoable " +
                "with Ctrl+Z. Use this when the user asks to label a section (\"add rehearsal mark A " +
                "at bar 17\", \"mark the chorus\").",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "Measure number, 1-based." },
                    text:    { type: "string",  description: "Rehearsal mark text, e.g. \"A\", \"B\", \"Verse\", \"Chorus\"." }
                },
                required: ["measure", "text"]
            }
        },
        {
            name: "get_notes_in_range",
            description:
                "Returns all notes and rests in the given measure range. Use startStaff/endStaff " +
                "(global 1-based staff numbers from get_score_info) to filter by staff — this is the " +
                "only reliable way to target a specific instrument when a score has multiple staves " +
                "with the same name. Omit staff filters to read all staves. Optional voice filter (1–4).",
            parameters: {
                type: "object",
                properties: {
                    startMeasure: { type: "integer", description: "First measure to include (1-based, inclusive)." },
                    endMeasure:   { type: "integer", description: "Last measure to include (1-based, inclusive)." },
                    startStaff:   { type: "integer", description: "Global staff number of the first staff to include (1 = top staff of the score). Obtain staff numbers from get_score_info (firstStaff field). Omit to include all staves." },
                    endStaff:     { type: "integer", description: "Global staff number of the last staff to include (inclusive). Set equal to startStaff for a single staff. Omit to include through the last staff." },
                    voice:        { type: "integer", description: "Voice 1–4; omit for all voices." }
                },
                required: ["startMeasure", "endMeasure"]
            }
        },
        {
            name: "get_harmony_in_range",
            description:
                "Returns all chord symbols (harmony markings) in the given measure range.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure: { type: "integer", description: "First measure to include (1-based, inclusive)." },
                    endMeasure:   { type: "integer", description: "Last measure to include (1-based, inclusive)." }
                },
                required: ["startMeasure", "endMeasure"]
            }
        },
        {
            name: "get_lyrics_in_range",
            description:
                "Returns all lyrics in the given measure range, with syllabic type " +
                "(single/begin/middle/end) and verse number.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure: { type: "integer", description: "First measure to include (1-based, inclusive)." },
                    endMeasure:   { type: "integer", description: "Last measure to include (1-based, inclusive)." },
                    startStaff:   { type: "integer", description: "Global staff number of the first staff to include. Obtain from get_score_info (firstStaff field). Omit for all staves." },
                    endStaff:     { type: "integer", description: "Global staff number of the last staff to include (inclusive). Omit for all remaining staves." }
                },
                required: ["startMeasure", "endMeasure"]
            }
        },

        // ── BATCH 3 WRITE TOOLS ────────────────────────────────────────────

        {
            name: "add_dynamic",
            description:
                "Adds a dynamic marking (ppp, pp, p, mp, mf, f, ff, fff, fp, sf, sfz, fz, rfz, sfp) " +
                "at a specific beat position in the score. Dynamics apply to a staff. Use " +
                "get_score_info first to get the correct global staff number.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number within the measure." },
                    beatFraction: { type: "string",  description: "Sub-beat offset as a fraction string: '0', '1/2', '1/4', '3/4', '1/3', '2/3'. Omit or use '0' for the exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    dynamic:      { type: "string",  enum: ["ppp","pp","p","mp","mf","f","ff","fff","fp","sf","sfz","fz","rfz","sfp"], description: "The dynamic marking." }
                },
                required: ["measure", "beat", "staff", "dynamic"]
            }
        },
        {
            name: "add_tempo_mark",
            description:
                "Adds a tempo marking at the start of a measure, setting the playback BPM. " +
                "Use for metronome marks (e.g. '♩=120') with an optional text label (e.g. " +
                "'Allegro'). Always positioned at beat 1 of the given measure.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." },
                    bpm:     { type: "integer", description: "Beats per minute (e.g. 120)." },
                    unit:    { type: "string",  description: "Beat unit for the metronome mark: 'quarter', 'half', 'eighth', 'dotted quarter', 'dotted half'. Defaults to 'quarter'." },
                    text:    { type: "string",  description: "Optional text label e.g. 'Allegro', 'Andante con moto'. Omit to show only the metronome mark." }
                },
                required: ["measure", "bpm"]
            }
        },
        {
            name: "add_staff_text",
            description:
                "Adds a staff text annotation (free text) above a specific staff at a beat " +
                "position. Visible above the staff only. Use for performance instructions " +
                "specific to one instrument.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset string: '0', '1/2', '1/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    text:         { type: "string",  description: "The text to add." }
                },
                required: ["measure", "beat", "staff", "text"]
            }
        },
        {
            name: "add_system_text",
            description:
                "Adds a system text annotation that appears above all staves (applies to the " +
                "whole ensemble). Positioned at the start of the given measure. Use for " +
                "instructions that affect all instruments (e.g. 'D.C. al Fine', 'Coda', 'Segue').",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." },
                    text:    { type: "string",  description: "The text to add." }
                },
                required: ["measure", "text"]
            }
        },
        {
            name: "add_harmony",
            description:
                "Adds a chord symbol (harmony) at a specific beat position above a staff. " +
                "Examples: 'C', 'Cmaj7', 'Fm', 'G7/B', 'Bdim7'. Use get_score_info first " +
                "to determine the correct staff number.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset string: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    text:         { type: "string",  description: "Chord symbol string e.g. 'Cmaj7', 'Fm', 'G7/B'." }
                },
                required: ["measure", "beat", "staff", "text"]
            }
        },
        {
            name: "add_hairpin",
            description:
                "Adds a crescendo or decrescendo hairpin spanning from a start position to an " +
                "end position. Both positions include a measure number, beat, and staff. " +
                "Hairpins span a single staff.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure:      { type: "integer", description: "1-based start measure number." },
                    startBeat:         { type: "integer", description: "1-based start beat." },
                    startBeatFraction: { type: "string",  description: "Sub-beat offset at start: '0', '1/2', etc." },
                    startStaff:        { type: "integer", description: "Global 1-based staff number for the start (from get_score_info)." },
                    endMeasure:        { type: "integer", description: "1-based end measure number." },
                    endBeat:           { type: "integer", description: "1-based end beat." },
                    endBeatFraction:   { type: "string",  description: "Sub-beat offset at end: '0', '1/2', etc." },
                    endStaff:          { type: "integer", description: "Global 1-based staff number for the end. Usually the same as startStaff." },
                    type:              { type: "string",  enum: ["cresc", "decresc"], description: "Hairpin direction: 'cresc' for crescendo (gets louder), 'decresc' for decrescendo (gets quieter)." }
                },
                required: ["startMeasure", "startBeat", "startStaff", "endMeasure", "endBeat", "endStaff", "type"]
            }
        },
        {
            name: "add_slur",
            description:
                "Adds a slur from one note position to another. A slur is a curved line " +
                "indicating legato playing — it is different from a tie. Slurs span a single staff.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure:      { type: "integer", description: "1-based start measure number." },
                    startBeat:         { type: "integer", description: "1-based start beat." },
                    startBeatFraction: { type: "string",  description: "Sub-beat offset at start." },
                    startStaff:        { type: "integer", description: "Global 1-based staff number." },
                    endMeasure:        { type: "integer", description: "1-based end measure number." },
                    endBeat:           { type: "integer", description: "1-based end beat." },
                    endBeatFraction:   { type: "string",  description: "Sub-beat offset at end." },
                    endStaff:          { type: "integer", description: "Global 1-based staff number. Usually same as startStaff." }
                },
                required: ["startMeasure", "startBeat", "startStaff", "endMeasure", "endBeat", "endStaff"]
            }
        },
        {
            name: "add_ottava",
            description:
                "Adds an ottava line (8va or 8vb) spanning from one position to another. " +
                "8va: play one octave higher than written. 8vb: play one octave lower than written.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure:      { type: "integer", description: "1-based start measure number." },
                    startBeat:         { type: "integer", description: "1-based start beat." },
                    startBeatFraction: { type: "string",  description: "Sub-beat offset at start." },
                    startStaff:        { type: "integer", description: "Global 1-based staff number." },
                    endMeasure:        { type: "integer", description: "1-based end measure number." },
                    endBeat:           { type: "integer", description: "1-based end beat." },
                    endBeatFraction:   { type: "string",  description: "Sub-beat offset at end." },
                    endStaff:          { type: "integer", description: "Global 1-based staff number." },
                    type:              { type: "string",  enum: ["8va", "8vb"], description: "'8va' = one octave higher, '8vb' = one octave lower." }
                },
                required: ["startMeasure", "startBeat", "startStaff", "endMeasure", "endBeat", "endStaff", "type"]
            }
        },
        {
            name: "insert_measures",
            description:
                "Inserts empty measures into the score after a given measure. Use afterMeasure=0 " +
                "to insert before measure 1. Existing measures shift right. The new measures " +
                "are empty.",
            parameters: {
                type: "object",
                properties: {
                    afterMeasure: { type: "integer", description: "Insert after this measure (1-based). Use 0 to insert before the first measure." },
                    count:        { type: "integer", description: "Number of empty measures to insert (minimum 1)." }
                },
                required: ["afterMeasure", "count"]
            }
        },
        {
            name: "append_measures",
            description: "Appends empty measures at the end of the score.",
            parameters: {
                type: "object",
                properties: {
                    count: { type: "integer", description: "Number of empty measures to append (minimum 1)." }
                },
                required: ["count"]
            }
        },
        {
            name: "delete_measure",
            description:
                "Deletes a measure and all its content from the score. Subsequent measures " +
                "shift left. This cannot be undone via the tool — the user must use Ctrl+Z.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number to delete." }
                },
                required: ["measure"]
            }
        },
        {
            name: "add_section_break",
            description:
                "Adds a section break at the end of a measure. A section break causes a gap " +
                "in the score layout between systems and resets instrument spacing. It does " +
                "not create a repeat or jump — it is purely a layout/separator element.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number after which to add the section break." }
                },
                required: ["measure"]
            }
        },
        {
            name: "add_system_break",
            description:
                "Adds a system break at the end of a measure, forcing the next measure to " +
                "start on a new system (line). Useful for controlling score layout.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number after which to add the system break." }
                },
                required: ["measure"]
            }
        },
        {
            name: "set_score_metadata",
            description:
                "Sets score metadata fields (title, composer, lyricist, copyright, subtitle). " +
                "Only fields you provide are updated; omit fields you want to leave unchanged.",
            parameters: {
                type: "object",
                properties: {
                    title:     { type: "string", description: "Score title (workTitle)." },
                    composer:  { type: "string", description: "Composer name." },
                    lyricist:  { type: "string", description: "Lyricist name." },
                    copyright: { type: "string", description: "Copyright string." },
                    subtitle:  { type: "string", description: "Subtitle or opus number (workNumber)." }
                },
                required: []
            }
        },

        // ── DIAGNOSTIC ─────────────────────────────────────────────────────

        {
            name: "get_debug_info",
            description:
                "Returns internal API values and score state for debugging purposes. Call this when you need to verify enum integer values, check which API surfaces are available, or diagnose unexpected tool behaviour. Not for musical use.",
            parameters: { type: "object", properties: {}, required: [] }
        },

        // ── BATCH 4: NOTE ENTRY, LYRICS, ARTICULATIONS, TIE, METADATA READ ─

        {
            name: "get_score_metadata",
            description:
                "Returns the score's writable metadata fields: title, composer, lyricist, copyright, subtitle, arranger, translator. Complement to get_score_info (which returns structural data). Use this before calling set_score_metadata to see what's already set.",
            parameters: { type: "object", properties: {}, required: [] }
        },
        {
            name: "add_note",
            description:
                "Adds a note at a specific position in the score, overwriting any existing note or rest at that location. Use add_note_to_chord to add a pitch to an existing chord without replacing it. Always call get_score_info first to confirm staff numbers.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4', '3/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4. Use 1 unless the user specifies otherwise." },
                    pitch:        { type: "string",  description: "Note name with octave: 'C4', 'F#3', 'Bb5', 'B4'. Middle C = C4." },
                    duration:     { type: "string",  description: "Note duration: 'whole', 'half', 'quarter', 'eighth', '16th', '32nd', '64th', 'dotted half', 'dotted quarter', 'dotted eighth', 'double-dotted quarter', etc." }
                },
                required: ["measure", "beat", "staff", "voice", "pitch", "duration"]
            }
        },
        {
            name: "add_note_to_chord",
            description:
                "Adds a pitch to an existing chord without changing its duration. Use this to build chords note by note. Fails if there is no chord (note) at the given position — use add_note first to create the first note of the chord.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4." },
                    pitch:        { type: "string",  description: "Note to add: 'C4', 'F#3', 'Bb5' etc." }
                },
                required: ["measure", "beat", "staff", "voice", "pitch"]
            }
        },
        {
            name: "add_rest",
            description: "Adds a rest at a specific position, overwriting any existing content.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    voice:        { type: "integer", description: "Voice 1–4." },
                    duration:     { type: "string",  description: "Rest duration: 'whole', 'half', 'quarter', 'eighth', '16th', '32nd', '64th', 'dotted quarter', etc." }
                },
                required: ["measure", "beat", "staff", "voice", "duration"]
            }
        },
        {
            name: "add_lyric",
            description:
                "Adds a lyric syllable to the note/chord at the given position. For multi-syllable words use syllabic to indicate the syllable's position within the word: 'begin' for the first syllable, 'middle' for inner syllables, 'end' for the last, 'single' for a complete word.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    voice:        { type: "integer", description: "Voice 1–4. Lyrics follow the voice of the sung melody." },
                    text:         { type: "string",  description: "The syllable text." },
                    syllabic:     { type: "string",  enum: ["single","begin","middle","end"], description: "'single' = complete word, 'begin' = first syllable of word, 'middle' = inner syllable, 'end' = last syllable." },
                    verse:        { type: "integer", description: "1-based verse number. Defaults to 1 if omitted." }
                },
                required: ["measure", "beat", "staff", "voice", "text", "syllabic"]
            }
        },
        {
            name: "add_tie",
            description:
                "Ties the note at the given position to the next occurrence of the same pitch, indicating that the note is sustained rather than re-attacked. A tie is different from a slur: a tie connects identical pitches; a slur connects different pitches and indicates legato.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    voice:        { type: "integer", description: "Voice 1–4." }
                },
                required: ["measure", "beat", "staff", "voice"]
            }
        },
        {
            name: "add_articulation",
            description:
                "Adds an articulation marking to the note or chord at the given position. Supported articulations: staccato, tenuto, accent, marcato, trill, mordent, turn, upBow, downBow. Other articulations (staccatissimo, fermata variants, snapPizzicato, harmonic, tremolo, etc.) are not yet implemented.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    voice:        { type: "integer", description: "Voice 1–4." },
                    articulation: { type: "string",  enum: ["staccato","tenuto","accent","marcato","trill","mordent","turn","upBow","downBow"], description: "The articulation to add." }
                },
                required: ["measure", "beat", "staff", "voice", "articulation"]
            }
        }
    ]

    var out = []
    for (var i = 0; i < CORE.length; i++) {
        var t = CORE[i]
        if      (providerFormat === "anthropic") out.push(_toAnthropic(t))
        else if (providerFormat === "gemini")    out.push(_toGemini(t))
        else                                     out.push(_toOpenAI(t))   // openai + custom
    }
    return out
}
