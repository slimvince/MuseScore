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

**Home.** `ARCHITECTURE.md:5128`

**Provenance.** ARCHITECTURE.md:4292-4296 (§6.1); the principle it realizes is D-070 (§2.1). No date or ratifier stated.

### D-129 — Style conflicts resolve by a declared priority - explicit overrides always win

> **Conflict resolution priority:**
> 1. System defaults — lowest priority
> 2. Mixin sources — in declared order, later overrides earlier
> 3. Explicit `overrides` in the style file — highest priority, always wins

**In plain words.** When a style assembles itself from several inherited sources, the order of precedence is fixed: system defaults are weakest, inherited sources come next in the order they are declared with later ones winning, and anything the style file states explicitly wins outright.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5172`

**Provenance.** ARCHITECTURE.md:4338-4341 (§6.2). No date or ratifier stated.

### D-130 — The style loader never names a style in code

> The style loader scans the styles directory recursively and loads all valid JSON files.
> It never references specific style IDs in code — it simply loads whatever it finds.

**In plain words.** The loader reads whatever style files it finds in the styles directory. No style's name appears anywhere in the program code.

**Why.** Stated constraint, ARCHITECTURE.md:487-490 (§2.4): no comparison against a style name anywhere in the codebase - style-specific behaviour flows entirely through parameters.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5208`

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

**Home.** `ARCHITECTURE.md:5274`

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

**Home.** `ARCHITECTURE.md:5309`

**Provenance.** `ARCHITECTURE.md`:4565-4570 (§6.7). ★ NARROWED and VERBATIM RE-TAKEN 2026-08-03 (CC, phase 1k) on the user's OI-279 ruling of the same date, sub-ruling (i): DEFERRED over the **per-preset weights alone**; the CLUSTERS half is SUPERSEDED BY the five-idiom ratification of 2026-06-30 (`cowork_style_taxonomy_proposal.md:3-9`; the encoded `enum class Idiom` + `IdiomSet`). The FORMER verbatim, preserved here under #12, made no such split: "It is a **theory-based v1**; **empirically grounding** it — deriving the clusters *and* the per-style weights by clustering corpora — is committed future work (`cowork_style_clustering_plan.md`)" — whose "theory-based v1" characterization was itself false in the other direction, the five idioms being empirically discovered. The former scope was therefore undifferentiated over two halves of which one was already delivered. No date or ratifier is stated for the original deferral; the narrowing is the user's, 2026-08-03. Note: `cowork_style_clustering_plan.md` itself still presents BOTH halves as future work and carries no annotation of the delivery — rowed as `OPEN_ITEMS.md` OI-282.

### D-133 — The harmonic vocabulary is a queried reference component, not a layer of the analysis

> It is reference knowledge **queried** by the layers and by
> future tools, **not a pipeline layer**. Entries carry **provenance** (established theory), not a ground-truth-validation
> status — validation is the *consumer's* concern (verifiability contract, §2.15).

**In plain words.** The catalogue of progressions and substitutions is something the analysis stages ask questions of, not a stage they pass through. Its entries say where the theory comes from; whether that theory holds up against real music is the caller's question, not the catalogue's.

**Why.** Stated constraint, ARCHITECTURE.md:4446 - the verifiability contract (D-029): reference knowledge grounded in established theory may be carried without corpus validation, provided the consumer that puts it under load is the one that must validate it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5508`

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

**Home.** `cowork_progression_schema_dictionary.md:35-41`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. What this component is` (heading at line 21). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:41-46 records the owner ruling as D5 of `cowork_progression_schema_design.md` §6, user-ratified 2026-07-02, with the cross-referencing comment blocks at `functionprogression.h` and `harmonicvocabulary.h` and the test at `progressionrecognizer_tests.cpp`. Beside D-341, which is the grammar-completion amendment this ruling's consistency test produced. NOTE: this document uses the label 'D5' for TWO different decisions — this ownership ruling (§1) and the harmonic-scope component decision (§7, entered as D-408) — which is a collision in the document's own local labelling, not in this register. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-407 — The vocabulary supplies ranked candidates and DECIDES nothing — the threshold, the style weighting and what to do with a candidate are the consumer's

> - **Decide anything.** The matching threshold, the style weighting, and the choice of what to do with a candidate are the
>   **consumer's**; the component only supplies ranked candidates.

**In plain words.** The catalog answers questions and hands back a ranked list. How good a match has to be before it counts, how much weight a style carries, and what is done with the answer are all decided by whatever is asking, never by the catalog.

**Why.** Stated in the document as the firewall line (§6): the component holds structural content and returns ranked structural matches, while the weighting, the threshold and the decision are precision-phase work at the consumer. Adding or correcting an entry is a content change here; tuning how strongly an entry fires is a change there. This keeps the catalog free of fitted values, so it can be shared by an analysis consumer and a future composition consumer that would weight it differently.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:53-54`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. What it does, and does not do` (heading at line 48). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:52-54 (§2, what it does not do), with the firewall line at :244-246 (§6). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

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

**Home.** `cowork_progression_schema_dictionary.md:55-59`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. What it does, and does not do` (heading at line 48). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:55-59 (§2), restated as component decision D5 at :261-263 (§7) with its rejected alternative, and carried as a risk at :279-280 (§9). Consistent with `ARCHITECTURE.md` §7, which states the same exclusion. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-409 — There is no binary match or no-match — only a score on a ranked list, and the list may be EMPTY

> consumer applies its own style weighting and its own threshold; there is no binary match/no-match, only the score (as the
> inference layers carry ranked alternatives with confidence). **The list may be empty** — for *recognise* (nothing
> matches), for *suggest follow/precede* (no progression fits), and for *suggest replace* (no substitution applies) — and a
> consumer must handle an empty result, never assuming a non-empty one.

**In plain words.** A query never comes back with a yes or a no. It comes back with a ranked list of candidates, each carrying a number saying how well it fits, and the list is sometimes empty. Anything asking must cope with an empty answer and must never assume there is one.

**Why.** Stated with the rule: this is the same shape the inference layers use, which carry ranked alternatives with a confidence rather than a forced single answer (the cross-cutting contract, D-027). Requiring the consumer to handle an empty list is what stops a recogniser from inventing a match to have something to return.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:121-124`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. The query interface — what a consumer supplies, and gets back` (heading at line 84). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:114-124 (§4). Beside D-027, the cross-cutting contract that every layer emits ranked candidates plus a confidence rather than a forced point estimate. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

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

**Home.** `cowork_progression_schema_dictionary.md:102-106`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. The query interface — what a consumer supplies, and gets back` (heading at line 84). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:96-106 (§4 recognise) and :114-118 (the match score under the partial matcher). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-411 — The Axis loop is ONE entry in one canonical rotation — its other rotations become rotation-tolerant matching on that entry, never three more entries

