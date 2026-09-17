# Phase 1d — the enumeration wave over the never-read surfaces: report

> **CC, 2026-08-02.** Dispatch `cc_instruction_phase1d_enumeration_wave.md`. Read-only on the
> system: no `src/` change, no golden / `tools/corpus/` / `tools/robust_stop/` movement, no
> behavior change, no fix, no design. The only specification edits are the two the dispatch
> authorized as riding acts. **No decision is ratified here** — every new register entry carries
> the record's own status and appears in the ratification queue below.

## The headline: a measured feasibility stop

The dispatch names a feasibility stop with a measured partition an accepted outcome. This is one.

The reading list was derived mechanically, as directed. It is **145 documents, 4.10 MB**. Measured
against the Read tool's own token accounting — `STATUS_ARCHIVE.md` reports **259,766 tokens for
789,462 characters**, a ratio of **3.04 characters per token** — **the list is ≈1.35 million
tokens**. That is larger than one session's entire context window, before Task 0, Task 2, the
entries, the guards and this report are paid for. No ordering makes the full wave a one-session
job.

**What was read IN FULL: 21 documents, 195 of the 1,533 clusters (12.7 %).** What was not: 124
documents, including both archives. The remainder is measured, partitioned and handed over rather
than estimated.

## Task 0 — the two riding acts (commit `19fbe9e271`)

`git push origin master` landed `91802e4d37` first; HEAD verified.

