# CC dispatch — the L3 application, SESSION 24 of several: Task 3 of the L3 application dispatch, fifteenth stretch (§L.39), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty.md`, which first verified session 23's
> stretch at the objects (no finding) and then wrote this file in the same sitting, under the user's Ruling 1 (d) of
> 2026-11-24. CHECKED 2026-11-24, as a turn of its own under the user's Ruling 1 (e) of 2026-11-24, by the NEW Cowork
> session booted on `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_one.md`: one
> correction (§3.6's edit neighbourhood), no line of §3.2 changed, the expected blob re-derived (§8, last paragraph).
> Only that session tells the user what to hand over.**
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
called **the Task 2 commit** below). Sessions 10 to 22 applied Task 3's first thirteen stretches, §L.1 to §L.36. Session 23
applied the fourteenth stretch, §L.37 and §L.38, in commit `865a4c24a0394e656e40efd246aab1b858690970` (called **the
stretch 14 commit** below), and committed its report as `eb6b94a172aaa1a87299c2b19639f5395ff24827`, the current tip.

**This is session 24. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry: §L.39, the record of family 1's last
surface, *the chord-suggestion tool and the cadential entries*. It commits that fifteenth stretch as ONE commit, pushes
it, writes its report, and STOPS.** §L.40 is a later session's.

**Why the stretch covers this one entry and stops at §L.40** (the user's Ruling 2 of 2026-11-24: a writing session
judges how many ledger entries fit). §L.39's record (9,543 bytes) places 13 row-parts on 9 rows and brings two kinds of
line this run has rarely written: seven `*RULED PLACEMENT (` lines placing row-parts outside every charter (form (c-P);
the file carries three lines of that label so far, all of another wording), and Row 46.14 split three ways, two of its
parts already carrying §L.6's lines. It also needs one correction of an earlier stretch's line, ruled by the user (§3.6).
The sitting that wrote this file had already carried a full verification of session 23's stretch, and judged that one
entry was the margin it had; the stretch stops at the boundary before §L.40.

