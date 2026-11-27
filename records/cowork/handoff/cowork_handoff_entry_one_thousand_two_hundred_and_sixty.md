# Cowork handoff entry 1260 — 2026-11-27 — SESSION 35'S INSTRUCTION (§L.51) CHECKED AT THE OBJECTS; NO FINDING IN THE STRETCH; ACT 1 CORRECTED TO LAND ENTRIES 1258, 1259 AND 1260; LANDED; FIVE NEW RULINGS OF THE USER ON READING LISTS AND STANDING FILES RECORDED; HANDED TO CLAUDE CODE

**The current entry point.** Entry 1259 is superseded as entry point and stands otherwise, except where §0 and §3
below change its plan. **[checked]** means read at the object by this sitting; **[relayed]** means not.

## 0. The user's rules in force, and his words to this sitting

**Carried unchanged:** entry 1259 §0 (the consolidated list, with Rulings A, B and C of 2026-11-27 at entry 1259 §2
item 5 and the settled practice at its §2 item 6), read whole by this sitting.

**His words to this sitting:** the opening instruction (entry 1259's §4 step 1 line); "shortened" (the session-start
read); "yes" (`python3 -I` in the container, on staged copies only, scripts outside the staged tree, nothing written to
the device by any shell); "Yes." (one shell copy of the corrected instruction into the outputs folder), with the five
rulings below; and his answer correcting ruling 1, below.

**The five rulings of 2026-11-27, given in this sitting** (his words: rulings given in the sitting booted on entry 1258
after it had landed entry 1259, and not in entry 1259). **All concern documentation and process only; no specification
text and no algorithm changes.** Where they conflict with entry 1259's plan, they govern for the acts they name. Order:
1 first, from stretch 27 on; then 2, then 3, then 4.

1. **Claude Code's reading list for a stretch, from the stretch 27 instruction (§L.52) on. AS CORRECTED by the user in
   this sitting** (his words: *"The word "only" in ruling 1 was a drafting error; the decision it records did not mean
   to drop these."*). Claude Code reads:
   - the instruction;
   - the §L entry or entries the stretch applies;
   - the ruling record or records the stretch's lines quote, read whole, with every quotation compared against the
     record before it is written, as now;
   - the big dispatch's forms section, only when the stretch brings a kind of line not met before;
   - the reading-file ranges the stretch touches;
   - its session-start read, under ruling 2: the instruction gives the sizes and modification times of `STATUS.md`,
     `DECISIONS.md` and the gating answer, and Claude Code reads a file in full only if it has changed;
   - `DEFECT_TYPES.md`, for the self-check after the work.

   Two items are dropped from its list only after a check: the topmost block of `cowork_handoff.md` (lines 1–255) and
   the dispatch-protocol section of `cowork_audit_protocol.md` (from line 180 to the end). The Cowork sitting that writes
   the stretch 27 instruction first checks which of their rules the stretches actually rely on, and carries any such rule
   into the instruction, before landing it. For these stretches this replaces the big dispatch's reading order (its line
   98). Also from stretch 27 on, as the writing side's own practice: each instruction's provenance section and check
   note move out of the file Claude Code reads, into the handoff entry or a file beside the instruction.

   *Original wording of ruling 1's first part, kept (#12):* "From the stretch 27 instruction (§L.52) on, Claude Code
   reads only: the instruction; the §L entry or entries the stretch applies; the big dispatch's forms section, but only
   when the stretch brings a kind of line not met before; the reading-file ranges the stretch touches."
