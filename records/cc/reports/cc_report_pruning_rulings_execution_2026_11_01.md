# CC report — the pruning iteration, step 4, first dispatch: Rulings 1 and 3 attempted, NEITHER committed; Rulings 2 and 4 carried by this batch's own form (2026-11-01)

> **STATUS: SESSION REPORT.** Claude Code, 2026-11-01, executing
> `records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md` (pinned at Task 0 as blob
> `17d9d39c487079ba18fb6ba1380b8ad8750ca822`, 102,666 bytes). **This report decides nothing.** It is the REPORT PROPER of
> Ruling 4's two-file form; its APPENDIX is named in §10. **Documentation only; no algorithm change.**

## 0. The outcome in one paragraph

Task 0 landed the dispatch, the ruling record and handoff entries 464 to 466 (`8112c4d226`, pushed). **Task 1 (Ruling 1)
and Task 2 (Ruling 3) were each carried out, byte-reconciled with their planted faults, and then NOT COMMITTED** under the
dispatch's A2 ★ rule — a red the dispatch did not predict, at the task's own check run, means the task's edits are reversed
to the Task 0 blobs and the batch goes on. Task 1's two unpredicted reds are **standing reds the batch did not cause** (red
at the reversed tree too); Task 2's four unpredicted reds are **caused by Task 2's own edits** (green again after the
reversal). Every reversed file was proved equal to its `<T0>` blob by `git hash-object`. The close ran in full. The two
rulings therefore remain to be executed by a later dispatch; §8 names what that dispatch's predictions would need.

## 1. The ordered first read

- **First tool call, exactly:** one `Read` of `c:\s\MS\records\cc\instructions\cc_instruction_pruning_rulings_execution_2026_11_01.md`,
  nothing else in the call and nothing in parallel. It returned a PARTIAL view at the tool's page limit (lines 1–602 of
  1,157); the second call read lines 603–1157 of the same file, before anything else — **declared**.
- **What reached my context as injected context at boot, each by name:** the whole of `CLAUDE.md` (as project instructions);
  the memory index `MEMORY.md`; the user's e-mail address; a git status snapshot (branch, the one standing modification,
  untracked paths, five recent commits); the commit-attribution reminder; the environment block; the skills list; the
  Claude Docs connector's instructions; the deferred-tools list.
- **Ruling 2's eight-line check — PASSED; the six-span read was NOT performed.** Each line read at the tree with the file
  tool and compared with the injected copy:

  | Line | As read at the tree | As injected |
  |---|---|---|
  | 1 (first) | `# Claude Code — Standing Instructions for This Repository` | identical |
  | 3 | `## Guiding principles` | identical |
  | 313 | `## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-26)` | identical |
  | 488 | `## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)` | identical |
  | 704 | `**Always read these two files at the start of every session:**` | identical |
  | 1536 | `## Conventions` | identical |
  | 1989 | `## The self-check after every coding exercise (user-directed, 2026-07-11)` | identical |
  | 1998 (last carrying text) | `memory of writing it. This applies to CC sessions and Cowork sessions alike.` | identical |

  The file object at `<T0>` is 170,942 bytes and ends with one newline (read at the scratch copy). *(The ruling's bound
  holds: an omission inside a span would pass this check.)*
