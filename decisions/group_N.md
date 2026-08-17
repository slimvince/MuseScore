# Decisions group N — Generation, constraints, visualization, and the LLM integration

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-440 — The language-model integration is purpose-built and does not wait for the plugin-API reform

> **Purpose-built, not part of the plugin API reform.** The LLM integration is
> a focused module (`src/llm/`, to be created) that taps the existing
> `INotationInteraction` and DOM layers directly. It does not wait for the general
> plugin API redesign.

**In plain words.** The language-model bridge is built as its own focused module against the interfaces that already exist, rather than waiting for the general plugin API to be redesigned. The two are separate projects on separate timetables and may converge later.

**Why.** Stated with the decision in the design document read in full this wave (`docs/llm_integration.md` §3.1): the general plugin API needs a complete redesign, that reform is a large long-term project requiring community buy-in, and the language-model integration has a narrower scope that a purpose-built internal interface can serve now. Note that this does not contradict D-143 — the bridge is confined to the core access layer precisely so it CAN become a plugin later.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:8113-8116`

**Provenance.** Recorded in ARCHITECTURE.md §19.2, whose own section banner marks the whole LLM integration as design-phase; the design document it summarises (`docs/llm_integration.md`) carries the banner "Design phase. No code written yet." and `src/llm/` does not exist at HEAD (checked this wave). Entered by the phase-1 reads wave 1 from the full read of `docs/llm_integration.md`; the record names no ratifier and no date, and none is inferred. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-441 — Analysis and modification are phases of ONE conversation; a follow-up instruction re-uses the reasoning rather than re-analysing

> **Conversational continuity.** Analysis and modification occur in one
> conversation thread. When the LLM identifies problems in a QA query, "make
> the fixes you suggested" executes without re-analysis — the LLM reasons from
> its own conversation history.

**In plain words.** Asking about the music and then changing it happen in a single conversation. When the model has already worked out what is wrong, an instruction to fix it is carried out from what it already reasoned through, not by analysing the music again.

**Why.** Stated with the decision in `docs/llm_integration.md` §3.6, read in full this wave: the conversation history IS the working context, which is what makes a question-then-fix exchange cheap, and it is the same model that makes a coding assistant effective.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:8135-8138`

**Provenance.** Recorded in ARCHITECTURE.md §19.2 alongside the other language-model decisions, all of which the register already carries as deferred (D-139…D-143). Entered by the phase-1 reads wave 1; the record names no ratifier and no date. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-442 — A validation failure goes back to the language model as a tool-call error and is never shown to the user

> Violations are fed back to the LLM as tool call errors, not shown to the user.
> The LLM corrects and retries. Only clean output reaches the score.

**In plain words.** When the checks reject something the model proposed — a note outside an instrument's range, parallel fifths, a malformed bar — the rejection is returned to the model, which corrects itself and tries again. The user never sees the rejected attempt; only output that passed the checks reaches the music.

**Why.** derivation not recorded — the design document states the rule and the retry loop, but gives no reason for hiding the failed attempt from the user rather than surfacing it.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:304-305`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.3** — `### 4.3 Validation Layer` (heading at line 296). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §4.3, read in full by the phase-1 reads wave 1. The document's banner reads "Design phase. No code written yet." and `src/llm/` does not exist at HEAD, so the record does not say whether this rule is in force; "not stated" is entered rather than a status inferred from the surrounding section's deferral. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-443 — Tool use is the only capability the provider abstraction requires; a provider without it is read-only

> Users choose their LLM provider in MuseScore preferences. The abstraction
> requires only that a provider supports tool use (function calling). Providers
> without tool use support may be used for read-only analysis but cannot drive
> score modification.

**In plain words.** The user picks which language-model provider to use. The only thing the system demands of a provider is that it can call tools. One that cannot may still be used to answer questions about the music, but it may not be used to change the music.

**Why.** Stated with the decision: the modification path is built entirely out of tool calls (`docs/llm_integration.md` §3.2, §8.2), so a provider that cannot call tools has no way to express a change — the restriction follows from the stateless tool-call model rather than being an added policy.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:601-604`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8.1** — `### 8.1 Multi-provider abstraction` (heading at line 599). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §8.1, read in full by the phase-1 reads wave 1; §3.5 states the same abstraction from the other side. ARCHITECTURE.md §19.1 records the multi-provider choice but NOT the tool-use requirement or the read-only consequence, which is why this is entered rather than treated as carried. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-444 — The core access layer is a facade over interfaces that already exist, not a redesign

