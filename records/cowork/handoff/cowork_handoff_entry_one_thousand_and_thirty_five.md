# Cowork handoff entry 1035 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 20 AND 21 CHECKED (THE WORKING FILE'S LINES 2609–2680, §L.31 AND §L.30), FINDINGS 30 TO 32; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 22 NEXT; HANDED OVER ON CAPACITY

**The current entry point.** Entry 1034 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 22 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1035 (staging answered *"does not exist"*, in a call of its own, after entry 1034 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1034 at
  10,906 bytes as staged; entry 1033 at 10,731; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 90,556, as entry 1034 says. Read whole: entries 1034, 1033, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("Shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1034 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "Continue" each time, given after the question
  whether to land):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 20's section (96,788 bytes, SHA-256 `e97ca0bf…`); slice 21's section. Now **102,115** bytes, SHA-256
    `faff2ba9…`. Each section stands after the previous section's provenance line and before slice 1's provenance line,
    which is still the file's last line; earlier sections untouched. The landed text differs from the text shown in
    line breaks; in each provenance line, which carries the user's word as given; and, in slice 21, in one sentence:
    the text shown said *"the parenthesis of findings 23 to 31"*, which named a range wider than the five findings of
    that kind; the landed text reads *"findings 23, 25, 27, 29 and 31"*. That change was made before landing and not
    shown before it; it is declared to the user with this entry.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1034 §1 lists, plus entry 1035.

## 2. What this sitting established

1. **Slice 20 done: 4 rows, two findings.** The working file's lines 2609–2650 (§L.31) [checked: §L.31 read whole at
   dispatch lines 3212–3304].
   - **Finding 30:** the three dispatch-line citations written at release in §L.31 (lines 3272 and 3278) are stale;
     the table lines stand at 3233–3235.
   - **Finding 31:** finding 23's kind at §L.31's point (2) (lines 3279–3280): the list-answers record's lines 34–36
     and 67–71, the surface's sentence at its line 105 [checked: both printed at those lines].
   - Not findings: point (1)'s *"that record's line 403"* (part 2 ruling record) and *"the record's lines 37, 46 and
     47"* (recognition part 1 record) hold [checked: printed].
2. **Slice 21 done: 4 rows, one finding.** The working file's lines 2651–2680 (§L.30) [checked: §L.30 read whole at
   dispatch lines 3108–3211].
   - **Finding 32:** the two dispatch-line citations written at release in §L.30 (lines 3174 and 3183) are stale; the
     table lines stand at 3129, 3130 and 3132.
   - Not findings: *"that record's line 403"*, *"the record's lines 34 and 38–39"* (lead-rows record) and *"that
     record's lines 957–968"* (part 2 ruling record) hold [checked: printed]. Not checked: the reading file's lines
     61267–61270.
   - The misplaced record-lines parenthesis (findings 23, 25, 27, 29, 31) does not arise at §L.30: its point (2) rests
     on Ruling 19 of the part 2 ruling record and names *"that record"*.
   Proposed fixes for findings 30 to 32 stand in the check file, for part 4. All are documentation only; no algorithm
   change.
3. **Handed over on capacity, at a verified stop.** After slice 20 landed, this sitting judged out loud that one more
   slice fitted and said it would hand over after it. **Degradation tells:** one caught before landing (§1, the range
   *"findings 23 to 31"*, a claim wider than what it named), and one slip in a message to the user (*"line 1, 994"* for
   line 994), corrected to him in the next message. Two of the kind the user's rule of 2026-08-15 names were not seen.
4. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. Nothing this sitting met tests
   whether Fable would do better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 22,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2681 (*§L.29 check note, lines 2522–2525*) onward, the §L ledger rows, highest dispatch line first. Take as
   many as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results
   to the check file as a new section, after the last section's provenance line and before slice 1's provenance line
   (the file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge
   out loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1), part 2 taking finding 18's
   open question with the other carried items. **Then step 6**, as entry 1024 §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1034 §3, and: (a) in the
dispatch at 874,206 bytes, §L.29 runs from line 3001 to 3107 (`### §L.` headings by `grep -n`); §L.29's rows are 4, at
the working file's lines 2681–2732 (by search for row openings: 2681, 2690, 2700, 2721), the first §L.28 row at line
2733. §L.29 is the catalog key record's entry
(`records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_key_sitting.md`). (b) Keep running both citation
searches (a number of two to five digits after *"line"* or *"lines"*, and lines ending in *"line"* or *"lines"*), and
rest the claim on the whole read. (c) Before landing, compare the text to be landed with the text shown, and show any
change of wording in the same turn as the landing. (d) Entry 1036 is
`cowork_handoff_entry_one_thousand_and_thirty_six.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty_five.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1036 exists (if it does, report and ask). It reads **this entry whole**, **entry 1034 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (102,115 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 102,115, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `tr`, `wc`, `sha256sum`, `tail`, `sleep`, `echo`). One `awk` in a pipeline had its output sent to
  `/dev/null`, by a slip; it wrote no file. Nothing written to any file by any shell command, in the container or on the
  device; no shell deleted anything. The check file's sections made with the Edit tool; this entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted. Nothing listed.
- **Finding the files:** entries 1033, 767 and 584 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives; the records and surfaces by the
  names the dispatch gives.
- **Read beyond entry 1034 §4 step 3's list:** entry 584 whole; the working file at lines 2609–2680 and its row openings
  by search (lines 2651–2800); the dispatch at lines 3108–3304, its `### §L.` headings for §L.29 to §L.31, and by
  search for citations; the list-answers part 2 ruling record at lines 32–37 and 65–73; the recognition part 1 surface
  at lines 34–36, 67–71 and 103–107; the recognition part 1 record at lines 36–48; the part 2 ruling record at lines
  401–405 and 955–970; the lead-rows record at lines 33–40; `STATUS.md`, the gating JSON and `DECISIONS.md` as the
  session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1034. The user's words: the opening
instruction; "Shortened" (the session-start read); "Continue" (slice 20's section); "Continue" (slice 21's section).*
