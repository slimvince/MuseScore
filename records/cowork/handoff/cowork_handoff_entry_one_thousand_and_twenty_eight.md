# Cowork handoff entry 1028 — 2026-11-16 — RELEASE STEP 5, PART 1: SLICE 6 CHECKED (THE WORKING FILE'S LINES 1555–1710, §L.47 AND §L.46), FINDINGS 8 AND 9; THE CHECK FILE LANDED ONCE AND PROVED; NO DISPATCH EDIT; SLICE 7 NEXT; HANDED OVER ON TWO DEGRADATION TELLS

**The current entry point.** Entry 1027 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 7 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1028 (staging answered *"does not exist"*, in a call of its own, after entry 1027 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1027 at
  10,821 bytes as staged; entry 1026 at 11,103; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 23,253, as entry 1027 says. Read whole: entries 1027, 1026, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1027 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (the landing guarded by the device copy's modification time and proved by staging
  back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical; the section's text sent to
  the user in full before landing, his word "yes"):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), one landing:
    slice 6's section. Now **28,282** bytes, SHA-256 `ee9f9100…`. The section stands after slice 5's provenance line
    and before slice 1's provenance line, which is still the file's last line; earlier sections untouched.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1027 §1 lists, plus entry 1028.

## 2. What this sitting established

1. **Slice 6 done: 16 rows, two findings.** The working file's lines 1555–1710 (§L.47's seven rows and §L.46's nine),
   each row read whole and the dispatch at its site [checked: §L.47 read whole at dispatch lines 4961–5063, §L.46 at
   4840–4959]. All sixteen applied or standing as quoted.
   - **Finding 8:** citations corrected during the edits are stale again: §L.47's *"line 555"* and *"line 2124"*
     (dispatch line 4995; now lines 704 and 2611) and §L.46's *"line 319"* and *"lines 313 and 325"* (line 4898; now
     lines 445, 439 and 451). Finding 4's kind.
   - **Finding 9:** the table line for Row 40.12 (iv) (dispatch line 4869) is given in single backticks and holds
     single backticks of its own; proposed: double backticks, its text unchanged.
   - Carried, not checked: line 20's stale sentences for §L.47 and §L.46 (checked at the *Line 20* row, the working
     file's last); P2-R11's observation on where the report lists rows held by ruling (the working file's section
     *Not dispatch lines*), left for part 2.
   Proposed fixes for findings 8 and 9 stand in the check file, for part 4. Documentation only; no algorithm change.
2. **Two degradation tells, and the handover.** (a) §L.46's rows were said to the user to be ten before they were
   counted; counted, nine. (b) Slice 6's draft shown to the user ended *"fourteen rows as applied or standing as
   quoted"* against its own table of sixteen; corrected before landing under the user's rule of 2026-09-22 and told to
   him. Neither reached the landed text. Under the user's rule of 2026-11-10, handed over at this verified stop.
3. **On the model.** `claude-opus-5-5`. Both tells are counts stated loosely; they came early, not after long reading.
   Nothing this sitting met shows whether a different model would have done better or worse.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 7,** by a session that has edited none of the dispatch: the working file's rows from
   its line 1711 (*§L.45 check note, line 3959*) onward, the §L ledger rows, highest dispatch line first. Take as many
   as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results to
   the check file as a new section, after the last section's provenance line and before slice 1's provenance line (the
   file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge out
   loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1). **Then step 6**, as entry 1024
   §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1027 §3, and: (a) in the
dispatch at 874,206 bytes, §L.45 runs from line 4755 to 4839 and §L.44 from 4635 to 4754 (`### §L.` headings by
`grep -n`). (b) State a count only after counting it, in the message where it is first said and in a result line
against its own table. (c) The Edit tool refuses a staged file read only earlier in the sitting; read its end again
just before the edit. (d) Entry 1029 is `cowork_handoff_entry_one_thousand_and_twenty_nine.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_twenty_eight.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1029 exists (if it does, report and ask). It reads **this entry whole**, **entry 1027 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (28,282 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 28,282, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `cut`, `awk`, `head`,
  `wc`, `sha256sum`, `sleep`). Nothing written by any shell command, in the container or on the device; no shell
  deleted anything. The check file's section made with the Edit tool; this entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s` was listed once before the grant (names only), then `C:\s\MS` requested and granted.
- **Finding the files:** entries 1026, 767 and 584 staged by their spelled-out names, each found at the first try;
  the working file and the dispatch staged by the names the check file's opening gives. Nothing listed after the grant.
- **Read beyond entry 1027 §4 step 3's list:** entry 584 whole; the working file at lines 1555–1743; the dispatch at
  lines 4840–5063, its `### §L.` headings, and by search; `STATUS.md`, the gating JSON and `DECISIONS.md` as the
  session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity the send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-16 (Stockholm), the sitting booted on entry 1027. The user's words: the opening
instruction; "shortened" (the session-start read); "yes" (slice 6's section).*
