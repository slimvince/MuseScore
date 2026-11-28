# CC dispatch — the L3 application, SESSION 40, the last: Task 5 of the L3 application dispatch (the close: the `STATUS.md` entries and the forward-bound move, the four artifacts, the batch report and the away-returns section, then the end-state guard run), and nothing else

> **STATUS: WRITTEN 2026-11-28; THE RECORD COMPARISON MADE 2026-11-28.** Written by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty.md`, whose handoff entry is 1281,
> and landed unchecked under Ruling A of 2026-11-27 as the user extended it to Task 5 (entry 1280 §0 ruling 2). The
> record comparison was made by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_one.md`, whose handoff entry is
> **1282** (`records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_two.md`); its corrections,
> and the user's ruling "A" of 2026-11-28 on the *Open* points, are applied in §4 item 6 and §5 acts 7 and 9. This file
> may now be handed to Claude Code. This file's provenance and the check notes are not in this file (ruling 1 of
> 2026-11-27, its last part): they stand in handoff entry 1281 §2 and in handoff entry 1282. Under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the big dispatch is
> executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands it over (D-252);
> the Cowork writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do
> not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0; sessions 2 to 8 its Task 1; session 9 its Task 2;
sessions 10 to 38 its Task 3; session 39 its Task 4. Session 39 landed the writing side's files in commit
`3367e3e275e8e956d29985a9ec9d99b403432537`, applied Task 4 in commit `2c7a0d2da51d304202e789c5b5f99f0a6c6784d2`
(called **the Task 4 commit** below: the last task commit of the batch before the close, which is what Task 5 (b)'s
*"the Task 4 commit"* means), and committed its report as `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e`, the current tip.

**This is session 40, the last. It does four things and STOPS:**

1. it lands the writing side's untracked files (§5 act 1);
2. it measures the guard set at the tree the close meets (§5 act 2);
3. it executes the big dispatch's **Task 5** up to and including the close commit (§5 acts 3 to 8);
4. it runs the end-state guard set and commits it as the one further commit (§5 act 9).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose.

**Documentation and record-keeping only. No algorithm is decided by this session.** Task 5 writes pointer entries,
moves superseded entries by the tool's own mechanism, regenerates artifacts whose tools already exist, and writes the
record of what the batch did. The method the specifications define stays as decided. Nothing is ratified.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section). A command whose output may be
long is redirected to a file in your session scratchpad and that file is read with the Read tool (the same section,
Rule 2).

0. **This file's banner.** If the banner above does not record that the record comparison has been made, STOP and
   report; do nothing else (the parked-instruction rule of `cowork_audit_protocol.md`, carried here as an order).
1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, and its pin.** You read this file from the working tree first, so the pin
   (`cowork_audit_protocol.md`, the standing clause P-2) takes its declared-departure route: declare in the report that
   the file was read before it was pinned; then
   `git hash-object -w records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md; echo "exit:$?"`.
   Record the hash. There is no expected value. §5 act 1 proves the file unmoved against this hash before staging.
4. **Every file Task 5 writes stands as the batch found it.** The eleven paths, called **the close's inputs** below:
   `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`,
   `tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json`,
   `tools/audit/l3_outgoing_population.json`, `tools/audit/per_session_reading.json`,
   `tools/audit/evidence_pin_membership.json`, `tools/audit/guard_state.json` and
   `records/cowork/handoff/cowork_away_returns.md`.
   - `git diff --quiet e855ff2a38883bc453b3f1c83cb20b9fd89cda05 a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- <the eleven paths>; echo "exit:$?"`
     must give exit 0 (no task of the batch committed a change to any of them; A5);
   - `git diff --quiet a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- <the eleven paths>; echo "exit:$?"` must give
     exit 0 (none is modified on disk).
   Either failing: STOP and report, nothing touched. *(The writing side's reading at the folder listings, not a
   measurement of content: each of the eleven carries a modification time of 2026-11-08 or earlier. Its staged copies:
   `STATUS.md` 11,726 bytes, 26 line feeds; the tool 352,058 bytes, 4,190 line feeds; `cowork_away_returns.md`
   2,371,205 bytes, 30,868 line feeds, ending in a line feed; all three line feeds only, no carriage return. Keep them
   so.)*
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: none.** One path appears modified and is not:
     `tools/audit/claude_md_finer_archive.json` differs from the tip only in line endings. Prove it:
     `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must print
     `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed.
   - **A tracked modification of any of the close's inputs, of the big dispatch or of this file: STOP and report** —
     each is an input of an act this file orders. **Any other tracked modification is movement no act of this batch
     caused: report it and grade it** (which act, if any, reads or lands that path), **and go on**; it is never staged.
     This is the standing clause P-3 of `cowork_audit_protocol.md`, carried here as an order: such movement is
     *"reported and graded, never absorbed and never auto-stopped"*.
   - **Untracked paths expected:** the files §5 act 1 lands (this instruction; handoff entries 1279, 1280 and 1281, and
     the entry of the Cowork sitting that makes the record comparison, which this file's banner names), plus the paths
     sessions 2 to 39 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; `docs/research_papers/desktop.ini`;
     `docs/research_papers/rowe`; the two PDFs under `external resarch summary/`;
     `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
     `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md`, which is not
     landed, not touched, and not a STOP). `.claude/` and `tools/extra scores/.mscbackup/` are git-ignored, so the tool
     does not list them; that is expected and not a STOP. List in the report every untracked path the tool reports
     outside those. A further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is
     not landed and is not a STOP (the big dispatch's A1, unchanged). **An untracked `cowork_rulings_*.md` under
     `records/cowork/rulings/` matters to act 5** (that tool lists the folder on disk): name it in the report.

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

This list is the user's ruling of 2026-11-28 for Task 5 (handoff entry 1280 §0 ruling 1: the minimized list, with the
close pointing at the session reports rather than copying their lists; ruling 5 of 2026-11-27 exercised for Task 5).
**It replaces, for this session, the big dispatch's line 98, and with it the read-first-block clause of
`cowork_audit_protocol.md` (every dispatch's read-first block names the current handover block of
`cowork_handoff.md`): `cowork_handoff.md` and the protocol's dispatch-protocol section are NOT read.** The rules of
theirs this session relies on are carried into this file as orders: the pin (§1 check 3), the movement rule (§1 check
5), the parked-instruction rule (§1 check 0), the figure rule and the self-check list (§6 items 7 and 8).

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
3. **The session-start read, by size and modification time (ruling 2 of 2026-11-27).** List the repository root and
   `tools/audit/` with the file tools and compare each of these with the values below. **A file whose size and
   modification time both equal its values is not read for the session-start read; a file where either differs is read
   in full** (`DECISIONS.md` in ranges of about 150 lines; of the gating answer, **only the list**
   `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`, as `CLAUDE.md`'s open-items
   register section, rule (a), names it). Report what you found for each.
   - `STATUS.md`: 11,726 bytes, modification time 1794136674043 (milliseconds since 1970);
   - `DECISIONS.md`: 120,603 bytes, modification time 1794081137207;
   - `tools/audit/nongating_apparatus_rows.json`: 178,066 bytes, modification time 1788814584416.
   **`STATUS.md` is read whole in any case** (item 7 below), because Task 5 writes there.
4. **`DEFECT_TYPES.md` whole** (18,368 bytes), for the self-check after the work.
5. **The big dispatch, at these lines only, with the Read tool by line range:**
   - **lines 7021–7134** (Task 5, whole, and *What this batch does NOT do*);
   - **lines 100–137** (the words section);
   - **lines 316–394** (assumptions A1 to A5, the declared start state, the standing bars, the commit-and-push
     discipline, and the findings rule);
   - **lines 405–412** (§L's opening paragraph on the decisions-register supersessions);
   - **line 6083** (Task 0's guard-set acts: the guard command and the membership tool);
   - **the E-lines of Tasks 0 to 4:** E0 at lines 6086–6093; E1 at lines 6560–6563; E2 at line 6609; E3 at lines
     6802–6811; E4 at lines 7007–7011.
   **Read nothing else of the big dispatch by the Read tool**: not its line 98 (the reading order §4 item 1 replaces),
   not its head's other lines, not §L, not Tasks 0 to 4 beyond their E-lines. **§L is met by search only**, at §5 act 7
   step 3.
6. **`tools/audit/gen_status_batch_bound.py` at these places only**, with the Read tool by line range (guides from the
   writing side's staged copy; locate each by its text and re-check before the edit): lines **2475–2498** (the last two
   re-aiming paragraphs of `BASE_COMMIT`'s comment, and the constant); **2724–2734** (the end of
   `PREVIOUS_BATCH_DISPATCH`'s comment, and the constant); **3019–3028** (the end of `ACT_DATE`'s comment, and the two
   constants); **3287–3305** (the end of `TASK`'s comment, `TASK`, `MOVE_KIND`, `RULINGS`, and the opening of
   `PREVIOUS_AIMINGS`); **3959–3992** (the list's last rows, its closing bracket, and the archive header);
   **4022–4104** (`moved_entries()` and `apply_move()`). Read nothing else of the tool (352,058 bytes).
7. **`STATUS.md` whole** (26 lines).
8. **The last section of `records/cowork/handoff/cowork_away_returns.md`**, which Task 5 appends after: lines
   **30753–30868** (the heading `# ═══ THE LANGUAGE-MODEL CORRECTION OF 2026-11-07, SECOND RESUME …` to the end of the
   file). Read nothing else of that file (2,371,205 bytes).
