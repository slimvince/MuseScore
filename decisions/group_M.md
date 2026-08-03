# Decisions group M — The style system and the knowledge base

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-128 — Styles are defined entirely in data; adding one never requires code changes

> Musical styles are defined entirely in JSON files. The C++ code implements mechanisms —
> voice leading optimization, chord generation, voicing rules — while JSON files define
> parameters. Adding a new style never requires C++ changes.

**In plain words.** A musical style is a data file. The program code implements the mechanisms - voice leading, chord generation, voicing - and the style file supplies the numbers that make one style behave differently from another. Adding a style is never a code change.

**Why.** Stated constraint, ARCHITECTURE.md:440-442 (§2.1) with the worked wrong/correct pair at :392-402: behaviour that branched on a style's identity would make every new or renamed style a code change.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4402`

**Provenance.** ARCHITECTURE.md:4292-4296 (§6.1); the principle it realizes is D-070 (§2.1). No date or ratifier stated.

### D-129 — Style conflicts resolve by a declared priority - explicit overrides always win

> **Conflict resolution priority:**
> 1. System defaults — lowest priority
> 2. Mixin sources — in declared order, later overrides earlier
> 3. Explicit `overrides` in the style file — highest priority, always wins

**In plain words.** When a style assembles itself from several inherited sources, the order of precedence is fixed: system defaults are weakest, inherited sources come next in the order they are declared with later ones winning, and anything the style file states explicitly wins outright.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4446`

**Provenance.** ARCHITECTURE.md:4338-4341 (§6.2). No date or ratifier stated.

### D-130 — The style loader never names a style in code

> The style loader scans the styles directory recursively and loads all valid JSON files.
> It never references specific style IDs in code — it simply loads whatever it finds.

**In plain words.** The loader reads whatever style files it finds in the styles directory. No style's name appears anywhere in the program code.

**Why.** Stated constraint, ARCHITECTURE.md:487-490 (§2.4): no comparison against a style name anywhere in the codebase - style-specific behaviour flows entirely through parameters.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4482`

**Provenance.** ARCHITECTURE.md:4372-4375 (§6.4); the principle it realizes is D-070 (§2.1/§2.4). No date or ratifier stated.

### D-131 — One shared style taxonomy, not two parallel vocabularies

> The style vocabulary the presets select on is **one shared, hierarchical taxonomy** (common-practice / jazz / vernacular
> families — Baroque, Classical/galant, Romantic; trad, swing/songbook, bebop, hard-bop, cool, modal; blues, ragtime,
> gospel-soul, rock, pop, folk, barbershop) — the **same** set the Harmonic Vocabulary (§7) tags its entries with, not two
> parallel vocabularies. Inclusion rule: a style is listed iff it has a **distinct functional-harmonic vocabulary** (free
> jazz / atonal excluded).

**In plain words.** The list of style families the presets choose from is the SAME list the harmonic vocabulary tags its entries with - one hierarchy, not two that can drift apart. A style earns a place on it only if its functional harmony is genuinely distinct, which is why free jazz and atonal music are not on it.

**Why.** Stated constraint, ARCHITECTURE.md:4422-4424 - #6, one path per concern, applied to a vocabulary: two parallel taxonomies of the same thing would diverge, and the inclusion rule (a distinct functional-harmonic vocabulary) is what keeps the list from growing by analogy.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4528`

**Provenance.** ARCHITECTURE.md:4418-4428 (§6.7); full proposal `cowork_progression_schema_dictionary.md` §6/§12 and `cowork_style_clustering_plan.md`. No date or ratifier stated.

### D-132 — The style taxonomy is a theory-based first version; grounding it empirically is committed work

> It is a **theory-based v1**; **empirically grounding** it — deriving the clusters *and* the
> per-style weights by clustering corpora — is committed future work (`cowork_style_clustering_plan.md`)

**In plain words.** The style families and their weights are currently drawn from music theory, not from data. Deriving both from corpora instead is recorded as work that will be done, not as an option.

