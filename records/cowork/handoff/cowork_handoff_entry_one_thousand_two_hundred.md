# Cowork handoff entry 1200 — 2026-11-23 — SESSION 11 OF THE L3 APPLICATION (TASK 3, SECOND STRETCH, §L.5 TO §L.12) VERIFIED AT THE OBJECTS: IT HOLDS; ONE SLIP IN THE WRITING SIDE'S INSTRUCTION AND ONE IN CLAUDE CODE'S REPORT RECORDED, NEITHER IN THE WORK; A NEW "REST" COLLISION OF THE WRITING SIDE'S OWN FOUND, ITS CORRECTION CARRIED TO SESSION 12; SESSION 12'S INSTRUCTION NOT BEGUN; HANDED OVER FOR IT

**The current entry point.** Entry 1199 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1200 asked for by staging in a call of its
  own, *"does not exist"*; entry 1199 (8,820 bytes), entry 1198 (9,927) and entry 1026 (11,103, its §3 included) read
  whole.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` read whole (11,726 bytes,
  1794136674043, unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207,
  unmoved; the gating answer 247 open, 222 gating, 25 non-gating, unchanged (`tools/audit/nongating_apparatus_rows.json`
  lines 183–185).
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `760c3cfb713be89aeb679966742ba0f1c9eae843`, modification times 1795437085951 and
  1795437088482 — moved from `73d26f37…` by session 11's three commits (§2 item 2). Nothing is running; no dispatch is
  out.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only, untracked. **Untracked writing-side entries now: 1200 only**
  (1198 and 1199 were landed by session 11's commit `b01263c5…`); session 12's instruction must land and read it.

## 2. What this sitting established

1. **Session 11's report read in FULL** (`records/cc/reports/cc_report_l3_application_session_11_task_3_stretch_2_2026_11_23.md`,
   26,840 bytes), and **session 11's instruction read whole** (52,518 bytes). The claims of items 2 to 4 below checked
   at the git objects (decompressed and SHA-1-verified over staged copies) and at the reading file, not taken from the
   report (the user's rule of 2026-09-03); item 7 names what was not checked.
2. **The three commits [checked]:** `b01263c5e5e4444e9532033984f476cdb979d33a` (parent `73d26f37…`) →
   `402ed789f5caba5de5ca64798b7ecf3d9c599212` → `760c3cfb713be89aeb679966742ba0f1c9eae843`, each subject exactly as the
   instruction gives it (its lines 500, 482, 507). By tree comparison down to the changed folders: the first ADDS
   exactly three paths — the instruction (blob `cb2d14d4…`), entry 1198 (`0cd059c6…`) and entry 1199 (`255941a6…`),
   each equal to the device copy as staged; the second changes ONE path, the reading file
   `ratification_surfaces/cowork_comparison_l3_reading.md`, blob `10cc2c71…` → `3438641649f942b74024832ad18b5fce47bfde2d`
   (5,186,605 bytes, 83,879 lines, line feeds only), and the working-tree file is byte-identical to it; the third ADDS
   the report only (`79c88242…`), equal to the copy read.
3. **The reading file's diff [checked]**, old blob against new: 198 lines added, 1 deleted; 84 changed passages with
   three lines of context, as the report states. Counts: `*RULED DISPOSITION (` 212, `*RULED PLACEMENT (` 3,
   `*RECORDED DISPOSITION (` 0. **All 98 lines** rebuilt by script from the instruction's §3.2 templates and row lists
   and compared character for character: each present exactly once as an added line, none missing, none extra; each
   under its own row heading; each preceded by a blank line, after the row's `*PROPOSED DISPOSITION.*` paragraph and
   after any session 10 line (the nine rows 3.1, 8.11, 8.24, 8.59, 8.96, 19.30, 19.31, 19.38, 19.58), followed by a blank
   line and then another ruled line, the row's `---` or an *At the source now* paragraph; new lines beneath each row in
   the order §3.2 gives. The in-progress line at line 54 is the instruction's §3.5 item 3 text exactly, and the one
   deleted line is its former text (§L.1 to §L.4). The §10 entry at line 80403 is the instruction's §3.3 text exactly,
   after the Rows 57.318 (i) and 57.322 (i) entry, under `**To *the measurement of the analysis* (NOT A LAYER).**` (line
   80232), before the blank line and §10's closing note.
4. **The report's declared departures, judged:** (1) row by row instead of entry by entry — the end state is the one
   ordered (item 3); (2) the pin by the standing fallback — as declared, the blob equal; (3) the instruction's §3.1 item
   3 list omits Rows 8.35, 8.113 and 19.38 — **true, a slip of the writing side's instruction** (entry 1199's sitting),
   not in the work: Claude Code applied the item's own rule and the order was checked (item 3); (4) session 10's lines
   on Rows 8.24, 19.30 (ii), 19.31 (ii) and 19.58 (iii) name no side — true at the file (lines 9266, 24567, 24592,
   25091); both lines on each row are HISTORICAL, so no two-record conflict arises; (5) §11 searched on an extract of the
   stretch 1 commit — not re-checked, §11 untouched by the diff; (6) one section read in passing — nothing follows.
5. **One slip in the report, recorded here and not edited into the committed report:** its §8 says the *"rest"* and
   *"part"* wording *"comes from the records and the forms"*. For *"rest"* that is half true: the instruction's §3.2 (r)
   says the label *"Its rest:"* is the writing side's (from §L.8's table, *"For the rest"*), and its §3.3 says the §10
   entry's subject clause (*"Row 7.37, its rest — …"*) is the writing side's.
6. **A new reserved-word collision, introduced by the writing side** [checked at the instruction and the reading file]:
   *"rest"* in the sense of remainder, at reading-file line 3812 (*"Its rest:"*) and line 80403 (*"Row 7.37, its rest"*).
   `CLAUDE.md`'s convention on music-theory words says no NEW collision is introduced and anything written for the user
   avoids the collided sense. Judged as no real choice (the convention decides it; the label was the writing side's and
   marked overrulable): **the correction is carried to session 12's instruction** (§3 step 1). *"Part"* is not in the
   same case: it is the big dispatch's forms' standing word for a part of a row's claim (form (b)'s *"names that part"*),
   an existing collision owned by `OPEN_ITEMS.md` OI-229; nothing further now. The user was told both judgments; his
   "yes" was to writing this entry, which carries them; he has not ruled on them separately and may overrule.
7. **Not re-checked by this sitting:** the quotations against the records (entry 1199 §2 item 2 checked every one at
   the instruction's writing; Claude Code reports each matched); the report's judgment that each row's outgoing
   statement fits its record; the 396 untracked paths [relayed]; the 440 added / 4 deleted against the Task 2 commit
   `4b6dc3bd…` [relayed]; the §10 and §11 searches (§10 changed only by the one entry, §11 untouched, at the diff).
8. **Degradation tells (2026-08-15 list): none observed.** Handed over before the instruction-writing on a capacity
   judgment stated to the user (the reading already done here, against the new reading the next stretch's sizing
   needs), his word "yes". **On the model (2026-11-12):** nothing suggests Opus was not enough.

## 3. The plan — carried forward

1. **Next Cowork session: write session 12's instruction** (Task 3, the next stretch from §L.13), on the pattern of
   sessions 10 and 11's instructions (§2 reading list, §3 rules and lines, §4 replaced orders, §5 acts), applying entry
   1194 §2 item 4's two-record rule across stretches, sized from §L.13 onward. Its first-checks tip is `760c3cfb…`; its
   Task 3 (f) diff base is session 11's Task 3 commit `402ed789…`; the reading file's expected blob is `34386416…`
   (counts 212 / 3 / 0); its act 1 lands **entry 1200** (and that session's own entry, if written before the hand-over).
   **It also orders the correction of item 6 above:** at reading-file line 3812, *"Its rest:"* → *"Its remainder:"*; at
   line 80403, *"Row 7.37, its rest —"* → *"Row 7.37, its remainder —"*; nothing else in either line changed; former
   text recoverable at `402ed789…` (#12's recoverable clause, as for the in-progress line) unless the user wants it kept
   in the file. Its diff arithmetic must count these two changed lines (2 more added, 2 more deleted against `402ed789…`;
   against the Task 2 commit, deleted 4 + 2). **Its own authored labels are checked against `CLAUDE.md`'s list of
   collided words before landing**, so the slip is not repeated. And its §3.1 list of rows with more than one line is
   checked against §3.2 (the slip of item 4 (3)). Check it as its own turn; land on the user's word; then give the user
   the hand-over to Claude Code with the long opening line of 2026-10-26.
2. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1192 §3 step 3.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1199 §3, and: (a) a
script that rebuilds every line from the instruction's §3.2 templates (by instruction line number) and compares them
as a multiset with the added lines, then checks each line's row heading, blank lines and order beneath the row, verifies
a stretch in one pass; (b) the loose objects of the three commits, their trees and the reading file's two blobs were all
loose under `.git/objects/` and staged without trouble (the reading file's blobs about 1.5 MB compressed each);
(c) entry 1201's file name would be `cowork_handoff_entry_one_thousand_two_hundred_and_one.md`; check by staging.

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** No dispatch is written; session 12's instruction is handed to
   Claude Code only by the session that writes and checks it.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1201 exists (if it does, report and ask), reads this entry whole,
   entry 1199 whole and entry 1026 §3, asks the session-start read, reads the three git reference files (anything but
   `760c3cfb…` means something ran: find out what first), then does §3 step 1.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only searches and measurements over staged copies (`grep`, `sed`, `cut`, `head`, `wc`,
  `diff`, `cmp`, `python3 -I` reading, inflating and comparing files), with scripts, two scratch copies of the reading
  file's blobs and the diff written to `/home/claude/scr` in the container. Nothing written by any shell into a staged
  copy, the repository or the device.
- **Staged beyond the boot list:** the git reference files; `STATUS.md` and the gating JSON; session 11's report and
  instruction; the reading file; the loose git objects of the three commits and the old tip, their root trees and the
  trees down to the changed folders, and the reading file's two blobs. **Listed:** the repository root.
- **This entry written in the outputs folder** with the Write tool and landed with the commit tool. No git on the
  device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1199. The user's words: the opening
instruction; "shortened"; "yes" (this entry and the hand-over).*
