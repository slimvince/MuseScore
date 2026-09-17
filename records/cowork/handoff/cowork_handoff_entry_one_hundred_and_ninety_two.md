# Cowork handoff entry 192 — 2026-09-17

**The current entry point.** Entry 191 is superseded as entry point and stands otherwise; its §3 open list carries
forward (§4 below). Grades: **[checked]** = opened or measured at the file by this sitting; **[relayed]** = taken from
CC's report or chat reply and not checked here.

## 0. State at close — A DISPATCH IS RUNNING

- **Running:** `records/cc/instructions/cc_instruction_root_records_move_finish_commit_two_2026_09_17.md` (§1 item
  8), handed to CC after this entry's last landing; its size is at its landing staging call and it was proved at
  content **[checked]**. It continues the resume dispatch (third issue, 11,857 bytes at landing **[checked]**).
- **Commit 1 exists:** `.git/refs/heads/master` reads `447311137a934ab8e3f51e7abf8e18e7b8d2bd0e` **[checked]** — the
  978 renames **[relayed]**. Nothing pushed.
  **Do not touch it, or its base dispatch, while it runs (D-251).**
- **Its base text:** `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md`, third issue,
  24,430 bytes at landing **[checked]**; CC reads it from blob `a16402ac47ed9f07de68629f299b65fd71eee51e` **[relayed]**.
