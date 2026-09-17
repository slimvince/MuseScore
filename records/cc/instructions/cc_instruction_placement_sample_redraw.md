# CC DISPATCH — REDRAW AND RE-SEAL THE PLACEMENT SAMPLE

*Written by the Cowork writing side, 2026-08-27, against tip
`aa3077709117962ab05b27d79466bfacc77a2382`. Executes Rulings 1, 2 and 3 of
`cowork_rulings_2026_08_27_stopped_strata_sitting.md`. This batch performs NO ratification, orders NO
register entry, MAKES NO ADMISSION, and **DOES NOT RUN THE PLACEMENT TEST** — the frame it would be
run against does not exist yet.*

---

## 0. What this batch is, and the property that governs every instruction below

The previous batch (`cc_instruction_placement_sample.md`, report
`cc_report_placement_sample.md`) enumerated eight strata, drew four, and stopped on four. The user
has since ruled three decisions. **The consequence is that almost the whole sample is redrawn:** three
strata are drawn for the first time, three are redrawn under a corrected selection rule, one is
recorded as not enumerable, and one carries across untouched.

**★ THE GOVERNING PROPERTY, UNCHANGED FROM THE PREVIOUS DISPATCH: YOU ARE NOT PERMITTED TO CHOOSE
WHAT GOES INTO THIS SAMPLE.** You will later be the side that runs the placement test. The selection
rule is written out below by the writing side; it is deterministic. **Where the rule does not decide
something, you STOP and report. You never decide it.**

**The seal.** Committing the new file is the seal.

**What is NOT re-opened.** `T = 25`, the threshold rule, and the ordering keys are unchanged.
**`T = 25` IS DECLARED, NOT DERIVED** — no measurement in this project supports it, and you must write
it down that way wherever it appears.

---

## Task 0 — start state and landings

**(a)** Read `.git/refs/heads/master` **with the file tool**. It must read
`aa3077709117962ab05b27d79466bfacc77a2382`. **If it does not, STOP and report.** Name the side
measured wherever you state a hash.

**(b) Do NOT run `git status`** (D-253). Run:

```
python tools/audit/changed_paths.py
```

Record the population: total changed-path records, untracked, tracked modifications. **Commit none of
the standing untracked population beyond what (c) names.** If any path is tracked-modified other than
`cowork_handoff.md`, **report it and do not commit it.**

**(c) Land, in one commit**, exactly these six paths:

- `cowork_handoff.md` — **TRACKED-MODIFIED.**
- `cowork_stopped_strata_surface_2026_08_27.md` — untracked
- `cowork_declared_readings_surface_2026_08_27.md` — untracked
- `cowork_take_rule_surface_2026_08_27.md` — untracked
- `cowork_rulings_2026_08_27_stopped_strata_sitting.md` — untracked
- this dispatch

**★ THIS DISPATCH DELIBERATELY ASSERTS NO COUNT OF NEW HANDOFF ENTRIES, AND YOU MUST NOT TAKE ONE
FROM IT.** The last two dispatches each stated how many entries were new and **both were wrong**,
because the figure was taken from the previous entry's prose rather than from the object. **Establish
it yourself:** resolve `cowork_handoff.md` at the tip to its blob, compare the working tree against
it, and report (i) **how many entries are new**, (ii) whether the change is additions-only and
prepended with no earlier entry reworded, and (iii) the arithmetic that closes the two sides. If the
change is anything other than additions-only prepended, **STOP and report before committing.**

Then run:

```
python tools/audit/gen_evidence_pin_membership.py
```

---

## Task 1 — the four strata that were STOPPED, now settled by Ruling 1

**Each membership and unit below is declared FOR THIS SAMPLE ONLY.** It is not a class definition,
nothing else in this project may cite it as one, and it expires when the sample is drawn. **Write
that scoping onto the face of each stratum's section in the sealed file.**

### 1.1 Stratum 1 — ruling records

