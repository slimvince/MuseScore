# CC INSTRUCTION — THE L2 BLIND DERIVATION AND ITS COMPANIONS COMMITTED, AND THE CLOSE (2026-09-27)

> **STATUS: RELEASED 2026-09-27. Run it from Task 0 in order.** Written and source-checked by the Cowork
> sitting booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_seven.md`.
> **If any expected result does not appear, stop at that step and report it. Do not continue to the
> next one, and do not resolve a bar that contradicts a task.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** This dispatch is final at hand-over. The writing side
> will not touch it, nor any file it names, while this batch runs. The one file the writing side writes
> after this dispatch lands and before hand-over is its own handoff entry,
> `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_eight.md`, which is why Task 0
> states no size for it.

**What this batch does.** Three things, in this order:

1. commits the blind derivation of L2, the released L2 brief, the Cowork side's handoff entries and
   this dispatch (Task 0);
2. runs the standing close: the `STATUS.md` entry, the forward bound, the regenerations, the closing
   guard capture (Task 1);
3. commits and pushes (Task 2).

**Nothing else.** This batch compares nothing, judges nothing and edits no content of any file Task 0
commits.

---

## 1. Bars

**B1 — ONE TOOL SOURCE IS EDITED, AND ONLY AT ITS AUTHORED AIMING:** `tools/audit/gen_status_batch_bound.py`
(Task 1(b)): its authored aiming inputs, their comments and one appended row of `PREVIOUS_AIMINGS`, and
no function. **No other tool source is touched.** If a task seems to need another tool edited, **STOP and
report it; do not resolve it.**

**B2 — THE FILES TASK 0 COMMITS ARE COMMITTED AS THEY STAND AND ARE NOT EDITED.** In particular
`cowork_blind_derivation_l2_2026_09_27.md` (the blind derivation) and `cowork_blind_session_brief_l2.md`
(the brief) are not opened for editing, not reformatted, not re-encoded and not line-ending-normalised.
Nothing under `tools/audit/derivation_boot_pack/`, `tools/audit/derivation_exemplars/` or `reading_pass/`
is touched. `cowork_derived_specification_l0_l1_2026_09_03.md` is not read and not written.

**B3 — no `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/`,
`tools/robust_stop/` or `tools/dcml/`, no measurement of the analysis, no paper.** No score or analysis
file is copied, moved or edited. **No session is booted.**

**B4 — NO OPEN-ITEMS ROW is created, flipped or discarded. NO DECISIONS-REGISTER IDENTITY IS
ALLOCATED** (register rule (c) is suspended at `cowork_register_rule_c_suspension_2026_08_28.md`).

**B5 — NO FIGURE IS TRANSCRIBED FROM THIS DISPATCH INTO ANY ARTIFACT (D-431).** The sizes and hashes this
file states are start-state bars and expected values.

**B6 — NO GOVERNING DOCUMENT IS AMENDED EXCEPT `STATUS.md` at Task 1(a).**

**B7 — CARRIED, NOT CHASED:** `tools/audit/gen_guard_classification.py`'s STOP (report it whole and carry
on); the live consumer at `tools/audit/gen_withheld_family_reading.py` lines 146–147 (not repaired);
`tools/audit/claude_md_finer_archive.json` (held back: not staged, not reverted, not investigated); the
untracked `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` (a score file, B3: left as
found).

**THE FOOTPRINT ASSUMPTION.** This batch **modifies** `STATUS.md`, `STATUS_ARCHIVE.md`,
`tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, and — only where the tool
that owns each writes it — `tools/audit/evidence_pin_membership.json`,
`tools/audit/l0_l1_outgoing_population.json`, `tools/audit/session_start_read_size.json`,
`tools/audit/defense_share.json` and the guard set's own artifacts. It **creates** your report. Anything
else the enumeration shows as modified by this batch is outside the assumption: report it and **STOP
before the commit**.

---

## 2. Task 0 — the start state, and the files committed

**0(a) — pin this dispatch:** `git hash-object -w records/cc/instructions/cc_instruction_l2_derivation_commit_2026_09_27.md`;
record the hash and `git cat-file -s <hash>`; take every later re-read of this dispatch from that blob.

**0(b) — the refs, expected to AGREE.** Read `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` **with the file tools** (D-253; never `git rev-parse`). **Both must read
`ce85cdec358f162ed5d9ef4fd009089c6948879b`** *(read so at both files by the writing side at release)*.
Anything else: **STOP**, and report both values as found.

**0(c) — the working tree.** `python tools/audit/changed_paths.py`; report every record other than the
untracked paths under `scratch_artifacts/` verbatim. **Nothing may be staged**; if anything is, report
exactly what and **STOP**. **Expected, as a guide and not as the bar** (the enumeration establishes the
actual set): the brief as a MODIFIED tracked file; the derivation, entries 256 and 257, this dispatch and
(if it exists) entry 258 as UNTRACKED; and the standing population the previous report listed — the
modified `tools/audit/claude_md_finer_archive.json`, the untracked research paths and the untracked
`bwv1049_03_presto.mscx`. **If the brief is reported UNTRACKED rather than modified, or if any other
tracked file is reported modified, STOP and report it.** Then check the last bytes of each TEXT file 0(d)
commits: **a trailing NUL byte, or a final line that breaks off mid-word, is a STOP** — name the file and
stop; do not repair it.

