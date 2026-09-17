# CC dispatch — phase 1q: the one re-classification pass, the write list, and three guards

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date (eighth set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1q_reclassification_and_guards.md`.
>
> **★ THIS DISPATCH ASSERTS NO FIGURES** (D-431). Quantities are named as an artifact and a field, or
> a document and a line.
>
> **★ `cc_instruction_phase1o_gate_partition_and_probe_rerun.md` REMAINS HELD.** Not part of this
> wave; not background.
>
> **★ RUN `tools/audit/process_check.py` OVER THIS FILE** as part of Task 6 and report what it finds,
> including against Cowork.

## 0. Standing constraints

1. **Every amendment lands in the PROPER LAYER** (#7).
2. **NO inference-problem fixing.** No fix, no design, no behavior change, no `src/` edit, no golden
   refresh, no `tools/corpus/` or `tools/robust_stop/` movement. Building a check is tooling.
3. **Never use the shell to read working-tree files** — file tools for content, existence, counts and
   searches; shell only for read-only git object queries by explicit hash and for the scripts named
   here. **This includes `git status`** — the phase-1p self-check recorded that exact slip.
4. **Never work from memory.** For a claim about the code, the code is primary; a register entry or a
   row is secondary (D-431's premise clause).
5. **A surprise is a STOP** (#13).
6. Bare words carry the musical meaning. Bash: append `; echo "exit:$?"`; no large single outputs.

## 1. The rulings this dispatch carries

| # | Subject | Ruling |
|---|---|---|
| X1 | OI-291, the home classification | **ONE re-classification pass, applied**, with a **write list** for the homes the record means to keep (option A3) |
| X2 | The W4-versus-bar collision | **Draft a proper delegation** rather than an exception; the delegating role and the home role are different tests (option B3) |
| X3 | The mechanism-keeping criterion | **Cowork's prose-retirement test is WITHDRAWN** and replaced by a measured one (option C2) |
| X4 | The shell-read guard | **Arm it, and put a CHECK in the record that verifies it is armed** (option D3) |
| X5 | The local patches | **Build the presence check**, with a declared retirement path (option E1) |

### 1.1 One refinement of X1, stated rather than slipped in

Cowork's recommendation said the pass should "run as a measurement first." Taken literally that
produces a **fourth measured-but-unapplied criterion**, which is the precise defect OI-291 exists to
record. So the reading applied here: **the measurement and the application happen in the SAME wave** —
measure, report the full movement, then apply it, with the former class preserved for every entry
(#12) so any part of it is reversible on the user's word. Nothing is left measured-and-unapplied.

## 2. Task 1 — The one re-classification pass (X1)

### 2.1 Apply every ratified criterion at once

Over the **whole** home population, not a staged subset. The criteria in force, each cited to its
register entry: the fifth home case (OI-268's ruling), the section-level unit (**D-430**), and the
delegation bar (**D-432**). The document-kind test and the delegation-specificity criterion are
**superseded** — phase 1n recorded them as steps toward D-430, not as rival tests; do not apply them
as if they still stand.

Generate the pass; do not hand-classify. For every entry: the former class, the new class, the
criterion that decided it, and the delegating line quoted from its file. The former class is
preserved in provenance (#12).

### 2.2 Produce the WRITE LIST

Where the outcome removes a home the record plainly means to keep, emit the case to a write list
rather than loosening the test. The two the user's surface named are `cowork_prefit_gates.md` (four
ratified protocols, delegated only by a citation list and a ratification attribution) and
`cowork_layer5_function_design.md` (a SIGNED layer specification delegated only by *"Full spec:"*);
enumerate any others the pass finds on the same footing.

For each: the entries affected, the current delegating line with its file and line, and a **DRAFT
delegation wording** in the form the bar admits.

**Do NOT write any delegation into `ARCHITECTURE.md` or `CLAUDE.md`.** Rule (g)'s guard is that only
the user writes a delegation, and the user has ratified the *approach*, not any wording. The drafts
come back for ratification.

### 2.3 Flip OI-291

With provenance naming the user's 2026-08-03 ruling, the option taken, and the write list as the
outstanding half. The detail file gains a dated note and never a status.

## 3. Task 2 — The W4 collision and the two roles (X2)

**The collision.** `CLAUDE.md:128-130` names `cowork_engage_arc_plan.md` for a stated concern (the
measure-before-build gate) inside a list of citations. W4's test passes; the bar excludes. **The bar
governs** — a mechanical test with a case-by-case exception is not a mechanical test, and W4's
admission is therefore **not applied**. Record W4 as superseded by D-432 on this point, with the
reason, rather than silently dropping it.

The remedy is a **drafted delegation** on the write list, exactly as §2.2 — the arc plan holds a
shelving with evidence and an entry load-bearing for the retirement map, so it is a case the record
means to keep.

**And write down the role distinction**, because it will be asked again. Delegating *from* a document
requires that document to be user-ratified. Being delegated *to* requires that someone delegated to
it. These are different tests with different subjects, and a document may satisfy one without the
other — so `cowork_engage_arc_plan.md` being a source of delegations does not make it a home. Home it
beside the criterion in `CLAUDE.md`'s decisions-register section, with a register entry.

## 4. Task 3 — Replace the mechanism-keeping criterion (X3)

**Record the withdrawal, with its reason.** Cowork's ratified test — *a mechanism must retire the
prose it replaces, or it is apparatus growth* — is withdrawn by the user 2026-08-03 because it is a
**structural proxy standing in for a behavioral quantity, unvalidated** (#17d): what matters is
whether the running burden or the failure rate falls, and prose retirement measures neither. A rule
may need stating for a human reader *and* be enforced by a machine; that is not the duplication #6
forbids, as the register itself demonstrates.

**The replacement, which is the test from here:** a mechanism is kept when it **runs automatically
with no human step**, has a **measured detection rate against known instances**, and has a **measured
false-positive rate at or near zero**. All three are measurable; none is judged.

Home it beside **D-431** and **D-434** in `cowork_audit_protocol.md`'s dispatch-protocol section, with
a register entry. `process_check.py` and `shell_read_guard.py` are **kept** under it; cite their
establishment artifacts rather than restating their figures.

## 5. Task 4 — The armed-guard check (X4)

Build a check, run beside the other guards, that verifies the shell-read guard is **installed and
active** in the local harness configuration.

**The design point that makes this worth building:** the machine-specific settings file stays
untracked, and the *control* enters the record as the check. That is what answers the OI-285
objection CC correctly raised — a live control existing only in an untracked file — without tracking
session state or hard-coding a machine-specific path into the repository.

**Expected state at delivery: FAILING.** Arming is the user's act on the user's machine, so until it
is done this guard reports NOT ARMED and exits non-zero. **Record that in `STATUS.md` as the one
expected-failing guard, with the owed action and the arming block**, so a later session does not read
it as a regression. Print the arming block, verbatim, in the check's own failure output — CC already
wrote it into the tool's docstring; do not retype it, read it from there.

`OI-292` records the arming as owed until it is done.

## 6. Task 5 — The local-patches presence check (X5)

`CLAUDE.md`'s "Local patches — do not revert" section carries four edits to code this project does not
own, each stated as do-not-revert against a dependency update. **Nothing verifies they are present**,
and a silent revert produces no failure and no signal. One of them changes the analysis input on the
zero-signature stems, so this is the only mechanism in the current set that guards the system rather
than the paperwork.

Build a check that verifies each patch is present at HEAD. Derive the patch list from `CLAUDE.md`'s
own section rather than hard-coding it, so a fifth patch recorded there is covered without a code
change (#17f applied to the check's own input).

**The retirement path is mandatory, not optional.** A patch that upstream later fixes must have a
declared way to be retired, or the check fails forever and gets disabled — which is worse than not
having it. Specify how a patch is marked superseded, and require that marking to carry the upstream
commit or release that supersedes it.

Establish it (#19): verify it **detects a deliberately absent patch** as well as passing on the
present ones. A check that only ever passes is not established.

## 7. Task 6 — Guards, the process check on this file, notes, close

Run every guard at the committed tree, including this wave's additions. Read each output separately.

Run `tools/audit/process_check.py` over **this dispatch** and report what it finds against Cowork —
that is the point of building it, not an embarrassment to soften.

`STATUS.md` gains one POINTER entry, naming the re-classification's scale, the write list as
outstanding, and the expected-failing guard with its owed action.

Commits by git plumbing; guards run explicitly at the committed tree.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's own remedy, OI-274's body-tense
half, OI-287, OI-288, OI-289, the 66 owed reads, the write list's ratification, the arming act, and
the held phase-1o dispatch.

## 8. Accepted outcomes

Tasks 1–6 are bounded and expected complete. **Task 4 delivering a failing guard is the expected
outcome**, not a defect. **Task 5's establishment failing to detect an absent patch is a STOP** — an
unestablished check on a live exposure is worse than none (#19). **The re-classification moving more
than expected is not a reason to narrow it**; enumerate it and report.

## 9. Self-check (D-434) — run by Cowork on this dispatch before release

- **Principles.** #12 — every former class preserved, no wording deleted. #13 — the W4 collision is
  resolved by ruling, not by building around it. #17(d) — the withdrawn criterion is named as the
  unvalidated proxy it was. #19 — both new checks carry an establishment step, and Task 5's is a STOP
  condition. #7 — each ruling homed at the surface that owns it.
- **Conventions.** No self-invented labels; the two roles in Task 2 are described in plain words. Bare
  words carry the musical meaning.
- **Figures and premises (D-431).** No bare quantity; every one named as an artifact field or a
  document and line. The one premise this dispatch rests on — that the delegation bar excludes
  documents currently admitted — is cited to `phase1p_delegation_bar.json` → `pre_apply_check`, read
  this session, not carried from a report.
- **File-tools rule.** Task 0 constraint 3 now names `git status` explicitly, after the phase-1p slip.
- **Uncertainty (#24).** This dispatch asserts no comparison between measured quantities.
- **Consistency between rulings.** Checked across X1–X5 before release, after the phase-1p surface
  shipped two recommendations that contradicted each other: X2's drafted delegation is X1's write list
  applied to its first case; X3's replacement criterion admits X4 and X5; nothing here contradicts
  anything else here.
