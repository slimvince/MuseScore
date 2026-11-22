# CC dispatch — the L3 application, SESSION 1 of several: Task 0 of the L3 application dispatch, and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_two.md`, on the user's ruling "C"
> (`records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`, Ruling 1). Executed by
> Claude Code when the user hands it over (D-252); the Cowork writing side never runs it. **If any expected result does
> not appear, stop at that step and report it. Do not continue to the next one.**

## 0. What this file is, and why it exists

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below), is 941,330 bytes and 7,157 lines. It cannot be read in one call. Its own reading order (its line 98)
requires reading roughly 750 KB of documents before Task 0, and its Tasks 1 and 3 each need roughly 1 MB of reading or
more (the writing side's estimates from file sizes). That is
more than one Claude Code session can hold together with the work. A previous Claude Code session stopped for that reason,
before doing anything. On the user's ruling, the big dispatch is now executed by **several NEW Claude Code sessions in
turn**. Each session gets a short instruction like this one, naming which part of the big dispatch it executes, what it
reads, and which of the big dispatch's orders it replaces.

**This is session 1. It executes the big dispatch's Task 0 (land the records and push), with Task 0's guard-set run, and
then STOPS.** It does not begin Task 1 or any later Task. Each later session is given its own instruction by the user,
written by a later Cowork sitting after this session's work has been verified.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §3,
and only for this session. Where this file and the big dispatch seem to differ on anything §3 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change.** This session commits files that already exist on disk. It writes no
specification text.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is the file this instruction was written against.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. (The writing side computed this from the file's 941,330 bytes, which
   contain no carriage return.) Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_1_task_0_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value, because a file cannot carry its own hash.

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **`CLAUDE.md`.** It is loaded whole into your context at session start as a project memory file. Do not read it
   again. If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
2. **`STATUS.md` whole. `DECISIONS.md` whole**, in ranges (it is about 120 KB; ranges of about 150 lines fit one read).
   **`BUILD_AND_TEST.md` in full** (this session runs the guard set). **The gating answer** at
   `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`; do not read the whole open-items index.
   This is the ordinary session-start read (Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_08_29_ratification_sitting.md`).
3. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (the dispatch-protocol clause on the read-first
   block), as the big dispatch's line 98 point (2) says. **Then two handoff entries, whole:**
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_three.md` (the current entry point,
   written by the sitting that wrote this file) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_two.md` (the one before it). Both are
   untracked; Task 0 lands them.
4. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***:
   every `###` section in it that carries the standing-clause marker, as the big dispatch's line 98 says.
5. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37 (the title, the release status, D-250's dated note, the writing side's restraint, the note on the
     earlier stop);
   - lines 59–97 (the head block: what the batch is and is not; the points sent back to the user; the start of the
     ordered first reads);
   - **line 98, with the shell, not the Read tool.** It is 4,352 characters long, and a file reader may cut a line that
     long. Use `sed -n '98p' records/cc/instructions/cc_instruction_l3_application_2026_11_08.md | fold -s -w 1000; echo "exit:$?"`.
     Read all of it. It is the reading order this file replaces, and you need to know what it said;
   - lines 99–394 (the words, the ruling ledger, the forms, the premise ledger with assumptions A1 to A5, the declared
     start state, the standing bars and the commit-and-push discipline, the findings rule);
   - lines 5907–6099 (Task 0, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:**
   - lines 38–58. They are the former draft banner and the construction-state table. Lines 43–44 say the table *"is not an
     instruction to Claude Code"*, and two of its lines are each more than 45,000 characters long;
   - lines 395–5906 (the ledger §L, used by Tasks 1, 3 and 4);
   - lines 6100–7110 (Tasks 1 to 5);
   - lines 7136 to the end (the writing side's self-check record).
6. **Not read in this session, although the big dispatch's line 98 orders them for the batch:** the fifty-five ruling
   records §L names; the derivation; the reading file; `decisions/group_K.md` D-674; `FRAMEWORK.md`;
   `cowork_derived_specification_l0_l1_2026_09_03.md`; `tools/audit/gen_status_batch_bound.py`;
   `records/cowork/handoff/cowork_away_returns.md`. Each is read by the later session whose Task uses it. Task 0 applies
   no ruling and edits no file, so reading them here would only use up context.

## 3. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Task 0 item 1** (the ruling records) → also lands
   `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (written by the
   sitting that wrote this file).
3. **Task 0 item 3** (the handoff entries) → the range is **586 to 1183** inclusive
   (`…five_hundred_and_eighty_six.md` to `…one_thousand_one_hundred_and_eighty_three.md`). Entry 1183 is the entry the
   sitting that wrote this file writes after this file lands and before hand-over.
4. **Task 0 item 4** (the dispatch) → also lands this file,
   `records/cc/instructions/cc_instruction_l3_application_session_1_task_0_2026_11_22.md`. Its expectation is UNTRACKED,
   like the rest of items 1 to 4.
5. **Act (3)'s commit subject** → exactly:
   `record: the L3 family records of 2026-11-08 and the family surfaces, the carry list, the application surface, the release records and surfaces of 2026-11-09 onward and entries 586 to 1183 landed with the L3 application dispatch and its session 1 instruction; the application act follows`
6. **The pin (standing clause P-2, at the end of Task 0)** → record BOTH blobs, the big dispatch's from §1 check 2 and
   this file's from §1 check 3, and immediately before staging the big dispatch for the commit, run §1 check 2 again. It
   must still print `b5274c2c7b82c171e1b44c1ed79635a34877b142`.
7. **Where the batch ends for this session.** After Task 0's acts (1) to (4), E0, and Task 0's guard-set acts (the full
   guard set run after act (4), its verdicts held to the declared start state's item 2, the membership movement measured
   before it is accepted), **this session STOPS.** It does not begin Task 1. E1 to E5, Tasks 1 to 5 and Task 5's close
   belong to later sessions.
8. **This session's report** (the big dispatch writes its one report at Task 5; until then, each session reports its
   own work). Write `records/cc/reports/cc_report_l3_application_session_1_task_0_2026_11_22.md` with the items of §4.
   Commit that ONE path alone, as a second commit after Task 0's commit and after the guard-set run, with exactly the
   subject `report: session 1 of the L3 application, Task 0 of the L3 application dispatch landed and its guard set run; Task 1 follows in a new session`.
   PUSH it to `origin` and verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md`
   entry; that belongs to Task 5.

## 4. What the report states, and the same in your closing message to the user

1. §1's three results, the two blobs, and the repeat of check 2 before staging.
2. Task 0's commit by its full hash, verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at it.
3. E0, item by item: every path of items 1 to 4 accounted for as landed, already tracked or absent; item 5's two paths
   each accounted for as landed, already committed or STOP-and-report; act (2)'s untracked paths listed in full.
4. The guard-set run: its verdicts set against the declared start state's item 2 (the thirteen failing tools, zero
   STOPs), any movement of `gen_evidence_pin_membership.py` with its measured cause, and every other red.
5. A1's check, as the premise ledger orders it.
6. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
7. The report commit by its full hash, and `origin/master` at it.
8. The last sentence, exactly: *"Session 1 of the L3 application ends here. Task 1 is not begun. Nothing else was done."*

## 5. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 1);
- the big dispatch's Task 0, its A1, its declared start state or its findings rule makes something a STOP;
- the guard-set run shows a red or a STOP outside the declared start state's item 2 and the one movement Task 0 allows;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §3 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1182. Read at the objects for this file: the
big dispatch at lines 1–158, 275–394, 5907–6099, 6100–6144, 6543–6546 and 6785–6788, its headings and line lengths by
read-only search; entries 1182, 1181 (by search) and 1026 §3; the ruling record of 2026-11-22 whole; the three git
reference files and the folder listings of the repository root, `.git` and the rulings folder; `CLAUDE.md`'s headings;
`cowork_audit_protocol.md`'s headings. The window of 1.0 million tokens, the 104.1k used at session start and
`CLAUDE.md` loaded as a memory file at 65.4k: from Claude Code's context display, which the user pasted. The user's
words: the opening instruction; "shortened"; "C"; the pasted context display.*
