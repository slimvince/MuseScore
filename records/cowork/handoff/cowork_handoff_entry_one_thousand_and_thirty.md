# Cowork handoff entry 1030 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 9, 10 AND 11 CHECKED (THE WORKING FILE'S LINES 1886–2098, §L.42 TO §L.40), FINDINGS 13 TO 15; THE CHECK FILE LANDED THREE TIMES AND PROVED; NO DISPATCH EDIT; SLICE 12 NEXT; HANDED OVER ON CAPACITY

**The current entry point.** Entry 1029 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 12 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1030 (staging answered *"does not exist"*, in a call of its own, after entry 1029 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1029 at
  10,289 bytes as staged; entry 1028 at 9,394; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 36,916, as entry 1029 says. Read whole: entries 1029, 1028, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1029 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "yes" each time):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), three landings:
    slice 9's section (39,373 bytes); slice 10's section (42,865 bytes); slice 11's section. Now **46,826** bytes,
    SHA-256 `961c629d…`. Each section stands after the previous section's provenance line and before slice 1's
    provenance line, which is still the file's last line; earlier sections untouched.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1029 §1 lists, plus entry 1030.

## 2. What this sitting established

1. **Slice 9 done: 4 rows, no finding.** The working file's lines 1886–1933 (§L.42) [checked: §L.42 read whole at
   dispatch lines 4434–4540]. Point (1)'s ADOPTED — proposed (item (3) of Ruling 9's paragraph, form (b), dispatch lines
   171–173) checked for coherence with §L.51's answered point (1) (lines 5440–5446): the same word by the same item.
   Point (4)'s two quotations of Ruling 1 identical at all five entries carrying them (lines 4151, 4273, 4396, 4510,
   4600), by search.
2. **Slice 10 done: 4 rows, two findings.** The working file's lines 1934–1981 (§L.41) [checked: §L.41 read whole at
   dispatch lines 4312–4433].
   - **Finding 13:** two dispatch-line citations written at release in §L.41 are stale: line 4400's *"(lines
     3544–3546)"* (now 4339–4341) and line 4340's *"(line 3863)"* (§L.44's Row 32.1, now 4661).
   - **Finding 14:** seen at §L.42 after slice 9 landed, not at a row: its 2026-11-09 check note (line 4486) says Row
     57.372 *"now stands at lines 1382, 1410 and 1433"*; it stands at 1788, 1816 and 1855, inside §L.17 (1740–1887).
     Finding 6's kind; finding 1's treatment proposed.
3. **Slice 11 done: 9 rows, one finding.** The working file's lines 1982–2098 (§L.40) [checked: §L.40 read whole at
   dispatch lines 4206–4311].
   - **Finding 15:** three dispatch-line citations written at release in §L.40 are stale: line 4277's *"(line 3461)"*
     (now 4230), line 4266's *"lines 3459–3460"* (now 4228–4229), line 4230's *"table line 3459"* (now 4228).
   - **Not a finding, for part 4:** batches 47 to 54 wrote such citations between §L entries and the rows did not
     record them as stale; how many stand in §L.39 to §L.1 and elsewhere is not established. A whole-dispatch search
     for dispatch-line citations may be cheaper in part 4 than finding them slice by slice; part 4's sitting judges.
   Proposed fixes for findings 13 to 15 stand in the check file, for part 4. All are documentation only; no algorithm
   change.
4. **Degradation tells: none noticed.** Every count written into a draft was taken by a command in the same turn.
   **Handed over on capacity**, judged out loud to the user after slice 11's landing: three slices and the boot read,
   and slice 12's dispatch section (131 lines) the largest so far.
5. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. No count was stated before it was
   counted this sitting; nothing this sitting met tests whether Fable would do better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 12,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2099 (*§L.39 check note, line 3428*) onward, the §L ledger rows, highest dispatch line first. Take as many
   as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results to
   the check file as a new section, after the last section's provenance line and before slice 1's provenance line (the
   file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge out
   loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1). **Then step 6**, as entry 1024
   §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1029 §3, and: (a) in the
dispatch at 874,206 bytes, §L.39 runs from line 4075 to 4205 and §L.38 from 3949 to 4074 (`### §L.` headings by
`grep -n`); §L.39's rows are 8, at the working file's lines 2099–2206 (by search for row openings), the first §L.38 row
at line 2207. (b) A search of an §L entry's range for *"line"* or *"lines"* followed by a four-digit number finds its
dispatch-line citations; slices 10 and 11 used it. (c) The Edit tool refuses a staged file read only earlier in the
sitting; read its end again just before the edit. (d) Entry 1031 is `cowork_handoff_entry_one_thousand_and_thirty_one.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1031 exists (if it does, report and ask). It reads **this entry whole**, **entry 1029 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (46,826 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 46,826, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `tr`, `wc`, `sha256sum`, `tail`, `sort`, `uniq`, `head`, `sleep`, `echo`, `printf`). Nothing written by any
  shell command, in the container or on the device; no shell deleted anything. The check file's sections made with the
  Edit tool; this entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted. Nothing listed.
- **Finding the files:** entries 1028, 767 and 584 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives.
- **Read beyond entry 1029 §4 step 3's list:** entry 584 whole; the working file at lines 1880–2098; the dispatch at
  lines 166–187, 4206–4540 and 5440–5452, its `### §L.` headings, and by search; `STATUS.md`, the gating JSON and
  `DECISIONS.md` as the session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-16 to 2026-11-17 (Stockholm), the sitting booted on entry 1029. The user's words: the
opening instruction; "shortened" (the session-start read); "yes" (slice 9's section); "yes" (slice 10's section); "yes"
(slice 11's section).*