**0(d) — ONE COMMIT: the derivation and its companions.** By explicit path, never a directory pathspec;
each size by `git hash-object -w --no-filters <path>` then `git cat-file -s <identity>`; **a size
different from the one given is a STOP**:

1. **This dispatch**, at the blob 0(a) pinned.
2. `cowork_blind_derivation_l2_2026_09_27.md` — **125,549** *(bridge staging result, read whole by the
   writing side)*.
3. `cowork_blind_session_brief_l2.md` — **35,952** *(bridge staging result)*.
4. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_six.md` — **6,829** *(bridge
   staging result)*.
5. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_seven.md` — **5,510** *(bridge
   staging result)*.
6. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_eight.md` — **only if it exists.**
   No size is stated (restraint paragraph above): report the size you find. If it does not exist, say so
   and commit the rest. **Do not wait for it.**

For item 2, additionally record and report: the first line of the file (expected
`# The blind derivation of L2 — the tonal reading`), and that the line
`> **STATUS: DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED.**` occurs in it exactly once. Either
not holding: **STOP**.

A path the enumeration reports that is not named here is held back and reported. Prove the staged set
before committing. Do not push yet.

**0(e) — THE OPENING GUARD CAPTURE, taken AFTER the commit.** `python tools/audit/gen_guard_state.py`;
save the capture **outside** the repository working tree; name the file in your report; record every
verdict. Then `python tools/audit/gen_guard_classification.py`, expected to STOP (B7).

---

## 3. Task 1 — the close: `STATUS.md`, the forward bound, the regenerations, the closing capture

**In this order and no other.**

**1(a) — the `STATUS.md` entry.** One new dated entry at the head of the dated entries, in the OI-222
pointer convention: a POINTER whose whole is your report, restating **no figure** (D-431). It says what
this batch did — the blind derivation of L2 committed as it stands, with its DRAFT banner, not compared and
not ratified; the released L2 brief committed; the Cowork side's handoff entries committed — and what it
did not do: **no comparison, no session booted, no file it committed edited**, no open-items row, no
`D-NNN`. **No existing sentence of `STATUS.md` is rewritten or removed**, the forward bound's own declared
prefix adjustment excepted. This is the last write to `STATUS.md` in this batch.

**1(b) — the forward bound.** Re-aim `tools/audit/gen_status_batch_bound.py` so that the batch it
identifies is the PREVIOUS one — `cc_instruction_l2_input_contract_cuts_2026_09_27.md`, whose entry heads
`STATUS.md`'s dated entries at the writing side's read. **The aiming, at the tool's authored inputs (read at
the tool by the writing side at release: `BASE_COMMIT` `9f42ec57cb…`, `PREVIOUS_BATCH_DISPATCH`
`cc_instruction_l2_brief_landing_2026_09_27.md`, `DISPATCH`
`cc_instruction_l2_input_contract_cuts_2026_09_27.md`, `TASK` `"Task 3"`, and that batch's own row already
the last of `PREVIOUS_AIMINGS`):**

- `BASE_COMMIT` = the hash of THIS batch's Task 0 commit. Task 0 commits no `STATUS.md`, so that commit's
  `STATUS.md` object is the one both refs carried at 0(b). If the tool's first STOP fires (the batch
  cannot be identified at the base commit), report it whole and make no further change.
- `PREVIOUS_BATCH_DISPATCH` = `"cc_instruction_l2_input_contract_cuts_2026_09_27.md"`.
- `DISPATCH` = `"cc_instruction_l2_derivation_commit_2026_09_27.md"`.
- `TASK` = `"Task 1"` — this dispatch orders this batch's own entry at 1(a) and this move at 1(b), both
  inside its Task 1, which §3's heading names in those words.
- `ACT_DATE` = the date the move actually runs.
- `MOVE_KIND` = `"ordinary"`. `RULINGS` unchanged.
- `PREVIOUS_AIMINGS`: APPEND one row, in the shape of the rows above it —
  `{"executing_act": "cc_instruction_l2_derivation_commit_2026_09_27.md, Task 1", "base_commit": <the
  BASE_COMMIT you set>, "the_then_previous_batch": "cc_instruction_l2_input_contract_cuts_2026_09_27.md",
  "the_kind_of_move": "ordinary"}`. Nothing else is appended and no row is edited.