**Membership: every repository-root file whose name begins `cowork_rulings_`, `cowork_ruling_`,
`cowork_owner_rulings_`, `cowork_pending_rulings_` or `cowork_document_route_rulings_`, and ends
`.md`.** This is the class `writing-side-ruling-records` of `tools/audit/gen_artifact_inventory.py`
— **the definition that was put to the user and ruled**, at
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` §16. The narrower matcher in
`tools/audit/gen_evidence_pin_membership.py` is **not** the definition for this sample.

**Expected: 78 files.** The writing side established 74 matching `cowork_rulings_*.md` plus four
others — `cowork_ruling_guard_family_2026_08_08.md`, `cowork_owner_rulings_2026_08_07.md`,
`cowork_pending_rulings_2026_08_02.md`, `cowork_document_route_rulings_2026_08_08.md` — at the
directory listing on 2026-08-27, before this dispatch was written. **Task 0(c) lands one further
ruling record**, `cowork_rulings_2026_08_27_stopped_strata_sitting.md`, which was already on disk when
that count was taken and is included in it. **If your count is not 78, report the difference and the
names; do not adjust the membership.**

**Unit: one numbered ruling in a ruling record.**

**★ THE FORM OF A "NUMBERED RULING" IS A DECLARED READING OF THE WRITING SIDE, BECAUSE THE RECORDS DO
NOT DECLARE ONE.** A numbered ruling is **a markdown heading (fence-aware, per Task 2.3) whose text,
after the leading `#` characters and after stripping leading `*`, `_`, `★` and whitespace, matches
EITHER `^(Ruling|RULING)\s+\d+` OR `^\d+\s*[.)]\s`**. Nothing else counts.

**A record matching zero contributes ZERO items and is reported as contributing zero — never
construed into having one.** If many records return zero, that is a finding about this project's
records and it must be visible. **Report the number of records returning zero and name them.**

### 1.2 Stratum 2 — decision surfaces

**Membership: exactly the 35 paths listed below, and NO signature of any kind.** No object enumerates
this class, and a filename convention on the word *surface* is verifiably wrong — it also admits
`cc_instruction_oi179_reply_and_phase2_surface.md`, a dispatch, and
`cowork_rulings_2026_08_17_governing_surface_split.md`, a ruling record.

Root level (4):

- `cowork_extent_decision_surface.md`
- `cowork_phase1_commissioning_surface_2026_08_11.md`
- `cowork_framework_phase_opening_surface_2026_08_26.md`
- `cowork_placement_sample_surface_2026_08_27.md`

Under `ratification_surfaces/` (31):

- `cowork_artifact_inventory_ruling_surface.md`
- `cowork_claude_md_finer_split_2026_08_17.md`
- `cowork_comparison_harmony_boundary_reading.md`
- `cowork_d580_transfer_fact_gathering_2026_08_09.md`
- `cowork_deciding_act_recovery_surface_2026_08_16.md`
- `cowork_decisions_filter_surface_2026_08_15.md`
- `cowork_decisions_pending_ratification.md`
- `cowork_decisions_pending_ratification_2.md`
- `cowork_decisions_pending_ratification_3.md`
- `cowork_decisions_pending_ratification_4.md`
- `cowork_decisions_pending_ratification_5.md`
- `cowork_decisions_pending_ratification_6.md`
- `cowork_decisions_pending_ratification_7.md`
- `cowork_decisions_pending_ratification_8.md`
- `cowork_decisions_ratification_delta.md`
- `cowork_discard_reach_surface_2026_08_16.md`
- `cowork_discard_residue_surface_2026_08_16.md`
- `cowork_governing_surface_split_2026_08_16.md`
- `cowork_oi354_legacy_mark_establishment_2026_08_09.md`
- `cowork_pending_ratifications_next_session.md`
- `cowork_perspective_inventory_ratification.md`
- `cowork_phase_definition_surface_2026_08_15.md`
- `cowork_reserved_word_inventory_2026_08_09.md`
- `cowork_restructuring_period_start_decision_surface.md`
- `cowork_rule_triage_entries_2026_08_09.md`
- `cowork_ruling_registration_queue_2026_08_09.md`
- `cowork_rulings_sort_surface_2026_08_16.md`
- `cowork_sizing_pack_leak_list_reading.md`
- `cowork_sizing_tests_reading.md`
- `cowork_standing_treatment_surface_2026_08_16.md`
- `cowork_withheld_family_harmony_boundary_reading.md`