9. **`tools/audit/gen_guard_state.py` at lines 35–36 only** (its own two usage lines: the writing run and `--check`).
   **`BUILD_AND_TEST.md` is not read:** the writing side searched it whole for the guard set and it carries no guard
   command (its only match is `tools/audit/corpus_arm_stamp.py --check`, under the corpus regression section), so the
   condition of `CLAUDE.md`'s conditional read — a measurement tool whose command lives there — is not met.
10. **The session reports, by search only — never by the Read tool, except where §5 act 7 names a line range.** The 38
    reports `records/cc/reports/cc_report_l3_application_session_<N>_*.md` (N = 2 to 39) are met through the Grep
    tool at the headings and phrases §5 act 7 names. **Session 1 wrote no report.**

## 3. The texts this session places, given whole

**The files use line feeds only, no carriage returns. Keep them so.** The characters `★`, `—` and `→` below are U+2605,
U+2014 (em dash) and U+2192, as in the files.

**The placeholders.** `<CLOSE-DATE>` and `<ACT-DATE>` are both the date on which §5 act 4 runs `--apply`, Stockholm
time, written `YYYY-MM-DD` (for example `2026-11-28`). `<DATE-T0>` to `<DATE-T4>` are each task's date, taken at §5
act 3 step 1 from its last commit's object. `<STATUS-BLOB>` is taken at §5 act 3 step 2. No placeholder survives into
any committed file: §5 acts 3 and 4 count them.

### 3.1 The `STATUS.md` entries (Task 5 item 1 (a))

**Site.** Line 7 is blank; line 8 opens `*Last updated: 2026-11-08 (CC — `records/cc/instructions/cc_instruction_llm_correction_second_resume_2026_11_08.md`, Task 3, the close.`.

**(1) The prefix moves.** In line 8, and nowhere else, the opening `*Last updated: 2026-11-08 (CC — ` becomes
`*2026-11-08 (CC — `. Nothing else of line 8 changes.

**(2) The six entries.** Between line 7 and line 8 insert these twelve lines — each entry one line, each followed by
one blank line — so that the banner's blank line is followed by the close entry, and the last inserted blank line is
followed by line 8 as edited:

```
*Last updated: <CLOSE-DATE> (CC — `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`, Task 5, the close. **★★ THE L3 APPLICATION ACT IS CLOSED: THE DERIVED L3 SPECIFICATION AS AMENDED IS WRITTEN, THE DERIVATION IS BANNERED, THE RULED AND RECORDED ROWS OF THE L3 READING FILE ARE RE-MARKED, AND THE CHARTER AND S-50 OF THE DERIVED L0/L1 SPECIFICATION ARE AMENDED WHERE THE RECORDS GIVE THE WORDS — NOTHING RATIFIED.** ★ The act was executed by several Claude Code sessions in turn, under Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`; each session's instruction and report stand in `records/cc/instructions/` and `records/cc/reports/`. ★ The successor `cowork_derived_specification_l3_2026_11_08.md` is **NOT RATIFIED**; its ratification act is a separate decision surface, the writing side's. **No `src/` change, build, test, golden, corpus of scores or measurement of the analysis; no decisions-register entry and no `D-NNN`; no tool edited but the forward-bound tool's re-aiming.** Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l3_application_2026_11_08.md` — and no figure is restated here (**D-431**).)*

*<DATE-T4> (CC — Same dispatch, Task 4. **THE CHARTER `FRAMEWORK.md` AND S-50 OF THE DERIVED L0/L1 SPECIFICATION ARE AMENDED WHERE THE L3 FAMILY RECORDS GIVE THE WORDS**, each with its former wording kept. **POINTER** — `records/cc/reports/cc_report_l3_application_2026_11_08.md` (**D-431**).)*

*<DATE-T3> (CC — Same dispatch, Task 3. **THE L3 READING FILE'S RULED AND RECORDED ROWS ARE RE-MARKED**, and its transfer list, ruled distribution and statements of its own state brought up to date; no row's proposed paragraph edited. **POINTER** — `records/cc/reports/cc_report_l3_application_2026_11_08.md` (**D-431**).)*

*<DATE-T2> (CC — Same dispatch, Task 2. **THE DERIVATION `cowork_blind_derivation_l3_2026_10_17.md` CARRIES ITS TOP BANNER UNDER D-674**, its body unchanged. **POINTER** — `records/cc/reports/cc_report_l3_application_2026_11_08.md` (**D-431**).)*

