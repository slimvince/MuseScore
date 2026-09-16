# `cowork_handoff.md` brought current — seven entries prepended in order (dispatch, 2026-09-01)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side on 2026-09-01.
> **The user opens it with the CC run of his choice.**
>
> **★★ WHEN THIS RUNS, AND WHAT IT DEPENDS ON. It depends on NOTHING and it blocks ONE thing.**
> **Run it as soon as the user chooses.** It is **not** gated on the blind L0+L1 deriving session, which
> reads only its brief and its pack and whose pack read-me forbids it `cowork_handoff.md` by name — **the
> two are independent and either may go first.** What this batch **blocks** is the next
> continuing-line Cowork session: that session boots on `cowork_handoff.md`, and until this batch runs
> that file's newest entry is the EIGHTY-FIRST. **Run this BEFORE the next continuing-line session is
> opened.** The writing side does not run it (the 2026-08-26 role ruling) and does not open any session
> that does.
>
> **The writing side's restraint.** From hand-over, the writing side does not touch this file, any file
> named in §0's read-first block, or any of the seven entry files, while the batch runs.
>
> **★ THE FINDING THAT CAUSED THIS, ESTABLISHED AT THE FILE.** `cowork_handoff.md`'s topmost entry is
> the **EIGHTY-FIRST**; its headings run 81, 80, 79, 78, 77, 76, 75, 74, newest first. **Entries
> EIGHTY-TWO through EIGHTY-EIGHT are not in it.** They exist only as standalone files at the
> repository root. **A session that boots on `cowork_handoff.md` and stops there misses seven entries
> and resumes from a superseded picture** — the exact failure the detail-specification phase's record
> clause names, and the reason the eighteenth stop exists.
>
> **★ WHY A BATCH AND NOT THE WRITING SIDE.** This is mechanical concatenation over about a megabyte.
> Doing it from the writing side would mean re-typing seven files' content out of tool output into an
> edit — **the one thing that must never be done to a governing file.** A batch reads the files and
> writes them; nothing is retyped, and the check at §4 proves it.
>
> **This batch changes no entry's content. Not one byte of any entry is edited, reordered inside
> itself, summarised or renumbered.**

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1).

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
   gating answer.
2. `BUILD_AND_TEST.md` — **conditionally mandatory, condition MET** (this batch runs a Python script it
   writes). **Check the condition rather than assume it**, as the last three batches did.
3. **`CLAUDE.md`'s commit rules and the dispatch protocol's — whole and binding.** Where they and this
   document differ, **THEY WIN and the difference is reported.**
4. **`cowork_handoff_entry_eighty_eight.md` — whole.** It is the newest entry, it records this finding,
   and it names this dispatch.
5. This document, whole.

**Do NOT read the other six entry files for their content.** This batch moves bytes; it does not need
to know what they say, and §0's read is not widened by curiosity.

The bash rules of `CLAUDE.md`'s VS Code section bind every command (#6).

## 1. Task 0 and Task 1 — pin, then establish the state

**Pin** this file and every file §0 names, **plus `cowork_handoff.md` and each of the seven entry
files**, with `git hash-object -w`. A read disagreeing with its pin is a **STOP**.

**Establish and report before anything rests on it:**

- **`cowork_handoff.md`'s current entry order**, read at the file: the line number and the ordinal of
  every `## COWORK SESSION CLOSE (` heading it holds, top to bottom. **Confirm the top is the
  EIGHTY-FIRST and that none of EIGHTY-TWO … EIGHTY-EIGHT appears anywhere in it.** **If any of the
  seven is already present, STOP and report** — this batch must not duplicate an entry.
- **That all seven entry files exist at the repository root**, with their byte sizes:
  `cowork_handoff_entry_eighty_two.md`, `…eighty_three.md`, `…eighty_four.md`, `…eighty_five.md`,
  `…eighty_six.md`, `…eighty_seven.md`, `…eighty_eight.md`. **A file that does not exist under that
  spelling is a STOP** — do not guess at a variant name; report what you find at the root instead.
- **Which of the seven are tracked and which untracked**, and the current tracked-modification shape.
  *If the standing shell-read guard refuses `git status --porcelain`, use the substitute it names and
  say so; six batches have now met that refusal.*

## 2. Task 2 — the prepend

**Insert the seven entries into `cowork_handoff.md` immediately after its title line and before its
current topmost entry, in this order, newest first:**

```
eighty-eight, eighty-seven, eighty-six, eighty-five, eighty-four, eighty-three, eighty-two
```

so that the file reads 88, 87, 86, 85, 84, 83, 82, 81, 80, … after the act.

**How, and this part is the whole of the method.** Write a script that **reads each entry file's bytes
and writes them**. **Nothing is retyped, transcribed, reformatted, re-indented, re-wrapped or
normalised.** Do not strip or add a trailing newline inside an entry's own bytes. Each entry file
already opens with its own `---` separator line; **preserve each file's bytes exactly as they are** and
join them so the separators fall where the existing file's separators fall.

**Report the join rule you used, in one sentence**, so the result can be checked against it.

