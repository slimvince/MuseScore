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
                "Adds a tempo marking at the start of a measure. Use this tool for ALL tempo " +
                "indications — both metronome marks (e.g. '♩=120') and tempo words (e.g. " +
                "'Allegro', 'Andante', 'Presto'). Do NOT use add_system_text for tempo words. " +
                "Always positioned at beat 1 of the given measure.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." },
                    bpm:     { type: "integer", description: "Beats per minute (e.g. 120). Required for a metronome mark. Omit when adding a tempo word only (e.g. 'Allegro') — MuseScore will derive playback speed from the word." },
                    unit:    { type: "string",  description: "Beat unit for the metronome mark: 'quarter', 'half', 'eighth', 'dotted quarter', 'dotted half'. Defaults to 'quarter'. Ignored if bpm is omitted." },
                    text:    { type: "string",  description: "Tempo word or label, e.g. 'Allegro', 'Andante con moto'. Required if bpm is omitted. Optional if bpm is provided (shows alongside the metronome mark)." }
                },
                required: ["measure"]
            }
        },
        {
            name: "add_staff_text",
            description:
                "Adds a staff text annotation (free text) above a specific staff at a beat " +
                "position. Visible above the staff only. Use for performance instructions " +
                "specific to one instrument. Set textType='expression' for italic performance " +
                "expression markings (dolce, espressivo, cantabile etc.); default is regular staff text.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset string: '0', '1/2', '1/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    text:         { type: "string",  description: "The text to add." },
                    textType:     { type: "string",  enum: ["staff", "expression"], description: "Text style: 'staff' (default) for regular staff text; 'expression' for italic performance expressions (dolce, espressivo, cantabile etc.)." }
                },
                required: ["measure", "beat", "staff", "text"]
            }
        },
        {
            name: "add_system_text",
            description:
                "Adds a system text annotation that appears above all staves (applies to the " +
                "whole ensemble). Positioned at the start of the given measure. Use for " +
                "rehearsal instructions (e.g. 'D.C. al Fine', 'Coda', 'Segue'). " +
                "Do NOT use for tempo words (Allegro, Andante, Presto, etc.) — use add_tempo_mark for those.",
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
                "8va: play one octave higher than written. 8vb: play one octave lower than written. " +
                "Two-octave variants (15ma, 15mb) are not supported — MuseScore exposes only 8va/8vb " +
                "through the registered command handlers, and constructing a 15ma/15mb spanner directly " +
                "via the cursor does not set up the spanner's end tick.",
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
            name: "add_page_break",
            description:
                "Inserts a page break at the end of the specified measure. Idempotent — does " +
                "nothing if a page break already exists there.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number after which to add the page break." }
                },
                required: ["measure"]
            }
        },
        {
            name: "add_key_signature",
            description:
                "Adds or changes a key signature at the start of a measure. `key` is an integer " +
                "from -7 (7 flats / C♭ major) to +7 (7 sharps / C# major), with 0 being C major / " +
                "A minor. Negative values add flats; positive values add sharps.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." },
                    key:     { type: "integer", minimum: -7, maximum: 7, description: "Integer -7..+7. Negative = flats, positive = sharps, 0 = C major / A minor." }
                },
                required: ["measure", "key"]
            }
        },
        {
            name: "add_time_signature",
            description:
                "Adds or changes a time signature at a measure. Provide `numerator` (beats per " +
                "measure) and `denominator` (beat unit as a power of 2: 2, 4, 8, 16). Changes the " +
                "rhythmic structure of the score from that measure onward.",
            parameters: {
                type: "object",
                properties: {
                    measure:     { type: "integer", description: "1-based measure number." },
                    numerator:   { type: "integer", description: "Beats per measure (e.g. 4 for 4/4, 3 for 3/4, 6 for 6/8)." },
                    denominator: { type: "integer", description: "Beat unit as a power of 2: 2, 4, 8, 16." }
                },
                required: ["measure", "numerator", "denominator"]
            }
        },
        {
            name: "add_clef",
            description:
                "Adds or changes a clef at a position in the score. `clefType` must be one of: " +
                "treble, treble8vb, treble8va, tenor, alto, bass, bass8vb, percussion, tab, tab4. " +
                "Use `beat` and `beatFraction` to place mid-measure clef changes.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number. Defaults to 1." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc. Defaults to '0'." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    clefType:     { type: "string",  enum: ["treble","treble8vb","treble8va","tenor","alto","bass","bass8vb","percussion","tab","tab4"], description: "Clef type." }
                },
                required: ["measure", "staff", "clefType"]
            }
        },
        {
            name: "add_fingering",
            description:
                "Adds a fingering annotation to a note. `finger` is the digit or symbol to " +
                "display (e.g. 1, 2, 3, 4, 5, 0, or classical guitar letters p/i/m/a). " +
                "`pitch` is optional — if the beat contains a chord with multiple notes, " +
                "provide the pitch (e.g. 'C4') to target a specific note; otherwise the " +
                "lowest note is used.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4. Defaults to 1." },
                    finger:       { description: "Fingering digit or symbol. Integer (0–5) or string ('p', 'i', 'm', 'a' etc.)." },
                    pitch:        { type: "string",  description: "Pitch of the note to annotate within a chord (e.g. 'C4'). Omit to target the lowest note." }
                },
                required: ["measure", "beat", "staff", "finger"]
            }
        },
        {
            name: "add_string_number",
            description:
                "Adds a string number annotation to a note (used in string and guitar " +
                "notation). `stringNumber` is 1–6 (or 0 for open string). `pitch` is optional " +
                "— if the beat contains a chord, provide the pitch to target a specific note; " +
                "otherwise the lowest note is used.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4. Defaults to 1." },
                    stringNumber: { type: "integer", description: "String number (1–6, or 0 for open string)." },
                    pitch:        { type: "string",  description: "Pitch of the note to annotate within a chord (e.g. 'C4'). Omit to target the lowest note." }
                },
                required: ["measure", "beat", "staff", "stringNumber"]
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
            name: "get_key_at",
            description:
                "Returns the key signature active at a given measure number. Use this to find out what key a specific section is in — useful when a score has key signature changes mid-piece. Returns { measure, keySignature, fifths } where keySignature is a string like \"C major\" or \"G major\" and fifths is the raw integer (-7..+7, negative = flats, positive = sharps).",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." }
                },
                required: ["measure"]
            }
        },
        {
            name: "get_time_sig_at",
            description:
                "Returns the time signature active at a given measure number. Use this to find the meter at a specific point in the score — useful when a score has time signature changes. Returns { measure, numerator, denominator, display } where display is e.g. \"4/4\" or \"3/8\".",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." }
                },
                required: ["measure"]
            }
        },
        {
            name: "get_clef_at",
            description:
                "Returns the clef type currently active at a given staff and measure. Use this before calling add_clef to check whether a change is actually needed. Returns { measure, staff, clefType, clefInt } where clefType is a string name (e.g. \"treble\", \"bass\", \"alto\", \"tenor\") and clefInt is the raw ClefType enum integer.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." },
                    staff:   { type: "integer", description: "Global 1-based staff number from get_score_info." }
                },
                required: ["measure", "staff"]
            }
        },
        {
            name: "get_chord_symbol_spelling",
            description:
                "Returns the chord symbol spelling convention used in this score. Possible values: \"STANDARD\", \"GERMAN\", \"GERMAN_PURE\", \"SOLFEGGIO\", \"FRENCH\", or null if unset.",
            parameters: { type: "object", properties: {}, required: [] }
        },
        {
            name: "get_concert_pitch",
            description:
                "Returns whether concert pitch is currently enabled for this score (true/false). When concert pitch is on, all staves are shown at concert (sounding) pitch; when off, transposing instruments show written pitch. Returns null if the setting is unreadable.",
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
                "Adds an articulation marking to the note or chord at the given position. Supported articulations: staccato, tenuto, accent, marcato, trill, mordent, turn, upBow, downBow, staccatissimo, snapPizzicato, harmonic, stress, unstress. For fermatas use add_fermata. Tremolo is not yet implemented.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    voice:        { type: "integer", description: "Voice 1–4." },
                    articulation: { type: "string",  enum: ["staccato","tenuto","accent","marcato","trill","mordent","turn","upBow","downBow","staccatissimo","snapPizzicato","harmonic","stress","unstress"], description: "The articulation to add." }
                },
                required: ["measure", "beat", "staff", "voice", "articulation"]
            }
        },

        // ── BATCH 5: get_measure, set_note_pitch, set_note_duration, add_fermata ─

        {
            name: "get_measure",
            description:
                "Returns structural metadata for a single measure: time signature, key signature, tempo marking, rehearsal mark, end barline type, and chord symbols. Does NOT return notes or lyrics — use get_notes_in_range and get_lyrics_in_range for those. Use this to get a quick structural snapshot of a specific measure.",
            parameters: {
                type: "object",
                properties: {
                    measure: { type: "integer", description: "1-based measure number." }
                },
                required: ["measure"]
            }
        },
        {
            name: "set_note_pitch",
            description:
                "Changes the pitch of a specific note at the given position. Use oldPitch to identify which note in a chord to change; if the chord has only one note, oldPitch can be omitted. Both oldPitch and newPitch are NoteName strings like 'C4', 'F#3', 'Bb5'.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4." },
                    oldPitch:     { type: "string",  description: "Current pitch of the note to change: 'C4', 'F#3' etc. Omit if the chord has only one note." },
                    newPitch:     { type: "string",  description: "New pitch: 'D4', 'Bb3' etc." }
                },
                required: ["measure", "beat", "staff", "voice", "newPitch"]
            }
        },
        {
            name: "set_note_duration",
            description:
                "Changes the duration of the note or chord at the given position. The chord's pitches are preserved; only the duration changes. This overwrites the position — if the new duration is shorter, trailing content is unaffected; if longer, it may overwrite subsequent notes.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    voice:        { type: "integer", description: "Voice 1–4." },
                    duration:     { type: "string",  description: "New duration: 'whole', 'half', 'quarter', 'eighth', '16th', 'dotted quarter', etc." }
                },
                required: ["measure", "beat", "staff", "voice", "duration"]
            }
        },
        {
            name: "add_fermata",
            description:
                "Adds a fermata (hold/pause symbol) above the note or rest at the given position. Type controls the length of the pause: 'normal' is the standard fermata, 'short' is a brief pause, 'long' is an extended hold, 'veryLong' is the longest.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number." },
                    type:         { type: "string",  enum: ["normal","short","long","veryLong"], description: "Fermata duration type. Defaults to 'normal'." }
                },
                required: ["measure", "beat", "staff"]
            }
        },

        // ── BATCH 6: selection, view settings, accidental, velocity, MIDI read ─

        {
            name: "get_selection",
            description:
                "Returns the current selection in the score — the element(s) or range the user has highlighted in MuseScore. Use this when the user refers to 'the selected notes', 'this measure', or otherwise expects context from what's highlighted.",
            parameters: {
                type: "object",
                properties: {},
                required: []
            }
        },
        {
            name: "get_view_settings",
            description:
                "Returns current score view and display settings: layout mode, visibility toggles (invisible elements, frames, page borders, instrument names), and concert pitch mode.",
            parameters: {
                type: "object",
                properties: {},
                required: []
            }
        },
        {
            name: "get_midi_channel_settings",
            description:
                "Returns MIDI channel parameters (volume, pan, chorus, reverb, mute, program, bank) for one or all instruments. These are MIDI byte values (0–127), not audio mixer dB levels.",
            parameters: {
                type: "object",
                properties: {
                    instrument: { type: "string", description: "Part name (case-insensitive substring match). Omit for all instruments." }
                },
                required: []
            }
        },
        {
            name: "set_view_settings",
            description:
                "Sets score display toggles. Only provided fields are updated.",
            parameters: {
                type: "object",
                properties: {
                    layoutMode:            { type: "string", enum: ["page","continuous","single","float"], description: "Score layout mode. 'page' is paginated; 'continuous' is a single horizontal line; 'single' fits one system per page; 'float' is the float layout." },
                    showInvisible:         { type: "boolean", description: "Show invisible elements." },
                    showUnprintable:       { type: "boolean", description: "Show unprintable formatting elements." },
                    showFrames:            { type: "boolean", description: "Show frame elements." },
                    showPageBorders:       { type: "boolean", description: "Show page border lines." },
                    showSoundFlags:        { type: "boolean", description: "Show sound flag indicators." },
                    showVerticalFrames:    { type: "boolean", description: "Show vertical frame elements." },
                    showInstrumentNames:   { type: "boolean", description: "Show instrument name labels." },
                    markIrregularMeasures: { type: "boolean", description: "Mark irregular (pickup/partial) measures." },
                    concertPitch:          { type: "boolean", description: "Concert pitch display mode (true = concert pitch, false = transposing pitch)." }
                },
                required: []
            }
        },
        {
            name: "set_note_accidental",
            description:
                "Sets or removes the accidental on a note. Use 'none' to let the key signature determine the accidental.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "1-based global staff number." },
                    voice:        { type: "integer", description: "Voice 1–4. Defaults to 1." },
                    pitch:        { type: "string",  description: "Note pitch to target in a chord (e.g. 'C4'). Optional if chord has one note." },
                    accidental:   { type: "string",  enum: ["sharp","flat","natural","doubleSharp","doubleFlat","none"], description: "Accidental to apply. 'none' removes an explicit accidental." }
                },
                required: ["measure", "beat", "staff", "accidental"]
            }
        },
        {
            name: "set_note_velocity",
            description:
                "Sets a per-note playback velocity override (0–127). This overrides score dynamics for that note. Prefer add_dynamic for musical expression; use this only for fine-grained per-note control.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', etc." },
                    staff:        { type: "integer", description: "1-based global staff number." },
                    voice:        { type: "integer", description: "Voice 1–4. Defaults to 1." },
                    pitch:        { type: "string",  description: "Note pitch to target in a chord (e.g. 'G3'). Optional if chord has one note." },
                    velocity:     { type: "integer", minimum: 0, maximum: 127, description: "Velocity value 0–127." }
                },
                required: ["measure", "beat", "staff", "velocity"]
            }
        },

        // ── BATCH 7: get_spanners_in_range ──

        {
            name: "get_spanners_in_range",
            description:
                "Returns all spanners (hairpins, slurs, ottavas, pedals, voltas, etc.) intersecting the given measure range. Each entry includes the spanner type, start and end measure, the staff it belongs to, the instrument name, and visibility.",
            parameters: {
                type: "object",
                properties: {
                    startMeasure: { type: "integer", description: "First measure to include (1-based, inclusive)." },
                    endMeasure:   { type: "integer", description: "Last measure to include (1-based, inclusive)." },
                    instrument:   { type: "string",  description: "Optional case-insensitive substring filter on the instrument long name (e.g. 'violin'). Omit to include all staves." }
                },
                required: ["startMeasure", "endMeasure"]
            }
        },

        // ── BATCH 8: set_midi_channel_settings ──

        {
            name: "set_midi_channel_settings",
            description:
                "Sets MIDI playback parameters (volume, pan, chorus, reverb, mute, program, bank) for an instrument channel. Values are MIDI bytes (0–127), not audio dB. Prefer add_dynamic for score-level dynamics — use this only for raw MIDI control. Only fields you provide are written; others are left unchanged.",
            parameters: {
                type: "object",
                properties: {
                    instrument: {
                        type: "string",
                        description: "Part name as in score (case-insensitive substring match)."
                    },
                    channelName: {
                        type: "string",
                        description: "Channel name within the instrument (e.g. 'normal', 'pizzicato', 'tremolo'). Default: 'normal'."
                    },
                    volume: {
                        type: "integer",
                        minimum: 0,
                        maximum: 127,
                        description: "MIDI volume (0–127)."
                    },
                    pan: {
                        type: "integer",
                        minimum: 0,
                        maximum: 127,
                        description: "Pan position (0=hard left, 64=centre, 127=hard right)."
                    },
                    chorus: { type: "integer", minimum: 0, maximum: 127 },
                    reverb: { type: "integer", minimum: 0, maximum: 127 },
                    mute:   { type: "boolean" },
                    midiProgram: {
                        type: "integer",
                        minimum: 0,
                        maximum: 127,
                        description: "General MIDI program number (0–127)."
                    },
                    midiBank: {
                        type: "integer",
                        minimum: 0,
                        description: "MIDI bank number."
                    }
                },
                required: ["instrument"]
            }
        },

        // ── BATCH D1: delete_note, add_tremolo ──

        {
            name: "delete_note",
            description:
                "Removes a note from a chord or replaces a single-note beat with a rest of the same duration. " +
                "If the beat has a chord (multiple notes), specify pitch to identify which note to remove. " +
                "If the beat has only one note, pitch can be omitted. " +
                "The change is undoable with Ctrl+Z.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc. Omit for exact beat." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4. Defaults to 1." },
                    pitch:        { type: "string",  description: "Pitch of the note to remove, e.g. 'C4', 'F#3'. Required if the chord has multiple notes; omit if the chord has only one note." }
                },
                required: ["measure", "beat", "staff"]
            }
        },
        {
            name: "add_tremolo",
            description:
                "Adds a single-note tremolo (rapid repeated-stroke effect) to a note or chord. " +
                "type controls the stroke subdivision: 'buzz' = unmeasured buzz roll, '8th' = eighth-note strokes, " +
                "'16th' = sixteenth-note strokes (most common), '32nd' = 32nd-note strokes, '64th' = 64th-note strokes. " +
                "Two-note (measured) tremolo between two chords is not yet supported.",
            parameters: {
                type: "object",
                properties: {
                    measure:      { type: "integer", description: "1-based measure number." },
                    beat:         { type: "integer", description: "1-based beat number." },
                    beatFraction: { type: "string",  description: "Sub-beat offset: '0', '1/2', '1/4' etc." },
                    staff:        { type: "integer", description: "Global 1-based staff number from get_score_info." },
                    voice:        { type: "integer", description: "Voice 1–4. Defaults to 1." },
                    type:         { type: "string",  enum: ["buzz","8th","16th","32nd","64th"], description: "Tremolo stroke type." }
                },
                required: ["measure", "beat", "staff", "type"]
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
