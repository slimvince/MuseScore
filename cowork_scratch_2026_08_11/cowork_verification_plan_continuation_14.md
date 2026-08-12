# Verification plan for the fourteenth return continuation's report

> **STATUS: COWORK WORKING DRAFT, written 2026-08-11 while
> `cc_instruction_return_continuation_14.md` is still running. It is OUTSIDE the tree by
> design — Cowork is READ-ONLY on the repository until that dispatch stops.** It is not a
> dispatch, not a ruling record, not a decision surface, and it asks no question. Its one
> job is to fix, BEFORE the report exists, what each of its claims will be checked at — so
> that verification is a comparison against a pre-recorded expectation rather than a
> reading of CC's own account of itself.
>
> **★ LANDING NOTE (2026-08-11, appended at the verified STOP; the banner above is preserved
> as written, #12). THE VERIFICATION HAS RUN.** The dispatch completed, the report was checked
> against every expectation below, and **the outcome is recorded in `cowork_handoff.md`'s
> entry-point block, which is its home — it is not restated here (#6).** The file is now in the
> tree at `cowork_scratch_2026_08_11/`, so *outside the tree* describes where it was written.
> **§7's closing sentence has come true:** this plan is superseded as a plan. It is kept as
> evidence of how the verification was conducted — specifically that its expectations were
> registered before the answers were visible.
>
> **★ WHY IT IS WRITTEN NOW RATHER THAN ON RETURN — CORRECTED 2026-08-11, and the former
> claim is preserved because it was the reason given and it was wrong (#12).** It formerly
> read: *"The pre-batch values below can only be read at HEAD-before-the-batch. Once the
> batch commits, the artifacts carry the new values and the old ones are recoverable only
> through git objects."* **That is false for a tracked artifact.**
> `tools/audit/phase1_finish_line.json` is committed, so its pre-batch value is recoverable
> at any time by a git object read at an explicit hash — which is the one shell use D-253
> sanctions. §2 is therefore a CONVENIENCE, not a rescue.
>
> **What genuinely cannot be recovered after the fact is §3: an expectation registered
> BEFORE the report exists.** Git preserves what the values were; it cannot preserve what
> Cowork expected them to be, and a prediction written after reading the answer is not a
> prediction (#17b). That is the whole of this file's time-sensitivity, and it is smaller
> than the claim it replaces. The failure it guards against is unchanged and is on this
> arc's record twice: two direction-claims were inverted against their own artifacts, and
> one of the two survived a structure-only verification.
>
> **★ EVERY VALUE BELOW WAS READ BY COWORK AT THE ARTIFACT NAMED, at HEAD, on 2026-08-11.**
> They are recorded here as a verification baseline, not published — this file is not a
> surface any derivation reads, and nothing here is a home for anything (#6).
>
> **★ THE ONE TENSION IN THIS FILE, NAMED RATHER THAN PAPERED OVER.** D-431 says values
> enter documents by citation to a generated artifact and never by transcription, and §2
> transcribes. The reason D-431 gives is that a transcribed value goes stale silently and
> is then carried — and **a pre-batch snapshot is the one case where that reason inverts**,
> because its whole job is to hold a value the artifact will no longer carry. It is
> therefore transcribed deliberately, kept outside the tree, read by no derivation, and
> **superseded the moment the report is verified.** If any value below is used for
> anything other than comparison against a post-batch read, that is the breach D-431
> forbids.

---

## 1. The three things being verified, kept apart

A report makes three kinds of claim and they fail in different ways, so they are checked
differently and are not run together.

1. **That an act was PERFORMED** — an edit exists at the document named. Checked by reading
   the document, or the committed blob by explicit hash.
2. **That a population MOVED, and in which DIRECTION** — checked by comparing the artifact's
   field at HEAD against §2's pre-batch baseline. **A structure-only check does not catch an
   inverted direction claim**; the value is read.
3. **That nothing else moved** — the read-only default. Checked at the commit's own file
   list, never at the report's assurance that it held.

---

## 2. The pre-batch baseline, read at the artifacts before the batch

**Source: `tools/audit/phase1_finish_line.json`, read at HEAD 2026-08-11.**

| Field | Value before the batch |
|---|---|
| `counted.items_on_the_finish_line` | 9 |
| `counted.items_that_gate` | 8 |
| `counted.register_entries_owed_a_home` | 21 |
| `counted.register_entries_owed_a_defense` | 0 |
| `counted.open_rows_owed_on_the_true_half_that_gate` | 42 |
| `counted.open_rows_owed_a_reach_verdict` | 17 |
| `counted.register_entries_owed_a_home_at_document_granularity` | 28 |
| `counted.register_entries_discharged_by_an_entry_level_ruling` | 7 |
| `counted.items_with_a_closing_route_only_the_user_may_take` | 1 |

Per-item populations, same artifact, same read:

| Item | Entries before | Documents before |
|---|---|---|
| Home document named in NO user-ratified surface | 10 | 8 |
| Home document named only in a form the bar excludes | 0 | 0 |
| Admitting delegation does not reach the section | 1 (D-402) | 1 |
| Delegation reaches, section records findings | 9 | 4 |
| No home at all | 1 (D-289, at `cowork_handoff_archive.md:3082`) | — |
| Defense not stated | 0 | — |

The gating TRUE-half row set before the batch, 42 rows, includes every row this batch acts
on: **OI-320, OI-322, OI-324, OI-369** (Task 0/2), and the session-small drain rows
**OI-45, OI-47, OI-90, OI-107, OI-150, OI-183, OI-274, OI-282, OI-304, OI-315, OI-318,
OI-321, OI-332** (Task 3). **OI-346 is NOT in that 42** — it sits in the 17-row reach item's
`rows_outside_it` list, which matters for §4's Task 1 check.

---

## 3. Predictions, registered before the report (#17b applied to Cowork's own verification)

**These are Cowork's expectations, not CC's claims.** A report that disagrees with one is
not thereby wrong — but the disagreement is investigated at the object before the report is
accepted, and a report that AGREES with all of them is not thereby verified either.

- **P1 — Ruling 61.** The no-home-at-all item's population goes **1 → 0**;
  `register_entries_owed_a_home` goes **21 → 20**;
  `register_entries_discharged_by_an_entry_level_ruling` goes **7 → 8**, with D-289 named in
  that item's `discharged_by_an_entry_level_ruling` field.
  **★ P1 IS SHARPENED BY OI-369's OWN ESTABLISHED FINDING, read at the row 2026-08-11, and
  the sharpening turns it from an expectation into two mechanism checks.** The row
  establishes at the generator that the four sibling items subtract through a `recut` helper
  reading `tools/audit/decisions/r1_superseded_reach.json`, **whose population is item 1's
  NO-HOME class and nothing else** — while D-289 sits in the decisions register's `unhomed`
  class, **a different cut**. The row's words: *"the subtraction could not reach this entry
  even if the item were built through the helper, because the artifact the helper consults
  never considers it."*

  - **P1a — wiring the item to the existing helper is NOT sufficient and would leave the
    population at 1.** For Ruling 61 to do what it says, the artifact's own cut must be
    EXTENDED to reach the `unhomed` class. Checked at the artifact's population definition,
    not at the item's output.
  - **P1b — a report claiming the item emptied WITHOUT that extension contradicts an
    established finding.** It is a STOP, not a discrepancy to reconcile in prose.
  - **P1c — extending the cut can move entries other than D-289**, which is precisely what
    A1's own STOP names. The reconciliation must enumerate every mover with its ground.

  *And the condition beneath all three:* the D-642 subtraction discharges an entry only where
  its live content is carried by a **homed successor**, and **Ruling 6 attached that
  condition explicitly** — *the successors carry ALL of its live content … a content residue
  no successor carries is a STOP back to the user.* OI-369 records that **D-287 and D-288 are
  homed and D-284 is NOT** — it is itself superseded and classed `gap`, chaining onward to
  D-036 with D-001/D-010, which that row did not re-check and does not rest on. **So a
  subtraction testing successors one level deep answers NO for D-289 and does not subtract
  it; only one following the chain answers YES.** Which of the two the machinery does is a
  checkable fact about the code, and it is checked rather than inferred from the item's
  output.
- **P2 — the gating row count.** Falls from 42 by the number of rows that flip. **It does
  not fall by 17.** OI-274's and OI-321's further halves are `NEEDS-RULING` and were not
  ruled at the fourteenth stop, so those two rows are expected to be HELD or to flip only
  in part; OI-332's third item IS resolved by Ruling 62, so OI-332 may flip whole.
  *A report claiming all thirteen drain rows flipped is checked row by row before it is
  believed.*
- **P3 — Ruling 60's entry.** The clause registered is the **second half of Ruling 59** —
  the bound-instead-of-a-measurement test — and nothing else. Its expected home is
  `cowork_audit_protocol.md`'s dispatch-protocol section, beside D-431, D-434, D-436,
  D-640–D-644, because the clause is about D-436's third condition and D-661.
  **If the entry lands anywhere else, the home is checked against what §19 actually
  proposed**, not against this expectation.
- **P4 — Ruling 64.** **ONE line** in `CLAUDE.md`, **conditional** on the `scoring_model`
  pattern (*any session that touches the joint estimator's behaviour reads …*). An
  unconditional mandatory-read line is the alternative the ruling **excluded by name**, and
  writing one would be a widening of a governing surface past its licence.
- **P5 — the guard set.** Zero failing, index lint passing, bijection holding. **A green
  guard set is expected and establishes nothing about the finish line** — it is a statement
  about the record's own machinery, as the commissioning surface says of itself.

---

## 4. Per-task checks, each naming its object

### Task 0 — the rulings' register and machinery acts

| Claim | Checked at |
|---|---|
| Ruling 60's entry exists, with a verified identifier | `DECISIONS.md` INDEX (identifier present, status cell opens with a canonical token) **and** its `decisions/group_*.md` entry |
| The entry landed in the commit that records the ruling (D-230) | `git show --stat <sha>` — the ruling record and the decisions register's data in ONE commit |
| The entry is generated, not hand-edited (the decisions register's rule (d)) | `tools/audit/decisions/backbone_decisions.json` changed **and** `gen_decisions_register.py --check` passes |
| The queue's §20 extension is by the same derivation | The section's own text; that §1–§19 are untouched — checked at the committed blob, not at the claim |
| A1 — the sibling subtraction is IMPORTED, not re-implemented (#6) | The generator source: a call into the shared subtraction, not a second copy of it |
| A1 — the movement reconciles both ways | The artifact's own reconciliation fields **and** §2's baseline; **values, not structure** |
| A1's STOP — any mover beyond D-289 and the defined class | The item's before/after entry lists, diffed by identity |
| OI-369 flips | `OPEN_ITEMS.md` INDEX row (canonical opening token) + `open_items/OI-369.md` carries a dated resolution note and **no status of its own** |
| Ruling 62's convention is written beside the Ruling 28 kind list | `cowork_design_doc_template.md`, at that list |
| Ruling 63's homing (A4) | `ARCHITECTURE.md` — the rule restated where the emission's evidential contract lives; the receiving section's kind judged BEFORE the write (D-668 step order); the phase-1z note **annotated, not reworded** (#12) |
| Ruling 63's small half | The `no exception` → `no PIECE-START exception` correction; OI-324's index row flips |
| Ruling 64 (P4) | `CLAUDE.md` — one line, conditional |

### ★ Ruling 63's homing, checked in detail — the one act in this batch whose subject is the analysis

Read at `open_items/OI-324.md`, 2026-08-11, before the batch reported.

The row establishes that **D-057 did not go stale — its home moved under it.** The
priority-of-evidence table (actual sounding notes strongest, notated signature weak, mode tag
weakest) is still implemented at the legacy key resolver, and the phase-1z scoping sentence
disclaims that whole section as describing the production key path — while **OI-228, a live
row about the production emission, rests on that very table** as the source the joint emission
departs from. Ruling 63 rules reading (i): the rule is **cross-cutting** and binds both arms.

| Claim | Checked at |
|---|---|
| The receiving section's KIND was judged BEFORE the write (D-668's step order) | The judgment and its evidence exist as an authored input; a write with the judgment recorded afterwards inverts the procedure |
| Step 1 — the pointer move — was tried first and its outcome recorded | The act's own log; **HOLD rather than write by stretch** is the procedure's own instruction |
| **The restated rule is NORMATIVE, not DESCRIPTIVE** | The written text. **This is the sharpest check in the act.** The production emission demonstrably reads STRUCK tones — that is the whole struck-versus-sounding family (OI-215, OI-226, OI-227, OI-228). So a sentence saying the joint emission *ranks sounding notes strongest* would be **FALSE AT HEAD**, creating doc-sync debt (C5) while purporting to discharge some. The rule states what SHALL be; the departure stays recorded at OI-228 as a non-conformance |
| The phase-1z scoping note is **annotated, not reworded** (A4, #12) | The original scoping sentence survives **verbatim**, with an annotation beside it |
| The small half's correction | *"no exception"* → *"no PIECE-START exception"*, removing the apparent contradiction with the one-narrow-fallback sentence, and qualifying a predicate that named no argument |
| OI-228's premise base kept sound (#17a) | OI-228's citation of D-057 still resolves to a rule that binds the arm OI-228 is about |
| Every site located by its **quoted words**, never by line number | The row's own coordinates have already drifted, which is D-307's point |

**And one consequence, recorded so it is not read as a defect when it appears:** after this
act the production arm is non-conformant to a rule now stated in its own specification. That
is the intended outcome, not a new problem — the decisions register records what was decided,
and non-conformance is tracked as ordinary rows pointing back at the decision violated. Ruling
63's own stated purpose is keeping OI-228's premise base sound.

### Task 1 — OI-346's marks

| Claim | Checked at |
|---|---|
| A5 — state derived fresh | The artifact that owns the marks, at HEAD, not the previous batch's account of it |
| A5 — each member's establishment performed inside its own act | Per member: the establishment's own evidence exists. **A member marked with no establishment beside it is a STOP**, whatever the report says |
| A member whose establishment failed is HELD with evidence, never marked | The held list, per member, with its reason |
| OI-346 flips whole, or reports exactly which members stand | The INDEX row; if partial, the row does not flip |
| Whether the flip moves the reach item's 17 | `open_rows_owed_a_reach_verdict` against §2's baseline — **an open question, not a prediction** |

### Task 2 — Ruling 62 applied

| Claim | Checked at |
|---|---|
| A2 — the enumeration is DERIVED | A generator exists and the enumeration is its output; the known instances entered as **seeds**, not as the answer |
| A2 — each kind call stated per document | The per-document verdict with its ground |
| A2's STOP — a document the two branches do not decide is HELD | The held list. **A document bannered by stretch is the failure this assumption exists against** |
| **Branch-one banners are INSERTIONS ONLY, zero body edits** | **Mechanically**, per file: the committed blob diffed by explicit hash; the only added lines are the banner. This is the highest-value check in the batch and is not delegated to the report's assurance |
| A3 — the score-inventory correction follows gate blocks (A)/(C)'s own split | `docs/score_inventory.md` against those two blocks, read at `CLAUDE.md` |
| A3 — no acceptance figure transcribed into prose (D-431) | The diff of that file: any bare numeral standing where a pointer belongs |
| OI-320, OI-322 flip; OI-332's third item resolved | The three INDEX rows and their detail files |

#### ★ Ruling 62's two named instances, read at their rows before the batch reported

**OI-322 — branch one, the re-bannering.** The audit runs three hundred and forty-odd lines
describing five deleted things in the present tense, with file and line citations into
`tools/batch_analyze.cpp`, and puts **three questions to the user that were answered by
deletion** — each marked *"(do not choose for user)"*. Its correcting sentence sits in its
last line, after everything it refutes.

- The banner must state **the subject's fate and the deleting commit**, which the audit's own
  closing line names. A banner saying only *this is a historical record* does **not** reach
  the defect the row records — a reader meeting the three questions and not the closing line
  is still invited to decide something already decided, and the answer is register entry
  **D-067**.
- **Body untouched, verified mechanically**, not by assurance: the dangling citations stay,
  which branch one accepts, because a top banner is met first.

**OI-320 — branch two, the body correction, and it carries an ORDERING hazard.** Four sites in
`docs/score_inventory.md` state the superseded batch gate as current. **Site 4 is different
from the other three**: the row says in terms that it is *recorded as the fourth site rather
than measured*, and points at **OI-150** as the standing row for stale suite baselines, *with
its own trigger discipline*.

- **OI-150 is in THIS batch's Task 3 drain.** So either OI-150's build-and-run happens FIRST
  and site 4 is stamped from that completed run, or site 4 must POINT rather than state.
  **A new value written at site 4 with no run behind it is a STOP** — the same shape already
  registered for OI-150 itself.
- **A3's real test is subtractive:** after the correction the document should carry **no
  acceptance values at all**, the sites pointing at gate blocks (A)/(C). Checked by looking
  for surviving bare numerals, not by reading the claim that none were transcribed.
- Per site, the governing-versus-diagnostic call must follow blocks (A)/(C)'s **own** split —
  block (C) deliberately keeps the batch form runnable as a diagnostic, so a site may
  correctly become *the diagnostic* rather than *the block-(A) unit*.

#### ★ A2's kind calls: the enumerated list does not decide the branch on its own

Read at `cowork_design_doc_template.md`'s kind list, 2026-08-11. **Ruling 62 says the kind
call follows that list. The two partitions are different cuts, and this is structural rather
than occasional.**

The list partitions by **structure-conformance genre** — eleven kinds, of which kind 9 is
*report or dossier, a dated record of what one investigation or measurement found*. Ruling 62
partitions by **dated report versus live governing surface**. They line up for kind 9, and
they do not line up elsewhere:

- **Kind 2, design document** — branch one only when *falsified or superseded*, which is a
  STATUS the kind list does not carry.
- **Kind 11, inventory or census** — `docs/score_inventory.md` is one, and it is branch two.
- **Kinds 10 and the exempt working genres** — the list places them; the branches do not.

**So the deciding property is a STATUS, and the kind list records a GENRE.** Two consequences,
both registered as expectations:

- **A2's derivation is the right instrument for the actual question** — it reads banner and
  closing-line signatures, which are status signals, seeded with the known instances. It is
  Ruling 62's phrase *follows the enumerated kind list* that under-describes what the call
  needs.
- **★ A SUBSTANTIAL HELD SET IS THE CORRECT OUTCOME, NOT A SHORTFALL.** A2's own STOP says a
  document the two branches do not decide is HELD to the user and never bannered by stretch,
  and Ruling 28's list carries the same STOP for an unlisted kind. **A report bannering the
  tree's completed audits cleanly with no holds is more suspicious than one with holds**, and
  is read that way rather than as thoroughness.

### Task 3 — the session-small drain

Per row, two separate checks, and the second is the one that matters: **(a)** the INDEX row
flipped with provenance; **(b)** the underlying act actually happened at the document the
row names. A flip without (b) is an index edit, not a discharge. Rows: OI-45, OI-47, OI-90,
OI-107, OI-150, OI-183, OI-274, OI-282, OI-304, OI-315, OI-318, OI-321, OI-332.

**OI-150 carries a build-and-test half** — build at HEAD, run both suites, re-stamp both
`BUILD_AND_TEST.md` baselines from those runs. Its values must come from **completed
processes' own exit codes**, which is the shape the thirteenth continuation deliberately
declined to predict. A stamped baseline with no run behind it is a STOP.

### Task 4 — the close

| Claim | Checked at |
|---|---|
| The finish line's end state derived fresh | The artifact's own regeneration, not the close's prose account of it |
| The remaining set grouped by blocker | Against the commissioning surface's §3 tables — a derivation plus authored sizing, **never a completion claim** |
| Phase 1's completion statement not written, drafted or partially written | The tree: no file drafts one |

---

## 5. The cross-cutting checks, run whatever the report says

- **Commit count and identity.** Counted by Cowork at the objects, per reported SHA
  (`git show --stat <sha>`), never from the report's own tally and never from a branch tip.
  **This arc has CC miscounting its own commits twice on the record.**
- **The read-only default held.** Per commit, the file list carries nothing under `src/`,
  no golden, nothing under `tools/corpus/` or `tools/robust_stop/`.
- **Push target.** `origin` only. A push toward `upstream` is a HARD STOP by the standing
  distribution constraint.
- **The guard set, re-run by Cowork rather than read from the report:**
  `tools/audit/register_lint.py`; `tools/open_items_split_check.py`;
  `tools/audit/index_status_lint.py --check`;
  `tools/audit/decisions/gen_decisions_register.py --check`;
  `tools/audit/decisions/gen_cluster_dispositions.py --verify` / `--check` / `--producible`;
  `tools/audit/decisions/reaim_home_anchors.py --check`.
- **Anchor drift after every insertion into `CLAUDE.md` / `ARCHITECTURE.md` /
  `OPEN_ITEMS.md`** — re-aimed per citation from the drift report, never by an assumed
  uniform shift.
- **D-253 in every dialect.** Cowork reads working-tree files with the file tools. Shell
  access is git object queries by explicit hash only — including in the sandbox, where the
  rule's own founding stale-mount hazard lives.

---

## 6. What Cowork still owes before the report arrives

Stated rather than left implicit, so the verification is not claimed to rest on more
reading than it does:

- The **thirteen earlier ruling records with their correction notes** — read whole when a
  claim touches their subject (D-643). Rulings 60–64 have been read whole; the earlier
  thirteen have not been re-read this session.
- **`cowork_away_returns.md` end to end** — the program's returns file.
- **`cowork_target_document_structure_2026_08_09.md`** — the orientation the completion
  statement opens with.
- The **detail files** of every row this batch touches, read before its flip is accepted.

---

## 7. What this file does not do

It authorizes nothing. It moves no row, no register entry, no home and no gate verdict. It
proposes no ruling and drafts no sentence of phase 1's completion statement. It is a
checklist Cowork holds against a report that does not yet exist, and it is superseded the
moment that report is verified.
