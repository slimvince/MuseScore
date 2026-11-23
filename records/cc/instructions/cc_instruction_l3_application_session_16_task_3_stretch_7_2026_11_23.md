# CC dispatch — the L3 application, SESSION 16 of several: Task 3 of the L3 application dispatch, seventh stretch (§L.25 to §L.28), and nothing else

> **STATUS: WRITTEN 2026-11-23, CHECKED AS A TURN OF ITS OWN AND CORRECTED 2026-11-23 (the same sitting; see the
> provenance), NOT YET RELEASED,** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_nine.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 14 applied Task 3's first five stretches, §L.1 to §L.23. Session 15
applied the sixth stretch, §L.24, in commit `4ab7231b3091933d087f50b089cb361f7fecd22a` (called **the stretch 6 commit**
below), and committed its report as `3d1a95a119069b208acfcb0c68c355773446d9f1`, the current tip.

**This is session 16. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for FOUR ledger entries: §L.25 to §L.28, the four cuts of
entry 481 §2 item 13 (display; kinds of span; general architecture rules; facts from the published literature). It
commits and pushes that seventh stretch, writes its report, and STOPS.** §L.29 is a later session's.

**What this stretch writes, in one paragraph.** **54 lines, all opening `*RULED DISPOSITION (`, all naming Ruling 1 of
their record, all with the word ADOPTED — proposed**, one per row-part, on 48 rows: 25 from the display record (§L.25),
11 from the span-kinds record (§L.26), 14 from the architecture-rules record (§L.27) and 4 from the literature-facts
record (§L.28). **51 say *as proposed***; the three ruled *"in the narrower wording"* (Rows 38.47 and 38.48, Row 36.106
(i)) do not. §3.2 gives every one with its exact text. And the in-progress line brought forward from §L.24 to §L.28
(§3.5). **Nothing at §10 and nothing at §11** (§3.3 and §3.4 say why).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the dispositions the records
already place; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `3d1a95a119069b208acfcb0c68c355773446d9f1`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_16_task_3_stretch_7_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 6 commit left it.**
   `git diff --quiet 4ab7231b3091933d087f50b089cb361f7fecd22a -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 3d1a95a119069b208acfcb0c68c355773446d9f1 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `8c9596ccb9b76ef6404fe38204a02e025544878d`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **354**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; and each of `cowork_rulings_2026_11_04_l3_display_sitting`,
   `cowork_rulings_2026_11_04_l3_span_kinds_sitting`, `cowork_rulings_2026_11_04_l3_architecture_rules_sitting` and
   `cowork_rulings_2026_11_04_l3_literature_facts_sitting` must count **0**. Any other result: STOP and report, the file
   not touched. (The writing side's staged copy: 5,260,769 bytes, 84,312 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 3d1a95a119069b208acfcb0c68c355773446d9f1 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1208 and 1209),
     plus the paths sessions 2 to 15 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_nine.md` (written by the sitting that
   verified session 15; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eight.md` (the one before it, written by
   the sitting that wrote session 15's instruction; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The four records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening). All under `records/cowork/rulings/`:
   - `cowork_rulings_2026_11_04_l3_display_sitting.md` (§L.25; 6,101 bytes, 78 lines);
   - `cowork_rulings_2026_11_04_l3_span_kinds_sitting.md` (§L.26; 6,011 bytes, 78 lines);
   - `cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md` (§L.27; 7,799 bytes, 94 lines);
   - `cowork_rulings_2026_11_04_l3_literature_facts_sitting.md` (§L.28; 6,707 bytes, 82 lines).
   **Do NOT read the records of §L.1 to §L.24 or of §L.29 to §L.55, and do not open the four records' surfaces** (the
   lines quote the records only).
8. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b) and its paragraph *Which ADOPTED word, and when
     as proposed is written* are the form every line of this stretch is written in**, the premise ledger, the declared
     start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 2618–3039 (§L.25 to §L.28, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–2617 (§L.1 to §L.24, applied); lines 3040–5906 (§L.29 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary);
   - **each of the 48 rows §3.2 names (54 row-parts), whole, at §6** (lines 435–79288): find each by its heading with the
     Grep tool, pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from
     that heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
   - §10 (lines 79747–80833) and §11 (lines 80834–82986), each searched with the Grep tool for every row number of this
     stretch (§3.3, §3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch: one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*` paragraph
   and every other sentence of the row untouched. Every line names its record's **Ruling 1** (each of the four records
   has one ruling), the record file written as its bare file name, as sessions 10 to 15 wrote theirs. Where §3.2 names a
   claim, the line names it (form (b)'s split-row rule: each record names these row-parts claim by claim); otherwise the
   line names none. **Each row-part gets exactly one line**, so six rows get two lines from this stretch (§3.1 item 2).
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"At the
   source now."* or *"The decisions register at this row."*). Each new line is followed by one blank line. Read each row's
   actual shape from its proposed paragraph to its end before writing. **The writing side read all 48 rows at the staged
   copy; every one ends with a blank line and then `---`.** Their shapes after the proposed paragraph:
   - **41 rows: nothing after the proposed paragraph** — 4.2, 4.3, 7.330, 15.42, 19.1, 19.3, 21.191, 21.205, 7.5, 7.6,
     7.24, 7.59, 7.226, 7.227, 7.228, 7.274, 8.54, 19.4, 19.5, 19.6, 19.8, 19.37, 19.40, 38.62, 38.64, 38.83, 38.84,
     38.63, 19.29, 19.53, 19.33, 19.56, 19.76, 19.77, 19.78, 19.82, 20.7, 38.47, 38.48, 20.31, 36.106. Each such row ends,
     after the edit: proposed paragraph, blank line, **the new line(s), each followed by a blank line**, `---`.
   - **4 rows carrying one earlier ruled line, on a different claim (item 6); the new line goes after it:** Row 7.329
     (claim (i), `cowork_rulings_2026_11_03_l3_cadence_type_sitting.md`, Ruling 2); Row 7.294 (claim (ii),
     `cowork_rulings_2026_11_03_l3_cadence_features_sitting.md`, Ruling 1); Row 8.105 (claim (ii),
     `cowork_rulings_2026_11_08_l3_disposition_words_sitting.md`, Ruling 1); Row 36.111 (claim (ii),
     `cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md`, Ruling 1), **which is followed by a paragraph headed
     *"The decisions register at this row."*: the new line goes between the earlier line and that paragraph.**
   - **3 rows with further paragraphs after the proposed paragraph and no earlier line; the new line(s) go directly
     beneath the proposed paragraph, above them:** Row 57.119 (*"At the source now."*, then *"The decisions register at
     this row."*); Row 57.354 (*"At the source now."*); Row 56.2 (*"At the source now."*, then *"The decisions register
     at this row."*).
   - **Six rows get two lines from this stretch, claim (i)'s line first:** 7.5, 38.62, 38.64, 38.83 (claim (i) from the
     span-kinds record's part A, claim (ii) from its part C), 19.29 and 56.2.
   If you find a different shape at a row (another earlier line, a further paragraph, or an ending other than `---`),
   state it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, that
   line is a STOP-and-report.
3. **The quotation.** Each line quotes the words §3.2 gives for it: **the record's own heading of the part that places
   the row-part** (the bold words of its §1 bullet, from the part's letter or *"Row"* to *"ADOPTED"*, the closing period
   and asterisks left out), and, for the three row-parts ruled in a narrower wording, also the narrower sentence the
   record quotes (the words inside its quotation marks) and the record's sentence that the row's own text is carried as
   written. **The writing side checked every quotation against its record by a read-only script (words and punctuation,
   line breaks read as spaces, asterisks not compared): each found exactly once, in the record's §1.** Before writing
   each line, find each of its quoted passages in the record yourself and compare it the same way: every word and every
   punctuation mark must match, line breaks read as spaces. The line keeps its marks exactly as §3.2 gives them. A
   difference is a STOP-and-report for that line: no line written, listed in the report under *rows the act could not
   place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that part is **ADOPTED — proposed** (item 5); and **the
   row's outgoing statement fits what the record says of the part placing it** (the part's sentence after its bold
   heading, in the record's §1). A row that does not fit is a STOP-and-report for that row-part: no line, listed under
   *rows the act could not place* with what was read.
5. **The word, and *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is written*; the §L
   entries' *Open* point (1), each answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). Each record writes
   *"ADOPTED"* (for three row-parts *"ADOPTED in the narrower wording"*) and names no L3-S number as carrying the
   content, so the paragraph's item (4) gives the word, as each §L entry's *Open* point (1) says: the row's proposed word
   for that part. **The writing side read the proposed paragraph of all 54 row-parts: each is ADOPTED — proposed for the
   part named** (for the split rows, at the claim named: Rows 7.5, 7.226, 7.294, 7.329, 15.42, 19.3, 19.29, 19.53, 19.56,
   19.76, 8.105, 36.111, 20.31, 56.2, 36.106, 38.62, 38.64 and 38.83; a claim of those rows that this stretch does not
   name gets nothing from it). So every line's word is **ADOPTED — proposed**.
   - **51 lines say *as proposed*:** their word is the row's own proposed word, and the record adopts the content as
     proposed.
   - **3 lines do not:** Rows 38.47 and 38.48 (the architecture-rules record, part E, *"ADOPTED in the narrower
     wording"*: *"The reading file's proposal sentence (…) is not adopted as written"*) and Row 36.106 (i) (the
     literature-facts record, *"ADOPTED in the narrower wording"*: the proposal clause *"is not adopted"*). Form (b)'s
     paragraph: *"Otherwise as proposed is not written, and the placement is given in the record's words. That includes
     … a ruling that adopts narrower content than the proposal (§L.27 part E, Rows 38.47 and 38.48; §L.28, Row 36.106
     (i))."*
   If you find a row-part's proposed word for the part named other than ADOPTED — proposed, that line is a
   STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of the 54 is listed in the report under
   *ADOPTED words read at the row*, with whether its line says *as proposed*.
6. **Rows named by more than one record** (form (b)'s two-record rule, by part). Four rows already carry another
   record's line, **each on a different claim from this stretch's line** (item 2's second bullet): Row 7.329 ((i) at §L.6;
   (ii) here), Row 7.294 ((ii) at §L.5; (i) here), Row 8.105 ((ii) at §L.2; (i) here), Row 36.111 ((ii) at §L.23; (i)
   here). Lines on different parts are each written, so both stand, and each row is listed under *rows named by more
   than one record*. Row 36.106's claim (iii) is among §L.24's relocated row-parts, with no line; list it there too,
   saying so. **Not cases of the rule:** Rows 19.29 and 38.83 are each split within their own record. If you find a claim
   where two lines would fall on the same part with differing words, that claim is a STOP-and-report and gets neither
   line; if one of those lines is an earlier stretch's, do not delete it: STOP, do not commit, and report.

### 3.2 The lines, record by record, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several row-parts, `<claim>` is filled in
from the row list (written `(i)`, `(ii)` … as the list gives it); where the list gives no claim, `<claim>` and the space
after it are dropped. Where a block's lines are given one by one, each is given whole.

**§L.25 — the display record (`cowork_rulings_2026_11_04_l3_display_sitting.md`): 25 lines.**

*Part A — 10 lines, each* as proposed. Row-parts, in this order: 4.2; 4.3; 7.329, written `(ii)`; 7.330; 15.42, written
`(iii)`; 19.1; 19.3, written `(ii)`; 21.191; 21.205; 57.119. *What the record says of them:* every display string is
produced outside the analysis, from published facts; the analysis carries no display convention; a Roman numeral and a
Nashville number are two renderings of one decided chord.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "A (10 row-parts: 4.2, 4.3, 7.329 (ii), 7.330, 15.42 (iii), 19.1, 19.3 (ii), 21.191, 21.205, 57.119) — ADOPTED".
```

*Part B — 10 lines, each* as proposed. Row-parts, in this order: 7.5, written `(i)`; 7.5, written `(ii)`; 7.6; 7.24; 7.59;
7.226, written `(ii)`; 7.227; 7.228; 7.274; 7.294, written `(i)`. *What the record says of them:* the tonic / subdominant
/ dominant summary is no published fact of the analysis, at most a read-out a display computes from the published chord,
defaulting its context-dependent cases to the tonic side, and no decision reads it.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "B (10 row-parts: 7.5 (i), 7.5 (ii), 7.6, 7.24, 7.59, 7.226 (ii), 7.227, 7.228, 7.274, 7.294 (i)) — ADOPTED".
```

*Part C — 1 line,* as proposed. Row 8.54. *What the record says of it:* the grouping has L3 as its only producer and is
the surface a display reads.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1).* **ADOPTED — proposed** — as proposed; "C (1 row-part: 8.54) — ADOPTED".
```

*Part D — 4 lines, each* as proposed. Rows, in this order: 19.4; 19.5; 19.6; 19.8. *What the record says of them:* nothing
L3 publishes is written into the score except by the user's explicit act.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1).* **ADOPTED — proposed** — as proposed; "D (4 row-parts: 19.4, 19.5, 19.6, 19.8) — ADOPTED".
```

**§L.26 — the span-kinds record (`cowork_rulings_2026_11_04_l3_span_kinds_sitting.md`): 11 lines.**

*Part A — 8 lines, each* as proposed. Row-parts, in this order: 19.37; 19.40; 38.62, written `(i)`; 38.62, written
`(ii)`; 38.64, written `(i)`; 38.64, written `(ii)`; 38.83, written `(i)`; 38.84. *What the record says of them:* L3's
kinds of span are distinct kinds, each named by what bounds it, and the bare word "region" is not used.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "A (8 row-parts: 19.37, 19.40, 38.62 (i), 38.62 (ii), 38.64 (i), 38.64 (ii), 38.83 (i), 38.84) — ADOPTED".
```

*Part B — 1 line,* as proposed. Row 38.63. *What the record says of it:* the music is segmented several ways at once.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1).* **ADOPTED — proposed** — as proposed; "B (1 row-part: 38.63) — ADOPTED".
```

*Part C — 2 lines, each* as proposed. Row-parts, in this order: 38.83, written `(ii)`; 57.354. *What the record says of
them:* for each pair of kinds of span the specification states whether one nests in the other or the two cut across,
and never states containment where they cut across.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "C (2 row-parts: 38.83 (ii), 57.354) — ADOPTED".
```

**§L.27 — the architecture-rules record (`cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md`): 14 lines.**

*Part A — 3 lines, each* as proposed. Row-parts, in this order: 19.29, written `(i)`; 19.29, written `(ii)`; 19.53,
written `(ii)`. *What the record says of them:* every cost-driving choice of L3 is an explicit setting; every optional
expensive refinement is a separable stage; re-analysis after an edit covers the edited span and a bounded margin.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "A (3 row-parts: 19.29 (i), 19.29 (ii), 19.53 (ii)) — ADOPTED".
```

*Part B — 1 line,* as proposed. Row 19.33. *What the record says of it:* any style-specific behavior of L3 lives only in
the fitted values of its model, never in its structure.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1).* **ADOPTED — proposed** — as proposed; "B (1 row-part: 19.33) — ADOPTED".
```

*Part C — 5 lines, each* as proposed. Row-parts, in this order: 19.56, written `(iii)`; 19.76, written `(ii)`; 19.77;
19.78; 19.82. *What the record says of them:* L3 reads, within its scope, all the information the layers beneath it publish without loss and
discards none; a ruled-out reading need not be published where its exclusion is recomputable; an alternative never
computed on measured evidence is no loss; a fact no consumer reads is declared dormant or removed.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "C (5 row-parts: 19.56 (iii), 19.76 (ii), 19.77, 19.78, 19.82) — ADOPTED".
```

*Part D — 1 line,* as proposed. Row 20.7. *What the record says of it:* the code computing L3's facts depends on no type
of the score editor.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1).* **ADOPTED — proposed** — as proposed; "D (1 row-part: 20.7) — ADOPTED".
```

*Part E — 2 lines, NOT* as proposed (§3.1 item 5). Rows, in this order: 38.47; 38.48. Both lines are the same:
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1).* **ADOPTED — proposed** — "E (2 row-parts: 38.47, 38.48) — ADOPTED in the narrower wording"; "A reading missing from L3's own candidate readings is remedied inside L3, by widening its candidate set; a backward edge is not the remedy, except as the deliberate, surfaced, measured and documented exception D-466 admits."; "The rows' own text is carried as written".
```