**★ THE ENTRY FILES THEMSELVES ARE NOT DELETED, MOVED OR EDITED.** They stay at the root exactly as they
stand. Whether they are later retired is the user's, not this batch's.

## 3. Task 3 — the commit

**One commit** following `CLAUDE.md`'s commit rules. The message says what it did — seven entries
prepended, no entry's content changed — and **carries no value of this project's own measurement**
(#17f, **D-431**).

**Commit `cowork_handoff.md`, and the seven entry files that Task 1 found UNTRACKED.** An entry file
already tracked and unmodified is not in the commit and is reported as such.

**The message ends with these two trailers, after whatever `CLAUDE.md`'s own form requires:**

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01B5AoBhq79pQk4FaSV9oMsN
```

**A note the last batch established and this one inherits: the repository's older form of the first
trailer carries a parenthetical this string does not.** Use the block above as given; **the difference
is the user's to standardise and is not resolved here.** If `CLAUDE.md` forbids either trailer, **it
wins** — omit it and report which and why.

**Nothing amended, squashed, rebased, force-pushed or tagged. Do not push.**

## 4. Task 4 — prove the entries are intact, which is the check that matters

**Content first, then order.**

- **For each of the seven, prove its bytes survived**: take the entry file's own `sha256` and the
  `sha256` of the corresponding span now inside `cowork_handoff.md`, and show them equal. **A single
  differing pair is a STOP** — it means something was retyped or normalised.
- **Prove `cowork_handoff.md` grew by exactly the seven files' combined size**, allowing only for the
  join rule §2 reports, and state the arithmetic.
- **Re-read the heading order** and show it runs 88, 87, 86, 85, 84, 83, 82, 81, 80, …
- **Prove no heading is duplicated** — every ordinal appears exactly once in the file.
- **Report the commit hash and its full path list**, taken from git; a path in it that §3 does not
  authorise is a **STOP**.

## 5. Done

Done when: the pre-state was established and none of the seven was already present; the prepend was made
by reading bytes rather than retyping them; all seven span digests match their source files; the size
arithmetic closes; the heading order is proven with no duplicate; and one commit exists. **Every STOP met
is written up. Then close on the ruled stop form.**

**The standing self-check runs before the report is written.**

## 6. STOPs

Any of the seven ordinals already present in `cowork_handoff.md`; an entry file missing under the
spelling §1 names; a span digest not equalling its source file's; a heading ordinal appearing twice; a
path in the commit that §3 does not authorise; a read disagreeing with its pin; any act outside §7.

**Not a STOP, and reported rather than resolved:** the shell-read guard refusing a command; an entry file
turning out to be already tracked; `CLAUDE.md` forbidding a trailer.

## 7. The footprint

**Edited: `cowork_handoff.md`, and ONLY by insertion.** Nothing already in that file is changed,
reordered or removed — **prove that too**, by showing the pre-existing content still present unchanged
below the insertion point. **Created:** one commit and this batch's report.

**Not touched:** the seven entry files' own content; `.gitattributes` and no ignore rule — **that
question is still owed to the user**; `tools/audit/derivation_exemplars/` — **still deliberately
untracked, still not committed**; no score anywhere; no registry, manifest or pin;
**`tools/snapshot_sources_manifest.json` and the eleven snapshot sources (Hard rule 2)**; no governing
document amended other than the handoff file this batch is for; `STATUS.md` unedited.

**Not done at all:** no build, no test, no golden, **no measurement of the analysis**; nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and no frozen pack
opened**; **no open-items row created, flipped or discarded**; **no decisions-register entry and no
`D-NNN`** — that register cannot accept one and `cowork_register_rule_c_suspension_2026_08_28.md` is
the route; the workbook not opened; **no score staged**; **no brief written or amended**; **no session
booted**; **nothing pushed**.

**And the three things the landing batches were forbidden to repair in passing stay unrepaired:** the
manifest's `rendered_from` line for pack member (7); the inherited bare uses of *bar* and *register*,
which belong to **OI-229**; and the `.gitattributes` question.

**The tracked-modification assumption.** The last batch closed with exactly one tracked-and-modified
path, `cowork_rulings_2026_08_31_decision_surface_sitting.md`. **This batch expects that one, and
expects `cowork_handoff.md` to become a second the moment §2 runs.** **Any OTHER tracked modification is
reported and you STOP before committing**, so the user rules on it.

**★ AND THREE FILES ARE OWED TO THE NEXT LANDING AND ARE NOT THIS BATCH'S:** the second landing dispatch
`cc_instruction_sitting_landing_second_2026_09_01.md`, its report, and the ruling record. **Do not
commit them here** — §3's authorisation is closed, and an unauthorised path is a STOP.

---

*Provenance: written by the Cowork writing side, 2026-09-01. **The finding was established at the file
by this side**: `cowork_handoff.md`'s heading ordinals were read at it and its topmost entry is the
eighty-first. **The seven entry files' contents were NOT read for this dispatch and are not this
dispatch's business** — it moves bytes and proves they are the same bytes. No shell command was run on
the repository by the writing side. No value of this project's own measurement is restated (#17f,
D-431).*
