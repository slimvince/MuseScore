# CC dispatch — the L3 application, SESSION 2 of several: Task 1 of the L3 application dispatch, first stretch (§L.1 to §L.15), and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_three.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0 and stopped at Task 0's guard-set check (§6 below).
Task 0's commit is `cbde76fd78a244540df64895191a511df186cc29`, verified at the object by the Cowork sitting that wrote
this file.

**This is session 2. It executes the big dispatch's Task 1 (the successor file
`cowork_derived_specification_l3_2026_11_08.md`) for the ledger entries §L.1 to §L.15 only, commits and pushes that
first stretch, writes its report, and STOPS.** Task 1 is divided into four stretches, each ending at a ledger entry's
boundary, because the ledger entries and the ruling records they rest on come to about 1,094 KB together and one
session cannot hold them with the rest of its reading. The four stretches are: §L.1–§L.15 (this session), §L.16–§L.28,
§L.29–§L.41, §L.42–§L.55. Each later stretch gets its own instruction, written after the previous one is verified.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §3,
and only for this session. Where this file and the big dispatch seem to differ on anything §3 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change.** This session writes the successor file by the big dispatch's Task 1, which
places the ruling records' own words; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `cbde76fd78a244540df64895191a511df186cc29`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_2_task_1_stretch_1_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The successor does not exist yet** (the big dispatch's Task 1, *Before the edit*, unchanged):
   `git ls-files --error-unmatch -- cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"` must give a non-zero
   exit, and no file may exist at that path. Otherwise: STOP and report.
5. **The working tree (replaces assumption A1's boot expectation for this session).** Enumerate the working tree with
   `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses `git status`).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree cbde76fd78a244540df64895191a511df186cc29 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the two files §4 item 1 lands (this instruction and handoff entry 1184), plus the
     395 untracked paths session 1 reported and did not land (387 under `scratch_artifacts/`; `.claude/`,
     `Claude outputs/`, `Codex research inventory/`, `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`;
     `tools/extra scores/.mscbackup/`). List every untracked path the tool reports outside those in the report. A
     further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is
     not a STOP (the big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **The fifteen ruling records §L.1 to §L.15 name, each WHOLE, in §L's order** (the file names are at the `### §L.n`
   headings of the big dispatch; §L.10's record included). They are the authority for every amendment this session
   applies: **the record's own words govern** (the big dispatch, §L's opening). Do NOT read the records of §L.16 to
   §L.55.
3. **The derivation WHOLE, §0 to §7, at the git object:**
   `git show e855ff2a38883bc453b3f1c83cb20b9fd89cda05:cowork_blind_derivation_l3_2026_10_17.md`, written to a scratch
   path outside the repository and read there with the Read tool in ranges. It is 127,533 bytes and has no line longer
   than 1,900 characters.
4. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
5. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard
   (its condition in `CLAUDE.md` is not met).
6. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 4 to 255 at this writing; the
   dispatch-protocol clause on the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_four.md` (the current entry point,
   written by the sitting that wrote this file; untracked, §4 item 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_three.md` (the one before it).
7. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
8. **`decisions/group_K.md`, D-674 whole** (from its heading `### D-674` to the next `###` heading): the filing
   convention Task 1 applies.
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 with the shell**, as it is 4,383 bytes long:
     `sed -n '98p' records/cc/instructions/cc_instruction_l3_application_2026_11_08.md | fold -s -w 1000; echo "exit:$?"`
     (if the guard refuses `sed` on the working-tree file, write the blob with `git hash-object -w` and read it with
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`, as
     session 1 did, and declare it);
   - lines 99–394 (the words, the ruling ledger, **the forms — form (a) is the form every amendment is written in**, the
     premise ledger, the declared start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 431–1634 (§L.1 to §L.15, your stretch)**;
   - lines 6100–6571 (Task 1, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 1635–6099 (§L.16 to §L.55, and Task 0); lines 6572–7110
   (Tasks 2 to 5); lines 7136 to the end. Nor the reading file, `FRAMEWORK.md`,
   `cowork_derived_specification_l0_l1_2026_09_03.md`, `tools/audit/gen_status_batch_bound.py` or
   `records/cowork/handoff/cowork_away_returns.md`: each belongs to a later Task's session.

## 3. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 1 applies** (Task 1 (a): *"Each §L entry's Successor — amendments part is applied, in
   ledger order"*) → **§L.1 to §L.15 only, in ledger order.** §L.16 to §L.55 are not applied, read or touched.
3. **Task 1 (c), split by stretch.** Apply here only the parts whose ordering record is one of §L.1 to §L.15:
   - (c) item 1: **L3-S7** (§L.14), **L3-S17** (§L.6), **L3-S23 family (iv)** (§L.11 and §L.12, one amendment),
     **L3-S24** (§L.12), **L3-S16** (ordered by the cadence-features record, §L.5), **L3-S9** and **L3-S42** (ordered by
     the thematic-parallelism record, §L.11). **Not here:** L3-S28, L3-S25 (§L.16), L3-S5 (ii) (§L.17), L3-S39 (§L.20).
   - (c) item 2 (L3-S7's falsifier, §L.14): here.
   - (c) item 3, the added statements: **§L.13's only**. The section `## Statements added by the L3 family rulings` is
     created by this session, after the last derived statement, with §L.13's statement in it.
   - (c) item 4 (OQ-L3-9, §L.17): not here. (c) item 5: unchanged. (c) item 6: unchanged, for this stretch's entries.
   - The `## Notes — lists the records place here, not ruled` section (form (a), last bullet): created by this session
     only if one of §L.1 to §L.15 places a list there; otherwise not created.
   If you find that a part assigned to this session depends on the words of a record outside §L.1 to §L.15, or a part
   not assigned here is ordered by a record inside it: STOP and report for that part; apply the rest.
4. **Task 1 (a) and (b) are applied whole by this session:** the file made from the derivation object; §0 to §4 carried;
   §5 to §7 replaced by the heading and paragraph Task 1 (a) gives (the blob filled in from git); the title and the
   banner of (b). **The ANSWERED set written into the banner is the set this file carries at this commit.** The writing
   side's expectation for §L.1 to §L.15, taken from Task 1 (b)'s own list: OQ-L3-2 (§L.6), OQ-L3-3 (§L.2), OQ-L3-4
   (§L.5), OQ-L3-5 (§L.11), OQ-L3-6 (§L.12), OQ-L3-8 (§L.14), OQ-L3-10 (§L.15) — seven. Re-take it at the file; a
   difference is reported.
5. **One line added beneath the banner, outside it**, because the banner describes the file as amended by all the
   records and this commit carries only fifteen of them (#10). Exactly:

   `*Application in progress: this file carries the amendments of §L.1 to §L.15 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.16 to §L.55 are applied by later Claude Code sessions, one stretch each; the banner above is true of the file only when the last of them removes this line.*`

   Attribute it in the diff table to *"session 2's instruction, §3 item 5"*.
6. **Task 1 (d), one commit for the whole of Task 1** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, commit the
   entries already applied, write in the in-progress line of item 5 the last entry actually applied instead of §L.15,
   and report which entries were applied. If you are inside an entry, do not commit; STOP and report which entries were
   applied to the uncommitted file and that it is not landed.
7. **Task 1 (e), the check before the commit,** is run as written (the diff against the derivation object, every changed
   passage attributed in a table in the report), with these changes for this stretch: the attributions available are
   only this stretch's §L entries and their amendment numbers, (a), (b), the parts of (c) §3 item 3 assigns here, and §3
   item 5's line; the bold-text exceptions are only L3-S7's and L3-S24's statements whole, L3-S17's second sentence and
   L3-S16's feature (6) closing clause; and **every statement and open question that none of §L.1 to §L.15 and none of
   the (c) parts assigned here names is byte-identical to the derivation's.** The commit subject is exactly:

   `application L3, Task 1 stretch 1 of 4 (§L.1 to §L.15): the derived specification as amended by the first fifteen L3 family ruling records written beside the derivation, every amendment citing its record, not ratified`

   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
8. **E1** is checked for this stretch only, as items 3 to 7 restrict it. The full E1 belongs to the session of the last
   stretch.
9. **Where the batch ends for this session.** After §4's acts, this session STOPS. It does not begin §L.16, Task 2 or
   any later Task.

## 4. The acts, in order

1. **Land the writing side's two files first, in a commit of their own.** Exactly two paths, both expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_2_task_1_stretch_1_2026_11_22.md`, and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_four.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entry 1184 and the session 2 instruction of the L3 application landed; Task 1 stretch 1 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 1 for §L.1 to §L.15**, as the big dispatch's Task 1 and §3 above give it, ending with §3 item 7's check, its
   commit and its push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_2_task_1_stretch_1_2026_11_22.md` with the
   items of §5. Commit that ONE path alone, subject exactly:
   `report: session 2 of the L3 application, Task 1 stretch 1 (§L.1 to §L.15) written; stretch 2 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 5. What the report states, and the same in your closing message to the user

1. §1's five results, the two blobs, and the repeat of check 2 before staging.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.1 to §L.15, in order: every amendment by its number, applied (and where), or STOP-and-report (and
   why). The same for each part of (c) §3 item 3 assigns here.
4. The ANSWERED set the file carries, set against §3 item 4's seven.
5. The diff table of §3 item 7, every changed passage attributed.
6. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
7. The last sentence, exactly: *"Session 2 of the L3 application ends here. Stretch 2 of Task 1 is not begun. Nothing else was done."*

## 6. What session 1 established, for the record (relayed here; verified by the Cowork sitting at the objects)

Session 1 committed Task 0 as `cbde76fd78a244540df64895191a511df186cc29` (693 paths added, 4 modified, none deleted)
and pushed it, then stopped at Task 0's guard-set check. Its full guard run showed two failing tools beyond the
thirteen of the declared start state, item 2: `gen_evidence_pin_membership.py` (it counts the ruling records on disk;
the 48 records written since its artifact of 2026-11-07 raised the count from 218 to 266, members and pinned count
unchanged) and `gen_per_session_reading.py` (it finds handoff entries through git; Task 0's commit raised its population
from 505 to 1103). **This session runs no guard**, so neither bears on its acts; both are declared here so that no later
reader takes them for this session's doing. Session 1 wrote no report file; handoff entry 1184 carries its results.

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 4);
- the big dispatch's Task 1, its forms, its standing bars or its findings rule makes something a STOP (an amendment
  that is STOP-and-report under them is reported and the rest applied, as they say);