>   variant `1̂–♭7̂–♭6̂–5̂`); Andalusian cadence `i–bVII–bVI–V`; doo-wop `I–vi–IV–V`; Axis `I–V–vi–IV` — **rotation rule (as built, verified at the catalog):** ONE entry, encoded in the canonical
>   rotation `I–V–vi–IV` only; the v1 exact matcher therefore recognises only that order, and admitting the other three
>   rotations (as rotation-tolerant matching on this one entry, never as three more entries) is a declared decision for
>   the Stage-5 partial matcher;

**In plain words.** The four-chord pop loop that can start on any of its four chords is stored once, in one chosen order. The first version therefore recognises only that order. Recognising the other three starting points is a planned change to how matching works on that single entry, and explicitly not a decision to store the loop four times.

**Why.** The reason is in the rule itself: storing a rotation as a separate entry would make one convention into four records, which is the duplication the catalog's one-entry-per-convention organisation exists to avoid (§6, one encyclopedia, not per-style silos). Recorded as verified at the catalog rather than assumed.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:185-188`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.2** — `### 5.2 Named progressions & schemas` (heading at line 168). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:185-188 (§5.2, the bass-line and pop loops). Same class as the circle-of-fifths entry-point rule (D-412): both fix what a realisation of one entry is allowed to look like. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-412 — The circle-of-fifths entry is the FULL cycle, and a realisation may enter at any member and run contiguously to the final tonic

