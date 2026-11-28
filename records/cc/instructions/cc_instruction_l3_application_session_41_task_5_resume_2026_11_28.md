# CC dispatch — the L3 application, SESSION 41: Task 5 of the L3 application dispatch RESUMED where session 40 stopped (the last regeneration, the away-returns section, the close commit, then the end-state guard run), keeping session 40's uncommitted close work, and nothing else

> **STATUS: WRITTEN 2026-11-28; THE RECORD COMPARISON MADE 2026-11-28.** Written by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_three.md`, whose handoff entry is
> 1284, on the user's ruling "1" of 2026-11-28 (handoff entry 1284 §0: keep session 40's uncommitted close work and
> resume). Landed unchecked, as session 40's instruction was under Ruling A of 2026-11-27 as the user extended it to
> Task 5 (that instruction's banner, line 5; entry 1280 §0 ruling 2). The record comparison was made by the Cowork
> sitting booted on `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_four.md`, whose
> handoff entry is **1285** (`records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_five.md`);
> its corrections are applied in §1 checks 4 and 6, §4 acts 2 and 6, and §5 items 5 and 6, and are listed in that
> entry. This file may now be handed to Claude Code. Executed by Claude Code when the user hands it over (D-252); the
> Cowork writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), was executed by Claude Code sessions 1 to 40.
Session 40 executed its Task 5 (the close) under
`records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md` (called **session 40's
instruction** below) and STOPPED at that instruction's §5 act 7 step 5. Its report,
`records/cc/reports/cc_report_l3_application_2026_11_08.md` (called **the batch report** below), records the stop in its
§0 and is committed alone as `a58acdb592e5005266555d7f8b1bd986a7a25b2e`, the current tip.

**Why it stopped.** `tools/audit/gen_per_session_reading.py` lists every `cowork_handoff_entry_*.md` under
`records/cowork/handoff/` on disk and STOPs on any of them that has no add-commit (its function `population_rows`).
Handoff entry 1283 was written into that folder by a Cowork sitting while session 40 ran. The fault is the writing
side's. Nothing session 40 did caused it.

**What session 40 left on disk, uncommitted, and this session KEEPS (the user's ruling "1"):** `STATUS.md`,
`STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`,
`tools/audit/evidence_pin_membership.json`, `tools/audit/session_start_read_size.json`,
`tools/audit/defense_share.json`, `tools/audit/l3_outgoing_population.json` and `tools/audit/per_session_reading.json`
— called **the nine kept files** below. Session 40's acts 3 to 6 made them; they are verified at §1 check 4 and are NOT
redone.

**This session does five things and STOPS:**

1. it verifies the nine kept files against what the batch report says (§1);
2. it lands the writing side's untracked files, so that the per-session tool can run (§4 act 1);
3. it re-checks session 40's act-6 artifacts at the tree the landing leaves, and adds its own section to the batch
   report (§4 acts 2 to 4);
4. it does session 40's instruction §5 act 7 steps 5 to 7 and act 8: the last regeneration, the away-returns section,
   the checks, and the close commit (§4 acts 5 to 8);
5. it does session 40's instruction §5 act 9: the end-state guard run and its commit (§4 act 9).

**The authority.** The big dispatch stays the authority for every order it gives, and session 40's instruction for every
order it gives for Task 5. This file replaces or adds to only the orders listed in §3, and only for this session. Where
this file, session 40's instruction and the big dispatch seem to differ on anything §3 does not list, STOP and report;
do not choose.

**Documentation and record-keeping only. No algorithm is decided by this session.** The method the specifications
define stays as decided. Nothing is ratified.

**ON ANY STOP IN THIS SESSION: restore nothing.** The nine kept files stay on disk as they are; the user's ruling keeps
them. Report the STOP and what stands on disk. *(This replaces session 40's instruction's restore-from-the-tip orders for
the acts this session repeats.)*

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section). A command whose output may be
long is redirected to a file in your session scratchpad and that file is read with the Read tool (the same section,
Rule 2).

0. **This file's banner.** If the banner above does not record that the record comparison has been made, STOP and
   report; do nothing else (the parked-instruction rule of `cowork_audit_protocol.md`, carried here as an order).
1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `a58acdb592e5005266555d7f8b1bd986a7a25b2e`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The two instructions are unchanged.**
   - `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
     `b5274c2c7b82c171e1b44c1ed79635a34877b142`.
   - `git hash-object records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md; echo "exit:$?"`
     must print `0bb3dca8a907656a8651d79cacf3d69fb1a3d210` (the pin the batch report's §1 check 3 records), and
     `git ls-tree a58acdb592e5005266555d7f8b1bd986a7a25b2e -- records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md; echo "exit:$?"`
     must show the same blob.
   Anything else: STOP and report.
3. **This instruction's own identity, and its pin.** You read this file from the working tree first, so the pin
   (`cowork_audit_protocol.md`, the standing clause P-2) takes its declared-departure route: declare in the report that
   the file was read before it was pinned; then
   `git hash-object -w records/cc/instructions/cc_instruction_l3_application_session_41_task_5_resume_2026_11_28.md; echo "exit:$?"`.
   Record the hash. There is no expected value. §4 act 1 proves the file unmoved against this hash before staging.
4. **The nine kept files are what the batch report says, and the other two inputs are untouched.** Each command in its
   own call, output to the scratchpad when long:
   - `git diff --quiet a58acdb592e5005266555d7f8b1bd986a7a25b2e -- records/cowork/handoff/cowork_away_returns.md tools/audit/guard_state.json records/cc/reports/cc_report_l3_application_2026_11_08.md; echo "exit:$?"`
     must give exit 0.
   - `git diff --numstat a58acdb592e5005266555d7f8b1bd986a7a25b2e -- <path>; echo "exit:$?"`, one call per path, must
     print exactly these added and deleted counts (the batch report's §4.2, §4.3 and §4.4):
     `tools/audit/gen_status_batch_bound.py` **35 5**; `tools/audit/evidence_pin_membership.json` **49 1**;
     `tools/audit/session_start_read_size.json` **8 8**; `tools/audit/defense_share.json` **1 1**;
     `tools/audit/l3_outgoing_population.json` **1 1**; `tools/audit/per_session_reading.json` **27 27**. *(The batch
     report's §4.2 and §4.3 give their commands against `a1938ebc…`; its §4.4 table heads the column "against the tip",
     and session 40's instruction §5 act 6 ordered that diff against `a1938ebc…`. The commits between `a1938ebc…` and
     `a58acdb…` are, as the batch report relays them, the landing commit `3f7c9faea4…` (five paths added, its §2) and
     the report commit (the report alone, its §0); if neither touches these six paths, the counts against `a58acdb…`
     are the same. The writing side could not establish this at the objects: these numstat runs are what establish it,
     and a count that differs is a STOP, as for any other.)*
   - For `STATUS.md`, `STATUS_ARCHIVE.md` and `tools/audit/status_batch_bound.json`, the numstat of each against
     `a58acdb…` is recorded with no expected value, and **`python tools/audit/gen_status_batch_bound.py --check; echo "exit:$?"`
     must give exit 0** (it re-derives the move from the base commit's object and reconciles it against both files).
   - With the Grep tool on `STATUS.md`, counting matching lines: the dated-entry pattern
     `^\*(Last updated: )?20\d\d-\d\d-\d\d` **8**; the fixed string `Same dispatch` **6**; `Last updated: ` **1**;
     `cc_instruction_llm_correction_second_resume_2026_11_08.md` **0**; a carriage return **0**. With the Grep tool on
     `STATUS_ARCHIVE.md`: the fixed string `★ RULING 4's FORWARD BOUND, 2026-11-28` **1**. *(The writing side took the five
     `STATUS.md` counts at its staged copy on 2026-11-28; the archive count is the batch report's §4.2.)*
   - `python tools/audit/gen_evidence_pin_membership.py --check; echo "exit:$?"` must give exit 0.
   Any result other than these: STOP and report. Nothing is touched.
5. **Keep a copy of the per-session artifact as session 40's act 6 left it, in git's object store:**
   `git hash-object -w tools/audit/per_session_reading.json; echo "exit:$?"`. Record the hash; it is called **the act-6
   blob** below. *(This replaces session 40's scratchpad copy made with `cp`, which a new session does not have and
   which the file-tools rule forbids.)*
6. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly the nine kept files**, plus `tools/audit/claude_md_finer_archive.json`,
     which differs from the tip only in line endings. Prove that one as session 40's instruction §1 check 5 does, with
     the tip `a58acdb592e5005266555d7f8b1bd986a7a25b2e` in place of `a1938ebc…`: `git hash-object` on it must print
     `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree a58acdb… -- <it>` must show the same blob. If both
     hold, it is not a modification and is not landed.
   - **Any other tracked modification of a file this session or session 40's instruction reads or writes: STOP and
     report.** Any other tracked modification is movement no act of this batch caused: report it and grade it, and go
     on; it is never staged (the standing clause P-3 of `cowork_audit_protocol.md`, carried here as an order).
     **One such path is foreseen:** `tools/audit/changed_paths_establishment.json` carries a modification time from
     inside session 40's run (1795856013532 at the writing side's listing of `tools/audit/`), and it is written only by
     `changed_paths.py --establish` (that tool, lines 311–320); session 40's report does not say that run was made. If
     it is listed as modified, it falls under the sentence before this one: report and grade it, go on, and never stage
     it. **Record the set of tracked modifications this check finds**; act 2 compares against it.
   - **Untracked paths expected:** the files §4 act 1 lands (this instruction; handoff entries 1283 and 1284, and the
     entry of the Cowork sitting that makes the record comparison, which this file's banner names), plus the paths
     sessions 2 to 40 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; `docs/research_papers/desktop.ini`;
     `docs/research_papers/rowe`; the two PDFs under `external resarch summary/`;
     `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
     `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md`, which is not
     landed, not touched, and not a STOP). List in the report every untracked path outside those.
   - **NEW, and a STOP: any other untracked file under `records/cowork/handoff/` or `records/cowork/rulings/`.** The
     per-session tool lists the first folder on disk and the membership tool the second, and either STOPs or turns red
     on a file with no commit. *(This replaces A1's sentence that a further untracked handoff entry or ruling record is
     not a STOP, for this session only.)*

## 2. What you read, in this order

The list replaces the big dispatch's line 98 and session 40's instruction §2 for this session, and with them the
read-first-block clause of `cowork_audit_protocol.md`: `cowork_handoff.md` and the protocol's dispatch-protocol section
are NOT read. The rules of theirs this session relies on are carried into this file as orders (§1 checks 0, 3 and 6;
§5 items 6 and 7).

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
3. **The session-start read, by size and modification time (ruling 2 of 2026-11-27).** List the repository root and
   `tools/audit/` with the file tools and compare each of these with the values below. A file whose size and
   modification time both equal its values is not read for the session-start read; a file where either differs is read
   in full (`DECISIONS.md` in ranges of about 150 lines; of the gating answer, only the list
   `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`). Report what you found for
   each. You may read the size and modification time with PowerShell `Get-Item`, as sessions 38 to 40 did; declare it.
   - `STATUS.md`: 12,041 bytes, modification time 1795856653795 (milliseconds since 1970; session 40's write) —
     read whole in any case (item 7);
   - `DECISIONS.md`: 120,603 bytes, modification time 1794081137207;
   - `tools/audit/nongating_apparatus_rows.json`: 178,066 bytes, modification time 1788814584416 (the writing side's
     value is relayed from handoff entry 1282 §1 and the batch report's §1; it did not list `tools/audit/`).
4. **Session 40's instruction, whole** (63,558 bytes, 685 lines). It is the authority for the acts this session repeats.
5. **The batch report, whole** (38,583 bytes).
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **`STATUS.md` whole** (30 lines).
8. **The last section of `records/cowork/handoff/cowork_away_returns.md`**, which the close appends after: lines
   **30753–30868** (the heading `# ═══ THE LANGUAGE-MODEL CORRECTION OF 2026-11-07, SECOND RESUME …` to the end of the
   file), as session 40's instruction §2 item 8 gives it. Read nothing else of that file.
9. **`tools/audit/gen_guard_state.py` at lines 35–36 only** (its two usage lines). `BUILD_AND_TEST.md` is not read
   (session 40's instruction §2 item 9 gives why).
10. **The big dispatch is NOT read** by the Read tool or searched. Its blob is checked at §1 check 2; every list the close
    needs from it was found by session 40 at that same blob and stands in the batch report's §5.1 to §5.3.

## 3. The orders of session 40's instruction this session replaces or adds to — the complete list

Nothing outside this list is replaced.

1. **Session 40's acts 1 to 6 are NOT repeated.** Their results stand in the batch report (§2 to §4) and on disk (§1
   check 4 verifies them). Session 40's act 2 (the start-state guard run, the batch report's §3) remains the start state
   that E5 is graded against.
2. **The landing.** §4 act 1 lands handoff entries 1283, 1284 and the record-comparison sitting's entry with this file.
3. **The handoff and rulings folders hold no untracked file from the landing to the close commit** (§1 check 6, and §4
   acts 2 and 5). *(The gap that stopped session 40; the writing side's error.)*
4. **The batch report is extended, not rewritten** (§4 act 4): a pointer line after its banner, and a new §10 at its end.
   Insertions only. Session 40's instruction §5 act 7 step 4 (*"the report is final when written"*) is replaced for this
   one extension, which is made BEFORE the last regeneration, so the report is still final before that regeneration
   runs.
5. **The last regeneration's diff is taken against the act-6 blob** (§1 check 5) instead of a scratchpad copy.
6. **The away-returns section's lists are taken from the batch report** (§4 act 6): the named-lists table from its §5.1,
   the *Register* list from its §5.2 and the *Open* pointer list from its §5.3, copied as they stand there. They are not
   searched again. *(The big dispatch is unchanged at its blob, so session 40's searches stand. Session 40's instruction
   orders these same lists into that section, so this adds no copy that order did not already make.)*
7. **The end-state check's added-path classes gain `tools/audit/stretch_verify/`** (§4 act 9). Its seven files were
   ordered landed by the writing side's own instruction for session 28
   (`records/cc/instructions/cc_instruction_l3_application_session_28_task_3_stretch_19_2026_11_24.md`, its item headed
   *Landing the measurement tool's seven files*, with their blobs listed below it). Session 40's instruction left the
   folder out of its class list, which is a stale list on the writing side; this fixes it under the user's rule of
   2026-09-22 on staleness. The batch report's §7 named the paths as a STOP-and-report; with this class added they are
   accounted for and are not a STOP. Report that.
8. **The closing sentence and the stop subject** name session 41 (§5 item 8).

## 4. The acts, in order

**NO FILE IS EDITED UNTIL ACT 1 HAS BEEN COMMITTED, PUSHED AND VERIFIED.** Until then, each is opened with the Read and
Grep tools only.

1. **Land the writing side's files first, in a commit of their own.** Exactly these paths, each UNTRACKED:
   - this file, `records/cc/instructions/cc_instruction_l3_application_session_41_task_5_resume_2026_11_28.md`;
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_three.md` (the sitting that
     planned the decision surface on the application approach, written while session 40 ran);
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_four.md` (the sitting that
     verified session 40's stop and wrote this file);
   - and the entry of the Cowork sitting that makes the record comparison, which this file's banner names.
   **Immediately before staging:** run §1 check 2 again; hash this file again and it must equal the hash §1 check 3
   recorded; and `git diff --quiet a58acdb592e5005266555d7f8b1bd986a7a25b2e -- records/cowork/handoff/cowork_away_returns.md tools/audit/guard_state.json records/cc/reports/cc_report_l3_application_2026_11_08.md; echo "exit:$?"`
   must give exit 0. Any of these failing: STOP and report, nothing staged. Stage the paths by name (never `git add` on
   a folder or with a pattern). The nine kept files are NOT staged. Subject exactly, with `<N>` the number of the entry
   the banner names:
   `record: handoff entries 1283 to <N> and the session 41 instruction of the L3 application landed; Task 5 resumes`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Then `git show --stat <the new tip>;
   echo "exit:$?"` must show exactly the paths above added, and nothing else. This commit is called **this session's
   landing commit** below.

2. **No untracked file in the two folders.** Run `tools/audit/changed_paths.py` again, as §1 check 6. It must list no
   untracked path under `records/cowork/handoff/` or `records/cowork/rulings/`, and the tracked modifications must be
   exactly the set §1 check 6 recorded (the nine kept files, the line-ending file, and any movement graded there),
   with nothing added. Otherwise: STOP and report.

3. **Session 40's act-6 artifacts, re-checked at the tree the landing left.** For
   `tools/audit/gen_session_start_read_size.py`, `tools/audit/gen_defense_share.py` and
   `tools/audit/gen_l3_outgoing_population.py`, in that order: `--check` in its own call, result recorded.
   - **Exit 0:** nothing more for that tool.
   - **Exit 1 (red):** the writing run (`python <tool>; echo "exit:$?"`), then `--check` again, which must give exit 0;
     then `git diff a58acdb592e5005266555d7f8b1bd986a7a25b2e -- <artifact>` to the scratchpad, read with the Read tool,
     with the movement reported **by field**, compared with session 40's movement in the batch report's §4.4. **A
     movement beyond session 40's is admitted only where every further moved field is caused by a path this session's
     landing commit added**; name the path for each. Anything else: STOP and report.
   - **A tool that STOPs (exit 2), or a second `--check` that fails: STOP and report.**
   `tools/audit/gen_per_session_reading.py` is NOT run here; it runs at act 5, after the report extension.

4. **Extend the batch report** `records/cc/reports/cc_report_l3_application_2026_11_08.md`, with the Edit tool,
   insertions only:
   - **after the banner's last line (its line 5)**, one blank line and then exactly this one line (the line between
     the fences, not the fences):
     ```
     > **★ RESUMED BY SESSION 41 (2026-11-28), under `records/cc/instructions/cc_instruction_l3_application_session_41_task_5_resume_2026_11_28.md`, keeping the uncommitted work §0 lists; see §10.**
     ```
   - **at the end of the file**, after one blank line, a new section headed `## 10. Session 41 — Task 5 resumed`,
     carrying the items of §5 items 1 to 6 below.
   Then `git diff --numstat a58acdb592e5005266555d7f8b1bd986a7a25b2e -- records/cc/reports/cc_report_l3_application_2026_11_08.md; echo "exit:$?"`
   must show **0 deleted lines**. Otherwise: STOP and report, nothing committed. The report is final after this act.

5. **The last regeneration** — session 40's instruction §5 act 7 step 5, with these changes. Immediately before it,
   run `tools/audit/changed_paths.py` again as act 2 and confirm no untracked path under the two folders (otherwise STOP
   and report, nothing committed). Then `python tools/audit/gen_per_session_reading.py --check; echo "exit:$?"`: **red
   expected (exit 1)**, because this session's landing commit and the committed report changed what it counts. **Exit 2
   (a STOP): STOP and report, nothing committed.** Then the writing run; then `--check` again, which must give exit 0.
   Then `git hash-object -w tools/audit/per_session_reading.json; echo "exit:$?"` and
   `git diff <the act-6 blob> <that hash> > "<your scratchpad>/l3_session41_per_session_diff.txt"; echo "exit:$?"`, read
   with the Read tool, and the movement reported **by field** in the away-returns section.

6. **Append the away-returns section** — session 40's instruction §5 act 7 step 6, whole, with its heading exactly as
   given there, and with these changes:
   - **the start-state guard run:** session 40's act 2, as the batch report's §3 records it;
   - **every commit hash:** the output of
     `git log --reverse --format="%H %ci %s" e855ff2a38883bc453b3f1c83cb20b9fd89cda05..<this session's landing commit> > "<your scratchpad>/l3_session41_log.txt"; echo "exit:$?"`,
     read with the Read tool, whole, as a list;
   - **E0 to E5 and each task's diff, as POINTERS:** as the batch report's §5 grades and locates them; E5 graded *"NOT
     ASSERTED HERE — the one further commit carries it"*;
   - **the named lists, the *Register* list and the *Open* pointer list:** copied from the batch report's §5.1, §5.2 and
     §5.3 as they stand (§3 item 6), with the two sentences session 40's instruction gives for them;
   - **the declared departures:** session 40's (the batch report's §8), this session's up to act 4 (the batch report's
     §10), every departure this session makes after act 4 (declared here, in this section, because §10 is final after
     act 4), and a pointer to each session report's *Departures* section, as the batch report's §5 locates them;
   - **the last regeneration:** act 5's movement by field;
   - **the plan's tell:** the batch report's §7 sentence, with the added sentence that the seven
     `tools/audit/stretch_verify/` files were ordered landed by the session 28 instruction (§3 item 7);
   - **the stop and the resumption, in one sentence each:** session 40 stopped at act 7 step 5 because a handoff entry
     was written into `records/cowork/handoff/` during it (the batch report's §0); this session resumed on the user's
     ruling "1" (handoff entry 1284 §0), keeping the work session 40 left on disk;
   - the provenance line: Claude Code, the date, session 40's boot tip `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e` and
     this session's boot tip `a58acdb592e5005266555d7f8b1bd986a7a25b2e`, session 40's instruction and this one.

7. **The checks before the close commit** — session 40's instruction §5 act 7 step 7, with the tip `a58acdb…` in place
   of `a1938ebc…` in its numstat command: each of the six `--check` runs it names must give exit 0, and
   `git diff --numstat a58acdb592e5005266555d7f8b1bd986a7a25b2e -- records/cowork/handoff/cowork_away_returns.md; echo "exit:$?"`
   must show **0 deleted lines**. Then `tools/audit/changed_paths.py` once more: still no untracked path under the two
   folders. Any failure: STOP and report; nothing is committed.

8. **The close commit** — session 40's instruction §5 act 8, unchanged: ONE commit for exactly its eleven paths
   (the nine kept files, `records/cowork/handoff/cowork_away_returns.md` and the batch report), staged by name, subject
   exactly `close: the L3 application act — STATUS entries, the forward-bound move and the away-returns section; nothing ratified`.
   PUSH; verify at `.git/refs/remotes/origin/master`; `git show --stat <the new tip>; echo "exit:$?"` must show those
   eleven paths and no other.

9. **The end state, as the one further commit** — session 40's instruction §5 act 9, with these changes:
   - step 2, **E5's condition:** as session 40's instruction gives it, with *act 2* meaning session 40's act 2 (the batch
     report's §3: none of the three admitted tools was red there). So the failing set expected is exactly the thirteen of
     the declared start state, item 2.
   - step 3, **A4 and A5:** the ADDED classes are those session 40's instruction names **plus
     `tools/audit/stretch_verify/`**, where exactly seven ADDED paths are expected (`README.md`, `blobhash.py`,
     `blobout.py`, `counts.py`, `gitobj.py`, `rebuild.py`, `treediff.py`). Any other path outside the classes: a
     STOP-and-report under A5, reported in the end-state portion, nothing repaired.
   - step 4, **the end-state portion:** as given there, with one added line saying that session 41 made the close.
   - step 5, **the commit:** as given there, subject exactly `close: end-state guard run after the L3 application act`.

## 5. What §10 of the batch report states, and the same in your closing message to the user

1. §1's results (checks 0 to 6), each blob and numstat as printed, the pin and its declared departure, and the checks
   repeated immediately before staging act 1; §2 item 3's result for each of the three files.
2. This session's landing commit by its full hash, verified at the object (`git show --stat`), and `origin/master` at
   it. (The close commit and the end-state commit cannot be named in a file the close commit carries: the closing
   message names both, each verified at the object, and `origin/master` at the last.)
3. Act 2's result, and act 3's result per tool (exit codes; any movement by field and its cause).
4. A sentence saying that the sentences of §0 which the stop made untrue are overtaken by this session as far as the
   close and the end state go, and that §0 itself is kept as written (#12).
5. Every departure from this file, session 40's instruction or the big dispatch, declared, as far as act 4 (§10 is final
   after act 4; a departure made after it is declared in the away-returns section, §4 act 6, and in the closing
   message); and a sentence saying that no recommendation is written anywhere — in `STATUS.md`, the tool, the report,
   the away-returns section or a commit message.
6. **The self-check after the work** (`CLAUDE.md`, its last section), over this session's own diffs, answering the five
   questions of session 40's instruction §6 item 8. **In §10:** the report's extension and any artifact act 3 rewrote.
   **In the closing message, in addition:** act 5's regenerated artifact and the away-returns section, which are written
   after §10 is final.
7. **Every figure in §10 is read at its object in this session, with the command or tool that produced it named beside
   it; no figure is copied from this file as a result** (the protocol's figure-by-citation clause, carried here as an
   order).
8. The closing message's last sentence, exactly: *"Session 41 of the L3 application ends here. Task 5 is done; the close
   commit and the end-state commit are pushed. The L3 application act is complete. Nothing else was done."* If the
   session stopped before the close commit, write *"Task 5 stopped as the report says"* in place of the second and third
   sentences. If the report had already been extended at act 4, it is then committed alone, with the subject
   `report: session 41 of the L3 application, Task 5 stopped as the report says`; if not, nothing further is
   committed after this session's landing commit.

## 6. Stop conditions, gathered in one place

STOP and report at once, restore nothing, and do nothing further, when:
- this file's banner does not record the record comparison as made (§1 check 0);
- any other check in §1 fails, or a tracked modification or an untracked file §1 check 6 names as a STOP appears;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- a check immediately before staging act 1 fails;
- an untracked path appears under `records/cowork/handoff/` or `records/cowork/rulings/` at act 2, act 5 or act 7;
- a tool STOPs at act 3 or act 5, a second `--check` fails, or a movement at act 3 is not admitted;
- the report's extension shows a deleted line (act 4);
- a check before the close commit fails, or the away-returns file shows a deleted line (act 7);
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file, session 40's instruction and the big dispatch seem to differ on something §3 does not list.

After a STOP, the report extension (if made) is committed alone as §5 item 8 says, and the session ends.
