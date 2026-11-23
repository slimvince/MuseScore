# CC dispatch — the L3 application, SESSION 17 of several: Task 3 of the L3 application dispatch, eighth stretch (§L.29 to §L.30), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twelve.md`; CHECKED AS A TURN OF ITS OWN AND
> CORRECTED 2026-11-24 by the sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirteen.md` (see the check note at the end);
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
called **the Task 2 commit** below). Sessions 10 to 15 applied Task 3's first six stretches, §L.1 to §L.24. Session 16
applied the seventh stretch, §L.25 to §L.28, in commit `a3624335004095deb1cc663749b65d8e84adcdb6` (called **the
stretch 7 commit** below), and committed its report as `8771c9b88e6c2434698fbf4c9ce523694e7cd506`, the current tip.

**This is session 17. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for TWO ledger entries: §L.29 and §L.30, the first two
records of family 1 (the catalog of named progressions). It commits and pushes that eighth stretch, writes its report,
and STOPS.** §L.31 is a later session's.

**What this stretch writes, in one paragraph.** **§L.29's record places no row, so it gives no line.** **§L.30's record
gives 19 lines, all opening `*RULED DISPOSITION (` and all naming Ruling 1 of
`cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md`, on 15 rows:** 14 lines with the word **ADOPTED — proposed**
(the eleven row-parts of the record's §3.1, Row 38.20 getting two; and the published-match half of each of the three
split row-parts of its §3.2), 4 lines with the word **RELOCATED** (Row 44.19 (iii), and the use half of each of the
three split row-parts), and 1 line with the word **HISTORICAL** (Row 38.79 (i), form (b-H)). **No line says *as
proposed*:** every one of these row-parts is proposed UNPLACED at its row. §3.2 gives every line with its exact text.
**At §10, four entries are appended** under the L2 heading, one for each RELOCATED row-part (§3.3). **Nothing at §11**
(§3.4). And the in-progress line brought forward from §L.28 to §L.30 (§3.5).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the placements the record
already makes; it decides nothing. §L.29's three charter amendments are Task 4's, not this session's (§4 item 2).

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `8771c9b88e6c2434698fbf4c9ce523694e7cd506`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_17_task_3_stretch_8_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 7 commit left it.**
   `git diff --quiet a3624335004095deb1cc663749b65d8e84adcdb6 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 8771c9b88e6c2434698fbf4c9ce523694e7cd506 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `7103b87c3300f977f30b440b986303756eb46a68`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **408**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; and each of `cowork_rulings_2026_11_06_l3_catalog_key_sitting` and
   `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting` must count **0**. Any other result: STOP and report, the file
   not touched. (The writing side's staged copy: 5,273,149 bytes, 84,420 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 8771c9b88e6c2434698fbf4c9ce523694e7cd506 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the five files §5 act 1 lands (this instruction and handoff entries 1210, 1211, 1212
     and 1213), plus the paths sessions 2 to 16 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twelve.md` (written by the sitting before
   the one that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eleven.md` (the one before it, written by
   the sitting that verified session 16; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The two records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening). Both under `records/cowork/rulings/`:
   - `cowork_rulings_2026_11_06_l3_catalog_key_sitting.md` (§L.29; 8,881 bytes, 113 lines);
   - `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md` (§L.30; 5,819 bytes, 82 lines).
   **Do NOT read the records of §L.1 to §L.28 or of §L.31 to §L.55, and do not open the two records' surfaces** (the
   lines quote the record only).
8. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, and form (b-H)**, the premise ledger, the declared start state, the standing bars, the
     findings rule);
   - lines 395–430 (how §L is written);
   - **lines 3040–3250 (§L.29 and §L.30, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3039 (§L.1 to §L.28, applied); lines 3251–5906 (§L.31 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary);
   - **each of the 15 rows §3.2 names, whole, at §6** (lines 435–79396): find each by its heading with the Grep tool,
     pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
     heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
   - §10 (lines 79855–80941): its destination headings (lines opening `**To `), and the whole block under
     ***L2 — The tonal reading. The one entangled decision.*** from its heading (line 80057) to the next heading (line
     80581) at least from line 80460 on; and §10 searched with the Grep tool for every row number of this stretch
     (§3.3);
   - §11 (lines 80942–83094), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch, and form (b-H) for Row 38.79 (i): one line ADDED to the row, the row's
   `*PROPOSED DISPOSITION.*` paragraph and every other sentence of the row untouched. Every line names
   `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1` (the record has one ruling), the record file
   written as its bare file name, as sessions 10 to 16 wrote theirs. Where §3.2 names a claim, the line names it (form
   (b)'s split-row rule); otherwise the line names none. **Each row-part, and each half of a split row-part, gets exactly
   one line**, so four rows get two lines from this stretch: Row 38.20 (claims (i) and (ii)) and Rows 38.21, 44.34 and
   46.46 (the two halves of one claim each, §3.1 item 7).
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"The
   decisions register at this row."*). Each new line is followed by one blank line. Read each row's actual shape from
   its proposed paragraph to its end before writing. **The writing side read all 15 rows at the staged copy; every one
   ends with a blank line and then `---`, and none carries an earlier `*RULED …` or `*RECORDED …` line.** Their shapes
   after the proposed paragraph:
   - **13 rows: nothing after the proposed paragraph** — 46.16, 46.17, 46.20, 46.21, 46.23, 44.2, 44.21, 38.20, 44.19,
     38.79, 38.21, 44.34, 46.46. Each such row ends, after the edit: proposed paragraph, blank line, **the new line(s),
     each followed by a blank line**, `---`.
   - **2 rows with a paragraph headed *"The decisions register at this row."* after the proposed paragraph; the new line
     goes directly beneath the proposed paragraph, above it:** Rows 46.18 and 46.19.
   - **Four rows get two lines from this stretch:** Row 38.20, claim (i)'s line first; and Rows 38.21, 44.34 and 46.46,
     the published-match half's line first (the order in which the record names the halves).
   If you find a different shape at a row (an earlier line, a further paragraph, or an ending other than `---`), state
   it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, that line
   is a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it, from the record's §1 (*"Ruling 1 — the lead
   row-parts' placements RATIFIED as the surface states them"*): for §3.1's eleven ADOPTED row-parts, the bullet's bold
   lead and the list after it; for Row 44.19 (iii), the bullet's second sentence; for Row 38.79 (i), its third sentence;
   for the three split row-parts, §3.2's bullet whole, its bold lead included. **The writing side checked every
   quotation against the record by a read-only script (words and punctuation, line breaks read as spaces, asterisks not
   compared): each found exactly once.** Before writing each line, find each of its quoted passages in the record
   yourself and compare it the same way: every word and every punctuation mark must match, line breaks read as spaces.
   The line keeps its marks exactly as §3.2 gives them (the record's spelling *"travelling"* is kept inside the
   quotation). A difference is a STOP-and-report for that line: no line written, listed in the report under *rows the
   act could not place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that part is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The record's §1 names the rows and their
   dispositions, says of Row 44.19 (iii) that it *"is wholly the use as evidence"* (surface §3.1 note 3), and states the
   method that stands; it does not say what each other part is about. That is in its §0 and in Ruling 1 of
   `cowork_rulings_2026_11_06_l3_catalog_key_sitting.md` (L3 publishes, as a read-off fact, which entries of the catalog
   of named progressions fit which stretches of L2's decided chords; the catalog is fixed reference knowledge L3 reads)
   and that record's Ruling 2 (the use of the catalog as evidence for choosing chords, a named candidate at the DP-O
   note). So the fit is: each ADOPTED row-part's outgoing statement is about the catalog's entries, its terms, or its
   standing as reference knowledge beside the layers; each RELOCATED row-part's (or half's) is about the recognition's
   use as evidence in choosing chords; Row 38.79 (i)'s says *"the preset selects it"*. A row that does not fit is a
   STOP-and-report for that row-part: no line, listed under *rows the act could not place* with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.30's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **The record names the
   word in full** for the fourteen ADOPTED lines (*"ADOPTED — proposed:"* before §3.1's eleven; *"the half on the
   published match ADOPTED — proposed under L3"* for §3.2's three), so item (1) of the paragraph gives **ADOPTED —
   proposed**. For the four RELOCATED lines and the HISTORICAL line the record names the word itself (*"RELOCATED to
   L2"*; *"Decided against"*, which form (b-H) writes HISTORICAL). **The writing side read the proposed paragraph at every
   one of the row-parts this stretch names: each is UNPLACED** (for the split rows, at the claim named: Rows 46.18 (i),
   46.19 (i), 46.21 (ii), 38.20 (i) and (ii), 44.19 (iii), 38.79 (i), 38.21 (i), 44.34 (ii), 46.46 (i)). So no line's
   word is the row's own proposed word, and **no line says *as proposed***: the paragraph's *"Otherwise as proposed is not
   written, and the placement is given in the record's words"*. If you find a row-part's proposed word for the part named
   other than UNPLACED, that line is a STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of
   the 14 ADOPTED lines is listed in the report under *ADOPTED words read at the row*, with the proposed word read
   (UNPLACED) and that its line does not say *as proposed*.
6. **The HISTORICAL line, form (b-H).** The record decides against Row 38.79 (i) *"in so far as a preset selects the
   catalog L3 reads"* and sends the remainder (*"idiom-specific"*) with the idiom-tag rows. The line names claim (i) and
   quotes the record's sentence, which itself names the part decided against, on the shape of the earlier stretches'
   partial HISTORICAL lines (for example the reading file's lines 1331 and 1335 at the writing side's staged copy:
   `(ii) **HISTORICAL** — "recorded as decided against **in so far as …**"`). The remainder gets no line from this
   record (§L.30's table; its *Open* point (4): it is met at the idiom-tag records' entries). Claim (ii) of Row 38.79 gets
   nothing from this stretch.
7. **The split row-parts, by half.** The record's §3.2 bullet places each of Rows 38.21 (i), 44.34 (ii) and 46.46 (i) in
   two halves: *"the half on the published match"* ADOPTED — proposed, and *"the half on use as evidence (for 46.46 (i),
   the "ranked" half)"* RELOCATED to L2. Each line names its claim and its half in the record's words, on the shape of
   the earlier stretches' half lines (for example the reading file's line 9925 at the writing side's staged copy:
   `(ii), its phrase half: **ADOPTED — carried** (L3-S8) — "…"`): `(i), its half on the published match:`,
   `(i), its half on use as evidence:` and, for Row 46.46, `(i), its "ranked" half:`. The two lines of one row-part fall
   on different parts, so form (b)'s two-record rule is not engaged (both are this record's).
