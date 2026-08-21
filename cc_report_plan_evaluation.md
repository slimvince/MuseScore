# Evaluation of the specification-reconstruction plan, under the neutral brief

> **STATUS: SESSION REPORT.** Claude Code, 2026-08-21, at branch tip `7d7a0e76f7`. Executing
> `cc_instruction_plan_evaluation.md` under the brief `cowork_plan_evaluation_brief_2026_08_21.md`
> and the read list `cowork_evaluation_boot_list_2026_08_21.md`.
>
> **This report evaluates. It executes nothing.** No `src/` change, no golden, no test changed,
> moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the
> analysis built, designed, scoped or run, no design, no repair, no mining, no document archived,
> moved or deleted as a file, no open-items row created, flipped or discarded, no specification
> text written or edited, no finding number allocated, no ruling taken. The plan is not ratified
> by anything here and is not treated as authority for anything.

---

## 0. Terms used before they are explained elsewhere

- **The plan** — the four files `cowork_specification_reconstruction_plan_2026_08_19.md` and its
  `_v2_`, `_v3_`, `_v4_` successors, read in that order, together with
  `cowork_curated_boot_list_draft_2026_08_19.md`. Where a statement holds of all four, "the plan"
  is written; where it holds of one, the version is named.
- **The ruled structure** — the six phases ruled on 2026-08-15, whose one home is
  `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3, ruled at
  `cowork_rulings_2026_08_15_phase_definition_sitting.md` §2.
- **The combined content score** — the quantity the ratified factorization document calls "the
  joint score": the weighted sum of factor terms a candidate reading earns
  (`cowork_joint_estimator_factorization.md:41-56`). Written this way here because the bare word
  *score* is reserved for the music.
- **MERIT** and **CONFORMANCE** — the brief's two labels (§4.1). A MERIT finding would survive if
  every ruling in this project were deleted tomorrow. A CONFORMANCE finding is a collision with a
  standing rule, and carries no merit weight. **No finding below carries both labels.**

### How values enter this report, and what uncertainty attaches to them

Every number below is cited to an artifact and a field, or to a `file:line` where the record
states it (D-431; `cowork_audit_protocol.md:512-519`). Two classes of number appear:

- **Object sizes and object counts**, produced by `git ls-tree -l` at an explicit commit hash, and
  **presence or absence of a string in a file**, produced by the file-search tool. These are exact
  reads of content-addressed or on-disk objects. **No sampling is involved, so no uncertainty range
  attaches to them** (#24 bounds sampling error; there is none here). Where I state a count I
  produced myself rather than read from a generated artifact, I say so at the point of use.
- **Values published by a generated artifact**, cited to artifact and field. Their uncertainty is
  whatever that artifact declares; none of them is compared against another measured quantity in
  this report, so no difference-within-noise question arises.

**No comparison between measured quantities is asserted anywhere in this report.**

---

## 1. Task 2 — the independence record

### 1.1 Every file I opened

Read whole or in substantial part, in this order:

1. `cc_instruction_plan_evaluation.md` (my dispatch)
2. `cowork_plan_evaluation_brief_2026_08_21.md` (whole)
3. `cowork_evaluation_boot_list_2026_08_21.md` (whole)
4. `cowork_specification_reconstruction_plan_2026_08_19.md` (whole)
5. `cowork_specification_reconstruction_plan_v2_2026_08_19.md` (whole)
6. `cowork_specification_reconstruction_plan_v3_2026_08_19.md` (whole)
7. `cowork_specification_reconstruction_plan_v4_2026_08_19.md` (whole)
8. `cowork_curated_boot_list_draft_2026_08_19.md` (whole)
9. `CLAUDE.md` (whole, lines 1–1845)
10. `DECISIONS.md` (whole, lines 1–859)
11. `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` (whole)
12. `cowork_rulings_2026_08_15_phase_definition_sitting.md` (whole, §6 included)
13. `cowork_rulings_2026_08_15_method_directions.md` (whole)
14. `tools/audit/nongating_apparatus_rows.json` — searched, not read whole: the
    `★_the_live_gating_answer` block and the `gating_ids` list
15. `ARCHITECTURE.md` — headings whole; read in full at `:265-550` (the joint estimator's standing
    rules, the evidential ranking, the counted quantities, the hard/soft line)
16. `docs/scoring_model.md` — headings whole; read in full at `:1367-1461` (§8's remaining portion)
17. `DEFECT_TYPES.md` — the defect-type table, read in part
18. `cowork_joint_estimator_factorization.md` — headings whole; read in full at `:21-215`
19. `cowork_audit_protocol.md` — the dispatch-protocol section's standing-clause headings, and
    `:512-581` in full
20. `STATUS.md` (`:1-19`, the live portion)
21. `tools/audit/decisions_filter_classification.json` — header `:1-45` and searched fields
22. `tools/audit/rulings_sort_classification.json` — header `:1-30` and searched fields
23. `tools/audit/decisions/home_classification.json` — searched; the population block and the
    home-document keys
24. `tools/audit/decisions/apply_field_diff.json` (`:1-40`)
25. `tools/audit/gen_decisions_filter.py` — searched; the pinned-reading block `:93-132`
26. `tools/audit/july_screen_report.md` (`:1-60`)

Searched by pattern without opening whole (low-exposure reads, listed for completeness): the
fifteen `cc_instruction_preparation_*.md` files, for the string *boot list* only; the four plan
versions, for several strings.

Git object queries by explicit hash, all read-only: `git rev-parse HEAD` (the one tip check the
dispatch orders); `git ls-tree -l` at `891bacc5d2`, `7d7a0e76f7` and `b006dc15b5`; `git ls-tree -r
--name-only` at `7d7a0e76f7` over `tools/audit/`; `git cat-file -t b006dc15b5`.

### 1.2 The excluded files, and whether I opened them

**I did not open any of them.** Each is recorded here by name:

| file | opened? |
|---|---|
| `cowork_handoff.md` — every block | **NOT OPENED** |
| `cc_report_plan_challenge.md` — the existing review | **NOT OPENED** |
| `cc_instruction_plan_challenge.md` — the refute-only dispatch | **NOT OPENED** |
| `cowork_review_findings_prediction_2026_08_21.md` — the sealed prediction | **NOT OPENED** |
| `cowork_rulings_2026_08_21_evaluation_brief_sitting.md` | **NOT OPENED** |
| `cowork_away_returns.md`, `STATUS_ARCHIVE.md`, `cowork_handoff_archive.md` | **NOT OPENED** |
| `cc_report_plan_evaluation.md` (the other evaluator's answer, had it existed) | did not exist at boot; checked by file-name search only, never opened |

I took no branch rule and read no commit log. `git log` was not run at any point, and the tip check
was a hash comparison alone.

### 1.3 Prior verdicts on the plan that I met

**Two, both inside my own inputs, both bounded and both recorded here rather than relied on.**

1. **The brief's own §0** (`cowork_plan_evaluation_brief_2026_08_21.md:13-37`) states that the plan
   has been evaluated once, that the first pass was briefed to refute, that its verdicts are
   uniformly negative, and that its largest stated return was that the plan is not situated against
   the ruled six-phase structure. I read this because the brief is dispatched to me whole and
   ordered read first. **What I saw:** the shape of the prior pass and one sentence naming its
   largest return. **What I did not see:** any of its findings, any evidence, any verdict on any
   component. I have treated the one named return as a claim to test, not to inherit — and it is
   tested below on its own evidence, where the ruled structure's collisions are labelled
   CONFORMANCE and are argued separately from merit exactly as §4.1 requires.
2. **The boot list's §2 and its ruling block** (`cowork_evaluation_boot_list_2026_08_21.md:53-71`,
   `:83-95`) state that `cowork_handoff.md`'s two most recent blocks carry the review's outcome and
   that the tip commit's subject line states the review's verdict. **What I saw:** that a verdict
   exists in those places. **What I did not see:** the verdict itself. I did not open the handoff
   record and did not run `git log`, so the tip commit's subject line never reached me.

**No third prior verdict reached me.** I did not encounter one in `CLAUDE.md`, `DECISIONS.md`,
`STATUS.md`, the phase-definition surface, either ruling record, or any artifact.

---

## 2. Task 1 §4 — the findings

### 2.1 What should be KEPT

**The diagnosis of the polluting instruction, and its supersession — MERIT.**
Every version's §1(a) states that until 2026-08-15 the phase-1 rule ordered *"the specification
text is corrected wherever it states something false at HEAD"*, that this is how code enters a
specification, and that `CLAUDE.md` now carries the opposite rule. Checked at the primary source
and correct in every particular: the superseded three-phase text stands preserved at
`CLAUDE.md:1613-1619`, and the replacement — *"A DISAGREEMENT BETWEEN SPECIFICATION AND CODE IS
EVIDENCE, RESERVED FOR THE AUDIT; NO DOCUMENT IS CORRECTED ON THE GROUND THAT THE CODE SAYS
OTHERWISE"* — at `CLAUDE.md:1599-1601`. The plan's added observation, that **the cause is stopped
and the damage is not repaired** (v1:35), is the correct reading of that pair and is the one
sentence that makes a reconstruction programme necessary at all. This is the plan's foundation and
it holds.

**Derive blind, then open the record — the ordering, and the reason given for it — MERIT.**
v1 §6 Step 2/Step 3, v2–v4 B2/B3, with the stated ground: *"Reading the record first would anchor
the derivation on the existing framing; reading it after turns it into a test of the derivation"*
(v1:168-169; v3:136; v4 carries the same shape). This is right on its own evidence, independently
of any ruling. A polluted source read first supplies both the answer and the standard by which the
answer is judged, so it yields no independent signal; read afterwards it becomes a second opinion
whose disagreements are informative. It is the only construction in the plan that turns a source
the plan itself distrusts into evidence rather than into authority.

**Sources declared before reading, shown to the user, then fixed for the pass — MERIT.**
v1 Step 1, v2–v4 B1. Two distinct goods in one step: a missing source is named while it is still
cheap to add, and the scope of a pass is a pre-declared object rather than something reconstructed
afterwards from what happened to be opened. The second is what makes an overrun detectable at all.

**The frame test run adversarially, by the side that did not author the frame — MERIT.**
v2 A5, v3/v4 A5, with the brief given as *"place these; report every one you cannot"* and
explicitly not *"does this frame look complete?"* (v3:88-91; v4:85-89), and with the reason stated:
*"a both-ways reconciliation runs INSIDE a frame, so a missing axis produces agreement on both
sides"* (v3:93-95; v4:91-93). That reasoning is correct and is the strongest single piece of
method-design in any of the four versions. It is also correctly separated from A4: A4 tests
membership, A5 tests the category, and the plan says so. The founding example given — a
chord-progression library placed into a frame of questions and not fitting — is a real
demonstration rather than an illustration, because it is the gap that actually produced v2.

**Proving the statement format before anything is written in it — MERIT.**
v3/v4 A6. This is #19 applied to the plan's own output form: a format is a measurement tool for
conformance, and an unestablished measurement tool may not be trusted. Deciding it after ten
sections have been written in it is the failure the step exists against, and v3's own §0(5) names
that failure. (The five test kinds chosen are the wrong sample — see §2.2 — but the step is right.)

**The declared budget with overrun as a stop, and the done condition written first — MERIT.**
Guardrails 5 and 6 in every version. Both address failures the plan names, and neither depends on
any ruling to be correct: a programme with no cost ceiling cannot be stopped on cost, and a done
condition written afterwards is written by whatever was achieved.

**The tell, and its self-referential clause — MERIT.**
Guardrail 11 in every version: one sentence checked at every pass end, *"checked by the user
reading one short thing, not by a guard"*, and — the clause that makes it work — *"If a session
proposes building something to check these guardrails, that proposal is itself the tell firing"*
(v1:230-233; v4:214-216). This is the establishment recursion closed by construction rather than by
resolve, and it is correct: the recorded cause of the apparatus backlog is a mechanism that draws
capacity indefinitely (`CLAUDE.md:388-392`), so a guardrail checked by new apparatus reproduces the
cause it was written against.

**v3 §6 — the end state declared at the start, as a bounded migration with a ruled terminus —
MERIT, and it improves on the ruled plan.**
v3:152-165, v4:162-174: two specifications of one system would violate #6, so the interim is
declared as a #23 bounded migration, nothing is deleted, and *which* of two termini applies is
ruled at the start *"because a migration with no ruled terminus is how the last one ended"*. This is
correct and it fills a genuine hole in the ruled pruning plan, which says the outgoing text is
archived when a derived text is ratified and that *"the old and new never coexist as live
surfaces"* (`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:550-554`). That
rule is written per specification, and `ARCHITECTURE.md` is one file holding many specifications, so
it cannot be executed as written for the largest subject. **The rule as ruled does not cover the
case; v3's construction does.** I state this as a place where the plan is right and the standing
text is incomplete.

**Marking what is AUTHORED, per version — MERIT.**
v2 §2, v3 §2, v4 §2. Each lists what in the plan is invented rather than derived, and v3/v4 expand
those items into the attack surface with a refutation test each. This is #17(a) applied to a plan
rather than to a design, and it is the reason this evaluation could locate several of its findings
at all: the plan names its own load-bearing assumptions, which is a service to any reader.

### 2.1a Good things that fell out of the lineage — all MERIT, all recoverable by restoring text

The brief's §1 asks for these specifically. I verified each at the files.

**v1's ten "*Stops:*" clauses — one per guardrail, naming the observed failure it stops.**
v1's §8 preamble states the reason in terms: *"Each is aimed at a failure observed in this project,
and the failure is named so the guardrail cannot be softened into general advice"* (v1:203-204). Ten
guardrails then carry a `*Stops:*` clause (v1:207, 210, 213, 216, 218, 220, 223, 225, 228, 229).
**A search of v2, v3 and v4 for the string `Stops:` returns zero occurrences in all three files.**
The guardrails survive as bare imperatives. This is the precise defect v1 predicted, and it is also
a collision with the standing convention that every design decision carries its defense at its home
(`CLAUDE.md:1574-1586`) — but the merit point stands without that: a guardrail whose founding
failure is unnamed cannot be tested against a later case, and cannot be retired when its failure
stops recurring.

**v1's guardrail 4 carried a parking clause; v2 onward dropped it.**
v1:215-216 reads: *"The sources are declared before reading and never extended mid-pass. **Anything
found outside them is written down as an input to a later question.**"* v2:176, v3:198 and v4:207
keep the first sentence and drop the second. The dropped sentence is the only mechanism in any
version for content discovered in the wrong place — and with it gone, guardrail 4 becomes a rule
that forbids following a lead and provides nowhere to put it. That is silent loss by construction,
and it is the same function the ruled cross-layer transfer list performs
(`cowork_rulings_2026_08_15_method_directions.md:55-60`).

**v2's unit-shape correction, with its ratified grounding — dropped at v3.**
v2:17-23 states that "questions the analysis answers" cannot hold a thing the analysis *knows* nor a
requirement that the implementation *not preclude* something, and grounds both classes in
`CLAUDE.md`'s fact-publication corollary, which requires an unconsumed derived fact to be either
declared dormancy with its future consumer named or waste, and requires evidence-class facts to be
published broadly even without a named consumer. I checked the corollary at `CLAUDE.md:239-252` and
v2's characterization of it is accurate. **v3 and v4 keep the anecdote and drop the rule:** the
chord-progression library survives at v3:95 and v4:93 as the reason A5 exists, while the ratified
corollary that made it a *class* the frame must hold appears in neither. A search of all four files
for `dormancy`, `fact-publication` and `not preclude` returns matches in v2 only.

**v2's governing correction — dropped at v3.**
v2:32-35: *"**And the correction that governs all three:** `ARCHITECTURE.md` is **one of several
polluted documents, not the polluted document** — and there is nothing better available, unless the
historical versions are read as well."* Absent from v3 and v4 (searched: `one of several` matches v2
only). Both halves matter. The first is what stops a reconstruction aimed at one file from believing
it has covered the subject. The second is the only sentence in any version that points at the
historical versions as a source — and §2.4 below records that the record's own ruled most-valuable
source is a historical version the plan never names.

**Three of v3's guardrails lost their operative second clause at v4.**
Guardrail 7: v3:201 *"No ruling is taken during a pass; **open questions accumulate to one
ratification.**"* → v4:210 *"No ruling is taken during a pass."* Guardrail 9: v3:203 *"A ratified
unit is closed; **re-opening takes the user's word.**"* → v4:212 *"A ratified unit is closed."*
Guardrail 10: v3:204 *"The frame is closed once ratified; an addition is the user's, **never a
session's.**"* → v4:213 *"...an addition is the user's."* In each case the dropped clause is the one
that says what happens instead — where the open questions go, who may reopen, and who may not add.
The surviving clause states a prohibition with no procedure, which is the shape a session routes
around.

### 2.2 What should be REPAIRED — right in intent, wrong in mechanism

**The dead-end outcome, and the trust measurement built on it — MERIT.**
Every version's third step gives four grading outcomes, of which the fourth is: *"records a dead end
the derivation walked into → the derived statement is withdrawn, and this is also the measurement of
whether the derivation method can be trusted"* (v1:166; v3:121-124; v4:133-136). The **intent** is
right and is the best methodological instinct in the plan: a derivation's trustworthiness should be
established against something the derivation could not have known (#19). The **mechanism is wrong at
the object**, for two reasons, both checked in the dead ends themselves.

*First, the dead ends in the record disclaim the use the plan puts them to.* The eight recorded dead
ends of `docs/scoring_model.md` §8 are marked ⚠ LEGACY-SCOPED, with their subject stated as *"this
document's scoring surface and the segmenter awaiting deletion"* (`docs/scoring_model.md:1369-1371`),
and one block says in terms that *"none of them says anything about what a rebuilt scoring layer may
do on evidence none of them had"* (`docs/scoring_model.md:1410-1411`), while another says *"none of
them says anything about extending the temporal context the analysis reads"* (`:1372-1373`).
Withdrawing a derived statement on a collision with one of these imports the very
implementation-derived material the derivation is barred from.

*Second, the collision rate measures nothing about the derivation.* A blind derivation states what
the analysis should do; a legacy dead end states what one superseded mechanism was measured to fail
at. These have different subjects, so agreement or disagreement between them is not a
trustworthiness signal in either direction.

*But the list is mixed, and that is the repair's hinge.* Some entries carry facts about the music and
the corpus that survive the implementation being thrown away — *"the premise 'an absent root means a
wrong reading' is false corpus-wide"* (`docs/scoring_model.md:1396`), and *"the overwhelming majority
of the genuine cases are bare three-note triads for which bass-as-root is the statistically correct
default"* (`:1434-1435`). Others are prohibitions on a mechanism that is being deleted. The plan
treats them as one undifferentiated class.

**The repair, in two parts.** (a) Separate the two kinds before either is used, by the test the
record already states for exactly this: *does the fact survive the implementation being thrown
away?* (`cowork_rulings_2026_08_15_method_directions.md:46-54`). (b) Replace the trust measurement
with one that has a subject in common with the derivation: the five real corpus traces already named
and already run at `cowork_joint_estimator_factorization.md:196-203` — `bwv145.5@12960`,
`bwv352@1440`, `bwv10.7@36000`, one relative-major/minor key failure, one genuinely modal
chorale — whose recorded outcome is that nine of ten traces passed and one specification
under-determination was found and amended (`:179-182`). A derived statement either predicts those
outcomes or does not, and that is a real establishment test with a recorded answer.

**A6's five test kinds do not sample the material — MERIT.**
A6 asks for *"a boundary rule, a knowledge item, an enablement constraint, a numeric threshold, and
an abstention rule"* (v3:97-99; v4:95-96), then has the other side judge whether the fifth field is
writable. **None of the five is a probabilistic factor form or a conditional-independence premise**,
and those two are the dominant statement kinds in the production inference layer's own ratified
specification: ten factors at `cowork_joint_estimator_factorization.md:73-132` and eight premises
with their false-negative paths at `:134-145`. So the test as designed would pass on five tractable
kinds while leaving the hard kind untested — which is precisely the failure v3's own §15 L2 says
*"would invalidate the entire output after all the work is done"*. **The repair is one line:** add a
factor form and a conditional-independence premise to A6's sample, and require the fifth field to be
written for both.

**Guardrail 2 — findings get no numbers and no rows — MERIT and CONFORMANCE, stated as two.**

*MERIT:* the intent is right. The named failure — a findings series that reached a large membership,
each member acquiring an owner, a lifecycle and a place in every future handover (v1:209-211) — is
real, and the record's own diagnosis agrees that a mechanism drawing capacity indefinitely is the
cause of the backlog (`CLAUDE.md:388-392`). *But the remedy is blunt where a graded one already
exists.* The record provides two routes that achieve the plan's aim without discarding the tracking:
the worth test, under which an issue bearing on neither of two named risks is DISCARDED with its
finding, its date and its reason, and *"no row, no gate, no capacity"* (`CLAUDE.md:44-48`); and the
lapse rule, under which an apparatus row stays open, stops gating and stops being owed
(`CLAUDE.md:376-392`). **The repair:** replace "no rows" with the worth test — a finding bearing on
the analysis gets its row, and the remainder is discarded with finding, date and reason. That
delivers the plan's aim and keeps the one thing the plan's version loses, which is any record that
the finding was made.

*CONFORMANCE, argued separately and carrying no merit weight:* as written, guardrail 2 collides with
the open-items register's rule (c) — every newly discovered issue gets an index row and its detail
file in the same commit that records the discovery — and rule (e), which makes prose-only tracking a
doc-sync violation (`CLAUDE.md:317-321`). **Is that rule right?** Rule (e) is right and should not
change: a prose-only obligation is one nobody can count. Rule (c) is right *as narrowed by the worth
test and the lapse rule*, which the record has already done; it would be wrong in its unqualified
form, and it no longer stands in that form.

**v4's depth axes omit the one quantity the plan was written about — MERIT.**
v4 §0 introduces three depth tiers on five axes: blast radius, error mass, how much theory settles,
density of prior attempts, and the user's own axis (v4:20-29). Four are derived and one is reserved,
which is careful work. **None of them is how implementation-derived the existing text is** — the
plan's own founding diagnosis, and the only axis that speaks directly to why a reconstruction is
needed at all. A document whose text is measured research-grounded needs a different treatment from
one that is a transcript of behaviour, and depth is exactly where that distinction should bite.
**The repair:** add the pollution axis, and take it from the measurement described in §2.4 below,
which already publishes a per-document distribution.

**v3/v4's Phase A budget — MERIT.**
v3's §0(1) correctly identifies that Phase A had no budget and that this broke the plan's own
guardrail 5. The repair chosen was three fixed session counts (v3:227-228; v4:239). In the same
section the plan says of Phase B that *"No number is fixed here because no honest basis for one
exists yet"* (v3:231-232). Both statements cannot be right about the same programme: Phase A's
numbers have no stated basis either, and A3 — walking the deletion history of every document in the
A1 set — is precisely what the plan's own L8/L9 says is unmeasured. **The repair:** state Phase A's
budget as a stop-and-report threshold rather than as an estimate, which is what guardrail 5 actually
requires and what the honest position supports.

### 2.3 What should be DROPPED — wrong at the root, not repairable by adjustment

**A1 — "the documents that specify the analysis are already computed: they are the home population
admitted by the delegation bar" — MERIT.**

This is stated in v2:74-83, v3:69-72 and v4:69-73, in each case with the instruction to *read that
derivation rather than listing documents by hand*. **Checked at the artifact, and it does not hold.**

- The population is published at `tools/audit/decisions/home_classification.json:15-18` as
  **146 entries across 34 documents**.
- **`ARCHITECTURE.md` is not one of the 34.** Neither is `CLAUDE.md`, `DEFECT_TYPES.md`,
  `docs/implementation_roadmap.md`, `docs/score_inventory.md`, `cowork_target_architecture.md`,
  `cowork_audit_protocol.md` or `cowork_design_doc_template.md`. (Established by reading the
  document keys of that artifact.)
- The exclusion is by construction, not by accident. `DECISIONS.md:250` states that entries classed
  process, project-convention or unhomed, **and every entry homed in a layer specification**, carry
  no section block because *"the criteria do not reach them"*. The home population is the population
  of **non-specification homes**. It was derived to answer the question *where does a register entry
  whose home is not a specification actually live* — which is a different question from *which
  documents specify the analysis*.

The consequence is not marginal. Every version's §1 names `ARCHITECTURE.md` as the polluted document
and cites its size (532,289 bytes; I confirmed this at the object with `git ls-tree -l` at both
`891bacc5d2` and `7d7a0e76f7` — identical, so it has not moved between the drafting commit and the
tip). `ARCHITECTURE.md` is also the canonical architecture document that wins every disagreement
(D-091, `DECISIONS.md:609`). **A2 enumerates the frame from the headings of the A1 set, and A3
enumerates every section ever deleted from those documents. Neither would touch `ARCHITECTURE.md`.**
The plan's Phase A would therefore build a frame that structurally cannot see the plan's own stated
subject.

A second, independent reason the set is wrong at the root: **it is being drained by design.**
`CLAUDE.md:582-603` makes re-homing the default closing route for every register entry whose home is
admitted by no delegation, and `tools/audit/decisions/apply_field_diff.json:36` records a document
being moved into a retired class *"because the 2026-08-07 owner-rulings wave re-homed its last four
entries and retired three other emptied documents"*. A set that shrinks toward empty as an
unconnected programme proceeds is not a stable frame for a multi-phase derivation.

This is not repairable by widening the set, because the defect is that the set answers a different
question. **The document set has to be derived from what specifies the analysis** — §3 below states
how I would do it.

**§7's parallel track, as stated — MERIT and CONFORMANCE, stated as two.**

v3:168-178 and v4:178-188 place the ground-truth ceiling measurement beside the plan, on three
grounds: it always gates as a #19 obligation, *"it is computable from data that already exists"*, and
*"Holding it behind ten ratifications buys nothing"*.

*MERIT:* the first and third grounds are correct and well cited. An establishment obligation gates
whatever its subject (`CLAUDE.md:364-366`), and #21's own text states that without the ceiling,
structural error and annotator disagreement are indistinguishable in the residual
(`CLAUDE.md:142-145`) — so every reported residual is uninterpretable until it exists. **The second
ground is not.** `CLAUDE.md:184-193` states that within the wider enumerated set the quantity is
computable by us **off-repertoire or of unchecked domain**, that *"neither computable route is
established (#19), and neither has been checked at its data"*, and that the choice between them *"is
a phase-2 design decision and is not settled here"*. The plan carries the computability and drops all
three qualifiers, which turns an undecided design question into a task that can simply be started.
**Repair, if this element is kept:** state the measurement as a design decision that is owed, not as
a computation that is available.

*CONFORMANCE, carrying no merit weight:* the ruled structure places this measurement at the
**measurement-design stage**, the fifth of six phases —
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:319-321` maps the commissioning
there explicitly, and that section was ruled whole
(`cowork_rulings_2026_08_15_phase_definition_sitting.md:42-55`). The plan does not say it is moving
a ruled placement; it says the measurement is *"entirely independent of this plan"*, which is true of
the plan and silent about the ruling. **Is the rule right?** On the evidence, **no, not as it
stands**, and I say so with grounds: the ceiling bounds the interpretation of every residual on
every axis, the obligation gates by the record's own #19 clause, and placing it fifth of six means
every measurement taken before it is uninterpretable in exactly the way #21 describes. The plan's
instinct to run it early is sound. What is wrong is the plan's account of what running it costs.

