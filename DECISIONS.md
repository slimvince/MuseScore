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
> upstreamable disposition, the OI-273 ruling). The register-level ratification does not overwrite
> per-entry provenance — an entry saying "ratifier not stated" still means the original record
> of THAT decision does not say; what the 2026-08-02 ratifications establish is that these
> entries are the standing decisions of record.
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

Each entry has six parts.

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
- **Home** — where the decision is actually recorded, as `file:line`. A decision about how a
  layer should work belongs in that layer's section of `ARCHITECTURE.md`, and a decision about
  anything else belongs in the specification that owns it. Where the home is neither, the entry
  says which of four cases it is: a **documentation gap** (a decision that governs a layer or a
  component, not findable from that layer's section — it carries an `OPEN_ITEMS.md` row); a
  decision **recorded only on a tracking surface** (an open-item row or a session handoff block —
  a place for tracking work, not a home for a standing decision); a **project-wide convention**
  with no owning layer, correctly homed in `CLAUDE.md` or the architectural principles; or a
  **decision about the process**, not about the system.
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

**316 decisions**, grouped by subject. They were enumerated by reading `ARCHITECTURE.md` and `CLAUDE.md` in full, because a decision written as plain specification carries no ruling vocabulary and no text search can find it, and by following the recorded rulings that live only in an open-item row, a handoff block, or one of the standing decision-bearing surfaces. Every verbatim quote below is mechanically checked to exist at the place it is cited to, and to start at the line it is cited to (`gen_cluster_dispositions.py --verify`), and every `D-…` and `OI-…` cross-reference is checked to resolve.

| | Count |
|---|---|
| Decisions recorded | **316** |
| — of which live | 263 |
| — of which superseded in fact | 5 |
| — of which superseded by | 9 |
| — of which deferred | 38 |
| — of which shelved with evidence | 1 |
| Decisions whose date is not stated in the record | 195 |
| Decisions whose ratifier is not stated in the record | 194 |
| Decisions recorded outside the specification that owns them | 125 |
| — of which a documentation gap | 28 |
| — of which recorded only on a tracking surface, with no home at all | 27 |
| — of which a project-wide convention, correctly homed | 34 |
| — of which a decision about the process, correctly homed | 36 |
| Decisions whose defense the record does not state | 45 |

That last row is the one meant to fall. **271 of 316** decisions here can point at the research, the measurement, or the constraint that decided them; the rest cannot, and say so. Filling a gap means recording the defense where the decision lives — never writing one afterwards from memory.

Alongside the register, every one of the harvested statements about decisions in this repository has been given a recorded disposition, so that none was silently passed over:

| | Count |
|---|---|
| Harvested statements | **15224** |
| Groups of near-identical statements ("clusters") | **14460** |
| Clusters carrying a recorded disposition | **14460** |
| — restates | 5511 |
| — not-a-decision | 5564 |
| — boilerplate | 74 |
| — no-spec-home | 594 |
| — unresolved | 2717 |

The full disposition table, and the numbered rule behind each one, are in `tools/audit/decisions/cluster_dispositions.csv` and `tools/audit/decisions/disposition_manifest.json`.

### What was read, and what was not

**Read in full.** ARCHITECTURE.md IN FULL (all 6,523 lines: the preamble, §1 Project Overview, §2 Architectural Principles, §3 Directory Structure including the Layer 1-6 specifications, §4 Existing Components, §5 Planned Analysis Extensions, §6 The Style System, §7 The Knowledge Base, §8 Planned Generation Components, §9 The Constraint System, §10 Visualization, §11 Intonation, §12 User Interface, §13 File Persistence, §14 ML Readiness, §15 Development Phases, §16 Scope Reference, §17 Coding Standards, §18 Contributing, §19 LLM Integration, and both appendices). Lines 1-3981 were read by the 2026-08-01 adjudication; §1 and §6-§19 plus the appendices by the 2026-08-01 completion pass. Also in full: CLAUDE.md (the guiding principles, the ratified corollaries, the gate and preset policy, the conventions, the local patches, the self-check). Targeted and cited: OPEN_ITEMS.md and its detail files, cowork_handoff.md, docs/scoring_model.md §8, DEFECT_TYPES.md, BUILD_AND_TEST.md, tools/REPRODUCIBILITY.md, cowork_confidence_contract.md, cowork_joint_estimator_factorization.md, cowork_design_doc_template.md.

**Not read in full.** The per-layer and per-component design documents (cowork_layer*_design.md, cowork_progression_schema_dictionary.md, cowork_voiceleading_axis_design.md, cowork_bounded_context_design.md and their siblings), which ARCHITECTURE.md §doc-governance names as the authoritative DETAIL for their own scope; both archives (STATUS_ARCHIVE.md, cowork_handoff_archive.md); and the cc_* session reports. Each was opened where a specific citation required it and is not claimed to be swept.

**The remainder, measured.** The harvest holds 15,224 candidate statements, of which 241 are sourced to ARCHITECTURE.md - all 241 now fall inside the range read in full. 6,374 clusters carry the 'unresolved' disposition: statements the pass could not mechanically classify as either restating a register decision or not being a decision. Sampling shows that residual is genuinely mixed - real rulings, deferred designs and ordinary narrative in one population - so it bounds what this register may claim about the documents it did not read in full.

*Why this is stated at all:* DEFECT_TYPES.md DT-26 — scope-assumed enumeration. A sweep that is complete inside its own file set reads as complete about the whole question. The scope and its measured remainder are therefore stated rather than left implicit.

---

## A. The estimator architecture — the joint estimator — [full entries](decisions/group_A.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-001 | Key, mode and chord are inferred by ONE joint decode | LIVE | `ARCHITECTURE.md` |
| D-002 | The fitted tables and weights are compiled into the binary verbatim | LIVE | `ARCHITECTURE.md` |
| D-003 | Inference is preset-independent; presets are presentation concerns | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-004 | The decode state space and the segment cap | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-005 | The joint estimator is the production inference layer on the batch and corpus surface | LIVE | `ARCHITECTURE.md` |
| D-006 | The published uncertainty surface is two full candidate lists, with no truncation | LIVE | `ARCHITECTURE.md` |
| D-007 | The published scores are log-scores, not probabilities | LIVE | `ARCHITECTURE.md` |
| D-008 | The true probabilities are deferred to a later step | DEFERRED | `ARCHITECTURE.md` |
| D-095 | The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state | SUPERSEDED IN FACT | `ARCHITECTURE.md` |
| D-096 | Fitted values are fit once against ground truth, never per-case tuned | LIVE | `ARCHITECTURE.md` |
| D-097 | Held-out evaluation and a capacity budget are declared before any fit | LIVE | `ARCHITECTURE.md` |
| D-098 | The exact-decode reserve - the declared prune was never adopted | LIVE | `ARCHITECTURE.md` |
| D-114 | The decoder commits its best path; there is no abstention on the key axis | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-270 | The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file | LIVE | `cowork_prefit_gates.md` ⚠gap |
| D-271 | The capacity budget - a cell keeps its own estimate only above a stated count, and free parameters are bounded against the training tokens | LIVE | `cowork_prefit_gates.md` ⚠gap |
| D-272 | The protocol constants are protocol, not tuning - changing one is an amendment, never a fitting act | LIVE | `cowork_prefit_gates.md` ⚠gap |
| D-273 | The architecture-adoption variant of the hard regression stop, written before any diff existed | LIVE | `cowork_prefit_gates.md` ⚠gap |
| D-274 | The reverse map - if the new estimator is not adopted it is removed whole, and the retirement map is void | LIVE | `cowork_prefit_gates.md` ⚠gap |
| D-283 | Meta-finding: never learn keys, the lever is keychain structure - superseded by the joint estimator and the forms-from-theory rule | SUPERSEDED BY D-001 and D-096 | `cowork_architecture_reassessment.md` ⚠gap |
| D-285 | Meta-finding: embellishment is chord-first, never a richer vocabulary - absorbed by the emission design and the ornament-label increment | SUPERSEDED BY the ratified factorization emission design (D-004 and the OI-194 increment) | `cowork_architecture_reassessment.md` ⚠gap |

## B. The notation output surface and the record path — [full entries](decisions/group_B.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-009 | The notation record is the ONE surface the in-app path reads, and it never re-decodes | LIVE | `ARCHITECTURE.md` |
| D-010 | The switch - the record path is the production in-app notation analysis | LIVE | `ARCHITECTURE.md` |
| D-011 | The producer decodes the WHOLE score once, and does not cache | LIVE | `ARCHITECTURE.md` |
| D-012 | Failure is unambiguous - never a partial record, never a silent fallback | LIVE | `ARCHITECTURE.md` |
| D-013 | Which staves feed the analysis is decided at the fact adapter, not by a later filter | LIVE | `ARCHITECTURE.md` |
| D-014 | The two seams read the record as pure views - no recomputation | LIVE | `ARCHITECTURE.md` |
| D-015 | A boundary tick belongs to the segment it starts | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-016 | Display renderings are presentation; facts are published | LIVE | `ARCHITECTURE.md` |
| D-017 | The inference/presentation boundary is guarded mechanically, both ways | LIVE | `ARCHITECTURE.md` |
| D-018 | The key-exposure bucket is decided once, at one site | LIVE | `ARCHITECTURE.md` |
| D-019 | The record arm publishes the raw key-axis gap, with no remapping to 0..1 | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-020 | The interactive path bypasses the old window cache and has none of its own | LIVE | `ARCHITECTURE.md` |
| D-021 | The pedal-point fields are suspended on the record arm | DEFERRED | `ARCHITECTURE.md` |
| D-275 | Every published record carries its own instrument provenance; a provenance-less analysis cannot exist | LIVE | `cowork_notation_output_contract.md` ⚠gap |
| D-276 | Modal colour is published as un-rounded per-degree counts; no mode label is inferred or published anywhere | LIVE | `cowork_notation_output_contract.md` ⚠gap |

## C. Cross-cutting analysis contracts — [full entries](decisions/group_C.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-022 | The founding principle - analyse at the finest grain, coarser views are derived | LIVE | `ARCHITECTURE.md` |
| D-023 | The atomic analysis unit is the constant-sonority slice, never the metric beat | LIVE | `ARCHITECTURE.md` |
| D-024 | The fact layers are style-agnostic; style lives only in calibration | LIVE | `ARCHITECTURE.md` |
| D-025 | Forward-only, with two scoped escapes | SUPERSEDED BY D-001 | `ARCHITECTURE.md` |
| D-026 | The global joint-lattice decode was measured inert (2026-06-29) | LIVE | `ARCHITECTURE.md` |
| D-027 | Every layer emits ranked candidates plus a confidence, never a forced point estimate | LIVE | `ARCHITECTURE.md` |
| D-028 | The span typology - every layer names the span it operates on; bare 'region' is banned | LIVE | `ARCHITECTURE.md` |
| D-029 | The verifiability contract | LIVE | `ARCHITECTURE.md` |
| D-030 | Bounded context - cost scales with the working span, not the whole score | LIVE | `ARCHITECTURE.md` |
| D-031 | Whole-score analysis is the degenerate case, not the design | LIVE | `ARCHITECTURE.md` |
| D-032 | Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named | LIVE | `ARCHITECTURE.md` |
| D-033 | Each layer owns one evidence-source-times-question contribution and uses all of L1's information | LIVE | `ARCHITECTURE.md` |
| D-034 | A new layer or axis is admitted only through three co-equal gates | LIVE | `ARCHITECTURE.md` |
| D-035 | The effort setting - every cost-driving choice is a setting, never a hardcoded constant | LIVE | `ARCHITECTURE.md` |
| D-036 | Accumulating gates are a warning sign - add iteration, not more gates | LIVE | `ARCHITECTURE.md` |
| D-099 | Negative evidence is information - a ruled-out possibility is carried, not dropped | LIVE | `ARCHITECTURE.md` |
| D-100 | Every derived fact is published exactly once, on the producing layer's output surface | LIVE | `ARCHITECTURE.md` |
| D-115 | The regression stop is the granularity-robust unit; root governs, key and Roman numeral ride beside | LIVE | `CLAUDE.md` |
| D-191 | The two-tier regression class policy - functional regression stops, rotation churn is tracked | LIVE | `CLAUDE.md` |
| D-210 | An exotic mode is graded against its parent collection's minor key, not its own tonic triad | LIVE | `CLAUDE.md` |
| D-211 | Key agreement is reported against both the global home key and the local key | LIVE | `CLAUDE.md` |
| D-212 | The regression stop is abstain-aware: an abstention counts as disagreement on root | LIVE | `CLAUDE.md` |
| D-243 | The planning band for the vertical engine, and the corpora excluded from it | SUPERSEDED IN FACT | `ARCHITECTURE.md` |
| D-260 | Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-261 | A layer never guesses how much context it needs - the amount is discovered by convergence | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-262 | The extension increment is chosen by the requesting layer, not by the layer that supplies the notes | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-263 | A refused or truncated extension is marked on the output, never silently absorbed | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-264 | Extension is an optimisation of load-more-then-rerun: any sequence of extensions equals one fresh run | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-265 | Asking a lower layer for more notes is a data-supply call, not a backward inference edge | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-266 | Layer 6 is prohibited until the bounded-context design is coded and regression-tested for Layers 1 to 5 | LIVE | `cowork_bounded_context_design.md` ⚠gap |
| D-267 | There are exactly two admissible confidence classes, and no layer may claim a calibrated probability until one is fitted | LIVE | `cowork_confidence_contract.md` ⚠gap |
| D-268 | A confidence attaches to a named decision, is compared only within its class and a declared frame, and keeps its identity downstream | LIVE | `cowork_confidence_contract.md` ⚠gap |
| D-269 | The frame table is the one home of the override arithmetic; a new override site declares its frame before it is built | LIVE | `cowork_confidence_contract.md` ⚠gap |
| D-278 | The joint key-and-chord step is SHELVED - measured not to pay | SHELVED WITH EVIDENCE | `cowork_engage_arc_plan.md` ⚠gap |
| D-282 | Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy | SUPERSEDED BY D-115 and D-191 | `cowork_architecture_reassessment.md` ⚠gap |
| D-286 | Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-288 | Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-289 | Meta-principle: precision lives in the evidence and the functional labelling, not in the search | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-293 | Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-294 | The only ground truth is the human annotation; the algorithmic analysis is a filter, and no self-annotation ever enters a measurement | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-297 | Correction of record: never computing a possibility is not information loss; only discarding a computed one is | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-313 | A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target | LIVE | `cowork_stage5_fitter_design.md` ⚠gap |

## D. Layer 1 — the note model — [full entries](decisions/group_D.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-037 | The note model is the single source of truth for what sounds, and reads the score once | LIVE | `ARCHITECTURE.md` |
| D-038 | Tied notes are one event; spans are answered by overlap with no horizon | LIVE | `ARCHITECTURE.md` |
| D-039 | Ineligible notes are kept and flagged, never dropped | LIVE | `ARCHITECTURE.md` |
| D-040 | The tie-unresolved atoms are republished additively for the joint estimator | LIVE | `ARCHITECTURE.md` |

## E. Layer 2 — the slicer — [full entries](decisions/group_E.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-041 | The slicer output covers the domain with no gaps and no overlaps | LIVE | `ARCHITECTURE.md` |
| D-042 | Slice boundaries are every onset AND every release | LIVE | `ARCHITECTURE.md` |
| D-043 | Slice identity IS the eligible sounding-note set | LIVE | `ARCHITECTURE.md` |
| D-044 | A note that opens no boundary still rides along in the slice's sounding set | LIVE | `ARCHITECTURE.md` |
| D-045 | The slicer re-decides nothing about eligibility | LIVE | `ARCHITECTURE.md` |
| D-046 | Zero interpretation - the slicer applies no thresholds and no musical judgment | LIVE | `ARCHITECTURE.md` |
| D-047 | No special-casing of any note kind | LIVE | `ARCHITECTURE.md` |
| D-048 | Boundaries are necessary but not sufficient; over-grab is structurally impossible | LIVE | `ARCHITECTURE.md` |
| D-049 | An interior stretch where everything rests is an explicit empty slice, not a gap | LIVE | `ARCHITECTURE.md` |
| D-050 | Slicing is clipped to the loaded span and never drags outside it | LIVE | `ARCHITECTURE.md` |

## F. Layer 3 — key and mode — [full entries](decisions/group_F.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-051 | The production key/mode path is the sequence decoder, not the per-stretch resolver | SUPERSEDED BY D-001 · derivation not recorded | `ARCHITECTURE.md` |
| D-052 | The signature read and declared-mode mapping live in ONE shared function | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-053 | The tick-local path keeps the older resolver (the ratified P4-defer) | SUPERSEDED IN FACT · derivation not recorded | `ARCHITECTURE.md` |
| D-054 | All 21 modes are scored against all 12 tonics; the harmonic major family is deferred | DEFERRED | `ARCHITECTURE.md` |
| D-055 | The 21 mode priors are independent and user-configurable | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-056 | Notes always win - the notated key signature is a weak hint, not a bypass | LIVE | `ARCHITECTURE.md` |
| D-057 | The priority of evidence - actual sounding notes are the strongest evidence | LIVE | `ARCHITECTURE.md` |
| D-058 | The piece-start shortcut | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-059 | The temporal window - 16 beats back, 8 beats forward, decayed | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-235 | Tonal-centre disambiguation may break a close tie but may not overturn a stronger raw winner | LIVE | `ARCHITECTURE.md` |
| D-287 | Key-as-distribution is SHELVED - its motivating case was already fixed and no live target was found | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-290 | The key-agnostic local cadence approach is FALSIFIED at its precision ceiling | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-306 | The key layer's backward re-reading stays switched off in the shipped configuration | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |

## G. Layer 4 — chord identity — [full entries](decisions/group_G.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-060 | The legacy chord analyzer is a vertical sonority analyzer - keep the boundary clean | LIVE | `ARCHITECTURE.md` |
| D-061 | Gate thresholds are Baroque-calibrated and must not be loosened for other styles | LIVE | `ARCHITECTURE.md` |
| D-062 | Progression signals are withheld while segmentation is being explored | LIVE | `ARCHITECTURE.md` |
| D-063 | Cold context on the tick-local path is the accepted contract | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-064 | The chord-scoring presets are a measurement-only artifact | SUPERSEDED IN FACT · derivation not recorded | `ARCHITECTURE.md` |
| D-065 | The look-ahead divergence between the two paths is intentional and load-bearing | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-066 | Chord symbols written in the score are never analyzer input | LIVE | `ARCHITECTURE.md` |
| D-067 | Jazz mode (chord-symbol-driven boundaries) is retired | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-068 | The chord identifier needs at least three distinct pitch classes | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-069 | Two identity modes for merged stretches - harmonic summary and as-written | DEFERRED · derivation not recorded | `ARCHITECTURE.md` |
| D-101 | Contextual inversion bonuses fire only for major and minor candidates | SUPERSEDED BY D-102 | `ARCHITECTURE.md` |
| D-102 | Augmented and half-diminished candidates receive the inversion bonuses too (Iter 46) | LIVE | `ARCHITECTURE.md` |
| D-103 | Pedal-point detection is a second pass, accepted only on two conditions | SUPERSEDED BY D-207 | `ARCHITECTURE.md` |
| D-104 | The bass-is-root bonus is conditioned on corroborating support | LIVE | `ARCHITECTURE.md` |
| D-105 | The spelling written in the score is read through ONE shared interpreter | LIVE | `ARCHITECTURE.md` |
| D-207 | The pedal-point class is defined voice-independently, superseding the bass-only fact | DEFERRED | `ARCHITECTURE.md` |
| D-236 | Chord-symbol trust is per symbol, not a per-score preference | DEFERRED | `ARCHITECTURE.md` |
| D-237 | Only a symbol marked trusted becomes analyzer input; an untrusted symbol is never read | DEFERRED | `ARCHITECTURE.md` |
| D-238 | Two pitch classes may nominate a chord but may not finalize one; one pitch class may not | DEFERRED | `ARCHITECTURE.md` |
| D-239 | Chord identity stays local; expansion is by one neighbouring region and is bounded | DEFERRED | `ARCHITECTURE.md` |
| D-240 | The monophonic smoothing terms are tunable parameters, not prose-only rules | DEFERRED | `ARCHITECTURE.md` |
| D-241 | The monophonic local-grouping problem is deferred to Phase 2 | DEFERRED | `ARCHITECTURE.md` |
| D-242 | Vertical and monophonic raw scores are never compared directly | DEFERRED | `ARCHITECTURE.md` |
| D-280 | Gates read structured fields only - never a chord symbol string and never a Roman numeral | LIVE | `docs/iteration_path1_summary.md` ⚠gap |
| D-284 | Meta-finding: selection/competition is saturated, stop adding re-ranking gates - superseded by the gates doctrine and the adoption | SUPERSEDED BY D-036 with D-001/D-010 | `cowork_architecture_reassessment.md` ⚠gap |
| D-299 | No negative-margin guard may be added - it would break every intentional backward-swap gate | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-300 | Gate M (minor read as diminished) is DEFERRED and must not be retried without a new runtime signal | DEFERRED | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-301 | Gate N (major read as an inverted minor) is DEFERRED and must not be retried without a multi-region model | DEFERRED | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-302 | No further local scoring fix for inversions may be attempted — the remaining divergence is not an analyzer defect | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-303 | Non-chord-tone detection is deferred, and if built it must be chord identification that knows about non-chord tones, never stripping after the fact | DEFERRED | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-305 | The ban on reading written harmony as analyzer input is decided by what an annotation says, not by how it is stored | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-312 | The carried alternative readings are inside the byte-identity acceptance contract — same winner with different alternatives is a behavior change | LIVE | `cowork_stage5_fitter_design.md` ⚠gap |

## H. Layer 5 and Layer 6 — function, cadence, grouping — [full entries](decisions/group_H.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-079 | The function layer annotates and resolves; it never rewrites the committed chord | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-080 | Carried abstentions are resolved by selecting among the carried readings, never re-derived | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-081 | The cadence detector is key-agnostic | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-082 | The grouping layer is additive, read-only, with no feedback | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-083 | Hierarchy, periods and prolongation are out of the validatable core | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-084 | The progression-schema recognizer is a consumer of the function layer, not a new layer | DEFERRED · derivation not recorded | `ARCHITECTURE.md` |
| D-085 | The voice-leading axis is a separate axis with its own layers | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-248 | Tonicization labels are not implemented and are deferred | DEFERRED | `ARCHITECTURE.md` |
| D-291 | The tonicization labeller is NOT wired, and the metric is NOT changed to credit it - both would hide a real key error | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |

## I. Module boundaries and code structure — [full entries](decisions/group_I.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-070 | Style behaviour is fully data-driven - no conditional logic on style identity | LIVE | `ARCHITECTURE.md` |
| D-071 | The analysis layer never produces display strings | LIVE | `ARCHITECTURE.md` |
| D-072 | The dependency rule - the analysis library knows nothing about the score format | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-073 | Single implementation for shared logic; mirroring is a last resort | LIVE | `ARCHITECTURE.md` |
| D-074 | Analyze and suggest - never modify the score without explicit user action | LIVE | `ARCHITECTURE.md` |
| D-075 | Interface-based design for machine-learning substitutability | LIVE | `ARCHITECTURE.md` |
| D-076 | Score inspection before diagnosis | LIVE | `ARCHITECTURE.md` |
| D-077 | The configuration interface is split into two narrow IoC interfaces | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-078 | The cross-layer value types live in a dependency-free leaf header | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-107 | American English throughout | LIVE | `ARCHITECTURE.md` |
| D-108 | Cross-platform by default | LIVE | `ARCHITECTURE.md` |
| D-227 | Read how MuseScore already does it, and never invent parallel infrastructure | LIVE | `ARCHITECTURE.md` |
| D-228 | The bridge pattern - engraving types enter and leave at named free functions in the notation namespace | LIVE | `ARCHITECTURE.md` |
| D-229 | The MuseScore-dependency rule - one general rule for what our code may depend on | LIVE | `ARCHITECTURE.md` |
| D-233 | Build and test commands run synchronously; one run, one result | LIVE | `ARCHITECTURE.md` |
| D-296 | READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-311 | The chord-analyzer file split happens once, after the retirements have settled — not before | DEFERRED | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |

## J. Presentation and output conventions — [full entries](decisions/group_J.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-086 | Roman numerals and Nashville numbers are presentation choices, not separate analyses | LIVE | `ARCHITECTURE.md` |
| D-087 | Display options live with the formatter, not with the analyzer preferences | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-088 | No automatic key signature injection | LIVE | `ARCHITECTURE.md` |
| D-089 | The legacy confidence exposure gates - 0.5 tentative, 0.8 assertive | SUPERSEDED BY D-018 · derivation not recorded | `ARCHITECTURE.md` |
| D-090 | Abstention is a valid outcome - high precision before coverage | LIVE | `ARCHITECTURE.md` |
| D-106 | The augmented-sixth labels are gated to the Standard and Baroque presets | SUPERSEDED IN FACT · derivation not recorded | `ARCHITECTURE.md` |
| D-234 | A chord symbol string must be valid under chords_std.xml; chords.xml is not relied on | LIVE | `ARCHITECTURE.md` |
| D-295 | Zero information loss to the end user - every inferred object must be displayable | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-304 | The analyzer always emits its fullest reading; simplifying it happens only when comparing against a corpus, never in the product | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |

## K. Documentation governance — [full entries](decisions/group_K.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-091 | ARCHITECTURE.md is the canonical architecture document and wins every disagreement | LIVE | `ARCHITECTURE.md` |
| D-092 | A cross-cutting contract is stated once and never redefined in a layer document | LIVE | `ARCHITECTURE.md` |
| D-093 | STATUS.md wins on current state; ARCHITECTURE.md on design | LIVE | `ARCHITECTURE.md` |
| D-094 | Each layer carries exactly one build state | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-109 | The open-items register is the one home for every unresolved issue, and the index is the status of record | LIVE | `OPEN_ITEMS.md` |
| D-110 | The decisions register records what was decided and its status - nothing else | LIVE | `open_items/OI-208.md` |
| D-111 | A decision belongs in the owning layer's specification; the register is an index | LIVE | `open_items/OI-208.md` |
| D-112 | Never work from memory instead of documented facts | LIVE | `CLAUDE.md` |
| D-113 | Music-theory words are reserved for their music-theory meaning | LIVE | `CLAUDE.md` |
| D-127 | An architectural decision that changes is documented in the same commit | LIVE | `ARCHITECTURE.md` |
| D-192 | A scoring change and its documentation land in the same commit | LIVE | `CLAUDE.md` |
| D-193 | The writing standards live in one place, and predicates must be qualified | LIVE | `CLAUDE.md` |
| D-194 | No self-invented labels, abbreviations, numbering schemes or jargon | LIVE · derivation not recorded | `CLAUDE.md` |
| D-195 | Every design decision carries its defense at its home | LIVE | `CLAUDE.md` |
| D-230 | The decisions register is a mandatory session-start read, and a new ruling lands in the register in the commit that records it | LIVE | `CLAUDE.md` |
| D-232 | The section numbers are authoritative; the "Rule N" labels are a legacy flat numbering | LIVE | `ARCHITECTURE.md` |
| D-255 | Every design document follows one fourteen-section structure, synthesized from three published standards | LIVE | `cowork_design_doc_template.md` |
| D-256 | Every design document opens with one of four declared status banners | LIVE | `cowork_design_doc_template.md` |
| D-257 | A specification carries a locator to its code and tests; code mechanics never do the explaining | LIVE | `cowork_design_doc_template.md` |
| D-307 | A specification cites code by function or section anchor, never by raw line number | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |

## L. Licensing, contribution, and coding standards — [full entries](decisions/group_L.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-116 | The system is a module inside MuseScore Studio, not a plugin | LIVE | `ARCHITECTURE.md` |
| D-117 | The long-term intent is an official contribution to MuseScore Studio | LIVE | `ARCHITECTURE.md` |
| D-118 | GPL v3, and every external library must be GPL v3 compatible | LIVE | `ARCHITECTURE.md` |
| D-119 | The MuseScore contributor licence agreement is signed before any pull request | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-120 | MuseScore's coding style is followed, with clang-format run before every commit | LIVE | `ARCHITECTURE.md` |
| D-121 | Where MuseScore's documentation practice is minimal, the higher standard applies | LIVE | `ARCHITECTURE.md` |
| D-122 | Every public class and method is documented in musical terms | LIVE | `ARCHITECTURE.md` |
| D-123 | Every non-obvious scoring weight or threshold explains its musical reasoning | LIVE | `ARCHITECTURE.md` |
| D-124 | The analyzer code must be readable by a musician | LIVE | `ARCHITECTURE.md` |
| D-125 | Every test documents the musical situation, the expected result, and what a failure means | LIVE | `ARCHITECTURE.md` |
| D-126 | One coherent piece of functionality per pull request | LIVE | `ARCHITECTURE.md` |
| D-292 | The fitting-pool licence constraint - values that ship are fitted only on freely-licensed music | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-315 | A one-line fix was made to MuseScore's own chord-symbol parser and is live in the fork | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |

## M. The style system and the knowledge base — [full entries](decisions/group_M.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-128 | Styles are defined entirely in data; adding one never requires code changes | LIVE | `ARCHITECTURE.md` |
| D-129 | Style conflicts resolve by a declared priority - explicit overrides always win | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-130 | The style loader never names a style in code | LIVE | `ARCHITECTURE.md` |
| D-131 | One shared style taxonomy, not two parallel vocabularies | LIVE | `ARCHITECTURE.md` |
| D-132 | The style taxonomy is a theory-based first version; grounding it empirically is committed work | DEFERRED | `ARCHITECTURE.md` |
| D-133 | The harmonic vocabulary is a queried reference component, not a layer of the analysis | LIVE | `ARCHITECTURE.md` |

## N. Generation, constraints, visualization, and the LLM integration — [full entries](decisions/group_N.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-134 | A voicing type is never requested directly; the style selects it | LIVE | `ARCHITECTURE.md` |
| D-135 | A fixed element is a hard constraint the optimizer may never modify | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-136 | The inference demo view is a developer tool and is not shipped | DEFERRED | `ARCHITECTURE.md` |
| D-137 | The harmony maps are our own visual design, and are chosen partly to avoid intellectual-property claims | DEFERRED | `ARCHITECTURE.md` |
| D-138 | Chord preview uses MuseScore's note-input pathway, not the playback pipeline | DEFERRED | `ARCHITECTURE.md` |
| D-139 | The language model holds no object references - every tool call carries its own musical address | DEFERRED | `ARCHITECTURE.md` |
| D-140 | The language model is a search agent and is never given the whole score | DEFERRED | `ARCHITECTURE.md` |
| D-141 | The language model sees what the user set, not what the engraving engine derived | DEFERRED | `ARCHITECTURE.md` |
| D-142 | The composing module is the language model's context provider; the model never re-derives harmony | DEFERRED | `ARCHITECTURE.md` |
| D-143 | The language-model bridge is built as a module but confined to the core access layer, so it can become a plugin | DEFERRED | `ARCHITECTURE.md` |

## O. Intonation — [full entries](decisions/group_O.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-144 | Percussion is excluded from analysis and tuning; fixed-pitch instruments are the tuning anchor | LIVE | `ARCHITECTURE.md` |
| D-145 | One preference chooses the tuning system, and no tuning code hardcodes one | LIVE | `ARCHITECTURE.md` |
| D-146 | A tie chain is one indivisible tuning event, and its tuning comes from one authority note | LIVE | `ARCHITECTURE.md` |
| D-147 | A slur, not a tie, joins the halves of a split note | LIVE | `ARCHITECTURE.md` |
| D-148 | The split is visible in the score; the invisible alternative is deferred | LIVE | `ARCHITECTURE.md` |
| D-149 | Only visible, sounding notes enter the pitch-class collection | LIVE | `ARCHITECTURE.md` |
| D-150 | The chord staff is the output, never an input to the analysis that fills it | LIVE | `ARCHITECTURE.md` |
| D-151 | Populating the chord staff overwrites whatever is in the selected range | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-152 | Roman numerals and Nashville numbers are never shown together on one staff | LIVE | `ARCHITECTURE.md` |
| D-153 | Interactive annotations are written in the score's normal colour; the batch pipeline writes red | LIVE | `ARCHITECTURE.md` |
| D-244 | Choosing an interval family for an ambiguous sonority is deferred; fixed tables are used | DEFERRED | `ARCHITECTURE.md` |
| D-245 | Voice role comes from staff position or explicit assignment; automatic melody detection is deferred | DEFERRED | `ARCHITECTURE.md` |
| D-246 | Fixed-pitch instruments are deferred, and will never receive tuning offsets | DEFERRED | `ARCHITECTURE.md` |
| D-247 | An anchor note stays at 12-TET, is never split, and is excluded from drift and centering | LIVE | `ARCHITECTURE.md` |

## P. The user interface, persistence, and machine-learning readiness — [full entries](decisions/group_P.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-154 | New panels use MuseScore's own panel and interface infrastructure | DEFERRED | `ARCHITECTURE.md` |
| D-155 | Every user-visible string goes through MuseScore's localization, in English and Swedish | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-156 | Accessibility follows MuseScore's existing patterns | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-157 | The harmonic-display preference exists for clarity, not for cost | LIVE | `ARCHITECTURE.md` |
| D-158 | Our data lives in separate files inside the score archive; the score file is never touched | DEFERRED | `ARCHITECTURE.md` |
| D-159 | Every custom file carries a format version, and the score file is never rewritten by our persistence | DEFERRED · derivation not recorded | `ARCHITECTURE.md` |
| D-160 | Arranger interactions are logged from the start, with consent, as future training data | DEFERRED | `ARCHITECTURE.md` |
| D-161 | Chord symbols already in a score are a second analyst's opinion, not ground truth | DEFERRED | `ARCHITECTURE.md` |

## Q. Scope and the development toolchain — [full entries](decisions/group_Q.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-162 | The development tools are not part of the shipping product | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-163 | The batch tool deliberately skips post-load layout | LIVE | `ARCHITECTURE.md` |
| D-164 | What is out of scope, and what degrades gracefully at the boundary | LIVE · derivation not recorded | `ARCHITECTURE.md` |
| D-308 | A newly acquired corpus enters as research material; the frozen regression corpus stays the gate until a deliberate re-baseline | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-309 | A corpus the analysis handles badly stays on the roadmap marked deferred; it is more valuable than one that confirms what already works | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |
| D-310 | Jazz accuracy is not measurable on the corpora held: the low agreement is missing bass and piano voicings, not a scoring failure | LIVE | `STATUS_ARCHIVE.md` ⚠tracking-surface-only |

## S. The guiding principles — [full entries](decisions/group_S.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-165 | #1 - build only on established fact and theory | LIVE | `CLAUDE.md` |
| D-166 | #2 - target the specific open question, not the general topic | LIVE | `CLAUDE.md` |
| D-167 | #3 - an unexpected finding is a failure to diagnose, not a curiosity | LIVE | `CLAUDE.md` |
| D-168 | #4 - the long-term goal is maximum-precision inference | LIVE | `CLAUDE.md` |
| D-169 | #5 - when facts may be scarce, investigate | LIVE | `CLAUDE.md` |
| D-170 | #6 - total unification: one path per concern | LIVE | `CLAUDE.md` |
| D-171 | #7 - a layer is enhanced only with what belongs to it | LIVE | `CLAUDE.md` |
| D-172 | #8 - no inference-problem-driven coding until every method sits in its correct layer | LIVE | `CLAUDE.md` |
| D-173 | #9 - measure only on corpora known to be non-stale and accurate | LIVE | `CLAUDE.md` |
| D-174 | #10 - documentation always in sync with code | LIVE | `CLAUDE.md` |
| D-175 | #11 - regression tests in sync with code, and run between iterations | LIVE · derivation not recorded | `CLAUDE.md` |
| D-176 | #13 - surface a surprise as a stop before building around it | LIVE | `CLAUDE.md` |
| D-177 | #14 - every behavior change is one user-ratified, revertible, provenance-stamped commit | LIVE · derivation not recorded | `CLAUDE.md` |
| D-178 | #15 - verify at the objects on the full output surface, never at an assertion | LIVE | `CLAUDE.md` |
| D-179 | #16 - every measurement is stamped to its corpus and its tooling, and the outgoing reference is snapshotted | LIVE | `CLAUDE.md` |
| D-180 | #17 - the Premise Gate | LIVE | `CLAUDE.md` |
| D-181 | #18 - an unverified causal premise is forbidden (Class A) | LIVE | `CLAUDE.md` |
| D-182 | #19 - an unestablished measurement tool is forbidden (Class B) | LIVE | `CLAUDE.md` |
| D-183 | #20 - fit and evaluation are separated | LIVE | `CLAUDE.md` |
| D-184 | #21 - ground truth is a measurement tool too, and its accuracy is measured | LIVE | `CLAUDE.md` |
| D-185 | #22 - every hard gate declares in advance how it handles the largest change it will meet | LIVE | `CLAUDE.md` |
| D-186 | #23 - an end-state principle needs a lawful transition | LIVE | `CLAUDE.md` |
| D-187 | #24 - every reported figure carries its uncertainty | LIVE | `CLAUDE.md` |
| D-188 | The constrained-optimum ledger corollary | LIVE | `CLAUDE.md` |
| D-189 | The scope of surprise, and the three-stage funnel | LIVE | `CLAUDE.md` |
| D-190 | The decision-neutrality corollary - what exists carries no weight in choosing a design | LIVE | `CLAUDE.md` |
| D-200 | Make it work first; compromise on performance only if performance proves a problem | LIVE | `CLAUDE.md` |
| D-201 | Very large scores must be handled, and are expected to be more common than our corpora | LIVE | `ARCHITECTURE.md` |
| D-202 | The effort control is one setting with several dials, and it must bound the time taken | DEFERRED | `ARCHITECTURE.md` |
| D-203 | Candidate admission is completion, not refinement - so #8 permits fixing it now | LIVE | `CLAUDE.md` |
| D-204 | One fix is designed once over the whole enumerated family, never per symptom | LIVE | `CLAUDE.md` |
| D-205 | A human acts as ground truth where no formal ground truth exists | LIVE | `ARCHITECTURE.md` |
| D-206 | Intonation is held as a future feature, and is a declared future consumer of the analysis | DEFERRED | `ARCHITECTURE.md` |
| D-277 | Measure before build - and a byte-identical structural refactor is exempt, because byte-identity is its prediction | LIVE | `cowork_engage_arc_plan.md` |

## T. Standing process rules and local patches — [full entries](decisions/group_T.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-196 | The self-check: re-read the diff against the principles before reporting | LIVE | `CLAUDE.md` |
| D-197 | The distribution constraint - the import-fix patch is fork-local and never goes upstream | LIVE | `CLAUDE.md` |
| D-198 | The Windows snap fix in the muse submodule is intentional and must not be reverted | LIVE | `CLAUDE.md` |
| D-199 | The MusicXML declared-mode import fix is intentional and must not be reverted | LIVE | `CLAUDE.md` |
| D-208 | A withheld finding never enters a mandatory session-start read | LIVE | `cowork_audit_protocol.md` |
| D-209 | Code that is about to be deleted gets no audit - only the no-information-loss check at deletion | LIVE | `cowork_audit_protocol.md` |
| D-231 | Issue-exhaustion and specification completion before any fix design - the three-phase sequencing rule | LIVE | `CLAUDE.md` |
| D-249 | The whole decision surface is delivered as user-visible text before any choice question | LIVE | `CLAUDE.md` |
| D-250 | Dispatches are written only when they are next; a parked instruction is revalidated first | LIVE | `cowork_audit_protocol.md` |
| D-251 | A running dispatch is never interrupted or steered mid-flight; every instruction is self-sufficient | LIVE | `cowork_audit_protocol.md` |
| D-252 | One side writes the instruction files and the other executes them, never the reverse | LIVE | `cowork_audit_protocol.md` |
| D-253 | Working-tree files are read with the file tools; bash is limited to git object queries by explicit hash | LIVE | `CLAUDE.md` |
| D-254 | Investigate by default; never ask the user whether to investigate or proceed | LIVE | `CLAUDE.md` |
| D-258 | A prune and tidy pass runs before any publish of the fork, and nothing on its list is acted on before it | DEFERRED | `cowork_prune_pass_checklist.md` |
| D-259 | Every upstream contribution is checked against the distribution constraint before it is posted | LIVE | `cowork_prune_pass_checklist.md` |
| D-279 | The Stage-3 entry gate - seven conditions before any engagement wiring reaches production | LIVE | `cowork_engage_arc_plan.md` ⚠gap |
| D-298 | The layer-by-layer audit - each layer is audited once its pieces are in place | LIVE | `cowork_handoff_archive.md` ⚠tracking-surface-only |
| D-314 | A correction rule kept for structural reasons must keep producing evidence that it still fires | LIVE | `cowork_stage5_fitter_design.md` ⚠gap |
| D-316 | The chord-symbol parser sussus fix is a recorded local patch with an UPSTREAMABLE distribution disposition | LIVE | `CLAUDE.md` |

## U. The standing decision-bearing surfaces — [full entries](decisions/group_U.md)

| ID | Decision | Status | Home |
|---|---|---|---|
| D-213 | The defect-type catalog is the living list of every problem type, and it is added to at discovery | LIVE | `DEFECT_TYPES.md` |
| D-214 | The dim7 characteristic bonus is the rotation selector and may not simply be removed | LIVE | `docs/scoring_model.md` |
| D-215 | Gating the root-continuity bonus on a sparse predecessor is a dead end | LIVE | `docs/scoring_model.md` |
| D-216 | The stepwise-bass bonus's four gates are each load-bearing | LIVE | `docs/scoring_model.md` |
| D-217 | The segmentation phase must suppress every context-dependent bonus | LIVE | `docs/scoring_model.md` |
| D-218 | Template array sizes derive from one constant, so the compiler enforces them | LIVE | `docs/scoring_model.md` |
| D-219 | Gates B, C and D were unreachable and were removed; no temporal condition may be added to the enharmonic flip | LIVE | `docs/scoring_model.md` |
| D-220 | The augmented-seventh guard requires both the major third and the augmented fifth | LIVE | `docs/scoring_model.md` |
| D-221 | A sparse upper-register lowest note does not earn inversion bonuses | LIVE | `docs/scoring_model.md` |
| D-222 | If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used | LIVE · derivation not recorded | `docs/scoring_model.md` |
| D-223 | A gate that judges the pre-correction winner reads a snapshot, not the live result | LIVE | `docs/scoring_model.md` |
| D-224 | Joint bass-and-chord scoring requires accumulated regional evidence | LIVE · derivation not recorded | `docs/scoring_model.md` |
| D-225 | A corpus is regenerated before its baseline figures are updated | LIVE | `BUILD_AND_TEST.md` |
| D-226 | The music21 export is version-pinned; regenerating it is a deliberate re-baseline | LIVE | `tools/REPRODUCIBILITY.md` |
| D-281 | The batch measurement tool must emit the structured fields on every alternative, or the corpus figures silently revert | LIVE | `docs/iteration_path1_summary.md` ⚠gap |

## Provenance of this register

- Adjudication: the OI-207 decision-conformance adjudication, 2026-08-01, at commit `58dea6702ac8aa9d5ef8b89244b94d587a75f7a5`.
- Coverage figures above regenerated at commit `3a186549bbd5c30ffda36cd0f21668dcb72e0d07`.
- Backbone data: `tools/audit/decisions/backbone_decisions.json` (sha256 `66191dac61df9153…`).
- Harvest: `tools/audit/decisions/decision_candidates.json` (sha256 `51850440b315e6e9…`).
- Clustering: `tools/audit/decisions/decision_clusters.json` (sha256 `0615b1e61bf10332…`).
- Shape: `open_items/OI-208.md` (user-ratified 2026-07-28).
- Standing rule for keeping it current: a new ratification, shelving or falsification gets its entry in `backbone_decisions.json` — and a regenerated `DECISIONS.md` — in the same commit that records it.