8. **Rows named by more than one record** (form (b)'s two-record rule, by part). **None of the 15 rows carries an earlier
   record's line** (the writing side read every one at the staged copy, §3.1 item 2). §L.29 names Rows 7.85, 38.79 (i),
   38.21 (i), 44.19 (iii), 44.34 (ii) and 46.46 (i) and places none of them, so it gives them no line and the rule is not
   engaged by it (§L.30, *Rows named by more than one record*). List those six in the report under *rows named by more
   than one record*, each saying that §L.29 names it and gives no line. If you find an earlier record's line on any part
   this stretch writes, apply the rule by part as the big dispatch gives it; if an earlier stretch's line would have to
   be deleted or edited, STOP, do not commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several row-parts, `<claim>` is filled in
from the row list (written `(i)`, `(ii)` as the list gives it); where the list gives no claim, `<claim>` and the space
after it are dropped.

**§L.29 — the catalog key record (`cowork_rulings_2026_11_06_l3_catalog_key_sitting.md`): no line.** The record places
no row (its §3; §L.29, *Reading file — rows*).

**§L.30 — the catalog lead-rows record (`cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md`): 19 lines.**

*§3.1's ADOPTED row-parts — 11 lines, none* as proposed. Row-parts, in this order: 46.16; 46.17; 46.18, written `(i)`;
46.19, written `(i)`; 46.20; 46.21, written `(ii)`; 46.23; 44.2; 44.21; 38.20, written `(i)`; 38.20, written `(ii)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — "§3.1, follow wholly (13): ADOPTED — proposed: 46.16, 46.17, 46.18 (i), 46.19 (i), 46.20, 46.21 (ii), 46.23, 44.2, 44.21, 38.20 (i), 38.20 (ii)".
```

*Row 44.19 (iii) — 1 line, RELOCATED:*
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (iii) **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "RELOCATED to L2 (*The tonal reading. The one entangled decision.*): 44.19 (iii), with parts (i) and (ii) of the same row".
```

*Row 38.79 (i) — 1 line, HISTORICAL, form (b-H):*
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (i) **HISTORICAL** — "Decided against in so far as a preset selects the catalog L3 reads: 38.79 (i), the remainder ("idiom-specific") going with the idiom-tag rows".
```

*§3.2's split row-parts — 6 lines, two per row-part, the published-match half first.* Every one of the six quotes the
same passage, written here once as `<Q>`:
`"§3.2, split by use (3): 38.21 (i), 44.34 (ii), 46.46 (i) — in each, the half on the published match ADOPTED — proposed under L3, the half on use as evidence (for 46.46 (i), the "ranked" half) RELOCATED to L2, travelling with the DP-O candidate of the key sitting's Ruling 2"`.
The six lines, in this order, each with `<Q>` written out in full where it stands:
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (i), its half on the published match: **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (i), its half on use as evidence: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those two at Row 38.21;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (ii), its half on the published match: **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (ii), its half on use as evidence: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those two at Row 44.34;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (i), its half on the published match: **ADOPTED — proposed** — <Q>.
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1).* (i), its "ranked" half: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — <Q>.
```
— those two at Row 46.46. Each line ends with the closing quotation mark of `<Q>` followed by a period, as the lines
above it do. (Within each row, the two lines stand as two lines, each followed by a blank line, §3.1 item 2.)

**The count.** `*RULED DISPOSITION (`: **19** — 14 **ADOPTED — proposed**, 4 **RELOCATED**, 1 **HISTORICAL**. None
opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) each line quotes, as the record's
placement, the record's own words naming the row-parts and the disposition: for §3.1's eleven, the bold lead and the
list (on the precedent of session 16's lines, which quote each part's bold heading with its row list); for Row 44.19
(iii) and Row 38.79 (i), each its own sentence of the bullet, without the bullet's bold lead, because each sentence
names its row and its disposition itself; for the split row-parts, §3.2's bullet whole, since its one sentence places
both halves; (2) the halves are named in the record's words (*"the half on the published match"*, *"the half on use as
evidence"*, *"the "ranked" half"*), not in the surface's (*"for the published name"*, *"for the evidence"*, *"holds
structural content"*, *"returns ranked matches"*), the record governing; (3) the RELOCATED lines take the destination
in the form the earlier stretches' ruled RELOCATED lines use (for example the reading file's line 1303 at the writing
side's staged copy: `**RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "…"`).

**What this stretch gives no line** (Task 3 (a)), as §L.29 and §L.30 name them:
- **§L.29:** the record places no row. It names Rows 7.85, 38.79 (i), 38.21 (i), 44.19 (iii), 44.34 (ii) and 46.46 (i)
  and does not place them (each is placed, or given no line, by §L.30), and names Row 38.80 at its §5 without placing
  it. No line from §L.29 for any of them.
- **§L.30, the five §3.3 row-parts — Rows 7.85, 46.1 (i), 46.8 (ii), 44.1 and 44.39:** *"No line from this record;
  listed in the report"*; each keeps its proposal and is listed under *rows given no line now* (Task 3 (a)).
- **§L.30, the four §3.4 row-parts — Rows 46.37, 46.45, 38.22 (ii) and 38.22 (i):** *"No line from this record."*
  **Row 38.22 (i) is listed in the report under *rows given no line now*** (Task 3 (a), which names it by §L.30, under
  the user's ruling *"A"*); Rows 46.37, 46.45 and 38.22 (ii) are not listed there (they are met at §L.36 and §L.39).
- **§L.30, parts (i) and (ii) of Row 44.19:** no line from this record; each keeps its proposed **RELOCATED** to
  ***L2 — The tonal reading. The one entangled decision.***, as a proposal; not STOP-and-report (§L.30's *Open* point
  (2), answered at release by Ruling 19 of the part 2 ruling record).
- **§L.30, the remainder of Row 38.79 (i)** (*"idiom-specific"*), and Row 38.79 (ii): no line from this record.
- **The other claims of the split rows** — Rows 46.18 (ii), 46.19 (ii) and (iii), 46.21 (i), 38.21 (ii), 44.34 (i),
  46.46 (ii) — get nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — four entries appended

- **Item 5: four RELOCATED row-parts, none of which §10 carries.** The writing side searched §10 (lines 79855–80941) for
  every row number of this stretch as a bare number with look-around. The hits: Rows 44.19 (i) and 44.19 (ii) (in the
  entry for *"Rows 44.5, 44.6, …"*, line 80468), Row 46.46 (ii) (the entry for *"Rows 46.39, 46.41, …"*, line 80504) and
  Row 46.21 (i) (under the second axis: the entry for *"Rows 46.21 (i), 46.22, …"*, line 80651, and again inside the
  entry for *"Rows 53.7 (ii), 53.12 (ii), …"*, at line 80657, *"(As Rows 46.21 (i), …)"*) — each **another claim** of
  the row, none a row-part of this stretch. *The writing side's settlement, overrulable by the user:* item 5's *"Check each at §10 by row number before
  appending; a row §10 already carries is not appended again"* is read **by claim**, so §10 carrying Rows 44.19 (i) and
  (ii) and Row 46.46 (ii) does not count as carrying Row 44.19 (iii) or Row 46.46 (i) — on the shape of form (b)'s
  two-record rule and item 6, which act by part since release. **The four entries, appended in ledger order (the order
  of §L.30's table) under `**To *L2 — The tonal reading. The one entangled decision.***`, directly after that heading's
  last entry** (the line opening `- Row 38.11 (i) — the key-independent chord symbol for each slice`, line 80579 at the
  writing side's staged copy) **and before the blank line that precedes `**To *the second axis — voice leading*.**`**;
  no blank line between them, as §10's own entries stand:
  ```
  - Row 44.19 (iii) — that no stage is added for the recognition of a named progression. *(cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1; as Rows 44.19 (i) and (ii).)*
  - Row 38.21 (i), its half on use as evidence — the catalog consumed by the old function layer (the progression prior / substitution-inversion). *(cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1; travelling with the DP-O candidate of the key sitting's Ruling 2.)*
  - Row 44.34 (ii), its half on use as evidence — that the recognition of a named progression, as evidence, adds no new layer. *(cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1; travelling with the DP-O candidate of the key sitting's Ruling 2.)*
  - Row 46.46 (i), its "ranked" half — that the catalog returns ranked structural matches. *(cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md, Ruling 1; travelling with the DP-O candidate of the key sitting's Ruling 2.)*
  ```
  Each subject clause is the writing side's, in §10's entry form (*"<the row's subject in one clause>"*), from the row's
  own claim; each parenthesis names the record and ruling and, after the semicolon, what travels with the row-part, in
  the record's words. The record's spelling *"travelling"* is kept, as in the lines. Before appending each, search §10
  with the Grep tool for its row number and claim; if §10 already carries that row-part, do not append it and report
  it. If the heading is not found exactly once, STOP and report before writing anything at §10.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row-part of this stretch. The writing side's search of §11 (lines 80942–83094)
  for every row number found only Row 46.19 (ii) (line 82967), another claim, not touched (item 7 (b): *"A §11 entry
  naming another claim of the row is not touched"*). Run the same search with the Grep tool; if you find an entry for a
  row-part of this stretch, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.30 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.31 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 7 commit, as in sessions 11 to 16.
   Attribute it in the diff table to *"session 17's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.29 and
   §L.30 only**, in that order, after sessions 10 to 16's §L.1 to §L.28. §L.31 to §L.55 are not applied, read or
   touched. §L.29's three charter amendments (*Open* point (2)) are Task 4's, under its *Not written* item 2, and its
   *Open* points (1) and (3) are answered at release with no listing of their own in the report (Rulings 28 and 24 of
   the part 2 ruling record, as §L.29 gives them): this session writes nothing for any of the three.
3. **A1, for four paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1210, 1211, 1212 and 1213 ARE landed**, with this file, in §5 act 1, as sessions 8 to 16 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the two records this stretch
   enters (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case not matched). The
   writing side's search: in the key record, none; in the lead-rows record, **one hit, its line 36**, *"Decided
   against"*, found only when case is not matched, naming Row 38.79 (i) — the hit §L.30 places, so it is written as
   §L.30 says (the HISTORICAL line of §3.2) and listed in the report with that line. Neither *"decides against"* nor
   *"decide against"* occurs. Item 2: not reached. Item 3: not reached. Item 4: not reached. **Item 5: four entries
   appended (§3.3).** Item 6: nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 7 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear before both entries are applied, do not commit; STOP and report
   which entries were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 7 commit:**
     `git diff a3624335004095deb1cc663749b65d8e84adcdb6 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session17_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; a §10 entry of §3.3; the in-progress line of §3.5 item 3; and a NOT
     QUARANTINED line only if §3.4 (b) found an entry. Then
     `git diff --numstat a3624335004095deb1cc663749b65d8e84adcdb6 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 43 added lines and 1 deleted line** (the 19 lines and their 19 blank lines, 38; the four §10
     entries, 4; the in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2
     that was STOP-and-report, less 1 added for each §10 entry not appended**, plus 1 added for each NOT QUARANTINED line
     §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,023 added lines and 4 deleted lines** (`1023` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 16 the file stood at 981 added and 4 deleted against the Task 2
     commit (session 16's instruction §4 item 8, and entry 1211 §2 item 1, which derived it [relayed by derivation]);
     this stretch adds 42 lines. The in-progress line replaces a line that is itself an addition against the Task 2
     commit, so it adds no line and deletes none there. The 4 deleted are the four lines session 10's state sentences
     were written into.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **427** (408 + 19, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting` **23** (the 19 lines and the four §10 entries; less 1 for
     each line that was STOP-and-report or §10 entry not appended, plus 1 for a NOT QUARANTINED line naming it),
     `cowork_rulings_2026_11_06_l3_catalog_key_sitting` **0**.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 8 (§L.29 to §L.30): the 19 lines of the catalog's lead row-parts written in the reading file under their ratification, four RELOCATED row-parts appended to the transfer list, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_17_task_3_stretch_8_2026_11_24.md`**, as sessions 2 to 16
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.31, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's five files first, in a commit of their own, before any edit to the reading file.**
   Exactly five paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_17_task_3_stretch_8_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_ten.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_eleven.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twelve.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirteen.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1210, 1211, 1212 and 1213 and the session 17 instruction of the L3 application landed; Task 3 stretch 8 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it, entry by entry in ledger
   order: §L.29 (no line; its rows listed as §3.2's last paragraph says), then §L.30: for each row-part (and each half),
   the row check of §3.1 item 4 and the word check of §3.1 item 5, then its line of §3.2; then the §10 entries of §3.3
   and the search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_17_task_3_stretch_8_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 17 of the L3 application, Task 3 stretch 8 (§L.29 to §L.30) written; stretch 9 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 19 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Rows 46.18 and 46.19 and as one sentence for the other
   13 if they were as stated; the four §10 entries of §3.3, each appended (with its line number) or not (and why), and
   the §10 search; the §11 search of §3.4.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (Rows 7.85, 46.1 (i), 46.8 (ii), 44.1 and 44.39, and Row 38.22 (i), each with §L.30 and the words
   that list it); *recorded lines not written: no disposition word* (none expected); *rows named by more than one
   record* (Rows 7.85, 38.79 (i), 38.21 (i), 44.19 (iii), 44.34 (ii) and 46.46 (i), each named at §L.29 with no line, as
   §3.1 item 8 says); *ADOPTED words read at the row* (all 14 ADOPTED lines, each with the proposed word read and that
   its line does not say *as proposed*); *audit questions added* (none); *audit questions no longer quarantined* (none
   expected); *§10 rows a record says leave, not named by row* (none: no record of this stretch says a row leaves §10);
   the decided-against search (§4 item 4), record by record, with its one hit and the line written for it.
5. The diff table of §4 item 8, every changed passage attributed, and the counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph, each with its §L
   entry. *A heading of this session's report only, as in sessions 10 to 16's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 17 of the L3 application ends here. Stretch 9 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a line of §3.2
  that is STOP-and-report under them or under §3.1 items 2 to 8 is reported and the rest of this stretch applied, as
  they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 8);
- the §10 heading of §3.3 is not found exactly once (§3.3);
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1212. Read at the objects for this file: the
three git reference files (both refs `8771c9b8…`); entries 1212, 1211 and 1026 whole; session 16's instruction whole
(its blob computed on the staged copy, `60c25745…`, 47,708 bytes, 540 lines, as entry 1211 gives it); session 15's
instruction at lines 128–189 and its headings; the two records whole; the lead-rows record's surface at its §3.1 and
§3.2 (lines 58–109), for the halves' naming only, the lines quoting the record; the big dispatch at lines 159–274 (the
forms), 3040–3250 (§L.29 and §L.30) and 6616–6820 (Task 3), its blob recomputed on the staged copy (`b5274c2c…`, 7,157
lines); the ranges before line 430 and the untracked paths as session 16's instruction gives them, the blob being the
same [relayed]. The reading file, by read-only scripts over the staged copy: its blob computed as git would
(`7103b87c…`, 5,273,149 bytes, 84,420 lines, no carriage return); its `##` headings; each of the 15 rows found exactly
once by its heading, inside §6, and read whole from its heading to its closing `---`; §10's destination headings, the
end of its L2 block (lines 80560–80581) and the entries holding Rows 44.19 (i) and (ii) and 46.46 (ii), and §10 and §11
searched for every row number as a bare number with look-around; earlier ruled lines of the RELOCATED, HISTORICAL and
half shapes found by search (lines 1303, 1331, 1335, 9925); the in-progress line at line 54; the six counts (408 / 3 /
53 / 26 / 1 / 1) and the two record names (0 each). Every quotation of §3.2 checked against the record by a read-only
script (line breaks joined, asterisks removed): each found exactly once. Both records searched for the three
decided-against phrases (line breaks joined, case matched and not): one hit, the lead-rows record, case not matched
only. The edit simulated on a copy of the reading file in the container by §3.1 item 2's placement rule, §3.3's
placement and §3.5 item 3's line gives, against the staged file, **43 added lines and 1 deleted**, and the counts
**427 / 3 / 53 / 26 / 1 / 1** and the record names **23 / 0**. Relayed, not re-checked here: the archive JSON's blob
`1df4f207…` and the untracked paths (session 16's instruction §1 item 5); the end of `cowork_handoff.md`'s topmost
block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 16's
instruction gives them); the 981 added and 4 deleted lines against the Task 2 commit after session 16 (entry 1211 §2
item 1, by derivation); the commit `a3624335…` as session 16's act 2 (entry 1211 §1).*

*The check, as a turn of its own: Cowork, 2026-11-24 (Stockholm), the next sitting, booted on entry 1213, the file not
yet handed to Claude Code, so its corrections keep no former wording (as session 16's check did). **The app's
permission check refused a read-only command that would have computed git blobs on the staged copies** (its stated
reason: *"Undermining Oversight"*). On the user's word ("continue", to the recommendation put), the check went on with
`wc`, `grep`, `awk`, `tr` and the file tools only; **no blob was computed, and no edit was simulated on a copy**.
Checked at the objects, over staged copies: the three git reference files (both refs `8771c9b8…`); the staged sizes
and modification times of the big dispatch (941,330), the reading file (5,273,149), session 16's instruction (47,708)
and the two records (8,881; 5,819), each as entry 1213 gives it; line counts by `wc -l`: the records 113 and 82, this
file 496 before this check's corrections, the reading file 84,420, the big dispatch 7,157; the two records read whole;
every quotation of §3.2 and the three half-names found exactly once in the lead-rows record (line breaks joined,
asterisks removed); the decided-against search over both records (one hit, the lead-rows record, case-blind only;
none in the key record); each of the 15 rows found exactly once by its heading, inside §6, and read whole from its
heading to its closing `---`, its shape and its proposed word for the part named as §3.1 items 2 and 5 state; §10's
destination headings, the L2 heading found exactly once in the file, and the end of the L2 block at lines 80570–80584;
§10 and §11 searched for every row number of this stretch as a bare number with look-around; the six counts (408 / 3 /
53 / 26 / 1 / 1) and the two record names (0 / 0); line 54 in full, the new in-progress line being it with *§L.28* and
*§L.29 to* moved on to *§L.30* and *§L.31 to*; the precedent lines 1303, 1331, 1335 and 9925; the big dispatch at
lines 118–125, 159–274, 3040–3250 and 6616–6820, its `##` and `###` headings outside §L, and line 98's length (4,383
bytes); the end of `cowork_handoff.md`'s topmost block at line 255 and the start of `cowork_audit_protocol.md`'s
dispatch-protocol section at line 180, both relayed until this check. **Derived by arithmetic, not simulated:** 43
added and 1 deleted against the stretch 7 commit (19 lines and their 19 blank lines, the four §10 entries, the replaced
in-progress line); the counts after, 427 / 3 / 53 / 26 / 1 / 1, none of the four §10 entries carrying a counted
pattern; the record names after, 23 / 0, the new text naming the key sitting only as *"the key sitting's Ruling 2"*;
1,023 and 4 against the Task 2 commit, from session 16's instruction's 981 and 4. **Relayed, not computed:** every full
hash in this file, each found as the same text in entry 1211 or session 16's instruction for the same object, the tip
also equal to the reference file. Claude Code's own checks (§1 checks 2, 4 and 5; §4 item 8) stop on any of them
before the reading file is touched or committed. Corrected: §3.3's account of the §10 hits, which left out Row 46.21
(i)'s second mention at line 80657; §3.1 item 4's *"names the rows and their dispositions only"*, wider than the
record's §1, which also states Row 44.19 (iii)'s note 3 and the method that stands; and, as entry 1213 §3 step 1 asked,
handoff entry 1213 added to what act 1 lands (§1 item 5, §4 item 3, §5 act 1 and its commit subject), the writing
side's settlement and overrulable by the user. No line of §3.2, row, disposition word or command changed, and no count
the reading file is checked against; what changed with entry 1213's landing is the number of files act 1 lands (four
to five), A1's paths in §4 item 3 (three to four), and act 1's commit subject.*