> - **Sequences** `[common-practice + jazz]` — circle-of-fifths (the full cycle `I–IV–viio–iii–vi–ii–V–I`; the common
>   tail is its last members, `iii–vi–ii–V–I` — **entry-point rule:** the skeleton is the full cycle and a realisation
>   may enter at any member, running contiguously to the final `I`); descending-thirds (`I–vi–IV–ii`, extendable by

**In plain words.** The circle-of-fifths sequence is stored once as the whole cycle rather than as the several shorter tails musicians commonly write. A passage counts as realising it if it joins the cycle at any point and then runs without a break to the closing tonic.

**Why.** The same organisation reason as the rotation rule: the common short tail is a way of entering the one pattern, not a second pattern, so it is expressed as a matching rule on one entry rather than as extra records. The document states the rule where the entry is defined, so a reader cannot meet the entry without meeting what counts as realising it.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:179-181`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.2** — `### 5.2 Named progressions & schemas` (heading at line 168). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:179-181 (§5.2, sequences). The descending-thirds entry beside it carries the same kind of rule, stated as a continuation rule rather than an ellipsis. Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-413 — Upper-structure and rootless VOICING substitution is outside the harmonic vocabulary — it is a voicing, not a function

> - **Upper-structure / voicing substitution** `[jazz]` — a *voicing* device (rootless, upper-structure triads, sus); it is
>   a voicing, not a function, so it is **outside this component** (noted only so it is not mistaken for a function-level
>   substitution).

**In plain words.** Jazz devices that change how a chord is spread across the instrument, rather than which function it fills, are not substitutions in this catalog's sense and are deliberately not held here. The exclusion is written down only so that nobody mistakes them for function-level substitutions.

**Why.** Follows from the component's stated scope: the catalog holds functions and the operations that replace one function with another, and a voicing device changes neither. The record notes the exclusion is stated defensively rather than because anything asked for it.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:220-222`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 Substitution operations` (heading at line 200). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:220-222 (§5.3, the substitution operations). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-414 — The catalog is GENERATIVE where it can be and enumerated only where it must be

> - **D3 — Generative where possible, enumerated where necessary.** The secondary/substitute apparatus is parameterised by
>   target degree; only the named recurring patterns are enumerated. *Rejected:* a fully enumerated flat list (combinatorial,
>   and it hides the systematic structure).

**In plain words.** The systematic part of harmony — the applied and substitute chords that exist for every degree of the scale — is stored once as a pattern with the degree left open, and produced on demand. Only the patterns that have individual names and cannot be generated are written out one by one.

**Why.** Recorded as component decision D3 with its rejected alternative: a fully enumerated flat list was refused as combinatorial and because it hides the systematic structure that makes the applied and substitute apparatus one idea rather than dozens.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `cowork_progression_schema_dictionary.md:255-257`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§7** — `## 7. Component decisions (with the alternatives weighed)` (heading at line 248). A delegation at ARCHITECTURE.md:5502 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_progression_schema_dictionary.md`:255-257 (§7, component decision D3), with the organisation it produces at :136-139 (§5) and the generative spine at :141-166 (§5.1). Found by the phase-1j continuation wave, 2026-08-02, reading `cowork_progression_schema_dictionary.md` IN FULL. The document is NOT a contract home: its banner reads 'component spec, v1 draft (2026-06-29)' — a draft names no ratifier — although `ARCHITECTURE.md` §7 does point at it, so the delegation half of the fifth-home-case criterion is satisfied and the ratification half is not. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1j ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1j queue presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §2 — the ratification is of the RULE itself, with the status exactly as the record states it; it does not supply a date or a ratifier the original record never had, and the 'not stated' facts above stand unchanged (#12). The `gap` home flag also stands: the dictionary's banner still reads 'component spec, v1 draft (2026-06-29)', so the fifth home case's banner half is unmet — that is the open question rowed as `OPEN_ITEMS.md` OI-281, deliberately NOT resolved by editing this document's banner.)

### D-421 — Idiom re-discovery rides every corpus wave, on research material only, and a changed cluster set is its own ratification event

> - **Idiom re-discovery RIDES EVERY CORPUS WAVE, on research material only, and a changed cluster
>   set is its own ratification event.** After each material corpus change the discovery pipeline is
>   re-run under the protocol above, on the **development set and outside research corpora only** —
>   held-out material excluded — asking first whether the five idioms **reproduce**. **A changed
>   cluster set is a ratified taxonomy-revision event**: it propagates to the style-tag values and to
>   the vocabulary's per-entry mapping, so once those tags are encoded it is a migration and not a
>   relabel. *Why:* the held-out exclusion is #20 applied to an unsupervised study — discovery
>   outputs become shipped parameters, so material used to discover them can never also measure them.
>   The re-run itself is the standing consequence of the finding this section rests on, that the
>   categories are empirical rather than asserted, which means new music can falsify them; the record
>   names the falsifiable edges in advance — whether the chromatic-coloristic idiom splits under new
>   chromatic mass, where the high-chromaticism composers land, and whether early modal material
>   separates or folds in — and naming them in advance is what makes the trigger a test rather than a
>   formality.

**In plain words.** Whenever the body of music the project holds changes materially, the study that discovered the five idioms is re-run under the same protocol, to ask whether the five reproduce. It is run only on the development set and outside research corpora, never on the music held back for evaluation, because what the study produces becomes a shipped parameter. If the clusters come out different, that is a taxonomy revision and needs its own ratification — it changes the tags on every catalog entry, so after the tags were encoded it is a migration, not a relabel.

**Why.** The held-out exclusion is stated with the rule and is guiding principle #20 (fit and evaluation separated) applied to an unsupervised study: discovery outputs become shipped parameters, so material used to discover them can never also measure them. The re-run itself is the standing consequence of the finding the study rests on — that the categories are empirical rather than asserted (`cowork_style_taxonomy_proposal.md:11-30`) — which means new music can falsify them; the record names the falsifiable edges in advance (does idiom five split under new chromatic mass, where do Wagner and Liszt land, does early modal material separate), which is what makes the trigger a test rather than a formality.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-03 · by user

**Home.** `ARCHITECTURE.md:5379-5392`

**Provenance.** `docs/implementation_roadmap.md`:183-191, recorded as a standing trigger of the user, 2026-07-02, beside the census's own standing rule that discovering a new corpus is a census defect (register entry D-359). It governs the style taxonomy that `ARCHITECTURE.md` §6.7 owns and is recorded in a plan rather than at that home, hence the documentation-gap flag. Load-bearing for the 2026-08-03 §6.7 restatement: the five idioms are stated there as empirically discovered, and this is the rule that keeps that claim current. The record notes two corpus waves executed and ratified (2026-07-02, 2026-07-03), the second checking the trigger and finding it NOT fired. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to §6.7 under the maintained-object rule — the re-discovery protocol, and that a changed cluster set is its own ratification event — in that section's own voice and with its defense. It is the rule that keeps §6.7's own claim current, that the five idioms are empirically discovered rather than theory-derived. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/implementation_roadmap.md:259`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 1, "section": "# Consolidated Implementation Roadmap — Reviews → Plan", "label": "the opening block (above the first section heading)", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "  **★ Standing trigger (user, 2026-07-02): idiom re-discovery rides each corpus wave.** After each material corpus
  change (each wave; the yearly census re-sweep), re-run the `idiom_discovery/` pipeline under the v1 protocol
  (multi-seed stability, cap-robustness, source-leakage/ARI confound test) on the **dev set + external research
  corpora only** (held-out material excluded — discovery outputs become shipped parameters). Primary question:
  do the five ratified idioms **reproduce**? Falsifiable v2 edges: does #5 Chromatic-coloristic split (the K=6
  candidate) under the new chromatic mass; where do Wagner/Liszt land (#2 vs #5 — the era≠axis re-test); does
  early-modal material (Monteverdi/Sweelinck) separate or fold into #4. A changed cluster set is a **ratified
  taxonomy-revision event** (it propagates to StyleTag values + the vocabulary entry mapping — post-swap it is a
  migration, not a relabel). Plan line only — the instruction is written just-in-time after the triggering wave." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-496 — RATIFIED AMENDMENT A-6: whether the pairwise progression grammar lives inside the harmonic vocabulary or stays a separate store is decided at the recognition-consumer build, explicitly

> - **Whether the pairwise progression grammar folds INTO this vocabulary or stays a SECOND store is
>   a decision that is OWED, and its trigger is the recognition-consumer build.** Knowledge about
>   which chord may follow which is currently held in two places — a pairwise rule set inside the
>   function layer, and this catalog of longer patterns. The choice between one store and two by
>   declared design **is not to be settled by drift**: it is made, explicitly, when the component
>   that queries this catalog is built. *Why:* the consumer design already asserts that this
>   vocabulary extends the pairwise grammar while the single-store-or-two decision is unmade, which
>   is a total-unification question (#6) and exactly the kind of coexistence the review's own
>   criterion says must be **decided** rather than tolerated. Stating the trigger rather than the
>   answer is the point: no section can yet state a rule here, and what is owed is the choice.

**In plain words.** Knowledge about which chord may follow which is held in two places: a pairwise rule set inside the function layer, and a catalog of longer patterns. Whether these become one store or stay two is not to be settled by drift — the amendment requires the choice to be made, and made when the component that queries the catalog is built.

**Why.** Stated with the finding it comes from: the consumer design asserts that the vocabulary extends the pairwise grammar, but the single-store-or-two decision is unmade — which is a total-unification (#6) question and is exactly the kind of coexistence the review's own criterion says must be decided rather than tolerated.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5531-5540`

**Provenance.** Amendment A-6 of the external architecture review, in a document whose banner records amendments A-1…A-10 as RATIFIED by the user on 2026-07-02. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it. Related but distinct: **D-133** rules that the vocabulary is a queried reference component rather than a layer, and **D-419** that the function layer does not touch it until the consumer is built; neither answers which store owns the pairwise motions. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded reason was that the amendment DEFERS the decision, so no section can yet state it as a rule. The user ruled the D-419 SHAPE: a deferred decision is stated at §7 WITH ITS TRIGGER — the recognition-consumer build — so what the specification carries is that a choice is owed and when it is made. Written into §7 beside D-419, in that section's own voice and with its defense. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_architecture_review_2026_07.md:326-327`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 307, "section": "## 9. Proposed amendments (ranked; each ratification-gated; none is code)", "label": "§9", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **A-6 (from F-6). Decide the progression-knowledge store question** at the recognition-consumer build (fold §5.0
  pairwise motions into the Vocabulary, or two stores by declared design)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-502 — The span a recognised named progression covers is called the progression-schema-span — the bare word 'sequence' is reserved for the harmonic sequence and 'progression' for the whole committed chord stream

> - **D6 — what to NAME the span a recognised progression covers — RESOLVED BY PREFIXING (user direction, 2026-07-02):
>   `progression-schema-span`.** The prefix answers the last collision standing: bare "schema" reads as *data* schema
>   to any coder, while **"progression schema" is already this component family's own name** (this design and the

**In plain words.** The stretch of music covered by a recognised named progression needed a name. It is called the progression-schema-span. The two shorter names were rejected because each already means something else here: a *sequence* is a progression repeated at rising or falling transpositions, and *the progression* is the entire analysed chord stream.

**Why.** Stated with the ruling and decided against the alternatives in the same block: 'sequence-span' collides permanently with the music-theory sense the same document uses correctly, and 'progression-span' reads as 'any span of the committed progression', which every span is — so neither name says the one thing it must, a RECOGNISED NAMED progression. The prefix resolves it because 'progression schema' is already this component family's own name.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:245-247`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 186). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** One of the ratification asks the document's banner records as settled in full. It is the span typology's latent 'sequence-span' finally instantiated, and it carries a propagation rider to `ARCHITECTURE.md` §2.15's latent list and the Layer-6 specification. Directly adjacent to `OPEN_ITEMS.md` OI-318, which records that the Layer-6 section of `ARCHITECTURE.md` still uses a reserved word for a different span. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-503 — The idiom mixture is DISCOVERED from the score and merely SEEDED by the user's preset, in three forward-only phases

> The consumer holds a weight vector `w` with one weight per idiom. **`w` is DISCOVERED from the score, seeded by the
> user's preference (user-ratified model, 2026-07-02), in three phases — forward-only, no loop:**

**In plain words.** How much weight each harmonic idiom carries is worked out from the music itself. The user's chosen preset only supplies the starting point, and the estimate moves away from it as recognised evidence accumulates. It runs in three passes that only ever feed forward, so nothing loops.

**Why.** The loop-freedom is argued at the mechanism rather than asserted: the recognition pass does not depend on the weights at all in this version, so the weight estimate is computed from recognition output only and never from its own downstream use. The document also records what happens when partial matching arrives and that dependence appears — estimation stays on the exact-match subset — so the property is preserved by a declared resolution rather than by luck.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:135-136`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.5** — `### 4.5 The idiom-mixture weighting (structure and directions fixed here; every value Stage-5)` (heading at line 134). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Ratification ask §4.5, recorded APPROVED in the banner in the user's own words. The prior strength of one recognition is the match score times the MAXIMUM of the idiom weights over the entry's idiom set — the maximum and not the sum, so that an entry tagged with several idioms is not thereby advantaged. Distinct from **D-293** (values are fitted per idiom, never per preset), which governs fitting; this governs a per-score estimate made at recognition time. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-504 — A recognised harmonic sequence is ALWAYS emitted as key evidence — the earlier gate that emitted it only where no cadence existed threw corroboration away

> ### 4.6 Harmonic sequences as evidence of the local key (the Layer-5 §5.3 channel; review A-4)
> A recognised harmonic sequence implies **motion of the local key** (the tonality — see the §0 "key" row). The consumer exposes each as a typed output
> `{progression, transposition step, span, number of repetitions, prior strength}`. **U1 ruling (2026-07-02): a sequence requires ≥2 transposed statements of the SAME recognised entry** — that is
> what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the
> evidence weight scales with it (more repetitions → stronger; direction fixed, values Stage-5). A **single**
> recognition of an internally-sequential entry (circle-of-fifths, Monte, Fonte) emits **no** §4.6 sequence — its
> key-motion implication is already carried by its schema-span (the entry's internal transposition structure is
> catalog knowledge, readable by the F-C consumer when that wiring is designed; recorded in §9 so it is decided
> there, not lost). **The consumer ALWAYS emits it —
> evidence is never discarded** (the no-information-loss and use-every-clue principles; user-directed correction
> 2026-07-02, replacing an earlier "only where no cadence exists" gate that threw corroboration away). Layer 5 §5.3
> uses it in two roles: **(i) corroboration, always** — sequence evidence agreeing with a confirming cadence raises
> the candidate key's vote, disagreeing tempers it; **(ii) the substitute confirming channel** for condition (a)
> **only where no authentic cadence confirms the candidate key**, at a weight **below** the cadence channel's
> (ordering fixed; values Stage-5) — the cadence remains the stronger confirmation wherever it exists, by weight, not
> by suppressing the other evidence. **Frame obligation:** comparing sequence evidence against the home-key
> confidence is a NEW comparison; it must be declared in the confidence contract §4 (frame **F-C**) **before** the
> §5.3 wiring is built. The consumer's own build (the annotation + the §5.5 feature) does not need it.

**In plain words.** When the same progression is recognised at successive transpositions, that is evidence about where the tonality is going. It is now always published. It corroborates a cadence that agrees with it and tempers one that disagrees, and it stands in as the confirming channel only where no authentic cadence confirms the candidate tonality — always at a weight below the cadence's.

**Why.** The user's own correction, stated with the rule: the replaced gate emitted the evidence only where no cadence existed, which discarded the corroborating case entirely — against the no-information-loss and use-every-clue principles. The cadence keeps its precedence BY WEIGHT rather than by suppressing the other evidence, which is what lets both be used at once.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:161-178`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.5** — `### 4.5 The idiom-mixture weighting (structure and directions fixed here; every value Stage-5)` (heading at line 134). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Ratification ask §4.6, recorded settled in the banner as 'always-emit corroboration + substitute channel'. It carries a FRAME OBLIGATION that is part of the decision: comparing sequence evidence against the home-key confidence is a new comparison and must be declared in the confidence contract §4 as frame F-C BEFORE the wiring is built — the consumer's own build does not need it. See **D-269** (the frame table is the one home of the override arithmetic). Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-505 — A harmonic sequence requires at least two transposed statements of the SAME recognised entry; a single internally-sequential entry emits none

> A recognised harmonic sequence implies **motion of the local key** (the tonality — see the §0 "key" row). The consumer exposes each as a typed output
> `{progression, transposition step, span, number of repetitions, prior strength}`. **U1 ruling (2026-07-02): a sequence requires ≥2 transposed statements of the SAME recognised entry** — that is
> what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the
> evidence weight scales with it (more repetitions → stronger; direction fixed, values Stage-5). A **single**
> recognition of an internally-sequential entry (circle-of-fifths, Monte, Fonte) emits **no** §4.6 sequence — its

**In plain words.** A recognised progression that is itself built out of transpositions — a circle of fifths, a Monte, a Fonte — does not by itself count as a sequence. Two or more transposed statements of the same catalog entry do. A single internally-sequential recognition publishes its own span instead, and its transposition structure stays where it belongs, in the catalog.

**Why.** Derived from the definition rather than chosen: the document's own terms table defines a harmonic sequence as the same progression repeated at successive transpositions, so counting one internally-sequential entry as a sequence would contradict the definition the same document gives. The evidence weight grows with the number of matched windows, which is why the count has to mean something.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:162-166`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.6** — `### 4.6 Harmonic sequences as evidence of the local key (the Layer-5 §5.3 channel; review A-4)` (heading at line 161). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The U1 ruling, taken with the §4.6 settlement. It also records where the un-emitted implication goes rather than dropping it — the entry's internal transposition structure is catalog knowledge readable by the F-C consumer when that wiring is designed — which is #12 applied to a decision not to emit. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-506 — Progression recognition is ADDITIVE: the literal Roman numeral is never rewritten, and a substitution is recorded only in the annotation

> - **D4 — Additive; the literal Roman numeral is never changed.** *Alternatives weighed and rejected:* rewriting the numeral to the
>   substituted-for function — it loses the literal label the ground truth scores.

**In plain words.** When the recogniser sees that a chord is standing in for another — a tritone substitute doing a dominant's job — it says so in the annotation and leaves the Roman numeral exactly as the analysis committed it.

**Why.** Stated with the decision and weighed against its alternative: rewriting the numeral to the substituted-for function loses the literal label the ground truth scores against, so the recogniser would improve its own story at the cost of the measurement.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:193-194`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 186). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Decision D4 of the design's architecture-decision list, inside the document the banner records as fully ratified. It is the recognition consumer's instance of the standing additive discipline; the catalog side of the same seam is **D-406**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-507 — A catalog entry defined by its melodic or bass lines is recognised by its chord skeleton alone and carries a 'chords-only' mark, with its prior strength reduced

> - **D7 — line-defined entries carry the "chords-only" mark** (§4.5) — the verifiability contract's explicit-mark
>   path; the mark retires per entry when the voice-leading layer supplies the other half.

**In plain words.** Some named patterns are defined by their melody and bass lines as much as by their chords. This consumer can only see the chords, so it recognises such a pattern by its chord skeleton, marks the recognition as chords-only, and trusts it less. The mark comes off, per entry, when the voice-leading work supplies the other half.

**Why.** Stated with the decision: an entry defined by its lines is under-identified by its chords alone, so the reduced weight states a real limit rather than a preference. The mark is the verifiability contract's explicit-mark path, which is what makes the limit visible to a consumer instead of silently absorbed.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:272-273`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 186). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Decision D7 of the same ratified list. The vocabulary side of the same boundary is **D-408** (voice-leading is a different dimension and is not held in the harmonic vocabulary). Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-508 — The catalog/grammar consistency test ships scoped to the MEASURED containment — an explicit known-gap list — and tightens to a clean assertion when the grammar amendment lands

>   silently un-license legitimate grammar). The **consistency test** ships scoped to the TRUE containment: every
>   pair is licensed OR on the explicit 6-entry known-gap list (any 7th failure = red); when the grammar amendment
>   lands, the list empties and the test tightens to the clean assert.