*<DATE-T1> (CC — Same dispatch, Task 1. **THE SUCCESSOR `cowork_derived_specification_l3_2026_11_08.md` IS WRITTEN** — the derived L3 specification as amended by the L3 family rulings, NOT RATIFIED. **POINTER** — `records/cc/reports/cc_report_l3_application_2026_11_08.md` (**D-431**).)*

*<DATE-T0> (CC — Same dispatch, Task 0. **THE L3 FAMILY RULING RECORDS, THEIR SURFACES, THE HANDOFF ENTRIES AND THIS DISPATCH ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_report_l3_application_2026_11_08.md` (**D-431**).)*

```

(The block's last line is the blank line after the Task 0 entry.) *Why each entry is worded so:* Task 5 (a) orders one
pointer entry per task that committed work, the close entry first and naming the dispatch by its file name, each
earlier entry saying `Same dispatch`, each naming the report and restating no figure. Every task 0 to 4 committed work
(§5 act 3 step 1 proves it at the objects). The entries' wording is this file's, on the shape of the entries now in
`STATUS.md`. **A task whose last commit act 3 step 1 cannot find gets no entry: STOP and report** before writing any.

### 3.2 The re-aiming of `tools/audit/gen_status_batch_bound.py` (Task 5 item 1 (b))

Five sites, each an insertion of comment lines and, where a constant's value changes, the constant's line replaced.
Nothing else in the tool changes. **Make them from the bottom up**, so each line number below, which is the line before
any edit, stays right for the next.

**(e) `PREVIOUS_AIMINGS` — this batch's own aiming appended.** Lines 3967–3970 are the list's last row (the language-
model correction batch's own aiming, `base_commit` `468aac14856d2cabf6cc5f9ee58678b7073d5c24`), and line 3971 is `]`.
Between lines 3970 and 3971 insert these four lines, exactly:

```
    {"executing_act": "cc_instruction_l3_application_2026_11_08.md, Task 5",
     "base_commit": "2c7a0d2da51d304202e789c5b5f99f0a6c6784d2",
     "the_then_previous_batch": "cc_instruction_llm_correction_second_resume_2026_11_08.md",
     "the_kind_of_move": "ordinary"},
```

(§4 item 5 says why this row and not a second copy of the superseded one.) `MOVE_KIND` (line 3301, `"ordinary"`) is not
edited: this move is an ordinary one, made in the same act that writes this batch's entries.

**(d) `TASK`.** Line 3293 ends `# which that dispatch's heading *"Task 3 — the close"* names in those words.)*`, and line
3294 is exactly `TASK = "Task 3"`. Line 3294 becomes these six lines, exactly:

```
# *(`TASK` read "Task 3" while `cc_instruction_llm_correction_second_resume_2026_11_08.md` was the executing
# act, and names Task 5 while `cc_instruction_l3_application_2026_11_08.md` is the executing act, that
# dispatch ordering both halves of the close — this batch's own entries at its item 1 (a) and this move at its
# items 1 (b) and 1 (c) — inside its own Task 5, which that dispatch's heading *"Task 5 — the close"* names in
# those words.)*
TASK = "Task 5"
```

**(c) `ACT_DATE` and `DISPATCH`.** Lines 3023–3026 are the last parenthesis of `ACT_DATE`'s comment (it ends `ran on
2026-11-08, so the two dates agree and `ACT_DATE` takes that value.)*`); line 3027 is exactly `ACT_DATE = "2026-11-08"`
and line 3028 exactly `DISPATCH = "cc_instruction_llm_correction_second_resume_2026_11_08.md"`. Lines 3027 and 3028
become these seven lines, exactly:

```
# *(`ACT_DATE` read "2026-11-08" and `DISPATCH` `cc_instruction_llm_correction_second_resume_2026_11_08.md`
# while that batch was the executing act; both are re-stated here for
# `cc_instruction_l3_application_2026_11_08.md`, dated 2026-11-08 in its file name, whose move ran on
# <ACT-DATE>, so the two dates differ and `ACT_DATE` takes the day the move ran, as that dispatch's Task 5
# item 1 (b) orders.)*
ACT_DATE = "<ACT-DATE>"
DISPATCH = "cc_instruction_l3_application_2026_11_08.md"
```

**(b) `PREVIOUS_BATCH_DISPATCH`.** Lines 2730–2733 are the last parenthesis of its comment (it ends `the two stopped
language-model correction batches between them wrote no `STATUS.md` entry.)*`); line 2734 is exactly
`PREVIOUS_BATCH_DISPATCH = "cc_instruction_records_landing_2026_11_07.md"`. Line 2734 becomes these four lines,
exactly:

```
# *(`PREVIOUS_BATCH_DISPATCH` read "cc_instruction_records_landing_2026_11_07.md" while
# `cc_instruction_llm_correction_second_resume_2026_11_08.md` was the executing act; it is re-stated here
# for `cc_instruction_l3_application_2026_11_08.md`, whose then-previous batch is that one.)*
PREVIOUS_BATCH_DISPATCH = "cc_instruction_llm_correction_second_resume_2026_11_08.md"
```

**(a) `BASE_COMMIT`.** Lines 2487–2497 are the last re-aiming paragraph (it opens `# ★★ RE-AIMED 2026-11-08 BY` and ends
`**NO COUNT OF THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431).`); line 2498 is exactly
`BASE_COMMIT = "468aac14856d2cabf6cc5f9ee58678b7073d5c24"`. Line 2498 becomes these fourteen lines, exactly:

```
#
# ★★ RE-AIMED <ACT-DATE> BY `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`
# Task 5 (b). `BASE_COMMIT` was `468aac14856d2cabf6cc5f9ee58678b7073d5c24` and is now
# `2c7a0d2da51d304202e789c5b5f99f0a6c6784d2`: this batch's Task 4 commit, which is its LAST TASK COMMIT
# before the close. That commit carries no `STATUS.md` change, so its `STATUS.md` object is the one both refs
# carried when this batch opened (the blob `<STATUS-BLOB>`, at the commit
# `e855ff2a38883bc453b3f1c83cb20b9fd89cda05` and at `2c7a0d2d…`, established at `git rev-parse` of each, one
# command per commit) — and it carries the language-model correction second resume batch's entries at the head
# of the dated entries. The then-previous batch is that batch. Its close entry's `Last updated: ` prefix was
# MOVED to this batch's close entry in the same edit that wrote this batch's entries, before `--apply` ran.
# The aiming this replaces is ALREADY the last row of `PREVIOUS_AIMINGS` — that batch recorded its own aiming
# in its own act — so it is not appended a second time, and this batch's aiming is appended instead.
# **NO COUNT OF THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431).
BASE_COMMIT = "2c7a0d2da51d304202e789c5b5f99f0a6c6784d2"
```

