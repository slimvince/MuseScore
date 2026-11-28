# Report — the L3 application act, executed under `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`; Task 5 (the close) by session 40

> **★ TASK 5 STOPPED AT §5 ACT 7 STEP 5 OF THIS SESSION'S INSTRUCTION — THE CLOSE COMMIT AND THE END-STATE COMMIT WERE
> NOT MADE. This report is committed alone. Read §0 first; the sections after it were written before the stop and are
> kept as written, except where §0 names a sentence they hold that the stop made untrue.**

> **★ RESUMED BY SESSION 41 (2026-11-28), under `records/cc/instructions/cc_instruction_l3_application_session_41_task_5_resume_2026_11_28.md`, keeping the uncommitted work §0 lists; see §10.**

## 0. The stop

**What happened.** After this report was written (act 7 step 4), act 7 step 5 ran
`python tools/audit/gen_per_session_reading.py --check`. The expected result was a red verdict (exit 1, the new report
being on disk). **It STOPPED instead, exit 2**, printing, whole:
*"STOP: a member of a derived population has no add-commit:
records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_three.md"*.

**Its cause, read at the objects.** The file
`records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighty_three.md` is untracked; it was not in
the working tree at §1 check 5 (the enumeration listed handoff entries 1279 to 1282 only). PowerShell `Get-Item` reads
its last-write time as 2026-11-28 10:07:08 (local time), 14063 bytes, against 10:05:40 for
`tools/audit/per_session_reading.json` as act 6's writing run left it — and act 6's second `--check` of that tool had
passed. So the file was written into `records/cowork/handoff/` during this session, after act 6. Under A1 a further
untracked handoff entry is the writing side's, is not landed and is not by itself a STOP; but the per-session tool
derives its handoff population from the folder on disk, needs an add-commit for each member, and STOPs on one without.
**The file was not opened by this session.**

**Why the session stopped there.** This session's instruction: *"If any expected result does not appear, stop at that
step and report it. Do not continue to the next one"* (its banner), and §7: a check before the close commit that fails
is a STOP-and-report with nothing committed. Step 5's writing run was **not** run, so step 5 is not done; step 7's checks
could not pass with this tool stopping; so step 6 (the away-returns section), act 8 (the close commit) and act 9 (the
end-state run and commit) were **not** done.

**What was done and pushed:** §1's checks; the landing commit `3f7c9faea48fd706372121db2ec757d6a9597820` (§2); act 2
(§3).