- Each field's comment is re-stated the way every previous re-aiming re-stated it — the former value
  named, not deleted (#12).

Run `--apply`, then `--check`. **The declared prefix adjustment is expected to fire**, the previous
batch's entry carrying the `Last updated: ` prefix at the base commit; that is why 1(a) writes this
batch's entry first. **If `--apply` reports its already-in-the-archive STOP, report it whole and make no
further change.** Do not read a green `--check` as proof the bound is met (`OPEN_ITEMS.md` OI-379): report
the entries `--apply` actually moved, by name. **The two 2026-09-02 entries do NOT move and are not moved by
hand.** Report the tool's whole diff by explicit blob hashes.

**1(c) — the regenerations the tree now forces**, after 1(a) and 1(b):

```
python tools/audit/gen_evidence_pin_membership.py
python tools/audit/gen_evidence_pin_membership.py --check
python tools/audit/gen_l0_l1_outgoing_population.py
python tools/audit/gen_l0_l1_outgoing_population.py --check
python tools/audit/gen_session_start_read_size.py
python tools/audit/gen_defense_share.py
python tools/audit/gen_session_start_read_size.py --check
python tools/audit/gen_defense_share.py --check
```

Record all eight outputs and exit codes verbatim. For each of `evidence_pin_membership.json` and
`l0_l1_outgoing_population.json`, compare with its blob at this batch's Task 0 commit and **report every
member or entry added, removed or changed, by name**; resolve none. **A `STOP:` line or a traceback from any
of the four tools is a STOP before the commit**; do not edit the tool.

**1(d) — THE CLOSING GUARD CAPTURE.** Compare it with 0(e)'s **verdict by verdict**.

> **THE CONDITION: no guard whose VERDICT was PASS at the opening capture may carry any other verdict at
> this capture.** FAIL → PASS is allowed and reported. No condition is written on printed output or on
> counts.

`gen_guard_classification.py` is expected to STOP (B7): report it whole and carry on. **A guard that moved
PASS → anything else is a STOP before the commit**: report the guard, its two verdicts and its output, and
name every path this batch has modified.

---

## 4. Task 2 — the commit and the push

**2(a) — THE BATCH COMMIT, by explicit path, never a directory pathspec.** The candidate set is exactly:

1. `STATUS.md`
2. `STATUS_ARCHIVE.md`
3. `tools/audit/gen_status_batch_bound.py`
4. `tools/audit/status_batch_bound.json`
5. `tools/audit/evidence_pin_membership.json`, `tools/audit/l0_l1_outgoing_population.json`,
   `tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json` — each only if its tool
   wrote it
6. `records/cc/reports/cc_report_l2_derivation_commit_2026_09_27.md`
7. the guard set's own artifacts, **only those the enumeration reports as modified** — name each.

**Prove the staged set is EXACTLY this set before committing.** **Held back, and confirmed absent from the
staged set:** everything B7 names, and every other path the enumeration reports that no commit in this
batch names.

**2(b) — push** every branch that received commits. `origin` is the fork; `upstream` is not used; **never
`--force`**. Read `.git/refs/remotes/origin/master` with the file tools afterwards and confirm it equals
`master`. If the push fails for any reason, report it.

---

## 5. The report

`records/cc/reports/cc_report_l2_derivation_commit_2026_09_27.md`, carrying in task order, verbatim,
every output this dispatch says to record:

1. Task 0 — the pin, both refs, the enumeration, the last-bytes check, 0(d)'s sizes and the two checks on
   the derivation, the commit's staged set proved and its hash, the opening capture's path and every
   verdict, the guard classification's output.
2. Task 1 — the `STATUS.md` entry quoted whole; the forward bound's aiming, `--apply` and `--check` with
   the entries moved by name; 1(c)'s eight outputs and the members changed; the verdict-by-verdict
   comparison of the two captures.
3. The commits' hashes, the pushed branches, and `origin/master` after the push.
4. **What you did NOT do**, named rather than counted: no tool source but `gen_status_batch_bound.py`'s
   aiming edited; no file Task 0 committed edited; the boot pack, the exemplars and the source
   specification not touched; no governing document but `STATUS.md` amended; no score or analysis file
   moved; no session booted; no comparison made; no open-items row and no `D-NNN` touched.

**WHAT GOES TO THE USER, named rather than counted:** that the derivation and its companions are
committed, with the Task 0 commit's hash; the 1(c) changes; and any STOP.

**If any expected result does not appear, stop at that task and report it. Do not continue to the next
one, and do not resolve a bar that contradicts a task.**

---

*Provenance: Cowork, 2026-09-27 (Stockholm), the sitting booted on entry 257, both refs read at
`ce85cdec35…` at their own files. Checked at the objects by that sitting before release: the four
files' sizes at their bridge staging results; the derivation read whole, its first line and its banner
line read at the file; `STATUS.md`'s head entry (the cuts batch's pointer, carrying the `Last updated: `
prefix); `gen_status_batch_bound.py`'s authored inputs and the last row of `PREVIOUS_AIMINGS`; the cuts
batch's report at its Task 0 enumeration, its closing enumeration, its 3(c) section and its §6 and §7; and
the previous dispatch, whose shape this file follows. **Read, not queried:** that the brief is tracked
rests on the cuts batch's two enumerations, where it appears neither as modified nor as untracked, and on
entry 256's record that it was edited (released) after that batch; that the derivation and entries 256 and
257 are untracked rests on their postdating that batch. No git query was made by this side; 0(c)
establishes both.*
