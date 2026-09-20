# CC INSTRUCTION — THE CLOSE OF THE BATCH THAT STOPPED AT §6(b) (2026-09-20)

**This batch finishes the close that `records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_2026_09_20.md`
could not finish, and it repairs the defect that stopped it. It takes no new work of any kind.**

**★ THIS DISPATCH WAS AMENDED 2026-09-20, AFTER IT WAS FIRST LANDED AND BEFORE IT RAN**, at the
writing side's own source-check of it, in three places besides this note and no others: **Task 1**, which ordered a
replacement that would have destroyed the wording it claimed to preserve and now orders an insertion
instead; **B5**, whose opening clause admitted the replacement and not the insertion; and **§5 item
2**, which described the replacement. Each carries its own note with the former wording. **Nothing
else changed** — no bar but B5's opening clause, no other task, no member of §4(a), no STOP. **Its
size is therefore no longer the 15,093 bytes handoff entry 221 §0 records**; take the current figure
at 0(a)'s pin. Nothing has run against the earlier text.

**THE DEFECT, DECLARED ON THIS DISPATCH'S FACE, BECAUSE IT WAS THE WRITING SIDE'S.** That dispatch's
§6(a) required that no guard whose verdict was PASS at the opening capture carry any other verdict at
the close, and then its §6(c) ordered a `STATUS.md` entry — an act that makes
`tools/audit/session_start_read_size.json` and `tools/audit/defense_share.json` stale and turns both
their checks red. It ordered no repair and its bars named neither artifact, so its own condition and
its own task could not both be satisfied. **The fact was on the record and the writing side had read
it**: handoff entry 219 §4 names those same two guards as the two that moved at the previous close.
The executing side stopped and reported rather than resolving it, which is what its §1 required.
**Nothing about the previous batch's work is in question** — it is intact on disk and this batch
verifies that before it does anything.

---

## 1. Bars

**B1 — NO TOOL SOURCE IS EDITED BY THIS BATCH. NONE.** Not `tools/audit/gen_derivation_boot_pack.py`,
which the previous batch already edited and this one must not touch; not either of the two generators
Task 2 runs; not `tools/audit/gen_status_batch_bound.py`; not any guard. **If a task below seems to
need a tool edited, that is a bar contradicting a task — STOP and report it.**

**B2 — THE FORWARD BOUND HAS ALREADY RUN AND IS NOT RE-AIMED AND NOT RE-RUN.** The previous batch
re-aimed `tools/audit/gen_status_batch_bound.py` at `d42fa5604538ece1abadcada6437415e67a81dbd`, ran
its `--apply`, and its `--check` is green; `STATUS_ARCHIVE.md` already holds the moved entry.
**Running `--apply` again would fire that tool's own already-in-the-archive STOP.** Do not run it in
either mode except where Task 3 runs the whole guard set, which invokes its `--check`.

**B3 — NOTHING under `tools/audit/derivation_boot_pack/` is read for content, written, deleted,
renamed or moved.** No pack file is opened for editing.

**B4 — no `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/`
or `tools/robust_stop/`, no measurement of the analysis, no paper, no reading-pass extract.**