*Part F — 2 lines, each* as proposed. Row-parts, in this order: 8.105, written `(i)`; 36.111, written `(i)`. *What the
record says of them:* the phrase and section grouping is an explanatory output of the analysis, not an accuracy
requirement on it.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "F (2 row-parts: 8.105 (i), 36.111 (i)) — ADOPTED".
```

**§L.28 — the literature-facts record (`cowork_rulings_2026_11_04_l3_literature_facts_sitting.md`): 4 lines.**

*Rows 20.31 (i), 56.2 (i) and 56.2 (ii) — 3 lines, each* as proposed. Row-parts, in this order: 20.31, written `(i)`;
56.2, written `(i)`; 56.2, written `(ii)`. *What the record says of them:* no validated deterministic rule set places
phrase boundaries in polyphonic music; almost all published work on locating phrase endings addresses a single melodic
line; for several simultaneous voices nothing comparable has been established.
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_literature_facts_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — as proposed; "Rows 20.31 (i), 56.2 (i) and 56.2 (ii) — ADOPTED".
```

*Row 36.106 (i) — 1 line, NOT* as proposed (§3.1 item 5):
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_literature_facts_sitting.md, Ruling 1).* (i) **ADOPTED — proposed** — "Row 36.106 (i) — ADOPTED in the narrower wording"; "That L3's specification record, as a fact of the published literature, that the phrase-boundary cues are validated on single melodic lines only."; "The row's own text is carried as written".
```

**The count.** `*RULED DISPOSITION (`: **54**, all **ADOPTED — proposed**: 25 + 11 + 14 + 4. By record name: the display
record **25**, the span-kinds record **11**, the architecture-rules record **14**, the literature-facts record **4**. None
opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) each line quotes, as the record's
placement, the record's own bold heading of the part that places it — the words that name the row-parts and say
*ADOPTED* — on the precedent of the key-areas lines an earlier stretch left in the file (its lines 1807 and 1855
at the writing side's staged copy), which quote the record's row-naming words (*"Rows 3.1(iii), 3.4, 8.12, … ADOPTED
(the definition as ruled)"*); the part's gist, which is long and which the big dispatch's Task 1 (c) item 3 places in
the successor with the added statement [relayed: the successor not read by the writing side], is not repeated on each
row; (2) for the
three narrower row-parts the line also quotes the narrower sentence and the record's *"carried as written"* sentence, so
that what is adopted, and that the row's text is not changed, stand at the row.

**What this stretch gives no line** (Task 3 (a)): the row-parts each §L entry lists under *Rows the record mentions and
does not place* — §L.25: the seventeen traveling row-parts (Ruling 13 of the part 2 ruling record for fourteen of them:
no line, each keeps its proposal, no listing of their own in your report; Rows 8.48 (i), 8.89 and 8.91 are §L.53's) and
item 13's remaining cuts (which are §L.26 to §L.28 themselves); §L.26: Rows 19.39 (ii) and 19.38, the remaining cuts and
the traveling row-parts; §L.27: Rows 8.105 (ii) and 36.111 (ii) (each already carrying an earlier stretch's line, §3.1
item 2), item 13's last cut (§L.28), Row 19.39 (ii) and the traveling row-parts; §L.28: Rows 8.105 (ii), 36.111 (ii) and
19.39 (ii), and the traveling row-parts. **The other claims of the split rows** (for example Row 7.226 (i), Row 19.53
(i) and (iii), Row 36.106 (ii) and (iii)) get nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — nothing written

- **Item 5:** no row-part of this stretch is placed RELOCATED, so nothing is appended to §10.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.
- **No row-part of this stretch stands in a §10 entry.** The writing side searched §10 (lines 79747–80833) for every row
  number of this stretch as a bare number with look-around: the hits name only other claims — Row 7.226 (i), Row 7.294
  (ii), (iii) and (iv), Row 19.56 (ii), Row 36.106 (iii) — none of them a row-part of this stretch. Run the same search
  with the Grep tool; if you find a row-part of this stretch in a §10 entry, STOP and report before writing anything
  there.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row-part of this stretch. The writing side's search of §11 (lines 80834–82986)
  for every row number found only: Row 15.42 (i) and (ii) and Row 19.3 (i), other claims, not touched (item 7 (b): *"A
  §11 entry naming another claim of the row is not touched"*); and two member headings whose section numbers read
  *4.3* (*"4.3 ChordSymbolFormatter"*, *"4.3b HarmonicRhythm"*), not rows. Run the same search with the Grep tool; if
  you find an entry for a row-part of this stretch, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its
  indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.28 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.29 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 6 commit, as in sessions 11 to 15.
   Attribute it in the diff table to *"session 16's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.25 to
   §L.28 only**, in that order, after sessions 10 to 15's §L.1 to §L.24. §L.29 to §L.55 are not applied, read or touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1208 and 1209 ARE landed**, with this file, in §5 act 1, as sessions 8 to 15 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the four records this stretch
   enters (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case not matched). §L.25 to
   §L.28 each say none occurs; the writing side's search found none in any of the four. List the result in the report,
   record by record. Item 2: not reached. Item 3: not reached. Item 4: not reached. Item 5: nothing to append (§3.3).
   Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 6 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before all four entries are applied, do not commit; STOP and
   report which entries were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 6 commit:**
     `git diff 4ab7231b3091933d087f50b089cb361f7fecd22a -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session16_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the in-progress line of §3.5 item 3; and a NOT QUARANTINED line only if §3.4
     (b) found an entry. Then
     `git diff --numstat 4ab7231b3091933d087f50b089cb361f7fecd22a -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 109 added lines and 1 deleted line** (the 54 lines and their 54 blank lines, 108; the
     in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2 that was
     STOP-and-report**, plus 1 added for each NOT QUARANTINED line §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 981 added lines and 4 deleted lines**, with the same adjustments as above. *The writing side's
     arithmetic: after session 15 the file stood at 873 added and 4 deleted against the Task 2 commit (session 15's
     instruction §4 item 8, and the verification recorded in entry 1209 §2 item 1, which found the file at the expected
     counts); this stretch adds 108 lines. The in-progress line replaces a line that is itself an addition against the
     Task 2 commit, so it adds no line and deletes none there. The 4 deleted are the four lines session 10's state
     sentences were written into.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **408** (354 + 54, less 1 for
     each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_04_l3_display_sitting` **25**, `cowork_rulings_2026_11_04_l3_span_kinds_sitting` **11**,
     `cowork_rulings_2026_11_04_l3_architecture_rules_sitting` **14**,
     `cowork_rulings_2026_11_04_l3_literature_facts_sitting` **4** (each less 1 for a line of that record that was
     STOP-and-report, plus 1 for a NOT QUARANTINED line naming it).
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 7 (§L.25 to §L.28): the 54 row-parts of the four item-13 cuts re-marked ADOPTED — proposed in the reading file under their ratifications, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_16_task_3_stretch_7_2026_11_23.md`**, as sessions 2 to 15
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.29, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own, before any edit to the reading file.**
   Exactly three paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_16_task_3_stretch_7_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eight.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_nine.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1208 and 1209 and the session 16 instruction of the L3 application landed; Task 3 stretch 7 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it, entry by entry in ledger
   order (§L.25, §L.26, §L.27, §L.28): for each row-part, the row check of §3.1 item 4 and the word check of §3.1 item 5,
   then its line of §3.2; then the searches of §3.3 and §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the
   push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_16_task_3_stretch_7_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 16 of the L3 application, Task 3 stretch 7 (§L.25 to §L.28) written; stretch 8 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 54 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for the seven rows of item 2's second and third bullets and
   as one sentence for the 41 of its first bullet if they were as stated; the results of the §10 and §11 searches of §3.3
   and §3.4.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (none expected); *recorded lines not written: no disposition word* (none expected); *rows named by
   more than one record* (Rows 7.329, 7.294, 8.105 and 36.111, each with the earlier record, its claim and this stretch's
   claim; and Row 36.106, its claim (iii) named at §L.24 with no line, as §3.1 item 6 says); *ADOPTED words read at the
   row* (all 54, each with the proposed word read and whether its line says *as proposed*); *audit questions added*
   (none); *audit questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by row*
   (none: no record of this stretch says a row leaves §10); the decided-against search (§4 item 4).
5. The diff table of §4 item 8, every changed passage attributed, and the counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: the rows each record mentions and does not
   place, as §3.2's last paragraph names them, each with its §L entry (the traveling row-parts by count and with Ruling
   13's words, as §L.25 *Open* point (3) gives them). *A heading of this session's report only, as in sessions 10 to
   15's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 16 of the L3 application ends here. Stretch 8 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a line of §3.2
  that is STOP-and-report under them or under §3.1 items 2 to 6 is reported and the rest of this stretch applied, as
  they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 6);
- a row-part of this stretch is found in a §10 entry (§3.3);
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1209. Read at the objects for this file: the
three git reference files (both refs `3d1a95a1…`); entries 1209, 1208 and 1026 whole; entry 1207 whole; session 15's
instruction whole; session 14's instruction at lines 1–300; the four records whole; the big dispatch at lines 159–274
(the forms), 2618–3039 (§L.25 to §L.28) and 6616–6820 (Task 3), and the boundary lines of the ranges §2 item 8 names or
bars from line 430 on (lines 430, 431, 2617, 2618, 3039, 3040, 5906, 5907, 6615, 6616, 6820, 7110, 7111, 7135, 7136);
the ranges before line 430 as session 15's instruction gives them, the blob being the same. Its blob
recomputed on the staged copy (`b5274c2c…`, 7,157 lines). The reading file, by read-only scripts over the staged copy:
its blob computed as git would (`8c9596cc…`, 5,260,769 bytes, 84,312 lines, no carriage return); its `##` headings; each
of the 48 rows found exactly once by its heading, inside §6, and read from its heading to its closing `---` (heading,
the derived statements, the current-text axis, the proposed paragraph and every paragraph after it in full; the
outgoing statement's first 150 to 260 characters); every row's shape after its proposed paragraph and its ending; §10
and §11 searched for every row number as a bare number with look-around; the in-progress line at line 54; the six
counts (354 / 3 / 53 / 26 / 1 / 1) and the four record names (0 each). Every quotation of §3.2 checked against its
record by a read-only script (line breaks joined, asterisks removed): each found exactly once. The four records searched
for the three decided-against phrases (line breaks joined, case not matched): none in any. The blobs of entries 1208
(`64573f95…`, 10,619 bytes) and 1209 (`8b507617…`, 11,493 bytes) computed on the staged copies. Relayed, not re-checked
here: the archive JSON's blob `1df4f207…` and the untracked paths (session 15's instruction §1 item 5, which entry 1209
§2 item 1 found session 15's report to agree with); the end of `cowork_handoff.md`'s topmost block at line 255 and the
line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 15's instruction gives them); the
873 added and 4 deleted lines against the Task 2 commit after session 15 (session 15's instruction and entry 1209 §2
item 1); that Rows 7.329 (i), 7.294 (ii), 8.105 (ii) and 36.111 (ii) carry the lines of §L.6, §L.5, §L.2 and §L.23 (read
at the rows by record name; the §L numbers as entry 1209 and the big dispatch's §L.25 and §L.27 give them).*

*The check, as a turn of its own: Cowork, 2026-11-23 (Stockholm), the same sitting, the file not yet handed to Claude
Code, so its corrections keep no former wording (as entry 1208 §2 item 3 did). By read-only script over the staged
copies: §3.2's fifteen blocks, with `<claim>` filled from their row lists, reproduce the 54 lines the writing side
derived from the records, none missing and none extra; the edit simulated on a copy of the reading file in the
container by §3.1 item 2's placement rule and §3.5 item 3's line gives, against the staged file, **109 added lines and 1
deleted**, and the counts **408 / 3 / 53 / 26 / 1 / 1** and the record names **25 / 11 / 14 / 4**; the new in-progress
line equals the current line 54 with *§L.24* and *§L.25 to* moved on to *§L.28* and *§L.29 to*; Rows 7.329, 36.111,
56.2 and 57.119 read in the simulated copy with the new line(s) where §3.1 item 2 says; every full hash in this file
one of the six objects it names. Corrected: §3.1 item 5, which said each record writes a *bare* "ADOPTED" (three
row-parts are ruled "ADOPTED in the narrower wording") and that the other claims of the split rows *"carry other
words"* (on six of those rows every claim is this stretch's); the §3.2 settlement's account of the key-areas precedent
(it named sessions 10 to 15 as its writers, not read) and of Task 1 (*"already wrote"*, not read; now relayed); one
dropped clause (*"within its scope"*) in part C's summary; and the provenance's account of the big dispatch's range
boundaries read. Also corrected before this check: the four records' line counts, first written one too high each from
a misreading of the read output. No line, row, disposition word, count, command or commit subject changed.*