**In plain words.** The premise that every adjacent chord pair inside every catalog entry is licensed by the analysis's own grammar was checked and turned out to be false: a handful of entries exercise musically correct motions the grammar did not license. The test therefore ships allowing exactly those, and any further failure is an error. When the grammar is completed the allowance list empties and the test becomes the plain assertion it was meant to be.

**Why.** The scoping is forced by a measurement that falsified the premise on first contact, and the document records the diagnosis rather than the count alone: what is narrow is the licensed set, which descends from the old scoring-bonus signals rather than from a complete functional grammar. Deriving the grammar FROM the catalog stays rejected for the stated reason — the catalog is enumerative and incomplete while the grammar is generative, so a missing entry would silently un-license legitimate motion.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:242-244`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 186). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The measured correction of Cowork's own premise, recorded inside the ratified document with the earlier arithmetic error owned in the same sentence. The grammar completion it waits on is **D-341**, ratified by the user 2026-07-03 and recorded as in force in the specification and not yet in code. The one-owner ruling this test is the sole coupling of is **D-406**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-509 — Where the analysis already committed a chord, a recognised progression corrects it through the EXISTING override frame and may only SELECT an already-carried reading — no new comparison frame, and never a reading built from the notes

> - **Where Layer 4 committed:** if an admitted recognised progression's member position demands a **different root
>   or quality** than the committed reading, the recognition's prior strength enters the **same contradiction
>   quantity frame F-B already compares** (the functional-plausibility difference), and the committed reading is
>   overridden **if and only if** that quantity exceeds the §8 threshold scaled to the committed reading's composite
>   confidence — the same threshold rule, the same tie-holds-the-incumbent rule, and the same
>   overridden-at-most-once-per-pass rule as every other F-B firing (§0). The correction **selects** an existing
>   reading (a ranked candidate, or the recognised member's realisation where it is one) — never a reading built from
>   the notes. No new comparison frame is introduced.

**In plain words.** If a recognised progression demands a different chord than the one already committed, the recogniser does not invent a chord from the notes. It puts its evidence into the comparison the correction mechanism already makes, under the same threshold, the same tie rule and the same once-per-pass rule, and it can only pick a reading that was already on the table.

**Why.** Stated with the rule and grounded in the architecture it rides: reusing the existing frame is what keeps the recogniser from introducing a second correction mechanism, and restricting it to selection is what keeps it from becoming a second chord identifier. Both are the one-path-per-concern discipline applied to a consumer rather than to a layer.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_progression_schema_design.md:121-128`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.3** — `### 4.3 The evidence contribution (both conditions fully stated)` (heading at line 117). A delegation at ARCHITECTURE.md:512 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The second half of §4.3, inside the fully-ratified document. The frame it rides is F-B, whose measured behaviour is now **D-490**/**D-491**/**D-492** — a reader of this decision should read those beside it, because the mechanism this consumer was designed to ride is the one measured net-harmful and recommended for demotion. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-542 — Idiom discovery runs DISCOVER-THEN-NAME: structure is learned on a low-level encoding carrying no theory or genre labels, and theory features and genre labels are interpretation lenses applied afterwards, never clustering input

