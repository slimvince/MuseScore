# The sitting's landing — the record and this sitting's products committed (dispatch, 2026-09-01)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side, executing the landing that
> **D-230** provides for: the ruling record is an interim carrier and lands in git at a later dispatch's
> Task 0. **This is that dispatch, and landing is its whole purpose rather than a step in something
> else.** **The user opens it with the CC run of his choice.**
>
> **The writing side's restraint.** From hand-over, the writing side does not touch this file or any file
> named in §0's read-first block, and **does not touch the working tree at all**, while the batch runs.
>
> **Why now.** The L0+L1 brief is complete and its next act is the user booting a deriving session. **A
> sitting that has produced twenty-four rulings should not run through a derivation with its record
> uncommitted.** This batch changes no content: everything it commits is already on disk and was written
> under a ruling.
>
> **★ ONE CLAIM OF THIS SIDE'S THAT THIS BATCH MUST ESTABLISH RATHER THAN INHERIT.** The writing side
> told the user the ruling record *"has never landed in git."* **That was asserted from D-230's wording
> and not from the tree**, and the changed-path enumerations of three preceding batches list
> `cowork_rulings_2026_08_31_decision_surface_sitting.md` as **` M `** — tracked and modified — which
> contradicts it. **Task 1 establishes the true state and reports it. This side's claim is not to be
> repeated by this batch on this side's authority.**

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1).

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
   gating answer.
2. `BUILD_AND_TEST.md` — **conditionally mandatory, condition NOT met**: this batch builds nothing, runs
   no test and runs no project tool.
