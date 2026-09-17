# CC dispatch — phase 1r: commit the delegations, re-aim, re-classify

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork).** Read IN FULL before touching anything it
> owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1r_commit_and_reclassify.md`.
>
> **★ THIS DISPATCH ASSERTS NO FIGURES** (D-431). Quantities are named as an artifact and a field, or
> as a generated report.
>
> **★ THERE ARE UNCOMMITTED EDITS IN THE WORKING TREE, MADE BY COWORK ON THE USER'S DIRECTION.**
> Task 1 commits them. **Do not rewrite, reformat or "improve" any of them** — the wordings are the
> user's write-list act (OI-293), and editing them would be an assistant revising a delegation, which
> rule (g) forbids. If one looks wrong, report it; do not fix it.
>
> **★ `cc_instruction_phase1o_gate_partition_and_probe_rerun.md` is queued BEHIND this wave.** Not
> part of it.
>
> **★ THIS WAVE READS NO OI-207 DOCUMENTS.** Reads resume as dedicated waves.

## 0. Standing constraints

1. **Every amendment lands in the PROPER LAYER** (#7).
2. **NO inference-problem fixing.** Phase 1 under D-231. No `src/` change, no golden refresh, no
   `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change, no fix, no design.
3. **Never use the shell to read working-tree files**, `git status` included. The shell-read guard is
   now ARMED for your side (Task 4 records it) — if it denies a command, that is the rule, not a
   fault; use the file tools.
