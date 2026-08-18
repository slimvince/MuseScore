# Verification plan — the preparation phase's TENTH batch

> **STATUS: PRE-REGISTERED EXPECTATIONS, written BEFORE the batch's report exists.** Drafted by
> the writing side (Cowork) on 2026-08-18 while `cc_instruction_preparation_tenth.md` was in
> flight and the writing side was READ-ONLY on the repository. It is on the precedent of
> `cowork_scratch_2026_08_11/cowork_verification_plan_continuation_14.md`, whose §3 the twelfth
> handover block records as the thing that turned two checks from opinions into tests:
> **pre-registration is the one thing git cannot reconstruct afterwards.**
>
> **This file is NOT in the repository and nothing here is executed by it.** It carries no
> ruling, edits nothing, and is not a dispatch. It lands in the tree only at a verified stop,
> and only if the user wants it landed. **No part of it is to be relayed to the executing side
> while the batch runs** — the standing no-mid-flight-steering rule (D-251) bars that
> absolutely, and §5 below is written for the RETURN SITTING and for nowhere else.

---

## 0. What this session did, and the departures it declares

This session booted in the remote Cowork environment. Its first act was the branch rule. It then
performed the twenty-eighth handover block's ordered read and the ruled session-start read, and
took the baseline measurements in §2 — all read-only, none of it touching the working tree.

**The branch rule, run twice.** At 06:40 UTC and again at 06:49 UTC the branch and the remote both
stood at `1760d9a4a8`, the ninth batch's terminus; no `cc_report_preparation_tenth.md` existed;
`cowork_away_returns.md` and `STATUS.md` carried modification times predating the twenty-eighth
close by roughly eight hours, so neither could carry a PREPARATION TENTH BATCH section or a tenth
batch's pointer entries. **Established: the batch had not yet written anything.** The user then
directed that this session do only work that does not interfere with it, so **this session treats
itself as READ-ONLY on the repository for its whole length**, whichever of the two remaining
states holds.

**What was read, stated so no reading is credited that was not done.**

- The twenty-eighth block's ordered read, items (1)–(9), in full: the ninth-return ruling record;
  `cc_instruction_preparation_tenth.md`; the session-start-read sitting record; the eighth-return
  record including its §6; the four sitting records of 2026-08-17 (seventh return with its §5
  correction, residue, callers, rulings sort); the sixth-return record, the governing-surface
  split record and `cowork_rulings_2026_08_16_preparation_return.md` §§1–7; the ninth batch's
  report in full and its FULL close (THE PREPARATION NINTH BATCH section of
  `cowork_away_returns.md`) in full; the twenty-eighth block; the twenty-seventh block.
- `cowork_handoff.md` **in full** — all 4,114 lines, every block down to the standing rules and
  the table of files at its foot.
- The ruled session-start read: `CLAUDE.md` **in full** (1,823 lines), `STATUS.md` **in full**,
  `DECISIONS.md` **in full** (858 lines), and the derived gating answer at
  `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`.
- `BUILD_AND_TEST.md` was **not** read. It is a CONDITIONAL read since the ninth batch's Task 3,
  and this session neither builds, tests, nor runs a measurement tool whose command lives there.
  **The condition is not met, so the read is not owed.**

**The declared environment departures.**

1. **The branch tip was read** (`git rev-parse`, `git log`) to establish that the tenth batch had
   not started. There is no close yet to supply an explicit hash, so no other route exists. This
   is the same departure the twenty-fifth, twenty-eighth and ninth-return records declared.
2. **Two untracked files were read through the device bridge** —
   `cc_instruction_preparation_tenth.md` and `cowork_rulings_2026_08_17_ninth_return.md` — because
   they are in no commit and therefore in no object. Everything else in §0 and §2 was taken by
   **git OBJECT read at the explicit hash `1760d9a4a8`**, which is the one sanctioned shell
   mechanism. **No working-tree file was read through a shell.**
3. **`git status` was NOT run** — the recorded index-refresh hazard on this mount, and the
   standing rule bars it. The working-tree state in §0 was established from file metadata
   (names, sizes, modification times) and from the absence of a named file, never from a shell
   read of any file's content.

