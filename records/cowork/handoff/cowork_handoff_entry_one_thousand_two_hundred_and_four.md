# Cowork handoff entry 1204 — 2026-11-23 — SESSION 13 OF THE L3 APPLICATION (ROW 7.67'S HELD LINE, THEN §L.21 AND §L.22) VERIFIED AT THE OBJECTS: IT HOLDS; NOTHING TO CORRECT; SESSION 14'S INSTRUCTION (§L.23 ALONE) NOT BEGUN; HANDED OVER FOR IT

**The current entry point.** Entry 1203 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1204 asked for by staging in a call of its
  own, *"does not exist"* (asked again in a call of its own before this entry was landed); entry 1203 (9,401 bytes),
  entry 1202 (13,520) and entry 1026 (11,103, its §3 included) read whole.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` read whole (11,726 bytes,
  1794136674043, unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207,
  unmoved; the gating answer 247 open, 222 gating, 25 non-gating, unchanged (`tools/audit/nongating_apparatus_rows.json`
  lines 183–185).
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `d56ccc6ee74fa9a5327a5076cc97b33104ecb704`, modification times 1795445511500 and
  1795445514185 — moved from `5ae0c467…` by session 13's three commits (§2 item 2). Nothing is running; no dispatch is
  out.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only, untracked. **Untracked writing-side entries now: 1204 only**
  (1202 and 1203 were landed by session 13's commit `380b906f…`); session 14's instruction must land and read it.

## 2. What this sitting established

1. **Session 13's report read in FULL** (`records/cc/reports/cc_report_l3_application_session_13_task_3_stretch_4_2026_11_23.md`,
   18,392 bytes), and **session 13's instruction read whole** (41,931 bytes, unchanged since its landing). The claims of
   items 2 to 5 below checked at the git objects (inflated and SHA-1-verified over staged copies) and at the reading
   file, not taken from the report (the user's rule of 2026-09-03); item 6 names what was not checked.
2. **The three commits [checked]:** `380b906fbc323586aa2a7579d45bd52e5d68cc3a` (parent `5ae0c467…`) →
   `857b2fa64fe1f57cd0ee649f95885b3e81ffd9a0` → `d56ccc6ee74fa9a5327a5076cc97b33104ecb704`, each subject exactly as the
   instruction gives it (its lines 386, 367, 395). By tree comparison down to the changed folders: the first ADDS
   exactly three paths — the instruction (blob `2d831c3e…`), entry 1202 (`619d032e…`) and entry 1203 (`e85a87bb…`),
   each equal to the device copy as staged; the second changes ONE path, the reading file
   `ratification_surfaces/cowork_comparison_l3_reading.md`, blob `40675143…` →
   `5bccffae70dcdf713d25549aa7ef7bca4e09bf4a` (5,225,074 bytes, 84,114 lines, line feeds only), and the working-tree
   file is byte-identical to it; the third ADDS the report only (`484215ec…`), equal to the copy read.
3. **The reading file's diff [checked]**, old blob against new: 48 lines added (27 with text, 21 blank), 1 deleted; 26
   changed passages with three lines of context. Counts in the new blob: `*RULED DISPOSITION (` 271,
   `*RULED PLACEMENT (` 3, `*RECORDED DISPOSITION (` 53, `*LEAVES L3 (` 4, `*Row 7.67 is not transferred` 1. **Every
   line of the instruction's §3.2, §3.3 and §3.5 item 3** rebuilt by script from its backticked texts and row lists (27
   lines) and compared as a multiset with the added text lines: **equal**, none missing, none extra. Placement compared
   per distinct text (9 distinct texts across the 21 row lines): the set of row headings each text stands under equals
   the instruction's row set for it; each of the 21 row headings matches once; each row has one
   `*PROPOSED DISPOSITION.*` paragraph and no earlier `*RULED` or `*RECORDED` line before the new one; each new line
   stands paragraph, blank, **line**, blank, `---`. The five §10 lines each stand directly after the last line of the
   entry the instruction names (entries at lines 79797, 79821, 79827, 79839, 79920), all inside §10 (heading line 79581;
   §11 heading line 80646); nothing changed in §11. The one deleted line is the in-progress line, replaced at line 54 by
   the instruction's text.
4. **Row 7.67 [checked]:** its line (4343) is identical, character for character, to the text between the backticks of
   Ruling 5's line 187 in `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`.
   Its §10 line (79841) equals Ruling 5's line 192 with the line's two leading spaces set aside on both sides (the
   instruction's §3.3 gives the line its two-space indentation). The new blob carries 13 lines opening `*RULED` or
   `*RECORDED` with `**ADOPTED — carried** (L3-S` (number outside the bold) and 1 with the number inside (Row 7.67's), as
   Ruling 5 words it and as the user was told.
5. **The quotations [checked]:** every quotation in the 14 distinct added texts that name a record is found in its
   record (the edge-of-span, first-cut and second-cut records, staged and read by script: asterisks dropped, whitespace
   collapsed). A finding test, not a whole-line comparison; the one ruling giving a line word for word (Ruling 5) was
   compared whole (item 4).
6. **Not re-checked by this sitting:** the 675 added / 4 deleted against the Task 2 commit `4b6dc3bd…` [relayed]; the
   untracked-path list and the archive JSON's line-ending-only blob `1df4f207…` [relayed]; the decided-against search
   over the two records [relayed: no hit]; the §11 search for this stretch's row numbers beyond the fact that the diff
   touches no line of §11 [relayed: no hit]; the report's judgment that each row's outgoing statement fits its record.
7. **Claude Code's four declared departures (report §8), weighed, none acted on:** (1) the instruction read before its
   blob was taken, because the opening line required that read first; the committed blob equals the landed file; (2)
   two scratch scripts read working-tree files, against the file-tools rule; declared, and the result now stands proven
   at the git objects; (3) §L.22's eight lines written in file order; the instruction sets no order inside an entry; (4)
   an observation that one section of `cowork_audit_protocol.md`'s dispatch-protocol part (headed *"When a shell-read
   policy cannot decide, it DENIES"*) carries no standing-clause marker; not part of the plan, not acted on (the user's
   rule of 2026-08-25).
8. **Degradation tells (2026-08-15 list): none.** Not a tell: a first placement check compared each line text against
   every position it occurs at and gave false alarms where many rows carry the same text (the shape entry 1202 recorded);
   redone per distinct text before any result was used. Handed over before the instruction-writing on a capacity
   judgment stated to the user (the verification done here, against what §L.23's 82 lines and eight sources need), his
   word "yes". **On the model (2026-11-12):** nothing suggests Opus was not enough.

## 3. The plan — carried forward

1. **Next Cowork session: write session 14's instruction: §L.23 alone**, on the pattern of session 13's instruction.
   Its first-checks tip is `d56ccc6e…`; its Task 3 (f) diff base is session 13's Task 3 commit `857b2fa6…`; the reading
   file's expected blob is `5bccffae…` (counts 271 / 3 / 53, *LEAVES L3* 4, *Row 7.67 is not transferred* 1; against
   the Task 2 commit 675 added and 4 deleted [relayed]); its act 1 lands **entry 1204** (and that session's own entry,
   if written before the hand-over). Its content as entry 1203 §3 step 2 gives it: 82 lines; 35 rows of cuts 1 and 2
   with their cut records' placement words, 45 rows of cuts 3 to 8 with their cut surfaces' §3 words as the big
   dispatch's §L.23 table gives them, Rows 3.5 (ii) and 3.15 in form (b-H); its *LEAVES L3* lines naming the
   ratification record, beside session 13's beneath the same §10 entries, Row 10.206 excepted; its §11 additions for
   the nine QUARANTINED rows with their twins' audit questions. Size at the objects and split again at an entry
   boundary only if it must. **Wherever a ruling gives a line word for word, compare the whole line.** Its own authored
   labels checked against `CLAUDE.md`'s list of collided words before landing. Check it as its own turn; land on the
   user's word; then give the user the hand-over to Claude Code with the long opening line of 2026-10-26.
2. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1192 §3 step 3.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1203 §3, and: (a) the
three commits, their root trees and the trees down to the changed folders, and both reading-file blobs, were loose
objects under `.git/objects/` and could be staged by path; (b) a Python `difflib` comparison of the two reading-file
blobs ran for more than two minutes in the container and was moved to the background by the tool's time limit; `diff -U3`
over the two inflated blobs is fast; (c) entry 1205's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_five.md`; check by staging.

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** No dispatch is written; session 14's instruction is handed to
   Claude Code only by the session that writes and checks it.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_four.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1205 exists (if it does, report and ask), reads this entry whole,
   entry 1203 whole and entry 1026 §3, asks the session-start read, reads the three git reference files (anything but
   `d56ccc6e…` means something ran: find out what first), then does §3 step 1.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only searches and measurements over staged copies (`grep`, `cut`, `diff`, `cat` of a task
  output file in the container, `python3 -I` inflating git objects, computing blobs and comparing texts), with
  scripts, the reading file's two inflated blobs and the diff written to `/home/claude/scr` in the container; one
  `sed -i` edited this sitting's own script there. One script exceeded the tool's time limit, was moved to the
  background by the tool, and was waited for. Nothing written by any shell into a staged copy, the repository or the
  device.
- **Staged beyond the boot list:** the git reference files; `STATUS.md` and the gating JSON; session 13's report and
  instruction; the reading file; the loose git objects of the three commits and the old tip, their root trees and the
  trees down to the changed folders, and the reading file's two blobs; the part 2, edge-of-span, first-cut and
  second-cut records (by script). **Listed:** the repository root; `.git/objects/d5`, `85` and `38`.
- **This entry written in the outputs folder** with the Write tool and landed with the commit tool. No git on the
  device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1203. The user's words: the opening
instruction; "shortened"; "yes" (this entry and the hand-over).*