**B5 — no governing document is amended except `STATUS.md`'s newest entry, and there only by the ONE
insertion Task 1 orders, at the ONE point Task 1 names. No existing sentence of it is rewritten or
removed (#12).** Not `CLAUDE.md`, not `ARCHITECTURE.md`, not `FRAMEWORK.md`, not `DECISIONS.md`, not
`OPEN_ITEMS.md`. No open-items row created, flipped or discarded. No decisions-register entry and no
`D-NNN` allocated. *(★ THE OPENING CLAUSE OF B5 WAS AMENDED 2026-09-20 with Task 1, at the writing
side's own source-check. It read "no governing document is amended except the ONE sentence of
`STATUS.md` Task 1 names", which admitted a rewriting of one sentence and not the insertion the
amended Task 1 orders — a bar that would have contradicted its own task, which is the same shape as
the defect this dispatch exists to repair. The rest of B5 is untouched.)*

**B6 — `tools/audit/claude_md_finer_archive.json` is held back**: not staged, not reverted, not
investigated. Its modification's cause is still established by nobody and establishing it is not this
batch's work.

**THE FOOTPRINT ASSUMPTION, written from the paths this batch's own tasks touch.** This batch's own
orders modify exactly three existing files: `STATUS.md` (Task 1),
`tools/audit/session_start_read_size.json` and `tools/audit/defense_share.json` (Task 2). It creates
exactly one new file, your report. **Every other path §4 commits is already on disk from the previous
batch or earlier and is committed unchanged**, and §4 orders each one's unchangedness proved.

**THE ORDER OF TASKS 1, 2 AND 3 IS ITSELF A RULE, NOT A CONVENIENCE.** `STATUS.md` is the second
member of `gen_session_start_read_size.py`'s measured set, and `gen_defense_share.py` imports that
same reader, so any `STATUS.md` edit after Task 2 would make both artifacts stale again and any guard
capture taken before Task 2 would measure a tree that no longer exists. **Task 1 is the LAST edit to
`STATUS.md` in this batch. Task 2 runs after it. Task 3's capture is taken after Task 2. Nothing
between Task 2 and the commit may write to `STATUS.md`.**

---

## 2. Task 0 — the start state, proved before anything is written

**0(a).** Pin this dispatch and take every later re-read of it from its blob:

```
git hash-object -w records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_close_2026_09_20.md
```

Record the hash. **The writing side has declared that it will not touch this dispatch, the previous
dispatch, or any file either names, while this batch runs.**

**0(b) — the refs.** Read `.git/refs/heads/master` and `.git/refs/remotes/origin/master` with the
file tools. **Both must read `d42fa5604538ece1abadcada6437415e67a81dbd`.** If either has moved,
STOP: something ran that this dispatch does not know about, and the whole start state is void.

**0(c) — the previous batch's work is intact.** Prove all four with the file tools, and report each
result:

1. `tools/audit/gen_derivation_boot_pack.py` carries `def frozen_from_disk(` **exactly once**.
2. It carries `def check_all(manifest: dict, packs: dict, displaced: list[dict]) -> int:` **exactly
   once**.
3. `tools/audit/derivation_boot_pack.json` carries **zero** occurrences of `lines_rendered`, and zero
   of `the_text_removed`.
4. `tools/audit/status_batch_bound.json` records, at its own top-level `base_commit` field,
   `d42fa5604538ece1abadcada6437415e67a81dbd`, with `the_then_previous_batch`
   `cc_instruction_backup_third_commit_and_push_2026_09_20.md` and `entries_moved` 1 — and
   `STATUS_ARCHIVE.md` already holds the entry the forward bound moved.

**Any one of these failing is a STOP.** Report which, and what you found instead. Do not repair it.

**0(d) — the working tree.** Take the enumeration with `python tools/audit/changed_paths.py` — the
sanctioned route, the shell-read guard having refused a working-tree `git diff` to the previous
batch. Report it whole. **Nothing may be staged when this batch opens**; if anything is, STOP.

**0(e) — the OPENING GUARD CAPTURE.** Run the guard set once and save the capture OUTSIDE the
repository working tree; name the file in your report. **Expected, and to be reported as found rather
than assumed:** `tools/audit/gen_session_start_read_size.py --check` FAIL,
`tools/audit/gen_defense_share.py --check` FAIL, `tools/audit/gen_derivation_boot_pack.py --check`
PASS. That is the state the previous batch left and the state this batch is written for. **If the two
first are already PASS, STOP and report it** — someone has run them since, and the start state is not
what this dispatch assumes.

---

## 3. The three tasks, in this order and no other

### Task 1 — supersede the block of `STATUS.md` that says the batch stopped, by insertion

The newest entry ends with a block recording the stop. It is true of the state it described and is
made stale by this batch, so it is **superseded in place with its former wording preserved (#12)**,
not deleted and not rewritten.

**Locate the block by its two anchors and confirm each is found EXACTLY ONCE, the closing after the
opening. If either is not found exactly once, STOP.**

- **Opening anchor:** `★★ **AND THE BATCH THEN STOPPED BEFORE ITS COMMIT`
- **Closing anchor:** `and it is reported here rather than worked around.`

**★ THIS TASK WAS AMENDED 2026-09-20, BEFORE THIS DISPATCH RAN, AT THE WRITING SIDE'S OWN
SOURCE-CHECK — AND THE DEFECT WAS AGAIN THE WRITING SIDE'S.** As first written this task ordered the
span REPLACED by a past-tense rewriting of it, and that rewriting ended by asserting that the former
wording stood preserved (#12). It would not have: every sentence of the former wording would have
been gone, the rewriting standing in its place, and the assertion would have been false of the file
the moment it was written — which is what #10 forbids a governing surface to do about itself. The
task now INSERTS and replaces nothing, so the preservation the preamble above promises is what
actually happens. *(The first writing also called the close's own entry "the second member of
`gen_session_start_read_size.py`'s measured set". The second member of that table is `STATUS.md`,
the file; the entry is text inside it. The inserted text below names the file.)*

**DO NOT REPLACE OR DELETE THE SPAN. It stands exactly as it is (#12).** Insert the text below
immediately after the end of the closing anchor, before whatever follows it. **It is set as a
quotation here only so its boundaries are visible: the leading `> ` markers are NOT part of it, and
it goes in as ordinary running prose inside the entry's existing italic paragraph, exactly like the
sentences on either side of it.** One space separates it from the closing anchor's full stop.

> ★★ **AND THE CLOSE WAS THEN TAKEN BY A DISPATCH OF ITS OWN** —
> `records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_close_2026_09_20.md`, which runs
> the two generators after the last edit to this file, takes its guard capture after them, and
> commits and pushes what both batches produced. **The sentences immediately above stand as written
> of the batch they describe (#12)** — they were true of it, and what supersedes them is this
> sentence and not a rewriting of them. The cause they name is unchanged and was established at the
> tools that carry it: **this file is the second member of `tools/audit/gen_session_start_read_size.py`'s
> `MEMBERS` table**, and `tools/audit/gen_defense_share.py` carries
> `import gen_session_start_read_size as reader`, so an edit to this file moves both artifacts.

**Nothing else in `STATUS.md` changes.** No other entry is touched, no `Last updated: ` prefix is
moved, and no second entry is written. **This is the last write to `STATUS.md` in this batch.**

### Task 2 — the two generators, in write mode, after Task 1 and not before

```
python tools/audit/gen_session_start_read_size.py
python tools/audit/gen_defense_share.py
python tools/audit/gen_session_start_read_size.py --check
python tools/audit/gen_defense_share.py --check
```

Neither tool takes an argument parser; running it with no `--check` is its write mode and prints
`wrote tools/audit/<artifact>.json`. **Report all four outputs verbatim and all four exit codes.**

**EXPECTED: the two write runs exit 0 and each names its artifact; both `--check` runs exit 0 and
print `the session-start read measurement re-derives` and `the defense-share measurement re-derives`.**

**STOP CONDITIONS, each ending the batch where it fires:**

1. **Either `--check` still reports `STALE vs the measurement`.** Report both outputs whole and make
   no further change. **Do not edit either tool** — B1 forbids it and a red check here means the
   cause is not what this dispatch believes.
2. **A `STOP:` line or a traceback from either tool.** Report it whole.
3. **Either write run modifying any path other than its own artifact.** Take
   `python tools/audit/changed_paths.py` immediately after the two write runs and report it; a third
   path appearing under `tools/audit/` that this dispatch does not name is a STOP.

### Task 3 — the CLOSING GUARD CAPTURE, taken after Task 2

Run the guard set once more and compare it against the opening capture of 0(e), **verdict by
verdict**.

> **THE CONDITION: no guard whose VERDICT was PASS at the opening capture may carry any other verdict
> at this capture.** A guard that moves FAIL → PASS is ALLOWED and REPORTED. **No condition is written
> on any guard's printed output, on any count in that text, or on the number of failing guards** —
> `gen_derivation_boot_pack.py --check` now prints a line that moves whenever a source moves, and an
> equality over output would stop this batch for a green guard.

**Expected movements, to be reported as found:** `gen_session_start_read_size.py --check` and
`gen_defense_share.py --check` both FAIL → PASS. `gen_derivation_boot_pack.py --check` stays PASS.

**If any guard that was PASS at 0(e) is not PASS here, STOP: commit nothing, and report which guard,
both verdicts and both outputs whole.**

---

## 4. The commit, and the push

**4(a) — by EXPLICIT PATH, never a directory pathspec.** The candidate set is exactly:

1. `tools/audit/gen_derivation_boot_pack.py`
2. `tools/audit/derivation_boot_pack.json`
3. `tools/audit/session_start_read_size.json`
4. `tools/audit/defense_share.json`
5. `tools/audit/gen_status_batch_bound.py`
6. `tools/audit/status_batch_bound.json`
7. `STATUS.md`
8. `STATUS_ARCHIVE.md`
9. `records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_2026_09_20.md`
10. `records/cc/reports/cc_report_boot_pack_frozen_manifest_2026_09_20.md`
11. `records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_close_2026_09_20.md`
12. `records/cc/reports/cc_report_boot_pack_frozen_manifest_close_2026_09_20.md`
13. `records/cc/reports/cc_report_backup_third_close_2026_09_20.md`
14. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nineteen.md`
15. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty.md`
16. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_one.md` — **only if it exists
    on disk.** If it does not, say so and commit the other fifteen. **Do not wait for it.**

**Establish members 10, 13, 14 and 15 rather than asserting them** — the four this batch does not
write. For each, take its size by the content-addressed route the previous batch used
(`git hash-object -w --no-filters <path>`, then `git cat-file -s <identity>`), read its last
non-empty line, and report both. **A tail that is not ordinary text, or a NUL byte, is a STOP.**
Members 13, 14 and 15 must still measure 26,585, 18,120 and 21,102 bytes; **a different figure at any
of them is a STOP**, because nothing in either batch may have changed them.

Then stage, and **prove the staged set is EXACTLY the candidate set and nothing else before
committing.**

**HELD BACK, AND NAMED SO NOTHING SWEEPS THEM IN:** `tools/audit/claude_md_finer_archive.json`; the
untracked `.mscx` under `tools/audit/derivation_exemplars/l0-l1/`; the `scratch_artifacts/` tree; the
two PDFs; and every other path the enumeration reports that the candidate set does not name.
**Confirm in your report that each is absent from the staged set.** Report anything unexpected and
leave it.

**4(b) — push.** After the commit, push every branch that received it. `origin` is the fork; `upstream`'s
push is disabled and is not to be used. **If the push fails for any reason, REPORT IT; do not skip it
silently and never pass `--force`.** Name the pushed branches.

---

## 5. The report

`records/cc/reports/cc_report_boot_pack_frozen_manifest_close_2026_09_20.md`, carrying:

1. Task 0's pin, both refs, the four start-state proofs of 0(c) with what you found, the enumeration
   of 0(d), and the opening capture with its path and its verdicts for the three named guards.
2. Task 1's two anchor counts; confirmation that the span was LEFT STANDING unchanged and that the
   insertion was made immediately after its closing anchor; and confirmation that no other part of
   `STATUS.md` changed.
3. Task 2's four outputs and four exit codes verbatim, and the enumeration taken after the write runs.
4. Task 3's verdict-by-verdict comparison: every guard whose verdict moved, in which direction, and
   the statement that no PASS became anything else.
5. The established set of 4(a): per held-over file, its blob, its size and its last non-empty line;
   the staged set proved exactly equal to the candidate set; the held-back paths confirmed absent.
6. The commit hash and the pushed branches.
7. **What you did NOT do**, named rather than counted — and in particular that no tool source was
   edited, that the forward bound was neither re-aimed nor re-applied, and that no pack file was read
   for content, written or moved.

**If any expected result does not appear, stop at that task and report it. Do not continue to the
next one, and do not resolve a bar that contradicts a task.**
