# Cowork handoff entry 1036 — 2026-11-17 — RELEASE STEP 5, PART 1: SLICES 22 AND 23 CHECKED (THE WORKING FILE'S LINES 2681–2757, §L.29 AND §L.28), NO FINDING; THE CHECK FILE LANDED TWICE AND PROVED; NO DISPATCH EDIT; SLICE 24 NEXT; HANDED OVER ON CAPACITY

**The current entry point.** Entry 1035 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3, the release check, part 1 (the row check), continues. Next is slice 24 (§3 below). **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1036 (staging answered *"does not exist"*, in a call of its own, after entry 1035 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1035 at
  11,328 bytes as staged; entry 1034 at 10,906; entry 767 at 10,922; the working file at 573,300; the dispatch at
  874,206; the check file at 102,115, as entry 1035 says. Read whole: entries 1035, 1034 and 767, and the check file.
  The working file at its opening part (lines 1–64). Entry 584, the frozen copy and the findings section not read. The
  handoff folder not listed.
- **Session-start read shortened** on the user's word ("Shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no
  dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1035 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time and proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum of the copy sent, identical each time; each
  section's text sent to the user in full before landing, his word "Yes" each time, given after the question whether to
  land):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), two landings:
    slice 22's section (107,386 bytes, SHA-256 `01c86147…`); slice 23's section. Now **110,954** bytes, SHA-256
    `889e5997…`. Each section stands after the previous section's provenance line and before slice 1's provenance line,
    which is still the file's last line; earlier sections untouched. The landed text differs from the text shown only
    in line breaks and in each provenance line, which carries the user's word as given (slice 22's shown provenance
    line also lacked the clause *"given after the section was shown with the question whether to land it"*, which the
    landed line carries).
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED) and the working file (573,300 bytes).
- **Not in git:** as entry 1035 §1 lists, plus entry 1036.

## 2. What this sitting established

1. **Slice 22 done: 4 rows, no finding.** The working file's lines 2681–2732 (§L.29) [checked: §L.29 read whole at
   dispatch lines 3001–3107]. All four rows as applied. §L.29 carries no dispatch-line citation; its four record
   citations hold (the part 2 ruling record's lines 1259–1261, 1259–1271 and 1497–1508, and Ruling 24's citation of the
   L2 nothing-from-L3 record's lines 88–106) [checked: the record printed at lines 1255–1274 and 1493–1510; 88–106
   found at its lines 1237 and 1251 by search; the L2 record not read]. Not findings, recorded in the check file: the
   unedited *"Until (2) and (3) …"* sentence (Ruling 24 orders no edit; left to part 5's sweep for paraphrase), and
   §L.29's DP-O paragraph, which stays true of the catalog-key record.
2. **Slice 23 done: 3 rows, no finding.** The working file's lines 2733–2757 (§L.28) [checked: §L.28 read whole at
   dispatch lines 2915–3000]. All three rows as applied. §L.28 carries no dispatch-line citation; the part 2 ruling
   record's lines 400–403 hold [checked: printed at lines 398–405], and D-607 stands at `DECISIONS.md` line 514
   [checked by search]. The display ruling record's lines 57–60 and 60 (written 2026-11-08) were not checked.
3. **Handed over on capacity, at a verified stop.** After slice 22 landed, this sitting judged out loud that one more
   slice fitted and said it would hand over after it. **Degradation tells: none noticed** in the text shown to the user.
4. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. Nothing this sitting met tests
   whether Fable would do better.

## 3. The plan — carried forward

1. **Next: step 5, part 1, slice 24,** by a session that has edited none of the dispatch: the working file's rows from
   its line 2758 (*§L.27 check note, lines 2363–2365*) onward, the §L ledger rows, highest dispatch line first. Take as
   many as capacity allows and stop at a §L entry's boundary. Findings only, no dispatch edit. Add each slice's results
   to the check file as a new section, after the last section's provenance line and before slice 1's provenance line
   (the file's last line), the earlier sections untouched; show the addition before landing; land and prove it. Judge
   out loud after each landing whether another slice fits (the user's rule of 2026-11-10).
2. **Then parts 2 to 5 of the split** (the check file's opening; entry 1025 §2 item 1), part 2 taking finding 18's
   open question with the other carried items. **Then step 6**, as entry 1024 §3 step 2 gives it.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1035 §3, and: (a) in the
dispatch at 874,206 bytes, §L.27 runs from line 2785 to 2914 (`### §L.` headings by `grep -n`), 130 lines; §L.27's
rows are 5, at the working file's lines 2758–2818 (row openings by search: 2758, 2767, 2778, 2794, 2808), the first
§L.26 row at line 2819. §L.27 is the architecture-rules record's entry
(`records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md`); of its row
openings as printed (70 characters each), the one at line 2767 is headed as a staleness row and the one at line 2778
names L-1515's entry. (b) Keep running both citation searches (a number of two to five digits
after *"line"* or *"lines"*, and lines ending in *"line"* or *"lines"*), and rest the claim on the whole read. §L.29
and §L.28 carried no release-written dispatch-line citation; §L.41 to §L.30 each did, and every one the check file's
slices 10 to 21 found was stale. (c) Before landing,
compare the text to be landed with the text shown, and show any change of wording in the same turn as the landing.
(d) The Edit tool refused an edit to the staged check file until the file's end was read again with the Read tool,
though it had been read whole earlier in the sitting; read the insertion point just before each edit. (e) Entry 1037
is `cowork_handoff_entry_one_thousand_and_thirty_seven.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_thirty_six.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1037 exists (if it does, report and ask). It reads **this entry whole**, **entry 1035 whole**,
   **entry 767 whole** (10,922 bytes), the working file at **its opening part (lines 1–64)**, and **the check file
   whole** (110,954 bytes). It does **not** read the frozen copy or the findings section whole, and does not list the
   handoff folder for the boot. It proves this entry's size as the device reports it when staged, the working file at
   573,300, the dispatch at 874,206 and the check file at 110,954, and reads both ref files (anything but `e855ff2a…`
   means something ran: find out what first). It reports the boot with a capacity judgment, asks the session-start
   read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies (`cd`, `grep`, `sed -n`, `awk`,
  `cut`, `head`, `tail`, `wc`, `sha256sum`, `sleep`, `echo`). Nothing written to any file by any shell command, in the
  container or on the device; no shell deleted anything. The check file's sections made with the Edit tool; this entry
  with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted. Nothing listed.
- **Entry 584 not read.** §4 step 3 of entry 1035 says to boot as entry 584 §4 step 3 says; this sitting followed the
  boot list entry 1035 gives at that step and did not open entry 584. Said here, not to the user before now.
- **Finding the files:** entries 1034 and 767 staged by their spelled-out names, each found at the first try; the
  working file and the dispatch staged by the names the check file's opening gives; the part 2 ruling record by the
  name the dispatch gives.
- **Read beyond entry 1035 §4 step 3's list:** the working file at lines 2681–2757 and its row openings by search (lines
  2733–2900); the dispatch at lines 2915–3107, its `### §L.` headings for §L.25 to §L.35, and by search for citations;
  the part 2 ruling record at lines 398–405, 1255–1274 and 1493–1510, and by search for *"88–106"* and its Ruling 24
  and 25 headings; `DECISIONS.md` by search for D-607; `STATUS.md`, the gating JSON and `DECISIONS.md` as the
  session-start read.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity each send returned; this entry written in the outputs folder with the Write tool, sent,
  and committed by the identity the send returned.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1035. The user's words: the opening
instruction; "Shortened" (the session-start read); "Yes" (slice 22's section); "Yes" (slice 23's section).*