**Why.** Stated constraint, ARCHITECTURE.md:4425-4427: the clusters and their feature distributions are one data-derived object, and it is reachable for jazz and pop from lead-sheet corpora even where note-level ground truth is scarce - which is what makes the grounding committable rather than aspirational.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4532`

**Provenance.** ARCHITECTURE.md:4418-4428 (§6.7). No date or ratifier stated.

### D-133 — The harmonic vocabulary is a queried reference component, not a layer of the analysis

> It is reference knowledge **queried** by the layers and by
> future tools, **not a pipeline layer**. Entries carry **provenance** (established theory), not a ground-truth-validation
> status — validation is the *consumer's* concern (verifiability contract, §2.15).

**In plain words.** The catalogue of progressions and substitutions is something the analysis stages ask questions of, not a stage they pass through. Its entries say where the theory comes from; whether that theory holds up against real music is the caller's question, not the catalogue's.

**Why.** Stated constraint, ARCHITECTURE.md:4446 - the verifiability contract (D-029): reference knowledge grounded in established theory may be carried without corpus validation, provided the consumer that puts it under load is the one that must validate it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4552`

**Provenance.** ARCHITECTURE.md:4437-4451 (§7); own specification `cowork_progression_schema_dictionary.md`. No date or ratifier stated.

### D-406 — The catalog owns the NAMED progressions and substitutions; the pairwise licensing grammar is owned by the function layer — the two are never derived from each other

> **The D5 dependency map (one owner per concern — restated here, mirrored in code).** Two places know about chord
> successions: **this component** owns the **named progressions and substitutions** (the catalog); **Layer 5's
> `functionprogression`** owns the **pairwise licensing grammar** (which root motions are licensed at all). *Changing the
> catalog* → change this component only (the grammar never needs an edit; but a new entry must pass the **consistency
> test** — every adjacent chord pair licensed — or it is mis-encoded OR a genuine grammar gap). *Changing the grammar* →
> change `functionprogression` only. The two are **not derived from each other**; the **only coupling is the consistency
> test**, and it runs **one way (catalog → grammar)**. Owner ruling: D5 (`cowork_progression_schema_design.md` §6),

**In plain words.** Two places in the system know about which chords may follow which. This reference catalog holds the named progressions and substitutions; the function layer holds the separate rule about which root motions are allowed at all. Neither is computed from the other. The single link between them runs one way: every adjacent pair in a new catalog entry must be allowed by the grammar, and a pair that is not is either a mis-encoded entry or a genuine gap in the grammar.