### 2.4 What is MISSING — needed for this job, and in no version

**A completeness mechanism over the outgoing text — MERIT, and the most important finding here.**

A search of all four files for `disposition`, `transfer list`, `quarantin`, `fact-gate`, `findings
ledger`, `retrospective` and `empirical findings` **returns zero matches in all four**.

The plan's four grading outcomes run in one direction: they grade **derived statements** against the
sources. Nothing in any version runs the other direction — from each statement of the outgoing text
to a recorded disposition. The landing step disposes of the old text wholesale: v1:177-179
re-banners the corresponding passages as reference; v3:158-161 and v4:168-171 mark them superseded.
**So any statement in the outgoing text that the derivation never went near is never looked at, and
nothing counts that it was not.** That is silent loss guaranteed by construction, and it defeats the
plan's own stated purpose — *"salvaging what is worth keeping"* (v1:15-16).

This is a MERIT finding: it holds without reference to any ruling. A reconstruction that claims to
lose nothing must have an accounting that runs over the thing being replaced.

*The same gap is also a CONFORMANCE collision, argued separately and carrying no merit weight.* The
ruled discipline requires every statement of an outgoing text to reach exactly one of five recorded
dispositions — adopted, relocated to the transfer list, quarantined as an audit question, discarded
under the worth test with finding, date and reason, or historical — **with completeness checked by
arithmetic** (`cowork_rulings_2026_08_15_method_directions.md:61-67`;
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:116-122` and `:295-299`). **Is
the rule right?** Yes, and its ground is the user's own recorded words: *"If we remove something from
a spec we must know where to move it to (unless it should be discarded)."* The arithmetic check is
what makes that a claim rather than an intention.

Two of the five dispositions have partial analogues in the plan — *adopted* in B3's salvage outcome,
*historical* in the re-bannering — and **three have none**: relocated, quarantined, and discarded
with its finding, date and reason. Of those, *quarantined* is the one whose absence bites hardest,
because it is the channel for an implementation description found in the current text. The plan does
have a guard here and it deserves credit: a statement supported only by the code is marked
UNSUPPORTED (v1:190-191; v3:143-147; v4:154-158). But that guard requires the deriver to recognize
that a specification sentence was written from the code, and the record's own measurement says that
is not visible: *"a narrowed rule reads exactly like a rule that was always narrow"*
(`tools/audit/july_screen_report.md:13`). So the guard is unreliable by the record's own finding, and
the quarantine channel is what the record built in its place.

**The pre-restructuring text, and the provenance measurement that already exists — MERIT.**

A search of all four files for `july`, `screen`, `b006dc15b5`, `pre-restructuring` and `preserved`
returns matches only for the phrase "preserved on disk" in the version banners. **No version names
either of the two inputs the ruled closure kept alive.**

*The measurement exists.* Every version's §1 carries the row *"No artifact in `tools/audit/` takes
either specification's provenance as its subject"* (v1:41; v2:47; v3:39; v4:40). This is **false at
the object**. `tools/audit/july_screen_report.md`, generated by `tools/audit/gen_july_screen.py`,
takes exactly that as its subject: it classifies 68 changed passages across 32 commits and 6
documents by whether the source of each change is a fact read in implementation code, and publishes
the distribution per document — `ARCHITECTURE.md` 27, `CLAUDE.md` 33, `docs/scoring_model.md` 5, and
three others (`tools/audit/july_screen_report.md:17-19`), with four verdict classes and their counts
at `:24-29`. That is a pollution measurement over both of the plan's named specifications. Its
period is bounded and its own limits are declared at `:13`, so it is not a complete answer — but the
plan's statement is that no such artifact exists, and one does.

*The earlier text exists.* The ruled closure of the restructuring phase kept two things alive by
name: *"the candidate artifacts and the July screen as the MINING MAP; the preserved
pre-restructuring version at `b006dc15b5` as the most valuable single untrusted source of the
pre-pollution text"* (`cowork_rulings_2026_08_15_phase_definition_sitting.md:114-117`). I confirmed
the commit and both blobs exist: at `b006dc15b5`, `ARCHITECTURE.md` is 383,785 bytes and
`docs/scoring_model.md` 82,528 bytes; at the tip they are 532,289 and 127,593 (all four values read
with `git ls-tree -l` at explicit hashes; these are exact object sizes, no sampling, no uncertainty
range).

This bears directly on the plan's §1(c): *"Provenance cannot be recovered where it was never
recorded, so the repair must not depend on it"* (v1:43-46). That premise is sound about *provenance*
and it does not reach *text*. The earlier text is one content-addressed read away, at a commit the
record names as the most valuable single source of the pre-pollution wording — and the plan's A3
already accepts git as a source, since it walks deletion history there. **The plan declines to use
the one source the record ruled most valuable, on a premise about a different thing.**

*What I am not claiming.* The pre-period text is an untrusted source and not a clean baseline; the
record says so, and says influence is invisible in the text. The finding is that the plan omits it,
not that it would settle anything by itself.

**Any place for a premise, and for its false-negative path — MERIT and CONFORMANCE, stated as two.**

*MERIT:* the statement form has five fields — statement, defense, source class, status, and what
would falsify it in code (v1:183-197; v3:141-148; v4:152-158). The dominant statement kind in the
production layer's own ratified specification is a modelling premise: eight of them, each with the
path that would break it and how it would be seen, at
`cowork_joint_estimator_factorization.md:134-145`. **A premise fits none of the five fields.** Its
defense is a citation, its status is settled, its source class is derived — and the thing that makes
it usable, the false-negative path, has nowhere to go. Worse, for a premise the fifth field is not
writable at all in the form the plan states it: P1's breakage shows *"as systematic emission residual
on specific voicings"* (`:138`), which is a residual diagnostic and not a code check. So a
reconstruction written in this form would silently drop the premise ledger of the one layer that has
one.

*CONFORMANCE, carrying no merit weight:* #17(a) requires every load-bearing causal claim to be
labelled FACT, THEORY or ASSUMPTION, and #17(e) requires every insulation claim to enumerate the
false-negative path explicitly (`CLAUDE.md:86-99`). The form provides for neither. **Is the rule
right?** Yes — and the eight-premise ledger is the demonstration: it is what lets a later reader test
a conditional independence rather than inherit it.

**No measurement of the plan's own founding premise — MERIT.**
v1:37-41 and v2–v4's §11/§13 both state that the plan does not measure how polluted the documents are
and *"does not need to"*. Under #18, a design may not carry load on a causal claim about our own data
that is checkable but unchecked (`CLAUDE.md:116-117`), and "the specifications are polluted by the
implementation" is exactly such a claim — checkable, as §2.4 above shows, and load-bearing for every
subsequent choice, including v4's depth tiers.

**No uncertainty anywhere in the output — MERIT.**
No version's statement form carries a confidence, a range or an establishment status for the derived
statement itself, and no version's budget carries one either: v3/v4 set the budget for everything
from the first unit at each tier, which is a sample of one. v3's L8 names this for the budget alone
and v4 inherits it unchanged. #24 requires every reported value to carry its uncertainty
(`CLAUDE.md:223-226`); a reconstruction is a series of reported claims and its own sizing is a series
of reported values.

**The per-phase retrospective — CONFORMANCE.**
Every phase closes with a recorded retrospective, ruled on 2026-08-15 and marked RULED rather than
proposed (`cowork_rulings_2026_08_15_phase_definition_sitting.md:57-82`;
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:379-399`). The plan defines
phases and closes them, and carries no such act. **Is the rule right?** Yes, on the ground stated
with it: *"a lesson that lives only in conversation is the eighteenth stop's founding failure
repeated."* Weight: low for this plan's substance, but it costs one section to add.

