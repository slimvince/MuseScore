# Score Context Architecture
_Last updated: 2026-05-15_

## Problem statement

The LLM needs to know about the open score to answer musical questions. The challenge is that scores vary enormously in size — from a 16-bar lead sheet (dozens of notes) to a full orchestral symphony (tens of thousands of notes) — and LLM context windows, while large, are not infinite. We need a strategy that works across this range without requiring the LLM to ask multiple round-trip questions for simple queries.

---

## Agreed architecture: database agent pattern

Inspired by how LLMs are given access to databases: you don't dump the entire database into the prompt. Instead you inject the schema (structure/metadata) always, and provide computational tools for queries the LLM can't answer from schema alone.

Three tiers:

### Tier 1 — Metadata (always injected)
Always present in the system prompt regardless of score size. Gives the LLM enough to answer structural questions without any computation.

Current fields injected:
- `title`, `composer`
- `nmeasures`, `nstaves`, `ntracks`
- `parts[]` — part names
- `hasHarmonies`, `harmonyCount`
- `hasLyrics`, `lyricCount`
- `noteCount` — total note count (always present even if note array is omitted)
- `notesOmitted: true` — flag set when score exceeds the note array size guard

### Tier 2 — Full note array (small scores only)
For scores with ≤ 2000 notes, the complete note array is injected alongside metadata. This lets the LLM answer any read query — apex, note count, interval patterns, lyric hyphenation errors, parallel fifths — in a single pass with no tool calls.

Note array fields per note (compact names to save tokens):
```json
{ "m": 12, "st": 0, "v": 1, "p": 64, "tpc": 18, "dur": "quarter", "tied": false }
```
- `m` — measure number
- `st` — staff index (0-based)
- `v` — voice (0–3)
- `p` — MIDI pitch (0–127)
- `tpc` — tonal pitch class (useful for enharmonic/spelling analysis)
- `dur` — duration string
- `tied` — true if this note is tied from a previous note (avoid double-counting)

**Verified working** in MS5 on "midnight" score — 6,907 notes triggers `notesOmitted: true` correctly.

Implementation: measure-based traversal (not cursor-based — cursor API behaves differently in Extensions 2.0). Covers all 4 voices per staff via `segment.elementAt(staffIdx * 4 + voice)`.

### Tier 3 — Computational read tools (large scores, future)
For scores where `notesOmitted: true`, the LLM cannot answer note-level queries from the injected context alone. The solution is QML-side computational tools that run the query and return only the answer — not raw data.

Planned tools (not yet implemented):
- `find_apex(staffIdx?)` → `{ pitch: 76, measure: 18, staff: 0 }` — highest note
- `count_notes(staffIdx?, voice?, measureRange?)` → `{ count: 342 }`
- `get_notes_in_range(measureStart, measureEnd, staffIdx?)` → note array for that slice
- `get_chord_at(measure, beat, staffIdx)` → chord spelling at a specific point
- `find_intervals(intervalType, staffIdx?)` → parallel fifths, octaves, etc.

These tools run entirely in QML, do the computation against the live score, and return a minimal answer. The LLM asks once, gets the answer, no repeated round-trips for the same data.

**Decision: tools for reads are not needed yet.** For the current use case (typical choral/chamber scores ≤ 2000 notes), full injection is simpler and sufficient. Tools become necessary when: (a) scores exceed the injection limit, or (b) write operations are needed. Implement tools when write operations are built; add read tools as optimization later.

---

## Chunking — open question

**Not yet resolved.** The user raised the question of passing the score "in chunks" — whether this means:

1. **Sequential injection across messages** — splitting the note array into pages and feeding them to the LLM across multiple turns before asking the question. Expensive in tokens and round-trips; only useful if the model needs to "read" the whole score before answering. Unlikely to be the right approach.

2. **On-demand slices via tools** — `get_notes_in_range(measureStart, measureEnd)` returns a chunk of the score the LLM specifically needs to examine. This is the computational tool approach above and IS the intended solution for large scores.

3. **Segment-level summaries** — pre-compute section summaries (e.g. "measures 1–16: Bb major, homophonic, forte") and inject those instead of raw notes for large scores. More complex but potentially very powerful for high-level structural questions.

**Current stance:** options 2 and 3 are both compatible with the database agent pattern. Option 2 (on-demand slices) maps directly to the computational tools in Tier 3. Option 3 (pre-computed summaries) is an additional layer that could be added to Tier 1. Neither is needed until write tools are being built. **Revisit when implementing Tier 3.**

---

## Write tools (future phase)

When the LLM should be able to modify the score, write tools are mandatory — you can't inject your way to a write. Planned write tools:

- `add_dynamic(measure, staff, dynamic)` — insert a dynamic marking
- `flip_enharmonic(measure, staff, voice, noteIndex)` — respell a note
- `transpose_selection(semitones)` — transpose selected region
- `add_lyric(measure, staff, syllable)` — attach a lyric

Write tools require careful UX: the LLM should propose changes, the user confirms, then the tool executes. Undo must work. This is a significant feature, not a quick add.

---

## Implementation notes

- The note walk is in `refreshScoreContext()` in Main.qml, runs on extension open and on the score-context refresh button
- The walk uses `s.firstMeasure` → `measure.nextMeasure` → `segment.elementAt(staffIdx * 4 + voice)` with `api.engraving.Element.CHORD` type check
- The result is JSON-stringified and injected into the system prompt for every LLM call
- Score context is displayed in the collapsible "Score context" chip at the top of the chat panel

---

## What NOT to do

**Do not add ad-hoc derived fields** to the injected context (e.g. pitch histograms, highest-note summaries, pre-computed statistics). These feel helpful but they:
1. Violate the database agent pattern — the LLM should get schema + tools, not pre-digested answers
2. Grow the always-injected Tier 1 context without a principled reason
3. Duplicate work that Tier 3 computational tools will do properly, on demand, for any query

When a user asks "where is the highest note?" on a large score and the LLM can't answer because `notesOmitted: true` — that is **correct and expected behaviour**. The right fix is to implement the `find_apex` tool (Tier 3), not to pre-inject the answer.

---

## 2000-note threshold — rationale

Chosen pragmatically: a 4-part SATB chorale of ~50 measures has ~800 notes (well under). A piano sonata movement might be 1,500–2,500. An orchestral excerpt quickly exceeds 2,000. The threshold keeps typical chamber/choral scores fully injected while preventing accidentally sending 10,000+ notes to the LLM. Adjustable if experience shows it's too conservative or too permissive.
