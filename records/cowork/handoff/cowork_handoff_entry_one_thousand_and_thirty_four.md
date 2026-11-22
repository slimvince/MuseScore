# Cowork handoff entry 1034 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 18 AND 19 CHECKED (THE WORKING FILE'S LINES 2538–2608, §L.33 AND §L.32), FINDINGS 26 TO 29; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 20 NEXT; HANDED OVER ON CAPACITY

**The current entry point.** Entry 1033 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 20 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1034 (staging answered *"does not exist"*, in a call of its own, after entry 1033 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1033 at
  10,731 bytes as staged; entry 1032 at 10,605; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 78,822, as entry 1033 says. Read whole: entries 1033, 1032, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("Shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1033 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "Yes" each time):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 18's section (84,644 bytes, SHA-256 `284b5075…`); slice 19's section. Now **90,556** bytes, SHA-256
    `5513f57c…`. Each section stands after the previous section's provenance line and before slice 1's provenance line,
    which is still the file's last line; earlier sections untouched. The landed text differs from the text shown only
    in line breaks.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1033 §1 lists, plus entry 1034.

## 2. What this sitting established

1. **Slice 18 done: 4 rows, two findings.** The working file's lines 2538–2572 (§L.33) [checked: §L.33 read whole at
   dispatch lines 3411–3503].
   - **Finding 26:** the three dispatch-line citations written at release in §L.33 (lines 3472 and 3478) are stale;
     the table lines stand at 3435–3437.
   - **Finding 27:** finding 23's kind at §L.33's point (2) (lines 3478–3480): the list-answers record's lines 34–36
     and 106–109, the surface's sentence at its line 116 [checked: both printed at those lines].
   - Not a finding: point (1)'s *"the record's lines 38, 48 and 51"* holds at the further-rows record [checked: printed].
2. **Slice 19 done: 4 rows, two findings.** The working file's lines 2573–2608 (§L.32) [checked: §L.32 read whole at
   dispatch lines 3305–3410].
   - **Finding 28:** the three dispatch-line citations written at release in §L.32 (lines 3380 and 3386) are stale;
     the table lines stand at 3330–3332.
   - **Finding 29:** finding 23's kind at §L.32's point (2) (lines 3387–3388): the list-answers record's lines 34–36
     and 86–89, the surface's sentence at its line 111 [checked: both printed at those lines].
   - Not findings: point (1)'s *"that record's line 403"* (part 2 ruling record) and *"the record's lines 37 and
     45–49"* (recognition part 2 record) hold [checked: printed].
   Proposed fixes for findings 26 to 29 stand in the check file, for part 4. All are documentation only; no algorithm
   change.
3. **Handed over on capacity, at a verified stop.** After slice 19 landed, this sitting judged a third slice would not
   fit safely in what remained of its context. **Degradation tells: none noticed in the text shown to the user.** One
   departure from the leave, told to the user at once: a `cp -p` of the staged check file to `/dev/null`, run with the
   checksum before slice 18's landing; it wrote no file and changed nothing.
4. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. Nothing this sitting met tests
   whether Fable would do better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 20,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2609 (*§L.31 check note, line 2696*) onward, the §L ledger rows, highest dispatch line first. Take as many
   as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results to
   the check file as a new section, after the last section's provenance line and before slice 1's provenance line (the
   file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge out
   loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1), part 2 taking finding 18's
   open question with the other carried items. **Then step 6**, as entry 1024 §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1033 §3, and: (a) in the
dispatch at 874,206 bytes, §L.31 runs from line 3212 to 3304 (`### §L.` headings by `grep -n`); §L.31's rows are 4, at
the working file's lines 2609–2650 (by search for row openings), the first §L.30 row at line 2651. (b) Point (2) of
§L.35 to §L.32 carried the misplaced record-lines parenthesis (findings 23, 25, 27, 29); §L.31's table line quotes its
surface's §3.2 sentence by Ruling 1 of the list-answers part 2 ruling record [relayed: working-file lines 2570–2571
and 2606–2607]: read §L.31's point (2) and its table line for the same, and print the record and
the part 1 surface at the lines named. (c) The search for lines ending in *"line"* or *"lines"* caught a number broken
onto the next line at §L.32 (line 3387); keep running it. (d) Entry 1035 is
`cowork_handoff_entry_one_thousand_and_thirty_five.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty_four.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1035 exists (if it does, report and ask). It reads **this entry whole**, **entry 1033 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (90,556 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 90,556, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `tr`, `wc`, `sha256sum`, `tail`, `head`, `sleep`, `echo`), and one `cp -p` to `/dev/null` (§2 item 3).
  Nothing written to any file by any shell command, in the container or on the device; no shell deleted anything. The
  check file's sections made with the Edit tool; this entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s` was looked at as a names-only skeleton, and `C:\s\MS` requested and granted.
- **Finding the files:** entries 1032, 767 and 584 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives; the records and surfaces by the
  names the dispatch gives.
- **Read beyond entry 1033 §4 step 3's list:** entry 584 whole; the working file at lines 2538–2608 and its row
  openings by search (lines 2573–2720); the dispatch at lines 3305–3503, its `### §L.` headings for §L.31 to §L.34, line
  20's §L.33 mentions by search, and by search for citations; the list-answers part 2 ruling record at lines 32–37,
  84–91 and 104–111; the further-rows surface at lines 34–36, 106–109 and 114–117; the further-rows record at lines 38,
  48, 49 and 51; the recognition part 2 surface at lines 34–36, 86–89 and 109–112; the recognition part 2 record at
  lines 37 and 45–49; the part 2 ruling record at lines 401–405; `STATUS.md`, the gating JSON and `DECISIONS.md` as the
  session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1033. The user's words: the opening
instruction; "Shortened" (the session-start read); "Yes" (slice 18's section); "Yes" (slice 19's section).*