**What this stretch writes, in one paragraph.** **13 lines on 9 rows**, all from
`cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md`: **7 opening
`*RULED PLACEMENT (`** (Ruling 1: outside every charter, no disposition word — Rows 38.81 (ii), 38.82's second part,
57.107 (ii)'s predictive half, 57.445 (ii), 57.433 (ii)'s second half, 46.27's composing half, 46.37 whole); and **6
opening `*RULED DISPOSITION (`** (Ruling 2): **4 with the word ADOPTED — proposed** (Row 38.21 (ii), Row 38.82's first
part, Row 57.107 (ii)'s part *"that a future tool may use the catalog"*, Row 46.14's catalog-entries part) and **2 with
the word HISTORICAL by form (b-H)** (Row 46.14's two decided-against parts). **No line says *as proposed*:** every
row-part named is proposed UNPLACED at its row. **One earlier line corrected:** §L.6's Ruling 2 line at Row 46.14 gains
the name of the part it places, its word and quotation unchanged (§3.6). §3.2 gives every line with its exact text.
**Nothing at §10** (§3.3), **nothing at §11** (§3.4), and the in-progress line brought forward from §L.38 to §L.39 (§3.5).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only.** This session copies into the reading file the placements the record already makes; it decides
nothing and changes no algorithm. The record states of each ruling *"Documentation only. Algorithm: no change."* Its
successor amendments (the boundary statement and the notes list, form (a)) are Task 1's, not this stretch's (§L.39,
*Successor*); it orders no charter or interface-contract amendment.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `eb6b94a172aaa1a87299c2b19639f5395ff24827`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_24_task_3_stretch_15_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 14 commit left it.**
   `git diff --quiet 865a4c24a0394e656e40efd246aab1b858690970 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree eb6b94a172aaa1a87299c2b19639f5395ff24827 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `aa5b2803720dea061fdf722ea9b765ceda781b31`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **508**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting` must count
   **17**; `cowork_rulings_2026_11_03_l3_cadence_type_sitting` must count **36**; and
   `cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting` must count **0**. Any other
   result: STOP and report, the file not touched. (The writing side's copy: 5,320,637 bytes, 84,636 lines, line feeds
   only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree eb6b94a172aaa1a87299c2b19639f5395ff24827 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the files §5 act 1 lands (this instruction and handoff entries 1231 and 1232), plus the paths sessions 2 to 23 reported and did not land (387 under `scratch_artifacts/`;
     `Claude outputs/`; `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
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
   the read-first block), and **the handoff entries §5 act 1 lands, whole**: entry 1231 (written by the sitting that
   wrote this file) and entry 1232 (written by the sitting that checked it). Both are untracked; §5 act 1 lands them.
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The record this stretch rests on, WHOLE** — it is the authority for every line this session writes (**the record's
   own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md`
   (§L.39; 9,543 bytes, 130 lines).
8. **Three release records, at these lines only, with the Read tool:**
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`, lines 12–49 (Ruling 1:
     the line for a row-part placed outside every charter) and lines 89–125 (Ruling 3: form (b)'s two-record rule
     applies by part);
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md`, lines 187–243
     (Ruling 5, from its heading: Row 46.14's catalog-entries part, *"ADOPTED — proposed, a line now"*);
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part4_sitting.md`, lines
     71–106 (Ruling 3: Row 38.82's first part and Row 57.107 (ii)'s part, ADOPTED — proposed).

   **Do NOT read the records of §L.1 to §L.38 or of §L.40 to §L.55, and do not open the record's surface** (the lines
   quote the record only). §3.6's correction quotes the earlier line as it stands at the reading file, not its record.
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, its two-record rule by part, form (b-H) and form (c-P)**, the premise ledger, the declared
     start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 827 and 875–881** (§L.6's table line for Row 46.14 and its *Open* point (3) answer: the two parts its
     HISTORICAL lines are for, the ground of §3.6);
   - **lines 4114–4244 (§L.39, your stretch)**;
   - lines 6616–6820 (Task 3, whole, **with (c) items 1 and 5, the decided-against search and the transfer list**);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–826, 828–874 and 882–4113 (§L.1 to §L.38, applied, but for
   the two places of §L.6 above); lines 4245–5906 (§L.40 to §L.55); lines 5907–6615 (Tasks 0 to 2, executed and
   checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the end. Nor the derivation, the successor, `FRAMEWORK.md` or
   `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 9 rows §3.2 names, whole, at §6** (lines 435–79596): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
      heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
    - §10 (lines 80055–81157), searched with the Grep tool for every row number of this stretch (§3.3);
    - §11 (lines 81158–83310), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The forms.**
   - **The 7 lines of Ruling 1 take form (c-P)** (the big dispatch's forms section; Ruling 1 of the release part 2
     record): `*RULED PLACEMENT (<record file>, Ruling 1).* Outside every charter — <the record's placement in its
     words>; listed in the successor's notes.`, naming the part where the ruling places a part only, the part named
     before *Outside every charter*, as §L.39's table gives each line. **No disposition word is written**; the row is
     not counted in the ruled distribution and is listed in the report as placed outside every charter.
   - **The 4 ADOPTED lines take form (b)**, one line ADDED to the row, naming its claim or part.
   - **The 2 HISTORICAL lines of Row 46.14 take form (b-H)**: form (b) with the word **HISTORICAL**, the placement
     quoting the record's sentence that decides against the part, the line naming that part.
   Every line names its record's file and its ruling, the record file written as its bare file name, as sessions 10 to
   23 wrote theirs. The row's `*PROPOSED DISPOSITION.*` paragraph and every other sentence of the row stay untouched,
   but for §3.6's one correction.
2. **Where the line goes.** A ruled line goes *"immediately beneath a row's `*PROPOSED DISPOSITION.*` paragraph"* (the
   big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after any earlier ruled
   or recorded line standing there, and above any paragraph that follows them** (such as *"At the source now."*). Each
   new line is followed by one blank line. Where one row gets several lines, they go in the order §3.2 gives them. Read
   each row's actual shape from its proposed paragraph to its end before writing. **The writing side read all 9 rows at
   its copy of the file (blob `aa5b2803…`).** Their shapes after the proposed paragraph:
   - **no earlier line, and nothing between the proposed paragraph and `---`; the new line goes after the blank line
     that follows the proposed paragraph, before `---`:** Rows 38.81, 38.82 and 46.37;
   - **earlier ruled lines, and nothing after them but `---`; the new lines go after the last earlier line and its
     blank line, before `---`:** Row 38.21 (two lines, both on claim (i), from
     `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md`), Row 46.27 (one line, its analysis half, from
     `cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md`) and Row 46.14 (two lines, from
     `cowork_rulings_2026_11_03_l3_cadence_type_sitting.md`, Rulings 1 and 2; the second is the line §3.6 corrects);
   - **earlier ruled lines, then a paragraph headed *"At the source now."*; the new lines go after the last earlier line
     and its blank line, above *At the source now.*:** Row 57.107 (one line, (ii)'s half *"read forward for the
     analysis"*, from `cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md`; *At the source now.* is followed
     by *The decisions register at this row.*), Row 57.433 (one line, (ii)'s half *"input to recognise"*, from the same
     further-rows record) and Row 57.445 (two lines, claim (i)'s two halves, from
     `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md`). The paragraphs after them are not touched.

   If you find a different shape at a row (an earlier line not listed here, a further paragraph, or an ending other
   than `---`), state it in the report and place the lines by the rule in bold above; if the rule does not settle where
   they go, that row's lines are a STOP-and-report.
3. **The quotation.** Each line quotes the record's words as §3.2 gives them:
   - the seven form (c-P) lines: the placement *"the design of a future chord-suggestion tool, carried for that tool's
     own specification"* (record lines 40–41), and, where a part is named, the part in the record's words from its
     list (record lines 43–50): *"read predictively to suggest"* (line 44), *"read predictively it serves a future
     chord-suggestion tool"* (line 45), *"composition offers it (proposes the substituted form)"* (line 48). **One part
     name is not a verbatim quotation and is not compared as one:** Row 57.433 (ii)'s *"the input to … suggest"*, which
     §L.39's table gives *"shortened from the record's "the input to recognise and suggest" (record line 47)"* — check
     that the record's line 47 carries *"the input to recognise and suggest"* and write the shortened form as §3.2 gives
     it;
   - Row 38.21 (ii): *"38.21 (ii) — ADOPTED — proposed, as that statement"* (record line 74);
   - Row 38.82's first part: *"follows in part: the shared catalog by the statement"* (record line 75);
   - Row 57.107 (ii)'s part: *"split as 38.82: that a future tool may use the catalog, by the statement"* (record line
     76);
   - Row 46.14, each of its three parts: the placement cell of its row of the record's Part B table (lines 83–85),
     whole; the part named by the first cell of the same row (for the inversion clause, in the words §L.6's line at the
     row already uses, *Its "perfect/imperfect by inversion" clause:*, §3.2's settlement (4)).

   **The writing side checked every quotation against its record by a read-only script (words and punctuation, line
   breaks and runs of spaces read as one space, asterisks and table bars not compared): each found in its record.**
   Before writing each line, find its quoted passages in the record yourself and compare them the same way: every word
   and every punctuation mark must match, line breaks read as spaces. The line keeps its marks exactly as §3.2 gives
   them. A difference is a STOP-and-report for that line: no line written, listed in the report under *rows the act
   could not place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that claim is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The fit, row by row:
   - Row 38.81 (ii): knowledge of longer progressions core to a future chord-suggestion tool (the record's line 43);
   - Row 38.82: the catalog a shared asset of the analyzer and the suggester, *"read predictively to suggest"* (lines
     44 and 75);
   - Row 57.107 (ii): the catalog read predictively for a future chord-suggestion tool, and usable by such a tool (lines
     45 and 76);
   - Row 57.445 (ii): the composition direction, reading a span to suggest (line 46);
   - Row 57.433 (ii): the span as the input to suggest (line 47);
   - Row 46.27: composition offering the substituted form (line 48);
   - Row 46.37: every entry usable in both directions, analysis and composition (line 49);
   - Row 38.21 (ii): the catalog built shareable for a chord-suggestion tool (the boundary statement, lines 71–74);
   - Row 46.14: the cadential entries of the catalog, authentic typed perfect/imperfect by inversion, and the list of
     cadence types (lines 83–85).

   A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act could not place*
   with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*). **Row 38.21 (ii):** the record names the word in full (*"38.21 (ii) — ADOPTED — proposed"*, its line
   74), so item (1) of the paragraph gives **ADOPTED — proposed**. **Row 38.82's first part and Row 57.107 (ii)'s part:**
   **ADOPTED — proposed**, without *as proposed*, ruled by Ruling 3 of the list-answers part 4 record (§L.39's *Open*
   point (3)). **Row 46.14's catalog-entries part:** **ADOPTED — proposed**, *"a line now"*, ruled by Ruling 5 of the
   release part 1 record (its line 237). The HISTORICAL lines take the record's *"Decided against"* (form (b-H)). **The
   writing side read the proposed paragraph at every row: at the claim or row named, each is UNPLACED** (Rows 38.21 (ii),
   38.81 (ii), 57.107 (ii), 57.433 (ii), 57.445 (ii), and the rows without claims, 38.82, 46.14, 46.27 and 46.37). So no
   line's word is the row's own proposed word, and **no line says *as proposed***. If you find a row-part's proposed
   word for the claim named other than UNPLACED, that row's lines are a STOP-and-report. No other wording (such as
   *"placed from"*) is added. Every one of the 4 ADOPTED lines is listed in the report under *ADOPTED words read at the
   row*, with the proposed word read (UNPLACED) and that its line does not say *as proposed*.
6. **The split rows and their parts.** Rows 38.82 and 57.107 (ii) get two lines each from this one record, one per part
   (§L.39's table): Ruling 1's line on the predictive part first, then Ruling 2's line on the part the statement
   carries. Row 46.14 gets three, one per part of the record's Part B table. Rows 57.107 (ii) and 57.433 (ii) each name
   claim (ii) and the part; Rows 38.81 (ii), 38.21 (ii) and 57.445 (ii) name claim (ii) only.
7. **Rows named by more than one record** (form (b)'s two-record rule, by part: *"lines on different parts are each
   written"*). List each in the report under *rows named by more than one record*, with what §L.39 says of it:
   - **Row 38.21** — (i) at §L.30 (two lines on claim (i)), (ii) here;
   - **Row 57.107** — (ii)'s forward half at §L.33 (one line), its predictive half and its part on the statement here;
   - **Row 57.433** — (ii)'s *"input to recognise"* half at §L.33 (one line), its *"input to suggest"* half here;
   - **Row 57.445** — (i) at §L.32 (two lines), (ii) here;
   - **Row 46.27** — its analysis half at §L.34 (one line), its composing half here;
   - **Row 46.37** — moved at §L.30 with no line there, placed here;
   - **Row 46.14** — its inversion clause and its list of cadence types decided against at §L.6 (Rulings 1 and 2) and
     here, **HISTORICAL in both, so under form (b) each part gets both records' lines, in ledger order** (§L.39, *Rows
     named by more than one record*); its catalog-entries part here only. §L.6's Ruling 2 line names no part as it
     stands; §3.6 corrects that first, on the user's ruling, so that the by-part rule reads the row as §L.6 placed it.
   No two lines fall on the same part with differing words. The earlier lines are not touched, but for §3.6. If you
   find an earlier record's line on a part this stretch writes with a differing word, apply the rule by part as the big
   dispatch gives it; if an earlier stretch's line other than §3.6's would have to be deleted or edited, STOP, do not
   commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written, in the order it goes at its row. The record file in every line
is `cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md`.

*Row 38.21 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2).* (ii) **ADOPTED — proposed** — "38.21 (ii) — ADOPTED — proposed, as that statement".
```

*Row 38.81 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* (ii) Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
```

*Row 38.82 — 2 lines, in this order:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* "read predictively to suggest" Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2).* Its part on the shared catalog: **ADOPTED — proposed** — "follows in part: the shared catalog by the statement".
```

*Row 46.14 — 3 lines, in this order (after §3.6's correction of the line above them):*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2).* Its "perfect/imperfect by inversion" clause: **HISTORICAL** — "Decided against in so far as the bass-derived inversion is the only criterion".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2).* Its part "The list as the list of cadence types": **HISTORICAL** — "Decided against in so far as it fixes one list as the only one; the list stays a candidate for a declared vocabulary".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2).* Its part "The catalog holds cadential formulas (authentic, half, deceptive, plagal, Phrygian half) as named-progression entries": **ADOPTED — proposed** — "Entries like any other; whether the final catalog holds them waits on the catalog's final content, confirmed at the ratification act of the amended L3 specification".
```

*Row 46.27 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* "composition offers it (proposes the substituted form)" Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
```

*Row 46.37 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
```

*Row 57.107 — 2 lines, in this order:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* (ii) "read predictively it serves a future chord-suggestion tool" Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2).* (ii), its part "that a future tool may use the catalog": **ADOPTED — proposed** — "split as 38.82: that a future tool may use the catalog, by the statement".
```

*Row 57.433 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* (ii) "the input to … suggest" Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
```

*Row 57.445 — 1 line:*
```
*RULED PLACEMENT (cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1).* (ii) Outside every charter — the design of a future chord-suggestion tool, carried for that tool's own specification; listed in the successor's notes.
```

**The count.** 13 lines: `*RULED PLACEMENT (`: **7**; `*RULED DISPOSITION (`: **6** — 4 **ADOPTED — proposed**, 2
**HISTORICAL**; all 13 naming the suggestion-tool record. None opens `*RECORDED DISPOSITION (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) the seven form (c-P) lines are §L.39's
table's lines, character for character; (2) where a row gets lines from both rulings (Rows 38.82 and 57.107), Ruling 1's
line comes first, in the order §L.39's table names them; (3) Row 46.14's three lines go in the order of §L.39's table
(the two decided-against parts, then the catalog-entries part), each quoting its placement cell whole and none its
ground cell, form (b-H) asking for *"the record's sentence that decides against it"*; (4) Row 46.14's parts are named
in the words the row's lines already use or the record's first cells give: the inversion clause as §L.6's line at the
row names it, the other two by the record's first cells, quoted; (5) the parts of Rows 38.82 and 57.107 (ii) carried by
the statement are named in the shapes the rows already carry (*Its part on …:*, *(ii), its part "…":*), the part named
in the record's words; (6) Row 38.21 (ii)'s line quotes the record's item only, the statement it names being written
in the successor by Task 1, not at the row.

**What this stretch gives no line** (Task 3 (a)):
- **The record names and does not place** Row 57.453 (its §2, Part B's ground) and, at its §3, L2 Rows 43.38 (ii),
  43.99, 43.98 and 26.1 (ii), rows of the L2 reading file (§L.39, *L2 sides*). No line from this record; not touched.
- **The other claims and parts of the rows this stretch writes** — Rows 38.21 (i), 38.81 (i), 57.107 (i), 57.107 (ii)'s
  forward half, 57.433 (i), 57.433 (ii)'s *"input to recognise"* half, 57.445 (i), 46.27's analysis half — get nothing
  from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — nothing written

- **Item 5:** the record places no row-part RELOCATED, so nothing is appended. The writing side searched §10 (lines
  80055–81157) for the nine row numbers of §3.2 as a bare number with look-around: **two hits, line 80781, Row 38.21 (i),
  and line 80787, Row 57.445 (i)**, other claims, not parts this stretch writes. Run the same search with the Grep tool
  and report it.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 81158–83310) for
  the same nine row numbers found none. Run the same search with the Grep tool; if you find an entry for a row-part
  this stretch writes, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.39 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.40 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 14 commit, as in sessions 11 to 23.
   Attribute it in the diff table to *"session 24's instruction, §3.5 item 3"*.

### 3.6 One earlier line corrected, on the user's ruling

**The line.** At Row 46.14, the second earlier line (the writing side's copy, line 64715) reads, whole:
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 2).* **HISTORICAL** — "recorded as decided against **in so far as they fix one list as the only one**; their lists remain candidates for declared vocabularies.".
```
**Replace it, in place, by this line, exactly** (the part's name inserted before the word; the word and the quotation
unchanged):
```
*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 2).* Its part "The list as the list of cadence types": **HISTORICAL** — "recorded as decided against **in so far as they fix one list as the only one**; their lists remain candidates for declared vocabularies.".
```
**Why.** The big dispatch places §L.6's Ruling 2 at Row 46.14 on one part only: its table gives the row a HISTORICAL line
*"for the two parts named"* and says *"The rest of the row stays UNPLACED"* (line 827), and its *Open* point (3) answer
says *"each of Row 46.14's two decided-against parts gets a **HISTORICAL** line"* (lines 875–881). As written, the line
names no part and reads as HISTORICAL for the whole row, so under form (b)'s rule by part the catalog-entries part's
ADOPTED line of §3.2 would fall on a part that line covers, with a differing word. **The user ruled, 2026-11-24, in the
sitting that wrote this file (his word "A", on a surface that put this alternative, leaving the line as it is, and
reporting the ADOPTED line as STOP-and-report): the line is corrected to name its part, then this stretch's lines are
written.** The part is named in the words of this stretch's record's Part B table (its line 85), the same words §3.2's
second Row 46.14 line uses, so that both records' lines on that part name it alike. Documentation only; no disposition
moved.

**How.** The same line, character for character, stands at **three** rows of the file: the writing side's Grep of the
whole line as a fixed string matched lines **3386, 3843 and 64715**. **Only the one at Row 46.14 is edited; the other
two are not touched.** Find Row 46.14 by its heading (§2 item 10), read it to its closing `---`, and confirm that
exactly one line inside it equals the line given above (the second of its two earlier lines). Edit that one line with
the Edit tool, giving as its neighbourhood the Ruling 1 line above it and the blank line between them: that pair
matches once in the file. **Do not use the closing `---` below it as the neighbourhood**: the line, its blank line and
`---` match at all three rows. Afterwards confirm with the Grep tool that the old line now matches exactly twice (the two other
rows, unchanged) and the new line exactly once (inside Row 46.14). This is the **only** earlier line this session edits
(§3.1 item 7). Its former wording goes into the report whole, under a heading of its own, *Earlier line corrected*, and
stays recoverable at the stretch 14 commit. If Row 46.14 does not carry exactly one such line, or the Grep counts after
the edit are not as given: STOP before writing anything more at Row 46.14 (undo nothing; report what was done), write the
other rows' lines, and report — Row 46.14's three lines then go under *rows the act could not place*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.39
   only**, after sessions 10 to 23's §L.1 to §L.38. §L.40 to §L.55 are not applied, read or touched.
3. **A1, for the writing side's handoff entries.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed.
   **Handoff entries 1231 and 1232 ARE landed**, with this file, in §5 act 1, as sessions 8 to 23 landed theirs. Any other
   untracked handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the record this stretch enters
   (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The writing
   side's search: **case matched, none; case not matched, two hits of *"decided against"*, record lines 84 and 85, both
   at Row 46.14's parts**, as §L.39's *The act's search* says; neither of the other phrases. Each hit is a part this
   stretch writes by form (b-H) (§3.2). Report the result. Item 2: not reached. Item 3: not reached. Item 4: not
   reached. Item 5: nothing appended (§3.3). Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed lines, not in the big dispatch:** the in-progress line of §3.5 item 3, and **§3.6's corrected line**. Task
   3 (f) admits each for this stretch as a changed passage of its own kind. Their former texts are the two deleted lines
   this stretch's diff against the stretch 14 commit may show.
7. **The standing order not to edit an earlier stretch's line** (session 23's instruction §3.1 item 7, and every
   session's before it) → **lifted for §3.6's one line only**, on the user's ruling stated there.
8. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before §L.39's lines, §3.6's correction and the in-progress
   line are all written, do not commit; STOP and report which of them were applied to the uncommitted copy and that it
   is not landed.
9. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 14 commit:**
     `git diff 865a4c24a0394e656e40efd246aab1b858690970 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session24_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the in-progress line of §3.5 item 3; §3.6's corrected line; and a NOT
     QUARANTINED line only if §3.4 (b) found an entry. Then
     `git diff --numstat 865a4c24a0394e656e40efd246aab1b858690970 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 28 added lines and 2 deleted lines** (the 13 lines and their 13 blank lines, 26; the
     in-progress line and §3.6's line, each a replaced line, one added and one deleted), **less 2 added for each line of
     §3.2 that was STOP-and-report**, plus 1 added for each NOT QUARANTINED line §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,223 added lines and 4 deleted lines** (`1223` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 23 the file stood at 1,197 added and 4 deleted against the Task 2
     commit (session 23's report gives that numstat [relayed: not re-run here]); this stretch adds 26 lines. The
     in-progress line and §3.6's line each replace a line that is itself an addition against the Task 2 commit, so
     they add no line and delete none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **514** (508 + 6, less 1
     for each such line that was STOP-and-report); `\*RULED PLACEMENT \(` must count **10** (3 + 7, the same way);
     `\*RECORDED DISPOSITION \(` must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not
     transferred` must count **1**; `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and
     the record names: `cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting` **13**
     (less 1 for each line that was STOP-and-report, plus 1 for a NOT QUARANTINED line naming it),
     `cowork_rulings_2026_11_03_l3_cadence_type_sitting` **36** and
     `cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting` **17** (both unchanged).
   - **Then, if every line of §3.2 and §3.6's correction were written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`b8be2e98cbcb40e993f439c1cb3465b8d8f11e50`** — the blob of the writing side's simulated edit (§8 below: 5,324,496
     bytes, 84,662 lines, line feeds only). A different blob with every count above as given means a byte differs
     somewhere in what was written: do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 15 (§L.39): the 13 lines of the suggestion-tool and cadential-entries row-parts written in the reading file under their ratification, seven of them placements outside every charter, §L.6's line at Row 46.14 given its part on the user's ruling, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
10. **E3** is checked for this stretch only, as items 2 to 9 restrict it. The full E3 belongs to the session of the last
    stretch, or to a check session after it.
11. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_24_task_3_stretch_15_2026_11_24.md`**, as sessions 2 to 23
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
12. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.40, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's files first, in a commit of their own, before any edit to the reading file.** Exactly
   these paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_24_task_3_stretch_15_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_one.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_two.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1231 and 1232 and the session 24 instruction of the L3 application landed; Task 3 stretch 15 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: §3.6's correction first (its
   check, then the edit); then for each row, the row check of §3.1 item 4 and the word check of §3.1 item 5, then its
   lines of §3.2; then the §10 search of §3.3; the §11 search of §3.4; §3.5 item 3; then §4 item 9's checks, the commit
   and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_24_task_3_stretch_15_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 24 of the L3 application, Task 3 stretch 15 (§L.39) written; stretch 16 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. **Earlier line corrected:** §3.6's line, its former wording whole, its new wording whole, the line number, and that
   it matched exactly once at Row 46.14.
4. The 13 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 46.14, 57.107 and 57.445 and as one sentence for
   the other six if they were as stated; the quotation check, each quoted passage stated, Row 57.433 (ii)'s shortened
   part name stated with the record's line 47; the §10 search of §3.3 and the §11 search of §3.4, with their results.
5. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   placed outside every charter* (the seven row-parts of Ruling 1, each with its line number; not counted in the ruled
   distribution); *recorded lines not written: no disposition word* (none expected); *rows named by more than one
   record* (the seven rows of §3.1 item 7, each with what §L.39 says of it); *ADOPTED words read at the row* (all 4
   ADOPTED lines, each with the proposed word read and that its line does not say *as proposed*); *audit questions
   added* (none); *audit questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by
   row* (none: the record says no row leaves §10); the decided-against search (§4 item 4), with its result.
6. The diff table of §4 item 9, every changed passage attributed, the counts, the two `--numstat` results and the blob.
7. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph. *A heading of this
   session's report only, as in sessions 10 to 23's.*
8. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
9. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
10. The last sentence, exactly: *"Session 24 of the L3 application ends here. Stretch 16 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a line of §3.2
  that is STOP-and-report under them or under §3.1 items 2 to 7 is reported and the rest of this stretch applied, as
  they say);
- §3.6's line is not found exactly once at Row 46.14 (Row 46.14 left untouched, the rest applied, as §3.6 says);
- a line an earlier stretch wrote, other than §3.6's, would have to be deleted or edited (§3.1 item 7);
- signs of context degradation appear before the commit (§4 item 8);
- §4 item 9's checks find a changed passage they cannot attribute, a count other than the ones they give, or a blob
  other than the one they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

## 8. Provenance

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1230, which first verified session 23's stretch at the
objects (entry 1231 §2 item 1: no finding) and then, under the user's Ruling 1 (d), wrote this file. Read at the objects
for this file, over staged copies: the three git reference files (both refs `eb6b94a1…`); the commit objects
`eb6b94a1…`, `865a4c24…`, `0f6624c2…` and `8beb212a…` decompressed and their SHA-1s recomputed; the reading file's
committed blob `aa5b2803…` decompressed and hashed (5,320,637 bytes, 84,636 lines, no carriage return), byte-identical
to the file on disk, its `##` headings (§6 at 435, §7 79597, §10 80055, §11 81158, §12 83311) and line 54 in full;
session 23's instruction whole (the pattern of this file); the big dispatch's staged copy (941,330 bytes, blob
`b5274c2c…` recomputed) at lines 159–274 (the forms, (c-P) among them), 827, 870–890 (§L.6's Row 46.14 line and its
*Open* point (3)) and 4114–4244 (§L.39 whole), and its `### §L.` headings; the record whole (9,543 bytes, 130 lines);
the release part 1 record at lines 186–245 (Ruling 5); the release part 2 record at lines 12–49 (Ruling 1) and its `##`
headings; the list-answers part 4 record at its `##` headings and the lines naming Rows 38.82 and 57.107 (Ruling 3,
lines 71–106). Each of the 9 rows found exactly once by its heading, inside §6, and read from its heading to its
closing `---` (Rows 57.107, 57.433 and 57.445 to their *At the source now.* paragraphs): its shape, its earlier lines,
its proposed word for the claim named (UNPLACED at each) and its outgoing statement, as §3.1 items 2, 4 and 5 state.
§10 and §11 searched for the nine row numbers as a bare number with look-around (§10: lines 80781 and 80787, Rows 38.21
(i) and 57.445 (i), other claims; §11: none). The record searched for the three decided-against phrases, line breaks
joined: case matched none; case not matched, *"decided against"* twice (record lines 84 and 85). Every quoted passage of
§3.2 checked against the record by a read-only script (line breaks and runs of spaces read as one space, asterisks and
table bars removed): each found, *"read predictively to suggest"* twice (record lines 44 and 75), each other once; the
shortened *"the input to … suggest"* checked as *"the input to recognise and suggest"*, found once (line 47). §3.6's line
found by its whole text at three rows (lines 3386, 3843, 64715), the third inside Row 46.14. **The user's ruling for
§3.6, his word "A",** given in this sitting on a surface put in its own message, the alternatives B (leave the line,
write the ADOPTED line anyway) and C (the ADOPTED line STOP-and-report) with A recommended. **The edit simulated on a copy
of the reading file in the container** by a `python3 -I` script (on the user's leave), the 13 lines taken from §3.2's
code blocks, §3.6's two lines from its code blocks and the in-progress line from §3.5 item 3, each row's lines placed
after the blank line that ends its proposed paragraph or its earlier ruled lines: against the committed blob, **28
added lines and 2 deleted** (line 54 and line 64715 replaced; the 13 lines and their blanks inserted at the nine rows,
Rows 57.107, 57.433 and 57.445 directly above *At the source now.*, the six others before `---`), the counts **514 / 10
/ 53 / 26 / 1 / 1**, the record names **13** (suggestion tool), **36** (cadence type) and **17** (pairwise grammar),
the old §3.6 line left at two rows and the new one at one, no new line saying *as proposed*, and the blob
**`b8be2e98cbcb40e993f439c1cb3465b8d8f11e50`** (5,324,496 bytes, 84,662 lines). Relayed, not re-checked here: the archive
JSON's blob `1df4f207…` and the untracked paths (session 23's report); the Task 2 commit `4b6dc3bd…` and the 1,197 added
and 4 deleted lines against it after session 23 (session 23's report); the end of `cowork_handoff.md`'s topmost block at
line 255 and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 23's instruction
gives them); the line ranges of the big dispatch §2 item 9 names outside those read above (as session 23's instruction
gives them, the dispatch unchanged).*

*Checked 2026-11-24 (Stockholm), as a turn of its own, by the NEW Cowork session booted on entry 1231 (Ruling 1 (e)),
over staged copies. **Read at the objects:** the three git reference files (both refs still `eb6b94a1…`); the blobs of
the big dispatch (`b5274c2c…`), the reading file (`aa5b2803…`, 5,320,637 bytes, 84,636 lines, no carriage return), the
record (9,543 bytes, 130 lines) and the archive JSON (`1df4f207…` once its carriage returns are read as line feeds),
each recomputed; the record whole; the big dispatch at the forms (lines 159–274), lines 827 and 875–881, §L.39 whole
(lines 4114–4244), its `##` and `### §L.` headings and lines 37–38, 58–59, 97–98 and 430–431; the release part 2 record
at Rulings 1 and 3 (lines 12–49 and 89–125, their headings at 12, 50, 89 and 126); the release part 1 record at Ruling
5 (lines 187–245, *"ADOPTED — proposed, a line now"* at line 237); the list-answers part 4 record at Ruling 3 (lines
71–106); the reading file's `##` headings, line 54 and the 9 rows, each found once by its heading inside §6 and read
whole: shapes, earlier lines and UNPLACED at every claim or part named, as §3.1 items 2 and 5 state, and each outgoing
statement fitting as §3.1 item 4 states. Every quotation of §3.2 found in the record (*"read predictively to suggest"*
twice, every other once; *"the input to recognise and suggest"* once, line 47); the seven form (c-P) lines equal to
§L.39's table's lines (six distinct texts, Rows 38.81 and 57.445 sharing one); the §10 search (lines 80781 and 80787
only) and the §11 search (none); the decided-against search (case matched none; case not matched, *"decided
against"* at lines 84 and 85 only; nothing across a line break). **Relayed facts now checked at their objects:** the end
of `cowork_handoff.md`'s topmost block at line 255; `cowork_audit_protocol.md`'s section heading at line 180; session
23's report giving `1197	4` against the Task 2 commit (its line 213) and 387 untracked paths under `scratch_artifacts/`
(its line 29). **The edit re-simulated** by a `python3 -I` script of this session's own (on the user's leave), the 13
lines taken from §3.2's code blocks, §3.6's two lines from its code blocks and the in-progress line from §3.5 item 3,
each row's lines placed before the first `---` or *At the source now.* after its heading: 28 added and 2 deleted; counts
514 / 10 / 53 / 26 / 1 / 1; record names 13 / 36 / 17; the old §3.6 line left at two rows (3386, 3843), the new at one
(64723 after the edit); no new line saying *as proposed*; **blob `b8be2e98cbcb40e993f439c1cb3465b8d8f11e50`** (5,324,496
bytes, 84,662 lines), as stated. **Corrected, no line of §3.2 and no expected figure changed:** §3.6's *How*, which
offered *"the Ruling 1 line above it, or the closing `---` below it"* as the edit's neighbourhood: the line followed by
its blank line and `---` matches at all three rows (lines 3386, 3843 and 64715), so only the Ruling 1 line above it
gives a unique match (that pair matches once); the *or* alternative is struck and a warning added. Added: entry 1232 to
§1 check 5, §2 item 4, §4 item 3 and §5 act 1 with its subject; the status banner. Former wordings not kept, as this
file is unreleased.*
