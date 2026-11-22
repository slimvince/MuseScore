# Cowork handoff entry 1183 — 2026-11-22 — CLAUDE CODE COULD NOT READ THE DISPATCH; ON THE USER'S RULING "C" THE RUN IS SPLIT INTO SEVERAL NEW CLAUDE CODE SESSIONS; SESSION 1 (TASK 0 ALONE) IS WRITTEN, LANDED AND GOES TO CLAUDE CODE

**The current entry point.** Entry 1182 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first; `C:\s\MS` connected. Entry 1183 checked by staging in a call of its
  own: *"does not exist"*. Entry 1182 read whole; entry 1026 §3 read.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (11,726 bytes, 1794136674043,
  unmoved); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207, unmoved, so the last full read stands; the
  gating answer at `tools/audit/nongating_apparatus_rows.json` (247 open, 25 non-gating); `CLAUDE.md` attached whole by
  the user's app.
- **Git [checked]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and `refs/remotes/origin/master` both
  `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`, modification times unmoved (1794137605021, 1794137607610); `.git/index` and
  `COMMIT_EDITMSG` at the commit's time (1794137605012); no `index.lock`. The stopped Claude Code session committed and
  pushed nothing.
- **The dispatch [checked]:** unchanged, 941,330 bytes, 7,157 lines, modification time 1795371843765, git blob
  `b5274c2c7b82c171e1b44c1ed79635a34877b142` (computed from the staged bytes).
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** three new files and nothing else — the ruling record
  `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`; the session 1
  instruction `records/cc/instructions/cc_instruction_l3_application_session_1_task_0_2026_11_22.md`; this entry. None
  is in git; session 1's Task 0 lands all three.

## 2. What this sitting established and did

1. **Claude Code's report** (pasted by the user) read in full as unverified: three read attempts, lines 1–40 read,
   nothing else done.
2. **What a reader that cannot hold the dispatch whole needs [checked]:** set out in the ruling record's §1. In short:
   the construction-state table (lines 38–58, about 100 KB, not an instruction) is in the way of reading from the top;
   the dispatch's own reading order (line 98) demands roughly 750 KB of whole reads before Task 0, so it cannot be
   followed in pieces without changing its text; the work divides by ledger entry; eleven lines are longer than 2,000
   characters.
3. **The decision surface** (A to D, each weighed towards the objective, the principles and its meta level;
   recommendation C), in its own turn; the user's word **"C"**. Recorded in the ruling record. Documentation only; no
   algorithm change.
