# Cowork handoff entry 1033 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 16 AND 17 CHECKED (THE WORKING FILE'S LINES 2396–2537, §L.35 AND §L.34), FINDINGS 22 TO 25; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 18 NEXT; HANDED OVER ON CAPACITY

**The current entry point.** Entry 1032 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 18 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1033 (staging answered *"does not exist"*, in a call of its own, after entry 1032 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1032 at
  10,605 bytes as staged; entry 1031 at 10,167; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 66,165, as entry 1032 says. Read whole: entries 1032, 1031, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("Shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1032 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "Yes" each time):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 16's section (72,490 bytes, SHA-256 `7fa0f2a4…`); slice 17's section. Now **78,822** bytes, SHA-256
    `a48d353f…`. Each section stands after the previous section's provenance line and before slice 1's provenance line,
    which is still the file's last line; earlier sections untouched. The landed text differs from the text shown only
    in line breaks, and in the provenance word, written as the user gave it.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1032 §1 lists, plus entry 1033.

## 2. What this sitting established

1. **Slice 16 done: 6 rows, two findings.** The working file's lines 2396–2459 (§L.35) [checked: §L.35 read whole at
   dispatch lines 3617–3714].
   - **Finding 22:** the three dispatch-line citations written at release in §L.35 (lines 3671, 3677, 3689) are stale;
     the table lines stand at 3636–3638.
   - **Finding 23:** point (2)'s parenthesis *"(its record lines 34–36 and 150–153)"* (lines 3677–3679) stands after
     the surface's §3.2 sentence, so it reads as the surface's lines; they are the list-answers part 2 ruling record's,
     and the surface's sentence is at its line 131 [checked: both printed at those lines].
   - Row 5's double-backtick line (3638) matches the working list's lines 1306–1309 joined [checked by search].
2. **Slice 17 done: 7 rows, two findings.** The working file's lines 2460–2537 (§L.34) [checked: §L.34 read whole at
   dispatch lines 3504–3616].
   - **Finding 24:** the four dispatch-line citations written at release in §L.34 (lines 3565, 3572, 3580) are stale;
     the table lines stand at 3535–3538.
   - **Finding 25:** finding 23's kind at §L.34's point (2) (lines 3573–3574): record lines 34–36 and 128–132, the
     surface's sentence at its line 164 [checked: both printed at those lines].
   - Not a finding: point (4)'s *"that record's lines 1567–1581"* covers Ruling 29's bullets [checked: part 2 ruling
     record lines 1565–1582 printed].
   Proposed fixes for findings 22 to 25 stand in the check file, for part 4. All are documentation only; no algorithm
   change.
3. **Handed over on capacity, at a verified stop.** After slice 17 landed, this sitting judged a third slice would not
   fit in what remained of its context. **Degradation tells: none in the text shown to the user.** Caught before
   showing: one search claim wider than the search (it missed numbers broken onto the next line); the landed text rests
   the claim on the whole read and says what the search misses.
4. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. Nothing this sitting met tests
   whether Fable would do better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 18,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2538 (*§L.33 check note, line 2866*) onward, the §L ledger rows, highest dispatch line first. Take as many
   as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results to
   the check file as a new section, after the last section's provenance line and before slice 1's provenance line (the
   file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge out
   loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1), part 2 taking finding 18's
   open question with the other carried items. **Then step 6**, as entry 1024 §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1032 §3, and: (a) in the
dispatch at 874,206 bytes, §L.33 runs from line 3411 to 3503 and §L.32 from 3305 to 3410 (`### §L.` headings by
`grep -n`); §L.33's rows are 4, at the working file's lines 2538–2572 (by search for row openings), the first §L.32 row
at line 2573. (b) Point (2) of §L.35 and §L.34 carried the misplaced record-lines parenthesis (findings 23 and 25);
read §L.33's point (2) for the same, and print the record and the surface at the lines it names. (c) A search for
citations misses a number broken onto the next line: also search for lines ending in *"line"* or *"lines"*, and rest
the claim on the whole read. (d) Entry 1034 is `cowork_handoff_entry_one_thousand_and_thirty_four.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty_three.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1034 exists (if it does, report and ask). It reads **this entry whole**, **entry 1032 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (78,822 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 78,822, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `tr`, `wc`, `nl`, `cat`, `sha256sum`, `tail`, `head`, `sleep`, `echo`, `printf`, and `python3 -I` for two
  searches). Nothing written by any shell command, in the container or on the device; no shell deleted anything. The
  check file's sections made with the Edit tool; this entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted. Nothing listed.
- **Finding the files:** entries 1031, 767 and 584 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives.
- **Read beyond entry 1032 §4 step 3's list:** entry 584 whole; the working file at lines 2396–2537 and its row
  openings by search (lines 2460–2800); the dispatch at lines 3504–3714, line 20's §L.35 mentions by search, its
  `### §L.` headings for §L.32 to §L.36, and by search for citations; the working list at lines 1302–1312; the
  list-answers part 2 ruling record at lines 34–36, 126–133 and 150–153; the substitution part 2 surface at lines
  34–36, 129–132 and 150–153; the substitution part 1 surface at lines 34–36, 128–132 and 162–165; the part 2 ruling
  record at lines 1565–1582; `STATUS.md`, the gating JSON and `DECISIONS.md` as the session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1032. The user's words: the opening
instruction; "Shortened" (the session-start read); "Yes" (slice 16's section); "Yes" (slice 17's section).*
