# CC dispatch — the L3 application, SESSION 22 of several: Task 3 of the L3 application dispatch, thirteenth stretch (§L.36), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_five.md`, a writing session that did
> not verify a stretch: the sitting booted on entry 1224 verified session 21's stretch and, on the user's word "B",
> handed the writing of §L.36 to a new session. CHECKED AS A TURN OF ITS OWN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_six.md` (its check note closes §8),
> and released with that check.**
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
called **the Task 2 commit** below). Sessions 10 to 20 applied Task 3's first eleven stretches, §L.1 to §L.34. Session 21
applied the twelfth stretch, §L.35, in commit `b3cec9999366ec330d2c7016f83115202cf8fe54` (called **the stretch 12
commit** below), and committed its report as `ad8f3ddda9a5b606e702433a7addd9e937fd8d5f`, the current tip.

**This is session 22. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry: §L.36, the record of family 1's
idiom-tags surface, part 1. It commits that thirteenth stretch as ONE commit, pushes it, writes its report, and
STOPS.** §L.37 is a later session's.

**Why the stretch covers one entry and stops at §L.37** (the user's ruling of 2026-11-24: a writing session judges how
many ledger entries fit). §L.36 alone gives 23 lines on 16 rows, six of those rows carrying two or three lines each in
the forms (b) and (b-H), with RELOCATED parts among them, and five entries for the transfer list. §L.37's entry runs
about 100 lines of the big dispatch and places 21 further row-parts of another record. The sitting that wrote this file
judged that adding it would leave too little margin to write it and re-run the simulation cleanly, and the stretch
stops at the boundary before it.

**What this stretch writes, in one paragraph.** **23 lines, all opening `*RULED DISPOSITION (`, on 16 rows**, from
`cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md`, Ruling 1 (the record's one ruling): **12 with the
word ADOPTED — proposed** (the nine rows of the record's *§3.1, follow wholly (9)* bullet, and one part each of Rows
46.44 (i), 38.22 (ii) and 38.79 (i)'s remainder); **6 with the word HISTORICAL** (one part each of Rows 46.44 (i),
38.22 (ii), 46.43, 38.79 (i)'s remainder, 24.2 and 57.454); and **5 with the word RELOCATED**, each to ***L2 — The
tonal reading. The one entangled decision.*** (one part each of Rows 38.22 (ii), 46.43, 24.2, 57.454 and 57.118). The
two lines of Row 46.43 are the text Ruling 15 of the release part 2 record gives, byte for byte. **No line says *as
proposed*:** every row-part named is proposed UNPLACED at its row. §3.2 gives every line with its exact text. **Five
entries appended to the transfer list, §10,** under its heading *To L2 — The tonal reading. The one entangled decision.*,
one for each RELOCATED part (§3.3). **Nothing at §11** (§3.4). And the in-progress line brought forward from §L.35 to
§L.36 (§3.5). **The nine rows of the record's §3.2 get no line** and are listed in the report under *rows given no line
now* (§3.2's last paragraph).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only.** This session copies into the reading file the placements the record already makes; it decides
nothing and changes no algorithm. The record states *"Documentation only. Algorithm: no change."* It orders no
amendment of the successor, the charter or the interface contract that belongs to Task 3 (§L.36, *Successor*,
*Charter*, *Interface contract*). The record's §2 carries the user's thought on labels, *"not a ruling"*, and two
writing-side readings, *"not decided"*; this session writes nothing from them.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `ad8f3ddda9a5b606e702433a7addd9e937fd8d5f`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_22_task_3_stretch_13_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 12 commit left it.**
   `git diff --quiet b3cec9999366ec330d2c7016f83115202cf8fe54 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree ad8f3ddda9a5b606e702433a7addd9e937fd8d5f -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `3343d6f34c0ac1f9bc82c6b2d3286239add0096f`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **468**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting` must count
   **7**; and `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting` must count **0**. Any other result: STOP
   and report, the file not touched. (The writing side's staged copy: 5,305,690 bytes, 84,551 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree ad8f3ddda9a5b606e702433a7addd9e937fd8d5f -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the four files §5 act 1 lands (this instruction and handoff entries 1225, 1226 and
     1227), plus the paths sessions 2 to 21 reported and
     did not land (387 under `scratch_artifacts/`; `Claude outputs/`; `Codex research inventory/`;
     `docs/research_papers/polyph9-release/`; the two PDFs under `external resarch summary/`;
     `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; and
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_six.md` (written by the sitting
   that wrote this file) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_seven.md` (written by the sitting
   that checked it); both untracked, §5 act 1 lands them.
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The one record this stretch rests on, WHOLE** — it is the authority for every line this session writes (**the
   record's own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md` (§L.36; 9,010 bytes, 116
   lines by `wc -l`).
8. **Two rulings of the release records, at these lines only, with the Read tool:**
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`, lines 700–740 (Ruling 15:
   Row 46.43's two lines); and
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md`, lines 231–236 (Ruling 5:
   the rows that take *"no line now"*).

   **Do NOT read the records of §L.1 to §L.35 or of §L.37 to §L.55, and do not open the record's surface** (the lines
   quote the record only).
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, its two-record rule by part, and form (b-H)**, the premise ledger, the declared start state,
     the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 3754–3887 (§L.36, your stretch)**;
   - lines 6616–6820 (Task 3, whole, **with (c) items 1 and 5, the decided-against search and the transfer list**);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3753 (§L.1 to §L.35, applied); lines 3888–5906 (§L.37 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 16 rows §3.2 names, whole, at §6** (lines 435–79516): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
      heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
    - §10 (lines 79975–81072): searched with the Grep tool for every row number of this stretch (§3.3), and **read from
      the last entries under its heading *To L2 — The tonal reading. The one entangled decision.* (from line 80700) to
      the next heading (line 80711)**;
    - §11 (lines 81073–83225), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch for the ADOPTED and RELOCATED lines, form (b-H) for the HISTORICAL lines:
   one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*` paragraph and every other sentence of the row
   untouched. Every line names its record's file and Ruling 1 (the record has one ruling), the record file written as
   its bare file name, as sessions 10 to 21 wrote theirs. Where §3.2 names a claim, the line names it (form (b)'s
   split-row rule). Where a record places several parts of one row-part, **each part placed gets exactly one line**,
   naming its part as §3.2 gives it; a part given no line is named in §3.2's last paragraph.
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"At the
   source now."*). Each new line is followed by one blank line. Where one row gets several lines, they go in the order
   §3.2 gives them. Read each row's actual shape from its proposed paragraph to its end before writing. **The writing
   side read all 16 rows at the staged copy; every one ends with a blank line and then `---`.** Their shapes after the
   proposed paragraph:
   - **no earlier line, and nothing between the proposed paragraph and `---`; the new lines go after the blank line
     that follows the proposed paragraph, before `---`:** Rows 46.38, 46.40, 46.49, 44.32, 46.45, 46.44, 38.22 and
     46.43;
   - **no earlier line, and a paragraph headed *"At the source now."* directly after the proposed paragraph; the new
     line goes directly beneath the proposed paragraph, above it:** Rows 57.516, 57.517, 57.532 and 57.535. Row 57.535's
     *At the source now.* is followed by the group's sections (*The arithmetic at this group* and the rest) before its
     closing `---`; they are not touched;
   - **earlier ruled lines, and nothing after them but `---`; the new lines go after the last earlier line and its blank
     line, before `---`:** Row 38.79 (one line, from `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md`) and
     Row 24.2 (two lines, from `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md`);
   - **one earlier ruled line, then *"At the source now."*; the new lines go beneath the earlier line, above *At the
     source now.*:** Row 57.454 (from the recognition part 2 record) and Row 57.118 (from
     `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md`, written by session 21).

   If you find a different shape at a row (an earlier line not listed here, a further paragraph, or an ending other
   than `---`), state it in the report and place the lines by the rule in bold above; if the rule does not settle where
   they go, that row's lines are a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it:
   - for the nine §3.1 rows, the record's *§3.1, follow wholly (9)* bullet whole (its lines 36–38), its bold lead
     included as words and its marks dropped, and its closing period dropped (the line's own period follows the closing
     quotation mark), as session 21 wrote its ADOPTED bullet;
   - for the split rows of the record's §3.3 and Row 57.118 of its §3.4, **the row's own item of the bullet**, from the
     row number to the item's closing semicolon or period, both dropped (the bullet's items are separated by
     semicolons; the record's lines 43–52);
   - for Row 46.43, the two lines Ruling 15 of the release part 2 record gives (its record lines 727 and 729), byte for
     byte, which quote the record's item for Row 46.43 and its words for Row 38.22 (ii)'s parts;
   - Row 38.22 (ii)'s selection line adds, after its item, the two quotations Ruling 15 gives Row 46.43's selection
     line: *"selection decided against as above"*, that is, *"decided against in so far as it selects the catalog L3
     reads"* (the second is the record's words for Row 46.44 (i), the place *"as above"* points to).

   **The writing side checked every quotation against its record by a read-only script (words and punctuation, line
   breaks read as spaces, asterisks not compared): each quoted passage found in the record; the seven items and the
   bullet exactly once each; *"decided against in so far as it selects the catalog L3 reads"* twice, at Rows 46.44 (i)
   and 57.454's items, as expected.** Before writing each line, find its quoted passages in the record yourself and
   compare them the same way: every word and every punctuation mark must match, line breaks read as spaces. The line
   keeps its marks exactly as §3.2 gives them. A difference is a STOP-and-report for that line: no line written, listed
   in the report under *rows the act could not place* with both texts. The record writes *"behaviour"*, British
   spelling, in its item for Row 46.43; the quotation keeps the record's spelling.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that claim is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The fit, row by row:
   - Rows 46.38, 46.40, 46.49, 57.516, 57.517 and 57.532, and the claims 44.32 (i) and 57.535 (i): the catalog's
     entries carrying idiom tags, multi-valued (the record's *"as content of the catalog L3 reads"*);
   - Row 46.45: one catalog, a shared convention a single entry (the record's *"one catalog, a shared convention a
     single entry"*);
   - Row 46.44 (i): the catalog carrying the style label, and the preset selecting the active subset (the record's
     *"the label"* and *"the preset selecting the active subset"*);
   - Row 38.22 (ii): the genre labels in the component, the genre-aware behavior — selection, weights, detection — at
     the consumer (the record's *"the labels"*, *"selection"*, *"weights"* and *"detection"*);
   - Row 46.43: style behavior the consumer's (the record's *"travels with 38.22 (ii)'s behaviour half"*);
   - Row 38.79 (i): the catalog finite and idiom-specific, the preset selecting it (the record's *"a catalog per idiom"*
     and *"entries specific to idioms"*; the preset's part is placed at §L.30 by the line already standing);
   - Row 24.2: the §6.7 idioms first doing work in the consumer, by weighting which entries count (the record's *"the
     weighting as evidence"* and *"a weight deciding which matches L3 publishes"*);
   - Row 57.454: the consumer reading the catalog *"queried, filtered per §4.5"* and the idiom-mixture weight vector (the
     record's *"the filter"* and *"the weight vector"*);
   - Row 57.118: each substitution carrying its style weights (the record's *"57.118's style weights"*).

   A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act could not place*
   with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.36's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **The record names the
   word in full** for every part it places ADOPTED (*"ADOPTED — proposed, as content of the catalog L3 reads"*, its line
   36; *"the label ADOPTED — proposed"*, *"the labels ADOPTED — proposed"* and *"entries specific to idioms ADOPTED —
   proposed as their tags"*, its lines 43–47), so item (1) of the paragraph gives **ADOPTED — proposed** for all twelve
   ADOPTED lines. The HISTORICAL lines are form (b-H) (the record decides against those parts) and the RELOCATED lines
   take the record's word. **The writing side read the proposed paragraph at every row this stretch names: at the
   claim or row named, each is UNPLACED** (Row 46.44 (i), Row 38.22 (ii), Row 38.79 (i), Row 44.32 (i), Row 57.535 (i),
   and the eleven rows without claims). So no line's word is the row's own proposed word, and **no line says *as
   proposed***: the paragraph's *"Otherwise as proposed is not written, and the placement is given in the record's
   words"*. If you find a row-part's proposed word for the claim named other than UNPLACED, that row's lines are a
   STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of the 12 ADOPTED lines is listed in
   the report under *ADOPTED words read at the row*, with the proposed word read (UNPLACED) and that its line does not
   say *as proposed*.
6. **The split rows and their parts.** The record's §3.3 splits six row-parts by subject and its §3.4 places one part of
   Row 57.118; each part placed gets one line, named in §3.2:
   - **Row 46.44 (i):** the label (ADOPTED — proposed) and the preset selecting the active subset (HISTORICAL). Claims
     (ii) and (iii) of the row are not named by the record and get nothing.
   - **Row 38.22 (ii):** the labels (ADOPTED — proposed), selection (HISTORICAL) and the weights (RELOCATED). The
     detection part, *"waiting on the open question the L2 tail-style-and-idiom record §1 holds"*, gets no line (§L.36's
     table).
   - **Row 46.43:** selection (HISTORICAL) and the weights (RELOCATED), the two lines of Ruling 15; *"No line for the
     detection part"* (Ruling 15).
   - **Row 38.79 (i)'s remainder:** a catalog per idiom (HISTORICAL) and the entries specific to idioms (ADOPTED —
     proposed). The other part of claim (i), the preset selecting the catalog, carries §L.30's line already.
   - **Row 24.2's idiom part:** the weighting as evidence (RELOCATED) and a weight deciding which matches L3 publishes
     (HISTORICAL). The row's other parts carry §L.32's two lines already.
   - **Row 57.454's idiom part:** the filter (HISTORICAL) and the weight vector (RELOCATED). The row's other half carries
     §L.32's line already.
   - **Row 57.118's style weights:** RELOCATED. Its voice-leading portion carries §L.35's line already (session 21).
7. **Rows named by more than one record** (form (b)'s two-record rule, by part: *"lines on different parts are each
   written"*). **Four rows this stretch writes carry an earlier record's line, each on another part**: Row 38.79 ((i),
   the preset's part, HISTORICAL, §L.30); Row 24.2 (the prior, RELOCATED, and the annotation, ADOPTED — proposed,
   §L.32); Row 57.454 (the decided chords and the catalog as inputs, ADOPTED — proposed, §L.32); Row 57.118 (the
   voice-leading implications, RELOCATED, §L.35). In each, the part this stretch writes is one the earlier line does not
   place: the earlier line of Row 38.79 says of its claim *"the remainder ("idiom-specific") going with the idiom-tag
   rows"*, and those of Rows 24.2 and 57.454 say *"the idiom weighting moved to the idiom-tag surface"* and *"the idiom
   filter and weight vector moved to the idiom-tag surface"*, and session 21's line on Row 57.118 places the
   voice-leading implications only. So no two lines fall on the same part, and every line of §3.2 is written. The
   earlier lines are not touched. Further rows §L.36 names as reached by another record: Rows 46.45, 38.22 (ii) and
   46.43 (named as moved here at §L.30 and §L.31, which gave them no line; the writing side found no `*RULED ` or
   `*RECORDED ` line at any of the three) and Row 57.399 (its other part placed at §L.33; given no line here). List all
   eight in the report under *rows named by more than one record*, each with what §L.36 says of it. If you find an
   earlier record's line on a part this stretch writes, apply the rule by part as the big dispatch gives it; if an
   earlier stretch's line would have to be deleted or edited, STOP, do not commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written, in the order it goes at its row. Where a block serves several
rows, `<claim>` is filled in from the row list (written `(i)` as the list gives it); where the list gives no claim,
`<claim>` and the space after it are dropped.

**§L.36 — the idiom-tags part 1 record (`cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md`): 23
lines.**

*The §3.1 rows — 9 lines, none* as proposed. Rows, in this order: 46.38; 46.40; 46.49; 44.32, written `(i)`; 57.516;
57.517; 57.532; 57.535, written `(i)`; 46.45.
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — "§3.1, follow wholly (9): ADOPTED — proposed, as content of the catalog L3 reads: 46.38, 46.40, 46.49, 44.32 (i), 57.516, 57.517, 57.532, 57.535 (i), 46.45 (one catalog, a shared convention a single entry — the writing side's derivation)".
```

*Row 46.44 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (i), its part on the label: **ADOPTED — proposed** — "46.44 (i) — the label ADOPTED — proposed, the preset selecting the active subset decided against in so far as it selects the catalog L3 reads".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (i), its part on the preset selecting the active subset: **HISTORICAL** — "46.44 (i) — the label ADOPTED — proposed, the preset selecting the active subset decided against in so far as it selects the catalog L3 reads".
```

*Row 38.22 — 3 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (ii) (labels) **ADOPTED — proposed** — "38.22 (ii) — the labels ADOPTED — proposed, selection decided against as above, weights RELOCATED to L2 with key Ruling 2's candidate, detection waiting on the open question the L2 tail-style-and-idiom record §1 holds".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (ii) (selection) **HISTORICAL** — "38.22 (ii) — the labels ADOPTED — proposed, selection decided against as above, weights RELOCATED to L2 with key Ruling 2's candidate, detection waiting on the open question the L2 tail-style-and-idiom record §1 holds"; "selection decided against as above", that is, "decided against in so far as it selects the catalog L3 reads".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (ii) (weights) **RELOCATED** — to ***L2 — The tonal reading. The one entangled decision.***: "38.22 (ii) — the labels ADOPTED — proposed, selection decided against as above, weights RELOCATED to L2 with key Ruling 2's candidate, detection waiting on the open question the L2 tail-style-and-idiom record §1 holds".
```

*Row 46.43 — 2 lines, in this order, exactly as Ruling 15 of the release part 2 record gives them:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (selection) **HISTORICAL** — "46.43 — travels with 38.22 (ii)'s behaviour half"; as there, "selection decided against as above", that is, "decided against in so far as it selects the catalog L3 reads".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (weights) **RELOCATED** — to ***L2 — The tonal reading. The one entangled decision.***: "46.43 — travels with 38.22 (ii)'s behaviour half"; as there, "weights RELOCATED to L2 with key Ruling 2's candidate".
```

*Row 38.79 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (i), its remainder's part on a catalog per idiom: **HISTORICAL** — "38.79 (i)'s remainder — a catalog per idiom decided against, entries specific to idioms ADOPTED — proposed as their tags".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (i), its remainder's part on the entries specific to idioms: **ADOPTED — proposed** — "38.79 (i)'s remainder — a catalog per idiom decided against, entries specific to idioms ADOPTED — proposed as their tags".
```

*Row 24.2 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* Its idiom part, on the weighting as evidence: **RELOCATED** — to ***L2 — The tonal reading. The one entangled decision.***: "24.2's idiom part — the weighting as evidence RELOCATED to L2 with the candidate, a weight deciding which matches L3 publishes decided against".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* Its idiom part, on a weight deciding which matches L3 publishes: **HISTORICAL** — "24.2's idiom part — the weighting as evidence RELOCATED to L2 with the candidate, a weight deciding which matches L3 publishes decided against".
```

*Row 57.454 — 2 lines, in this order:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* Its idiom part, on the filter: **HISTORICAL** — "57.454's idiom part — the filter decided against in so far as it selects the catalog L3 reads, the weight vector RELOCATED to L2 with the candidate".
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* Its idiom part, on the weight vector: **RELOCATED** — to ***L2 — The tonal reading. The one entangled decision.***: "57.454's idiom part — the filter decided against in so far as it selects the catalog L3 reads, the weight vector RELOCATED to L2 with the candidate".
```

*Row 57.118 — 1 line:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* Its part on the style weights: **RELOCATED** — to ***L2 — The tonal reading. The one entangled decision.***: "57.118's style weights RELOCATED to L2 with the candidate".
```

**The count.** `*RULED DISPOSITION (`: **23** — 12 **ADOPTED — proposed**, 6 **HISTORICAL**, 5 **RELOCATED**; all 23
naming the idiom-tags part 1 record. None opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) the nine §3.1 lines quote the record's
*§3.1, follow wholly (9)* bullet whole, its bold lead's marks and its closing period dropped, as session 21 did with its
ADOPTED bullet; (2) every §3.3 and §3.4 line quotes the row's own item of the bullet rather than the whole bullet, as
Ruling 15 quotes Row 46.43's item (session 19 quoted the recognition part 2 record's whole §3.3 bullet on Rows 24.2 and
57.454; that record's bullet is not this one); (3) the parts are named in the shapes the rows already carry: Row 38.22
(ii) in Ruling 15's shape for the same three placements (*(selection)*, *(weights)*, and so *(labels)*), Rows 24.2 and
57.454 in session 19's shape (*Its part on …:*, *Its half on …:*) with the record's own *"idiom part"*, Row 57.118 in
that shape too, and the claims of Rows 46.44 (i) and 38.79 (i) as *(i), its part on …:*, the part named in the
record's words; (4) the RELOCATED lines follow Ruling 15's shape, `**RELOCATED** — to ***<charter>***: "<quotation>"`;
(5) Row 38.22 (ii)'s selection line adds Ruling 15's two quotations for the selection after the item, for the reason
§3.1 item 3 gives. Row 46.43's two lines are not the writing side's: they are Ruling 15's text, reproduced byte for byte
(the writing side compared the big dispatch's §L.36 table line with the record's lines 727 and 729 by script: equal).

**What this stretch gives no line** (Task 3 (a)), as §L.36 names them:
- **The nine rows of the record's §3.2 — Rows 44.11, 57.535 (ii), 57.518, 57.533, 57.519, 57.520, 57.521, 57.522 and
  57.523:** *"No line now"* for the part that follows and the part that waits, as Ruling 5 of
  `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md` rules it (its record lines
  233–236): each *"keeps its proposed UNPLACED until what it waits for is settled"* (for these rows, the catalog's final
  content) and *"is listed in Claude Code's report"* (§L.36's table and its *Open* point (2)). Each is listed in the
  report under *rows given no line now*, with §L.36 and those words. Row 57.535 (i) gets its line above; claim (ii) of
  the same row gets none.
- **Row 38.22 (ii)'s detection part and Row 46.43's detection part:** no line (§L.36's table; Ruling 15's *"No line for
  the detection part"*); each keeps its proposed UNPLACED. Not listed under *rows given no line now*.
- **Row 57.399's listing of entries by style:** *"No line from this record"* (§L.36's table; the record: *"57.399's
  listing of entries by style waiting on the presentation decision"*). Not listed under *rows given no line now*.
- **Rows the record names and does not place:** Rows 46.47 and 46.48 (its §2), Rows 38.79 (ii) and 57.396 (ii), and
  the second parts of Rows 57.107 (ii) and 57.433 (ii) (its §3). No line from this record, not touched.
- **The other claims of the rows this stretch writes** — Rows 46.44 (ii) and (iii), Row 38.22 (i), Row 44.32 (ii),
  Row 38.79 (ii) — get nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — FIVE entries appended

- **Item 5:** five parts are placed RELOCATED, out of UNPLACED, to ***L2 — The tonal reading. The one entangled
  decision.*** §10 has that heading, *"**To *L2 — The tonal reading. The one entangled decision.***"*, at line 80177 of
  the file as it stands now, its entries running to line 80709 and the next heading, *To the second axis — voice
  leading*, at line 80711. None of the five parts is listed in §10: the writing side searched §10 (lines 79975–81072)
  for the row number of every row-part the record places or names (46.38, 46.40, 46.49, 44.32, 57.516, 57.517, 57.532,
  57.535, 46.45, 46.44, 38.22, 46.43, 38.79, 24.2, 57.454, 57.118, 44.11, 57.518, 57.519, 57.520, 57.521, 57.522, 57.523,
  57.533, 57.399, 46.47, 46.48, 57.396, 57.107 and 57.433) as a bare number with look-around. **Six hits, on five lines, none the
  part this stretch writes:** line 80589 (Row 44.32 (ii), another claim); line 80624 (Rows 46.44 (ii) and 46.47, another
  claim and a row the record does not place); line 80684 (Row 57.396 (i), another claim); line 80706 (Row 24.2, its part
  on the prior, another part); line 80791 (Row 57.118, its part on the voice-leading implications, another part).
  **Item 5's *"a row §10 already carries is not appended again"* is read by row-part**, as its own first sentence
  states the population (*"Every row-part a §L entry places RELOCATED, out of UNPLACED or against its proposal, that §10
  does not already carry"*) and as session 19 applied it, appending two entries for two parts of Row 57.470 (ii) under
  one heading (lines 80708 and 80709). So the hits at lines 80706 and 80791 do not stop the entries for Rows 24.2 and 57.118, and this is not a difference from the big dispatch under
  §0. So item 5 appends FIVE entries, in §10's own entry form and in ledger order, **directly after the last entry under that
  heading** (the entry for Row 57.470 (ii)'s part on the old §4.6 harmonic-sequence output, now at line 80709) and
  **before the blank line that precedes the next heading** — no blank line added, as §10's entries under one heading
  stand on consecutive lines. The entries, exactly, in this order:
  ```
  - Row 38.22 (ii), its part on the weights — that the genre-aware weights are the consumer's. *(cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1; with key Ruling 2's candidate.)*
  - Row 46.43, its part on the weights — that style behavior, in its weights, is the consumer's. *(cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1; travelling with Row 38.22 (ii)'s weights, with key Ruling 2's candidate.)*
  - Row 24.2, its idiom part on the weighting as evidence — that the idioms first do work by weighting which entries count. *(cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1; with the candidate.)*
  - Row 57.454, its idiom part on the weight vector — that the consumer consumes the idiom-mixture weight vector. *(cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1; with the candidate.)*
  - Row 57.118, its part on the style weights — that each substitution carries its style weights. *(cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1; with the candidate.)*
  ```
  *The writing side's wording, overrulable by the user:* each clause is the row's own outgoing statement or one-claim
  reading at §6, cut to the part placed; the part is named on the shape of the entries session 19 and session 21
  appended (*"Row 24.2, its part on the prior — …"*, *"Row 57.118, its part on the voice-leading implications — …"*);
  the parenthesis names the record and ruling and what travels with the part in the record's own words (*"with key
  Ruling 2's candidate"* for Row 38.22 (ii)'s weights, *"with the candidate"* for the others; Row 46.43's adds that it
  travels with Row 38.22 (ii)'s weights, the record's *"travels with 38.22 (ii)'s behaviour half"*). Run the same search
  with the Grep tool before appending and report it. If you find one of the five parts already in §10, do not append it
  again and report it.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 81073–83225) for
  the same thirty row numbers as §3.3 found none. Run the same search with the Grep tool; if you find an entry for a
  row-part this stretch writes, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report
  it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.36 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.37 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 12 commit, as in sessions 11 to 21.
   Attribute it in the diff table to *"session 22's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.36
   only**, after sessions 10 to 21's §L.1 to §L.35. §L.37 to §L.55 are not applied, read or touched.
3. **A1, for the writing side's handoff entries.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed.
   **Handoff entries 1225, 1226 and 1227 ARE landed**, with this file, in §5 act 1, as
   sessions 8 to 21 landed theirs. Any other untracked handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the record this stretch enters
   (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The writing
   side's search: ***"decided against"* five times, in either search, and the other two phrases not at all**, as §L.36's
   *The act's search* says (the record's lines 44, 45, 47 and 49, two at line 49: Rows 46.44 (i), 38.22 (ii), 38.79 (i)'s
   remainder, 24.2's idiom part and 57.454's idiom part). **Every one is a part §3.2 places HISTORICAL** by a line of its
   own; no hit is left without a line. Report the result. Item 2: not reached. Item 3: not reached. Item 4: not reached.
   **Item 5: FIVE entries appended (§3.3).** Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 12 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before §L.36's lines, its §10 entries and the in-progress line
   are all written, do not commit; STOP and report which of them were applied to the uncommitted copy and that it is not
   landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 12 commit:**
     `git diff b3cec9999366ec330d2c7016f83115202cf8fe54 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session22_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the §10 additions of §3.3 (five lines, no blank line); the in-progress line
     of §3.5 item 3; and a NOT QUARANTINED line only if §3.4 (b) found an entry. Then
     `git diff --numstat b3cec9999366ec330d2c7016f83115202cf8fe54 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 52 added lines and 1 deleted line** (the 23 lines and their 23 blank lines, 46; the §10
     entries, 5; the in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2
     that was STOP-and-report**, less 1 for each §10 entry not appended, plus 1 added for each NOT QUARANTINED line
     §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,163 added lines and 4 deleted lines** (`1163` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 21 the file stood at 1,112 added and 4 deleted against the Task 2
     commit (session 21's instruction gave that figure and its report confirmed it [relayed: the numstat itself not
     re-run here]); this stretch adds 51 lines. The in-progress line replaces a line that is itself an addition against
     the Task 2 commit, so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **491** (468 + 23, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting` **28** (the 23 lines and the 5 §10 entries; less 1
     for each line that was STOP-and-report, less 1 for each §10 entry not appended, plus 1 for a NOT QUARANTINED line
     naming it), `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting` **7** (unchanged).
   - **Then, if every line of §3.2 and every §10 entry were written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`720b5073cd129493bd196112acb20ce3e9c277a2`** — the blob of the writing side's simulated edit (§8 below: 5,314,921
     bytes, 84,602 lines, line feeds only). A different blob with every count above as given means a byte differs
     somewhere in what was written: do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 13 (§L.36): the 23 lines of the idiom-tags part 1 row-parts written in the reading file under their ratification, five RELOCATED parts added to the transfer list, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_22_task_3_stretch_13_2026_11_24.md`**, as sessions 2 to 21
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.37, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's files first, in a commit of their own, before any edit to the reading file.** Exactly
   these paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_22_task_3_stretch_13_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_five.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_six.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_seven.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1225, 1226 and 1227 and the session 22 instruction of the L3 application landed; Task 3 stretch 13 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: for each row, the row check of
   §3.1 item 4 and the word check of §3.1 item 5, then its lines of §3.2; then the §10 search and the §10 entries of
   §3.3; the §11 search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_22_task_3_stretch_13_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 22 of the L3 application, Task 3 stretch 13 (§L.36) written; stretch 14 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 23 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 38.79, 24.2, 57.454, 57.118 and 57.535 and as one
   sentence for the other eleven if they were as stated; the quotation check, each quoted passage stated; the §10 search
   and the five §10 entries of §3.3 (their line numbers after the edit), and the §11 search of §3.4, with their results.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (the nine rows of the record's §3.2, each with §L.36 and the words that list it); *recorded lines
   not written: no disposition word* (none expected); *rows named by more than one record* (Rows 38.79, 24.2, 57.454,
   57.118, 46.45, 38.22, 46.43 and 57.399, as §3.1 item 7 says); *ADOPTED words read at the row* (all 12 ADOPTED lines,
   each with the proposed word read and that its line does not say *as proposed*); *audit questions added* (none);
   *audit questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by row* (none: the
   record does not say a row leaves §10); the decided-against search (§4 item 4), with its result and the line each hit
   is written in.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph. *A heading of this
   session's report only, as in sessions 10 to 21's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 22 of the L3 application ends here. Stretch 14 of Task 3 is not begun. Nothing else was done."*

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

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1225, a writing session (entry 1225 §3 step 1: the
sitting booted on entry 1224 verified session 21's stretch at the objects, no finding, and this sitting does not
re-verify it). Read at the objects for this file, over staged copies: the three git reference files (both refs
`ad8f3ddd…`); the reading file's blob recomputed, `3343d6f34c0ac1f9bc82c6b2d3286239add0096f` (5,305,690 bytes, 84,551
lines, no carriage return), its `##` headings (§6 at 435, §7 79517, §10 79975, §11 81073, §12 83226) and line 54 in
full; session 21's instruction whole (blob `2a24ae49…`, recomputed); the big dispatch's blob recomputed on the staged
copy (`b5274c2c…`, 941,330 bytes, 7,157 lines), at lines 99–394 (the forms), 3754–3887 (§L.36 whole) and 6616–6820
(Task 3 whole), and at §L.37's heading and opening (line 3888 on, for the judgment of where the stretch stops); the
record whole (blob `4aa210c7eadfa68e54e58d36cc38e893274c690e`, 9,010 bytes, 116 lines by `wc -l`, no carriage return);
the release part 2 record at lines 700–744 (Ruling 15) and its blob (`441e0d01…`); the release part 1 record at lines
215–243 (Ruling 5) and its blob (`b17c6754…`). Each of the 16 rows found exactly once by its heading, inside §6, and
read whole from its heading to its closing `---`: its shape, its earlier lines (Rows 38.79, 24.2, 57.454 and 57.118
only), its proposed word for the claim named (UNPLACED at each) and its outgoing statement, as §3.1 items 2, 4 and 5
state; §10's headings (L2 at 80177, the second axis at 80711), its lines 80700–80711, and §10 and §11 searched for the
thirty row numbers as a bare number with look-around (§10: lines 80589, 80624, 80684, 80706 and 80791, none the part
written; §11: none); the counts §1 check 4 gives. Every quotation of §3.2 checked against its record by a read-only
script (line breaks joined, asterisks removed): the §3.1 bullet and the seven items each found exactly once. Row 46.43's
two lines compared by script between the big dispatch's §L.36 table (line 3782) and the release part 2 record's lines
727 and 729: equal. The record searched for the three decided-against phrases (line breaks joined, case matched and
not): *"decided against"* five times each way, the other two none. **The edit simulated on a copy of the reading file
in the container** by §3.1 item 2's placement rule, §3.3's entries and §3.5 item 3's line, the lines taken by script
from this file's own text, gives, against the staged file, **52 added lines and 1 deleted**, the counts **491 / 3 / 53 / 26 / 1 / 1**,
the record names **28** (idiom-tags part 1) and **7** (substitution part 2), no new line saying *as proposed*, and the
blob **`720b5073…`** (5,314,921 bytes, 84,602 lines; the 9,231 bytes added equal the sum computed from the 23 lines,
their 23 blank lines and the five §10 entries, the in-progress line's change adding no byte); each row's insertion
point found by the rule, at the place §3.1 item 2 states for it, and the five entries directly after line 80709. Relayed, not re-checked here: the archive
JSON's blob `1df4f207…` and the untracked paths (session 21's instruction and the sitting booted on entry 1224); the Task
2 commit `4b6dc3bd…` and the stretch 12 commit `b3cec999…` (entry 1225 §2 item 1, which recomputed it); the 1,112 added
and 4 deleted lines against the Task 2 commit after session 21; the end of `cowork_handoff.md`'s topmost block at line
255 and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 21's instruction gives
them).*

