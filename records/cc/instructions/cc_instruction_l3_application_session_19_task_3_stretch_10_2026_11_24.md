# CC dispatch — the L3 application, SESSION 19 of several: Task 3 of the L3 application dispatch, tenth stretch (§L.32), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighteen.md`; CHECKED AS A TURN OF ITS OWN
> AND CORRECTED 2026-11-24 by the sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_nineteen.md` (see the check note at the end;
> one bound declared there, on the user's word "1": the expected blob of §4 item 8 was not re-derived by that check,
> and §4 item 8 itself stops before any commit if the blob differs),** under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 17 applied Task 3's first eight stretches, §L.1 to §L.30. Session 18
applied the ninth stretch, §L.31, in commit `51543b657ed1d3777f25812abede359615816369` (called **the stretch 9 commit**
below), and committed its report as `f1e7c9144b9f78b0287f12a5573cb8523263fd6d`, the current tip.

**This is session 19. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry: §L.32, the fourth record of family 1
(the catalog of named progressions; recognition and its span, part 2). It commits and pushes that tenth stretch, writes
its report, and STOPS.** §L.33 is a later session's.

**What this stretch writes, in one paragraph.** **§L.32's record gives 14 lines, all opening `*RULED DISPOSITION (` and
all naming Ruling 1 of `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md`, on 10 rows:** 9 lines with
the word **ADOPTED — proposed** (the five rows of the record's §3.1, and one part each of the four split row-parts of
its §3.3), 4 lines with the word **RELOCATED** (the other parts of those split row-parts that the record relocates), and
1 line with the word **HISTORICAL** (Row 24.1, the record's §3.5). **No line says *as proposed*:** every one of these
row-parts is proposed UNPLACED at its row. §3.2 gives every line with its exact text. **At §10, four entries are
appended** under the L2 heading, one for each RELOCATED part (§3.3). **Nothing at §11** (§3.4). And the in-progress line
brought forward from §L.31 to §L.32 (§3.5). **The other row-parts and parts the record places get no line** (§3.2's
last paragraph); ten of them are listed in the report under *rows given no line now*.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the placements the record
already makes; it decides nothing. The record orders no amendment of the successor, the charter or the interface
contract (§L.32, *Successor*, *Charter*, *Interface contract*).

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `f1e7c9144b9f78b0287f12a5573cb8523263fd6d`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_19_task_3_stretch_10_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 9 commit left it.**
   `git diff --quiet 51543b657ed1d3777f25812abede359615816369 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree f1e7c9144b9f78b0287f12a5573cb8523263fd6d -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `27e0d551e284fc33895803a98e83ace15859bbe6`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **438**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting` must count
   **13**; `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting` must count **23**; and
   `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting` must count **0**. Any other result: STOP and
   report, the file not touched. (The writing side's staged copy: 5,286,365 bytes, 84,486 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree f1e7c9144b9f78b0287f12a5573cb8523263fd6d -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the four files §5 act 1 lands (this instruction and handoff entries 1218, 1219 and 1220),
     plus the paths sessions 2 to 18 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighteen.md` (written by the sitting before
   the one that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventeen.md` (the one before it; landed by
   session 18).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The record this stretch rests on, WHOLE** — it is the authority for every line this session writes (**the
   record's own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md` (§L.32; 8,008 bytes, 101
   lines by `wc -l`). **Do NOT read the records of §L.1 to §L.31 or of §L.33 to §L.55, and do not open the record's
   surface** (the lines quote the record only).
8. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, and form (b-H)**, the premise ledger, the declared start state, the standing bars, the
     findings rule);
   - lines 395–430 (how §L is written);
   - **lines 3344–3449 (§L.32, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3343 (§L.1 to §L.31, applied); lines 3450–5906 (§L.33 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary);
   - **each of the 10 rows §3.2 names, whole, at §6** (lines 435–79456): find each by its heading with the Grep tool,
     pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
     heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
   - §10 (lines 79915–81007): its destination headings (lines opening `**To `), and the block under
     ***L2 — The tonal reading. The one entangled decision.*** from its heading (line 80117) to the next heading (line
     80647) at least from line 80600 on; and §10 searched with the Grep tool for every row number of this stretch
     (§3.3);
   - §11 (lines 81008–83160), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch: one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*`
   paragraph and every other sentence of the row untouched. Row 24.1's HISTORICAL line is form (b) as well: the record
   places it HISTORICAL in its own word, and the act's search finds none of the three decided-against phrases (§L.32,
   *The act's search*), so form (b-H) is not engaged. Every line names
   `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1` (the record has one ruling), the record
   file written as its bare file name, as sessions 10 to 18 wrote theirs. Where §3.2 names a claim, the line names it
   (form (b)'s split-row rule); otherwise the line names none. **Each row-part, and each part of a split row-part that
   the record places at L3 or relocates to L2, gets exactly one line**, so three rows get more than one line from this
   stretch: Rows 24.2 and 57.445 two each, Row 57.470 three (§3.1 item 7).
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"At the
   source now."*). Each new line is followed by one blank line. Read each row's actual shape from its proposed
   paragraph to its end before writing. **The writing side read all 10 rows at the staged copy; none carries an earlier
   ruled or recorded line, and every one ends with a blank line and then `---`.** Their shapes after the proposed
   paragraph:
   - **3 rows: nothing after the proposed paragraph** — 38.80, 24.1 and 24.2. Each such row ends, after the edit:
     proposed paragraph, blank line, **the new line(s), each followed by a blank line**, `---`.
   - **7 rows with a paragraph headed *"At the source now."* after the proposed paragraph; the new line(s) go directly
     beneath the proposed paragraph, above it:** Rows 57.400, 57.448, 57.455, 57.485, 57.445, 57.454 and 57.470. *(The
     reading file already carries 16 ruled lines placed this way, beneath a proposed paragraph or an earlier ruled line
     and above an* At the source now. *paragraph, by earlier stretches.)*
   - **Three rows get more than one line from this stretch:** Rows 24.2 (two), 57.445 (two) and 57.470 (three), the
     lines in the order in which the record names the parts (§3.2).
   If you find a different shape at a row (an earlier line, a further paragraph, or an ending other than `---`), state
   it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, that line
   is a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it, from the record's §1 (*"Ruling 1 — the 24
   row-parts' placements RATIFIED as the surface states them"*): for §3.1's five rows, §3.1's bullet whole, its bold lead
   included; for the split row-parts, §3.3's bullet whole, its bold lead included; for Row 24.1, §3.5's bullet whole, its
   bold lead included. **The writing side checked every quotation against the record by a read-only script (words and
   punctuation, line breaks read as spaces, asterisks not compared): each found exactly once.** Before writing each line,
   find its quoted passage in the record yourself and compare it the same way: every word and every punctuation mark
   must match, line breaks read as spaces. The line keeps its marks exactly as §3.2 gives them. A difference is a
   STOP-and-report for that line: no line written, listed in the report under *rows the act could not place* with both
   texts. **The record spells *"recognise"* (British spelling) in its §3.3 bullet; the quotation and the half name keep
   the record's spelling, as a quotation must** (the big dispatch's own text was changed to *"recognize"* at release,
   finding 57; the record was not, and the record governs).
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that part is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The record's §1 gives each §3.1 row a gloss in
   brackets, each §3.3 part its subject, and Row 24.1 its ground (*"the old dormancy of the function layer's use of the
   catalog"*). So the fit is: Row 38.80 (i), the recognition additive over the committed progression (the gloss: the
   matches read off L2's decided chords, changing none); Row 57.400, the recognize query returning the entries a span
   realizes (the gloss: for a stretch of decided chords, the entries it fits); Row 57.448, nothing produced where
   nothing is recognized; Row 57.455, the recognition run over the committed progression; Row 57.485, what the consumer
   produces additive over the function layer; Row 24.1, the function layer not touching the vocabulary until the
   recognition consumer is built; Row 24.2, the consumer making the catalog a prior and an annotation, the idioms
   weighting its entries; Row 57.445 (i), the analysis direction reading a progression to recognise or disambiguate it;
   Row 57.454, the consumer's inputs (the committed progression, the vocabulary filtered per §4.5, the weight vector);
   Row 57.470 (ii), the §4.3, §4.4 and §4.6 outputs emitted. A row that does not fit is a STOP-and-report for that
   row-part: no line, listed under *rows the act could not place* with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.32's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **The record names the
   word in full** for the nine ADOPTED lines (*"ADOPTED — proposed:"* before §3.1's five; *"ADOPTED — proposed"* after
   each of the four parts of §3.3 it places so), so item (1) of the paragraph gives **ADOPTED — proposed**. For the four
   RELOCATED lines and the HISTORICAL line the record names the word itself (*"RELOCATED to L2"*; *"HISTORICAL"*). **The
   writing side read the proposed paragraph at every one of the row-parts this stretch names: each is UNPLACED** (for
   the rows with claims, at the claim named: Rows 38.80 (i), 57.445 (i), 57.470 (ii); Row 57.470's claim (i) is proposed
   RELOCATED and gets nothing here). So no line's word is the row's own proposed word, and **no line says *as
   proposed***: the paragraph's *"Otherwise as proposed is not written, and the placement is given in the record's
   words"*. If you find a row-part's proposed word for the part named other than UNPLACED, that line is a
   STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of the 9 ADOPTED lines is listed in
   the report under *ADOPTED words read at the row*, with the proposed word read (UNPLACED) and that its line does not
   say *as proposed*.
6. **The HISTORICAL line.** The record places Row 24.1 HISTORICAL whole (*"§3.5, HISTORICAL (1): 24.1 (the old dormancy
   of the function layer's use of the catalog)."*). Row 24.1 states no claims, so the line names none.
7. **The split row-parts, by part.** The record's §3.3 bullet places each of its four row-parts in parts:
   - **Row 24.2 (no claims), three parts:** *"the prior RELOCATED to L2 with key Ruling 2's candidate, the annotation
     ADOPTED — proposed, the idiom weighting moved to the idiom-tag surface"*. Two lines: `Its part on the prior:` and
     `Its part on the annotation:`. The idiom weighting gets no line (§L.32's table: *"met at the idiom-tag records'
     entries"*).
   - **Row 57.445 (i), two parts:** *"to recognise ADOPTED — proposed, to disambiguate RELOCATED to L2 with the
     candidate"*. Two lines: `(i), its half "to recognise":` and `(i), its half "to disambiguate":`.
   - **Row 57.454 (no claims), two parts:** *"the decided chords and the catalog as inputs ADOPTED — proposed, the idiom
     filter and weight vector moved to the idiom-tag surface"*. One line:
     `Its half on the decided chords and the catalog as inputs:`. The idiom filter and weight vector get no line
     (§L.32's table, as for Row 24.2).
   - **Row 57.470 (ii), three parts:** *"the old §4.4 annotation ADOPTED — proposed, the old §4.3 evidence contribution
     RELOCATED to L2 with the candidate, the old §4.6 harmonic-sequence output RELOCATED to L2 with the sequence term at
     DP-O (D-504, D-505)"*. Three lines: `(ii), its part on the old §4.4 annotation:`,
     `(ii), its part on the old §4.3 evidence contribution:` and `(ii), its part on the old §4.6 harmonic-sequence output:`.
   The lines of one row-part are this record's all, on different parts, so form (b)'s two-record rule is not engaged
   between them.
8. **Rows named by more than one record** (form (b)'s two-record rule, by part). **No row this stretch writes carries an
   earlier record's line**: the writing side read all 10 at the staged copy and found no `*RULED ` or `*RECORDED ` line
   in any of them. §L.32's *Rows named by more than one record* names Row 38.77 ((ii) here, (i) at §L.12, (iii) named at
   §L.14 and not placed) and Row 38.79 ((ii) here, moved; (i) at §L.30); neither gets a line from this stretch (38.77
   (ii) is a §3.2 row-part, 38.79 (ii) the §3.6 move). List both in the report under *rows named by more than one
   record*, each with what §L.32 says of it. If you find an earlier record's line on any part this stretch writes, apply
   the rule by part as the big dispatch gives it; if an earlier stretch's line would have to be deleted or edited, STOP,
   do not commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several rows, `<claim>` is filled in from
the row list (written `(i)` as the list gives it); where the list gives no claim, `<claim>` and the space after it are
dropped.

**§L.32 — the catalog recognition part 2 record (`cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md`):
14 lines.**

*§3.1's ADOPTED rows — 5 lines, none* as proposed. Rows, in this order: 38.80, written `(i)`; 57.400; 57.448; 57.455;
57.485.
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed: 38.80 (i) (the matches read off L2's decided chords, changing none; their place L3's read-off — the writing side's reading of *"Layer 5"*); 57.400 (for a stretch of decided chords, the entries it fits); 57.448 (where no entry fits, no match is published); 57.455 (the matching runs over L2's decided chords); 57.485 (additive, as part 1's Rows 44.20 (ii) and 44.37 (i))".
```

*Row 24.1 — 1 line, HISTORICAL:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* **HISTORICAL** — "§3.5, HISTORICAL (1): 24.1 (the old dormancy of the function layer's use of the catalog)".
```

*§3.3's split row-parts — 8 lines, in the order in which the record names the parts.* Every one of the eight quotes the
same passage, written here once as `<Q>`:
`"§3.3, split by use (4): 24.2 — the prior RELOCATED to L2 with key Ruling 2's candidate, the annotation ADOPTED — proposed, the idiom weighting moved to the idiom-tag surface; 57.445 (i) — to recognise ADOPTED — proposed, to disambiguate RELOCATED to L2 with the candidate; 57.454 — the decided chords and the catalog as inputs ADOPTED — proposed, the idiom filter and weight vector moved to the idiom-tag surface; 57.470 (ii) — the old §4.4 annotation ADOPTED — proposed, the old §4.3 evidence contribution RELOCATED to L2 with the candidate, the old §4.6 harmonic-sequence output RELOCATED to L2 with the sequence term at DP-O (D-504, D-505)"`.
The eight lines, in this order, each with `<Q>` written out in full where it stands:
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* Its part on the prior: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* Its part on the annotation: **ADOPTED — proposed** — <Q>.
```
— those two at Row 24.2;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* (i), its half "to recognise": **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* (i), its half "to disambiguate": **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those two at Row 57.445;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* Its half on the decided chords and the catalog as inputs: **ADOPTED — proposed** — <Q>.
```
— that one at Row 57.454;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* (ii), its part on the old §4.4 annotation: **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* (ii), its part on the old §4.3 evidence contribution: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1).* (ii), its part on the old §4.6 harmonic-sequence output: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those three at Row 57.470. Each line ends with the closing quotation mark of `<Q>` followed by a period, as the lines
above it do. (Within each row, the lines stand as separate lines, each followed by a blank line, §3.1 item 2.)

**The count.** `*RULED DISPOSITION (`: **14** — 9 **ADOPTED — proposed**, 4 **RELOCATED**, 1 **HISTORICAL**. None
opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) each line quotes, as the record's
placement, the record's bullet whole, its bold lead's marks dropped as sessions 17 and 18 dropped them — §3.1's bullet
is the record's list of ADOPTED rows alone, as part 1's was; for Row 24.1, its one-row bullet; for the split row-parts,
§3.3's bullet whole, since its one sentence places every part of all four, as session 18 quoted part 1's §3.3 bullet
whole for each of its four half lines. The record's italic marks around its inner quotation *"Layer 5"* are kept
(`*"Layer 5"*`), as earlier stretches kept the record's own emphasis inside a quotation (for example the lines of the
cadence-features record), so that the inner quotation marks read as the record's; (2) each part is named in the
record's own words, after *"its half on"* where the record splits the row-part in two (Row 57.454) and *"its part on"*
where it splits it in three (Rows 24.2 and 57.470 (ii)), the shape of sessions 17 and 18's half lines; Row 57.445 (i)'s
two halves, which the record names by the verbs *"to recognise"* and *"to disambiguate"*, are named with the verb in
quotation marks (`its half "to recognise"`), on the shape of §10's existing entry `Row 46.46 (i), its "ranked" half`;
a row with no claims opens with *"Its"*, on the shape of an existing line, *"Its perfect/imperfect half:"* (the
cadence-type record's line at the reading file's line 1374); (3) within a row the lines follow the order in which the
record names the parts — for Row 24.2 the RELOCATED part first, as the record names *"the prior"* before *"the
annotation"*; (4) every RELOCATED line takes the destination ***L2 — The tonal reading. The one entangled decision.***,
the record saying *"RELOCATED to L2"* for each, in the form the earlier stretches' ruled RELOCATED lines use; what
travels with each (*"with key Ruling 2's candidate"*; *"with the candidate"*; *"with the sequence term at DP-O (D-504,
D-505)"*) stands inside `<Q>` and in the §10 entries (§3.3).

**What this stretch gives no line** (Task 3 (a)), as §L.32 names them:
- **The ten §3.2 row-parts — Rows 38.18 (i), 38.77 (ii), 38.78, 57.97, 57.393 (ii), 57.394, 57.435 (i), 57.435 (ii),
  57.467 (i) and 57.478:** *"No line from this record; listed in the report"*, as Ruling 2 of
  `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part2_sitting.md` rules it, in
  the form of that record's Ruling A, quoting the recognition part 2 surface's §3.2 sentence *"Each row's one
  disposition is written when what it waits for is settled."* (§L.32's table and its *Open* point (2)). Each is listed
  in the report under *rows given no line now*, with §L.32 and those words; each keeps its proposed UNPLACED.
- **The three §3.4 row-parts — Rows 38.80 (ii), 57.401 (i) and 57.490 (i):** *"No line from this record."* Not listed
  under *rows given no line now* (Task 3 (a): that name covers the row-parts a §L entry lists in the report, and §L.32
  does not list these).
- **Row 38.79 (ii) (§3.6):** *"No line from this record."* The record moves it to the catalog-and-pairwise-grammar
  surface; it is met at that record's entry. Not listed under *rows given no line now*.
- **The idiom parts of Rows 24.2 and 57.454** (§3.3): no line from this record; met at the idiom-tag records' entries.
  Not listed under *rows given no line now*.
- **Rows 44.20 (ii), 44.37 (i) and 8.94**, which the record names and does not place (its §3.1 gloss for 57.485; its
  §4): no line from this record, not touched.
- **The other claims of the rows this stretch writes** — Rows 38.80 (ii) (above), 57.445 (ii) and 57.470 (i) — get
  nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — four entries appended

- **Item 5: four RELOCATED parts, none of which §10 carries.** The writing side searched §10 (lines 79915–81007) for
  every row number of this stretch as a bare number with look-around. The one hit: Row 57.470 (i) (in the entry for
  *"Rows 57.465, 57.466 (i), …"*, line 80626) — **another claim** of the row, not a part this stretch relocates. Read
  **by claim**, as sessions 17 and 18 read item 5's *"a row §10 already carries is not appended again"* (the writing
  side's settlement, overrulable by the user). **The four entries, appended in the order §3.2 gives the parts, under
  `**To *L2 — The tonal reading. The one entangled decision.***`, directly after that heading's last entry** (the line
  opening `- Row 44.28 (ii), its half on the key motion as evidence of the local key —`, line 80645 at the writing
  side's staged copy, written by session 18) **and before the blank line that precedes
  `**To *the second axis — voice leading*.**`**; no blank line between them, as §10's own entries stand:
  ```
  - Row 24.2, its part on the prior — that the catalog is the function layer's multi-chord disambiguation prior. *(cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1; with key Ruling 2's candidate.)*
  - Row 57.445 (i), its half "to disambiguate" — that the analysis direction reads an existing progression to disambiguate it. *(cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1; with the candidate.)*
  - Row 57.470 (ii), its part on the old §4.3 evidence contribution — that the §4.3 output, the evidence contribution, is emitted. *(cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1; with the candidate.)*
  - Row 57.470 (ii), its part on the old §4.6 harmonic-sequence output — that the §4.6 output, the harmonic sequence, is emitted. *(cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md, Ruling 1; with the sequence term at DP-O (D-504, D-505).)*
  ```
  Each subject clause is the writing side's, in §10's entry form (*"<the row's subject in one clause>"*), from the row's
  own statement and claim; each parenthesis names the record and ruling and, after the semicolon, what travels with the
  part, in the record's words. Before appending each, search §10 with the Grep tool for its row number and claim; if
  §10 already carries that part, do not append it and report it. If the heading is not found exactly once, STOP and
  report before writing anything at §10.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 81008–83160) for
  every row number of the 10 rows found none. Run the same search with the Grep tool; if you find an entry for a
  row-part of this stretch, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.32 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.33 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 9 commit, as in sessions 11 to 18.
   Attribute it in the diff table to *"session 19's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.32
   only**, after sessions 10 to 18's §L.1 to §L.31. §L.33 to §L.55 are not applied, read or touched.
3. **A1, for three paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1218, 1219 and 1220 ARE landed**, with this file, in §5 act 1, as sessions 8 to 18 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the record this stretch
   enters (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The
   writing side's search: **none of the three, in either search** (as §L.32's *The act's search* says). Item 2: not
   reached. Item 3: not reached. Item 4: not reached. **Item 5: four entries appended (§3.3).** Item 6: nothing written
   (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 9 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before the entry is applied, do not commit; STOP and report
   which lines were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 9 commit:**
     `git diff 51543b657ed1d3777f25812abede359615816369 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session19_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; a §10 entry of §3.3; the in-progress line of §3.5 item 3; and a NOT
     QUARANTINED line only if §3.4 (b) found an entry. Then
     `git diff --numstat 51543b657ed1d3777f25812abede359615816369 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 33 added lines and 1 deleted line** (the 14 lines and their 14 blank lines, 28; the four §10
     entries, 4; the in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2
     that was STOP-and-report, less 1 added for each §10 entry not appended**, plus 1 added for each NOT QUARANTINED line
     §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,079 added lines and 4 deleted lines** (`1079` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 18 the file stood at 1,047 added and 4 deleted against the Task 2
     commit (session 18's report, its diff table, as read by the sitting booted on entry 1217 [relayed: not re-run
     here]); this stretch adds 32 lines. The in-progress line replaces a line that is itself an addition against the
     Task 2 commit, so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **452** (438 + 14, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting` **18** (the 14 lines and the four §10 entries;
     less 1 for each line that was STOP-and-report or §10 entry not appended, plus 1 for a NOT QUARANTINED line naming
     it), `cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting` **13** (unchanged),
     `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting` **23** (unchanged).
   - **Then, if every line of §3.2 and all four §10 entries were written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`9bc1717744a690b557bc33f16ce6c18df095b0c4`** — the blob of the writing side's simulated edit (§8 below: 5,297,185
     bytes, 84,518 lines, line feeds only). A different blob with every count above as given means a byte differs
     somewhere in what was written: do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 10 (§L.32): the 14 lines of the catalog recognition's part 2 row-parts written in the reading file under their ratification, four RELOCATED parts appended to the transfer list, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_19_task_3_stretch_10_2026_11_24.md`**, as sessions 2 to 18
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.33, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's four files first, in a commit of their own, before any edit to the reading file.**
   Exactly four paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_19_task_3_stretch_10_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eighteen.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_nineteen.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1218, 1219 and 1220 and the session 19 instruction of the L3 application landed; Task 3 stretch 10 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: §L.32, for each row-part (and
   each part), the row check of §3.1 item 4 and the word check of §3.1 item 5, then its line of §3.2; then the §10
   entries of §3.3 and the search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_19_task_3_stretch_10_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 19 of the L3 application, Task 3 stretch 10 (§L.32) written; stretch 11 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 14 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 24.2, 57.445 and 57.470 and as one sentence for
   the other seven if they were as stated; the four §10 entries of §3.3, each appended (with its line number) or not
   (and why), and the §10 search; the §11 search of §3.4.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (the ten §3.2 row-parts, each with §L.32 and the words that list it); *recorded lines not written:
   no disposition word* (none expected); *rows named by more than one record* (Rows 38.77 and 38.79, as §3.1 item 8
   says); *ADOPTED words read at the row* (all 9 ADOPTED lines, each with the proposed word read and that its line does
   not say *as proposed*); *audit questions added* (none); *audit questions no longer quarantined* (none expected); *§10
   rows a record says leave, not named by row* (none: the record does not say a row leaves §10); the decided-against
   search (§4 item 4), with its result.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph, each with §L.32.
   *A heading of this session's report only, as in sessions 10 to 18's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 19 of the L3 application ends here. Stretch 11 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a line of §3.2
  that is STOP-and-report under them or under §3.1 items 2 to 8 is reported and the rest of this stretch applied, as
  they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 8);
