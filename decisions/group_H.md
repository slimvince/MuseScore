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

**Home.** `ARCHITECTURE.md:1234-1235`

**Provenance.** ARCHITECTURE.md:1231-1240 (Layer 5 - Built+Dormant, design ratified)

### D-080 — Carried abstentions are resolved by selecting among the carried readings, never re-derived

> the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived)

**In plain words.** Where the chord stage could not decide, the function stage picks from the options it was handed. It does not work the chord out again from the notes.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1238-1239`

**Provenance.** ARCHITECTURE.md:1231-1240

### D-081 — The cadence detector is key-agnostic

> The cadence
> detector is **key-agnostic** (it votes for the key; it does not read a resolved key).

**In plain words.** The part that spots cadences must not be told what key it is in - it is one of the things that decides the key, so reading the answer first would be circular.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1238-1239`

**Provenance.** ARCHITECTURE.md:1239. open_items/OI-166 records that the built detector is key-agnostic but CHORD-derived, not the bass-driven pre-scan specified

### D-082 — The grouping layer is additive, read-only, with no feedback

> additive, read-only, no feedback into L5.

**In plain words.** The stage that assembles phrases and key areas only organises what earlier stages decided. It never changes their answers.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1246`

**Provenance.** ARCHITECTURE.md:1242-1249 (Layer 6 - Design-only, v1 spec)

### D-083 — Hierarchy, periods and prolongation are out of the validatable core

> Hierarchy,
> periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15).

**In plain words.** Deeper structural theory - nested hierarchy, periods, prolongation - is deliberately left out, because we have no annotated music to check it against.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1247-1248`

**Provenance.** ARCHITECTURE.md:1242-1249, deriving from D-029

### D-084 — The progression-schema recognizer is a consumer of the function layer, not a new layer

> an L5 *consumer* (a prior + an annotation), not a new layer

**In plain words.** Recognising well-known chord patterns is something that reads the finished analysis and annotates it. It is not another stage in the chain.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1253`

**Provenance.** ARCHITECTURE.md:1251-1256 'Scaffolding-first, deferred'

### D-085 — The voice-leading axis is a separate axis with its own layers

> the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
>   chord **voicing / arrangement** are analysed)

**In plain words.** How the individual voices move is a second, independent line of analysis alongside the harmonic one, with its own stages.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Home.** `ARCHITECTURE.md:829-830`

**Provenance.** ARCHITECTURE.md:830-833 records the foundation BUILT (dormant). ARCHITECTURE.md:1257-1258 still says the voice-leading layer is 'not built' - see OPEN_ITEMS OI-232