**OI-265 — the Layer-4 truth-sync. RESOLVED.** The Layer-4 correction block now carries the
scoping sentence the Layer-3 one does, and goes one step further because the Layer-4 case differs:
the offending sentence is about a *different* path (the legacy `analyzeChord` pipeline, not the
decoder the section describes), which a bare scoping sentence would not have reached. The
correction therefore quotes it, says it was true when written and is false at HEAD, and records
what is true instead. `useJointNotationRecord` defaulting `true` was **verified at the code this
session** — [composingconfiguration.cpp:178](src/composing/composingconfiguration.cpp#L178) — not
carried from memory.

**OI-266 — the six working-protocol rules. RESOLVED.** Homed by what each governs, not by where it
was found:

| entry | homed at | governs |
|---|---|---|
| D-249 the whole decision surface before any choice question | `CLAUDE.md` Conventions | how the user is asked |
| D-253 file tools for working-tree reads, git objects by hash | `CLAUDE.md` Conventions | how the record is read |
| D-254 investigate by default | `CLAUDE.md` Conventions | beside principle #5, which it operationalizes |
| D-252 one side writes instructions, the other executes | `cowork_audit_protocol.md`, new section | how a dispatch is commissioned |
| D-250 no dispatch ahead of need; parked instructions revalidated | same | when a dispatch is written |
| D-251 no mid-flight steering | same | how a dispatch is run |

Two judgments are recorded so they can be disputed rather than hidden. **First**,
`cowork_audit_protocol.md` is titled *The Certification-Audit Protocol*, and the three dispatch
rules are wider than audits; the new section says so in its own lead-in, and `open_items/OI-266.md`
records why it is the least-bad home (P5's withheld-finding rule and P8's ordering are already
dispatch-construction rules, and every audit there is commissioned as a dispatch). **Second**,
D-253's planning-side scope is taken **from the record** — the heading it sits under and D-252's
own text both state it — not decided here; homing it unqualified would have contradicted the same
file's mandatory build and test sections.

The register's *recorded only on a tracking surface* count returns **6 → 0**.

## Task 1 — the reading list, and what was read

### The list (145 files, 1,535 file-attributions, 4.10 MB)

Per surface, as the cluster records give it:

| surface | files | clusters | source | read in full |
|---|---|---|---|---|
| `cowork_*` design documents | 100 | 871 | 1.97 MB | 14 |
| `docs/` design documents | 43 | 408 | 0.86 MB | 7 |
| the two archives | 2 | 256 | 1.28 MB | **0** |

The per-file counts for all 145 are the derived list; the 21 read IN FULL, with their cluster
counts, are:

| # | document | clusters | banner |
|---|---|---|---|
| 1 | `docs/beam_widening_design.md` | 37 | SHELVED |
| 2 | `cowork_bounded_context_design.md` | 21 | **SIGNED 2026-07-02** |
| 3 | `cowork_spec_language_sweep.md` | 14 | AS-BUILT |
| 4 | `docs/stage6_functional_layer_design.md` | 13 | DRAFT |
| 5 | `docs/scoped_joint_design.md` | 13 | DRAFT |
| 6 | `cowork_phase5_branch_backfill_spec.md` | 12 | — |
| 7 | `cowork_architecture_reassessment.md` | 12 | — |
| 8 | `cowork_layer5_spec_review.md` | 9 | — |
| 9 | `cowork_design_doc_template.md` | 8 | — |
| 10 | `cowork_prefit_gates.md` | 8 | **RATIFIED 2026-07-19** |
| 11 | `docs/iteration_path1_summary.md` | 7 | — |
| 12 | `cowork_engage_arc_plan.md` | 6 | **RATIFIED 2026-07-07** |
| 13 | `cowork_audit_postscoringgates.md` | 5 | — |
| 14 | `cowork_confidence_contract.md` | 5 | **RATIFIED 2026-07-02** |
| 15 | `cowork_premise_gate_reflection.md` | 5 | **RATIFIED 2026-07-10** |
| 16 | `cowork_audit_harmonicfunctionlayer.md` | 4 | — |
| 17 | `cowork_prune_pass_checklist.md` | 4 | — |
| 18 | `cowork_audit_regionanalyzer.md` | 3 | — |
| 19 | `cowork_audit_jointkeydecision.md` | 3 | — |
| 20 | `cowork_audit_remaining_layers.md` | 3 | — |
| 21 | `cowork_notation_output_contract.md` | 3 | **RATIFIED 2026-07-26** |

**READ-IN-FULL is confirmed for each of the 21.** No document was skimmed, and no document was
partially read: a file is either on this list or in the remainder.

### The declared priority, and why the archives were deferred

The dispatch gave the archives particular care, so they were addressed first — but by measurement,
not by assumption. All **256** archive clusters were dumped and reviewed, which confirmed the
surface does carry the binding class (*"Gate M … DEFERRED — do not retry"*, *"Gate N … DEFERRED —
do not retry"*, *"key-as-distribution SHELVED (premise obsolete)"*, *"Iter 90 — shelved"*, *"Do not
attempt further local scoring fixes for inversions"*). The cost was then measured: **1.28 MB /
≈421 k tokens for 256 clusters — 78 % of a realistic reading budget for 17 % of the population.**

Reading them in full would have consumed the wave and left the design documents — which this
audit's own record names *"the highest expected yield of genuine unregistered decisions"* — untouched.
The budget went to the design documents instead, and the archives are named as the next partition
with their measured cost. **They are swept by no bulk rule, exactly as before.** This is a
deviation from the dispatch's ordering, made on measurement, and it is stated here rather than
absorbed.

Within the design documents the wave used a mechanical high-signal filter: the **status-banner
convention** (which this wave then registered as D-256). **28 of the 143 design documents carry a
SIGNED / RATIFIED / AS-BUILT banner**; the small and mid-sized members of that set were read
first. Seven of the 21 carry an explicit user ratification, and they produced 17 of the 27 entries.

## The new decisions — 27 entries, register 254 → 281 (commit `042f8dde79`)

Every verbatim is **extracted from its home by line range, never retyped**. Status, date and
ratifier come from the record only; "not stated" appears wherever the record does not say, and
nothing was inferred.

### ★ RATIFICATION QUEUE — for the user

**None of these is ratified.** Each carries the status its own record states.

| entry | title | home | status / date / ratifier from the record |
|---|---|---|---|
| D-255 | Every design document follows one fourteen-section structure, from arc42 + IEEE 1016 + ISO/IEC/IEEE 42010 | `cowork_design_doc_template.md:3-7` | live · 2026-06-22 · user |
| D-256 | Every design document opens with one of four declared status banners | `:75-78` | live · not stated · not stated |
| D-257 | A specification carries a locator to its code and tests; code mechanics never do the explaining | `:82-91` | live · 2026-06-24 · user |
| D-258 | A prune and tidy pass runs before any publish of the fork | `cowork_prune_pass_checklist.md:3-5` | **deferred** · 2026-06-22 · user |
| D-259 | Every upstream contribution is checked against the distribution constraint before posting | `:43-46` | live · not stated · not stated |
| D-260 | Analysis output covers exactly the selection; everything beyond it is evidence, never a result | `cowork_bounded_context_design.md:43-44` | live · 2026-07-02 · user |
| D-261 | A layer never guesses how much context it needs — the amount is discovered by convergence | `:57-69` | live · 2026-07-02 · user |
| D-262 | The extension increment belongs to the requesting layer, not the note supplier | `:73-81` | live · 2026-07-02 · user |
| D-263 | A refused or truncated extension is marked on the output, never silently absorbed | `:82-86` | live · 2026-07-02 · user |
| D-264 | Any sequence of extensions equals one fresh run over the final loaded span | `:121-126` | live · 2026-07-02 · user |
| D-265 | Asking a lower layer for more notes is a data-supply call, not a backward inference edge | `:115-120` | live · 2026-07-02 · user |
| D-266 | **Layer 6 is prohibited until the bounded-context design is coded and regression-tested for L1–L5** | `:213-217` | live · 2026-07-02 · user |
| D-267 | Two admissible confidence classes; no layer may claim a calibrated probability until one is fitted | `cowork_confidence_contract.md:25-34` | live · 2026-07-02 · user |
| D-268 | A confidence attaches to a named decision, is compared only within its class and a declared frame | `:36-48` | live · 2026-07-02 · user |
| D-269 | The frame table is the one home of the override arithmetic | `:83-85` | live · 2026-07-02 · user |
| D-270 | The held-out protocol — five-fold cross-validation grouped by ground-truth analysis file | `cowork_prefit_gates.md:32-42` | live · 2026-07-19 · user |
| D-271 | The capacity budget — cell-count floor, parameter bound, weight-vector cap | `:68-81` | live · 2026-07-19 · user |
| D-272 | Protocol constants are protocol, not tuning — changing one is an amendment | `:17-19` | live · 2026-07-19 · user |
| D-273 | The architecture-adoption variant of the hard regression stop, written before any diff existed | `:116-121` | live · 2026-07-19 · user |
| D-274 | The reverse map — if the estimator is not adopted it is removed whole | `:189-191` | live · 2026-07-19 · user |
| D-275 | Every published record carries its instrument provenance; a provenance-less analysis cannot exist | `cowork_notation_output_contract.md:54-57` | live · 2026-07-26 · user |
| D-276 | Modal colour is published as un-rounded counts; no mode label is inferred anywhere | `:139-147` | live · 2026-07-26 · user |
| D-277 | Measure before build — and a byte-identical structural refactor is exempt | `cowork_engage_arc_plan.md:97-102` | live · 2026-07-07 · user |
| D-278 | **The joint key-and-chord step is SHELVED — measured not to pay** | `:103-112` | **shelved-with-evidence** · 2026-07-07 · user |
| D-279 | The Stage-3 entry gate — seven conditions before engagement wiring reaches production | `:64-67` | live · 2026-07-10 · user |
| D-280 | Gates read structured fields only — never a chord symbol, never a Roman numeral | `docs/iteration_path1_summary.md:74-78` | live · not stated · not stated |
| D-281 | The batch measurement tool must emit the structured fields on every alternative | `:66-72` | live · not stated · not stated |

### The two that matter most

**D-278 is the class this audit exists for.** A **shelving with evidence** — the joint key-and-chord
step, measured not to pay (≈0.05–0.16 pp net over ~6200 stretches, harm at 75–90 % of correction,
firing rate 1.4 %, the cause being that carried alternative keys are siblings within one
collection) — recorded only in a design document, invisible to the register until the document was
read. That is the same failure shape as the Stage-3.1b shelving that produced OI-207.

**D-266 is a live prohibition** — Layer 6 may not resume until the bounded-context design is coded
and regression-tested across Layers 1 to 5 — sitting in a document no session-start read opens.

### ★ Measurement-tools section (for the sealed instruments partition)

The dispatch asked for decisions about measurement tools to be listed separately so the next
dispatch can account for them without reading these findings as its own. **This section is not
empty. It has one entry:**

- **D-281** — the batch analysis tool must emit root pitch class, bass pitch class, quality and
  bass-is-root on **every alternative entry**, not only the winner. Those fields activate the
  comparison script's reclassification of readings where the corroborating source matches our
  second or third candidate; without them the corpus measurement **silently reverts** to its
  earlier counts. Home `docs/iteration_path1_summary.md:66-72`; no date or ratifier stated. The
  failure behind it: the change was lost to a hard reset and went undetected for three weeks.

**Consequence for the sealed partition, stated plainly:** this one entry is also the reason the
wave wrote **no bulk rule over the `tools/` script comments**. That surface is the instruments
partition's own subject, and D-281 proves it carries real decisions — so sweeping it here would
both pre-empt that review and be exactly the blind class sweep the ruling-vocabulary guardrail
forbids. All **295** `tools/` clusters remain `unresolved`, now by a stated reservation rather than
by falling through.

## Task 2 — the residue is judged, not merely counted (commit `33a821d64c`)

**Three new bulk rules (33 clusters).** Each widens an existing rule's stated reasoning to prose of
the same surface, under the **same** ruling vocabulary, and each runs after BR-3/BR-4 so a cluster
naming a backbone decision is never swept:

| rule | class | clusters |
|---|---|---|
| BR-14 | open-items register **prose** that is not a row or header, no ruling word — BR-10's reasoning widened; a detail file carries narrative and provenance only and is never a status of record, by its own standing banner | 17 |
| BR-15 | session-handoff prose, no ruling word — OI-240 and OI-266 establish it tracks work and is not a home, and the six that were are now homed | 14 |
| BR-16 | a defect-type catalog row — the catalog is D-213; a row is a catalogued problem TYPE with its detection signature | 2 |

Plus 8 patterns on D-249/D-250/D-252/D-253 so their numbered sub-items in the former home record as
restatements instead of falling to the residual.

**The larger half of Task 2 is what was deliberately NOT swept.**
`disposition_manifest.json` now carries a generated `unresolved_reservation_by_surface` giving
**every** surviving surface its reason beside its count. A surface appearing without one is emitted
as `NO REASON STATED` rather than silently omitted; none currently is. The two biggest:

- **`tools/` script comments (295)** — reserved for the sealed measurement-tools partition (above).
- **`src` production comments (276)** — reserved for a reading against `docs/scoring_model.md`
  §4/§8. These are largely the musical-reasoning comments **D-123 requires** at every non-obvious
  scoring weight, so they state design decisions **with their defense** (D-195) and cannot be swept
  as narrative. Settling each means comparing it against the scoring model's own §4 term table and
  §8 constraint list — a reading this wave did not reach. *(Note: D-209's retiring-code exemption
  was not used here; the dispatch rules it out, this being a read of the record, not an audit of
  code.)*

The rest are named for what they are: the BR-11/BR-12/BR-13 **exemption sets** (683 — units those
sweeps refused because they carry a ruling word, each needing a reader); the **two archives** (256 —
swept by no rule, deliberately); the **governing documents** (67 — already read in full by the
2026-08-01 completion pass, so judged, not unread); and this wave's own measured design-document
remainder (1,264).

### The final disposition table, over 14,460 clusters

| disposition | at session start | now |
|---|---|---|
| restates | 5,511 | 5,511 |
| not-a-decision | 5,389 | **5,418** |
| boilerplate | 74 | 74 |
| no-spec-home | 551 | **578** |
| **unresolved** | **2,935** | **2,879** |

Coverage unchanged and re-proved: **14,460/14,460 clusters, 15,224/15,224 occurrences**.

### The remaining 2,879, by surface

| surface | clusters | character |
|---|---|---|
| `cowork_*` design documents | 857 | this wave's measured remainder |
| `docs/` design documents | 407 | same |
| `cc_*` session reports | 316 | the BR-12 exemption set |
| `tools/` script comments | 295 | reserved — the sealed instruments partition |
| `cc_instruction_*` dispatches | 291 | the BR-11 exemption set |
| `src` production comments | 276 | reserved — the scoring-model reading |
| the two archives | 256 | swept by no rule, deliberately |
| `src` test comments | 76 | the BR-13 exemption set |
| `ARCHITECTURE.md` | 55 | read in full 2026-08-01; judged |
| the open-items register | 17 | the BR-14 exemption set |
| `CLAUDE.md` | 12 | read in full 2026-08-01; judged |
| the session handoff | 12 | the BR-15 exemption set |
| mixed sources | 9 | span more than one surface; never swept |

## Task 3 — rows, notes, guards

**Three new rows, each with its detail file in the same commit (register rule (c)):**

- **[OI-268](open_items/OI-268.md)** — ★ twenty-two of the 27 new entries are recorded in a
  **ratified contract or cross-layer design document**, not a layer specification. The question is
  narrower than "unhomed": `ARCHITECTURE.md` **explicitly delegates** the bounded-context concern to
  its design document, and **D-092** makes one non-layer home for a cross-cutting contract
  conformant. So does OI-208 ruling 2's *"wherever possible"* reach a contract a layer specification
  deliberately delegates to? Either 22 homing acts are owed, or the register needs a fifth
  non-specification case. **A ruling, so this pass did not make it.**
- **[OI-269](open_items/OI-269.md)** — a **conflict**, both sides quoted:
  `docs/iteration_path1_summary.md:112-116` (*"Commit all changes that affect BIR metrics
  immediately"*) against `CLAUDE.md` Conventions (*"Commit only when explicitly asked"*). The
  document carries no superseded banner and is still cited as live — two of its architecture
  decisions are registered and this wave entered two more from it. Nothing fixed.
- **[OI-270](open_items/OI-270.md)** — **the wave's one recorded REMAINDER.**
  `cowork_architecture_reassessment.md` lists four cross-cutting *"meta-findings to
  institutionalize"* — including **"never learn keys"** and **"selection/competition is
  saturated"** — but the same document's closing section puts them to the user as *"Ratify:"* and
  records no answer. Entering them would have meant inferring ratification from conduct, which the
  never-work-from-memory rule and this dispatch both forbid. **The dispatch's stop condition fired
  and the row is the record instead.**

**Dated notes:** [OI-207](open_items/OI-207.md) (method, the derived list, the declared priority
and why the archives were deferred, the yield, the reservations, the arithmetic, the two-partition
handover) and [OI-208](open_items/OI-208.md) (the same-commit rule honored twice; the home-vocabulary
question; and a measured observation — **D-256's status-banner convention is not universally
applied**, 101 of the 143 design documents carry no banner at all).

**OI-207 does NOT close, and the arithmetic says why.** Its remaining scope was the unread
population; **124 of the 145 documents are still unread**, including both archives. Proposed next
partition:

| partition | clusters | source |
|---|---|---|
| the remaining design documents | 1,084 | ≈2.2 MB |
| the two archives | 256 | 1.28 MB |

**Guards, at the final tree — all PASS:**

- `gen_cluster_dispositions.py --verify` — **281/281** verbatim quotes found at their cited home,
  **276/276** line anchors correct, **all** `D-…`/`OI-…` cross-references resolving.
- `gen_cluster_dispositions.py --check` — **OVERALL PASS**, 14,460/14,460 clusters,
  15,224/15,224 occurrences.
- `gen_decisions_register.py --check` — the register matches its data across all **21** files.
- `tools/open_items_split_check.py` — **OVERALL PASS**, index 270 = detail 270, all 200 original
  items byte-verbatim.

Specification insertions shifted anchors as expected; **258 backbone citations were remapped from
the actual diff**, content-anchored and re-proved by `--verify`, never from hand-counted deltas.

## Anomalies, each diagnosed

1. **The reading list is ~30 % larger in tokens than a character-count estimate suggests.** Cause:
   the real ratio is 3.04 characters per token on this prose, not the ~4 a first estimate assumed.
   Diagnosed by reading the Read tool's own reported token count for a file of known size. Not a
   surprise about the system — a measurement of the instrument, taken before it could mislead the
   plan.
2. **My own first write of the six re-homed entries carried two defects, caught by the standing
   self-check before commit:** the re-taken verbatims were three-line excerpts ending mid-sentence,
   and the provenance field *appended* to the old `status_source` instead of replacing it, so each
   entry stated its former home twice. Both corrected (full blocks; single-statement provenance).
3. **My own tool edit carried two more, caught by the same check:** a hand-typed count
   ("21 of the 143") inside a generated artifact's input, which would go stale as later waves read
   more — replaced by a pointer to the dated note; and one reservation string BR-16 makes
   unreachable — removed.

**No surprise about the system arose** (#13), so no STOP is raised on that axis. The one deviation
from the dispatch — deferring the archives — is a resource decision made on measurement and is
stated in full above and in the OI-207 note, not absorbed silently.

## What the user is asked for

1. **Ratify or correct D-255…D-281** (the queue above). D-278 and D-266 are the two worth reading
   first.
2. **Rule on [OI-268](open_items/OI-268.md)** — does ruling 2 reach a delegated cross-cutting
   contract? The answer decides whether 22 homing acts are owed or the register gains a fifth case.
3. **Rule on [OI-269](open_items/OI-269.md)** (the commit-rule conflict) and
   [OI-270](open_items/OI-270.md) (were the four meta-findings ratified?).
4. **Direct the wave's second partition** — the remaining 1,084 design-document clusters and the
   256 archive clusters — before phase 2 opens, since a decision still hiding there would make
   phase 2's conformance audits silently under-report.
