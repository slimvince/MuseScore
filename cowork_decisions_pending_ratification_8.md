# The 9 decisions pending ratification (D-406…D-414) — complete entries

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** From the phase-1j full read of
> `cowork_progression_schema_dictionary.md` (the schema dictionary and the five-idiom style
> taxonomy, RATIFIED 2026-06-30 per its own record). Entered with status from the record only —
> RATIFICATION IS YOURS. The companion ruling is OI-279: `ARCHITECTURE.md` §6.7 still shows the
> RETIRED hand-made genre taxonomy as canonical, and register entries D-131/D-132 quote that
> stale text.


## Group M — The style system and the knowledge base

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

