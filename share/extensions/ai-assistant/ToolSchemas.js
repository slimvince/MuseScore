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

// Core, provider-neutral definitions.
var CORE = [
    {
        name: "get_score_info",
        description:
            "Returns basic metadata about the open score: title, composer, lyricist, " +
            "copyright, subtitle, measure count, duration (seconds), initial key/time/tempo, " +
            "and the list of parts (instruments). Use this when the user asks about the score " +
            "in general terms (\"what is this piece?\", \"who composed it?\", \"how long is it?\").",
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
            "Returns all notes and rests in the given measure range. Optional filters narrow by " +
            "instrument (part name as in the score), staff (1-based within instrument), or voice " +
            "(1–4). Use this tool to read actual pitches and rhythms in the score.",
        parameters: {
            type: "object",
            properties: {
                startMeasure: { type: "integer", description: "First measure to include (1-based, inclusive)." },
                endMeasure:   { type: "integer", description: "Last measure to include (1-based, inclusive)." },
                instrument:   { type: "string",  description: "Part name as it appears in the score; omit for all instruments." },
                staff:        { type: "integer", description: "1-based staff index within the instrument (e.g. piano treble=1, bass=2); omit for all staves." },
                voice:        { type: "integer", description: "Voice number 1–4; omit for all voices." }
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
                instrument:   { type: "string",  description: "Part name as in the score; omit for all instruments." }
            },
            required: ["startMeasure", "endMeasure"]
        }
    }
]

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
    var out = []
    for (var i = 0; i < CORE.length; i++) {
        var t = CORE[i]
        if (providerFormat === "anthropic")    out.push(_toAnthropic(t))
        else if (providerFormat === "gemini")  out.push(_toGemini(t))
        else                                   out.push(_toOpenAI(t))   // openai + custom
    }
    return out
}
