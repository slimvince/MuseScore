# CC dispatch — the L3 application, SESSION 14 of several: Task 3 of the L3 application dispatch, fifth stretch (§L.23 alone), and nothing else

> **STATUS: WRITTEN 2026-11-23, CHECKED AS A TURN OF ITS OWN AND CORRECTED 2026-11-23 (the sitting booted on handoff
> entry 1205; see the provenance), NOT YET RELEASED,** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_four.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 12 applied Task 3's first three stretches, §L.1 to §L.20. Session 13
applied the fourth stretch — Row 7.67's held line of §L.15, then §L.21 and §L.22 — in commit
`857b2fa64fe1f57cd0ee649f95885b3e81ffd9a0` (called **the stretch 4 commit** below), and committed its report as
`d56ccc6ee74fa9a5327a5076cc97b33104ecb704`, the current tip.

**This is session 14. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry only: §L.23, the L3-S38 ratification
record. It commits and pushes that fifth stretch, writes its report, and STOPS.** §L.24 is a later session's.

**What this stretch writes, in one paragraph.** **82 lines, all opening `*RULED DISPOSITION (`, all naming
`cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1`**, each beneath its row's last existing line: the
35 derived rows of cuts 1 and 2 (the rows the first-cut and second-cut records filed as this side's derivation, which
the ratification record's Ruling 1 ratified — 27 HISTORICAL, 6 QUARANTINED, 2 RELOCATED), the 45 rows of cuts 3 to 8
(42 HISTORICAL, 3 QUARANTINED), and Rows 3.5 (ii) and 3.15 (HISTORICAL, form (b-H)). §3.2 gives every one with its exact
text. Beside them: **22 *LEAVES L3* lines** at the transfer list §10 (Task 3 (c) item 6); **9 audit-question entries
and 1 NOT QUARANTINED line** at §11 (Task 3 (c) item 7); and the in-progress line brought forward from §L.22 to §L.23.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's or surface's own words differ, the
record governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this
batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the dispositions the records
already place; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `d56ccc6ee74fa9a5327a5076cc97b33104ecb704`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_14_task_3_stretch_5_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 4 commit left it.**
   `git diff --quiet 857b2fa64fe1f57cd0ee649f95885b3e81ffd9a0 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree d56ccc6ee74fa9a5327a5076cc97b33104ecb704 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `5bccffae70dcdf713d25549aa7ef7bca4e09bf4a`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **271**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **4**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **0**. Any other result: STOP and report, the file not touched. (The writing side's
   staged copy: 5,225,074 bytes, 84,114 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree d56ccc6ee74fa9a5327a5076cc97b33104ecb704 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1204 and 1205),
     plus the paths sessions 2 to 13 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). `.claude/` and
     `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is expected and
     not a STOP. List in the report every untracked path the tool reports outside those. A further untracked
     `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a STOP (the big
     dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
3. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the remainder of that
   section or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and
   no guard.
4. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_five.md` (the current entry point, written
   by the sitting that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_four.md` (the one before it, written by the
   sitting that verified session 13; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md` (§L.23; 5,897 bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md` (6,889 bytes; its §1b, as amended,
     names cut 1's derived rows and their placement words);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md` (7,391 bytes; its §2 names cut 2's
     derived rows and their placement words);
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_item_six_reading_sitting.md` (5,402 bytes;
     Ruling 1: Task 3 (c) item 6 acts by claim).
   **Do NOT read the records of §L.1 to §L.20 or of §L.24 to §L.55.**
8. **The surfaces whose words the lines quote, at these line ranges only, with the Read tool by offset** (each range
   located by the writing side at the staged copy, 2026-11-23; if a range does not open at the heading named, find the
   heading with the Grep tool and report the new range). All under `ratification_surfaces/`:
   - `cowork_l3_s38_ratification_surface_2026_11_03.md` (11,858 bytes): lines 30–81, its §2 (the row lists Ruling 1
     ratifies);
   - `cowork_l3_s38_second_cut_surface_2026_11_03.md` (13,403 bytes): lines 41–89, its §3 (Row 10.207 (ii)'s question);
   - `cowork_l3_s38_third_cut_surface_2026_11_03.md` (12,711 bytes): lines 46–105, its §3;
   - `cowork_l3_s38_fourth_cut_surface_2026_11_03.md` (11,547 bytes): lines 38–90, its §3;
   - `cowork_l3_s38_fifth_cut_surface_2026_11_03.md` (13,555 bytes): lines 39–106, its §3;
   - `cowork_l3_s38_sixth_cut_surface_2026_11_03.md` (17,546 bytes): lines 54–127, its §3;
   - `cowork_l3_s38_seventh_cut_surface_2026_11_03.md` (18,088 bytes): lines 41–53 (its §2, where the twin's question is
     quoted), lines 54–134 (its §3), and lines 162–182 (its §6 to item 2, the correction to QUARANTINED);
   - `cowork_l3_s38_eighth_cut_surface_2026_11_03.md` (12,670 bytes): lines 29–44 (its §2, where Row 5.59's question is
     quoted) and lines 45–90 (its §3);
   - **the L2 reading file**, `cowork_comparison_l2_reading.md` (5,069,084 bytes), at three entries of its §11 only:
     lines 76436–76437 (*"Row 5.59, with Rows 5.125, 5.128(ii) and 5.198(ii) — …"*), lines 76447–76448 (*"Row 5.69(ii)
     — …"*) and lines 76677–76678 (*"Rows 8.12 and 8.73 — travelling with Row 5.148: …"*). Nothing else in that file.
9. **One side record, at one line range only, with the Read tool by offset:**
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes): **Ruling
   3** lines 89–125 (form (b)'s two-record rule applies by part).
10. **The big dispatch, at these lines only, with the Read tool by line range:**
    - lines 1–37;
    - lines 59–97;
    - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
      `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
    - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when
      as proposed is written*, and form (b-H) are the forms every line of this stretch is written in**, the premise
      ledger, the declared start state, the standing bars, the findings rule);
    - lines 395–430 (how §L is written);
    - **lines 2266–2276 and 2336–2346** (the tables of §L.21 and §L.22, which hand their derived rows' lines to §L.23);
    - **lines 2398–2515 (§L.23, your stretch)**;
    - lines 6616–6820 (Task 3, whole);
    - lines 7111–7135 (*What this batch does NOT do*).

    **Do not read in this session:** lines 38–58; lines 431–2265 and 2277–2335 and 2347–2397 (the other entries of §L.1
    to §L.22, applied); lines 2516–5906 (§L.24 to §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines
    6821–7110 (Tasks 4 and 5); lines 7136 to the end. Nor the derivation, the successor, `FRAMEWORK.md` or
    `cowork_derived_specification_l0_l1_2026_09_03.md`.
11. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 77 rows §3.2 names (82 row-parts), whole, at §6** (lines 435–79122): find each by its heading with
      the Grep tool, pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** inside §6; read
      from that heading to the row's closing `---`. The writing side found every one exactly once, in the whole file;
    - §10 (lines 79581–80645) at the 22 entries §3.3 names, and by search for every row number of this stretch;
    - §11 (lines 80646–82788) at the places §3.4 names, and by search for every row number of this stretch.

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch (form (b-H) for Rows 3.5 (ii) and 3.15), one line ADDED to the row, the
   row's `*PROPOSED DISPOSITION.*` paragraph and every other sentence of the row untouched. Every line names
   `cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1` as its record and ruling: the ratification record
   ratifies the 80 derived rows (§L.23: *"So the 80 derived rows get ruled lines, form (b), naming this record's Ruling
   1, not recorded lines"*). The record file is written as its bare file name, as sessions 10 to 13 wrote it. Where §3.2
   names a claim, the line names it as §3.2 gives it (form (b)'s split-row rule); otherwise the line names none.
2. **Where the line goes.** Every row ends: its last existing paragraph or line, one blank line, then the row's closing
   `---` (the writing side checked all 77 at the staged copy; check each at the row). Insert the new line, followed by one
   blank line, after that blank line, so the row ends: last existing paragraph or line, blank line, **new line**, blank
   line, `---` — as the earlier stretches' lines stand. **Seven rows already carry lines from earlier stretches, and the
   new line goes after them** (ledger order). Two carry a line on the same claim (item 6): Row 2.6
   (`cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md`, a RECORDED line) and Row 3.5 (two lines of
   `cowork_rulings_2026_11_03_l3_key_areas_sitting.md`, claims (i) and (ii)). Five carry lines on other claims only:
   Row 7.189 (claim (i)), Row 7.209 (claim (i)), Row 9.89 (claim (iii)), Row 19.38 (claims (iii) twice and (vii)) and
   Row 38.26 (claim (i)). The other 70 rows carry no `*RULED …` or `*RECORDED …`
   line yet. Each row-part gets exactly one line from this stretch.
3. **The quotation.** Each line quotes the words §3.2 gives for it. **The writing side checked every quotation against
   its source by a read-only script (words and punctuation, line breaks read as spaces, a leading `>` of a quoted block
   dropped, the bold and italic asterisks not compared): every one was found, each in the section of its source that the
   line names.** **Before writing each line, find each of its quoted passages in the source the line names, among
   those you read under §2 items 7 and 8, and compare them the same way: every word and every punctuation mark must match, line breaks read as spaces; asterisks are not compared,
   and the line keeps its marks exactly as §3.2 gives them.** The sources, passage by passage: the first quotation of
   every line of the 80 (*"the 100 DIFFERS as the eight cuts file them"*) is the ratification record's §1, first bullet;
   the next quotation(s) are the cut record's or cut surface's words, from the section the line names (for Row 40.40
   (ii), the seventh-cut surface's §2 for the twin's placement, as the line names it); an audit question is from the
   place the line names (the L2 reading file's §11 for the twin's question at cuts 1 and 2 save Row 10.207 (ii); the
   second-cut surface's §3 for Row 10.207 (ii); the seventh-cut surface's §2 for cut 7; the eighth-cut surface's §2 for
   cut 8). The form (b-H) quotation is the ratification record's §1, third bullet. A difference is a
   STOP-and-report for that line: no line written, listed in the report under *rows the act could not place* with both
   texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in §6; the claim §3.2 names exists
   in the row and the derived statement that speaks to it is **L3-S38**, at **DIFFERS** (at **AGREES** for Rows 3.5 (ii)
   and 3.15); and **the row's outgoing statement fits what the record or surface says of it**. A row that does not fit is
   a STOP-and-report for that row-part: no line, listed under *rows the act could not place* with what was read. Nothing
   is re-read into a different placement.
5. **As proposed** (form (b)'s paragraph, and the big dispatch's §L.23 table: *"A line says as proposed only where it is
   marked so here"*). Written on **ten lines only**: the four of cut 3 §3 A, the one of cut 4 §3 B and the five of cut 6
   §3 A, each a row proposed HISTORICAL and placed HISTORICAL with the comparison's own proposal kept. The writing side
   read each of the ten rows' `*PROPOSED DISPOSITION.*` for the claim named: **HISTORICAL**. If you find any of the ten
   proposed otherwise, that line is a STOP-and-report. No other line says *as proposed*, and no other wording (such as
   *"placed from"*) is added.
6. **Two lines on the same claim** (form (b)'s two-record rule, by part). Two claims of this stretch already carry a line
   on the same claim: **Row 2.6** (§L.17's RECORDED line, **RELOCATED** to *L2 — The tonal reading. The one entangled
   decision.*) and **Row 3.5 (ii)** (§L.13's RULED line, **HISTORICAL**). In both, the word is the same as this stretch's,
   so both lines stand and the row is listed under *rows named by more than one record*. If you find a claim where two
   lines' words differ, that claim is a STOP-and-report and gets neither line; if one of those lines is an earlier
   stretch's, do not delete it: STOP, do not commit, and report. **The 20 rows ruled earlier** (first-cut Ruling 1's
   twelve; second-cut Ruling 1's three and five) **get no line from this stretch** (§L.23 *Open* point (2): *"no line
   naming this Ruling 1 is added"*).
7. **A §10 or §11 line follows its row's line.** A *LEAVES L3* line (§3.3) names only row-parts whose line of §3.2 is
   written, and is not written at all if none of the row-parts it would name has its line written. A §11 entry (§3.4
   (a)) is written only if its row's line is written; the NOT QUARANTINED line (§3.4 (b)) only if Row 35.154's line is
   written.

### 3.2 The lines, cut by cut, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several rows, `<claim>` is filled in from
the row list (written `(i)`, `(ii)` … as the list gives it); where the row list gives no claim, `<claim>` and the space
after it are dropped. Where a block serves one row, the line is given whole with its claim already in it.

**The 35 derived rows of cuts 1 and 2** — the rows the first-cut record's §1b (as amended) and the second-cut record's §2
file *"as this side's derivation"*, which §L.21's and §L.22's tables hand to this entry (*"the line is §L.23's"*). Each
line quotes the ratification record's words and then the cut record's placement words. For the six QUARANTINED rows the
line also quotes the twin's audit question, which the cut record names (*"each with its twin's audit question"*) without
quoting: the twin is the one the cut's surface names (the first-cut surface's §4 table; the second-cut surface's §3),
and its question is quoted from the L2 reading file's §11 entry naming that twin (cuts 1 and 2) — or, for Row
10.207 (ii), from the second-cut surface's §3, which quotes it.

**Cut 1 (the first-cut record), HISTORICAL — 12 lines.**

Rows, in this order: 2.24; 7.209, written `(ii)`; 7.210; 7.211; 7.213; 7.217; 7.232, written `(i)`; 7.238; 7.239; 7.242, written `(i)`; 7.305; 7.319.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, §1b: "The cut now stands: HISTORICAL 29 (the twelve of Ruling 1, the five of that ruling, and the twelve derived)".
```

**Cut 1, QUARANTINED — 4 lines, one per row, each with its own question.**

Row 7.53:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, §1b: "QUARANTINED 4 (7.53, 7.62(ii), 7.117, 7.189(ii), derivation)"; "each with its twin's audit question"; the twin, the L2 reading file's Row 5.59: "does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change?".
```

Row 7.62 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, §1b: "QUARANTINED 4 (7.53, 7.62(ii), 7.117, 7.189(ii), derivation)"; "each with its twin's audit question"; the twin, the L2 reading file's Row 5.69(ii): "does the dormant function layer confirm a key-span by a cadence whose arrival falls inside it, by that test alone?".
```

Row 7.117:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, §1b: "QUARANTINED 4 (7.53, 7.62(ii), 7.117, 7.189(ii), derivation)"; "each with its twin's audit question"; the twin, the L2 reading file's Row 5.125: "does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change?".
```

Row 7.189 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, §1b: "QUARANTINED 4 (7.53, 7.62(ii), 7.117, 7.189(ii), derivation)"; "each with its twin's audit question"; the twin, the L2 reading file's Row 5.198(ii): "does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change?".
```

**Cut 1, RELOCATED — 1 line.**

Row 2.6:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, §1b: "RELOCATED to L2, naming L2-S30 (1), as proposed".
```

**Cut 2 (the second-cut record), HISTORICAL — 15 lines.**

Rows, in this order: 9.65; 10.4; 10.5; 10.204; 10.156; 10.198; 10.205; 8.106; 8.108; 9.94; 10.11, written `(ii)`; 9.89, written `(i)`; 10.141, written `(ii)`; 10.26, written `(ii)`; 10.146.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, §2: "HISTORICAL (18): the three of Ruling 1; and, as this side's derivation (surface §3)".
```

**Cut 2, QUARANTINED — 2 lines.**

Row 9.71:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, §2: "QUARANTINED, each with its twin's audit question (2), derivation"; the twin, the L2 reading file's Row 8.73: "does the dormant resolver decide a relative-pair slice by the cadence tonic-vote and the three same-collection cues?".
```

Row 10.207 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, §2: "QUARANTINED, each with its twin's audit question (2), derivation"; cowork_l3_s38_second_cut_surface_2026_11_03.md, §3: "does the dormant function layer override only by selecting among the chord engine's carried readings?".
```

**Cut 2, RELOCATED — 1 line.**

Row 10.206:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "the 100 DIFFERS as the eight cuts file them"; cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, §2: "RELOCATED to L2, naming L2-S43 (1), derivation".
```

**Cut 3, §3 A — 4 lines, each *as proposed*, each with its own second quotation.**

Row 12.13 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **HISTORICAL** — as proposed; "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 A: "The comparison's own proposal is HISTORICAL, kept"; "a status of a delivered design".
```

Row 13.23 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **HISTORICAL** — as proposed; "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 A: "The comparison's own proposal is HISTORICAL, kept"; "a build state".
```

Row 13.25:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — as proposed; "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 A: "The comparison's own proposal is HISTORICAL, kept"; "a build state".
```

Row 19.20:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — as proposed; "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 A: "The comparison's own proposal is HISTORICAL, kept"; "a design instruction for the superseded Phase E".
```

**Cut 3, §3 B — 5 lines.**

Rows, in this order: 17.2, written `(iii)`; 19.25; 19.27, written `(iv)`; 19.34, written `(i)`; 19.34, written `(ii)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 B: "The forward override — following Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md`".
```

**Cut 3, §3 C — 2 lines.**

Rows, in this order: 19.19, written `(i)`; 19.19, written `(ii)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 C: "The route back into the chord or the key — nothing-from-L3 Ruling 2"; "What is superseded is the route: a later layer's decided facts fed back to choose the chord or the key".
```

**Cut 3, §3 D — 1 line.**

Row 19.38 (v):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (v) **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_third_cut_surface_2026_11_03.md, §3 D: "The shared cadence detector"; "So the sentence's one detector feeding both is a superseded plan on both halves".
```

**Cut 4, §3 A — 3 lines.**

Rows, in this order: 20.44, written `(ii)`; 21.38; 22.1.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_fourth_cut_surface_2026_11_03.md, §3 A: "The comparison points to a row already filed HISTORICAL".
```

**Cut 4, §3 B — 1 line, *as proposed*.**

Row 21.54:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — as proposed; "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_fourth_cut_surface_2026_11_03.md, §3 B: "The comparison's own proposal is HISTORICAL, kept"; "a plan of the earlier layer stack for its Phase 2".
```

**Cut 4, §3 C — 1 line.**

Row 22.2:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_fourth_cut_surface_2026_11_03.md, §3 C: "A work list whose L2 twin is HISTORICAL; the comparison's RELOCATED not followed".
```

**Cut 5 — 2 lines** (the fifth-cut surface's §3 has no lettered groups).

Row 36.111 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_fifth_cut_surface_2026_11_03.md, §3: "What is superseded is the route: a later layer's decided facts fed back to choose the chord or the key"; "a means to key".
```

Row 35.154:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_fifth_cut_surface_2026_11_03.md, §3: "an event, a build state".
```

**Cut 6, §3 A — 5 lines, each *as proposed*.**

Rows, in this order: 38.10, written `(iii)`; 38.26, written `(iii)`; 38.36; 38.53; 38.105.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — as proposed; "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_sixth_cut_surface_2026_11_03.md, §3 A: "The gated Stage-5 step — the comparison's own proposal HISTORICAL, kept".
```

**Cut 6, §3 B — 4 lines.**

Rows, in this order: 38.41; 38.42; 38.43, written `(ii)`; 38.46.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_sixth_cut_surface_2026_11_03.md, §3 B: "The forward override — following Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md` and the third cut's §3 B".
```

**Cut 6, §3 C — 1 line.**

Row 38.49:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_sixth_cut_surface_2026_11_03.md, §3 C: "departs from the comparison's RELOCATED"; "The twin, the same sentence, is HISTORICAL by one-decision Ruling 3".
```

**Cut 6, §3 D — 1 line.**

Row 38.68:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_sixth_cut_surface_2026_11_03.md, §3 D: "departs from the comparison's RELOCATED"; "The sentence defines a key change by establishment and cadence confirmation".
```

**Cut 6, §3 E — 1 line.**

Row 38.76:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_sixth_cut_surface_2026_11_03.md, §3 E: "departs from the comparison's UNPLACED"; "The third cut filed 19.38(v) HISTORICAL as its derivation".
```

**Cut 7, §3 A — 1 line.**

Row 40.40 (ii):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_seventh_cut_surface_2026_11_03.md, §3 A: "departs from the comparison's UNPLACED"; §2, the twin's placement: "a superseded plan. What is superseded is the route: a later layer's decided facts fed back to choose the chord or the key.".
```

**Cut 7, §3 B — 2 lines.**

Rows, in this order: 39.179, written `(i)`; 40.51.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_seventh_cut_surface_2026_11_03.md, §3 B: "the old selection and the old pipeline, departing from the comparison's RELOCATED".
```

**Cut 7, §3 C — 3 lines.**

Rows, in this order: 43.19, written `(ii)`; 43.80, written `(i)`; 43.80, written `(ii)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_seventh_cut_surface_2026_11_03.md, §3 C: "the key layer's residual handed to the old function layer".
```

**Cut 7, §3 D — 1 line.**

Row 43.24:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_seventh_cut_surface_2026_11_03.md, §3 D: "the cadence-confirmed modulation"; "the cadence-confirmed modulation re-run".
```

**Cut 7, §3 E as corrected at its §6 item 2 — 2 lines, QUARANTINED.**

Rows, in this order: 43.105, written `(iii)`; 43.124, written `(ii)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_seventh_cut_surface_2026_11_03.md, §3 E as corrected at its §6 item 2: "QUARANTINED, each with the audit question its twin carries"; §2, Row 7.9(ii)'s audit question: "does the dormant key decoder decide the key before and apart from any chord, and what reads its key-spans?".
```

**Cut 8, §3 A — 3 lines, one per claim.**

Rows, in this order: 44.30, written `(i)`; 44.30, written `(ii)`; 44.30, written `(iii)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* <claim> **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_eighth_cut_surface_2026_11_03.md, §3 A: "a superseded plan. What is superseded is the route: a recogniser over decided chords feeding its output back to revise the key".
```

**Cut 8, §3 B — 1 line, QUARANTINED.**

Row 45.16 (i):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (i) **QUARANTINED** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_eighth_cut_surface_2026_11_03.md, §3 B: "QUARANTINED, with the audit question its twin carries by travel"; §2, Row 5.59's audit question: "does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change?".
```

**Cut 8, §3 C — 1 line.**

Row 45.21 (i):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (i) **HISTORICAL** — "the 100 DIFFERS as the eight cuts file them"; cowork_l3_s38_eighth_cut_surface_2026_11_03.md, §3 C: "the cadence-confirmed modulation re-run".
```

**Rows 3.5 (ii) and 3.15, form (b-H) — 2 lines** (the ratification record's §1, third bullet; Row 3.5 names claim (ii), Row 3.15 has no claims):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "Rows 3.5(ii) and 3.15 as key-areas Ruling 2 decides them (decided against; 3.15 by travel with 3.5(ii), this side's derivation)".
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* **HISTORICAL** — "Rows 3.5(ii) and 3.15 as key-areas Ruling 2 decides them (decided against; 3.15 by travel with 3.5(ii), this side's derivation)".
```

**The count.** `*RULED DISPOSITION (`: cut 1, 12 + 4 + 1 = 17; cut 2, 15 + 2 + 1 = 18; cuts 3 to 8, 12 + 5 + 2 + 12 + 9
+ 5 = 45; form (b-H), 2; in all **82**. By word: HISTORICAL 12 + 15 + 42 + 2 = **71**; QUARANTINED 4 + 2 + 2 + 1 =
**9**; RELOCATED **2**. None opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, each the writing side's and overrulable by the user:* (1) every line of the 80 quotes the
ratification record's *"the 100 DIFFERS as the eight cuts file them"* first, then the cut's words, naming the cut record
or cut surface by its bare file name and section (the big dispatch says *"each with its cut record's placement words"*
and *"each with its cut surface's placement words"* without giving cuts 1 and 2's words or a shape); (2) cut 1's words are
taken from the first-cut record's amendment (*"The cut now stands: …"*) for HISTORICAL, and from its amendment and its
§1b bullet for QUARANTINED, because the bullet's count *"(24)"* is the former wording; (3) **the six QUARANTINED rows of
cuts 1 and 2 carry their twin's audit question as found at the L2 reading file**: the twins are the cut surfaces' (Rows
5.59, 5.69(ii), 5.125, 5.198(ii), 8.73, 6.190 (iii)); Rows 5.125 and 5.198(ii) carry *"as at Row 5.59"* there, so their
question is Row 5.59's; Row 8.73's is the question of its §11 entry, *"travelling with Row 5.148"* (the second-cut
surface also calls Row 9.71 *"the group of 7.53"*; the writing side reads that as the filing group, not the question);
(4) where the big dispatch's table describes a cut surface's placement without quoting it (cut 6 §3 C, D and E; cut 7
§3 B and C), the line quotes the cut surface's own §3 heading words and, for cut 6 §3 C to E, one sentence of the ground
beneath it; at cut 7 §3 A and D, where the table quotes a ruling's words as the surface gives them, the line quotes the
§3 heading words and then those words, at the place in the surface where they stand (§2 for §3 A, §3 D for §3 D).

### 3.3 The transfer list, §10 (Task 3 (c) item 6)

Task 3 (c) item 6, acting by claim (the item-six record's Ruling 1): beneath each §10 entry that names a row-part
carrying a ruled line from this stretch, ONE line naming the row-parts it covers. Every line below goes beneath the last
line of the §10 entry named, **opening with exactly two spaces** (the indentation of the entry's continuation lines, as
sessions 12 and 13 wrote theirs), the entry and every other line under it untouched. **Three of the entries already
carry a *LEAVES L3* line written by session 13; the new line goes after it.** Line numbers are those of the staged copy,
before any edit; find each entry by its opening text, which the writing side found exactly once.

Each quotation is the ratification record's take-off sentence (its §1, the *Documentation* sentence, lines 54–55); compare
it as §3.1 item 3 says.

1. Beneath the entry beginning `- Row 2.24` (line 79809), after its last line, line 79810, which ends `layers above publish. *(L3-S38 DIFFERS at the row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 2.24: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
2. Beneath the entry beginning `- Rows 7.15, 7.28 (ii), 7.55, 7.62 (i), 7.130, 7.131, 7.132, 7.133, 7.134, 7.149, 7.150, 7.191, 7.194, 7.209 (ii),` (line 79821), after its last line, the *LEAVES L3* line session 13 wrote beneath it (line 79826), which names the first-cut record:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 7.209 (ii), 7.210, 7.213, 7.217, 7.238, 7.239, 7.242 (i) and 7.305: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
3. Beneath the entry beginning `- Rows 7.12, 7.13 (i), 7.16, 7.17 (i), 7.46, 7.56, 7.57, 7.135 to 7.145, 7.147, 7.148, 7.192, 7.193, 7.196 (iii),` (line 79827), after its last line, the *LEAVES L3* line session 13 wrote beneath it (line 79832), which names the second-cut record:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 7.211 and 7.232 (i): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
4. Beneath the entry beginning `- Rows 7.53, 7.62 (ii), 7.97 (ii), 7.98, 7.99, 7.117, 7.118, 7.119, 7.189 (ii), 7.282 and 7.319` (line 79835), after its last line, line 79838, which ends `consumption of cadence facts the same way.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 7.53, 7.62 (ii), 7.117, 7.189 (ii) and 7.319: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
5. Beneath the entry beginning `- Rows 8.106 and 8.108` (line 79858), after its last line, line 79859, which ends `election among carried readings. *(L3-S38 DIFFERS at both.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 8.106 and 8.108: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
6. Beneath the entry beginning `- Rows 9.33 (ii), 9.34 (ii), 9.64, 9.65, 9.66 (i), 9.67, 9.89 (i) and 9.130` (line 79862), after its last line, line 79864, which ends `*(L3-S38 DIFFERS at Rows 9.65 and 9.89 (i).)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 9.65 and 9.89 (i): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
7. Beneath the entry beginning `- Rows 9.68, 9.69, 9.70, 9.71, 9.72, 9.73, 9.74 (i), 9.75, 9.76, 9.78 and 9.79` (line 79869), after its last line, line 79871, which ends `e, the weights fitted later. *(L3-S38 DIFFERS at Row 9.71.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 9.71: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
8. Beneath the entry beginning `- Row 9.94` (line 79884), after its last line, line 79884, which ends `recompute, never a back-edge. *(L3-S38 DIFFERS at the row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 9.94: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
9. Beneath the entry beginning `- Rows 10.4, 10.5, 10.11 (ii), 10.23 (i), 10.26 (ii), 10.141 (ii), 10.146, 10.147 (ii), 10.156, 10.178, 10.198, 10.204,` (line 79920), after its last line, the *LEAVES L3* line session 13 wrote beneath it (line 79924), which names the second-cut record:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 10.4, 10.5, 10.11 (ii), 10.26 (ii), 10.141 (ii), 10.146, 10.156, 10.198, 10.204, 10.205 and 10.207 (ii): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
10. Beneath the entry beginning `- Row 17.2 (iii)` (line 79967), after its last line, line 79968, which ends `ward recompute. *(As Row 7.238; L3-S38 DIFFERS at the row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 17.2 (iii): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
11. Beneath the entry beginning `- Rows 19.19 (i), 19.19 (ii), 19.25, 19.27 (iv), 19.34 (i) and 19.34 (ii)` (line 79969), after its last line, line 79971, which ends `onfirming the key. *(As Row 7.238; L3-S38 DIFFERS at each.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 19.19 (i), 19.19 (ii), 19.25, 19.27 (iv), 19.34 (i) and 19.34 (ii): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
12. Beneath the entry beginning `- Row 20.44 (ii)` (line 79981), after its last line, line 79982, which ends `7.13 (i); L3-S38 DIFFERS at the row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 20.44 (ii): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
13. Beneath the entry beginning `- Row 21.38` (line 80000), after its last line, line 80001, which ends `it. *(As Row 2.24; L3-S38 DIFFERS at the row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 21.38: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
14. Beneath the entry beginning `- Row 22.1` (line 80008), after its last line, line 80009, which ends `21.38; L3-S38 DIFFERS at the row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 22.1: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
15. Beneath the entry beginning `- Row 22.2` (line 80010), after its last line, line 80011, which ends `row.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 22.2: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
16. Beneath the entry beginning `- Rows 38.38, 38.39, 38.40, 38.41, 38.42, 38.43 (ii), 38.44, 38.45, 38.46 and 38.49` (line 80067), after its last line, line 80071, which ends `38.49.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 38.41, 38.42, 38.43 (ii), 38.46 and 38.49: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
17. Beneath the entry beginning `- Rows 38.65, 38.66, 38.68, 38.69, 38.73, 38.74, 38.75 and 38.77 (iii)` (line 80077), after its last line, line 80080, which ends ` as one span with the other tonality's reading as a rival.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 38.68: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
18. Beneath the entry beginning `- Rows 39.107 (ii), 39.161 (i), 39.162, 39.163, 39.165 (i), 39.177 (i), 39.179 (i), 39.180, 39.197 (i), 39.203 (iii),` (line 80098), after its last line, line 80105, which ends `-S8 publishes pedal point among the elaboration relations.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 39.179 (i): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
19. Beneath the entry beginning `- Rows 40.49, 40.50 (ii), 40.51, 40.52, 40.53 (i), 40.57, 40.58 and 40.59` (line 80118), after its last line, line 80121, which ends `ternatives already carried. *(L3-S38 DIFFERS at Row 40.51.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Row 40.51: "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
20. Beneath the entry beginning `- Rows 43.9, 43.19 (i), 43.19 (ii), 43.20 (i), 43.20 (ii), 43.22 (ii), 43.23, 43.24, 43.25 (i), 43.25 (ii), 43.27 (i),` (line 80161), after its last line, line 80167, which ends `43.20 (ii) lie on register entry D-343's home, unmarked.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 43.19 (ii), 43.24, 43.80 (i), 43.80 (ii), 43.105 (iii) and 43.124 (ii): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
21. Beneath the entry beginning `- Rows 44.17, 44.18, 44.25, 44.26, 44.27 (i), 44.27 (ii), 44.28 (i), 44.29, 44.30 (i), 44.30 (ii), 44.30 (iii) and` (line 80186), after its last line, line 80192, which ends `(ii) and 44.28 (i) on D-505's as well, SEEN homes, marked.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 44.30 (i), 44.30 (ii) and 44.30 (iii): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```
22. Beneath the entry beginning `- Rows 45.16 (i) and 45.21 (i)` (line 80193), after its last line, line 80196, which ends `unmarked.)*`:
   ```
  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — Rows 45.16 (i) and 45.21 (i): "the 100 DIFFERS and Rows 3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application dispatch, not now."
   ```

**What is not named, and why.** The writing side searched §10 for every row number of this stretch as a bare number
with look-around and read each hit. The 22 entries above name the 63 row-parts listed in them. Every other hit is a
mention by way of comparison (*"As Row 2.24"*, *"as at Rows 38.46 and 40.51"*, *"As Rows 19.25 and 19.34"*) or names
another claim (Rows 7.62 (i), 7.209 (i), 9.89 (ii), (iv) and (v), 10.11 (i), 10.26 (i), 10.141 (i), 10.207 (iii), 19.27
(iii), 19.38 (i), (ii) and (iv), 20.44 (i), 38.10 (i) and (ii), 38.26 (ii), 38.43 (i), 40.40 (i), 43.19 (i), 43.80 (iii),
43.105 (ii), 43.124 (i), 45.16 (ii), 45.21 (ii)), and gets nothing. No range in §10 (*"n to m"*) covers a row of this
stretch. **Rows 2.6 and 10.206** are RELOCATED by their lines here and get no *LEAVES L3* line (Task 3 (c) item 6: *"A row whose own line in this
dispatch is RELOCATED gets no LEAVES L3 line"*); Row 10.206 stays named in the entry beginning `- Rows 10.4, 10.5`, Row
2.6 in the entry beginning `- Row 2.3(ii), with Rows 2.5 and 2.6`. **Fifteen row-parts of this stretch stand in no §10
entry** (Rows 12.13 (ii), 13.23 (ii), 13.25, 19.20, 19.38 (v), 21.54, 35.154, 36.111 (ii), 38.10 (iii), 38.26 (iii), 38.36,
38.53, 38.76, 38.105, 40.40 (ii); proposed HISTORICAL, QUARANTINED or UNPLACED, not RELOCATED), nor do Rows 3.5 (ii) and
3.15 (proposed ADOPTED — proposed). 63 + 2 + 15 + 2 = 82. **No §10 addition under Task 3 (c) item 5**: Rows 2.6 and
10.206 are already carried by §10.

### 3.4 The audit questions, §11 (Task 3 (c) item 7)

**(a) Nine entries added**, one for each row-part this stretch places QUARANTINED; none of the nine is carried by §11 now
(the writing side's search of §11 by row number and claim: for Row 10.207 only claim (i) is carried, for Row 45.16 only
claim (iii); neither is touched). Each entry is ONE line in §11's own entry form, the audit question quoted as the row's
line quotes it, then the record in a parenthesis, placed under its member's heading at its place in row order:

1. Under **Member 7**, two lines **before** the line beginning `- Row 7.72 — do the as-built modulation recompute` (line
   80762), in this order, after the entry `- Row 7.22 — …` (line 80761):
   ```
- Row 7.53 — does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
- Row 7.62 (ii) — does the dormant function layer confirm a key-span by a cadence whose arrival falls inside it, by that test alone? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
2. Under **Member 7**, one line **before** the line beginning `- Row 7.128 — are §5.3 and §5.4 implemented` (line 80767),
   after the entry beginning `- Row 7.80, with Row 7.86 —` (line 80766):
   ```
- Row 7.117 — does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
3. Under **Member 7**, one line **before** the line beginning `- Row 7.204 (i) — is the function confidence's` (line
   80786), after the entry `- Row 7.182 (i) — …` (line 80785):
   ```
- Row 7.189 (ii) — does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
4. Under **Member 9**, one line **before** the line beginning `- Row 9.74 (ii) — does the as-built resolver test` (line
   80908), after the entry beginning `- Row 9.63 —` (lines 80906–80907):
   ```
- Row 9.71 — does the dormant resolver decide a relative-pair slice by the cadence tonic-vote and the three same-collection cues? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
5. Under **Member 10**, one line **before** the line beginning `- Row 10.209, with Row 10.212 —` (line 80971), after the
   entry beginning `- Row 10.207 (i) —` (lines 80969–80970), which is not touched:
   ```
- Row 10.207 (ii) — does the dormant function layer override only by selecting among the chord engine's carried readings? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
6. Under **Member 43**, one line **before** the line beginning `- Row 43.109 — does the key decoder's candidate scoring`
   (line 82588), after the entry beginning `- Row 43.103 —` (line 82587):
   ```
- Row 43.105 (iii) — does the dormant key decoder decide the key before and apart from any chord, and what reads its key-spans? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
7. Under **Member 43**, one line **before** the line beginning `- Row 43.125 — on which run or simulation` (line 82597),
   after the entry beginning `- Row 43.123 —` (lines 82595–82596):
   ```
- Row 43.124 (ii) — does the dormant key decoder decide the key before and apart from any chord, and what reads its key-spans? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```
8. Under **Member 45**, one line **before** the line beginning `- Row 45.16 (iii) — on which run was the cadence vote`
   (line 82630), which is not touched, after the entry beginning `- Row 45.15 (iv) —` (lines 82628–82629):
   ```
- Row 45.16 (i) — does the dormant cadence detector cast a weighted tonic vote per region, and what does the vote change? *(cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1.)*
   ```

*Where the claim stands in the entry — `- Row 7.62 (ii) —`, a space before the parenthesis, as §11 writes `- Row 10.207
(i) —` — and the one-line form are the writing side's settlement; item 7 (a) gives the form `- Row n.m — <the audit
question>` and does not say how a claim is written. Overrulable by the user.*

**(b) One NOT QUARANTINED line.** §11 carries an entry for **Row 35.154** (lines 82034–82035, beginning `- Row 35.154 —
does `HarmonicFunctionContext` carry phrase-boundary`), the whole row, which this stretch places **HISTORICAL**.
Beneath its last line (line 82035, `  the chord competition read it?`), ONE line, opening with exactly two spaces:
```
  *NOT QUARANTINED (cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* — placed **HISTORICAL** at the row.
```
The writing side's search found no other §11 entry for a claim this stretch places with a word other than QUARANTINED
(the §11 entries for Rows 13.23 (i), 10.207 (i), 38.10 (iv), 39.179 (ii) and 45.16 (iii) name other claims, and are not
touched). Run the same search yourself; if you find another, add the NOT QUARANTINED line item 7 (b) gives, and report
it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.23 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.24 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 4 commit, as in sessions 11 to 13.
   Attribute it in the diff table to *"session 14's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.23
   only**, after sessions 10 to 13's §L.1 to §L.22. §L.24 to §L.55 are not applied, read or touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1204 and 1205 ARE landed**, with this file, in §5 act 1, as sessions 8 to 13 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the one record §L.23 enters
   (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case not matched). §L.23 says it
   finds two hits, both *"decided against"*, at the record's lines 18 and 39, both naming Rows 3.5 (ii) and 3.15, which
   §3.2 places by form (b-H); the writing side's search found the same and nothing else. List the result in the report.
   Item 2: not reached. Item 3: not reached. Item 4: not reached. Item 5: nothing to append (§3.3, last sentence). Item 6:
   §3.3. Item 7: §3.4.
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 4 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry, and this stretch is one entry: if signs of context degradation appear before every line is applied, do
   not commit; STOP and report which lines were applied to the uncommitted copy and that it is not landed. *(The
   writing side sized the stretch against sessions 10 to 12: they wrote 306 of the reading file's 327 RULED, RULED
   PLACEMENT and RECORDED lines between them, about 100 a session.)*
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 4 commit:**
     `git diff 857b2fa64fe1f57cd0ee649f95885b3e81ffd9a0 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session14_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; a *LEAVES L3* line of §3.3; an audit-question entry of §3.4 (a); the NOT
     QUARANTINED line of §3.4 (b), and any further one §3.4 (b) found; the in-progress line of §3.5 item 3. Then
     `git diff --numstat 857b2fa64fe1f57cd0ee649f95885b3e81ffd9a0 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1 deleted line** and **2 × N + 33 added lines**, N being the number of lines of §3.2 you wrote
     (82 less the STOP-and-reports; **197 added** if none), less 1 for each *LEAVES L3* line, §11 entry or NOT
     QUARANTINED line not written under §3.1 item 7, plus 1 for each further NOT QUARANTINED line §3.4 (b) found. *The
     writing side's arithmetic for the 33: 22 LEAVES L3 lines, 9 §11 entries, 1 NOT QUARANTINED line, and the in-progress
     line (a replaced line: one added, one deleted).*
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 4 deleted lines** (the four lines session 10's state sentences were written into) and **707 +
     2 × N added lines** (**871** if none), with the same adjustments as above. *The writing side's arithmetic: against
     the Task 2 commit the reading file stood at 675 added and 4 deleted after session 13 (from session 13's report;
     checked at the check turn by comparing the Task 2 commit's blob of the file, `48e24b2f82f76c57cfd5cd14b86780c567db0f70`,
     with the staged copy); this stretch adds 2 × N lines and the 32 lines of §3.3 and §3.4 (675 + 32 = 707). The
     in-progress line replaces a line that is itself an addition against the Task 2 commit, so it adds no line and
     deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **271 + 82 = 353**, less the
     number of §3.2's lines you listed as STOP-and-report; `\*RECORDED DISPOSITION \(` must count **53**;
     `\*RULED PLACEMENT \(` must count **3**; `\*LEAVES L3 \(` must count **4 + 22 = 26**, less those not written;
     `\*Row 7\.67 is not transferred` must count **1**; `\*NOT QUARANTINED \(` must count **1**, or the number §3.4 (b)
     gives you.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 5 (§L.23): the rows of the L3-S38 ratification re-marked in the reading file, twenty-two LEAVES L3 lines added to the transfer list, nine audit questions and one NOT QUARANTINED line added, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_14_task_3_stretch_5_2026_11_23.md`**, as sessions 2 to 13
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.24, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own, before any edit to the reading file.**
   Exactly three paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_14_task_3_stretch_5_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_four.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_five.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1204 and 1205 and the session 14 instruction of the L3 application landed; Task 3 stretch 5 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: §3.2's lines in the order
   given (cut 1, cut 2, cuts 3 to 8, then Rows 3.5 (ii) and 3.15), each row's *LEAVES L3* line written when the last of
   the row-parts it names has its line; then §3.4 (a) and (b); then §3.5 item 3; then §4 item 8's checks, the commit and
   the push. *(The order inside the stretch is the writing side's; the big dispatch sets none.)*
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_14_task_3_stretch_5_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 14 of the L3 application, Task 3 stretch 5 (§L.23) written; stretch 6 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each cut, and for Rows 3.5 (ii) and 3.15: every line by row and claim, written (with its reading-file line number
   after the edit) or STOP-and-report (and why). The same for §3.3's 22 lines and §3.4's ten.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place*; *rows given no line now*
   (none expected); *recorded lines not written: no disposition word* (none expected); *rows named by more than one
   record* — Row 2.6 (§L.17's RECORDED line and this stretch's ruled line, both RELOCATED to L2) and Row 3.5 (ii) (§L.13
   and this stretch, both HISTORICAL); *ADOPTED words read at the row* (none expected); *audit questions added* (the nine
   of §3.4 (a)); *audit questions no longer quarantined* (Row 35.154); *§10 rows a record says leave, not named by row*:
   the 16 AGREES row-parts proposed RELOCATED which the ratification surface's §2 lists (15 to L2, 1 to the second axis)
   and which stand in §10 — the record keeps their proposals (*"38 of the 40 AGREES with their proposals standing, not
   re-marked"*), so they get no line and no *LEAVES L3* line; list them by number from the surface's §2 and say so; the
   decided-against search (§4 item 4).
5. The diff table of §4 item 8, every changed passage attributed, and the six counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: the 38 AGREES other than Rows 3.5 (ii) and
   3.15 (*"not re-marked"*; Row 8.110 among them); the 20 rows ruled earlier (their lines are §L.21's and §L.22's; §L.23
   *Open* point (2)); and the rows §L.23 lists as mentioned and not placed (the L2 twins Rows 53.53 and 52.14). *A
   heading of this session's report only, as in sessions 10 to 13's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 14 of the L3 application ends here. Stretch 6 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a row-part that
  is STOP-and-report under them, or under §3.1 items 3 to 7, is reported and the remaining ones applied, as they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 6);
- an entry §3.3 or §3.4 names is not found exactly once by its opening text, or its last line does not end as given;
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1204. Read at the objects for this file: the
three git reference files (both refs `d56ccc6e…`); entries 1204, 1203 and 1026 (its §3) whole; session 13's instruction
whole; the ratification, first-cut and second-cut records whole; the ratification surface whole; the first-cut surface at
its §4 and by its headings; the second-cut surface at its §3; the third- to eighth-cut surfaces at their §3, by their
headings and lettered groups, and by search; the L2 reading file at the twins' rows (their `*PROPOSED`, `*RULED` and
`*RECORDED` lines) and at three entries of its §11; the big dispatch at lines 159–274, 2252–2515 and 6616–6820 and by
its headings. The reading file, by read-only scripts over the staged copy: its `##` headings, the 77 rows' headings (each
once in the whole file), each row's claims, derived statements, axis, `*PROPOSED DISPOSITION.*` paragraph, earlier lines
and closing lines; §10 and §11 searched for this stretch's row numbers as bare numbers with look-around, every §10 hit
read by the entry it stands in; the 22 §10 entries' opening and last lines; the §11 places of §3.4; the in-progress line;
and the current counts. Every quotation of §3.2, §3.3 and §3.4 checked against its source by a read-only script (words and
punctuation, line breaks read as spaces, a leading `>` dropped, asterisks not compared): all found. Every line of §3.2
generated by script from one table of groups, rows and quotations, and the 82 lines counted by word from it. Computed
as git would on the staged copy: the reading file's blob `5bccffae…` (counts 271 / 3 / 53; *LEAVES L3* 4; *Row 7.67 is
not transferred* 1; NOT QUARANTINED 0). Relayed, not re-checked here: the big dispatch's blob `b5274c2c…` (entry 1204
and session 13's instruction), the archive JSON's blob `1df4f207…` and the untracked paths (session 13's instruction and
entry 1204), the end of `cowork_handoff.md`'s topmost block at line 255, the line-180 start of
`cowork_audit_protocol.md`'s dispatch-protocol section, the part 2 record's Ruling 3 at lines 89–125 (as session 13's
instruction gives them), and the 675 added and 4 deleted lines against the Task 2 commit.*

*The check, as a turn of its own: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1205, the file not yet
handed to Claude Code, so its corrections keep no former wording (as entry 1203 §2 item 4 did). Read at the objects:
this file whole; the ratification, first-cut, second-cut and item-six records whole; the ratification surface's §2; the
second- to eighth-cut surfaces at their §2 and §3 (the seventh-cut surface's §6 item 2 too); the first-cut surface at
its §4 twins line; the L2 reading file at the three §11 entries and at the twins' rows, Row 8.73's travel read through
Row 8.12 to Row 5.148; the big dispatch at §L.21's and §L.22's tables, §L.23 whole, the forms section and Task 3 (c)
item 7. By read-only scripts over the staged copies: every quotation of §3.2 and §3.3 found in the section of its
source the line names, and every §3.4 question equal to its row's line; the 82 lines rebuilt from the templates (71
HISTORICAL, 9 QUARANTINED, 2 RELOCATED; *as proposed* on the ten only); the 82 row-parts at their rows (each heading
once, inside §6; the claim present; L3-S38 at DIFFERS, AGREES at Rows 3.5 (ii) and 3.15; the earlier lines as §3.1 item
2 lists them; each row ending blank line then `---`); the 22 §10 entries and every §10 mention of this stretch's rows;
the 16 AGREES rows proposed RELOCATED, each in §10; the §11 places, member headings and row order; the in-progress line
and the six counts. Checked here and no longer relayed: the big dispatch's blob `b5274c2c…` (computed on the staged
copy) and the 675 added and 4 deleted lines (the Task 2 commit `4b6dc3bd…`, its tree and the reading file's blob
`48e24b2f…` inflated from loose objects and compared with the staged copy). Corrected: Row 40.40 (ii)'s line, whose
second quotation stands at the seventh-cut surface's §2, not its §3 A; the lines of Rows 43.105 (iii), 43.124 (ii) and
45.16 (i), which now name the cut surfaces' §2 for their audit questions; §3.1 item 3 to match; settlement (4) of §3.2,
which named cut 7 §3 A and D among the places the big dispatch does not quote; §3.3's list of other claims, which lacked
10.207 (iii) and 43.19 (i); the placeholder `<part>` written `<claim>` and "lettered parts" written "lettered groups"
(`CLAUDE.md`'s reserved words); §4 item 8's note on the 675. No line's disposition word, row, claim or count changed.*
