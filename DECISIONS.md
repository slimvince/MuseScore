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
> **Content RATIFIED by the user, 2026-08-02:** the 115 originally-enumerated entries with the
> user's review corrections applied, and the 113 completion-pass entries (reviewed via the
> pending-ratification reading aid). **Second ratification event, 2026-08-02:** the 23
> residual-pass entries (D-232…D-254), with two qualifications recorded in the entries
> themselves — the four intonation entries (D-244…D-247) ratified-for-now, to be reviewed when
> that held feature's implementation is revisited; and D-248 (tonicization labels deferred)
> ratified with its revisit to be PLANNED (row OI-267 — for maximum-precision inference the
> feature may be needed). **Third ratification event, 2026-08-02:** the 27 phase-1d entries
> (D-255…D-281 — D-266 and D-278 under individual rulings recorded in their entries and at their
> homes) and the four OI-270 split entries (D-282…D-285, each superseded-by its named
> successors). **Fourth ratification event, 2026-08-02:** the 14 phase-1e archive entries
> (D-286…D-299 — D-286 the Stage-3.1b shelving, the audit's founding case; D-292 under its
> individual OI-271 ruling, the constraint reaffirmed BINDING with the licence-class
> verification as the remaining action). **Fifth ratification event, 2026-08-02:** the 16
> phase-1f entries (D-300…D-315) and D-316 (the third local patch recorded with its
> upstreamable disposition, the OI-273 ruling). **Sixth ratification event, 2026-08-02:** the 26
> phase-1g entries (D-317…D-342) — D-319…D-341 directly; D-317/D-318 with rephrased plain
> restatements under the LEGACY-marking convention (an entry whose subject is the dormant
> pipeline is explicitly marked, so a ruling about soon-deleted code is never mistaken for one
> about the live solution); D-342 with the live-handling clarification. The ratification is of
> each RULE itself; homes and provenance are bookkeeping. **Seventh ratification event,
> 2026-08-02:** the 58 phase-1h entries (D-343…D-400) — D-385 with its plain restatement
> rephrased at the user's direction (the pedaled note can be in any voice, the D-207
> voice-independent class governing); D-345 under the OI-275 transfer treatment (letter
> legacy-homed and marked; D-003 governs the live estimator). **Eighth ratification event,
> 2026-08-02:** the 5 phase-1i entries (D-401…D-405), the 79-entry LEGACY-marked set confirmed
> as drawn (mechanism marked, surviving principle not), the OI-278 ruling (FQ-1 lapses with the
> legacy path; D-386's phantom second alternative struck), and the transitive-authority
> refinement of the contract-home case. The register-level ratification does not overwrite
> per-entry provenance — an entry saying "ratifier not stated" still means the original record
> of THAT decision does not say; what the 2026-08-02 ratifications establish is that these
> entries are the standing decisions of record. **Ninth ratification event, 2026-08-03:** the 9
> phase-1j entries (D-406…D-414), the four status banners behind fourteen contract-home
> re-classifications, and the OI-279 ruling that corrected `ARCHITECTURE.md` §6.7 over the five
> idioms (with the D-132 narrowing). **Tenth ratification event, 2026-08-03:** the 9 phase-1l entries
> (D-415…D-423), ratified AS DRAFTED with the statuses exactly as the record states them — and,
> recorded separately because they are separate acts, the OI-284 scope ruling on D-417 (the engage
> criteria govern engaging the dormant spine, not the joint estimator's adoption) and the OI-285
> ruling committing the ratification surfaces. **D-416's disposition was NOT written**: the check the
> ruling depended on did not confirm its premise, and the STOP is recorded in that entry's provenance
> and at `OPEN_ITEMS.md` OI-286. **Eleventh ratification event, 2026-08-04:** the 28 READ WAVE 1
> entries (D-440…D-467), ratified AS DRAFTED with the statuses exactly as the record states them —
> several of them "not stated", and left that way. What a ratification of an ENTRY settles is that
> the register records the decision correctly; it is not a judgment that the decision is good, and it
> supplies no date and no ratifier the original record never had. Two acts landed in the same commit
> and are **not** entry ratifications: **D-058** moved to *superseded in fact* (the piece-start
> shortcut — removed from the code on 2026-06-14 and specified in the present tense until this wave,
> `OPEN_ITEMS.md` OI-315), and **D-468** was entered (the pinned block-(A) instrument's declared
> inference arm, recorded but **not** user-ruled — see that entry's provenance).
> **Twelfth ratification event, 2026-08-04:** the 33 READ WAVE 2 entries (D-469…D-501), ratified AS
> DRAFTED with the statuses exactly as the record states them — several of them "not stated", and
> left that way. Two things this event is explicitly not. It is **not a conformance finding**: what
> is ratified is that the register records each decision correctly, never that the code obeys it.
> And for **D-494…D-500** it is **not a second ratification of the decision** — those entries carry
> amendments the user ratified at the 2026-07-02 architecture review, so ratifying the ENTRY records
> only that the register transcribes that event correctly, and nothing is counted twice. Landing in
> the same commit and **not** entry ratifications: **D-468**'s ratifier correction was made in the
> preceding wave, and the riders this wave's dispatch ordered — D-492 marked a phase-3 fix-plan input
> with the reachability of its subject checked at the code, and the D-474/D-475 consequences recorded
> at principle #21 and on `OPEN_ITEMS.md` OI-179.
>
> **From 2026-08-03 each entry carries its own ratification as a FIELD**, not only as prose inside
> the provenance — see *Entry ratified* below. It is backfilled mechanically from the provenance
> markers and from nowhere else; where an entry shows none, its own provenance records none, and the
> register-level events above are where to look.
>
> **GENERATED FILE — do not hand-edit.** Source of record:
> `tools/audit/decisions/backbone_decisions.json`; generator
> `tools/audit/decisions/gen_decisions_register.py`. Every number below is computed, never
> transcribed.
>
> **This file is the INDEX** (the open-items register's index-plus-detail shape, applied here
> 2026-08-02 when the one-file register outgrew rendering): one row per decision below; the FULL
> entries — verbatim quote, plain restatement, Why, status, home, provenance — are in one
> generated file per group under `decisions/`, linked from each group heading.

## How to read an entry

Each entry has six parts, and a seventh where the record states one.

- **The decision, verbatim** — quoted exactly from the document that records it, word for word.
  (Where the source wrote the passage inside a quotation block, its `>` markers are dropped so the
  entry reads cleanly; nothing else is altered.) Quoted text keeps its original wording even where
  that wording uses a word in a non-musical sense; the plain restatement beneath it does not.
- **In plain words** — one or two sentences, written for a reader who knows music but not this
  project's private vocabulary.
- **Why** — the defense the record gives for the decision: the published research or algorithm
  adopted, the measurement that decided it, or the constraint that forced it, cited to where it
  is written down. Where the record gives none, this reads **derivation not recorded** — the gap
  is stated, never filled in afterwards from memory. (Standing rule: `CLAUDE.md` Conventions,
  *every design decision carries its defense at its home*, user-directed 2026-08-01.)
- **Status** — see the table below. Where the record does not say when a decision was made or
  who ratified it, the entry says **not stated**. Nothing is inferred.
- **Entry ratified** — when this REGISTER ENTRY was reviewed and ratified, and by whom. This is a
  different event from the decision itself: a decision made in June 2026 by whoever made it can have
  its entry — the quote, the restatement, the status — ratified much later, and conflating the two
  would falsify one of them. The line appears only where the entry's own provenance records such an
  event; its absence means the provenance does not record one, not that the entry was rejected. The
  register-level ratification events are listed in the preamble above. (Field added 2026-08-03 on the
  user's ruling of that date; before it, an entry ratification could only be read out of the
  provenance prose.)
- **Home** — where the decision is actually recorded, as `file:line`. A decision about how a
  layer should work belongs in that layer's section of `ARCHITECTURE.md`, and a decision about
  anything else belongs in the specification that owns it. Where the home is neither, the entry
  says which of five cases it is: a **documentation gap** (a decision that governs a layer or a
  component, not findable from that layer's section — it carries an `OPEN_ITEMS.md` row); a
  decision **recorded only on a tracking surface** (an open-item row or a session handoff block —
  a place for tracking work, not a home for a standing decision); a **project-wide convention**
  with no owning layer, correctly homed in `CLAUDE.md` or the architectural principles; a
  **decision about the process**, not about the system; or a **ratified contract document** the
  owning `ARCHITECTURE.md` section points at, which is a proper home (the fifth case, user-ratified
  2026-08-02 at `open_items/OI-268.md` — the pointer, never a copy, is what a missing delegation
  owes).
- **Home section** — which SECTION of the home document the decision is recorded in, and whether a
  user-ratified surface delegates to that section. The user narrowed the fifth home case's unit from
  the document to the section on 2026-08-03, and the narrowing is applied **staged**: an entry carries
  this line only where section granularity decides something. Its absence means the entry has not been
  brought to section granularity yet — never that the whole document is claimed as the home. The
  section itself is derived from the home document's own headings and this entry's own cited line, and
  is re-derived by a check, so it cannot go stale when a heading moves. See *The home field's
  granularity* below.
- **Provenance** — where the status comes from, and any later ruling that bears on it.

An entry may additionally carry **⚠ LEGACY**. That means its subject is the dormant pipeline
awaiting deletion at the retirement map — a ruling about soon-deleted code, which a reader must
never mistake for one about the live solution (marking convention user-ratified 2026-08-02;
`CLAUDE.md`, the decisions-register section, rule (f)). The flag is about WHAT THE DECISION IS
ABOUT, not about how old it is: a decision that governs the live solution carries no flag however
early it was made. Where a LEGACY-marked decision's *principle* was separately transferred to the
live design by a ruling, the entry's plain restatement says so — read it before concluding the
principle lapsed with the code.

**What the mark does NOT say** (wording weakened by the user's ruling of 2026-08-03). Until that
date the mark ended *"it has no effect on the live solution"*. That was a claim about the live
system which the marking pass never checked, and it failed twice — at D-329, whose principle a
later ruling carried across to the live family design, and at D-311, whose subject produced
`chordsymbolformatter.cpp`, which the record arm runs. A swept population with two demonstrated
errors is not established (#19), so the clause was removed rather than re-argued: the mark now
states only what the decision is ABOUT. **A LEGACY mark is therefore not evidence that the marked
subject is unreachable**, and no design may put load on it as though it were. The full
re-verification of the marked set against a live-reachability test is `OPEN_ITEMS.md` OI-289.

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

**545 decisions**, grouped by subject. They were enumerated by reading `ARCHITECTURE.md` and `CLAUDE.md` in full, because a decision written as plain specification carries no ruling vocabulary and no text search can find it, and by following the recorded rulings that live only in an open-item row, a handoff block, or one of the standing decision-bearing surfaces. Every verbatim quote below is mechanically checked to exist at the place it is cited to, and to start at the line it is cited to (`gen_cluster_dispositions.py --verify`), and every `D-…` and `OI-…` cross-reference is checked to resolve.

| | Count |
|---|---|
| Decisions recorded | **545** |
| — of which live | 463 |
| — of which superseded in fact | 7 |
| — of which superseded by | 9 |
| — of which deferred | 50 |
| — of which shelved with evidence | 2 |
| Decisions whose date is not stated in the record | 225 |
| Decisions whose ratifier is not stated in the record | 311 |
| Decisions recorded outside the specification that owns them | 341 |
| — of which a documentation gap | 134 |
| — of which recorded only on a tracking surface, with no home at all | 11 |
| — of which a project-wide convention, correctly homed | 35 |
| — of which a decision about the process, correctly homed | 62 |
| Decisions whose defense the record does not state | 44 |
| Entries whose own ratification the provenance records | 248 |
| Entries whose home is recorded at SECTION granularity | 134 |

The second-to-last row is about the DECISIONS; the last is about the ENTRIES. **248 of 545** entries carry a recorded event at which the entry itself — this quote, this restatement, this status — was reviewed and ratified. The remaining 297 do not carry one in their own provenance; the register-level ratification events listed in the preamble are the place to look for those, and nothing is inferred from them into the per-entry field.

That last row is the one meant to fall. **501 of 545** decisions here can point at the research, the measurement, or the constraint that decided them; the rest cannot, and say so. Filling a gap means recording the defense where the decision lives — never writing one afterwards from memory.

Alongside the register, every one of the harvested statements about decisions in this repository has been given a recorded disposition, so that none was silently passed over:

| | Count |
|---|---|
| Harvested statements | **15224** |
| Groups of near-identical statements ("clusters") | **14460** |
| Clusters carrying a recorded disposition | **14460** |
| — restates | 5515 |
| — not-a-decision | 5552 |
| — boilerplate | 74 |
| — no-spec-home | 651 |
| — unresolved | 2668 |

The full disposition table, and the numbered rule behind each one, are in `tools/audit/decisions/cluster_dispositions.csv` and `tools/audit/decisions/disposition_manifest.json`.

### The home field's granularity, and what sets a home class

THE HOME CLASS OF EVERY NON-SPECIFICATION ENTRY IS SET BY ONE PASS, and the field records the SECTION the entry sits in wherever the home-class criteria reach it. From 2026-08-03 (phase 1q) the three criteria in force are applied together to the whole home population: clause (a), the fifth home case (a user-ratified surface must delegate to the home at all); D-432, the delegation bar (which wordings delegate); and D-430, the section-level unit (the delegation must reach the SECTION the entry sits in, and that section must state rules rather than record findings). Every entry whose class is `contract-home` or `gap` therefore carries a `home_section` block naming its section, the criterion that decided it, and the class it carried before this pass — and, where phase 1n's staged application had already moved it, the class it carried before that (#12: neither movement is lost). Entries classed `process`, `project-convention` or `unhomed`, and every entry homed in a layer specification, carry no section block: the criteria do not reach them. The section is DERIVED from the home document's own headings and the entry's own cited line by tools/audit/decisions/gen_home_classification.py, whose --check re-derives it, so a heading moving inside a home document cannot leave a stale section behind. THE PRECEDING REGIME, superseded and recorded here rather than deleted: from the phase-1n ruling of the same day until phase 1q the field was deliberately MIXED — D-430 was applied to 46 entries across 5 documents, where section granularity decided something, and every other entry carried a document-level home pending the next touch. The user ended that staging on 2026-08-03 by ruling ONE re-classification pass over the whole population (`OPEN_ITEMS.md` OI-291).

> **The criterion, as ruled.** A home is a SECTION of a document. It is admitted when a user-ratified surface delegates a stated concern to that section by name, and that section states rules rather than recording findings. (User, 2026-08-03; dispatch cc_instruction_phase1n_criterion_premise_and_reading_regime.md §2.1. Register entry D-430.)
>
> **What it supersedes.** This SUBSUMES the two earlier tests rather than replacing them, and both are recorded superseded-by rather than falsified: the phase-1l DELEGATION-SPECIFICITY criterion (by name, for a stated concern, stable enough to be cited — measured at open_items/OI-281.md, note of 2026-08-03) and the phase-1m KIND test (which replaced that third clause with a test on the document's purpose — measured in the same row's second note). Each was a proxy for the section-level test, and each produced the evidence that located its own error: the specificity criterion's residue was clause (c) as a judgment, and the kind test's residue was that kind is a property of the DOCUMENT while a delegation points at a SECTION. Rule (g)'s guard is intact — the delegation confers, and only the user writes a delegation into ARCHITECTURE.md.
>
> **How a whole-document delegation is read.** A delegation that names a DOCUMENT and no section reaches EVERY section of it; a delegation that names SECTIONS reaches those sections and their subsections and no others; and the rule-stating half is judged PER SECTION in both cases. **THIS IS NOW PART OF THE RULE, NOT AN INTERPRETATION OF IT (user, 2026-08-03, phase 1r).** At phase 1q it was this pass's reading of D-430's "delegates a stated concern to that section BY NAME", taken on the record's own precedent rather than a preference — `OPEN_ITEMS.md` OI-290 states in terms that "`ARCHITECTURE.md:1331` delegates 'this layer' and admits all sixteen of that document's entries" — and the strict alternative was recorded as available to the user. The user then WROTE the reading into `CLAUDE.md` rule (h) itself as the GRANULARITY clause, so D-430's verbatim now carries it and the strict alternative is CLOSED. Its defense, stated with it: the strict reading would evict every document delegated as a whole, signed layer specifications among them, on the accident of how a pointer happens to be phrased, making the rule retroactively destructive rather than refining. THE STRICT ALTERNATIVE, PRESERVED (#12): read literally, a whole-document delegation names no section, so no section of it would be admitted and the seven whole-document homes would lose every entry between them.
>
> **Scope of application.** APPLIED IN FULL, 2026-08-03 (phase 1q, the user's ruling of that date, option A3 at `OPEN_ITEMS.md` OI-291). The staged application of phase 1n — five documents, 46 entries — is superseded: every entry of the home population carries a section home and a class derived from the criteria in force. The applier is tools/audit/decisions/gen_home_classification.py, whose --check re-derives both the classification and its artifact; it replaces gen_section_homes.py, which applied D-430 alone to the staged subset and is deleted rather than left beside it (#6). **RE-RUN 2026-08-03 (phase 1r), after the user WROTE the delegations the first run's WRITE LIST asked for (the OI-293 list).** The criteria are unchanged; what changed is the delegations they read. All six write-list documents move, two of them only in part, and the movement caused by the written delegations alone is at `phase1q_reclassification.json` -> `the_phase_1r_re_run`. Because the pass now runs twice over the same entries, each entry carries a THIRD frozen class — `class_before_phase1r`, the class it held between the two runs — so neither movement is lost (#12).

### What was read, and what was not

**Read in full.** ARCHITECTURE.md IN FULL (all 6,523 lines: the preamble, §1 Project Overview, §2 Architectural Principles, §3 Directory Structure including the Layer 1-6 specifications, §4 Existing Components, §5 Planned Analysis Extensions, §6 The Style System, §7 The Knowledge Base, §8 Planned Generation Components, §9 The Constraint System, §10 Visualization, §11 Intonation, §12 User Interface, §13 File Persistence, §14 ML Readiness, §15 Development Phases, §16 Scope Reference, §17 Coding Standards, §18 Contributing, §19 LLM Integration, and both appendices). Lines 1-3981 were read by the 2026-08-01 adjudication; §1 and §6-§19 plus the appendices by the 2026-08-01 completion pass. Also in full: CLAUDE.md (the guiding principles, the ratified corollaries, the gate and preset policy, the conventions, the local patches, the self-check). Targeted and cited: OPEN_ITEMS.md and its detail files, cowork_handoff.md, docs/scoring_model.md §8, DEFECT_TYPES.md, BUILD_AND_TEST.md, tools/REPRODUCIBILITY.md, cowork_confidence_contract.md, cowork_joint_estimator_factorization.md, cowork_design_doc_template.md.

**Not read in full.** The per-layer and per-component design documents (cowork_layer*_design.md, cowork_progression_schema_dictionary.md, cowork_voiceleading_axis_design.md, cowork_bounded_context_design.md and their siblings), which ARCHITECTURE.md §doc-governance names as the authoritative DETAIL for their own scope; both archives (STATUS_ARCHIVE.md, cowork_handoff_archive.md); and the cc_* session reports. Each was opened where a specific citation required it and is not claimed to be swept.

**The remainder, measured.** The harvest holds 15,224 candidate statements, of which 241 are sourced to ARCHITECTURE.md - all 241 now fall inside the range read in full. 6,374 clusters carry the 'unresolved' disposition: statements the pass could not mechanically classify as either restating a register decision or not being a decision. Sampling shows that residual is genuinely mixed - real rulings, deferred designs and ordinary narrative in one population - so it bounds what this register may claim about the documents it did not read in full.

*Why this is stated at all:* DEFECT_TYPES.md DT-26 — scope-assumed enumeration. A sweep that is complete inside its own file set reads as complete about the whole question. The scope and its measured remainder are therefore stated rather than left implicit.

---

## A. The estimator architecture — the joint estimator — [full entries](decisions/group_A.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-001 | Key, mode and chord are inferred by ONE joint decode | LIVE | — | `ARCHITECTURE.md` |
| D-002 | The fitted tables and weights are compiled into the binary verbatim | LIVE | — | `ARCHITECTURE.md` |
| D-003 | Inference is preset-independent; presets are presentation concerns | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-004 | The decode state space and the segment cap | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-005 | The joint estimator is the production inference layer on the batch and corpus surface | LIVE | — | `ARCHITECTURE.md` |
| D-006 | The published uncertainty surface is two full candidate lists, with no truncation | LIVE | — | `ARCHITECTURE.md` |
| D-007 | The published scores are log-scores, not probabilities | LIVE | — | `ARCHITECTURE.md` |
| D-008 | The true probabilities are deferred to a later step | DEFERRED | — | `ARCHITECTURE.md` |
| D-095 | The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state | SUPERSEDED IN FACT | — | `ARCHITECTURE.md` |
| D-096 | Fitted values are fit once against ground truth, never per-case tuned | LIVE | — | `ARCHITECTURE.md` |
| D-097 | Held-out evaluation and a capacity budget are declared before any fit | LIVE | — | `ARCHITECTURE.md` |
| D-098 | The exact-decode reserve - the declared prune was never adopted | LIVE | — | `ARCHITECTURE.md` |
| D-114 | The decoder commits its best path; there is no abstention on the key axis | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-270 | The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file | LIVE | 2026-08-02 · user | `cowork_prefit_gates.md` “The held-out evaluation protocol” |
| D-271 | The capacity budget - a cell keeps its own estimate only above a stated count, and free parameters are bounded against the training tokens | LIVE | 2026-08-02 · user | `cowork_prefit_gates.md` “The capacity budget” |
| D-272 | The protocol constants are protocol, not tuning - changing one is an amendment, never a fitting act | LIVE | 2026-08-02 · user | `cowork_prefit_gates.md` the opening block (above the first section heading) |
| D-273 | The architecture-adoption variant of the hard regression stop, written before any diff existed | LIVE | 2026-08-02 · user | `cowork_prefit_gates.md` “The robust-stop architecture-adoption protocol” |
| D-274 | The reverse map - if the new estimator is not adopted it is removed whole, and the retirement map is void | LIVE | 2026-08-02 · user | `cowork_prefit_gates.md` “The sanctioned dual path and the retirement map” |
| D-283 | Meta-finding: never learn keys, the lever is keychain structure - superseded by the joint estimator and the forms-from-theory rule | SUPERSEDED BY D-001 and D-096 | — | `cowork_architecture_reassessment.md` §4 ⚠gap |
| D-285 | Meta-finding: embellishment is chord-first, never a richer vocabulary - absorbed by the emission design and the ornament-label increment | SUPERSEDED BY the ratified factorization emission design (D-004 and the OI-194 increment) | — | `cowork_architecture_reassessment.md` §4 ⚠gap |
| D-376 | The joint key-and-chord step was designed as a BOUNDED COUPLING over the two existing decoders, and the unified single-state alternative was REJECTED — the option later adopted as the production architecture | SHELVED WITH EVIDENCE ⚠LEGACY | 2026-08-02 · user | `cowork_joint_key_chord_design.md` “§1.1 The decision: a BOUNDED coupling step, NOT a unified `(key,chord)` hidden state” |
| D-379 | Whether an alternative tonality would change the chord CANNOT be measured without re-deciding under it — the exact coupled-case condition is not computable read-only, which is why it stayed unmeasured | LIVE | 2026-08-02 · user | `cowork_joint_key_chord_design.md` “§3.1 The trigger, grounded in C3” |
| D-449 | Factor granularity is fixed: the bass factor is evaluated per event, the missing-tone penalty per event of segment length, the emission per tone, and the boundary-family factors per boundary | LIVE | 2026-08-04 · user | `cowork_factorization_desk_simulation.md` ⚠gap |
| D-450 | The key-signature and declared-mode prior conditions the INITIAL key state only, re-entering only at a notated signature change | LIVE | 2026-08-04 · user | `cowork_factorization_desk_simulation.md` ⚠gap |
| D-451 | A desk simulation's table values are provisional, enter no fit, and a verdict that would flip inside a provisional value's plausible range is reported as a near-tie, never as a win | LIVE | 2026-08-04 · user | `cowork_factorization_desk_simulation.md` ⚠gap |
| D-452 | Every desk-simulation trace runs at identity weights — the ratified ablation baseline — so the trace tests the structure and the tables, not the weighting | LIVE | 2026-08-04 · user | `cowork_factorization_desk_simulation.md` ⚠gap |
| D-453 | The desk simulation's verdict: the ratified factorization passes nine of ten traces and no finding reopens the structure | LIVE | 2026-08-04 · user | `cowork_factorization_desk_simulation.md` ⚠gap |
| D-524 | The joint state's mode axis is TWO modes — major and composite minor; modal and chromatic colour lives in the pitch emission, and the un-rounded reading is published | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-525 | The fit is STAGED: the factor tables are counted from ground truth and frozen, and only a small vector of combination weights is fit discriminatively — with an all-weights-equal ablation arm that must be beaten | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-526 | The joint state's chord axis is SCALE-DEGREE-VALUED — a Roman numeral relative to the state's own tonic and mode — and the chord symbol is a DERIVED fact published once | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-527 | There is NO live non-chord-tone cleaning stage: each tone is emitted by category inside the one decode, conditioned on chord-independent melodic and metric covariates, and ornament labels are derived AFTER it | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-528 | The key signature and declared mode enter as a WEAK FITTED SOFT PRIOR with no conditional gate anywhere — the probability calculus delivers 'consult it only when unsure', and the hard declared-mode wall is formally retired | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-529 | The joint architecture's expected win is ASYMMETRIC — large on key and mode, modest on chord root — and the written predictions must say so, because a large root claim would itself be a surprise | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-530 | The joint architecture is a CONSTRAINED optimum, not a global one: the learned shared-representation models measure better and are excluded because they are un-establishable and undiagnosable | LIVE | — | `cowork_joint_estimator_architecture.md` ⚠gap |
| D-532 | The chord-transition table gains one pooling level that groups a secondary dominant's continuations by their RELATION to its target — restoring from counts the one behaviour that defines the chord class | LIVE | — | `cowork_sensitive_cell_probe.md` ⚠gap |
| D-533 | A continuation too rare to have its own stored probability is scored by dividing the row's leftover in PROPORTION to each chord's overall frequency — never evenly, and never as impossible | LIVE | — | `cowork_sensitive_cell_probe.md` ⚠gap |
| D-534 | The penalty for a chord tone that never sounds is COUNTED per chord factor — root, third, fifth, seventh — replacing one invented blanket number; the per-factor asymmetry then comes free | LIVE | — | `cowork_sensitive_cell_probe.md` ⚠gap |
| D-535 | The checking stage's verdict: the real counted tables overturn no desk-simulation verdict, but margins moved in both directions and one margin expectation was plainly wrong | LIVE | — | `cowork_sensitive_cell_probe.md` ⚠gap |

## B. The notation output surface and the record path — [full entries](decisions/group_B.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-009 | The notation record is the ONE surface the in-app path reads, and it never re-decodes | LIVE | — | `ARCHITECTURE.md` |
| D-010 | The switch - the record path is the production in-app notation analysis | LIVE | — | `ARCHITECTURE.md` |
| D-011 | The producer decodes the WHOLE score once, and does not cache | LIVE | — | `ARCHITECTURE.md` |
| D-012 | Failure is unambiguous - never a partial record, never a silent fallback | LIVE | — | `ARCHITECTURE.md` |
| D-013 | Which staves feed the analysis is decided at the fact adapter, not by a later filter | LIVE | — | `ARCHITECTURE.md` |
| D-014 | The two seams read the record as pure views - no recomputation | LIVE | — | `ARCHITECTURE.md` |
| D-015 | A boundary tick belongs to the segment it starts | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-016 | Display renderings are presentation; facts are published | LIVE | — | `ARCHITECTURE.md` |
| D-017 | The inference/presentation boundary is guarded mechanically, both ways | LIVE | — | `ARCHITECTURE.md` |
| D-018 | The key-exposure bucket is decided once, at one site | LIVE | — | `ARCHITECTURE.md` |
| D-019 | The record arm publishes the raw key-axis gap, with no remapping to 0..1 | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-020 | The interactive path bypasses the old window cache and has none of its own | LIVE | — | `ARCHITECTURE.md` |
| D-021 | The pedal-point fields are suspended on the record arm | DEFERRED | — | `ARCHITECTURE.md` |
| D-275 | Every published record carries its own instrument provenance; a provenance-less analysis cannot exist | LIVE | 2026-08-02 · user | `cowork_notation_output_contract.md` §2 |
| D-276 | Modal colour is published as un-rounded per-degree counts; no mode label is inferred or published anywhere | LIVE | 2026-08-02 · user | `cowork_notation_output_contract.md` §3.4 |
| D-425 | The uncertainty surface's contract IS the full posterior; the local slice is the first delivered step, and the completion is a named step, never an indefinite upgrade | LIVE | — | `cowork_notation_adoption_increment.md` §4 ⚠gap |
| D-426 | The modal reading lands inside the notation increment; the ornament labels get their own increment, with the tracking row created at ruling time | LIVE | — | `cowork_notation_adoption_increment.md` §7 ⚠gap |

## C. Cross-cutting analysis contracts — [full entries](decisions/group_C.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-022 | The founding principle - analyse at the finest grain, coarser views are derived | LIVE | — | `ARCHITECTURE.md` |
| D-023 | The atomic analysis unit is the constant-sonority slice, never the metric beat | LIVE | — | `ARCHITECTURE.md` |
| D-024 | The fact layers are style-agnostic; style lives only in calibration | LIVE | — | `ARCHITECTURE.md` |
| D-025 | Forward-only, with two scoped escapes | SUPERSEDED BY D-001 | — | `ARCHITECTURE.md` |
| D-026 | The global joint-lattice decode was measured inert (2026-06-29) | LIVE | — | `ARCHITECTURE.md` |
| D-027 | Every layer emits ranked candidates plus a confidence, never a forced point estimate | LIVE | — | `ARCHITECTURE.md` |
| D-028 | The span typology - every layer names the span it operates on; bare 'region' is banned | LIVE | — | `ARCHITECTURE.md` |
| D-029 | The verifiability contract | LIVE | — | `ARCHITECTURE.md` |
| D-030 | Bounded context - cost scales with the working span, not the whole score | LIVE | — | `ARCHITECTURE.md` |
| D-031 | Whole-score analysis is the degenerate case, not the design | LIVE | — | `ARCHITECTURE.md` |
| D-032 | Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named | LIVE | — | `ARCHITECTURE.md` |
| D-033 | Each layer owns one evidence-source-times-question contribution and uses all of L1's information | LIVE | — | `ARCHITECTURE.md` |
| D-034 | A new layer or axis is admitted only through three co-equal gates | LIVE | — | `ARCHITECTURE.md` |
| D-035 | The effort setting - every cost-driving choice is a setting, never a hardcoded constant | LIVE | — | `ARCHITECTURE.md` |
| D-036 | Accumulating gates are a warning sign - add iteration, not more gates | LIVE | — | `ARCHITECTURE.md` |
| D-099 | Negative evidence is information - a ruled-out possibility is carried, not dropped | LIVE | — | `ARCHITECTURE.md` |
| D-100 | Every derived fact is published exactly once, on the producing layer's output surface | LIVE | — | `ARCHITECTURE.md` |
| D-115 | The regression stop is the granularity-robust unit; root governs, key and Roman numeral ride beside | LIVE | — | `CLAUDE.md` |
| D-191 | The two-tier regression class policy - functional regression stops, rotation churn is tracked | LIVE | — | `CLAUDE.md` |
| D-210 | An exotic mode is graded against its parent collection's minor key, not its own tonic triad | LIVE | — | `CLAUDE.md` |
| D-211 | Key agreement is reported against both the global home key and the local key | LIVE | — | `CLAUDE.md` |
| D-212 | The regression stop is abstain-aware: an abstention counts as disagreement on root | LIVE | — | `CLAUDE.md` |
| D-243 | The planning band for the vertical engine, and the corpora excluded from it | SUPERSEDED IN FACT ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-260 | Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §2 |
| D-261 | A layer never guesses how much context it needs - the amount is discovered by convergence | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §3 |
| D-262 | The extension increment is chosen by the requesting layer, not by the layer that supplies the notes | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §3 |
| D-263 | A refused or truncated extension is marked on the output, never silently absorbed | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §3 |
| D-264 | Extension is an optimisation of load-more-then-rerun: any sequence of extensions equals one fresh run | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §4 |
| D-265 | Asking a lower layer for more notes is a data-supply call, not a backward inference edge | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §4 |
| D-266 | Layer 6 is prohibited until the bounded-context design is coded and regression-tested for Layers 1 to 5 | LIVE | 2026-08-02 · user | `cowork_bounded_context_design.md` §8 |
| D-267 | There are exactly two admissible confidence classes, and no layer may claim a calibrated probability until one is fitted | LIVE | 2026-08-02 · user | `cowork_confidence_contract.md` §2 |
| D-268 | A confidence attaches to a named decision, is compared only within its class and a declared frame, and keeps its identity downstream | LIVE | 2026-08-02 · user | `cowork_confidence_contract.md` §2 |
| D-269 | The frame table is the one home of the override arithmetic; a new override site declares its frame before it is built | LIVE | 2026-08-02 · user | `cowork_confidence_contract.md` §4 |
| D-278 | The joint key-and-chord step is SHELVED - measured not to pay | SHELVED WITH EVIDENCE ⚠LEGACY | 2026-08-02 · user | `cowork_engage_arc_plan.md` “The stages” |
| D-282 | Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy | SUPERSEDED BY D-115 and D-191 | — | `cowork_architecture_reassessment.md` §4 ⚠gap |
| D-286 | Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading | LIVE | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-288 | Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-289 | Meta-principle: precision lives in the evidence and the functional labelling, not in the search | LIVE | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-293 | Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-294 | The only ground truth is the human annotation; the algorithmic analysis is a filter, and no self-annotation ever enters a measurement | LIVE | 2026-08-02 · user | `CLAUDE.md` |
| D-297 | Correction of record: never computing a possibility is not information loss; only discarding a computed one is | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-313 | A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target | LIVE | 2026-08-02 · user | `cowork_stage5_fitter_design.md` §9 |
| D-339 | A confident earlier decision can be overturned by decisive later evidence, through ONE confidence-weighted forward-recompute mechanism — architecture-wide | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |
| D-377 | The forbidden back-edge, stated concretely: a chord decision may NOT write into the committed tonality and re-run the tonality decode — a coupled decision is OWNED by its own bounded box, never patched backward | LIVE | 2026-08-02 · user | `cowork_joint_key_chord_design.md` “§1.3 How it avoids re-introducing a cross-layer cycle” |
| D-422 | The jazz fit is deferred to the jazz ground-truth conversion; only the classical common-practice idiom is fitted now | DEFERRED | 2026-08-03 · user | `docs/implementation_roadmap.md` “Stage 5” ⚠gap |
| D-466 | Forward-only is a strong DEFAULT, not dogma — a backward edge is admissible only as a deliberate, surfaced, measured, documented exception | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |
| D-468 | The pinned block-(A) instrument declares which inference arm its baselines were measured on, and refuses a corpus whose stamp disagrees | LIVE | — | `CLAUDE.md` |
| D-474 | No published study reports per-axis inter-annotator agreement for Roman-numeral analysis of Baroque/classical symbolic music — the ground-truth ceiling principle #21 demands is unmeasured by the entire field | LIVE | 2026-08-04 · user | `cowork_term_theory_grounding.md` ⚠gap |
| D-475 | The BCMH chorale annotations are NOT established as an instrument: the annotator is unknown, the annotations sit on a reduction, and they reached the repository through a machine translation | LIVE | 2026-08-04 · user | `cowork_term_theory_grounding.md` ⚠gap |
| D-486 | A measurement publishes its coverage denominator and its per-corpus breakdown; a single aggregate number that hides which corpus moved is not reported | LIVE | 2026-08-04 · user | `docs/precision_metric_design.md` ⚠gap |
| D-497 | RATIFIED AMENDMENT A-7: the empirically-unvalidated mark must be APPLIED to the Jazz preset constants and the unvalidated idioms, with the validation path named | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |
| D-500 | The user ratified CORPUS EXPANSION at the architecture review: gate-grade jazz ground truth, chromatic material of the Wagner class, and more non-Bach, non-Baroque annotation generally | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |
| D-521 | The general law of the circularity map: an abstract circle becomes acyclic in the concrete by one of four named conditions — and every alleged circle in this system fell to one of them | LIVE | — | `cowork_evidence_inventory.md` ⚠gap |
| D-522 | Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that already exist — not a new analysis | LIVE | — | `cowork_evidence_inventory.md` ⚠gap |
| D-523 | If the algorithmic second opinion's LOCAL key is ever adopted it enters UNVALIDATED, and adopting it is a corroborator re-baseline under user ratification — not a refresh | DEFERRED | — | `cowork_evidence_inventory.md` ⚠gap |
| D-531 | The hand-built emission is CONFIRMED and the learned replacement is NOT triggered — retained as an explicit fallback with a concrete trigger, and scoped to one repertoire with a named re-check gate | LIVE | — | `docs/back_half_design.md` ⚠gap |
| D-539 | The standing method for every error slice: decompose it into structural, fitted and ceiling BEFORE building anything — derive, never assert | LIVE | — | `docs/back_half_design.md` ⚠gap |

## D. Layer 1 — the note model — [full entries](decisions/group_D.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-037 | The note model is the single source of truth for what sounds, and reads the score once | LIVE | — | `ARCHITECTURE.md` |
| D-038 | Tied notes are one event; spans are answered by overlap with no horizon | LIVE | — | `ARCHITECTURE.md` |
| D-039 | Ineligible notes are kept and flagged, never dropped | LIVE | — | `ARCHITECTURE.md` |
| D-040 | The tie-unresolved atoms are republished additively for the joint estimator | LIVE | — | `ARCHITECTURE.md` |
| D-517 | The note model's span query uses a start-time-ordered list plus a running latest-end-time tree, chosen because it is the simplest structure that is fast AND returns notes in scan order | NOT STATED | — | `cowork_layer1_note_model_design.md` ⚠gap |
| D-518 | The planned cue-note flag was specified and then REMOVED: after import a cue note cannot be told from a muted note, and the does-it-sound flag already covers both | NOT STATED | — | `cowork_layer1_note_model_design.md` ⚠gap |
| D-519 | Only TIES join written notes into one sounding note — slurred notes stay separate, whatever their pitches | NOT STATED | — | `cowork_layer1_note_model_design.md` ⚠gap |
| D-520 | Widening the loaded span was built DECOUPLED from the whole-score-read fix — superseding the recorded framing that the two were one coupled change | DEFERRED | — | `cowork_layer1_note_model_design.md` ⚠gap |

## E. Layer 2 — the slicer — [full entries](decisions/group_E.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-041 | The slicer output covers the domain with no gaps and no overlaps | LIVE | — | `ARCHITECTURE.md` |
| D-042 | Slice boundaries are every onset AND every release | LIVE | — | `ARCHITECTURE.md` |
| D-043 | Slice identity IS the eligible sounding-note set | LIVE | — | `ARCHITECTURE.md` |
| D-044 | A note that opens no boundary still rides along in the slice's sounding set | LIVE | — | `ARCHITECTURE.md` |
| D-045 | The slicer re-decides nothing about eligibility | LIVE | — | `ARCHITECTURE.md` |
| D-046 | Zero interpretation - the slicer applies no thresholds and no musical judgment | LIVE | — | `ARCHITECTURE.md` |
| D-047 | No special-casing of any note kind | LIVE | — | `ARCHITECTURE.md` |
| D-048 | Boundaries are necessary but not sufficient; over-grab is structurally impossible | LIVE | — | `ARCHITECTURE.md` |
| D-049 | An interior stretch where everything rests is an explicit empty slice, not a gap | LIVE | — | `ARCHITECTURE.md` |
| D-050 | Slicing is clipped to the loaded span and never drags outside it | LIVE | — | `ARCHITECTURE.md` |
| D-540 | A slice is a unit of constant CONTENT, not of constant musical TIME — the layers above must never treat slices as equal-weight units, and a slice's metric extent is evidence weighted by metric structure, not by tempo | LIVE | — | `cowork_layer2_slicing_design.md` ⚠gap |
| D-541 | The metric weight of a slice IS the beat-strength at its start tick, taken from one shared preference-free notation primitive that no consuming layer re-defines | LIVE | — | `cowork_layer2_slicing_design.md` ⚠gap |

## F. Layer 3 — key and mode — [full entries](decisions/group_F.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-051 | The production key/mode path is the sequence decoder, not the per-stretch resolver | SUPERSEDED BY D-001 ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-052 | The signature read and declared-mode mapping live in ONE shared function | LIVE ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-053 | The tick-local path keeps the older resolver (the ratified P4-defer) | SUPERSEDED IN FACT ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-054 | All 21 modes are scored against all 12 tonics; the harmonic major family is deferred | DEFERRED ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-055 | The 21 mode priors are independent and user-configurable | LIVE ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-056 | Notes always win - the notated key signature is a weak hint, not a bypass | LIVE | — | `ARCHITECTURE.md` |
| D-057 | The priority of evidence - actual sounding notes are the strongest evidence | LIVE | — | `ARCHITECTURE.md` |
| D-058 | The piece-start shortcut | SUPERSEDED IN FACT ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-059 | The temporal window - 16 beats back, 8 beats forward, decayed | LIVE ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-235 | Tonal-centre disambiguation may break a close tie but may not overturn a stronger raw winner | LIVE ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-287 | Key-as-distribution is SHELVED - its motivating case was already fixed and no live target was found | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-290 | The key-agnostic local cadence approach is FALSIFIED at its precision ceiling | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-306 | The key layer's backward re-reading stays switched off in the shipped configuration | LIVE ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-323 | Asking whether a pitch belongs to the key is a question about the collection, never about the tonic — the tonic-anchored form must not return | LIVE | 2026-08-02 · user | `docs/scoring_model.md` “`dim7CharacteristicBonus`” |
| D-343 | The key/mode layer owns the candidate space and the note-evidence model outright; the residual is SELECTED from its carried alternatives, never re-scored | LIVE | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §1 |
| D-344 | A scale outside the twenty-one recognized modes is reported as the best-fitting recognized mode, never as the unrecognized scale | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §1 |
| D-345 | The style preset first enters the analysis at the key/mode layer, as a deliberately weak prior over the modes that the note evidence overrides | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §2 |
| D-346 | The candidate set for the whole-run tonality decision is the UNION of every stretch's best candidates, made available at every stretch | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §5 |
| D-347 | The cost of changing tonality is cheap-to-stay plus a term growing with tonal distance plus a large extra penalty on the relative major/minor switch | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §9 |
| D-348 | Tonal distance in the change cost is circle-of-fifths distance — not semitone distance, not differing scale tones — and brief-versus-sustained has no duration threshold at all | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §4 |
| D-349 | The key/mode confidence compares whole readings — the winning run against the best run forced to a different tonality there — not the top two candidates at that stretch | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §9 |
| D-350 | Of the layer's two confidence numbers, the whole-run margin is the published one; the per-stretch emission sigmoid is demoted to a gate input and a diagnostic | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` the opening block (above the first section heading) ⚠gap |
| D-351 | The key/mode search is its own decoder; the chord decoder is not reused for it | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §9 |
| D-352 | The key/mode grading bar splits the cases first: agreement where the published analyses are unanimous, any recorded reading (or an uncertain mark) where they are not | LIVE | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §10 |
| D-353 | The key/mode layer is graded on two goals kept apart — agreement where the notes decide, and whether its own uncertainty lands on the genuinely ambiguous cases | LIVE | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §10 |
| D-354 | The key/mode decoder's own settings are exhausted — no setting of its own moves the fixable error set, so the remaining headroom is not a decoder setting | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §11 |
| D-355 | The identified key/mode lever is the shared scorer's scale-membership term, applied once to the shared scorer at the wiring step and gated on the corpus stop and the pinned outputs | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §11 |
| D-356 | The leading-note presence gate is brittle and its fix is a later key/mode emission step, not a foundation patch — and the scale-membership lever is measured NOT to fix it | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §11 |
| D-357 | Reading the notated spelling as tonality evidence belongs at the function layer, where function gates it — NOT as a standalone key/mode emission patch | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §15 |
| D-358 | A sonority shaped like a dominant is note-level evidence for the tonality it implies, and belongs in the key/mode emission — deferred, design-first | DEFERRED ⚠LEGACY | 2026-08-02 · user | `cowork_layer3_keymode_design.md` §15 |
| D-405 | The full ranked key resolve retained as a segmentation seed is KEPT — adjudicated load-bearing, not dead scoring work | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_structural_integrity_audit.md` §3.1 ⚠gap |
| D-494 | RATIFIED AMENDMENT A-4: the function layer must gain key-confirmation channels that do not require a cadence, plus an enharmonic-identity rule for key spans | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |

## G. Layer 4 — chord identity — [full entries](decisions/group_G.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-060 | The legacy chord analyzer is a vertical sonority analyzer - keep the boundary clean | LIVE ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-061 | Gate thresholds are Baroque-calibrated and must not be loosened for other styles | LIVE ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-062 | Progression signals are withheld while segmentation is being explored | LIVE ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-063 | Cold context on the tick-local path is the accepted contract | LIVE ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-064 | The chord-scoring presets are a measurement-only artifact | SUPERSEDED IN FACT ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-065 | The look-ahead divergence between the two paths is intentional and load-bearing | LIVE ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-066 | Chord symbols written in the score are never analyzer input | LIVE | — | `ARCHITECTURE.md` |
| D-067 | Jazz mode (chord-symbol-driven boundaries) is retired | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-068 | The chord identifier needs at least three distinct pitch classes | LIVE ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-069 | Two identity modes for merged stretches - harmonic summary and as-written | DEFERRED ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-101 | Contextual inversion bonuses fire only for major and minor candidates | SUPERSEDED BY D-102 ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-102 | Augmented and half-diminished candidates receive the inversion bonuses too (Iter 46) | LIVE ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-103 | Pedal-point detection is a second pass, accepted only on two conditions | SUPERSEDED BY D-207 ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-104 | The bass-is-root bonus is conditioned on corroborating support | LIVE ⚠LEGACY | — | `ARCHITECTURE.md` |
| D-105 | The spelling written in the score is read through ONE shared interpreter | LIVE | — | `ARCHITECTURE.md` |
| D-207 | The pedal-point class is defined voice-independently, superseding the bass-only fact | DEFERRED | — | `ARCHITECTURE.md` |
| D-236 | Chord-symbol trust is per symbol, not a per-score preference | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-237 | Only a symbol marked trusted becomes analyzer input; an untrusted symbol is never read | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-238 | Two pitch classes may nominate a chord but may not finalize one; one pitch class may not | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-239 | Chord identity stays local; expansion is by one neighbouring region and is bounded | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-240 | The monophonic smoothing terms are tunable parameters, not prose-only rules | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-241 | The monophonic local-grouping problem is deferred to Phase 2 | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-242 | Vertical and monophonic raw scores are never compared directly | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-280 | Gates read structured fields only - never a chord symbol string and never a Roman numeral | LIVE | 2026-08-02 · user | `docs/iteration_path1_summary.md` “Architecture decisions made during this path” ⚠gap |
| D-284 | Meta-finding: selection/competition is saturated, stop adding re-ranking gates - superseded by the gates doctrine and the adoption | SUPERSEDED BY D-036 with D-001/D-010 ⚠LEGACY | — | `cowork_architecture_reassessment.md` §4 ⚠gap |
| D-299 | No negative-margin guard may be added - it would break every intentional backward-swap gate | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-300 | Gate M (minor read as diminished) is DEFERRED and must not be retried without a new runtime signal | DEFERRED ⚠LEGACY | 2026-08-02 · user | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-301 | Gate N (major read as an inverted minor) is DEFERRED and must not be retried without a multi-region model | DEFERRED ⚠LEGACY | 2026-08-02 · user | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-302 | No further local scoring fix for inversions may be attempted — the remaining divergence is not an analyzer defect | LIVE ⚠LEGACY | 2026-08-02 · user | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-303 | Non-chord-tone detection is deferred, and if built it must be chord identification that knows about non-chord tones, never stripping after the fact | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-305 | The ban on reading written harmony as analyzer input is decided by what an annotation says, not by how it is stored | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-312 | The carried alternative readings are inside the byte-identity acceptance contract — same winner with different alternatives is a behavior change | LIVE | 2026-08-02 · user | `cowork_stage5_fitter_design.md` “§15 Open items & ratification asks” |
| D-317 | The backward-walk boundary change is a dead end — do not retry it | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/redesign_plan.md` “Dead end: `noteEnd <= startTickInt` → `noteEnd < startTickInt`” ⚠gap |
| D-318 | A short-region external merger is a dead end — do not retry it | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/redesign_plan.md` “Dead end: short-region merger trigger” ⚠gap |
| D-319 | Re-analysing the merged aggregate is a dead end — no tone-aggregation approach fixes the arpeggio root failure | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/redesign_plan.md` “Dead end: re-analysis of inline-merged aggregate” ⚠gap |
| D-320 | The absent-root guard is REVERTED and must not be retried — 'absent root means wrong reading' is false corpus-wide | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/redesign_plan.md` “What NOT to do first” ⚠gap |
| D-321 | Winner selection compares candidate scores exactly, with no epsilon anywhere in the ranking | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` “Floating-point tie policy” |
| D-322 | Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` “Floating-point tie policy” |
| D-324 | Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` “§6a. The unified promotion primitive `promoteToWinner()`” |
| D-325 | A correction rule that changes a committed chord's identity is retired or folded in BEFORE the search is widened past it | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/decoder_design.md` §13 ⚠gap |
| D-326 | The chord-path search emits the whole path with every stretch's alternatives and margins, not the committed reading alone | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/decoder_design.md` §13 ⚠gap |
| D-327 | The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/decoder_design.md` “§6 amendment” ⚠gap |
| D-328 | A wider search cannot fix the arpeggio root failure — the wrong reading IS the global optimum, so only re-weighting or joint segmentation can | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/decoder_design.md` §11 ⚠gap |
| D-329 | Completeness of the candidate list is the priority — a chord never listed can never be chosen | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §4 |
| D-330 | Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §8 |
| D-331 | Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |
| D-332 | A carried alternative's added notes are marked UNKNOWN rather than asserted absent — never synthesized | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §7 |
| D-333 | The membership tie-break's direction is an idiom-calibrated number, never a branch on style — the three-tier structure is fixed | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |
| D-334 | The bare-fifth chord type stays in the catalogue structurally; whether it wins is an idiom-calibrated number | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |
| D-378 | Re-deciding a chord under a different tonality is well-defined ONLY on the decoder path — the legacy multi-pass emission cannot be faithfully re-decoded, and a naive re-emit injects a measured ~6 % same-tonality root-flip artifact | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_joint_key_chord_design.md` “§2.2 The chord re-decoded under each carried key” |
| D-380 | The carry's meaningful axis is DISTINCT ROOTS, and every above-threshold root is carried at graded confidence — a carry of winner-plus-one discards the third root on about a quarter of slices | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§2.2 The exclusion tail is load-bearing and must be carried” |
| D-381 | The carry must cap on DISTINCT ROOTS, not on voicings — the existing voicing-keyed cap gives no structural guarantee that a third root survives | DEFERRED ⚠LEGACY | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§2.3 Does the decoder's governed carry provide this? The distinct-root guarantee is OWED [code]” |
| D-385 | Pedal-point detection's home is DECIDED: a reader over the chord layer's carry that annotates a carried reading — never a second analysis that overwrites the winner | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§6.3 Placement” |
| D-386 | No fourth hand-rolled scan for the best different-root alternative — the pedal reader consumes the carry's own ranking, or the one unified primitive | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§6.5 The diff-root need is served by the carry / FQ-1” |
| D-402 | The inversion-append is a pure cap artifact that dissolves when the cap is removed; the below-threshold bass promotion is a targeted promotion that stays | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_structural_integrity_audit.md` §1.2 ⚠gap |
| D-403 | STOP, not forced: the four best-different-root scans are NOT one decision at code, so the one-decision-four-sites premise over-counts | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_structural_integrity_audit.md` §3.1 ⚠gap |
| D-423 | The gate-retirement stage is the only sanctioned way the post-scoring gates change, and three do-not rules hold through every stage | LIVE ⚠LEGACY | 2026-08-03 · user | `docs/implementation_roadmap.md` “Relationship to the existing phase roadmap” ⚠gap |
| D-463 | The temporal signals sitting in the vertical scorer are left where they are, and the gate that depends on them must move with them | LIVE | 2026-08-04 · user | `docs/layer_architecture_audit.md` ⚠gap |
| D-464 | No further progression-level signal may be added to the single-step look-around structure; it goes in the progression context instead | LIVE | 2026-08-04 · user | `docs/layer_architecture_audit.md` ⚠gap |
| D-465 | The policy for judging a proposed post-scoring gate: another bias correction gets the bias fixed first, a structural condition is sound, and a cascade means the missing thing is functional context | LIVE | 2026-08-04 · user | `docs/layer_architecture_audit.md` ⚠gap |
| D-467 | A rebuilt or re-tuned chord scoring must not rely on the held-note repetition bonus the faithful note model removed | LIVE | 2026-08-04 · user | `cowork_target_architecture.md` ⚠gap |
| D-501 | A tool may read a written chord symbol ONLY as a comparison or ground-truth label — never as input that influences what the analyzer computes | LIVE | 2026-08-04 · user | `docs/symbol_input_audit.md` ⚠gap |
| D-510 | The correct carry is the one that keeps the distinct alternative reading, not the one that appends a near-duplicate of the winner — chosen on the carry's purpose, not on which code is at HEAD | LIVE | — | `cowork_gateA_unification_design.md` ⚠gap |
| D-511 | One promotion primitive with a present-first dedup guard replaces the two ad-hoc promotion idioms; the append branch fires only when the target is genuinely absent | LIVE | — | `cowork_gateA_unification_design.md` ⚠gap |
| D-512 | Gate A becomes removable only once the unified promotion reproduces its carry byte-for-byte — that reproduction IS the retirement condition, not the winner-inertness that preceded it | LIVE | — | `cowork_gateA_unification_design.md` ⚠gap |
| D-536 | The bass note and the chord are chosen TOGETHER — the winner is the (bass, root, template) triple — replacing the sequential commit-the-bass-then-score pipeline | LIVE ⚠LEGACY | — | `docs/iter92_joint_bass_chord_scoring.md` ⚠gap |
| D-537 | The completeness bonus fires ONLY for a root-position reading whose three triad tones are all present — the guard that stops it from demoting genuine slash chords | LIVE ⚠LEGACY | — | `docs/iter92_joint_bass_chord_scoring.md` ⚠gap |
| D-538 | A multi-signal scoring change lands one signal at a time, with the corpus check re-run after each step and any increase in errors a hard stop before the next | LIVE ⚠LEGACY | — | `docs/iter92_joint_bass_chord_scoring.md` ⚠gap |

## H. Layer 5 and Layer 6 — function, cadence, grouping — [full entries](decisions/group_H.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-079 | The function layer annotates and resolves; it never rewrites the committed chord | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-080 | Carried abstentions are resolved by selecting among the carried readings, never re-derived | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-081 | The cadence detector is key-agnostic | LIVE | — | `ARCHITECTURE.md` |
| D-082 | The grouping layer is additive, read-only, with no feedback | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-083 | Hierarchy, periods and prolongation are out of the validatable core | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-084 | The progression-schema recognizer is a consumer of the function layer, not a new layer | DEFERRED · derivation not recorded | — | `ARCHITECTURE.md` |
| D-085 | The voice-leading axis is a separate axis with its own layers | LIVE | — | `ARCHITECTURE.md` |
| D-248 | Tonicization labels are not implemented and are deferred | DEFERRED ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-291 | The tonicization labeller is NOT wired, and the metric is NOT changed to credit it - both would hide a real key error | LIVE | 2026-08-02 · user | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-335 | The function layer outputs the Roman numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |
| D-336 | Cadence detection is key-agnostic and votes for the key rather than reading one | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |
| D-337 | A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |
| D-338 | The function layer selects among the chord layer's carried readings and never re-derives a chord from the notes | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |
| D-340 | The reading the function layer emits IS the selected source's committed identity, carried whole — never rebuilt field by field | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §7 |
| D-341 | The licensed root-motion set is completed by theory — the ascending fifth, the descending second and the diatonic diminished fifth are added | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §5.0 |
| D-342 | Putting the function layer into production is DEFERRED INDEFINITELY — the posture is a dormant build with ground-truth validation | DEFERRED ⚠LEGACY · derivation not recorded | 2026-08-02 · user | `cowork_layer5_function_design.md` §11 |
| D-382 | The function layer selects by JOINT CONSISTENCY across tonality, root, inversion and bass — not by maximizing any one score — and every ambiguity kind reasons over the full carried distribution | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score” |
| D-383 | Bass, spelling and tonality-consistency DECIDE; a licensed progression is only a tie-break among already-consistent readings and may never override a committed root | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§3.2 The evidence channels, ranked by the research” |
| D-384 | Re-ranking the tonality under chord evidence is a SEPARATE step, never part of the function layer's selection — the function layer reasons inside a tonality already fixed | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§4.1 Layer boundaries” |
| D-387 | A contradiction between the function context and a committed chord is surfaced on the ONE open mark, enriched with a reason — not on a second parallel flag, and not by overloading the plain undecided mark | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§7.2 The vehicle” |
| D-388 | Texture is read primarily from HOW VOICES MOVE TOGETHER, not from how far each line leaps — the interval-led alternative was measured weaker and partly an encoding artifact | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §9 |
| D-389 | A notated voice is a FACT and an inferred perceptual line is a JUDGMENT — the two are separate types and are never conflated | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §9 |
| D-390 | The first version classifies the WHOLE selection as one texture — classifying within a piece is deferred behind a measurement, because the evidence is per-piece | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §9 |
| D-391 | Reads between the two analysis dimensions are admissible only where the combined dependency graph stays acyclic — harmonic layers may take voice-leading FACTS freely; a voice-leading component may take a committed harmonic result only if nothing that result depends on consumes it back | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §9 |
| D-392 | The later voice-leading components are CLAIMS WITH OWNERS, not builds — each clears its own design document and its own evidence before any instruction exists | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §9 |
| D-393 | Every voice-leading inference publishes the committed answer AND the FULL ranked list of all alternatives with their weights — nothing below the top is discarded | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §5.3 |
| D-394 | Reducing a chord-bearing voice to one line is a DECLARED parameter of the request, uniform across sources — never silent, never chosen per source; the first version offers exactly one rule | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §5.1 |
| D-395 | Three named floors govern abstention, and the FIT floor is the one that lets a passage resembling NO known texture decline rather than be forced to its nearest | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §5.3 |
| D-396 | The voice-leading dimension covers NOTATED music only, and its style coordinate is UNDEFINED — not zero — for sources that carry no voices | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §8 |
| D-397 | The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §16 ⚠gap |
| D-398 | Parallel motion is judged SEMITONE-EXACT, not by generic diatonic size — a same-direction move whose semitone interval changes counts as similar motion | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §15 ⚠gap |
| D-399 | The texture feature space was decided BY MEASUREMENT among three named candidates — the standardized combination of both views won; the unstandardized combination was rejected before testing for a measured dilution | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §5.3 |
| D-400 | A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice | LIVE | 2026-08-02 · user | `cowork_voiceleading_axis_design.md` §16 ⚠gap |
| D-419 | Until the recognition consumer is built, the function layer does not touch the harmonic vocabulary | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` the opening block (above the first section heading) ⚠gap |
| D-454 | The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-455 | A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-457 | A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-458 | The codetta refinement is read as the as-built tiling: keep the strong cut, drop the weak one, and record the codetta end as an annexe | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-459 | The key-area confidence is a declared margin-class boundary confidence, and its input is the declared key confidence — never the grading diagnostics' sigmoid | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-460 | A group counts as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-461 | The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-462 | Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` ⚠gap |
| D-472 | Key areas are grouped by a smoothing pass over the already-stabilized regions, and a region that disagrees without clearing the confidence test keeps its own key while being grouped into the enclosing area | LIVE | 2026-08-04 · user | `docs/unified_analysis_pipeline.md` ⚠gap |
| D-476 | The phrase-boundary primitive is owned by the notation-derived view layer — not by the note model, and not by the function layer that consumes it | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-477 | Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-478 | A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-479 | The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-480 | The phrase-boundary primitive is NOT an accuracy requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept proportionate | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-481 | The notated markers are emitted as boundaries unconditionally; only the surface-cue strength is peak-picked | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-482 | The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-483 | The picked boundaries are validated against the analysts' own phrase marks; a fermata-derived phrase list is inadmissible as ground truth because the primitive reads fermatas | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-484 | The phrase-boundary primitive is a derived view: it inherits the loaded span, requests no extension of its own, and publishes a per-profile max-normalised boundary confidence | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-485 | Each picked boundary should carry which cue fired and at what scope; the picked set is scope-blind today and the refinement waits for the inference phase | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` ⚠gap |
| D-490 | FALSIFIED: no threshold can make the fine-grain function override net-positive — the harm rate is flat against both quantities the threshold is built from | LIVE | 2026-08-04 · user | `cowork_fb_redesign_design.md` ⚠gap |
| D-491 | REFUTED: making the override's comparison vertically fair does not repair it — even where the alternative fits the notes at least as well, it is still about 71 % harmful | LIVE | 2026-08-04 · user | `cowork_fb_redesign_design.md` ⚠gap |
| D-492 | The recommended redesign is to demote the override to an annotation — carrying the earlier reading unchanged and surfacing the contradiction — floored by simply disabling it | LIVE | 2026-08-04 · user | `cowork_fb_redesign_design.md` ⚠gap |
| D-493 | Restricting the override to the genuinely-coupled key-and-chord minority is UN-COMPUTABLE, not merely unmeasured: its trigger is not computed anywhere and building it is the still-owed joint step | LIVE | 2026-08-04 · user | `cowork_fb_redesign_design.md` ⚠gap |
| D-495 | RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |

## I. Module boundaries and code structure — [full entries](decisions/group_I.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-070 | Style behaviour is fully data-driven - no conditional logic on style identity | LIVE | — | `ARCHITECTURE.md` |
| D-071 | The analysis layer never produces display strings | LIVE | — | `ARCHITECTURE.md` |
| D-072 | The dependency rule - the analysis library knows nothing about the score format | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-073 | Single implementation for shared logic; mirroring is a last resort | LIVE | — | `ARCHITECTURE.md` |
| D-074 | Analyze and suggest - never modify the score without explicit user action | LIVE | — | `ARCHITECTURE.md` |
| D-075 | Interface-based design for machine-learning substitutability | LIVE | — | `ARCHITECTURE.md` |
| D-076 | Score inspection before diagnosis | LIVE | — | `ARCHITECTURE.md` |
| D-077 | The configuration interface is split into two narrow IoC interfaces | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-078 | The cross-layer value types live in a dependency-free leaf header | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-107 | American English throughout | LIVE | — | `ARCHITECTURE.md` |
| D-108 | Cross-platform by default | LIVE | — | `ARCHITECTURE.md` |
| D-227 | Read how MuseScore already does it, and never invent parallel infrastructure | LIVE | — | `ARCHITECTURE.md` |
| D-228 | The bridge pattern - engraving types enter and leave at named free functions in the notation namespace | LIVE | — | `ARCHITECTURE.md` |
| D-229 | The MuseScore-dependency rule - one general rule for what our code may depend on | LIVE | — | `ARCHITECTURE.md` |
| D-233 | Build and test commands run synchronously; one run, one result | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-296 | READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-311 | The chord-analyzer file split happens once — the SEQUENCING is spent (the split happened first, not last); the once-only LESSON is what carries forward | SUPERSEDED IN FACT | 2026-08-02 · user | `cowork_engage_arc_plan.md` “The stages” |
| D-401 | The refactor sequencing call — the portable unification wins run before Layer 5, the legacy-path tangles fold into the decoder engagement, and the file split is last | LIVE | 2026-08-02 · user | `cowork_structural_integrity_audit.md` “The one coherent order” |
| D-404 | Relocating the neighbour-chord temporal-context computation out of the derived-view layer is DEFERRED to the decoder engagement, which owns regional temporal context | DEFERRED ⚠LEGACY | 2026-08-02 · user | `cowork_structural_integrity_audit.md` §3.1 ⚠gap |
| D-416 | Two structural refactors are DEFERRED and OWED, and must be surfaced at every planning checkpoint until done | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` |
| D-427 | Component (1a) of the two-deferred-refactors mandate — the physical `chordanalyzer.cpp` file split: DELIVERED 2026-06-17 | LIVE | — | `docs/implementation_roadmap.md` |
| D-428 | Component (1b) of the two-deferred-refactors mandate — the iteration-vocabulary API renames: STILL OWED, and the subject is the LEGACY arm | DEFERRED ⚠LEGACY | — | `docs/implementation_roadmap.md` |
| D-429 | Component (2) of the two-deferred-refactors mandate — dissolving the post-hoc gate-correction layer into fitted weights: STILL OWED, and its PRINCIPLE binds the live design | DEFERRED ⚠LEGACY | — | `docs/implementation_roadmap.md` |
| D-469 | The tick-local path is left OUTSIDE the unified pipeline by design — its point-in-time semantics would be distorted by one shared interface | LIVE | 2026-08-04 · user | `docs/unified_analysis_pipeline.md` ⚠gap |
| D-470 | The temporal-context extension fields are recorded during the pipeline's own analysis pass; no consumer re-runs the chord analysis to rebuild them | LIVE | 2026-08-04 · user | `docs/unified_analysis_pipeline.md` ⚠gap |

## J. Presentation and output conventions — [full entries](decisions/group_J.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-086 | Roman numerals and Nashville numbers are presentation choices, not separate analyses | LIVE | — | `ARCHITECTURE.md` |
| D-087 | Display options live with the formatter, not with the analyzer preferences | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-088 | No automatic key signature injection | LIVE | — | `ARCHITECTURE.md` |
| D-089 | The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive | SUPERSEDED BY D-018 ⚠LEGACY · derivation not recorded | — | `ARCHITECTURE.md` |
| D-090 | Abstention is a valid outcome - high precision before coverage | LIVE | — | `ARCHITECTURE.md` |
| D-106 | The augmented-sixth labels are gated to the Standard and Baroque presets | SUPERSEDED IN FACT · derivation not recorded | — | `ARCHITECTURE.md` |
| D-234 | A chord symbol string must be valid under chords_std.xml; chords.xml is not relied on | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-295 | Zero information loss to the end user - every inferred object must be displayable | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-304 | The analyzer always emits its fullest reading; simplifying it happens only when comparing against a corpus, never in the product | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-471 | The sub-beat annotation duration gate is not retired on argument — it is kept or dropped on a measured observation run, with the verdict stated in advance | LIVE | 2026-08-04 · user | `docs/unified_analysis_pipeline.md` ⚠gap |
| D-498 | RATIFIED AMENDMENT A-9: a product stance is owed for output that is mostly uncertain, and for music outside the tonal vocabulary altogether | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |

## K. Documentation governance — [full entries](decisions/group_K.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-091 | ARCHITECTURE.md is the canonical architecture document and wins every disagreement | LIVE | — | `ARCHITECTURE.md` |
| D-092 | A cross-cutting contract is stated once and never redefined in a layer document | LIVE | — | `ARCHITECTURE.md` |
| D-093 | STATUS.md wins on current state; ARCHITECTURE.md on design | LIVE | — | `ARCHITECTURE.md` |
| D-094 | Each layer carries exactly one build state | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-109 | The open-items register is the one home for every unresolved issue, and the index is the status of record | LIVE | — | `OPEN_ITEMS.md` |
| D-110 | The decisions register records what was decided and its status - nothing else | LIVE | — | `open_items/OI-208.md` |
| D-111 | A decision belongs in the owning layer's specification; the register is an index | LIVE | — | `open_items/OI-208.md` |
| D-112 | Never work from memory instead of documented facts | LIVE | — | `CLAUDE.md` |
| D-113 | Music-theory words are reserved for their music-theory meaning | LIVE | — | `CLAUDE.md` |
| D-127 | An architectural decision that changes is documented in the same commit | LIVE | — | `ARCHITECTURE.md` |
| D-192 | A scoring change and its documentation land in the same commit | LIVE | — | `CLAUDE.md` |
| D-193 | The writing standards live in one place, and predicates must be qualified | LIVE | — | `CLAUDE.md` |
| D-194 | No self-invented labels, abbreviations, numbering schemes or jargon | LIVE · derivation not recorded | — | `CLAUDE.md` |
| D-195 | Every design decision carries its defense at its home | LIVE | — | `CLAUDE.md` |
| D-230 | The decisions register is a mandatory session-start read, and a new ruling lands in the register in the commit that records it | LIVE | — | `CLAUDE.md` |
| D-232 | The section numbers are authoritative; the "Rule N" labels are a legacy flat numbering | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-255 | Every design document follows one fourteen-section structure, synthesized from three published standards | LIVE | 2026-08-02 · user | `cowork_design_doc_template.md` |
| D-256 | Every design document opens with one of four declared status banners | LIVE | 2026-08-02 · user | `cowork_design_doc_template.md` |
| D-257 | A specification carries a locator to its code and tests; code mechanics never do the explaining | LIVE | 2026-08-02 · user | `cowork_design_doc_template.md` |
| D-307 | A specification cites code by function or section anchor, never by raw line number | LIVE | 2026-08-02 · user | `cowork_design_doc_template.md` |
| D-420 | One cross-layer extension specification, and the duplicate written the same day is killed into it | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` |
| D-424 | A decision surface names the principle behind every pro and con, and rates every option on two axes | LIVE | — | `cowork_notation_adoption_increment.md` the opening block (above the first section heading) ⚠gap |
| D-430 | The contract-home criterion's unit is a SECTION of a document, not the document | LIVE | — | `CLAUDE.md` |
| D-432 | What counts as a delegation, graded by form — the clause the section-level criterion did not touch | LIVE | — | `CLAUDE.md` |
| D-433 | A shelved section can be a home — shelving is a status, not a kind | LIVE | — | `CLAUDE.md` |
| D-435 | Delegating to a document and being a home are different tests with different subjects | LIVE | — | `CLAUDE.md` |
| D-499 | RATIFIED AMENDMENT A-10: four documentation riders — a consolidated ownership page for the notation-derived views, the membership tie-breaker recorded as idiom-calibrated, and the producer-agnostic seam pinned as a design property | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |

## L. Licensing, contribution, and coding standards — [full entries](decisions/group_L.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-116 | The system is a module inside MuseScore Studio, not a plugin | LIVE | — | `ARCHITECTURE.md` |
| D-117 | The long-term intent is an official contribution to MuseScore Studio | LIVE | — | `ARCHITECTURE.md` |
| D-118 | GPL v3, and every external library must be GPL v3 compatible | LIVE | — | `ARCHITECTURE.md` |
| D-119 | The MuseScore contributor licence agreement is signed before any pull request | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-120 | MuseScore's coding style is followed, with clang-format run before every commit | LIVE | — | `ARCHITECTURE.md` |
| D-121 | Where MuseScore's documentation practice is minimal, the higher standard applies | LIVE | — | `ARCHITECTURE.md` |
| D-122 | Every public class and method is documented in musical terms | LIVE | — | `ARCHITECTURE.md` |
| D-123 | Every non-obvious scoring weight or threshold explains its musical reasoning | LIVE | — | `ARCHITECTURE.md` |
| D-124 | The analyzer code must be readable by a musician | LIVE | — | `ARCHITECTURE.md` |
| D-125 | Every test documents the musical situation, the expected result, and what a failure means | LIVE | — | `ARCHITECTURE.md` |
| D-126 | One coherent piece of functionality per pull request | LIVE | — | `ARCHITECTURE.md` |
| D-292 | The fitting-pool licence constraint - values that ship are fitted only on freely-licensed music | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-315 | A one-line fix was made to MuseScore's own chord-symbol parser and is live in the fork | LIVE | 2026-08-02 · user | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-375 | Every real source of difficulty labels is research-only or proprietary — a difficulty-grading feature needs a licence path before it can be sold | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-489 | The snapshot sources are hash-pinned rather than copied in-tree, because their licences make an in-tree copy incompatible with this project's licence | LIVE | 2026-08-04 · user | `docs/score_inventory.md` |

## M. The style system and the knowledge base — [full entries](decisions/group_M.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-128 | Styles are defined entirely in data; adding one never requires code changes | LIVE | — | `ARCHITECTURE.md` |
| D-129 | Style conflicts resolve by a declared priority - explicit overrides always win | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-130 | The style loader never names a style in code | LIVE | — | `ARCHITECTURE.md` |
| D-131 | One shared style taxonomy, not two parallel vocabularies | LIVE | — | `ARCHITECTURE.md` |
| D-132 | The remaining empirical grounding is the per-preset WEIGHTS alone; the clusters half is delivered by the ratified five-idiom set | DEFERRED | — | `ARCHITECTURE.md` |
| D-133 | The harmonic vocabulary is a queried reference component, not a layer of the analysis | LIVE | — | `ARCHITECTURE.md` |
| D-406 | The catalog owns the NAMED progressions and substitutions; the pairwise licensing grammar is owned by the function layer — the two are never derived from each other | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §1 |
| D-407 | The vocabulary supplies ranked candidates and DECIDES nothing — the threshold, the style weighting and what to do with a candidate are the consumer's | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §2 |
| D-408 | Voice-leading is a DIFFERENT DIMENSION and is not held in the harmonic vocabulary — a schema defined by its voice-leading is present only by its harmonic pattern | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §2 |
| D-409 | There is no binary match or no-match — only a score on a ranked list, and the list may be EMPTY | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §4 |
| D-410 | The first version matches EXACTLY AND WHOLE; the partial matcher is deferred with its decision structure already fixed and only its constants left open | DEFERRED | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §4 |
| D-411 | The Axis loop is ONE entry in one canonical rotation — its other rotations become rotation-tolerant matching on that entry, never three more entries | DEFERRED | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §5.2 |
| D-412 | The circle-of-fifths entry is the FULL cycle, and a realisation may enter at any member and run contiguously to the final tonic | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §5.2 |
| D-413 | Upper-structure and rootless VOICING substitution is outside the harmonic vocabulary — it is a voicing, not a function | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §5.3 |
| D-414 | The catalog is GENERATIVE where it can be and enumerated only where it must be | LIVE | 2026-08-03 · user | `cowork_progression_schema_dictionary.md` §7 |
| D-421 | Idiom re-discovery rides every corpus wave, on research material only, and a changed cluster set is its own ratification event | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` the opening block (above the first section heading) ⚠gap |
| D-496 | RATIFIED AMENDMENT A-6: whether the pairwise progression grammar lives inside the harmonic vocabulary or stays a separate store is decided at the recognition-consumer build, explicitly | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` ⚠gap |
| D-502 | The span a recognised named progression covers is called the progression-schema-span — the bare word 'sequence' is reserved for the harmonic sequence and 'progression' for the whole committed chord stream | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-503 | The idiom mixture is DISCOVERED from the score and merely SEEDED by the user's preset, in three forward-only phases | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-504 | A recognised harmonic sequence is ALWAYS emitted as key evidence — the earlier gate that emitted it only where no cadence existed threw corroboration away | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-505 | A harmonic sequence requires at least two transposed statements of the SAME recognised entry; a single internally-sequential entry emits none | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-506 | Progression recognition is ADDITIVE: the literal Roman numeral is never rewritten, and a substitution is recorded only in the annotation | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-507 | A catalog entry defined by its melodic or bass lines is recognised by its chord skeleton alone and carries a 'chords-only' mark, with its prior strength reduced | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-508 | The catalog/grammar consistency test ships scoped to the MEASURED containment — an explicit known-gap list — and tightens to a clean assertion when the grammar amendment lands | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-509 | Where the analysis already committed a chord, a recognised progression corrects it through the EXISTING override frame and may only SELECT an already-carried reading — no new comparison frame, and never a reading built from the notes | LIVE | — | `cowork_progression_schema_design.md` ⚠gap |
| D-542 | Idiom discovery runs DISCOVER-THEN-NAME: structure is learned on a low-level encoding carrying no theory or genre labels, and theory features and genre labels are interpretation lenses applied afterwards, never clustering input | NOT STATED | — | `cowork_idiom_discovery_design.md` ⚠gap |
| D-543 | The encoding is key-normalised tonal-pitch-class TRANSITIONS — spelled where spelling is reliable, mod-12 only where it is genuinely absent — run as two complementary views | NOT STATED | — | `cowork_idiom_discovery_design.md` ⚠gap |
| D-544 | Confound control is a FIRST-CLASS GATE, and the source-leakage test decides validity: if the clusters are explained by which corpus a piece came from, the result is bookkeeping and not idiom | NOT STATED | — | `cowork_idiom_discovery_design.md` ⚠gap |
| D-545 | The uniform mechanical extractor for idiom discovery is the external library, stopping at the note-and-slice front — OUR OWN key/chord/function inference must NEVER touch the extraction | NOT STATED | — | `cowork_idiom_discovery_design.md` ⚠gap |

## N. Generation, constraints, visualization, and the LLM integration — [full entries](decisions/group_N.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-134 | A voicing type is never requested directly; the style selects it | LIVE | — | `ARCHITECTURE.md` |
| D-135 | A fixed element is a hard constraint the optimizer may never modify | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-136 | The inference demo view is a developer tool and is not shipped | DEFERRED | — | `ARCHITECTURE.md` |
| D-137 | The harmony maps are our own visual design, and are chosen partly to avoid intellectual-property claims | DEFERRED | — | `ARCHITECTURE.md` |
| D-138 | Chord preview uses MuseScore's note-input pathway, not the playback pipeline | DEFERRED | — | `ARCHITECTURE.md` |
| D-139 | The language model holds no object references - every tool call carries its own musical address | DEFERRED | — | `ARCHITECTURE.md` |
| D-140 | The language model is a search agent and is never given the whole score | DEFERRED | — | `ARCHITECTURE.md` |
| D-141 | The language model sees what the user set, not what the engraving engine derived | DEFERRED | — | `ARCHITECTURE.md` |
| D-142 | The composing module is the language model's context provider; the model never re-derives harmony | DEFERRED | — | `ARCHITECTURE.md` |
| D-143 | The language-model bridge is built as a module but confined to the core access layer, so it can become a plugin | DEFERRED | — | `ARCHITECTURE.md` |
| D-440 | The language-model integration is purpose-built and does not wait for the plugin-API reform | DEFERRED | 2026-08-04 · user | `ARCHITECTURE.md` |
| D-441 | Analysis and modification are phases of ONE conversation; a follow-up instruction re-uses the reasoning rather than re-analysing | DEFERRED | 2026-08-04 · user | `ARCHITECTURE.md` |
| D-442 | A validation failure goes back to the language model as a tool-call error and is never shown to the user | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |
| D-443 | Tool use is the only capability the provider abstraction requires; a provider without it is read-only | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |
| D-444 | The core access layer is a facade over interfaces that already exist, not a redesign | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |
| D-445 | A musical address does not identify a single note, so the note entity carries its own identifier | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |
| D-446 | The language model resolves how the user names a passage; no index is built and the kinds of reference are not enumerated | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |
| D-447 | The model's tool definitions are generated from the operation set, never maintained by hand | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |
| D-448 | The operation set is curated from observed use, not an exposure of every editing method | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` ⚠gap |

## O. Intonation — [full entries](decisions/group_O.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-144 | Percussion is excluded from analysis and tuning; fixed-pitch instruments are the tuning anchor | LIVE | — | `ARCHITECTURE.md` |
| D-145 | One preference chooses the tuning system, and no tuning code hardcodes one | LIVE | — | `ARCHITECTURE.md` |
| D-146 | A tie chain is one indivisible tuning event, and its tuning comes from one authority note | LIVE | — | `ARCHITECTURE.md` |
| D-147 | A slur, not a tie, joins the halves of a split note | LIVE | — | `ARCHITECTURE.md` |
| D-148 | The split is visible in the score; the invisible alternative is deferred | LIVE | — | `ARCHITECTURE.md` |
| D-149 | Only visible, sounding notes enter the pitch-class collection | LIVE | — | `ARCHITECTURE.md` |
| D-150 | The chord staff is the output, never an input to the analysis that fills it | LIVE | — | `ARCHITECTURE.md` |
| D-151 | Populating the chord staff overwrites whatever is in the selected range | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-152 | Roman numerals and Nashville numbers are never shown together on one staff | LIVE | — | `ARCHITECTURE.md` |
| D-153 | Interactive annotations are written in the score's normal colour; the batch pipeline writes red | LIVE | — | `ARCHITECTURE.md` |
| D-244 | Choosing an interval family for an ambiguous sonority is deferred; fixed tables are used | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-245 | Voice role comes from staff position or explicit assignment; automatic melody detection is deferred | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-246 | Fixed-pitch instruments are deferred, and will never receive tuning offsets | DEFERRED | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-247 | An anchor note stays at 12-TET, is never split, and is excluded from drift and centering | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-366 | Recorded-performance intonation material is OUT of corpus scope — the intonation features are validated by theory and by listening | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |

## P. The user interface, persistence, and machine-learning readiness — [full entries](decisions/group_P.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-154 | New panels use MuseScore's own panel and interface infrastructure | DEFERRED | — | `ARCHITECTURE.md` |
| D-155 | Every user-visible string goes through MuseScore's localization, in English and Swedish | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-156 | Accessibility follows MuseScore's existing patterns | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-157 | The harmonic-display preference exists for clarity, not for cost | LIVE | — | `ARCHITECTURE.md` |
| D-158 | Our data lives in separate files inside the score archive; the score file is never touched | DEFERRED | — | `ARCHITECTURE.md` |
| D-159 | Every custom file carries a format version, and the score file is never rewritten by our persistence | DEFERRED · derivation not recorded | — | `ARCHITECTURE.md` |
| D-160 | Arranger interactions are logged from the start, with consent, as future training data | DEFERRED | — | `ARCHITECTURE.md` |
| D-161 | Chord symbols already in a score are a second analyst's opinion, not ground truth | DEFERRED | — | `ARCHITECTURE.md` |

## Q. Scope and the development toolchain — [full entries](decisions/group_Q.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-162 | The development tools are not part of the shipping product | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-163 | The batch tool deliberately skips post-load layout | LIVE | — | `ARCHITECTURE.md` |
| D-164 | What is out of scope, and what degrades gracefully at the boundary | LIVE · derivation not recorded | — | `ARCHITECTURE.md` |
| D-308 | A newly acquired corpus enters as research material; the frozen regression corpus stays the gate until a deliberate re-baseline | LIVE | 2026-08-02 · user | `CLAUDE.md` |
| D-309 | A corpus the analysis handles badly stays on the roadmap marked deferred; it is more valuable than one that confirms what already works | LIVE | 2026-08-02 · user | `docs/score_inventory.md` |
| D-310 | Jazz accuracy is not measurable on the corpora held: the low agreement is missing bass and piano voicings, not a scoring failure | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |
| D-359 | Discovering a new corpus counts as a CENSUS DEFECT — the fix is to enumerate its container to closure, never to ingest the one repository | LIVE | 2026-08-02 · user | `cowork_score_census.md` §1 ⚠gap |
| D-360 | A corpus enters the registry only with all five admission fields decided — annotation type, score alignment, format, licence class, decision tier | LIVE | 2026-08-02 · user | `cowork_score_census.md` §3 ⚠gap |
| D-361 | Corpora are de-duplicated by WORK, not by container — and a work in the regression corpus is excluded as reference data from every other container | LIVE | 2026-08-02 · user | `cowork_score_census.md` §4 ⚠gap |
| D-362 | What the census may claim, stated exactly: closure over the enumerated containers, a citation-closure argument for gradable harmony reference data, and a BOUNDED claim for everything else | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8 ⚠gap |
| D-363 | Four named reasons license leaving a source un-enumerated — and non-Western symbolic music is closed by RULING, not by enumeration | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8 ⚠gap |
| D-364 | Every new analysis purpose triggers its own corpus sweep BEFORE its design document is signed — having enumerated the container does not discharge the duty to ask the new question of it | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8b ⚠gap |
| D-365 | A corpus search driven by the SUM of all needs is worth running, but it is step 3 of 3 — the needs list and the re-scoring of what is already enumerated come first | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-367 | A corpus found FOR one need is scored against the WHOLE needs list at intake, and every annotation layer it carries is inventoried — never tagged to the purpose that found it | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-368 | When new material bears on an already-settled conclusion, the rework question is settled by a recorded protocol — record, measure cheaply, then fork on whether it CONTRADICTS or merely enriches | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-369 | The DCML figured-bass repository is a REALIZATION SCRIPT, not reference data — walked and recorded so it is never mistaken for reference data again | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-370 | Reference data for implied polyphony does not exist and the negative is FINAL — the two candidate sets were never released | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-371 | No dataset pairs an ornament sign with its written-out realization — confirmed absent, so the ornament expansion ships rule-based and unvalidated, as predicted | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-372 | Marked part-writing errors must be BUILT, not downloaded — no public dataset exists and the two commercial holders keep theirs closed | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-373 | The only dual-annotator reference data actually on disk is the 27 TAVERN A/B pairs — the assumed second source was measured to have ZERO overlap | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-374 | The flexible multi-reading chorale annotations are RECORD-ONLY — they overlap the regression repertoire, so any use over those pieces is a future user ruling | LIVE | 2026-08-02 · user | `cowork_score_census.md` §8c |
| D-487 | The eleven snapshot source scores are frozen and hash-pinned; changing the set or bumping a pin is a deliberate golden and gate re-baseline | LIVE | 2026-08-04 · user | `docs/score_inventory.md` |
| D-488 | The two Bach chorale collections are independent selections, not sub- and superset — and the diff between them is not recoverable in-repo | LIVE | 2026-08-04 · user | `docs/score_inventory.md` |
| D-513 | A corpus registry's content summary is enumeration provenance, not evidence that an annotation layer is present — per-slice presence must be measured | LIVE | — | `cowork_census_full_needs_audit.md` ⚠gap |
| D-514 | A newly acquired annotation set whose works OVERLAP the regression corpus is RECORD-ONLY: it may not be wired to, compared against, or bulk-diffed with the gate corpus without a user ruling | LIVE | — | `cowork_census_full_needs_audit.md` ⚠gap |
| D-515 | Pedal-point ground truth gets its OWN needs row rather than riding as a note on another — the user's reason: it can improve inference precision and nothing is lost | LIVE | — | `cowork_census_full_needs_audit.md` ⚠gap |
| D-516 | Two ground-truth classes with named consumers but no needs row were ADOPTED at the first full-needs audit — contrapuntal/imitative structure, and marked part-writing errors | LIVE | — | `cowork_census_full_needs_audit.md` ⚠gap |

## S. The guiding principles — [full entries](decisions/group_S.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-165 | #1 - build only on established fact and theory | LIVE | — | `CLAUDE.md` |
| D-166 | #2 - target the specific open question, not the general topic | LIVE | — | `CLAUDE.md` |
| D-167 | #3 - an unexpected finding is a failure to diagnose, not a curiosity | LIVE | — | `CLAUDE.md` |
| D-168 | #4 - the long-term goal is maximum-precision inference | LIVE | — | `CLAUDE.md` |
| D-169 | #5 - when facts may be scarce, investigate | LIVE | — | `CLAUDE.md` |
| D-170 | #6 - total unification: one path per concern | LIVE | — | `CLAUDE.md` |
| D-171 | #7 - a layer is enhanced only with what belongs to it | LIVE | — | `CLAUDE.md` |
| D-172 | #8 - no inference-problem-driven coding until every method sits in its correct layer | LIVE | — | `CLAUDE.md` |
| D-173 | #9 - measure only on corpora known to be non-stale and accurate | LIVE | — | `CLAUDE.md` |
| D-174 | #10 - documentation always in sync with code | LIVE | — | `CLAUDE.md` |
| D-175 | #11 - regression tests in sync with code, and run between iterations | LIVE · derivation not recorded | — | `CLAUDE.md` |
| D-176 | #13 - surface a surprise as a stop before building around it | LIVE | — | `CLAUDE.md` |
| D-177 | #14 - every behavior change is one user-ratified, revertible, provenance-stamped commit | LIVE · derivation not recorded | — | `CLAUDE.md` |
| D-178 | #15 - verify at the objects on the full output surface, never at an assertion | LIVE | — | `CLAUDE.md` |
| D-179 | #16 - every measurement is stamped to its corpus and its tooling, and the outgoing reference is snapshotted | LIVE | — | `CLAUDE.md` |
| D-180 | #17 - the Premise Gate | LIVE | — | `CLAUDE.md` |
| D-181 | #18 - an unverified causal premise is forbidden (Class A) | LIVE | — | `CLAUDE.md` |
| D-182 | #19 - an unestablished measurement tool is forbidden (Class B) | LIVE | — | `CLAUDE.md` |
| D-183 | #20 - fit and evaluation are separated | LIVE | — | `CLAUDE.md` |
| D-184 | #21 - ground truth is a measurement tool too, and its accuracy is measured | LIVE | — | `CLAUDE.md` |
| D-185 | #22 - every hard gate declares in advance how it handles the largest change it will meet | LIVE | — | `CLAUDE.md` |
| D-186 | #23 - an end-state principle needs a lawful transition | LIVE | — | `CLAUDE.md` |
| D-187 | #24 - every reported figure carries its uncertainty | LIVE | — | `CLAUDE.md` |
| D-188 | The constrained-optimum ledger corollary | LIVE | — | `CLAUDE.md` |
| D-189 | The scope of surprise, and the three-stage funnel | LIVE | — | `CLAUDE.md` |
| D-190 | The decision-neutrality corollary - what exists carries no weight in choosing a design | LIVE | — | `CLAUDE.md` |
| D-200 | Make it work first; compromise on performance only if performance proves a problem | LIVE | — | `CLAUDE.md` |
| D-201 | Very large scores must be handled, and are expected to be more common than our corpora | LIVE | — | `ARCHITECTURE.md` |
| D-202 | The effort control is one setting with several dials, and it must bound the time taken | DEFERRED | — | `ARCHITECTURE.md` |
| D-203 | Candidate admission is completion, not refinement - so #8 permits fixing it now | LIVE | — | `CLAUDE.md` |
| D-204 | One fix is designed once over the whole enumerated family, never per symptom | LIVE | — | `CLAUDE.md` |
| D-205 | A human acts as ground truth where no formal ground truth exists | LIVE | — | `ARCHITECTURE.md` |
| D-206 | Intonation is held as a future feature, and is a declared future consumer of the analysis | DEFERRED | — | `ARCHITECTURE.md` |
| D-277 | Measure before build - and a byte-identical structural refactor is exempt, because byte-identity is its prediction | LIVE | 2026-08-02 · user | `cowork_engage_arc_plan.md` |

## T. Standing process rules and local patches — [full entries](decisions/group_T.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-196 | The self-check: re-read the diff against the principles before reporting | LIVE | — | `CLAUDE.md` |
| D-197 | The distribution constraint - the import-fix patch is fork-local and never goes upstream | LIVE | — | `CLAUDE.md` |
| D-198 | The Windows snap fix in the muse submodule is intentional and must not be reverted | LIVE | — | `CLAUDE.md` |
| D-199 | The MusicXML declared-mode import fix is intentional and must not be reverted | LIVE | — | `CLAUDE.md` |
| D-208 | A withheld finding never enters a mandatory session-start read | LIVE | — | `cowork_audit_protocol.md` |
| D-209 | Code that is about to be deleted gets no audit - only the no-information-loss check at deletion | LIVE | — | `cowork_audit_protocol.md` |
| D-231 | Issue-exhaustion and specification completion before any fix design - the three-phase sequencing rule | LIVE | — | `CLAUDE.md` |
| D-249 | The whole decision surface is delivered as user-visible text before any choice question | LIVE | 2026-08-02 · user | `CLAUDE.md` |
| D-250 | Dispatches are written only when they are next; a parked instruction is revalidated first | LIVE | 2026-08-02 · user | `cowork_audit_protocol.md` |
| D-251 | A running dispatch is never interrupted or steered mid-flight; every instruction is self-sufficient | LIVE | 2026-08-02 · user | `cowork_audit_protocol.md` |
| D-252 | One side writes the instruction files and the other executes them, never the reverse | LIVE | 2026-08-02 · user | `cowork_audit_protocol.md` |
| D-253 | Working-tree files are read with the file tools; bash is limited to git object queries by explicit hash | LIVE | 2026-08-02 · user | `CLAUDE.md` |
| D-254 | Investigate by default; never ask the user whether to investigate or proceed | LIVE | 2026-08-02 · user | `CLAUDE.md` |
| D-258 | A prune and tidy pass runs before any publish of the fork, and nothing on its list is acted on before it | DEFERRED | 2026-08-02 · user | `cowork_prune_pass_checklist.md` |
| D-259 | Every upstream contribution is checked against the distribution constraint before it is posted | LIVE | 2026-08-02 · user | `cowork_prune_pass_checklist.md` |
| D-279 | The Stage-3 entry gate - seven conditions before any engagement wiring reaches production | LIVE | 2026-08-02 · user | `cowork_engage_arc_plan.md` “The stages” |
| D-298 | The layer-by-layer audit - each layer is audited once its pieces are in place | LIVE | 2026-08-02 · user | `cowork_audit_protocol.md` |
| D-314 | A correction rule kept for structural reasons must keep producing evidence that it still fires | LIVE | 2026-08-02 · user | `cowork_stage5_fitter_design.md` “§15 Open items & ratification asks” |
| D-316 | The chord-symbol parser sussus fix is a recorded local patch with an UPSTREAMABLE distribution disposition | LIVE | — | `CLAUDE.md` |
| D-415 | An item on the roadmap may be marked done only with the evidence its own verify column names | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` |
| D-417 | The engage criteria — six gates that must all hold, a staged plan, and the user ratification event | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` |
| D-418 | The retirement map — nothing retires by silence; ten named retirements, each with its trigger and its order | LIVE | 2026-08-03 · user | `docs/implementation_roadmap.md` |
| D-431 | A figure enters a dispatch or a report by citation to a generated artifact, never by transcription — and so does a premise | LIVE | — | `cowork_audit_protocol.md` |
| D-434 | The writing side runs the standing self-check before a dispatch is released, and records its output | LIVE | — | `cowork_audit_protocol.md` |
| D-436 | A mechanism is judged on three measured conditions — automatic, detection rate, false-positive rate — and a failing one is REPORTED, not automatically removed | LIVE | — | `cowork_audit_protocol.md` |
| D-437 | Phase 3 waits on the phase-2 items that could find another member of the family being designed for, not on all of phase 2 | LIVE | — | `CLAUDE.md` |
| D-438 | Open-items register rows whose subject is this project's own tracking and documentation apparatus gate nothing — but an establishment obligation always gates | LIVE | — | `CLAUDE.md` |
| D-439 | The perspective inventory's §4 is the one home for the enumerated discovery channels, and CLAUDE.md's phase-2 clause points at it instead of listing its own subjects | LIVE | — | `CLAUDE.md` |
| D-473 | A theory-grounding pass labels every load-bearing claim FACT / THEORY / CONJECTURE, cross-checks its central sources independently, and carries no equation out of a text it could not fetch | LIVE | 2026-08-04 · user | `cowork_term_theory_grounding.md` ⚠gap |

## U. The standing decision-bearing surfaces — [full entries](decisions/group_U.md)

| ID | Decision | Status | Entry ratified | Home |
|---|---|---|---|---|
| D-213 | The defect-type catalog is the living list of every problem type, and it is added to at discovery | LIVE | — | `DEFECT_TYPES.md` |
| D-214 | The dim7 characteristic bonus is the rotation selector and may not simply be removed | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-215 | Gating the root-continuity bonus on a sparse predecessor is a dead end | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-216 | The stepwise-bass bonus's four gates are each load-bearing | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-217 | The segmentation phase must suppress every context-dependent bonus | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-218 | Template array sizes derive from one constant, so the compiler enforces them | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-219 | Gates B, C and D were unreachable and were removed; no temporal condition may be added to the enharmonic flip | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-220 | The augmented-seventh guard requires both the major third and the augmented fifth | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-221 | A sparse upper-register lowest note does not earn inversion bonuses | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-222 | If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used | LIVE ⚠LEGACY · derivation not recorded | — | `docs/scoring_model.md` |
| D-223 | A gate that judges the pre-correction winner reads a snapshot, not the live result | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |
| D-224 | Joint bass-and-chord scoring requires accumulated regional evidence | LIVE ⚠LEGACY · derivation not recorded | — | `docs/scoring_model.md` |
| D-225 | A corpus is regenerated before its baseline figures are updated | LIVE | — | `BUILD_AND_TEST.md` |
| D-226 | The music21 export is version-pinned; regenerating it is a deliberate re-baseline | LIVE | — | `tools/REPRODUCIBILITY.md` |
| D-281 | The batch measurement tool must emit the structured fields on every alternative, or the corpus figures silently revert | LIVE | 2026-08-02 · user | `docs/iteration_path1_summary.md` “Architecture decisions made during this path” ⚠gap |

## Provenance of this register

- Adjudication: the OI-207 decision-conformance adjudication, 2026-08-01, at commit `58dea6702ac8aa9d5ef8b89244b94d587a75f7a5`.
- Coverage figures above regenerated at commit `0f311091c147a6200e6ddd96702fc5c63507799d`.
- Backbone data: `tools/audit/decisions/backbone_decisions.json` (sha256 `38ec4aa4dfc1d2c1…`).
- Harvest: `tools/audit/decisions/decision_candidates.json` (sha256 `51850440b315e6e9…`).
- Clustering: `tools/audit/decisions/decision_clusters.json` (sha256 `0615b1e61bf10332…`).
- Shape: `open_items/OI-208.md` (user-ratified 2026-07-28).
- Standing rule for keeping it current: a new ratification, shelving or falsification gets its entry in `backbone_decisions.json` — and a regenerated `DECISIONS.md` — in the same commit that records it.

