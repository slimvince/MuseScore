# Cowork handoff entry 1031 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 12 AND 13 CHECKED (THE WORKING FILE'S LINES 2099–2301, §L.39 AND §L.38), FINDINGS 16 TO 18; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 14 NEXT; HANDED OVER ON ONE DEGRADATION TELL

**The current entry point.** Entry 1030 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 14 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1031 (staging answered *"does not exist"*, in a call of its own, after entry 1030 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1030 at
  10,438 bytes as staged; entry 1029 at 10,289; entry 767 at 10,922; entry 584 at 4,843; the working file at 573,300;
  the dispatch at 874,206; the check file at 46,826, as entry 1030 says. Read whole: entries 1030, 1029, 767 and 584,
  and the check file. The working file at its opening part (lines 1–64). The frozen copy and the findings section not
  read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1030 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "yes" each time):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 12's section (51,840 bytes); slice 13's section. Now **56,814** bytes, SHA-256 `61818f5f…`. Each section
    stands after the previous section's provenance line and before slice 1's provenance line, which is still the
    file's last line; earlier sections untouched.
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1030 §1 lists, plus entry 1031.

## 2. What this sitting established

1. **Slice 12 done: 8 rows, one finding.** The working file's lines 2099–2206 (§L.39) [checked: §L.39 read whole at
   dispatch lines 4075–4205].
   - **Finding 16:** all eleven dispatch-line citations written at release in §L.39 (batches 55, 57 and 58; four in
     the *Open* points, seven in the table's cells) are stale; where each now stands is in the check file.
   - **Not a finding:** the 2026-11-09 sentence *"the carry list itself still does not name it, so the point stands"*
     (line 4196), contradicted by point (4) as rewritten at release, records that day's check and stands.
2. **Slice 13 done: 9 rows, two findings.** The working file's lines 2207–2301 (§L.38) [checked: §L.38 read whole at
   dispatch lines 3949–4074].
   - **Finding 17:** all four dispatch-line citations written at release in §L.38 (batch 59, in the *Open* points) are
     stale.
   - **Finding 18:** §L.38's 2026-11-09 note (line 4010) says *"Row 46.1 (i) is placed at §L.30"*; §L.30's line for
     it (3133) reads *"No line from this record"*. *"46.1 (i)"* occurs at dispatch lines 3133, 3553 and 4010 only, and
     none gives it a line. Left **not established, for part 2:** whether a ruling record gives Row 46.1 (i) its line,
     or a general rule of the dispatch covers a row left waiting so; §L.30's other four waiting rows not checked.
   Proposed fixes for findings 16 to 18 stand in the check file, for part 4. All are documentation only; no algorithm
   change.
3. **One degradation tell, and the handover.** In slice 13's draft shown to the user, the *Carried* item was hedged
   (*"if it names §L.38's points"*) about line 20, which had not been read; it was read before landing (it names
   §L.38 points (1) to (3)), the item corrected, and the tell told to the user. Not in the landed text. Under the
   user's rule of 2026-11-10, handed over at this verified stop, slice 14 not begun.
4. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. This sitting's tell was a hedge
   about an unexamined thing, not a count stated before counting; nothing this sitting met tests whether Fable would
   do better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 14,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2302 (*§L.37 check note, line 3225*) onward, the §L ledger rows, highest dispatch line first. Take as many
   as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results to
   the check file as a new section, after the last section's provenance line and before slice 1's provenance line (the
   file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge out
   loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1), part 2 taking finding 18's
   open question with the other carried items. **Then step 6**, as entry 1024 §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1030 §3, and: (a) in the
dispatch at 874,206 bytes, §L.37 runs from line 3849 to 3948 and §L.36 from 3715 to 3848 (`### §L.` headings by
`grep -n`); §L.37's rows are 4, at the working file's lines 2302–2334 (by search for row openings), the first §L.36 row
at line 2335. (b) Before writing a *Carried* item about line 20, read line 20's sentence for that §L entry by search
(`grep -oE 'Left for the releasing sitting: §L\.NN[^.]*\.'`). (c) Count backtick spans and table pipes with `tr -cd`
and `wc -c`; check nesting by printing each span's opening. (d) Entry 1032 is
`cowork_handoff_entry_one_thousand_and_thirty_two.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty_one.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1032 exists (if it does, report and ask). It reads **this entry whole**, **entry 1030 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (56,814 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 56,814, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `tr`, `wc`, `sha256sum`, `tail`, `head`, `sleep`, `echo`, `printf`). Nothing written by any shell command, in
  the container or on the device; no shell deleted anything. The check file's sections made with the Edit tool; this
  entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted. Nothing listed.
- **Finding the files:** entries 1029, 767 and 584 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives.
- **Read beyond entry 1030 §4 step 3's list:** entry 584 whole; the working file at lines 2099–2301 and its row
  openings by search; the dispatch at lines 3949–4205, 3129, 3133, 3162–3167 and 3550–3558, line 20 and its `### §L.`
  headings by search, and by search for citations and row numbers; `STATUS.md`, the gating JSON and `DECISIONS.md` as
  the session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1030. The user's words: the opening
instruction; "shortened" (the session-start read); "yes" (slice 12's section); "yes" (slice 13's section).*