- §3 item 7's check finds a changed passage it cannot attribute;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §3 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1183. Read at the objects for this file: the
three git reference files; the commit `cbde76fd…` and its tree against `e855ff2a…`'s, folder by folder; the big
dispatch (blob computed from the staged bytes) at lines 98, 161–199, 310–375, 395–430, 6083, 6100–6200, 6539–6571 and
7064–7110, its `### §L.` headings, its (c) item 1 list by search, and every line length; the sizes of the fifteen
records and of §L.1–§L.55; `cowork_audit_protocol.md`'s section from line 180 by size; `cowork_handoff.md`'s top
block by size; the derivation's section headings; `decisions/group_K.md`'s D-674 heading; `tools/audit/gen_evidence_pin_membership.py`
and `tools/audit/gen_per_session_reading.py` at their counting code; `tools/audit/evidence_pin_membership.json`'s counts;
`tools/audit/claude_md_finer_archive.json`'s hash with and without carriage returns; the session 1 instruction whole.
Session 1's guard figures (15 failing, 4 not run, 20 historical, 83 run) and its 395 untracked paths are relayed from
its closing message. The estimate of about 2.6 bytes per token is relayed from Claude Code's context display as the user
pasted it last sitting, measured on `CLAUDE.md` alone. The user's words: the opening instruction with Claude Code's
closing message; "shortened"; "continue"; "continue".*
