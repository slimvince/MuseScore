# Cowork handoff entry 1194 — 2026-11-23 — SESSION 9'S THREE COMMITS VERIFIED AT THE OBJECTS, ALL AS REPORTED; TASK 3 READ AND SIZED; SESSION 10'S INSTRUCTION (TASK 3, FIRST STRETCH) IS NOT YET WRITTEN; HANDED OVER ON CONTEXT LOAD, NO DEGRADATION TELL MET

**The current entry point.** Entry 1193 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1193 staged and read whole (8,057 bytes);
  entry 1194 asked for by staging in a call of its own, *"does not exist"*; entry 1026 read whole, its §3 included.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` read whole (11,726 bytes,
  1794136674043, unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207,
  unmoved; the gating answer 247 open, 222 gating, 25 non-gating, unchanged (`tools/audit/nongating_apparatus_rows.json`
  lines 183–185).
- **Git [checked]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and `refs/remotes/origin/master` both
  `905808a7a8b8b8f6e1b609273b19b0dc1a06f76f` (modification times 1795423950355 and 1795423957843, both before entry
  1193's 1795424305215). Nothing ran after entry 1193 was written. Nothing is running; no dispatch is out.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only (untracked). **Entries 1193 and 1194 are both untracked**; the
  session that writes session 10's instruction lands both with it (as session 9 landed 1191 and 1192).

## 2. What this sitting established

1. **Session 9's three commits verified at the git objects [checked]**, on the user's leave "A" (verification only:
   loose object files staged and decompressed by short `python3 -I` scripts in the container; each object's SHA-1 of
   its decompressed content equals its name). All of Claude Code's figures held:
   - The chain is linear: `839c6818…` (parent `0f26ac1b…`) → `4b6dc3bd…` → `905808a7…`.
   - Commit 1 `839c68182386e13d900f84c3911c7a430940e148` adds exactly three paths and changes nothing else in the tree:
     session 9's instruction (blob `ea91bc6a42610b05b8cbd0483593de74840f7214`), entry 1191
     (`df8ee45b8e701964d5772b8ddb31f11b6ccf53e8`) and entry 1192 (`82dd0cc513ee88202f62bbdc06294333c59dd4a2`).
   - Commit 2 `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774` changes exactly one path, the derivation, from blob
     `c01793f98c51e0267fb0dc7487613ac477cc1fbb` to `50a6ce97703502eb7d8161f4234aba170bfd9943`. Compared line by line:
     9 added, 0 removed, all after line 1 — a blank line and the eight-line banner naming blob `c01793f9…`.
   - Commit 3 `905808a7a8b8b8f6e1b609273b19b0dc1a06f76f` changes exactly two paths: session 9's report added (blob
     `963f0e4264c1b3ea43ab70bb2b8267624a96ce31`) and session 8's report changed (`02472b6e…` →
     `8765b628cb343580312f75f68e2dc0ebf1562eac`).
   - The six working-tree files, staged and hashed as git blobs, equal the committed blobs, byte for byte.
   - Not checked: the content of session 8's corrected line 166 beyond the blob equality (entry 1193 §2 item 3 read it
     in the working tree).
2. **Task 3 read whole** at the big dispatch's lines 6616–6820 [checked], and the split ruling
   (`records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`) read whole
   [checked]. Its Ruling 1 already settles the cut: *"Task 3 in stretches"*, each stretch *"sized, when its instruction
   is written, so that the session's whole reading stays well under half the window"*, Task 3 (e)'s one commit becoming
   *"one commit per stretch, each stopping at an entry boundary"*. No new ruling is needed for stretching.
3. **Sizing facts [checked unless marked]:**
   - The reading file: 5,135,614 bytes, 83,443 lines; §6 runs from line 433 to line 78,466 (§7 at 78,467); §10 at
     78,925, §11 at 79,980, §12 at 82,118, §13 at 83,178, §14 at 83,319, §15 at 83,429, §16 at 83,435. One row read
     (Row 8.24, lines 9100–9114): about 1 KB, 15 lines. `grep -c` gives 0 for `RULED DISPOSITION` and 0 for
     `RECORDED DISPOSITION` in the staged copy.
   - Row-parts per entry, where read: §L.2 (lines 446–529) — 74 rows given a line through the disposition-words record
     (23 + 7 + 35 + 9, the 35 listed in the disposition-word surface's §4, not in the dispatch), and Rows 19.39 (ii) and
     57.511 left to §L.48; §L.3 (530–630) — 21 rows, four of them with two lines; §L.4 (631–699) — 22 row entries (13
     DIFFERS and the cadence side of 9 carried rows); §L.5 (700–777) — 21 rows. §L.1 places no row.
   - A crude count of distinct row-number tokens in each entry's *Reading file* part gives 1,366 over §L.1–§L.55. It
     under-counts (§L.2 gives 41 against 74), because entries place families and rows listed on other surfaces. **The
     writing side's estimate, not a measurement: some 1,500 to 2,000 row-parts in all.**
   - §L.1–§L.55 span lines 431–5906; 54 paragraphs headed *"Rows named by more than one record"*, each the writing
     side's comparison *"as far as this entry's writer could see"*.
   - Side files the entries send Claude Code to, by size at the listing: the release part 2 ruling record
     (`…_2026_11_11_l3_application_release_part2_sitting.md`) 211,236 bytes; the release working list
     (`ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md`) 475,634; the release check
     (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`) 1,336,363; the disposition-words record
     3,694 and its surface (`ratification_surfaces/cowork_l3_disposition_word_surface_2026_11_08.md`) 12,557; the Part
     1a ruling record 13,326. **The three large ones cannot be read whole by a stretch session; the instruction must
     give line ranges for each ruling and list item a stretch's entries cite.** None located yet.
   - How Task 1 was actually cut (session 7's instruction §0 [checked]): §L.1–15, 16–25, 26–33, 34–40, 41–48, 49–55,
     then a check session of its own (session 8).
4. **The writing side's design proposals for the Task 3 instructions — authored, not ruled, each to be shown to the
   user with the instruction and overrulable:**
   1. **First stretch §L.1 to §L.4** (an estimate: about 120 row-parts at roughly 1,000 tokens each for locating,
      reading, checking and editing, plus the entries, their records and side reads, over the ordinary base). Session
      2's D-672 clause is kept: stop at an entry boundary on any degradation sign and commit what is applied. Later
      stretches are sized when their instructions are written.
   2. **The two-record rule across stretches.** A later stretch that finds a part already carrying an earlier stretch's
      line with a differing disposition word removes that line and gives the part neither, listing it STOP-and-report
      — the end state one session would reach. So Task 3 (f)'s check becomes two: every changed passage against the
      previous stretch's commit attributed, removals allowed only of such named lines; and against the Task 2 commit
      (`4b6dc3bd…`), no deleted line save those (d)'s state sentences are written into.
   3. **(d)'s four state sentences in the first stretch** (they are true at every stage); **§13's added sentence and
      §13a in the last stretch** (§13a is derived from every added line). Probably a check session at the end for the
      full E3, as session 8 was for Task 1.
   4. **(c) items 1, 5, 6 and 7 applied per stretch for its own entries**; item 6's *LEAVES L3* lines fall in the stretch
      holding §L.21 to §L.24, and the Row 7.67 line in the one holding §L.15.
5. **Degradation tells (2026-08-15 list): none met.** Handed over on context load (two large folder listings and much
   reading now carried) before the line-range work in the side files, on the user's "yes". **On the model
   (2026-11-12):** nothing met suggests the work exceeded Opus.

## 3. The plan — carried forward

1. **Next Cowork session: write session 10's instruction — Task 3, first stretch** — on the form of sessions 2 and 9's
   instructions (read them at the object), with §2 item 4's proposals. Before writing: read §L.1 to §L.4 whole (lines
   431–699), their four records whole, and locate at the objects, by line range, every other record, surface or list
   item those entries and Task 3's text cite for them (§2 item 3, side files). Re-check the stretch size against what
   that reading finds; narrow it if needed. Send the instruction whole; land it on the user's "yes"; prove it by
   staging back. Claude Code's act 1 lands the instruction with entries 1193 and 1194.
