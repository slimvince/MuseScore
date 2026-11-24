# CC dispatch — the L3 application, SESSION 21 of several: Task 3 of the L3 application dispatch, twelfth stretch (§L.35), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_two.md`, the sitting that verified
> session 20 (the user's ruling of 2026-11-24: the session that verifies a stretch also writes the next stretch's
> instruction). CHECKED AS A TURN OF ITS OWN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_three.md` (its check note closes §8),
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
called **the Task 2 commit** below). Sessions 10 to 19 applied Task 3's first ten stretches, §L.1 to §L.32. Session 20
applied the eleventh stretch, §L.33 and §L.34, in commit `824f968ef3772106a0106d2a31b05e5429e46c90` (called **the
stretch 11 commit** below), and committed its report as `22990f339c12a1e832151b9eeba3c2c99e8188bd`, the current tip.

**This is session 21. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry: §L.35, the seventh record of family 1
(the catalog's substitution rows, part 2). It commits that twelfth stretch as ONE commit, pushes it, writes its report,
and STOPS.** §L.36 is a later session's.

**Why the stretch covers one entry and stops at §L.36** (the user's ruling of 2026-11-24: a writing session judges how
many ledger entries fit). §L.35 gives 6 lines and the run's first transfer-list entry under *the second axis — voice
leading*, and one of its lines quotes its record with an ellipsis. §L.36 gives about 25 lines on 26 row-parts: seven
split rows carrying two or three lines each in forms (b), (b-H) and RELOCATED, the two-line text Ruling 15 of the
release part 2 record gives Row 46.43, five RELOCATED parts each needing a transfer-list entry, and a second record's
line on Row 57.118. The sitting that wrote this file had first carried a full verification of session 20's stretch, so
it judged that §L.36 would leave too little margin to write it and re-run the simulation cleanly, and the stretch stops
at the boundary before it.

**What this stretch writes, in one paragraph.** **6 lines, all opening `*RULED DISPOSITION (`, on 6 rows**, from
`cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md`, Ruling 1 (the record's one ruling): **5 lines with
the word ADOPTED — proposed** (Rows 57.401 (ii), 57.429, 57.432, 57.487 (ii) and 57.489 (i), the record's *ADOPTED —
proposed (5)* bullet) and **1 line with the word RELOCATED** (Row 57.118, its voice-leading portion, to ***the second
axis — voice leading***, in the exact text the big dispatch's §L.35 table gives). **No line says *as proposed*:** every
row-part named is proposed UNPLACED at its row. §3.2 gives every line with its exact text. **One entry appended to the
transfer list, §10,** under its heading *To the second axis — voice leading*, for Row 57.118's voice-leading portion
(§3.3). **Nothing at §11** (§3.4). And the in-progress line brought forward from §L.34 to §L.35 (§3.5). **The record's
other eight row-parts get no line** and are listed in the report under *rows given no line now* (§3.2's last
paragraph).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only.** This session copies into the reading file the placements the record already makes; it decides
nothing and changes no algorithm. The record states *"Documentation only. Algorithm: no change."* It orders no
amendment of the successor, the charter or the interface contract that belongs to Task 3 (§L.35, *Successor*,
*Charter*, *Interface contract*): Row 57.118's voice-leading portion is placed toward `FRAMEWORK.md`'s *The second axis —
voice leading*, but the record gives no text for the framework, and this session writes none.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `22990f339c12a1e832151b9eeba3c2c99e8188bd`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_21_task_3_stretch_12_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 11 commit left it.**
   `git diff --quiet 824f968ef3772106a0106d2a31b05e5429e46c90 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 22990f339c12a1e832151b9eeba3c2c99e8188bd -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `d00497918ff18efe85fb9ed97543decf7df49b25`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **462**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting` must count
   **8**; `cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting` must count **2**; and
   `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting` must count **0**. Any other result: STOP and
   report, the file not touched. (The writing side's staged copy: 5,301,823 bytes, 84,538 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 22990f339c12a1e832151b9eeba3c2c99e8188bd -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1223 and 1224), plus the
     paths sessions 2 to 20 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_four.md` (written by the sitting
   that checked this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_three.md` (written by the sitting
   that wrote this file; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The one record this stretch rests on, WHOLE** — it is the authority for every line this session writes (**the
   record's own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md` (§L.35; 6,651 bytes, 88
   lines by `wc -l`).

   **Do NOT read the records of §L.1 to §L.34 or of §L.36 to §L.55, and do not open the record's surface** (the lines
   quote the record only).
8. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, and form (b-H)**, the premise ledger, the declared start state, the standing bars, the
     findings rule);
   - lines 395–430 (how §L is written);
   - **lines 3656–3753 (§L.35, your stretch)**;
   - lines 6616–6820 (Task 3, whole, **with (c) item 5, the transfer list**);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3655 (§L.1 to §L.34, applied); lines 3754–5906 (§L.36 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary; its list of the charters a RELOCATED line may name, at line 402, names
     ***the second axis — voice leading***);
   - **each of the 6 rows §3.2 names, whole, at §6** (lines 435–79504): find each by its heading with the Grep tool,
     pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
     heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
   - §10 (lines 79963–81059): searched with the Grep tool for every row number of this stretch (§3.3), and **read from
     its heading *To the second axis — voice leading* (line 80699) to the next heading (line 80780)**;
   - §11 (lines 81060–83212), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch: one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*`
   paragraph and every other sentence of the row untouched. Every line names its record's file and Ruling 1 (the record
   has one ruling), the record file written as its bare file name, as sessions 10 to 20 wrote theirs. Where §3.2 names a
   claim, the line names it (form (b)'s split-row rule); otherwise the line names none. Row 57.118 has no claims; its
   line names the part it places by the record's phrase (*"for the voice-leading implications"*), as the §L.35 table
   gives it. **Each row-part that the record places gets exactly one line**, and no row gets more than one line from
   this stretch.
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"At the
   source now."*). Each new line is followed by one blank line. Read each row's actual shape from its proposed
   paragraph to its end before writing. **The writing side read all 6 rows at the staged copy; none carries an earlier
   ruled or recorded line, and every one ends with a blank line and then `---`.** Their shapes after the proposed
   paragraph: **all 6 have a paragraph headed *"At the source now."* directly after the proposed paragraph; the new line
   goes directly beneath the proposed paragraph, above it** — Rows 57.401, 57.429, 57.432, 57.487, 57.489 and 57.118.
   Row 57.401 carries a further paragraph after *At the source now.*, headed *"The decisions register at this row."*; it
   is not touched, and the line goes above *At the source now.* as at the others (as session 20 placed Row 57.107's).
   If you find a different shape at a row (an earlier line, a further paragraph, or an ending other than `---`), state
   it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, that line
   is a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it: for the five ADOPTED rows, the record's
   *ADOPTED — proposed (5)* bullet of *The placements* whole, its bold lead included as words and its marks dropped, and
   its closing period dropped (the line's own period follows the closing quotation mark, as session 20's line at Row
   44.4 dropped its bullet's closing period); for Row 57.118, the text the big dispatch's §L.35 table gives, which
   quotes the record's *Split by subject (1)* bullet in **two pieces joined by an ellipsis** (`…`): the first piece ends
   *"the voice-leading implications"*, the second begins *"RELOCATED to the second axis"*, and what the ellipsis stands
   for is the one word *"proposed"* in the record. **The writing side checked every quotation against its record by a
   read-only script (words and punctuation, line breaks read as spaces, asterisks not compared): the ADOPTED bullet
   found exactly once; each of Row 57.118's two pieces found exactly once, the first before the second, with only
   *" proposed "* between them.** Before writing each line, find its quoted passage (each piece, for Row 57.118) in the
   record yourself and compare it the same way: every word and every punctuation mark must match, line breaks read as
   spaces. The line keeps its marks exactly as §3.2 gives them. A difference is a STOP-and-report for that line: no
   line written, listed in the report under *rows the act could not place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that part is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The fit, row by row: Row 57.401 (ii), a chord
   matching a member through a substitution entry's mapping, the returned entry carrying that mapping (the record's
   gloss: *"matching through a substitution, the match carrying the mapping"*); Row 57.429, the glossary's
   *Substitution* (*"the glossary terms *substitution* and *substitution mapping*, as terms of the catalog L3 reads"*);
   Row 57.432, the glossary's *Substitution mapping* (the same gloss); Row 57.487 (ii), the substitution recorded only in
   the annotation (the record quotes *recorded only in the annotation* and glosses it *"the annotation is the published
   match"*); Row 57.489 (i), the
   consumer recording what the chord stands in for (*"the match records what the chord stands in for"*); Row 57.118,
   each substitution carrying its voice-leading implications and its style weights, of which this line places the
   voice-leading implications (*"the voice-leading implications"*). A row that does not fit is a STOP-and-report for
   that row-part: no line, listed under *rows the act could not place* with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.35's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **The record names the
   word in full** for its ADOPTED lines (*"ADOPTED — proposed (5):"*, the record's line 40), so item (1) of the
   paragraph gives **ADOPTED — proposed** for all five. For Row 57.118 the word is **RELOCATED**, in the text §L.35's
   *Open* point (3) points at (Ruling 2 of the same release part 2 record, writing the line as the working list's item
   (xxxix) gives it), not *as proposed*, the row being proposed UNPLACED. **The writing side read the proposed paragraph
   at every row-part this stretch names: each is UNPLACED** (for the rows with claims, at the claim named: Rows 57.401
   (ii), 57.487 (ii) and 57.489 (i); Row 57.487's claim (i) is proposed RELOCATED and gets nothing here). So no line's
   word is the row's own proposed word, and **no line says *as proposed***: the paragraph's *"Otherwise as proposed is
   not written, and the placement is given in the record's words"*. If you find a row-part's proposed word for the part
   named other than UNPLACED, that line is a STOP-and-report. No other wording (such as *"placed from"*) is added. Every
   one of the 5 ADOPTED lines is listed in the report under *ADOPTED words read at the row*, with the proposed word read
   (UNPLACED) and that its line does not say *as proposed*.
6. **The split row-part.** **Row 57.118 (no claims)** is split by its record by subject: *"the voice-leading
   implications proposed RELOCATED to the second axis (`FRAMEWORK.md`, *The second axis — voice leading*); the style
   weights moved to the family's idiom-tags surface, and, as evidence when choosing chords, travelling with key Ruling 2's
   candidate (D-503 travels with it)"*. One line, for the voice-leading portion. The style weights get no line from this
   record (form (b): *"A part a record says it moves to another record gets no line from the record that moves it"*);
   they are met at §L.36's entry, a later session's.
7. **Rows named by more than one record** (form (b)'s two-record rule, by part). **No row this stretch writes carries an
   earlier record's line**: the writing side read all 6 at the staged copy and found no `*RULED ` or `*RECORDED ` line
   in any of them. §L.35's *Rows named by more than one record* names **Row 57.401** ((ii) here; (i) at §L.32, given no
   line there, waiting wholly). Two further rows are named by this record and another, by part: **Row 57.118** (its
   voice-leading portion here; its style weights at §L.36, not applied in this session) and **Row 46.27** (named here
   for its composition half, which this record does not place; its analysis half carries §L.34's line, written by
   session 20). None gets a second line from this stretch. List all three in the report under *rows named by more than
   one record*, each with what §L.35 says of it. If you find an earlier record's line on any part this stretch writes,
   apply the rule by part as the big dispatch gives it; if an earlier stretch's line would have to be deleted or edited,
   STOP, do not commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several rows, `<claim>` is filled in from
the row list (written `(ii)` or `(i)` as the list gives it); where the list gives no claim, `<claim>` and the space after
it are dropped.

**§L.35 — the catalog's substitution part 2 record
(`cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md`): 6 lines.**

*The ADOPTED rows — 5 lines, none* as proposed. Rows, in this order: 57.401, written `(ii)`; 57.429; 57.432; 57.487,
written `(ii)`; 57.489, written `(i)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — "ADOPTED — proposed (5): Row 57.401 (ii) (matching through a substitution, the match carrying the mapping); Rows 57.429 and 57.432 (the glossary terms *substitution* and *substitution mapping*, as terms of the catalog L3 reads); Row 57.487 (ii) (*"recorded only in the annotation"*: the annotation is the published match; its part (i) already proposed RELOCATED to L2 by the reading file; its L2 side ruled RELOCATED to L3 by the L2 nothing-from-L3 Ruling 5); Row 57.489 (i) (the match records what the chord stands in for)".
```

*The split row-part — 1 line, at Row 57.118*, exactly as the big dispatch's §L.35 table gives it:
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md, Ruling 1).* **RELOCATED** — to ***the second axis — voice leading***, for the voice-leading implications: "Split by subject (1): Row 57.118 — the voice-leading implications … RELOCATED to the second axis (`FRAMEWORK.md`, *The second axis — voice leading*)".
```
The ellipsis is the one character `…` (U+2026) with one space on each side, as the big dispatch's table writes it.

