# Cowork handoff entry 1032 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 14 AND 15 CHECKED (THE WORKING FILE'S LINES 2302–2395, §L.37 AND §L.36), FINDINGS 19 TO 21; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 16 NEXT; HANDED OVER ON ONE DEGRADATION TELL

**The current entry point.** Entry 1031 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 16 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1032 (staging answered *"does not exist"*, in a call of its own, after entry 1031 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1031 at
  10,167 bytes as staged; entry 1030 at 10,438; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 56,814, as entry 1031 says. Read whole: entries 1031, 1030, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("Shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1031 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "Yes" each time):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 14's section (60,160 bytes); slice 15's section. Now **66,165** bytes, SHA-256 `bcc48c17…`. Each section
    stands after the previous section's provenance line and before slice 1's provenance line, which is still the
    file's last line; earlier sections untouched.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1031 §1 lists, plus entry 1032.

## 2. What this sitting established

1. **Slice 14 done: 4 rows, one finding.** The working file's lines 2302–2334 (§L.37) [checked: §L.37 read whole at
   dispatch lines 3849–3948].
   - **Finding 19:** the one dispatch-line citation written at release in §L.37 (batch 61, point (1)'s *"line 3174"*,
     line 3913) is stale; the table line stands at 3870.
2. **Slice 15 done: 7 rows, two findings.** The working file's lines 2335–2395 (§L.36) [checked: §L.36 read whole at
   dispatch lines 3715–3848].
   - **Finding 20:** all four places where batches 62 and 63 wrote four-digit dispatch-line citations in §L.36 (lines
     3796, 3803, 3810 and 3743) are stale; the table lines stand at 3739–3744.
   - **Finding 21:** §L.36 cites form (b)'s two-record sentence at *"lines 157–159"* twice: point (4), written at
     release by batch 62 (line 3817), and the 2026-11-09 check note (line 3830). It stands at lines 187–194 (the new
     sentence at 187–192, the former wording kept at 192–194). Whether 157–159 was right when batch 62 wrote it is not
     established.
   - **Not a finding, for part 4:** the search slices 10 to 15 used finds four-digit numbers only; three-digit
     dispatch-line citations (into the forms section and §L.1 to §L.10) were not searched for in slices 10 to 14. If
     part 4 runs a whole-dispatch citation search, it should take three-digit numbers too and read each hit.
   Proposed fixes for findings 19 to 21 stand in the check file, for part 4. All are documentation only; no algorithm
   change.
3. **One degradation tell, and the handover.** In slice 15's draft shown to the user, finding 21's bracket said
   *"lines 183–199 printed"*; the command had printed lines 182–199. Corrected to 182–199 before landing and told to
   the user; the landed text differs from the text he approved by that number only. Under the user's rule of
   2026-11-10, handed over at this verified stop, slice 16 not begun.
4. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. This sitting's tell was a figure
   written that did not match the command that produced it; nothing this sitting met tests whether Fable would do
   better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 16,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2396 (*§L.35 check note, line 3030*) onward, the §L ledger rows, highest dispatch line first. Take as many
   as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results to
   the check file as a new section, after the last section's provenance line and before slice 1's provenance line (the
   file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge out
   loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1), part 2 taking finding 18's
   open question with the other carried items. **Then step 6**, as entry 1024 §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1031 §3, and: (a) in the
dispatch at 874,206 bytes, §L.35 runs from line 3617 to 3714 and §L.34 from 3504 to 3616 (`### §L.` headings by
`grep -n`); §L.35's rows are 6, at the working file's lines 2396–2459 (by search for row openings), the first §L.34 row
at line 2460. (b) Search an §L entry's range for three-digit as well as four-digit numbers after *"line"* or
*"lines"*, and read each hit to tell dispatch lines from record, inventory and list lines. (c) Write a bracket's line
range from the command's own output, not from the command's arguments; when printing a range through a filter, print
the line numbers. (d) Entry 1033 is `cowork_handoff_entry_one_thousand_and_thirty_three.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty_two.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1033 exists (if it does, report and ask). It reads **this entry whole**, **entry 1031 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (66,165 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 66,165, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `tr`, `wc`, `sha256sum`, `tail`, `head`, `sleep`, `echo`). Nothing written by any shell command, in the
  container or on the device; no shell deleted anything. The check file's sections made with the Edit tool; this entry
  with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s` was looked at as a names-only skeleton, and `C:\s\MS` requested and granted.
- **Listed:** `records/cowork` once, without recursion, to find where the check file's folder stands (it is not under
  `records/cowork`; it was then staged at `ratification_surfaces/` from the repository root). Not listed: the handoff
  folder, the repository root.
- **Finding the files:** entries 1030, 767 and 584 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives.
- **Read beyond entry 1031 §4 step 3's list:** entry 584 whole; the working file at lines 2302–2395 and its row
  openings by search (lines 2335–2700); the dispatch at lines 3715–3948, lines 182–199 (printed through a filter),
  line 20's sentences for §L.37 and §L.36 by search, its `### §L.` headings for §L.33 to §L.38, and by search for
  citations; `STATUS.md`, the gating JSON and `DECISIONS.md` as the session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1031. The user's words: the opening
instruction; "Shortened" (the session-start read); "Yes" (slice 14's section); "Yes" (slice 15's section).*