**Why.** One owner per concern (guiding principle #6), applied to a case where two components could each plausibly have held the knowledge. The one-way consistency test is what keeps the split honest, and it has already earned itself: running it at the consumer build on 2026-07-02 found 6 entries using 11 root motions the grammar did not license, all of them musically correct — so they were ruled grammar gaps rather than catalog errors, and the amendment closing them was ratified 2026-07-03.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_dictionary.md:35-41`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:41-46 records the owner ruling as D5 of `cowork_progression_schema_design.md` §6, user-ratified 2026-07-02, with the cross-referencing comment blocks at `functionprogression.h` and `harmonicvocabulary.h` and the test at `progressionrecognizer_tests.cpp`. Beside D-341, which is the grammar-completion amendment this ruling's consistency test produced. NOTE: this document uses the label 'D5' for TWO different decisions — this ownership ruling (§1) and the harmonic-scope component decision (§7, entered as D-408) — which is a collision in the document's own local labelling, not in this register. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-407 — The vocabulary supplies ranked candidates and DECIDES nothing — the threshold, the style weighting and what to do with a candidate are the consumer's

> - **Decide anything.** The matching threshold, the style weighting, and the choice of what to do with a candidate are the
>   **consumer's**; the component only supplies ranked candidates.

**In plain words.** The catalog answers questions and hands back a ranked list. How good a match has to be before it counts, how much weight a style carries, and what is done with the answer are all decided by whatever is asking, never by the catalog.

**Why.** Stated in the document as the firewall line (§6): the component holds structural content and returns ranked structural matches, while the weighting, the threshold and the decision are precision-phase work at the consumer. Adding or correcting an entry is a content change here; tuning how strongly an entry fires is a change there. This keeps the catalog free of fitted values, so it can be shared by an analysis consumer and a future composition consumer that would weight it differently.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:53-54`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:52-54 (§2, what it does not do), with the firewall line at :244-246 (§6). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-408 — Voice-leading is a DIFFERENT DIMENSION and is not held in the harmonic vocabulary — a schema defined by its voice-leading is present only by its harmonic pattern

> - **Hold voice-leading.** It is the **harmonic** vocabulary — chords and functions. Voice-leading (the motion of
>   individual voices — for example the melodic lines that, together with the harmony, complete a galant schema) is a
>   **different dimension**, held elsewhere (a future voice-leading layer, or a separate voice-leading vocabulary). A schema
>   conventionally defined by voice-leading is present here **only by its harmonic pattern**; its voice-leading is held
>   elsewhere and combined when the complete schema is recognised.

**In plain words.** This catalog holds chords and functions. How individual voices move is a separate dimension kept elsewhere. Patterns that musicians define partly by their melodic lines — the galant schemata among them — appear here by their chord pattern alone, and are only fully recognised when the voice-leading side is brought in from where it lives.

**Why.** Recorded as component decision D5 with its rejected alternative: holding voice-leading here was considered and refused because it is a different dimension with its own future layer. The consequence is carried as a stated risk (§9) rather than hidden — a consumer must not read a galant entry as full schema recognition.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:55-59`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:55-59 (§2), restated as component decision D5 at :261-263 (§7) with its rejected alternative, and carried as a risk at :279-280 (§9). Consistent with `ARCHITECTURE.md` §7, which states the same exclusion. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-409 — There is no binary match or no-match — only a score on a ranked list, and the list may be EMPTY

> consumer applies its own style weighting and its own threshold; there is no binary match/no-match, only the score (as the
> inference layers carry ranked alternatives with confidence). **The list may be empty** — for *recognise* (nothing
> matches), for *suggest follow/precede* (no progression fits), and for *suggest replace* (no substitution applies) — and a
> consumer must handle an empty result, never assuming a non-empty one.

**In plain words.** A query never comes back with a yes or a no. It comes back with a ranked list of candidates, each carrying a number saying how well it fits, and the list is sometimes empty. Anything asking must cope with an empty answer and must never assume there is one.

**Why.** Stated with the rule: this is the same shape the inference layers use, which carry ranked alternatives with a confidence rather than a forced single answer (the cross-cutting contract, D-027). Requiring the consumer to handle an empty list is what stops a recogniser from inventing a match to have something to return.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:121-124`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:114-124 (§4). Beside D-027, the cross-cutting contract that every layer emits ranked candidates plus a confidence rather than a forced point estimate. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-410 — The first version matches EXACTLY AND WHOLE; the partial matcher is deferred with its decision structure already fixed and only its constants left open

>   substitution), and the returned entry then carries that mapping for the substituted member. **As built (v1) the
>   realisation is exact and whole** — every member matched, full length, no partial spans; the declared Stage-5
>   **partial matcher** relaxes this by crediting matched members with penalties for gaps and substitutions (that
>   decision structure — credit per matched member, order preserved, length credited, substituted members admitted at a
>   penalty — is fixed here; its constants are the consumer's precision-phase weights).

**In plain words.** As built, a pattern is recognised only when every one of its members is present, in order, at full length. The looser matcher that credits partial matches is planned, and its shape is already decided — credit for each matched member, order preserved, length counted, members reached through a substitution admitted at a cost. What is not decided is the size of those costs, which are fitted later at whatever is asking.

**Why.** The split follows the project's firewall between structure and fitted values: the decision structure is settled now, in the specification, so the later fitting event chooses numbers rather than a design. The as-built exactness is verified at the recogniser rather than asserted — the document records that no intermediate score can arise in the first version because no partial match can.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:102-106`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:96-106 (§4 recognise) and :114-118 (the match score under the partial matcher). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-411 — The Axis loop is ONE entry in one canonical rotation — its other rotations become rotation-tolerant matching on that entry, never three more entries

>   variant `1̂–♭7̂–♭6̂–5̂`); Andalusian cadence `i–bVII–bVI–V`; doo-wop `I–vi–IV–V`; Axis `I–V–vi–IV` — **rotation rule (as built, verified at the catalog):** ONE entry, encoded in the canonical
>   rotation `I–V–vi–IV` only; the v1 exact matcher therefore recognises only that order, and admitting the other three
>   rotations (as rotation-tolerant matching on this one entry, never as three more entries) is a declared decision for
>   the Stage-5 partial matcher;