3. **`CLAUDE.md`'s branch and commit rules, and the dispatch protocol's own — whole and binding.** This is
   the one batch of this sitting that writes to git, so **the repository's own rules about branches,
   commit shape and what may be committed govern every act below, and where they and this document
   differ, THEY WIN and the difference is reported.**
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` — **whole.** It is the principal object being
   landed, and **D-230** is its authority.
5. This document, whole.

The bash rules of `CLAUDE.md`'s VS Code section bind every command (#6).

## 1. Task 0 and Task 1 — establish the true state before committing anything

**Pin** this file and every file §0 names with `git hash-object -w`. A read disagreeing with its pin is a
**STOP**.

**Establish and report, before anything rests on it:**

- **The full changed-path enumeration** — every tracked-and-modified path and every untracked path,
  reported whole and not summarised. *If the standing shell-read guard refuses `git status --porcelain`,
  use the substitute it names and say so; three preceding batches met exactly this.*
- **Whether `cowork_rulings_2026_08_31_decision_surface_sitting.md` is tracked**, and if it is, **how far
  the working copy has diverged from what HEAD holds** — the committed blob's size, and the number of
  lines added and removed. **Report it plainly whichever way it falls.** This answers §0's flagged claim.
- **The branch state, and what `CLAUDE.md`'s rules require of it.** Report the current branch, and what
  those rules say must happen before a commit on it. **If they forbid committing where you stand, STOP
  and report; do not create, switch or rebase anything on your own judgment.**
- **Whether the repository's conventions treat `cc_instruction_*.md` and `cc_*_report_*.md` as committed
  material**, established at `CLAUDE.md` and the dispatch protocol rather than inferred from the fact that
  older ones exist in history. **If the convention is silent, say so and commit them anyway under §2's
  list, flagging the silence.**

## 2. Task 2 — the commit set, enumerated, and the one deliberate exclusion

**Commit exactly the paths below that Task 1 found present, and nothing else.** A path in this list that
Task 1 did not find is reported, not hunted for.

**The record and the instrument it produced:**

- `cowork_rulings_2026_08_31_decision_surface_sitting.md`
- `cowork_blind_session_brief_l0_l1.md`

**The governing document corrected under a ruling, and the pack machinery:**

- `FRAMEWORK.md`
- `tools/audit/gen_derivation_boot_pack.py`
- `tools/audit/derivation_boot_pack.json`
- everything under `tools/audit/derivation_boot_pack/l0-l1/`

**The score-tag instrument and its table:**

- `tools/audit/gen_score_tags.py`
- `tools/audit/score_tags_l0l1_sweep.json`

**This sitting's dispatches and their reports** — every `cc_instruction_*_2026_08_31.md`,
`cc_instruction_*_2026_09_01.md` and matching `cc_*report*_2026_08_31.md` / `cc_*report*_2026_09_01.md`
that Task 1 finds, **listed individually in your report rather than committed by wildcard.**

**★ THE ONE DELIBERATE EXCLUSION, AND ITS REASON, WHICH IS NOT TIDINESS.**

**Do NOT commit `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` or its
`.provenance.md`.** `.gitattributes` carries `*  text=auto` and **no rule for `*.mscx`** — established at
the object by two preceding batches, and its own comment says `.mscx` is left under that rule by design.
**The exemplar is a 1.7 MB LF-only file whose provenance record claims, and proves, that not one byte was
altered from the container extraction.** Committing it under `text=auto` puts a CRLF checkout between
that file and its own provenance claim — **the OI-195 / OI-34 line-ending class that `.gitattributes`
names in terms.**

**Whether `.gitattributes` should gain a rule for committed `.mscx` exemplars is OWED TO THE USER (§3y),
and this batch does not answer it, does not edit `.gitattributes`, and does not add an ignore rule.** The
two files stay **untracked on disk**, where the deriving session can read them exactly as they stand.
**Report this exclusion prominently, as a thing left undone on purpose.**

## 3. Task 3 — the commit

**One commit**, following `CLAUDE.md`'s commit rules for shape and message. The message says what landed
and under what authority — **the sitting's rulings, the completed L0+L1 brief, the pack, the score-tag
instrument, and this sitting's dispatches and reports** — and it **names the exclusion and its reason in
one line.**

**No figure of this project's own measurement appears in the message (#17f, D-431).** No count of rulings,
no byte size, no score figure; the message names what landed, not how much of it there is.

**Nothing is amended, squashed, rebased, force-pushed, tagged or pushed.** **Do not push.** If
`CLAUDE.md`'s rules require a push for a commit to count as landed, **STOP and report that** rather than
pushing on your own judgment.

## 4. Task 4 — prove what landed

**After the commit, establish and report:**

- **The commit's own hash, and the full list of paths it contains**, taken from git and not from §2.
- **That every path of §2 that Task 1 found is in it**, and that **no path outside §2 is** — a path in the
  commit that §2 does not name is a **STOP**.
- **That the two excluded files are still untracked and still on disk**, unchanged in size and `sha256`
  from Task 1.
- **The changed-path enumeration re-run**, showing what remains uncommitted and why — the exclusion, this
  batch's own report, and anything Task 1 found that §2 does not name.

## 5. Done

Done when: the true tracked state of the record is reported and §0's flagged claim answered; the branch
rules were read and obeyed; one commit exists carrying exactly §2's found paths; the exclusion is
reported with its reason; and the post-commit enumeration is given. **Every STOP met is written up. Then
close on the ruled stop form.**

**The standing self-check runs before the report is written** — the actual diff on disk of every touched
file, against the principles, the conventions and `DEFECT_TYPES.md`.

## 6. STOPs

`CLAUDE.md`'s rules forbidding a commit where you stand; a path in the commit that §2 does not name;
either excluded file appearing in the commit, or having moved on disk; a read disagreeing with its pin;
any act outside §7.

**Not a STOP, and reported rather than resolved:** a §2 path Task 1 does not find; the record turning out
to be tracked, or untracked, either way; the conventions being silent on `cc_*` files; the shell-read
guard refusing a command.

## 7. The footprint

**This is the one batch of this sitting that changes the repository's history, and that is its whole
purpose.** It **creates one commit** and **this batch's report**.

**Edited: NOTHING.** **No file's content is changed by this batch** — every file it commits is already on
disk, written under a ruling, and is committed as it stands. **`.gitattributes` is NOT edited and no
ignore rule is added.** No score is edited, renamed, moved, converted, copied or re-saved. No registry,
manifest or pin is touched; **`tools/snapshot_sources_manifest.json` and the eleven snapshot sources are
untouched (Hard rule 2)**. **No governing document is amended** — `FRAMEWORK.md` is committed in the state
a ruled batch already left it, not further edited.

**Not done at all:** no build, no test, no golden, no measurement of the analysis; nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and neither frozen pack
opened**; **no open-items row created, flipped or discarded**; **no decisions-register entry and no
`D-NNN`** — that register cannot accept one and `cowork_register_rule_c_suspension_2026_08_28.md` is the
route; the workbook not opened; **no score staged**; **no brief written or amended** — the brief is
committed, not touched; **no session booted**; **nothing pushed**.

**And three things this batch must NOT quietly repair while it is in the tree.** The manifest's
`rendered_from` line for pack member (7) says two removed passages where the filter carries three. The
inherited bare uses of *bar* and *register* belong to the scoped terminology pass (**OI-229**). The
`.gitattributes` question is the user's. **All three are committed as they stand.**

**The tracked-modification assumption, as a shape.** This batch expects the four tracked-and-modified
paths the three preceding batches all established — `FRAMEWORK.md`,
`cowork_rulings_2026_08_31_decision_surface_sitting.md`, `tools/audit/derivation_boot_pack.json`,
`tools/audit/gen_derivation_boot_pack.py` — **plus `cowork_blind_session_brief_l0_l1.md`, which the
writing side amended after those batches ran and which may appear as either modified or untracked.**
**Any OTHER tracked modification this batch did not make is reported**; here it is **not** a STOP, because
this batch's purpose is to land what is in the tree, and an unexpected modification must be seen and
described before it is committed. **If one appears, report it and STOP before committing** so the user
rules on it.

---

*Provenance: written by the Cowork writing side, 2026-09-01, executing the landing D-230 provides for.
**The facts this dispatch asserts were read at their objects by this side with file tools**: the
`.gitattributes` `text=auto` rule and its absent `*.mscx` rule; the exemplar's size and its provenance
record's byte-identity claim; the pack directory's ten members. **The tracked state of the ruling record
is NOT asserted here — this side's earlier claim about it is flagged in §0 as unchecked and Task 1
establishes it.** No shell command was run on the repository by the writing side. No figure of this
project's own measurement is restated (#17f, D-431).*
