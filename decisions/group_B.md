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

**Home.** `ARCHITECTURE.md:75-77`

**Provenance.** ARCHITECTURE.md:73 names 'Decision A2' and cites cowork_notation_output_contract.md §3.1-§3.4

### D-010 — The switch - the record path is the production in-app notation analysis

> flipped `useJointNotationRecord`'s default to **ON**.

**In plain words.** Since 27 July 2026 the harmony you see inside the program is produced by the joint estimator. The old path is still compiled in but is only reachable by explicitly turning the new one off.

**Why.** Measurement, ARCHITECTURE.md:246-251: every legacy->record difference in the refreshed pipeline-snapshot goldens was reconciled to the P6 classified taxonomy - 0 unexplained, 0 input-scoping, the non-flag-gated surfaces byte-identical - with the P6 report and the OI-178 adoption record cited as the switch's preconditions.

**Status.** LIVE · decided 2026-07-27 · ratified by user

**Home.** `ARCHITECTURE.md:243`

**Provenance.** ARCHITECTURE.md:239; CLAUDE.md gate block (A) 'STAGED SCOPE - CLOSED AT THE NOTATION SWITCH'; confirmed at composingconfiguration.cpp:178 Val(true)

### D-011 — The producer decodes the WHOLE score once, and does not cache

