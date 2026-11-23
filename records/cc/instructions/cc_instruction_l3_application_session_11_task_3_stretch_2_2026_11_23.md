# CC dispatch — the L3 application, SESSION 11 of several: Task 3 of the L3 application dispatch, second stretch (§L.5 to §L.12), and nothing else

> **STATUS: WRITTEN 2026-11-23, NOT YET RELEASED,** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_eight.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Sessions 2 to 7 applied Task 1 in six stretches.
Session 8 checked Task 1. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`, called **the
Task 2 commit** below). Session 10 applied the first stretch of Task 3, §L.1 to §L.4 (commit
`3df4da39120026195e5f58fa6c9e2ea3d3747ef5`, called **the stretch 1 commit** below), and committed its report as
`73d26f37239cd199611026101552ccc9d2e8581c`, the current tip.

**This is session 11. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for the ledger entries §L.5 to §L.12 only, commits and pushes
that second stretch, writes its report, and STOPS.** Each later stretch gets its own instruction, written after the
previous one is verified.

**What this stretch writes, in one paragraph.** One line beneath the `*PROPOSED DISPOSITION.*` paragraph of each
row-part §L.5, §L.6, §L.7, §L.8 and §L.12 place, after any line an earlier stretch already wrote there — **95 lines in
form (b) or (b-H)**, each opening `*RULED DISPOSITION (`, and **3 lines opening `*RULED PLACEMENT (`** for the three
rows the sections record holds (§3.2 lists every one, with its exact text); one entry appended to the transfer list at
the reading file's §10; and the in-progress line beneath the banner brought forward from §L.4 to §L.12. §L.9, §L.10 and
§L.11 place no row.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the rest applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the dispositions the ruling
records already place; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `73d26f37239cd199611026101552ccc9d2e8581c`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_11_task_3_stretch_2_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 1 commit left it.**
   `git diff --quiet 3df4da39120026195e5f58fa6c9e2ea3d3747ef5 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 73d26f37239cd199611026101552ccc9d2e8581c -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `10cc2c712d9b3d72289f1e9fd4e34e16d28cb15c`. Then, with the **Grep tool** in count mode on that file: the pattern
   `\*RULED DISPOSITION \(` must count **117**; `\*RULED PLACEMENT \(` must count **0**; `\*RECORDED DISPOSITION \(`
   must count **0**. Any other result: STOP and report, the file not touched. (The writing side's staged copy: 5,166,424
   bytes, 83,682 lines, line feeds only, no line longer than 1,900 characters.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 73d26f37239cd199611026101552ccc9d2e8581c -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1198 and 1199),
     plus the 393 untracked paths sessions 2 to 10 reported and did not land (387 under `scratch_artifacts/`;
     `Claude outputs/`; `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
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
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard.
4. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_nine.md` (the current entry point,
   written by the sitting that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_eight.md` (the one before it,
   written by the sitting that verified session 10; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md` (§L.5; 12,603 bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md` (§L.6; 9,376);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md` (§L.7; 7,292);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md` (§L.8; 6,575);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md` (§L.9; 6,388);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md` (§L.12; 20,068);
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part_1a_sitting.md` (13,326)
     — its Rulings 5 to 8 give the words for Row 7.104 (§L.6), Row 7.37's rest (§L.8), the section side of four rows
     and Row 7.34 (§L.12); its Rulings 1 to 4 are session 10's;
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part5_sitting.md` (3,709)
     — Row 46.14 (§L.6);
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part14_sitting.md` (6,946)
     — the twelve rows of §L.12's first table line.
   **The two records §L.10 and §L.11 enter are NOT read whole**: they place no row (§L.10: *"Reading file — rows:
   none"*; §L.11: *"None placed"*). Run Task 3 (c) item 1's search over them with the Grep tool only (§4 item 4).
   **Do NOT read the records of §L.1 to §L.4 or of §L.13 to §L.55.**
8. **Side records, at these line ranges only, with the Read tool by offset** (each range was located by the writing
   side at the staged copy, 2026-11-23; if a range does not open and close at the heading named, find the heading with
   the Grep tool and report the new range):
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part_1b_sitting.md`
     (10,894 bytes): lines 9–23 (**Ruling 1**, Rows 8.37 (i) and 8.38 (i)) and lines 89–108 (**Ruling 6**, Row 42.36
     (ii)).
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md` (20,333 bytes): lines
     8–29 (**Ruling 1**, Row 7.115 (i)).
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes, 2,254
     lines): **Ruling 3** lines 89–125 (form (b)'s two-record rule applies by part); **Ruling 4** lines 126–161 (Rows
     8.23, 8.35 (i) and 8.113 (ii), held: the line they get); **Ruling 7** lines 265–312 (§11 kept in step with the
     placed rows); **Ruling 9** lines 363–420 (which ADOPTED word, and when *as proposed* is written); **Ruling 35**
     lines 1960–2060 (§L.12's six unnamed rows get no line).
   - `ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md` (475,634 bytes, 4,245 lines): lines
     235–330 (*§L.6 (1)*, *§L.8 (2)* and *§L.12 (2)*, items (v) to (xi)); lines 877–906 (*§L.6 (3)*, item (xxxi));
     lines 2080–2131 (*§L.12 (1)*, item (liii)).
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, form (b-H) and form (c-P) are the forms every line of this stretch is written in**, the
     premise ledger, the declared start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 700–1328 (§L.5 to §L.12, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–699 (§L.1 to §L.4, applied by session 10); lines 1329–5906
   (the other ledger entries); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5);
   lines 7136 to the end. Nor the derivation, the successor, `FRAMEWORK.md` or
   `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 82 rows §3.2 names, whole, at §6** (lines 435–78702): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** inside §6; read from that
      heading to the row's closing `---`. The writing side found every one of the 82 exactly once; together they come to
      about 99 KB (98,626 bytes from each heading to the line before its closing `---`, measured at the staged copy);
    - §10 (lines 79161–80218) at its six `**To …**` headings, at the entries named in §3.3, and by search for each
      RELOCATED row-part of this stretch; §11 (lines 80219–82356) by search for each row number of this stretch (§3.4);
    - lines 83668–83680 (§15 and §16's first bullet), to see that session 10's state sentences stand.

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch, one line ADDED beneath the row's `*PROPOSED DISPOSITION.*` paragraph,
   the paragraph and every other sentence of the row untouched:
   `*RULED DISPOSITION (<record file>, Ruling N).* <part, if any> **<disposition>** — <placement>.` The record file is
   written as its bare file name, as session 10's lines write it. Where §3.2 names a part, a side or a half, the line
   names it as §3.2 gives it; otherwise the line names no part.
2. **Where the line goes.** Each line is preceded by one blank line, as session 10's lines stand (for example beneath
   Row 2.15). Where the row carries no `*RULED …` line yet, the new line goes after the blank line that follows the
   `*PROPOSED DISPOSITION.*` paragraph. **Where the row already carries one or more lines from session 10, the new line
   goes after the last of them**, so that every row's lines stand in ledger order. *Authored by the writing side,
   overrulable by the user. Ground: Task 3 (b), "every line the ledger gives them, in ledger order"; session 10's
   instruction §3.1 item 6.* The rows of this stretch that already carry a session 10 line: 8.11, 8.59, 19.38, 8.24,
   19.30, 19.31, 19.58, 3.1 and 8.96 (each read at the staged copy; check each at the row).
3. **Order beneath a row that gets more than one line from this stretch.** Ledger order first (§L.5, then §L.6, §L.7,
   §L.8, §L.12); within one entry, the order §3.2 gives. Rows that get more than one line from this stretch: 2.7, three
   ((ii) and (iii) from §L.5, then (i) from §L.6); 7.1, 7.31, 7.101, 7.107, 7.301, 8.40 (§L.5's part, then §L.6's); 2.9
   (§L.6's half, then §L.7's); 7.114 ((i) from §L.6, then (ii) from §L.7); 46.14 (Ruling 1's part, then Ruling 2's);
   7.37 (the HISTORICAL part, then the rest); 57.315 ((i), then (ii)).
4. **The record each line names.** The record that places the row in the §L entry's table, with the ruling the table
   names (§3.2 gives it for every line). For the rows whose word a later ruling of the application's release gives (Rows
   7.104, 8.37 (i), 8.38 (i), 46.14, 7.37's rest, 42.36 (ii), the twelve rows of §L.12's first table line, the section
   side of four rows and Row 7.34), the line still names the family record whose sentence it quotes, not the release
   ruling. *Authored by the writing side, overrulable by the user. Ground: as session 10's instruction §3.1 item 2; the
   Part 1b record's Ruling 6 names the line "(form (b), the L3 cadential six-four record, Ruling 1)", and the Part 1a
   record's Ruling 6 says of Row 7.37's two lines that "both lines come from the one record".*
5. **The quotation.** Each line quotes the words §3.2 gives for it. **The writing side took them from the big dispatch's
   §L table cell for the row, where the cell quotes the record, and checked each against the record**; where the cell
   names no quotation, from the release ruling that gives the word. **Before writing each line, find its quoted words in
   the record you read whole (§2 item 7) and compare them character for character, line breaks read as spaces.** A
   difference is a STOP-and-report for that line: no line written, listed in the report under *rows the act could not
   place* with both texts. Where §3.2's quotation carries `…`, the comparison is of the two pieces either side of it.
   Where the record bolds or italicises words inside the quoted span, the line keeps those marks. **One exception:** the
   three held lines of §3.2 (y) are the line the part 2 record's Ruling 4 gives, word for word (its lines 146–147),
   which writes the inner quotation without the sections record's italics; compare each with that ruling's text.
6. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in §6; the part §3.2 names exists in
   the row's `*PROPOSED DISPOSITION.*` paragraph; and **the row's outgoing statement fits what the record says of it**.
   A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act could not place*
   with what was read. Nothing is re-read into a different placement. For Rows 2.8 and 7.105 (§L.5 item b, no part
   named): §L.5's *Open* point (2) applies — if the row's §6 text shows no part other than keeping the fact unpublished,
   the line covers the whole row and names no part; if the split is unclear, STOP-and-report that row.
7. **As proposed.** §3.2 writes *as proposed* on eight lines only: Rows 7.98 and 20.48 (§L.5; the record: *"as the
   reading file proposes"*), Rows 2.7 (iii) and 7.108 (§L.5; the record's sentence states the proposal's own content,
   the writing side's reading), Row 7.95 (§L.8; the record carries the AGREES row with the word it was proposed with,
   on the writing side's reading of *"Row 7.95 carried (AGREES)"*), and Rows 19.38 (vii), 19.43 (i) and 38.77 (i) (§L.12; the
   Part 14 record's Ruling 1). On every other line, *as proposed* is not written and the placement is given in the
   record's words. *Authored by the writing side, overrulable by the user. Grounds: form (b)'s paragraph — "The line
   says as proposed only where its word, and its number if any, are the row's own proposed word for that part, and the
   record adopts the content as proposed"; for the RELOCATED and QUARANTINED lines, the Part 1b record's Ruling 6, which
   the user ruled on Row 42.36 (ii): "form (b) gives the placement in the record's words and writes as proposed only for
   a row the record places "as proposed"". So the six RELOCATED rows of §L.5's first table line (proposed RELOCATED to
   L1, which the record places without saying "as proposed" of them: its "as the reading file proposes" closes the
   clause on Rows 7.98 and 20.48, and the big dispatch's table cell reads it so), Row 7.99 and Row 28.47 do not say it.
   For the six rows of §L.6 Ruling 3 item e the record adopts them "as types or rules of the declared vocabularies; each
   wording written from its source when that vocabulary is declared", which is not the proposal's content as proposed.*
   Check each line's word against the row's `*PROPOSED DISPOSITION.*` paragraph for that part; if you find a line where
   this choice contradicts form (b)'s paragraph, STOP-and-report that line. No other wording (such as *"placed from"*)
   is added.
8. **Two lines on the same part with differing dispositions** (form (b)'s two-record rule, by part). **None in this
   stretch, by the writing side's comparison**, across stretches included: Row 19.38 (iii) gets a second HISTORICAL line
   (session 10's from the disposition-words record; this stretch's from the sections record, Ruling 2) — the same word,
   so both are written; the section side of Rows 8.24, 19.30 (ii), 19.31 (ii) and 19.58 (iii) is another side than the
   phrase side session 10 wrote, with the same word (the Part 1a record's Ruling 7: *"each row gets two lines with the
   same word"*). If you find a part where two lines' words differ, that part is a STOP-and-report and gets neither line;
   if one of those lines is session 10's, do not delete it: STOP, do not commit, and report.

### 3.2 The lines, entry by entry, with their exact text

Each line below is given whole, as it is to be written, the angle-bracketed part filled in as the paragraph says;
where the row has no part, `<part>` and the space after it are dropped. Each quotation keeps the record's own marks as
the record writes them.

**§L.5 — the cadence-features record; every line names it.** 21 lines.

(a) Ruling 1 item a, the L1 group — 6 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).* <part> **RELOCATED** to ***L1 — Change points, candidates and notated evidence*** — "(the key-agnostic cues)".`
Rows: 2.4, 7.52, 7.120, 7.229, 7.294 (ii), 20.46 (ii). Each is already on §10 (§3.3).

(b) Ruling 1 item a, the L2 pair — 2 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — as proposed; "(the aggregation into the tonality), as the reading file proposes".`
Rows: 7.98, 20.48. Each is already on §10 (§3.3).

(c) Ruling 1 item b — 11 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).* <part> **HISTORICAL** — "recorded as decided against **in so far as they keep the fact unpublished**".`
Rows: 2.7 (ii), 2.8, 7.1 (ii), 7.31 (i), 7.101 (ii), 7.105, 7.107 (i), 7.301 (ii), 8.40 (ii), 36.36 (i), 36.130 (i).
(2.8 and 7.105 as §3.1 item 6 says.)

(d) Ruling 1 item c — 2 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).* <part> **ADOPTED — proposed** — as proposed; "L3 never attempts to identify a structural melody among the voices".`
Rows: 2.7 (iii), 7.108. The word by form (b)'s paragraph, item (4) (the record writes a bare *"ADOPTED"*; both rows
proposed ADOPTED — proposed). List both under *ADOPTED words read at the row*.

**§L.6 — the cadence-type record; every line names it.** 36 lines.

(e) Ruling 1 — 14 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 1).* <part> **HISTORICAL** — "recorded as decided against **in so far as they make the bass-derived inversion the only criterion**".`
Rows: 2.7 (i), 7.1 (i), 7.31 (ii), 7.100, 7.101 (i), 7.102, 7.103, 7.106, 7.107 (ii), 7.189 (i), 7.269, 7.301 (i),
8.40 (i); and 2.9, written `Its perfect/imperfect half:` (its confidence half is §L.7's).

(f) Ruling 2 — 7 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 2).* <part> **HISTORICAL** — "recorded as decided against **in so far as they fix one list as the only one**; their lists remain candidates for declared vocabularies.".`
Rows: 7.8, 7.35, 7.44 (i), 7.329 (i), 8.11 (i), 8.59 (i), 57.60 (i).

(g) Row 46.14 — 2 lines, form (b-H) (the Part 5 record's Ruling 1), in this order:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 1).* Its "perfect/imperfect by inversion" clause: **HISTORICAL** — "recorded as decided against **in so far as they make the bass-derived inversion the only criterion**".`
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 2).* **HISTORICAL** — "recorded as decided against **in so far as they fix one list as the only one**; their lists remain candidates for declared vocabularies.".`
The row is one claim at §6 (the working list's item (xxxi)); the second line names no label because its quotation
names the part. **The rest of the row gets no line** (the record: *"Row 46.14's reading-file proposal stays UNPLACED"*).
*The first line's label is the writing side's, from the record's own words; overrulable by the user.*

(h) Ruling 3 item a — 4 lines:
- Rows 8.88 (i) and 38.26 (i), form (b-H), each:
  `*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).* (i) **HISTORICAL** — "Rows 8.88 (i) and 38.26 (i) recorded as decided against".`
- Row 7.99:
  `*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "Row 7.99 **RELOCATED** to *L2 — The tonal reading. The one entangled decision.*".`
  Already on §10 (§3.3).
- Row 28.47:
  `*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).* **QUARANTINED** — "Row 28.47 **QUARANTINED** for the audit".`
  Already on §11 (§3.4).

(i) Ruling 3 item b — Row 7.104, 1 line (the Part 1a record's Ruling 5):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).* **HISTORICAL** — "Row 7.104: the perfect/imperfect split is computable wherever its features carry values; *type not computable* only where a feature is missing.".`

(j) Ruling 3 item c — **Row 7.115 (i): no line.** The part 1 record's Ruling 1: the row *"gets no line at the
application act; it stays UNPLACED and is listed in Claude Code's report among the points left open"*. List it under
*rows given no line now* (Task 3 (a)).

(k) Ruling 3 item d — Rows 8.37 (i) and 8.38 (i), 2 lines (the Part 1b record's Ruling 1), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).* (i) **ADOPTED — proposed** — "follow from Ruling 1c of the 2026-11-03 cadence-features record"; that ruling: "L3 never attempts to identify a structural melody among the voices".`
Not *as proposed* (the Part 1b record's Ruling 1). The second quotation is from the cadence-features record (Ruling 1,
item c), which you read whole. List both under *ADOPTED words read at the row*. *The joining words "; that ruling:" are
the writing side's; overrulable by the user.*

(l) Ruling 3 item e — 6 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).* <part> **ADOPTED — proposed** — "as types or rules of the declared vocabularies; each wording written from its source when that vocabulary is declared.".`
Rows: 7.109, 7.110 (i), 7.111, 7.113, 7.114 (i), 7.97 (i). The word by form (b)'s paragraph, item (1) (the record names
it in full). List all six under *ADOPTED words read at the row*.

**§L.7 — the cadence-mass record; every line names it, Ruling 1.** 5 lines.

(m) Rows 7.112 (ii), 7.114 (ii), 7.115 (ii) — 3 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "Recorded as decided against **in so far as they lower confidence by a fixed rule**".`

(n) Row 7.249 — 1 line, form (b-H):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md, Ruling 1).* Its by-rule part: **HISTORICAL** — "Recorded as decided against **in so far as they lower confidence by a fixed rule**".`
(The record: *"Row 7.249's forecast … is not decided against; only its by-rule part is."* The label is the writing
side's, from those words; overrulable by the user.)

(o) Row 2.9 — 1 line, form (b-H):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md, Ruling 1).* Its confidence half: **HISTORICAL** — "Recorded as decided against **in so far as they lower confidence by a fixed rule**: … and Row 2.9's confidence half".`

**§L.8 — the cadential six-four record; every line names it, Ruling 1.** 6 lines.

(p) Row 7.94 — form (b-H):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* **HISTORICAL** — "Recorded as decided against: Row 7.94 (the collapse)".`

(q) Row 7.273 — form (b-H), its quotation naming the part:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* **HISTORICAL** — "Row 7.273 (the glossary entry) in so far as it picks one theory".`

(r) Row 7.37 — 2 lines, in this order (the second by the Part 1a record's Ruling 6):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* **HISTORICAL** — "Row 7.37 in so far as it fixes one label for the analysis's output".`
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* Its rest: **RELOCATED** to ***the measurement of the analysis*** — "its stated purpose, comparison with the ground truth, belongs to *the measurement of the analysis*, as the L2 ruling placed Row 23.109 (i) and Row 5.42's six-four half".`
The rest is appended to §10 (§3.3). *The label "Its rest:" is the writing side's, from §L.8's table ("For the rest");
overrulable by the user.*

(s) Row 7.95 — 1 line:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* **ADOPTED — carried** (L3-S20) — as proposed; "L3-S20 filed as the L3 statement. Row 7.95 carried (AGREES).".`
The word by form (b)'s paragraph, item (2) (§L.8's *Open* point (1)). List it under *ADOPTED words read at the row*.

(t) Row 42.36 (ii) — 1 line (the Part 1b record's Ruling 6), not *as proposed*:
`` *RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* (ii) **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "Row 42.36 (ii) (*"representable as its own degree class"*) is the `Cad64` reading the L2 ruling already excluded by name; nothing is added at L3.". ``
*(Double backticks delimit this line here only because its quotation carries backticks; write the line itself with
none of the delimiters.)* Already on §10 (§3.3).

**§L.9 — the §9 point 3 record; §L.10 — the research-registry record; §L.11 — the thematic-parallelism record.** No
line. §L.9 places no row (its rows' lines come from §L.6); §L.10 and §L.11 place none. **Nothing is written at the
reading file's §9 for point 3**: no form writes at §9, and the point is answered by a ratified ruling, as Ruling 26 of
the part 2 record has it for points 2 and 8; it is not listed under *points answered by a record's own derivation,
nothing written*. *Authored by the writing side, overrulable by the user.*

**§L.12 — the sections record; every line names it.** 27 lines in form (b) or (b-H), and 3 held lines.

(u) Ruling 1, the twelve rows (the Part 14 record's Ruling 1) — 12 lines. The nine not *as proposed*, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1).* <part> **HISTORICAL** — "recorded as overtaken by the charter".`
Rows: 8.35 (ii), 8.36 (i), 8.113 (i), 8.114 (i), 8.115, 8.140, 8.141, 19.59 (iv), 57.320 (i).
The three *as proposed*, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1).* <part> **HISTORICAL** — as proposed; "recorded as overtaken by the charter".`
Rows: 19.38 (vii), 19.43 (i), 38.77 (i).

(v) Ruling 1, the section side of four rows (the Part 1a record's Ruling 7) — 4 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1).* <part, its section side:> **HISTORICAL** — "recorded as overtaken by the charter".`
Rows: 8.24, written `Its section side:`; 19.30 (ii) and 19.31 (ii), written `(ii), its section side:`; 19.58 (iii),
written `(iii), its section side:`. Each row already carries session 10's phrase-side line (§3.1 items 2 and 8).
*The quotation is the big dispatch's §L.12 table cell's ("one line per row quoting the sections record's Ruling 1
Documentation (*"recorded as overtaken by the charter"*)"); the Part 1a record's Ruling 7 and the working list's item
(x) quote a longer span of the same sentence with an ellipsis, of which this is the opening. Authored by the writing
side, overrulable by the user.*

(w) Ruling 1, Row 7.34 (the Part 1a record's Ruling 8) — 1 line:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1).* **HISTORICAL** — "recorded as overtaken by item (3)".`
*(The quotation is the big dispatch's table cell's, as at (v).)*

(x) Ruling 2 — 10 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 2).* <part> **HISTORICAL** — "the ten rows that call the grouping flat are recorded as decided against".`
Rows: 3.1 (i), 3.3, 8.21, 8.22, 8.25, 8.34, 8.96 (ii), 19.38 (iii), 57.315 (i), 57.315 (ii). *(Row 57.315 gets two
lines, one per part. Row 19.38 (iii) already carries session 10's HISTORICAL line: §3.1 item 8.)*

(y) Ruling 3, Rows 8.23, 8.35 (i) and 8.113 (ii), held — 3 lines (the part 2 record's Ruling 4; form (c-P)'s label, the
big dispatch line 253), each:
`*RULED PLACEMENT (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3).* <part> Held, travelling with the naming-scheme question — "their proposed disposition, "ADOPTED — carried (L3-S24)", no longer stands as proposed".`
8.23 with no part; 8.35 written `(i)`; 8.113 written `(ii)`. The proposed paragraph is kept; no disposition word; the
rows are listed in the report as *held by ruling*. *The place of the part, after the label, is the writing side's, on
form (b)'s split-row rule; overrulable by the user.*

(z) **Rows §L.12 names and does not place** — 57.352, 19.39 (iii), 41.63, 36.50, 38.61, 38.72, 40.5 (iii): no line
(the part 2 record's Ruling 35).

**The count.** §L.5: 6 + 2 + 11 + 2 = 21. §L.6: 14 + 7 + 2 + 4 + 1 + 0 + 2 + 6 = 36. §L.7: 3 + 1 + 1 = 5. §L.8:
1 + 1 + 2 + 1 + 1 = 6. §L.12: 12 + 4 + 1 + 10 = 27. **95 lines opening `*RULED DISPOSITION (`**, and **3 opening
`*RULED PLACEMENT (`**, 98 in all.

### 3.3 The transfer list, §10 (Task 3 (c) item 5)

**One entry is appended.** Row 7.37's rest is placed RELOCATED out of UNPLACED, and §10 does not carry Row 7.37 at the
writing side's search (every RELOCATED row-part of this stretch searched as a bare number, so that entries listing
several rows are reached, and each hit read for its claim). Append it **after the last entry under `**To *the
measurement of the analysis* (NOT A LAYER).**`** (line 80036 at staging) — the entry for Rows 57.318 (i) and 57.322 (i),
lines 80205–80206 at staging — and before the blank line and §10's closing note on the members' relocations (lines
80207–80208), in §10's entry form:

`- Row 7.37, its rest — that the DCML conventions for variants serve comparison with the ground truth. *(cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1.)*`

*The subject clause is the writing side's, taken from the row's heading and the record's words; overrulable by the
user.* Check at §10 by row number and claim before appending.

**Already on §10, nothing appended:** Row 2.4 (line 79246 at staging); Rows 7.52, 7.120, 7.229 and 7.294 (ii) (the
entry beginning `- Row 7.52, with Rows 7.120, 7.229 and 7.294 (ii)`, line 79249); Row 20.46 (ii) (line 79270); Rows
7.98 and 7.99 (the entry beginning `- Rows 7.53, 7.62 (ii), 7.97 (ii), 7.98, 7.99,`, line 79412); Row 20.48 (the entry
beginning `- Rows 20.45 (i), 20.45 (ii), 20.46 (i), 20.47 (i), 20.48`, line 79558); Row 42.36 (ii) (the entry beginning
`- Rows 42.31, 42.32, 42.33, 42.34, 42.35, 42.36 (i), 42.36 (ii),`, line 79710). Run the same search yourself. Task 3
(c) item 6 (*LEAVES L3* lines and the Row 7.67 line) does not reach this stretch.

### 3.4 The audit questions, §11 (Task 3 (c) item 7)

**Expected: nothing to write.** Row 28.47 is placed QUARANTINED and §11 carries it (line 81307 at staging), so (a)
adds nothing; it is not placed *out of another proposal* in any case, having been proposed QUARANTINED. The writing side
searched §11 for every row number of this stretch as a bare number: the only other hits are Row 19.59 (iii) (line
80809) and four entries for other rows whose text names Row 19.59 (entries starting at lines 81201, 81676, 81686 and
81719) —
none of them a part this stretch places (it places 19.59 (iv)), so (b) adds nothing. Run the same search yourself; if
you find a §11 entry for a part this stretch places with a word other than QUARANTINED, add the NOT QUARANTINED line
(c) item 7 (b) gives, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54 at staging) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION and RULED PLACEMENT lines in this file are those of §L.1 to §L.12 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.13 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   This is the one deleted line this stretch allows. Its former text is not preserved in the file: the line is the
   application's own temporary marker, which its own words say the last stretch removes, and its former text stays
   recoverable at the stretch 1 commit, which is the case #12's recoverable clause covers. *Authored by the writing
   side, overrulable by the user (for example if he wants the former text kept in the file's preserved-wording shape).*
   Attribute it in the diff table to *"session 11's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.5 to
   §L.12 only, in ledger order**, after session 10's §L.1 to §L.4. §L.13 to §L.55 are not applied, read or touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1198 and 1199 ARE landed**, with this file, in §5 act 1, as sessions 8 to 10 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the eight records §L.5 to §L.12
   enter only — the six of §2 item 7 that you read whole, and the research-registry and thematic-parallelism records by
   the Grep tool. The writing side's search, line breaks joined, case not matched, found twelve hits: the
   cadence-features record's line 63 (§3.2 (c)); the cadence-type record's lines 39, 64 and 82 (§3.2 (e), (f) with (g),
   and (h)); the cadence-mass record's line 43 (*"Algorithmic (decided against the older documents)"*, no row) and lines
   47 and 50 (§3.2 (m) to (o); line 50's *"is not decided against; only its by-rule part is"* is why Row 7.249's line
   names its by-rule part); the cadential six-four record's line 36 (*"Algorithmic (decided against the older documents
   only)"*, no row) and line 41 (§3.2 (p) to (r)); the §9 point 3 record's line 44 (Rows 7.44 and 57.60, whose lines
   are §L.6's, §3.2 (f)); the sections record's line 112 (§3.2 (x)) and line 168 (*"rather than being decided
   against"*, the held rows, §3.2 (y)); none in the research-registry or thematic-parallelism records. Nothing is written
   from the hits without a row. List each hit you find in the report. Items 2, 3, 4 and 6: not reached by this stretch.
   Item 5: §3.3. Item 7: §3.4.
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **A changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against
   the stretch 1 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, write the
   in-progress line naming the last entry actually applied instead of §L.12 (and the next one instead of §L.13), commit
   the entries already applied, and report which. If you are inside an entry, do not commit; STOP and report which
   entries were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 1 commit:**
     `git diff 3df4da39120026195e5f58fa6c9e2ea3d3747ef5 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session11_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line before it; the §10 entry of §3.3; a NOT QUARANTINED line only if §3.4 found one; the
     in-progress line of §3.5 item 3. Then
     `git diff --numstat 3df4da39120026195e5f58fa6c9e2ea3d3747ef5 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1 deleted line** and **2 × N + 2 added lines**, N being the number of lines of §3.2 you wrote
     (98 less the STOP-and-reports; 198 added if none), plus 1 for each NOT QUARANTINED line §3.4 adds, if any (one
     line at the entry's indentation, (c) item 7 (b)).
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 4 deleted lines** (the four lines session 10's state sentences were written into; session 10's
     report gives 243 added and 4 deleted for its own stretch) and **244 + 2 × N added lines** (plus 1 for each NOT
     QUARANTINED line). *The writing side's arithmetic: 243 from session 10, one more §10 entry, and the in-progress
     line's replacement adds no line.*
   - Then, with the Grep tool in count mode: `\*RULED DISPOSITION \(` must count **117 + 95 = 212**, less the number of
     §3.2's RULED DISPOSITION lines you listed as STOP-and-report; `\*RULED PLACEMENT \(` must count **3**, less those
     of §3.2 (y) listed as STOP-and-report; `\*RECORDED DISPOSITION \(` must count **0**.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 2 (§L.5 to §L.12): the rows placed by ledger entries five to twelve re-marked in the reading file, one transfer-list entry added and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_11_task_3_stretch_2_2026_11_23.md`**, as sessions 2 to 10
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.13, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own.** Exactly three paths, all expected
   UNTRACKED: this file, `records/cc/instructions/cc_instruction_l3_application_session_11_task_3_stretch_2_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_eight.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_nine.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1198 and 1199 and the session 11 instruction of the L3 application landed; Task 3 stretch 2 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for §L.5 to §L.12**, as the big dispatch's Task 3 and §3 and §4 above give it: the lines of §3.2 entry by
   entry, with §3.3's entry at §L.8; then §3.4's search; then §3.5 item 3; then §4 item 8's checks, the commit and the
   push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_11_task_3_stretch_2_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 11 of the L3 application, Task 3 stretch 2 (§L.5 to §L.12) written; stretch 3 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.5 to §L.12, in order: every line by row and part, written (with its reading-file line number after the
   edit) or STOP-and-report (and why). The same for §3.3's entry and §3.4's search.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place*; *rows given no line now*
   (Row 7.115 (i)); *held by ruling* (Rows 8.23, 8.35 (i), 8.113 (ii)); *rows named by more than one record* — Row
   19.38 (iii) (session 10's line and this stretch's, both HISTORICAL), the section side of Rows 8.24, 19.30 (ii), 19.31
   (ii) and 19.58 (iii) (session 10's phrase-side line beside), and Rows 2.7, 7.1, 7.31, 7.101, 7.107, 7.301, 8.40,
   8.11, 8.59, 7.114, 2.9, 3.1 and 8.96 (lines on different parts or halves from two records); and, marked *to be
   written by a later stretch*, the row numbers of this stretch the writing side's bare-number search met in §L.13 to
   §L.54, not read for claim: 46.14 (§L.39), 7.110, 7.112, 7.114 and 7.97 (§L.49; 7.97 also §L.50 and §L.51), 7.294
   (§L.25, §L.47), 7.108 and 7.329 (§L.25), 7.189 (§L.21), 38.26 (§L.23), 8.38 (§L.24), 7.35 (§L.40), 19.38 (§L.23,
   §L.26, §L.31, §L.38), 19.59 (§L.24, §L.43), 38.77 (§L.14, §L.32), 3.1 and 3.3 (many entries from §L.13 on); *ADOPTED
   words read at the row* (Rows 2.7 (iii), 7.108, 8.37 (i), 8.38 (i), the six of §3.2 (l), and 7.95); the decided-against
   hits (§4 item 4).
5. The diff table of §4 item 8, every changed passage attributed, and the three counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: Row 7.115 (i) (§3.2 (j)); the rest of Row
   46.14 (§3.2 (g)); the rows of §3.2 (z); and the rows the §L entries of this stretch list as mentioned and not placed
   by their record (§L.5: 7.109, 8.37 (i), 7.97 (i), whose lines are §L.6's, and the rows its §5 lists as read *"in
   passing"*; §L.6: 57.60 (ii), 7.96; §L.7: 8.30 (ii), 8.85, 42.26 (ii), and L3-S20's five rows, whose lines are §L.8's;
   §L.9: 7.44, 57.60, 2.7 (iii), 7.108, 7.109, 7.97 (i), 8.37 (i), whose lines are other entries').
   *A heading of this session's report only, as in session 10's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 11 of the L3 application ends here. Stretch 3 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a row-part that
  is STOP-and-report under them, or under §3.1 items 5 to 8, is reported and the rest applied, as they say);
- a line of session 10's would have to be deleted or edited (§3.1 item 8);
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1198. Read at the objects for this file: the
three git reference files (both refs `73d26f37…`); entries 1198, 1197 and 1194 whole, and entry 1026 whole; session
10's instruction whole; the eight records §L.5 to §L.12 enter (six whole; the research-registry and thematic-parallelism
records by search for rows and for the decided-against words); the Part 1a, Part 5 and Part 14 records whole; the Part
1b record at its headings and Rulings 1 and 6; the part 1 record at its headings and Ruling 1; the part 2 record at its
headings and Rulings 3 and 4; the working list at lines 234–343, 876–906 and 2080–2140; the big dispatch at lines
200–261, 700–1328 and 6616–6820, its `### §L.` headings, and a bare-number search of lines 1329–5906 for this
stretch's rows; the reading file at lines 38–59 and 83668–83690, its `##` headings, §10's `**To …**` headings and its
last entries (lines 80036–80219), and, by a read-only script over the staged copy, each of the 82 rows' heading (once in
§6), `*PROPOSED DISPOSITION.*` paragraph and any `*RULED …` line, and §10 and §11 searched for this stretch's row
numbers as bare numbers with look-around matching, each hit's entry read for its claims. Computed as git would on the
staged copies: the big dispatch's blob `b5274c2c…` and the reading file's `10cc2c71…`. Relayed, not re-checked here:
the archive JSON's blob `1df4f207…` and the 393 untracked paths (from session 10's instruction and entry 1198), the end
of `cowork_handoff.md`'s topmost block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s
dispatch-protocol section (checked by the sitting booted on entry 1196), and session 10's report's 243 added and 4
deleted lines (entry 1198 §2 item 3, checked there). Checked for coherence, completeness, correctness and overstated
words as a turn of its own by the same sitting before landing; eight corrections were made in place then, no former
wording kept, the file never having landed: the rows' total size (re-measured in bytes); the list of rows that get more
than one line (Row 2.7 gets three; Row 57.315 was missing); two readings marked as the writing side's (Rows 2.7 (iii)
and 7.108, Row 7.95); two lists of rows mentioned and not placed completed (§L.5's rows read in passing, §L.7's
L3-S20 rows); and the added-line count for a NOT QUARANTINED line, one line and not two, in both checks. Before the
check, the same sitting added the exception for the held lines' italics, fixed a typo and an unclear sentence in §4,
and corrected a count of §11 entries from three to four. The user's words: the opening instruction; "shortened";
"continue".*
