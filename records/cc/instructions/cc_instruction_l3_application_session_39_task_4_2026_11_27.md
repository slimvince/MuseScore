# CC dispatch — the L3 application, SESSION 39 of several: Task 4 of the L3 application dispatch (the charter `FRAMEWORK.md` and S-50 of the derived L0/L1 specification amended where the records give the words), and nothing else

> **STATUS: WRITTEN 2026-11-27; THE RECORD COMPARISON MADE 2026-11-27.** Written by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_six.md`, whose handoff entry is
> 1277, and landed unchecked under Ruling A of 2026-11-27 as the user extended it to Task 4 (entry 1276 §0 ruling 2).
> The record comparison was made by the next Cowork sitting, booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_seven.md`, whose handoff entry is
> 1278; that sitting set this banner. This file's provenance and the check notes are not in this file (ruling 1 of
> 2026-11-27, its last part): they stand in handoff entries 1277 §2 and 1278 §2. Under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the big dispatch is
> executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands it over (D-252);
> the Cowork writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do
> not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Sessions 10 to 38 applied its Task 3 in twenty-nine stretches. Session 38 landed
the writing side's files in commit `524f0139c04d5c951edd125512861c400d1018cd`, applied the last stretch in commit
`8ce907b9962149eb8c7cdff5a8b1610a966d77cb` (called **the Task 3 commit** below: the last commit of Task 3, and the one
Task 4's *"`git diff <the Task 3 commit>`"* means), and committed its report as
`b24195e1b824fae274451ab697e33aa39656c83c`, the current tip.

**This is session 39. It does three things and STOPS:**

1. it lands the writing side's untracked files (§5 act 1);
2. it executes the big dispatch's **Task 4** — four edits to `FRAMEWORK.md` (the charter) and one to S-50 of
   `cowork_derived_specification_l0_l1_2026_09_03.md` (the derived L0/L1 specification, whose §3.7 S-50 is the ratified
   L1 face the big dispatch calls IC-L1), each with its former wording kept, as one commit (§5 act 2);
3. it writes its own report (§5 act 3).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text and a ruling record's own words differ, the record governs**:
STOP-and-report for that edit, the rest applied (the big dispatch's *Findings in this batch*, its words entry *The
ledger*, and form (e)).

**Documentation only. No algorithm is decided by this session.** Task 4 places in the charter and in S-50 the words the
ruling records of 2026-11-03 already decided, and the user ratified Task 4's wordings and placements as written (Ruling
10 of `records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_part_b_third_sitting.md`, which says:
*"Documentation only. No algorithmic change is decided by Ruling 10. The amendments' substance was decided by the
rulings Task 4 cites"*). The method the specifications define stays as decided.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

0. **This file's banner.** If the banner above does not record that the record comparison has been made, STOP and
   report; do nothing else (the parked-instruction rule of `cowork_audit_protocol.md`, carried here as an order).
1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `b24195e1b824fae274451ab697e33aa39656c83c`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, and its pin.** You read this file from the working tree first, so the pin
   (`cowork_audit_protocol.md`, the standing clause P-2) takes its declared-departure route: declare in the report that
   the file was read before it was pinned; then
   `git hash-object -w records/cc/instructions/cc_instruction_l3_application_session_39_task_4_2026_11_27.md; echo "exit:$?"`.
   Record the hash. There is no expected value. §5 act 1 proves the file unmoved against this hash before staging.
4. **The two files Task 4 edits stand as the tip has them, and as the Task 3 commit had them.** For each of
   `FRAMEWORK.md` and `cowork_derived_specification_l0_l1_2026_09_03.md`:
   `git ls-tree b24195e1b824fae274451ab697e33aa39656c83c -- <path>; echo "exit:$?"` and
   `git hash-object <path>; echo "exit:$?"` must both show, for `FRAMEWORK.md`,
   `bc1d1265fc0d59fc2121b433408687d32bfb035a`, and for the specification, `8148e8d34b0f2dd061589240e4d8448ad5447771`;
   and `git diff --quiet 8ce907b9962149eb8c7cdff5a8b1610a966d77cb b24195e1b824fae274451ab697e33aa39656c83c -- <path>; echo "exit:$?"`
   must give exit 0. Then, with the **Grep tool** counting matching lines (fixed-string where the pattern says so):
   - in `FRAMEWORK.md`: `★ AMENDED` **6**; `THE FORMER WORDING WAS` **6**; `| L1 → L3 |` **2**; `| L0 → L2 |` **0**;
     `| L0 → L3 |` **0**; `restatement relation` **0**; `spelled intervals` **0**; `highest sounding` **0**;
     `form-function names` **0**; `cc_instruction_l3_application_2026_11_08` **0**;
   - in the specification: `(was: "S-50.` **1**; `- *Amended by Ruling` **7**;
     `*The derived list stands at the derivation, S-50.*` **1**; `cowork_rulings_2026_11_03_l3` **0**; `OQ-L3-` **0**;
     `highest sounding` **0**; `restatement relation` **0**; `spelled intervals` **0**.
   Any other result: STOP and report, neither file touched. (The writing side's staged copies: `FRAMEWORK.md` 158,103
   bytes, 2,141 line feeds; the specification 142,523 bytes, 1,740 line feeds; both line feeds only, no carriage
   return.)
5. **The reading file is as Task 3 left it** (Task 4 does not touch it; the big dispatch's A5).
   `git diff --quiet 8ce907b9962149eb8c7cdff5a8b1610a966d77cb -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0, and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must
   print `a83519b1f14bba9282fb9bf53600d59d5e27b213`. Anything else: STOP and report.
6. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: none.** One path appears modified and is not:
     `tools/audit/claude_md_finer_archive.json` differs from the tip only in line endings. Prove it:
     `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must print
     `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree b24195e1b824fae274451ab697e33aa39656c83c -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed.
   - **A tracked modification of `FRAMEWORK.md`, of the specification, of the reading file, of the big dispatch or of
     this file: STOP and report** — each is an input of an act this file orders (§1 checks 2 to 5). **Any other tracked
     modification is movement no act of this batch caused: report it and grade it** (which act, if any, reads or lands
     that path), **and go on**; it is never staged. This is the standing clause P-3 of `cowork_audit_protocol.md`,
     carried here as an order: such movement is *"reported and graded, never absorbed and never auto-stopped"*.
   - **Untracked paths expected:** the files §5 act 1 lands (this instruction; handoff entries 1274, 1275, 1276 and 1277,
     and the entry of the Cowork sitting that makes the record comparison, if this file's banner names one), plus the
     paths sessions 2 to 38 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; `docs/research_papers/desktop.ini`;
     `docs/research_papers/rowe`; the two PDFs under `external resarch summary/`;
     `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
     `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md`, which is not
     landed, not touched, and not a STOP). `.claude/` and `tools/extra scores/.mscbackup/` are git-ignored, so the tool
     does not list them; that is expected and not a STOP. List in the report every untracked path the tool reports
     outside those. A further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is
     not landed and is not a STOP (the big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

This list is the user's ruling of 2026-11-27 for Task 4 (handoff entry 1276 §0 ruling 1: the minimized list, unsplit,
ruling 5 of 2026-11-27 exercised for Task 4). **It replaces, for this session, the big dispatch's line 98, and with it
the read-first-block clause of `cowork_audit_protocol.md` (every dispatch's read-first block names the current handover
block of `cowork_handoff.md`): `cowork_handoff.md` and the protocol's dispatch-protocol section are NOT read.** The rules
of theirs this session relies on are carried into this file as orders: the pin (§1 check 3), the movement rule (§1
check 6), the parked-instruction rule (§1 check 0), the figure rule and the self-check list (§6 items 6 and 7).

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
3. **The session-start read, by size and modification time (ruling 2 of 2026-11-27).** List the repository root and
   `tools/audit/` with the file tools and compare each of these with the values below. **A file whose size and
   modification time both equal its values is not read; a file where either differs is read in full** (`DECISIONS.md`
   in ranges of about 150 lines; of the gating answer, **only the list** `tools/audit/nongating_apparatus_rows.json` →
   `★_the_live_gating_answer` → `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it). Report
   what you found for each.
   - `STATUS.md`: 11,726 bytes, modification time 1794136674043 (milliseconds since 1970);
   - `DECISIONS.md`: 120,603 bytes, modification time 1794081137207;
   - `tools/audit/nongating_apparatus_rows.json`: 178,066 bytes, modification time 1788814584416.
   **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard.
4. **`DEFECT_TYPES.md` whole** (18,368 bytes), for the self-check after the work.
5. **The eight ruling records whose words Task 4's edits carry, each read WHOLE with the Read tool**, all in
   `records/cowork/rulings/`:
   - `cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md` (11,895 bytes) — Edit 1 (a);
   - `cowork_rulings_2026_11_03_l3_sections_sitting.md` (20,068) — Edit 1 (b), form-function names;
   - `cowork_rulings_2026_11_03_l3_key_areas_sitting.md` (11,601) — Edit 1 (b), key areas;
   - `cowork_rulings_2026_11_03_l3_pivot_label_sitting.md` (10,502) — Edit 1 (b), the pivot label;
   - `cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md` (10,763) — Edit 2, Edit 3 (a), Edit 4 item 2;
   - `cowork_rulings_2026_11_03_l3_figured_bass_sitting.md` (10,846) — Edit 2, Edit 3 (a), Edit 4 item 3, and S-49;
   - `cowork_rulings_2026_11_03_l3_cadence_features_sitting.md` (12,603) — Edit 3 (a), Edit 4 item 1;
   - `cowork_rulings_2026_11_03_l3_boundaries_sitting.md` (12,069) — Edit 3 (a) to (c) and the sentence the table notes
     quote.
   **Before any text of §3 is written, compare every quotation in it with its record** (§3's opening says how). Read
   nothing else of any ruling record.
6. **The big dispatch, at these lines only, with the Read tool by line range:**
   - **lines 6821–7020 (Task 4, whole)**;
   - **lines 127–136** (the words *An amendment*, *The ledger* and *A changed passage*);
   - **lines 261–273** (form (e));
   - **lines 316–327** (assumption A1, the working tree);
   - **lines 362–393** (the standing bars, the commit-and-push discipline, and the findings rule).
   **Read nothing else of the big dispatch**: not its line 98 (the reading order §4 item 1 replaces), not §L, not Tasks
   0 to 3 or 5, not its head's other lines.
7. **`FRAMEWORK.md` and `cowork_derived_specification_l0_l1_2026_09_03.md` at the edit sites only**, with the Read tool
   by line range (guides from the writing side's staged copies; locate each site by the quoted text, and re-check it
   before the edit):
   - `FRAMEWORK.md` lines **333–365** (the L1 section's *Publishes* list and the 2026-10-13 note, ending at line 364),
     **474–499** (the L3 section to the line before `### The second axis`), **525–538** (the §5 boundary-contracts table
     and the paragraph after it), **1876–1889** (the S5 copy of the table and the paragraph after it);
   - the specification lines **1445–1522** (S-50, from `### 3.7` to the line `**S-51.` opens).
   Read nothing else of either file.
8. **The outgoing-text check is a search, not a read** (§5 act 2 step 1): the Grep tool over the reading file, never the
   Read tool.

## 3. The texts this session places, given whole

**How every quotation is compared with its record before it is written.** For each block below, take every passage that
is a ruling record's words (named beside the block) and find it in the record you read under §2 item 5: the words must
be the record's, in the record's order, with the record's spelling and punctuation; emphasis marks (`*`, `**`) the record
carries may be dropped where the block drops them, and nothing else may differ. A difference in any word: STOP-and-report
for that edit (form (e) and the findings rule), the other edits applied. **Every former wording quoted in a note is
compared with the file itself, not with this file**: the quoted text, its line breaks read as single spaces, must equal
the site's text as it stands before the edit, its line breaks and its bullet markers (`- ` and `  - `, with the
continuation indent) read as single spaces. A difference: do not commit; STOP and report.