**If any listed path is not on disk, STOP and report it. Do not substitute, and do not add a path
that is on disk but not listed.**

**Unit: one numbered decision in a decision surface.**

**★ THE FORM OF A "NUMBERED DECISION" IS A DECLARED READING OF THE WRITING SIDE.** A numbered decision
is **a markdown heading (fence-aware) whose text, stripped as in §1.1, matches EITHER
`^(Decision|DECISION)\s+\d+` OR `^\d+\s*[.)]\s`**. Nothing else counts.

**★ A LISTED FILE MATCHING ZERO CONTRIBUTES ZERO AND IS REPORTED AS ZERO — NEVER CONSTRUED INTO
HAVING ONE.** The writing side expects several of the 31 to return zero: by name they present as
ratification queues or as readings rather than as documents that argue alternatives towards a choice.
**Report the count of zero-returning files and name every one.** That list is a finding about the
directory and is one of this batch's deliverables.

### 1.3 Stratum 3 — dossiers

**Membership: exactly these 25 repository-root files.** They are the 26 root-level files matching
`*_dossier.md` **minus** `cc_instruction_stage3_4i_gate_retirement_dossier.md`, which the ruled
whole-tree classification already places in `dispatches-to-the-coding-side`.

- `cc_anchor_design_dossier.md`
- `cc_anchor_redesign_dossier.md`
- `cc_b_guard_scoping_dossier.md`
- `cc_cadence_key_investigation_dossier.md`
- `cc_cadence_precision_investigation_dossier.md`
- `cc_functional_residual_dossier.md`
- `cc_j_key_iii_integration_dossier.md`
- `cc_joint_architecture_dossier.md`
- `cc_key_emission_headroom_dossier.md`
- `cc_layer1_audit_dossier.md`
- `cc_layer2_audit_dossier.md`
- `cc_layer3_decoder_audit_dossier.md`
- `cc_layer3_keymode_audit_dossier.md`
- `cc_layer3_wiring_design_dossier.md`
- `cc_layer4_audit_dossier.md`
- `cc_metric_first_dossier.md`
- `cc_modulation_keypath_scoping_dossier.md`
- `cc_module_layering_assessment_dossier.md`
- `cc_precision_headroom_dossier.md`
- `cc_refactor1_split_design_dossier.md`
- `cc_stage2_2_ab_dossier.md`
- `cc_stage3_4i_dossier.md`
- `cc_stage4b_scoping_dossier.md`
- `cc_tonicization_modulation_metric_dossier.md`
- `cowork_adjudication_dossier.md`

**If any listed path is not on disk, STOP and report it.**

**Unit: every markdown list item at any nesting depth** — the same reading confirmed for the evidence
inventory by Ruling 2 — **enumerated fence-aware per Task 2.3.**

**★ RECORDED IN THE RULING AND TO BE WRITTEN ONTO THE FACE OF THIS STRATUM IN THE SEALED FILE:** the
dispatch's original unit was *"one claim or finding entry in a dossier"*; **no dossier declares such a
unit and this is a mechanical stand-in that will over-admit ordinary prose bullets.** Consequently a
**placeable** result from stratum 3 is weak evidence and the placement report must say so where it
reports stratum 3. An **unplaceable** result from stratum 3 is unaffected.

### 1.4 Stratum 6 — declared dormancies — **NOT ENUMERABLE. Do not draw it.**

**Do not enumerate this stratum and do not draw from it.** Write a section for it in the sealed file
recording it as **NOT ENUMERABLE**, with the three candidate readings and why each fails:

1. the evidence inventory's DORMANT-status rows plus its §8b `Declared future consumers, named by the
   user (2026-07-13)` — **enumerable, but its rows sit inside `cowork_evidence_inventory.md`, which is
   stratum 5**, so it is a subset of a stratum already in the sample and would double-count across two
   strata that must be reported separately;
2. the free-text declarations across `ARCHITECTURE.md`, dispatches, reports and per-layer audit
   dispositions — the reading with real coverage, **not enumerable at all until a marker convention
   exists**, which is construction work and not a ruling;
3. the specification document set's per-member `live_or_dormant` property — **a different subject**
   (whether a document is dormant, not whether a published fact is), ruled out by name.

**Write, in that section:** the concept is ratified at `CLAUDE.md:251-255` and **this project has
never built a population of it.** That record is stratum 6's contribution to the placement test.

---

## Task 2 — the units confirmed by Ruling 2, for the strata that were already drawn

### 2.1 Stratum 5 — the evidence inventory

**Membership: `cowork_evidence_inventory.md`, one file.** **Unit: every markdown list item at any
nesting depth**, enumerated fence-aware per §2.3.

**★ STOP CONDITION.** Ruling 2 confirms this reading **at `N = 33`**. Fence-awareness was ruled for
markdown headings, and this dispatch extends it to list items by parity of reasoning — a `-` line
inside a fenced code block is not a record. **If the fence-aware enumeration does not return exactly
33, STOP and report the difference and the excluded lines.** Do not proceed on a different `N` for
this stratum.

### 2.2 Strata 7 and 8 — "member" means the whole member FILE

**The whole member file, not only its delegated sections.** `delegation_scope` governs how far a
delegation reaches; it is **not** a boundary on the population. `ARCHITECTURE.md` contributes all of
its headings, not the three named regions'.

Membership for both is `tools/audit/specification_document_set.json`. **Run
`python tools/audit/gen_specification_document_set.py --check` first**, read-only, to establish the
artifact is current; if it does not re-derive, **STOP and report**.

### 2.3 Both strata, and every list-item enumeration in this dispatch — **fence-aware**

A `#` line inside a fenced code block is a shell comment, not a heading; a `-` line inside one is not
a list item. **Exclude the contents of fenced code blocks everywhere in this batch.** Report the
excluded lines by file and line number, as the previous batch did, so they can be checked by eye.

**Expected, from the previous batch and unchanged by any ruling: stratum 7 `N = 730` (naive 737),
stratum 8 `N = 59` (naive 60).** If either differs, report the difference; **do not adjust.**

### 2.4 Stratum 4 — the DEFERRED entries of the decisions register — **carried across unchanged**

`N = 21`, at or below the threshold, therefore a **census**. No take rule applies to it and Ruling 3
does not touch it. Re-enumerate it to confirm `N = 21` and carry the census. **If it is not 21, STOP
and report** — the register has changed under a stratum the user was told carries across untouched.

---

## Task 3 — the selection rule, as corrected by Ruling 3

### 3.1 The ordering — unchanged, and no other ordering is permitted

Within each stratum, order the enumerated items by this tuple, ascending:

1. the repository-relative path of the file the item is found in, by byte order;
2. then the line number at which the item begins;
3. then, **for stratum 8 only**, the hash of the commit that deleted the heading, lexicographically.

**Do not order by importance, recency, topic, length or interest.** If two items coincide on all three
keys, STOP and report — that means the unit is ambiguous and the writing side must fix it, not you.
*(The previous dispatch worded this condition with a word `CLAUDE.md` reserves for the notated tie;
this one avoids it. The condition is unchanged.)*

### 3.2 The threshold — unchanged

Let `N` be a stratum's enumerated count and `T = 25`.

- **If `N ≤ T`: the stratum goes in WHOLE.** Census; no uncertainty range needed.
- **If `N > T`: the stratum contributes exactly `T = 25` items**, at the positions §3.3 gives.

**`T = 25` IS DECLARED, NOT DERIVED. Write it down that way wherever it appears.**

### 3.3 ★ THE TAKE — REPLACED BY RULING 3. THE OLD FORMULA IS VOID.

**Do not use `1, 1+k, …, 1+24k`. It has a defect and it is superseded.** Its last reachable position
was `1 + 24·floor(N/T)`, so the end of every large stratum's ordering was impossible to draw — and
because the ordering is path-then-line, that region is always the end of the last-sorted files, an
exclusion correlated with content.

