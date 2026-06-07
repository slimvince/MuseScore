# LLM Integration in MuseScore Studio — Design Document

> **Status:** Design phase. No code written yet.  
> This document captures architectural decisions and rationale from the initial
> design session (May 2026). It is the starting point for implementation, not a
> finished specification.

---

## Table of Contents

1. [Vision](#1-vision)
2. [What LLMs Can Do in MuseScore](#2-what-llms-can-do-in-musescore)
3. [Key Design Decisions](#3-key-design-decisions)
4. [Architecture](#4-architecture)
5. [The Core Access Layer](#5-the-core-access-layer)
6. [Score Addressing](#6-score-addressing)
7. [Serialization Design](#7-serialization-design)
8. [The LLM Client](#8-the-llm-client)
9. [Implementation Phases](#9-implementation-phases)
10. [Relationship to the Composing Module](#10-relationship-to-the-composing-module)
11. [Relationship to the Plugin API](#11-relationship-to-the-plugin-api)

---

## 1. Vision

MuseScore Studio should support natural-language interaction with scores — the
ability to ask questions about a score, identify problems, compare sections, and
make changes through conversation with an LLM of the user's choice.

The analogy is what AI coding assistants have become in software development:
an always-available collaborator with deep domain knowledge, capable of
reasoning about the artefact you are working on, offering suggestions, catching
errors, and executing tedious tasks on request.

**Claude Composer** is the working name for this capability.

The central difference from coding assistants is that music has dimensions
code does not: it is temporal, emotional, physical (instruments have breath
and range), and often communicates through affect rather than correctness.
The LLM brings music theory, orchestration knowledge, style awareness, and
compositional judgment — not just pattern matching.

---

## 2. What LLMs Can Do in MuseScore

These are not exhaustive feature specs but the *categories of capability* the
architecture must support.

### 2.1 Analytical Intelligence (read-only)

Questions about the score answered in plain language:

- *"Where do you think the climax of this piece is, and why?"*
- *"What key is this in, and does it modulate?"*
- *"Describe the form of this piece."*
- *"What's the most technically demanding passage for the oboe?"*
- *"Why does bar 23 sound unresolved?"*
- *"What harmonic technique is being used in the bridge?"*

These require no score modification. They are conversations about the score.
Phase 1 is entirely this category.

### 2.2 Quality Assurance and Comparison (read-only)

Systematic checks and cross-section comparison:

- *"The section between rehearsal marks C and D should be the same as between
  G and H. Can you identify any differences in the oboe part that should not
  be there?"*
- *"Are there any parallel fifths in the string section?"*
- *"Check that the trumpet part never exceeds its comfortable range."*
- *"Are the dynamics consistent across all the wind parts?"*
- *"Find every place where the rhythm in the violins does not match the cellos."*

These are tasks a human editor would perform by tedious manual scanning.
The LLM replaces that labour. Phase 2 is this category.

### 2.3 Targeted Modification (read + write)

Executing changes identified through conversation:

- *"Make the fixes you just suggested."*  
  (Continues directly from a QA conversation — no re-analysis needed.)
- *"Let trumpet 1 and baritone sax swap notes in bars 12–16."*
- *"Add staccato markings to every note in the oboe part that has one in
  the clarinet at the same beat."*
- *"The section between C and D should be identical to G–H. Make it so."*

### 2.4 Creative Assistance (generation)

Higher-level compositional tasks:

- *"Reharmonize the second verse. Preserve voice leading quality. Respect
  each instrument's comfortable range."*
- *"Add an 8-bar intro in a slower tempo, in the parallel minor, with a
  chord progression that leads naturally to verse 1."*
- *"The drums in the last verse could be more intense — add short fills
  and ghost notes where appropriate."*
- *"Write a walking bass line for bars 9–16 that supports these chord
  changes."*
- *"Fill in the alto part to complete the SATB texture."*

### 2.5 Ambient Intelligence (always-on)

Passive assistance the user did not explicitly request:

- Parallel fifths and octaves highlighted as the user edits
- Out-of-range notes flagged per instrument
- Harmonic inconsistencies noted
- Phrase completion suggestions shown as ghost notes
- Hover tooltips showing harmonic function, voice leading quality,
  instrument range status

The ambient layer uses the rule-based analysis from the composing module,
not the LLM, for latency reasons. The LLM handles the on-demand tiers above.

---

## 3. Key Design Decisions

### 3.1 Purpose-built integration, not a general plugin API

The LLM integration is a focused, purpose-built system — not a byproduct
of the general plugin API reform.

The general plugin API needs a complete redesign (the current `src/engraving/api/v1/`
is architecturally weak, exposes the raw DOM through a thin QML wrapper, and
lacks the operation coverage required for programmatic use). That reform is a
large, long-term project requiring community buy-in.

The LLM integration has a narrower scope and can be built on a purpose-built
internal API without waiting for the general reform. The two projects evolve
independently and may converge later.

### 3.2 Stateless tool-call model

The LLM interacts with the score through **tool calls** — discrete, self-contained
operations that carry their own target address. The LLM does not hold object
references between calls.

This is the right model because LLMs are inherently stateless across tool
invocations. It also simplifies the implementation: no object lifecycle
management, no proxy objects, no handle invalidation logic. Each tool call
is complete in itself.

Contrast with the stateful model needed for traditional plugins (long-lived,
hold object references, react to change events). These are different programming
models with different requirements; the LLM integration deliberately adopts
the simpler one.

### 3.3 LLM as search agent, not score dump recipient

The LLM is never given the entire score as a blob of data. For large scores,
this would exhaust the context window with noise and degrade reasoning quality.

Instead, the LLM has **search tools** it calls against the score:

```
find_notes(instrument, pitch, octave, measure_range) → NoteList
get_part(instrument, from, to) → PartSection
get_measure(n) → MeasureDetail
search_harmony(chord_type, measure_range) → HarmonyList
get_structural_events() → TempoMarks, KeyChanges, RehearsalMarks, InstrumentEntries
```

This mirrors how Claude Code works with a large codebase: it does not paste
all files into context. It uses Grep, Glob, and Read to find and read precisely
what it needs. Claude Composer uses the equivalent search tools against the
score.

The quality of what these tools return is as important as having them.
See Section 6.

### 3.4 The filter: intentional vs. computed

The LLM sees everything the user intentionally set. It does not see what the
engraving engine computed automatically.

**Visible to LLM:** pitch, duration, voice, dynamics, articulation, note
colors, visibility flags, text formatting (italic lyrics, bold text), manual
placement overrides, instrument assignments, chord symbols, lyrics, tempo
marks, key signatures, time signatures, rehearsal marks, spanners (ties,
slurs, hairpins).

**Hidden from LLM:** pixel positions, bounding boxes, beam geometry, stem
lengths, slur curves, spacing adjustments, staff line positions — anything
in `LayoutData`.

The practical boundary: if a property is stored via the `Pid` property system
on an `EngravingObject`, it is intentional and belongs in the LLM's view.
If it lives in `LayoutData` and is regenerated on each layout pass, it is
computed and should be excluded.

Note that visual properties such as color are *semantically meaningful* and
must be included. A user who has colored certain notes red is using color to
communicate intent — *"these notes are flagged for review"* — and the LLM
needs to see that.

### 3.5 Multi-provider LLM support

The system supports multiple LLM providers with a thin abstraction layer:
Anthropic (Claude), OpenAI (GPT), Ollama (local models), and others.
Users configure their provider and API key in MuseScore preferences.

This mirrors how AI integrations in modern IDEs work — the tool is provider-
agnostic; the user brings their own model.

The abstraction is thin: `ILLMProvider` with a single `complete(messages,
tools, stream)` method. Each implementation handles its own authentication,
tool-call protocol, and streaming format. Adding a new provider is a few
days of work.

### 3.6 Conversational continuity

Analysis and modification are phases in one conversation thread, not separate
operations. When the LLM identifies differences in a QA query, it holds that
knowledge in the conversation history. "Make the fixes you suggested" does
not require re-analysis — the LLM executes what it already reasoned through.

This is the same model that makes Claude Code effective: read the files,
understand the problem, make the changes — all in one reasoning thread.
The conversation history *is* the working context.

---

## 4. Architecture

```
┌─────────────────────────────────────────────────────┐
│  MuseScore Studio UI                                │
│  Chat panel — conversation history, streaming       │
│  response, diff preview, accept/reject              │
└─────────────────┬───────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────┐
│  LLM Bridge (src/llm/ — new module)                 │
│                                                     │
│  ConversationManager — multi-turn history           │
│  ContextAssembler — builds LLM request context      │
│  ToolDispatcher — routes LLM tool calls             │
│  ValidationLayer — checks output before apply       │
│  LLMClient — ILLMProvider + implementations         │
└──────┬──────────────────────────┬───────────────────┘
       │                          │
┌──────▼──────────┐   ┌───────────▼───────────────────┐
│  Score Reader   │   │  Operation Set                │
│  (search tools) │   │  (modification tools)         │
│                 │   │                               │
│  find_notes()   │   │  set_pitch()                  │
│  get_part()     │   │  transpose()                  │
│  get_measure()  │   │  set_dynamic()                │
│  search_harmony │   │  add_note()                   │
│  get_events()   │   │  delete_note()                │
│                 │   │  set_chord_symbol()            │
│  Taps directly  │   │  copy_section()               │
│  into DOM +     │   │  set_articulation()            │
│  composing      │   │  … ~40 operations total       │
│  module output  │   │                               │
└──────┬──────────┘   └───────────┬───────────────────┘
       │                          │
┌──────▼──────────────────────────▼───────────────────┐
│  MuseScore Internal Layer                           │
│  INotationInteraction, INotationElements            │
│  Composing module (harmonic analysis)               │
│  UndoStack — all modifications are undoable         │
└─────────────────────────────────────────────────────┘
```

### 4.1 Score Reader

Provides the LLM's read access to the score through discrete search tools.
Each tool returns a compact, clean, musically-meaningful representation.

Built directly on the MuseScore DOM (`src/engraving/dom/`) and the composing
module's analysis output. Does not require the general plugin API.

Instrument addressing uses the part name as the user knows it ("Trumpet 1",
"Oboe", "Gran Cassa"). Section addressing uses the full range of musical
landmarks — see Section 5.

### 4.2 Operation Set

~40 curated operations covering the high-value modification tasks. Not an
attempt to expose every `INotationInteraction` method. Chosen by observing
which operations Phase 1 and Phase 2 usage actually reaches for.

Each operation:
- Has a JSON schema (for LLM tool-call definitions)
- Groups into one undo macro (the entire LLM response is one Ctrl+Z)
- Validates its arguments before executing
- Returns a structured result including any warnings

### 4.3 Validation Layer

Before any modification is applied, the validation layer checks:

- Instrument range violations (per-instrument comfortable and absolute ranges)
- Voice leading issues (parallel fifths/octaves, voice crossing) — via composing module
- Rhythmic consistency (operation does not produce malformed measures)

Violations are fed back to the LLM as tool call errors, not shown to the user.
The LLM corrects and retries. Only clean output reaches the score.

### 4.4 LLM Client

```cpp
class ILLMProvider {
public:
    virtual ~ILLMProvider() = default;
    virtual Response complete(
        const std::vector<Message>& history,
        const std::vector<ToolDefinition>& tools,
        bool stream
    ) = 0;
    virtual std::string name() const = 0;
    virtual Capabilities capabilities() const = 0;  // streaming, toolUse, maxTokens
};
```

Implementations: `AnthropicProvider`, `OpenAIProvider`, `OllamaProvider`.
Tool definitions are generated automatically from the operation set schemas.

---

## 5. The Core Access Layer

### 5.1 Shared foundation

Both the LLM bridge and the plugin API need the same underlying capabilities:
full read access to the score DOM, full write access via operations, access to
MuseScore settings and preferences, and access to playback and project state.
Rather than each consumer building its own private wiring into the internals,
a shared **Core Access Layer** provides this foundation once.

```
┌──────────────────────────────────────────────────┐
│           Core Access Layer                      │
│  IScoreReader    IScoreWriter                    │
│  ISettingsReader  ISettingsWriter                │
│  IStateReader    IStateWriter                    │
│  IInstrumentDatabase                             │
└──────────────┬───────────────────┬───────────────┘
               │                   │
    ┌──────────▼──────┐   ┌────────▼──────────────┐
    │   LLM Bridge    │   │     Plugin API        │
    │  Serialisation  │   │  Event subscriptions  │
    │  Tool schemas   │   │  Object handles       │
    │  LLM client     │   │  Language bindings    │
    └─────────────────┘   └───────────────────────┘
```

The LLM bridge and plugin API diverge at the layer above this:
- LLM bridge adds: serialisation, tool schemas, LLM client, conversation management
- Plugin API adds: event subscriptions, EID-backed object handles, long-lived
  sessions, language bindings (QML, potentially Python/Lua)

Event subscriptions are plugin territory only. The LLM is stateless — it does
not sit waiting for score changes. It is called, responds, and is done.

### 5.2 The existing interfaces already define most of this

A thorough audit of the MuseScore source (`src/notation/`, `src/project/`,
`src/playback/`, `muse/framework/`) reveals that the internal interface
family already covers almost everything the Core Access Layer needs. **The
Core Access Layer is not a redesign — it is a facade over interfaces that
already exist.**

Key existing interfaces and what they cover:

| Interface | File | Covers |
|-----------|------|--------|
| `INotation` | `src/notation/inotation.h` | Master aggregator; entry point to all notation sub-interfaces |
| `INotationElements` | `src/notation/inotationelements.h` | Score element query and search |
| `INotationParts` | `src/notation/inotationparts.h` | Parts, staves, instruments — full structural control |
| `INotationStyle` | `src/notation/inotationstyle.h` | Style properties, load/save |
| `INotationInteraction` | `src/notation/inotationinteraction.h` | All editing operations (~350 lines) |
| `INotationNoteInput` | `src/notation/inotationnoteinput.h` | Note input mode and state |
| `INotationSelection` | `src/notation/inotationselection.h` | Current selection, clipboard |
| `INotationUndoStack` | `src/notation/internal/inotationundostack.h` | Undo/redo, transaction batching |
| `INotationPlayback` | `src/notation/inotationplayback.h` | Playback tracks, tempo, timing |
| `INotationConfiguration` | `src/notation/inotationconfiguration.h` | UI/behaviour preferences (~235 lines) |
| `IInstrumentsRepository` | `src/notation/iinstrumentsrepository.h` | Instrument templates, genres, ranges |
| `INotationProject` | `src/project/inotationproject.h` | File operations, metadata, cloud |
| `IProjectConfiguration` | `src/project/iprojectconfiguration.h` | Project paths and preferences |
| `IProjectAudioSettings` | `src/project/iprojectaudiosettings.h` | Per-track audio, FX, solo/mute |
| `IPlaybackController` | `src/playback/iplaybackcontroller.h` | Master playback control and state |
| `IMasterNotation` | `src/notation/imasternotation.h` | Master score, excerpts |

The notification system (`muse::async::Channel<T>`, `muse::async::Notification`)
is also already in place throughout these interfaces. `INotationUndoStack`
already exposes `changesChannel()` emitting `ScoreChanges` on every committed
operation — this is the event source for the plugin API's subscription layer.

### 5.3 The information model — key design point

There are **no direct object references** from Note to Staff or Note to Measure.
The `MusicalAddress` embedded in every ChordRest (and inherited by Note) is the
sole locator:

| Field | Derives |
|---|---|
| `partId` + `staffIndexInPart` | Which staff |
| `measureNumber` | Which measure |
| `voice` | Which voice (1–4) |
| `beat` / `tick` | Exact position |

**Consequence:** queries are pure filter operations over MusicalAddresses — no
graph traversal. `notesInRange(partId, measureRange)` filters ChordRests where
`address.partId == X and address.measureNumber in [from..to]`.

**MusicalAddress as join key:** Harmony, Annotation, and Note at the same
MusicalAddress are co-located. "What chord symbol is sounding at this note?" is
a match on the composite key — equivalent to a SQL join.

**Address alone does not uniquely identify a Note.** Multiple notes in the same
chord share an identical address (same part + staff + measure + beat + voice).
A `NoteId` is required to unambiguously target a single note. `NoteId` must
appear explicitly on the Note entity; it maps internally to the EID system.

### 5.4 What needs to be added

The existing interfaces are designed for MuseScore's own UI layer — they are
not broken, but they are not immediately consumable by an LLM bridge or a
general plugin API without a thin adaptor layer. Three gaps:

**1. LLM-friendly query methods**

`INotationElements` returns raw `EngravingItem*` vectors — useful internally,
not for external consumption. The Core Access Layer adds clean query methods:

```cpp
// Existing (internal):
std::vector<EngravingItem*> elements(FilterElementsOptions) const;

// New (Core Access Layer):
NoteList notesInRange(PartId, VoiceIndex, MeasureRange) const;
HarmonyList harmoniesInRange(MeasureRange) const;
StructuralEvents structuralIndex() const;  // tempos, keys, rehearsal marks, instrument entries
```

**2. Batch / transactional write**

`INotationInteraction` operates one action at a time. The Core Access Layer
wraps `INotationUndoStack::prepareChanges()` / `commitChanges()` into an
explicit transaction scope so that an entire LLM response — potentially
dozens of individual note changes — collapses into a single Ctrl+Z:

```cpp
class IScoreTransaction {
    void begin(const std::string& label);
    void commit();
    void rollback();
    // All IScoreWriter calls between begin/commit are one undo step
};
```

**3. Aggregated change description**

The existing `ScoreChanges` struct (emitted by `changesChannel()`) contains
`changedObjects` as a map of raw `EngravingObject*` pointers — opaque to
external consumers. The Core Access Layer translates these to stable musical
addresses (part + measure + beat + voice) before surfacing them to plugin
subscribers.

### 5.5 What the Core Access Layer is NOT responsible for

- Serialisation to LLM text format — that is the LLM bridge's job
- Tool schema generation — LLM bridge
- Event subscription management — plugin API
- Object handle / EID lifecycle — plugin API
- Language bindings (QML, Python) — plugin API
- LLM client / conversation management — LLM bridge

---

## 6. Score Addressing

Musicians address regions of a score through musical events and content —
not through bar numbers (though bar numbers work too). The system must
resolve all of these to measure ranges:

**Explicit markers stored in the score:**
- Rehearsal marks: *"between C and D"*, *"from rehearsal mark 4"*
- Tempo marks: *"from the Andante"*, *"where the Presto starts"*
- Key changes: *"after the modulation to B flat"*, *"the second key change"*
- Section labels if present: *"the bridge"*, *"verse 2"*
- Double barlines and repeat signs

**Texture and instrumentation events (inferred):**
- *"When the choir enters"* — detect when vocal staves go from resting to playing
- *"Where the solo ends"* — detect texture change in a solo instrument
- *"When the strings drop out"*
- *"The first time the full orchestra plays together"*

**Content references:**
- *"The first C sharp in the cello"* — pitch search in a specific part
- *"The second beat of the gran cassa"* — beat position in a specific instrument
- *"The bar with the trumpet high C"*

**Conversation references:**
- *"The enharmonic spelling we just fixed"* — resolved from conversation history,
  not from the score at all. The LLM already knows which bar was modified.

**Relative references:**
- *"Three bars before the key change"*
- *"The last four bars of the bridge"*
- *"The second time the main theme appears"*

**Resolution strategy:** The LLM is the resolver. It is given the score's
structural events (all tempo marks, key changes, rehearsal marks, instrument
activity map) and resolves natural language references against that. For
content references ("first C sharp in the cello"), it calls `find_notes()`.
For conversation references, it uses its own history.

No pre-built index. The LLM's language understanding is the resolution
mechanism. Do not try to enumerate and pre-categorize reference types —
the space is open-ended. The system only needs to ensure the LLM has the
information required to resolve whatever reference the user makes.

---

## 7. Serialization Design

The quality of the score representation given to the LLM is the single most
important design decision in the system. Garbage in, garbage out.

### 7.1 Principles

**Hierarchical, not flat.** Instrument → Measure → Beat → Note, not a flat
list of events sorted by tick.

**Beat-aligned, not tick-aligned.** Beats expressed relative to the time
signature, not as raw tick fractions. "Beat 2 of a 3/4 measure" is more
meaningful to reasoning than "tick 1440."

**Musically annotated.** Include chord symbols and harmonic analysis from
the composing module alongside the notes. The LLM should not have to
re-derive harmony from raw pitch data.

**Clean.** No rendering data. No layout objects. No beam geometry. No
bounding boxes. The filter is: intentional properties only (see §3.4).

**Compact.** Optimised for LLM context window efficiency. Abbreviate where
unambiguous. For large scores, the LLM calls search tools iteratively to
read only the sections it needs — it never receives the whole score at once.

### 7.2 Example (sketch)

```json
{
  "part": "Oboe",
  "transposition": "concert",
  "measures": [
    {
      "measure": 12,
      "key": "G major",
      "timeSig": "4/4",
      "tempo": "Andante ♩=76",
      "harmony": "V7",
      "beats": [
        { "beat": 1, "notes": [{ "pitch": "D5", "duration": "quarter", "dynamic": "mp" }] },
        { "beat": 2, "notes": [{ "pitch": "C5", "duration": "quarter", "articulation": "staccato" }] },
        { "beat": 3, "notes": [{ "pitch": "B4", "duration": "half" }] }
      ]
    }
  ]
}
```

### 7.3 What to include

| Property | Include? | Notes |
|----------|----------|-------|
| Pitch (concert) | Yes | Always concert pitch unless user requests written |
| Duration | Yes | As beat fraction or common name (quarter, half, etc.) |
| Voice | Yes | When multi-voice content is present |
| Dynamic | Yes | Only when explicitly marked |
| Articulation | Yes | staccato, tenuto, accent, etc. |
| Chord symbols | Yes | From composing module analysis |
| Key | Yes | Per measure where it changes |
| Tempo | Yes | Per measure where it changes |
| Rehearsal marks | Yes | As measure annotations |
| Lyrics | Yes | With syllable boundaries |
| Note color | Yes | Semantically meaningful (user-set) |
| Visibility flag | Yes | Hidden notes affect LLM reasoning |
| Ties / slurs | Yes | As note properties ("tiedForward", "slurStart") |
| Stem direction | No | Computed by engraving engine |
| Beam type | No | Computed |
| Pixel positions | No | Computed |
| Staff line position | No | Computed |

---

## 8. The LLM Client

### 8.1 Multi-provider abstraction

Users choose their LLM provider in MuseScore preferences. The abstraction
requires only that a provider supports tool use (function calling). Providers
without tool use support may be used for read-only analysis but cannot drive
score modification.

**Supported at launch:**
- Anthropic (Claude 3+ — tool use supported)
- OpenAI (GPT-4+ — function calling supported)
- Ollama (local models — tool use varies by model)

### 8.2 Tool definitions

Tool definitions for the LLM are generated automatically from the operation
set schemas. Adding a new operation to the operation set automatically makes
it available as an LLM tool. No manual maintenance.

### 8.3 Context window strategy

For short conversations about small scores: send the full relevant section
upfront.

For large scores or long conversations: the LLM uses search tools to fetch
sections on demand. The conversation history contains the results of previous
searches — the LLM does not need to re-fetch what it already read.

The composing module's harmonic analysis of the relevant section is always
included in the initial context, even when notes are not. This gives the LLM
the harmonic landscape without requiring it to re-derive from pitch data.

---

## 9. Implementation Phases

### Phase 1 — Score Intelligence (read-only) — ~2 weeks

**Goal:** The user can ask questions about the open score and receive
musically intelligent answers.

**Deliverables:**
- Score serializer: whole score → clean JSON (small/medium scores)
- Partial serializer: get section by instrument + measure range
- LLM client with multi-provider support (Anthropic + OpenAI at minimum)
- Basic chat panel UI in MuseScore (send message, receive streamed response)
- No score modification, no tool calls

**Example interactions that work:**
- *"Where is the climax of this piece and why?"*
- *"What key is this in? Does it modulate?"*
- *"Describe the form."*
- *"What's the hardest passage for the horn?"*

### Phase 2 — Score QA and Comparison — ~1–2 additional weeks

**Goal:** The user can compare sections, find inconsistencies, and run
targeted checks. Still no modification.

**Deliverables:**
- Search tools (find_notes, get_part, get_measure, get_events)
- Structural events index (tempo marks, key changes, rehearsal marks,
  instrument activity) passed as context
- Multi-section serialization (send two sections for comparison)
- LLM tool-call handling in the bridge (read-only tools only)

**Example interactions that work:**
- *"Find differences between the oboe in C–D vs. G–H."*
- *"Are there parallel fifths in the brass section?"*
- *"Check all trumpet notes are within comfortable range."*

### Phase 3 — Score Modification — ~4–6 additional weeks

**Goal:** The LLM can make changes to the score, with preview and undo.

**Deliverables:**
- Operation set (~40 operations, beginning with the highest-value ones)
- Undo macro grouping (entire LLM response = one Ctrl+Z)
- Validation layer (range, voice leading)
- Diff preview UI (show what will change before applying)
- Accept / reject flow

**Example interactions that work:**
- *"Make the fixes you suggested."*
- *"Swap trumpet 1 and baritone sax in bars 12–16."*
- *"Add staccato to every note in the oboe that has one in the clarinet
  at the same beat."*

### Phase 4 — Creative Generation — ongoing

Higher-level tasks (reharmonization, generating new sections, arranging
from a melody) are built on top of the Phase 3 infrastructure. No new
architectural pieces required — the capability comes from the model's
musical knowledge applied through the existing tool set.

---

## 10. Relationship to the Composing Module

> **Note:** `src/composing/` is not part of official MuseScore Studio. It is
> a module under active development by this project, intended as a future
> contribution to MuseScore. It is not yet merged upstream.

The composing module is not just a separate analysis tool — it is a critical
component of the LLM integration.

**The composing module is the LLM's context provider.** Rather than asking the
LLM to re-derive harmonic structure from raw pitch data, the composing module's
analysis is included in every score section sent to the LLM:

- Chord symbols and Roman numeral analysis per measure
- Key and mode inference
- Harmonic rhythm (where chord changes occur)
- Voice leading quality assessments (parallel motion, voice crossing)

This is the "language server" insight applied to music: the composing module
provides pre-digested musical context that makes LLM reasoning more accurate
and less reliant on inference from raw data. Code assistants are better when
they have type information and call graphs, not just source text. Musical
assistants are better when they have harmonic analysis, not just note lists.

**The validation layer uses the composing module.** After the LLM generates
modified score content, the composing module's voice leading and harmonic
analysis is applied as a validator before the changes reach the score.

When the composing module is eventually surfaced through the Core Access Layer
(as a first-class query service alongside score read/write), both the LLM
bridge and the plugin API gain access to it without either having to know about
its internal implementation.

---

## 11. Relationship to the Plugin API

The current plugin API (`src/engraving/api/v1/`) is architecturally weak:
a thin QML wrapper around the raw DOM that bypasses the clean `INotation*`
interface layer, lacks operation coverage, and has no cross-process capability.
A full redesign is a separate long-term project.

### The deeper architectural point

With a properly designed plugin API — one that sits on top of the Core Access
Layer and includes network access and UI extension points — **the LLM
integration does not need to be in MuseScore core at all.** It becomes a
plugin. This has significant implications:

- The LLM bridge is optional — users who do not want it do not ship it
- Multiple LLM integrations can coexist (different providers, different UX
  approaches, community-built alternatives)
- MuseScore core has no dependency on any specific LLM provider
- The integration can be updated independently of MuseScore releases

### The UI extension point question

Whether the ambient intelligence layer (ghost note completions, score overlays,
inline annotations) can live in a plugin depends on whether the plugin API
exposes rendering hooks into the score view — not just separate side panels.
This is a deliberate design decision in the plugin API that determines whether
the LLM integration can be fully external or requires a thin ambient layer in
core.

### Build strategy

**Short term:** Build the Core Access Layer. Implement the LLM bridge as a
native module, but strictly constrained — it only uses the Core Access Layer,
never going behind it to the DOM directly. This gives a working demo quickly.

**Medium term:** Build the plugin API on top of the same Core Access Layer.
Since the LLM bridge already respects the Core Access Layer boundary, migrating
it to run as a plugin is then straightforward.

**End state:** LLM integration is a plugin (or family of plugins). Core
Access Layer is the shared foundation for both the plugin API and any
remaining thin core layer for ambient intelligence.

### The two plugin API tiers, for reference

- **Stateless tier** (command/query, musical addresses) — this is what the
  LLM bridge needs. The LLM bridge as currently designed is a working
  prototype of this tier.

- **Stateful tier** (EID-backed object handles, event subscriptions,
  long-lived sessions) — this is what live reactive plugins need. Not
  required for LLM integration.

---

*Document created: May 2026. Authors: Vincent Wong, Claude (Anthropic).*  
*Update this document when architectural decisions change. Do not let it go stale.*