**The fact-gate and the empirical findings ledger — CONFORMANCE, with a MERIT consequence already
recorded above.**
The ruled preparation phase makes the fact-gate the admission mechanism for our own experimental
findings, on the test *does the fact survive the implementation being thrown away?*
(`cowork_rulings_2026_08_15_method_directions.md:46-54`;
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:92-99`), and routes measurement
outputs, probe records and coding-side reports through it (`:206-212`). The plan reads
`docs/scoring_model.md` §8 directly instead (v1:122; v4:194-196). **Is the rule right?** Yes, and
§2.2 is the demonstration: the dead-end list is mixed, the plan has no separator, and the fact-gate
is the separator the record built for that exact material. The ledger it feeds has never been built
— the plan's own fact row records one of the five preparation outputs as never built, and the boot
list draft names it (`cowork_curated_boot_list_draft_2026_08_19.md:137-147`) — so this is a real
prerequisite, unbuilt, that no version of the plan names as a prerequisite.

**A statement of what the analysis must decide, derived rather than authored — MERIT.**
v1's ten questions were authored and v1 says so (v1:75, and §14 question 1). v2 withdrew them as an
assumption under #17(a) (v2:12-15) — correctly — and replaced the unit with the section structure of
existing documents, which is a second authored object with a second unmeasured premise (v2:64-66).
**Neither version reaches the thing the record already holds.** The production inference layer's
ratified specification states what is jointly chosen — the segmentation, and per segment a
(key, chord) state with its degree vocabulary *"derived from the ground truth, not invented"*
(`cowork_joint_estimator_factorization.md:23-35`) — and then ten factors, each with its form, its
table and its published-research provenance (`:73-132`). That is a derived enumeration of what the
analysis decides, ratified by the user on 2026-07-19, and no version of the plan uses it as the unit.

### 2.5 What I CANNOT ESTABLISH

Recorded as such, and not resolved by argument.

**Whether any of the four plans is affordable.** The ruled structure exists partly to produce the
sizing facts that would answer this, and the surface states in terms that time per derived statement
and the share of differences needing a user ruling *"cannot honestly be sized before the pilot"*
(`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:564-574`). Those numbers do
not exist. Nothing in this evaluation can supply them, and I make no estimate.

**Whether blind derivation on this subject is productive (the plan's L7).** The one adjacent data
point on the record is the factorization's desk simulation, whose recorded outcome is nine of ten
traces passing with one under-determination found (`cowork_joint_estimator_factorization.md:179-182`)
— but that was a trace of an existing specification, not a blind derivation, so it does not answer
the question. Settling L7 requires running one unit, which is what a pilot is.

**Whether A5's sample size of 60 and its threshold of "more than ten" are right.** Both appear in
v3:88 and v3:217-219, and in v4:85 and v4:230-231, and **neither carries a defense anywhere in either
file.** Under the standing convention that every design decision carries its defense at its home
(`CLAUDE.md:1574-1586`) they are unsupported as written; whether the values are nonetheless correct
cannot be established from the record, and I do not guess. What can be said without guessing is that
the threshold is a hard branch to a STOP, so an unsupported value there decides whether a phase halts.

**Which register population the plan's fact row describes, as a live statement.** The row reads
*"Decisions register: 677 entries — 411 with a nameable deciding act, 182 with none, 84 ambiguous"*
(v2:52; v3:44; v4:45), cited to `tools/audit/decisions_filter_classification.json`. Those values are
accurate to that artifact (`:94` and `:100-102`). **But the artifact is deliberately pinned**, at
commit `0a2cc3f86a` (`tools/audit/gen_decisions_filter.py:131`), and the tool's own reason is stated
there: the user ruled from that split, *"and the soft-discard that followed was ruled over the
non-keep residue it defines. The discard then retires 165 of the very entries this artifact
classifies"* (`:102-105`), so a live reading would restate a completed measurement against the
population the act it authorized changed. Meanwhile the rendered index publishes **474 decisions**
(`DECISIONS.md:212`). **So the plan cites a knowingly historical value as a present-tense fact this
plan rests on**, without saying that it is historical or which act moved it. That much is
established. What I cannot establish is what the A1 population would actually be at execution time,
because the home classification was derived over the pre-discard population and no artifact in the
tree states what the discard did to it. Settling that needs a derivation this batch may not run.

**The remaining fact rows I checked all held.** For the record, since a check that passes is
evidence too: 244 / 167 / 0 for the rulings sort
(`tools/audit/rulings_sort_classification.json:206-208`, and the sort is RULED per its own `:2` and
the 2026-08-17 sitting it names); 532,289 and 127,593 bytes for the two specifications, confirmed at
the objects; `DEFECT_TYPES.md` as a table of engineering and method defect types carrying no musical
knowledge; and *"read to line 1328, about 130 lines remain"* for `docs/scoring_model.md` §8, which is
exactly right — §8 runs from `:1129` to `:1458`.

One small provenance inconsistency inside that last item, recorded because the plan asks its own
executors to declare sources before reading: the fact row *"Every hand-set scoring magnitude on that
surface is declared UNFALSIFIED, NOT ESTABLISHED"* is true — I verified it at
`docs/scoring_model.md:1447-1450` — but that line sits at 1450, inside the portion the same table
declares unread. And the unread remainder is not a residue: it holds eight of the section's recorded
dead ends (`:1367-1439`), which is the material the plan's own trust measurement depends on.

---

## 3. Task 1 §5 — the counterfactual, derived from the objective

Written separately from §2 and derived from maximum-precision inference (#4), not from the plan.
Where it lands in the same place as the plan I say so.

### 3.1 The reasoning it starts from

A specification serves maximum-precision inference in exactly one way: it lets someone state what
the analysis should do, independently of what it does, at a grain where a disagreement is decidable.
Three consequences follow immediately, and they fix the shape.

- *The unit must be where a precision change lands.* If the unit is coarser, a disagreement cannot
  be attributed; if it is finer, the statements cannot be checked against anything.
- *The unit must not assert an independence the model does not have.* Key and chord are decided
  together; a specification split into independently-derivable sections asserts a factorization, and
  an unstated factorization is an unverified causal premise (#18).
- *The programme's own founding premise must be measured before it is spent against.* "The
  specifications are polluted by the implementation" is a checkable claim about our own data.

### 3.2 Step 0 — measure the subject before choosing the method

**Widen the existing provenance measurement rather than build one.**
`tools/audit/gen_july_screen.py` already classifies a changed passage by whether the source of the
change is a fact read in implementation code the commit did not write, with four verdict classes
(`tools/audit/july_screen_report.md:31-36`) and a per-document distribution (`:17-19`). Widen its
period; do not touch its method.

*Output:* a per-document pollution distribution over the whole candidate set.
*Cost:* one working session, on the ground that the generator exists and the classes are ruled.
*Failure signal:* the distribution is uninformative — most passages land UNDETERMINED. That is a STOP
and not a licence to proceed, because it would mean the founding premise is not measurable and every
later choice would rest on an unverified causal premise, which #18 forbids outright.

*Where this differs from the plan:* the plan declines this measurement and says it does not need it.
It does need it, and v4 needs it twice, because v4's depth tiers have no pollution axis without it.

### 3.3 Step 1 — take the unit from the model

**The unit is the factor, and above it the variable structure.**
`cowork_joint_estimator_factorization.md` §1 states what is jointly chosen and §3 states ten factors,
each with its form, its table and its published-research provenance. A factor is the right unit for
four reasons, each of which is one of the requirements in §3.1:

1. **It is where a precision change lands.** Every fitted value, every table and every emission
   attaches to exactly one factor.
2. **It does not assert an independence the model lacks.** The factors are terms in one combined
   content score (`:41-56`), so a per-factor specification is a specification of a term, not of an
   independent subproblem.
3. **The independences the split does rest on are already enumerated**, with their false-negative
   paths, as eight premises at `:134-145`. The separability question is answered by the record rather
   than assumed by the plan.
4. **It is directly comparable to code**, because a factor is a term in an implemented sum — which is
   what makes the later comparison mechanical rather than interpretive.

The frame then has three tiers, each with a home the record already recognizes:

- **the variable structure and the objective** — what is estimated, and what is maximized;
- **one specification per factor** — form, table, provenance, premises with their false-negative
  paths, and fit protocol;
- **the surrounding contracts** — what is published, what the measurement grades, what consumers
  read.

The third tier is what neither v1's ten questions nor v2–v4's document sections can hold cleanly:
the fit event, the held-out protocol, the capacity budget, the licence pool, the idiom split, the
decode's tie-break and the key-axis abstention policy are ruled and attach to the estimator as a
whole (`ARCHITECTURE.md:280-383`). v1's questions have nowhere to put them; v2 corrected this and
deserves the credit recorded in §2.1a.

### 3.4 Step 2 — order by dependency through the objective, not between questions

In a joint model there is no dependency order between questions — that is what *joint* means. There
is a dependency order in the objective. The variable structure and the segmentation index every
factor; the pitch, spelling and bass factors carry the chord axis; the transition, entry and key
factors carry the key axis; the boundary and cadence factors sit at the joins. So: variables and
objective first, then the factor everything else is indexed by (segmentation and boundary), then the
emissions, then the transitions.

**This coincides with the plan's "segmentation first" (v1:88-94), and the coincidence is evidence.**
The plan reaches it from three measured facts; I reach it from the structure of the objective. Two
independent derivations landing on the same first unit is the kind of agreement that should raise
confidence in it.

### 3.5 Step 3 — prove the method on one factor, against a trace set that already has an answer

Choose the **boundary factor**. Three reasons, all from the record: it has published grounding
(`cowork_joint_estimator_factorization.md:110-114`); the record already names a real failing case for
it, `bwv10.7@36000`; and a specification error in it has a measured cost, the length-bias finding
that decided merge against split on that case (`:62-71`).

Derive it blind. Then run the derived statement against the five real corpus traces already declared
at `:196-203`, whose outcomes are on record. **The trust measurement is whether the derived statement
predicts those outcomes.** This is a genuine establishment test (#19), because the traces have a
subject in common with the derivation — what the analysis should do on real music — which the
dead-end collision test does not.

*Output:* one factor specification, plus the numbers the whole programme's budget must come from —
elapsed effort, statements produced, salvage found, open questions raised, and how much of the
declared reading turned out to matter.
*Cost:* unknown, and that is the point of the step. **No estimate is invented here** — the record
states this cannot be sized before a pilot, and I do not overrule it.
*Failure signals, declared in advance:* the derived statement cannot be written without opening the
fitted table, which would mean theory does not determine the form and the whole derive-blind ordering
is wrong for this material; or the derived statement agrees with all five traces, which would mean
the traces do not discriminate and the trust measurement is empty.

### 3.6 Step 4 — dispose of the outgoing text from the outgoing text's side

Every statement of the outgoing passages reaches exactly one of the five ruled dispositions, with
completeness checked by arithmetic. This runs in the opposite direction from grading a derivation and
is the only construction that makes "nothing is lost" a claim rather than an intention. **I reach
this from the objective and not from the ruling:** a reconstruction whose accounting runs only over
what it produced cannot know what it dropped. That it is also the ruled discipline is a convergence,
not the reason.

### 3.7 Step 5 — a statement form that can carry the material

Six fields, not five:

1. **the statement**;
2. **its defense** — the theory, the published research fetched and read, or the measurement, under
   the theory-grounding corollary that forbids carrying an equation out of a source nobody opened
   (`CLAUDE.md:268-278`);
3. **its source class** — derived, salvaged or measured;
4. **its status** — settled or open;
5. **the premise it rests on, and that premise's false-negative path** (#17a, #17e) — the field the
   plan's form has no place for, and the one without which a conditional independence is inherited
   rather than testable;
6. **what would falsify it** — in code where the statement is behavioral, **in the residual** where
   it is a modelling premise, because for a premise there is no code site to check.

Field 5 and the residual half of field 6 are what A6 must test hardest, and are exactly what A6's
five kinds never reach.

### 3.8 Where I converge with the plan, and where I differ

**Convergence — and each of these is evidence for the plan, not against it:** derive before compare;
declare the sources before reading and fix them for the pass; an adversarial placement test run by
the side that did not author the object; prove the output format before writing in it; a budget whose
overrun is a stop; segmentation first; nothing deleted.

**Divergence, and what each turns on:**

| | the plan | this derivation | what it turns on |
|---|---|---|---|
| the unit | a question (v1), then a document section (v2–v4) | a factor of the model | whether the unit must be where a precision change lands and must not assert an unstated independence |
| the document set | the delegation-bar home population | derived from what specifies the analysis, plus the pollution measurement | whether an existing derivation answers this question or a neighbouring one — §2.3 |
| the trust measurement | collisions with recorded dead ends | the five ratified corpus traces | whether the measurement shares a subject with the thing measured |
| the disposition | from the derivation outward | from the outgoing text inward | whether "nothing is lost" is a claim or an intention |
| the statement form | five fields | six, adding the premise and its false-negative path | whether the material contains modelling premises — it does |
| the founding premise | declared not to need measuring | measured first | #18 |

**Is the plan's approach substantially right?** In its **method** — yes, and I say so plainly: derive
before compare, declare before read, test the frame adversarially, prove the format first, budget with
a stop. Those five are correct, and an independent derivation from the objective reaches all five.
In its **objects** — the unit, the document set and the trust measurement — no, and those three are
where the work would actually be spent.

---

## 4. Declared departures

1. **`cowork_handoff.md` was not read.** The dispatch's read-first block declares this departure from
   the standing clause at `cowork_audit_protocol.md:274`, with its ground and its width. I record the
   departure here as executed: no block of that file was opened.
2. **Two counts in this report were produced by me rather than read from a generated artifact**, and
   both are labelled at the point of use: the 474 index rows of `DECISIONS.md` (which agrees with that
   file's own generated value at `:212`, so the two are stated together), and the presence or absence
   of search strings in the four plan files. Both are exact reads of on-disk content with no sampling.
   The byte sizes are `git ls-tree -l` output at explicit hashes, and that tool is named at each use
   per the standing character-value clause (`cowork_audit_protocol.md:564-579`).
3. **`BUILD_AND_TEST.md` was not read.** It is a conditional session-start read and the condition is
   not met: this session built nothing, tested nothing and ran no measurement tool.
4. **No `OPEN_ITEMS.md` row was opened.** I read the gating identity list as rule (a) directs and
   needed no row; [[OI-179]] was confirmed present in `gating_ids` at
   `tools/audit/nongating_apparatus_rows.json`.

---

## 5. The standing self-check over this session's own work

Run against the guiding principles, the Conventions, the gate and threshold policies, and
`DEFECT_TYPES.md`, over what is on disk rather than over the intention.

1. **What was touched.** One file created, `cc_report_plan_evaluation.md`. Nothing else. No `src/`
   change, no golden, no test, nothing under `tools/corpus/` or `tools/robust_stop/`, no open-items
   row, no specification text, no finding number, no ruling. The two guard blobs the dispatch names
   are untouched because nothing in this batch reads or writes them.
2. **#17(f) and D-431 — figures.** Every value is cited to an artifact and a field or to a
   `file:line`; the two I produced myself are labelled as such in §4, which is the honest form rather
   than a violation dressed as a citation. No value is carried across from a surface that merely
   repeats it.
3. **#24 — uncertainty.** Stated at §0: no comparison between measured quantities is asserted
   anywhere in this report, and the quantities present are exact object reads with no sampling. I have
   attached no uncertainty range where none exists, which would be worse than stating the class.
4. **#19 — establishment.** No prior verdict about the plan entered as established; the two I met are
   recorded in §1.3 with their extent. Where I could not settle a question I said CANNOT ESTABLISH
   (§2.5) rather than choosing the reading that suited the argument, as the brief's §3 requires.
5. **The brief's §4.1 — MERIT and CONFORMANCE never combined.** Four findings have both a merit and a
   conformance side; each is written as two labelled halves with the conformance half explicitly
   carrying no merit weight, and each states separately whether I think the rule is right (§2.2
   guardrail 2; §2.3 the parallel track; §2.4 the disposition discipline; §2.4 the premise field).
6. **The brief's §4.2 — both polarities.** §2.1 and §2.1a are positive findings with cited grounds, and
   §2.5 records four fact rows that checked out. This is not an all-negative return.
7. **Conventions — reserved words.** American English throughout. *Score* is never used bare in the
   numerical sense; the model's quantity is written as **the combined content score** and §0 records
   that the ratified document's own term is quoted rather than adopted. *Instrument* does not appear in
   my own prose — *measurement tool*, *check* and *generator* are used; where #19's own wording is
   invoked it is quoted. *Register* appears only as *the open-items register* or *the decisions
   register*, in full. *Root* is used only for a chord root; the other sense is written *underlying
   cause*. *Note*, *part*, *rest*, *mode*, *key*, *measure*, *figure*, *interval*, *resolution*,
   *scale*, *beat*, *flat* and *tie* were each checked for a bare non-musical use and none stands.
8. **Conventions — no self-invented labels.** No finding is numbered and no abbreviation is coined. The
   section labels MERIT, CONFORMANCE, KEPT, REPAIRED, DROPPED, MISSING and CANNOT ESTABLISH are the
   brief's own vocabulary.
9. **Never work from memory.** Every verdict rests on a source opened in this session; §1.1 lists them
   and §1.2 lists what was not opened. No claim rests on a summary, a close, a commit message or
   another session's report.
10. **`DEFECT_TYPES.md`.** Checked against my own output: no hand-transcribed measurement value
    (DT-11); no stale anchor — every `file:line` cited was read in this session (DT-12); no
    scope-assumed enumeration (DT-26) — §1.1 states what I read, §2.5 states what I could not settle,
    and the two bound each other.
11. **One thing I could not do and did not fake.** The brief asks for the counterfactual taken *"as far
    as you honestly can"*, including what each step costs. Step 3's cost is the number the whole
    programme turns on and the record states it cannot be honestly sized before a pilot. I left it
    unsized rather than invent one, and said so at the point of use.

---

*Provenance: Claude Code, 2026-08-21, at branch tip `7d7a0e76f7`, executing
`cc_instruction_plan_evaluation.md` under `cowork_plan_evaluation_brief_2026_08_21.md` and
`cowork_evaluation_boot_list_2026_08_21.md`. Every source opened is listed at §1.1 and every excluded
file at §1.2. The tip was checked once, by hash comparison; `git log` was not run.*