**The date.** Every `<COMMIT-DATE>` below is the date on which you make the Task 4 commit, Stockholm time, written
`YYYY-MM-DD` (for example `2026-11-28`) — the same date in all four notes.

**The files use line feeds only, no carriage returns. Keep them so.** The characters `→`, `↔`, `—`, `–` and `★` below
are U+2192, U+2194, U+2014 (em dash), U+2013 (en dash) and U+2605, as in the files.

### 3.1 Edit 1 — `FRAMEWORK.md`, the L3 *Publishes* bullet, and its note

**Site.** Under `### L3 — The read-off facts` (line 474), the bullet at lines 479–481. Line 479 is unchanged. **Lines
480 and 481**, now exactly

```
  grouping**; the **chord symbol** — root pitch class, quality and bass note; the **figured bass**; the
  **harmonic rhythm**.
```

**become these four lines**, exactly:

```
  grouping**; the **chord symbol** — root (spelled), with its pitch class, quality and bass note; the
  **figured bass**; the **harmonic rhythm**; the **form-function names** (Ruling 3 of the 2026-11-03
  sections record); the **key areas** (Ruling 1 of the 2026-11-03 key-areas record); the **pivot
  label** (Ruling 1 of the 2026-11-03 pivot-label record).
```

*Record words in it:* `root (spelled), with its pitch class` (the chord-symbol record, Ruling 1, its *Documentation*
line); *form-function names* (the sections record, Ruling 3, its *Documentation* line); *key areas* (the key-areas
record, Ruling 1, its *Documentation* line); *the pivot label* (the pivot-label record, Ruling 1, its *Documentation*
line). The bold, the order, the citation form and the re-wrap are Task 4's, ratified as written (Ruling 10).