2. **Later:** the remaining stretches of Task 3, a check session if needed, then Tasks 4 and 5, each instruction
   written only when next. Entry 1193 §3 step 2 stands (the guard set's two reds of entry 1184 §2 item 2; Task 5's
   regeneration of `evidence_pin_membership.json`; Task 5's report pointing at every session report).
3. **Open with the user, not ruled:** as entry 1192 §3 step 3.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1193 §3, and: (a) loose
git objects can be read by staging `.git/objects/xx/…` and decompressing with `python3 -I` (zlib); a tree's entries are
`mode name\0` + 20 raw bytes. That needs the user's leave beyond searches. (b) A folder listing of
`records/cowork/rulings` or `ratification_surfaces` is large; stage known paths instead where possible. (c) Entry 1195's
file name would be `cowork_handoff_entry_one_thousand_one_hundred_and_ninety_five.md` (checked by staging: not present).

## 4. Who does what, in this order

1. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_one_hundred_and_ninety_four.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1195 exists (if it does, report and ask), reads this entry whole and
   entry 1026 §3, asks the session-start read, then does §3 step 1.
2. **Nothing goes to Claude Code from this entry.** The instruction for session 10 comes from the session that writes
   and checks it.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Shell uses beyond searches:** under leave "A", `python3 -I` scripts written to the container's scratch folder
  (`gitobj.py` with the Write and Edit tools; `blobdiff.py` by a shell here-document) to decompress, hash and compare
  git objects and staged files. **Beyond leave "A"**: one sizing script, `ledger_sizes.py`, written by a shell
  here-document and run over the staged big dispatch; and a `python3 -I -c` reading a saved folder listing. Read-only
  `grep`, `awk`, `sed`, `cut`, `head`, `wc` over staged copies. Nothing written by any shell into a staged copy, the
  repository or the device.
- **Staged beyond the boot list:** the git reference files; 23 loose git objects; the six working-tree files of §2
  item 1; the big dispatch; sessions 2, 7 and 9's instructions; the split ruling record; the reading file. **Listed:**
  the repository root, `records/cc/instructions` (saved to a file, read by script), `records/cowork/rulings`,
  `ratification_surfaces`.
- **This entry written in the outputs folder** and sent with the commit tool. No git on the device, widget, task list,
  subagent, memory write or web access.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1193. The user's words: the opening
instruction; "shortened"; "A" (the leave to verify session 9's commits at the objects); "yes" (this handover).*