**The count.** `*RULED DISPOSITION (`: **6** — 5 **ADOPTED — proposed**, 1 **RELOCATED**; all 6 naming the substitution
part 2 record. None opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) the five ADOPTED lines quote, as the
record's placement, the record's *ADOPTED — proposed (5)* bullet whole, its bold lead's marks dropped as sessions 17 to
20 dropped them, and its closing period dropped as session 20 dropped Row 44.4's; the record's inner emphasis is kept —
the italics around *substitution* and *substitution mapping*, and the italic quotation *"recorded only in the
annotation"* with its own quotation marks — as earlier stretches kept a record's own emphasis inside a quotation (the
part 2 record's `*"Layer 5"*`, kept by session 19; the further-rows record's bold, kept by session 20); (2) Row 57.118's
line is not the writing side's: it is the text the big dispatch's §L.35 table gives, as Ruling 2 of the release part 2
record orders it written from the working list's item (xxxix); it is reproduced here byte for byte from the table.

**What this stretch gives no line** (Task 3 (a)), as §L.35 names them:
- **§L.35's eight row-parts — Rows 57.110, 57.112, 57.113, 57.114, 57.115, 57.116, 57.117 and 57.489 (ii):** *"No line
  from this record; listed in the report"*, as Ruling 5 of
  `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part2_sitting.md` rules it, in
  the form of that record's Ruling A, quoting the substitution part 2 surface's §3.2 sentence *"Each row's one
  disposition is written when what it waits for is settled."* (§L.35's table and its *Open* point (2)). Each is listed
  in the report under *rows given no line now*, with §L.35 and those words; each keeps its proposed UNPLACED.