> WHOLE-score decode ONCE; deterministic; NO caching (a
> later, measured concern — #17's funnel, not built speculatively).

**In plain words.** Every request analyses the entire score from the beginning, every time, and nothing is remembered between requests.

**Why.** Recorded for the no-caching half only, ARCHITECTURE.md:119-120: a cache is 'a later, measured concern - #17's funnel, not built speculatively'. The whole-score extent itself has no recorded derivation (open_items/OI-210 records that the last ruling on extent went the other way).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:119-120`

**Provenance.** Recorded as specification, no ratification named. Conflicts with D-030 (bounded context) - see OPEN_ITEMS OI-210 (the extent question) and OI-212 (the whole-score analysis input); the no-caching half is OI-203 (the deferred record cache) and OI-213 (the per-command multiplier)

### D-012 — Failure is unambiguous - never a partial record, never a silent fallback

> never a partial record, never a silent fallback (#13).

**In plain words.** If the analysis cannot be produced, the program says so and returns nothing. It never returns half an answer or quietly falls back to the old method.

**Why.** Stated constraint, ARCHITECTURE.md:122 - #13, a surprise is surfaced as a stop rather than built around: a partial record or a silent fallback would hide the failure from the caller.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:122`

**Provenance.** ARCHITECTURE.md:121-122; restated at :205-206 for the note seam

### D-013 — Which staves feed the analysis is decided at the fact adapter, not by a later filter

> INPUT selection at the fact
> adapter (the layer that owns its input surface, #7), before the note enters the L1 fact view the decode reads; NOT a
> consumer-side post-filter, NOT an inference change

**In plain words.** When a staff is excluded from analysis - for instance the chord staff the program itself writes to - its notes are dropped before the analysis starts, not filtered out of the answer afterwards.

**Why.** Stated constraint, ARCHITECTURE.md:124-128: input selection belongs at the layer that owns its input surface (#7), and doing it there is what stops a populated chord staff's own notes from being fed back into a re-analysis - the self-feedback hazard the legacy design guarded against (ARCHITECTURE.md:5786-5787).

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:124-126`

**Provenance.** open_items/OI-204 (RESOLVED 2026-07-27); confirmed at jointnotationproducer.h:72-73

### D-014 — The two seams read the record as pure views - no recomputation

> The two §1 seams READ this record as pure VIEWS (#6, no recompute)

**In plain words.** The two ways of asking the record a question - 'what is in this stretch of music' and 'what is at this moment' - only look things up. Neither works anything out for itself.

**Why.** Stated constraint, ARCHITECTURE.md:130 - #6, one path per concern: a view cannot disagree with the record it reads, a second computation can.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:130`

**Provenance.** ARCHITECTURE.md:130-136; confirmed at jointnotationproducer.h:86-90

### D-015 — A boundary tick belongs to the segment it starts

> a boundary
> tick belongs to the segment it STARTS

**In plain words.** When a moment is exactly where one chord ends and the next begins, it counts as belonging to the new chord.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:133-134`

**Provenance.** ARCHITECTURE.md:132-134. Derivation not recorded: the convention is stated as a definition, with no alternative considered and no reason given

### D-016 — Display renderings are presentation; facts are published

> display renderings are presentation, facts are published

**In plain words.** The Roman numeral is a fact the estimator publishes. The chord symbol you read on screen and the Nashville number are ways of showing that fact, produced by the display code.

**Why.** Stated constraint, ARCHITECTURE.md:154-155 (Decision D2 + the contract §3.3 amendment), resting on §2.3 (ARCHITECTURE.md:483-485): the analysis layer produces structured data and never display strings, a separation `ChordSymbolFormatter` already establishes.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:155`

**Provenance.** ARCHITECTURE.md:154 names 'Decision D2 + the contract §3.3 amendment'

### D-017 — The inference/presentation boundary is guarded mechanically, both ways

> **THE BOUNDARY
> IS PERMANENTLY GUARDED both ways** by a mechanical include-closure test

**In plain words.** A test enforces that the analysis code cannot reach the display code and the display code cannot reach the analysis internals. The test itself is checked by deliberately breaking it.

**Why.** Stated constraint, ARCHITECTURE.md:161-166: the boundary D-071 draws is enforceable only mechanically, so an include-closure test asserts it in both directions and carries a negative control that fires on a perturbed include.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:160-161`

**Provenance.** ARCHITECTURE.md:160-167; the guard carries a negative control

### D-018 — The key-exposure bucket is decided once, at one site

> The implode reads the stored bucket (#6 — one thresholding site per gate).

**In plain words.** How confident the program is about the tonality is turned into 'below tentative / tentative / assertive' in exactly one place, and everything downstream reads that answer instead of deciding again.

**Why.** Stated constraint, ARCHITECTURE.md:178 - #6, one thresholding site per gate: the bucket is set once at the section-layer set site and the implode reads it, instead of each consumer re-thresholding.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:178`

**Provenance.** ARCHITECTURE.md:172-178; open_items/OI-182 (EXECUTED at the record surface)

### D-019 — The record arm publishes the raw key-axis gap, with no remapping to 0..1

> `keyConfidence` = the RAW §3.3
> key-axis gap in nats (a model-internal quantity, NO [0,1] remap)

**In plain words.** The confidence value carried on the record arm is the estimator's own raw score gap, on its own scale - deliberately not converted into a 0-to-1 number.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:205-206`

**Provenance.** ARCHITECTURE.md:176-177 and :198-199; confirmed at sectionrecordadapter.cpp:293. CONFLICTS with the ratified confidence contract rule U2 (D-032) and with the declared range of the field it is written into (keymodeanalyzer.h:111) - see OPEN_ITEMS OI-231

### D-020 — The interactive path bypasses the old window cache and has none of its own

> The bounded-window decode
> cache is BYPASSED on the record arm (a whole-score produce per invocation, the P3a/P4 pattern; a record cache is a later
> measured concern

**In plain words.** Clicking a note re-analyses the whole score. The old shortcut that reused a small window's work is not used on the new path, and no replacement has been built yet.

**Why.** Stated constraint, ARCHITECTURE.md:214-216: bypassing the bounded-window cache is recorded as a cost, not a structural incompatibility - a record cache is 'a later measured concern', the same measure-before-build funnel as D-011.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:213-215`

**Provenance.** open_items/OI-203 (OPEN, priority raised post-switch); open_items/OI-206

### D-021 — The pedal-point fields are suspended on the record arm

> the pedal fields stay false/-1 (suspended, OI-194)

**In plain words.** The new path does not yet mark pedal points - a sustained bass note the harmony moves over. The field is left empty rather than guessed.

**Why.** Stated constraint, open_items/OI-194.md:7: the labels' independent validation resource is not on disk, and coupling an open establishment question to the one commit whose verification must be airtight would mix the two (#22/#13); publication before validation is lawful only status-marked unvalidated with no consumer under load (#19).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:206`

**Provenance.** open_items/OI-194 (OPEN - its own increment after the switch)