**The note.** Line 482 is blank and line 483 opens `**Why cadence type is here while the cadence cues are at L1.**`.
Between them, insert these eight lines and then one blank line, so that the bullet is followed by a blank line, the
note, a blank line, and line 483 as now:

```
**★ AMENDED <COMMIT-DATE> ON THE USER'S RULINGS OF 2026-11-03, WITH THE FORMER WORDING PRESERVED IN PLACE
(#12.)** Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md`, Ruling 3 of
`records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md`, Ruling 1 of
`records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md` and Ruling 1 of
`records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md`, written by the application act of
`records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (Task 4). **THE FORMER WORDING WAS:**
*"**Publishes:** the **cadence** at each phrase end, with its type; the **phrase and section grouping**; the
**chord symbol** — root pitch class, quality and bass note; the **figured bass**; the **harmonic rhythm**."*
```

The quoted former wording is the bullet's text after its `- ` marker, its line breaks read as spaces (§3's opening).

### 3.2 Edit 2 — `FRAMEWORK.md`, the L1 *Publishes* list, and its note

**Site.** Under `### L1 — Change points, candidates and notated evidence` (line 333), the `**Publishes:**` list. The
bullet `per slice, the **lowest sounding pitch** …` stands at lines 341–342 and ends `the 2026-10-08 structural-bass
record);`; line 343 opens `  - per change point, its **metric strength class**;`. **Between lines 342 and 343, insert
these three lines**, exactly:

```
  - a **restatement relation** over the notes (Ruling 1 of the 2026-11-03 thematic-parallelism record);
  - per slice, the **spelled intervals** above its lowest sounding pitch (Ruling 1 of the 2026-11-03
    figured-bass record);
```

*Record words in it:* *a restatement relation over the notes* (the thematic-parallelism record, Ruling 1, its first
*Algorithmic* bullet); *the spelled intervals above its lowest sounding pitch*, from *"L1 publishes, at every slice, the
spelled intervals above its lowest sounding pitch"* (the figured-bass record, Ruling 1, *As ruled*), shortened to the
list's form as Task 4 says.

**The note.** The 2026-10-13 note opens at line 351 and ends at line 364 (`by the application act.`); line 365 is blank
and line 366 opens `**Why a layer.**`. **The 2026-10-13 note is not edited.** Between lines 364 and 365, insert one blank
line and then these eleven lines, so that the old note is followed by a blank line, the new note, a blank line, and
`**Why a layer.**` as now:

```
**★ AMENDED <COMMIT-DATE> ON THE USER'S RULINGS OF 2026-11-03, WITH THE FORMER WORDING PRESERVED IN PLACE
(#12.)** Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md` and
Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md`, written by the
application act of `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (Task 4).
**THE FORMER WORDING WAS:** *"the ordered, covering, gapless and non-overlapping list of **slices** — the
stretches between consecutive change points, where a change point is every onset **and every release** of an
eligible note; per slice, the **lowest sounding pitch** of its sounding set, published under that name (Ruling 2
of the 2026-10-08 structural-bass record); per change point, its **metric strength class**; per change point,
the **notated boundary evidence** at it: bar line, fermata, rest, repeat sign, double bar; the **local cadence
cues**: a falling-fifth or rising-fourth bass motion, a leading-tone resolution, the sounding together of the
fourth and seventh degrees of a candidate tonality in the approach."* — the list's five bullets, in order.
```

The quoted former wording is the list's five bullets as they stand before the edit (lines 338–348), markers and indents
read as spaces (§3's opening).

### 3.3 Edit 3 — `FRAMEWORK.md`, the boundary-contracts table in §5 and its copy in S5, with a note beneath each

**Authority:** Ruling 1 of the boundaries record (*As ruled*, its three bullets) and, for the restatement relation in
the `L1 → L3` row, Ruling 1 of the thematic-parallelism record (its second *Algorithmic* bullet); one writing serves
both. The second cells are the boundaries record's words, the first letter capitalised to the table's form; the
direction `forward only`, the last cell `—` and the rows' positions are Task 4's, ratified as written (Ruling 10).

**The three row changes, made identically at both tables:**

- **(a)** the row, now exactly `| L1 → L3 | Notated phrase evidence | forward only | — |`, becomes exactly

```
| L1 → L3 | Notated phrase evidence; the restatement relation (OQ-L3-5); the highest sounding pitch per slice (OQ-L3-4); the spelled intervals above the lowest sounding pitch per slice (OQ-L3-7) | forward only | — |
```

- **(b)** immediately after the `| L0 → L1 |` row, this row is inserted:

```
| L0 → L2 | The key-signature value | forward only | — |
```

- **(c)** immediately after the `| L1 → L3 |` row (its position the same whether (a) is made before or after it), this
  row is inserted:

```
| L0 → L3 | The key-signature value; the spellings of the notes L2's facts reference; slurs and dynamics only if measured to help (L3-S9 (iv)) | forward only | — |
```

Every other row, the `| spine ↔ voice-leading axis |` row included, is untouched. In §5 the table's rows stand at lines
529–534 (L0 → L1 at 529, L1 → L3 at 533, the spine row at 534); in the copy, at lines 1880–1884 (L0 → L1 at 1880, L1 → L3
at 1884, the last row of that table).

**The note beneath the §5 table.** Line 534 is the spine row, line 535 blank, and line 536 opens `**The contract that
carries the most weight, stated plainly:**`. After the table (its last row the spine row), insert one blank line and
then these twelve lines, so that the table is followed by a blank line, the note, a blank line, and that paragraph as
now:

```
**★ AMENDED <COMMIT-DATE> ON THE USER'S RULINGS OF 2026-11-03, WITH THE FORMER WORDING PRESERVED IN PLACE
(#12.)** Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md` and Ruling 1 of
`records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md`, written by the application
act of `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (Task 4). The boundaries record:
*"The consume lines remain the governing text; the table summarises them."* **THE FORMER WORDING WAS:** the
table's rows, whole, each as it stood, in order:
`| L0 → L1 | The notated record, whole | forward only | Nothing derived. L1 may not treat the key signature as the tonality. |`;
`| L1 → L2 | Slices; metric strength; notated boundary evidence; cadence cues | forward only | No decided boundary — L1 decides none. No tonality claim. |`;
`| L2 → L3 | Segmentation; tonality per span; chord per span; chord-tone assignment and elaboration relation per note; rivals with mass | forward only | Nothing L2 did not publish — in particular no intermediate quantity of L2's own scoring. |`;
`| L3 → L2 | **Nothing.** | — | A read-off fact may not revise the decision it was read off. §8.4 states what happens instead. |`;
`| L1 → L3 | Notated phrase evidence | forward only | — |`;
`| spine ↔ voice-leading axis | Published facts only, in either direction, each carrying its establishment status | either | Neither axis may re-derive a fact the other publishes. |`.
```

**The note beneath the copy table.** Line 1884 is the copy's `| L1 → L3 |` row, line 1885 blank, and line 1886 opens
`**The one contract that carries the most weight, stated plainly:**`. After the copy table's last row as it stands
before the edit (line 1884, the `| L1 → L3 |` row; §5 act 2 step 3 writes this note before the rows, and row (c) then
goes between that row and the blank line, so the table ends with the new `| L0 → L3 |` row), insert one blank line and
then these eleven lines, so that the table is followed by a blank line, the note, a blank line, and that paragraph as
now:

```
**★ AMENDED <COMMIT-DATE> ON THE USER'S RULINGS OF 2026-11-03, WITH THE FORMER WORDING PRESERVED IN PLACE
(#12.)** Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md` and Ruling 1 of
`records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md`, written by the application
act of `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (Task 4). The boundaries record:
*"The consume lines remain the governing text; the table summarises them."* **THE FORMER WORDING WAS:** the
table's rows, whole, each as it stood, in order:
`| L0 → L1 | The notated record, whole | forward only | Nothing derived; L1 may not treat the key signature as the tonality |`;
`| L1 → L2 | Candidate onsets; metric strength; notated boundary evidence; cadence features | forward only | No decided boundary — L1 decides none; no tonality claim |`;
`| L2 → L3 | Segmentation; tonality per span; chord per span; chord-tone assignment per note; rivals with mass | forward only | Nothing L2 did not publish; in particular no intermediate quantity of L2's own scoring |`;
`| L3 → L2 | **Nothing.** | — | A later fact may not revise an earlier decision (C44's class, and the ordering that makes L2's answer measurable at all) |`;
`| L1 → L3 | Notated phrase evidence | forward only | — |`.
```

**How the former rows are quoted, and the check.** Each row is quoted whole as an inline code span on a line of its own,
so that no line of the note begins with `|` and the charter's tables are not extended by the note. **Each quoted row,
the backticks and the closing `;` or `.` taken off, must equal byte for byte the table's row as it stands before the
edit** — compare against the file, not against this file; a difference: do not commit; STOP and report.

### 3.4 Edit 4 — S-50 of `cowork_derived_specification_l0_l1_2026_09_03.md`

**Site.** S-50, located by its opening `**S-50. L1 publishes exactly: the slice list` (line 1447). Its bold text runs from
line 1447 to `*degree* or *function*.**` at line 1464; the existing `(was: …)` follows on lines 1464–1480 and ends
`cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2)` (line 1480); `- *Defense.*` opens at line 1481; the
last sub-item, `- *Amended by Ruling 2 of cowork_rulings_2026_10_08_l2_structural_bass_sitting.md …`, runs from line 1512
to line 1520, which ends `*The derived list stands at the derivation, S-50.*`; line 1521 is blank and line 1522 opens
`**S-51.`. **S-50's *Defense*, *Source class*, *Status*, *Premise* and *Falsifier*, every sub-item already there, and
S-49 are not edited.**

**(1) The three items, inside line 1450.** Line 1450 is now exactly

```
(Ruling 2 of the 2026-10-08 structural-bass record, OQ-L2-11); the span's two edges published as such,
```

and it **becomes these nine lines**, exactly (the insertion point, *"… OQ-L2-11);"* followed by *"the span's two edges
published as such"*, lies inside this one line; line 1451, `with a record-edge mark where an edge is the`, follows as
now):

```
(Ruling 2 of the 2026-10-08 structural-bass record, OQ-L2-11); per slice, the highest sounding pitch
of its sounding set, published under that name (Ruling 2 of the 2026-11-03 cadence-features record,
OQ-L3-4); a restatement relation over the notes — each instance naming the stretch, the earlier stretch
it restates, the transposition (none, or an interval), and the representation under which it matched;
with its witnesses (the notes), its establishment status, its provenance and, where not computed, a
named reason (the forms S-50 already requires); named for the pattern detected, never *boundary*,
*phrase* or *theme*; the matching measure UNESTABLISHED until measured (Ruling 1 of the 2026-11-03
thematic-parallelism record, OQ-L3-5); per slice, the spelled intervals above its lowest sounding pitch
(Ruling 1 of the 2026-11-03 figured-bass record, OQ-L3-7); the span's two edges published as such,
```

*Record words in it:* item 1, *"per slice, the highest sounding pitch of its sounding set"*, *"published under that
name"* (the cadence-features record, Ruling 2, its bold sentence at §2a); item 2, from *"a restatement relation over the
notes"* through *"the matching measure UNESTABLISHED until measured"* (the thematic-parallelism record, Ruling 1, its
first *Algorithmic* bullet), compared word for word, the record's italics on *boundary*, *phrase* and *theme* kept;
item 3, *"the spelled intervals above its lowest sounding pitch"* (the figured-bass record, Ruling 1, *As ruled*). The
items' position and order and the citation parentheses are Task 4's, ratified as written (Ruling 10).

**(2) The former wording, a second `(was: …)`.** Immediately after line 1480 and before `- *Defense.*`, insert these
twenty-one lines:

```
(was: "S-50. L1 publishes exactly: the slice list (S-29–S-33) with each slice's sounding set by event
identity; per slice, the lowest sounding pitch of its sounding set, published under that name, with its
witness (the note), its establishment status, its provenance and, where not computed, a named reason
(Ruling 2 of the 2026-10-08 structural-bass record, OQ-L2-11); the span's two edges published as such,
with a record-edge mark where an edge is the
record's own start or end (S-32, Ruling 40, Ruling 46 (vi)), events marked *entered sounding* and *cut
by the span* (S-32), and a tie cut by the span so marked (S-25); per change point, its metric strength
class (S-35) and its boundary flag set (S-39), every flag with its scope (Ruling 48); the positioned
marks list, complete over every notated mark of face (e), the flags referencing it by identity (S-41,
Ruling 51); the junction adjacencies (S-27); per onset change point and per notated voice, the three
relations to that voice's preceding event with their witnesses (Ruling 49) and the chordal count with
its witnesses (Ruling 61); per onset change point, the cue flags (S-45–S-47) with the interval content
(S-49); the PEDAL-HELD attribute on every change point inside a pedal span (S-54); the ornamental
attachments and ornament attributes (S-16, S-17); the silent-notes and annotation carriers (S-2,
S-18); and the defect flags (S-10, S-24, S-25). Every predicate is published with its witnesses, its
establishment status (S-52), its provenance — how it was arrived at (Ruling 62 item 9) — and, where it
is not computed or is empty, a named reason (Ruling 62 item 7). No published field is named
*boundary*, *cadence*, *phrase*, *chord*, *key*, *tonality*, *degree* or *function*.";
cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 2;
cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1;
cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1)
```

**Build its first eighteen lines from the file, not from this block:** take lines 1447 to 1463 as they stand before the
edit, replace the first line's leading `**` with `(was: "`, and append the line
`*boundary*, *cadence*, *phrase*, *chord*, *key*, *tonality*, *degree* or *function*.";` (line 1464's text up to its
`.**`, with `";` in place of the `**` and of everything after it). The result must equal the block's first eighteen
lines byte for byte; a difference: do not commit; STOP and report. The form is the one the L2 application act settled
for this statement (Task 4, Edit 4, *The former wording, preserved*); the existing `(was: …)` is not edited.

**(3) The three sub-items.** After line 1520 (the last line of the structural-bass sub-item) and before the blank line
1521, insert these thirteen lines:

```
- *Amended by Ruling 2 of cowork_rulings_2026_11_03_l3_cadence_features_sitting.md (OQ-L3-4) — the
  highest sounding pitch per slice.* "IC-L1 S-50's list gains "per slice, the highest sounding pitch of
  its sounding set", published under that name." *The derived list stands at the derivation, S-50.*
- *Amended by Ruling 1 of cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md (OQ-L3-5) — the
  restatement relation over the notes.* "L1's published list (IC-L1 S-50) gains one item: a restatement
  relation over the notes — each instance naming the stretch, the earlier stretch it restates, the
  transposition (none, or an interval), and the representation under which it matched; with its witnesses
  (the notes), its establishment status, its provenance and, where not computed, a named reason (the forms
  S-50 already requires); named for the pattern detected, never *boundary*, *phrase* or *theme*; the
  matching measure UNESTABLISHED until measured." *The derived list stands at the derivation, S-50.*
- *Amended by Ruling 1 of cowork_rulings_2026_11_03_l3_figured_bass_sitting.md (OQ-L3-7) — the spelled
  intervals above the lowest sounding pitch per slice.* "L1 publishes, at every slice, the spelled
  intervals above its lowest sounding pitch." *The derived list stands at the derivation, S-50.*
```

*Record words quoted in them, each the record's sentence that orders the addition:* the first, the cadence-features
record's bold sentence at §2a (*"IC-L1 S-50's list gains *"per slice, the highest sounding pitch of its sounding set"*,
published under that name."*), its emphasis dropped as the big dispatch's §L.5 quotes it; the second, the
thematic-parallelism record's first *Algorithmic* bullet, from *"L1's published list (IC-L1 S-50) gains one item"*
through *"until measured"*, its bold dropped and its italics on *boundary*, *phrase* and *theme* kept; the third, the
figured-bass record's Ruling 1, *As ruled*, its first sentence. The sub-items' wording around the quotations is Task
4's, ratified as written (Ruling 10).

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session (the user's ruling of 2026-11-27, handoff entry 1276 §0
   ruling 1). With it, **the read-first-block clause of `cowork_audit_protocol.md` is replaced** for this session (§2's
   opening).
2. **A1, for the writing side's handoff entries.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed.
   **Handoff entries 1274, 1275, 1276 and 1277, and the entry of the sitting that makes the record comparison if this
   file's banner names one, ARE landed**, with this file, in §5 act 1, as sessions 8 to 38 landed theirs. Any other
   untracked handoff entry or ruling record stays as A1 says.
3. **Task 4's texts, given whole** (§3). Task 4 describes its edits and their notes; §3 gives the exact lines, built to
   Task 4's descriptions. Where Task 4 says a quotation is *"as §L quotes it"*, §3 gives the record's words and names
   the record's passage; the record governs (the words entry *The ledger*). §3's line wrapping of the new and re-wrapped
   lines is this file's, and Task 4's *"a deleted line is allowed only where an edit replaces or re-wraps that line"*
   admits it.
4. **`git diff <the Task 3 commit>`** → `git diff 8ce907b9962149eb8c7cdff5a8b1610a966d77cb` (§0), with the exact counts
   of §5 act 2 step 4.
5. **E4's listing of the eight items not written** (Task 4, *Not written — listed in the report for the user*): each is
   listed in the report under the heading *charter and contract amendments left to the user*, **in Task 4's own words
   and with the line of the big dispatch where they stand**. The records behind items 1 to 4 and 7 (§L.2, §L.29, §L.34,
   §L.42, §L.50 and §L.6) are not on §2's list and are not read: Task 4 records that its writing side did not open the
   ruling records either, so the listing reports what Task 4 says, and says so. Items 5 (S-49) and 6 (IC-L2 §0) rest on
   the figured-bass and chord-symbol records, which you read; for each, quote the record's sentence Task 4 relies on
   (the figured-bass record's *"IC-L1 S-49/S-50 and the charter's L1 list amended"*; the chord-symbol record's §2 (g)).
   **Edit 4 item 1 is listed as written** (Task 4, *Also listed for the user*).
6. **E4's report** (the batch's report of Task 5, `records/cc/reports/cc_report_l3_application_2026_11_08.md`) →
   **this session's own report, `records/cc/reports/cc_report_l3_application_session_39_task_4_2026_11_27.md`**, as
   sessions 2 to 38 each wrote theirs. Task 5's report, when its session writes it, points at this one.
7. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin Task 5.

## 5. The acts, in order

**NEITHER FILE TASK 4 EDITS IS EDITED UNTIL ACT 1 HAS BEEN COMMITTED, PUSHED AND VERIFIED.** Until act 1's push is
verified at `.git/refs/remotes/origin/master`, `FRAMEWORK.md` and the specification are opened with the Read and Grep tools
only — no Edit or Write call names them. **Every read §2 orders is made in the place §2 orders it, before the edit.**

1. **Land the writing side's files first, in a commit of their own.** Exactly these paths, each UNTRACKED:
   - this file, `records/cc/instructions/cc_instruction_l3_application_session_39_task_4_2026_11_27.md`;
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_four.md` (the sitting that
     verified session 38);
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_five.md` (the sitting that located
     Task 4's sites);
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_six.md` (the sitting that took the
     user's two rulings for Task 4);
   - `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventy_seven.md` (the sitting that wrote
     this file);
   - and the entry of the Cowork sitting that makes the record comparison, if this file's banner names one.
   **Immediately before staging:** run §1 check 2 again; hash this file again (`git hash-object`, as §1 check 3) and it
   must equal the hash §1 check 3 recorded and pinned; and, for each of `FRAMEWORK.md` and the specification,
   `git diff --quiet b24195e1b824fae274451ab697e33aa39656c83c -- <path>; echo "exit:$?"` must give exit 0 (neither yet
   touched). Any of these failing: STOP and report, nothing staged. Stage the paths by name (never `git add` on a folder
   or with a pattern). Subject exactly:
   `record: handoff entries 1274 to 1277 and the session 39 instruction of the L3 application landed; Task 4 follows`
   (if the banner names a further entry, write *"1274 to 1278"* in place of *"1274 to 1277"*).
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Then `git show --stat <the new tip>;
   echo "exit:$?"` must show exactly the paths above added, and nothing else.

2. **Task 4**, in this order:
   1. **The outgoing-text check, before any edit** (Task 4, *Before any edit*). With the Grep tool over
      `ratification_surfaces/cowork_comparison_l3_reading.md`, output mode showing matching lines: pattern `^### 6\.`
      must match **57** lines (the writing side's count at the staged copy); and the pattern
      `^### 6\..*(FRAMEWORK\.md|cowork_derived_specification_l0_l1_2026_09_03\.md)` must match **0**. If either name is
      named in a `### 6.` heading, Task 4 is a STOP-and-report as a whole: edit nothing, write the report. If the count
      of `^### 6\.` is not 57, report the count found and go on only if the second pattern matches 0 (the check is the
      second pattern; the count is a guide).
   2. **The quotation comparison** (§3's opening), for every block, before any edit. Report each block's result.
   3. **The edits**, with the Edit tool, **each file from the bottom up, so that each line number §3 gives before the edit
      stays right for the next edit**:
      - `FRAMEWORK.md`: Edit 3 at the copy table (its note after line 1884, then row (c) after line 1884, row (a) at
        line 1884, row (b) after line 1880); Edit 3 at the §5 table (its note after line 534, then row (c) after line
        533, row (a) at line 533, row (b) after line 529); Edit 1 (its note, then lines 480–481); Edit 2 (its note after
        line 364, then the two bullets after line 342);
      - the specification: Edit 4 (3) the sub-items after line 1520; (2) the `(was: …)` after line 1480; (1) line 1450.
      Touch nothing else. Before each edit, re-read the site's lines and confirm they read as §3 says.
   4. **The check before the commit** (Task 4, *The check before the commit*):
      `git diff 8ce907b9962149eb8c7cdff5a8b1610a966d77cb -- FRAMEWORK.md > "<your scratchpad>/l3_session39_framework_diff.txt"; echo "exit:$?"`
      and
      `git diff 8ce907b9962149eb8c7cdff5a8b1610a966d77cb -- cowork_derived_specification_l0_l1_2026_09_03.md > "<your scratchpad>/l3_session39_spec_diff.txt"; echo "exit:$?"`,
      each read with the Read tool (never with a shell text tool on a working-tree file). Then
      `git diff --numstat 8ce907b9962149eb8c7cdff5a8b1610a966d77cb -- FRAMEWORK.md cowork_derived_specification_l0_l1_2026_09_03.md; echo "exit:$?"`
      must show **exactly 59 added and 4 deleted lines for `FRAMEWORK.md`** (Edit 1: 4 + 9 added, 2 deleted; Edit 2: 3
      + 12 added; Edit 3 at §5: 1 + 2 + 13 added, 1 deleted; Edit 3 at the copy: 1 + 2 + 12 added, 1 deleted) **and
      exactly 43 added and 1 deleted for the specification** (9 added, 1 deleted at line 1450; 21; 13). *These counts
      are the writing side's, counted by hand from §3's blocks; the record comparison checks them before you run this.*
      **In `FRAMEWORK.md`, every changed passage lies at one of four sites:** the L3 *Publishes* bullet with its new
      note; the L1 *Publishes* list with its new note; the §5 table with its note; the S5 copy table with its note.
      **In the specification, every changed passage lies inside S-50**, between its opening and the line before
      `**S-51.`. **The four deleted lines in `FRAMEWORK.md` are lines 480, 481, 533 and 1884 before the edit, each
      replaced at its site and its former text standing in the note at the same site; the one deleted line in the
      specification is line 1450, re-wrapped, its text standing in the new `(was: …)`.** Attribute every changed passage
      in a table in the report. Then, with the Grep tool counting matching lines (fixed-string):
      - in `FRAMEWORK.md`: `★ AMENDED` **10**; `THE FORMER WORDING WAS` **10**;
        `ON THE USER'S RULINGS OF 2026-11-03, WITH THE FORMER WORDING PRESERVED IN PLACE` **4**; `| L0 → L2 |` **2**;
        `| L0 → L3 |` **2**; `| L1 → L3 |` **4** (two rows and two quoted former rows); `restatement relation` **3**;
        `spelled intervals` **3**; `highest sounding` **2**; `form-function names` **1**;
        `cc_instruction_l3_application_2026_11_08` **4**;
      - in the specification: `(was: "S-50.` **2**; `- *Amended by Ruling` **10**;
        `*The derived list stands at the derivation, S-50.*` **4**; `cowork_rulings_2026_11_03_l3` **6**; `OQ-L3-` **6**.
      Then `git hash-object <path>; echo "exit:$?"` for each file, recorded (no expected value: the date in the notes is
      yours). Any other count, a changed passage at another site, or a deleted line other than those named: do not
      commit; restore the file from the object
      (`git checkout 8ce907b9962149eb8c7cdff5a8b1610a966d77cb -- <path>; echo "exit:$?"`); STOP and report.
   5. **The commit.** ONE commit for both files, those two paths alone, subject exactly (the big dispatch's line 7004):
      `application L3: the charter's L3 and L1 lists, its boundary tables and S-50 of the derived L0/L1 specification amended where the L3 family records give the words, former wordings kept`
      PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Record both new blobs with
      `git ls-tree <the new tip> -- FRAMEWORK.md cowork_derived_specification_l0_l1_2026_09_03.md; echo "exit:$?"`; each
      must equal the hash step 4 recorded. If an edit was STOP-and-report under §3 or form (e), commit the rest, its
      counts adjusted by that edit's lines, and say so in the report.

3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_39_task_4_2026_11_27.md` with the items of
   §6. Commit that ONE path alone, subject exactly:
   `report: session 39 of the L3 application, Task 4 (the charter and S-50 amended where the records give the words) written; Task 5 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that belongs
   to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's results (checks 0 to 6), the blobs, the pin and its declared departure, and the checks repeated immediately
   before staging act 1; §2 item 3's result for each of the three files; a sentence saying whether either edited file
   was opened by any Edit or Write call before act 1's push was verified (§5's opening); and a sentence saying whether
   every read of §2 was made in its ordered place before the edit.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. **E4, graded** (Task 4, *E4*): the outgoing-text check and its result; the quotation comparison, block by block;
   Edits 1 to 4 each applied with its preserved wording, or listed as STOP-and-report with what was read; the date
   written into the notes; the eight items not written, listed under *charter and contract amendments left to the user*
   as §4 item 5 says, with Edit 4 item 1 listed as written; the two diffs attributed site by site, the numstat, the
   counts and the blobs; and that no recommendation is written anywhere — in the two files, the report or a commit
   message.
4. Every departure from this file or the big dispatch, declared, including any order of reads or acts you could not
   follow.
5. **Every line number the report gives is a line number of the file as committed by the Task 4 commit, unless the
   sentence giving it says otherwise.**
6. **Every figure in the report is read at its object in this session, with the command or tool that produced it named
   beside it; no figure is copied from this file as a result** (the protocol's figure-by-citation and character-figure
   clauses, carried here as an order).
7. **The self-check after the work** (`CLAUDE.md`, its last section), over the two diffs, answering each of these five,
   the writing side's standing self-check list (`cowork_audit_protocol.md`, carried here as an order): (a) the guiding
   principles the work touches, and whether it conforms; (b) the conventions — American English in your own words (a
   record's words placed keep the record's spelling, as the standing bars say), no self-invented labels, music-theory
   words in their musical sense only, every non-musical use qualified; (c) every figure and premise cited to its object
   (D-431); (d) the file-tools rule (D-253); (e) **the uncertainty of any comparison the report makes (#24)** — say so if
   the report makes none.
8. The last sentence, exactly: *"Session 39 of the L3 application ends here. Task 4 is done. Task 5 is not begun. Nothing else was done."*
   (If Task 4 was STOP-and-report as a whole, write *"Task 4 stopped as the report says"* in place of *"Task 4 is
   done"*.)

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- this file's banner does not record the record comparison as made (§1 check 0);
- any other check in §1 fails, or a tracked modification §1 check 6 names as a STOP appears;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- a check immediately before staging act 1 fails (§5 act 1);
- the outgoing-text check finds either name in a `### 6.` heading (then Task 4 is STOP-and-report as a whole);
- a former wording quoted in a note, or the `(was: …)`, does not equal the file's text (§3);
- §5 act 2 step 4 finds a changed passage outside the four sites or outside S-50, a deleted line other than those
  named, or a count other than the ones given (the file restored first);
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

A quotation that differs from its record (§3's opening) is a STOP-and-report **for that edit only**: that edit is not
written, the others are, and the report lists it (form (e), the findings rule). After a STOP, report what you did and
what you did not do. Do not try to repair anything.
