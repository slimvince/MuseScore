# Cowork handoff entry 1027 — 2026-11-16 — RELEASE STEP 5, PART 1: SLICES 4 AND 5 CHECKED (THE WORKING FILE'S LINES 1195–1554, §L.55 TO §L.48), FINDINGS 4 TO 7; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 6 NEXT; HANDED OVER ON ONE DEGRADATION TELL

**The current entry point.** Entry 1026 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 6 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1027 (staging answered *"does not exist"*, in a call of its own, after entry 1026 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1026 at
  11,103 bytes as staged; entry 1025 at 9,818; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 13,750, as entry 1026 says. Read whole: entries 1026, 1025, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Where the files are** (entry 1026 gives names, not folders): the check file and the working file in
  `C:\s\MS\ratification_surfaces\`; the dispatch in `C:\s\MS\records\cc\instructions\`.
- **Session-start read shortened:** the user's word was "continue", taken as the shortened read, as the two sittings
  before did, and said to him. `STATUS.md` whole (latest entry still the close of the second resume batch,
  2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247, `non_gating` 25); D-599 at
  `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1026 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "yes" each time):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 4's section (20,704 bytes); slice 5's section. Now **23,253** bytes, SHA-256 `17f53f2b…`. Each section
    stands after the previous section's provenance line and before slice 1's provenance line, which is still the
    file's last line; earlier sections untouched.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1026 §1 lists, plus entry 1027.

## 2. What this sitting established

1. **Slice 4 done: 26 rows, three findings.** The working file's lines 1195–1471 (§L.55 to §L.50), each row read whole
   and the dispatch at its site [checked]. All twenty-six applied or standing as quoted; rows 6, 8 and 17 carry
   finding 4.
   - **Finding 4:** three citations corrected at release (batches 18 and 22: §L.54's *"line 319"* and *"lines
     546–548"*, §L.52's *"line 328"*) are stale again; the passages now stand at lines 445, 695–697 and 453–454.
   - **Finding 5:** Task 3 (c) item 3 (dispatch lines 6638–6640) still treats §L.51's point (1) as open; Ruling 9
     answered it. No row checked so far holds that sentence.
   - **Finding 6:** older citations of 2026-11-09 in §L.52's and §L.50's notes are stale. Seen beside the rows, not
     by a whole-dispatch search; how many more the dispatch carries is not established.
   - Three noticed points recorded as not findings (§L.55's paraphrase of form (b)'s rule, left to part 5; Row
     4.17's double pointer, open to the user's overrule; §L.53's check note of 2026-11-09).
2. **Slice 5 done: 8 rows, one finding.** The working file's lines 1472–1554 (§L.49 and §L.48) [checked]. **Finding
   7:** §L.49's citations of §L.4's *"7.97"* (*"lines 496–497"*, batch 27) and of §L.6's Row 7.96 (*"line 640"*) are
   stale again; those passages now stand at lines 633–635 and 809–810.
   Proposed fixes for findings 4 to 7 stand in the check file, for part 4. All are documentation only; no algorithm change.
3. **One degradation tell, and the handover.** In slice 5's draft shown to the user, §L.48's note was cited as
   *"lines 5111–5113"* when only lines 5111 and 5112 had been printed (a claim wider than its check). Caught before
   landing; the landed text says *"from line 5111"*; told to the user. Under the user's rule of 2026-11-10 (hand over
   if any degradation tell has appeared), handed over at this verified stop.
4. **On the model.** `claude-opus-5-5`. The tell came after much dispatch reading in one sitting. Nothing this sitting
   met shows whether a different model would have done better or worse.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 6,** by a session that has edited none of the dispatch: the working file's rows from
   its line 1555 (*§L.47 check note, line 4153*) onward, the §L ledger rows, highest dispatch line first. Most are
   short. Take as many as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each
   slice's results to the check file as a new section, after the last section's provenance line and before slice 1's
   provenance line (the file's last line), the earlier sections untouched; show the addition before landing; land and
   prove it. Judge out loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1). **Then step 6**, as entry 1024
   §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1026 §3, and: (a) the
dispatch's `### §L.` headings by `grep -n` first, then each site by its quoted text within that entry's line range;
`awk 'NR>=a && NR<b && /…/'` keeps a search inside one entry. (b) Before citing a line range, print its first and last
lines; do not extend a range past what was printed. (c) Many §L notes carry line citations as the dispatch stood on
2026-11-09 or at a batch's landing; expect them stale (findings 4, 6 and 7) and record them at the rows that name them.
(d) Entry 1028 is `cowork_handoff_entry_one_thousand_and_twenty_eight.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_twenty_seven.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1028 exists (if it does, report and ask). It reads **this entry whole**, **entry 1026 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (23,253 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 23,253, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `wc`, `sha256sum`, `tail`, `sleep`). One print exceeded the tool's output limit; the tool, not the command,
  saved its start to a file in the container, which was not used. Nothing written by any shell command, in the
  container or on the device; no shell deleted anything. The check file's sections made with the Edit tool; this entry
  with the Write and Edit tools.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted.
- **Finding the files:** one staging at a wrong guess (`records\cowork\ratification_surfaces\`, *"does not exist"*);
  **listed** `C:\s\MS\records\cowork` and `C:\s\MS\records`; the site table
  (`ratification_surfaces/cowork_l3_application_release_site_table_2026_11_12.md`) staged by mistake for the working
  file and **not read**. Its size as staged, 751,491 bytes, differs from the 751,224 the working file's opening gives
  it; not looked into (outside this step).
- **Read beyond entry 1026 §4 step 3's list:** entry 584 whole; the working file at lines 1195–1580; the dispatch at
  lines 183–200, 319, 396, 440–445, 453–456, 633–635, 688–698, 1034, 1063, 1333–1377 (by search), 4942, 5186, 5304, 5207–5257 (in parts),
  5334–5362 (in parts), 5440–5463 (in parts), 5498–5504, 5540–5590, 5615–5690 (in parts), 5720–5760, 5761–5867,
  6633–6640, its `### §L.` and `## Task` headings, and by search; `STATUS.md`, the gating JSON and `DECISIONS.md` as
  the session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-16 (Stockholm), the sitting booted on entry 1026. The user's words: the opening
instruction; "continue" (taken as the shortened session-start read); "yes" (slice 4's section); "yes" (slice 5's
section).*