**The take, for `i = 0 … T−1`, at 1-indexed ordered position:**

```
p_i = 1 + ( i * (N - 1) + 12 ) // 24
```

**Integer division. `12` is `(T−1)/2` and `24` is `T−1`, with `T = 25`.** Use integer arithmetic
exactly as written. **Do not use a rounding function** — a rounding rule has an implementation-defined
answer at exactly one half, and this rule must be deterministic.

**★ SELF-CHECK, MANDATORY, PER STRATUM WITH `N > T`.** Before drawing:

- `p_0` **must equal 1**;
- `p_24` **must equal `N`**;
- the 25 positions must be **strictly increasing and distinct**.

**If any of the three fails, STOP and report. Do not adjust the formula.**

**Worked values to reproduce, as an arithmetic check on your implementation** — for `N = 33`,
`p_0 = 1` and `p_24 = 33`; for `N = 59`, `p_0 = 1` and `p_24 = 59`; for `N = 730`, `p_0 = 1` and
`p_24 = 730`.

**Recorded so you do not report it as a defect you found:** item 1 and item `N` are **always** drawn.
That is a known and declared cost of the corrected rule, not an error.

---

## Task 4 — write the new sealed sample

**Path: `cowork_placement_sample_sealed_redraw_2026_08_27.md` at the repository root.** Chosen by the
writing side on the existing root convention; it is not ruled and the user may rename it in one line.

**★ DO NOT DELETE, EDIT, MOVE OR REGENERATE `cowork_placement_sample_sealed_2026_08_27.md`.** It
stands as the record of what was drawn under the defective rule. The new file **supersedes** it and
says so in its banner.

**★ THE BANNER MUST CARRY, IN THIS ORDER AND WHERE IT CANNOT BE MISSED:**

1. **DO NOT READ IF YOU ARE AUTHORING THE FRAME.** This file is withheld from the frame's author
   alongside the code. **And so is the superseded file** — name it, so the author does not read the
   old one believing only the new one is withheld.
2. That this is the **sealed** placement sample, drawn at tip
   `aa3077709117962ab05b27d79466bfacc77a2382`, and that it is closed.
3. That it **supersedes `cowork_placement_sample_sealed_2026_08_27.md`**, which was drawn under a take
   rule since found defective, and that the superseded file is kept, not deleted.
4. That `T = 25` is **declared, not derived**.
5. That **stratum 6 is NOT ENUMERABLE and is not drawn**, and that **no stratum remains STOPPED** —
   so the frame's gate is no longer a decision, only this file's existence.

**Per stratum, the body carries:** the defining object or the explicit path list; the quoted text
establishing it where there is one; the declared scoping (*for this sample only*) for strata 1, 2 and
3; `N`; census or take; the drawn items, each with its **verbatim text** and its `path:line`
provenance. For stratum 3, the weak-evidence note of §1.3 on its face. For stratum 2, the list of
zero-returning files on its face.

**What this file does NOT carry:** any judgement about whether an item is placeable, any grouping by
topic, any commentary on the frame, any ranking. **It is a list.**

---

## Task 5 — the root-population hazard

`tools/audit/gen_filing_convention_application.py` is the guard behind the one standing DECISION red,
`[[OI-372]]`. At the previous batch's close its derived candidate population was **18** and its STOP
list was **four**.

**This batch adds root-level `.md` files — the new sealed file, this dispatch's report, and Task 0(c)
lands four more.** Read the tool's candidate derivation and report, **before writing the sealed file**,
which of them you expect to enter. Then run the sweep with everything on disk and report the measured
candidate list and STOP list.

**If the list widens: report it prominently, do NOT classify it, do NOT cure it, and do NOT regenerate
the guard.**

**★ AND DO NOT SHAPE ANY FILE TO STAY OUT OF THAT POPULATION.** Write each file as its content
requires and let the guard say what it says.

---

## Task 6 — `STATUS.md`, the forward bound, the sweep, the report, the commit