2. **`STATUS.md`, `DECISIONS.md` and the gating answer during stretch work.** Each sitting compares each of the three
   files by size and modification time with the values recorded in the newest handoff entry; any change triggers a full
   read of that file. Every handoff entry records the values it found (this entry's: §1).
3. **One standing file of the rules and plan in force.** Updated in place, former wordings kept; a sitting that changes
   a rule updates the file in the same act. Handoff entries then carry only what the sitting established, its state and
   the next step. The user's words, the lists of files staged and the declared shell commands go to a log file beside
   each entry: kept, but not read by default. Entry 1259 §0 is the starting content. The file's name and the timing are
   proposed to the user (§3 item 6); not yet ruled.
4. **`CLAUDE.md`'s six session-start spans.** Each span's operative rules are split from their defences. The rules stay
   in `CLAUDE.md` and in the session-start read; the defences move, word for word, to a companion file read when a rule
   is challenged or its scope is unclear. A move, not a copy. The largest act; comes last; needs a dispatch Claude Code
   executes. Its timing is proposed to the user (§3 item 7); not yet ruled.
5. **Standing rule:** whenever a different kind of work from the present one (the L3 application's stretches) begins,
   revisit what the session-start read and the other standing reads need to contain for that work — whole documents,
   and parts of documents that could be left out or moved to separate files — and put it to the user as a decision
   surface before the new kind of work begins.

**Declined, for the record:** for (4), leaving `CLAUDE.md` as is, and making spans conditional on the kind of work; for
(2), reading as now, and leaving `STATUS.md` out entirely; for (1), leaving it as now, and a separate extract of the
protocol's rules; for (3), keeping the chained handoff entries.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1260 asked for by staging: *"does not
  exist"* (at boot and again before writing). Read whole: entries 1259, 1258 and 1257; the README of
  `tools/audit/stretch_verify/`; session 35's instruction.
- **Session-start read, shortened [checked]; the values ruling 2 asks for:**
  - `STATUS.md`: 11,726 bytes, modification time 1794136674043, read whole (latest entry still the close of 2026-11-08);
  - `DECISIONS.md`: 120,603 bytes, modification time 1794081137207 (at the listing);
  - the gating answer `tools/audit/nongating_apparatus_rows.json`: 178,066 bytes, modification time 1788814584416;
    `open_rows` 247 (lines 26 and 185), `non_gating` 25 (line 49), `gating_rows` 222 (line 183), `gating_ids` from
    line 186.
- **Also at the listing:** `records/cowork/handoff/cowork_handoff.md` 1,140,412 bytes, 1789629842494;
  `cowork_audit_protocol.md` 122,030 bytes, 1789979289703.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `89e107d35fc589f47da20cdf2821187a36e5014d`, unmoved.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **Session 35's instruction, CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_35_task_3_stretch_26_2026_11_27.md`, now **58,836
    bytes, 632 lines**, no carriage return, blob `131c80835a8fb2bc07fa9a4ec844ab6e4dde10ea` (was 53,720 bytes, 587
    lines, blob `f55588f5…`, as landed unchecked). Landed guarded by the device copy's modification time; **proved**:
    staged back and compared byte for byte with the copy sent (`cmp`), identical. Untracked.
  - This entry (untracked).
- **Untracked writing-side files for session 35's act 1:** the instruction and entries 1258, 1259 and 1260 — the four
  paths its §5 act 1 now names.

## 2. What this sitting established

1. **The check, as a turn of its own (Ruling 1 (e) as it stood), over staged copies [checked].** The objects, reads and
   results are in the instruction's check note at the end of its §8, which is the record of this check and is not
   repeated here. In short: every hash re-derived at the objects; the record, §L.51, form (b)'s step (3) and split-row
   sentence, Task 3 (c) items 3 and 7 read at their lines; both rows and the §11 blocks as the instruction states them;
   part C in the successor; every quotation found where stated; **re-simulated by this sitting's own placement script**
   (`place39.py`, kept in the container only): blob **`5809b5b9dd7b041d06c04ddda6be44c38184e9b2`**, every count and
   position as the instruction gives them; negative test DIFFERS; re-run on the corrected file, the same blob.
2. **No finding in the stretch.** Settlement (1) is consistent with earlier QUARANTINED lines that quote the twin's
   audit question under a label of their own (reading file line 4154 and others of the s38 ratification record);
   settlements (2) and (3) stand; none put to the user.
3. **Corrected, bookkeeping only (entry 1259 §3 step 1, under Ruling 1 (f)):** act 1 now lands entries 1258, 1259 and
   1260 — the banner (CHECKED), §1 check 6's expected untracked list, §2 item 4, §4 item 3, §5 act 1's path list, its
   count of paths, its `git show --stat` count and its commit subject. No line, count, position or expected figure
   changed. Former wordings not kept, the instruction being unreleased.
4. **Not re-read, under entry 1259 §2 item 6:** the established scripts (each equal to its committed blob, run
   unread); `cowork_handoff.md` and `cowork_audit_protocol.md` (their modification times predate the sittings that last
   read their bounds).
5. **Degradation tells: none met.** On the model (2026-11-12): nothing raises a suspicion about Opus.

## 3. The plan — carried forward

1. **Now: Claude Code executes session 35's instruction** (§4 step 1): lands the instruction and entries 1258, 1259 and
   1260 (act 1), applies §L.51 (act 2), writes
   `records/cc/reports/cc_report_l3_application_session_35_task_3_stretch_26_2026_11_27.md` (act 3), stops.
2. **Then a NEW Cowork session verifies stretch 26** (§4 step 2): the session-start read by ruling 2 against §1's
   values; the established scripts staged and run; its own placement script for the rebuild (this stretch is outside
   `rebuild.py`'s *Limits*; expected blob `5809b5b9…`); the report read in FULL; Ruling 1 (b) as narrowed.
3. **Then, in that sitting where capacity allows, judged out loud (Ruling 2 of 2026-11-24):** the `rebuild.py`
   extension and its establishment test (entry 1259 §2 item 6 (a)); and **stretch 27's instruction from §L.52**, by copy
   and change from session 35's checked instruction (Ruling B), with Ruling C's orders, and with ruling 1 above:
   - Claude Code's reading list as ruling 1 (corrected) gives it, replacing the big dispatch's line 98 for the stretch;
   - **before landing:** the check of which rules of `cowork_handoff.md`'s topmost block (lines 1–255) and of
     `cowork_audit_protocol.md`'s dispatch-protocol section (line 180 to the end) the stretches rely on, each such rule
     carried into the instruction; only then are the two dropped from the list;
   - the instruction gives the three files' sizes and modification times (ruling 2) for Claude Code's session-start
     read;
   - the provenance section and the check note kept outside the file Claude Code reads (in the handoff entry or a file
     beside the instruction).
   It lands the instruction unchecked on the user's word. **It does NOT tell the user to hand it to Claude Code.** If
   capacity does not allow, it hands over at a verified stop.
4. **From stretch 27 on (Ruling A):** the NEXT Cowork session makes the record comparison of the waiting instruction
   first, corrects what it finds, tells the user what to hand to Claude Code, waits, verifies the commit, and writes the
   next instruction.
5. **Ruling 2 from now on:** every handoff entry records the three files' sizes and modification times it found.
6. **Ruling 3 — proposed to the user, not ruled:** the standing file at
   `records/cowork/handoff/cowork_rules_and_plan_in_force.md`, its starting content entry 1259 §0 with this entry's §0;
   each entry's log beside it, named as the entry with `_log` before `.md`. **Timing proposed:** written by the sitting
   that makes the record comparison of the stretch 27 instruction (step 4), before it tells the user what to hand to
   Claude Code, so that stretch 27's act 1 lands it; from that sitting on, entries carry only what was established, the
   state and the next step. The sitting that reaches it puts the proposal to the user first if he has not ruled.
7. **Ruling 4 — timing proposed to the user, not ruled:** after the L3 application's Task 5 has closed and before the
   next kind of work begins, together with ruling 5's decision surface; so that `CLAUDE.md` is not changed between the
   stretches of a batch in progress.
8. **After the L3 application's Task 5 has closed:** as entry 1254 §3 step 3; and ruling 5's decision surface.
   **Carried:** as entry 1254 §3 step 4. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry
   1211 §3 step 2, and the duplicate of entry 1218 §2 item 5; and §3 items 6 and 7 above.

**Practical notes, no rules:** as entries 1258 and 1259 §3, and: (a) entry 1261's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_sixty_one.md`; check by staging; (b) the archive JSON on disk
carries carriage returns (its own blob `fb5249c1…`); `git hash-object` gives the committed `1df4f207…`, as session 35's
§1 check 6 says.

## 4. Who does what, in this order

1. **THE USER opens a NEW Claude Code session in `C:\s\MS` and gives it exactly this:**
   > Read and execute `records/cc/instructions/cc_instruction_l3_application_session_35_task_3_stretch_26_2026_11_27.md`. Your first tool call must be one read of that file and nothing else: no other file in that call, and nothing read in parallel with it. Then follow the order it gives.

   Wait until Claude Code reports that it has stopped (its last sentence: *"Session 35 of the L3 application ends
   here. Stretch 27 of Task 3 is not begun. Nothing else was done."*), or that it stopped at a STOP condition.
   **Do not** give it anything else, and do not start the Cowork session of step 2 before it has stopped.
2. **Then THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this**, together with Claude Code's closing message:
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_sixty.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   **No other Cowork session is open on this work at the same time.** That session checks by staging that entry 1261
   does not exist (if it does, report and ask); reads this entry whole, entry 1259 whole and session 35's instruction
   whole, and the README of `tools/audit/stretch_verify/`; makes the session-start read by ruling 2 against §1's values;
   reads the three git reference files (if Claude Code ran cleanly they no longer read `89e107d3…`: the new tip is
   session 35's report commit, found at the objects); asks the user's leave for `python3 -I`; then does §3 steps 2 and
   3. If Claude Code stopped at a STOP condition, it reports that to the user first and asks one question.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only reads and searches over staged copies (`cat`, `grep`, `sed -n`, `awk`, `cut`, `cmp`,
  `sha1sum`), a `mkdir` and a `cp` of the staged scripts into a scratch folder in the container, and, on the user's
  leave, `python3 -I -B` runs of the copied established scripts (`gitobj.py`, `blobhash.py`, `blobout.py`,
  `counts.py`; not read, per entry 1259 §2 item 6 (b)) and of this sitting's own `place39.py` (written with the Write
  tool in that scratch folder); `python3 -I -c` for the quotation, decided-against, §10/§11 checks, the listing filter
  and the negative test's changed copy (written outside the staged tree).
- **One shell copy, on the user's leave:** the corrected instruction from its staged path into the outputs folder,
  checked equal by `cmp`.
- **The instruction corrected with the Edit tool on its staged copy**, copied as above, landed with the commit tool
  (guarded by the device copy's modification time), the landing proved by staging back and comparing.
- This entry written in the outputs folder with the Write tool and landed with the commit tool, the landing proved by
  staging back and comparing. No git on the device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-27 (Stockholm), the sitting booted on entry 1259. The user's words as §0 gives them.*
