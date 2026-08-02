# Decisions group H — Layer 5 and Layer 6 — function, cadence, grouping

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-079 — The function layer annotates and resolves; it never rewrites the committed chord

> additive over L4 (it annotates and resolves; it never
> rewrites the committed chord identity)

**In plain words.** The stage that works out a chord's role in the key may label it and settle open questions, but it may not change which chord was identified.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1392-1393`

**Provenance.** ARCHITECTURE.md:1389-1398 (Layer 5 - Built+Dormant, design ratified)

### D-080 — Carried abstentions are resolved by selecting among the carried readings, never re-derived

> the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived)

**In plain words.** Where the chord stage could not decide, the function stage picks from the options it was handed. It does not work the chord out again from the notes.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1396-1397`

**Provenance.** ARCHITECTURE.md:1389-1398

### D-081 — The cadence detector is key-agnostic

> The cadence
> detector is **key-agnostic** (it votes for the key; it does not read a resolved key).

**In plain words.** The part that spots cadences must not be told what key it is in - it is one of the things that decides the key, so reading the answer first would be circular.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1396-1397`

**Provenance.** ARCHITECTURE.md:1397. open_items/OI-166 records that the built detector is key-agnostic but CHORD-derived, not the bass-driven pre-scan specified

### D-082 — The grouping layer is additive, read-only, with no feedback

> additive, read-only, no feedback into L5.

**In plain words.** The stage that assembles phrases and key areas only organises what earlier stages decided. It never changes their answers.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1404`

**Provenance.** ARCHITECTURE.md:1400-1407 (Layer 6 - Design-only, v1 spec)

### D-083 — Hierarchy, periods and prolongation are out of the validatable core

> Hierarchy,
> periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15).

**In plain words.** Deeper structural theory - nested hierarchy, periods, prolongation - is deliberately left out, because we have no annotated music to check it against.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1405-1406`

**Provenance.** ARCHITECTURE.md:1400-1407, deriving from D-029

### D-084 — The progression-schema recognizer is a consumer of the function layer, not a new layer

> an L5 *consumer* (a prior + an annotation), not a new layer

**In plain words.** Recognising well-known chord patterns is something that reads the finished analysis and annotates it. It is not another stage in the chain.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1411`

**Provenance.** ARCHITECTURE.md:1409-1414 'Scaffolding-first, deferred'

### D-085 — The voice-leading axis is a separate axis with its own layers

> the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
>   chord **voicing / arrangement** are analysed)

**In plain words.** How the individual voices move is a second, independent line of analysis alongside the harmonic one, with its own stages.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Home.** `ARCHITECTURE.md:895-896`

**Provenance.** ARCHITECTURE.md:896-899 records the foundation BUILT (dormant). ARCHITECTURE.md:1415-1415 still says the voice-leading layer is 'not built' - see OPEN_ITEMS OI-232

### D-248 — Tonicization labels are not implemented and are deferred

> - Tonicization labels (V/V, V/ii, V/IV etc.) — **NOT YET IMPLEMENTED**
>   (deferred; no `relativeRoot`/secondary-dominant field in
>   `ChordFunction`; requires standalone implementation first)

**In plain words.** Applied-chord labels such as V/V are not produced. The data structure has no field for the relative root, and the feature waits on a standalone implementation.

**Why.** The constraint is stated in the record: `ChordFunction` carries no `relativeRoot` or secondary-dominant field, so the label has nowhere to live (ARCHITECTURE.md:6013-6014).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6012-6014`

**Provenance.** ARCHITECTURE.md:6012-6014. Section 5.10 (ARCHITECTURE.md:3860) is the tonicization section; the memory-held backlog item is recorded in the same terms. ★ RATIFIED (user, 2026-08-02) with the revisit to be PLANNED: for the ultimate objective (maximum-precision inference) the feature may be needed — the ground truth annotates applied chords, so not producing them costs Roman-numeral agreement wherever the annotator wrote one. Row OI-267 carries the planning obligation, including the OI-53 tension (a live classifier emitting V7/x was found on the legacy path while this entry's home says not implemented).