4. **Never work from memory.** For a claim about the code, the code is primary; a row or a register
   entry is secondary (D-431's premise clause).
5. **A surprise is a STOP** (#13).
6. Bare words carry the musical meaning. Bash: append `; echo "exit:$?"`; no large single outputs.

## 1. Task 1 — Commit the write-list delegations

Seven edits sit uncommitted in the working tree, made by Cowork on the user's direction of
2026-08-03 executing the OI-293 write list. Uncommitted, they are the OI-285 class exactly — a change
on disk and not in the record.

The edits, by location, each carrying its own provenance sentence in the text:

- `ARCHITECTURE.md`, the Layer-5 function section — a delegation pointer for
  `cowork_layer5_function_design.md`;
- `ARCHITECTURE.md`, the joint-estimator block — a delegation pointer for `cowork_prefit_gates.md`;
- `ARCHITECTURE.md`, the voice-leading-span criterion — named sections widened;
- `ARCHITECTURE.md`, the notation output-surface record — contract sections widened;
- `CLAUDE.md`, after the provenance paragraph of the guiding principles — a delegation pointer for
  `cowork_engage_arc_plan.md`;
- `CLAUDE.md`, decisions-register rule (h) — **the granularity clause** (the user's ruling of
  2026-08-03, option 1C);
- `cowork_engage_arc_plan.md`, arc #10 — a delegation for `cowork_joint_key_chord_design.md`.

**Verify before committing, and report:** that each edit is present and reads as described, and that
no other working-tree file was touched. If anything else is modified, **STOP and report** — Cowork
made these seven and no others.

## 2. Task 2 — D-430's verbatim, and the granularity clause

The granularity clause is a **scope clarification of D-430**, ruled by the user 2026-08-03, not a new
decision — so it does not get a sibling entry competing with D-430 for the same subject (#6).

- Re-take **D-430**'s verbatim from the corrected `CLAUDE.md` rule (h) text.
- Record the clarification in the entry with its date and ratifier, and **preserve the former
  verbatim in provenance** (#12).
- If, on reading the corrected text, you judge the clause is a separate decision rather than a scope
  clarification, **say so and give your reason** rather than deciding silently — that judgment is
  reportable either way.

## 3. Task 3 — Re-aim the drifted anchors

The two insertions moved line anchors in `CLAUDE.md`, `ARCHITECTURE.md` and
`cowork_engage_arc_plan.md`. The count is in the `--verify` drift report; every verbatim was intact
when Cowork ran it (quotes all found at their cited home), so **nothing was damaged — only line
numbers moved.**

```
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/ver_1r.txt 2>&1; echo "exit:$?"
```

**Re-aim each citation individually from the drift report's own line numbers. An assumed uniform
shift is forbidden** — three prior waves re-aimed theirs one by one for this reason, and the
insertions here are at three different depths in two files, so no single offset is correct anywhere.

## 4. Task 4 — Re-run the re-classification

The six write-list documents now carry delegations the bar admits, or name the sections they were
missing. **Re-run `gen_home_classification.py`** and report the movement.

Expected direction, registered as a prediction before the run (#17b): the entries in those six
documents move `gap` → `contract-home`, in whole or in part — in part for the two whose delegation was
already admitted and whose **named sections** were widened, since the rule-stating half is still
judged per section. **A document that does NOT move is a #13 STOP** — it would mean a delegation
Cowork wrote does not do what it was written to do, and that must be reported rather than patched.

Preserve the former class on every entry (#12).

**Then flip the rows:** OI-293 (the write list — delivered, with any case that did not move stated),
and OI-291 (the re-classification and its write-list half both now complete, or the remainder named).

## 5. Task 5 — Record the armed guard and its coverage limit

`guard_armed_check.py` now passes: the hook is declared in `.claude/settings.json`. Record it on
OI-292's arming item — **and record the coverage limit rather than closing clean**:

- the matcher names the CC-side shell tools, so **the guard covers CC's side and not Cowork's**,
  whose shell tool carries a different name and does not match;
- the check verifies the hook is **declared**, not that it **fired**;
- the configuration lives in a gitignored file, which is why the control is in the record as the
  check rather than as the settings.

**Do not describe the file-tools rule as enforced.** It is enforced on one side. That asymmetry is the
honest state and the row must say so (#19 — a control believed to be in place and not in place is
worse than none).

## 6. Task 6 — One maintenance act on the process check

`process_check.py` missed the phase-1q dispatch's "four local patches" because the quantity was
**spelled out** rather than written as a digit. Extend the pattern to English number words.

This is **closing a class, not tuning to a specimen** — the distinction the establishment artifact
draws — so it is legitimate maintenance on a kept mechanism (D-436). **Re-establish afterwards:**
re-run `--establish` and report the new detection and false-positive figures from the artifact. If
the false-positive rate rises materially, **revert the change and report** — a check that cries wolf
gets disabled, which is worse than one with a known blind spot.

## 7. Task 7 — Guards, notes, close

Run every guard at the committed tree; read each output separately:

```
cd C:\s\MS && python tools/audit/decisions/gen_decisions_register.py --check > /tmp/reg_1r.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/ver_1r_final.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/open_items_split_check.py > /tmp/split_1r.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/decisions/gen_section_homes.py --check > /tmp/sec_1r.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/local_patches_check.py > /tmp/lp_1r.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/guard_armed_check.py > /tmp/ga_1r.txt 2>&1; echo "exit:$?"
```

Run `tools/audit/process_check.py` over **this dispatch** and report what it finds against Cowork.

**One commit, or as few as the same-commit rule allows (D-230):** the delegations, D-430's re-taken
verbatim, the re-aimed anchors, the re-classification and the row flips belong together — the rulings
land in the commit that records them. Commits by git plumbing; guards run explicitly at the committed
tree because plumbing bypasses hooks. Report the SHAs.

`STATUS.md` gains one POINTER entry naming the write list as delivered, the re-classification's
movement, and the guard's one-sided coverage.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's own remedy, OI-274's body-tense
half, OI-287, OI-288, OI-289, OI-290's document-side remedy, the owed reads, and the queued phase-1o
dispatch.

## 8. Accepted outcomes

Tasks 1–5 and 7 are bounded and expected complete. **A write-list document failing to move at Task 4
is a STOP and a success of the check** — it means a delegation does not do what it was written to do,
and Cowork wrote it, so it is Cowork's to fix, not yours. **Task 6 reverting is an acceptable
outcome** if the false-positive rate rises.

## 9. Self-check (D-434) — run by Cowork on this dispatch before release

- **Principles.** #12 — every former verbatim and class preserved. #13 — Task 4's non-movement case
  is a STOP, not a patch. #19 — Task 5 refuses to describe a one-sided control as enforced; Task 6
  re-establishes after changing a kept mechanism. #6 — the granularity clause clarifies D-430 rather
  than opening a rival entry. #7 — each edit sits in the surface that owns its concern.
- **Conventions.** No self-invented labels. Bare words carry the musical meaning.
- **Figures and premises (D-431).** No bare quantity: the drift count is named as the `--verify`
  report, the establishment figures as the artifact. The premise that the seven edits exist and touch
  nothing else is stated as a thing to **verify**, not as a fact.
- **File-tools rule.** Named in §0 with `git status` called out, and the guard is now armed on CC's
  side.
- **Uncertainty (#24).** No comparison between measured quantities is asserted.
- **Consistency between rulings.** Checked across Tasks 1–6: Task 2's clarification is what makes
  Task 4's expected movement correct; Task 5's coverage limit is why Task 6's maintenance still
  matters on Cowork's side, where no guard runs.
