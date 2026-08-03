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

> The style vocabulary the presets select on is **one shared taxonomy** — the **five idioms**: *Diatonic-functional* ·
> *Chromatic-functional* · *Seventh-functional* · *Triadic-modal* · *Chromatic-coloristic* — with **mode** (major/minor)
> and **chromaticism** (diatonic/chromatic) carried beside them as two **orthogonal cross-attributes**, not folded into
> the idiom names. Tags are **multi-valued**: one entry may carry several idioms. It is the **same** set the Harmonic
> Vocabulary (§7) tags its entries with, **not two parallel vocabularies** — that shared-set property is what this section
> exists to state, and it is unaffected by the 2026-06-30 replacement of the list itself.

**In plain words.** The list of style categories the presets choose from is the SAME list the harmonic vocabulary tags its entries with — one shared set, not two that can drift apart. That set is the five idioms (Diatonic-functional, Chromatic-functional, Seventh-functional, Triadic-modal, Chromatic-coloristic), with major/minor and diatonic/chromatic carried separately beside them; an entry may carry more than one idiom.

**Why.** One path per concern (guiding principle #6) applied to a vocabulary, with the failure mode named at `cowork_progression_schema_dictionary.md:227-229` and `:258-260`: a tag set private to the harmonic vocabulary would need a brittle preset-to-tag mapping and would drift from the presets. The set itself is empirically decided rather than asserted — cross-tradition clustering over 5,243 pieces found harmony is not organised by genre (tradition-ARI about 0.3, robust across caps) and that the robust structure is these five progression idioms plus the two cross-axes (`cowork_style_taxonomy_proposal.md:11-30`, `cowork_idiom_discovery_findings.md:122`).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4530`

**Provenance.** `ARCHITECTURE.md`:4528-4579 (§6.7). The SUBJECT is unchanged — one shared style taxonomy, not two parallel vocabularies — and the property it records survived the taxonomy's replacement intact. ★ VERBATIM RE-TAKEN 2026-08-03 (CC, phase 1k) from the corrected §6.7, on the user's OI-279 ruling of the same date (option (a): order the doc-sync correction, the genre list retained as marked historical context). The FORMER verbatim, preserved here under #12, quoted the retired hand-made genre taxonomy: "The style vocabulary the presets select on is **one shared, hierarchical taxonomy** (common-practice / jazz / vernacular families — Baroque, Classical/galant, Romantic; trad, swing/songbook, bebop, hard-bop, cool, modal; blues, ragtime, gospel-soul, rock, pop, folk, barbershop) — the **same** set the Harmonic Vocabulary (§7) tags its entries with, not two parallel vocabularies. Inclusion rule: a style is listed iff it has a **distinct functional-harmonic vocabulary** (free jazz / atonal excluded)." That list was superseded by the five-idiom set, ratified by the user 2026-06-30 and encoded (`cowork_progression_schema_dictionary.md:317-330`); the old inclusion rule belonged to the genre list and is retired with it, NOT carried across to the idioms — the idioms' own admission basis is the discovery study's cap-robustness check (`cowork_style_taxonomy_proposal.md:58-61`), now stated in §6.7. No date or ratifier is stated for the shared-taxonomy decision itself.

### D-132 — The remaining empirical grounding is the per-preset WEIGHTS alone; the clusters half is delivered by the ratified five-idiom set

> **What remains future work is the per-preset WEIGHTS, not the clusters.** Presets become named **idiom-weightings** over
> the five — a distribution over the idioms rather than a name picked from a list — and deriving those weights by
> clustering corpora is the committed work (`cowork_style_clustering_plan.md`); the weighting itself is a joint decision
> with the preset system and the recognition consumer's job, not the Harmonic Vocabulary's
> (`cowork_progression_schema_dictionary.md:317-330`). The **clusters half is delivered**: the clusters *are* the five
> idioms, discovered and encoded.

**In plain words.** Grounding the style system in data was recorded as two pieces of committed work: discovering the categories, and measuring how strongly each one weighs in each preset. The first is done — the five idioms were discovered from corpora, ratified and encoded. What is still owed is the second: a per-preset weighting over those five, derived by clustering corpora rather than asserted.

**Why.** The narrowing is decided by what was delivered: the five idioms are the clusters, discovered empirically over 5,243 pieces and ratified by the user 2026-06-30 (`cowork_style_taxonomy_proposal.md`, `cowork_progression_schema_dictionary.md:317-330`), so a status deferring that half would defer delivered work. The weights half remains genuinely owed and carries its own defense at `cowork_style_clustering_plan.md`:20-30 — the per-style progression and substitution statistics are load-bearing for a future chord-suggestion tool, and a well-calibrated style prior is one of the sub-point inference gains the best-possible-inferrer goal is made of.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4565`

**Provenance.** `ARCHITECTURE.md`:4565-4570 (§6.7). ★ NARROWED and VERBATIM RE-TAKEN 2026-08-03 (CC, phase 1k) on the user's OI-279 ruling of the same date, sub-ruling (i): DEFERRED over the **per-preset weights alone**; the CLUSTERS half is SUPERSEDED BY the five-idiom ratification of 2026-06-30 (`cowork_style_taxonomy_proposal.md:3-9`; the encoded `enum class Idiom` + `IdiomSet`). The FORMER verbatim, preserved here under #12, made no such split: "It is a **theory-based v1**; **empirically grounding** it — deriving the clusters *and* the per-style weights by clustering corpora — is committed future work (`cowork_style_clustering_plan.md`)" — whose "theory-based v1" characterization was itself false in the other direction, the five idioms being empirically discovered. The former scope was therefore undifferentiated over two halves of which one was already delivered. No date or ratifier is stated for the original deferral; the narrowing is the user's, 2026-08-03. Note: `cowork_style_clustering_plan.md` itself still presents BOTH halves as future work and carries no annotation of the delivery — rowed as `OPEN_ITEMS.md` OI-282.

### D-133 — The harmonic vocabulary is a queried reference component, not a layer of the analysis

> It is reference knowledge **queried** by the layers and by
> future tools, **not a pipeline layer**. Entries carry **provenance** (established theory), not a ground-truth-validation
> status — validation is the *consumer's* concern (verifiability contract, §2.15).

**In plain words.** The catalogue of progressions and substitutions is something the analysis stages ask questions of, not a stage they pass through. Its entries say where the theory comes from; whether that theory holds up against real music is the caller's question, not the catalogue's.

**Why.** Stated constraint, ARCHITECTURE.md:4446 - the verifiability contract (D-029): reference knowledge grounded in established theory may be carried without corpus validation, provided the consumer that puts it under load is the one that must validate it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4596`

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

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:35-41`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:41-46 records the owner ruling as D5 of `cowork_progression_schema_design.md` §6, user-ratified 2026-07-02, with the cross-referencing comment blocks at `functionprogression.h` and `harmonicvocabulary.h` and the test at `progressionrecognizer_tests.cpp`. Beside D-341, which is the grammar-completion amendment this ruling's consistency test produced. NOTE: this document uses the label 'D5' for TWO different decisions — this ownership ruling (§1) and the harmonic-scope component decision (§7, entered as D-408) — which is a collision in the document's own local labelling, not in this register. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-407 — The vocabulary supplies ranked candidates and DECIDES nothing — the threshold, the style weighting and what to do with a candidate are the consumer's

> - **Decide anything.** The matching threshold, the style weighting, and the choice of what to do with a candidate are the
>   **consumer's**; the component only supplies ranked candidates.

**In plain words.** The catalog answers questions and hands back a ranked list. How good a match has to be before it counts, how much weight a style carries, and what is done with the answer are all decided by whatever is asking, never by the catalog.

**Why.** Stated in the document as the firewall line (§6): the component holds structural content and returns ranked structural matches, while the weighting, the threshold and the decision are precision-phase work at the consumer. Adding or correcting an entry is a content change here; tuning how strongly an entry fires is a change there. This keeps the catalog free of fitted values, so it can be shared by an analysis consumer and a future composition consumer that would weight it differently.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:53-54`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:52-54 (§2, what it does not do), with the firewall line at :244-246 (§6). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-408 — Voice-leading is a DIFFERENT DIMENSION and is not held in the harmonic vocabulary — a schema defined by its voice-leading is present only by its harmonic pattern

> - **Hold voice-leading.** It is the **harmonic** vocabulary — chords and functions. Voice-leading (the motion of
>   individual voices — for example the melodic lines that, together with the harmony, complete a galant schema) is a
>   **different dimension**, held elsewhere (a future voice-leading layer, or a separate voice-leading vocabulary). A schema
>   conventionally defined by voice-leading is present here **only by its harmonic pattern**; its voice-leading is held
>   elsewhere and combined when the complete schema is recognised.

**In plain words.** This catalog holds chords and functions. How individual voices move is a separate dimension kept elsewhere. Patterns that musicians define partly by their melodic lines — the galant schemata among them — appear here by their chord pattern alone, and are only fully recognised when the voice-leading side is brought in from where it lives.

**Why.** Recorded as component decision D5 with its rejected alternative: holding voice-leading here was considered and refused because it is a different dimension with its own future layer. The consequence is carried as a stated risk (§9) rather than hidden — a consumer must not read a galant entry as full schema recognition.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:55-59`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:55-59 (§2), restated as component decision D5 at :261-263 (§7) with its rejected alternative, and carried as a risk at :279-280 (§9). Consistent with `ARCHITECTURE.md` §7, which states the same exclusion. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-409 — There is no binary match or no-match — only a score on a ranked list, and the list may be EMPTY

> consumer applies its own style weighting and its own threshold; there is no binary match/no-match, only the score (as the
> inference layers carry ranked alternatives with confidence). **The list may be empty** — for *recognise* (nothing
> matches), for *suggest follow/precede* (no progression fits), and for *suggest replace* (no substitution applies) — and a
> consumer must handle an empty result, never assuming a non-empty one.

**In plain words.** A query never comes back with a yes or a no. It comes back with a ranked list of candidates, each carrying a number saying how well it fits, and the list is sometimes empty. Anything asking must cope with an empty answer and must never assume there is one.

**Why.** Stated with the rule: this is the same shape the inference layers use, which carry ranked alternatives with a confidence rather than a forced single answer (the cross-cutting contract, D-027). Requiring the consumer to handle an empty list is what stops a recogniser from inventing a match to have something to return.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:121-124`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:114-124 (§4). Beside D-027, the cross-cutting contract that every layer emits ranked candidates plus a confidence rather than a forced point estimate. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-410 — The first version matches EXACTLY AND WHOLE; the partial matcher is deferred with its decision structure already fixed and only its constants left open

>   substitution), and the returned entry then carries that mapping for the substituted member. **As built (v1) the
>   realisation is exact and whole** — every member matched, full length, no partial spans; the declared Stage-5
>   **partial matcher** relaxes this by crediting matched members with penalties for gaps and substitutions (that
>   decision structure — credit per matched member, order preserved, length credited, substituted members admitted at a
>   penalty — is fixed here; its constants are the consumer's precision-phase weights).

**In plain words.** As built, a pattern is recognised only when every one of its members is present, in order, at full length. The looser matcher that credits partial matches is planned, and its shape is already decided — credit for each matched member, order preserved, length counted, members reached through a substitution admitted at a cost. What is not decided is the size of those costs, which are fitted later at whatever is asking.

**Why.** The split follows the project's firewall between structure and fitted values: the decision structure is settled now, in the specification, so the later fitting event chooses numbers rather than a design. The as-built exactness is verified at the recogniser rather than asserted — the document records that no intermediate score can arise in the first version because no partial match can.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:102-106`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:96-106 (§4 recognise) and :114-118 (the match score under the partial matcher). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-411 — The Axis loop is ONE entry in one canonical rotation — its other rotations become rotation-tolerant matching on that entry, never three more entries

>   variant `1̂–♭7̂–♭6̂–5̂`); Andalusian cadence `i–bVII–bVI–V`; doo-wop `I–vi–IV–V`; Axis `I–V–vi–IV` — **rotation rule (as built, verified at the catalog):** ONE entry, encoded in the canonical
>   rotation `I–V–vi–IV` only; the v1 exact matcher therefore recognises only that order, and admitting the other three
>   rotations (as rotation-tolerant matching on this one entry, never as three more entries) is a declared decision for
>   the Stage-5 partial matcher;

