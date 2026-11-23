# CC dispatch — the L3 application, SESSION 10 of several: Task 3 of the L3 application dispatch, first stretch (§L.1 to §L.4), and nothing else

> **STATUS: RELEASED 2026-11-23** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_five.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.** *Re-checked at the objects 2026-11-23 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_six.md`; its corrections are marked
> where they stand, each former wording kept (#12).*

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Sessions 2 to 7 applied Task 1 in six stretches.
Session 8 checked Task 1. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`, called **the
Task 2 commit** below) and committed its report as `905808a7a8b8b8f6e1b609273b19b0dc1a06f76f`, the current tip.

**This is session 10. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for the ledger entries §L.1 to §L.4 only, commits and pushes
that first stretch, writes its report, and STOPS.** Task 3 is done in stretches because the split ruling sizes each
stretch so that the session's whole reading stays well under half its window; the whole of Task 3 is, on the writing
side's estimate (entry 1194, not a measurement), some 1,500 to 2,000 row-parts, against this stretch's 117 lines. Each later stretch gets
its own instruction, written after the previous one is verified.

**What this stretch writes, in one paragraph.** One line beneath the `*PROPOSED DISPOSITION.*` paragraph of each
row-part §L.2, §L.3 and §L.4 place — **117 lines on 102 rows** by the writing side's count (§3.2 lists every one, with
its exact text); three entries appended to the transfer list at the reading file's §10; one sentence added in each of
the four places Task 3 (d) names; and one in-progress line beneath the banner. §L.1 places no row.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the rest applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the dispositions the ruling
records already place; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `905808a7a8b8b8f6e1b609273b19b0dc1a06f76f`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_10_task_3_stretch_1_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is unchanged since the declared start tip** (the big dispatch's Task 3, *Before the edit*):
   `git diff --quiet e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 905808a7a8b8b8f6e1b609273b19b0dc1a06f76f -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must show the same blob;
   record it. Then, with the **Grep tool** in count mode on that file, `RULED DISPOSITION` and `RECORDED DISPOSITION`
   must each count 0. Any other result: STOP and report, the file not touched. (The writing side's staged copy: 5,135,614
   bytes, 83,443 lines, line feeds only, no line longer than 1,900 characters.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 905808a7a8b8b8f6e1b609273b19b0dc1a06f76f -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the six files §5 act 1 lands (this instruction and handoff entries 1193, 1194, 1195,
     1196 and 1197) *(amended 2026-11-23 by the sitting booted on entry 1196, which wrote entry 1197 before this file
     was handed over, as entry 1196 §3 step 1 orders; former wording, kept (#12): "the five files §5 act 1 lands (this
     instruction and handoff entries 1193, 1194, 1195 and 1196)")*, plus the 393 untracked paths sessions 2 to 9 reported and did not land (387 under `scratch_artifacts/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_seven.md` (the current entry point,
   written by the sitting that re-checked this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_six.md` (the one before it, written
   by the sitting that wrote this file; untracked, §5 act 1 lands it). *(Amended 2026-11-23 by the sitting booted on
   entry 1196, as entry 1196 §3 step 1 orders; former wording, kept (#12): entry 1196 as "the current entry point,
   written by the sitting that wrote this file" and entry 1195 as "the one before it", each "untracked, §5 act 1 lands
   it".)*
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md` (§L.1; 9,951 bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md` (§L.2; 12,321);
   - `records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md` (§L.3; 12,428);
   - `records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md` (§L.4; 12,277);
   - `records/cowork/rulings/cowork_rulings_2026_11_08_l3_disposition_words_sitting.md` (3,694) — its Ruling 1 gives the
     words for the rows of §L.2 and §L.3 (the big dispatch carries its lines at §L.2's and §L.3's settled notes; §L.55,
     the record's own entry, says it orders no line beyond them);
   - its surface `ratification_surfaces/cowork_l3_disposition_word_surface_2026_11_08.md` (12,557) — its §2 to §6 list
     the rows;
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part_1a_sitting.md` (13,326)
     — its Rulings 1 to 4 give the words for §L.4's items a, b, d and e.
   **Do NOT read the records of §L.5 to §L.55.**
8. **Two large side files, at these line ranges only, with the Read tool by offset** (each range was located by the
   writing side at the staged copy, 2026-11-23; if a range does not open and close at the heading named, find the
   heading with the Grep tool and report the new range):
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes,
     2,254 lines): **Ruling 3** lines 89–125 (form (b)'s two-record rule applies by part); **Ruling 7** lines 265–312
     (§11 kept in step with the placed rows); **Ruling 9** lines 363–420 (which ADOPTED word, and when *as proposed* is
     written); **Ruling 10** lines 421–471 (Rows 19.39 (ii) and 57.511; *"UNPLACED is not a disposition"*); **Ruling 26**
     lines 1345–1398 (the reading file's §9 points 2 and 8). Rulings 5 and 27 of that record bear on §L.15 and §L.19
     only and are not read.
   - `ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md` (475,634 bytes, 4,245 lines): lines
     172–234 — the *A3* heading paragraph and items (i) to (iv), which Rulings 1 to 4 of the Part 1a record ratify.
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b) and form (b-H) are the forms every line of this
     stretch is written in**, the premise ledger, the declared start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 431–699 (§L.1 to §L.4, your stretch)**;
   - lines 1375–1379 (§L.13's paragraph on the tonality half of Rows 7.63, 8.52 (ii), 19.39 (iv) and 57.353);
   - lines 5800–5906 (§L.55, the disposition-words record's own entry);
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 700–1374 and 1380–5799 (the other ledger entries); lines
   5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the end. Nor the
   derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, §0's heading paragraph);
    - lines 366–432 (§5, the closed vocabulary);
    - **each of the 102 rows of §3.2 below, whole, at §6** (lines 433–78466): find each by its heading with the Grep
      tool, pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** inside §6; read from that
      heading to the row's closing `---`. The writing side found every one of the 102 exactly once; together they come
      to about 152 KB (151,645 bytes from each heading to the line before its closing `---`, measured at the staged
      copy by the re-checking sitting) *(corrected 2026-11-23 by the sitting booted on entry 1196, an apparent error:
      the former figure did not reproduce; former wording, kept (#12): "about 147 KB")*;
    - §10 (lines 78925–79979) at its six `**To …**` headings and at the entries named in §3.3, and §11 (lines
      79980–82117) by search for each row number of this stretch (§3.4);
    - lines 83429–83444 (§15 and §16's first bullet).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch, one line ADDED immediately beneath the row's `*PROPOSED DISPOSITION.*`
   paragraph, the paragraph and every other sentence of the row untouched:
   `*RULED DISPOSITION (<record file>, Ruling N).* <part, if any> **<disposition>** — <placement>.` The record file is
   written as its bare file name, as Ruling 10 of the part 2 record writes it (its lines 451 and 453). Where §3.2 names a
   part, the line names it as §3.2 gives it; otherwise the line names no part.
2. **The record each line names.** For the rows of §L.2 and §L.3 that the disposition-words record places: that record,
   Ruling 1 (the big dispatch's §L.2 settled note: *"Each line is form (b), naming the disposition-words record, Ruling
   1, and quoting the phrase-ends record's own placement"*; §L.3's settled note, the same for the phrase-units record).
   For the rows §L.3 places by the phrase-units record's own words (its Ruling 1 and Ruling 2 item f): the phrase-units
   record. **For every row of §L.4: the cadence-placement record** — Ruling 1 for its five decided-against rows, Ruling 2
   for every other row, including the fifteen row entries whose word Rulings 1 to 4 of the Part 1a record ratify.
   *Authored by the writing side, overrulable by the user. Grounds: Task 3 (a) adds, for every row-part a §L entry
   places, a line in the forms section's form, and form (b) names the record that places the row; §L.4's Open note
   says the fifteen get "one HISTORICAL line quoting its item's sentence", the item being the cadence-placement record's;
   and Ruling 6 of the Part 1a record says of a line it ratifies the same way that "both lines come from the one record",
   which the writing side reads as the cadential six-four record, whose ruling that line quotes, not the Part 1a
   record. Unlike the disposition-words record, the Part 1a record
   does not say which record a line names.*
3. **The quotation.** Each line quotes the words §3.2 gives for it, taken from the record §3.2 says the line quotes:
   the phrase-ends record for (a) to (c), the phrase-units record for (e) to (g), the cadence-placement record for (h)
   to (m). For (a) to (c) and (g) that is not the record the line names (§3.1 item 2) *(corrected 2026-11-23 by the
   sitting booted on entry 1196, an apparent error: "the cell" named nothing in this file; former wording, kept (#12):
   "taken from the record named in the cell")*. **Before
   writing each line, find those words in the record you read whole (§2 item 7) and compare them character for
   character, line breaks read as spaces.** A difference is a STOP-and-report for that line: no line written, listed
   in the report under *rows the act could not place* with both texts. Where §3.2's quotation carries `…`, the
   Part 1a record quotes it so (its Ruling 3), and the comparison is of the two pieces either side of it.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in §6; the part §3.2 names exists in
   the row's *Outgoing statement* claims; and **the row's outgoing statement fits what the record says of it** — the
   ruling's condition binds here (disposition-words record, Ruling 1: *"Where the surface sorts rows from the reading
   file's §12 one-sentence lines (§3's seven, §4, §5), the act reads each row at §6 and stops and reports any that does
   not fit."*). A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act
   could not place* with what was read. Nothing is re-read into a different placement.
5. **As proposed.** §3.2 says *as proposed* only on the three lines where the row's own proposed word is the word
   placed and the record says *"as proposed"* (Rows 57.157, 28.35, 28.50). Check each line's word against the row's
   `*PROPOSED DISPOSITION.*` paragraph for that part; if you find a line where §3.2's choice disagrees with form (b)'s
   paragraph *Which ADOPTED word, and when as proposed is written*, STOP-and-report that line. No other wording (such as
   *"placed from"*) is added — Ruling 9 of the part 2 record, in force over the disposition-words record's *"placed from
   UNPLACED"* for Row 40.24 (iii).
6. **Order beneath a row with more than one line.** The lines stand in the order of the ledger entry that carries them:
   §L.2's lines (the disposition-words record's, as §L.2's settled note carries them) first, then §L.3's, then §L.4's.
   *Authored by the writing side, overrulable by the user. Ground: §L.55 says the disposition-words record's lines are
   "carried at" §L.2's and §L.3's settled notes and that "this entry and those notes describe the same line, not two";
   Task 3 (b) lists the entries in ledger order.*
7. **Sides and halves.** For the nine rows the phrase-ends record carries to the cadence family, the record names a
   *"phrase side"* and a *"cadence side"*; for Rows 7.63, 8.52 (ii), 19.39 (iv) and 57.353 the disposition-words record
   names a *"phrase half"* and a *"tonality half"*. The line names its part and then its side or half, as §3.2 gives it
   (for example `(ii), its phrase side:`). *Authored by the writing side, overrulable by the user; the forms section has
   no form for a side of a part.*
8. **Two lines on the same part with differing dispositions** (form (b)'s two-record rule, by part): the writing side
   found none in this stretch, comparing the row and part numbers of §3.2. If you find one, that part is a STOP-and-report and gets neither line.

### 3.2 The lines, entry by entry, with their exact text

Each line below is given whole, as it is to be written, the angle-bracketed part filled in as the paragraph says;
where the row has no part, `<part>` and the space after it are dropped. Each quotation keeps the record's own marks
(italics, backticks) as the record writes them.

**§L.1 — the route record.** No line (its §4: *"places no row"*).

**§L.2 — the phrase-ends record; every line names the disposition-words record, Ruling 1, and quotes the phrase-ends record.** 74 lines.

(a) The 23 rows the record names as overtaken and the seven more the surface reads as of that kind (surface §3) — 30
lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* <part> **HISTORICAL** — "recorded as overtaken by the charter and Ruling 48, a consequence recorded under D-599 and not a separate choice".`
Rows (part in brackets where named): 2.16 (ii), 7.33 (ii), 7.68 (i), 8.24, 8.26 (i), 8.95, 8.96 (i), 8.97, 8.101 (i),
8.105 (ii), 8.112, 19.30 (ii), 19.31 (ii), 19.58 (iii), 36.21, 36.38 (ii), 36.40 (i), 36.86 (ii), 36.109 (i),
38.1 (ii), 57.50, 57.249, 57.290; and 3.1 (ii), 8.14 (ii), 8.16 (ii), 8.28 (ii), 8.60 (i), 8.87, 19.41.

(b) The 35 rows the surface reads as method rows (surface §4) — 35 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* <part> **HISTORICAL** — "The method rows (peak-picking, forcing markers, the primitive's worked examples) are the rows Ruling 1 decides against.".`
Rows: 7.116 (ii), 8.16 (i), 8.43, 8.66, 10.9, 19.38 (iii), 36.4 (i), 36.4 (ii), 36.11 (ii), 36.16 (i), 36.37 (ii),
36.37 (iii), 36.45 (ii), 36.48 (ii), 36.60 (i), 36.60 (ii), 36.61, 36.64, 36.65, 36.76 (ii), 36.77 (ii), 36.78 (ii),
36.79 (ii), 36.80 (ii), 36.81 (ii), 36.82, 36.91 (i), 36.94 (iii), 36.113 (i), 36.115 (ii), 36.124, 36.125 (ii),
38.71, 40.6, 57.153 (ii). *(Rows 36.4, 36.37 and 36.60 get two lines each, one per part.)*

(c) The phrase side of the nine rows carried to the cadence family (surface §5) — 9 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* <part, its phrase side:> **HISTORICAL** — "Ruling 1 settles their phrase side only.".`
*(Corrected 2026-11-23 by the sitting booted on entry 1196, an apparent error: the closing full stop form (b) puts
after every placement, as in every other line of §3.2, was missing; former wording, kept (#12): the same line ending
`only."` with no full stop after the closing quotation mark.)*
Rows: 36.6 (ii), 36.12 (ii), 36.14 (iii), 36.58 (i), 36.133 (ii) — written `(ii), its phrase side:` and so on; and
2.15, 2.18, 7.336 — written `Its phrase side:`; and 57.502 (i) — written `(i), its phrase side:`.

(d) **No line from §L.2 for Rows 19.39 (ii) and 57.511.** UNPLACED is not a disposition (Ruling 10 of the part 2
record); their one line is the chord-span pair record's, written by the stretch that applies §L.48.

**§L.3 — the phrase-units record.** 21 lines.

(e) Ruling 1's seven decided-against rows — 7 lines, each naming **the phrase-units record, Ruling 1**, form (b-H):
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 1).* <part> **HISTORICAL** — "Rows 8.4 (i), 8.68, 8.69, 8.70, 8.72, 36.10 (ii) and 36.113 (ii) recorded as decided against.".`
Rows: 8.4 (i), 8.68, 8.69, 8.70, 8.72, 36.10 (ii), 36.113 (ii).

(f) Row 57.157 — 1 line:
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).* **RELOCATED** to ***L1 — Change points, candidates and notated evidence*** — as proposed; "semitone versus spelled interval is L1's publication (RELOCATED as proposed)".`
§10 already carries the row (§3.3); nothing is appended for it.

(g) The thirteen rows the disposition-words record places (surface §2), each line naming **the disposition-words record, Ruling 1**, quoting the
phrase-units record's Ruling 2 item:
- 36.63 (item a): `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* **HISTORICAL** — "the phrase end is where L3 decides it, not at a picked peak; follows from Ruling 1 of the morning's record".`
- 8.84 (i) (item b): `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* (i) **HISTORICAL** — "the cadential arrival (L3-S10) is not held to a fixed window".`
- 36.74 (i) and 36.146 (item c), one line each (36.74 written with `(i)`, 36.146 with no part):
  `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* <part> **HISTORICAL** — "the phrase-length term (L3-S9 family (iii)) is in the model from the start as a fitted weight"; the term itself is L3-S9 family (iii).`
  *(The closing clause is the surface's §2 item c: "the line adding that the term itself is L3-S9 family (iii)".)*
- 40.24 (iii) (item d): `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* (iii) **ADOPTED — proposed** — "accelerating harmonic rhythm before a candidate position, read from L2's published boundaries, enters as a candidate term admitted only if a held-out measurement repays it (as L3-S9 (iv))".`
  Not *as proposed* (the part was proposed UNPLACED). List it under *ADOPTED words read at the row*.
- 37.46 (item e): `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* **RELOCATED** to ***the second axis — voice leading*** — "no conflict of substance with L3-S9: reading per-voice surface cues as phrase evidence is not modelling voice leading, which the framework gives its own axis".`
- 8.45 (ii) and 57.259 (item h), one line each (8.45 written with `(ii)`, 57.259 with no part):
  `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* <part> **RELOCATED** to ***L1 — Change points, candidates and notated evidence*** — "the notated evidence and its scope stay at L1 (relayed through L3-S9 (i)); L3 does not copy them onto its units (#6)".`
- 36.112 (item i): `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* **HISTORICAL** — "the stable-key-run fallback is not adopted".`
- 7.63, 8.52 (ii), 19.39 (iv), 57.353 (item g), **the phrase half only**, one line each (7.63 and 57.353 written
  `Its phrase half:`, the other two `(ii), its phrase half:` and `(iv), its phrase half:`):
  `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1).* <part, its phrase half:> **ADOPTED — carried** (L3-S8) — "a change of tonality may fall inside a phrase unit and a phrase may end without one; follows from Ruling 1 (no evidence forces or forbids a phrase end)".`
  Not *as proposed* (each was proposed ADOPTED — proposed). List all four under *ADOPTED words read at the row*.
- **The tonality half of those four rows gets no line.** §L.13 found the key-areas record does not reach them, so on
  the disposition-words record's words it is UNPLACED (the big dispatch, lines 1375–1379); UNPLACED is not a
  disposition (Ruling 10 of the part 2 record), and *"Rows no family reaches stay proposals"* (the route record, line
  58). *Authored by the writing side, overrulable by the user.* List the four under §6 item 6 of this file.

**§L.4 — the cadence-placement record; every line names the cadence-placement record.** 22 lines.

(h) Ruling 1's five decided-against rows — 5 lines, form (b-H):
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 1).* <part> **HISTORICAL** — "Rows 8.47 (ii), 8.86, 8.116 (ii), 8.129 (ii) and 8.130 recorded as decided against.".`
Rows: 8.47 (ii), 8.86, 8.116 (ii), 8.129 (ii), 8.130.

(i) Rows 28.35 and 28.50 (item c) — 2 lines, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).* **QUARANTINED** — as proposed; "QUARANTINED as proposed: the reading file's vocabulary places a statement of *"how the implementation currently works"* there, and under the phase rule a disagreement between specification and code is evidence reserved for the audit".`
§11 already carries both rows (§3.4); nothing is added there for them.

(j) Item a — 5 lines, the part named, each (Part 1a record, Ruling 1):
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).* <part> **HISTORICAL** — "the cadence is L3's, read off L2's decided chords at L3's decided phrase ends, not detected by the old function layer and read by the grouping layer; follows from the charter".`
Rows: 8.11 (ii), 8.59 (ii), 8.101 (ii), 9.89 (iii), 37.31 (i).

(k) Item b — Row 40.64, 1 line (Part 1a record, Ruling 2):
`` *RULED DISPOSITION (cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).* **HISTORICAL** — "evidence-class facts are published without a named consumer, each with its establishment status (`CLAUDE.md`, the fact-publication corollary's amendment of 2026-07-12); and the pattern evidence has a consumer in any case, L3's phrase decision (L3-S9 (ii)). Documentation only.". ``
*(Double backticks delimit this line here only because its quotation carries backticks; write the line itself with
none of the delimiters.)*

(l) Item e — the cadence side of Rows 2.15, 2.18, 7.336 and 57.502 (i), 4 lines (Part 1a record, Ruling 3), the first
three written `Its cadence side:`, the last `(i), its cadence side:`:
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).* <part, its cadence side:> **HISTORICAL** — "D-495 (the flat-profile fallback) loses its subject at L3 … Algorithm: the old fallback rule drops out; no new mechanism.".`

(m) Item d — the cadence side of Rows 36.6 (ii), 36.12 (ii), 36.133 (ii), 36.14 (iii) and 36.58 (i), 5 lines (Part 1a
record, Ruling 4), each written `(ii), its cadence side:` and so on:
`*RULED DISPOSITION (cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).* <part, its cadence side:> **HISTORICAL** — "the cadence is read at L3's decided phrase ends, not at a gate fed by peaks picked from the page; follows from the morning's Ruling 1 and the charter. Algorithm: nothing beyond Ruling 1.".`
**The (i) parts of Rows 36.6, 36.12 and 36.133 get no line** (Part 1a record, Ruling 4).

(n) **Rows §L.4 mentions and does not place** — 2.7 (iii), 7.108, 7.109, 2.16, 2.17, 8.37, 7.97: no line from the cadence-placement record. (Row
2.16 (ii) has its §L.2 line from (a); that is not a line from the cadence-placement record.)

**The count.** §L.2: 30 + 35 + 9 = 74. §L.3: 7 + 1 + 13 = 21 (the thirteen being 1 + 1 + 2 + 1 + 1 + 2 + 1 + 4).
§L.4: 5 + 2 + 5 + 1 + 4 + 5 = 22. **117 lines on 102 rows**; the fifteen rows with two lines are the nine carried rows
and Rows 8.101, 36.113, 8.16, 36.4, 36.37 and 36.60.

### 3.3 The transfer list, §10 (Task 3 (c) item 5)

Three row-parts are placed RELOCATED out of another proposal and are not on §10 at the writing side's search (every
row number of the stretch searched as a bare number, so that entries listing several rows are reached, and each hit
read for its claim). Append each **after the last entry under its destination heading and before the next
`**To …**` heading**, in §10's entry form, in this order:

- Under `**To *L1 — Change points, candidates and notated evidence*.**` (line 79008 at staging; the next heading at
  line 79125):
  `- Row 8.45 (ii) — that each phrase unit carry the notated evidence that opened and closed it, with that evidence's scope. *(cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1.)*`
  `- Row 57.259 — that each phrase unit carry the scope of the notated evidence that opened and closed it. *(As Row 8.45 (ii), travelling with it; cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1.)*`
- Under `**To *the second axis — voice leading*.**` (line 79621 at staging; the next heading at line 79701):
  `- Row 37.46 — that the harmonic spine is structurally blind to how the lines move. *(cowork_rulings_2026_11_08_l3_disposition_words_sitting.md, Ruling 1.)*`

*The subject clauses are the writing side's, taken from each row's own heading or proposal; overrulable by the user.*
Check each at §10 by row number and claim before appending; a row-part §10 already carries is not appended. Row 57.157
is on §10 already (in the entry beginning `- Rows 57.153 (i), 57.154 (i), …`, line 79117 at staging): nothing is
appended for it. Task 3 (c) item 6 (*LEAVES L3* lines and the Row 7.67 line) does not reach this stretch.

### 3.4 The audit questions, §11 (Task 3 (c) item 7)

**Expected: nothing to write.** Rows 28.35 and 28.50 are placed QUARANTINED as proposed and §11 carries both (lines
81052 and 81072 at staging). The writing side searched §11 for every row number of this stretch as a bare number: the
only other hits are Row 8.4 (ii) and Row 57.502 (ii), which are other claims than the parts this stretch places, so
they are not touched. The same search of §10 found twenty-nine of the stretch's rows, besides Row 57.157, in §10 entries, every one for a claim
other than the part this stretch places (for example Rows 19.30 (i), 36.37 (i), 36.94 (i) and (ii), 38.1 (i), 9.89 (i), (ii), (iv) and (v));
none of them is touched, since Task 3 (c) item 6 does not reach this stretch. Run the same search yourself; if you find a §11 entry for a part this stretch places with a word other than
QUARANTINED, add the NOT QUARANTINED line (c) item 7 (b) gives, and report it.

### 3.5 The file's own statements of its state (Task 3 (d), part)

1. **The four state sentences, written in this stretch.** The banner's sentence `**EVERY DISPOSITION BELOW IS A
   PROPOSAL.**` (line 41), §0's heading paragraph (line 58 onward), §15's `**NOTHING.**` paragraph (line 83431) and
   §16's first bullet (line 83437) each gain the sentence Task 3 (d) gives, word for word, with the former wording kept
   in place in the file's own preserved-wording shape, exactly as Task 3 (d) orders. The sentence is true at every
   stage of the stretches: it says which rows carry a line and that every other row remains a proposal.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a.** The §13 sentence says the ruled
   distribution *"is §13a"*, and §13a is derived from every added line; both are written by the session of the last
   stretch. *Authored by the writing side, overrulable by the user.*
3. **The in-progress line.** Insert ONE line, and one blank line after it, between the blank line 53 (the one after the
   banner's last line, line 52, ending *"…the deriving session relays the same counts in its own §4 and §5."*) and the
   `---` at line 54, so that the banner block is followed by a blank line, this line, a blank line and the `---`; the
   line stands outside the banner. *(Corrected 2026-11-23 by the sitting booted on entry 1196, an apparent error: the
   former place, between line 52 and line 53, contradicted the result the same sentence states and would have joined
   the line to the banner's quotation block; former wording, kept (#12), the quoted banner sentence elided as [the
   sentence quoted above]: "between the banner's last line (line 52, ending [the sentence quoted above]) and the blank
   line before the `---` at line 54".)* Exactly:

   `*Application in progress: the RULED DISPOSITION lines in this file are those of §L.1 to §L.4 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.5 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   *Authored by the writing side, on the shape of session 2's in-progress line in the successor; overrulable by the
   user.* Attribute it in the diff table to *"session 10's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.1 to
   §L.4 only, in ledger order, with the disposition-words record's lines for §L.2's and §L.3's rows written at those
   entries** (§3.1 item 6). §L.5 to §L.55 are not applied, read or touched.
3. **A1, for five paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1193, 1194, 1195, 1196 and 1197 ARE landed**, with this file, in §5 act 1, as sessions 8 and 9 landed theirs.
   *(Amended 2026-11-23 by the sitting booted on entry 1196; former wording, kept (#12): "A1, for four paths only";
   "Handoff entries 1193, 1194, 1195 and 1196 ARE landed".)* Any other
   untracked handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the four records of §L.1 to §L.4
   and the disposition-words record only. The writing side's search, line breaks joined, case not matched, found three
   hits, each already placed by its entry: the phrase-ends record's *"are the rows Ruling 1 decides against"* (§3.2
   (b)), the phrase-units record's *"recorded as decided against"* (§3.2 (e)) and the cadence-placement record's
   *"recorded as decided against"* (§3.2 (h)); none in the route record or the disposition-words record. List each hit
   you find in the report. Items 2, 3 and 4: not reached by this stretch (§L.3's §9 points are Ruling 26's: nothing
   written at §9 and no listing of their own). Item 5: §3.3. Item 6: not reached. Item 7: §3.4.
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **An added line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, finish
   §3.5 with the in-progress line naming the last entry actually applied instead of §L.4 (and §L.5 accordingly), commit
   the entries already applied, and report which. If you are inside an entry, do not commit; STOP and report which
   entries were applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run as written, against the Task 2 commit:
   `git diff 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session10_task3_diff.txt"; echo "exit:$?"`,
   read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted in this
   stretch:** a line under (a) for §L.2, §L.3 or §L.4; a §10 addition of §3.3; a NOT QUARANTINED line only if §3.4
   found one; one of the four state sentences with its preserved former wording; the in-progress line. No §13 sentence,
   no §13a, no *LEAVES L3* line, no Row 7.67 line. No deleted line, save a line one of the four state sentences is
   written into. Then, with the Grep tool in count mode: the pattern `\*RULED DISPOSITION \(` (a line's opening label)
   must count **117 less the number of row-parts you listed as STOP-and-report**, and `\*RECORDED DISPOSITION \(` must
   count 0. (The bare words `RULED DISPOSITION` and `RECORDED DISPOSITION` also occur in the four state sentences and
   in the in-progress line, so they are not counted bare.) Any other count, or a changed
   passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 1 (§L.1 to §L.4): the rows placed by the first four ledger entries re-marked in the reading file, three transfer-list entries added and the file's state sentences written, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_10_task_3_stretch_1_2026_11_23.md`**, as sessions 2 to 9 each
    wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.5, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's six files first, in a commit of their own.** Exactly six paths, all expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_10_task_3_stretch_1_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_three.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_four.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_five.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_six.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety_seven.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1193 to 1197 and the session 10 instruction of the L3 application landed; Task 3 stretch 1 follows`
   *(Amended 2026-11-23 by the sitting booted on entry 1196, entry 1197 added; former wording, kept (#12): "five files",
   "Exactly five paths", the list ending at entry 1196, and the subject's "handoff entries 1193 to 1196".)*
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for §L.1 to §L.4**, as the big dispatch's Task 3 and §3 and §4 above give it: the lines of §3.2 entry by
   entry, with §3.3's appendices at §L.3; then §3.4's search; then §3.5; then §4 item 8's check, its commit and its
   push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_10_task_3_stretch_1_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 10 of the L3 application, Task 3 stretch 1 (§L.1 to §L.4) written; stretch 2 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.1 to §L.4, in order: every line by row and part, written (with its reading-file line number after the
   edit) or STOP-and-report (and why). The same for §3.3's three entries and §3.4's search.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place*; *rows named by more than
   one record* (the nine carried rows, with both lines; and, as the §L entries of this stretch and §L.55 name them, the
   rows of this stretch a later entry also places — Rows 19.39 (ii) and 57.511 at §L.48, the 39 rows at §L.52, the
   section side of Rows 8.24, 19.30 (ii), 19.31 (ii) and 19.58 (iii) and Row 19.38 (iii) at §L.12, Rows 7.116 (ii) and
   40.6 at §L.46, Rows 7.63 and 8.52 (ii) at §L.25 — each marked *to be written by a later stretch*); *ADOPTED words read
   at the row* (the five rows of §3.2 (g) named there); the decided-against hits (§4 item 4).
5. The diff table of §4 item 8, every changed passage attributed, and the two counts.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: Rows 19.39 (ii) and 57.511 (§3.2 (d)); the
   tonality half of Rows 7.63, 8.52 (ii), 19.39 (iv) and 57.353 (§3.2 (g)); the (i) parts of Rows 36.6, 36.12 and
   36.133 (§3.2 (m)); the rows of §3.2 (n). *A heading of this session's report only, authored by the writing side; it
   is not one of the headings Task 3 names.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 10 of the L3 application ends here. Stretch 2 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a row-part that
  is STOP-and-report under them, or under §3.1 items 3 to 5 and 8, is reported and the rest applied, as they say);
- §4 item 8's check finds a changed passage it cannot attribute, or a count other than the one it gives;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1195. Read at the objects for this file: the
three git reference files (both refs `905808a7…`); entries 1195, 1194 and 1026 whole; the seven files of
§2 item 7 whole; the release part 2 record's headings and its Rulings 9 and 10 whole; the working list at lines 131–239;
the big dispatch at lines 99–699, 1372–1411, 5800–5906 and 6616–6820, and its `###` and `##` headings; sessions 2 and
9's instructions whole; the reading file at lines 1–60 and 83429–83444, its `##` headings, its §10 `**To …**` headings
and the entries at lines 79112–79122 and 79600–79702, its §11 entries for Rows 28.35 and 28.50, the proposed paragraphs
of Rows 57.157, 28.35, 28.50, 7.63, 8.52, 19.39, 57.353, 40.24, 36.112, 36.63, 8.84, 36.74 and 36.146, and the headings
of Rows 37.46, 8.45 and 57.259. Measured by read-only searches over staged copies: each of the 102 rows' headings
occurring once in §6, and their blocks' total size (146,545 bytes); the §10 and §11 hits for every row number of the
stretch, searched as bare numbers, each hit's entry read for its claims (two first searches were replaced: one required the
word "Row" before the number and so missed entries listing several rows, and one, with an alternation in its pattern,
missed some hits in this container's grep; the search relied on uses look-around matching); the decided-against hits in the six records; the reading file's line count and line endings; the line ranges
of §2 item 8. Not computed by this sitting: any git blob or hash; the hashes in §1 are relayed from entries 1194 and
1195 [checked there] and are re-checked by Claude Code in §1 before they are relied on. Relayed, not re-checked here:
the end of `cowork_handoff.md`'s topmost block at line 255, the size and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section, and the 393 untracked paths,
as session 9's instruction gives them. The user's words: the opening instruction; "shortened".*

*Provenance of the re-check: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1196. Read at the objects: this
file whole (44,591 bytes, SHA-256 `8158c93a…`, as entry 1196 records it); the seven files of §2 item 7 whole, every
quotation of §3.2 compared with its record, line breaks read as spaces (all equal); the big dispatch at lines 99–699,
1372–1381, 5816–5884 and 6616–6820, and lines 5800–5859 by search; the release part 2 record at Rulings 3, 9 and 10 whole and its `##` headings (the
line ranges of §2 item 8 open and close at their headings); the working list at lines 165–239; the reading file at
lines 50–57, its `##` headings, the 102 rows' headings and `*PROPOSED DISPOSITION.*` paragraphs (every part §3.2 names
present; every proposed word as §3.2 assumes; *as proposed* only on 57.157, 28.35 and 28.50), §10 and §11 searched for
every row number of the stretch as a bare number with look-around matching and each hit's claim read (§10: thirty rows,
57.157 and twenty-nine others, each hit another claim; §11: 8.4 (ii), 28.35, 28.50, 57.502 (ii)); the decided-against
search over the five records (three hits, as §4 item 4); session 9's report at its working-tree row (393 untracked;
`1df4f207…`). Computed as git would on the staged copies: the big dispatch's blob `b5274c2c…` and the archive JSON's
`1df4f207…` once its carriage returns are removed. `cowork_handoff.md`'s topmost block ends at line 255 and
`cowork_audit_protocol.md`'s dispatch-protocol section opens at line 180 [checked]. Four apparent errors corrected and
entry 1197 added, each marked where it stands. The user's words: the opening instruction; "shortened".*