> family already covers almost everything the Core Access Layer needs. **The
> Core Access Layer is not a redesign — it is a facade over interfaces that
> already exist.**

**In plain words.** The shared foundation the language-model bridge and any future plugin interface both sit on is not new machinery. An audit of the existing internal interfaces found they already cover almost everything it needs, so the layer is a clean face over what is there.

**Why.** Stated with the decision: `docs/llm_integration.md` §5.2 tabulates sixteen existing interfaces against what the core access layer needs, and §5.4 names the only three gaps (query methods shaped for an external consumer, a transaction scope, and change descriptions carrying musical addresses rather than raw pointers). This is D-227's rule — read how MuseScore already does it and never invent parallel infrastructure — applied to a whole layer.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:367-369`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.2** — `### 5.2 The existing interfaces already define most of this` (heading at line 363). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §5.2, read in full by the phase-1 reads wave 1. The layer is named in ARCHITECTURE.md §19.4 as the thing the bridge is confined to (D-143), but the facade decision and its audit are recorded only in the design document. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-445 — A musical address does not identify a single note, so the note entity carries its own identifier

> **Address alone does not uniquely identify a Note.** Multiple notes in the same
> chord share an identical address (same part + staff + measure + beat + voice).
> A `NoteId` is required to unambiguously target a single note. `NoteId` must
> appear explicitly on the Note entity; it maps internally to the EID system.

**In plain words.** Several notes of one chord sit at exactly the same address — same part, staff, bar, beat and voice — so an address cannot name one note. The note therefore carries an identifier of its own, and that identifier is what a change is aimed at.

**Why.** Stated with the decision: §5.3 derives it from the information model it has just set out — the musical address is the sole locator and there are no object references, which makes queries pure filtering rather than graph walking, and the same property is what leaves a single note unaddressable without an identifier.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:418-421`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 The information model — key design point` (heading at line 397). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §5.3, read in full by the phase-1 reads wave 1. D-139 carries the stateless every-call-carries-its-address half from ARCHITECTURE.md:6962; the consequence that an address is not enough is recorded only here. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-446 — The language model resolves how the user names a passage; no index is built and the kinds of reference are not enumerated

> No pre-built index. The LLM's language understanding is the resolution
> mechanism. Do not try to enumerate and pre-categorize reference types —
> the space is open-ended. The system only needs to ensure the LLM has the
> information required to resolve whatever reference the user makes.

**In plain words.** Musicians point at music in open-ended ways — from a rehearsal mark, from where the choir enters, from the first C sharp in the cello, from something said earlier in the conversation. The system does not try to list those ways or build a lookup for them. It makes sure the model has the structural facts and the search tools, and lets the model do the resolving.

**Why.** Stated with the decision: the space of references is open-ended, so an enumeration would be incomplete by construction; §6 lists five families of reference precisely to show that the list does not close.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:518-521`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Score Addressing` (heading at line 479). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §6, read in full by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-447 — The model's tool definitions are generated from the operation set, never maintained by hand

> Tool definitions for the LLM are generated automatically from the operation
> set schemas. Adding a new operation to the operation set automatically makes
> it available as an LLM tool. No manual maintenance.

**In plain words.** What the model is told it can do is derived from the operations themselves. Adding an operation makes it available to the model with no second list to keep in step.

**Why.** Stated with the decision — no manual maintenance, so the two cannot drift. This is #6 (one path per concern) applied to the tool surface: a hand-kept second list is the duplication that goes stale.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:613-615`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8.2** — `### 8.2 Tool definitions` (heading at line 611). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §8.2, read in full by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-448 — The operation set is curated from observed use, not an exposure of every editing method

> ~40 curated operations covering the high-value modification tasks. Not an
> attempt to expose every `INotationInteraction` method. Chosen by observing
> which operations Phase 1 and Phase 2 usage actually reaches for.

**In plain words.** The model gets a chosen set of about forty editing operations covering the changes that matter, rather than everything the editor can do. Which ones are chosen is decided by watching what the read-only phases actually reach for.

**Why.** Stated with the decision: the set is chosen by observing real use in the two earlier read-only phases, so the curation has an evidence source rather than being a guess at what will be needed.

**Status.** NOT STATED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/llm_integration.md:286-288`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.2** — `### 4.2 Operation Set` (heading at line 284). A delegation at ARCHITECTURE.md:8096 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `docs/llm_integration.md` §4.2, read in full by the phase-1 reads wave 1. ARCHITECTURE.md §19.4's phase table records the count but not the curation rule or its evidence source. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

