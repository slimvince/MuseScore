# Decisions group B — The notation output surface and the record path

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-009 — The notation record is the ONE surface the in-app path reads, and it never re-decodes

> assembles the ONE surface the in-app notation path will read (Decision A2), from the
> decode outputs + the decode's prior inputs + the compiled-in provenance — it NEVER re-decodes and never reads the
> score.

**In plain words.** Everything the program shows you about harmony in the score comes from one assembled result. Nothing downstream re-runs the analysis or looks at the notes again.

**Why.** Stated constraint, ARCHITECTURE.md:130 and :71-72 - the seams read the record as pure views (#6, one path per concern): the record never re-decodes and never reads the score, so there is exactly one place the in-app answer comes from.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:82-84`

**Provenance.** ARCHITECTURE.md:73 names 'Decision A2' and cites cowork_notation_output_contract.md §3.1-§3.4

### D-010 — The switch - the record path is the production in-app notation analysis

> flipped `useJointNotationRecord`'s default to **ON**.

**In plain words.** Since 27 July 2026 the harmony you see inside the program is produced by the joint estimator. The old path is still compiled in but is only reachable by explicitly turning the new one off.

**Why.** Measurement, ARCHITECTURE.md:246-251: every legacy->record difference in the refreshed pipeline-snapshot goldens was reconciled to the P6 classified taxonomy - 0 unexplained, 0 input-scoping, the non-flag-gated surfaces byte-identical - with the P6 report and the OI-178 adoption record cited as the switch's preconditions.

**Status.** LIVE · decided 2026-07-27 · ratified by user

**Home.** `ARCHITECTURE.md:250`

**Provenance.** ARCHITECTURE.md:239; CLAUDE.md gate block (A) 'STAGED SCOPE - CLOSED AT THE NOTATION SWITCH'; confirmed at composingconfiguration.cpp:178 Val(true)

### D-011 — The producer decodes the WHOLE score once, and does not cache

> WHOLE-score decode ONCE; deterministic; NO caching (a
> later, measured concern — #17's funnel, not built speculatively).

**In plain words.** Every request analyses the entire score from the beginning, every time, and nothing is remembered between requests.

**Why.** Recorded for the no-caching half only, ARCHITECTURE.md:119-120: a cache is 'a later, measured concern - #17's funnel, not built speculatively'. The whole-score extent itself has no recorded derivation (open_items/OI-210 records that the last ruling on extent went the other way).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:126-127`

**Provenance.** Recorded as specification, no ratification named. Conflicts with D-030 (bounded context) - see OPEN_ITEMS OI-210 (the extent question) and OI-212 (the whole-score analysis input); the no-caching half is OI-203 (the deferred record cache) and OI-213 (the per-command multiplier)

### D-012 — Failure is unambiguous - never a partial record, never a silent fallback

> never a partial record, never a silent fallback (#13).

**In plain words.** If the analysis cannot be produced, the program says so and returns nothing. It never returns half an answer or quietly falls back to the old method.

**Why.** Stated constraint, ARCHITECTURE.md:122 - #13, a surprise is surfaced as a stop rather than built around: a partial record or a silent fallback would hide the failure from the caller.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:129`

**Provenance.** ARCHITECTURE.md:121-122; restated at :205-206 for the note seam

### D-013 — Which staves feed the analysis is decided at the fact adapter, not by a later filter

> INPUT selection at the fact
> adapter (the layer that owns its input surface, #7), before the note enters the L1 fact view the decode reads; NOT a
> consumer-side post-filter, NOT an inference change

**In plain words.** When a staff is excluded from analysis - for instance the chord staff the program itself writes to - its notes are dropped before the analysis starts, not filtered out of the answer afterwards.

**Why.** Stated constraint, ARCHITECTURE.md:124-128: input selection belongs at the layer that owns its input surface (#7), and doing it there is what stops a populated chord staff's own notes from being fed back into a re-analysis - the self-feedback hazard the legacy design guarded against (ARCHITECTURE.md:5786-5787).

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:131-133`

**Provenance.** open_items/OI-204 (RESOLVED 2026-07-27); confirmed at jointnotationproducer.h:72-73

### D-014 — The two seams read the record as pure views - no recomputation

> The two §1 seams READ this record as pure VIEWS (#6, no recompute)

**In plain words.** The two ways of asking the record a question - 'what is in this stretch of music' and 'what is at this moment' - only look things up. Neither works anything out for itself.

**Why.** Stated constraint, ARCHITECTURE.md:130 - #6, one path per concern: a view cannot disagree with the record it reads, a second computation can.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:137`

**Provenance.** ARCHITECTURE.md:130-136; confirmed at jointnotationproducer.h:86-90

### D-015 — A boundary tick belongs to the segment it starts

> a boundary
> tick belongs to the segment it STARTS

**In plain words.** When a moment is exactly where one chord ends and the next begins, it counts as belonging to the new chord.

**Why.** SEARCHED 2026-08-09 and the record holds NO DERIVATION — an established gap, not an unexamined field. The convention is stated as a DEFINITION at its home and at `ARCHITECTURE.md:132-134`: no alternative is considered, no reason is given, and no measurement or citation is attached anywhere the search reached. It is one of the founding instances `CLAUDE.md`'s carry-its-defense rule names in its own text. The gap is stated rather than filled: a boundary convention of this shape has obvious pragmatic grounds a session could invent, and inventing one is what the never-work-from-memory rule forbids.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:140-141`

**Provenance.** ARCHITECTURE.md:132-134. Derivation not recorded: the convention is stated as a definition, with no alternative considered and no reason given

### D-016 — Display renderings are presentation; facts are published

> display renderings are presentation, facts are published

**In plain words.** The Roman numeral is a fact the estimator publishes. The chord symbol you read on screen and the Nashville number are ways of showing that fact, produced by the display code.

**Why.** Stated constraint, ARCHITECTURE.md:154-155 (Decision D2 + the contract §3.3 amendment), resting on §2.3 (ARCHITECTURE.md:483-485): the analysis layer produces structured data and never display strings, a separation `ChordSymbolFormatter` already establishes.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:162`

**Provenance.** ARCHITECTURE.md:154 names 'Decision D2 + the contract §3.3 amendment'

### D-017 — The inference/presentation boundary is guarded mechanically, both ways

> **THE BOUNDARY
> IS PERMANENTLY GUARDED both ways** by a mechanical include-closure test

**In plain words.** A test enforces that the analysis code cannot reach the display code and the display code cannot reach the analysis internals. The test itself is checked by deliberately breaking it.

**Why.** Stated constraint, ARCHITECTURE.md:161-166: the boundary D-071 draws is enforceable only mechanically, so an include-closure test asserts it in both directions and carries a negative control that fires on a perturbed include.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:167-168`

**Provenance.** ARCHITECTURE.md:160-167; the guard carries a negative control

### D-018 — The key-exposure bucket is decided once, at one site

> The implode reads the stored bucket (#6 — one thresholding site per gate).

**In plain words.** How confident the program is about the tonality is turned into 'below tentative / tentative / assertive' in exactly one place, and everything downstream reads that answer instead of deciding again.

**Why.** Stated constraint, ARCHITECTURE.md:178 - #6, one thresholding site per gate: the bucket is set once at the section-layer set site and the implode reads it, instead of each consumer re-thresholding.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:185`

**Provenance.** ARCHITECTURE.md:172-178; open_items/OI-182 (EXECUTED at the record surface)

### D-019 — The record arm publishes the raw key-axis gap, with no remapping to 0..1

> `keyConfidence` = the RAW §3.3
> key-axis gap in nats (a model-internal quantity, NO [0,1] remap)

**In plain words.** The confidence value carried on the record arm is the estimator's own raw score gap, on its own scale - deliberately not converted into a 0-to-1 number.

**Why.** SEARCHED 2026-08-09 and the record holds NO REASON for the choice. What it holds INSTEAD is a recorded CONFLICT, which is why this gap is the sharper kind: the raw nats gap is written into a field whose declared range is 0 to 1, and carrying an unmapped model-internal quantity there contradicts the ratified confidence contract's rule that a confidence is compared only within its declared class and frame (**D-032**). The conflict is tracked at `OPEN_ITEMS.md` OI-231 and is not resolved here. So the entry records a decision whose defense is absent AND whose conformance is disputed — two different things, and neither is filled in from memory.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:212-213`

**Provenance.** ARCHITECTURE.md:176-177 and :198-199; confirmed at sectionrecordadapter.cpp:293. CONFLICTS with the ratified confidence contract rule U2 (D-032) and with the declared range of the field it is written into (keymodeanalyzer.h:111) - see OPEN_ITEMS OI-231

### D-020 — The interactive path bypasses the old window cache and has none of its own

> The bounded-window decode
> cache is BYPASSED on the record arm (a whole-score produce per invocation, the P3a/P4 pattern; a record cache is a later
> measured concern

**In plain words.** Clicking a note re-analyses the whole score. The old shortcut that reused a small window's work is not used on the new path, and no replacement has been built yet.

**Why.** Stated constraint, ARCHITECTURE.md:214-216: bypassing the bounded-window cache is recorded as a cost, not a structural incompatibility - a record cache is 'a later measured concern', the same measure-before-build funnel as D-011.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:220-222`

**Provenance.** open_items/OI-203 (OPEN, priority raised post-switch); open_items/OI-206

### D-021 — The pedal-point fields are suspended on the record arm

> the pedal fields stay false/-1 (suspended, OI-194)

**In plain words.** The new path does not yet mark pedal points - a sustained bass note the harmony moves over. The field is left empty rather than guessed.

**Why.** Stated constraint, open_items/OI-194.md:7: the labels' independent validation resource is not on disk, and coupling an open establishment question to the one commit whose verification must be airtight would mix the two (#22/#13); publication before validation is lawful only status-marked unvalidated with no consumer under load (#19).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:213`

**Provenance.** open_items/OI-194 (OPEN - its own increment after the switch)

### D-275 — Every published record carries its own instrument provenance; a provenance-less analysis cannot exist

> Every published record carries its instrument provenance: the embedded table set's source-artifact
> hashes and the selected weight-vector identity (both compiled in per Decision D1), plus the
> decoder's version. A consumer — and any future measurement — can always answer "which fitted
> values produced this analysis" from the record itself; a provenance-less analysis cannot exist.

**In plain words.** Each record published for the notation path carries the source-artifact hashes of the fitted table set, the identity of the selected weight vector, and the decoder's version. A consumer, or any later measurement, can always answer which fitted values produced a given analysis from the analysis itself.

**Why.** It is principle #16 (every measurement stamped to its corpus and its tooling) applied at the record level rather than at the measurement level: an analysis that has left the module can otherwise no longer be attributed to the values that produced it, which makes any later reproduction check impossible.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_notation_output_contract.md:54-57`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Provenance on the surface (#16/#19)` (heading at line 52). A delegation at ARCHITECTURE.md:79 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_notation_output_contract.md:3 records the user's ratification, dated 2026-07-26, as specified and without amendments; the provenance rule at :52-57. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-276 — Modal colour is published as un-rounded per-degree counts; no mode label is inferred or published anywhere

> For each key run and each scale degree 1..7 of its key: the sounding duration and onset count of
> EVERY chromatic inflection of that degree actually observed in the run (computed from the
> published L1 note facts relative to (tonic, mode)). This is the whole publication — counted,
> un-rounded, nothing hand-set: minor's variable 6̂/7̂ (Dorian color, subtonic-vs-leading-tone),
> major's lowered 7̂ (Mixolydian color) or raised 4̂ (Lydian color), and every borrowing appear as
> their actual counts. The presentation layer may FORMAT a reading from it ("Dorian-leaning"); the
> published fact is the counts, with establishment status (§5.4). No 21-value mode label is
> inferred or published anywhere (C1); the two-mode key plus this table informationally dominates
> the retired labels (#12).

**In plain words.** For each key run and each scale degree, the record publishes the sounding duration and onset count of every chromatic inflection of that degree actually observed. That is the whole publication - counted, un-rounded, nothing hand-set - so minor's variable sixth and seventh, major's lowered seventh or raised fourth, and every borrowing appear as their actual counts. A presentation layer may format a reading from it; no twenty-one-value mode label is inferred or published.

**Why.** The reason is stated with the decision (cowork_notation_output_contract.md:146-147): the two-mode key plus the count table informationally dominates the retired mode labels, so publishing counts rather than a label loses nothing (#12) while removing an inference nobody had established. Register entry D-054 records the twenty-one-mode vocabulary this supersedes on the record surface.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_notation_output_contract.md:139-147`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§3.4** — `### 3.4 Per key run — the un-rounded modal reading (C1; ratified decision 1 delivered)` (heading at line 137). A delegation at ARCHITECTURE.md:79 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_notation_output_contract.md:3 records the user's ratification, dated 2026-07-26, as specified and without amendments; the modal reading at :137-147. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-425 — The uncertainty surface's contract IS the full posterior; the local slice is the first delivered step, and the completion is a named step, never an indefinite upgrade

> **Recommendation: the contract IS B-full; B-slice is the first DELIVERED step (it is established
> today and is a strict subset of B-full's surface), and the marginal completion is a NAMED, ROWED
> step of this increment — not an indefinite upgrade.** Register row at ruling time (register rule
> (c)); the slice's fields are defined as views of the posterior so nothing is published twice
> (#6). If the marginal oracle's establishment surfaces a blocker, that is a #13 STOP returning to
> the user — never a silent regression to B-slice-as-end-state.

**In plain words.** What the analysis publishes about its own uncertainty is, by contract, the full spread of probability over every reading it considered — not just a note about the runner-up. The narrower runner-up form ships first, because it is the part already checked and it is a subset of the full form; finishing the rest is a named, tracked step of the same piece of work, not something that waits for someone to ask for it. If checking the full form turns up a problem, that stops the work and goes back to the user; it never quietly becomes a decision to keep the narrow form forever.

**Why.** Three recorded grounds point the same way and are given with the decision. The ratified decode plan already requires it — "the full posterior (not only the best path) is retained for the published alternatives and the uncertainty surface" — so delivering less would re-ratify away a ratified clause. The evidence-publication amendment (`CLAUDE.md`, the fact-publication corollary as amended 2026-07-12) says evidence-class facts are published broadly EVEN WITHOUT a named consumer, which answers the "wait for a consumer" deferral directly. And the named information loss is specific rather than general: a local slice hides the mass that lies across segmentations, so a passage whose boundaries are ambiguous looks artificially certain (#17e, the false-negative path stated). The document also records that the previous writing recommended the slice and that the recommendation was VOID, because its basis was the slice's ready-made checking tool — reuse value, which the decision-neutrality corollary (D-190) ranks secondary.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `cowork_notation_adoption_increment.md:282`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. Decision B — what the published posterior IS (the uncertainty surface)` (heading at line 215). A delegation at ARCHITECTURE.md:6869 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_notation_adoption_increment.md`:282-287, the Decision-B recommendation, which the document's §9 records the user granting on 2026-07-26 — "B-full (slice-first, completion rowed OI-193)" — and its opening banner repeats. Distinct from D-006 (the record publishes two full candidate lists with no truncation) and from D-007/D-008 (the published values are log-scores, with true probabilities deferred), which govern what the RECORD carries and in what units; this governs what the uncertainty surface IS by contract, and it carries the anti-regression guard. The completion step is tracked as `OPEN_ITEMS.md` OI-193. Its natural home is the notation output-surface contract `cowork_notation_output_contract.md`, which `ARCHITECTURE.md`:73 names and which is a contract home (D-275/D-276), hence the documentation-gap flag. Found by the phase-1l continuation wave, 2026-08-03, reading `cowork_notation_adoption_increment.md` IN FULL (the OI-207 reading list's next document, 17 unresolved clusters). The document carries a status banner and is user-ratified 2026-07-26, but NO user-ratified surface names it — it is absent from `ARCHITECTURE.md`, `CLAUDE.md` and `cowork_engage_arc_plan.md` alike (measured this session at Task 7) — so it is not a contract home under either the phase-1i criterion or the delegation-specificity criterion the user ruled 2026-08-03. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1l ratification queue.

### D-426 — The modal reading lands inside the notation increment; the ornament labels get their own increment, with the tracking row created at ruling time

> **Recommendation: modal reading inside the increment; ornament labels as their own increment
> (E-orn-2) with the row created at ruling time.**

**In plain words.** Of the two publications the record already promised, the one describing a passage's modal colour ships with this piece of work, because everything it is computed from is already checked. The one naming ornamental notes becomes a separate piece of work, because the material that would independently validate it is not held; its tracking entry is opened at the moment the decision is made, so the gap has a named way out rather than becoming something forgotten.

**Why.** The two halves are split on a stated establishment difference, not on size. The modal reading is computed from emission quantities that are already fitted and already established, so nothing blocks it. The ornament labels' independent validation resource is a dataset the record names and that is NOT on disk (verified at the OI-185/OI-179 rows), so publishing them now would be lawful only marked unvalidated — and attaching an open establishment question to the ONE commit whose verification has to be airtight would weaken exactly the event that must not be weakened (#22/#13/#15). The drop-out risk the split creates is answered by the register mechanism itself: the row is opened at ruling time (the decisions register's rule (c)), which makes it a declared and bounded migration state (#23) with a named exit rather than an item that quietly disappears.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `cowork_notation_adoption_increment.md:436`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§7** — `## 7. Decision E — scheduling the two ratified presentation publications` (heading at line 394). A delegation at ARCHITECTURE.md:6869 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_notation_adoption_increment.md`:436-437, the Decision-E recommendation, which §9 records the user granting on 2026-07-26 — "the E split (modal reading in-increment; ornament labels rowed OI-194)". The ornament increment is `OPEN_ITEMS.md` OI-194, and D-207 (the voice-independent pedal-point class, DEFERRED) is one of the classes it carries. The modal-reading half is delivered and registered as D-276, homed in the notation output-surface contract; what is registered HERE is the SCHEDULING decision and its establishment reason, which lives in neither. Its natural home is that same contract, hence the documentation-gap flag. Found by the phase-1l continuation wave, 2026-08-03, reading `cowork_notation_adoption_increment.md` IN FULL (the OI-207 reading list's next document, 17 unresolved clusters). The document carries a status banner and is user-ratified 2026-07-26, but NO user-ratified surface names it — it is absent from `ARCHITECTURE.md`, `CLAUDE.md` and `cowork_engage_arc_plan.md` alike (measured this session at Task 7) — so it is not a contract home under either the phase-1i criterion or the delegation-specificity criterion the user ruled 2026-08-03. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1l ratification queue.

