# DECISIONS — the decisions register

> **What this is.** One entry per recorded decision about how this system works: what was
> decided, in the words it was decided in, what it means in plain language, and whether it
> still stands. Nothing else. Whether the code currently obeys a decision is **not** recorded
> here — that is tracked in `OPEN_ITEMS.md` as ordinary rows, each pointing back at the
> decision it violates. The two things change on different clocks, and holding them in one row
> produces a register that silently goes stale.
>
> **Shape ratified by the user, 2026-07-28** (`open_items/OI-208.md`, three rulings).
> **Populated by the OI-207 decision-conformance adjudication, 2026-08-01.**
>
> **GENERATED FILE — do not hand-edit.** Source of record:
> `tools/audit/decisions/backbone_decisions.json`; generator
> `tools/audit/decisions/gen_decisions_register.py`. Every number below is computed, never
> transcribed.

## How to read an entry

Each entry has five parts.

- **The decision, verbatim** — quoted exactly from the document that records it, word for word.
  (Where the source wrote the passage inside a quotation block, its `>` markers are dropped so the
  entry reads cleanly; nothing else is altered.) Quoted text keeps its original wording even where
  that wording uses a word in a non-musical sense; the plain restatement beneath it does not.
- **In plain words** — one or two sentences, written for a reader who knows music but not this
  project's private vocabulary.
- **Status** — see the table below. Where the record does not say when a decision was made or
  who ratified it, the entry says **not stated**. Nothing is inferred.
- **Home** — where the decision is actually recorded, as `file:line`. A decision about how a
  layer should work belongs in that layer's section of `ARCHITECTURE.md`; entries marked
  **home is not a layer specification** are decisions recorded somewhere else, which is a
  documentation gap and carries an `OPEN_ITEMS.md` row.
- **Provenance** — where the status comes from, and any later ruling that bears on it.

### The status words

| Status | Meaning |
|---|---|
| **LIVE** | In force. Nothing in the record supersedes, shelves or falsifies it. |
| **SUPERSEDED BY** | A later ruling replaces it. The replacement is named. |
| **SUPERSEDED IN FACT** | A later *build* replaced what it governs, without any ruling that names it. Recorded exactly that way — never quietly upgraded to "superseded by". |
| **SHELVED WITH EVIDENCE** | Withdrawn against a cited measurement. |
| **FALSIFIED** | A cited measurement contradicts it. |
| **DEFERRED** | Decided to be built later. The decision itself stands. |
| **NOT STATED** | The record does not say. |

### Terms used in the plain-language restatements

Standard music theory is used in its standard sense throughout. The terms below are this
project's own and are defined here because they are used before any entry explains them.

