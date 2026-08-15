# CC dispatch — phase 1x: make the guards visible, establish the true state, then commit

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date (thirteenth set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1x_guard_visibility_and_commit.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).**
>
> **★ ORDER IS THE RULING.** Task 1 makes guard failures visible; Task 2 establishes what is actually
> failing; Task 3 commits. **Do not commit before Task 2 has run** — the point of the sequence is that
> the commit records a state that has been established rather than one that was reported by a channel
> known to truncate.
>
> **★ PHASE 1w's WORK IS ON DISK AND UNCOMMITTED.** Task 3 commits it together with this wave's.
> **Do not rewrite any of it.**
>
> **★ QUEUE.** `cc_instruction_phase1t_restatement_and_pruning.md` (stage 1) has still not run and
> remains queued; this wave does not supersede it.
>
> **★ NO `src/` CHANGE, no goldens, no `tools/corpus/`, no `tools/robust_stop/`, no behaviour change,
> no fix to the analysis, no design.** Phase 1 under D-231. Task 4 is documentation truth, not a
> behaviour change — read its own limit clause before acting.

## 0. THE PREMISE LEDGER (#17a)

**FACT — established at the object by Cowork in the session that wrote this dispatch:**

- **F1.** `gen_home_classification.py --check` **exits 1 at HEAD**: four `home_section` fields do not
  re-derive (D-321, D-322, D-323, D-324, all homed in `docs/scoring_model.md`),
  `phase1q_reclassification.json` does not re-derive, and one write-list document still holds a `gap`
  entry. Run by Cowork this session.
- **F2.** That tool's output contains characters outside `cp1252` — its diff lines use a Unicode
  minus. Observed in the run output.
- **F3.** `batch_analyze.cpp:4917` initialises the joint artifact directory empty, and the joint path
  runs only `if (!jointInferenceDir.empty())` at `:5590`. **The flag is opt-in.**
- **F4.** `BUILD_AND_TEST.md:24` documents the invocation as `batch_analyze.exe "<score>" --preset
  Jazz` — **without the flag**.
- **F5.** The OI-302 class: entries about the dormant pipeline that a live specification restates as
  standing do-not-retry prohibitions, at `ARCHITECTURE.md:1420` with the same construction at `:1344`
  and `:306`; `docs/redesign_plan.md:4` states the distinction in its own words —
  `open_items/OI-302.md:19-27`.

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That phase 1w's work is uncommitted, and that nothing else is. From a session report.
  → **Task 3.1**, via `tools/audit/changed_paths.py`.
- **A2.** That one encoding fix covers both OI-297 (the process check) and OI-305 (the classification
  check). Cowork inferred this from the symptom; it is not established. → **Task 1.1**.
- **A3.** That gate block (C)'s corpus commands omitting the flag is **correct**, because those are
  legacy-path diagnostics. **This is Cowork's judgment, not a read fact.** → **Task 4.2**.

## 1. Task 1 — Make guard failures visible

**1.1 Check A2.** Establish whether OI-297's and OI-305's crashes share one cause. If they do, fix it
once. If they do not, fix each and say so — the shared-cause claim is Cowork's inference and must not
become a reason to fix only one.

**1.2 The fix.** A guard must be able to report its findings on the console it is run on. Fix the
encoding path so a non-`cp1252` character cannot truncate the findings list or replace it with a
traceback. **The artifact is already written first in both tools, so no recorded figure is at risk
— what is at risk is the reader.**

**1.3 Establish it.** Verify the fixed tools emit their complete findings, and that a non-zero exit
still means what it meant. **A guard that now prints but no longer fails is worse than one that fails
invisibly** — check both halves.

## 2. Task 2 — Establish the true guard state

Run **every** guard, with the visibility fix in place. **Derive the list from what exists**, not from
any dispatch — the phase-1r wave named a guard deleted two waves earlier and nobody noticed.

Report, per guard: pass or fail, and for each failure its complete findings. **This is the first run
in this arc whose output can be trusted to be complete**, so state plainly whether anything is failing
that no previous wave reported.

**Do not fix what this task finds.** F1's STALE fields and the write-list gap entry are reported here
and dispositioned later; fixing them now would be acting before the extent is known.

## 3. Task 3 — Commit

