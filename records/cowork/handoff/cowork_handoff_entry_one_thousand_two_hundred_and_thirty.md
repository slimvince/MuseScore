# Cowork handoff entry 1230 — 2026-11-24 — SESSION 23'S INSTRUCTION (§L.37 AND §L.38) CHECKED AT THE OBJECTS; THREE CORRECTIONS, NO LINE CHANGED, THE EXPECTED BLOB RE-DERIVED; LANDED; HANDED TO CLAUDE CODE

**The current entry point.** Entry 1229 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried

**A message to the user either asks him ONE question or hands over to another session — NEVER BOTH** (entry 1215 §0).
This sitting asked two questions, each in a message of its own (the session-start read; leave to run `python3 -I` in
the container), and hands over in a later message. **The user's two rulings of 2026-11-24** (entry 1221 §0, verbatim
there) stand and are carried forward unchanged.

**The user's leave of 2026-11-24 to this sitting, "yes":** to run `python3 -I` in the container, on staged copies
only, the script kept in a scratch folder outside the staged tree, writing nothing to the device. That leave was this
sitting's; a later sitting asks again before it needs a script.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1230 asked for by staging before any
  other boot read: *"does not exist"*. Entries 1229 (12,473 bytes) and 1221 (16,479) read whole; entry 1026 at §3 (the
  file 11,103).
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` whole (11,726 bytes, 1794136674043,
  unmoved); `DECISIONS.md` at the listing (120,603 bytes, 1794081137207, unmoved); the gating answer at
  `tools/audit/nongating_apparatus_rows.json` by search (`open_rows` 247 at lines 26 and 185, `non_gating` 25 at line
  49, `gating_ids` from line 186). `CLAUDE.md` came with the user's second message, whole.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `8beb212a03499965cef2e57c725c075c99193f2f`. Nothing has run since session 22.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **Session 23's instruction, CHECKED and corrected:**
    `records/cc/instructions/cc_instruction_l3_application_session_23_task_3_stretch_14_2026_11_24.md`, now **57,958
    bytes, 619 lines**, no carriage return, blob `2590317a437887c92f6f13f798c130aa71ae9ef1` (was 54,354 bytes, blob
    `eb238a30…`, as landed unchecked). Landed over the unchecked copy, guarded by its modification time; the landing's
    proof is in the closing message of this sitting. Untracked.
  - This entry (untracked).
- **Untracked writing-side entries: 1228, 1229 and 1230.** The instruction's §5 act 1 lands all three with it (Ruling
  1 (f)).

## 2. What this sitting established

1. **The check, as a turn of its own (Ruling 1 (e)), over staged copies [checked]:** the blobs of the big dispatch
   (`b5274c2c…`), the reading file (`720b5073…`, 5,314,921 bytes, 84,602 lines) and the instruction as landed
   (`eb238a30…`), each recomputed; both records whole; the release part 1 record at lines 137–244; the list-answers
   part 4 record at lines 1–72; the big dispatch at lines 159–258 and 3888–4113 and its headings; every quotation of
   the 17 lines found in its record; the reading file's ten counts, its headings and line 54; the 11 rows each found
   once inside §6, UNPLACED at the claim named, their outgoing statements fitting, their shapes as stated; the 21 §L.37
   rows each found once and UNPLACED; §10 (one hit, line 80730, Row 57.396 (i)) and §11 (none); the decided-against
   search over both records: none. The six settlements stand on precedents found at the reading file (the instruction's
   §8, last paragraph, names them).
2. **Re-simulated** by this sitting's own `python3 -I` script from the instruction's own text: 35 added and 1 deleted;
   counts 508 / 3 / 53 / 26 / 1 / 1; record names 17 / 0 / 28 / 7; no new line saying *as proposed*; **blob
   `aa5b2803720dea061fdf722ea9b765ceda781b31`** (5,320,637 bytes, 84,636 lines), as the writing side stated. Re-run
   after the corrections: the same blob.
3. **Three corrections, no line of §3.2 and no expected figure changed:** (1) §2 item 8's ranges of the release part 1
   record, which began after Ruling 4's and Ruling 5's headings, widened to lines 137–177 and 187–243; (2) §3.2's last
   paragraph, *"the rows its §4 names as read"*, narrowed to the other rows, Rows 24.4 and 24.6 named aside (they get
   lines); (3) §8's insertion point for Row 57.496, *"78868"*, to 78869, the blank line after its proposed paragraph —
   a slip in the provenance only, as the simulation places the line there and gives the stated blob. Entry 1230 added
   to §1 check 5, §2 item 4, §4 item 3 and §5 act 1 with its subject; the status banner and a check note (§8) added.
   Former wordings not kept, the instruction being unreleased.
4. **Degradation tells: none of the listed kinds.** Two shell commands were refused by the harness before running: a
   `git hash-object` over staged copies (blobs then recomputed with `sha1sum` over the `blob <size>\0` header, read
   only) and a `cp` of the instruction into the outputs folder, a write the opening instruction does not allow — the
   edits were then made with the Edit tool on the staged copy. **On the model (2026-11-12):** nothing here raises a
   suspicion about Opus.

## 3. The plan — carried forward

1. **Now: Claude Code executes session 23's instruction:** lands it and entries 1228, 1229 and 1230, applies §L.37 and
   §L.38, writes its report `records/cc/reports/cc_report_l3_application_session_23_task_3_stretch_14_2026_11_24.md`,
   stops.
2. **Then a NEW Cowork session verifies session 23's stretch and, under Rulings 1 and 2, writes the next stretch's
   instruction in the same sitting**, from §L.39 (entry 1229 §2 item 1's remarks on §L.39 are a reading of its table
   rows only, to be re-judged at the objects there). Its verification: the chain of commits, the tree changes, the
   reading file rebuilt independently from `720b5073…` and compared byte for byte with `aa5b2803…` and the file on
   disk, and the report read in FULL. It will need the user's leave for `python3 -I`.
3. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above and entry 1221 §0. **Practical notes, no rules:** as entries 908 and 910
to 1229 §3, and: (a) a git blob can be recomputed read-only as `{ printf 'blob %s\0' <size>; cat <file>; } | sha1sum`
over a staged copy; (b) a staged copy can be edited with the Edit tool after a fresh Read of it, sent with the
send-file tool, and committed by the identity the send returns; (c) entry 1231's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_thirty_one.md`; check by staging.