- the §10 heading of §3.3 is not found exactly once (§3.3);
- §4 item 8's checks find a changed passage they cannot attribute, a count other than the ones they give, or a blob
  other than the one they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

## 8. Provenance

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1218. Read at the objects for this file, over staged
copies: the three git reference files (both refs `f1e7c914…`); entries 1218, 1217 and 1216 whole and 1026 §3; session
18's instruction whole (blob `6cc7f8be…`, 49,121 bytes, 527 lines); session 18's report at its §1 and §2 and by search
(its numstat table: `25 1` against the stretch 8 commit and `1047 4` against the Task 2 commit); the record whole (blob
`95b0ac7bf07a8d5df9a0734b416b5ed1e4e1be61`, 8,008 bytes, 101 lines by `wc -l`, no carriage return); the big dispatch at
lines 3344–3453 (§L.32 and §L.33's heading) and 6616–6695 (Task 3 (a) to (c) item 4), its blob recomputed on the staged
copy (`b5274c2c…`, 941,330 bytes, 7,157 lines); the list-answers part 2 record at lines 25–40 and 80–95 (Ruling A and
Ruling 2) and the recognition part 2 surface at lines 109–112 (its §3.2 sentence at line 111). The reading file, by
read-only scripts over the staged copy: its blob computed as git would (`27e0d551…`, 5,286,365 bytes, 84,486 lines, no
carriage return; equal to the blob session 18's report gives for the stretch 9 commit); its `##` headings; each of the
10 rows found exactly once by its heading, inside §6, and read whole from its heading to its closing `---`, its shape,
its proposed word for the part named and its outgoing statement as §3.1 items 2, 4 and 5 state; the headings of the ten
§3.2 rows, the three §3.4 rows and Row 38.79 found exactly once each, inside §6 (not read; Rows 38.77 and 38.79 searched only
for their proposed and ruled lines); the 16 existing ruled lines that stand beneath a proposed paragraph or an earlier ruled
line and above an *At the source now.* paragraph, counted by script; §10's destination headings, the L2 heading at line
80117 and the next heading at 80647, the end of the L2 block at lines 80622–80647; §10 and §11 searched for every row
number of the 10 rows as a bare number with look-around (one §10 hit, Row 57.470 (i) at line 80626, read; no §11 hit);
the counts §1 check 4 gives; line 54 in full. Every quotation of §3.2, every part name and every travelling phrase
checked against the record by a read-only script (line breaks joined, asterisks removed): each quotation found exactly
once. The record searched for the three decided-against phrases (line breaks joined, case matched and not): none. **The
edit simulated on a copy of the reading file in the container** by §3.1 item 2's placement rule, §3.3's placement and
§3.5 item 3's line gives, against the staged file, **33 added lines and 1 deleted**, the counts **452 / 3 / 53 / 26 / 1 /
1**, the record names **18** (part 2), **13** (part 1) and **23** (lead rows), and the blob **`9bc17177…`** (5,297,185
bytes, 84,518 lines); each new line's place in the copy read back at Rows 57.400, 57.470 and 24.2 and at §10. Relayed,
not re-checked here: the archive JSON's blob `1df4f207…` and the untracked paths (session 18's report, §1 item 5); the
Task 2 commit `4b6dc3bd…` (the same text session 18's instruction gives for the same object); the stretch 9 commit
`51543b65…` as session 18's act 2 (entry 1218 §2, checked there at the objects); the end of `cowork_handoff.md`'s
topmost block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session
18's instruction gives them); the 1,047 added and 4 deleted lines against the Task 2 commit after session 18 (session
18's report, not re-run).*

*Check note — checked as a turn of its own, Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1219, a sitting
that did not write this file. Read at the objects, over staged copies, with the file tools and read-only container
searches (`grep`, `sed -n`, `awk`, `wc`, `cut`, `tr`, `diff`): the three git reference files (both refs `f1e7c914…`);
this file whole as landed (49,209 bytes, 525 lines, no carriage return); the record whole (8,008 bytes, 101 lines by
`wc -l`), every quotation of §3.2, every part name and every travelling phrase compared with it, each found; the
decided-against search over the record (none of the three, case matched or not); each of the 10 rows found exactly once
by its heading and read whole from its heading to its closing `---`: its shape, no earlier ruled or recorded line, its
proposed word for the part named (UNPLACED at each) and its fit with the record as §3.1 items 2, 4 and 5 state; the
reading file's `##` headings at the lines §2 item 9 gives, its size and lines (5,286,365 bytes, 84,486) and the nine
counts of §1 check 4; line 54 in full; the 16 ruled lines above an *At the source now.* paragraph, counted; §10's L2
heading found exactly once at line 80117, the end of its block at lines 80596–80647, the next heading at 80647; §10 and
§11 searched for the 10 rows' numbers with look-around (one §10 hit, Row 57.470 (i) at line 80626, another claim; no
§11 hit); the big dispatch's size and lines (941,330 bytes, 7,157), its headings at the lines §2 item 8 gives, its
§L.32 whole (lines 3344–3449) and its form (b) (lines 159–274); the list-answers part 2 record at lines 25–94 (Ruling A
at its heading, line 9, and Ruling 2) and the surface's §3.2 sentence at line 111; Ruling 9's *"placed from"* sentence
at its record's line 403; the precedents §3.2's settlements cite (the RELOCATED form at lines 1303, 4875, 4896; session
17's and 18's half lines; the bold kept inside the cadence-features record's quotations at line 1331 and others; line
1374); `cowork_handoff.md`'s topmost block ending at line 255 and `cowork_audit_protocol.md`'s dispatch-protocol section
opening at line 180; the full hashes in this file, each one of the objects named. **The size of the edit computed from
this file's own text** (the 14 lines with `<claim>` and `<Q>` filled in, their 14 blank lines, the four §10 entries,
and the in-progress line against line 54): **10,820 bytes added, 32 lines**, so 5,297,185 bytes and 84,518 lines, as
the simulation above gives. **Not re-derived by this check, declared (the user's word "1"):** the blob `9bc17177…`,
the record's blob `95b0ac7b…` and the reading file's blob `27e0d551…` — the session's permission check refused every
container command that computes a git blob, and the edit was not re-simulated on a copy. §1 check 4 and §4 item 8 stop
before any edit or commit if either reading-file blob differs. **Corrected:** handoff entry 1220 added to what act 1
lands (§1 item 5, §4 item 3, §5 act 1 and its subject), as entry 1219 §3 step 1 asked; the banner. No line of §3.2,
row, disposition word, command or count the reading file is checked against changed; what changed is the number of
files act 1 lands (three to four), A1's paths in §4 item 3 (two to three), and act 1's commit subject.*
