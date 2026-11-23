# CC dispatch — the L3 application, SESSION 13 of several: Task 3 of the L3 application dispatch, fourth stretch (Row 7.67's held line, then §L.21 and §L.22), and nothing else

> **STATUS: WRITTEN 2026-11-23, NOT YET RELEASED,** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_two.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 and 11 applied Task 3's first two stretches, §L.1 to §L.12. Session 12
applied the third stretch, §L.13 to §L.20 (commit `6d26bee4cff5f93d553ea16dbc9e39f122383293`, called **the stretch 3
commit** below), and committed its report as `5ae0c46774f53e67b308a14df515561b89dcebd1`, the current tip.

**This is session 13. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for three things only, in this order: first the one line of
§L.15 that session 12 held back (Row 7.67) with its transfer-list line; then the ledger entries §L.21 and §L.22. It
commits and pushes that fourth stretch, writes its report, and STOPS.** §L.23 is the next session's.

**What this stretch writes, in one paragraph.** **21 lines, all opening `*RULED DISPOSITION (`**, each beneath the
`*PROPOSED DISPOSITION.*` paragraph of its row: Row 7.67's (form (b), §L.15), the twelve rows of the first-cut record's
Ruling 1 (§L.21) and the eight rows of the second-cut record's Ruling 1 (§L.22), all twenty of these HISTORICAL. §3.2
gives every one with its exact text. Beside them, at the transfer list §10: the *Row 7.67 is not transferred* line
(Task 3 (c) item 6), and **four *LEAVES L3* lines** (Task 3 (c) item 6), one beneath each §10 entry that names a row of
§L.21 or §L.22. And the in-progress line brought forward from §L.20 to §L.22. Nothing is added to §11 (§3.4).