- **Then, in order:** `STATUS.md` whole; `DECISIONS.md` whole (four ranges, 861 lines); `BUILD_AND_TEST.md` whole (the
  condition is met); rule (a)'s `gating_ids` (222 identities, read whole, no index read); `cowork_audit_protocol.md` lines
  180–1606, the dispatch-protocol section to the file's end, every marked `###` section; the ruling record whole; entries
  464, 465 and **466 whole (466 exists at boot — it is the current handover block, not 465 as the dispatch's (4) supposed)**;
  the 2026-10-07 record at Ruling 6 (lines 196–224); `CLAUDE_ARCHIVE.md` whole; the generator whole; the backbone at lines
  1–36 and 1081–1082; `DECISIONS_ARCHIVE.md` whole; the split application's `DECISIONS.md` entry (lines 2083–2126); the
  step-1 dispatch at lines 223–310. Also read, to know the 26 ruled terms 3(a) names: the step-1 dispatch line 220 and
  `L3_KEYWORDS` at `tools/audit/gen_l3_outgoing_population.py:155-164`.

## 2. The capacity judgment (1(a)), quoted whole

```
CAPACITY JUDGMENT BEFORE TASK 1 — written after the 0(g) BEFORE captures, before any edit.

What Tasks 1 and 2 do. Task 1 replaces two bracketed former wordings in CLAUDE.md's decision-surface
block with dated pointers and appends both, verbatim, to CLAUDE_ARCHIVE.md; proved by a scratch
reconciliation with two planted faults; one commit. Task 2 makes eight edits to
gen_decisions_register.py, regenerates DECISIONS.md, appends the four classes and the three old
sentences verbatim to DECISIONS_ARCHIVE.md; proved the same way with two planted faults; one commit.

What the ordered reads took, by my own account. The largest were DECISIONS.md whole (about 860
lines), the dispatch-protocol section of cowork_audit_protocol.md (lines 180 to 1606), the dispatch
itself (1157 lines, two ranges), the generator whole and BUILD_AND_TEST.md whole. The protocol
section and DECISIONS.md together took the most. The eight-line check of Ruling 2 replaced the
six-span read of CLAUDE.md (the injected copy is in context).

Whether a summary of my context has fallen. No. No summary of this session's context has fallen
at the time of writing.

What the batch still owes after Task 2. The close (STATUS.md entries and the prefix move, the
forward-bound re-aim and --apply, the A2 regenerations, the two-file report and its appendix, the
away-returns section, the close commit) and the end state (a full guard run in write mode, the
classification check, the end-state section, its commit).

Judgment. The proof scripts for Tasks 1 and 2 (the record check, the excerpt check and both
reconciliations) are already written in scratch and the 1(b) record check and 2(a) excerpt check
have already passed on git-object copies. The remaining edits are small and located. I judge I can
finish both tasks whole and still close and reach the end state; the risk is context length, and
it is mitigated by keeping every printout in scratch files and quoting only what the report needs.
```

**No summary of this session's context fell** at any point up to the writing of this report.

## 3. Task 0 — landed, pushed

- **0(a)** pin: blob `17d9d39c…`, `git cat-file -s` 102,666; re-hashed with `--no-filters` immediately before staging, equal.
- **0(b)** both ref files `a18148e5…`; `git show --stat` of the four hashes, each in its own command: `a18148e5` ← `d17a84af`
  ← `91e45d62` ← `023353b2` ← `aa0b8155`, subjects and file lists as the FACT states.
- **0(c)** A1 (§6). Every named path's `git diff --stat a18148e5 -- <path>` empty (29 paths); the five landing paths untracked.
- **0(d)** last bytes, at blobs written `--no-filters`: dispatch 102,666; record 28,805 (`ce715295…`); entry 464 17,607
  (`40e857eb…`); entry 465 10,793 (`9dab0095…`); entry 466 6,295 (`cd911c01…`). Each ends with a newline after a complete
  line; zero zero-bytes in each.
- **0(e)** evidence pin: `--check` red (*"STALE vs the derivation"*); write mode; `--check` green (*"ruling records read
  171"*, members 7, pinned 5, unresolved 0). `git diff 7c29492a… f460a683…` (tip blob vs new blob): exactly
  `counts.ruling_records_read` 170 → 171 and the one path added to `ruling_records_read` — **as predicted; no member, route
  or state moved.** Staged set proved (6 paths); commit `8112c4d2260d381dd35fe050df6837bb0488bcf7`, subject `record:
  entries 464 to 466, the pruning-iteration ruling record and the step-4 first dispatch` (entry 466 exists); push line
  `a18148e529..8112c4d226  master -> master`; `origin/master` read equal.
- **0(f)** opening capture (`--check`): header *"STALE vs the run: guard_state.json does not re-derive"*; **83 run, 14
  failing, 4 not run, 20 historical; zero STOPs**; failing set = the thirteen + `gen_per_session_reading.py --check` —
  **exactly A2**. Classification `--check`: exit 2, STOP naming exactly the five relayed tools.
- **0(g)** BEFORE: `gen_session_start_read_size.py --check` green; `gen_defense_share.py --check` green; the decisions-register generator's `--check`
  *"the register matches the data (20 files: the index + 19 group files)"* — **both preconditions met**;
  `gen_cluster_dispositions.py --verify` exit 1 with six LINE DRIFT lines (D-196, D-253, D-254 in `CLAUDE.md`, +12; D-268,
  D-269, D-601 in `cowork_confidence_contract.md`, +18); `reaim_home_anchors.py --check` lists the same six, *"anchors
  drifted: 6"*.

## 4. Task 1 — Ruling 1: carried out, reconciled, then NOT committed (A2's ★ case)

- **1(b) the record check — PASSED.** The sentence as read at the source, line breaks shown: `- **Carried for the next
  dispatch (not applied here):** amend \`CLAUDE.md\` Conventions, *How a decision surface\n  is written*, step 4, replacing
  the OPEN QUESTION clause with this ruling, former wording preserved in place\n  (#12).` After setting aside exactly the
  three named differences (the dash, the bold, two line breaks with their two-space continuations) it equals the ledger's
  quotation character for character (scratch script `t1b_record_check.py`). *Declared order departure:* run while the
  opening guard capture ran, before 1(a), on a scratch copy of the `<T0>` object; read-only, no edit made.
- **1(c)** the four end strings, each found once: lines 1890, 1894, 1925 (by its locator), 1928.
- **1(d)/(e)** the two edits and the append made as ordered, act date 2026-11-01.
- **1(f) reconciliation — PASS** (`TASK 1 RECONCILIATION PASS`); assertions 1–3 pass; **sizes in characters:** old
  `CLAUDE.md` 169,617, new 169,182 (−435); P1 455; P2 309; pointer 1 165; pointer 2 164; old `CLAUDE_ARCHIVE.md` 12,881,
  new 14,768; appended block 1,887. **Planted faults:** F1 (character 16 of the new `CLAUDE.md`) failed assertion 2;
  F2 (one character of P1 in the archive copy) failed assertion 3 — both as required.
- **1(g) — THE ★ CASE.** `gen_governing_surface_split.py --check --pair CLAUDE.md` exit 0. **`gen_claude_md_finer_archive.py
  --check` → *"FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json"*, and
  `gen_claude_md_prune_backlog.py --check` → *"FAIL: the prune-at-amendment backlog record does not re-derive:
  tools\audit\claude_md_prune_backlog.json"*.** A2 lists both as expected GREEN throughout. So the full guard capture was
  not run and **nothing of Task 1 was committed**: both edits reversed with the file-editing tool; `git hash-object
  CLAUDE.md` = `807c547d328982f2fec73eb73a5e5fd846ac18da` = its blob at `<T0>`; `CLAUDE_ARCHIVE.md` =
  `1abd251820ccfa110150d4f3d58070b214b280ac` = its blob at `<T0>`.
- **The cause, established at the tools' text and objects (D-669):** both tools rebuild their whole artifact and compare it
  with the committed file (`main`, `gen_claude_md_finer_archive.py:567-590`, `gen_claude_md_prune_backlog.py:594-617`).
  **Both are red at the reversed tree as well** — i.e. at `<T0>` — so the red is STANDING and not Task 1's. A scratch
  script importing each tool's `build()` and comparing field by field (`cause_diag.py`) finds exactly one differing value
  in each: `reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once` (finer archive) and
  `reconciliation.every_span_the_reading_flagged_is_still_present_at_site_exactly_once` (prune backlog), committed `True`,
  rebuilt `False`. A settled span either tool tracks is no longer found exactly once in the live `CLAUDE.md` — consistent
  with the ruling record's §1 (*"found by its opening, amended since"*, and *"2 not found"*). Both tools are HISTORICAL
  records in the guard runner, so the guard state never ran them and never showed the red; **A2's "expected GREEN" for them
  was a prediction never measured at the tree.**

## 5. Task 2 — Ruling 3: carried out, reconciled, then NOT committed (A2's ★ case)

- **2(a)** every site stood where the dispatch says, by its text (read whole at ordered read (6)); the backbone at `<T0>`:
  `PRECEDING_REGIME_START` once in `home_granularity`, `REMOVED_FILE_START` once in `scope_of_application`, `REMOVED_FILE_END`
  once after it; (iii-a) and (iii-b) begin and end as ordered (`t2a_excerpts.py`, *"2(a) EXCERPTS PASS"*; declared early,
  read-only, on the scratch copy).
- **2(b)** the eight edits S0–S7 made as written (act date 2026-11-01). The edited generator blob was `ebf2c8f2…`; a diff
  against `<T0>` showed the changes only at the eight sites (ten changed passages, S5 and S7 each split by unchanged lines).
- **2(c)** write mode *"wrote 20 files: DECISIONS.md (the index, 772 lines) + 19 group files"*; `--check` *"the register
  matches the data (20 files …)"*; `git diff --stat <T0> -- decisions/` **empty**.
- **2(d)** the append made as ordered (header paragraph, (1)–(5), texts taken from the `<T0>` copy; line numbers as at
  `<T0>`: 10–83, 233–246, 250, 258, 270–276, 88, 122, 229 — none differs from the dispatch's).
- **2(e) reconciliation — PASS** (`TASK 2 RECONCILIATION PASS`). **Ruling 3's before and after, measured in the act, in
  characters:** old `DECISIONS.md` 127,727, new 117,490 (**−10,237**); archived block (1) 7,012; block (2) 657; excerpt
  (iii-a) 466; excerpt (iii-b) 1,354; block (4) 2,291; old line 88 48; old line 122 101; old line 229 437; pointers: S1 377,
  S2 line 99, S3 line 140, S4 line 449, S5 397, (iii-a) 143, (iii-b) 203, S7 323; old `DECISIONS_ARCHIVE.md` 1,670, new
  15,976; appended block 14,306. **Planted faults:** F3 (a row of the index) failed assertion 2; F4 (one character of block
  (1) in the archive copy) failed assertion 3 — both as required.
- **2(f)** `--pair DECISIONS.md` exit 0. **Decision 2's AFTER equals its BEFORE** for both tools, line for line (no
  `CLAUDE.md` line moved, Task 1 being reversed). **The full capture — THE ★ CASE:** *"83 guard(s) run, 19 failing, 4 not
  run, 20 historical record(s)"*, header *"STALE vs the run"*, zero STOPs. Against the opening capture, five verdicts moved
  PASS → FAIL, where 2(f) predicted only `gen_session_start_read_size.py`:
  `gen_session_start_read_size.py --check` (predicted), **`gen_defense_share.py --check`, `gen_l0_l1_outgoing_population.py
  --check`, `gen_l3_outgoing_population.py --check`, `decisions/gen_phase1w_legacy_verification.py --check` (not
  predicted)**. Their messages: phase1w — *"STOP: A1 (the marker is generated text): quote not at
  tools/audit/decisions/gen_decisions_register.py:514. It is now at line(s) [473] — re-aim the citation."*; L0/L1 and L3 —
  *"STALE vs the derivation: … does not re-derive"*; defense share — *"STALE vs the measurement: defense_share.json does
  not re-derive"*. **Nothing of Task 2 was committed:** the generator's eight edits reversed with the file-editing tool
  (`3449a69692a30f79e8bb62849ff8a5c5afe9d798` = its `<T0>` blob); the archive append reversed
  (`a780627fd6d0813105936796d867dbfb4c1642a7` = its `<T0>` blob); `DECISIONS.md` regenerated from the reversed generator,
  `--check` green, `f48596e05dcc043131790b7de3ac30b7ebf5c636` = its `<T0>` blob.
- **The cause, established (D-669):** at the reversed tree all five checks are green again, so **every one of the five reds
  was caused by Task 2's edits**: the phase1w tool carries a line citation INTO the generator (line 514, shifted by S0's
  added lines and S1's removed ones); the L0/L1 and L3 population tools and the defense share read `DECISIONS.md` (its
  size, or its lines). A2 classes the defense share and the two population tools as reds of this batch's acts only by
  OTHER causes (Task 1's `CLAUDE.md` edit; the close's `STATUS.md` edit), and names phase1w nowhere.
- **2(g)** word scan over the generator's added lines and the appended block: every hit is quoted text, the qualified *the
  decisions register*, or the index's own term *register-level* (the appendix carries the hit lines); no hit of my own wording.

## 6. Task 3 — the close

- **3(a)** two entries written at the top of `STATUS.md` — the close entry (naming this dispatch, carrying `Last updated: `)
  and Task 0's; **no Task 1 or Task 2 entry, those tasks not being committed**, which the close entry says with the reason.
  The prefix was MOVED off the remainder batch's close entry in the same edit; one line carries it (checked). The
  case-insensitive search for the 26 ruled terms and *repeat*/*tie* returns one hit, the standing *paraphrase* line.
- **3(b)** the tool read at the `a18148e5` object first: its constants were the FACT's. `STATUS.md` blob at `<T0>` =
  at `a18148e5` = `a3d66a18f4fbc484c1e06620ba2965b0f59b2841` (each `git rev-parse` in its own command). Re-aimed:
  `BASE_COMMIT` → `<T0>` (the last task commit made), `PREVIOUS_BATCH_DISPATCH` → the remainder dispatch, `ACT_DATE` keeps
  2026-11-01, `DISPATCH` → this dispatch, `TASK` → `Task 3`, `MOVE_KIND` stays `ordinary`; one aiming appended; the former
  values named in the head comments. `--apply`: *"entries moved: 3, 2,718 characters"*, present in the archive once, absent
  from the must-read; `the_moved` = the base's lines 8 (the close entry, the one declared adjustment applied), 10 and 12
  (its Task 1 and Task 0 entries) — **exactly the prediction; no STOP**; the two 2026-09-02 entries stay. The four archive
  checks exit 0 (`gen_status_batch_bound.py`, `--pair STATUS.md`, `gen_status_residue_move.py`, `gen_status_archive_pass.py`).
- **3(c)** before regeneration: evidence pin GREEN (171), L0/L1 GREEN, defense share / session-start read size / L3 RED,
  `gen_per_session_reading.py` exit 2 *"STOP: the imported ordinary read measures 248127 characters and its committed
  artifact says 248426 at the same tree"* (its own ordering STOP, cleared by regenerating the read size first). Regenerated
  in order — read size, defense share, L3, the per-session table LAST — and all six then green. **Moved values, each diffed
  between explicit blobs against `a18148e5`:**
  - `session_start_read_size.json` (`bd65f9f3…` → `0220060a…`): `STATUS.md` 11,997 → 11,698; total 248,426 → 248,127; the
    two regime comparisons' `to_total`, change and percent. **`DECISIONS.md` member 127,727 and `CLAUDE.md` member 105,876,
    before and after — UNCHANGED**, Tasks 1 and 2 not being committed (the whole-file value Ruling 3 ordered re-derived
    therefore carries no Ruling 3 movement).
  - `defense_share.json` (`371d7932…` → `b0fe1494…`): only the whole-read denominator, 248,426 → 248,127.
  - `l3_outgoing_population.json` (`13d1750b…` → `7b4f925f…`): only the *paraphrase* residue record's line number, 20 → 18
    — no population member, item-4 passage or tabulation member.
  - `per_session_reading.json` (`cfdbb22d…` → `931c00dc…`): the `STATUS.md` member and the totals including it; the handoff
    population count 383 → 386 and the three latest entries now 465, 464, 466 (34,448 characters, was 46,985); the two side
    totals (Claude Code 709,543 / 879,160 → 696,707 / 866,324; Cowork 1,008,362 → 995,526); the defense denominator. Nothing
    of the protocol row, the two arc populations or `the_settled_spans` counts moved.
- **3(d)** this report and its appendix (§10). **3(e)** the close section appended to
  `records/cowork/handoff/cowork_away_returns.md`. **3(f)** the close commit (§7).

## 7. The commits

| Task | Commit | Parent | Committed blobs |
|---|---|---|---|
| 0 | `8112c4d2260d381dd35fe050df6837bb0488bcf7` | `a18148e5…` | dispatch `17d9d39c…`, record `ce715295…`, entries `40e857eb…`/`9dab0095…`/`cd911c01…`, evidence pin `f460a683…` |
| 1 | — not committed (★ case) | | |
| 2 | — not committed (★ case) | | |
| close | named in the away-returns end-state portion (written after the commit exists) | `8112c4d2…` | |

## 8. Grades

- **E0 — MET.** **E1 — NOT MET:** the move was made and proved, but a red outside A2's prediction stopped the commit; the
  red is standing, not this batch's. **E2 — NOT MET:** made and proved, sizes measured, Decision 2 compared; four
  unpredicted reds, caused by the task. **E3** — asserted at Task 4, not here.
- **A1 — HELD** (`changed_paths.py`: the one standing modification; the five landing paths untracked; the standing
  population). **A2 — FAILED IN THREE PLACES**: (i) `gen_claude_md_finer_archive.py --check` and
  `gen_claude_md_prune_backlog.py --check` are RED at the start tree, not green; (ii) a Task 2 edit of the generator breaks
  `decisions/gen_phase1w_legacy_verification.py` (a line citation into the generator); (iii) a Task 2 edit of
  `DECISIONS.md` turns the defense share and both outgoing-population checks red. Its other predictions held: the opening
  failing set, the evidence-pin movement, the close's reds and regenerations. **A3 — HELD** (not run). **A4/A5** — verified
  at Task 4.
- **What a re-dispatch of Rulings 1 and 3 would need, stated as facts and not as a design:** for Ruling 1, a ruling or a
  premise on the two HISTORICAL tools' standing red (both are red before any edit); for Ruling 3, the phase1w citation of
  `gen_decisions_register.py:514`, and the defense share and the two population artifacts among the reds Task 2 causes.

## 9. Declared departures and observations

**Departures.** (1) The dispatch was read from the working tree before it was pinned (the opening line orders the read;
P-2's fallback: pinned at Task 0, proved unmoved before staging). (2) 1(b) and 2(a) were run early, read-only, on scratch
copies of `<T0>` objects, while the opening capture ran. (3) The appendix was assembled by a scratch script and placed in
`records/cc/reports/` by one `cp` from scratch, so that every printout is verbatim rather than retyped. (4) Shell loops over
named paths or tool names, and a few declared chains of git queries, each hash literal. (5) Commands ran with the
repository as working directory for the repository's own tools, `git commit` and `git push` (the standing exceptions).
(6) At 1(e) and 2(d) the companion already ended with a blank line, and "append one blank line" was followed literally,
leaving two blank lines before each appended block — moot, both appends being reversed.

**Observations, not acted on.** (a) Entry 466 existed at boot, so the current handover block is 466. (b)
`gen_claude_md_finer_archive.py` and `gen_claude_md_prune_backlog.py` are HISTORICAL in the guard runner yet red at the tree
(§4). (c) `decisions/gen_phase1w_legacy_verification.py` pins a line number of a tool, so any edit above that line of the
generator moves it. (d) `gen_decisions_register.py` write mode uses `write_text` without `newline`, so it writes
platform line endings; the group files' diff against `<T0>` was empty, as git normalizes them. (e) `old_DECISIONS.md` at
`<T0>` is 129,487 bytes LF (130,348 in the CRLF working copy); 127,727 characters.

## 10. The appendix

`records/cc/reports/cc_report_pruning_rulings_execution_2026_11_01_appendix.md`, **89,013 bytes** (its blob
`5f20c1eca7cf70d099c8741bbe28249e33701bcf`). It holds 69 printouts, verbatim, each under a heading naming its command and
step: A1's enumeration whole, the untracked and diff-stat loops, the last-bytes check, the evidence-pin runs and diff, the
staged set, commit and push, **both guard captures whole** (opening; Task 2), the classification STOP, the 0(g) BEFORE
captures, **`gen_cluster_dispositions.py --verify` and `reaim_home_anchors.py --check` BEFORE and AFTER whole**, the 1(b)
record check, both reconciliations and the four planted faults, the Task 1 reds and their cause diagnosis, the 2(a)
excerpts, the 2(c) outputs, the Task 2 reds and the captures' comparison, the changed-passage list, both word scans with
every hit line, the reversal proofs, the 3(b) and 3(c) outputs and the four artifact diffs.

## 11. The ordered reads against the work, and the tell

**What took most:** `DECISIONS.md` whole and the protocol section (lines 180–1606), then the dispatch itself. **A summary of
context did not fall.** **What the eight-line check saved, by my own account:** the six-span file-tool read (some 105,876
characters by the artifact) was replaced by eight single-line reads; the measurement is step 4's second dispatch's.

**The tell.** This batch produced nothing beyond the landed records, the Task 0 evidence-pin artifact, the Task 3 files
(`STATUS.md`, `STATUS_ARCHIVE.md`, the forward-bound tool and its artifact, the four regenerated artifacts), this report and
its appendix, the away-returns section, the end state's guard artifact — and, outside the repository, scratch files and loose
blob objects from `git hash-object -w`. **The A4 edits of Tasks 1 and 2 were made and reversed; none is committed.**

## 12. The self-check

Re-read at the diffs of every touched file. **Principles:** #12 kept (every reversed text proved byte-equal to its blob);
#13/#3 — the unpredicted reds were surfaced as STOPs, not built around; #14 — no behavior change; #15/#19 — every check at
the objects; #17(f)/D-431 — every value here is a printout of a named tool or script in the appendix, the sizes from the
reconciliation scripts. **Conventions:** American spelling; no invented labels; the musical words only in their musical
sense in my wording. **File tools:** working-tree reads with the file tools; shell for git object queries by explicit hash,
the sanctioned tools and scratch scripts; one `cp` into the repository, declared. **Uncertainty:** no difference between
measured quantities is asserted beyond the printouts.
