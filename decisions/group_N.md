# Decisions group N — Generation, constraints, visualization, and the LLM integration

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-134 — A voicing type is never requested directly; the style selects it

>     // Style determines which voicing types are used and in what proportion.
>     // Never call with a specific voicing type directly — encode that in the style.

**In plain words.** A caller asking for a voicing says which style it wants, never which voicing technique. The style decides whether the answer is a drop-2, a shell, a chorale spacing or something else, and in what proportion.

**Why.** Stated constraint, ARCHITECTURE.md:4555-4558: keeping the interface voicing-type agnostic is what lets a new voicing type be added as a generator implementation plus a style parameter, without the interface changing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4563`

**Provenance.** ARCHITECTURE.md:4550-4572 (§8.2); the principle it realizes is D-070 (§2.1). No date or ratifier stated.

### D-135 — A fixed element is a hard constraint the optimizer may never modify

> Fixed elements are hard constraints in the voice leading optimizer — they anchor
> the dynamic programming search. The optimizer guarantees never modifying them.

**In plain words.** Anything the user has pinned - a note, a voice, a chord, a passage - anchors the search for good voice leading. The optimizer works around it and never changes it.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4732`

**Provenance.** ARCHITECTURE.md:4694-4733 (§9.1-§9.2). No date or ratifier stated.

### D-136 — The inference demo view is a developer tool and is not shipped

> A step-through visualization of the inference pipeline, for use by developers
> during quality assurance and algorithmic development. Not shipped to end users.

**In plain words.** The step-by-step view of the analysis making its decisions exists so a developer can watch and judge it by eye and ear. It is not part of what a user gets.

**Why.** Stated constraint, ARCHITECTURE.md:4751-4753: it exists to make musical correctness checkable by eye and ear rather than only through the automated agreement numbers.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4747`

**Provenance.** ARCHITECTURE.md:4745-4835 (§10.0), whose own status line reads 'Not yet started'. No date or ratifier stated.

### D-137 — The harmony maps are our own visual design, and are chosen partly to avoid intellectual-property claims

> MTH Pro-style map based on Berklee chord-scale theory (Nettles, Levine). Positions
> chords by functional region (tonic, subdominant, dominant) and shows available
> tensions. Our own visual design — not a reproduction of MTH Pro's specific layout.

**In plain words.** The planned map of harmonic function draws on published chord-scale theory but is laid out our own way, not copied from the commercial product that inspired it.

**Why.** Stated constraint, ARCHITECTURE.md:4888 and :4573: the circle of fifths and the Tonnetz were chosen partly because they carry no intellectual-property claim - the Tonnetz being a nineteenth-century mathematical structure - and the same reasoning is what forces an original layout for the functional map.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4906`

**Provenance.** ARCHITECTURE.md:4885-4908 (§10.2-§10.4), all three marked planned. No date or ratifier stated.

### D-138 — Chord preview uses MuseScore's note-input pathway, not the playback pipeline

> **Implementation note:** Use MuseScore's note-input preview pathway (same as hearing
> a note when clicking in input mode) — not the full score playback pipeline. The
> full pipeline has too much latency for interactive map exploration. Inference runs
> on a background thread via `QtConcurrent` to keep the UI responsive.

**In plain words.** Clicking a chord on a harmony map plays it through the same quick path MuseScore uses when you hear a note as you enter it, not through full score playback.

**Why.** Stated constraint, ARCHITECTURE.md:4938-4940: the full playback pipeline has too much delay for interactive exploration, and the inference runs on a background thread so the interface stays responsive.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4937`

**Provenance.** ARCHITECTURE.md:4910-4940 (§10.5), a planned component. No date or ratifier stated.

### D-139 — The language model holds no object references - every tool call carries its own musical address

> **Stateless tool-call model.** The LLM does not hold object references. Each
> tool call carries its own musical address. No proxy objects, no EID handles,
> no lifecycle management. This is the right model for LLM interaction and the
> simpler one to implement.

**In plain words.** When a language model asks the program to do something, it names the place in the music each time. It never holds a handle to an object in the score.

**Why.** Stated constraint, ARCHITECTURE.md:6789-6790: no proxy objects, no element handles and no lifecycle management - recorded as both the right model for this kind of interaction and the simpler one to implement.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6787`

