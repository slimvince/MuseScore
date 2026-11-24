# CC dispatch — the L3 application, SESSION 23 of several: Task 3 of the L3 application dispatch, fourteenth stretch (§L.37 and §L.38), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_eight.md`, a writing session that did
> not verify a stretch: the sitting booted on entry 1227 verified session 22's stretch and, on the user's word "hand
> over", handed the writing of §L.37 on to a new session. CHECKED 2026-11-24, as a turn of its own under the user's
> Ruling 1 (e) of 2026-11-24, by the NEW Cowork session booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_nine.md`: three corrections, no line
> of §3.2 changed, the expected blob re-derived (§8, last paragraph). Only that session tells the user what to hand
> over.**
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
called **the Task 2 commit** below). Sessions 10 to 21 applied Task 3's first twelve stretches, §L.1 to §L.35. Session 22
applied the thirteenth stretch, §L.36, in commit `2c21e606b3864f2f681b46f8d3fc3185f2973b37` (called **the stretch 13
commit** below), and committed its report as `8beb212a03499965cef2e57c725c075c99193f2f`, the current tip.

**This is session 23. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for TWO ledger entries: §L.37, the record of family 1's
idiom-tags surface, part 2, and §L.38, the record of family 1's surface *the catalog and the pairwise grammar*. It
commits that fourteenth stretch as ONE commit, pushes it, writes its report, and STOPS.** §L.39 is a later session's.

**Why the stretch covers these two entries and stops at §L.39** (the user's Ruling 2 of 2026-11-24: a writing session
judges how many ledger entries fit). §L.37's record (6,479 bytes) places 21 row-parts and gives none of them a line now:
each takes *"no line now"* under Ruling 5 of the release part 1 record, so §L.37 adds no line to the reading file and
only lists its rows in the report. §L.38's record (8,180 bytes) places 15 row-parts on 11 rows in 17 lines, each in a
form this run has written before (Row 24.6's added quotations on the shape of session 22's Row 38.22 (ii) selection
line, §3.2's settlement (6)); it adds nothing to §10 or §11. §L.39's record (9,543 bytes) brings a further
kind: seven row-parts given *"the line"* a release ruling orders, and Row 46.14 split three ways. The sitting that wrote
this file judged that adding a third record would leave too little margin to write it and re-run the simulation
cleanly, and the stretch stops at the boundary before §L.39.

**What this stretch writes, in one paragraph.** **17 lines, all opening `*RULED DISPOSITION (`, on 11 rows**, all from
`cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md`, Ruling 1 (the record's one ruling): **7 with the
word ADOPTED — proposed** (the five rows of the record's *§3.1, follow wholly (5)* bullet, and one part each of Rows
57.494 (i) and 57.396 (ii)); and **10 with the word HISTORICAL** (the five rows of the record's *§3.3* bullet, one part
each of Rows 57.494 (i), 24.4, 57.396 (ii) and 38.79 (ii), and Row 24.6 whole). **No line says *as proposed*:** every
row-part named is proposed UNPLACED at its row. §3.2 gives every line with its exact text. **Nothing at §10** (§3.3),
**nothing at §11** (§3.4), and the in-progress line brought forward from §L.36 to §L.38 (§3.5). **§L.37 gives no line
at any row**: its 21 row-parts are listed in the report under *rows given no line now*, and so are the following and
waiting parts of Rows 24.4 and 38.79 (ii) from §L.38 (§3.2's last paragraph).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only.** This session copies into the reading file the placements the records already make; it decides
nothing and changes no algorithm. Each record states *"Documentation only. Algorithm: no change."* Neither orders an
amendment of the successor, the charter or the interface contract that belongs to Task 3 (§L.37 and §L.38, *Successor*,
*Charter*, *Interface contract*).

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `8beb212a03499965cef2e57c725c075c99193f2f`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_23_task_3_stretch_14_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 13 commit left it.**
   `git diff --quiet 2c21e606b3864f2f681b46f8d3fc3185f2973b37 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 8beb212a03499965cef2e57c725c075c99193f2f -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `720b5073cd129493bd196112acb20ce3e9c277a2`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **491**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting` must count
   **28**; `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting` must count **7**;
   `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting` must count **0**; and
   `cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting` must count **0**. Any other result: STOP and report,
   the file not touched. (The writing side's staged copy: 5,314,921 bytes, 84,602 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 8beb212a03499965cef2e57c725c075c99193f2f -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the files §5 act 1 lands (this instruction and handoff entries 1228, 1229 and 1230), plus
     the paths sessions 2 to 22 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
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
   the read-first block), and **the handoff entries this file names, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_nine.md` (written by the sitting
   that wrote this file) and `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty.md`
   (written by the sitting that checked it). Both are untracked; §5 act 1 lands them.
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The two records this stretch rests on, WHOLE** — they are the authority for every line this session writes and
   every row it lists (**the record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md` (§L.37; 6,479 bytes, 87
     lines);
   - `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md` (§L.38; 8,180 bytes, 100
     lines).
8. **Two release records, at these lines only, with the Read tool:**
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md`, lines 137–177 (Ruling 4,
   from its heading: Row 24.6 whole HISTORICAL) and lines 187–243 (Ruling 5, from its heading: the rows that take *"no
   line now"*); and
   `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part4_sitting.md`, lines 9–70
   (Rulings 1 and 2: the ADOPTED — proposed parts of Rows 57.494 (i) and 57.396 (ii)).

   **Do NOT read the records of §L.1 to §L.36 or of §L.39 to §L.55, and do not open either record's surface** (the
   lines quote the records only).
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, its two-record rule by part, and form (b-H)**, the premise ledger, the declared start state,
     the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 3888–4113 (§L.37 and §L.38, your stretch)**;
   - lines 6616–6820 (Task 3, whole, **with (c) items 1 and 5, the decided-against search and the transfer list**);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3887 (§L.1 to §L.36, applied); lines 4114–5906 (§L.39 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 11 rows §3.2 names, whole, at §6** (lines 435–79562): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
      heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
    - §10 (lines 80021–81123), searched with the Grep tool for every row number of this stretch (§3.3);
    - §11 (lines 81124–83276), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch, one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*` paragraph
   and every other sentence of the row untouched. Every line names its record's file and Ruling 1 (the record has one
   ruling), the record file written as its bare file name, as sessions 10 to 22 wrote theirs. Where §3.2 names a
   claim, the line names it (form (b)'s split-row rule). Where the record places several parts of one row-part, **each
   part placed gets exactly one line**, naming its part as §3.2 gives it; a part given no line is named in §3.2's last
   paragraph. **None of the 17 lines is form (b-H)**: the record writes its HISTORICAL placements in its own words
   (*"HISTORICAL — a superseded plan"*, *"HISTORICAL"*), not as *"decided against"* (§L.38, *The act's search*); they
   take form (b) with the word HISTORICAL, as §L.38's table gives them.
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"At the
   source now."*). Each new line is followed by one blank line. Where one row gets several lines, they go in the order
   §3.2 gives them. Read each row's actual shape from its proposed paragraph to its end before writing. **The writing
   side read all 11 rows at the staged copy; every one ends with a blank line and then `---`.** Their shapes after the
   proposed paragraph:
   - **no earlier line, and nothing between the proposed paragraph and `---`; the new line goes after the blank line
     that follows the proposed paragraph, before `---`:** Rows 24.4 and 24.6;
   - **no earlier line, and a paragraph headed *"At the source now."* directly after the proposed paragraph; the new
     lines go directly beneath the proposed paragraph, above it:** Rows 57.396, 57.398, 57.405, 57.451, 57.493, 57.494,
     57.495 and 57.496. At Row 57.398 *At the source now.* is followed by a paragraph headed *The decisions register at
     this row.*; at Row 57.496 it is followed by the group's sections (*The arithmetic at this group* and the rest)
     before its closing `---`. They are not touched;
   - **earlier ruled lines, and nothing after them but `---`; the new line goes after the last earlier line and its
     blank line, before `---`:** Row 38.79 (three lines, on claim (i): one from
     `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md` and two from
     `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md`, the last two written by session 22).

   If you find a different shape at a row (an earlier line not listed here, a further paragraph, or an ending other
   than `---`), state it in the report and place the lines by the rule in bold above; if the rule does not settle where
   they go, that row's lines are a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it:
   - for the five §3.1 rows, the lead of the record's *§3.1, follow wholly (5)* bullet (its lines 33–34, from *"§3.1"*
     to *"counted pair table"*), its bold marks and the italic marks around *"the grammar"* dropped, then, as §L.38's
     table orders (*"each row with the record's gloss in brackets"*), the row's own item of the bullet with its gloss,
     from the row number to the closing parenthesis of the gloss. Rows 57.398 (i) and 57.495 (i) share one gloss in the
     record, so both quote *"57.398 (i), 57.495 (i) (the catalog and the grammar not derived from each other)"*;
   - for the five §3.3 rows, the record's *§3.3* bullet whole (its lines 39–40), its bold lead's marks dropped and its
     closing period dropped (the line's own period follows the closing quotation mark), as session 22 wrote its §3.1
     bullet;
   - for Row 57.494 (i), the record's *§3.2* bullet's one item whole (its lines 37–38), from the row number to the
     bullet's end, its closing period dropped, the italic marks around the quoted sentence dropped;
   - for Rows 24.4, 24.6, 57.396 (ii) and 38.79 (ii), **the row's own item of the record's *§3.4* bullet** (its lines
     41–46), from the row number to the item's closing parenthesis; the semicolon or period after it dropped, the italic
     marks inside it dropped;
   - Row 24.6's line adds, after its item, the words of Ruling 4 of the release part 1 record that make the rest of the
     row HISTORICAL (that record's lines 159–161): *"a requirement the rulings have met, read as a status"* and *"the
     whole of Row 24.6 is HISTORICAL"*.

   **The writing side checked every quotation against its record by a read-only script (words and punctuation, line
   breaks and runs of spaces read as one space, asterisks not compared): each quoted passage found in its record.**
   Before writing each line, find its quoted passages in the record yourself and compare them the same way: every word
   and every punctuation mark must match, line breaks read as spaces. The line keeps its marks exactly as §3.2 gives
   them. A difference is a STOP-and-report for that line: no line written, listed in the report under *rows the act
   could not place* with both texts. Where the record quotes inside an item (*"but a new entry must PASS the
   consistency test"*, *"not to be settled by drift"*, *"licensed root motion"*, *"composed from"*, *"the grammar"*), the
   line keeps the inner straight double quotation marks and drops the asterisks, as sessions 10 to 22 did.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that claim is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The fit, row by row:
   - Rows 57.398 (i) and 57.495 (i): the catalog and the grammar not derived from each other (the record's gloss);
   - Row 57.451: a change to the catalog changes the catalog only (the record's *"a catalog change changes the catalog
     only"*);
   - Row 57.493 (i): a change of the grammar never needs an edit of the catalog (the record's *"a grammar change needs
     no catalog edit"*);
   - Row 57.496: a licensed pair in no catalog entry is not a gap of the catalog (the record's *"a licensed pair in no
     entry is no gap of the catalog"*);
   - Rows 57.398 (ii), 57.405, 57.493 (ii), 57.494 (ii) and 57.495 (ii): the consistency test coupling the catalog to the
     grammar, or what follows from its failing (the record's *"the consistency test"*);
   - Row 57.494 (i): a change of the catalog never needs an edit of the grammar, but a new entry must pass the
     consistency test (the record's two parts, *"a catalog change needs no edit of the grammar"* and *"but a new entry
     must PASS the consistency test"*);
   - Row 24.4: the decision whether the pairwise grammar folds into the vocabulary owed, its trigger the consumer's build
     (the record's *"the build-timing half"*);
   - Row 24.6: the choice between one store and two not to be settled by drift, made when the consumer is built (the
     record's *"not to be settled by drift"* and *"the timing half"*);
   - Row 57.396 (ii): the catalog never defines or re-implements the licensed root motion (the record's *"the catalog
     defines none of L2's chord-pair knowledge"* and *"the "licensed root motion" it names"*);
   - Row 38.79 (ii): full progressions composed from the catalog by the pairwise functional grammar (the record's *"the
     yes/no grammar"* and *"composed from"*).

   A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act could not place*
   with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.38's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **The record names the
   word in full** for the five §3.1 rows (*"§3.1, follow wholly (5): ADOPTED — proposed"*, its line 33), so item (1) of
   the paragraph gives **ADOPTED — proposed**. For the parts of Rows 57.494 (i) and 57.396 (ii) that follow, the word
   **ADOPTED — proposed**, without *as proposed*, is ruled by Rulings 1 and 2 of the list-answers part 4 record (its
   lines 27–30 and 60–64), as §L.38's table gives it. The HISTORICAL lines take the record's word. **The writing side
   read the proposed paragraph at every row this stretch names: at the claim or row named, each is UNPLACED** (Rows
   57.398 (i) and (ii), 57.493 (i) and (ii), 57.494 (i) and (ii), 57.495 (i) and (ii), 57.396 (ii) and 38.79 (ii), and
   the rows without claims, 57.405, 57.451, 57.496, 24.4 and 24.6). So no line's word is the row's own proposed word,
   and **no line says *as proposed***: the paragraph's *"Otherwise as proposed is not written, and the placement is given
   in the record's words"*. If you find a row-part's proposed word for the claim named other than UNPLACED, that row's
   lines are a STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of the 7 ADOPTED lines is
   listed in the report under *ADOPTED words read at the row*, with the proposed word read (UNPLACED) and that its line
   does not say *as proposed*.
6. **The split rows and their parts.** The record splits four row-parts by subject (its §3.2 and §3.4); each part placed
   gets one line, named in §3.2:
   - **Row 57.494 (i):** the consistency test (HISTORICAL) and a catalog change needing no edit of the grammar (ADOPTED —
     proposed). Claim (ii) of the row gets its own line from the §3.3 bullet.
   - **Row 24.4:** the build-timing half (HISTORICAL). The rest, *"the owed decision made: two stores, the pair table
     L2's, the catalog the reference L3 reads; whether L2 also draws on the catalog waits on DP-O's catalog term"*, gets
     no line now (Ruling 5 of the release part 1 record; §3.2's last paragraph).
   - **Row 24.6:** the whole row, HISTORICAL, in one line (Ruling 4 of the release part 1 record: *"the whole of Row
     24.6 is HISTORICAL"*; §L.38's table: *"One line for the row"*).
   - **Row 57.396 (ii):** the *"licensed root motion"* it names (HISTORICAL) and the catalog defining none of L2's
     chord-pair knowledge (ADOPTED — proposed). Claim (i) of the row is not this record's and gets nothing.
   - **Row 38.79 (ii):** the yes/no grammar (HISTORICAL). The rest, *"read for the analysis: the whole progression is
     L2's decision, weighed link by link; "composed from" the catalog in L2 waits on DP-O's catalog term"*, gets no line
     now (Ruling 5 of the release part 1 record; §3.2's last paragraph).
7. **Rows named by more than one record** (form (b)'s two-record rule, by part: *"lines on different parts are each
   written"*). **One row this stretch writes carries earlier records' lines, each on another claim:** Row 38.79, whose
   three lines (from the lead-rows record, §L.30, and the idiom-tags part 1 record, §L.36) all place parts of claim (i);
   this stretch writes claim (ii). So no two lines fall on the same part, and every line of §3.2 is written. The earlier
   lines are not touched. **Row 57.396 (ii)** was moved to this record at §L.33, which gave it no line (the writing side
   found no `*RULED ` or `*RECORDED ` line at Row 57.396). List both in the report under *rows named by more than one
   record*, each with what §L.38 says of it. If you find an earlier record's line on a part this stretch writes, apply
   the rule by part as the big dispatch gives it; if an earlier stretch's line would have to be deleted or edited, STOP,
   do not commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written, in the order it goes at its row.

**§L.37 — the idiom-tags part 2 record (`cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md`): no line.**
Its 21 row-parts are listed in the report (this section's last paragraph).

**§L.38 — the pairwise-grammar record (`cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md`): 17 lines.**

*Row 57.396 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii), its part on the "licensed root motion" it names: **HISTORICAL** — "57.396 (ii) (the catalog defines none of L2's chord-pair knowledge; the "licensed root motion" it names HISTORICAL by L2 Ruling 1)".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii), its part on the catalog defining none of L2's chord-pair knowledge: **ADOPTED — proposed** — "57.396 (ii) (the catalog defines none of L2's chord-pair knowledge; the "licensed root motion" it names HISTORICAL by L2 Ruling 1)".
```

*Row 57.398 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (i) **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed, as rules about the catalog L3 reads, "the grammar" read as L2's counted pair table"; "57.398 (i), 57.495 (i) (the catalog and the grammar not derived from each other)".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "§3.3, HISTORICAL — a superseded plan (5), the consistency test: 57.398 (ii), 57.405, 57.493 (ii), 57.494 (ii), 57.495 (ii). Ground: L2 Ruling 1; L2 holds no yes/no licensed set for an entry's pairs to be tested against".
```

*Row 57.405 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* **HISTORICAL** — "§3.3, HISTORICAL — a superseded plan (5), the consistency test: 57.398 (ii), 57.405, 57.493 (ii), 57.494 (ii), 57.495 (ii). Ground: L2 Ruling 1; L2 holds no yes/no licensed set for an entry's pairs to be tested against".
```

*Row 57.451 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed, as rules about the catalog L3 reads, "the grammar" read as L2's counted pair table"; "57.451 (a catalog change changes the catalog only)".
```

*Row 57.493 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (i) **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed, as rules about the catalog L3 reads, "the grammar" read as L2's counted pair table"; "57.493 (i) (a grammar change needs no catalog edit)".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "§3.3, HISTORICAL — a superseded plan (5), the consistency test: 57.398 (ii), 57.405, 57.493 (ii), 57.494 (ii), 57.495 (ii). Ground: L2 Ruling 1; L2 holds no yes/no licensed set for an entry's pairs to be tested against".
```

*Row 57.494 — 3 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (i), its part on the consistency test: **HISTORICAL** — "57.494 (i) — a catalog change needs no edit of the grammar, follows; "but a new entry must PASS the consistency test", HISTORICAL — a superseded plan".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (i), its part on a catalog change needing no edit of the grammar: **ADOPTED — proposed** — "57.494 (i) — a catalog change needs no edit of the grammar, follows; "but a new entry must PASS the consistency test", HISTORICAL — a superseded plan".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "§3.3, HISTORICAL — a superseded plan (5), the consistency test: 57.398 (ii), 57.405, 57.493 (ii), 57.494 (ii), 57.495 (ii). Ground: L2 Ruling 1; L2 holds no yes/no licensed set for an entry's pairs to be tested against".
```

*Row 57.495 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (i) **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed, as rules about the catalog L3 reads, "the grammar" read as L2's counted pair table"; "57.398 (i), 57.495 (i) (the catalog and the grammar not derived from each other)".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "§3.3, HISTORICAL — a superseded plan (5), the consistency test: 57.398 (ii), 57.405, 57.493 (ii), 57.494 (ii), 57.495 (ii). Ground: L2 Ruling 1; L2 holds no yes/no licensed set for an entry's pairs to be tested against".
```

*Row 57.496 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed, as rules about the catalog L3 reads, "the grammar" read as L2's counted pair table"; "57.496 (a licensed pair in no entry is no gap of the catalog)".
```

*Row 24.4 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* Its part on the build-timing half: **HISTORICAL** — "24.4 (the owed decision made: two stores, the pair table L2's, the catalog the reference L3 reads; whether L2 also draws on the catalog waits on DP-O's catalog term; the build-timing half HISTORICAL)".
```

*Row 24.6 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* **HISTORICAL** — "24.6 ("not to be settled by drift" met; the timing half HISTORICAL)"; the rest, "a requirement the rulings have met, read as a status", so that "the whole of Row 24.6 is HISTORICAL".
```

*Row 38.79 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md, Ruling 1).* (ii), its part on the yes/no grammar: **HISTORICAL** — "38.79 (ii) (read for the analysis: the whole progression is L2's decision, weighed link by link; "composed from" the catalog in L2 waits on DP-O's catalog term; the yes/no grammar HISTORICAL)".
```

**The count.** `*RULED DISPOSITION (`: **17** — 7 **ADOPTED — proposed**, 10 **HISTORICAL**; all 17 naming the
pairwise-grammar record. None opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) the five §3.1 lines quote the bullet's
lead and then the row's item with its gloss, as §L.38's table orders, the two quotations separated by `; `, the record's
italic marks around *the grammar* dropped and its inner straight quotation marks kept; (2) the five §3.3 lines quote the
§3.3 bullet whole, its bold lead's marks and its closing period dropped, as session 22 did with its §3.1 bullet; (3)
every §3.2 and §3.4 line quotes the row's own item, from the row number to the item's closing parenthesis (or, for Row
57.494 (i), to the bullet's end), as session 22 quoted the rows' own items; (4) where a row gets a HISTORICAL and an
ADOPTED line for parts of one claim (Rows 57.494 (i) and 57.396 (ii)), the HISTORICAL line comes first, in the order
§L.38's table names the parts; both lines quote the same item, as session 22's split rows did; (5) the parts are named in
the shapes the rows already carry, *(i), its part on …:* and *Its part on …:*, the part named in the record's words; (6)
Row 24.6's line adds, after its item, Ruling 4's two quotations for the rest of the row, without naming the release
record, on the shape of session 22's Row 38.22 (ii) selection line (*"…"; "…", that is, "…"*), because the record's own
item names only the timing half HISTORICAL and the whole-row word is Ruling 4's.

**What this stretch gives no line** (Task 3 (a)), as §L.37 and §L.38 name them:
- **The 21 row-parts of §L.37 — Rows 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7 (i), 53.8, 53.9, 53.10, 53.11, 53.12 (i),
  53.13, 53.14, 53.15, 53.16, 53.17, 53.18, 53.19, 53.20 and 53.21 (i):** *"No line now"* for the part that follows and
  the part that waits, as Ruling 5 of
  `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md` rules it (its record lines
  233–236): each *"keeps its proposed UNPLACED until what it waits for is settled"* (for these rows, the catalog's final
  content) and *"is listed in Claude Code's report"* (§L.37's table and its *Open* point (1)). Each is listed in the
  report under *rows given no line now*, with §L.37 and those words. Before listing them, find each row by its heading
  with the Grep tool (pattern `^\*\*Row 53\.<m> —`), which must match exactly once; read only its `*PROPOSED
  DISPOSITION.*` paragraph and confirm the claim named is UNPLACED. A row not found once, or not UNPLACED at the claim
  named, is reported under *rows the act could not place*; nothing is written for any of them either way. The writing
  side found each of the 21 headings exactly once, the proposed word UNPLACED at the claim named (claim (i) at Rows
  53.7, 53.12 and 53.21, the whole row at the others).
- **The following and waiting parts of Rows 24.4 and 38.79 (ii):** *"no line now"* under the same Ruling 5 (for these
  rows, DP-O's catalog term), each listed in the report under *rows given no line now*, with §L.38 and those words. The
  HISTORICAL line of each is written above (*"The HISTORICAL parts of Rows 24.4 and 38.79 (ii) are not touched by this
  ruling"*).
- **Parts (ii) of Rows 53.7, 53.12 and 53.21:** outside §L.37's population; no line (§L.37: *"they get no line from
  it"*). Not listed under *rows given no line now*.
- **Rows the records name and do not place:** Rows 57.519 to 57.523 (placed at §L.36), Rows 38.79 (ii) and 57.396 (ii)
  and the second parts of Rows 57.107 (ii) and 57.433 (ii) as named in §L.37's record §2, the L2 Rows 55.10 to 55.17
  (rows of the L2 reading file); and from §L.38's record, the L2 twins and L2 Row 5.83 (rows of the L2 reading file),
  Rows 7.77, 7.78 (i), 7.81 to 7.84, 46.1 (ii) and 57.396 (i) (Ruling 22 of the release part 2 record, as §L.38's
  *Open* point (3) relays it: no line, each keeps its proposal), and the other rows its §4 names as read (Rows 24.4 and
  24.6 aside, which get the lines above). No line from either record, not touched.
- **The other claims of the rows this stretch writes** — Row 57.396 (i), Row 38.79 (i) — get nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — nothing written

- **Item 5:** neither record places a row-part RELOCATED, so nothing is appended. The writing side searched §10 (lines
  80021–81123) for the eleven row numbers of §3.2 as a bare number with look-around: **one hit, line 80730, Row 57.396
  (i)**, another claim, not a part this stretch writes. Run the same search with the Grep tool and report it.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 81124–83276) for
  the same eleven row numbers found none. Run the same search with the Grep tool; if you find an entry for a row-part
  this stretch writes, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.38 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.39 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 13 commit, as in sessions 11 to 22.
   Attribute it in the diff table to *"session 23's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.37 and
   §L.38 only**, after sessions 10 to 22's §L.1 to §L.36. §L.39 to §L.55 are not applied, read or touched.
3. **A1, for the writing side's handoff entries.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed.
   **Handoff entries 1228, 1229 and 1230 ARE landed**, with this file, in §5 act 1, as sessions 8 to 22 landed theirs. Any
   other untracked handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the two records this stretch
   enters (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The
   writing side's search: **none of the three phrases in either record, in either search**, as §L.37's and §L.38's *The
   act's search* say. Report the result. Item 2: not reached. Item 3: not reached. Item 4: not reached. Item 5: nothing
   appended (§3.3). Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 13 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before §L.38's lines and the in-progress line are all written,
   do not commit; STOP and report which of them were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 13 commit:**
     `git diff 2c21e606b3864f2f681b46f8d3fc3185f2973b37 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session23_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the in-progress line of §3.5 item 3; and a NOT QUARANTINED line only if §3.4
     (b) found an entry. Then
     `git diff --numstat 2c21e606b3864f2f681b46f8d3fc3185f2973b37 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 35 added lines and 1 deleted line** (the 17 lines and their 17 blank lines, 34; the
     in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2 that was
     STOP-and-report**, plus 1 added for each NOT QUARANTINED line §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,197 added lines and 4 deleted lines** (`1197` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 22 the file stood at 1,163 added and 4 deleted against the Task 2
     commit (session 22's instruction gave that figure and its report confirmed it [relayed: the numstat itself not
     re-run here]); this stretch adds 34 lines. The in-progress line replaces a line that is itself an addition against
     the Task 2 commit, so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **508** (491 + 17, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting` **17** (less 1 for each line that was
     STOP-and-report, plus 1 for a NOT QUARANTINED line naming it),
     `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting` **0**,
     `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting` **28** and
     `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting` **7** (all three unchanged).
   - **Then, if every line of §3.2 was written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`aa5b2803720dea061fdf722ea9b765ceda781b31`** — the blob of the writing side's simulated edit (§8 below: 5,320,637
     bytes, 84,636 lines, line feeds only). A different blob with every count above as given means a byte differs somewhere in what was written: do not
     commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 14 (§L.37 and §L.38): the 17 lines of the pairwise-grammar row-parts written in the reading file under their ratification, the 21 idiom-tags part 2 row-parts given no line now, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_23_task_3_stretch_14_2026_11_24.md`**, as sessions 2 to 22
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.39, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's files first, in a commit of their own, before any edit to the reading file.** Exactly
   these paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_23_task_3_stretch_14_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_eight.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_nine.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1228, 1229 and 1230 and the session 23 instruction of the L3 application landed; Task 3 stretch 14 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: for each row, the row check of
   §3.1 item 4 and the word check of §3.1 item 5, then its lines of §3.2; the check of the 21 §L.37 rows of §3.2's last
   paragraph; then the §10 search of §3.3; the §11 search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and
   the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_23_task_3_stretch_14_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 23 of the L3 application, Task 3 stretch 14 (§L.37 and §L.38) written; stretch 15 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 17 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 38.79, 57.398 and 57.496 and as one sentence for
   the other eight if they were as stated; the quotation check, each quoted passage stated; the §10 search of §3.3 and
   the §11 search of §3.4, with their results.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (the 21 row-parts of §L.37, each with §L.37 and the words that list it, and the following and
   waiting parts of Rows 24.4 and 38.79 (ii), each with §L.38 and those words); *recorded lines not written: no
   disposition word* (none expected); *rows named by more than one record* (Rows 38.79 and 57.396, as §3.1 item 7
   says); *ADOPTED words read at the row* (all 7 ADOPTED lines, each with the proposed word read and that its line does
   not say *as proposed*); *audit questions added* (none); *audit questions no longer quarantined* (none expected); *§10
   rows a record says leave, not named by row* (none: neither record says a row leaves §10); the decided-against search
   (§4 item 4), with its result.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph. *A heading of this
   session's report only, as in sessions 10 to 22's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 23 of the L3 application ends here. Stretch 15 of Task 3 is not begun. Nothing else was done."*

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

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1228, a writing session (entry 1228 §3 step 1: the sitting
booted on entry 1227 verified session 22's stretch at the objects, no finding, and this sitting does not re-verify it).
Read at the objects for this file, over staged copies: the three git reference files (both refs `8beb212a…`); the
commit object `8beb212a…` decompressed and its SHA-1 recomputed, its parent `2c21e606b3864f2f681b46f8d3fc3185f2973b37`;
the reading file's blob recomputed, `720b5073cd129493bd196112acb20ce3e9c277a2` (5,314,921 bytes, 84,602 lines, no
carriage return), its `##` headings (§6 at 435, §7 79563, §10 80021, §11 81124, §12 83277) and line 54 in full; session
22's instruction whole; the big dispatch's staged copy (941,330 bytes), at lines 159–258 (the forms), 3888–3987 (§L.37
whole), 3988–4113 (§L.38 whole) and §L.39's table rows (for the judgment of where the stretch stops); the two records
whole (6,479 and 8,180 bytes as staged); the release part 1 record at lines 140–244 (Rulings 4 and 5); the list-answers
part 4 record whole; §L.39's record at its size only (9,543 bytes). Each of the 11 rows found exactly once by its
heading, inside §6, and read from its heading to its closing `---` (the L2 entry paragraphs of the rows of member 57
skipped as not bearing on the line): its shape, its earlier lines (Row 38.79 only), its proposed word for the claim
named (UNPLACED at each) and its outgoing statement, as §3.1 items 2, 4 and 5 state; §10 and §11 searched for the eleven
row numbers as a bare number with look-around (§10: line 80730, Row 57.396 (i), another claim; §11: none); the counts
§1 check 4 gives. The record names searched at the reading file: pairwise-grammar 0, idiom-tags part 2 0. The 21 rows
of §L.37 found exactly once each by their headings, their proposed paragraphs' openings read (UNPLACED at the claim
named). Every quotation of §3.2 checked against its record by a read-only script (line breaks and runs of spaces read
as one space, asterisks removed): the 22 quotations from the pairwise-grammar record each found there, every one exactly
once; Row 24.6's two added quotations found in the release part 1 record. Both records searched for the three
decided-against phrases (line breaks joined, case matched and not): none. **The edit simulated on a copy of the reading
file in the container** by §3.1 item 2's placement rule and §3.5 item 3's line, the lines taken by script from this
file's own text, gives, against the staged file, **35 added lines and 1 deleted** (the deletion at line 54; the 17
lines and their blanks inserted at the eleven rows, each at the place §3.1 item 2 states for it: after line 33937 (Row
24.4), 33965 (24.6), 48796 (38.79, after its three earlier lines), 76809 (57.396), 76853 (57.398), 77066 (57.405),
77892 (57.451), 78745 (57.493), 78787 (57.494), 78830 (57.495) and 78869 (57.496), each but the first three directly
above *At the source now.*), the counts **508 / 3 / 53 / 26 / 1 / 1**, the record names **17** (pairwise grammar), **0**
(idiom-tags part 2), **28** (idiom-tags part 1) and **7** (substitution part 2), no new line saying *as proposed*, and
the blob **`aa5b2803…`** (5,320,637 bytes, 84,636 lines). Relayed, not re-checked here: the archive JSON's blob
`1df4f207…` and the untracked paths (session 22's instruction and the sitting booted on entry 1227); the Task 2 commit
`4b6dc3bd…` (as session 22's instruction gives it); the 1,163 added and 4 deleted lines against the Task 2 commit after
session 22; the end of `cowork_handoff.md`'s topmost block at line 255 and the line-180 start of
`cowork_audit_protocol.md`'s dispatch-protocol section (as session 22's instruction gives them); the line ranges of the
big dispatch §2 item 9 names outside 159–258 and 3888–4113 (as session 22's instruction gives them, the dispatch
unchanged).*

*Checked 2026-11-24 (Stockholm), as a turn of its own, by the NEW Cowork session booted on entry 1229 (Ruling 1 (e)),
over staged copies. Re-read at the objects: the three git reference files (both refs `8beb212a…`, unmoved); the blobs of
the big dispatch (`b5274c2c…`), the reading file (`720b5073…`, 5,314,921 bytes, 84,602 lines, no carriage return) and
this file as landed unchecked (`eb238a30…`), each recomputed; both records whole; the release part 1 record at lines
137–244 (Rulings 4 and 5, with the section headings); the list-answers part 4 record at lines 1–72 (Rulings 1 and 2);
the big dispatch at lines 159–258 (the forms, form (b)'s paragraph *Which ADOPTED word*, its rule by part, form (b-H))
and 3888–4113 (§L.37 and §L.38 whole), and its `##` and `### §L.3x` headings, which agree with the ranges §2 item 9
gives. Every quotation of §3.2 compared with its record, word and punctuation: each found. The reading file's ten counts
of §1 check 4 and its `##` headings as stated; line 54 as stated; the 11 rows each found once inside §6, each proposed
UNPLACED at the claim named, their outgoing statements read at the rows' openings and fitting §3.1 item 4, their shapes
as §3.1 item 2 states; the 21 §L.37 rows each found once, UNPLACED at the claim named; §10 searched (one hit, line
80730, Row 57.396 (i)) and §11 (none); the decided-against search over both records, line breaks joined, case not
matched: none. The settlements: (3) and (4) stand on the precedent of Row 46.44 (i)'s two lines at the reading file
(both quoting the whole item) and of §L.36's table naming short phrases for those parts; (5) on the shapes at lines
33898, 65249 and 78279; (6) on §L.38's table's own wording for Row 24.6 and Row 38.22 (ii)'s line, line 47778. **The
edit re-simulated** by a `python3 -I` script of this session's own (on the user's leave), the 17 lines taken from §3.2's
code blocks and the in-progress line from §3.5 item 3, each row's lines placed after the blank line that ends its
proposed paragraph or its earlier ruled lines: 35 added and 1 deleted; counts 508 / 3 / 53 / 26 / 1 / 1; record names
17 / 0 / 28 / 7; no new line saying *as proposed*; **blob `aa5b2803720dea061fdf722ea9b765ceda781b31`** (5,320,637 bytes,
84,636 lines), as stated. **Corrected, no line of §3.2 and no expected figure changed:** (1) §2 item 8's ranges of the
release part 1 record, from *"lines 140–177"* and *"lines 231–243"*, which began after Ruling 4's and Ruling 5's headings
(lines 137 and 187), to lines 137–177 and 187–243; (2) §3.2's last paragraph, *"and the rows its §4 names as read"*,
wider than the act (Rows 24.4 and 24.6 are among them and get lines), narrowed to the other rows, 24.4 and 24.6 named
aside; (3) this section's insertion point for Row 57.496, *"78868"*, to 78869, the blank line after its proposed
paragraph (the simulation places it there and gives the blob above). Added: entry 1230 to §1 check 5, §2 item 4, §4
item 3 and §5 act 1 with its subject; the status banner. Former wordings not kept, as this file is unreleased.*
