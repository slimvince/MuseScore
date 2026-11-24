# CC dispatch — the L3 application, SESSION 25 of several: Task 3 of the L3 application dispatch, sixteenth stretch (§L.40), and nothing else

> **STATUS: WRITTEN AND CHECKED 2026-11-24.** Written by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_two.md`, which first verified session
> 24's stretch at the objects (no finding) and then wrote this file in the same sitting, under the user's Ruling 1 (d) of
> 2026-11-24. Checked as a turn of its own by a NEW Cowork session (Ruling 1 (e)), the sitting booted on entry 1233:
> no finding, no line of §3.2 and no expected figure changed; that session added its own entry 1234 to what §5 act 1
> lands (§8, the check note).
> Under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 23 applied Task 3's first fourteen stretches, §L.1 to §L.38. Session
24 applied the fifteenth stretch, §L.39, in commit `b8bd4bddf4d1ac0fa1632ef19d049f76860e30e2` (called **the stretch 15
commit** below), and committed its report as `75955ee9d3da2fbeba04742375e3c9364e374106`, the current tip.

**This is session 25. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry: §L.40, the record of family 2, *how
published facts are displayed*. It commits that sixteenth stretch as ONE commit, pushes it, writes its report, and
STOPS.** §L.41 is a later session's.

**Why the stretch covers this one entry and stops at §L.41** (the user's Ruling 2 of 2026-11-24: a writing session
judges how many ledger entries fit). §L.40's record (6,063 bytes) places 16 row-parts on 15 rows in one ruling, and
gives 17 lines: 13 placements outside every charter (form (c-P)), 3 ADOPTED lines whose word is read at the row's axis
(form (b)'s paragraph *Which ADOPTED word*, item (4)), and 1 HISTORICAL line (form (b-H)). No row carries an earlier
line, and nothing goes to §10 or §11. §L.41 (its record 8,381 bytes) brings RELOCATED lines with their §10 entries and a
row split four ways, one part *"carried by L3-S1"*; the sitting that wrote this file had already carried a full
verification of session 24's stretch and judged that it could not add §L.41 and still re-run its simulation cleanly.
The stretch stops at the boundary before §L.41.

**What this stretch writes, in one paragraph.** **17 lines on 15 rows**, all from
`cowork_rulings_2026_11_07_l3_display_family_sitting.md`, Ruling 1: **13 opening `*RULED PLACEMENT (`** (outside every
charter, no disposition word — Rows 4.6, 4.18, 4.19, 48.35, 40.60 and 7.36 whole; Rows 48.26 (ii) and 48.27 (ii); Rows
48.36 (i) and 48.36 (iii), two lines at one row; Rows 22.58 (i) and 50.2 (i); and Row 48.20 (ii)'s second half); and
**4 opening `*RULED DISPOSITION (`**: **2 with the word ADOPTED — carried (L3-S5)** (Row 48.19, and Row 48.20 (ii)'s
first half), **1 with the word ADOPTED — proposed** (Row 40.61) and **1 with the word HISTORICAL by form (b-H)** (Row
48.17 (iii)). **No line says *as proposed*:** every row-part named is proposed UNPLACED at its row. §3.2 gives every
line with its exact text. **Nothing at §10** (§3.3), **nothing at §11** (§3.4), and the in-progress line brought
forward from §L.39 to §L.40 (§3.5). **No earlier line is edited.**

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only.** This session copies into the reading file the placements the record already makes; it decides
nothing and changes no algorithm. The record states *"Documentation only. Algorithm: no change."* and *"The ruling adds
no published fact, field, evidence or check."* Its notes list (form (a), the successor's *Notes*) is Task 1's, not this
stretch's (§L.40, *Successor*); it orders no charter or interface-contract amendment.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `75955ee9d3da2fbeba04742375e3c9364e374106`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_25_task_3_stretch_16_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 15 commit left it.**
   `git diff --quiet b8bd4bddf4d1ac0fa1632ef19d049f76860e30e2 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 75955ee9d3da2fbeba04742375e3c9364e374106 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `b8be2e98cbcb40e993f439c1cb3465b8d8f11e50`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **514**; `\*RULED PLACEMENT \(` must count **10**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting`
   must count **13**; `cowork_rulings_2026_11_03_l3_cadence_type_sitting` must count **36**; and
   `cowork_rulings_2026_11_07_l3_display_family_sitting` must count **0**. Any other result: STOP and report, the file
   not touched. (The writing side's copy: 5,324,496 bytes, 84,662 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 75955ee9d3da2fbeba04742375e3c9364e374106 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the files §5 act 1 lands (this instruction and handoff entries 1233 and 1234), plus the paths sessions 2 to 24 reported and did not land (387 under
     `scratch_artifacts/`; `Claude outputs/`; `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the
     two PDFs under `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
     `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md`, which session
     18 reported byte-identical to its own instruction and did not land — it is not landed here either, not touched, and
     not a STOP). `.claude/` and `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list
     them; that is expected and not a STOP. List in the report every untracked path the tool reports outside those. A
     further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is
     not a STOP (the big dispatch's A1, unchanged).

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
   the read-first block), and **the handoff entries §5 act 1 lands, whole**: entry 1233 (written by the sitting that
   wrote this file) and entry 1234 (written by the session that checked it). Both are untracked; §5 act 1 lands them.
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The record this stretch rests on, WHOLE** — it is the authority for every line this session writes (**the record's
   own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md` (§L.40; 6,063 bytes, 80 lines).
8. **Two release records and the working list, at these lines only, with the Read tool:**
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`, lines 12–49 (Ruling 1:
     the line for a row-part placed outside every charter) and lines 363–420 (Ruling 9: which ADOPTED word a line
     writes, with the writing side's reading of the axis for §L.40's three ADOPTED rows at its lines 407–409);
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part3_sitting.md`, lines
     9–38 (Ruling 1: Row 48.17 (iii) HISTORICAL for part (iii) whole, the record's sentence quoted whole);
   - `ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md` (the working list), lines 831–849 (item
     (xxix), Row 48.17 (iii)) and lines 971–1000 (item (xxxiii), the thirteen row-parts and Row 48.20 (ii)'s two lines).

   **Do NOT read the records of §L.1 to §L.39 or of §L.41 to §L.55, and do not open the record's surface** (the lines
   quote the record only).
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, form (b-H) and form (c-P)**, the premise ledger, the declared start state, the standing bars,
     the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 4245–4350 (§L.40, your stretch)**;
   - lines 6616–6820 (Task 3, whole, **with (c) items 1 and 5, the decided-against search and the transfer list**);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–4244 (§L.1 to §L.39, applied); lines 4351–5906 (§L.41 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 15 rows §3.2 names, whole, at §6** (lines 435–79622): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
      heading to the row's closing `---`, **its *Current-text axis* paragraph included** (§3.1 item 5 reads the word
      there). The writing side found every one exactly once, inside §6;
    - §10 (lines 80081–81183), searched with the Grep tool for every row number of this stretch (§3.3);
    - §11 (lines 81184–83336), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The forms.**
   - **The 13 placement lines take form (c-P)** (the big dispatch's forms section; Ruling 1 of the release part 2
     record): `*RULED PLACEMENT (<record file>, Ruling 1).* Outside every charter — <the record's placement in its
     words>; listed in the successor's notes.`, naming the part where the ruling places a part only, the part named
     before *Outside every charter*, as §L.40's table gives each line. **No disposition word is written**; the row-part
     is not counted in the ruled distribution and is listed in the report as placed outside every charter.
   - **The 3 ADOPTED lines take form (b)**, one line ADDED to the row; Row 48.20's names its claim and half.
   - **The HISTORICAL line of Row 48.17 takes form (b-H)**: form (b) with the word **HISTORICAL**, the placement quoting
     the record's sentence that decides against the part, whole, its ground included (the list-answers part 3 record,
     Ruling 1), the line naming part (iii).
   Every line names its record's file and its ruling, the record file written as its bare file name, as sessions 10 to
   24 wrote theirs. The row's `*PROPOSED DISPOSITION.*` paragraph and every other sentence of the row stay untouched.
2. **Where the line goes.** A ruled line goes *"immediately beneath a row's `*PROPOSED DISPOSITION.*` paragraph"* (the
   big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after any earlier ruled
   or recorded line standing there, and above any paragraph that follows them.** Each new line is followed by one blank
   line. Where one row gets several lines, they go in the order §3.2 gives them. Read each row's actual shape from its
   proposed paragraph to its end before writing. **The writing side read all 15 rows at its copy of the file (blob
   `b8be2e98…`). No row carries an earlier ruled, placement or recorded line.** Their shapes after the proposed
   paragraph:
   - **nothing between the proposed paragraph and `---`; the new lines go after the blank line that follows the
     proposed paragraph, before `---`:** Rows 4.6, 4.18, 4.19, 7.36, 22.58, 48.17, 48.19, 48.20, 48.26, 48.27, 48.35,
     48.36 and 50.2;
   - **the proposed paragraph, then a paragraph headed *"The decisions register at this row."*, then `---`; the new line
     goes after the blank line that follows the proposed paragraph, above *The decisions register at this row.*:** Rows
     40.60 and 40.61. That paragraph is not touched.

   If you find a different shape at a row (an earlier line not listed here, a further paragraph, or an ending other
   than `---`), state it in the report and place the lines by the rule in bold above; if the rule does not settle where
   they go, that row's lines are a STOP-and-report.
3. **The quotation.** Each line quotes the record's words as §3.2 gives them:
   - the 13 form (c-P) lines: the placement *"carried for a display's own specification"* (record line 34), and, for
     Row 48.20 (ii)'s second half, the half in the record's words *"one shared presentation formatter"* (record lines
     35–36, across a line break);
   - Rows 48.19 and 48.20 (ii)'s first half: *"ADOPTED (3): Row 48.19 and the first half of Row 48.20 (ii) (never
     published on the record), travelling with Row 4.2 (display Ruling 1 part A)"* (record lines 32–33), and, for Row
     48.20, the half named in the record's words *"never published on the record"* (line 32);
   - Row 40.61: *"Row 40.61, on D-522 (its home marked ⚠gap at the index, not opened)"* (record line 33);
   - Row 48.17 (iii): *"Decided against (1): Row 48.17 (iii), in so far as it makes the augmented-sixth sub-type a
     display's re-derivation from the notes; the sub-type is L2's chord kind (the chord-vocabulary Ruling 1), which a
     display renders."* (record lines 40–41).

   **The record's emphasis marks are not carried into the quotations** (its bold on *"ADOPTED (3):"* and *"Decided
   against (1):"*, its italics on *never published on the record*, *⚠gap* and *one shared presentation formatter*), as
   §L.40's table quotes them. **The writing side checked every quotation against its record by a read-only script
   (words and punctuation, line breaks and runs of spaces read as one space, asterisks not compared): each found in its
   record.** Before writing each line, find its quoted passages in the record yourself and compare them the same way:
   every word and every punctuation mark must match, line breaks read as spaces. The line keeps its marks exactly as
   §3.2 gives them. A difference is a STOP-and-report for that line: no line written, listed in the report under *rows
   the act could not place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that claim is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The fit, row by row:
   - Rows 4.6, 4.18, 4.19, 48.35, 40.60 and 7.36, and the parts 48.26 (ii), 48.27 (ii), 48.36 (i), 48.36 (iii),
     22.58 (i), 50.2 (i) and 48.20 (ii)'s second half: a statement of how a display presents published facts (a display
     convention, a presentation constant or formatter, the staff a display writes to, a want of the product's display),
     which the record carries *"for a display's own specification"* (record lines 34–39);
   - Rows 48.19 and 48.20 (ii)'s first half: the display chord symbol and the Nashville number as presentation
     derivations from published facts, never published on the record (record lines 32–33);
   - Row 40.61: *"show me why"* as a late-bound display consumer of facts already published, the row lying in D-522's
     home (record line 33);
   - Row 48.17 (iii): the derivation from the sounding content as a presentation-layer read that carries the
     augmented-sixth distinction (record lines 40–41).

   A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act could not place*
   with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*). The record writes a bare *"ADOPTED"* and names no L3-S number for Rows 48.19, 48.20 (ii) (first half) and
   40.61, so **item (4)** gives the word: the row's proposed word for that part is **UNPLACED**, not an ADOPTED word, so
   the word is read at the row's *Current-text axis* for that part:
   - **Row 48.19:** the axis reads *"L3-S5: **AGREES** — its premise leaves a display that "chooses its own convention,
     as a display act""*, exactly one derived statement named, AGREES: **ADOPTED — carried (L3-S5)**;
   - **Row 48.20 (ii), its first half:** the axis for (ii) reads *"L3-S5: **AGREES** — its premise's display "never
     publishes it back into the analysis""*, exactly one derived statement named, AGREES: **ADOPTED — carried
     (L3-S5)**;
   - **Row 40.61:** the axis reads *"**THE DERIVATION IS SILENT**"*: **ADOPTED — proposed**.
   These are the words Ruling 9 of the release part 2 record states as the writing side's reading (its lines 407–409:
   *"Rows 48.19 and 48.20 (ii) (first half) **ADOPTED — carried (L3-S5)**, Row 40.61 **ADOPTED — proposed**, none as
   proposed"*); read each at the row. The ADOPTED — carried lines write the number after the bold word, `**ADOPTED —
   carried** (L3-S5)`, as most such lines in the file do. The HISTORICAL line takes the record's *"Decided against"*
   (form (b-H)). **The writing side read the proposed paragraph at every row: at the claim or row named, each is
   UNPLACED** (Rows 4.6, 4.18, 4.19, 7.36, 40.60, 40.61, 48.19 and 48.35, which have no claims; and 22.58 (i), 48.17
   (iii), 48.20 (ii), 48.26 (ii), 48.27 (ii), 48.36 (i), 48.36 (iii) and 50.2 (i)). So no line's word is the row's own
   proposed word, and **no line says *as proposed***. If you find a row-part's proposed word for the claim named other
   than UNPLACED, or an axis other than the one given above, that row's lines are a STOP-and-report. No other wording
   (such as *"placed from"*) is added. Every one of the 3 ADOPTED lines is listed in the report under *ADOPTED words read
   at the row*, with the proposed word read (UNPLACED), the axis read, and that its line does not say *as proposed*.
6. **The split rows and their parts.** Row 48.20 (ii) gets two lines from this one record, one per half (§L.40's table:
   *"the row has two lines from this one record, one per half, and form (b)'s two-record rule is not met"*): the ADOPTED
   line on its first half first, then the placement line on its second half. Row 48.36 gets two placement lines, (i)
   then (iii). Rows 48.26, 48.27, 22.58, 50.2 and 48.17 name the claim placed only. The other parts of these rows get
   nothing from this stretch (§3.2's last paragraph).
7. **Rows named by more than one record.** §L.40 says none, and the writing side found no earlier ruled, placement or
   recorded line at any of the 15 rows. Report the heading *rows named by more than one record* as **none**. If you find
   an earlier record's line on a part this stretch writes with a differing word, apply the rule by part as the big
   dispatch gives it; if an earlier stretch's line would have to be deleted or edited, STOP, do not commit, and report.
   **No earlier line is edited in this stretch.**

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written, in the order it goes at its row. The record file in every line
is `cowork_rulings_2026_11_07_l3_display_family_sitting.md`.

*Row 4.6 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 4.18 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 4.19 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 7.36 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 22.58 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (i) Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 40.60 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 40.61 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* **ADOPTED — proposed** — "Row 40.61, on D-522 (its home marked ⚠gap at the index, not opened)".
```

*Row 48.17 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (iii) **HISTORICAL** — "Decided against (1): Row 48.17 (iii), in so far as it makes the augmented-sixth sub-type a display's re-derivation from the notes; the sub-type is L2's chord kind (the chord-vocabulary Ruling 1), which a display renders.".
```

*Row 48.19 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* **ADOPTED — carried** (L3-S5) — "ADOPTED (3): Row 48.19 and the first half of Row 48.20 (ii) (never published on the record), travelling with Row 4.2 (display Ruling 1 part A)".
```

*Row 48.20 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (ii), its first half "never published on the record": **ADOPTED — carried** (L3-S5) — "ADOPTED (3): Row 48.19 and the first half of Row 48.20 (ii) (never published on the record), travelling with Row 4.2 (display Ruling 1 part A)".
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (ii) "one shared presentation formatter" Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 48.26 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (ii) Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 48.27 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (ii) Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 48.35 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 48.36 — 2 lines, in this order:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (i) Outside every charter — carried for a display's own specification; listed in the successor's notes.
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (iii) Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

*Row 50.2 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1).* (i) Outside every charter — carried for a display's own specification; listed in the successor's notes.
```

**The count.** 17 lines on 15 rows: `*RULED PLACEMENT (`: **13**; `*RULED DISPOSITION (`: **4** — 2 **ADOPTED — carried**
(L3-S5), 1 **ADOPTED — proposed**, 1 **HISTORICAL**; all 17 naming the display-family record. None opens `*RECORDED
DISPOSITION (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) the 13 form (c-P) lines are §L.40's
table's lines, character for character; (2) the record's emphasis marks are dropped inside the quotations, as §L.40's
table quotes them (§3.1 item 3); (3) Rows 48.19 and 48.20 (ii)'s first half quote the same passage, the record's
*"ADOPTED (3):"* item up to its semicolon, which names both; Row 40.61 quotes the item's second clause, after that
semicolon, without the *"ADOPTED (3):"* label, as §L.40's table quotes it; (4) Row 48.20 (ii)'s first half is named
*"(ii), its first half "never published on the record":"*, in the shape the file's split lines use (*(ii), its phrase
half:*, *(ii), its part "…":*) with the record's words for the half, as §L.40's table names the second half by the
record's words (*"(ii) "one shared presentation formatter""*); (5) at Row 48.20 the first half's line goes before the
second half's, and at Row 48.36 (i) before (iii), in the order of the parts; (6) the ADOPTED — carried lines write the
number after the bold word (`**ADOPTED — carried** (L3-S5)`), the form most of the file's such lines use (one line, at
Row 7.67, has it inside the bold).