(The block is thirteen comment lines and the constant; with line 2498 replaced, the file gains thirteen lines here.)
The comment wording at all five sites is this file's, on the shape of the earlier re-aimings at the
same sites.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session (the user's ruling of 2026-11-28, handoff entry 1280 §0
   ruling 1). With it, **the read-first-block clause of `cowork_audit_protocol.md` is replaced** for this session (§2's
   opening). Line 98's item (6) — the tool at the tip and the last section of `cowork_away_returns.md` — is kept, as §2
   items 6 and 8.
2. **A1, for the writing side's handoff entries.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed.
   **Handoff entries 1279, 1280 and 1281, and the entry of the sitting that makes the record comparison, which this
   file's banner names, ARE landed**, with this file, in §5 act 1, as sessions 8 to 39 landed theirs. Any other
   untracked handoff entry or ruling record stays as A1 says.
3. **The declared start state's guard figures (item 2) are overtaken, with known causes, and are declared again here**
   (the user's rule of 2026-09-22 on staleness; the shape the standing clause *"A dispatch's DECLARED START STATE is
   stated at the tree the dispatch will meet"* of `cowork_audit_protocol.md` exists against). At session 1 the full
   guard set showed fifteen failing, not thirteen [relayed from Claude Code's closing message, handoff entry 1184 §2
   item 2]; the two further reds, with their causes [checked at the tools by that sitting]:
   `gen_evidence_pin_membership.py --check` (the tool lists every ruling record in `records/cowork/rulings/` on disk,
   and records were written there after its artifact) and `gen_per_session_reading.py --check` (the tool finds handoff
   entries through git history, and the batch's commits landed many). **No guard artifact has been written since**
   (`tools/audit/guard_state.json` still carries modification time 1794137557660, 2026-11-08). **So this session
   measures the start state itself** (§5 act 2) **and grades E5 against what it measures**, under the rule §5 act 2
   states. The two reds' artifacts are regenerated by this session's ordered acts: `per_session_reading.json` at Task 5
   (d) as written, and `evidence_pin_membership.json` at §5 act 5, which is item 4 below.
4. **Added: the regeneration of `tools/audit/evidence_pin_membership.json` at the close** (§5 act 5; owed into this
   instruction by handoff entry 1184 §2 item 2). A5 already admits that artifact's movement; this file orders the
   regeneration and adds it to the close commit's paths.
5. **Task 5 (b)'s *"append the superseded aiming to `PREVIOUS_AIMINGS`"*** → **this batch's own aiming is appended**
   (§3.2 (e)). The superseded aiming — the language-model correction batch's, `base_commit`
   `468aac14856d2cabf6cc5f9ee58678b7073d5c24` — is already the list's last row, recorded there by that batch in its own
   act; appending it again would put the same aiming in the list twice. The tool's own record states this case and its
   practice at earlier re-aimings (its `BASE_COMMIT` comment: *"The aiming it replaces is … ALREADY the last row of
   `PREVIOUS_AIMINGS` … so it is not appended a second time, and this batch's aiming is appended instead"*). A
   staleness fix, made without a question under the user's rule of 2026-09-22, and shown to the user by the writing
   side.
6. **Task 5 item 2's lists → POINTERS** (the user's ruling of 2026-11-28, entry 1280 §0 ruling 1). The big dispatch says
   the lists stand in the away-returns section *"as lists under the report sections the Tasks name"*. **For this
   session, the batch report and the away-returns section grade each Task (E0 to E5) and point at the session report —
   by path and commit — and at the section where each named list stands. The lists are NOT copied.** The pointers are
   gathered by searching the reports (§5 act 7), not by reading them whole. **Two further lists of item 2 stand in the
   big dispatch itself, not in a session report, and are handled so:**
   - **the decisions-register supersessions** (each §L entry's *Register* list) **are restated as a list**, as §L's
     opening paragraph fixes (*"the close restates the lists (Task 5)"*, fixed at release under Ruling 4 of the first
     Part B ruling record) — one line per §L entry, naming the decisions-register identities its *Register* paragraph
     names, or *none*, read by search (§5 act 7 step 3);
   - **every §L entry's *Open* points** are **pointed at**, not restated: the line of the big dispatch where each of the
     entry's paragraphs labelled `**Open, for the releasing sitting:**` and `**Carried open by the record:**` stands,
     found by search, with the sentence that they are NOT YOURS and untouched beyond what the Tasks write. **This is the
     user's ruling "A" of 2026-11-28** (handoff entry 1282), taken on a surface that weighed it against restating the
     paragraphs as the big dispatch's Task 5 and the release rulings that rely on that restatement word it (Rulings 21 to
     24 and 26 of `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). *Why the
     difference from the Register list:* the *Register* restatement is a fixed, ratified order, and its paragraphs come
     to about 18 KB of the big dispatch by the writing side's count at its staged copy; the *Open* and *Carried open*
     paragraphs come to about 220 KB, which a copy would duplicate (#6). *(Corrected at the record comparison: the
     writer's version pointed at the `**Open` paragraphs only, so the 54 `**Carried open by the record:**` paragraphs
     would have been met by no pointer, and it rested on the writing side's reading of ruling 1, which the user has now
     ruled.)*
7. **An added regeneration of `per_session_reading.json` after the report is final** (§5 act 7 step 6). Task 5 (d)
   orders it LAST after the final edit to `STATUS.md`; the batch report is written after that, and the tool counts the
   reports on disk. The last close met exactly this and regenerated once more after its report was final (the last
   section of `cowork_away_returns.md`, its *3(c′)*), and this session does the same. That run's movement is recorded in
   the away-returns section, not in the report, which is not edited after it.
8. **The close commit's paths.** Task 5 (d) names eight paths; this session's close commit carries those eight, plus
   `tools/audit/evidence_pin_membership.json` (item 4), `records/cowork/handoff/cowork_away_returns.md` (Task 5 item 2)
   and the batch report `records/cc/reports/cc_report_l3_application_2026_11_08.md` (Task 5 item 2's last sentence):
   eleven paths, listed at §5 act 8.
9. **The end-state commit's paths.** Task 5 item 4 orders *"the one further commit with the end-state guard run"*. It
   carries `tools/audit/guard_state.json` and the end-state portion appended to `cowork_away_returns.md`, as the last
   two closes' end states did (the last one declared that departure at its foot).
10. **Where the batch ends.** After §5 act 9, this session STOPS. The batch is then complete; nothing further is
    begun.

## 5. The acts, in order

**NONE OF THE CLOSE'S INPUTS IS EDITED UNTIL ACT 1 HAS BEEN COMMITTED, PUSHED AND VERIFIED, AND ACT 2 HAS PASSED.** Until
then, each is opened with the Read and Grep tools only — no Edit or Write call names it. **Every read §2 orders is
made before the act that needs it.**

1. **Land the writing side's files first, in a commit of their own.** Exactly these paths, each UNTRACKED:
   - this file, `records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md`;
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_nine.md` (the sitting that
     verified session 39);
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty.md` (the sitting that took the
     user's two rulings for Task 5);
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_one.md` (the sitting that wrote
     this file);
   - and the entry of the Cowork sitting that makes the record comparison, which this file's banner names.
   **Immediately before staging:** run §1 check 2 again; hash this file again (`git hash-object`, as §1 check 3) and it
   must equal the hash §1 check 3 recorded and pinned; and `git diff --quiet a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- <the eleven inputs>; echo "exit:$?"`
   must give exit 0 (none yet touched). Any of these failing: STOP and report, nothing staged. Stage the paths by name
   (never `git add` on a folder or with a pattern). Subject exactly, with `<N>` the number of the entry the banner
   names:
   `record: handoff entries 1279 to <N> and the session 40 instruction of the L3 application landed; Task 5 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Then `git show --stat <the new tip>;
   echo "exit:$?"` must show exactly the paths above added, and nothing else. This commit is called **the landing
   commit** below.

2. **The start-state guard run, at the tree the landing commit left, before any edit.** Run
   `python tools/audit/gen_guard_state.py --check > "<your scratchpad>/l3_session40_guard_start.txt" 2>&1; echo "exit:$?"`
   (the tool's own usage, its line 36: *"run every guard, exit 1 on any drift"*; the command of the big dispatch's line
   6083) and read the file with the Read tool. A non-zero exit is expected, because the verdicts differ from the
   artifact; it writes nothing. **The rule, and the prediction:**
   - **Expected [relayed, entry 1184 §2 item 2, from session 1's run; not re-measured since]:** 83 guards run, zero
     STOPs in the runner, and the failing set the thirteen of the declared start state, item 2, plus
     `gen_evidence_pin_membership.py --check` and `gen_per_session_reading.py --check`.
   - **Admitted beside them, each reported with its verdict line:** a red at `gen_session_start_read_size.py --check`,
     `gen_defense_share.py --check` or `gen_l3_outgoing_population.py --check` — the three tools whose artifacts Task 5
     (d) regenerates, so that any red there is cleared by an ordered act. Each such red's cause is measured at act 6,
     as the movement of its artifact by field.
   - **A STOP in the runner, a population other than 83, or any other red: STOP and report**, with the verdict lines
     as printed. Nothing is edited. *(The big dispatch: "A failing verdict outside the declared start state is a
     STOP-and-report"; this rule is that sentence applied to the start state item 3 of §4 declares.)*
   - Record the whole verdict list in the report, and compare it, verdict by verdict, with the artifact the last close
     committed (`tools/audit/guard_state.json` at the tip); name every verdict that differs.

3. **The `STATUS.md` entries** (Task 5 item 1 (a)), in these steps:
   1. **Each task's last commit and its date, at the objects.** One command per path, each output written to the
      scratchpad and read with the Read tool:
      `git log -1 --format="%H %ci %s" a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- <path>; echo "exit:$?"` for
      Task 1 with `cowork_derived_specification_l3_2026_11_08.md`, Task 2 with `cowork_blind_derivation_l3_2026_10_17.md`,
      Task 3 with `ratification_surfaces/cowork_comparison_l3_reading.md`, and Task 4 with `FRAMEWORK.md`; and for
      Task 0, `git show -s --format="%H %ci %s" cbde76fd78a244540df64895191a511df186cc29; echo "exit:$?"`. **Expected:**
      Task 3's hash `8ce907b9962149eb8c7cdff5a8b1610a966d77cb` and Task 4's `2c7a0d2da51d304202e789c5b5f99f0a6c6784d2`;
      Task 1's hash named in one of the reports of sessions 2 to 8, and Task 2's in session 9's report (a Grep search
      of those reports for the hash's first ten characters); and the order Task 0, Task 1, Task 2, Task 3, Task 4 by
      commit date. Any other result: STOP and report, nothing written. Each `<DATE-Tn>` is the date in that output, which is local time with its offset: if
      the offset is `+0100`, take the date as printed; otherwise convert to Stockholm time and say so in the report.
   2. **Write §3.1** with the Edit tool: the prefix moved in line 8, then the twelve lines inserted before it, the
      placeholders filled. Then read lines 1–24 back with the Read tool and confirm, with the Grep tool counting matching
      lines: `^\*(Last updated: )?20\d\d-\d\d-\d\d` (the tool's own dated-entry pattern, imported by the forward-bound
      tool from `gen_status_archive_pass.py`) **12**; `Last updated: ` **1** (fixed-string; it is the close entry's); the
      fixed string `cc_instruction_l3_application_2026_11_08.md` **1**; the fixed string `Same dispatch` **9** (this
      batch's five entries for Tasks 4 to 0, the second resume batch's three, and the second 2026-09-02 entry; the
      writing side counted 4 at its staged copy before the edit); and `<DATE-` **0**, `<CLOSE-DATE>` **0**. Any other
      count: restore `STATUS.md` from the tip
      (`git checkout a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- STATUS.md; echo "exit:$?"`), STOP and report.

4. **The re-aiming, then the move** (Task 5 item 1 (b) and (c)):
   1. **The blob for the comment.** `git rev-parse e855ff2a38883bc453b3f1c83cb20b9fd89cda05:STATUS.md; echo "exit:$?"`
      and `git rev-parse 2c7a0d2da51d304202e789c5b5f99f0a6c6784d2:STATUS.md; echo "exit:$?"`, one command per commit,
      must print the same blob; that blob is `<STATUS-BLOB>`. If they differ, a task of the batch changed `STATUS.md`
      against A5: STOP and report, nothing edited in the tool.
   2. **The five edits of §3.2**, with the Edit tool, in the order (e), (d), (c), (b), (a). Before each, re-read the
      site's lines and confirm they read as §3.2 says.
   3. **The check before the move.**
      `git diff --numstat a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- tools/audit/gen_status_batch_bound.py; echo "exit:$?"`
      must show **exactly 35 added and 5 deleted lines** ((e) 4 added; (d) 6 added, 1 deleted; (c) 7 added, 2 deleted;
      (b) 4 added, 1 deleted; (a) 14 added, 1 deleted — the writing side's count of §3.2's blocks, taken by a search
      over this file; the record comparison checks it). And with the Grep tool, fixed-string, counting matching lines in
      the tool: `2c7a0d2da51d304202e789c5b5f99f0a6c6784d2` **3**; `<ACT-DATE>` **0**; `<STATUS-BLOB>` **0**;
      `TASK = "Task 5"` **1**; `DISPATCH = "cc_instruction_l3_application_2026_11_08.md"` **1**. Any other count:
      restore the tool from the tip
      (`git checkout a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- tools/audit/gen_status_batch_bound.py; echo "exit:$?"`),
      STOP and report.
   4. **Run the move:** `python tools/audit/gen_status_batch_bound.py --apply > "<your scratchpad>/l3_session40_apply.txt" 2>&1; echo "exit:$?"`,
      read with the Read tool. **Prediction, from `STATUS.md` read whole at the writing side's staged copy on 2026-11-28
      (it equals Task 5 (c)'s prediction of 2026-11-09):** the run moves **exactly the second resume batch's four
      entries** — its close entry (Task 3, the one naming its dispatch) and the three below it that say `Same
      dispatch`; the run stops at the first 2026-09-02 entry, which says neither, so both 2026-09-02 entries stay (the
      declared standing state that `STATUS.md`'s own 2026-09-07 pointer records — not a STOP, and no row is created for
      it). Exit 0 and the printout's two reconciliation lines `True`. **If the tool STOPs (exit 2), or exits non-zero in
      any other way** (an error while the edited file is loaded is one): restore it to its
      passing aim (`git checkout a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- tools/audit/gen_status_batch_bound.py STATUS.md STATUS_ARCHIVE.md tools/audit/status_batch_bound.json; echo "exit:$?"`),
      which undoes act 3's entries too, so that nothing written by this session stays on disk uncommitted; then
      re-run `python tools/audit/gen_status_batch_bound.py --check; echo "exit:$?"` to prove it green, report the STOP
      with the tool's message, move nothing by hand, and STOP the session.
   5. **After the move:** `python tools/audit/gen_status_batch_bound.py --check; echo "exit:$?"` must give exit 0; with
      the Grep tool on `STATUS.md`, the dated-entry pattern of act 3 step 2 must count **8** (this batch's six and the
      two 2026-09-02 entries) and the fixed string `cc_instruction_llm_correction_second_resume_2026_11_08.md` **0**;
      and in `STATUS_ARCHIVE.md` the fixed string `★ RULING 4's FORWARD BOUND, <ACT-DATE>` (filled) must count **1**.
      Any other result: STOP and report; do not repair.

5. **The membership artifact** (§4 item 4). `python tools/audit/gen_evidence_pin_membership.py --check; echo "exit:$?"`
   first, its result recorded (red expected, §4 item 3); then the writing run,
   `python tools/audit/gen_evidence_pin_membership.py; echo "exit:$?"`; then `--check` again, which must give exit 0.
   Then `git diff a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- tools/audit/evidence_pin_membership.json > "<your scratchpad>/l3_session40_pin_diff.txt"; echo "exit:$?"`,
   read with the Read tool, and report the movement **field by field**. **The movement expected:** the count of records
   read, and the records listed, larger by the ruling records written since its artifact (2026-11-07). **A movement in
   the members or the pinned set** is accepted only where a ruling record's own PINNED sentence causes it: find that
   sentence with the Grep tool in the record the artifact names, and quote it in the report (*"measure before
   accepting"*, the big dispatch's line 6083). **If no such sentence is found:** restore the artifact from the tip
   (`git checkout a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- tools/audit/evidence_pin_membership.json; echo "exit:$?"`),
   leave it out of the close commit, report it as STOP-and-report for that artifact, and go on; its red then stands at
   E5 and is named there.

6. **The four artifacts** (Task 5 (d)), in this order — `tools/audit/gen_session_start_read_size.py`,
   `tools/audit/gen_defense_share.py`, `tools/audit/gen_l3_outgoing_population.py`, and
   `tools/audit/gen_per_session_reading.py` LAST — each: `--check` in its own call, result recorded; the writing run
   (`python <tool>; echo "exit:$?"`, output to the scratchpad when long); `--check` again in its own call, which must give
   exit 0. Then, for each artifact, `git diff a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- <artifact>` to the scratchpad,
   read with the Read tool, and the movement reported **by field**. Nothing here is predicted beyond this: each moves
   because `STATUS.md` changed or because the batch's commits changed what it counts, and the report names which field
   moved. **A second `--check` that fails, or a tool that STOPs: restore that artifact from the tip, STOP and report.**
   `STATUS.md` is not edited after act 4: its last edit is the move, so act 6 runs after the final edit to `STATUS.md`,
   as Task 5 (d) orders.

7. **The batch report, then the last regeneration, then the away-returns section** (Task 5 item 2):
   1. **Every commit of the batch.**
      `git log --reverse --format="%H %ci %s" e855ff2a38883bc453b3f1c83cb20b9fd89cda05..<the landing commit> > "<your scratchpad>/l3_session40_log.txt"; echo "exit:$?"`,
      read with the Read tool. This is the list of every commit hash Task 5 item 2 asks for, up to the landing commit;
      the close commit and the end-state commit are named in the closing message and in the end-state portion.
   2. **The pointers into the session reports, by search** (§4 item 6). With the Grep tool, headings mode
      (`^## |^### `), over each report `records/cc/reports/cc_report_l3_application_session_<N>_*.md`, and with the
      fixed-string searches named, confirm that each pointer below lands on a heading or line that exists; correct a
      section number only where the search shows it, and say so. **The writing side's locations, from a heading search
      of its staged copies on 2026-11-28:**
      - **Task 0 (E0):** no report. The commit `cbde76fd78a244540df64895191a511df186cc29`, which you grade at the
        object (`git show --stat cbde76fd…; echo "exit:$?"`, written to the scratchpad); its guard-set run is
        **[relayed]** in handoff entry 1184 §2 items 1 and 2 (the writing side's verification of session 1).
      - **Task 1 (E1):** sessions 2 to 7's reports, each at its §3 (entry by entry) and §5 (the diff table); session 7
        also at its §6 (*For the user*); **session 8's report** (the full check) at its §4 (the diff table over the
        whole successor) and **§6 (E1, graded item by item)**, whose item 3 gathers the STOP-and-report items and the
        points the reports list for the user — the place *amendments with no words from the record* is answered.
      - **Task 2 (E2):** session 9's report, §3 (E2, graded).
      - **Task 3 (E3):** sessions 10 to 37's reports, each at the section headed *The report headings Task 3 names*
        (its §4; session 24's §5) — where *rows the act could not place*, *rows named by more than one record*, *ADOPTED
        words read at the row*, *audit questions added*, *audit questions no longer quarantined*, *§10 rows a record
        says leave*, *held by ruling*, *placed outside every charter*, *rows given no line now*, *recorded lines not
        written: no disposition word*, *points answered by a record's own derivation* and the decided-against hits
        stand, as far as each stretch had any — and at the section headed *Row-parts this stretch gives no line* (its
        §6; session 24's §7); session 12 also at its §7 (*§10 entries left standing*). *(The headings' wording varies,
        found by the record comparison's heading search; the section numbers above hold: sessions 10 and 11 head their
        §4 *The headings Task 3 names*; session 19 heads its §6 *Row-portions this stretch gives no line*; sessions 34
        to 37 head their §6 *Row-parts and rows this stretch gives no line*.)* **Session 38's report** at its §3
        (the searches), the paragraph *The report headings Task 3 names, for this stretch* inside its §4, and **§5 (the
        check before the commit and E3)**. For each named list, the fixed-string searches the writing side ran over the
        38 reports found its phrase in these sessions' reports, case ignored: *rows the act could not place*, *named by
        more than one record*, *ADOPTED words read at the row* — sessions 10 to 38; *audit questions added*, *no longer
        quarantined*, *no disposition word* — 12 to 38; *a record says leave* — 13 to 38; *placed outside every
        charter* — 24 to 38; *rows given no line now* — 11 to 23; *held by ruling* — 11 and 32; *answered by a record's
        own derivation* — 12; *decided-against* or *decided against* — sessions 7 and 10 to 38. *Charter and contract
        amendments left to the user* — 39 only. Re-run them and report what you find.
      - **Task 4 (E4):** session 39's report, §3 (E4, graded) and §3.4 (*Charter and contract amendments left to the
        user*).
      - **Each session's declared departures:** the section of each report headed *Departures*.
      Each report's own commit is taken from the log of step 1 by its subject (`report: session <N> of the L3
      application, …`).
   3. **The big dispatch's two lists, by search** (§4 item 6). With the Grep tool over the big dispatch, lines 395–5906
      (§L): the pattern `\*\*Register:\*\*` with enough lines after each match to reach the paragraph's end (the
      paragraph ends at its blank line or at the next `**…:**` label), and the two patterns
      `\*\*Open, for the releasing sitting:\*\*` (not anchored at the line's start: one such paragraph opens mid-line)
      and `^\*\*Carried open by the record:\*\*`. **For *Register*:** one
      line per §L entry, `§L.<n> — <the decisions-register identities its paragraph names, as written there, or
      "none">`. **For *Open*:** one line per §L entry carrying either paragraph,
      `§L.<n> — Open, the big dispatch, line <line>; Carried open, line <line>`, each part left out where the entry has
      no such paragraph. *(The record comparison's search at the staged copy: 51 lines carry the first label, one of them
      mid-line at line 620; 54 lines open with the second; §L.1 carries neither; re-count them and report what you find.)* Read nothing more of §L than
      the matched lines and the lines after them that the *Register* paragraphs need.
   4. **Write the batch report** `records/cc/reports/cc_report_l3_application_2026_11_08.md` with the items of §6. The
      report is final when written: it is not edited after step 5.
   5. **The last regeneration** (§4 item 7): `python tools/audit/gen_per_session_reading.py --check; echo "exit:$?"`
      (red expected, the new report being on disk); the writing run; `--check` again, which must give exit 0; the
      artifact's diff against the one act 6 left, read and reported by field in the away-returns section.
   6. **Append the away-returns section** at the end of `records/cowork/handoff/cowork_away_returns.md`, after one blank
      line, headed exactly
      `## THE L3 APPLICATION ACT: THE DERIVED L3 SPECIFICATION AS AMENDED WRITTEN, THE DERIVATION BANNERED, THE RULED AND RECORDED ROWS RE-MARKED, THE CHARTER AND S-50 OF THE DERIVED L0/L1 SPECIFICATION AMENDED WHERE THE RECORDS GIVE THE WORDS, NOTHING RATIFIED`
      (Task 5 item 2's heading words; the `##` level is this file's), carrying, in this order:
      - one sentence saying the whole of the batch's close is the report and this section points at it and at the
        session reports;
      - **the start-state guard run of act 2** (both guard states: this one, and the end state the further commit
        appends) and session 1's guard-set run as relayed in entry 1184 §2;
      - **every commit hash**: the log of step 1, whole, as a list;
      - **E0 to E5, each graded** (*met*, *met with the departures named*, or *not met*, and why), each pointing at its
        session report(s) by path and commit and at the section, as step 2 locates them; E5 graded *"NOT ASSERTED
        HERE — the one further commit carries it"*;
      - **each task's diff, attributed by site or passage, as a POINTER** to the report section of step 2 that attributes
        it;
      - **the named lists of Task 5 item 2, as POINTERS** — a table, one row per list name, in Task 5 item 2's order,
        each naming the reports and sections where it stands (step 2), and *none in any report* where the searches find
        none;
      - **the decisions-register supersessions**, restated as the list of step 3, with the sentence that this batch
        writes nothing into `DECISIONS.md` and allocates no `D-NNN`;
      - **the points that are not this batch's**: the *Open* pointer list of step 3, and the sentence *"every item this
        dispatch marked as authored and overrulable before Task 0, where its mark has been brought into line, stands as
        the user ruled it at the record that mark names; NOT YOURS, and untouched beyond what the Tasks write"*;
      - **the declared departures**: this session's, and a pointer to each session report's *Departures* section;
      - **the last regeneration of step 5**, with its movement by field;
      - **the plan lines:** *"The check turn and the ratification act are the writing side's; the ratification act is a
        separate decision surface over the successor (Task 3 (d): §15 of the reading file still reads NOTHING), where
        the points above return."*;
      - **the plan's tell in one sentence**: did this batch produce anything other than the landed paths of Task 0, the
        successor, the derivation's banner, the reading file's added lines and sections and the sentences Task 3 (d)
        writes into its existing lines, the four `FRAMEWORK.md` sites with their notes, S-50 of the derived L0/L1
        specification, the Task-5 files and the report? If yes, name it;
      - **THE END STATE IS NOT ASSERTED HERE** — the one further commit carries it (Task 5 item 3);
      - a provenance line: Claude Code, the date, the boot tip, this instruction.
   7. **The checks before the close commit**, each in its own call, each must give exit 0:
      `gen_status_batch_bound.py --check`, `gen_evidence_pin_membership.py --check` (unless act 5 restored it),
      `gen_session_start_read_size.py --check`, `gen_defense_share.py --check`, `gen_l3_outgoing_population.py --check`,
      `gen_per_session_reading.py --check`. Then
      `git diff --numstat a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e -- records/cowork/handoff/cowork_away_returns.md; echo "exit:$?"`
      must show **0 deleted lines**: the file is appended to and nothing else. Any failure: STOP and report; nothing is
      committed.

8. **The close commit.** ONE commit for exactly these paths, staged by name (the eleven of §4 item 8, less any act 5
   or act 6 restored): `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, `STATUS.md`,
   `STATUS_ARCHIVE.md`, `tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json`,
   `tools/audit/l3_outgoing_population.json`, `tools/audit/per_session_reading.json`,
   `tools/audit/evidence_pin_membership.json`, `records/cowork/handoff/cowork_away_returns.md`,
   `records/cc/reports/cc_report_l3_application_2026_11_08.md`. Subject exactly (the big dispatch's line 7100):
   `close: the L3 application act — STATUS entries, the forward-bound move and the away-returns section; nothing ratified`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip; `git show --stat <the new tip>; echo
   "exit:$?"` must show those paths and no other.

9. **The end state, as the one further commit** (Task 5 item 4 and E5).
   1. **A fresh full guard run as a writing run**, at the tree the close commit left:
      `python tools/audit/gen_guard_state.py > "<your scratchpad>/l3_session40_guard_end.txt" 2>&1; echo "exit:$?"`
      (the tool's usage, its line 35), read with the Read tool; its result at `tools/audit/guard_state.json` →
      `summary`.
   2. **E5's condition, derived from the start state plus this batch's footprint (P-3):** 83 guards run; zero STOPs in
      the runner; **the failing set exactly the thirteen of the declared start state, item 2, less any of them this
      batch's acts cleared (none is expected)** — the start state of act 2
      **LESS** the reds this session's ordered acts cleared (the membership tool, the per-session tool, and any of the
      three admitted at act 2), **PLUS NONE**. A red act 5 left standing is named as such. Compare the run verdict by
      verdict with act 2's, and name every verdict that differs.
   3. **A4 and A5, verified at the objects.**
      `git diff --name-status e855ff2a38883bc453b3f1c83cb20b9fd89cda05 <the close commit> > "<your scratchpad>/l3_session40_name_status.txt"; echo "exit:$?"`,
      read with the Read tool, and every path accounted for **by class**: every ADDED path lies under
      `records/cowork/handoff/`, `records/cowork/rulings/`, `ratification_surfaces/`, `records/cc/instructions/` or
      `records/cc/reports/`, or is the successor `cowork_derived_specification_l3_2026_11_08.md`; every MODIFIED path is
      one of: the four Task 0 tracked paths (`docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
      `ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md`,
      `ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md`), the derivation (Task 2), the reading file
      (Task 3), `FRAMEWORK.md` and `cowork_derived_specification_l0_l1_2026_09_03.md` (Task 4), the paths of the
      close commit, and a path under `records/cc/` that a later session's report declares it corrected (session 9's
      report declares one line of session 8's report corrected); nothing DELETED. Report the counts per class as the listing gives them, and name any path outside
      these classes — that is a STOP-and-report under A5, reported here and nothing repaired. And
      `git diff e855ff2a38883bc453b3f1c83cb20b9fd89cda05 <the close commit> -- cowork_blind_derivation_l3_2026_10_17.md`
      to the scratchpad must show **one changed passage, at the top, insertions only** (A5, as E2).
   4. **Append the end-state portion** to `cowork_away_returns.md`, headed
      ``### THE END STATE — run at the tree the close commit `<the close commit's full hash>` left, appended in the one further commit``
      (the hash in backticks, as the three earlier end-state headings in that file carry it), on the shape of the last
      section's end-state portion (lines 30812–30868, read at §2 item 8): the close commit
      pushed and verified; the run's first and last lines verbatim; E5's condition, MET or NOT MET item by item; A4 and
      A5 as step 3 found them; *"This commit adds only the guard run's artifact and this portion."*; a provenance line.
   5. **Commit exactly `tools/audit/guard_state.json` and `records/cowork/handoff/cowork_away_returns.md`**, staged by
      name, subject exactly (the big dispatch's line 7102):
      `close: end-state guard run after the L3 application act`
      PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip; `git show --stat <the new tip>; echo
      "exit:$?"` must show those two paths and no other.

## 6. What the report states, and the same in your closing message to the user

1. §1's results (checks 0 to 5), the blobs, the pin and its declared departure, and the checks repeated immediately
   before staging act 1; §2 item 3's result for each of the three files; a sentence saying whether any of the close's
   inputs was opened by an Edit or Write call before act 1's push was verified and act 2 passed (§5's opening); and a
   sentence saying whether every read of §2 was made before the act that needs it.
2. The landing commit by its full hash, verified at the object (`git show --stat`), and `origin/master` at it. (The
   close commit and the end-state commit cannot be named in a file the close commit carries: the closing message names
   both, each verified at the object, and `origin/master` at the last.)
3. **Act 2, the start-state guard run:** the whole verdict list, the comparison with the committed artifact, and each
   admitted red named.
4. **Task 5, act by act:** each task's last commit and date (act 3 step 1); the `STATUS.md` counts; the blob and the
   tool's numstat and counts (act 4); the `--apply` printout and the checks after it; the membership movement by field
   (act 5); each of the four artifacts' `--check` before and after and its movement by field (act 6).
5. **E0 to E5, graded**, each with its pointers as §5 act 7 step 2 found them; E5 *"not asserted here"*. **The named
   lists as the pointer table** of §5 act 7 step 6, **the *Register* list and the *Open* pointer list** of step 3,
   and **the commit list** as a pointer to the away-returns section's list (the big dispatch: *"where it would name
   hashes it cannot contain, it points at the git log"*).
6. Every departure from this file or the big dispatch, declared, including any order of reads or acts you could not
   follow; and a sentence saying that no recommendation is written anywhere — in `STATUS.md`, the tool, the report, the
   away-returns section or a commit message.
7. **Every figure in the report is read at its object in this session, with the command or tool that produced it named
   beside it; no figure is copied from this file as a result** (the protocol's figure-by-citation and character-figure
   clauses, carried here as an order). Every line number the report gives is a line number of the file as committed by
   the close commit, unless the sentence giving it says otherwise.
8. **The self-check after the work** (`CLAUDE.md`, its last section), over the diffs of the close commit, answering each
   of these five, the writing side's standing self-check list (`cowork_audit_protocol.md`, carried here as an order):
   (a) the guiding principles the work touches, and whether it conforms (#12 — every moved entry moved by the tool,
   every superseded aiming kept; #6 — the lists pointed at, not copied; D-431 — no figure in `STATUS.md`); (b) the
   conventions — American English in your own words (a record's words placed keep the record's spelling, as the
   standing bars say), no self-invented labels, music-theory words in their musical sense only, every non-musical use
   qualified; (c) every figure and premise cited to its object (D-431); (d) the file-tools rule (D-253); (e) **the
   uncertainty of any comparison the report makes (#24)** — say so if the report makes none.
9. The last sentence, exactly: *"Session 40 of the L3 application ends here. Task 5 is done; the close commit and the
   end-state commit are pushed. The L3 application act is complete. Nothing else was done."*
   (If the session stopped before the close commit, write *"Task 5 stopped as the report says"* in place of the second
   and third sentences; the report is then committed alone, with the subject
   `report: session 40 of the L3 application, Task 5 stopped as the report says`.)

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- this file's banner does not record the record comparison as made (§1 check 0);
- any other check in §1 fails, or a tracked modification §1 check 5 names as a STOP appears;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- a check immediately before staging act 1 fails (§5 act 1);
- the start-state guard run shows a STOP, a population other than 83, or a red outside the fifteen and the three
  admitted (§5 act 2);
- a task's last commit is not found, or its hash or order differs from the expected (§5 act 3 step 1);
- a count after writing the `STATUS.md` entries or the re-aiming differs from the one given (the file restored first;
  §5 acts 3 and 4);
- the two `STATUS.md` blobs of §5 act 4 step 1 differ;
- the forward-bound tool STOPs, or its `--check` fails after the move (restored as §5 act 4 step 4 says);
- a second `--check` of act 6 fails, or a tool there STOPs (that artifact restored);
- a check before the close commit fails, or the away-returns file shows a deleted line (§5 act 7 step 7);
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

A membership movement with no PINNED sentence behind it is a STOP-and-report **for that artifact only** (§5 act 5): the
artifact is restored and left out, the rest goes on, and E5 names its red. A pointer whose heading the search does not
find is corrected where the search shows the right one, and reported; it is never filled from memory. After a STOP,
report what you did and what you did not do. Do not try to repair anything.