- **Row 57.118's style weights:** *"moved to the family's idiom-tags surface"*; no line from this record; met at §L.36.
  Not listed under *rows given no line now*.
- **Rows the record names and does not place:** Row 57.487 (i) (*"already proposed RELOCATED to L2 by the reading
  file"*; §10 carries it already, at line 80684 of the file as it stands now, with Row 57.486) and Row 46.27 (its
  composition half, in the record's §2). No line from this record, not touched.
- **The other claims of the rows this stretch writes** — Row 57.401 (i) (named at §L.32, waiting wholly; not named by
  this record), Row 57.487 (i) (above, named and not placed) and Row 57.489 (ii) (above, given no line now) — get
  nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — ONE entry appended

- **Item 5:** Row 57.118's voice-leading portion is placed RELOCATED, out of UNPLACED, to ***the second axis — voice
  leading***. §10 has that heading, *"**To *the second axis — voice leading*.**"*, at line 80699 of the file as it stands
  now, its entries running to line 80778 and the next heading, *To the uncertainty surface (NOT A LAYER)*, at line
  80780. Row 57.118 is not listed under it, nor anywhere in §10: the writing side searched §10 (lines 79963–81059) for
  the row number of every row-part the record places or names (57.401, 57.429, 57.432, 57.487, 57.489, 57.118, 57.110,
  57.112, 57.113, 57.114, 57.115, 57.116, 57.117 and 46.27) as a bare number with look-around. **One hit: line 80684**,
  the entry for *"Rows 57.486 and 57.487 (i)"* — **another claim** than the one this stretch writes. So item 5 appends
  ONE entry, in §10's own entry form, **directly after the last entry under that heading** (the entry for Row 37.46, now
  at line 80778, whose parenthesis names `cowork_rulings_2026_11_08_l3_disposition_words_sitting.md`) and **before the
  blank line that precedes the next heading** — no blank line added, as §10's entries under one heading stand on
  consecutive lines. The entry, exactly:
  ```
  - Row 57.118, its part on the voice-leading implications — that each substitution carries its voice-leading implications. *(cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md, Ruling 1.)*
  ```
  *The writing side's wording, overrulable by the user:* the clause is the row's own one-claim reading at §6 (*"each
  substitution carries its voice-leading implications and its style weights"*), cut to the portion placed; the part is
  named on the shape of the entries session 19 appended (*"Row 24.2, its part on the prior — …"*); the parenthesis names
  only the record and ruling, as the Row 37.46 entry's does, the record naming nothing that travels with this portion
  (D-503 travels with the style weights, which go elsewhere). Run the same search with the Grep tool before appending
  and report it. If you find Row 57.118 already in §10, append nothing and report it.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 81060–83212) for
  the same fourteen row numbers as §3.3 found none. Run the same search with the Grep tool; if you find an entry for a
  row-part this stretch writes, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report
  it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.35 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.36 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 11 commit, as in sessions 11 to 20.
   Attribute it in the diff table to *"session 21's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.35
   only**, after sessions 10 to 20's §L.1 to §L.34. §L.36 to §L.55 are not applied, read or touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1223 and 1224 ARE landed**, with this file, in §5 act 1, as sessions 8 to 20 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the record this stretch enters
   (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The writing
   side's search: **none of the three, in either search** (as §L.35's *The act's search* says; the record's lines 34, 35
   and 62 carry *"decided chords"*, *"decides key and chord together"* and *"not decided"*, none of them one of the three
   phrases). Report the result. Item 2: not reached. Item 3: not reached. Item 4: not reached. **Item 5: ONE entry
   appended (§3.3).** Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 11 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before §L.35's lines, its §10 entry and the in-progress line are
   all written, do not commit; STOP and report which of them were applied to the uncommitted copy and that it is not
   landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 11 commit:**
     `git diff 824f968ef3772106a0106d2a31b05e5429e46c90 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session21_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the §10 addition of §3.3 (one line, no blank line); the in-progress line of
     §3.5 item 3; and a NOT QUARANTINED line only if §3.4 (b) found an entry. Then
     `git diff --numstat 824f968ef3772106a0106d2a31b05e5429e46c90 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 14 added lines and 1 deleted line** (the 6 lines and their 6 blank lines, 12; the §10 entry,
     1; the in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2 that was
     STOP-and-report**, less 1 if the §10 entry was not appended, plus 1 added for each NOT QUARANTINED line §3.4 (b)
     found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,112 added lines and 4 deleted lines** (`1112` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 20 the file stood at 1,099 added and 4 deleted against the Task 2
     commit (session 20's report, its §5 [relayed: the numstat itself not re-run here; the 20 lines session 20 added
     were re-derived by the writing side's rebuild of the file]); this stretch adds 13 lines. The in-progress line
     replaces a line that is itself an addition against the Task 2 commit, so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **468** (462 + 6, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting` **7** (the 6 lines and the §10 entry; less 1 for
     each line that was STOP-and-report, less 1 if the §10 entry was not appended, plus 1 for a NOT QUARANTINED line
     naming it), `cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting` **2** (unchanged),
     `cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting` **8** (unchanged).
   - **Then, if every line of §3.2 and the §10 entry were written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`3343d6f34c0ac1f9bc82c6b2d3286239add0096f`** — the blob of the writing side's simulated edit (§8 below: 5,305,690 bytes,
     84,551 lines, line feeds only). A different blob with every count above as given means a byte differs
     somewhere in what was written: do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 12 (§L.35): the 6 lines of the catalog's substitution part 2 row-parts written in the reading file under their ratification, Row 57.118's voice-leading portion added to the transfer list, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_21_task_3_stretch_12_2026_11_24.md`**, as sessions 2 to 20
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.36, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own, before any edit to the reading file.**
   Exactly three paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_21_task_3_stretch_12_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_three.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_four.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1223 and 1224 and the session 21 instruction of the L3 application landed; Task 3 stretch 12 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: for each row-part, the row
   check of §3.1 item 4 and the word check of §3.1 item 5, then its line of §3.2; then the §10 search and the §10 entry
   of §3.3; the §11 search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_21_task_3_stretch_12_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 21 of the L3 application, Task 3 stretch 12 (§L.35) written; stretch 13 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 6 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Row 57.401 and as one sentence for the other five if
   they were as stated; the quotation check, with Row 57.118's two pieces stated separately; the §10 search and the §10
   entry of §3.3 (its line number after the edit), and the §11 search of §3.4, with their results.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (§L.35's eight row-parts, each with its §L entry and the words that list it); *recorded lines not
   written: no disposition word* (none expected); *rows named by more than one record* (Rows 57.401, 57.118 and 46.27,
   as §3.1 item 7 says); *ADOPTED words read at the row* (all 5 ADOPTED lines, each with the proposed word read and that
   its line does not say *as proposed*); *audit questions added* (none); *audit questions no longer quarantined* (none
   expected); *§10 rows a record says leave, not named by row* (none: the record does not say a row leaves §10); the
   decided-against search (§4 item 4), with its result.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph. *A heading of this
   session's report only, as in sessions 10 to 20's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 21 of the L3 application ends here. Stretch 13 of Task 3 is not begun. Nothing else was done."*

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

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1222, which first verified session 20's stretch at the
objects (no finding; entry 1223 §2) and then, under the user's ruling of 2026-11-24, wrote this file. Read at the
objects for this file, over staged copies: the three git reference files (both refs `22990f33…`); the three commit
objects of session 20 and their trees on every changed path, each SHA-1 recomputed; the reading file at the stretch 11
commit's blob, rebuilt independently from blob `9bc17177…` and byte-identical to `d0049791…` and to the file on disk
(5,301,823 bytes, 84,538 lines, no carriage return), its `##` headings (§6 at 435, §7 79505, §10 79963, §11 81060, §12
83213) and line 54 in full; session 20's instruction whole (blob `30f6ef4a…`) and report whole (blob `432d60a9…`); the
big dispatch at lines 3656–3753 (§L.35) and 3754–3887 (§L.36, for the judgment of where the stretch stops) and
6616–6820 (Task 3), and by search for its `### §L.` headings, its blob recomputed on the staged copy (`b5274c2c…`,
941,330 bytes, 7,157 lines); the record whole (blob `80539b387836b9b30fb75955a488011b771d72c0`, 6,651 bytes, 88 lines
by `wc -l`, no carriage return); the substitution part 1 record's two placement bullets (its lines 56 and 60, for the
precedent of the dropped closing period); the list-answers part 2 record at its `##` headings and lines 34–36 and
150–153 (Ruling A's ruling and Ruling 5's); the substitution part 2 surface's §3.2 sentence at its line 131; the release
part 2 record at lines 84–88 (Ruling 2's order on the working list's items (xxxvii) to (xxxix)); the working list
`ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md` at lines 1280–1311 (item (xxxix), whose line
text is the one the §L.35 table gives). Each of the 6 rows found exactly once by its heading, inside §6, and read whole
from its heading to its closing `---`: its shape, no earlier ruled or recorded line, its proposed word for the part named
(UNPLACED at each) and its outgoing statement, as §3.1 items 2, 4 and 5 state; the reading file's §5 at line 402 (the
second axis among the charters a RELOCATED line may name); §10 from line 80697 to line 80782 (the second-axis heading,
its entries, and the next heading), and §10 and §11 searched for the fourteen row numbers as a bare number with
look-around (§10: one hit, line 80684, another claim; §11: none); the counts §1 check 4 gives. Every quotation of §3.2
checked against its record by a read-only script (line breaks joined, asterisks removed): the ADOPTED bullet found
exactly once; Row 57.118's two pieces each found exactly once, in order, with only *" proposed "* between them. The
record searched for the three decided-against phrases (line breaks joined, case matched and not): none. **The edit
simulated on a copy of the reading file in the container** by §3.1 item 2's placement rule, §3.3's entry and §3.5 item
3's line, the lines taken by script from this file's own text, gives, against the staged file, **14 added lines and 1
deleted**, the counts **468 / 3 / 53 / 26 / 1 / 1**, the record names **7** (substitution part 2), **2** (substitution
part 1) and **8** (further rows), no line saying *as proposed*, and the blob **`3343d6f3…`** (5,305,690
bytes, 84,551 lines; the 3,867 bytes added equal the sum computed from the six lines, their blank lines, the §10 entry
and the in-progress line's change, which changes no byte count); each new line's place in the copy read back at Rows
57.401 and 57.118 and under §10's second-axis heading. Relayed, not re-checked here: the archive JSON's blob `1df4f207…` and the untracked paths
(session 20's report, §1 item 5); the Task 2 commit `4b6dc3bd…` (the same text session 20's instruction gives for the
same object); the 1,099 added and 4 deleted lines against the Task 2 commit after session 20 (session 20's report, not
re-run); the end of `cowork_handoff.md`'s topmost block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s
dispatch-protocol section (as session 20's instruction gives them); the forms section of the big dispatch (lines 99–394)
and line 98, not read by this sitting, whose wording of form (b), of its paragraph* Which ADOPTED word *and of the place
a ruled line goes is taken from session 20's checked instruction.*

*Check note: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1223, checking this file as a turn of its own
(the user's Ruling 1 (e) of 2026-11-24). Read at the objects, over staged copies: the three git reference files (both
refs `22990f33…`); the blobs of the big dispatch (`b5274c2c…`), the reading file (`d0049791…`, 5,301,823 bytes,
84,538 lines), the record (`80539b38…`) and this file as written (`37abdc68…`), each recomputed; the record whole; the
big dispatch at line 98 and lines 99–394 (the forms: form (b), its paragraph on which ADOPTED word, the two-record
rule, form (b-H)), lines 3656–3753 (§L.35 whole) and 6616–6820 (Task 3 whole), and its `##` and `### §L.` headings, which
place every range §2 item 8 names; the 6 rows, each found once inside §6 and read whole (shape, no earlier line, UNPLACED
at the part named, the fit), and Row 46.27's §L.34 line; line 54; line 402; §10 from line 80676 to line 80782; the
starting counts; the precedents at Row 44.4 (line 61875, the closing period dropped) and Row 57.107 (line 74085, above its
paragraph on the source now); the list-answers part 2 record's Ruling A (lines 34–36) and Ruling 5 (lines 150–153) and its
headings; the release part 2 record's Ruling 2 (lines 83–87 inside it) and its headings; the substitution part 2
surface's §3.2 sentence (line 131); the working list's item (xxxix) (lines 1284–1311); session 20's report at its §1
item 5 and its numstat lines (`1099` and `4`). The ADOPTED quotation equal to the record's bullet, its bold lead's marks
and its closing period dropped; Row 57.118's two pieces each found in the record with only the word "proposed" between them,
and its whole line found exactly once in the big dispatch, at the §L.35 table (line 3677); the decided-against search
(none); §10 and §11 searched for the fourteen row numbers (§10: line 80684 only; §11: none). **Re-simulated from this
file's own text: the blob `3343d6f34c0ac1f9bc82c6b2d3286239add0096f`, 5,305,690 bytes, 84,551 lines, 14 added and 1
deleted, the counts as §4 item 8 gives them, no further "as proposed".** Found: nothing in the lines, rows, words,
counts, searches or the expected blob. Corrected, no former wording kept (unreleased): handoff entry 1224 added to what
act 1 lands (§1 item 5, §4 item 3 and its heading, §5 act 1 and its subject); §2 item 4's two entries to read now 1224
and 1223 (1222 dropped: it checked session 20's instruction and bears on nothing of session 21's); the banner. Relayed,
not re-checked: the archive JSON's blob, the Task 2 commit, `cowork_handoff.md`'s line 255 and
`cowork_audit_protocol.md`'s line 180.*