**What this stretch gives no line** (Task 3 (a)):
- **The record names and does not place** Row 4.2 (its §1, the row Rows 48.19 and 48.20 (ii) travel with; placed at
  §L.25) and L2 reading file Row 51.3 (its §2, Row 50.2's L2 twin, not read by the sitting). No line from this record;
  not touched.
- **The other claims and parts of the rows this stretch writes** — Rows 22.58 (ii), 48.17 (i) and (ii), 48.20 (i) and
  (iii), 48.26 (i), 48.27 (i), 48.36 (ii), 50.2 (ii) and (iii) — get nothing from this stretch.
- **The alternatives the record offered and did not take** (Rows 4.6 and 48.35 as QUARANTINED; Row 7.36 with the
  measurement of the analysis; the *"not a sounding part"* half of Row 50.2 (i) RELOCATED to L0): no line.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — nothing written

- **Item 5:** the record places no row-part RELOCATED, so nothing is appended. The writing side searched §10 (lines
  80081–81183) for the fifteen row numbers of §3.2 as a bare number with look-around: **five hits, all on other claims
  or other rows' text:** line 80262 (Row 50.2 (iii)), line 80747 (Row 48.20 (iii)), line 80815 (*"§4.6"*, a section of
  an old document named at Row 57.470 (ii), not Row 4.6), and lines 80989 and 80993 (Rows 48.26 (i), 48.27 (i) and
  48.36 (ii)). None is a part this stretch writes. Run the same search with the Grep tool and report it.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries entries for other claims of four of this stretch's rows and for none of the parts it writes. The
  writing side's search of §11 (lines 81184–83336) for the same fifteen row numbers found **four hits:** line 82112 (Row
  22.58 (ii)), line 83241 (Row 48.17 (ii)), line 83243 (Row 48.20 (i)) and line 83261 (Row 50.2 (ii)) — each a
  QUARANTINED claim this stretch does not write, so no NOT QUARANTINED line is added. Run the same search with the Grep
  tool; if you find an entry for a row-part this stretch writes, add the NOT QUARANTINED line item 7 (b) gives beneath
  it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.40 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.41 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 15 commit, as in sessions 11 to 24.
   Attribute it in the diff table to *"session 25's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.40
   only**, after sessions 10 to 24's §L.1 to §L.39. §L.41 to §L.55 are not applied, read or touched.