**F57 is applied rather than assumed.** Every character count in §2 is stated with the read that
produced it named, so a later comparison can reproduce it or show that it cannot. Where a figure
in the record does not reproduce, §4 says so instead of adopting it.

---

## 1. What the batch is bound to do, restated only as far as the checks need

The dispatch is the authority for its own tasks and expectations and is not restated here (#6).
The seven acts the checks below attach to are: **Task 0a** landing three paths; **Task 0b** the two
recorded corrections of Ruling 2(a) and 2(b); **Task 1** Ruling 1's pinned kind extended to a class
with its membership derived; **Task 2** Ruling 3's narrowing of rule (a)'s pointer; **Task 3**
Ruling 2(c)'s read-first clause written at a derived home; **Task 4** the retirement caller census
re-pinned; **Task 5** the close, plus the one further commit the E-ordering rule requires.

---

## 2. The BEFORE values, measured at `1760d9a4a8` before the batch could move them

Every value here was read at the git object by explicit hash. They exist so the AFTER values are
compared against a measurement rather than against a memory.

### 2.a Blob identities of every file the batch may touch

| path | blob at `1760d9a4a8` |
|---|---|
| `CLAUDE.md` | `982b01d485` |
| `CLAUDE_ARCHIVE.md` | `ed5efeb399` |
| `STATUS.md` | `131bca636d` |
| `STATUS_ARCHIVE.md` | `35e72afd9d` |
| `DECISIONS.md` | `5a74c0bc4c` |
| `OPEN_ITEMS.md` | `6ae67d8603` |
| `cowork_handoff.md` | `5414ef4fdb` |
| `cowork_away_returns.md` | `2c9499aab4` |
| `tools/audit/nongating_apparatus_rows.json` | `5bb43d0b3a` |
| `tools/audit/guard_state.json` | `1decaaff8e` |
| `tools/audit/guard_classification.json` | `452c6a5b44` |
| `tools/audit/retirement_caller_check.json` | `ae7a9cf441` |
| `cowork_design_doc_template.md` | `518048459d` |
| `cowork_audit_protocol.md` | `4f22a4d6d1` |

**Use:** any file the close does not name as touched must still carry its blob above. A file that
moved without being named is a STOP-and-report at the sitting, not a discrepancy to reconcile.

### 2.b The open-items register's INDEX, for the no-row-moved proof

`OPEN_ITEMS.md` at `1760d9a4a8` carries **375 table rows** whose first cell opens with an
open-items identifier. **This reproduces the ninth-return record's own figure exactly** and is the
check to re-run after the batch: **375 before and 375 after, or a row was created or discarded.**

**A caveat that must travel with this figure, because it is the difference between a proof and an
assertion.** A naive pipe-split of the same rows yields **133** resolved-mark rows and **232**
open rows, with 10 rows it cannot split. The record's own figures are **136** and **241**. The
gap is the known naive-splitter defect the session-start-read sitting's §0 already names — about
six rows carry a pipe character inside a code span — and **the project's ONE index parser
(`tools/audit/index_status_lint.py`) is the authority, not this split.** So: the 375 total is a
usable proof and is used; **the resolved/open split must be re-derived at the parser at the
return and never at a hand split.**

### 2.c The derived gating answer, which Ruling 3 narrows the pointer to but does not touch

Read at `tools/audit/nongating_apparatus_rows.json` at `1760d9a4a8`:
**216 gating + 25 non-gating = 241 open rows**; `[[OI-179]]` present in the gating set with its
ground; `[[OI-372]]` and `[[OI-374]]` present.

**Use:** Ruling 3 changes a clause in `CLAUDE.md` and nothing in this artifact's answer. **If the
answer moves, something other than the pointer moved, and that is a STOP-and-report** — the more
so because Task 4 regenerates artifacts and Task 1 pins generators, either of which could reach
this file by accident.

### 2.d `CLAUDE_ARCHIVE.md` carries exactly ONE former rule-(a) wording

At `1760d9a4a8` the file carries a single block introduced *"From `CLAUDE.md`, the open-items
register section, rule (a), superseded 2026-08-17 by …"* — the wording the NINTH batch superseded.

**Use:** Task 2 supersedes the wording the ninth batch itself wrote, so after the batch the
companion must carry **TWO** rule-(a) blocks, **each byte-present exactly once**, and `CLAUDE.md`
must carry **a dated pointer at the site for each** and **neither superseded wording at site**.
Both directions, the second being the load-bearing one.

---

## 3. The checks, per task, each with what would falsify it

The registered expectations E0a, E0b and E1–E5 are the dispatch's and are not restated (#6). What
follows is what the WRITING side checks at the objects, over and above reading the report.

### 3.0 The chain, before anything else

Confirm each commit's parent at the object and each commit's path count to the digit, ending at
the E-ordering terminus the batch cannot name. Confirm branch and remote at the same commit.
**A path count that disagrees with the close is a STOP-and-report, whichever direction it runs.**

### 3.1 Task 0a — E0a

- **Exactly three paths**, not four. The ninth batch's Task 0a landed four; this dispatch says
  *"exactly these THREE paths and no fourth"*. **Four paths is a discrepancy, not a rounding.**
- One modification (`cowork_handoff.md`) whose content is the twenty-eighth block inserted plus
  the twenty-seventh heading's demotion marker, and two additions.
- A1's check must have been taken **blob against blob by explicit hash**, and the report must say
  so.

**★ The premise ledger's two measured FACTs are VERIFIED, not accepted.** The dispatch states that
`cowork_handoff.md` hashed equal to its committed blob at `1760d9a4a8` with content sha256
`f14f9944c9…` at 317,754 bytes, and that the file is stored with LF line endings and zero carriage
returns. Re-derived at that object this session: **317,754 bytes**, sha256
`f14f9944c95e27382980b56892aafe3493a9896e21186daa39a6b4a3ed4eba80`, **zero carriage returns.** All
three reproduce exactly. **So A1's F57 caveat does not arise for the one file A1 names, exactly as
the dispatch states, and this is now proven rather than asserted** — which also means that if
Task 0a's check reports that file as differing from its blob by its own line count, the check has
misread it and that is a STOP.

### 3.2 Task 0b — E0b

- Both correction sites carry a **dated correction note** with the **former number preserved beside it**.
- **The corrected text itself is not rewritten** at either site — the twenty-seventh block's own
  findings paragraph and the ninth close's §8 must be byte-identical to their committed form,
  with the corrections **appended**. This is the check the report is least likely to assert and
  the one #12 rests on.
- No finding's content, weight or population moves; F1–F59 remain fifty-nine findings.

### 3.3 Task 1 — E1, and this is where a STOP is most likely

- **The class rule stands verbatim** at `tools/audit/gen_guard_classification.py`.
- **The membership is DERIVED and published**, with each member's document, generator, ruling
  record and resolved commit named.
- **`gen_claude_md_finer_surface.py`'s existing pin is RECORDED, not re-taken** — its pinned value
  must still be `cfb69a7ecb` and its artifact byte-unchanged.
- **Each pinned generator carries, at its own site, the statement that the underlying data file is
  NOT pinned and continues to re-derive** — the clause that keeps this from reading as a second
  F22 ossification.
- **No document's committed content moves.** A member whose current rendering differs from its
  committed one must be **restored to its committed bytes and the difference reported**.

**★ The pre-registered expectation, and it is the sharpest one in this plan.** Assumption A3 says
every generated document put to the user for a ruling can have its ruling commit DERIVED from a
ruling record that names it, and orders a STOP on any member where it cannot.

Measured at the objects this session: **`cowork_rulings_2026_08_17_seventh_return.md` names a
commit (`cfb69a7ecb`). The residue sitting record, the rulings-sort sitting record and the
governing-surface split record each name their surface and the artifacts its populations bind at,
and NONE of the three names a commit.** The ninth-return record's own ground names exactly those
three as carrying the same exposure. Separately, the tree holds **27 files under
`ratification_surfaces/`**, of which a substantial share are generated and were put to the user
for a ruling.

**So the expectation is: either Task 1 STOPs on A3 for several members, or it derives their pin
commits by a route the dispatch does not name.** The second outcome is not a failure — a
derivation through the batch close that produced the surface is legitimate — but it is a
**departure that must be declared and checked at the objects**, because a pin is only worth
anything if the commit it names is the one the user actually ruled from. **A pin taken at a
branch tip, or at the commit that happens to carry the surface today rather than at the ruling,
is the defect this ruling exists against.**

### 3.4 Task 2 — E2

- Rule (a) names the **list of gating identities**, not the whole section; the grounds are
  reachable from the clause; **the #19 distinction stands at the site** in terms.
- The superseded wording is byte-present in `CLAUDE_ARCHIVE.md` **exactly once** and **absent from
  `CLAUDE.md`**, with a dated pointer at the site — both directions, per §2.d.
- Every re-aimed anchor verified at its new coordinate; `gen_cluster_dispositions.py --verify`
  is the drift authority and `reaim_home_anchors.py --check` is not (F3, eleven times surfaced).
- **No row created, flipped or discarded**; `[[OI-179]]` OPEN and GATES; §2.b's 375 unchanged;
  §2.c's answer unchanged.

**The arithmetic to check rather than the number to accept.** Ruling 3 predicts the session-start
read falls from 360,213 to *"approximately 294,000"*. The reduction attributable to Ruling 3
alone is **67,950 − 2,079 = 65,871 characters**, giving **294,342**. So the identity to check is:

> after = 360,213 − 65,871 ± (the `CLAUDE.md` clause delta)

and **any residual beyond a few hundred characters must be explained by the `CLAUDE.md` edit
itself** — the narrowed clause, the #19 distinction added, the superseded wording moved out, the
dated pointer left in. An after-figure that lands near 294,000 without that decomposition
published is a number that agrees rather than a number that was derived. See §4.1, which is why
this is stated as an identity and not as a target.

### 3.5 Task 3 — E3, and there is a finding to bring to the sitting

- The clause stands at a home **the record makes a home**, with the ground recorded and F58 named;
  or a STOP with the candidates read and the reason stated. No other authoring rule moves.

**★ The pre-registered expectation, and it is a writing-side finding about the dispatch itself.**
Task 3 orders the home DERIVED and names two candidates to read: `cowork_design_doc_template.md`
and `CLAUDE.md`'s Conventions section. **Measured at the objects this session, neither is the
record's home for dispatch-authoring rules, and a third document that the dispatch does not name
is.**

`cowork_audit_protocol.md` carries a section headed **"The dispatch protocol these audits are
commissioned and run under"**, and under it live, as their own subsections, the rules that govern
exactly this: *one side writes the instruction files and the other executes them* (D-252);
*dispatches are written only when they are next* (D-250); *a running dispatch is never interrupted
or steered mid-flight* (D-251); *a figure enters a dispatch or a report by citation to a generated
artifact* (D-431); *the writing side runs the standing self-check before a dispatch is released*
(D-434); *a claim that invokes a ruling as an application quotes that ruling in full* (D-643);
*a task that cannot be stopped partway is dispatched first* (D-670); and the publication and
stopping rules D-671 and D-672. `cowork_design_doc_template.md`, by contrast, carries the
document-structure standard, the two writing standards, the kind list, the filing convention and
the status-banner convention — **it is the home for how a document is WRITTEN, not for how a
dispatch is CONSTRUCTED.**

**So the three outcomes to expect, and how each is treated at the sitting.**

1. **CC STOPs**, on the letter of the instruction, having read the two named candidates and found
   neither is the home. E3 is met by its own second limb and CC has done nothing wrong — **but a
   cycle is spent and the clause does not land**, and the cause is the dispatch's candidate list.
2. **CC widens beyond the named candidates**, finds the dispatch-protocol section and writes the
   clause there. **This is the substantively right outcome** and is a departure to declare and
   check — the widening must be visible, not silent.
3. **CC writes the clause at `CLAUDE.md`'s Conventions.** Defensible — that section does carry
   cross-cutting rules binding both sides — but it separates one dispatch-authoring rule from the
   eight that already live together, which is the tension #6 exists over.

**This is a finding of the F58 family at one remove: a dispatch that names a candidate set which
omits the site. F58's own lesson was that a dispatch ordering a write into a document must also
order the read of it; the neighbouring lesson is that a dispatch ordering a DERIVATION must not
pre-narrow the candidate set the derivation is allowed to read.**

**It is deliberately NOT given a finding number here.** Ruling 2's allocation point is the
dispatch's read-first block naming the current handover block, and the tenth batch has already
read the twenty-eighth block; a number allocated now would be invisible to it and would reproduce
the F52 double-booking that Ruling 2 exists to prevent. **The number is allocated at the return
sitting, once CC's own allocations for this batch are known.** Recording the finding without a
number, and saying why, is the ruling working.

**And it is NOT relayed to the executing side.** No mid-flight steering (D-251).

### 3.6 Task 4 — E4

- The check PASSES at the new pin; every difference classed with **zero unclassed**; every
  set-aside naming stays published; any verdict flip is enumerated and confers candidacy only.
- The KIND-UNDERIVABLE population returns as published data. **It stood at ONE at the ninth
  batch's re-pin.**

**Pre-registered expectations.**

- **The read-regime class places NOTHING again.** Task 2 narrows which PART of an artifact rule (a)
  points at; it neither adds nor removes a named file. The ninth batch's own finding was that this
  class held for no movement because the files the read regime re-classes are governing documents
  rather than retirement candidates, and that reasoning applies unchanged. **An empty class must
  still be published as a MEASUREMENT** — the ninth batch's own pattern.
- **A new naming of `cowork_handoff.md` appears, from Task 3's clause.** The clause says every
  dispatch's read-first block names the current handover block, and the callers sitting ruled that
  a mandatory-read or boot listing HOLDS a candidate. Whether this naming is of that kind is for
  the derivation to place — **and a caller whose kind the derivation cannot place STOPS to the
  user and is never guessed.**

### 3.7 Task 5 and the end state — E5

- One `STATUS.md` pointer entry per task, and **in the same act the NINTH batch's entries move
  verbatim to `STATUS_ARCHIVE.md`, both directions proven.** After the batch, `STATUS.md` must
  carry the TENTH batch's entries **alone**.
- The full close appended as a PREPARATION TENTH BATCH section, with both guard states, every
  SHA, every expectation graded MET or NOT MET **with its reason**, and every declared departure.
- **The end-state guard run is taken AFTER the Task 5 commit exists** and lands in one further
  commit. A batch-level summary sentence written in the same commit as the work it summarizes is
  the same defect at a smaller grain, and the ninth batch declared its instance rather than hide
  it; the same is expected here.

**Pre-registered expectation for the end state: 69 run, 68 passing, ONE failing
(`gen_filing_convention_application.py --check`, `[[OI-372]]`), 4 not run, 16 historical, zero
STOPs** — the ninth batch's proven end state, which is also this dispatch's declared start state.
**The one thing that could lawfully move it is Task 1**: pinning further generators may add check
invocations, in which case the run count rises and the new-tool rule's discharge must be visible
in the same commit. **A run count that moves with no such cause named is a STOP-and-report.**

### 3.8 The proofs the writing side takes that the report is not expected to assert

Two per return has been the pattern; four are registered here.

1. **The open-items register's bijection.** `OPEN_ITEMS.md` carries **375** table rows before and after
   (§2.b), and the resolved/open split re-derived **at the index parser**, not at a hand split.
2. **Ruling 4's forward bound working rather than asserted.** `STATUS.md` carries the tenth
   batch's entries alone; the ninth's are byte-present in `STATUS_ARCHIVE.md` exactly once.
3. **The gating answer is unmoved** (§2.c) — 216 + 25 = 241, `[[OI-179]]` present with its ground.
   Ruling 3 moved a pointer; if it moved an answer, that is the failure the ruling's own #19
   paragraph exists to make visible.
4. **Every untouched file still carries its blob** from §2.a.

---

## 4. Two things that do not reproduce, recorded now rather than discovered later

### 4.1 Ruling 3's three character figures are not reproducible from the artifact by a raw read

The ninth-return record's §3 states, *"taken at `tools/audit/nongating_apparatus_rows.json` at the
terminus `1760d9a4a8`"*: the section rule (a) names is **67,950** characters; the list of gating
identities is **2,079**; the same 216 rows carrying each one's recorded ground is **56,388**; the
frozen comparison is **3,893**.

**Measured independently this session at that same object**, the corresponding spans are
**74,859**, **2,749**, **60,278** and **4,795**. Every one of the four is larger than the recorded
figure, and the ratios differ between them, so no single formatting or line-ending adjustment
reconciles them. **The record does not state the normalisation its measurement used.**

**Why this matters and is not bookkeeping.** Task 2's step 6 orders the session-start read's
character total published *"before and after, each value read from the files at explicit objects
and not estimated"*. If the batch measures under a different normalisation than the ruling did,
its before-and-after pair will be internally consistent and **not comparable to the 360,213 and
the ≈294,000 the ruling predicts** — and the arc's headline reduction would then rest on two
measurements taken under two unstated conventions. **The remedy is one clause: a published
character figure names the normalisation it was taken under.** This is the D-431 family — a
figure enters by citation to a generated artifact, and a figure nobody can re-derive is a figure
that has stopped being a citation.

**What is NOT claimed:** that either measurement is wrong. Both may be right under their own
reading. What is established is that they cannot be compared without a statement neither carries.

> **★ CORRECTION, appended 2026-08-18 at the tenth batch's return sitting, before this file landed
> in the tree. The corrected wording stands above rather than being deleted (#12).**
>
> **(a) The finding is CONFIRMED and its cause is now closed at the arithmetic.** The tenth batch
> built `tools/audit/gen_session_start_read_size.py` and measures the section at **74,858**
> characters and the identity list at **2,748** — within one character of the two figures measured
> above, the difference being that this file took an index difference where the tool takes a span.
> **An independently built generator reproduces this file's figures and not the record's.** The
> record's total of 360,213 is short by **exactly 6,908**, which is exactly 74,858 − 67,950; every
> other member of the read agrees to the digit. Ruling 3 of the tenth-return sitting corrects the
> record at both sites and withdraws the derived percentage rather than recomputing it by hand.
>
> **(b) ONE FIGURE-CONVENTION ERROR IN THIS FILE IS OWNED AND CORRECTED.** The per-file sizes this
> plan quotes elsewhere — 154,486 for `CLAUDE.md`, 12,365 for `STATUS.md`, 128,528 for
> `DECISIONS.md` — are **BYTE** counts, taken with a byte-counting read. **This project measures
> CHARACTERS**, and the same files measure 153,246, 12,243 and 126,774 in characters; the
> difference is the multi-byte characters the record's own prose is full of. **The section
> measurements in §4.1 are unaffected** — both sides took those in characters and they agree to one
> character — but the per-file figures above should be read as byte counts, and this file should
> have said so when it stated them. **The general form is Ruling 3's standing clause: a published
> character figure names the tool that produced it.**

### 4.2 The three ruling records that name no commit

Recorded at §3.3 and repeated here so it is not read as part of Task 1's checks alone: of the four
generated ratification documents the ninth-return record's own ground names as carrying the
unpinned exposure, **exactly one has its ruling commit written into a ruling record.** The other
three name their surface and their populations' artifacts and no commit. A3's STOP is therefore a
live prospect rather than a formality.

---

## 5. What is put to the user at the return sitting, and in what order

Written for the sitting, not for the batch. Nothing here is a recommendation yet — the
recommendations are drafted once the return is verified at the objects, in the ruled form, with
each alternative rated TOWARDS the ultimate objective and TOWARDS the guiding principles.

1. **Whatever the batch STOPs on**, Task 1's A3 first (§3.3).
2. **The Task 3 home question** (§3.5) — either as a ruling on where the clause lands, if CC
   STOPped, or as a ratification of the widening it declared.
3. **The unstated-normalisation finding** (§4.1), which bears on how the arc's own headline
   reduction is stated.
4. **The one remaining caller whose kind the derivation cannot place**, published as data.
5. The standing queue, unchanged: the curated boot list drafted for ruling **at its own ruled
   definition**; the empirical findings ledger behind its fact-gate; the archiving wave read at
   the REGENERATED census; the mining and landing of the 284 newly visible instruction files.

---

*Provenance: Cowork, 2026-08-18, written in the remote Cowork environment while
`cc_instruction_preparation_tenth.md` was in flight and the writing side was read-only on the
repository. Every figure in §2 and §4 was read at the git object `1760d9a4a8` by explicit hash,
except the two untracked files named in §0, which were read through the device bridge because they
are in no commit. `git status` was not run. This file is outside the repository and lands in the
tree only at a verified stop, on the user's direction — the standing pattern that the writing side
drafts outside the tree and lands at stops.*