**In plain words.** The four-chord pop loop that can start on any of its four chords is stored once, in one chosen order. The first version therefore recognises only that order. Recognising the other three starting points is a planned change to how matching works on that single entry, and explicitly not a decision to store the loop four times.

**Why.** The reason is in the rule itself: storing a rotation as a separate entry would make one convention into four records, which is the duplication the catalog's one-entry-per-convention organisation exists to avoid (§6, one encyclopedia, not per-style silos). Recorded as verified at the catalog rather than assumed.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:185-188`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:185-188 (§5.2, the bass-line and pop loops). Same class as the circle-of-fifths entry-point rule (D-412): both fix what a realisation of one entry is allowed to look like. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-412 — The circle-of-fifths entry is the FULL cycle, and a realisation may enter at any member and run contiguously to the final tonic

> - **Sequences** `[common-practice + jazz]` — circle-of-fifths (the full cycle `I–IV–viio–iii–vi–ii–V–I`; the common
>   tail is its last members, `iii–vi–ii–V–I` — **entry-point rule:** the skeleton is the full cycle and a realisation
>   may enter at any member, running contiguously to the final `I`); descending-thirds (`I–vi–IV–ii`, extendable by

**In plain words.** The circle-of-fifths sequence is stored once as the whole cycle rather than as the several shorter tails musicians commonly write. A passage counts as realising it if it joins the cycle at any point and then runs without a break to the closing tonic.

**Why.** The same organisation reason as the rotation rule: the common short tail is a way of entering the one pattern, not a second pattern, so it is expressed as a matching rule on one entry rather than as extra records. The document states the rule where the entry is defined, so a reader cannot meet the entry without meeting what counts as realising it.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:179-181`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:179-181 (§5.2, sequences). The descending-thirds entry beside it carries the same kind of rule, stated as a continuation rule rather than an ellipsis. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-413 — Upper-structure and rootless VOICING substitution is outside the harmonic vocabulary — it is a voicing, not a function

> - **Upper-structure / voicing substitution** `[jazz]` — a *voicing* device (rootless, upper-structure triads, sus); it is
>   a voicing, not a function, so it is **outside this component** (noted only so it is not mistaken for a function-level
>   substitution).

**In plain words.** Jazz devices that change how a chord is spread across the instrument, rather than which function it fills, are not substitutions in this catalog's sense and are deliberately not held here. The exclusion is written down only so that nobody mistakes them for function-level substitutions.

**Why.** Follows from the component's stated scope: the catalog holds functions and the operations that replace one function with another, and a voicing device changes neither. The record notes the exclusion is stated defensively rather than because anything asked for it.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:220-222`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:220-222 (§5.3, the substitution operations). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-414 — The catalog is GENERATIVE where it can be and enumerated only where it must be

> - **D3 — Generative where possible, enumerated where necessary.** The secondary/substitute apparatus is parameterised by
>   target degree; only the named recurring patterns are enumerated. *Rejected:* a fully enumerated flat list (combinatorial,
>   and it hides the systematic structure).

**In plain words.** The systematic part of harmony — the applied and substitute chords that exist for every degree of the scale — is stored once as a pattern with the degree left open, and produced on demand. Only the patterns that have individual names and cannot be generated are written out one by one.

**Why.** Recorded as component decision D3 with its rejected alternative: a fully enumerated flat list was refused as combinatorial and because it hides the systematic structure that makes the applied and substitute apparatus one idea rather than dozens.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:255-257`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `cowork_progression_schema_dictionary.md`:255-257 (§7, component decision D3), with the organisation it produces at :136-139 (§5) and the generative spine at :141-166 (§5.1). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-421 — Idiom re-discovery rides every corpus wave, on research material only, and a changed cluster set is its own ratification event

>   **★ Standing trigger (user, 2026-07-02): idiom re-discovery rides each corpus wave.** After each material corpus
>   change (each wave; the yearly census re-sweep), re-run the `idiom_discovery/` pipeline under the v1 protocol
>   (multi-seed stability, cap-robustness, source-leakage/ARI confound test) on the **dev set + external research
>   corpora only** (held-out material excluded — discovery outputs become shipped parameters). Primary question:
>   do the five ratified idioms **reproduce**? Falsifiable v2 edges: does #5 Chromatic-coloristic split (the K=6
>   candidate) under the new chromatic mass; where do Wagner/Liszt land (#2 vs #5 — the era≠axis re-test); does
>   early-modal material (Monteverdi/Sweelinck) separate or fold into #4. A changed cluster set is a **ratified
>   taxonomy-revision event** (it propagates to StyleTag values + the vocabulary entry mapping — post-swap it is a
>   migration, not a relabel). Plan line only — the instruction is written just-in-time after the triggering wave.

**In plain words.** Whenever the body of music the project holds changes materially, the study that discovered the five idioms is re-run under the same protocol, to ask whether the five reproduce. It is run only on the development set and outside research corpora, never on the music held back for evaluation, because what the study produces becomes a shipped parameter. If the clusters come out different, that is a taxonomy revision and needs its own ratification — it changes the tags on every catalog entry, so after the tags were encoded it is a migration, not a relabel.

**Why.** The held-out exclusion is stated with the rule and is guiding principle #20 (fit and evaluation separated) applied to an unsupervised study: discovery outputs become shipped parameters, so material used to discover them can never also measure them. The re-run itself is the standing consequence of the finding the study rests on — that the categories are empirical rather than asserted (`cowork_style_taxonomy_proposal.md:11-30`) — which means new music can falsify them; the record names the falsifiable edges in advance (does idiom five split under new chromatic mass, where do Wagner and Liszt land, does early modal material separate), which is what makes the trigger a test rather than a formality.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:220`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** `docs/implementation_roadmap.md`:183-191, recorded as a standing trigger of the user, 2026-07-02, beside the census's own standing rule that discovering a new corpus is a census defect (register entry D-359). It governs the style taxonomy that `ARCHITECTURE.md` §6.7 owns and is recorded in a plan rather than at that home, hence the documentation-gap flag. Load-bearing for the 2026-08-03 §6.7 restatement: the five idioms are stated there as empirically discovered, and this is the rule that keeps that claim current. The record notes two corpus waves executed and ratified (2026-07-02, 2026-07-03), the second checking the trigger and finding it NOT fired. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

