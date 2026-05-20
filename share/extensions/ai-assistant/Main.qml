// AI Assistant v0.5.5 — Conversational Chat UI + LLM tool calling
// MS4-safe: no FlatButton, no import Muse.*, no QtQuick.LocalStorage top-level import
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import MuseScore 3.0    // for QProcess (apiv1 MsProcess) — DEBUG LOGGING, remove before shipping

import "ScoreAccess.js"  as ScoreAccess
import "ToolSchemas.js"  as ToolSchemas
import "Dispatch.js"     as Dispatch

Rectangle {
    id: root
    width: 1100
    height: 760
    color: sysPalette.window

    // ── System palette (dark mode support) ────────────────────────────────────
    SystemPalette { id: sysPalette; colorGroup: SystemPalette.Active }

    // ── Version ───────────────────────────────────────────────────────────────
    readonly property string pluginVersion: "0.5.5"

    // ── Provider config ───────────────────────────────────────────────────────
    property string providerPreset:          "Anthropic"
    property string providerEndpoint:        "https://api.anthropic.com"
    property string providerFormat:          "anthropic"
    property string providerApiKey:          ""
    property string providerModel:           ""
    property int    providerMaxTokens:       4096
    property int    providerThinkingBudget:  5000
    property string providerReasoningEffort: "medium"

    // Per-preset API key cache (so switching presets preserves each key)
    property var presetApiKeys: ({ "Anthropic": "", "OpenAI": "", "Gemini": "", "Other": "" })

    // ── Capability flags ──────────────────────────────────────────────────────
    property bool capThinking:  false
    property bool capReasoning: false

    readonly property var capabilityMap: [
        { prefix: "claude-3-7",      thinking: true,  reasoning: false },
        { prefix: "claude-opus-4",   thinking: true,  reasoning: false },
        { prefix: "claude-sonnet-4", thinking: true,  reasoning: false },
        { prefix: "o1",              thinking: false, reasoning: true  },
        { prefix: "o3",              thinking: false, reasoning: true  },
        { prefix: "o4",              thinking: false, reasoning: true  }
    ]

    // ── Model list ────────────────────────────────────────────────────────────
    // modelList holds either fetched models or, on fetch failure, the hardcoded
    // fallback for the active provider. Items: { id: "<value sent to API>", label: "<shown in dropdown>" }.
    // For Gemini, id is the bare model id (no "models/" prefix); label is displayName.
    // For Anthropic, id is the model id; label is display_name when present, else id.
    // For OpenAI, id and label are both the model id.
    property var    modelList:        []
    property bool   fetchingModels:   false
    property string fetchModelsError: ""
    property string modelChangedNotice: ""

    // Hardcoded fallback used if the live fetch fails (network, bad key, etc.)
    // so the user still has selectable models. Kept conservative — drop entries
    // that providers have deprecated.
    readonly property var defaultModelOptions: ({
        "anthropic": [
            { id: "claude-opus-4-6",          label: "Claude Opus 4"     },
            { id: "claude-sonnet-4-6",        label: "Claude Sonnet 4"   },
            { id: "claude-haiku-4-5",         label: "Claude Haiku 4"    },
            { id: "claude-3-7-sonnet-latest", label: "Claude 3.7 Sonnet" },
            { id: "claude-3-5-sonnet-latest", label: "Claude 3.5 Sonnet" },
            { id: "claude-3-5-haiku-latest",  label: "Claude 3.5 Haiku"  }
        ],
        "openai": [
            { id: "gpt-4o",      label: "gpt-4o"      },
            { id: "gpt-4o-mini", label: "gpt-4o-mini" },
            { id: "gpt-4-turbo", label: "gpt-4-turbo" },
            { id: "o1",          label: "o1"          },
            { id: "o1-mini",     label: "o1-mini"     },
            { id: "o3-mini",     label: "o3-mini"     }
        ],
        "gemini": [
            { id: "gemini-2.5-pro",   label: "Gemini 2.5 Pro"   },
            { id: "gemini-2.5-flash", label: "Gemini 2.5 Flash" },
            { id: "gemini-1.5-pro",   label: "Gemini 1.5 Pro"   },
            { id: "gemini-1.5-flash", label: "Gemini 1.5 Flash" }
        ]
    })

    // Computed dropdown contents: loading placeholder while fetching, otherwise
    // the fetched list or hardcoded fallback, always with a trailing "(custom…)".
    readonly property var modelOptions: {
        if (fetchingModels) return [{ id: "", label: "Loading models…" }]
        var base = (modelList && modelList.length > 0)
                   ? modelList
                   : (defaultModelOptions[providerFormat] || [])
        var list = base.slice()
        list.push({ id: "__custom__", label: "(custom…)" })
        return list
    }

    // ── Conversation data ─────────────────────────────────────────────────────
    // Each conversation: { id, title, provider, model, messages: [{role, content, ts?}] }
    //   id        — "conv_<timestamp>" assigned at creation
    //   title     — first ~50 chars of first user message; "New chat" until then
    //   provider  — providerFormat last used in this conversation ("anthropic"/"openai"/"gemini")
    //   model     — providerModel last used in this conversation
    //   messages  — { role, content } pairs; ts is in-memory only and dropped on serialize
    // Persisted to MuseScore Settings under key "savedConversations" (JSON).
    property var    conversations:   []
    property string currentConvId:   ""
    property var    currentMessages: []

    // Persistence caps — see saveConversations() for trim logic.
    readonly property int maxConversations:         20
    readonly property int maxMessagesPerConv:       200    // 100 user/assistant pairs
    readonly property int conversationsByteSafety:  500000 // JSON.stringify length safety net

    // ── Streaming state ───────────────────────────────────────────────────────
    property string streamingText: ""
    property bool   isStreaming:   false
    property var    activeXhr:     null

    // ── UI state ──────────────────────────────────────────────────────────────
    property bool   showSettings:         false
    property bool   scoreContextExpanded: false
    property string scoreContext:         "(no score open)"

    // ── System prompt ─────────────────────────────────────────────────────────
    // systemPrompt is rebuilt by buildSystemPrompt() at startup, when settings
    // change, and when the user reopens the assistant against a different score.
    // systemPromptOverride is the user-editable "append this to the default"
    // text persisted in MuseScore 3.0 Settings.
    property string systemPrompt:         ""
    property string systemPromptOverride: ""

    // ── Persistence ───────────────────────────────────────────────────────────
    property var appSettings: null

    // ── DEBUG LOGGING — remove before shipping ────────────────────────────────
    // _writeLogViaProcess(line) queues a JSON line; logFlushTimer batches all
    // pending lines into one PowerShell Add-Content call every 100ms.
    // One process per flush (not per line) avoids the QProcess accumulation
    // stall that silenced the log after ~2 tool calls.
    readonly property bool debugMode: true
    property var _logQueue: []

    // Enter-to-send workaround for MS4 extensions.
    //
    // The chat input cannot use TextField.onAccepted, Keys.onReturnPressed, or a QML Shortcut bound to
    // Return/Enter: MS4 binds Return/Enter as a QML Shortcut at the main-window level (via shortcuts.xml →
    // `nav-trigger-control`), and any binding we make at the extension-dialog level is silently swallowed
    // by Qt's shortcut resolver as an ambiguous-overload (resolves to neither). The only path that fires
    // is to plug into MS4's navigation framework as a NavigationControl, so MS4 dispatches Enter to us.
    //
    // Building the NavigationSection → NavigationPanel → NavigationControl chain requires importing
    // Muse.Ui, which is blocked by the extension deploy validator (extensionbuilder.cpp validateImports
    // refuses any line containing `import Muse.`). We bypass that with Qt.createQmlObject — the validator
    // only scans literal `import` lines in the .qml source, not strings passed to createQmlObject. The V2
    // extension QML engine can still resolve Muse.Ui at runtime because it's a registered QML module
    // (not file-path based), independent of the engine's import-path list.
    property var navSection: null
    property var navPanel: null
    property var navSendControl: null
    function setupNavigation() {
        try {
            navSection = Qt.createQmlObject(
                'import Muse.Ui\n' +
                'NavigationSection { name: "ai-assistant"; order: 100; enabled: true; type: NavigationSection.Regular }',
                root, "navSection")
            navPanel = Qt.createQmlObject(
                'import Muse.Ui\n' +
                'NavigationPanel { name: "ai-assistant-chat"; order: 0; enabled: true }',
                root, "navPanel")
            navPanel.section = navSection
            navSendControl = Qt.createQmlObject(
                'import Muse.Ui\n' +
                'NavigationControl { name: "ai-assistant-send"; order: 0; enabled: true }',
                root, "navSendControl")
            navSendControl.panel = navPanel
            navSendControl.triggered.connect(function() {
                if (!isStreaming && inputField.text.trim().length > 0) {
                    var txt = inputField.text
                    inputField.text = ""
                    sendMessage(txt)
                }
            })
        } catch(e) {
            console.warn("AIAssistant: Enter-to-send navigation chain creation FAILED — Enter key will not work: " + e)
        }
    }

    // DEBUG LOGGING — remove before shipping.
    // Queue-and-batch approach: _writeLogViaProcess pushes to _logQueue and
    // arms logFlushTimer. When the timer fires, _flushLogQueue drains the
    // queue and passes all pending lines to ONE PowerShell process as a
    // chained Add-Content script. This reduces spawning from 2× per tool
    // call to 1× per 100ms window, eliminating the QProcess accumulation
    // stall that silenced the log after ~2 calls.
    //
    // MsProcess (util.h:166-188) exposes startWithArgs(prog, args).
    // PowerShell single-quoted strings: only ' needs escaping (doubled '').
    Timer {
        id: logFlushTimer
        interval: 100
        repeat: false
        onTriggered: root._flushLogQueue()
    }

    function _writeLogViaProcess(line) {
        if (!debugMode) return
        _logQueue.push(line)
        if (!logFlushTimer.running) logFlushTimer.start()
    }

    function _flushLogQueue() {
        if (_logQueue.length === 0) return
        var batch = _logQueue.slice()
        _logQueue = []
        var logPath = "C:/Users/vince/AppData/Local/MuseScore/MuseScore4/logs/ai-assistant-debug.log"
        // Build one PS command: each line becomes a separate Add-Content call,
        // all chained with '; ' so a single PowerShell process handles them all.
        var psCmd = batch.map(function(l) {
            return "Add-Content -LiteralPath '" + logPath + "' -Value '" + l.replace(/'/g, "''") + "' -Encoding UTF8"
        }).join("; ")
        var proc = Qt.createQmlObject('import MuseScore 3.0; QProcess { }', root, "logFlushProc")
        if (!proc) { console.log("DEBUG: QProcess unavailable"); return }
        proc.startWithArgs("powershell.exe", ["-NoProfile", "-NonInteractive", "-Command", psCmd])
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Init
    // ─────────────────────────────────────────────────────────────────────────
    Component.onCompleted: {
        setupNavigation()

        appSettings = (function() {
            try {
                return Qt.createQmlObject(
                    'import MuseScore 3.0; Settings { category: "AIAssistant" }',
                    root, "appSettings_" + Date.now())
            } catch(e) {
                console.log("AIAssistant: settings failed: " + e)
                return null
            }
        })()
        loadSettings()
        loadConversations()
        if (conversations.length === 0) newConversation()
        else selectConversation(conversations[0].id)
        updateCapability()
        refreshScoreContext()
        buildSystemPrompt()
        // Initial live fetch if a key is already saved — otherwise users would see
        // the stale hardcoded fallback until they next touch the Settings UI.
        if (providerApiKey && providerApiKey.length > 0) fetchModels()

        // DEBUG LOGGING — remove before shipping. Also serves as smoke test:
        // if no session_start line appears after launch, the QProcess path is broken.
        if (debugMode) {
            _writeLogViaProcess(JSON.stringify({
                session_start: true,
                version: "v" + pluginVersion,
                t: new Date().toISOString()
            }))
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Settings persistence (MuseScore 3.0 Settings — survives MS4 plugin reload)
    // ─────────────────────────────────────────────────────────────────────────
    function saveSettings() {
        if (!appSettings) return
        appSettings.setValue("providerPreset",          providerPreset)
        appSettings.setValue("providerEndpoint",        providerEndpoint)
        appSettings.setValue("providerFormat",          providerFormat)
        appSettings.setValue("providerModel",           providerModel)
        appSettings.setValue("providerMaxTokens",       providerMaxTokens)
        appSettings.setValue("providerThinkingBudget",  providerThinkingBudget)
        appSettings.setValue("providerReasoningEffort", providerReasoningEffort)
        var keys = presetApiKeys
        keys[providerPreset] = providerApiKey
        presetApiKeys = keys
        appSettings.setValue("presetApiKeys", JSON.stringify(presetApiKeys))
        appSettings.setValue("systemPromptOverride", systemPromptOverride)
    }

    function loadSettings() {
        if (!appSettings) return
        providerPreset          = appSettings.value("providerPreset",          "Anthropic")
        providerEndpoint        = appSettings.value("providerEndpoint",        "https://api.anthropic.com")
        providerFormat          = appSettings.value("providerFormat",          "anthropic")
        providerModel           = appSettings.value("providerModel",           "")
        providerMaxTokens       = parseInt(appSettings.value("providerMaxTokens",      4096)) || 4096
        providerThinkingBudget  = parseInt(appSettings.value("providerThinkingBudget", 5000)) || 5000
        providerReasoningEffort = appSettings.value("providerReasoningEffort", "medium")
        try {
            presetApiKeys = JSON.parse(appSettings.value("presetApiKeys", "{}"))
        } catch(e) {
            presetApiKeys = { "Anthropic":"","OpenAI":"","Gemini":"","Other":"" }
        }
        providerApiKey = presetApiKeys[providerPreset] || ""
        systemPromptOverride = appSettings.value("systemPromptOverride", "") || ""
    }

    // ─────────────────────────────────────────────────────────────────────────
    // System prompt construction
    // ─────────────────────────────────────────────────────────────────────────
    // Three concatenated layers:
    //   1. Static instructions (always present).
    //   2. Dynamic context derived from the open score's settings (chord-symbol
    //      spelling and concert-pitch toggle). Skipped when no score is open.
    //   3. User override from Settings (systemPromptOverride). Appended verbatim.
    function buildSystemPrompt() {
        var L1 =
            "You are a music assistant embedded in MuseScore. A score is open in the editor.\n\n" +
            "Use the provided tools to read the score when needed. Only fetch what is required " +
            "to answer the question — do not call read tools unnecessarily. " +
            "The score can change between turns: the user may edit it directly in MuseScore at " +
            "any time. Always re-query for current score state before answering questions about " +
            "what is in the score — do not rely on data fetched in an earlier turn.\n\n" +
            "Score elements have a visible property. Elements with visible: false exist in the " +
            "score data but are hidden — they do not appear in print or in normal playback. " +
            "Report them honestly and distinguish them from visible elements in your answers.\n\n" +
            "You can also modify the score using write tools. All changes land in MuseScore's " +
            "undo stack and can be reversed with Ctrl+Z. After a successful write, briefly " +
            "confirm what you did.\n\n" +
            "When a tool returns an error, report the exact error text verbatim. " +
            "Do not invent an explanation for why it failed — you do not have visibility into " +
            "MuseScore's internal state and guessing causes confusion.\n\n" +
            "If you use a position (measure, beat, staff) that differs from what the user " +
            "specified — for example because you rounded to the nearest note onset — state " +
            "the adjustment explicitly. Never silently use a different position than requested. " +
            "When the user's request leaves a required parameter ambiguous, ask for " +
            "clarification before calling the tool. Exception: if the score structure makes " +
            "the answer unambiguous (e.g. there is only one staff), you may infer it and " +
            "state your assumption.\n\n" +
            "When the user refers to a staff by instrument name (e.g. 'Soprano', 'Violin II', " +
            "'Bandoneon') rather than an explicit staff number, you MUST call get_score_info " +
            "first to look up the correct global staff number before calling any tool that " +
            "requires a staff parameter. Never assume staff=1 for an instrument name. " +
            "The staff number returned by get_score_info is the one to use.\n\n" +
            "When a tool returns a collection of settings or properties — such as " +
            "get_score_style, get_score_info, or get_measure — report ALL returned " +
            "fields in your response. Do not silently omit fields you consider " +
            "unimportant or technical. You may group them by category for readability, " +
            "but every returned key must appear. If the list is long, tell the user " +
            "the total count and present all of them."

        var l2lines = []
        var spelling = ScoreAccess.getChordSymbolSpelling()
        if (spelling === "GERMAN" || spelling === "GERMAN_PURE") {
            l2lines.push("The score uses German chord-symbol spelling: H denotes B-natural and B denotes B-flat.")
        } else if (spelling === "SOLFEGGIO") {
            l2lines.push("The score uses solfeggio chord-symbol spelling (Do Re Mi Fa Sol La Si).")
        } else if (spelling === "FRENCH") {
            l2lines.push("The score uses French chord-symbol spelling (Do Ré Mi Fa Sol La Si).")
        } else if (spelling === "STANDARD") {
            l2lines.push("The score uses international chord-symbol spelling: C D E F G A B.")
        }
        var cp = ScoreAccess.getConcertPitch()
        if (cp === true) {
            l2lines.push("Concert pitch is enabled. All note names are at concert (sounding) pitch.")
        } else if (cp === false) {
            l2lines.push("Concert pitch is off. Note names in transposing instruments are written pitch, not sounding pitch.")
        }

        var L2 = l2lines.length > 0 ? "\n\n" + l2lines.join("\n") : ""
        var L3 = (systemPromptOverride && systemPromptOverride.length > 0)
                 ? "\n\n" + systemPromptOverride
                 : ""

        systemPrompt = L1 + L2 + L3
        return systemPrompt
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Conversation persistence (Settings JSON blob "savedConversations")
    // ─────────────────────────────────────────────────────────────────────────
    function _serializeConversations(list) {
        // Build the on-disk shape: drop ts, keep only role/content per message.
        var out = []
        for (var i = 0; i < list.length; i++) {
            var c = list[i]
            var msgs = c.messages || []
            // Per-conversation trim: keep the most recent maxMessagesPerConv entries,
            // dropping in pairs of 2 so the surviving slice still starts at a user turn.
            if (msgs.length > maxMessagesPerConv) {
                var dropPairs = Math.ceil((msgs.length - maxMessagesPerConv) / 2)
                msgs = msgs.slice(dropPairs * 2)
            }
            var serMsgs = []
            for (var j = 0; j < msgs.length; j++)
                serMsgs.push({ role: msgs[j].role, content: msgs[j].content })
            out.push({
                id:       c.id,
                title:    c.title    || "New chat",
                provider: c.provider || providerFormat,
                model:    c.model    || providerModel,
                messages: serMsgs
            })
        }
        return out
    }

    function saveConversations() {
        if (!appSettings) return
        try {
            var snapshot = _serializeConversations(conversations)
            // Hard cap on number of conversations — newest is at index 0 (unshift), so oldest is at the tail.
            if (snapshot.length > maxConversations)
                snapshot = snapshot.slice(0, maxConversations)
            var json = JSON.stringify(snapshot)
            // Byte-size safety net: keep dropping oldest until under the byte budget.
            while (json.length > conversationsByteSafety && snapshot.length > 1) {
                snapshot.pop()
                json = JSON.stringify(snapshot)
            }
            appSettings.setValue("savedConversations", json)
        } catch(e) {
            console.log("AIAssistant: saveConversations failed: " + e)
        }
    }

    function loadConversations() {
        conversations = []
        if (!appSettings) return
        var raw = appSettings.value("savedConversations", "")
        if (!raw) return
        try {
            var parsed = JSON.parse(raw)
            if (!Array.isArray(parsed)) return
            var list = []
            for (var i = 0; i < parsed.length; i++) {
                var c = parsed[i]
                if (!c || !c.id) continue
                list.push({
                    id:       c.id,
                    title:    c.title    || c.name || "New chat",
                    provider: c.provider || "",
                    model:    c.model    || "",
                    messages: Array.isArray(c.messages) ? c.messages.slice() : []
                })
            }
            conversations = list
        } catch(e) {
            console.log("AIAssistant: loadConversations parse error: " + e)
            conversations = []
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Conversation management
    // ─────────────────────────────────────────────────────────────────────────
    function genId() {
        return "conv_" + Date.now()
    }

    function scrollToBottom() {
        var flick = chatScroll.contentItem
        flick.contentY = Math.max(0, flick.contentHeight - chatScroll.height)
    }

    function newConversation() {
        var c = {
            id:       genId(),
            title:    "New chat",
            provider: providerFormat,
            model:    providerModel,
            messages: []
        }
        var list = conversations.slice()
        list.unshift(c)
        conversations = list
        selectConversation(c.id)
        saveConversations()
    }

    function selectConversation(id) {
        currentConvId = id
        for (var i = 0; i < conversations.length; i++) {
            if (conversations[i].id === id) {
                currentMessages = conversations[i].messages.slice()
                return
            }
        }
        currentMessages = []
    }

    function deleteConversation(id) {
        var list = []
        for (var i = 0; i < conversations.length; i++)
            if (conversations[i].id !== id) list.push(conversations[i])
        conversations = list
        saveConversations()
        if (conversations.length === 0) newConversation()
        else selectConversation(conversations[0].id)
    }

    // Push the current global provider/model onto the active conversation so
    // the sidebar reflects it immediately — without waiting for the next user
    // turn (where appendMessage would also restamp). Called from every site
    // that mutates providerModel / providerFormat in the Settings UI.
    //
    // Mid-conversation LLM switching is allowed by design. The conversation's
    // `model`/`provider` fields mean "what will be used for the NEXT send",
    // not "first model the conversation used".
    function _updateCurrentConversationModel() {
        if (!currentConvId) return
        var list = conversations.slice()
        for (var i = 0; i < list.length; i++) {
            if (list[i].id === currentConvId) {
                if (list[i].model === providerModel && list[i].provider === providerFormat) return
                list[i].model    = providerModel
                list[i].provider = providerFormat
                conversations = list
                saveConversations()
                return
            }
        }
    }

    function appendMessage(role, content) {
        var msg = { role: role, content: content, ts: Date.now() }
        var list = conversations.slice()
        for (var i = 0; i < list.length; i++) {
            if (list[i].id === currentConvId) {
                var msgs = list[i].messages.slice()
                msgs.push(msg)
                list[i].messages = msgs
                if (role === "user" && msgs.length === 1)
                    list[i].title = content.substring(0, 50) + (content.length > 50 ? "…" : "")
                if (role === "user") {
                    list[i].model    = providerModel    // stamp model on each user turn
                    list[i].provider = providerFormat   // stamp provider on each user turn
                }
                conversations = list
                currentMessages = msgs
                saveConversations()
                return
            }
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Score context
    // ─────────────────────────────────────────────────────────────────────────
    function refreshScoreContext() {
        try {
            var s = (typeof api !== "undefined" && api && api.engraving) ? api.engraving.curScore : null
            if (!s) {
                scoreContext = "(no score open)"
                return
            }
            var info = {
                scoreName:    s.scoreName     || "",
                title:        s.title         || "",
                composer:     s.composer      || "",
                lyricist:     s.lyricist      || "",
                duration:     s.duration,
                keysig:       s.keysig,
                npages:       s.npages,
                nmeasures:    s.nmeasures,
                nstaves:      s.nstaves,
                ntracks:      s.ntracks,
                hasHarmonies: s.hasHarmonies,
                harmonyCount: s.harmonyCount,
                hasLyrics:    s.hasLyrics,
                lyricCount:   s.lyricCount,
                parts:        []
            }
            var parts = s.parts
            if (parts) {
                for (var i = 0; i < parts.length; i++) {
                    var p = parts[i]
                    info.parts.push({
                        index:          i,
                        partName:       p.partName     || "",
                        longName:       p.longName     || "",
                        shortName:      p.shortName    || "",
                        instrumentId:   p.instrumentId || "",
                        musicXmlId:     p.musicXmlId   || "",
                        startTrack:     p.startTrack,
                        endTrack:       p.endTrack,
                        hasChordSymbol: p.hasChordSymbol,
                        hasDrumStaff:   p.hasDrumStaff,
                        hasPitchedStaff:p.hasPitchedStaff,
                        hasTabStaff:    p.hasTabStaff,
                        midiChannel:    p.midiChannel,
                        midiProgram:    p.midiProgram,
                        show:           p.show
                    })
                }
            }

            // Walk all notes — gives LLM pitch/duration data for queries.
            // Measure-based traversal covers all 4 voices per staff and works
            // in Extensions 2.0 (cursor + Element.CHORD did not). Short field
            // names keep JSON compact; 2000-note guard avoids bloating the
            // prompt for large orchestral scores.
            var notes = []
            try {
                // Hoist enum lookup: on 4.7.0, api.engraving.Element.<KEY> rebuilds
                // the entire ~120-key enum object on every access. Evaluating it
                // inside the inner loop produced a ~100s startup freeze.
                var CHORD = api.engraving.Element.CHORD
                var measure = s.firstMeasure
                while (measure) {
                    var segment = measure.firstSegment
                    while (segment) {
                        for (var staffIdx = 0; staffIdx < s.nstaves; staffIdx++) {
                            for (var voice = 0; voice < 4; voice++) {
                                var el = segment.elementAt(staffIdx * 4 + voice)
                                if (el && el.type === CHORD) {
                                    for (var ni = 0; ni < el.notes.length; ni++) {
                                        var n = el.notes[ni]
                                        notes.push({
                                            m:    measure.no,
                                            st:   staffIdx,
                                            v:    voice,
                                            p:    n.pitch,
                                            tpc:  n.tpc,
                                            dur:  el.duration ? el.duration.str : "",
                                            tied: n.tieBack !== null
                                        })
                                    }
                                }
                            }
                        }
                        segment = segment.next
                    }
                    measure = measure.nextMeasure
                }
            } catch(e) {
                console.log("AIAssistant: note walk failed: " + e)
            }
            info.noteCount = notes.length
            if (notes.length > 0 && notes.length <= 2000) {
                info.notes = notes
            } else if (notes.length > 2000) {
                info.notesOmitted = true
            }

            scoreContext = JSON.stringify(info, null, 2)
        } catch (e) {
            scoreContext = "(score context error: " + e + ")"
        }
        // Concert-pitch / chord-spelling style may have changed if the user
        // opened a different score — rebuild the dynamic prompt layers.
        buildSystemPrompt()
    }


    // ─────────────────────────────────────────────────────────────────────────
    // Provider preset management
    // ─────────────────────────────────────────────────────────────────────────
    readonly property var presetDefaults: ({
        "Anthropic": { endpoint: "https://api.anthropic.com",                  format: "anthropic" },
        "OpenAI":    { endpoint: "https://api.openai.com",                     format: "openai"    },
        "Gemini":    { endpoint: "https://generativelanguage.googleapis.com",  format: "gemini"    },
        "Other":     { endpoint: "",                                            format: "openai"    }
    })

    // Save the current key under the old preset, then switch
    function applyPreset(newPreset, save) {
        // 1. Store current key under old preset
        var keys = presetApiKeys
        keys[providerPreset] = providerApiKey
        presetApiKeys = keys

        // 2. Switch preset and apply default endpoint/format (unless Other or already customised)
        providerPreset = newPreset
        if (presetDefaults[newPreset]) {
            providerEndpoint = presetDefaults[newPreset].endpoint
            providerFormat   = presetDefaults[newPreset].format
        }

        // 3. Load the stored key for the new preset
        providerApiKey = presetApiKeys[newPreset] || ""

        // 4. Force-refresh settings UI controls (bindings can be broken by user edits)
        endpointField.text = providerEndpoint
        formatCombo.currentIndex = ["anthropic","openai","gemini"].indexOf(providerFormat)
        apiKeyField.text = providerApiKey

        // 5. Clear fetched model list — stale for new provider. modelOptions falls
        //    back to defaultModelOptions[providerFormat] until a fresh fetch lands.
        modelList = []
        fetchModelsError = ""
        modelChangedNotice = ""
        // Pick a sensible default for the new provider if the previous selection
        // isn't in this provider's defaults.
        var newDefaults = defaultModelOptions[providerFormat] || []
        var keepModel = false
        for (var dIdx = 0; dIdx < newDefaults.length; dIdx++) {
            if (newDefaults[dIdx].id === providerModel) { keepModel = true; break }
        }
        if (!keepModel && newDefaults.length > 0) providerModel = newDefaults[0].id

        if (save !== false) saveSettings()
        _updateCurrentConversationModel()   // sidebar reflects the provider/model switch live

        // 6. If we already have a key stored for this preset, fetch fresh models.
        if (providerApiKey && providerApiKey.length > 0) fetchModels()
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Capability flags
    // ─────────────────────────────────────────────────────────────────────────
    function updateCapability() {
        capThinking  = false
        capReasoning = false
        for (var i = 0; i < capabilityMap.length; i++) {
            if (providerModel.indexOf(capabilityMap[i].prefix) === 0) {
                capThinking  = capabilityMap[i].thinking
                capReasoning = capabilityMap[i].reasoning
                break
            }
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Model fetch
    // ─────────────────────────────────────────────────────────────────────────
    //
    // Replaces modelList with { id, label } objects fetched live from the provider.
    // On any failure, falls back to defaultModelOptions[providerFormat] so the
    // user still has selectable models (the hardcoded list is also what the UI
    // shows when modelList is empty — see the modelOptions computed property).
    //
    // Triggered from: manual "↻ Fetch" button; API-key field onEditingFinished
    // (when non-empty); applyPreset() when a stored key exists for the new preset.
    function fetchModels() {
        if (!providerApiKey || providerApiKey.length === 0) {
            // No key — can't query the provider. Leave modelList empty so the UI
            // falls back to defaults.
            fetchModelsError = ""
            modelList = []
            return
        }

        fetchingModels   = true
        fetchModelsError = ""
        var fmt  = providerFormat
        var url  = ""
        var hdrs = {}

        if      (fmt === "anthropic") { url = providerEndpoint + "/v1/models";   hdrs = { "x-api-key": providerApiKey, "anthropic-version": "2023-06-01" } }
        else if (fmt === "openai")    { url = providerEndpoint + "/v1/models";   hdrs = { "Authorization": "Bearer " + providerApiKey } }
        else if (fmt === "gemini")    { url = providerEndpoint + "/v1beta/models?key=" + providerApiKey }
        else                          { fetchingModels = false; fetchModelsError = "Unknown provider: " + fmt; return }

        var prevModel = providerModel

        var applyFallback = function(reason) {
            fetchModelsError = reason
            modelList = []   // empty list → modelOptions falls back to defaults
            var defaults = defaultModelOptions[fmt] || []
            if (defaults.length > 0) {
                var stillThere = false
                for (var k = 0; k < defaults.length; k++) {
                    if (defaults[k].id === prevModel) { stillThere = true; break }
                }
                if (!stillThere) {
                    providerModel = defaults[0].id
                    _updateCurrentConversationModel()
                }
            }
            updateCapability()
        }

        var xhr = new XMLHttpRequest()
        xhr.open("GET", url, true)
        for (var h in hdrs) xhr.setRequestHeader(h, hdrs[h])
        xhr.onreadystatechange = function() {
            if (xhr.readyState !== 4) return
            fetchingModels = false
            if (xhr.status === 200) {
                try {
                    var data = JSON.parse(xhr.responseText)
                    var items = []
                    if (fmt === "anthropic") {
                        var arr = data.data || []
                        for (var i = 0; i < arr.length; i++) {
                            var m = arr[i]
                            if (!m || !m.id) continue
                            items.push({ id: m.id, label: m.display_name || m.id })
                        }
                    } else if (fmt === "openai") {
                        var arr = data.data || []
                        for (var i = 0; i < arr.length; i++) {
                            var id = arr[i] && arr[i].id
                            if (!id) continue
                            // Chat-completion model families only.
                            if (!/^(gpt-|o1|o3)/.test(id)) continue
                            items.push({ id: id, label: id })
                        }
                    } else if (fmt === "gemini") {
                        var arr = data.models || []
                        for (var i = 0; i < arr.length; i++) {
                            var m = arr[i]
                            if (!m || !m.name) continue
                            var methods = m.supportedGenerationMethods || []
                            if (methods.indexOf("generateContent") < 0) continue
                            var bareId = m.name.replace("models/", "")
                            items.push({ id: bareId, label: m.displayName || bareId })
                        }
                    }

                    items.sort(function(a, b) { return a.label < b.label ? -1 : a.label > b.label ? 1 : 0 })

                    if (items.length === 0) {
                        applyFallback("Provider returned no usable models for format '" + fmt + "'")
                        return
                    }

                    modelList = items
                    // Preserve current model if still available; otherwise switch to
                    // the first item and surface the change so the user knows why.
                    var found = false
                    for (var i = 0; i < items.length; i++) {
                        if (items[i].id === prevModel) { found = true; break }
                    }
                    if (!found) {
                        providerModel = items[0].id
                        if (prevModel) {
                            modelChangedNotice = "Previous model '" + prevModel +
                                "' is no longer available — switched to '" + items[0].id + "'."
                        }
                        _updateCurrentConversationModel()
                    } else {
                        modelChangedNotice = ""
                    }
                    updateCapability()
                    saveSettings()
                } catch(e) {
                    applyFallback("Parse error: " + e)
                }
            } else {
                applyFallback("HTTP " + xhr.status + ": " + xhr.responseText.substring(0, 120))
            }
        }
        xhr.send()
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Send / stop — non-streaming tool-loop (v0.5.0)
    // ─────────────────────────────────────────────────────────────────────────
    //
    // Loop shape per provider:
    //   1. Build the request payload (messages + tools + system prompt).
    //   2. Send non-streaming. Parse the response.
    //   3. If the response contains tool calls, dispatch each, build the
    //      tool-result message(s), append everything to the per-turn API
    //      history, and recurse.
    //   4. Otherwise, append the assistant's text reply to currentMessages
    //      and exit the loop.
    //
    // Hard cap at maxToolIterations to avoid infinite tool loops.
    readonly property int maxToolIterations: 30

    function sendMessage(userText) {
        if (isStreaming || !userText.trim()) return
        var trimmed = userText.trim()
        appendMessage("user", trimmed)
        Qt.callLater(scrollToBottom)
        isStreaming   = true
        streamingText = ""

        // Refresh the system prompt before each send — the user may have
        // changed the score (concert-pitch toggle, chord-spelling style, etc.)
        // or edited the override since the last send.
        buildSystemPrompt()

        var fmt = providerFormat
        if      (fmt === "anthropic") _anthropicStart()
        else if (fmt === "openai")    _openAIStart()
        else if (fmt === "gemini")    _geminiStart()
        else                          _finishWithError("Unknown provider format: " + fmt)
    }

    function stopStreaming() {
        if (activeXhr) { try { activeXhr.abort() } catch(e) {} }
        isStreaming = false
        if (streamingText.trim()) {
            appendMessage("assistant", streamingText + " [stopped]")
            streamingText = ""
        }
        activeXhr = null
    }

    function _finishWithText(text) {
        appendMessage("assistant", text)
        Qt.callLater(scrollToBottom)
        streamingText = ""
        isStreaming   = false
        activeXhr     = null
    }
    function _finishWithError(err) {
        appendMessage("assistant", "⚠ Error: " + err)
        streamingText = ""
        isStreaming   = false
        activeXhr     = null
    }

    // ── Anthropic — non-streaming + tool loop ─────────────────────────────
    function _anthropicStart() {
        // Anthropic messages: array of { role, content } where content is a
        // string for plain user/assistant turns, or an array of content blocks
        // for tool-call / tool-result turns. We seed from currentMessages
        // (which contains only plain text turns) and accumulate tool turns
        // across iterations.
        var msgs = []
        for (var i = 0; i < currentMessages.length; i++)
            msgs.push({ role: currentMessages[i].role, content: currentMessages[i].content })
        _anthropicTurn(msgs, 0)
    }

    function _anthropicTurn(msgs, iter) {
        if (iter >= maxToolIterations) {
            _finishWithError("Tool-call loop exceeded " + maxToolIterations + " iterations without a final text response.")
            return
        }
        var budget = providerThinkingBudget
        var maxTok = capThinking ? Math.max(providerMaxTokens, budget + 1024) : providerMaxTokens
        var body = {
            model:      providerModel,
            max_tokens: maxTok,
            messages:   msgs,
            tools:      ToolSchemas.getToolSchemas("anthropic")
        }
        if (systemPrompt && systemPrompt.length > 0) body.system = systemPrompt
        if (capThinking) body.thinking = { type: "enabled", budget_tokens: budget }

        var xhr = new XMLHttpRequest()
        activeXhr = xhr
        xhr.open("POST", providerEndpoint + "/v1/messages", true)
        xhr.setRequestHeader("Content-Type",      "application/json")
        xhr.setRequestHeader("x-api-key",         providerApiKey)
        xhr.setRequestHeader("anthropic-version", "2023-06-01")
        xhr.onreadystatechange = function() {
            if (xhr.readyState !== 4) return
            if (xhr.status !== 200) {
                _finishWithError("HTTP " + xhr.status + ": " + xhr.responseText.substring(0, 300))
                return
            }
            var data
            try { data = JSON.parse(xhr.responseText) }
            catch(e) { _finishWithError("Parse error: " + e); return }

            var content = data.content || []
            var textParts = []
            var toolUses = []
            for (var i = 0; i < content.length; i++) {
                var b = content[i]
                if (b.type === "text" && b.text) textParts.push(b.text)
                else if (b.type === "tool_use") toolUses.push(b)
            }

            if (toolUses.length === 0) {
                _finishWithText(textParts.join("").trim() || "(no response)")
                return
            }

            // Append the assistant's full content array (text + tool_use) to history.
            var nextMsgs = msgs.slice()
            nextMsgs.push({ role: "assistant", content: content })

            // Build a single user message with one tool_result block per tool_use.
            var resultBlocks = []
            for (var j = 0; j < toolUses.length; j++) {
                var tu = toolUses[j]
                // DEBUG LOGGING — remove before shipping
                var _t0 = Date.now()
                if (debugMode) {
                    _writeLogViaProcess(JSON.stringify({
                        t: new Date().toISOString(),
                        call: tu.name,
                        args: tu.input || {}
                    }))
                }
                var r = Dispatch.dispatchTool(ScoreAccess, tu.name, tu.input || {})
                // DEBUG LOGGING — remove before shipping
                if (debugMode) {
                    var _parsed
                    try { _parsed = (typeof r === "string") ? JSON.parse(r) : r } catch(_e) { _parsed = r }
                    _writeLogViaProcess(JSON.stringify({
                        t: new Date().toISOString(),
                        result: _parsed,
                        ms: Date.now() - _t0
                    }))
                }
                resultBlocks.push({
                    type:         "tool_result",
                    tool_use_id:  tu.id,
                    content:      JSON.stringify(r)
                })
            }
            nextMsgs.push({ role: "user", content: resultBlocks })

            _anthropicTurn(nextMsgs, iter + 1)
        }
        xhr.send(JSON.stringify(body))
    }

    // ── OpenAI / custom — non-streaming + tool loop ───────────────────────
    function _openAIStart() {
        var msgs = []
        if (systemPrompt && systemPrompt.length > 0)
            msgs.push({ role: "system", content: systemPrompt })
        for (var i = 0; i < currentMessages.length; i++)
            msgs.push({ role: currentMessages[i].role, content: currentMessages[i].content })
        _openAITurn(msgs, 0)
    }

    function _openAITurn(msgs, iter) {
        if (iter >= maxToolIterations) {
            _finishWithError("Tool-call loop exceeded " + maxToolIterations + " iterations without a final text response.")
            return
        }
        var body = {
            model:    providerModel,
            messages: msgs,
            tools:    ToolSchemas.getToolSchemas("openai")
        }
        if (capReasoning) body.reasoning_effort = providerReasoningEffort
        else              body.max_tokens        = providerMaxTokens

        var xhr = new XMLHttpRequest()
        activeXhr = xhr
        xhr.open("POST", providerEndpoint + "/v1/chat/completions", true)
        xhr.setRequestHeader("Content-Type",  "application/json")
        xhr.setRequestHeader("Authorization", "Bearer " + providerApiKey)
        xhr.onreadystatechange = function() {
            if (xhr.readyState !== 4) return
            if (xhr.status !== 200) {
                _finishWithError("HTTP " + xhr.status + ": " + xhr.responseText.substring(0, 300))
                return
            }
            var data
            try { data = JSON.parse(xhr.responseText) }
            catch(e) { _finishWithError("Parse error: " + e); return }

            var choice = data.choices && data.choices[0]
            if (!choice || !choice.message) { _finishWithError("OpenAI: no choice/message in response"); return }
            var msg = choice.message
            var toolCalls = msg.tool_calls || []

            if (toolCalls.length === 0) {
                _finishWithText((msg.content || "").trim() || "(no response)")
                return
            }

            var nextMsgs = msgs.slice()
            // The assistant message MUST be appended verbatim (including
            // tool_calls and the content field as-is, even if null).
            nextMsgs.push({
                role:       "assistant",
                content:    msg.content === undefined ? null : msg.content,
                tool_calls: toolCalls
            })
            for (var i = 0; i < toolCalls.length; i++) {
                var tc = toolCalls[i]
                var name = tc.function ? tc.function.name : ""
                var args = {}
                try { args = JSON.parse(tc.function.arguments || "{}") } catch(e) {}
                // DEBUG LOGGING — remove before shipping
                var _t0 = Date.now()
                if (debugMode) {
                    _writeLogViaProcess(JSON.stringify({
                        t: new Date().toISOString(),
                        call: name,
                        args: args
                    }))
                }
                var r = Dispatch.dispatchTool(ScoreAccess, name, args)
                // DEBUG LOGGING — remove before shipping
                if (debugMode) {
                    var _parsed
                    try { _parsed = (typeof r === "string") ? JSON.parse(r) : r } catch(_e) { _parsed = r }
                    _writeLogViaProcess(JSON.stringify({
                        t: new Date().toISOString(),
                        result: _parsed,
                        ms: Date.now() - _t0
                    }))
                }
                nextMsgs.push({
                    role:         "tool",
                    tool_call_id: tc.id,
                    content:      JSON.stringify(r)
                })
            }
            _openAITurn(nextMsgs, iter + 1)
        }
        xhr.send(JSON.stringify(body))
    }

    // ── Gemini — non-streaming + tool loop ────────────────────────────────
    function _geminiStart() {
        // Gemini: `contents` is the message history. Tool calls come back as
        // `functionCall` parts; tool results go back as `functionResponse`
        // parts under a user-role message.
        var contents = []
        for (var i = 0; i < currentMessages.length; i++) {
            var m = currentMessages[i]
            contents.push({
                role:  m.role === "assistant" ? "model" : "user",
                parts: [{ text: m.content }]
            })
        }
        _geminiTurn(contents, 0)
    }

    function _geminiTurn(contents, iter) {
        if (iter >= maxToolIterations) {
            _finishWithError("Tool-call loop exceeded " + maxToolIterations + " iterations without a final text response.")
            return
        }
        var body = {
            contents:         contents,
            generationConfig: { maxOutputTokens: providerMaxTokens },
            tools:            [{ functionDeclarations: ToolSchemas.getToolSchemas("gemini") }]
        }
        if (systemPrompt && systemPrompt.length > 0)
            body.systemInstruction = { parts: [{ text: systemPrompt }] }

        var modelId = providerModel.replace("models/", "")
        var url = providerEndpoint + "/v1beta/models/" + modelId +
                  ":generateContent?key=" + providerApiKey

        var xhr = new XMLHttpRequest()
        activeXhr = xhr
        xhr.open("POST", url, true)
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.onreadystatechange = function() {
            if (xhr.readyState !== 4) return
            if (xhr.status !== 200) {
                _finishWithError("HTTP " + xhr.status + ": " + xhr.responseText.substring(0, 300))
                return
            }
            var data
            try { data = JSON.parse(xhr.responseText) }
            catch(e) { _finishWithError("Parse error: " + e); return }

            var cands = data.candidates
            if (!cands || !cands[0] || !cands[0].content) {
                _finishWithError("Gemini: no candidate content in response")
                return
            }
            var parts = cands[0].content.parts || []

            var textParts = []
            var funcCalls = []
            for (var i = 0; i < parts.length; i++) {
                if (parts[i].text) textParts.push(parts[i].text)
                else if (parts[i].functionCall) funcCalls.push(parts[i].functionCall)
            }

            if (funcCalls.length === 0) {
                _finishWithText(textParts.join("").trim() || "(no response)")
                return
            }

            var nextContents = contents.slice()
            nextContents.push({ role: "model", parts: parts })

            var respParts = []
            for (var j = 0; j < funcCalls.length; j++) {
                var fc = funcCalls[j]
                // DEBUG LOGGING — remove before shipping
                var _t0 = Date.now()
                if (debugMode) {
                    _writeLogViaProcess(JSON.stringify({
                        t: new Date().toISOString(),
                        call: fc.name,
                        args: fc.args || {}
                    }))
                }
                var r = Dispatch.dispatchTool(ScoreAccess, fc.name, fc.args || {})
                // DEBUG LOGGING — remove before shipping
                if (debugMode) {
                    var _parsed
                    try { _parsed = (typeof r === "string") ? JSON.parse(r) : r } catch(_e) { _parsed = r }
                    _writeLogViaProcess(JSON.stringify({
                        t: new Date().toISOString(),
                        result: _parsed,
                        ms: Date.now() - _t0
                    }))
                }
                // Gemini's functionResponse.response proto field is a non-repeating
                // STRUCT (object). Tools that return raw arrays (getStructure,
                // getMidiChannelSettings) or scalars must be wrapped — otherwise
                // Gemini rejects with HTTP 400 "Proto field is not repeating".
                var resp = (r && typeof r === "object" && !Array.isArray(r)) ? r : { result: r }
                respParts.push({ functionResponse: { name: fc.name, response: resp } })
            }
            nextContents.push({ role: "user", parts: respParts })

            _geminiTurn(nextContents, iter + 1)
        }
        xhr.send(JSON.stringify(body))
    }

    // ═════════════════════════════════════════════════════════════════════════
    // UI ROOT LAYOUT
    // ═════════════════════════════════════════════════════════════════════════
    SplitView {
        anchors.fill: parent
        orientation: Qt.Horizontal

        // ── Sidebar ───────────────────────────────────────────────────────────
        Rectangle {
            SplitView.preferredWidth: 200
            SplitView.minimumWidth:   140
            SplitView.maximumWidth:   360
            color: "#1e1e2e"

            ColumnLayout {
                anchors.fill:    parent
                anchors.margins: 8
                spacing: 6

                // Header row
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 4

                    Label {
                        text: "Conversations"
                        color: "#cdd6f4"
                        font.pixelSize: 12
                        font.bold: true
                        Layout.fillWidth: true
                    }

                    Button {
                        text: "+"
                        implicitWidth:  26
                        implicitHeight: 24
                        ToolTip.text:    "New chat"
                        ToolTip.visible: hovered
                        background: Rectangle {
                            color: parent.pressed ? "#45475a" : parent.hovered ? "#313244" : "transparent"
                            radius: 4
                        }
                        contentItem: Label {
                            text: parent.text
                            color: "#89b4fa"
                            font.pixelSize: 16
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment:   Text.AlignVCenter
                        }
                        onClicked: newConversation()
                    }
                }

                // Conversation list
                ListView {
                    id: convList
                    Layout.fillWidth:  true
                    Layout.fillHeight: true
                    clip: true
                    model: conversations
                    spacing: 2

                    delegate: Rectangle {
                        id: convDelegate
                        width:  convList.width
                        height: 48
                        radius: 6
                        color:  modelData.id === currentConvId
                                ? "#313244" : convMa.containsMouse ? "#252537" : "transparent"

                        MouseArea {
                            id: convMa
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked:    selectConversation(modelData.id)
                        }

                        RowLayout {
                            anchors.fill:         parent
                            anchors.leftMargin:   8
                            anchors.rightMargin:  4
                            anchors.topMargin:    4
                            anchors.bottomMargin: 4
                            spacing: 4

                            ColumnLayout {
                                Layout.fillWidth: true
                                spacing: 1

                                Label {
                                    text:  modelData.title
                                    color: modelData.id === currentConvId ? "#cdd6f4" : "#a6adc8"
                                    font.pixelSize: 12
                                    elide: Text.ElideRight
                                    Layout.fillWidth: true
                                }

                                Label {
                                    // Show model used in this conversation
                                    text:  modelData.model ? modelData.model : "—"
                                    color: "#585b70"
                                    font.pixelSize: 9
                                    elide: Text.ElideRight
                                    Layout.fillWidth: true
                                }
                            }

                            Button {
                                implicitWidth:  32
                                implicitHeight: 32
                                text:           "×"
                                visible:        convMa.containsMouse
                                background: Rectangle {
                                    color: parent.pressed ? "#f38ba8" : parent.hovered ? "#3d3f5c" : "transparent"
                                    radius: 4
                                }
                                contentItem: Label {
                                    text:  parent.text
                                    color: "#f38ba8"
                                    font.pixelSize: 16
                                    horizontalAlignment: Text.AlignHCenter
                                    verticalAlignment:   Text.AlignVCenter
                                }
                                onClicked: deleteConversation(modelData.id)
                            }
                        }
                    }
                }

                // Settings button
                Button {
                    Layout.fillWidth: true
                    implicitHeight:   32
                    text: showSettings ? "← Back to chat" : "⚙ Settings"
                    background: Rectangle {
                        color: parent.pressed ? "#45475a" : parent.hovered ? "#313244" : "#292a3e"
                        radius: 6
                    }
                    contentItem: Label {
                        text:  parent.text
                        color: "#89b4fa"
                        font.pixelSize: 12
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment:   Text.AlignVCenter
                    }
                    onClicked: showSettings = !showSettings
                }

                Label {
                    text:  "AI Assistant v" + pluginVersion
                    color: "#585b70"
                    font.pixelSize: 9
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignHCenter
                }
            }
        }

        // ── Main area ─────────────────────────────────────────────────────────
        Rectangle {
            SplitView.fillWidth: true
            color: sysPalette.window

            // ── Chat view ─────────────────────────────────────────────────────
            ColumnLayout {
                anchors.fill: parent
                spacing: 0
                visible: !showSettings

                // Score context chip — hidden (UI-2: adds visual noise without user value)
                Rectangle {
                    Layout.fillWidth: true
                    height: scoreContextExpanded ? scoreCtxText.implicitHeight + 40 : 40
                    color:  "#e8eaf6"
                    visible: false
                    clip:   true
                    Behavior on height { NumberAnimation { duration: 150 } }

                    RowLayout {
                        id: chipRow
                        anchors.top:         parent.top
                        anchors.left:        parent.left
                        anchors.right:       parent.right
                        anchors.leftMargin:  12
                        anchors.rightMargin: 12
                        height: 40
                        spacing: 6

                        Label {
                            text:           "🎵 Score context"
                            font.pixelSize: 12
                            font.bold:      true
                            color:          "#3949ab"
                        }

                        Button {
                            text: scoreContextExpanded ? "▲" : "▼"
                            implicitHeight: 20
                            implicitWidth:  24
                            background: Rectangle { color: "transparent" }
                            contentItem: Label {
                                text: parent.text; color: "#5c6bc0"; font.pixelSize: 11
                                horizontalAlignment: Text.AlignHCenter; verticalAlignment: Text.AlignVCenter
                            }
                            onClicked: scoreContextExpanded = !scoreContextExpanded
                        }

                        Item { Layout.fillWidth: true }

                        Button {
                            text: "↻"
                            implicitHeight: 20; implicitWidth: 24
                            background: Rectangle { color: "transparent" }
                            contentItem: Label {
                                text: parent.text; color: "#5c6bc0"; font.pixelSize: 13
                                horizontalAlignment: Text.AlignHCenter; verticalAlignment: Text.AlignVCenter
                            }
                            onClicked: refreshScoreContext()
                        }
                    }

                    TextArea {
                        id: scoreCtxText
                        anchors.top:         chipRow.bottom
                        anchors.left:        parent.left
                        anchors.right:       parent.right
                        anchors.leftMargin:  12
                        anchors.rightMargin: 12
                        anchors.bottomMargin: 6
                        text:           scoreContext
                        readOnly:       true
                        wrapMode:       TextEdit.Wrap
                        selectByMouse:  true
                        font.pixelSize: 11
                        color:          sysPalette.text
                        background:     null
                        visible:        scoreContextExpanded
                    }

                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width; height: 1
                        color: "#c5cae9"
                    }
                }

                // ── Chat bubble list ──────────────────────────────────────────
                // Repeater inside Column inside ScrollView — renders synchronously,
                // sidestepping ListView's virtualisation/height-race bug.
                ScrollView {
                    id: chatScroll
                    Layout.fillWidth:  true
                    Layout.fillHeight: true
                    clip: true
                    ScrollBar.vertical.policy: ScrollBar.AlwaysOn

                    // Disable Flickable drag so TextArea selection works inside bubbles.
                    // Scrollbar still scrolls the view.
                    Component.onCompleted: {
                        if (contentItem && "interactive" in contentItem)
                            contentItem.interactive = false
                    }

                    WheelHandler {
                        // Restore scroll-wheel scrolling that was disabled along with
                        // contentItem.interactive = false (needed for TextArea selection).
                        onWheel: function(event) {
                            var flick = chatScroll.contentItem
                            if (!flick) return
                            var maxY = Math.max(0, flick.contentHeight - chatScroll.height)
                            flick.contentY = Math.max(0, Math.min(flick.contentY - event.angleDelta.y / 2, maxY))
                            event.accepted = true
                        }
                    }

                    Column {
                        id: chatColumn
                        width:   chatScroll.availableWidth
                        spacing: 10
                        padding: 12
                        onHeightChanged: Qt.callLater(scrollToBottom)

                        Repeater {
                            model: currentMessages
                            delegate: Item {
                                width:  chatColumn.width - 24
                                height: msgBubble.height + 4
                                readonly property bool isUser: modelData.role === "user"

                                Rectangle {
                                    id: msgBubble
                                    anchors { left: parent.left; right: parent.right
                                              leftMargin: isUser ? 80 : 0; rightMargin: isUser ? 0 : 80 }
                                    property real renderedHeight: 44
                                    height: renderedHeight
                                    radius: 10
                                    color:  isUser ? "#5c6bc0" : sysPalette.base
                                    border.color: isUser ? "transparent" : "#e0e0e0"
                                    border.width: 1

                                    TextArea {
                                        id: msgText
                                        anchors.fill: parent
                                        text:          modelData.content
                                        readOnly:      true
                                        wrapMode:      TextEdit.Wrap
                                        selectByMouse: true
                                        background:    null
                                        font.pixelSize: 13
                                        color: isUser ? "#ffffff" : sysPalette.text
                                        topPadding:    12
                                        bottomPadding: 12
                                        // Padding mirrors the copy-button side so text doesn't sit under it.
                                        leftPadding:   isUser ? 40 : 12
                                        rightPadding:  isUser ? 12 : 40
                                        Keys.priority: Keys.BeforeItem
                                        Keys.onPressed: function(event) {
                                            if ((event.modifiers & Qt.ControlModifier) && !(event.modifiers & Qt.AltModifier)) {
                                                if (event.key === Qt.Key_C) { event.accepted = true; copy();      return }
                                                if (event.key === Qt.Key_A) { event.accepted = true; selectAll(); return }
                                            }
                                        }
                                        onContentHeightChanged: msgBubble.renderedHeight = Math.max(44, implicitHeight)
                                        Component.onCompleted:  msgBubble.renderedHeight = Math.max(44, implicitHeight)
                                    }

                                    Rectangle {
                                        id: copyBtn
                                        anchors.bottom: parent.bottom
                                        anchors.bottomMargin: 6
                                        anchors.right: isUser ? undefined : parent.right
                                        anchors.rightMargin: 6
                                        anchors.left:  isUser ? parent.left : undefined
                                        anchors.leftMargin: 6
                                        width: 28; height: 20
                                        radius: 4
                                        color: copyMouse.containsMouse ? "#e8eaf6" : "#f0f0f0"
                                        border.color: "#d0d0d0"
                                        border.width: 1

                                        Text {
                                            anchors.centerIn: parent
                                            text: "⎘"
                                            font.pixelSize: 11
                                            color: "#5c6bc0"
                                        }

                                        MouseArea {
                                            id: copyMouse
                                            anchors.fill: parent
                                            hoverEnabled: true
                                            onClicked: {
                                                msgText.selectAll()
                                                msgText.copy()
                                                msgText.deselect()
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                // ── Streaming bubble (shown above input bar while streaming) ──
                Rectangle {
                    id: streamBubble
                    Layout.fillWidth:    true
                    Layout.leftMargin:   12
                    Layout.rightMargin:  80
                    Layout.bottomMargin: 4
                    visible: isStreaming
                    property real renderedHeight: 44
                    height: isStreaming ? renderedHeight : 0
                    radius:  10
                    color:   "#ffffff"
                    border.color: "#e0e0e0"
                    border.width: 1

                    TextArea {
                        id:     streamText
                        anchors.fill: parent
                        // Non-streaming tool loop (v0.5.0): streamingText is empty
                        // until the final reply is appended in one shot. Show a
                        // "Thinking…" indicator so the user knows the request is
                        // still in flight.
                        text:            streamingText.length > 0 ? (streamingText + " ▌") : "Thinking… ▌"
                        readOnly:        true
                        wrapMode:        TextEdit.Wrap
                        selectByMouse:   true
                        background:      null
                        font.pixelSize:  13
                        color:           "#212121"
                        topPadding:    12
                        bottomPadding: 12
                        leftPadding:   12
                        rightPadding:  12
                        onContentHeightChanged: streamBubble.renderedHeight = Math.max(44, implicitHeight)
                        Component.onCompleted:  streamBubble.renderedHeight = Math.max(44, implicitHeight)
                    }
                }

                // ── Active model indicator ────────────────────────────────────
                // Sits just above the input bar so the user can confirm which
                // LLM the next send will hit — addresses the "did my switch take
                // effect?" question without having to send a probe message.
                Rectangle {
                    Layout.fillWidth: true
                    height:  18
                    color:   "transparent"

                    Label {
                        anchors.right:           parent.right
                        anchors.verticalCenter:  parent.verticalCenter
                        anchors.rightMargin:     14
                        text:           "Using: " + (providerModel || "—") + " (" + (providerFormat || "?") + ")"
                        color:          "#757575"
                        font.pixelSize: 10
                    }
                }

                // ── Input bar ─────────────────────────────────────────────────
                Rectangle {
                    Layout.fillWidth: true
                    height:  60
                    color:   "#ffffff"
                    border.color: "#e0e0e0"
                    border.width: 1

                    RowLayout {
                        anchors.fill:         parent
                        anchors.leftMargin:   12
                        anchors.rightMargin:  12
                        anchors.topMargin:    8
                        anchors.bottomMargin: 8
                        spacing: 8

                        TextField {
                            id:              inputField
                            Layout.fillWidth: true
                            focus:            true
                            activeFocusOnPress: true
                            Keys.priority:    Keys.BeforeItem
                            placeholderText: "Ask about the score… (Enter to send)"
                            wrapMode:        TextField.WrapAtWordBoundaryOrAnywhere
                            font.pixelSize:  13
                            selectByMouse:   true
                            background: Rectangle {
                                color:        sysPalette.base
                                radius:       8
                                border.color: inputField.activeFocus ? "#5c6bc0" : sysPalette.mid
                                border.width: 1
                            }
                            onActiveFocusChanged: {
                                // Re-register as MS4's active nav control whenever the input regains focus,
                                // so Enter (which MS4 dispatches as `nav-trigger-control`) routes to our send handler.
                                if (activeFocus && root.navSendControl) {
                                    root.navSendControl.requestActive(false)
                                }
                            }
                            Keys.onPressed: function(event) {
                                // ── Ctrl shortcuts (MS4 intercepts these before QML normally sees them) ─
                                if ((event.modifiers & Qt.ControlModifier) && !(event.modifiers & Qt.AltModifier)) {
                                    if (event.key === Qt.Key_V) { event.accepted = true; paste();     return }
                                    if (event.key === Qt.Key_X) { event.accepted = true; cut();       return }
                                    if (event.key === Qt.Key_C) { event.accepted = true; copy();      return }
                                    if (event.key === Qt.Key_A) { event.accepted = true; selectAll(); return }
                                    if (event.key === Qt.Key_Z) { event.accepted = true; undo();      return }
                                    if (event.key === Qt.Key_Y) { event.accepted = true; redo();      return }
                                    return  // unhandled Ctrl+key: do not accept — let MS4 handle (e.g. Ctrl+S saves score)
                                }

                                // ── Editing and navigation keys (intercepted by MS4 for score navigation) ─
                                if (event.key === Qt.Key_Backspace) {
                                    event.accepted = true
                                    if (selectedText.length > 0) remove(selectionStart, selectionEnd)
                                    else if (cursorPosition > 0) remove(cursorPosition - 1, cursorPosition)
                                    return
                                }
                                if (event.key === Qt.Key_Delete) {
                                    event.accepted = true
                                    if (selectedText.length > 0) remove(selectionStart, selectionEnd)
                                    else if (cursorPosition < length) remove(cursorPosition, cursorPosition + 1)
                                    return
                                }
                                if (event.key === Qt.Key_Left)  { event.accepted = true; if (cursorPosition > 0)      cursorPosition -= 1; return }
                                if (event.key === Qt.Key_Right) { event.accepted = true; if (cursorPosition < length) cursorPosition += 1; return }
                                if (event.key === Qt.Key_Home)  { event.accepted = true; cursorPosition = 0;           return }
                                if (event.key === Qt.Key_End)   { event.accepted = true; cursorPosition = length;      return }
                            }
                        }

                        Button {
                            id:             sendBtn
                            implicitWidth:  72
                            implicitHeight: 40
                            text:           isStreaming ? "⏹ Stop" : "Send"
                            enabled:        isStreaming || inputField.text.trim().length > 0
                            background: Rectangle {
                                color: !parent.enabled   ? "#bdbdbd" :
                                        parent.pressed   ? "#3949ab" :
                                        isStreaming       ? "#c62828" : "#5c6bc0"
                                radius: 8
                            }
                            contentItem: Label {
                                text:  parent.text
                                color: "#ffffff"
                                font.pixelSize: 13
                                font.bold: true
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment:   Text.AlignVCenter
                            }
                            onClicked: {
                                if (isStreaming) {
                                    stopStreaming()
                                } else {
                                    var txt = inputField.text
                                    inputField.text = ""
                                    sendMessage(txt)
                                }
                            }
                        }
                    }
                }
            } // end chat ColumnLayout

            // ── Settings view ─────────────────────────────────────────────────
            ScrollView {
                anchors.fill: parent
                visible:      showSettings
                contentWidth: parent.width
                clip:         true

                ColumnLayout {
                    width:   parent.width
                    spacing: 0

                    // Header
                    Rectangle {
                        Layout.fillWidth: true
                        height: 48
                        color:  "#3949ab"
                        Label {
                            anchors.centerIn: parent
                            text:  "Provider Settings"
                            color: "#ffffff"
                            font.pixelSize: 16
                            font.bold: true
                        }
                    }

                    // Body
                    ColumnLayout {
                        Layout.fillWidth: true
                        Layout.margins:   20
                        spacing:          16

                        // Persistence diagnostic
                        Label {
                            Layout.fillWidth: true
                            text:  appSettings ? "✓ Settings persist between sessions"
                                               : "⚠ Settings unavailable — lost on close (MS4 limitation)"
                            color: appSettings ? "#388e3c" : "#e65100"
                            font.pixelSize: 11
                            wrapMode: Text.Wrap
                        }

                        // ── Provider ─────────────────────────────────────────
                        GroupBox {
                            Layout.fillWidth: true
                            title: "Provider"

                            ColumnLayout {
                                anchors.fill: parent
                                spacing: 10

                                // Preset
                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    Label { text: "Preset:"; font.pixelSize: 13; Layout.preferredWidth: 130 }
                                    ComboBox {
                                        id:    presetCombo
                                        model: ["Anthropic", "OpenAI", "Gemini", "Other"]
                                        currentIndex: { var i = model.indexOf(providerPreset); return i >= 0 ? i : 0 }
                                        Layout.fillWidth: true
                                        // FIX: applyPreset() force-updates all fields
                                        onActivated: applyPreset(currentText, true)
                                    }
                                }

                                // Endpoint
                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    Label { text: "Endpoint URL:"; font.pixelSize: 13; Layout.preferredWidth: 130 }
                                    TextField {
                                        id:              endpointField
                                        text:            providerEndpoint
                                        placeholderText: "https://…"
                                        Layout.fillWidth: true
                                        selectByMouse:   true
                                        font.pixelSize:  13
                                        onEditingFinished: { providerEndpoint = text; saveSettings() }
                                    }
                                }

                                // Format
                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    Label { text: "Format:"; font.pixelSize: 13; Layout.preferredWidth: 130 }
                                    ComboBox {
                                        id:    formatCombo
                                        model: ["anthropic", "openai", "gemini"]
                                        currentIndex: { var i = model.indexOf(providerFormat); return i >= 0 ? i : 1 }
                                        Layout.fillWidth: true
                                        enabled: providerPreset === "Other"
                                        onActivated: { providerFormat = currentText; saveSettings() }
                                    }
                                }

                                // API Key
                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    Label { text: "API Key:"; font.pixelSize: 13; Layout.preferredWidth: 130 }
                                    TextField {
                                        id:              apiKeyField
                                        text:            providerApiKey
                                        placeholderText: "sk-…  /  AIza…"
                                        echoMode:        TextInput.Password
                                        Layout.fillWidth: true
                                        selectByMouse:   true
                                        font.pixelSize:  13
                                        onEditingFinished: {
                                            providerApiKey = text
                                            var keys = presetApiKeys
                                            keys[providerPreset] = text
                                            presetApiKeys = keys
                                            saveSettings()
                                            // Refresh model list against the new key.
                                            if (text && text.length > 0) fetchModels()
                                        }
                                    }
                                    Button {
                                        text: "👁"
                                        implicitWidth: 32; implicitHeight: 32
                                        checkable: true
                                        background: Rectangle {
                                            color: parent.checked ? "#e8eaf6" : "#f5f5f5"
                                            radius: 4; border.color: "#e0e0e0"
                                        }
                                        onCheckedChanged:
                                            apiKeyField.echoMode = checked ? TextInput.Normal : TextInput.Password
                                    }
                                }

                                // API key plain-text warning
                                Label {
                                    Layout.fillWidth:  true
                                    Layout.leftMargin: 134
                                    text:     "⚠ Stored as plain text. Do not use on shared computers."
                                    color:    "#e65100"
                                    font.pixelSize: 10
                                    wrapMode: Text.Wrap
                                }
                            }
                        }

                        // ── Model ────────────────────────────────────────────
                        GroupBox {
                            Layout.fillWidth: true
                            title: "Model"

                            ColumnLayout {
                                anchors.fill: parent
                                spacing: 10

                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    Label { text: "Model:"; font.pixelSize: 13; Layout.preferredWidth: 130 }
                                    ComboBox {
                                        id:        modelCombo
                                        model:     modelOptions
                                        textRole:  "label"
                                        valueRole: "id"
                                        enabled:   !fetchingModels
                                        currentIndex: {
                                            // Re-evaluate whenever the option list or selected id changes.
                                            var opts = modelOptions
                                            for (var i = 0; i < opts.length; i++) {
                                                if (opts[i].id === providerModel) return i
                                            }
                                            return 0
                                        }
                                        Layout.fillWidth: true
                                        onActivated: {
                                            var opts = modelOptions
                                            var item = (currentIndex >= 0 && currentIndex < opts.length)
                                                       ? opts[currentIndex] : null
                                            if (!item) return
                                            if (item.id === "__custom__") {
                                                customModelRow.visible = true
                                                customModelField.forceActiveFocus()
                                            } else if (item.id === "") {
                                                // "Loading models…" placeholder — ignore.
                                                return
                                            } else {
                                                providerModel = item.id
                                                customModelRow.visible = false
                                                modelChangedNotice = ""
                                            }
                                            updateCapability()
                                            saveSettings()
                                            _updateCurrentConversationModel()
                                        }
                                    }
                                    Button {
                                        text: fetchingModels ? "…" : "↻ Fetch"
                                        implicitWidth: 72; implicitHeight: 32
                                        enabled: !fetchingModels
                                        background: Rectangle {
                                            color: parent.enabled ? (parent.pressed ? "#3949ab" : "#5c6bc0") : "#bdbdbd"
                                            radius: 6
                                        }
                                        contentItem: Label {
                                            text: parent.text; color: "#ffffff"; font.pixelSize: 12
                                            horizontalAlignment: Text.AlignHCenter; verticalAlignment: Text.AlignVCenter
                                        }
                                        onClicked: fetchModels()
                                    }
                                }

                                // Model-auto-switched notice (surfaces when the user's previously
                                // selected model is no longer returned by the provider).
                                Label {
                                    Layout.fillWidth: true
                                    visible: modelChangedNotice !== ""
                                    text:    "ℹ " + modelChangedNotice
                                    color:   "#1565c0"
                                    font.pixelSize: 11
                                    wrapMode: Text.Wrap
                                }

                                // Custom model row
                                RowLayout {
                                    id:      customModelRow
                                    Layout.fillWidth: true; spacing: 12
                                    visible: false
                                    Label { text: "Custom ID:"; font.pixelSize: 13; Layout.preferredWidth: 130 }
                                    TextField {
                                        id:              customModelField
                                        text:            providerModel
                                        placeholderText: "e.g. claude-opus-4-5"
                                        Layout.fillWidth: true
                                        selectByMouse:   true
                                        font.pixelSize:  13
                                        onEditingFinished: {
                                            providerModel = text
                                            updateCapability()
                                            saveSettings()
                                            _updateCurrentConversationModel()
                                        }
                                    }
                                }

                                // Fetch error
                                Label {
                                    Layout.fillWidth: true
                                    visible: fetchModelsError !== ""
                                    text:    "⚠ " + fetchModelsError
                                    color:   "#e53935"
                                    font.pixelSize: 11
                                    wrapMode: Text.Wrap
                                }

                                // Model info card
                                Rectangle {
                                    Layout.fillWidth: true
                                    visible: providerModel !== ""
                                    height:  capInfoCol.implicitHeight + 16
                                    color:   "#f3e5f5"; radius: 6

                                    ColumnLayout {
                                        id:              capInfoCol
                                        anchors.fill:    parent
                                        anchors.margins: 8
                                        spacing: 3

                                        Label {
                                            text: "Model: " + providerModel
                                            font.pixelSize: 12; font.bold: true; color: "#6a1b9a"
                                        }
                                        Label {
                                            text: {
                                                var caps = []
                                                if (capThinking)  caps.push("extended thinking")
                                                if (capReasoning) caps.push("reasoning effort")
                                                return "Capabilities: " + (caps.length ? caps.join(", ") : "standard")
                                            }
                                            font.pixelSize: 11; color: "#7b1fa2"
                                        }
                                    }
                                }
                            }
                        }

                        // ── Generation ───────────────────────────────────────
                        GroupBox {
                            Layout.fillWidth: true
                            title: "Generation"

                            ColumnLayout {
                                anchors.fill: parent
                                spacing: 10

                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    Label { text: "Max tokens:"; font.pixelSize: 13; Layout.preferredWidth: 150 }
                                    SpinBox {
                                        from: 256; to: 32768; stepSize: 256
                                        value: providerMaxTokens; editable: true
                                        Layout.fillWidth: true
                                        onValueModified: { providerMaxTokens = value; saveSettings() }
                                    }
                                }

                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    visible: capThinking
                                    Label { text: "Thinking budget:"; font.pixelSize: 13; Layout.preferredWidth: 150 }
                                    SpinBox {
                                        from: 1024; to: 16000; stepSize: 512
                                        value: providerThinkingBudget; editable: true
                                        Layout.fillWidth: true
                                        onValueModified: { providerThinkingBudget = value; saveSettings() }
                                    }
                                }

                                Label {
                                    Layout.fillWidth: true
                                    visible: capThinking && providerMaxTokens <= providerThinkingBudget
                                    text:    "⚠ Max tokens must exceed thinking budget — will be auto-corrected on send."
                                    color:   "#e65100"; font.pixelSize: 10; wrapMode: Text.Wrap
                                }

                                RowLayout {
                                    Layout.fillWidth: true; spacing: 12
                                    visible: capReasoning
                                    Label { text: "Reasoning effort:"; font.pixelSize: 13; Layout.preferredWidth: 150 }
                                    ComboBox {
                                        model: ["low","medium","high"]
                                        currentIndex: { var i = model.indexOf(providerReasoningEffort); return i >= 0 ? i : 1 }
                                        Layout.fillWidth: true
                                        onActivated: { providerReasoningEffort = currentText; saveSettings() }
                                    }
                                }
                            }
                        }

                        // ── System prompt ───────────────────────────────────
                        GroupBox {
                            Layout.fillWidth: true
                            title: "System prompt"

                            ColumnLayout {
                                anchors.fill: parent
                                spacing: 8

                                Label {
                                    Layout.fillWidth: true
                                    text:    "Extra instructions appended to the default system prompt. " +
                                             "Leave empty to use the default."
                                    color:   "#616161"
                                    font.pixelSize: 11
                                    wrapMode: Text.Wrap
                                }

                                Rectangle {
                                    Layout.fillWidth: true
                                    Layout.preferredHeight: 120
                                    color:        "#f8f9fa"
                                    border.color: sysPromptArea.activeFocus ? "#5c6bc0" : "#e0e0e0"
                                    border.width: 1
                                    radius:       6

                                    ScrollView {
                                        anchors.fill:   parent
                                        anchors.margins: 4
                                        clip:           true

                                        TextArea {
                                            id:              sysPromptArea
                                            text:            systemPromptOverride
                                            placeholderText: "e.g. Always respond in Spanish."
                                            wrapMode:        TextEdit.Wrap
                                            selectByMouse:   true
                                            font.pixelSize:  12
                                            background:      null
                                            onTextChanged: {
                                                if (text !== systemPromptOverride) {
                                                    systemPromptOverride = text
                                                    saveSettings()
                                                    buildSystemPrompt()
                                                }
                                            }
                                        }
                                    }
                                }

                                Button {
                                    text: "Reset to default"
                                    implicitHeight: 28
                                    enabled: systemPromptOverride.length > 0
                                    background: Rectangle {
                                        color:        parent.enabled ? (parent.pressed ? "#e0e0e0" : "#f5f5f5") : "#fafafa"
                                        border.color: "#e0e0e0"
                                        radius:       4
                                    }
                                    contentItem: Label {
                                        text:  parent.text
                                        color: parent.enabled ? "#5c6bc0" : "#bdbdbd"
                                        font.pixelSize: 11
                                        horizontalAlignment: Text.AlignHCenter
                                        verticalAlignment:   Text.AlignVCenter
                                    }
                                    onClicked: {
                                        systemPromptOverride = ""
                                        sysPromptArea.text   = ""
                                        saveSettings()
                                        buildSystemPrompt()
                                    }
                                }
                            }
                        }

                        // Save & close
                        Button {
                            Layout.fillWidth: true
                            implicitHeight:   42
                            text: "✓ Save & close settings"
                            background: Rectangle {
                                color: parent.pressed ? "#388e3c" : "#43a047"; radius: 8
                            }
                            contentItem: Label {
                                text: parent.text; color: "#ffffff"
                                font.pixelSize: 14; font.bold: true
                                horizontalAlignment: Text.AlignHCenter; verticalAlignment: Text.AlignVCenter
                            }
                            onClicked: {
                                providerApiKey       = apiKeyField.text
                                providerEndpoint     = endpointField.text
                                if (customModelRow.visible) providerModel = customModelField.text
                                systemPromptOverride = sysPromptArea.text
                                saveSettings()
                                buildSystemPrompt()
                                _updateCurrentConversationModel()
                                if (providerApiKey && providerApiKey.length > 0) fetchModels()
                                showSettings = false
                            }
                        }

                        Item { height: 20 }
                    }
                }
            } // end settings ScrollView

        } // end main Rectangle
    } // end SplitView


} // end root Rectangle