4. **The context size [relayed, from Claude Code's context display pasted by the user]:** a window of 1.0 million
   tokens; 104.1k in use at session start; `CLAUDE.md` loaded whole as a memory file at 65.4k, which is about 2.6 bytes
   per token. So `CLAUDE.md` costs a session no read of its own.
5. **Session 1's instruction written**, shown whole to the user, landed on his word. It covers Task 0 alone, its
   guard-set run, a report of its own (`records/cc/reports/cc_report_l3_application_session_1_task_0_2026_11_22.md`,
   committed separately) and a stop. It adds the ruling record, entry 1183 and itself to Task 0's lists.
6. **A step the surface did not name, declared:** the per-session report file. The surface said each session commits
   and pushes its own work; a report file is how a later session (Task 5's) can read session 1's results at an object
   rather than through a relay. Shown to the user with the instruction.
7. **Degradation tells (2026-08-15 list):** none noticed.
8. **On the model (2026-11-12):** nothing this sitting met suggests the work exceeded the model.

## 3. The plan — carried forward

1. **Now: Claude Code session 1 runs** (§4). The writing side writes nothing into the repository while it runs.
2. **Next Cowork session, after session 1 reports:**
   1. read Claude Code's closing message and its report file in full as unverified, and verify at the objects: both
      commits by hash, `origin/master` at the report commit, Task 0's landed paths against items 1 to 5 as session 1's
      §3 amends them, act (2)'s untracked list, the guard-set verdicts against the declared start state's item 2;
   2. then write **session 2's instruction: the first stretch of Task 1.** Size the stretches at the objects when
      writing, from the sizes of each §L entry and its ruling record. The aim: each session's total reading (104.1k at
      start, plus its fixed reads, plus its Task text, plus the successor file, plus its entries and records) stays well
      under half of 1.0 million tokens. The writing side's estimate, not a measurement: Task 1 in about three stretches.
      Session 2's instruction must also:
      - replace Task 1's *"Before the edit"* check for the stretches after the first;
      - replace Task 1 (d)'s one commit with one commit per stretch;
      - name the declared start state as session 1's report commit;
      - read lines 2432, 4141, 4269, 4379 and 4700 (each longer than 2,000 characters) through the shell in pieces,
        where they fall in its stretch;
      - account for the untracked files the writing side adds between sessions, and for session 1's report file, in
        A1 and A5.
   3. Size it out loud first.
3. **Later:** Task 1's further stretches, Task 2, Task 3 in stretches, Task 4, Task 5. Each instruction is written only
   when it is next, after the previous session's work has been verified. A Cowork sitting verifies each finished Task
   before the next Task's first instruction goes out.
4. **Open with the user, not ruled:** as entry 1181 §3 step 3.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1182 §3, and: (a) the
dispatch is 941,330 bytes, 7,157 lines, blob `b5274c2c…`; while it stays unedited, its line numbers in this entry and
in session 1's instruction hold. (b) Entry 1184's file name would be
`cowork_handoff_entry_one_thousand_one_hundred_and_eighty_four.md`; check by staging. (c) The dispatch-protocol section
of `cowork_audit_protocol.md` runs from line 180 to the end (line 1605), about 100 KB.

## 4. Who does what, in this order

1. **THE USER now opens a NEW Claude Code session in `C:\s\MS`.** Not the session that stopped, and not the one used
   only to show the context size. He gives it exactly this:
   > Read and execute `records/cc/instructions/cc_instruction_l3_application_session_1_task_0_2026_11_22.md`. Your first tool call must be one read of that file and nothing else: no other file in that call, and nothing read in parallel with it. Then follow the order it gives.

   That instruction carries the commits and the PUSH to `origin` (its §3 items 7 and 8).
2. **While Claude Code runs, and after it ends:** no Cowork session writes anything into the repository. When the
   session ends with *"Session 1 of the L3 application ends here. Task 1 is not begun. Nothing else was done."*, or
   stops and reports, the user does **not** ask it to go on with Task 1 or to repair anything, whatever it offers.
3. **Then the user opens a NEW Cowork session** (with `C:\s\MS` added before the first message), and gives it Claude
   Code's closing message together with exactly this:
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_one_hundred_and_eighty_three.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1184 exists (if it does, report and ask), reads this entry whole and
   entry 1026 §3, asks the session-start read, then does §3 step 2.
4. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **The device-info call was made first**, before any other act of the sitting; only a tool-loading lookup (the
  device-info tool and the commit tool together) came before it.
- **The container shell, under the leave:** read-only `grep`, `sed -n`, `awk`, `wc`, `ls` on staged copies, and
  read-only `python3 -I` scripts given on standard input or by `-c` (section sizes, line lengths, the blob hash). Nothing
  written by any shell. No shell on the device.
- **Staged beyond the boot list:** the three git reference files; the dispatch; entry 1181; the ruling record of
  2026-11-22 (two uncommitted edits); `cowork_audit_protocol.md`; `records/cowork/handoff/cowork_handoff.md`;
  `CLAUDE.md`. Listed: the repository root, `.git`, the rulings folder. Staging checked that the two new files' names
  were free.
- **Read with the memory tool:** the project's note on dispatch-writing rules. No memory written.
- **The three files written in the session's outputs with the Write and Edit tools** and committed to the device
  with the commit tool, then staged back and read. No git, widget, task list, subagent or web access.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1182. The user's words: the opening instruction
with Claude Code's report; "shortened"; "C"; the pasted context display; "yes".*