**What was done and stands ON DISK, UNCOMMITTED, not restored and not repaired** (each as §4 records it):
`STATUS.md` (act 3's entries and act 4's move), `STATUS_ARCHIVE.md` (act 4's move), `tools/audit/gen_status_batch_bound.py`
(act 4's re-aiming), `tools/audit/status_batch_bound.json` (act 4), `tools/audit/evidence_pin_membership.json` (act 5),
`tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json`, `tools/audit/l3_outgoing_population.json`
and `tools/audit/per_session_reading.json` (act 6). `records/cowork/handoff/cowork_away_returns.md` and
`tools/audit/guard_state.json` are untouched. Handoff entry 1283 is untracked and untouched.

**Sentences below that the stop made untrue, corrected here and not in place:** §6 says the commit list stands in the
away-returns section — that section was not appended; the list is the output of the `git log` command §6 names. §7 says
the end-state portion reports the `tools/audit/stretch_verify/` paths — act 9 was not reached; they are reported here,
at §7, only. E5 (§5) is not asserted, and no end-state run was made. The header's sentence on line numbers *"as the
close commit carries it"* has no close commit to refer to: the big dispatch's and the session reports' line numbers are
those at this report's commit, and the line numbers given for `STATUS.md` (lines 8 to 22) and `STATUS_ARCHIVE.md`
(line 6253) are those of the uncommitted files on disk.

> **Written 2026-11-28 by Claude Code, session 40 of the L3 application**, under
> `records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md` (called **this session's
> instruction** below) and the big dispatch it executes, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`
> (called **the big dispatch**). Boot tip `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e`. Documentation and record-keeping
> only: no algorithm is decided, nothing is ratified, and this report decides nothing. The close commit and the end-state
> commit cannot be named in a file the close commit carries; the closing message to the user names both, and the
> away-returns section's end-state portion names the close commit. Every line number below is a line number of the file
> as the close commit carries it, unless the sentence giving it says otherwise. The big dispatch and the session reports
> are not changed by the close, so their line numbers are the same at the tip and at the close.

## 1. The first checks (this session's instruction §1), the pin, and the reads

- **Check 0, the banner.** The banner records *"THE RECORD COMPARISON MADE 2026-11-28"* (this session's instruction,
  line 3). Held.
- **Check 1, the tip.** Read with the Read tool: `.git/HEAD` = `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both = `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e`. Held.
- **Check 2, the big dispatch.** `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`
  printed `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Held.
- **Check 3, the pin.** This session's instruction was read from the working tree first (the user's opening line
  ordered that read as the first tool call), so the pin took its declared-departure route: **declared here — the file was
  read before it was pinned.** `git hash-object -w` on it printed `0bb3dca8a907656a8651d79cacf3d69fb1a3d210`.
- **Check 4, the close's eleven inputs.** `git diff --quiet e855ff2a… a1938ebc… -- <the eleven>` exit 0, and
  `git diff --quiet a1938ebc… -- <the eleven>` exit 0. Held.
- **Check 5, the working tree.** `python tools/audit/changed_paths.py` (output to the scratchpad, read with the file
  tools) reported 402 changed path records: one tracked modification, `tools/audit/claude_md_finer_archive.json`, and
  401 untracked paths. The modification is line endings only: `git hash-object` on it printed
  `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree a1938ebc… -- <it>` shows the same blob; it is not a
  modification and was not landed. The untracked paths are exactly those check 5 expects: this session's instruction;
  handoff entries 1279, 1280, 1281 and 1282 (1282 is the entry the banner names); 387 under `scratch_artifacts/`
  (a Grep count of the tool's output); `Claude outputs/`; `Codex research inventory/`;
  `docs/research_papers/desktop.ini`; `docs/research_papers/polyph9-release/`; `docs/research_papers/rowe`; the two
  PDFs under `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
  `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md`. **No untracked
  path outside those. No untracked `cowork_rulings_*.md` under `records/cowork/rulings/`.**
- **`CLAUDE.md`** was in this session's context as a loaded project memory file; it was not read again.
- **§2 item 3, the session-start read by size and modification time.** Read with PowerShell `Get-Item` (length, and the
  last-write time in milliseconds since 1970), as sessions 38 and 39 did; declared at §8:
  - `STATUS.md`: 11726 bytes, 1794136674043 — both equal; not read for the session-start read (it was read whole under
    §2 item 7 in any case);
  - `DECISIONS.md`: 120603 bytes, 1794081137207 — both equal; **not read**;
  - `tools/audit/nongating_apparatus_rows.json`: 178066 bytes, 1788814584416 — both equal; **not read**.
- **The checks immediately before staging the landing commit.** Check 2 again: `b5274c2c7b82c171e1b44c1ed79635a34877b142`.
  This session's instruction hashed again: `0bb3dca8a907656a8651d79cacf3d69fb1a3d210`, equal to the pinned hash.
  `git diff --quiet a1938ebc… -- <the eleven>` exit 0. All three held.
- **No Edit or Write call named any of the close's inputs before the landing commit's push was verified and act 2
  passed.** The first such call was the `STATUS.md` edit of act 3 step 2.
- **Every read §2 orders was made before the act that needs it**: all of §2 items 1 to 9 were made before act 1; §2
  item 10 (the session reports, by search) was made at act 3 step 1 and act 7 step 2, which are the acts that need it.

## 2. The landing commit

`3f7c9faea48fd706372121db2ec757d6a9597820`, parent `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e`, subject
`record: handoff entries 1279 to 1282 and the session 40 instruction of the L3 application landed; Task 5 follows`.
Pushed; `.git/refs/remotes/origin/master` read equal to it. `git show --stat` shows exactly five paths added and nothing
else: this session's instruction and handoff entries 1279, 1280, 1281 and 1282.

## 3. Act 2 — the start-state guard run

`python tools/audit/gen_guard_state.py --check` at the tree the landing commit left, before any edit; exit 1 (a
`--check` against the committed artifact, which the verdicts differ from); it wrote nothing. Its last line, verbatim:
*"83 guard(s) run, 15 failing, 4 not run, 20 historical record(s)"*; no `STOP` anywhere in the output (a Grep count of
0); 68 `[PASS]` lines and 15 `[FAIL]` lines (Grep counts).

**The whole verdict list.** FAIL (15): `gen_phase3_gate_partition.py --check`, `gen_filing_convention_application.py
--check`, `gen_artifact_inventory.py --check`, `gen_artifact_inventory_surface.py --check`,
`gen_test_construction_evidence.py --check`, `gen_retirement_caller_check.py --check`,
`decisions/apply_soft_discard.py --check`, `decisions/apply_residue_discard.py --check`,
`gen_evidence_pin_membership.py --check`, `gen_per_session_reading.py --check`, `gen_epoch_write_path.py --check`,
`gen_recognizer_establishment_sort.py --check`, `decisions/gen_cluster_dispositions.py --verify`,
`decisions/gen_home_classification.py --check`, `decisions/gen_phase1p_delegation_bar.py --check` (all under
`tools/audit/`). PASS (68): every other guard of the run, including `gen_status_batch_bound.py --check`,
`gen_session_start_read_size.py --check`, `gen_defense_share.py --check` and `gen_l3_outgoing_population.py --check`.
NOT RUN (4): `gen_ratification_surface_set.py`, `reaim_ratification_surface_paths.py`,
`decisions/gen_verbatim_subject_consistency.py`, `gen_reserved_word_scanner.py`. HISTORICAL (20), as the committed
artifact lists them.

**Against the prediction of this session's instruction §5 act 2:** 83 run, zero STOPs in the runner, and the failing set
is exactly the thirteen of the declared start state, item 2, plus `gen_evidence_pin_membership.py --check` and
`gen_per_session_reading.py --check`. **None of the three admitted tools is red** (`gen_session_start_read_size.py`,
`gen_defense_share.py`, `gen_l3_outgoing_population.py` all PASS). No STOP.

**Against the committed artifact** (`tools/audit/guard_state.json` at the tip; its `summary`: run 83, passing 70, failing
13; its thirteen FAIL entries read by Grep): **exactly two verdicts differ — `gen_evidence_pin_membership.py --check`
and `gen_per_session_reading.py --check`, each PASS → FAIL.** The thirteen standing FAIL verdicts are the same tools; no
other verdict differs.

## 4. Task 5, act by act

### 4.1 Act 3 — the `STATUS.md` entries

**Each task's last commit, at the objects** (`git show -s` for Task 0; `git log -1 a1938ebc… -- <path>` for the others;
output to the scratchpad, read with the Read tool):

| Task | Path searched | Last commit | Commit date (as printed) |
|---|---|---|---|
| 0 | the commit `cbde76fd…` itself | `cbde76fd78a244540df64895191a511df186cc29` | 2026-11-22 20:01:13 +0100 |
| 1 | `cowork_derived_specification_l3_2026_11_08.md` | `0241e328f773cafe7ebfeb83b634f26838a8c268` | 2026-11-22 23:04:52 +0100 |
| 2 | `cowork_blind_derivation_l3_2026_10_17.md` | `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774` | 2026-11-23 09:50:30 +0100 |
| 3 | `ratification_surfaces/cowork_comparison_l3_reading.md` | `8ce907b9962149eb8c7cdff5a8b1610a966d77cb` | 2026-11-27 22:26:44 +0100 |
| 4 | `FRAMEWORK.md` | `2c7a0d2da51d304202e789c5b5f99f0a6c6784d2` | 2026-11-28 05:03:28 +0100 |

Task 3's and Task 4's hashes equal the expected ones. Task 1's hash (`0241e328f7`) is named in session 7's report; Task
2's (`4b6dc3bd4b`) in session 9's report, among others (Grep searches of the session reports). The order by commit date
is Task 0, 1, 2, 3, 4. Every offset is `+0100`, so each date is taken as printed: Task 0 2026-11-22, Task 1 2026-11-22,
Task 2 2026-11-23, Task 3 2026-11-27, Task 4 2026-11-28. The close date is 2026-11-28 (Stockholm time, read with
PowerShell before the edit).

**The edit** (the Edit tool): the prefix `*Last updated: ` moved off the second resume batch's close entry, and the
twelve lines of this session's instruction §3.1 inserted above it, placeholders filled. Read back, lines 1–24. **The
counts** (Grep, counting matching lines): the dated-entry pattern 12; `Last updated: ` 1;
`cc_instruction_l3_application_2026_11_08.md` 1; `Same dispatch` 9; `<DATE-` and `<CLOSE-DATE>` 0; no carriage return.
Each equals the expected count.

### 4.2 Act 4 — the re-aiming and the move

- **The blob.** `git rev-parse e855ff2a…:STATUS.md` and `git rev-parse 2c7a0d2d…:STATUS.md`, one command each, both
  printed `2a137cccb050df0dfea6335ae92d5f28b66fdbf6`. Equal.
- **The five edits of this session's instruction §3.2** (the Edit tool), in the order (e), (d), (c), (b), (a),
  `<ACT-DATE>` filled as 2026-11-28 and `<STATUS-BLOB>` as the blob above.
- **The check before the move.** `git diff --numstat a1938ebc… -- tools/audit/gen_status_batch_bound.py` printed
  `35	5`. Grep counts in the tool: `2c7a0d2da51d304202e789c5b5f99f0a6c6784d2` 3; `<ACT-DATE>` 0; `<STATUS-BLOB>` 0;
  `TASK = "Task 5"` 1; `DISPATCH = "cc_instruction_l3_application_2026_11_08.md"` 1; no carriage return. Each equals
  the expected count.
- **The move.** `python tools/audit/gen_status_batch_bound.py --apply`, exit 0. Its printout, whole: *"wrote
  tools\audit\status_batch_bound.json"*, *"entries moved: 4, 2,337 characters"*, *"byte-present in the archive exactly
  once: True"*, *"absent from the must-read:                True"*. Four entries moved, as predicted: the second resume
  batch's close entry and the three below it saying `Same dispatch`; the two 2026-09-02 entries stayed.
- **After the move.** `gen_status_batch_bound.py --check` exit 0. In `STATUS.md` the dated-entry pattern counts 8 (this
  batch's six at lines 8, 10, 12, 14, 16 and 18, and the two 2026-09-02 entries at lines 20 and 22) and
  `cc_instruction_llm_correction_second_resume_2026_11_08.md` counts 0. In `STATUS_ARCHIVE.md`
  `★ RULING 4's FORWARD BOUND, 2026-11-28` counts 1, at line 6253.

### 4.3 Act 5 — the membership artifact

`gen_evidence_pin_membership.py --check`: exit 1, *"STALE vs the derivation: evidence_pin_membership.json does not
re-derive"*. The writing run: exit 0; its printout: *"generated ratification documents 7; ruling records read 266"*,
*"members 7 — pinned 5, UNRESOLVED 0"*, *"tools carrying a pin constant 8; outside this class 3"*. `--check` again:
exit 0. **The movement, field by field** (`git diff a1938ebc… -- tools/audit/evidence_pin_membership.json`, numstat
`49	1`):

- `counts.ruling_records_read`: 218 → 266;
- the list of ruling records read: 48 paths added, each a ruling record under `records/cowork/rulings/` dated from
  2026-11-08 to 2026-11-22 (from `cowork_rulings_2026_11_08_l3_application_surface_sitting.md` to
  `cowork_rulings_2026_11_22_l3_application_two_uncommitted_edits_sitting.md`), placed in name order; nothing removed;
- **nothing else moved**: `generated_ratification_documents` 7, `members` 7, `members_pinned` 5,
  `members_unresolved` 0 are unchanged context lines of the diff, and no member or pinned entry changed.

The movement is the one expected: records read and records listed larger by the ruling records written since the
artifact. There is **no movement in the members or the pinned set**, so no PINNED sentence was needed or sought. The
artifact is carried in the close commit.

### 4.4 Act 6 — the four artifacts

Each tool's `--check` was run in its own call before its writing run and again after it.

| Tool | `--check` before | Writing run | `--check` after | `git diff --numstat` against the tip |
|---|---|---|---|---|
| `gen_session_start_read_size.py` | exit 1 | exit 0 | exit 0 | 8 8 |
| `gen_defense_share.py` | exit 1 | exit 0 | exit 0 | 1 1 |
| `gen_l3_outgoing_population.py` | exit 1 | exit 0 | exit 0 | 1 1 |
| `gen_per_session_reading.py` (last) | exit 1 | exit 0 | exit 0 | 27 27 |

**The movement, field by field** (each artifact's `git diff` against the tip, read with the Read tool):

- **`session_start_read_size.json`:** `characters_per_member.STATUS.md` 11617 → 11926; `total_characters` 238016 →
  238325; in the two regime-crossing comparisons, `to_total` 238016 → 238325 in each, and `change_in_characters` /
  `change_percent` −129105 / −35.17 → −128796 / −35.08 and −58816 / −19.81 → −58507 / −19.71. All caused by `STATUS.md`
  changing.
- **`defense_share.json`:** `the_whole_ordinary_session_start_read` 238016 → 238325, the imported total above.
- **`l3_outgoing_population.json`:** one `line_number` in a hit record for the term `phrase` in `STATUS.md` (the
  *"★ ARCHIVED 2026-08-17, THE SECOND ACT"* pointer), 22 → 26: that line moved down four lines because six entries were
  added and four moved out. The hit's text is unchanged.
- **`per_session_reading.json`:** the imported session-start figures as above (`STATUS.md` 11617 → 11926; total 238016 →
  238325, at four places); the blind derivation of L3's `characters` 126702 → 127626 (at two places; the cause is Task 2's
  banner); the handoff-entry member: `the_population_count` 505 → 1202, and the three files with the latest add-commits
  changed from entries 581, 583 and 582 (commit `9a2b3c2d…`) to entries 1281, 1282 and 1279 (the landing commit
  `3f7c9faea4…`), their sum 23232 → 28766; the totals that sum those members, 675380 → 682147, 844562 → 851329,
  739121 → 745888 and 974684 → 980527.

**`STATUS.md` was not edited after act 4.** Act 6 therefore ran after the final edit to `STATUS.md`, as Task 5 (d)
orders.

## 5. E0 to E5, graded

Each report named below is `records/cc/reports/cc_report_l3_application_session_<N>_*.md`; its own commit is the
`report: session <N> of the L3 application, …` commit in the commit list (§6). **Departures:** every session report
carries a section headed *Departures* — sessions 2, 4, 5 and 6 at §6; session 3 at §6 (*Departures and authored
choices*); session 7 at §7; session 8 at §7; session 9 at §5; sessions 10, 11, and 15 to 23 at §7; sessions 12, 13, 14
and 24 at §8; sessions 25 to 37 at §7; session 38 at §6; session 39 at §4 (a heading search of the 38 reports).

- **E0 — MET, with the departures named in the record.** Session 1 wrote no report. The Task 0 commit
  `cbde76fd78a244540df64895191a511df186cc29` was graded at its object (`git show --name-status`, written to the
  scratchpad): 697 paths, 693 added and 4 modified, the 4 being the four tracked paths A1 names
  (`docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
  `ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md`,
  `ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md`); nothing deleted. Its guard-set run is
  **[relayed]** in handoff entry 1184 §2 items 1 and 2.
- **E1 — MET, with the departures each report names.** Sessions 2 to 7 (Task 1 stretches 1 to 6): each report's §3
  (entry by entry) and §5 (the diff table); session 7 also §6 (*For the user*). Session 8 (the full Task 1 check): §4
  (the diff table over the whole successor) and §6 (*E1, graded item by item*), whose item 3 (line 218) gathers the
  STOP-and-report items and the points listed for the user.
- **E2 — MET.** Session 9, §3 (*E2, graded*).
- **E3 — MET, with the departures each report names.** Sessions 10 to 37, each at the section of the headings Task 3
  names (§4; session 24 at §5) and at the section of the row-parts given no line (§6; session 24 at §7); session 12 also
  §7 (*§10 entries left standing for rows now placed otherwise*). The headings' wording varies as the record comparison
  found: sessions 10 and 11 head their §4 *The headings Task 3 names*; session 19 heads its §6 *Row-portions this stretch
  gives no line*; sessions 34 to 37 head their §6 *Row-parts and rows this stretch gives no line*. Session 38: §3 (the
  searches), the paragraph *The report headings Task 3 names, for this stretch* inside its §4 (line 169), and §5 (*The
  check before the commit (§4 item 8) and E3 (§4 item 9)*).
- **E4 — MET, with the departures its report names.** Session 39, §3 (*E4, graded*) and §3.4 (*Charter and contract
  amendments left to the user*).
- **E5 — NOT ASSERTED HERE — the one further commit carries it.**

**Each task's diff, attributed by site or passage — POINTERS:** Task 0, the commit's own path list (above); Task 1, the
diff tables of sessions 2 to 7 (§5 each) and session 8's §4; Task 2, session 9's §3; Task 3, each of sessions 10 to 38's
check-before-commit section (§5; session 24 at §6); Task 4, session 39's §3.5 (*The two diffs, attributed site by
site*).

### 5.1 The named lists of Task 5 item 2 — where each stands (POINTERS)

Searched with the Grep tool over the 38 session reports, case ignored (session numbers are the reports the phrase occurs
in):

| List, as Task 5 item 2 names it | Where it stands |
|---|---|
| *rows the act could not place* | sessions 10 to 38, the section of the headings Task 3 names |
| *rows named by more than one record* | sessions 10 to 38, the same section |
| *amendments with no words from the record* | the phrase occurs in no report; session 8's §6, item 3, answers it (E1) |
| *points answered by a record's own derivation, nothing written* | session 12 only |
| *§10 rows a record says leave, not named by row* | sessions 13 to 38 |
| *charter and contract amendments left to the user* | session 39 only, §3.4 |
| *ADOPTED words read at the row* | sessions 10 to 38 |
| *audit questions added* | sessions 12 to 38 |
| *audit questions no longer quarantined* | sessions 12 to 38 |
| *held by ruling* | sessions 11 and 32 |
| *placed outside every charter* | sessions 24 to 38 |
| *rows given no line now* | sessions 11 to 23 |
| *recorded lines not written: no disposition word* | sessions 12 to 38 |
| the decided-against hits not tied to a row number | *decided against* or *decided-against*: sessions 7 and 10 to 38 |

Every search's result equals the writing side's, as this session's instruction §5 act 7 step 2 records it.

### 5.2 The decisions-register supersessions — each §L entry's *Register* paragraph, restated as a list

Read by a Grep of `\*\*Register:\*\*` over the big dispatch (55 matches, one per §L entry, lines 439 to 5902), with the
lines after each match that its paragraph needed. Each line names the decisions-register identities the paragraph names,
with the paragraph's own word for each, as written there.

- §L.1 — none.
- §L.2 — D-477, D-478 and D-481 (supersession at L3 for the application act and the register route to carry).
- §L.3 — D-458, at its L3 home (supersession for the application act and the register route to carry); named, not
  superseded: D-455, D-480, D-485, D-582, D-254.
- §L.4 — D-455, at L3 (supersession for the application act and the register route to carry); D-495 (*"loses its
  subject at L3"*, not called a supersession); named, not superseded: D-336.
- §L.5 — D-336 and D-081 (*"superseded at L3 only"*); D-584 (superseded *"in that respect only"*); named, not superseded:
  D-100.
- §L.6 — D-584 (superseded at L3, in that respect only).
- §L.7 — none superseded; D-096 cited as a ground.
- §L.8 — none.
- §L.9 — none.
- §L.10 — none.
- §L.11 — none.
- §L.12 — D-454 and D-456 (*"the charter overtakes D-454 and D-456"*); named as grounds, not superseded: D-295, D-100.
- §L.13 — D-472 (*"decided against by this ruling, its register status settled at the ratification act"*); named as
  grounds, not superseded: D-605, D-295, D-100.
- §L.14 — none superseded; named as grounds: D-100, D-295, D-472.
- §L.15 — none superseded; named as grounds: D-260, D-261, D-263, D-624, D-030; D-457 named in its check correction.
- §L.16 — none superseded; named as grounds: D-100, D-295, D-297.
- §L.17 — none superseded; named as grounds: D-100, D-295, D-254.
- §L.18 — none superseded; named as grounds: D-022, D-100, D-297, D-295.
- §L.19 — none superseded; named as grounds: D-295, D-599; D-425, D-L3a and D-349 occur only inside a quotation.
- §L.20 — none superseded; named as grounds: D-100, D-599.
- §L.21 — none.
- §L.22 — none.
- §L.23 — none; named as grounds: D-100, D-599.
- §L.24 — none superseded; D-599 named as a ground.
- §L.25 — none; named as grounds: D-100, D-335, D-295, D-599.
- §L.26 — none; named as grounds: D-028, D-599.
- §L.27 — none; named as grounds: D-035, D-030, D-024, D-033, D-099, D-297, D-100, D-581, D-295, D-522, D-229, D-072,
  D-466, D-461, D-480; D-202 named; D-599.
- §L.28 — none allocated; named as a ground: D-607; D-599.
- §L.29 — none allocated; named, not superseded: D-406, D-410, D-411, D-414, D-502, D-506, D-507, D-503, D-293, D-504,
  D-505, D-254, D-599, D-250.
- §L.30 — none; named: D-599, D-250.
- §L.31 — none; named, not superseded: D-502, D-504, D-505, D-599, D-250.
- §L.32 — none; named, not superseded: D-502, D-410, D-507, D-504, D-505, D-599, D-250.
- §L.33 — none allocated; named, not superseded: D-406, D-502, D-599, D-250; D-133 named as a fact recorded.
- §L.34 — none allocated; named, not superseded: D-506, D-599, D-250.
- §L.35 — none allocated; named, not superseded: D-599, D-643, D-503, D-506, D-410, D-250.
- §L.36 — none; named, not superseded: D-599, D-250.
- §L.37 — none; named, not superseded: D-599, D-250.
- §L.38 — none allocated; named, not superseded: D-599, D-406, D-341, D-250; D-410, D-411, D-414 and D-502 named among
  the rows the record read.
- §L.39 — none; named, not superseded: D-599, D-250.
- §L.40 — none; named as a ground: D-522; named: D-599, D-250.
- §L.41 — none; named, not superseded: D-599, D-623, D-100, D-229, D-072, D-250.
- §L.42 — none; named as grounds: D-276, D-524; named: D-599, D-250.
- §L.43 — none; named as grounds: D-033, D-034; named: D-599, D-250.
- §L.44 — none; named as grounds: D-587, D-589, D-590, D-498; named: D-599, D-250.
- §L.45 — none; named: D-599, D-250.
- §L.46 — none; named: D-599, D-250.
- §L.47 — none; named: D-599.
- §L.48 — none; named: D-599, D-250, D-297.
- §L.49 — none; named: D-599, D-250, D-297.
- §L.50 — none; named: D-599, D-100, D-297, D-250.
- §L.51 — none; named: D-297, D-599, D-250.
- §L.52 — D-479 (*"superseded at its L3 home only so far as its boundaries are picked boundaries that decide a phrase
  end"*, for the application act and the register route to carry); named: D-599, D-250.
- §L.53 — none; named: D-599, D-250.
- §L.54 — none; named: D-674, D-599, D-250.
- §L.55 — none; named: D-599, D-250.

**This batch writes nothing into `DECISIONS.md` and allocates no `D-NNN`**, as §L's opening paragraph on the
supersessions fixes (the big dispatch, line 410).

### 5.3 The points that are not this batch's — POINTERS

Every §L entry's *Open, for the releasing sitting* and *Carried open by the record* paragraphs stand in the big dispatch
at these lines (a Grep of `\*\*Open, for the releasing sitting:\*\*` — 51 lines, one of them, line 620, not at a line's
start — and of `^\*\*Carried open by the record:\*\*` — 54 lines; §L.1 carries neither):

§L.2 — Carried open, line 527 · §L.3 — Open, line 620; Carried open, line 614 · §L.4 — Open, 676; Carried open, 696 ·
§L.5 — Open, 754; Carried open, 773 · §L.6 — Open, 851; Carried open, 890 · §L.7 — Carried open, 940 · §L.8 — Open,
974; Carried open, 1004 · §L.9 — Carried open, 1037 · §L.10 — Open, 1061; Carried open, 1078 · §L.11 — Open, 1133;
Carried open, 1166 · §L.12 — Open, 1251; Carried open, 1323 · §L.13 — Open, 1381; Carried open, 1414 · §L.14 — Open,
1489; Carried open, 1535 · §L.15 — Open, 1593; Carried open, 1630 · §L.16 — Open, 1713; Carried open, 1773 · §L.17 —
Open, 1867; Carried open, 1922 · §L.18 — Open, 1987; Carried open, 2008 · §L.19 — Open, 2088; Carried open, 2132 ·
§L.20 — Open, 2217; Carried open, 2247 · §L.21 — Open, 2305; Carried open, 2319 · §L.22 — Open, 2373; Carried open,
2394 · §L.23 — Open, 2471; Carried open, 2512 · §L.24 — Open, 2570; Carried open, 2613 · §L.25 — Open, 2678; Carried
open, 2723 · §L.26 — Open, 2792; Carried open, 2821 · §L.27 — Open, 2900; Carried open, 2949 · §L.28 — Open, 3004;
Carried open, 3035 · §L.29 — Open, 3100; Carried open, 3142 · §L.30 — Open, 3207; Carried open, 3245 · §L.31 — Open,
3304; Carried open, 3338 · §L.32 — Open, 3412; Carried open, 3444 · §L.33 — Open, 3506; Carried open, 3535 · §L.34 —
Open, 3600; Carried open, 3649 · §L.35 — Open, 3706; Carried open, 3746 · §L.36 — Open, 3829; Carried open, 3881 ·
§L.37 — Open, 3948; Carried open, 3981 · §L.38 — Open, 4052; Carried open, 4109 · §L.39 — Open, 4189; Carried open,
4241 · §L.40 — Open, 4301; Carried open, 4346 · §L.41 — Open, 4424; Carried open, 4468 · §L.42 — Open, 4536; Carried
open, 4575 · §L.43 — Open, 4638; Carried open, 4670 · §L.44 — Open, 4732; Carried open, 4787 · §L.45 — Open, 4844;
Carried open, 4875 · §L.46 — Open, 4952; Carried open, 4996 · §L.47 — Open, 5062; Carried open, 5101 · §L.48 — Open,
5164; Carried open, 5205 · §L.49 — Open, 5279; Carried open, 5304 · §L.50 — Open, 5379; Carried open, 5407 · §L.51 —
Open, 5479; Carried open, 5510 · §L.52 — Open, 5588; Carried open, 5632 · §L.53 — Open, 5706; Carried open, 5730 ·
§L.54 — Open, 5776; Carried open, 5796 · §L.55 — Open, 5893; Carried open, 5905.

They are **NOT YOURS, and untouched beyond what the Tasks write.** Every item this dispatch marked as authored and
overrulable before Task 0, where its mark has been brought into line, stands as the user ruled it at the record that
mark names; NOT YOURS, and untouched beyond what the Tasks write.

## 6. Every commit of the batch

The list of every commit from Task 0 up to and including the landing commit stands, whole, in the away-returns section
this close appends to `records/cowork/handoff/cowork_away_returns.md`; it was produced by
`git log --reverse --format="%H %ci %s" e855ff2a38883bc453b3f1c83cb20b9fd89cda05..3f7c9faea48fd706372121db2ec757d6a9597820`
(116 commits). The close commit and the end-state commit follow it; for those, see the git log.

## 7. The plan lines, and the plan's tell

*"The check turn and the ratification act are the writing side's; the ratification act is a separate decision surface
over the successor (Task 3 (d): §15 of the reading file still reads NOTHING), where the points above return."*

**The plan's tell: YES — one thing.** Besides the landed paths of Task 0, the successor, the derivation's banner, the
reading file's added lines and sections and the sentences Task 3 (d) writes into its existing lines, the four
`FRAMEWORK.md` sites with their notes, S-50 of the derived L0/L1 specification, the Task-5 files and the report (and the
handoff entries, session instructions and session reports landed under the split into sessions, Ruling 1 of
`records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`, with the one line of
session 8's report that session 9 corrected), **the batch added seven files under `tools/audit/stretch_verify/`** —
`README.md`, `blobhash.py`, `blobout.py`, `counts.py`, `gitobj.py`, `rebuild.py`, `treediff.py` — in the commit
`53b3f2db77af5d31562f29ffeea215ca5a755aad` (subject *"record: handoff entries 1241 to 1243, the session 28 instruction of the L3 application and
the stretch verification scripts landed; Task 3 stretch 19 follows"*), and edited the README's banner in the commit
`8dfffc59c9bbaa4df18e9f92df4f3369cfa5f834`. Found by `git diff --name-status e855ff2a… 3f7c9faea4…` (written to the scratchpad and searched with the
Grep tool for every path not ADDED under `records/` or `ratification_surfaces/`). These paths lie outside the ADDED
classes this session's instruction §5 act 9 step 3 names, so the end-state portion reports them as a STOP-and-report
under A5; **nothing is repaired.** The guard population is unchanged at 83 (act 2), so none of them is an enrolled
guard.

## 8. Departures from this session's instruction or the big dispatch, declared

1. **The pin was taken after the first read** of this session's instruction (§1 check 3's declared-departure route).
2. **§2 item 3 was read with PowerShell `Get-Item`, not with the file tools**, which give neither size nor modification
   time. Only those two attributes were read, and no file content.
3. **One shell command named a working-tree file:** while learning the usage of `tools/audit/changed_paths.py`, a
   command opened with `head -40 tools/audit/changed_paths.py >/dev/null` before running the tool's `--help`. Its output
   was discarded and nothing of the file entered this session, but it is a shell read of a working-tree file, which the
   file-tools rule (D-253) forbids. Recorded, not repeated.
4. **Two reads outside §2's list**, made to learn how earlier sessions read size and modification time: a Grep of the
   session 39 report for *modification time*, and the Read tool on its lines 34–37 and 196–203. **One further read**
   outside §2's list: `tools/audit/guard_state.json` at lines 1643–1649 and its FAIL entries by Grep, which act 2's
   comparison with the committed artifact needs.
5. **The five tool edits of act 4 step 2** were sent together, each anchored by the text of its site; the sites had been
   read at §2 item 6, not re-read immediately before each edit. Each anchor's text is the text §3.2 states as standing
   there, an Edit fails on any other text, and the numstat check (35 added, 5 deleted) and the counts confirmed the
   result.
6. **The heading search of act 7 step 2** used `^## ` over all 38 reports and `^### ` over session 39's report only,
   where §3.4 was the pointer to confirm; and the session 38 paragraph was found by a search of its text. The phrase
   searches were run with the Grep tool's regular-expression search on the literal phrases, case ignored; *decided
   against* and *decided-against* were run as one pattern. To place each *Open* and *Carried open* line under its §L
   entry, the §L headings were found by a Grep (`^#+ .*§L\.\d+`); nothing of §L was read beyond the matched lines and the
   lines four *Register* paragraphs needed (lines 611–612, 3138–3140, 3645–3647, 5629–5630).
7. **A copy** of `tools/audit/per_session_reading.json`, as act 6 left it, was made to the scratchpad with `cp`, as the
   base for act 7 step 5's diff *"against the one act 6 left"*, which no commit holds.
8. **An unordered `git diff --name-status`** from `e855ff2a…` to the landing commit was run before this report was
   final, so that the plan's tell (§7) could be answered at the objects; act 9 step 3's ordered run, to the close
   commit, follows it.
9. **The commit messages** carry the subjects this session's instruction gives, exactly, followed by a
   `Co-Authored-By` attribution line in the message body.
10. **After the stop (§0):** a Glob of `records/cowork/handoff/` and `records/cowork/rulings/`, and a PowerShell
    `Get-Item` read of the size and last-write time of handoff entry 1283, `tools/audit/per_session_reading.json` and this
    report, to establish the stop's cause. No content of entry 1283 was read.

**No recommendation is written anywhere** — not in `STATUS.md`, the tool, this report, the away-returns section or a
commit message.

## 9. The self-check after the work (`CLAUDE.md`, its last section), over the diffs of the close commit

The diffs re-read: `STATUS.md` (act 3's six entries and the prefix move, then the tool's move), `STATUS_ARCHIVE.md` (the
tool's appended block), `tools/audit/gen_status_batch_bound.py` (35 added, 5 deleted), the six regenerated artifacts
(§4.3, §4.4), this report, and the away-returns section.

- **(a) The guiding principles.** #12: every moved entry was moved by the tool, verbatim, from the base commit's own
  object, and the superseded aimings stay in the tool's comments and in `PREVIOUS_AIMINGS`; nothing was deleted by hand.
  #6: the named lists and the *Open* points are pointed at, not copied; the *Register* list is restated because §L's
  opening paragraph fixes that restatement. D-431: the six `STATUS.md` entries carry no figure. #14: no behavior
  change; nothing ratified.
- **(b) The conventions.** American English in this session's own words; record words placed keep the record's spelling
  (for example *traveling*, as the big dispatch now spells it). No self-invented labels. The bare word *score* does not
  occur in this session's own words except as *corpus of scores*; *key*, *measure*, *note* and *register* are used only
  in qualified forms (*decisions register*, *the open-items register*).
- **(c) Every figure and premise cited to its object.** Each figure above is named beside the command or tool that
  produced it in this session; no figure is copied from this session's instruction as a result.
- **(d) The file-tools rule (D-253).** Working-tree files were read with the Read and Grep tools; shell commands were git
  object queries, the ordered tools, the size-and-time read of declared departure 2, and the two declared exceptions
  (departures 3 and 7).
- **(e) Uncertainty (#24).** This report makes no comparison whose sampling uncertainty applies: every comparison is
  exact equality of hashes, counts or verdicts.

## 10. Session 41 — Task 5 resumed

> **Written 2026-11-28 by Claude Code, session 41 of the L3 application**, under
> `records/cc/instructions/cc_instruction_l3_application_session_41_task_5_resume_2026_11_28.md` (called **this
> session's instruction** in this section), on the user's ruling "1" of 2026-11-28 (handoff entry 1284 §0): keep the work
> session 40 left uncommitted on disk, and resume. Boot tip `a58acdb592e5005266555d7f8b1bd986a7a25b2e`. Documentation and
> record-keeping only; nothing is ratified and this section decides nothing. **This section is final when written**
> (this session's instruction §4 act 4). The last regeneration, the away-returns section, the close commit and the
> end-state commit come after it; they are recorded in the away-returns section and in the closing message to the user,
> not here. Every line number in this section is a line number of a file as it stands at this session's landing commit,
> unless the sentence says otherwise.

### 10.1 The first checks (this session's instruction §1), the pin, and the reads

- **Check 0, the banner.** It records *"THE RECORD COMPARISON MADE 2026-11-28"* (this session's instruction, line 3).
  Held.
- **Check 1, the tip.** Read with the Read tool: `.git/HEAD` = `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both = `a58acdb592e5005266555d7f8b1bd986a7a25b2e`. Held.
- **Check 2, the two instructions.** `git hash-object` on the big dispatch printed
  `b5274c2c7b82c171e1b44c1ed79635a34877b142`; on session 40's instruction, `0bb3dca8a907656a8651d79cacf3d69fb1a3d210`;
  and `git ls-tree a58acdb… -- <session 40's instruction>` showed the blob `0bb3dca8a907656a8651d79cacf3d69fb1a3d210`.
  Held.
- **Check 3, the pin.** This session's instruction was read from the working tree first (the user's opening line ordered
  that read as the first tool call), so the pin took its declared-departure route: **declared here — the file was read
  before it was pinned.** `git hash-object -w` on it printed `ca81a43a259f3d25e1b51460a540bb3bb663ee42`.
- **Check 4, the nine kept files and the other inputs.**
  - `git diff --quiet a58acdb… -- records/cowork/handoff/cowork_away_returns.md tools/audit/guard_state.json records/cc/reports/cc_report_l3_application_2026_11_08.md`:
    exit 0.
  - `git diff --numstat a58acdb… -- <path>`, one call per path, printed (added, deleted):
    `tools/audit/gen_status_batch_bound.py` 35 5; `tools/audit/evidence_pin_membership.json` 49 1;
    `tools/audit/session_start_read_size.json` 8 8; `tools/audit/defense_share.json` 1 1;
    `tools/audit/l3_outgoing_population.json` 1 1; `tools/audit/per_session_reading.json` 27 27. Each equals the
    expected count.
  - Recorded with no expected value, by the same command: `STATUS.md` 8 4; `STATUS_ARCHIVE.md` 10 0;
    `tools/audit/status_batch_bound.json` 33 11. `python tools/audit/gen_status_batch_bound.py --check`: exit 0.
  - Grep tool, counting matching lines, on `STATUS.md`: the dated-entry pattern `^\*(Last updated: )?20\d\d-\d\d-\d\d`
    8; `Same dispatch` 6; `Last updated: ` 1; `cc_instruction_llm_correction_second_resume_2026_11_08.md` 0; a carriage
    return 0. On `STATUS_ARCHIVE.md`: `★ RULING 4's FORWARD BOUND, 2026-11-28` 1. Each equals the expected count.
  - `python tools/audit/gen_evidence_pin_membership.py --check`: exit 0.
  - **Added, unordered (declared at §10.5):** `git diff --quiet a1938ebc… a58acdb… -- <the nine kept files>` gave exit 0,
    so the two commits between session 40's boot tip and this session's boot tip change none of the nine; the numstat
    counts above are therefore the same against either tip.
- **Check 5, the act-6 blob.** `git hash-object -w tools/audit/per_session_reading.json` printed
  `78186966e1b5bc33a35364c0f4ba6ff04f58f960`.
- **Check 6, the working tree.** `python tools/audit/changed_paths.py` (output to the scratchpad, read with the file
  tools) reported 410 changed path records: 10 tracked modifications and 400 untracked paths.
  - The tracked modifications are exactly the nine kept files and `tools/audit/claude_md_finer_archive.json`. That one is
    line endings only: `git hash-object` on it printed `1df4f20771b6782cbb965c293db4d445bc7ec892`, and
    `git ls-tree a58acdb… -- <it>` showed the same blob; it is not a modification and was not landed.
    `tools/audit/changed_paths_establishment.json` was **not** listed as modified, so the foreseen movement did not
    appear. No other tracked modification.
  - The untracked paths are exactly those check 6 expects: this session's instruction; handoff entries 1283, 1284 and
    1285 (1285 is the entry the banner names); 387 under `scratch_artifacts/` (a Grep count of the tool's output);
    `Claude outputs/`; `Codex research inventory/`; `docs/research_papers/desktop.ini`;
    `docs/research_papers/polyph9-release/`; `docs/research_papers/rowe`; the two PDFs under `external resarch summary/`;
    `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
    `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md`. **No untracked
    path outside those; no untracked path under `records/cowork/rulings/`; under `records/cowork/handoff/` only the
    three entries act 1 lands.**
- **`CLAUDE.md`** was in this session's context as a loaded project memory file; it was not read again.
- **§2 item 3, the session-start read by size and modification time.** Read with PowerShell `Get-Item` (length, and the
  last-write time in milliseconds since 1970), as sessions 38 to 40 did; declared at §10.5:
  - `STATUS.md`: 12041 bytes, 1795856653795 — both equal; read whole under §2 item 7 in any case;
  - `DECISIONS.md`: 120603 bytes, 1794081137207 — both equal; **not read**;
  - `tools/audit/nongating_apparatus_rows.json`: 178066 bytes, 1788814584416 — both equal; **not read**.
- **The big dispatch was not read by the Read tool and not searched** (§2 item 10); only its blob was taken.
- **The checks immediately before staging act 1.** Check 2 again: `b5274c2c7b82c171e1b44c1ed79635a34877b142`,
  `0bb3dca8a907656a8651d79cacf3d69fb1a3d210`, and the `git ls-tree` blob `0bb3dca8a907656a8651d79cacf3d69fb1a3d210`.
  This session's instruction hashed again: `ca81a43a259f3d25e1b51460a540bb3bb663ee42`, equal to the pinned hash.
  `git diff --quiet a58acdb… -- <the away-returns file, the guard artifact, this report>`: exit 0. All held.
- **No file was edited before act 1 was committed, pushed and verified.** The first Edit call of this session is the
  first insertion of act 4.

### 10.2 This session's landing commit

`4a07f73f639ce8edde6d217c4ff60fccea9643cc`, parent `a58acdb592e5005266555d7f8b1bd986a7a25b2e`, subject
`record: handoff entries 1283 to 1285 and the session 41 instruction of the L3 application landed; Task 5 resumes`.
Pushed; `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read equal to it. `git show --stat` shows
exactly four paths added (782 insertions) and nothing else: this session's instruction and handoff entries 1283, 1284
and 1285. The nine kept files were not staged.

### 10.3 Acts 2 and 3

- **Act 2.** `python tools/audit/changed_paths.py` again (output to the scratchpad, read with the Grep tool): 406
  changed path records; the tracked modifications exactly the ten check 6 recorded, nothing added; **no untracked path
  under `records/cowork/handoff/` or `records/cowork/rulings/`.** Held.
- **Act 3**, each `--check` in its own call, output to the scratchpad: `tools/audit/gen_session_start_read_size.py`
  exit 0; `tools/audit/gen_defense_share.py` exit 0; `tools/audit/gen_l3_outgoing_population.py` exit 0. **None was red,
  so no writing run was made and no artifact was rewritten**; session 40's act-6 artifacts stand as §4.4 records them.

### 10.4 The sentences of §0 that the stop made untrue

The sentences of §0 that the stop made untrue — that the close commit and the end-state commit were not made, that the
away-returns section was not appended, that E5 is not asserted and no end-state run was made, and that the
`tools/audit/stretch_verify/` paths are reported at §7 only — **are overtaken by this session as far as the close and the
end state go**: the last regeneration, the away-returns section, the close commit and the end-state run and commit are
made after this section, as this session's instruction §4 acts 5 to 9 order. **§0 itself is kept as written (#12).**

### 10.5 Departures from this session's instruction, session 40's instruction or the big dispatch, as far as act 4

1. **The pin was taken after the first read** of this session's instruction (§1 check 3's declared-departure route).
2. **§2 item 3 was read with PowerShell `Get-Item`, not with the file tools**, which give neither size nor modification
   time; one call for the three files. Only those two attributes were read, and no file content.
3. **One added, unordered check** at §1 check 4: `git diff --quiet a1938ebc… a58acdb… -- <the nine kept files>`, a git
   object query by explicit hash, to establish at the objects what the instruction's note leaves to the numstat runs.
4. **`python tools/audit/changed_paths.py --help`** was run once, to the scratchpad, to learn the tool's options; and
   once with `--staged`, unordered, after staging act 1, to see that exactly the four paths were staged. Both are the
   sanctioned tool; neither reads file content.
5. **The reads of §2 items 6, 7 and 9 were made in one parallel call, and item 8 after it**, so item 8 was read after
   item 9 rather than before it. All of §2 was read before act 1.
6. **Session 40's instruction was read in two consecutive ranges** (lines 1–577, then 578–686), because the Read tool
   truncates a file of that size; together they are the whole file. The batch report was read whole in one call.
7. **The checks immediately before staging act 1 were sent as one shell call** carrying five commands, each with its own
   `echo "exit:$?"`; this session's instruction orders those checks run again but does not order a call per command
   there.
8. **The commit message** carries the subject this session's instruction gives, exactly, followed by a `Co-Authored-By`
   attribution line in the message body, as session 40's commits did (§8 item 9).
9. **One Grep call was refused** by the tool (a look-ahead pattern it does not support) and was replaced by counting and
   reading the scratchpad listing; nothing was read by it.

**No recommendation is written anywhere** — not in `STATUS.md`, the tool, this report, the away-returns section or a
commit message.

### 10.6 The self-check after the work (`CLAUDE.md`, its last section), over this session's diffs as far as act 4

The diffs re-read: this report's two insertions (the pointer line after the banner, and this section). **No artifact was
rewritten at act 3.** The nine kept files were not edited by this session.

- **(a) The guiding principles.** #12: nothing in this report was deleted or rewritten; the extension is insertions only,
  and §0 stands as written. #6: this section points at §4.4 and the earlier sections rather than restating them; the
  numbers it gives are this session's own readings. D-431: no number was written into `STATUS.md`. #14: no behavior
  change; nothing ratified.
- **(b) The conventions.** American English in this session's own words; no self-invented labels (every name used is the
  one the instructions or the files give); the bare words *score*, *key*, *note*, *measure* and *register* do not occur
  in a non-musical sense in this session's own words — *corpus of scores* and *the decisions register* are the qualified
  forms used.
- **(c) Every number and premise cited to its object.** Each hash, count and exit code above is named beside the command
  or tool that produced it in this session; none is copied from this session's instruction as a result.
- **(d) The file-tools rule (D-253).** Working-tree files were read with the Read and Grep tools; shell commands were git
  object queries by explicit hash, the ordered tools, git staging, commit and push, and the size-and-time read of
  departure 2.
- **(e) Uncertainty (#24).** This section makes no comparison whose sampling uncertainty applies: every comparison is
  exact equality of hashes, counts, exit codes or path lists.