**In plain words.** The four-chord pop loop that can start on any of its four chords is stored once, in one chosen order. The first version therefore recognises only that order. Recognising the other three starting points is a planned change to how matching works on that single entry, and explicitly not a decision to store the loop four times.

**Why.** The reason is in the rule itself: storing a rotation as a separate entry would make one convention into four records, which is the duplication the catalog's one-entry-per-convention organisation exists to avoid (§6, one encyclopedia, not per-style silos). Recorded as verified at the catalog rather than assumed.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:185-188`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:185-188 (§5.2, the bass-line and pop loops). Same class as the circle-of-fifths entry-point rule (D-412): both fix what a realisation of one entry is allowed to look like. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-412 — The circle-of-fifths entry is the FULL cycle, and a realisation may enter at any member and run contiguously to the final tonic

> - **Sequences** `[common-practice + jazz]` — circle-of-fifths (the full cycle `I–IV–viio–iii–vi–ii–V–I`; the common
>   tail is its last members, `iii–vi–ii–V–I` — **entry-point rule:** the skeleton is the full cycle and a realisation
>   may enter at any member, running contiguously to the final `I`); descending-thirds (`I–vi–IV–ii`, extendable by

**In plain words.** The circle-of-fifths sequence is stored once as the whole cycle rather than as the several shorter tails musicians commonly write. A passage counts as realising it if it joins the cycle at any point and then runs without a break to the closing tonic.

**Why.** The same organisation reason as the rotation rule: the common short tail is a way of entering the one pattern, not a second pattern, so it is expressed as a matching rule on one entry rather than as extra records. The document states the rule where the entry is defined, so a reader cannot meet the entry without meeting what counts as realising it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:179-181`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:179-181 (§5.2, sequences). The descending-thirds entry beside it carries the same kind of rule, stated as a continuation rule rather than an ellipsis. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-413 — Upper-structure and rootless VOICING substitution is outside the harmonic vocabulary — it is a voicing, not a function

> - **Upper-structure / voicing substitution** `[jazz]` — a *voicing* device (rootless, upper-structure triads, sus); it is
>   a voicing, not a function, so it is **outside this component** (noted only so it is not mistaken for a function-level
>   substitution).

**In plain words.** Jazz devices that change how a chord is spread across the instrument, rather than which function it fills, are not substitutions in this catalog's sense and are deliberately not held here. The exclusion is written down only so that nobody mistakes them for function-level substitutions.

**Why.** Follows from the component's stated scope: the catalog holds functions and the operations that replace one function with another, and a voicing device changes neither. The record notes the exclusion is stated defensively rather than because anything asked for it.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:220-222`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:220-222 (§5.3, the substitution operations). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

### D-414 — The catalog is GENERATIVE where it can be and enumerated only where it must be

> - **D3 — Generative where possible, enumerated where necessary.** The secondary/substitute apparatus is parameterised by
>   target degree; only the named recurring patterns are enumerated. *Rejected:* a fully enumerated flat list (combinatorial,
>   and it hides the systematic structure).

**In plain words.** The systematic part of harmony — the applied and substitute chords that exist for every degree of the scale — is stored once as a pattern with the degree left open, and produced on demand. Only the patterns that have individual names and cannot be generated are written out one by one.

**Why.** Recorded as component decision D3 with its rejected alternative: a fully enumerated flat list was refused as combinatorial and because it hides the systematic structure that makes the applied and substitute apparatus one idea rather than dozens.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `cowork_progression_schema_dictionary.md:255-257`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:255-257 (§7, component decision D3), with the organisation it produces at :136-139 (§5) and the generative spine at :141-166 (§5.1). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue.