**3.1 Check A1** through `tools/audit/changed_paths.py`: what is uncommitted, and is any of it
outside phase 1w and this wave? If anything else is modified, **STOP and report**.

**3.2 Commit** phase 1w's work and this wave's together.

**3.3 Record the guard state honestly in `STATUS.md`**, using the pattern already in use for the
armed-guard check: a **known-failing guard, named, pointed at OI-305**, with its findings cited to
Task 2's output rather than transcribed. The classification check's failure is **pre-existing** —
verified as such — so the entry says which wave introduced it if that is establishable, and says "not
established" if it is not.

## 4. Task 4 — Correct the command references (documentation truth only)

### 4.1 The defect

F3 and F4 together: the authoritative command reference, a mandated session-start read, documents an
invocation that runs the **dormant** pipeline. A session following it measures the wrong system.

Correct `BUILD_AND_TEST.md` to state the flag, and to state when it may be omitted.

### 4.2 Check A3, and audit every other site

Gate block (C)'s corpus commands also omit the flag. **Cowork judged that correct** — those are the
retired batch diagnostic, a legacy-path measurement — **but that is a judgment, not a read fact.**
Check it at the block's own text and report.

Then audit **every** command reference in the record for the same omission, and **judge each site
rather than sweeping**: a legacy diagnostic that omits the flag may be right; a production-surface
command that omits it is not.

### 4.3 The limit — read this before acting

**Do NOT change the flag's default.** That is a behaviour change and D-231 forbids one in phase 1. Row
it against phase 3, stating the case for it and that it was deliberately not taken here.

## 5. Task 5 — The reverse pointer for the OI-302 class (F5)

The prohibition is published once, in the specification (#6); what is missing is the reverse
direction. For each entry in the class, add the pointer **from the entry to the live section that
restates it as binding**, so a reader meeting the mark is one hop from the rule that still constrains
them.

**Do not add a register field** and **do not re-word the marker** — the first would be a second copy
of a live rule, the second would be a third revision of a marker weakened one wave ago.

**D-055 stays reported and uncorrected.** It turns on a scoping judgment rather than a code fact, and
that is the user's.

## 6. Task 6 — Close

Run the guards again at the committed tree and read each output separately. Run
`tools/audit/process_check.py` over **this dispatch** and report what it finds against Cowork.

`STATUS.md` gains one POINTER entry.

**Report, do not resolve:** the divergence between `gen_home_classification.py`'s expectation that a
write-list document holds no `gap` entry and the user's ruling that deliberately excluded
`cowork_voiceleading_axis_design.md` §15/§16 as ratification asks. **One of the two is wrong and it is
the user's to say which** — it is a question about what a write-list document may look like, not a
bug.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's remedy, OI-274's body-tense half,
OI-288 half (a), OI-290's document-side remedy, OI-296's sweep, OI-299, OI-300, OI-301, OI-305's
STALE findings (reported here, dispositioned later), OI-306, the `CLAUDE.md` mechanism-coverage
measurement, the owed reads, and the queued phase-1t dispatch.

## 7. Accepted outcomes

**Task 2 finding failures no previous wave reported is the expected outcome** — it is why the
visibility fix precedes it, and reporting them is the deliverable. **A2 coming back refuted is a
result**, and fixing both separately is then correct. **A3 coming back refuted means more command
sites need correcting than Cowork thought**, which is also a result.

## 8. Self-check (D-434) — run by Cowork before release

- **#17(a).** Five facts, each established at the object — F1 by running the tool, F3 and F4 by
  reading the code and the command file. Three assumptions, all checked before the acts resting on
  them, and two of them (A2, A3) are explicitly Cowork's own inference or judgment rather than
  anything read.
- **Sequencing.** Visibility, then establishment, then the commit — facts before action, applied to
  our own instruments. Task 2 explicitly forbids fixing what it finds.
- **Principles.** #19 — a control that cannot report is not established, and Task 1.3 checks the fix
  did not disable the failure. #12 — nothing deleted; D-055 reported not corrected. #6 — Task 5 adds
  a pointer rather than a copy. #13 — two STOPs. D-231 — Task 4.3 names the behaviour change it
  refuses to make.
- **D-431.** No bare quantity; F1's failures are enumerated by identifier rather than counted.