**Why Row 7.67 comes first.** Session 12 held it as STOP-and-report: its instruction's text of the line had left out the
record's last sentence and put *"(L3-S40)"* outside the bold, where Ruling 5 of the part 2 ruling record has it inside.
Session 12 was right to stop. The text in §3.2 (a) below is Ruling 5's line, character for character (compared as a
whole line by the writing side, not only found inside the record). It is written first because it belongs to §L.15,
which comes before §L.21 in ledger order.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the dispositions the records
already place; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `5ae0c46774f53e67b308a14df515561b89dcebd1`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_13_task_3_stretch_4_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 3 commit left it.**
   `git diff --quiet 6d26bee4cff5f93d553ea16dbc9e39f122383293 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 5ae0c46774f53e67b308a14df515561b89dcebd1 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `40675143ebc02109b9534e271e9f135853f01db7`. Then, with the **Grep tool** counting matching lines in that file: `\*RULED DISPOSITION \(`
   must count **250**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(` must count **53**;
   `\*LEAVES L3 \(` must count **0**; `\*Row 7\.67 is not transferred` must count **0**. Any other result: STOP and
   report, the file not touched. (The writing side's staged copy: 5,217,818 bytes, 84,067 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 5ae0c46774f53e67b308a14df515561b89dcebd1 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1202 and 1203),
     plus the paths sessions 2 to 12 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_three.md` (the current entry point, written
   by the sitting that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_two.md` (the one before it, written by the
   sitting that verified session 12; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md` (§L.15, for Row 7.67 only; 8,964
     bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md` (§L.21; 6,889 bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md` (§L.22; 7,391 bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_item_six_reading_sitting.md` (5,402 bytes;
     Ruling 1: Task 3 (c) item 6 acts by claim).
   **Do NOT read the records of §L.1 to §L.20 (save the edge-of-span record) or of §L.23 to §L.55.**
8. **One side record, at these line ranges only, with the Read tool by offset** (each range located by the writing side
   at the staged copy, 2026-11-23; if a range does not open at the heading named, find the heading with the Grep tool and
   report the new range):
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes): **Ruling
   3** lines 89–125 (form (b)'s two-record rule applies by part); **Ruling 5** lines 162–210 (Row 7.67's line, at its
   line 187, and its §10 line, at its line 192).
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b) and its paragraph *Which ADOPTED word, and when
     as proposed is written* are the forms every line of this stretch is written in**, the premise ledger, the declared
     start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 1540–1634 (§L.15, for its table line and its *Open* point on Row 7.67 only)**;
   - **lines 2252–2397 (§L.21 and §L.22, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–1539 and 1635–2251 (the other entries of §L.1 to §L.20,
   applied); lines 2398–5906 (§L.23 to §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110
   (Tasks 4 and 5); lines 7136 to the end. Nor the derivation, the successor, `FRAMEWORK.md` or
   `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 21 rows §3.2 names, whole, at §6** (lines 435–79080): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** inside §6; read from that
      heading to the row's closing `---`. The writing side found every one exactly once, none carrying an earlier
      `*RULED …` or `*RECORDED …` line;
    - §10 (lines 79539–80598) at the five entries §3.3 names, and by search for every row number of this stretch;
    - §11 (lines 80599–82741) by search for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch, one line ADDED beneath the row's `*PROPOSED DISPOSITION.*` paragraph,
   the paragraph and every other sentence of the row untouched:
   `*RULED DISPOSITION (<record file>, Ruling N).* <part, if any> **<disposition>** — <placement in the record's words>.`
   The record file is written as its bare file name, as sessions 10 to 12 wrote it. Where §3.2 names a claim, the line
   names it as §3.2 gives it (form (b)'s split-row rule); otherwise the line names none.
2. **Where the line goes.** None of the 21 rows carries a `*RULED …` or `*RECORDED …` line yet (the writing side's check
   at the staged copy; check each at the row). Each row now ends: the `*PROPOSED DISPOSITION.*` paragraph, one blank line,
   then the row's closing `---`. Insert the new line, followed by one blank line, after that blank line, so the row ends:
   paragraph, blank line, **new line**, blank line, `---` — as the earlier stretches' lines stand. Each row gets exactly
   one line from this stretch.
3. **The quotation.** Each line quotes the words §3.2 gives for it. **The writing side checked every quotation against
   its record by a read-only script (words and punctuation, line breaks read as spaces, the bold and italic asterisks not
   compared), and compared Row 7.67's whole line with Ruling 5's line 187 character for character.** **Before writing
   each line, find its quoted words in the record you read whole (§2 item 7) and compare them the same way: every word
   and every punctuation mark must match, line breaks read as spaces; asterisks are not compared, and the line keeps its
   marks exactly as §3.2 gives them. For Row 7.67, also compare your whole line with Ruling 5's line 187 (the text between
   its backticks): they must be identical, character for character.** A difference is a STOP-and-report for that line: no
   line written, listed in the report under *rows the act could not place* with both texts. Where a line carries two
   quotations, each is compared.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in §6; the claim §3.2 names exists
   in the row's `*PROPOSED DISPOSITION.*` paragraph and is proposed **RELOCATED** to
   ***L2 — The tonal reading. The one entangled decision.*** (the writing side's reading, all 21); and **the row's
   outgoing statement fits what the record says of it**. A row that does not fit is a STOP-and-report for that row-part:
   no line, listed under *rows the act could not place* with what was read. Nothing is re-read into a different
   placement.
5. **As proposed.** Not written on any line of this stretch. Every row is proposed RELOCATED and placed with another
   word: Row 7.67 ADOPTED — carried (L3-S40), the other twenty HISTORICAL (form (b)'s paragraph: *as proposed* only where
   the word is the row's own proposed word). No other wording (such as *"placed from"*) is added.
6. **Two lines on the same claim with differing dispositions** (form (b)'s two-record rule, by part). **None in this
   stretch**, by the writing side's comparison: Rows 7.13 (i), 7.17 (i), 7.46, 7.56 and 7.135 are named by the first-cut
   record and the second-cut record, but the first-cut record's own amendment at its §1b hands them to the second-cut
   record (*"re-filed **HISTORICAL** by ruling"*), so they get the second-cut record's line only (form (b): *"A part a
   record says it moves to another record gets no line from the record that moves it"*). If you find a claim where two
   lines' words differ, that claim is a STOP-and-report and gets neither line; if one of those lines is an earlier
   stretch's, do not delete it: STOP, do not commit, and report.
7. **A §10 line follows its row's line.** The *Row 7.67 is not transferred* line (§3.3 item 1) is written only if Row
   7.67's line is written; a *LEAVES L3* line (§3.3 item 2) names only rows whose line of §3.2 is written, and is not
   written at all if none of the rows it would name has its line written.

### 3.2 The lines, entry by entry, with their exact text

Each line below is given whole, as it is to be written, `<part>` filled in from the row list; where the row list gives
no claim, `<part>` and the space after it are dropped.

**§L.15 — the edge-of-span record, Ruling 1. Row 7.67's line, held by session 12, written now.** 1 line.

(a) Row 7.67, 1 line, form (b) (Ruling 5 of the part 2 ruling record, its line 187, exactly):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* **ADOPTED — carried (L3-S40)** — "Row 7.67 (proposed RELOCATED to L2 only because L3's right to ask was open) may be re-marked ADOPTED — carried (L3-S40). The re-marking is the application dispatch's act."`
The word by form (b)'s paragraph, item (1) (the record names it in full). Not *as proposed* (proposed RELOCATED). Its
quotation is the edge-of-span record's documentation paragraph (its lines 78–80), last sentence included. Its §10 line:
§3.3 item 1. **About the bold:** this line closes the bold after *"(L3-S40)"*; the 13 other *ADOPTED — carried* lines
already in the file close it before the number. That is as Ruling 5 rules the text; do not make it uniform. List the row
in the report under *ADOPTED words read at the row* and under a heading of its own, *§L.15's line held by session 12,
written now*.

**§L.21 — the first-cut record; every line names it, Ruling 1.** 12 lines, all ruled.

(b) Ruling 1 — 12 lines, form (b), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, Ruling 1).* <part> **HISTORICAL** — "from the comparison's proposal RELOCATED to *L2 — The tonal reading. The one entangled decision.*: HISTORICAL — rules of a superseded design".`
Rows: 2.3, written `(i)`; 7.15; 7.28, written `(ii)`; 7.55; 7.130; 7.131; 7.132; 7.149; 7.150; 7.191; 7.194; 7.311.
The quotation is the record's §1 heading sentence (its lines 25–26), from *"from"* to *"design"*, which carries both the
placement and the proposal it is placed from.

**The other 22 rows of the first-cut record get no line from this entry.** Twelve HISTORICAL, four QUARANTINED and Row
2.6 are the record's §1b derivation, ratified by the ratification record's Ruling 1; their lines are §L.23's, for the
next session. Rows 7.13 (i), 7.17 (i), 7.46, 7.56 and 7.135 get the second-cut record's line (§3.2 (d)).

**§L.22 — the second-cut record; every line names it, Ruling 1.** 8 lines, all ruled.

(c) Ruling 1, of the second cut — 3 lines, form (b), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, Ruling 1).* <part> **HISTORICAL** — "from the comparison's proposal RELOCATED to *L2 — The tonal reading. The one entangled decision.*: HISTORICAL — rules of a superseded design".`
Rows: 10.23, written `(i)`; 10.147, written `(ii)`; 10.178.

(d) Ruling 1, of the first cut — 5 lines, form (b), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, Ruling 1).* <part> **HISTORICAL** — "from the comparison's proposal RELOCATED to *L2 — The tonal reading. The one entangled decision.*: HISTORICAL — rules of a superseded design"; "Of the first cut (5), re-filed from QUARANTINED, which the first-cut record §1b held as this side's derivation".`
Rows: 7.13, written `(i)`; 7.17, written `(i)`; 7.46; 7.56; 7.135.
The first quotation is the record's §1 heading sentence (its lines 31–32); the second is its §1 second bullet (its line
36), as §L.22's table gives it.

**The other 18 rows of the second cut get no line from this entry**: they are the record's §2 derivation, ratified by
the ratification record's Ruling 1; their lines are §L.23's, for the next session.

*The settlements in §3.2, each the writing side's and overrulable by the user: quoting the heading sentence of each
record's §1 from "from" to "design" as one quotation, so that the record's own words carry both the placement and the
proposal it is placed from (§L.21's and §L.22's tables quote the two halves separately); and the second quotation at
(d).*

**The count.** `*RULED DISPOSITION (`: 1 + 12 + 3 + 5 = **21**. None opens `*RECORDED DISPOSITION (` or
`*RULED PLACEMENT (`.

### 3.3 The transfer list, §10 (Task 3 (c) item 6)

Every line below goes beneath the last line of an existing §10 entry, opening with two spaces (the indentation of the
entry's continuation lines, as session 12's instruction read *"at the entry's indentation"*), the entry and every other
row it names untouched. Line numbers are those of the staged copy, before any edit; find each entry by its opening text,
which the writing side found exactly once.

1. **The Row 7.67 line** (as session 12's instruction §3.3 item 4 gave it; the text is Ruling 5's line 192 and the big
   dispatch's Task 3 (c) item 6, which agree). ONE line beneath the entry beginning
   `- Rows 7.60, 7.61, 7.64, 7.65, 7.66, 7.67, 7.277 and 7.278` (line 79794), after its last line, which ends
   `*(L3-S40 AGREES at Row 7.67, citing L2-S22.)*` (line 79795):

   `  *Row 7.67 is not transferred (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1)* — re-marked ADOPTED — carried (L3-S40): "proposed RELOCATED to L2 only because L3's right to ask was open".`

   The other §10 entry that names Row 7.67 (the one ending `as at Rows 10.58 and 7.67; as Rows 7.66 and 10.60.)*`) names
   it only as a comparison and gets nothing. It is not a *LEAVES L3* line.

2. **Four *LEAVES L3* lines.** Task 3 (c) item 6, acting by claim (the item-six record's Ruling 1): beneath each §10 entry
   that names a row-part carrying a ruled line from §L.21 or §L.22, ONE line naming the row-parts it covers. The writing
   side searched §10 for every row number of this stretch as a bare number with look-around and read each hit: these four
   entries name them, and every other hit is a mention by way of comparison inside a parenthesis (*"As Row 2.3 (i)"*,
   *"As Rows 7.13 (i) and 7.150"*, *"As Row 7.13 (i)"*) or names another claim (Row 2.3 (ii), Row 10.147 (i)), and gets
   nothing.
   - Beneath the entry beginning `- Row 2.3(i) — the confidence-weighted forward override's two instances` (line 79755),
     after its last line, which ends `the fine-grain chord override. *(L3-S38 DIFFERS at the row.)*` (line 79756):

     `  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, Ruling 1).* — Row 2.3 (i): "The rows are re-marked, and the 33 rows other than 2.6 taken off the reading file's §10 row by row, by the application dispatch, not now."`

   - Beneath the entry beginning `- Rows 7.15, 7.28 (ii), 7.55, 7.62 (i),` (line 79778), after its last line, which ends
     `7.239, 7.242 (i), 7.305 and 7.311.)*` (line 79782):

     `  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md, Ruling 1).* — Rows 7.15, 7.28 (ii), 7.55, 7.130, 7.131, 7.132, 7.149, 7.150, 7.191, 7.194 and 7.311: "The rows are re-marked, and the 33 rows other than 2.6 taken off the reading file's §10 row by row, by the application dispatch, not now."`

   - Beneath the entry beginning `- Rows 7.12, 7.13 (i), 7.16, 7.17 (i),` (line 79783), after its last line, `  7.232 (i).)*`
     (line 79787). The entry names Row 7.135 as the start of the range *"7.135 to 7.145"*; the line names 7.135 alone:

     `  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, Ruling 1).* — Rows 7.13 (i), 7.17 (i), 7.46, 7.56 and 7.135: "The rows are re-marked, and taken off the reading file's §10 row by row, by the application dispatch, not now."`

   - Beneath the entry beginning `- Rows 10.4, 10.5, 10.11 (ii), 10.23 (i),` (line 79874), after its last line, which ends
     `L3-S38 DIFFERS at every row here but 10.207 (iii).)*` (line 79877):

     `  *LEAVES L3 (cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md, Ruling 1).* — Rows 10.23 (i), 10.147 (ii) and 10.178: "The rows are re-marked, and taken off the reading file's §10 row by row, by the application dispatch, not now."`

   Each quotation is the take-off sentence of its record (the first-cut record's §2, its lines 69–70; the second-cut
   record's §3, its lines 89–90); compare it as §3.1 item 3 says. The same entries also name rows whose lines are §L.23's
   (Rows 7.209 (ii), 7.210, 7.213, 7.217, 7.238, 7.239, 7.242 (i), 7.305; 7.211, 7.232 (i); 10.4, 10.5, 10.11 (ii),
   10.26 (ii), 10.141 (ii), 10.146, 10.156, 10.198, 10.204, 10.205, 10.207 (ii)): **they are not named now.** The next
   session writes §L.23's *LEAVES L3* lines beneath its own, naming the ratification record. Row 10.206 (RELOCATED,
   §L.23's line) gets no *LEAVES L3* line at all (item 6). *Where the row names stand in the line — after the dash,
   followed by a colon and the quotation, as in the Row 7.67 line — is the writing side's settlement; item 6 says the line
   names the row-parts it covers and does not say where. Overrulable by the user.*
3. **No §10 addition under Task 3 (c) item 5**: no row of this stretch is placed RELOCATED.
4. **No row of this stretch is left out of the take-off while named by its record**, so the report heading *§10 rows a
   record says leave, not named by row* is empty for this stretch. The first-cut record's *"33 rows other than 2.6"* and
   the second-cut record's rows whose lines are §L.23's are taken off by the next session (§3.3 item 2).

### 3.4 The audit questions, §11 (Task 3 (c) item 7)

**Nothing is added to §11 in this stretch.** (a) No row-part of this stretch is placed QUARANTINED. (b) The writing
side's search of §11, every row number of this stretch (Row 7.67 included) as a bare number with look-around, found no
entry, so no NOT QUARANTINED line is due. Run the same search yourself; if you find a §11 entry for a claim this stretch
places with a word other than QUARANTINED, add the NOT QUARANTINED line item 7 (b) gives, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.22 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.23 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 3 commit, as in sessions 11 and 12.
   Attribute it in the diff table to *"session 13's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **Row 7.67's
   line of §L.15, then §L.21 and §L.22 only, in ledger order**, after sessions 10 to 12's §L.1 to §L.20. §L.23 to §L.55
   are not applied, read or touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1202 and 1203 ARE landed**, with this file, in §5 act 1, as sessions 8 to 12 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the two records §L.21 and §L.22
   enter only (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case not matched). The
   writing side's search found **no hit in either**, as §L.21 and §L.22 say. List the result in the report. Item 2: not
   reached. Item 3: not reached. Item 4: not reached. Item 5: not reached (§3.3 item 3). Item 6: §3.3 items 1 and 2.
   Item 7: §3.4.
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 3 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry, Row 7.67's line counting as its own unit before §L.21: if signs of context degradation appear, apply no
   further unit. If you are between units, write the in-progress line naming the last entry actually applied instead of
   §L.22 (and the next one instead of §L.23), commit what was applied, and report which. If you are inside a unit, do not
   commit; STOP and report which units were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 3 commit:**
     `git diff 6d26bee4cff5f93d553ea16dbc9e39f122383293 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session13_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the Row 7.67 line of §3.3 item 1; a *LEAVES L3* line of §3.3 item 2; a NOT
     QUARANTINED line only if §3.4 found one; the in-progress line of §3.5 item 3. Then
     `git diff --numstat 6d26bee4cff5f93d553ea16dbc9e39f122383293 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1 deleted line** and **2 × N + 6 added lines**, N being the number of lines of §3.2 you wrote
     (21 less the STOP-and-reports; **48 added** if none), less 1 for each §10 line not written under §3.1 item 7, plus 1
     for each NOT QUARANTINED line §3.4 adds, if any. *The writing side's arithmetic for the 6: the Row 7.67 §10 line,
     four LEAVES L3 lines, and the in-progress line (a replaced line: one added, one deleted).*
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 4 deleted lines** (the four lines session 10's state sentences were written into) and **633 +
     2 × N added lines** (**675** if none), with the same two adjustments as above. *The writing side's arithmetic:
     session 12's report gives 628 added and 4 deleted against the Task 2 commit; this stretch adds 2 × N lines, the Row
     7.67 §10 line and four LEAVES L3 lines. The in-progress line replaces a line that is itself an addition against the
     Task 2 commit, so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **250 + 21 = 271**, less the number of
     §3.2's lines you listed as STOP-and-report; `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(`
     must count **3**; `\*LEAVES L3 \(` must count **4**, less those not written; `\*Row 7\.67 is not transferred` must
     count **1**, or 0 if Row 7.67's line was a STOP-and-report.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly
   (if Row 7.67's line was a STOP-and-report, drop the words `Row 7.67's held line and its transfer-list line written, `
   and nothing else):

   `application L3, Task 3 stretch 4 (§L.21 and §L.22): Row 7.67's held line and its transfer-list line written, the rows of the first and second L3-S38 cuts ruled HISTORICAL re-marked in the reading file, four LEAVES L3 lines added to the transfer list and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_13_task_3_stretch_4_2026_11_23.md`**, as sessions 2 to 12
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.23, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own, before any edit to the reading file.**
   Exactly three paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_13_task_3_stretch_4_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_two.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_three.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1202 and 1203 and the session 13 instruction of the L3 application landed; Task 3 stretch 4 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. *(Session 12 made its first reading-file
   edits before its act 1 commit, a declared departure; this order is restated so it is not repeated.)*
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: first Row 7.67's line (§3.2
   (a)) and its §10 line (§3.3 item 1); then §L.21's twelve lines and their two *LEAVES L3* lines; then §L.22's eight
   lines and their two *LEAVES L3* lines; then §3.4's search; then §3.5 item 3; then §4 item 8's checks, the commit and
   the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_13_task_3_stretch_4_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 13 of the L3 application, Task 3 stretch 4 (§L.21 and §L.22) written; stretch 5 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For Row 7.67 and for each of §L.21 and §L.22, in order: every line by row and claim, written (with its reading-file
   line number after the edit) or STOP-and-report (and why). The same for §3.3's §10 lines and §3.4's search. For Row
   7.67, state the result of the whole-line comparison with Ruling 5's line 187.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place*; *rows given no line now*
   (none expected from this stretch); *recorded lines not written: no disposition word* (none expected); *rows named by
   more than one record* — Rows 7.13 (i), 7.17 (i), 7.46, 7.56 and 7.135 (the first-cut and second-cut records; the
   second-cut record's line only, the first-cut record's amendment handing them over); *ADOPTED words read at the row*
   (Row 7.67); *§L.15's line held by session 12, written now* (Row 7.67); *audit questions added* (none expected);
   *audit questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by row* (none
   expected, §3.3 item 4); the decided-against search (§4 item 4).
5. The diff table of §4 item 8, every changed passage attributed, and the five counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: the first-cut record's 17 derived rows and
   the second-cut record's 18 derived rows (their lines are §L.23's); and the rows §L.21 and §L.22 list as mentioned and
   not placed (§L.21: the L2 twins of Ruling 1's rows — Rows 4.3 (i), 5.16, 5.31, 5.61, 5.138, 5.139, 5.140, 5.158,
   5.159, 5.200 (ii), 5.203, 5.321 — and Rows 7.128, 7.151, 7.207, 5.315, 5.219 and 5.220; §L.22: Row 9.66 (ii), the L2
   twins Rows 6.21, 6.137 (ii), 6.160, 5.14 and 5.18, and Rows 12.13 (ii) and 45.21 (i)). *A heading of this session's
   report only, as in sessions 10 to 12's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 13 of the L3 application ends here. Stretch 5 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a row-part that
  is STOP-and-report under them, or under §3.1 items 3 to 7, is reported and the remaining ones applied, as they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 6);
- an entry §3.3 names is not found exactly once by its opening text, or its last line does not end as §3.3 gives it;
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1202. Read at the objects for this file: the
three git reference files (both refs `5ae0c467…`); entries 1202, 1201 and 1026 (its §3) whole; session 12's instruction
whole; session 12's report at its §1, §2 and §8 and by search; the first-cut, second-cut and item-six records whole; the
edge-of-span record at lines 76–81; the part 2 record at Ruling 5's lines 185–192 and by its headings; the big dispatch at
lines 200–247, 1540–1634 (by search at Row 7.67), 2252–2515 and 6616–6820, its `### §L.` headings, and a bare-number
search of lines 431–5906 for this stretch's rows (met at §L.21 and §L.22 only; a hit at §L.19 is L2's Row 7.13); the
reading file, by read-only scripts over the staged copy: its `##` headings, the 21 rows' headings (each once in §6),
`*PROPOSED DISPOSITION.*` paragraphs and closing lines (no earlier line under any), §10 and §11 searched for this
stretch's row numbers as bare numbers with look-around, every §10 hit read, the five §10 entries' opening and closing
lines, the in-progress line, and the current counts. Every quotation of §3.2 and §3.3 checked against its record by a
read-only script (words and punctuation, line breaks read as spaces, asterisks not compared): all found; Row 7.67's line
compared as a whole with Ruling 5's line 187 and the Row 7.67 §10 line with Ruling 5's line 192: identical. Computed as
git would on the staged copies: the big dispatch's blob `b5274c2c…` and the reading file's `40675143…` (counts 250 / 3 /
53; *LEAVES L3* 0; *Row 7.67 is not transferred* 0). Relayed, not re-checked here: the archive JSON's blob `1df4f207…`
and the untracked paths (from session 12's report), the end of `cowork_handoff.md`'s topmost block at line 255 and the
line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 12's instruction relays them), and
session 12's 628 added and 4 deleted lines against the Task 2 commit. Every label this file authors was checked
against `CLAUDE.md`'s list of collided words before landing. Checked for coherence, completeness, correctness and
overstated words as a turn of its own by the same sitting before landing: every line of §3.2 rebuilt by script from the
checked data and found producible from the file's templates; the counts (250 + 21; 13 *ADOPTED — carried* lines closing
the bold before the number, none after), the arithmetic, the line ranges and the one §10 ending not read before
re-read at their objects. Two corrections were made in place then, no former wording kept, the file never having
landed: *"Note on the bold"* became *"About the bold"*, and the Grep tool's *"count mode"* became *"counting matching
lines"* (twice), both bare uses of words reserved for their musical sense. The user's words: the opening instruction;
"shortened"; "continue" (the check).*