*Check note: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1226, checking this file as a turn of its own
(the user's Ruling 1 (e) of 2026-11-24). Read at the objects, over staged copies: the three git reference files (both
refs `ad8f3ddd…`); the blobs of this file as written (`94bcd49f…`, 56,274 bytes, 589 lines), the big dispatch
(`b5274c2c…`), the reading file (`3343d6f3…`, 5,305,690 bytes, 84,551 lines), the record (`4aa210c7…`, 9,010 bytes, 116
lines), the release part 2 record (`441e0d01…`), the release part 1 record (`b17c6754…`) and session 21's instruction
(`2a24ae49…`), each recomputed; the record whole; the release part 2 record at lines 700–744 and the release part 1
record at lines 215–243; the big dispatch at lines 159–274 (the forms, with form (b)'s paragraph *Which ADOPTED word*,
its two-record rule and form (b-H)), 3754–3887 (§L.36 whole) and 6703–6724 (Task 3 (c) items 5 and 6), and its `##` and
`### §L.3` headings, which place the ranges §2 item 9 names; the reading file's `##` headings, line 54, lines 80175–80177
and 80698–80712, and the 16 rows, each found exactly once inside §6 and read whole (the shape §3.1 item 2 gives at each,
the earlier lines at Rows 38.79, 24.2, 57.454 and 57.118 only, UNPLACED at the claim or row named, the fit of §3.1 item
4); session 21's report at its numstat lines (`1112` and `4`); the starting counts of §1 check 4. Every quotation of §3.2
found in the record (line breaks joined, asterisks removed): the bullet and the seven items once each, *"decided against
in so far as it selects the catalog L3 reads"* twice; Row 46.43's two lines equal to the release part 2 record's lines
727 and 729 and found in the big dispatch's line 3782; the decided-against search: five hits (lines 44, 45, 47 and 49,
two at 49), the other two phrases none. §10 and §11 searched for the thirty row numbers: §10 lines 80589, 80624 (two),
80684, 80706 and 80791, each read, none the part written; §11 none. **Re-simulated from this file's own text by this
sitting's own script: the blob `720b5073cd129493bd196112acb20ce3e9c277a2`, 5,314,921 bytes, 84,602 lines, 52 added and
1 deleted, the counts 491 / 3 / 53 / 26 / 1 / 1, the record names 28 and 7, no new line saying *as proposed*.** Found:
nothing in the lines, rows, words, counts, searches or the expected blob. Corrected, no former wording kept
(unreleased): handoff entry 1227 added to what act 1 lands (§1 item 5, §2 item 4, §4 item 3, §5 act 1 and its subject);
the banner; and one sentence added to §3.3 item 5 reading Task 3 (c) item 5's *"a row §10 already carries"* by
row-part, with session 19's precedent at lines 80708–80709, so that the hits at lines 80706 and 80791 are not taken
for a difference from the big dispatch. Relayed, not re-checked: the archive JSON's blob, the Task 2 and stretch 12
commits (not as git objects), the untracked paths, `cowork_handoff.md`'s line 255 and `cowork_audit_protocol.md`'s line
180.*
