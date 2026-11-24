# CC dispatch — the L3 application, SESSION 18 of several: Task 3 of the L3 application dispatch, ninth stretch (§L.31), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_fifteen.md`; CHECKED AS A TURN OF ITS OWN AND
> CORRECTED 2026-11-24 by the sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_sixteen.md` (see the check note at the end);
> NOT YET RELEASED,** under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 16 applied Task 3's first seven stretches, §L.1 to §L.28. Session 17
applied the eighth stretch, §L.29 to §L.30, in commit `e61ad38abad3fcf6637f668c55defe0aef5fe3e6` (called **the stretch
8 commit** below), and committed its report as `03a15953c701aeaece39a2932f8132719bc2c465`, the current tip.

**This is session 18. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry: §L.31, the third record of family 1
(the catalog of named progressions; recognition and its span, part 1). It commits and pushes that ninth stretch, writes
its report, and STOPS.** §L.32 is a later session's.

**What this stretch writes, in one paragraph.** **§L.31's record gives 11 lines, all opening `*RULED DISPOSITION (` and
all naming Ruling 1 of `cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md`, on 9 rows:** 8 lines with
the word **ADOPTED — proposed** (the six row-parts of the record's §3.1, and the first half of each of the two split
row-parts of its §3.3), 2 lines with the word **RELOCATED** (the second half of each split row-part), and 1 line with
the word **HISTORICAL** (Row 8.94, the record's §3.5). **No line says *as proposed*:** every one of these row-parts is
proposed UNPLACED at its row. §3.2 gives every line with its exact text. **At §10, two entries are appended** under the
L2 heading, one for each RELOCATED half (§3.3). **Nothing at §11** (§3.4). And the in-progress line brought forward from
§L.30 to §L.31 (§3.5). **The other 19 row-parts the record places get no line** (§3.2's last paragraph); ten of them are
listed in the report under *rows given no line now*.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the placements the record
already makes; it decides nothing. The record orders no amendment of the successor, the charter or the interface
contract (§L.31, *Successor*, *Charter*, *Interface contract*).

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `03a15953c701aeaece39a2932f8132719bc2c465`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 8 commit left it.**
   `git diff --quiet e61ad38abad3fcf6637f668c55defe0aef5fe3e6 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 03a15953c701aeaece39a2932f8132719bc2c465 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `b98e85128b11e363a0f909fb79fc5c3389499be7`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **427**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting` must count **23**;
   and `cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting` must count **0**. Any other result: STOP and
   report, the file not touched. (The writing side's staged copy: 5,280,457 bytes, 84,462 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 03a15953c701aeaece39a2932f8132719bc2c465 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the five files §5 act 1 lands (this instruction and handoff entries 1214, 1215, 1216
     and 1217), plus the paths sessions 2 to 17 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_fifteen.md` (written by the sitting before
   the one that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_fourteen.md` (the one before it; untracked,
   §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The record this stretch rests on, WHOLE** — it is the authority for every line this session writes (**the
   record's own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md` (§L.31; 7,479 bytes, 92
   lines by `wc -l`). **Do NOT read the records of §L.1 to §L.30 or of §L.32 to §L.55, and do not open the record's
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
   - **lines 3251–3343 (§L.31, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3250 (§L.1 to §L.30, applied); lines 3344–5906 (§L.32 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary);
   - **each of the 9 rows §3.2 names, whole, at §6** (lines 435–79434): find each by its heading with the Grep tool,
     pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
     heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
   - §10 (lines 79893–80983): its destination headings (lines opening `**To `), and the block under
     ***L2 — The tonal reading. The one entangled decision.*** from its heading (line 80095) to the next heading (line
     80623) at least from line 80500 on; and §10 searched with the Grep tool for every row number of this stretch
     (§3.3);
   - §11 (lines 80984–83136), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch: one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*`
   paragraph and every other sentence of the row untouched. Row 8.94's HISTORICAL line is form (b) as well: the record
   places it HISTORICAL in its own word, and the act's search finds none of the three decided-against phrases (§L.31,
   *The act's search*), so form (b-H) is not engaged. Every line names
   `cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1` (the record has one ruling), the record
   file written as its bare file name, as sessions 10 to 17 wrote theirs. Where §3.2 names a claim, the line names it
   (form (b)'s split-row rule); otherwise the line names none. **Each row-part, and each half of a split row-part, gets
   exactly one line**, so two rows get two lines from this stretch: Rows 44.34 and 44.28 (the two halves of one claim
   each, §3.1 item 7).
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"The
   decisions register at this row."*). Each new line is followed by one blank line. Read each row's actual shape from
   its proposed paragraph to its end before writing. **The writing side read all 9 rows at the staged copy; every one
   ends with a blank line and then `---`.** Their shapes after the proposed paragraph:
   - **5 rows: nothing after the proposed paragraph** — 8.50, 8.94, 44.20, 44.33, 44.35. Each such row ends, after the
     edit: proposed paragraph, blank line, **the new line, followed by a blank line**, `---`.
   - **2 rows carrying earlier ruled lines, on another claim, after the proposed paragraph; the new line(s) go after
     them, above the closing `---`:** Row 8.52 (one line on claim (ii), naming
     `cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1`) and Row 44.34 (two lines on claim (ii), naming
     `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1`, written by session 17).
   - **2 rows with a paragraph headed *"The decisions register at this row."* after the proposed paragraph and no earlier
     ruled line; the new line(s) go directly beneath the proposed paragraph, above it:** Rows 44.28 and 44.37.
   - **Two rows get two lines from this stretch:** Rows 44.34 and 44.28, the first half's line (the ADOPTED one) first,
     the order in which the record names the halves.
   If you find a different shape at a row (another earlier line, a further paragraph, or an ending other than `---`),
   state it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, that
   line is a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it, from the record's §1 (*"Ruling 1 — the 28
   row-parts' placements RATIFIED as the surface states them"*): for §3.1's six ADOPTED row-parts, §3.1's bullet whole,
   its bold lead included; for the two split row-parts, §3.3's bullet whole, its bold lead included; for Row 8.94,
   §3.5's bullet whole, its bold lead included. **The writing side checked every quotation against the record by a
   read-only script (words and punctuation, line breaks read as spaces, asterisks not compared): each found exactly
   once.** Before writing each line, find its quoted passage in the record yourself and compare it the same way: every
   word and every punctuation mark must match, line breaks read as spaces. The line keeps its marks exactly as §3.2
   gives them. A difference is a STOP-and-report for that line: no line written, listed in the report under *rows the
   act could not place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that part is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The record's §1 gives each §3.1 row-part a
   gloss in brackets, each §3.3 half its subject, and Row 8.94 its ground (*"the dormant state of the old consumer"*).
   So the fit is: Rows 8.50 and 8.52 (iii), a match (a schema span) crossing a phrase-unit (punctuation-span) boundary,
   one phrase unit holding several; Row 44.33 (i), the matcher the same for every idiom; Row 44.35, chords only; Rows
   44.20 (ii) and 44.37 (i), the recognition read-only and additive; Row 44.34 (i), the recognition yielding a name and
   evidence; Row 44.28 (ii), a single internally-sequential entry's key motion carried by its schema span; Row 8.94, the
   output empty absent the (dormant) consumer. A row that does not fit is a STOP-and-report for that row-part: no line,
   listed under *rows the act could not place* with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.31's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **The record names the
   word in full** for the eight ADOPTED lines (*"ADOPTED — proposed:"* before §3.1's six; *"the name ADOPTED — proposed"*
   and *"the match over the entry's whole stretch ADOPTED — proposed"* at §3.3), so item (1) of the paragraph gives
   **ADOPTED — proposed**. For the two RELOCATED lines and the HISTORICAL line the record names the word itself
   (*"RELOCATED to L2"*; *"HISTORICAL"*). **The writing side read the proposed paragraph at every one of the row-parts
   this stretch names: each is UNPLACED** (for the rows with claims, at the claim named: Rows 8.52 (iii), 44.20 (ii),
   44.33 (i), 44.37 (i), 44.34 (i), 44.28 (ii)). So no line's word is the row's own proposed word, and **no line says
   *as proposed***: the paragraph's *"Otherwise as proposed is not written, and the placement is given in the record's
   words"*. If you find a row-part's proposed word for the part named other than UNPLACED, that line is a
   STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of the 8 ADOPTED lines is listed in
   the report under *ADOPTED words read at the row*, with the proposed word read (UNPLACED) and that its line does not
   say *as proposed*.
6. **The HISTORICAL line.** The record places Row 8.94 HISTORICAL whole (*"§3.5, HISTORICAL (1): 8.94 (the dormant
   state of the old consumer)."*). Row 8.94 states no claims, so the line names none.
7. **The split row-parts, by half.** The record's §3.3 bullet places each of Rows 44.34 (i) and 44.28 (ii) in two
   halves: for 44.34 (i), *"the name ADOPTED — proposed, the evidence RELOCATED to L2 with key Ruling 2's candidate"*;
   for 44.28 (ii), *"the match over the entry's whole stretch ADOPTED — proposed (the surface marks this half as the
   writing side's reading), the key motion as evidence of the local key RELOCATED to L2 with the sequence term at DP-O
   (D-504, D-505)"*. Each line names its claim and its half in the record's words, on the shape of session 17's half
   lines (`(ii), its half on the published match:`): `(i), its half on the name:`, `(i), its half on the evidence:`,
   `(ii), its half on the match over the entry's whole stretch:` and
   `(ii), its half on the key motion as evidence of the local key:`. The two lines of one row-part are this record's
   both, on different halves, so form (b)'s two-record rule is not engaged between them.
8. **Rows named by more than one record** (form (b)'s two-record rule, by part). Two rows of this stretch carry an
   earlier record's line, **each on another claim**: Row 8.52 (claim (ii), from
   `cowork_rulings_2026_11_08_l3_disposition_words_sitting.md`) and Row 44.34 (claim (ii), from
   `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md`, §L.30). Neither earlier line is touched; the new line
   goes after them (§3.1 item 2). §L.31's *Rows named by more than one record* also names Rows 19.38 ((vi) here), 19.39
   ((v) here), 46.18 ((ii) here) and 46.19 ((iii) here), which get no line from this stretch. List all six in the
   report under *rows named by more than one record*, each with what §L.31 says of it and, for Rows 8.52 and 44.34, the
   earlier line found. If you find an earlier record's line on any part this stretch writes, apply the rule by part as
   the big dispatch gives it; if an earlier stretch's line would have to be deleted or edited, STOP, do not commit, and
   report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several row-parts, `<claim>` is filled in
from the row list (written `(i)`, `(ii)`, `(iii)` as the list gives it); where the list gives no claim, `<claim>` and the
space after it are dropped.

**§L.31 — the catalog recognition part 1 record (`cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md`):
11 lines.**

*§3.1's ADOPTED row-parts — 6 lines, none* as proposed. Row-parts, in this order: 8.50; 8.52, written `(iii)`; 44.33,
written `(i)`; 44.35; 44.20, written `(ii)`; 44.37, written `(i)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — "§3.1, follow wholly (6): ADOPTED — proposed: 8.50, 8.52 (iii) (a match may cross a phrase-unit boundary; one phrase unit may hold several); 44.33 (i) (the matcher the same for every idiom); 44.35 (chords only); 44.20 (ii), 44.37 (i) (read-only and additive: publishing the matches revises nothing L2 published and changes no other L3 output)".
```

*Row 8.94 — 1 line, HISTORICAL:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1).* **HISTORICAL** — "§3.5, HISTORICAL (1): 8.94 (the dormant state of the old consumer)".
```

*§3.3's split row-parts — 4 lines, two per row-part, the ADOPTED half first.* Every one of the four quotes the same
passage, written here once as `<Q>`:
`"§3.3, split by use (2): 44.34 (i) — the name ADOPTED — proposed, the evidence RELOCATED to L2 with key Ruling 2's candidate; 44.28 (ii) — the match over the entry's whole stretch ADOPTED — proposed (the surface marks this half as the writing side's reading), the key motion as evidence of the local key RELOCATED to L2 with the sequence term at DP-O (D-504, D-505)"`.
The four lines, in this order, each with `<Q>` written out in full where it stands:
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1).* (i), its half on the name: **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1).* (i), its half on the evidence: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those two at Row 44.34;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1).* (ii), its half on the match over the entry's whole stretch: **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1).* (ii), its half on the key motion as evidence of the local key: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those two at Row 44.28. Each line ends with the closing quotation mark of `<Q>` followed by a period, as the lines
above it do. (Within each row, the two lines stand as two lines, each followed by a blank line, §3.1 item 2.)

**The count.** `*RULED DISPOSITION (`: **11** — 8 **ADOPTED — proposed**, 2 **RELOCATED**, 1 **HISTORICAL**. None
opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) each line quotes, as the record's
placement, the record's bullet whole, bold lead included — for §3.1's six, on the precedent of session 17's lines, which
quote the lead-rows record's §3.1 bold lead and the whole of its list of ADOPTED rows, and not that bullet's further
sentences, which place other rows RELOCATED and decided against; this record's §3.1 bullet is its list of ADOPTED rows
alone, so its bullet is quoted whole; for Row 8.94, its one-row bullet; for the split row-parts,
§3.3's bullet whole, since its one sentence places both rows' halves, as session 17 quoted the lead-rows record's §3.2
bullet whole for each of its six half lines; (2) the halves are named in the record's own words for each half (*"the
name"*, *"the evidence"*, *"the match over the entry's whole stretch"*, *"the key motion as evidence of the local
key"*), each after *"its half on"*, the shape of session 17's half lines; (3) both RELOCATED lines take the destination
***L2 — The tonal reading. The one entangled decision.***, the record saying *"RELOCATED to L2"* for both, in the form
the earlier stretches' ruled RELOCATED lines use (for example Row 44.34's line on claim (ii)'s use half, written by
session 17); what travels with each (*"with key Ruling 2's candidate"*; *"with the sequence term at DP-O (D-504,
D-505)"*) stands inside `<Q>` and in the §10 entries (§3.3).

**What this stretch gives no line** (Task 3 (a)), as §L.31 names them:
- **The ten §3.2 row-parts — Rows 8.18, 8.32, 8.49, 8.51, 19.38 (vi), 19.39 (v), 44.10 (i), 44.16, 44.20 (i) and 44.50
  (iii):** *"No line from this record; listed in the report"*, as Ruling 1 of
  `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part2_sitting.md` rules it
  (§L.31's table and its *Open* point (2)). Each is listed in the report under *rows given no line now*, with §L.31 and
  those words; each keeps its proposal.
- **The eight §3.4 row-parts — Rows 8.33, 8.92, 8.93, 44.36 (i), 44.44, 44.45, 46.18 (ii) and 46.19 (iii):** *"No line
  from this record."* Not listed under *rows given no line now* (Task 3 (a): that name covers the row-parts a §L entry
  lists in the report, and §L.31 does not list these).
- **Row 46.43 (§3.6):** *"No line from this record."* The record moves it to the idiom-tag surface; it is met at the
  idiom-tag records' entries. Not listed under *rows given no line now*.
- **The sixteen part-2 rows §L.31's check sum names** (57.97 to 57.490 (i), the record's §2): carried to §L.32, no line
  from this record, not touched.
- **The other claims of the rows this stretch writes** — Rows 8.52 (i) and (ii), 44.20 (i), 44.33 (ii), 44.37 (ii),
  44.34 (ii), 44.28 (i) and (iii) — get nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — two entries appended

- **Item 5: two RELOCATED halves, neither of which §10 carries.** The writing side searched §10 (lines 79893–80983)
  for every row number of this stretch as a bare number with look-around. The hits: Row 44.33 (ii) and Row 44.37 (ii)
  (in the entry for *"Rows 44.5, 44.6, …"*, line 80507; Row 44.37 (ii) again at lines 80513 and 80616), Row 44.28 (i)
  (the entry for *"Rows 44.17, 44.18, …"*, lines 80518 and 80524) and Row 44.34 (ii) (session 17's entry, line 80620) —
  each **another claim** of the row, none a row-part of this stretch. Read **by claim**, as session 17 read item 5's
  *"a row §10 already carries is not appended again"* (session 17's instruction §3.3, the writing side's settlement,
  overrulable by the user). **The two entries, appended in the order §3.2 gives the halves, under
  `**To *L2 — The tonal reading. The one entangled decision.***`, directly after that heading's last entry** (the line
  opening `- Row 46.46 (i), its "ranked" half — that the catalog returns ranked structural matches.`, line 80621 at the
  writing side's staged copy) **and before the blank line that precedes `**To *the second axis — voice leading*.**`**;
  no blank line between them, as §10's own entries stand:
  ```
  - Row 44.34 (i), its half on the evidence — that the recognition of a named progression yields evidence. *(cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1; with key Ruling 2's candidate.)*
  - Row 44.28 (ii), its half on the key motion as evidence of the local key — that a single internally-sequential entry's implication of a key motion is carried by its schema span. *(cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md, Ruling 1; with the sequence term at DP-O (D-504, D-505).)*
  ```
  Each subject clause is the writing side's, in §10's entry form (*"<the row's subject in one clause>"*), from the row's
  own claim; each parenthesis names the record and ruling and, after the semicolon, what travels with the half, in the
  record's words. Before appending each, search §10 with the Grep tool for its row number and claim; if §10 already
  carries that half, do not append it and report it. If the heading is not found exactly once, STOP and report before
  writing anything at §10.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 80984–83136) for
  every row number of the 9 rows found none. Run the same search with the Grep tool; if you find an entry for a row-part
  of this stretch, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.31 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.32 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 8 commit, as in sessions 11 to 17.
   Attribute it in the diff table to *"session 18's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.31
   only**, after sessions 10 to 17's §L.1 to §L.30. §L.32 to §L.55 are not applied, read or touched.
3. **A1, for four paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1214, 1215, 1216 and 1217 ARE landed**, with this file, in §5 act 1, as sessions 8 to 17 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the record this stretch
   enters (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The
   writing side's search: **none of the three, in either search** (as §L.31's *The act's search* says). Item 2: not
   reached. Item 3: not reached. Item 4: not reached. **Item 5: two entries appended (§3.3).** Item 6: nothing written
   (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 8 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before the entry is applied, do not commit; STOP and report
   which lines were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 8 commit:**
     `git diff e61ad38abad3fcf6637f668c55defe0aef5fe3e6 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session18_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; a §10 entry of §3.3; the in-progress line of §3.5 item 3; and a NOT
     QUARANTINED line only if §3.4 (b) found an entry. Then
     `git diff --numstat e61ad38abad3fcf6637f668c55defe0aef5fe3e6 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 25 added lines and 1 deleted line** (the 11 lines and their 11 blank lines, 22; the two §10
     entries, 2; the in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2
     that was STOP-and-report, less 1 added for each §10 entry not appended**, plus 1 added for each NOT QUARANTINED line
     §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,047 added lines and 4 deleted lines** (`1047` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 17 the file stood at 1,023 added and 4 deleted against the Task 2
     commit (session 17's instruction §4 item 8, and entry 1215 §3 note (a) [relayed by derivation]); this stretch adds
     24 lines. The in-progress line replaces a line that is itself an addition against the Task 2 commit, so it adds no
     line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **438** (427 + 11, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting` **13** (the 11 lines and the two §10 entries;
     less 1 for each line that was STOP-and-report or §10 entry not appended, plus 1 for a NOT QUARANTINED line naming
     it), `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting` **23** (unchanged).
   - **Then, if every line of §3.2 and both §10 entries were written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`27e0d551e284fc33895803a98e83ace15859bbe6`** — the blob of the writing side's simulated edit (§8 below: 5,286,365
     bytes, 84,486 lines, line feeds only). A different blob with every count above as given means a byte differs
     somewhere in what was written: do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 9 (§L.31): the 11 lines of the catalog recognition's part 1 row-parts written in the reading file under their ratification, two RELOCATED halves appended to the transfer list, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_18_task_3_stretch_9_2026_11_24.md`**, as sessions 2 to 17
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.32, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's five files first, in a commit of their own, before any edit to the reading file.**
   Exactly five paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_fourteen.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_fifteen.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_sixteen.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seventeen.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1214, 1215, 1216 and 1217 and the session 18 instruction of the L3 application landed; Task 3 stretch 9 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: §L.31, for each row-part (and
   each half), the row check of §3.1 item 4 and the word check of §3.1 item 5, then its line of §3.2; then the §10
   entries of §3.3 and the search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_18_task_3_stretch_9_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 18 of the L3 application, Task 3 stretch 9 (§L.31) written; stretch 10 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 11 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 8.52, 44.34, 44.28 and 44.37 and as one sentence
   for the other five if they were as stated; the two §10 entries of §3.3, each appended (with its line number) or not
   (and why), and the §10 search; the §11 search of §3.4.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (the ten §3.2 row-parts, each with §L.31 and the words that list it); *recorded lines not written:
   no disposition word* (none expected); *rows named by more than one record* (Rows 8.52, 19.38, 19.39, 44.34, 46.18 and
   46.19, as §3.1 item 8 says); *ADOPTED words read at the row* (all 8 ADOPTED lines, each with the proposed word read
   and that its line does not say *as proposed*); *audit questions added* (none); *audit questions no longer
   quarantined* (none expected); *§10 rows a record says leave, not named by row* (none: the record does not say a row
   leaves §10); the decided-against search (§4 item 4), with its result.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph, each with §L.31.
   *A heading of this session's report only, as in sessions 10 to 17's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 18 of the L3 application ends here. Stretch 10 of Task 3 is not begun. Nothing else was done."*

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

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1215. Read at the objects for this file: the three git
reference files (both refs `03a15953…`); entries 1215, 1214, 1213, 1212 whole and 1026 §3; session 17's instruction
whole (its blob computed on the staged copy, `29c2d8cc…`, 50,719 bytes, 536 lines, equal to entry 1215's); the record
whole (blob `04cab0e5955e8b627f9e1719f6ee20012714bf76`, 7,479 bytes, 92 lines, no carriage return); the big dispatch at
lines 3251–3449 (§L.31, and §L.32 for sizing only) and 6640–6652 (Task 3 (a), the *rows given no line now* sentence),
its blob recomputed on the staged copy (`b5274c2c…`, 7,157 lines). The reading file, by read-only scripts over the
staged copy: its blob computed as git would (`b98e8512…`, 5,280,457 bytes, 84,462 lines, no carriage return); its `##`
headings; each of the 9 rows found exactly once by its heading, inside §6, and read whole from its heading to its
closing `---`, its shape and its proposed word for the part named as §3.1 items 2 and 5 state; the ten §3.2 rows'
headings found exactly once each (not read; the §3.4 rows not searched); §10's destination headings, the L2 heading found
exactly once in the file, the end of the L2 block at lines 80610–80623; §10 and §11 searched for every row number of
the 9 rows as a bare number with look-around; the in-progress line at line 54 in full. Every quotation of §3.2 checked
against the record by a read-only script (line breaks joined, asterisks removed): each found exactly once. The record
searched for the three decided-against phrases (line breaks joined, case matched and not): none. **The edit simulated
on a copy of the reading file in the container** by §3.1 item 2's placement rule, §3.3's placement and §3.5 item 3's
line gives, against the staged file, **25 added lines and 1 deleted**, the counts **438 / 3 / 53 / 26 / 1 / 1**, the
record names **13** (part 1) and **23** (lead rows), and the blob **`27e0d551…`** (5,286,365 bytes, 84,486 lines); each
new line's place in the copy read back. Relayed, not re-checked here: the archive JSON's blob `1df4f207…` and the
untracked paths (session 17's instruction §1 item 5); the stretch 8 commit `e61ad38a…` as session 17's act 2 and the
reading file's blob in it (entry 1215 §2 item 2, checked there at the objects); the end of `cowork_handoff.md`'s topmost
block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 17's
instruction gives them); the 1,023 added and 4 deleted lines against the Task 2 commit after session 17 (entry 1215,
by derivation).*

*The check, as a turn of its own: Cowork, 2026-11-24 (Stockholm), the next sitting, booted on entry 1216, the file not
yet handed to Claude Code, so its corrections keep no former wording (as the checks of sessions 16 and 17 did). The
hash measurement ran, unrefused: a `python3 -I` script, its file under `/home/claude/scr`, the paths passed as
arguments, over staged copies. Checked at the objects, over staged copies: the three git reference files (both refs
`03a15953…`); this file as landed (blob `c4f4722d…`, 44,317 bytes, 484 lines, no carriage return, equal to entry
1216's); the blobs of the big dispatch (`b5274c2c…`, 941,330 bytes, 7,157 lines), the record (`04cab0e5…`, 7,479 bytes,
92 lines), the reading file (`b98e8512…`, 5,280,457 bytes, 84,462 lines) and session 17's instruction (`29c2d8cc…`),
none with a carriage return; the archive JSON's staged copy carries carriage returns and its blob with them changed to
line feeds is `1df4f207…`, the value §1 item 5 gives; the record read whole; the three quotations of §3.2 and the four
half-names each found in the record (line breaks joined, asterisks removed), each quotation exactly once; the
decided-against search over the record (none of the three, case matched or not); each of the 9 rows found exactly once
by its heading, inside §6, and read whole from its heading to its closing `---`, its shape, its proposed word for the
part named (UNPLACED at each) and its fit with the record's gloss as §3.1 items 2, 4 and 5 state; the headings of the ten
§3.2 rows, the eight §3.4 rows and Row 46.43 each found exactly once; the reading file's `##` headings at the lines §2
item 9 gives; §10's destination headings, the L2 heading found exactly once, the end of the L2 block at lines
80617–80623; §10 and §11 searched for every row number of the 9 rows as a bare number with look-around, the §10 hits
read and each another claim, as §3.3 says, and no §11 hit; line 54 in full; the big dispatch at lines 3251–3343
(§L.31) and 6638–6653 (Task 3 (a) and (b)), the headings that open §L (line 395), §L.31 (3251), §L.32 (3344), Task 3
(6616), Task 4 (6821), *What this batch does NOT do* (7111) and the self-check after it (7136), at the lines §2 item 8
gives, and line 98's length (4,383 bytes); the row lists of §3.2's last paragraph and §3.1 item 8 against §L.31's table and its *Rows named
by more than one record*; the 427 existing ruled lines, each naming its record by bare file name; the lead-rows record's
§3.1 and §3.2 bullets, against session 17's lines. **The edit simulated again on a copy, from this file's own text** (the
lines of §3.2 with `<claim>` and `<Q>` filled in, the two §10 entries of §3.3, the line of §3.5 item 3), by §3.1 item
2's placement rule and §3.3's placement: 25 added and 1 deleted, the counts 438 / 3 / 53 / 26 / 1 / 1, the record names
13 and 23, and the blob `27e0d551…` (5,286,365 bytes, 84,486 lines); each new line's place read back at Rows 8.52,
44.34, 44.28 and 44.37. **Relayed, not computed:** the Task 2 commit `4b6dc3bd…` (the same text session 17's instruction
gives for the same object), the stretch 8 commit `e61ad38a…` (entry 1215 §2 item 2, checked there at the objects), the
1,023 and 4 against the Task 2 commit (by derivation), the untracked paths and the precedents of sessions 8 to 16, the
end of `cowork_handoff.md`'s topmost block at line 255 and the start of `cowork_audit_protocol.md`'s dispatch-protocol
section at line 180. Claude Code's own checks (§1 checks 2, 4 and 5; §4 item 8) stop on any of them before the reading
file is touched or committed. Corrected: §3.2's settlement (1), which said session 17's lines quote the lead-rows
record's *"bold lead and list whole"*, now saying exactly what they quote (the bold lead and the whole list of ADOPTED
rows, not that bullet's further sentences); and, as entry 1216 §3 step 1 asked, handoff entry 1217 added to what act 1
lands (§1 item 5, §4 item 3, §5 act 1 and its commit subject), the writing side's settlement and overrulable by the
user. No line of §3.2, row, disposition word, command or count the reading file is checked against changed; what
changed with entry 1217's landing is the number of files act 1 lands (four to five), A1's paths in §4 item 3 (three to
four), and act 1's commit subject.*