3. **A1, for the writing side's handoff entries.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed.
   **Handoff entries 1233 and 1234 ARE landed**, with this file, in §5 act 1, as sessions 8 to 24
   landed theirs. Any other untracked handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the record this stretch enters
   (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The writing
   side's search: **case matched, none; case not matched, one hit of *"decided against"*, record line 40, *"Decided
   against (1)"*, at Row 48.17 (iii)**, as §L.40's *The act's search* says; neither of the other phrases. The hit is the
   part this stretch writes by form (b-H) (§3.2). Report the result. Item 2: not reached. Item 3: not reached. Item 4:
   not reached. Item 5: nothing appended (§3.3). Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **A changed line, not in the big dispatch:** the in-progress line of §3.5 item 3. Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 15 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before §L.40's lines and the in-progress line are all written,
   do not commit; STOP and report which of them were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 15 commit:**
     `git diff b8bd4bddf4d1ac0fa1632ef19d049f76860e30e2 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session25_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the in-progress line of §3.5 item 3; and a NOT QUARANTINED line only if §3.4
     (b) found an entry for a part this stretch writes. Then
     `git diff --numstat b8bd4bddf4d1ac0fa1632ef19d049f76860e30e2 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 35 added lines and 1 deleted line** (the 17 lines and their 17 blank lines, 34; the in-progress
     line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2 that was STOP-and-report**,
     plus 1 added for each NOT QUARANTINED line §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,257 added lines and 4 deleted lines** (`1257` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 24 the file stood at 1,223 added and 4 deleted against the Task 2
     commit (checked by the writing side at the objects: the Task 2 commit's blob `48e24b2f…` against `b8be2e98…`); this
     stretch adds 34 lines. The in-progress line replaces a line that is itself an addition against the Task 2 commit,
     so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **518** (514 + 4, less 1
     for each such line that was STOP-and-report); `\*RULED PLACEMENT \(` must count **23** (10 + 13, the same way);
     `\*RECORDED DISPOSITION \(` must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not
     transferred` must count **1**; `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and
     the record names: `cowork_rulings_2026_11_07_l3_display_family_sitting` **17** (less 1 for each line that was
     STOP-and-report, plus 1 for a NOT QUARANTINED line naming it),
     `cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting` **13** and
     `cowork_rulings_2026_11_03_l3_cadence_type_sitting` **36** (both unchanged).
   - **Then, if every line of §3.2 was written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`50ba22f5ca28336b7744d22be5639086fbce3a43`** — the blob of the writing side's simulated edit (§8 below:
     5,328,147 bytes, 84,696 lines, line feeds only). A different blob with every count above as given means a byte differs somewhere in what was written:
     do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 16 (§L.40): the 17 lines of the display-family row-parts written in the reading file under their ratification, thirteen of them placements outside every charter, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_25_task_3_stretch_16_2026_11_24.md`**, as sessions 2 to 24
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.41, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's files first, in a commit of their own, before any edit to the reading file.** Exactly
   these paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_25_task_3_stretch_16_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_three.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_four.md` (the checking session's
   entry). Run §1 check 2 again immediately before staging. Subject exactly:
   `record: handoff entries 1233 and 1234 and the session 25 instruction of the L3 application landed; Task 3 stretch 16 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: for each row, the row check of
   §3.1 item 4 and the word check of §3.1 item 5, then its lines of §3.2; then the §10 search of §3.3; the §11 search of
   §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_25_task_3_stretch_16_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 25 of the L3 application, Task 3 stretch 16 (§L.40) written; stretch 17 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 17 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 40.60, 40.61, 48.20 and 48.36 and as one sentence
   for the other eleven if they were as stated; the quotation check, each quoted passage stated with its record line;
   the §10 search of §3.3 and the §11 search of §3.4, with their results.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   placed outside every charter* (the thirteen row-parts, each with its line number; not counted in the ruled
   distribution); *recorded lines not written: no disposition word* (none expected); *rows named by more than one
   record* (none expected, §3.1 item 7); *ADOPTED words read at the row* (all 3 ADOPTED lines, each with the proposed
   word read, the axis read and that its line does not say *as proposed*); *audit questions added* (none); *audit
   questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by row* (none: the record
   says no row leaves §10); the decided-against search (§4 item 4), with its result.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph. *A heading of this
   session's report only, as in sessions 10 to 24's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 25 of the L3 application ends here. Stretch 17 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a line of §3.2
  that is STOP-and-report under them or under §3.1 items 2 to 7 is reported and the rest of this stretch applied, as
  they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 7);
- signs of context degradation appear before the commit (§4 item 7);
- §4 item 8's checks find a changed passage they cannot attribute, a count other than the ones they give, or a blob
  other than the one they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

## 8. Provenance

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1232, which first verified session 24's stretch at the
objects (entry 1233 §2 item 1: no finding) and then, under the user's Ruling 1 (d), wrote this file. Read at the objects
for this file, over staged copies: the three git reference files (both refs `75955ee9…`); the commit objects
`75955ee9…`, `b8bd4bdd…`, `efa1bf4d…`, `eb6b94a1…` and `4b6dc3bd…` decompressed and their SHA-1s recomputed; the reading
file's committed blob `b8be2e98…` decompressed and hashed (5,324,496 bytes, 84,662 lines, no carriage return),
byte-identical to the file on disk, its `##` headings (§6 at 435, §7 79623, §10 80081, §11 81184, §12 83337) and line 54;
the Task 2 commit's blob of the reading file, `48e24b2f…`, compared with `b8be2e98…` (1,223 lines added, 4 deleted);
session 24's instruction whole (the pattern of this file); the big dispatch's staged copy (941,330 bytes, blob
`b5274c2c…` recomputed) at lines 159–274 (the forms: form (b) and its paragraph *Which ADOPTED word*, (b-H), (c-P)),
4245–4350 (§L.40 whole) and 4351–4400 (the opening of §L.41, for Ruling 2's judgment only), and its `### §L.` headings
near §L.40; the record whole (6,063 bytes, 80 lines); the release part 2 record at lines 12–49 (Ruling 1) and 363–420
(Ruling 9), and its `##` headings; the list-answers part 3 record at lines 1–60 (Ruling 1, and Ruling 2's opening); the
working list at lines 831–849 ((xxix)) and 971–1000 ((xxxiii)). Each of the 15 rows found exactly once by its heading, inside §6, and read from its
heading to its closing `---` (Rows 40.60, 40.61, 48.19 and 48.20 with their *Current-text axis*; the others at their
proposed paragraphs and claims): its shape (no earlier line at any; Rows 40.60 and 40.61 with *The decisions register at
this row.* after the proposed paragraph), its proposed word for the claim named (UNPLACED at each) and its outgoing
statement, as §3.1 items 2, 4 and 5 state. §10 and §11 searched for the fifteen row numbers as a bare number with
look-around (§10: lines 80262, 80747, 80815, 80989 and 80993, none a part this stretch writes; §11: lines 82112, 83241,
83243 and 83261, other claims). The record searched for the three decided-against phrases, line breaks joined: case
matched none; case not matched, *"Decided against"* once (record line 40). Every quoted passage of §3.2 checked
against the record by a read-only script (line breaks and runs of spaces read as one space, asterisks removed): each
found once, and the placement *"carried for a display's own specification"* once. The 13 form (c-P) lines compared with
the backtick-quoted lines of §L.40's table (dispatch line 4269): five distinct texts, each equal to one of the table's
five. **The edit simulated on a copy of the reading file in the container** by a `python3 -I` script (on the user's
leave), the 17 lines taken from §3.2's code blocks and the in-progress line from §3.5 item 3, each row's lines placed
after the blank line that ends its proposed paragraph: against the committed blob `b8be2e98…`, **35 added lines and 1
deleted** (line 54 replaced; the 17 lines and their blanks inserted at the fifteen rows, Rows 40.60 and 40.61 directly
above *The decisions register at this row.*, the thirteen others before `---`); against the Task 2 commit's blob, 1,257
added and 4 deleted; the counts **518 / 23 / 53 / 26 / 1 / 1**, the record names **17** (display family), **13**
(suggestion tool) and **36** (cadence type), no new line saying *as proposed*, and the blob
**`50ba22f5ca28336b7744d22be5639086fbce3a43`** (5,328,147 bytes, 84,696 lines). Relayed, not re-checked here: the
archive JSON's blob `1df4f207…` and the untracked paths (session 24's report and closing message); the end of
`cowork_handoff.md`'s topmost block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s
dispatch-protocol section (as session 24's instruction gives them, checked there on 2026-11-24); the line ranges of the
big dispatch §2 item 9 names outside those read above (as session 24's instruction gives them, the dispatch
unchanged).*

*Check note: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1233, checking this file as a turn of its own
(Ruling 1 (e)), over staged copies. Read at the objects: the three git reference files (both refs `75955ee9…`); this
file as landed unchecked (48,259 bytes, 559 lines, blob `fa88821c…` recomputed) whole; the record whole (6,063 bytes,
80 lines); the big dispatch (941,330 bytes, 7,157 lines, blob `b5274c2c…` recomputed) at lines 159–274 (the forms) and
4245–4350 (§L.40 whole), its `##` and `### §L.4` headings (the ranges of §2 item 9) and the length of line 98; the release
part 2 record at lines 12–49 (Ruling 1) and 363–420 (Ruling 9, the writing side's reading at lines 407–409); the
list-answers part 3 record whole (Ruling 1 at lines 9–37); the working list at lines 831–849 ((xxix)) and 971–1000
((xxxiii)); the reading file (5,324,496 bytes, 84,662 lines, no carriage return, blob `b8be2e98…` recomputed), its nine
counts of §1 check 4 as given, line 54, its `##` headings as §8 gives them, and the 15 rows, each found once by its
heading inside §6 and read from heading to `---`: shapes as §3.1 item 2 states, no earlier line at any row, the word
UNPLACED at every row or part named, the axes of Rows 48.19, 48.20 (ii) and 40.61 as §3.1 item 5 quotes them; the Task 2
commit's blob `48e24b2f…` decompressed and its SHA-1 recomputed; §10 and §11 searched for the fifteen row numbers as
§3.3 and §3.4 give the search (the same nine hits, none a part this stretch writes); the record searched for the three
decided-against phrases, line breaks joined (case matched none; case not matched, *"Decided against"* once); the
relayed facts of this §8 at their objects (`cowork_handoff.md`'s topmost block ending at line 255, the dispatch-protocol
heading at `cowork_audit_protocol.md` line 180, the archive JSON's blob `1df4f207…` with its carriage returns read as
line feeds, and session 24's report on the untracked paths). Every quoted passage of §3.2 found once in the record
(line breaks and runs of spaces read as one space, asterisks removed); the 13 form (c-P) lines each equal to one of the
five backtick-quoted lines of §L.40's table; the in-progress line equal to line 54 with only §L.39 and §L.40 brought
forward. **Re-simulated** by this sitting's own `python3 -I` script from this file's own text (the 17 lines taken from
§3.2's code blocks, each row's lines after the blank line that ends its proposed paragraph, line 54 replaced): 35 added
and 1 deleted against `b8be2e98…`, 1,257 added and 4 deleted against the Task 2 commit's blob; counts 518 / 23 / 53 /
26 / 1 / 1; record names 17 / 13 / 36; no line saying *as proposed*; **blob
`50ba22f5ca28336b7744d22be5639086fbce3a43`** (5,328,147 bytes, 84,696 lines), as the writing side stated. **No finding:**
no line of §3.2, no count and no expected figure changed. The edits of this check: the status banner; entry 1234
added at §1 check 5, §2 item 4, §4 item 3 and §5 act 1 with its subject; this note. Former wordings not kept, the file
being unreleased.*