## 4. Who does what, in this order

1. **THE USER opens a NEW Claude Code session in `C:\s\MS` and gives it exactly this:**
   > Read and execute `records/cc/instructions/cc_instruction_l3_application_session_23_task_3_stretch_14_2026_11_24.md`. Your first tool call must be one read of that file and nothing else: no other file in that call, and nothing read in parallel with it. Then follow the order it gives.

   Wait until Claude Code reports that it has stopped (its last sentence: *"Session 23 of the L3 application ends
   here. Stretch 15 of Task 3 is not begun. Nothing else was done."*), or that it stopped at a STOP condition.
   **Do not** give it anything else, and do not start the Cowork session of step 2 before it has stopped.
2. **Then THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this**, together with Claude Code's closing message:
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_thirty.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1231 exists (if it does, report and ask), reads this entry whole,
   entry 1221 whole (the two rulings) and entry 1026 §3, asks the session-start read, reads the three git reference
   files (if Claude Code ran cleanly they no longer read `8beb212a…`: the new tip is session 23's report commit, found
   at the objects), then does §3 step 2. If Claude Code stopped at a STOP condition, it reports that to the user first
   and asks one question.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies (`grep`, `awk`, `sed -n`, `cut`, `tr`, `wc`, `diff`, `stat`,
  `sha1sum`), and, on the user's leave, one `python3 -I` script in a scratch folder outside the staged tree, writing
  its simulated copies there. Two commands refused by the harness and not run (§2 item 4). Nothing written by any
  shell into a staged copy, the outputs folder or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the three git reference files; session 23's
  instruction; session 22's instruction (staged, not read); the big dispatch; the two records; the release part 1
  record; the list-answers part 4 record; the reading file. **Listed:** the repository root. Path asked for by staging
  and found free: entry 1230.
- **Read beyond the boot list:** session 23's instruction whole; the records and ranges §2 item 1 names; the reading
  file at the rows, line 54, its headings, and by search.
- **The instruction edited in its staged copy with the Edit tool; this entry written in the outputs folder with the
  Write tool; both landed with the commit tool.** No git on the device, widget, task list, subagent, memory write or
  web access.

*Provenance: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1229. The user's words: the opening
instruction; "shortened"; "yes" (leave for `python3 -I`).*