**Provenance.** ARCHITECTURE.md:6780-6790 (§19.2), a planned module; full design `docs/llm_integration.md`. No date or ratifier stated.

### D-140 — The language model is a search agent and is never given the whole score

> **LLM as search agent.** The LLM is never given a full score dump. It has
> search tools (`find_notes`, `get_part`, `get_measure`, `search_harmony`) and
> fetches what it needs iteratively — exactly as Claude Code uses Grep and Read
> in a large codebase. Serialization quality is the critical foundation: clean,
> hierarchical, beat-aligned, free of layout noise.

**In plain words.** Rather than being handed the entire score, the language model is given tools to find what it needs and fetches it piece by piece - the way a person reads a large document by searching it.

**Why.** Stated constraint, ARCHITECTURE.md:6795-6796: because the model reads what it fetches, the quality of that serialization - clean, hierarchical, beat-aligned, free of layout noise - is the critical foundation.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6792`

**Provenance.** ARCHITECTURE.md:6780-6796 (§19.2), a planned module. No date or ratifier stated.

### D-141 — The language model sees what the user set, not what the engraving engine derived

> **Intentional vs. computed.** The LLM sees everything the user deliberately
> set (pitch, dynamics, articulation, note color, lyrics formatting, visibility).
> It does not see what the engraving engine derived (positions, beam geometry,
> stem lengths, `LayoutData`). The `Pid` property system is the practical
> boundary.

**In plain words.** The model is shown the composer's own choices - pitches, dynamics, articulation, colour, lyrics, visibility - and not the results of laying the music out, such as positions, beam geometry or stem lengths.

**Why.** Stated constraint, ARCHITECTURE.md:6802: MuseScore's own property system is the practical boundary between the two, so the split is enforceable rather than judged case by case.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6798`

**Provenance.** ARCHITECTURE.md:6780-6802 (§19.2), a planned module. No date or ratifier stated.

### D-142 — The composing module is the language model's context provider; the model never re-derives harmony

> The composing module (`src/composing/`) is the LLM's context provider. Its
> harmonic analysis output (chord symbols, Roman numerals, key inference,
> harmonic rhythm) is included in every score section sent to the LLM. The LLM
> does not re-derive harmony from raw pitch data — it receives pre-digested
> musical context.

**In plain words.** Every stretch of music sent to a language model arrives with our harmonic analysis already attached - chord symbols, Roman numerals, key, harmonic rhythm. The model reads that; it does not work the harmony out from the notes itself.

**Why.** Stated constraint, ARCHITECTURE.md:6817-6819: the same analysis also drives the validation step that checks voice leading and harmonic consistency before a generated change reaches the score, so one analysis serves both directions.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6811`

**Provenance.** ARCHITECTURE.md:6809-6823 (§19.3), a planned module. No date or ratifier stated.

### D-143 — The language-model bridge is built as a module but confined to the core access layer, so it can become a plugin

> **Build strategy:** Implement the LLM bridge as a native module initially for
> speed, but strictly constrained to the Core Access Layer only (never bypassing
> it to the DOM). When the plugin API matures, migration to a plugin is then
> straightforward. See `docs/llm_integration.md §11` for the full argument.

**In plain words.** It is written inside the program for speed of development, but restricted to the same narrow interface a plugin would have, so that moving it out to a plugin later is straightforward.

**Why.** Stated constraint, ARCHITECTURE.md:6825-6830: with a properly designed plugin interface the bridge does not need to live in the core at all - it becomes optional, independently updatable, provider-agnostic and open to community alternatives - so the constraint is what keeps that end state reachable.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6832`

**Provenance.** ARCHITECTURE.md:6825-6835 (§19.4), a planned module; full argument `docs/llm_integration.md` §11. No date or ratifier stated.

