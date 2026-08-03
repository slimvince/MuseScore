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

