# CC Instruction — Survey MuseScore Extension API for LLM Tool Exposure

## Mandatory reads before starting
- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS\memory\`

---

## Goal

We are designing a set of LLM tools for the ai-assistant MuseScore extension. The LLM will call these tools to read and modify the open score, control playback, and access mixer/settings — rather than receiving a pre-injected copy of the score data.

Before designing the tool surface we need to know what the MS4 extension API actually exposes. This task is a survey only — no code changes. Produce a structured report.

---

## What to survey

### 1. Score reading
Starting from `curScore`, walk the accessible object tree and document what can be read:

- Score-level properties (title, composer, measure count etc.)
- Parts, instruments, staves — names, counts, relationships
- Voices — how addressed, what constraints
- Measures — access by index, properties available (key sig, time sig, tempo, barline type etc.)
- Notes and rests — pitch, duration, voice, beat position, tied, grace notes
- Articulations, dynamics, slurs, ties — accessible per note / per segment?
- Chord symbols / harmony — accessible, how addressed
- Lyrics — accessible, verse number, syllable type
- Structural elements — rehearsal marks, repeat barlines, voltas, section breaks, tempo changes
- Any other musically relevant readable data

For each: note the QML/JS access path, and any known gaps or limitations.

### 2. Score writing
What mutations are possible from a QML extension? Survey both:

- **Direct API** — properties or methods on curScore / its children that accept writes
- **cmd() dispatch** — which MuseScore command strings are useful for note entry, dynamics, articulations, pitch changes, key/time signature changes, text etc.

Note whether writes land in MuseScore's undo stack (this is required — we do not want writes that bypass undo).

### 3. Playback control
What playback operations are available from a QML extension?
- Play, pause, stop, rewind
- Play from a specific measure / beat position
- Get current playback position
- Via cmd(), dedicated API, or not available?

### 4. Mixer and audio settings
What mixer access is available?
- Per-instrument volume, pan, mute, solo
- Master volume
- Via API or not exposed?

### 5. User/score settings
Any other useful controls accessible from an extension — view settings, transposition, concert pitch toggle etc.

---

## Where to look

- `C:\s\MS-core-api\` — extension API implementation, especially:
  - `muse/framework/extensions/api/v1/extapiv1.cpp` (known registration point)
  - Any v2 equivalent
  - QML-facing API files
- `C:\s\MS\ai-assistant\Main.qml` — what the extension already accesses (good starting point for confirmed-working reads)
- MuseScore source for `cmd()` string inventory — search for registered command names
- Any existing MuseScore plugin/extension API documentation in the repo

---

## Output format

Produce a markdown report with four sections: **Read**, **Write**, **Playback**, **Mixer/Settings**.

For each item:
- What it is (musical description, not internal jargon)
- How to access it (QML path or cmd() string)
- Status: ✅ confirmed available / ⚠️ partially available or uncertain / ❌ not exposed
- Any notes on limitations

Flag anything where the answer is genuinely unknown — do not guess. Unknown is useful information.

Save the report to `C:\s\MS\ai-assistant\api_survey.md`.