**(a)** One **POINTER** entry in `STATUS.md` (OI-222 remedy; **D-431**: no count, no identity, no
rendered value). **Exactly one — the previous batch's self-check had to remove a second one.** **Write
it BEFORE running the forward-bound tool.**

**(b)** Re-aim `tools/audit/gen_status_batch_bound.py` — the **five** aiming constants — and
**append** the outgoing aiming to `PREVIOUS_AIMINGS` rather than overwriting it (#12). Both are inside
the carve-out ruled for this tool by name. Read the tool's own parser for the flag; report the exact
command line and the values set. **`TASK` is a choice — declare which task number you used and why.**

**(c) The sweep:** `gen_guard_state.py`, then `gen_guard_classification.py`, in that order, to a
fixpoint. **Do not pass `--help` to either** — the previous two batches both did, and in at least one
the flag was inert and the tool ran the whole sweep in write mode. Three reds are standing and are
**not yours to cure**: `[[OI-372]]`'s guard, `apply_soft_discard.py --check`,
`apply_residue_discard.py --check`. A staleness red caused by this batch's own writes is cured under
the standing sweep rule. **For any other red: if you cannot tell whether it is a decision red or a
regeneration red, treat it as a DECISION red and STOP.**

**(d)** Write `cc_report_placement_sample_redraw.md` at the root, then commit. State separately:

- the Task 0(c) establishment of the modified handoff, **including your own count of new entries and
  how you derived it**;
- **for each of the eight strata**: its defining object or path list, your quotation where there is
  one, its `N`, census-or-take, and — for every take — the 25 positions your formula produced, with
  `p_0` and `p_24` shown;
- **stratum 1's count of records returning zero numbered rulings, with names**;
- **stratum 2's count of files returning zero numbered decisions, with names**;
- stratum 6 recorded as NOT ENUMERABLE;
- whether the root population widened, and its measured candidate and STOP lists;
- every path written;
- **every departure and every instruction you could not obey.**

*(The report cannot carry its own closing commit hash. If you add it in a second commit whose whole
diff is that line, declare it — the precedent is this project's own and was declared last batch.)*

---

## §7 THE FENCE

Writes permitted at **exactly** these paths:

- `cowork_placement_sample_sealed_redraw_2026_08_27.md` — new
- `cc_report_placement_sample_redraw.md` — new
- `STATUS.md` — one pointer entry
- `tools/audit/gen_status_batch_bound.py` — the five aiming constants and the appended row, carve-out
- the six Task 0(c) landings and `tools/audit/evidence_pin_membership.json`
- **any file a tool this dispatch orders you to run writes as its own output.** Name each in the
  report.

**Explicitly forbidden.** **No frame text authored, no part of the frame written, no statement placed,
no judgement about placeability recorded.** No edit, deletion or regeneration of
`cowork_placement_sample_sealed_2026_08_27.md`. No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md`
edit. **No register entry** — this batch performs no ratification, so rule (c) is not engaged and the
two mutually unsatisfiable discard-act checks stay out of its path. *(That is again a batch shaped to
route around the register blocker rather than to cure it — the sixth consecutive one. It is recorded
here, not hidden; curing it is a decision act that has never been put to the user.)* No item added to,
removed from or reordered in the sample except by the rule at Task 3. **No existing ruling record,
surface, dossier, register entry or inventory row edited — you are reading these, not maintaining
them.** No `src/` change, no test changed, moved or run, no golden. Nothing under `tools/corpus/` or
`tools/robust_stop/`. No open-items row created, flipped or discarded. No finding number allocated.
Neither blind output opened; neither pack, the generator, the manifest or any withheld family
touched. No other `.py` source edited. Do not cure the two discard-act checks; do not regenerate
`[[OI-372]]`.

**★ THE STANDING CLAUSE.** **If obeying any instruction here would require a write outside this
fence, STOP and report the conflict. Do not choose a route, do not widen the fence, and do not
substitute a weaker form of the instruction to stay inside it.** Stopping and reporting is the
correct outcome.