| Term | Meaning |
|---|---|
| **layer** | One stage of the analysis, responsible for one question. The stages are: reading the notes; cutting the music into stretches of unchanging sound; deciding the tonality; deciding the chord; deciding the chord's role; and assembling the result for display. |
| **slice** | The smallest stretch of music analysed: a span during which exactly the same notes are sounding. It begins when any note starts or stops and ends at the next such moment. |
| **onset / release** | The moment a note is struck and the moment it stops sounding. |
| **sounding note set** | Every note actually sounding during a stretch — including notes struck earlier and still held. Distinct from the notes *struck* at the start of that stretch. |
| **pitch class** | A note name irrespective of octave: every C is the same pitch class. |
| **the joint estimator** | The current analysis engine. It decides the tonality, the major/minor character, the chord, and where one chord ends and the next begins, all together in one pass rather than one after another. |
| **decode** | One run of that engine over a piece: the search for the best overall reading. |
| **emission** | The part of the engine that asks "how well do these notes fit this chord in this key?" for one moment of music. |
| **prior** | A standing assumption about how likely something is before any notes are examined — for instance that a piece is more likely to be in a common mode than a rare one. |
| **the corpus** | The 326 annotated Bach chorales the engine's numbers were learned from and is graded against. |
| **ground truth** | The published human annotations we grade against — here the *When in Rome* / DCML analyses of those chorales. |
| **held-out** | Music deliberately kept back from the learning step so that the reported accuracy is measured on material the engine has not seen. |
| **content score** | A number the engine assigns to a candidate reading. Higher is better. It is not a probability and cannot be read as one. |
| **gap (in nats)** | The difference between the best reading's content score and the next one's, on the engine's own scale. A larger gap means a more clear-cut decision. *Nats* is the unit that scale is expressed in. |
| **the record** | The single assembled result the program reads when it shows you anything about harmony: the committed reading for each stretch, its alternatives, and the facts derived from them. |
| **the record arm / the legacy arm** | The two code paths that can produce that result — the current one built on the joint estimator, and the older stage-by-stage one it replaced. The current one is what runs. |
| **the robust unit** | The way accuracy is measured: the music is cut at every boundary either we or the annotator placed, and agreement is counted by how much *time* it covers, so that a change in how finely we cut cannot move the number. |
| **the hard stop** | The rule that decides whether a change may ship: the total time on which we name the wrong chord root, counted only where the root is decidable at all, must not increase. |
| **measurement tool** | A script that measures something. (Never called an "instrument" in this project's writing — that word is reserved for a violin.) |


## What is in this register, counted

**115 decisions**, grouped by subject. They were enumerated by reading the `ARCHITECTURE.md` layer specifications in full, because a decision written as plain specification carries no ruling vocabulary and no text search can find it. Every verbatim quote below is mechanically checked to exist at the place it is cited to (`gen_cluster_dispositions.py --verify`).

| | Count |
|---|---|
| Decisions recorded | **115** |
| — of which live | 101 |
| — of which superseded in fact | 6 |
| — of which superseded by | 3 |
| — of which deferred | 5 |
| Decisions whose date is not stated in the record | 83 |
| Decisions whose ratifier is not stated in the record | 86 |
| Decisions recorded outside any layer specification | 16 |

Alongside the register, every one of the harvested statements about decisions in this repository has been given a recorded disposition, so that none was silently passed over:

| | Count |
|---|---|
| Harvested statements | **15224** |
| Groups of near-identical statements ("clusters") | **14460** |
| Clusters carrying a recorded disposition | **14460** |
| — restates | 2603 |
| — not-a-decision | 3629 |
| — boilerplate | 74 |
| — no-spec-home | 1780 |
| — unresolved | 6374 |

The full disposition table, and the numbered rule behind each one, are in `tools/audit/decisions/cluster_dispositions.csv` and `tools/audit/decisions/disposition_manifest.json`.

### What was read, and what was not

**Read in full.** ARCHITECTURE.md lines 1-3981 — the preamble (the joint estimator, the posterior slice, the A-native notation record, the record path P0-P7, doc governance), §2 Architectural Principles including §2.14 and §2.15, §3.3 Module Boundaries including the Layer 1-6 specifications and the path-divergence decisions, §4 Existing Components (§4.1-§4.6), and §5 Planned Analysis Extensions (§5.1-§5.16). Plus, targeted and cited: CLAUDE.md, OPEN_ITEMS.md and its detail files, cowork_confidence_contract.md, cowork_design_doc_template.md.

**Not read in full.** ARCHITECTURE.md lines 3982-6523 — §6 The Style System through §19 LLM Integration, plus the appendices. These specify the style system, the knowledge base, the generation components, the constraint system, visualization, intonation, the user interface, persistence, machine-learning readiness, development phases, the scope reference, coding standards, contributing, and LLM integration. None of them is a layer of the harmonic-analysis stack this adjudication was scoped to.

**The remainder, measured.** The harvest holds 241 candidate statements sourced to ARCHITECTURE.md: 176 fall in the read range and 65 in the unread range (31 of those admitted by the harvest's HIGH signature tier). Decisions stated only in the unread range are NOT in this register.

*Why this is stated at all:* DEFECT_TYPES.md DT-26 — scope-assumed enumeration. A sweep that is complete inside its own file set reads as complete about the whole question. The scope and its measured remainder are therefore stated rather than left implicit.

---

## A. The estimator architecture — the joint estimator

### D-001 — Key, mode and chord are inferred by ONE joint decode

> Key, mode, and chord are inferred by ONE probabilistic decode
> over `(tonic, mode, chord)` with segmentation as a modeled (semi-Markov) variable and every enumerated clue
> as a theory-grounded factor

**In plain words.** The tonality, the major/minor character and the chord are not worked out one after another. They are worked out together, in a single pass that also decides where one chord ends and the next begins.

**Status.** LIVE · decided 2026-07-17 · ratified by user

**Home.** `ARCHITECTURE.md:4-6`

**Provenance.** ARCHITECTURE.md:3 (GOVERNING DECISION banner); OPEN_ITEMS.md:15-26

### D-002 — The fitted tables and weights are compiled into the binary verbatim

> compiles the five committed artifacts + the selected weight vector
> VERBATIM (JSON bytes, not a parsed-structure codegen) into the generated `jointembeddedartifacts.{h,cpp}`

**In plain words.** The numbers the estimator was trained on are built into the program at compile time rather than read from disk at run time, so a running copy cannot quietly disagree with the numbers we published.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:21-22`

**Provenance.** ARCHITECTURE.md:20 names it 'ratified Decision D1'; the ratifier and date are not stated at this home

### D-003 — Inference is preset-independent; presets are presentation concerns

> Inference is **preset-independent** (presets are
> presentation concerns)

**In plain words.** Choosing the Baroque, Jazz or Default preset changes nothing about what the estimator concludes; it changes only how the result is shown.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:33-34`

**Provenance.** CLAUDE.md gate block (A), the OI-178 adoption; open_items/OI-178

### D-004 — The decode state space and the segment cap

> State = `24 keys × a ground-truth-derived Roman-numeral
> vocabulary`, chord = scale-degree-valued (the chord symbol is the derived published fact from (key, degree)), segmentation is a modeled semi-Markov variable, seg_cap 4.

**In plain words.** The estimator chooses among 24 tonalities and a list of chord roles read off the annotated corpus; a chord is named by its role in the key, and the chord symbol is worked out from that. One chord may span at most four consecutive events.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:31-33`

**Provenance.** ARCHITECTURE.md:43-44 cites cowork_joint_estimator_factorization.md as the full specification. The cap's FORM is the established semi-Markov default (cowork_joint_estimator_factorization.md:112-114); the VALUE 4 has no recorded derivation anywhere in the record - derivation not recorded

### D-005 — The joint estimator is the production inference layer on the batch and corpus surface

> the joint estimator
> is now the PRODUCTION inference layer on the batch/corpus surface

**In plain words.** Everything the measurement corpus is graded on now comes from the joint estimator, not from the older chord-by-chord pipeline.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:11-12`

**Provenance.** CLAUDE.md gate block (A); tools/joint_estimator/adoption_record.json; open_items/OI-178

### D-006 — The published uncertainty surface is two full candidate lists, with no truncation

> publishes, per
> committed segment, the ESTABLISHED content-score uncertainty surface as two full candidate lists (no truncation
> constant)

**In plain words.** For every chord it commits to, the estimator also publishes how every other tonality and every other chord would have scored - the complete lists, not a top-few.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:47-49`

**Provenance.** ARCHITECTURE.md:46 names it 'the notation output-surface contract §3.3 GROUP (i)'

### D-007 — The published scores are log-scores, not probabilities

> The scores are LOG-scores, NOT probabilities, and gaps
> are score differences

**In plain words.** The numbers beside each alternative are not chances of being right. They are model scores, and the difference between two of them is a score gap, not a percentage.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:54-55`

**Provenance.** ARCHITECTURE.md:54-56; the true-probability step is deferred to OI-193

### D-008 — The true probabilities are deferred to a later step

> **GROUP (ii) forward-backward marginals are NOT delivered here — OI-193's later step.**

**In plain words.** The proper probability for each reading - the kind that can be checked against how often it is actually right - has not been built yet; it is a named later piece of work.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:55`

**Provenance.** open_items/OI-193 (OPEN)

### D-095 — The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state

> STAGED SCOPE (declared migration state, #23)

**In plain words.** Building the new estimator beside the old one temporarily breaks the rule that there is one way to do each thing. That was declared in advance, bounded, and given a retirement plan.

**Status.** SUPERSEDED IN FACT · decided 2026-07-19 · ratified by user

**Home.** `ARCHITECTURE.md:39`

**Provenance.** open_items/OI-180 (PROTOCOL RATIFIED 2026-07-19; forward exit EXECUTED on both surfaces 2026-07-27). The ARCHITECTURE.md text at :39-40 still says the notation layer stays legacy - see OPEN_ITEMS OI-232

### D-096 — Fitted values are fit once against ground truth, never per-case tuned

> forms from theory, values fit ONCE against GT (#19), never per-case tuned

**In plain words.** The shape of each piece of evidence comes from music theory. Its numerical strength is learned once from annotated music, and never adjusted to make a particular passage come out right.

**Status.** LIVE · decided 2026-07-17 · ratified by user

**Home.** `OPEN_ITEMS.md:25`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:15-26 (the governing architecture decision banner). NOT recorded in any ARCHITECTURE.md layer specification - see OPEN_ITEMS OI-237

### D-097 — Held-out evaluation and a capacity budget are declared before any fit

> 5-fold CV grouped by WiR file, all fitted objects train-fold-only, headline = pooled CV + piece-bootstrap CI

**In plain words.** Before the estimator's numbers are learned, we say in advance which music will be held back to test them on, and how many numbers we are allowed to learn at all. The headline number is always the one measured on the held-back music.

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Home.** `OPEN_ITEMS.md:123`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-176 and OI-177 (PROTOCOL RATIFIED 2026-07-19). The standing principles are CLAUDE.md #20. NOT recorded in any ARCHITECTURE.md layer specification - see OPEN_ITEMS OI-237

### D-098 — The exact-decode reserve - the declared prune was never adopted

> the exact-decode reserve is the declared remedy (never budgeted at fitted weights)

**In plain words.** The estimator was meant to be allowed to narrow its search when that gets too slow. The narrowing rule that was specified turned out to cost more than it saved, so the estimator still searches exactly - and how it actually narrows in practice was never specified.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `OPEN_ITEMS.md:194`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-188 (OPEN - 'bounds every ceiling claim'); the admission rule actually in production has no ratified basis (open_items/OI-226)

### D-114 — The decoder commits its best path; there is no abstention on the key axis

> **key-abstain 0** — A commits its MAP path, the OI-33 flag reads zero

**In plain words.** The joint estimator always names a key. It never declines to answer on the key axis, so the abstention counter is always zero.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `CLAUDE.md`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** CLAUDE.md gate block (A), the OI-178 adoption baselines. NOT recorded in any ARCHITECTURE.md layer specification, and it sits in tension with D-090 (calibrated abstention) - see OPEN_ITEMS OI-237

---

## B. The notation output surface and the record path

### D-009 — The notation record is the ONE surface the in-app path reads, and it never re-decodes

> assembles the ONE surface the in-app notation path will read (Decision A2), from the
> decode outputs + the decode's prior inputs + the compiled-in provenance — it NEVER re-decodes and never reads the
> score.

**In plain words.** Everything the program shows you about harmony in the score comes from one assembled result. Nothing downstream re-runs the analysis or looks at the notes again.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:70-72`

**Provenance.** ARCHITECTURE.md:68 names 'Decision A2' and cites cowork_notation_output_contract.md §3.1-§3.4

### D-010 — The switch - the record path is the production in-app notation analysis

> flipped `useJointNotationRecord`'s default to **ON**.

**In plain words.** Since 27 July 2026 the harmony you see inside the program is produced by the joint estimator. The old path is still compiled in but is only reachable by explicitly turning the new one off.

**Status.** LIVE · decided 2026-07-27 · ratified by user

**Home.** `ARCHITECTURE.md:236`

**Provenance.** ARCHITECTURE.md:232; CLAUDE.md gate block (A) 'STAGED SCOPE - CLOSED AT THE NOTATION SWITCH'; confirmed at composingconfiguration.cpp:178 Val(true)

### D-011 — The producer decodes the WHOLE score once, and does not cache

> WHOLE-score decode ONCE; deterministic; NO caching (a
> later, measured concern — #17's funnel, not built speculatively).

**In plain words.** Every request analyses the entire score from the beginning, every time, and nothing is remembered between requests.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:114-115`

**Provenance.** Recorded as specification, no ratification named. Conflicts with D-030 (bounded context) - see OPEN_ITEMS OI-210 (the extent question) and OI-212 (the whole-score analysis input); the no-caching half is OI-203 (the deferred record cache) and OI-213 (the per-command multiplier)

### D-012 — Failure is unambiguous - never a partial record, never a silent fallback

> never a partial record, never a silent fallback (#13).

**In plain words.** If the analysis cannot be produced, the program says so and returns nothing. It never returns half an answer or quietly falls back to the old method.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:117`

**Provenance.** ARCHITECTURE.md:116-117; restated at :205-206 for the note seam

### D-013 — Which staves feed the analysis is decided at the fact adapter, not by a later filter

> INPUT selection at the fact
> adapter (the layer that owns its input surface, #7), before the note enters the L1 fact view the decode reads; NOT a
> consumer-side post-filter, NOT an inference change

**In plain words.** When a staff is excluded from analysis - for instance the chord staff the program itself writes to - its notes are dropped before the analysis starts, not filtered out of the answer afterwards.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:119-121`

**Provenance.** open_items/OI-204 (RESOLVED 2026-07-27); confirmed at jointnotationproducer.h:72-73

### D-014 — The two seams read the record as pure views - no recomputation

> The two §1 seams READ this record as pure VIEWS (#6, no recompute)

**In plain words.** The two ways of asking the record a question - 'what is in this stretch of music' and 'what is at this moment' - only look things up. Neither works anything out for itself.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:125`

**Provenance.** ARCHITECTURE.md:125-131; confirmed at jointnotationproducer.h:86-90

### D-015 — A boundary tick belongs to the segment it starts

> a boundary
> tick belongs to the segment it STARTS

**In plain words.** When a moment is exactly where one chord ends and the next begins, it counts as belonging to the new chord.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:128-129`

**Provenance.** ARCHITECTURE.md:127-129. Derivation not recorded: the convention is stated as a definition, with no alternative considered and no reason given

### D-016 — Display renderings are presentation; facts are published

> display renderings are presentation, facts are published

**In plain words.** The Roman numeral is a fact the estimator publishes. The chord symbol you read on screen and the Nashville number are ways of showing that fact, produced by the display code.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:148`

**Provenance.** ARCHITECTURE.md:147 names 'Decision D2 + the contract §3.3 amendment'

### D-017 — The inference/presentation boundary is guarded mechanically, both ways

> **THE BOUNDARY
> IS PERMANENTLY GUARDED both ways** by a mechanical include-closure test

**In plain words.** A test enforces that the analysis code cannot reach the display code and the display code cannot reach the analysis internals. The test itself is checked by deliberately breaking it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:153-154`

**Provenance.** ARCHITECTURE.md:153-160; the guard carries a negative control

### D-018 — The key-exposure bucket is decided once, at one site

> The implode reads the stored bucket (#6 — one thresholding site per gate).

**In plain words.** How confident the program is about the tonality is turned into 'below tentative / tentative / assertive' in exactly one place, and everything downstream reads that answer instead of deciding again.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:171`

**Provenance.** ARCHITECTURE.md:165-171; open_items/OI-182 (EXECUTED at the record surface)

### D-019 — The record arm publishes the raw key-axis gap, with no remapping to 0..1

> `keyConfidence` = the RAW §3.3
> key-axis gap in nats (a model-internal quantity, NO [0,1] remap)

**In plain words.** The confidence value carried on the record arm is the estimator's own raw score gap, on its own scale - deliberately not converted into a 0-to-1 number.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:198-199`

**Provenance.** ARCHITECTURE.md:169-170 and :198-199; confirmed at sectionrecordadapter.cpp:293. CONFLICTS with the ratified confidence contract rule U2 (D-032) and with the declared range of the field it is written into (keymodeanalyzer.h:111) - see OPEN_ITEMS OI-231

### D-020 — The interactive path bypasses the old window cache and has none of its own

> The bounded-window decode
> cache is BYPASSED on the record arm (a whole-score produce per invocation, the P3a/P4 pattern; a record cache is a later
> measured concern

**In plain words.** Clicking a note re-analyses the whole score. The old shortcut that reused a small window's work is not used on the new path, and no replacement has been built yet.

**Status.** LIVE · decided 2026-07-27 · ratifier not stated

**Home.** `ARCHITECTURE.md:206-208`

**Provenance.** open_items/OI-203 (OPEN, priority raised post-switch); open_items/OI-206

### D-021 — The pedal-point fields are suspended on the record arm

> the pedal fields stay false/-1 (suspended, OI-194)

**In plain words.** The new path does not yet mark pedal points - a sustained bass note the harmony moves over. The field is left empty rather than guessed.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:199`

**Provenance.** open_items/OI-194 (OPEN - its own increment after the switch)

---

## C. Cross-cutting analysis contracts

### D-022 — The founding principle - analyse at the finest grain, coarser views are derived

> **The founding principle: analyze at the finest grain where harmony is well-defined, and make everything coarser a
> *derived view*.**

**In plain words.** The analysis works on the smallest stretch over which the sounding harmony does not change. Phrases, key areas and sections are then read off that, never analysed directly.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:746-747`

**Provenance.** ARCHITECTURE.md:744 heading says '(ratified; full statements in cowork_target_architecture.md)'; the date and ratifier are not stated at this home

### D-023 — The atomic analysis unit is the constant-sonority slice, never the metric beat

> The atomic analysis unit is the **constant-sonority slice** (L2), never the metric beat

**In plain words.** The smallest thing analysed is a stretch during which exactly the same notes are sounding - not a beat of the bar.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:747`

**Provenance.** ARCHITECTURE.md:744-751. The joint estimator's own unit is the ONSET event (jointdecoder.h:67), not this slice - see OPEN_ITEMS OI-228

### D-024 — The fact layers are style-agnostic; style lives only in calibration

> L1 (notes) and L2 (slicing) are **style-agnostic and
>   lossless** — they carry facts, never style. Style-specificity lives **only** in the *calibration* of the judgment
>   layers (their priors/weights), **never in structure**.

**In plain words.** Reading the notes and cutting the music into constant-sound stretches works the same for every kind of music. Whether a piece is Baroque or jazz can change only the numbers the judging layers use, never the shape of the code.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:753-756`

**Provenance.** ARCHITECTURE.md:744 ratified banner; sharpens §2.1 (D-070)

### D-025 — Forward-only, with two scoped escapes

> The **ratified** architecture (user-ratified;
> `cowork_target_architecture.md` §2) is **forward-only**:

**In plain words.** Each stage was to pass its answer forward and never reach back. A confident earlier answer could be overturned only by re-running that one stretch forwards, and the one genuinely tangled key-versus-chord case got a narrow, gated exception.

**Status.** SUPERSEDED IN FACT · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:726-727`

**Provenance.** The 2026-07-17 governing decision (D-001) replaces the mechanism with ONE joint decode - the mechanism this block had ruled out. No supersession banner was added to §2.14 - see OPEN_ITEMS OI-234

### D-026 — The global joint-lattice decode was measured inert (2026-06-29)

> The subsequent investigation
> **measured the full joint cross-layer search INERT**

**In plain words.** An earlier plan to search all the possibilities at once was tested and found to add nothing, so the effort was redirected into better evidence flowing forwards.

**Status.** SUPERSEDED IN FACT · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:723-724`

**Provenance.** The joint estimator (D-001) is a global joint decode and is in production on both surfaces. The record does not state how this measurement was reconciled with the later ruling - see OPEN_ITEMS OI-234

### D-027 — Every layer emits ranked candidates plus a confidence, never a forced point estimate

> each layer is feed-forward and emits **ranked candidates + a confidence**, never a forced point estimate;

**In plain words.** No stage is allowed to report only its single best answer. It reports the runners-up too, with a measure of how clear-cut the choice was.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:728`

**Provenance.** The mechanism around it (D-025) is superseded in fact, but the ranked-alternatives requirement is carried forward by the joint estimator's published candidate lists (D-006)

### D-028 — The span typology - every layer names the span it operates on; bare 'region' is banned

> "Region" unqualified is **banned** as
>   ambiguous; every layer names the span it operates on.

**In plain words.** The word 'region' on its own is forbidden, because it hides which kind of stretch is meant. Each stretch has its own name: the chord-span, the key-span, the punctuation-span and so on.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:786-787`

**Provenance.** ARCHITECTURE.md:765-772 records the rename CONFIRMED (user, 2026-07-02) and EXECUTED 2026-07-03 'propagated through every layer spec'. ARCHITECTURE.md itself still uses the banned word 216 times including section headings - see OPEN_ITEMS OI-233

### D-029 — The verifiability contract

> prefer what we can verify against ground truth (it is how we catch our own theory
>   errors); for sound theory we cannot verify against the current corpus, build it with an explicit
>   **alternative-confidence path** *and* an **"empirically-unvalidated" mark**, rather than refusing it

**In plain words.** Prefer what we can check against annotated music. Where the theory is sound but we have nothing to check it against, build it anyway - but mark it as unchecked and give it its own confidence path.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:794-796`

**Provenance.** ARCHITECTURE.md:744 ratified banner

### D-030 — Bounded context - cost scales with the working span, not the whole score

> The binding scale requirements: **(R1)** cost scales with the working span, not the whole
>   score; **(R2)**
>   re-analysis is incremental over the dirty span plus a bounded margin; **(R3)** the working span is **extensible**

**In plain words.** Analysis runs on what the user has selected. The work must grow with the size of that selection, not with the size of the piece; re-analysis after an edit must only redo the changed part; and a layer that needs more music asks for it rather than reading everything.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:800-802`

**Provenance.** ARCHITECTURE.md:802-806 names cowork_bounded_context_design.md as the ONE detailed cross-layer spec and records the 2026-07-02 user directive making it 'the hard gate before L6'. DIRECTLY CONTRADICTED by D-011 (whole-score decode per query, no caching) - see OPEN_ITEMS OI-210/OI-212

### D-031 — Whole-score analysis is the degenerate case, not the design

> Whole-score analysis is the degenerate case (selection = score).

**In plain words.** Analysing the whole piece is what happens when the user has selected the whole piece. It is not the normal mode of operation.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:802`

**Provenance.** Same home as D-030. The record producer analyses the whole score regardless of the requested span (OI-212)

### D-032 — Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named

> At a **layer boundary** (any value another layer may read), a confidence is **[0,1], class-declared, with
>   its decision named**. Unbounded internal scores are permitted *inside* a layer but must be squashed at the boundary.

**In plain words.** Inside a stage, a confidence can be on any scale. The moment another stage can read it, it must be a 0-to-1 number, labelled with what kind of confidence it is and what decision it belongs to.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_confidence_contract.md:39-40`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_confidence_contract.md:3 'Status: RATIFIED (user, 2026-07-02)'. ARCHITECTURE.md:762 still calls it 'ratification-gated' - a stale status at the canonical home (OPEN_ITEMS OI-232, item 5). Contradicted by D-019 on the production record arm - see OPEN_ITEMS OI-231

### D-033 — Each layer owns one evidence-source-times-question contribution and uses all of L1's information

> each layer owns one *(evidence-source × question)*
>   contribution — stated as "owns the *[named evidence]* contribution to *X*", with what it does **not** own made
>   explicit — defers what needs later evidence (carried as ranked alternatives + an uncertain mark), and within its scope
>   uses *all* the information L1 carries losslessly (notated spelling, metric weight, voice).

**In plain words.** Each stage owns one contribution and says plainly what it does not own, handing unresolved cases forward as ranked options. Owning one contribution does not narrow what it may look at: within its scope it uses all the information the note reader carries - how the note is spelt, where it falls in the bar, and which voice it is in.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:807-810`

**Provenance.** ARCHITECTURE.md:744 ratified banner. The joint emission reads only struck notes (OI-228) and the shared tone surface is voice-blind (OI-74)

### D-034 — A new layer or axis is admitted only through three co-equal gates

> **A new layer or axis is admitted only when it clears three co-equal gates,
>   all required:**

**In plain words.** A new stage is added only if it carries one distinct responsibility, can be validated somehow, and buys something we can actually check. Carrying a distinct responsibility is enough on its own, even with no immediate accuracy gain.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:824-825`

**Provenance.** ARCHITECTURE.md:824-831

### D-035 — The effort setting - every cost-driving choice is a setting, never a hardcoded constant

> **(a)** every cost-driving choice is an
> explicit *setting*, never a hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off
> stage.

**In plain words.** Anything that makes the analysis slower must be something the user or the caller can turn down, not a number baked into the code; and any expensive extra step must be separable so it can be switched off.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:739-741`

**Provenance.** ARCHITECTURE.md:737-741. Not implemented: the effort setting does not exist and the decode's cost drivers (segment cap, key prune width) are compiled-in constants - tracked at OI-209/OI-210

### D-036 — Accumulating gates are a warning sign - add iteration, not more gates

> When a feedforward layer acquires many gates
> and guards to compensate for missing upstream feedback, that is a symptom of missing
> iteration — not a sign that the layer needs more gates.

**In plain words.** If a stage keeps needing new special cases, the problem is that it is missing information from elsewhere. Adding another special case makes it worse.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:657-659`

**Provenance.** ARCHITECTURE.md:657-661; restated as an ongoing concern at :2131-2136

### D-099 — Negative evidence is information - a ruled-out possibility is carried, not dropped

> Negative/exclusion evidence is information ("finding by exclusion") —
>    carry a ruled-out possibility at low confidence rather than dropping it, unless the exclusion is
>    recomputable from what is kept.

**In plain words.** Knowing that something is not the case is itself useful. A reading that has been ruled out is kept at low confidence rather than thrown away, unless we could work out the exclusion again from what we did keep.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** CLAUDE.md guiding principle #12, ratified 2026-07-06. NOT recorded in any ARCHITECTURE.md layer specification, though it governs every layer's output surface - see OPEN_ITEMS OI-237

### D-100 — Every derived fact is published exactly once, on the producing layer's output surface

> every derived analytical fact is **published exactly once, on the producing layer's output surface;
> consumers read, never re-derive.**

**In plain words.** Whatever a stage works out, it publishes on its own output surface; every later stage reads that instead of working it out again. Facts that are hints a later stage might one day use are published broadly even when nothing reads them yet, each carrying whether it has been established, because a consumer may not rely on an unestablished fact. What to do with a fact nobody reads is decided case by case: keep it with a named future reader stated, or remove it - and a reader outside the analysis counts.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** CLAUDE.md 'Fact-publication corollary to #6/#7/#12', ratified 2026-07-10, amended 2026-07-12 (publish EVIDENCE-class facts broadly, each carrying its establishment status). NOT recorded in any ARCHITECTURE.md layer specification - see OPEN_ITEMS OI-237

### D-115 — The regression stop is the granularity-robust unit; root governs, key and Roman numeral ride beside

> the **class-(b) (pitch-class-decidable-root) root-disagree DURATION
>   must be NON-INCREASING** vs the committed reference — the *meaningful* functional errors never grow.

**In plain words.** A change is allowed to ship only if the total amount of music on which we name the wrong chord root - counted where the root is decidable at all - does not grow. The key and the Roman numeral are watched alongside but do not govern.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** CLAUDE.md gate block (A), ratified R10-b 2026-07-06; supersedes the batch case-identity stop preserved as block (C)

---

## D. Layer 1 — the note model

### D-037 — The note model is the single source of truth for what sounds, and reads the score once

> **The lossless, tie-resolved NOTE MODEL — the single source of truth for "what sounds."** `NoteModel::build(score)` reads the score **once**

**In plain words.** One component reads the score and works out which notes are sounding when. Everything else asks it, and nothing else reads the score.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1008`

**Provenance.** ARCHITECTURE.md:997-1008 (Layer 1 - Built+Live)

### D-038 — Tied notes are one event; spans are answered by overlap with no horizon

> Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/`lastTiedNote`/`playTicksFraction`); spans are true `[onset,release)` answered by **overlap with no horizon** (the old 4-whole-note backward cap is gone).

**In plain words.** A note tied across a barline counts once, starting where it was struck and ending where it stops. Asking what is sounding at a moment looks back as far as needed, with no arbitrary cut-off.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1008`

**Provenance.** ARCHITECTURE.md:1008; the behaviour change it caused is the ratified trade-off at :1026-1032

### D-039 — Ineligible notes are kept and flagged, never dropped

> Grace / non-playing / invisible / staff-ineligible notes are **kept and flagged, never dropped**.

**In plain words.** Notes that should not drive the analysis - grace notes, hidden notes, notes on a non-musical staff - are still recorded, marked as such. Nothing is thrown away.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1008`

**Provenance.** ARCHITECTURE.md:1008; the standing no-information-loss principle is CLAUDE.md #12

### D-040 — The tie-unresolved atoms are republished additively for the joint estimator

> `notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata` flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent`

**In plain words.** As well as merging tied notes, the note reader also publishes them separately, each with a marker saying it is a continuation. The joint estimator needs both views.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1008`

**Provenance.** ARCHITECTURE.md:1008 records it as 'Purely additive' under the OI-180 dual-path sanction

---

## E. Layer 2 — the slicer

### D-041 — The slicer output covers the domain with no gaps and no overlaps

> returns an ordered, **covering, lossless** list of half-open `[start,end)` spans that **tile the domain with no gaps and no overlaps**

**In plain words.** The music is cut into consecutive stretches that between them account for every moment exactly once.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1045`

**Provenance.** ARCHITECTURE.md:1035-1045 (Layer 2 - Built+Live)

### D-042 — Slice boundaries are every onset AND every release

> Boundaries = the sorted-unique union of every **onset AND every release** of the **eligible** notes; consecutive boundaries form the slices.

**In plain words.** A new stretch begins whenever any note starts and also whenever any note stops - because a note ending changes what is sounding just as much as a note beginning.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1045`

**Provenance.** ARCHITECTURE.md:1045. Cited by open_items/OI-228 as the primary source the joint emission departs from

### D-043 — Slice identity IS the eligible sounding-note set

> **Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC set — a
> unison/octave shrink is a real boundary though the PC set is unchanged).

**In plain words.** What makes one stretch different from the next is the exact set of notes sounding through it - not merely which pitch names are present. Two voices collapsing onto the same note is a real change even though no pitch name was lost.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1052-1053`

**Provenance.** ARCHITECTURE.md:1052-1053. The joint decoder's per-event note set is ONSET-only (jointdecoder.h:67) - open_items/OI-228

### D-044 — A note that opens no boundary still rides along in the slice's sounding set

> A muted / invisible / non-tonal-staff note opens
> **no** boundary, yet still rides along in each slice's `overlapping()` set (passed through, not
> dropped).

**In plain words.** A note that is not allowed to create a new stretch is still recorded as sounding during the stretches it spans.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1049-1051`

**Provenance.** ARCHITECTURE.md:1047-1053

### D-045 — The slicer re-decides nothing about eligibility

> **Boundaries over layer-1's eligibility annotation — never re-decided.**

**In plain words.** Whether a note counts was settled by the note reader. The slicer reads that decision and does not second-guess it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1047`

**Provenance.** ARCHITECTURE.md:1047-1049

### D-046 — Zero interpretation - the slicer applies no thresholds and no musical judgment

> **Zero interpretation.** No thresholds, min-gap, merge, or snapping; no notion of
> "ornamental/passing/structural".

**In plain words.** The cutting-up step makes no musical decisions at all. It does not decide that a note is ornamental, does not merge short stretches, and has no adjustable numbers.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1072-1074`

**Provenance.** ARCHITECTURE.md:1072-1080

### D-047 — No special-casing of any note kind

> **No special-casing of any note kind** — grace and tuplet
> outcomes fall out of the note-model spans as facts

**In plain words.** Grace notes and tuplets need no special code. Their timing is a fact the note reader already carries, and the right answer falls out of it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1073-1075`

**Provenance.** ARCHITECTURE.md:1072-1077

### D-048 — Boundaries are necessary but not sufficient; over-grab is structurally impossible

> Boundaries are **necessary but not sufficient** for
> a chord change (the exhaustive candidate grid): a real chord change can never be missed
> (over-grab is structurally impossible), and the slicer never asserts a change

**In plain words.** Every place a chord could change is offered as a candidate, so no real chord change can be missed. Whether a candidate is a real change is decided later, by a stage that judges harmony.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1077-1079`

**Provenance.** ARCHITECTURE.md:1077-1080

### D-049 — An interior stretch where everything rests is an explicit empty slice, not a gap

> An interior span where all eligible voices rest is an **explicit
> EMPTY slice** (empty eligible overlap set), not a gap

**In plain words.** Silence in the middle of the music is recorded as a stretch with nothing in it, rather than as a hole in the coverage.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1063-1065`

**Provenance.** ARCHITECTURE.md:1055-1066

### D-050 — Slicing is clipped to the loaded span and never drags outside it

> slicing never drags outside the loaded span

**In plain words.** The slicer cuts only within the span it was handed: a note sounding across the edge of that span is cut at the edge, and the slicer never reaches outside it. Widening what is analysed is the orchestration's job, not the slicer's, and re-slicing a wider span must reproduce the narrower one exactly - which is what makes widening safe.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1060`

**Provenance.** ARCHITECTURE.md:1055-1062; cites cowork_layer2_reslice_design.md §2

---

## F. Layer 3 — key and mode

### D-051 — The production key/mode path is the sequence decoder, not the per-stretch resolver

> **The production region key/mode path is the decoder, not the per-region resolver.**

**In plain words.** The tonality is worked out for the whole piece at once, as a sequence, rather than separately for each stretch.

**Status.** SUPERSEDED BY D-001 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1094`

**Provenance.** The joint estimator now decides key on both surfaces (D-005, D-010). The Layer-3 section still reads 'Built+Live' - see OPEN_ITEMS OI-232

### D-052 — The signature read and declared-mode mapping live in ONE shared function

> The signature read + declared-mode
> mapping + declared-gated Baroque `partialSignatureCorrection` was lifted verbatim into a shared
> public `resolveKeySignatureContext`, **called by both** the resolver and the wiring — so no
> signature/partial-correction logic is duplicated.

**In plain words.** Reading the printed key signature and turning it into a starting assumption happens in one place that both callers use, so the two cannot drift apart.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1116-1119`

**Provenance.** ARCHITECTURE.md:1114-1119

### D-053 — The tick-local path keeps the older resolver (the ratified P4-defer)

> **P4 tick-local still uses `resolveKeyAndModeRanked` + `collectPitchContext`** (the ratified
>   P4-defer).

**In plain words.** One narrow fallback - answering about a single moment when no surrounding stretch is available - still uses the older method. That was a deliberate deferral.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1130-1131`

**Provenance.** On the switched build the note-seam funnel returns from the record arm before this fallback is reachable (notationcomposingbridge.cpp:728-738). The D-P4 revisit trigger (D-063) was never discharged

### D-054 — All 21 modes are scored against all 12 tonics; the harmonic major family is deferred

> Harmonic major modes are
> significantly rarer as tonal centers than melodic and harmonic minor modes, and the
> validation corpus is unlikely to calibrate them well.

**In plain words.** The key finder considers 21 scale types on each of the 12 possible tonics. The harmonic major family was left out because it is rare and we have no annotated music to calibrate it against.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2214-2216`

**Provenance.** ARCHITECTURE.md:2148-2149 (21 modes), :2213-2217 (harmonic major deferred)

### D-055 — The 21 mode priors are independent and user-configurable

> **21 independent additive priors**, one per mode, user-configurable
>   via `IComposingAnalysisConfiguration::modePrior{ModeName}()`

**In plain words.** How likely each scale type is considered to be is a separate adjustable number per scale type, exposed in the preferences.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2162-2163`

**Provenance.** ARCHITECTURE.md:2162-2164, :3020-3073. Superseded on the production path by D-003 (inference is preset-independent)

### D-056 — Notes always win - the notated key signature is a weak hint, not a bypass

> The key/mode inferrer always runs. The notated key signature's `KeyMode` enum
> (`MAJOR`, `MINOR`, etc.) is no longer a bypass gate — it is passed as a weak hint
> (`declaredMode`) to `analyzeKeyMode()`

**In plain words.** The key printed at the start of the score does not settle the question. It only nudges the answer; what the notes actually do decides.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3120-3122`

**Provenance.** ARCHITECTURE.md:3118-3130

### D-057 — The priority of evidence - actual sounding notes are the strongest evidence

> | Strongest | Actual sounding notes | what is literally happening now |

**In plain words.** In deciding the key, what is actually sounding right now outranks the surrounding bars, which outrank the printed key signature, which outranks the major/minor tag on it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3138`

**Provenance.** ARCHITECTURE.md:3134-3141. Cited by open_items/OI-228 as the primary source the joint emission departs from. NOT catchable by the harvest's signature net - the reason this adjudication had to read the specifications in full

### D-058 — The piece-start shortcut

> when the
> analysis tick is within the first 16 quarter-note beats (a separate constant from the 16-beat lookback window below —
> they coincide in value, not by design), no prior result exists (`prevResult == nullptr`),
> and the key signature carries an explicit mode, the function returns the declared mode
> immediately (confidence 0.5) rather than waiting for pitch evidence that cannot yet exist.

**In plain words.** At the very start of a piece there is not yet enough music to judge the key, so if the score declares major or minor the program simply believes it, marked as a middling-confidence answer.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3125-3129`

**Provenance.** ARCHITECTURE.md:3125-3130 calls it 'a deliberate pragmatic choice for the score opening, not a general bypass'. NOT catchable by the harvest's signature net

### D-059 — The temporal window - 16 beats back, 8 beats forward, decayed

> The bridge uses a 16-beat lookback + 8-beat lookahead window:

**In plain words.** To judge the key at a point, the program looks about four bars back and two bars forward, giving less weight to music further away.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3163`

**Provenance.** ARCHITECTURE.md:3161-3173; legacy-arm only since the switch (D-010). Derivation not recorded: the only stated basis for 16 and 8 is the in-code gloss '~4 measures in 4/4' / '~2 measures ahead' (ARCHITECTURE.md:3166-3167) - no theory citation and no measurement

---

## G. Layer 4 — chord identity

### D-060 — The legacy chord analyzer is a vertical sonority analyzer - keep the boundary clean

> Do not
> attempt to improve corpus agreement by adding heuristics to `RuleBasedChordAnalyzer`
> that embed contextual assumptions — keep the vertical/contextual boundary clean.

**In plain words.** The chord identifier is meant to say what chord the notes sounding at one moment spell, and nothing more. Improving its score by teaching it about what came before or after was explicitly forbidden.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1877-1879`

**Provenance.** ARCHITECTURE.md:1853-1879. Contradicted by the same document's §4.1b/§4.1d contextual bonuses, which score a candidate from the neighbouring chords - see OPEN_ITEMS OI-235

### D-061 — Gate thresholds are Baroque-calibrated and must not be loosened for other styles

> They must not be
> loosened to accommodate other styles. When a gate causes regressions in a non-Baroque
> preset, the fix is either (a) a tighter structural entry condition that excludes the
> problematic chord type in all styles, or (b) a preset-specific threshold value

**In plain words.** The adjustable cut-offs in the chord scorer were tuned on Baroque music. If they misbehave on other music, tighten the entry condition for everyone or give that style its own value - never widen the Baroque one.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1575-1579`

**Provenance.** ARCHITECTURE.md:1573-1581; the same policy is in CLAUDE.md 'Gate threshold and preset policy'

### D-062 — Progression signals are withheld while segmentation is being explored

> the progression signals are withheld
> during `greedyExpandSegmentation`'s internal boundary-exploration calls, which run in
> `ScoringPhase::Segmentation` — prevents the bonus from biasing segmentation
> before the final per-region pass

**In plain words.** While the program is still deciding where one chord ends and the next begins, the bonuses that reward a chord for fitting its neighbours are switched off, so that the answer does not bias the question.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1776-1779`

**Provenance.** ARCHITECTURE.md:1776-1779, :1816-1822; the residual coupling is recorded as debt at :2105-2112

### D-063 — Cold context on the tick-local path is the accepted contract

> Cold context on P4 is the **current contract**, documented and accepted (the same
> precedent as the Stage 2.3 diagnose context banner: a path may legitimately analyze with less
> context, provided that is stated, not silent).

**In plain words.** One narrow path analyses a moment without knowing what came before. That is allowed because it is written down, not hidden.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1293-1295`

**Provenance.** ARCHITECTURE.md:1284-1301. Its revisit trigger - 'Stage 3 design must state explicitly what P4 (and the bridge) consume from the decode' (:1299-1300) - has not been discharged by the joint/record design

### D-064 — The chord-scoring presets are a measurement-only artifact

> The
> chord-scoring preset system is currently a **measurement-only artifact** of `batch_analyze`. Do
> **not** silently flip the live product onto preset chordPrefs

**In plain words.** The Baroque and Jazz chord-scoring settings exist only in the measurement tool. The program the user runs has never used them, and switching it over would be a product decision, not a code tidy-up.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1356-1359`

**Provenance.** D-003 makes inference preset-independent on the production path, so the divergence this decision manages no longer exists there; it still describes the legacy path

### D-065 — The look-ahead divergence between the two paths is intentional and load-bearing

> **D1 — `excludeLookAheadOnDenseStart`** is **intentionally divergent and load-bearing.**

**In plain words.** One setting deliberately differs between the measurement tool and the program, because making them the same made the program worse on a specific repertoire.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1263`

**Provenance.** ARCHITECTURE.md:1263-1266, restated at :1363-1366

### D-066 — Chord symbols written in the score are never analyzer input

> chord symbols must never be used as analyzer input in
> production because they are user content and may be incorrect.

**In plain words.** The chord names already written in a score are the user's own text and may be wrong. The analysis reads only the notes, the key signature and the settings.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2301-2302`

**Provenance.** ARCHITECTURE.md:2300-2302, restated as the retirement rationale's 'Core principle' at :2335-2337

### D-067 — Jazz mode (chord-symbol-driven boundaries) is retired

> **Status: Retired** — production analysis paths in commit 02e3733afb, tool-side surfaces in 69716deead. Chord symbols are no longer read by any analysis or tool path.

**In plain words.** The separate jazz analysis mode that took its stretch boundaries from written chord symbols has been removed entirely.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2269`

**Provenance.** ARCHITECTURE.md:2269, retirement rationale at :2324-2339

### D-068 — The chord identifier needs at least three distinct pitch classes

> Minimum 3 distinct pitch classes required. Returns empty vector if insufficient data.

**In plain words.** With fewer than three different pitch names sounding, the chord identifier declines to answer rather than guessing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1605`

**Provenance.** ARCHITECTURE.md:1605

### D-069 — Two identity modes for merged stretches - harmonic summary and as-written

> **Harmonic summary mode** (status bar, analysis, tuning): region identity = root pitch
> class + quality.

**In plain words.** When neighbouring stretches are merged, they count as the same chord if the root and the major/minor character match. A second mode that would also require the exact voicing to match is designed but not built.

**Status.** DEFERRED · decided 2026-04-11 · ratifier not stated

**Home.** `ARCHITECTURE.md:1726-1727`

**Provenance.** ARCHITECTURE.md:1722 'Region identity modes (decided 2026-04-11)'; :1734-1736 records as-written mode deferred

### D-101 — Contextual inversion bonuses fire only for major and minor candidates

> Bonuses never fire for
> Diminished, HalfDiminished, Augmented, or Suspended candidates — only Major and Minor.

**In plain words.** The bonuses that let a neighbouring chord tip an inversion reading were restricted to plain major and minor chords, after three earlier attempts without that restriction all made things worse.

**Status.** SUPERSEDED BY D-102 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1643-1644`

**Provenance.** ARCHITECTURE.md:1931-1939 records Iter 46 extending the same helpers to Augmented and HalfDiminished. The §4.1b statement carries no supersession note - see OPEN_ITEMS OI-236

### D-102 — Augmented and half-diminished candidates receive the inversion bonuses too (Iter 46)

> Extending these gates put Augmented and
> HalfDiminished inversion candidates on equal footing with Major/Minor.

**In plain words.** The restriction above was later relaxed for augmented and half-diminished chords, because without the bonuses their correct inverted readings never reached the shortlist at all. It was the single largest improvement of that iteration path.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1938-1939`

**Provenance.** ARCHITECTURE.md:1929-1942 (Iter 46, commit 36bf4738a8)

### D-103 — Pedal-point detection is a second pass, accepted only on two conditions

> **Pass 2** is triggered only when the Pass 1 bass PC is NOT a chord tone of the
> winner.

**In plain words.** When the lowest note does not belong to the chord the upper voices spell, the program re-analyses without it. It accepts that reading only if the upper voices give at least two different pitch names and the answer is clearly better than the next different-rooted one.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3630-3631`

**Provenance.** ARCHITECTURE.md:3613-3643 'Status: Implemented (Session 18, master fb9a27ce9a)'. Suspended on the record arm - see D-021

### D-104 — The bass-is-root bonus is conditioned on corroborating support

> `bassNoteRootBonus` is now conditioned on corroborating root-position support in the
> accumulated tones:

**In plain words.** Being the lowest note no longer counts as strong evidence of being the chord's root unless the chord above actually supports that reading. Without a third or fifth above it, the bonus almost vanishes.

**Status.** LIVE · decided 2026-04-09 · ratifier not stated

**Home.** `ARCHITECTURE.md:3423-3424`

**Provenance.** ARCHITECTURE.md:3400-3448; the failure it fixed is documented across four corpora at :3406-3419

### D-105 — The spelling written in the score is read through ONE shared interpreter

> read through the **shared** `engravingbridge::lineOfFifths` primitive (the Layer-1.5 spelling
>   view) — one interpreter, not a per-layer tpc copy.

**In plain words.** How a note is spelt on the page - F sharp versus G flat - is interpreted in one shared place, not re-implemented by each stage that needs it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1173-1174`

**Provenance.** ARCHITECTURE.md:1171-1174. ARCHITECTURE.md:1182-1186 records the unification residual: the legacy scorer still carries its own second reader until the legacy path retires

---

## H. Layer 5 and Layer 6 — function, cadence, grouping

### D-079 — The function layer annotates and resolves; it never rewrites the committed chord

> additive over L4 (it annotates and resolves; it never
> rewrites the committed chord identity)

**In plain words.** The stage that works out a chord's role in the key may label it and settle open questions, but it may not change which chord was identified.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1195-1196`

**Provenance.** ARCHITECTURE.md:1192-1201 (Layer 5 - Built+Dormant, design ratified)

### D-080 — Carried abstentions are resolved by selecting among the carried readings, never re-derived

> the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived)

**In plain words.** Where the chord stage could not decide, the function stage picks from the options it was handed. It does not work the chord out again from the notes.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1199-1200`

**Provenance.** ARCHITECTURE.md:1192-1201

### D-081 — The cadence detector is key-agnostic

> The cadence
> detector is **key-agnostic** (it votes for the key; it does not read a resolved key).

**In plain words.** The part that spots cadences must not be told what key it is in - it is one of the things that decides the key, so reading the answer first would be circular.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1199-1200`

**Provenance.** ARCHITECTURE.md:1200. open_items/OI-166 records that the built detector is key-agnostic but CHORD-derived, not the bass-driven pre-scan specified

### D-082 — The grouping layer is additive, read-only, with no feedback

> additive, read-only, no feedback into L5.

**In plain words.** The stage that assembles phrases and key areas only organises what earlier stages decided. It never changes their answers.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1207`

**Provenance.** ARCHITECTURE.md:1203-1210 (Layer 6 - Design-only, v1 spec)

### D-083 — Hierarchy, periods and prolongation are out of the validatable core

> Hierarchy,
> periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15).

**In plain words.** Deeper structural theory - nested hierarchy, periods, prolongation - is deliberately left out, because we have no annotated music to check it against.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1208-1209`

**Provenance.** ARCHITECTURE.md:1203-1210, deriving from D-029

### D-084 — The progression-schema recognizer is a consumer of the function layer, not a new layer

> an L5 *consumer* (a prior + an annotation), not a new layer

**In plain words.** Recognising well-known chord patterns is something that reads the finished analysis and annotates it. It is not another stage in the chain.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1214`

**Provenance.** ARCHITECTURE.md:1212-1217 'Scaffolding-first, deferred'

### D-085 — The voice-leading axis is a separate axis with its own layers

> the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
>   chord **voicing / arrangement** are analysed)

**In plain words.** How the individual voices move is a second, independent line of analysis alongside the harmonic one, with its own stages.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Home.** `ARCHITECTURE.md:817-818`

**Provenance.** ARCHITECTURE.md:818-821 records the foundation BUILT (dormant). ARCHITECTURE.md:1218-1219 still says the voice-leading layer is 'not built' - see OPEN_ITEMS OI-232

---

## I. Module boundaries and code structure

### D-070 — Style behaviour is fully data-driven - no conditional logic on style identity

> The C++ implementation contains no conditional logic based on style identity. All
> behavioral differences between musical styles are expressed as parameter values in
> style JSON files.

**In plain words.** Nowhere does the code ask 'is this jazz?'. Differences between styles are numbers in a settings file.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:388-390`

**Provenance.** ARCHITECTURE.md:381-384 states the §2 principles are 'hard constraints, not guidelines'; restated at §2.4 :435-438

### D-071 — The analysis layer never produces display strings

> Analysis components produce structured data — they never produce display strings.
> Formatting is handled by separate formatter classes.

**In plain words.** The analysis returns facts. Turning those facts into text on screen is somebody else's job.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:431-432`

**Provenance.** ARCHITECTURE.md:429-433; mechanically guarded for the joint module by D-017

### D-072 — The dependency rule - the analysis library knows nothing about the score format

> This dependency order is **enforced**. Any code that would invert it (e.g. a composing header forward-declaring `mu::engraving::Note`) must be moved to the notation bridge layer.

**In plain words.** The music-theory library must not know how MuseScore stores a score. Anything that needs both lives in a thin bridge layer in between.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:955`

**Provenance.** ARCHITECTURE.md:941-972, checklist at :1424-1431

### D-073 — Single implementation for shared logic; mirroring is a last resort

> Any algorithm that must produce identical results in both the notation bridge and
> `batch_analyze` belongs in the `composing` module (`src/composing/`), not in either
> consumer.

**In plain words.** If the program and the measurement tool must agree, the code that makes them agree lives in one shared place. Copying it into both is a last resort that must be flagged as debt.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:484-486`

**Provenance.** ARCHITECTURE.md:482-515; the standing project-wide form is CLAUDE.md #6 (total unification)

### D-074 — Analyze and suggest - never modify the score without explicit user action

> The system presents analytical findings and suggestions. It never modifies the main score
> automatically. All score modifications require explicit user action.

**In plain words.** The program tells you what it thinks. It never changes your music unless you ask it to.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:475-477`

**Provenance.** ARCHITECTURE.md:473-480

### D-075 — Interface-based design for machine-learning substitutability

> Every component that may eventually be replaced or augmented by a machine learning
> model must be defined behind a pure abstract interface.

**In plain words.** Anything that might one day be replaced by a trained model is hidden behind an interface, so the replacement can be dropped in without touching everything else.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:406-407`

**Provenance.** ARCHITECTURE.md:404-427; the substitution points are listed at §14.1

### D-076 — Score inspection before diagnosis

> Claude Code does not have direct score access and must not substitute
> statistical inference for visual score inspection.

**In plain words.** When a corpus number looks odd, somebody opens the actual music and looks at it before anyone changes code or runs more statistics.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:544-545`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** ARCHITECTURE.md:517-545

### D-077 — The configuration interface is split into two narrow IoC interfaces

> The implode bridge has no business knowing about status-bar display preferences; the analysis bridge has no business knowing about chord-staff output settings.

**In plain words.** Settings are exposed through two small interfaces rather than one big one, so each component can only see the settings it actually needs.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1404`

**Provenance.** ARCHITECTURE.md:1394-1406, restated at :2967-2978

### D-078 — The cross-layer value types live in a dependency-free leaf header

> **The cross-layer value-types LEAF** — a dependency-free header (STL only; no `chord/`, `key/`, or engraving includes) holding the value types that cross the L1.5 / L3 / L4 boundaries

**In plain words.** The small data types that several stages share live in one header that depends on nothing, which removed two places where a lower stage had to include a higher one.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1238`

**Provenance.** ARCHITECTURE.md:1238-1246

### D-107 — American English throughout

> All identifiers, comments, and documentation use American English spelling.

**In plain words.** Analyzer, not analyser; color, not colour.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:442`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** ARCHITECTURE.md:440-450; restated in CLAUDE.md Conventions

### D-108 — Cross-platform by default

> All code must run on every platform officially supported by MuseScore Studio: Windows,
> macOS, and Linux.

**In plain words.** Everything must work on Windows, macOS and Linux; platform-specific code is allowed only where unavoidable and must be walled off.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:626-627`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** ARCHITECTURE.md:624-630

---

## J. Presentation and output conventions

### D-086 — Roman numerals and Nashville numbers are presentation choices, not separate analyses

> Roman numerals and Nashville numbers are **presentation choices**, not
>   separate analyses — they are alternative formatters on the same `ChordAnalysisResult`.

**In plain words.** Showing the harmony as Roman numerals or as Nashville numbers is a choice of how to display one and the same analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2994-2995`

**Provenance.** ARCHITECTURE.md:2991-2995; consistent with D-016

### D-087 — Display options live with the formatter, not with the analyzer preferences

> Display options (`Options`) live in `ChordSymbolFormatter`, not in
> `ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**In plain words.** Which spelling convention to use on screen is a formatter setting, kept away from the settings that affect the analysis itself.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2706-2707`

**Provenance.** ARCHITECTURE.md:2672-2707

### D-088 — No automatic key signature injection

> No automatic key signature
> injection is planned.

**In plain words.** The program will never add a key signature to your score by itself. It shows what it inferred in the chord staff and leaves the decision to you.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3595-3596`

**Provenance.** ARCHITECTURE.md:3588-3596; an instance of D-074

### D-089 — The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive

> - Above 0.8 — display without qualifier
> - 0.5–0.8 — append "?" to key/mode label
> - Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

**In plain words.** On the old path, a key the program is unsure of is shown with a question mark, and one it is very unsure of is not shown at all rather than shown wrongly.

**Status.** SUPERSEDED BY D-018 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3280-3282`

**Provenance.** The record arm replaces the 0.5/0.8 literals with the fitted nats constants (ARCHITECTURE.md:168-170); the literals are legacy-arm-only (sectionanalyzer.cpp::legacyKeyExposureBucket)

### D-090 — Abstention is a valid outcome - high precision before coverage

> - high precision on exposed results
> - calibrated abstention when evidence is weak

**In plain words.** The aim is not to put a label on everything. It is to be right about what we do label, and to say nothing when the evidence is thin.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3300-3301`

**Provenance.** ARCHITECTURE.md:3287-3339

### D-106 — The augmented-sixth labels are gated to the Standard and Baroque presets

> Gated to
> Standard and Baroque presets only. Jazz and Nashville presets continue to
> emit chromatic Roman numerals or chord symbols respectively.

**In plain words.** The specific Italian, French and German augmented-sixth labels are shown only under the classical presets.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3609-3611`

**Provenance.** open_items/OI-112 already records this preset-gating as stale; open_items/OI-201 records that the record arm collapses the family to a plain major triad symbol

---

## K. Documentation governance

### D-091 — ARCHITECTURE.md is the canonical architecture document and wins every disagreement

> **When any doc disagrees with
> this one, this one wins, and a new ratified decision lands here first.**

**In plain words.** Where two documents disagree about the architecture, this one is right, and a new ruling must be written into it before anywhere else.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `ARCHITECTURE.md:263-264`

**Provenance.** ARCHITECTURE.md:256-264 'Doc governance (2026-06-29) - the hierarchy'

### D-092 — A cross-cutting contract is stated once and never redefined in a layer document

> a **cross-cutting contract is stated once, here (§2.15), and never redefined in a
> layer doc**

**In plain words.** Rules that apply to every stage are written down in one place. A stage's own document may use such a rule but may not restate it in its own words.

**Status.** LIVE · decided 2026-06-29 · ratifier not stated

**Home.** `ARCHITECTURE.md:260-261`

**Provenance.** ARCHITECTURE.md:256-264

### D-093 — STATUS.md wins on current state; ARCHITECTURE.md on design

> Where a
> heading's status and STATUS.md disagree, STATUS.md wins. This section describes the **designs**.

**In plain words.** For what is built right now, read STATUS.md. For what was decided, read this document. Where they disagree about built-or-not, STATUS.md is right.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3102-3103`

**Provenance.** ARCHITECTURE.md:3101-3103, consistent with :251-254

### D-094 — Each layer carries exactly one build state

> Each layer below is tagged with exactly one build state: **Built+Live** (wired into the
> production pipeline), **Built+Dormant** (built and tested but not wired — reachable only via diagnostics, byte-identical on
> production), or **Design-only** (specified, not yet built).

**In plain words.** Every stage is labelled as live, built-but-not-connected, or designed-only - one label each, no ambiguity.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:986-988`

**Provenance.** ARCHITECTURE.md:986-989. Three layer tags and two prose statements are stale after the switch - see OPEN_ITEMS OI-232

### D-109 — The open-items register is the one home for every unresolved issue, and the index is the status of record

> this file is the complete INDEX and
> the **authoritative status surface**

**In plain words.** Every known unresolved problem has exactly one row in one file, and that row - not the longer write-up beside it - is the official statement of where it stands.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `OPEN_ITEMS.md:5-10`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:3-13; the standing rule is in CLAUDE.md 'The open-items register'

### D-110 — The decisions register records what was decided and its status - nothing else

> **The register holds WHAT WAS DECIDED, and its status. Nothing else.** The proposed
>    `conformance` field is REMOVED.

**In plain words.** This decisions register says what was decided and whether it still stands. Whether the code obeys it is tracked separately, in the open-items register, because those two things change on different clocks.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `open_items/OI-208.md:48-49`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-208.md:46-67 (SHAPE RATIFIED, three rulings)

### D-111 — A decision belongs in the owning layer's specification; the register is an index

> **A decision belongs, wherever possible, in the OWNING LAYER'S SPECIFICATION** — that layer's
>    section of `ARCHITECTURE.md` — and the register is the **index and pointer**, never a
>    substitute home.

**In plain words.** A decision about how a stage should work is written into that stage's part of the architecture document. This decisions register only points at it.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `open_items/OI-208.md:55-57`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-208.md:46-67; follows the CLAUDE.md Conventions rule of 2026-07-28

### D-112 — Never work from memory instead of documented facts

> No assertion, design, decision, dispatch or report may rest on recalled or
>   inferred content when a documented source exists. Open the primary source and cite it
>   (file:line).

**In plain words.** If a document records something, read it and quote it rather than remembering it. Being right from memory does not count, because correct memory and incorrect memory look the same until you check.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** CLAUDE.md Conventions, user-directed 2026-07-28; its founding instance is the Layer-2 note-collection reading that this adjudication's method is built to prevent

### D-113 — Music-theory words are reserved for their music-theory meaning

> Any term that coincides even slightly with music theory is used
>   ONLY in its musical sense.

**In plain words.** In this project a score is a piece of music, a key is a tonality, and a measure is a bar. Where a word is needed in its everyday computing sense, it must be qualified - candidate score, map key, measurement.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md`  ⚠ **home is not a layer specification** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** CLAUDE.md Conventions, user-directed 2026-07-28; open_items/OI-229 records the convention STANDING for new writing and the tree-wide cleanup as an unratified future work item

---

## Provenance of this register

- Adjudication: the OI-207 decision-conformance adjudication, 2026-08-01, at commit `58dea6702ac8aa9d5ef8b89244b94d587a75f7a5`.
- Backbone data: `tools/audit/decisions/backbone_decisions.json` (sha256 `433600ac00a8da2f…`).
- Harvest: `tools/audit/decisions/decision_candidates.json` (sha256 `51850440b315e6e9…`).
- Clustering: `tools/audit/decisions/decision_clusters.json` (sha256 `0615b1e61bf10332…`).
- Shape: `open_items/OI-208.md` (user-ratified 2026-07-28).
- Standing rule for keeping it current: a new ratification, shelving or falsification gets its entry in `backbone_decisions.json` — and a regenerated `DECISIONS.md` — in the same commit that records it.