- **The branch pointer at this sitting's boot:** `5d24edb565b2e0e9efc92e082c163112bd97087f` **[checked]**.
- **The working tree** (the renames now in Commit 1) carries Task 1's 43 quote edits, the register regeneration,
  and the files rewritten by the write modes run so far (third run: discard records, specification document set,
  rulings sort with its surface, finer archive; resume runs 1 and 2: read size, defense share, boot pack; run 2 also period stratum split), all uncommitted
  **[relayed, CC's reports]**. `tools/audit/claude_md_finer_archive.json` is modified and must stay uncommitted (§2).
- **The second backup is still undone.** It is the running batch's push.

## 1. What happened this sitting, in order [each report read whole, checked]

1. Boot per entry 191 §4. Wrote the follow-up dispatch entry 191 §2 asked for (the `…_finish_…` file).
2. **Run 1 stopped at Task 1(a)** (`records/cc/reports/cc_report_root_records_move_finish_2026_09_17.md`). Eight of
   the 43 register quotes homed in `CLAUDE.md` start 39 or 55 lines below their cited line. **Checked at `CLAUDE.md`:**
   D-294 at 976 (cited 937), D-308 at 962 (923), D-200 at 1806 (1751), D-675 at 1714 (1659); D-200 and D-308 quote no
   moved file and drift by the same amounts, so the drift is not caused by the moved names inside the quotes (CC
   relays that the move added no lines; not checked here). **Checked at `gen_cluster_dispositions.py` `verify_backbone()`:** a
   missing quote is reported and skipped; a found quote at another line is `LINE DRIFT`. **Writing side's defect.**
   Second issue: allow exactly those eight `LINE DRIFT` lines; change no cited line (a pre-existing failure is
   reported, not corrected; fixing eight of a drifting family breaks D-204).
3. **Run 2 stopped at Task 0** on a guard refusal of a `tail` CC added (`…_finish_second_2026_09_17.md`). CC's
   defect. Third issue: reports handled by filename pattern; captures read only with Read or Grep.
4. **Run 3 completed Task 1 and three write modes, then stopped** on `gen_claude_md_finer_archive.py` exiting 1
   (`…_finish_third_2026_09_17.md`). **Checked at the tool, line 463:** each ruled "refused" passage is counted by its
   exact wording at a pinned commit in the live `CLAUDE.md`. **Derived by CC, not checked here and not measured per
   passage:** at least three of the four refused passages quote moved files by root name, which the move changed to
   `records/…` paths. `gen_post_split_archive.py` and `gen_claude_md_prune_backlog.py` import the same passages and
   count them in the live file **[checked at their imports and count lines]**.
5. **User ruling (§2).** Then the resume dispatch.
6. **Resume run 1 stopped at Task 2(c)** (`…_finish_resume_2026_09_17.md`): `gen_period_stratum_split.py --check`
   newly failed. **Checked at the tool:** it stores the sha256 of the regenerated `specification_document_set.json`
   (line 409) and its plain run writes only `period_stratum_split.json` (lines 606–607). Same class as the regenerated
   guards, not the ruled class, so no user decision was put. **Writing side's defect:** the guard lists named only
   guards already failing, not ones downstream of a regenerated file. Second issue adds its write mode.
7. **Resume run 2 stopped at Task 2(b)** (`…_finish_resume_second_2026_09_17.md`): its four write modes ran and passed
   **[relayed]**, then the working tree showed one unallowed new record, **this entry**, which the writing side landed
   while the batch ran. **Writing side's defect.** Third issue: start again from Task 0; allow this entry and add it to
   Commit 2, like entries 189–191.
8. **Resume run 3 made Commit 1 and stopped before Commit 2** (`…_finish_resume_third_2026_09_17.md`), on a guard
   refusal of a `cat` CC added. **CC's defect.** Task 2(c) matched the stated pattern: 18 failing, the three ruled
   checks among them **[relayed]**. A new short dispatch, `…_finish_commit_two_2026_09_17.md`, starts at Commit 2.

## 2. The user's ruling, 2026-09-17

On a full surface with four alternatives and a recommendation, the user answered **"I agree on recommendation."**
Ruled: **Alternative A** — finish and push now; leave `gen_claude_md_finer_archive.py`, `gen_post_split_archive.py` and
`gen_claude_md_prune_backlog.py` failing and reported with their cause (the resume dispatch orders them named in the `STATUS.md` entry); do not run their write modes; keep
`claude_md_finer_archive.json` out of every commit. **Not ruled:** how those three tools are settled afterwards.

## 3. Correction to entry 191

Entry 191 §2 guessed the boot-pack failure came from a subject that is not frozen. **Withdrawn, checked at
`gen_derivation_boot_pack.py`:** every subject its `build` loop takes from `WITHHELD` is in `FROZEN`, and `write_all`
writes nothing into a frozen subject's directory; the failure was the manifest. Resume run 1 reports the boot pack's
write mode and check passing with all three subjects frozen **[relayed]**.

## 4. Boot order and what comes next

1. The ordinary session-start read (entry 186's Boot block: `CLAUDE.md` at its six spans, `DECISIONS.md` whole,
   `STATUS.md`, the gating answer), the 118th's bridge-fault section, the 152nd's (v)–(x), the 169th whole. Then this
   entry whole; entry 191 only where pointed.
2. **Read CC's report on the running batch whole:**
   `records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`, and its chat reply (ask the
   user to paste it). Verify any commit it claims at `.git/refs/heads/master` and `.git/refs/remotes/origin/master`.
3. **If it stopped:** read the stop at the objects; check whether the record already answers it before putting it to
   the user. Every earlier report of this line is listed in §1.
4. **If it pushed:** the open questions, one per turn, full surfaces with recommendation, question in a later turn:
   - **The three passage-protection tools:** change them to apply the move's renames when comparing, declare them
     historical records, or restore the old names in the passages. **Establish first, read-only:** which of the four
     refused passages fail, and whether the post-split and prune-backlog failures come from the same passages; and
     whether post-split and prune-backlog are finished acts (finer-archive's own record calls its question CLOSED).
   - **The `CLAUDE.md` line drift:** 35 `LINE DRIFT` lines after Task 1, 27 of them earlier **[relayed]**; cause not
     established.
   - Entry 191 §3's list: the 173 other root `cowork_*.md` files; the 24 unclassified files; CC's five self-check rows;
     entry 189 decision 4.
   - Seen in a listing, not opened: `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_two-1.md`
     beside the 182nd **[checked, name and size only]**.

**Dispatch rules learned this sitting:** a check that compares cited line numbers or exact wording breaks when a file
drifts or its names become paths; a guard list must cover guards downstream of every regenerated artifact, not only
those already failing; tell CC to read captures with Read or Grep only; **the writing side lands nothing in the
repository while a batch runs whose checks enumerate new files.**

## 5. Declared departures of this side

- **No shell command**, in the container or on the device. One folder-access grant (`C:\s\MS`); one names-only
  skeleton of `C:\s`; one listing of `records/cowork/handoff/`. Every repository read was Read or Grep over staged
copies.
- Six project memory files read; nothing written. The verbatim message channel used once. No popup, subagent, web
  access or task list.
- Dispatches and this entry landed by committing twice (a new path unguarded, an existing path guarded by its staged
  modification time, then forced), staged back and proved at content and size.
- **Degradation.** Three writing-side defects (§1 items 2, 6 and 7), each costing a CC run. Under the user's
  standing rule this sitting hands over at a verified stop: the dispatch is landed and proved, and CC is running it.