> - **The governing order is DISCOVER, THEN NAME.** Structure is learned on a **low-level encoding
>   carrying no theory and no genre labels**; only afterwards is the emergent structure held up
>   against theory features **and** genre labels, both as **interpretation lenses, never as
>   clustering input**. *Why:* stated as a refusal rather than a preference — there is no
>   zero-prejudice method, so the discipline is to push the unavoidable priors down to the lowest,
>   most theory-neutral level and interpret afterwards, never to pretend they are absent. Feeding
>   theory features in could only rediscover the priors already encoded, which is the alternative the
>   design rejects by name.

**In plain words.** The grouping of music into harmonic idioms is learned from a plain, label-free encoding of the notes and chords. Only afterwards is the result held up against theory terms and against genre labels to see what the emergent groups correspond to. Neither is ever fed in.

**Why.** The governing reason is stated as a refusal rather than a preference: there is no zero-prejudice method, so the discipline is to push the unavoidable priors to the lowest, most theory-neutral level and interpret afterwards — never to pretend they are absent. Feeding theory features in could only rediscover the priors already encoded, which is the alternative the decision list rejects by name.

**Status.** NOT STATED · decided 2026-06-30 · ratifier not stated

**Home.** `ARCHITECTURE.md:5333-5340`

**Provenance.** The core principle of the idiom-discovery design, which the document's own banner marks a research/analysis component and not a runtime layer. Its output feeds the style tags and weights of the harmonic vocabulary and ultimately the presets. The standing rule that idiom re-discovery rides every corpus wave on research material only is **D-421**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that §6.7 owns the taxonomy but not the method that discovers it. The user ruled THE MAINTAINED-OBJECT RULE: a maintained object and its maintenance or discovery method belong together, so §6.7 owns BOTH the canonical style taxonomy and the protocols and method that produce and re-produce it. Written into §6.7 in that section's own voice, with its defense and with the rejected alternative the record names. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_design.md:28-30`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 23, "section": "## 2. The core principle — minimal prejudice, not zero", "label": "§2", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The governing order is **discover → then name**: learn structure on a low-level encoding carrying **no** theory or
genre labels; only afterward hold the emergent structure up against theory features **and** genre labels, both as
**interpretation lenses, never as clustering input**." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-543 — The encoding is key-normalised tonal-pitch-class TRANSITIONS — spelled where spelling is reliable, mod-12 only where it is genuinely absent — run as two complementary views

> - **The encoding is KEY-NORMALIZED TONAL-PITCH-CLASS TRANSITIONS — spelled where spelling is
>   reliable, plain pitch classes only where no spelling exists — run as TWO complementary views.**
>   Every piece is transposed to a common tonic and encoded as chord-to-chord moves, using the
>   written note names wherever the source spells them (classical scores and trusted lead-sheet
>   symbols); a second, order-free vocabulary view of the same material runs alongside as a
>   cross-check. *Why:* grounded in the prior art the design adopts — the line-of-fifths encoding is
>   what made the published topics interpretable, and it stays low-prejudice because it is the raw
>   written note rather than a functional label. Three alternatives are rejected with their reasons:
>   high-level functional features prejudge the answer; audio or raw performance data lets timbre and
>   instrumentation swamp harmony; bare pitch classes everywhere discard the very structure that made
>   the published result readable.

**In plain words.** Pieces are encoded as sequences of chord-to-chord moves with every piece transposed to a common tonic, using the written note names wherever the source spells them. Where no spelling exists at all, plain pitch classes are used. A second, order-free view of the same material runs alongside as a cross-check.

**Why.** Grounded in the prior art the design adopts: the line-of-fifths encoding is what made the published topics interpretable, and it stays low-prejudice because it is the raw written note rather than a functional label. Three alternatives are rejected with reasons — high-level functional features prejudge the answer, audio or raw performance data lets timbre and instrumentation swamp harmony (the lesson of one of the cited studies), and bare pitch classes everywhere discard the very structure that made the published result readable.

**Status.** NOT STATED · decided 2026-06-30 · ratifier not stated

**Home.** `ARCHITECTURE.md:5341-5351`

**Provenance.** Decision D2 of the design, with the lead-sheet trust ruling folded in — chord symbols on lead sheets are trusted for the features clustered on. The transition view is deliberately the axis the closest published precedent discards, which is the document's own answer to why the study is re-run rather than cited. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to §6.7 under the maintained-object rule, beside D-542, in that section's own voice, with its defense and with the three rejected alternatives the record names. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_design.md:158-162`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 155, "section": "## 9. Decisions (with alternatives weighed)", "label": "§9", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **D2 — minimal low-level encoding: key-normalized tonal-pitch-class transitions** (line-of-fifths where spelling is
  reliable — classical scores + trusted lead-sheet symbols — else mod-12), run as two views (progression + vocabulary,
  §3). *Rejected:* high-level functional features (prejudges the answer); raw audio/MIDI (timbre/instrumentation/
  performance confounds swamp harmony — Mauch's lesson); bare mod-12 pitch classes everywhere (discards the
  line-of-fifths structure that made Moss's topics interpretable)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-544 — Confound control is a FIRST-CLASS GATE, and the source-leakage test decides validity: if the clusters are explained by which corpus a piece came from, the result is bookkeeping and not idiom

> - **Confound control is a FIRST-CLASS VALIDITY GATE, and the source-leakage test decides
>   validity.** The dominant failure mode of this kind of study is discovering **which corpus a piece
>   came from**, what key it is in, how long it is, its instrumentation or its encoding quirks —
>   before it ever reaches idiom. So the controls are mandatory and matched to it one by one:
>   key-normalize, length-normalize, balance and stratify sources, de-duplicate, exclude melody-only
>   sources, audit extraction noise on a labelled subset. **The source-leakage test is mandatory:**
>   hold out the source label and test whether the clusters are explained by source, key or length.
>   **If the clusters approximate the source, the study found bookkeeping and not idiom** — back to
>   the encoding. A discovered structure earns the word *idiom* only after surviving these. *Why:*
>   stated as a gate rather than a footnote precisely because the alternative — naive clustering —
>   finds bookkeeping and calls it style; it is #19 in the discovery setting, where a cluster set is
>   trusted after being positively established against the confound and never because nothing has
>   contradicted it.

**In plain words.** The dominant way this kind of study fails is by discovering which collection a piece came from, or what key it is in, or how long it is, and calling that a style. So the source label is held out and the clusters are tested against it. If they are explained by it, the encoding goes back to the drawing board. A discovered structure earns the word idiom only after surviving this.

**Why.** The failure mode is named concretely and the controls are matched to it one by one — key-normalise, length-normalise, balance and stratify sources, de-duplicate, exclude melody-only material, and audit the extraction noise on a labelled subset. Stating it as a gate rather than a footnote is the point: the alternative rejected by name is naive clustering, which finds bookkeeping and calls it style.

**Status.** NOT STATED · decided 2026-06-30 · ratifier not stated

**Home.** `ARCHITECTURE.md:5352-5364`

**Provenance.** Decision D4 of the design, and the criterion its §5 exists to enforce. It is #19 in the discovery setting: a cluster set is trusted after being positively established against the confound, never because nothing has yet contradicted it. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to §6.7 under the maintained-object rule — confound control as a first-class validity gate — in that section's own voice and with its defense, the mandatory source-leakage test stated with the verdict it forces. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_design.md:119-126`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 118, "section": "## 5. Confound control (the part that actually decides validity)", "label": "§5", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The dominant failure mode: naive clustering discovers **which corpus a piece came from, what key it is in, how long it
is, instrumentation, or encoding quirks** *before* it ever reaches "idiom." So this is a first-class gate, not a
footnote:
- **key-normalize** (§3); **length-normalize** (rate features, fixed-length windows); **balance/stratify** sources;
  **de-duplicate**; **exclude** melody-only sources; **audit** chordify extraction noise on a labeled subset.
- **The source-leakage test (mandatory):** hold out the **source label** and test whether the clusters are explained
  by source/key/length. **If clusters ≈ source, we found bookkeeping, not idiom** — back to the encoding.
A discovered structure earns the word "idiom" only **after** it survives these." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-545 — The uniform mechanical extractor for idiom discovery is the external library, stopping at the note-and-slice front — OUR OWN key/chord/function inference must NEVER touch the extraction

> - **The uniform mechanical extractor is the EXTERNAL library, and extraction stops at the
>   note-and-slice front: OUR OWN key/chord/function inference never touches it.** One external tool
>   (music21) is applied identically to every source, and only as far as reading notes and cutting
>   them into simultaneities; our own analyzer is deliberately not used for the extraction, and its
>   trust is **banked rather than assumed** — a shared subset is run through both and the streams
>   compared. *Why:* chosen against our own cleaner slicer for a stated reason that is the study's
>   own validity — our slicer cannot ingest every corpus format, so using it would force a **mix** of
>   extractors correlated with source, which is exactly the confound the gate above forbids. Using
>   the full analyzer would be worse: it is tuned on one repertoire, it would rediscover our own
>   priors, and it would inject genre-correlated error into a study about whether the grouping is
>   genre. The distinction the rule rests on is stated with it — reading notes and slicing them is
>   mechanical, so an error there is a bug rather than a misinference, while everything above is
>   inference and would carry our priors. *Mechanical* means unbiased, not clean: the raw
>   simultaneities still contain passing tones, which is correct output.

**In plain words.** Turning every corpus into chords for this study is done by one external library applied identically to every source, and only as far as reading notes and cutting them into simultaneities. Our own analyzer is deliberately not used for it.

**Why.** Chosen against our own cleaner slicer for a stated reason, and the reason is the study's own validity: our slicer cannot ingest every corpus format, so using it would force a MIX of extractors correlated with source — precisely the confound the gate forbids. Using the full analyzer would be worse: it is tuned on one repertoire, would rediscover our own priors, and would inject genre-correlated error into a study about whether the grouping is genre. The trust is banked rather than assumed — a shared subset is run through both and the verticality streams compared.

**Status.** NOT STATED · decided 2026-06-30 · ratifier not stated

**Home.** `ARCHITECTURE.md:5365-5378`

**Provenance.** Decision D6 of the design, resolving one of its open items. The distinction it rests on is stated with it: reading notes and slicing them is mechanical, so an error there is a bug rather than a misinference, while everything above is inference and would carry our priors. It is also careful to say that mechanical means unbiased and not clean — the raw simultaneities still contain passing tones, which is correct output. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to §6.7 under the maintained-object rule — the external extractor and the prohibition on our own inference touching it — in that section's own voice, with its defense, both rejected alternatives, and the mechanical-means-unbiased-not-clean qualification the record states. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_design.md:168-173`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 155, "section": "## 9. Decisions (with alternatives weighed)", "label": "§9", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **D6 — music21 as the uniform mechanical extractor; extraction stops at the L1/L2 (mechanical) front; our L3+
  analyzer never used.** *Rejected:* our own L1/L2 as the extractor (cleaner change-point slicing, and it's our audited
  code — but it can't ingest ABC/kern, so it would force a *mix* of extractors correlated with source, a §5 confound);
  our full analyzer for extraction (Baroque-tuned bias that correlates with genre — the worst confound for a
  genre-vs-not study). music21 is chosen for **uniform** format coverage, **cross-validated** against our L1/L2 on a
  shared MusicXML subset to bank the trust." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-554 — The voice-leading axis's independence from the harmonic axis is MEASURED, not assumed — cross-agreement between the two clusterings is at the level of statistical independence

> - **The voice-leading axis's independence from the harmonic axis is MEASURED, not assumed.** On the
>   pieces carrying both views the two groupings agree at the level of statistical independence — the
>   joint table is close to the product of its margins — with the harmonic groupings barely tracking
>   texture while the voice-leading groupings do. The full style structure is therefore at least
>   two-dimensional: harmonic idiom and voice-leading idiom, with the two cross-attributes beside
>   them. *Why:* the decision that the voice-leading axis is separate is recorded elsewhere; this is
>   the evidence for it — a formal independence test at full note-level coverage rather than a pilot's
>   impression — and the confound gate below is measured beside it, so the grouping is not an artifact
>   of how many voices a piece carries or which collection it came from.

**In plain words.** That how the voices move is a genuinely separate question from what the chords are is not an assumption. On the pieces carrying both views the two groupings agree at essentially chance level, and the joint table is close to the product of its margins — the harmonic groupings barely track texture while the voice-leading groupings do. So the style structure has at least two independent dimensions.

**Why.** Measured, and the measurement is the point: **D-085** records the DECISION that the voice-leading axis is separate, and this is the evidence for it — a formal orthogonality test at full note-level coverage rather than the pilot's impression. The confound gate is measured beside it, so the grouping is not an artifact of how many voices a piece has or which collection it came from.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5410-5418`

**Provenance.** `cowork_idiom_discovery_findings.md`, the v1–v2.0 empirical record of the idiom-discovery pipeline; the v2.0 axis-2 study is marked ratified in the document's own heading (CC, 2026-07-03). Read in full by READ WAVE 4, 2026-08-04. The measured values are the document's own and are not restated in this entry (**D-431**). It is the DEFENSE of **D-085**, whose own home records the decision. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed under the maintained-object rule to `ARCHITECTURE.md` §6.7, the section that owns the canonical style taxonomy and already states that the idioms are empirically discovered, in that section's own voice and with its defense. NO MEASURED VALUE WAS CARRIED ACROSS (D-431): the finding is stated qualitatively and the numbers stay in the study's own record. FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_findings.md:212-215`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 190, "section": "## v2.0 — the AXIS-2 STUDY: VL idioms discovered + orthogonality formally measured (CC, 2026-07-03; ratified)", "label": "“v2.0”", "delegated": null, "delegation": "ARCHITECTURE.md:4734", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **★ ORTHOGONALITY FORMALLY CONFIRMED: cross-ARI(VL, harmonic) = 0.030** on the 1,283 pieces carrying both views —
  statistical independence; the contingency table ≈ product of marginals. Harmonic clusters are ~texture-invariant
  (0.024) while VL tracks texture — two independent partitions of the same music. **The full style structure is
  ≥ 2-D: (harmonic idiom) ⟂ (voice-leading idiom) + mode + chromaticism.**" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-555 — The voice-leading layer's feature set is MOTION-TYPE-led, with the interval profile a secondary descriptor, and its coverage is notated music only

> - **The voice-leading layer's feature set is MOTION-TYPE-LED, the interval profile is a secondary
>   descriptor, and its coverage is notated music only.** What discriminates one way of writing voices
>   from another is how the voices move together — parallel, similar, contrary, oblique — with the
>   size-of-leap profile kept as a secondary description of melodic complexity, over a texture
>   taxonomy of contrapuntal, homophonic-classical, homophonic-pianistic and mixed. The axis applies
>   only to music notated in voices: a lead sheet has none to compare. *Why:* measured by ablation —
>   the motion-type view alone recovers texture far better than the leap-profile view alone, and
>   combining them raw lets the larger leap feature set outvote the smaller motion-type one. The
>   caveat is honored in the same place: the leap view's era signal is partly an encoding artifact, so
>   the primary finding rests on the view that carries no such artifact.

**In plain words.** What discriminates one way of writing voices from another is how the voices move together — parallel, similar, contrary, oblique — not how far each one leaps. The size-of-leap profile stays as a secondary description of melodic complexity. The axis applies only to music notated in voices: a lead sheet has no voices to compare.

**Why.** Measured by ablation, reported with the finding: the motion-type view alone recovers texture far better than the interval view alone, and combining them raw lets the larger interval feature set outvote the smaller motion-type one. The caveat is honored in the same place — the interval view's era signal is partly an encoding artifact, and the primary finding is rested on the view that has no such artifact.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5419-5428`

**Provenance.** `cowork_idiom_discovery_findings.md`, the v1–v2.0 empirical record of the idiom-discovery pipeline; the v2.0 axis-2 study is marked ratified in the document's own heading (CC, 2026-07-03). Read in full by READ WAVE 4, 2026-08-04. Recorded as the stated *footing for the voice-leading layer spec*. The measured values are the document's own (**D-431**). ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed under the maintained-object rule to `ARCHITECTURE.md` §6.7, in that section's own voice and with the ablation that decided it. NO MEASURED VALUE WAS CARRIED ACROSS (D-431). FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_findings.md:221-224`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 190, "section": "## v2.0 — the AXIS-2 STUDY: VL idioms discovered + orthogonality formally measured (CC, 2026-07-03; ratified)", "label": "“v2.0”", "delegated": null, "delegation": "ARCHITECTURE.md:4734", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Footing for the voice-leading layer spec:** a **motion-type-led** feature set (parallel/similar/contrary/oblique)
  as the primary discriminator, the interval profile as a secondary melodic-complexity descriptor, and a texture
  taxonomy of **{contrapuntal, homophonic-classical, homophonic-pianistic, moderate/mixed}**; coverage is
  notated-music only (lead sheets have no voices). Levers recorded for their proper layers (not coded): a" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-556 — Texture and era are declared per-source interpretation lenses, applied after the fact and never given to the clustering as input

> - **The texture and era covariates are declared PER SOURCE and read only after the grouping exists.**
>   This is the discover-then-name bullet above applied to the second axis, and it is not restated
>   (#6): what is added is that the lens labels are attached per source in advance, and that the
>   confound gate was run against voice count and against source and the grouping tracks neither.
>   *Why:* it is what makes the covariate agreement a finding rather than a tautology — a grouping
>   that had been given the texture label would of course recover it.

**In plain words.** The labels used to describe what a discovered grouping turned out to mean — the kind of texture, the historical period — are attached to each source in advance and read only after the grouping exists. They are never fed to the algorithm that forms the groupings.

**Why.** It is what makes the covariate agreement a finding rather than a tautology: a grouping that had been given the texture label would of course recover it. The confound gate reported in the same bullet is the other half — the grouping is measured against voice count and against source, and tracks neither.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5429-5434`

**Provenance.** `cowork_idiom_discovery_findings.md`, the v1–v2.0 empirical record of the idiom-discovery pipeline; the v2.0 axis-2 study is marked ratified in the document's own heading (CC, 2026-07-03). Read in full by READ WAVE 4, 2026-08-04. The record calls this the specification's own §6 discipline and states it was verified at the lens maps. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed under the maintained-object rule to `ARCHITECTURE.md` §6.7. ★ THE HOMING IS DELIBERATELY PARTIAL, TO AVOID A SECOND COPY (#6): the never-clustering-input half is ALREADY stated in that section's discover-then-name bullet, which the 2026-08-07 wave homed there, so the new text POINTS at it and adds only what no other home carries — that the lens labels are declared per source in advance, and that the confound gate was run against voice count and against source. NO MEASURED VALUE WAS CARRIED ACROSS (D-431). FORMER HOME, PRESERVED (#12): `cowork_idiom_discovery_findings.md:198-201`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 190, "section": "## v2.0 — the AXIS-2 STUDY: VL idioms discovered + orthogonality formally measured (CC, 2026-07-03; ratified)", "label": "“v2.0”", "delegated": null, "delegation": "ARCHITECTURE.md:4734", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **★ VL organizes by TEXTURE, not corpus or instrumentation.** Confound gate: VL-cluster ARI vs voice-count
  **0.034–0.046** (the instrumentation worry — decisively absent) and vs source **0.07–0.11** (not bookkeeping);
  vs **texture 0.32** (View B's top covariate). The texture/era covariates are declared per-source interpretation
  lenses, post-hoc only, never clustering input (spec §6 discipline — Cowork-verified at the lens maps)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

