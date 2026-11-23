# CC dispatch — the L3 application, SESSION 9 of several: Task 2 (the derivation's banner), one correction to session 8's report, and nothing else

> **STATUS: RELEASED 2026-11-23** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_two.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Sessions 2 to 7 applied Task 1, the successor file
`cowork_derived_specification_l3_2026_11_08.md`, in six stretches. Session 8 ran the full check of Task 1 (Task 1 (e)
and E1) and committed its report as `0f26ac1b9d40a45d6e473927b5b672122f2e5761`, the current tip.

**This is session 9. It does three things and STOPS:**

1. it lands the writing side's three untracked files (§5 act 1);
2. it executes the big dispatch's **Task 2** — one blockquote inserted at the head of the derivation
   `cowork_blind_derivation_l3_2026_10_17.md`, nothing else in that file (§5 act 2);
3. it corrects **one line** of session 8's report, keeping the former wording in place, and writes its own report
   (§5 act 3).

**Why the correction.** Session 8's report, in the paragraph headed *"Pairing differences outside the rows above"*,
says derivation line 1375 (a `---` line) was *"removed by session 2 hunk 40"*. The Cowork sitting that wrote handoff
entry 1192 checked this at the git objects (that entry's §2 item 6): in session 2's own diff, `git diff -U0` from the
derivation blob `c01793f98c51e0267fb0dc7487613ac477cc1fbb` to session 2's successor blob
`e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1`, line 1375 is removed in the changed passage `@@ -1375 +1424,3 @@`, which
is the 39th changed passage of that diff; the 40th is `@@ -1377,97 +1428,5 @@`. So the line should say *hunk 39*. The
error is in prose about a line that carries no text; no table row of the report is wrong. It is corrected under the
user's standing rule of 2026-09-22 (staleness and apparent errors in the record are fixed without asking him). You
confirm the two headers yourself before correcting anything (§5 act 3, step 1). *Authored by the writing side;
overrulable by the user.*

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §4,
and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change is decided by this session.** It places a banner the user ratified as
worded (Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_part_b_sitting.md`, as
the big dispatch's Task 2 records) and corrects one reference to a git diff passage. Neither changes what the
specification says the algorithm is.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `0f26ac1b9d40a45d6e473927b5b672122f2e5761`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_9_task_2_banner_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The derivation stands as the declared start tip has it.**
   `git ls-tree e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"`
   must show blob `c01793f98c51e0267fb0dc7487613ac477cc1fbb`, and
   `git hash-object cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"` must print the same blob. Anything else:
   STOP and report. (Task 2's own two checks before the edit follow in §5 act 2.)
5. **Session 8's report stands as session 8 committed it.**
   `git ls-tree 0f26ac1b9d40a45d6e473927b5b672122f2e5761 -- records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md; echo "exit:$?"`
   and `git hash-object records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md; echo "exit:$?"`
   must show the **same** blob, and it must begin `02472b6e` (the writing side holds only that prefix, from entry 1192).
   Record the full blob. Anything else: STOP and report.
6. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 0f26ac1b9d40a45d6e473927b5b672122f2e5761 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction, handoff entry 1191 and handoff
     entry 1192), plus the 393 untracked paths sessions 2 to 8 reported and did not land (387 under
     `scratch_artifacts/`; `Claude outputs/`; `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the
     two PDFs under `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`).
     `.claude/` and `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is
     expected and not a STOP. List in the report every untracked path the tool reports outside those. A further
     untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a
     STOP (the big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
3. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard.
4. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_two.md` (the current entry point;
   untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_one.md` (the one before it;
   untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole** (18,368 bytes), for the self-check after the work.
7. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger's opening, the forms, the premise ledger, the declared start state, the
     standing bars, the findings rule);
   - **lines 6572–6615 (Task 2, whole)**;
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 395–6571 (how §L is written, the ledger entries, Task 0 and
   Task 1, all already executed and checked); lines 6616–7110 (Tasks 3 to 5); lines 7136 to the end.
8. **The derivation at lines 1–6 only**, with the Read tool: `cowork_blind_derivation_l3_2026_10_17.md`. Do not read
   the rest of it.
9. **Session 8's report at lines 160–170 only**, with the Read tool:
   `records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md`. Do not read the rest of it.

## 3. The two texts this session places, given whole

**3.1 The banner (Task 2).** The big dispatch's lines 6593–6601 give it, with one placeholder at its end:
`` `<the blob, from git ls-tree>` ``. Take the blob from the `git ls-tree` of §1 check 4; it must be
`c01793f98c51e0267fb0dc7487613ac477cc1fbb`. With the placeholder filled, the big dispatch's last two banner lines (6600 and 6601) become one, and the eight lines are exactly:

```
> **★ THIS IS THE RECORD OF THE BLIND ACT, AND ITS BODY IS NOT REWRITTEN (D-674, branch one; the L3 route
> ruling of 2026-11-02, `records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md` §2 step 2).**
> Written 2026-10-17 by a fresh Cowork session with nothing mounted, under the brief `cowork_blind_session_brief_l3.md`
> (its own banner below); compared in `ratification_surfaces/cowork_comparison_l3_reading.md`; its statements and open
> questions dispositioned by the ruling records of 2026-11-02 to 2026-11-08 listed at
> `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` §L. **The derived L3 specification as amended
> by those rulings is `cowork_derived_specification_l3_2026_11_08.md`: the NEW file the route ruling's step 2 names.
> The amendments stand there, not here.** Everything below this banner stands as it was written at blob `c01793f98c51e0267fb0dc7487613ac477cc1fbb`.
```

Compare these eight lines with the big dispatch's lines 6593–6601 as you read them. **Apart from the filled
placeholder, which joins lines 6600 and 6601 into one, they must be identical**; if any other character differs, the big dispatch governs: STOP and report the
difference, and place nothing.

**3.2 The corrected line (session 8's report, its line 166).** The line now reads exactly:

```
(`---`, removed by session 2 hunk 40), which the full diff keeps — pairing difference, no text. With the six named in rows 1, 4
```

It becomes exactly:

```
(`---`, removed by session 2 hunk 39; was: "removed by session 2 hunk 40", an error found at the git objects by the Cowork sitting that wrote handoff entry 1192, its §2 item 6, and corrected under the user's rule of 2026-09-22 by `records/cc/instructions/cc_instruction_l3_application_session_9_task_2_banner_2026_11_23.md` §3.2), which the full diff keeps — pairing difference, no text. With the six named in rows 1, 4
```

Nothing else in that line or in the report changes. The dash after *"keeps"* is the existing em dash (U+2014); keep
it.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **A1, for three paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff
   entries 1191 and 1192 ARE landed**, with this file, in §5 act 1, as session 8 landed entry 1190. Any other
   untracked handoff entry or ruling record stays as A1 says.
3. **An added act, not in the big dispatch: the correction of §3.2.** A1 makes a modification at any tracked path a
   STOP-and-report unless a Task writes it. Session 8's report is not written by any Task; **this file adds it to the
   write set for this one line only**, after §5 act 3 step 1 has confirmed the two headers. *Authored by the writing
   side, under the user's rule of 2026-09-22; overrulable by the user.*
4. **The report Task 2's E2 belongs to** (the batch's report of Task 5, `records/cc/reports/cc_report_l3_application_2026_11_08.md`)
   → **this session's own report,
   `records/cc/reports/cc_report_l3_application_session_9_task_2_banner_2026_11_23.md`**, as sessions 2 to 8 each
   wrote theirs. Task 5's report, when its session writes it, points at this one. *Authored by the writing side, on the
   shape the eight session reports set; overrulable by the user.*
5. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin Task 3 or any later
   Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own.** Exactly three paths, all expected
   UNTRACKED: this file, `records/cc/instructions/cc_instruction_l3_application_session_9_task_2_banner_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_one.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_two.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1191 and 1192 and the session 9 instruction of the L3 application landed; Task 2 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.

2. **Task 2, as the big dispatch's lines 6581–6609 order it.**
   - **Before the edit**, the big dispatch's two checks, each must give exit 0:
     `git ls-files --error-unmatch -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"` and
     `git diff --quiet e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"`.
     Any other exit: STOP and report, the file not touched.
   - **The edit**, with the Edit tool. The file's lines 1–3 are the title line, a blank line, and
     `> **STATUS: DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED.**`. Insert the eight lines of §3.1 and then one
     blank line between the blank line 2 and that line 3. The file uses line feeds only, no carriage returns; keep it so.
     Touch nothing else.
   - **The check before the commit**, two commands:
     `git diff --numstat e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"`
     must print `9	0	cowork_blind_derivation_l3_2026_10_17.md` (nine lines added, none removed); and
     `git diff -U0 e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- cowork_blind_derivation_l3_2026_10_17.md > "<your scratchpad>/l3_session9_task2_diff.txt"; echo "exit:$?"`,
     read with the Read tool: **exactly ONE changed passage, at the file's head, insertions only.** Its header is
     `@@ -1,0 +2,9 @@` or `@@ -2,0 +3,9 @@` (git may pair the blank line either way; both mean the same insertion). Its
     nine added lines are the eight of §3.1 and one blank line. Anything else is a STOP-and-report, and the file is
     restored from the object: `git checkout e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"`.
   - **Commit** that ONE path alone, subject exactly (the big dispatch's line 6606):
     `application L3: the derivation re-bannered as the record of the blind act under D-674, body untouched`
     PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Record the new blob with
     `git ls-tree <the new tip> -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"`.

3. **The correction, then the report.**
   - **Step 1: confirm the two headers at the objects before changing anything.**
     `git diff -U0 c01793f98c51e0267fb0dc7487613ac477cc1fbb e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1 > "<your scratchpad>/l3_session2_diff.txt"; echo "exit:$?"`.
     Find every line beginning `@@` in that file with the Grep tool (line numbers on), and count them in order. **The
     39th must be `@@ -1375 +1424,3 @@` and the 40th must be `@@ -1377,97 +1428,5 @@`, and there must be 41 in all**
     (session 8's script counted 41 for session 2). Read the 39th passage's lines and confirm that the line it removes,
     `-` followed by the text, is `----` (the removal mark and the three dashes of `---`). If any of these does not hold:
     **do not correct the report**; write the report without the correction, state what you found, and say so in the
     closing message. This is not a STOP of the session.
   - **Step 2: the correction**, with the Edit tool: line 166 of session 8's report, from §3.2's first text to its
     second. Then `git diff --numstat 0f26ac1b9d40a45d6e473927b5b672122f2e5761 -- records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md; echo "exit:$?"`
     must print `1	1	` followed by the path, and
     `git diff -U0 0f26ac1b9d40a45d6e473927b5b672122f2e5761 -- records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md > "<your scratchpad>/l3_session9_correction_diff.txt"; echo "exit:$?"`,
     read with the Read tool, must show one changed passage `@@ -166 +166 @@`, its removed line §3.2's first text and its
     added line §3.2's second. Anything else: restore the file from the object
     (`git checkout 0f26ac1b9d40a45d6e473927b5b672122f2e5761 -- <that path>; echo "exit:$?"`), do not commit it, and
     say so in the report and the closing message.
   - **Step 3: the report.** Write
     `records/cc/reports/cc_report_l3_application_session_9_task_2_banner_2026_11_23.md` with the items of §6. Commit
     the report and the corrected session 8 report (TWO paths; ONE if step 1 or step 2 withheld the correction), subject
     exactly:
     `report: session 9 of the L3 application, Task 2 (the derivation's banner) done; one line of session 8's report corrected, its former wording kept; Task 3 follows in a new session`
     (if the correction was withheld, drop the words *"; one line of session 8's report corrected, its former wording
     kept"*). PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry;
     that belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's six results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. **E2, graded:** Task 2's two checks before the edit; the numstat and the one changed passage, its header and its nine
   lines; the derivation's new blob; `origin/master` at the commit.
4. **The correction:** step 1's 41 headers, the 39th and 40th as found, and the removed line; step 2's numstat and
   changed passage; or, if withheld, why.
5. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
6. The self-check after the work (`CLAUDE.md`, its last section), over the two changed files' diffs.
7. The last sentence, exactly: *"Session 9 of the L3 application ends here. Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the banner of §3.1 differs from the big dispatch's lines 6593–6601 by anything but the filled placeholder;
- either of Task 2's checks before the edit gives an exit other than 0, or the check before its commit does not show
  exactly the one insertion (the file restored first, §5 act 2);
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

A failed confirmation or a failed check of the correction (§5 act 3, steps 1 and 2) is NOT a stop of the session: the
correction is withheld and the report says so. After a STOP, report what you did and what you did not do. Do not try to
repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1192. Read at the objects for this file: the
three git reference files (both refs `0f26ac1b…`); the big dispatch at lines 316–327 and 6572–6615, and the headings
of lines 7100–7140; session 8's instruction at lines 1–146 and 362–522; session 8's report at lines 1–28 and 158–171,
its line 166 shown byte by byte; session 3's instruction at lines 158–171; the derivation at lines 1–6, with 1,501
lines and no carriage return; `records/cowork/handoff/cowork_handoff.md` at lines 248–262 (the topmost block ends at
line 255). Not computed by this sitting: any blob. The hashes in §1 and §5 are relayed from entry 1192 [checked there]
and session 8's report, and each is re-checked by Claude Code in §1 or §5 before it is relied on. Relayed, not
re-checked here: the size and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section, as session
8's instruction gives them. The user's words: the opening instruction; "Shortened".*
