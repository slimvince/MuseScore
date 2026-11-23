# CC dispatch — the L3 application, SESSION 12 of several: Task 3 of the L3 application dispatch, third stretch (§L.13 to §L.20), and nothing else

> **STATUS: WRITTEN 2026-11-23, NOT YET RELEASED,** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Session 10 applied Task 3's first stretch, §L.1 to §L.4. Session 11 applied the
second stretch, §L.5 to §L.12 (commit `402ed789f5caba5de5ca64798b7ecf3d9c599212`, called **the stretch 2 commit**
below), and committed its report as `760c3cfb713be89aeb679966742ba0f1c9eae843`, the current tip.

**This is session 12. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for the ledger entries §L.13 to §L.20 only, commits and
pushes that third stretch, writes its report, and STOPS.**

**What this stretch writes, in one paragraph.** One line beneath the `*PROPOSED DISPOSITION.*` paragraph of each
row-part §L.13, §L.15, §L.16, §L.17, §L.18, §L.19 and §L.20 place, after any line an earlier stretch already wrote
there — **92 lines: 39 opening `*RULED DISPOSITION (`** (form (b) or (b-H)) **and 53 opening `*RECORDED DISPOSITION (`**
(form (d), the first recorded lines of the application). §3.2 lists every one with its exact text. Beside them: one
entry appended to the transfer list at §10 (Row 38.11 (i)); the *Row 7.67 is not transferred* line at §10 (Task 3 (c)
item 6); five audit questions added to §11 (Rows 8.31 (i), 15.16 (i), 21.27, 21.28, 21.29); **two labels session 11
wrote corrected** (*"rest"* → *"remainder"*, §3.5 item 4); and the in-progress line brought forward from §L.12 to §L.20.
§L.14 gives no line in this stretch (§3.2, §L.14).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the dispositions the records
already place; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `760c3cfb713be89aeb679966742ba0f1c9eae843`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_12_task_3_stretch_3_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 2 commit left it.**
   `git diff --quiet 402ed789f5caba5de5ca64798b7ecf3d9c599212 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 760c3cfb713be89aeb679966742ba0f1c9eae843 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `3438641649f942b74024832ad18b5fce47bfde2d`. Then, with the **Grep tool** in count mode on that file: the pattern
   `\*RULED DISPOSITION \(` must count **212**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **0**. Any other result: STOP and report, the file not touched. (The writing side's staged copy: 5,186,605
   bytes, 83,879 lines, line feeds only, no line longer than 1,867 characters.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 760c3cfb713be89aeb679966742ba0f1c9eae843 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1200 and 1201),
     plus the 393 untracked paths sessions 2 to 11 reported and did not land (387 under `scratch_artifacts/`;
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
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the remainder of that
   section or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and
   no guard.
4. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_one.md` (the current entry point, written
   by the sitting that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred.md` (the one before it, written by the sitting
   that verified session 11; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The records this stretch rests on, each WHOLE** — they are the authority for every line this session writes
   (**the record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md` (§L.13; 11,601 bytes);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md` (§L.15; 8,964);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md` (§L.16; 10,846);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md` (§L.17; 11,895);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md` (§L.18; 10,955);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md` (§L.19; 13,203);
   - `records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md` (§L.20; 12,069).
   **The pivot-label record §L.14 enters** (`records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md`)
   **is NOT read whole**: no line is written from it in this stretch (§3.2, §L.14). Run Task 3 (c) item 1's search over
   it with the Grep tool only (§4 item 4).
   **Do NOT read the records of §L.1 to §L.12 or of §L.21 to §L.55.**
8. **Side records, at these line ranges only, with the Read tool by offset** (each range was located by the writing
   side at the staged copy, 2026-11-23; if a range does not open and close at the heading named, find the heading with
   the Grep tool and report the new range):
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part_1b_sitting.md`
     (10,894 bytes): lines 24–88 (**Rulings 2 to 5**: the marking claim of Rows 54.14 (i) and 54.36 (ii); Rows 4.23 (i),
     4.28 and 4.29; the remainder of Rows 4.24 (ii) and 4.26; the remainder of Row 4.17's figured-bass item) and lines
     109–128 (**Ruling 7**, Row 10.34).
   - `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes, 2,254
     lines): **Ruling 3** lines 89–125 (form (b)'s two-record rule applies by part); **Ruling 5** lines 162–210 (Row 7.67
     and its §10 line); **Ruling 7** lines 265–312 (§11 kept in step with the placed rows); **Ruling 9** lines 363–420
     (which ADOPTED word, and when *as proposed* is written); **Ruling 12** lines 523–574 (Rows 36.5 (ii), 45.14 (i) and
     45.15 (i) get no line); **Ruling 27** lines 1399–1461 (the reading file's §9 point 1).
   - `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part13_sitting.md` (5,832
     bytes): lines 12–59 (**Ruling 1**: the five rows of the figured-bass record's §2 (a) already stand on §10).
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, form (b-H) and form (d) are the forms every line of this stretch is written in**, the premise
     ledger, the declared start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 1329–2251 (§L.13 to §L.20, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–1328 (§L.1 to §L.12, applied by sessions 10 and 11); lines
   2252–5906 (the other ledger entries); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4
   and 5); lines 7136 to the end. Nor the derivation, the successor, `FRAMEWORK.md` or
   `cowork_derived_specification_l0_l1_2026_09_03.md`.
10. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
    the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
    - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
    - lines 368–434 (§5, the closed vocabulary);
    - **each of the 87 rows §3.2 names, whole, at §6** (lines 435–78898): find each by its heading with the Grep tool,
      pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** inside §6; read from that
      heading to the row's closing `---`. The writing side found every one of the 87 exactly once; together they come to
      about 123 KB (123,447 bytes from each heading to the line before its closing `---`, measured at the staged copy);
    - the two lines session 11 wrote that §3.5 item 4 corrects (by search, §3.5 item 4);
    - §10 (lines 79357–80415) at its six `**To …**` headings, at the places §3.3 names, and by search for each RELOCATED
      row-part of this stretch; §11 (lines 80416–82553) at the member blocks §3.4 names, and by search for each row number
      of this stretch;
    - §15 and §16's first bullet (find each by its heading), to see that session 10's state sentences stand.

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch for a ruled line, form (d) for a recorded line, one line ADDED beneath the
   row's `*PROPOSED DISPOSITION.*` paragraph, the paragraph and every other sentence of the row untouched:
   `*RULED DISPOSITION (<record file>, Ruling N).* <part, if any> **<disposition>** — <placement>.` or
   `*RECORDED DISPOSITION (<record file>, §<section>).* <part, if any> **<disposition>** — <as proposed, or the placement
   in the record's words>; <the record's ground for the row, in its words>. Recorded by the record as this side's
   derivation, not ruled; challengeable at the row.` The record file is written as its bare file name, as sessions 10 and
   11 wrote it. Where §3.2 names a claim or a portion, the line names it as §3.2 gives it; otherwise the line names none.
2. **Where the line goes.** Each line is preceded by one blank line, as the earlier stretches' lines stand. Where the row
   carries no `*RULED …` or `*RECORDED …` line yet, the new line goes after the blank line that follows the
   `*PROPOSED DISPOSITION.*` paragraph. **Where the row already carries one or more lines from an earlier stretch, the new
   line goes after the last of them**, so that every row's lines stand in ledger order. *Authored by the writing side,
   overrulable by the user; the same rule as session 11's instruction §3.1 item 2.* The rows of this stretch that already
   carry an earlier line: **3.1** (two lines: the disposition-words record's on (ii), the sections record's on (i)) and
   **40.24** (the disposition-words record's on (iii)) — each read at the staged copy; check each at the row.
3. **Order beneath a row that gets more than one line from this stretch.** Ledger order first; within one entry, the
   order §3.2 gives. Rows that get more than one line from this stretch: **3.5** ((i), then (ii), both §3.2 (b));
   **54.14** ((ii) from (d), then (i)'s tag-only portion from (e), then (i)'s marking portion from (f)); **54.36** ((i)
   from (d), then (ii)'s tag-only portion from (e), then (ii)'s marking portion from (f)). No other row gets two lines from
   this stretch (checked against §3.2 by the writing side, row by row).
4. **The record each line names.** The record that places the row in the §L entry's table, with the ruling or the
   section the table names (§3.2 gives it for every line). For the rows whose word a ruling of the application's release
   gives (Rows 54.14 (i) and 54.36 (ii) for their marking portion, 4.23 (i), 4.28, 4.29, 4.17, 4.24 (ii), 4.26, 7.67 and
   10.34), the line still names the family record whose sentence it quotes, not the release ruling. *Authored by the
   writing side, overrulable by the user; the same rule as session 11's instruction §3.1 item 4. Ground: the Part 1b
   record's Ruling 7 names Row 10.34's line "(form (d), the chord-symbol record, §2 (c))".*
5. **The quotation.** Each line quotes the words §3.2 gives for it. **The writing side took them from the record, guided
   by the big dispatch's §L table cell for the row, and checked every one against the record by a read-only script (words
   and punctuation, line breaks read as spaces, the bold and italic asterisks not compared).** **Before writing each line,
   find its quoted words in the record you read whole (§2 item 7) and compare them the same way: every word and every
   punctuation mark must match, line breaks read as spaces; asterisks are not compared, and the line keeps its marks
   exactly as §3.2 gives them.** A difference is a STOP-and-report for that line: no line written, listed in the report
   under *rows the act could not place* with both texts. Where §3.2's quotation carries `…`, the comparison is of the two
   pieces either side of it. Where a line carries two or three quotations, each is compared. *(The asterisk rule is the
   writing side's, overrulable by the user: several quotations here open or close inside a span the record writes in bold
   — for example the mass-and-status record's §2 (a) heading — and session 11's rule, which kept the record's marks inside
   the span, did not say what to do with a mark that opens before the span.)*
6. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in §6; the claim §3.2 names exists
   in the row's `*PROPOSED DISPOSITION.*` paragraph; and **the row's outgoing statement fits what the record says of
   it**. A row that does not fit is a STOP-and-report for that row-part: no line, listed under *rows the act could not
   place* with what was read. Nothing is re-read into a different placement.
7. **As proposed.** §3.2 writes *as proposed* on the lines whose record places the row as proposed in its own words
   (*"as proposed"*, *"proposals stand"*, *"Their proposals stand"*, *"The proposals stand"*, *"stay QUARANTINED"*): §3.2
   (i), (j), (m), (n), (p), (q), (r), (s), (u), (v), (w), (x), (bb), (ii). It is **not** written on any other line. In
   particular: **§3.2 (a)**, the seven key-area rows, each proposed ADOPTED — proposed — the record writes *"ADOPTED (the
   definition as ruled)"*, which adopts the ruled definition, not each row's proposal as proposed (the writing side's
   reading, overrulable by the user; §L.13's *Open* point (1) leaves *as proposed* to be read at the row); **§3.2 (o)**
   (Row 38.11 (i), proposed UNPLACED); **§3.2 (t)** (Row 10.34, the Part 1b record's Ruling 7: *"the line does **not**
   say *as proposed*"*); and every line whose row the record *"corrected"* from its proposal. *Ground: form (b)'s paragraph
   — "The line says as proposed only where its word, and its number if any, are the row's own proposed word for that
   part, and the record adopts the content as proposed"; and the Part 1b record's Rulings 2 to 5 and 7, each "no as
   proposed".* Check each line's word against the row's `*PROPOSED DISPOSITION.*` paragraph for that claim; if you find a
   line where this choice contradicts form (b)'s paragraph, STOP-and-report that line. No other wording (such as
   *"placed from"*) is added.
8. **Two lines on the same claim with differing dispositions** (form (b)'s two-record rule, by part; form (d)'s last
   sentence). **None in this stretch, by the writing side's comparison**, across stretches included: Row 3.1's (iii) is
   another claim than the (i) and (ii) the earlier lines name; Row 40.24's (ii) is another claim than the (iii) the earlier
   line names. If you find a claim where two lines' words differ, that claim is a STOP-and-report and gets neither line; if
   one of those lines is an earlier stretch's, do not delete it: STOP, do not commit, and report.
9. **A §10 or §11 addition follows its row's line.** The §10 entry for Row 38.11 (i) (§3.3) and each §11 addition (§3.4)
   is written only if that row's line of §3.2 is written. If the row's line is a STOP-and-report, so is its addition.

### 3.2 The lines, entry by entry, with their exact text

Each line below is given whole, as it is to be written, `<part>` filled in from the row list as the paragraph says;
where the row has no claim named, `<part>` and the space after it are dropped. Where the row list gives a label (for
example `(i), its tag-only portion:`), that label is the `<part>`.

**§L.13 — the key-areas record; every line names it.** 10 lines: 9 ruled, 1 recorded.

(a) Ruling 2 — 7 lines, form (b), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_key_areas_sitting.md, Ruling 2).* <part> **ADOPTED — proposed** — "Rows 3.1(iii), 3.4, 8.12, 8.75, 20.47(ii), 57.278 and 57.369 ADOPTED (the definition as ruled)".`
Rows: 3.1 (iii), 3.4, 8.12, 8.75, 20.47 (ii), 57.278, 57.369.
The word by form (b)'s paragraph, item (4) (the record writes a bare *"ADOPTED"* and names no L3-S number as carrying
the content; every one of the seven proposes ADOPTED — proposed, read at the staged copy). Not *as proposed* (§3.1 item
7). List all seven under *ADOPTED words read at the row*.

(b) Ruling 2 — 2 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_key_areas_sitting.md, Ruling 2).* <part> **HISTORICAL** — "Rows 3.5(i) and 3.5(ii) decided against".`
Rows: 3.5 (i), 3.5 (ii). (Row 3.5 (iii) gets no line in this stretch: §L.14 below.)

(c) §2c, not a ruling — Row 8.31 (i), 1 line, form (d):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_key_areas_sitting.md, §2c).* (i) **QUARANTINED** — "placed QUARANTINED, this side's derivation"; audit question: "does any built code hand the function layer's open marks to a grouping step, and does that step pass them unchanged?"; "one treatment with the open-mark rows placed QUARANTINED by Ruling 3 of `cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md`". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
The row is proposed ADOPTED — proposed for (i); its audit question is added to §11 (§3.4). *The joining word "audit
question:" and the order placement, audit question, ground are the writing side's; overrulable by the user.* A later
stretch writes §L.53's ruled line beneath this one (Task 3 (c) item 2).

**§L.14 — the pivot-label record. No line in this stretch.** Its one row, Row 3.5 (iii), carries a recorded placement
that names no disposition word; §L.14's table says the act writes the row's line once, from §L.52's entry, and writes no
line from this entry, as Task 3 (c) item 2 orders. List Row 3.5 (iii) under *recorded lines not written: no disposition
word* and, marked *to be written by a later stretch*, under *rows named by more than one record*.

**§L.15 — the edge-of-span record; every line names it, Ruling 1.** 9 lines, all ruled.

(d) 4 lines, form (b-H), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* <part> **HISTORICAL** — "Recorded as decided against: the outgoing texts' "the grouping layer only tags the edge and never acts on the tag" — Rows 8.64, 8.65, 54.14(ii), 54.36(i)".`
Rows: 8.64, 8.65, 54.14 (ii), 54.36 (i).

(e) 2 lines, form (b-H), for the tag-only portion of a claim, each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* <part> **HISTORICAL** — "Recorded as decided against: the outgoing texts' "the grouping layer only tags the edge and never acts on the tag" — … and the tag-only part of Rows 54.14(i) and 54.36(ii)".`
Rows: 54.14, written `(i), its tag-only portion:`; 54.36, written `(ii), its tag-only portion:`.

(f) 2 lines, form (b), for the marking portion of the same claims (the Part 1b record's Ruling 2), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* <part> **ADOPTED — carried** (L3-S40) — "their marking part agrees with L3-S40's cut mark".`
Rows: 54.14, written `(i), its marking portion:`; 54.36, written `(ii), its marking portion:`.
Not *as proposed* (both proposed UNPLACED). List both under *ADOPTED words read at the row*. *The labels at (e) and (f)
are the writing side's, from the record's "the tag-only part" and "their marking part"; "portion" is used in place of
"part" because "part" is reserved for the musical part (`CLAUDE.md`, the reserved-word convention); overrulable by the
user.*

(g) Row 7.67, 1 line, form (b) (Ruling 5 of the part 2 record):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* **ADOPTED — carried** (L3-S40) — "Row 7.67 (proposed RELOCATED to L2 only because L3's right to ask was open) may be re-marked ADOPTED — carried (L3-S40)".`
Not *as proposed* (proposed RELOCATED). List it under *ADOPTED words read at the row*. Its §10 line: §3.3.

**§L.16 — the figured-bass record; every line names it.** 11 lines: 3 ruled, 8 recorded.

(h) Ruling 1 — 3 lines, form (b) (the Part 1b record's Ruling 3), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1).* <part> **ADOPTED — carried** (L3-S28) — "Rows 4.23(i), 4.28 and 4.29 placed with the new output".`
Rows: 4.23 (i), 4.28, 4.29. Not *as proposed*. List all three under *ADOPTED words read at the row*.

(i) §2 (a), not a ruling — 4 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (a)).* **RELOCATED** to ***L0 — The notated record*** — as proposed, "Their proposals stand: the four Row 21 rows RELOCATED to L0"; "treat the composer's written symbols as input; `FRAMEWORK.md` §3.1 and IC-L1 S-8 [relayed] decide against them". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 21.139, 21.143, 21.144, 21.172. Already on §10 (§3.3). The record's *"decide against"* is a hit of Task 3 (c)
item 1, written as the entry says (no HISTORICAL line) and listed in the report.

(j) §2 (a), not a ruling — Row 41.57 (i), 1 line, form (d):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (a)).* (i) **RELOCATED** to ***the measurement of the analysis*** — as proposed, "Row 41.57(i) RELOCATED to the measurement of the analysis"; "treat the composer's written symbols as input; `FRAMEWORK.md` §3.1 and IC-L1 S-8 [relayed] decide against them". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Already on §10 (§3.3).

(k) §2 (b), not a ruling — Row 4.17, 1 line, form (d) (the Part 1b record's Ruling 5):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (b)).* The remainder of its figured-bass item: **ADOPTED — carried** (L3-S27) — "a display may still render it (L3-S27's views)"; "Row 4.17 differs only where it treats the figured bass as a formatting choice rather than a published fact; the charter places it among L3's outputs". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Not *as proposed* (proposed UNPLACED). Row 4.17's three chord-name items get no line from this record (§L.16 *Open*
point (2): their line is §L.52's). A later stretch writes §L.52's ruled lines beneath this one (Task 3 (c) item 2).

(l) §2 (c), not a ruling — 2 lines, form (d) (the Part 1b record's Ruling 4), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (c)).* <part> **ADOPTED — carried** (L3-S27) — "L3-S27's full figure, short forms a view under a named convention"; "on this side's reading of D-295 (octave reduction loses 9 against 2)". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 4.24, written `(ii), its remainder:`; 4.26, written `Its remainder:`. Not *as proposed*. A later stretch writes
§L.52's ruled lines beneath these.
List the three rows of (k) and (l) under *ADOPTED words read at the row*. *The labels at (k) and (l) are the writing
side's, from the Part 1b record's Rulings 4 and 5 ("the rest" there; "remainder" is used because "rest" is reserved for
the silence, and the big dispatch's §L.16 was amended the same way at release, finding 57); overrulable by the user.*

**§L.17 — the chord-symbol record; every line names it.** 33 lines: 2 ruled, 31 recorded.

(m) §2 (a), not a ruling — 7 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (a)).* <part> **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — as proposed, "The proposals stand (seven RELOCATED to L2, three QUARANTINED)"; "decided against by the charter's lines 489–492, with which the method stated beside the 2026-10-08 Ruling 1 agrees". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 10.14 (i), 10.24 (i), 10.131 (i), 10.149, 38.24 (ii), 43.44 (i), 47.10 (ii).

(n) §2 (a), not a ruling — 3 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (a)).* <part> **QUARANTINED** — as proposed, "The proposals stand (seven RELOCATED to L2, three QUARANTINED)"; "decided against by the charter's lines 489–492, with which the method stated beside the 2026-10-08 Ruling 1 agrees". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 1.15, 1.18, 21.188 (ii).
The record's *"decided against"* at (m) and (n) is a hit of Task 3 (c) item 1, written as the entry says (form (d), no
HISTORICAL line; the big dispatch's §L.17 *Open* point (1)) and listed in the report.

(o) §2 (a), not a ruling — Row 38.11 (i), 1 line, form (d):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (a)).* (i) **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "proposed placed as Row 10.14(i) is — RELOCATED to L2"; "the chord that layer decided being L2's chord". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Proposed UNPLACED; appended to §10 (§3.3). A later stretch writes §L.52's ruled line beneath this one.

(p) §2 (b), not a ruling — 6 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (b)).* <part> **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — as proposed, "RELOCATED to L2 as proposed"; "the degree is L2's decided field". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 7.19, 7.51, 7.90, 7.220, 10.25 (ii), 38.12 (i).

(q) Ruling 1, its documentation — 2 lines, form (b), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, Ruling 1).* <part> **QUARANTINED** — as proposed; "Rows 22.84(ii) and 22.86 stay QUARANTINED.".`
Rows: 22.84 (ii), 22.86.

(r) §2 (c), not a ruling — 3 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (c)).* <part> **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — as proposed, "proposals stand"; "each augmented sixth is its own L2 chord kind (chord-vocabulary Ruling 1)". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 7.18 (i), 7.185, 48.16.

(s) §2 (c), not a ruling — Row 15.23 (iii), 1 line, form (d):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (c)).* (iii) **QUARANTINED** — as proposed, "proposals stand"; "each augmented sixth is its own L2 chord kind (chord-vocabulary Ruling 1)". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`

(t) §2 (c), not a ruling — Row 10.34, 1 line, form (d) (the Part 1b record's Ruling 7):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (c)).* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — "Row 10.34's minor-major seventh is proposed for OQ-L2-1's closure measurement, not in the vocabulary now." Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Not *as proposed*. The record's one sentence fills both the placement and the ground: the Part 1b record's Ruling 7 says
how it fills them *"is a matter of writing at release and does not change the word"*; *this writing is the writing
side's, overrulable by the user.* Already on §10 (§3.3).

(u) §2 (d), not a ruling — 6 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (d)).* <part> **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — as proposed, "RELOCATED to L2 as proposed"; "chord-vocabulary Ruling 2". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 10.35, 10.36, 10.82, 10.101, 10.132 (i), 19.84.

(v) §2 (e), not a ruling — 2 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (e)).* <part> **QUARANTINED** — as proposed, "Rows 15.43(ii) and 15.50(ii) stay QUARANTINED"; "L3 publishes the quality, the bass and a named reason in place of the root; a dominant-seventh respelling would assert a chord L2 did not decide, so it is a display's own act". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 15.43 (ii), 15.50 (ii).

(w) §2 (f), not a ruling — Row 2.6, 1 line, form (d):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (f)).* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** — as proposed, "RELOCATED to L2 as proposed"; "the charter's line 478". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`

**Row 22.83: no line** (named at the record's §0 only; §L.17's check sum).
*In every line of (i), (j), (m), (n), (p) and (r) to (w) the form "as proposed, <the record's placement words>; <its
ground>" is the writing side's way of filling form (d)'s two slots, so that the record's own "as proposed" words stand
in the line; overrulable by the user.*

**§L.18 — the harmonic-rhythm record; every line names it.** 13 lines, all recorded.

(x) §2 (a), not a ruling — 6 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (a)).* <part> **QUARANTINED** — as proposed, "QUARANTINED with their audit questions, as proposed"; "Descriptions of the old code"; its L2 twin: "<twin>". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows, each with its `<twin>`, the record's words for it, by the record's order:

| Row | `<twin>` |
|---|---|
| 5.3 (i) | `Row 23.314 (recorded as derivation, challengeable)` |
| 6.4 (i) | `30.16(i) (ruled, adjacent spans Ruling 1)` |
| 6.6 | `30.19 (proposed only)` |
| 18.4 (i) | `20.4 (named in the any-boundary-set Ruling 1's placement of Row 30.16(ii), as the reading file records it [relayed — that record not read])` |
| 22.21 | `24.52 (ruled)` |
| 28.58 | `30.81 (proposed only)` |

*The pairing of each row with its twin by the order of the two lists is the writing side's reading of the record's
"Their L2 twins: …"; overrulable by the user.*

(y) §2 (b), not a ruling — 3 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (b)).* **QUARANTINED** — "corrected to QUARANTINED, travelling with L2's Row 23.72, with that row's audit question (*"which fields make two regions' readings the same on each path at the current commit, and which path merges adjacent regions by them?"*)"; "since L2 placed the same three sentences (Rows 23.72 to 23.74) so by the adjacent-spans Ruling 1". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 21.27, 21.28, 21.29. Proposed RELOCATED; their audit question is added to §11 (§3.4). Their §10 entry stands
untouched (§3.3). A later stretch writes §L.53's ruled lines beneath these.

(z) §2 (c), not a ruling — Row 22.9, 1 line, form (d):
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (c)).* **HISTORICAL** — "corrected to HISTORICAL — a plan"; "as its twin Row 24.34 was ruled". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Its §10 entry stands untouched (§3.3). A later stretch writes §L.53's ruled line beneath this one.

(aa) §2 (d), not a ruling — 3 lines, form (d), each:
`*RECORDED DISPOSITION (cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (d)).* <part> **HISTORICAL** — "corrected to HISTORICAL — a superseded plan"; "as their twins Rows 44.33(ii), 44.50(vi) and 44.76(iii) were ruled by the nothing-from-L3 Ruling 4; the slice-duration reading of harmonic rhythm is also met by Ruling 62 item 3". Recorded by the record as this side's derivation, not ruled; challengeable at the row.`
Rows: 40.24 (ii), 40.41 (ii), 40.63 (ii). (Row 40.24 already carries the disposition-words record's line on (iii):
§3.1 item 2.) A later stretch writes §L.52's ruled lines beneath Rows 40.24 and 40.41, and §L.53's beneath Row 40.63.

**§L.18's §9 point 5:** nothing is written at §9 (Task 3 (c) item 4); list the record's sentence *"§9 point 5 is answered
by L3-S30."* (§2 (e)) under *points answered by a record's own derivation, nothing written*.

**§L.19 — the mass-and-status record; every line names it, Ruling 2.** 13 lines, all ruled (Ruling 2 ratifies §2 (a)
to (e)).

(bb) §2 (a) — 9 lines, form (b), each:
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* <part> **RELOCATED** to ***the uncertainty surface*** — as proposed; "Agrees with its twin — RELOCATED to *the uncertainty surface*, as proposed."; its L2 twin: "<pair>".`
Rows, each with its `<pair>`, the record's own token for it:

| Row | `<pair>` |
|---|---|
| 7.209 (i) | `7.209(i)↔5.218(i)` |
| 8.78 (i) | `8.78(i)↔41.92(i)` |
| 19.36 | `19.36↔21.47` |
| 19.72 | `19.72↔21.69` |
| 39.17 | `39.17↔9.22` |
| 45.6 | `45.6↔52.4` |
| 36.31 (i) | `36.31(i)↔40.28` |
| 36.32 (i) | `36.32(i)↔40.29` |
| 45.12 (i) | `45.12(i)↔52.10(i)` |

Each is already on §10 (§3.3).

(cc) §2 (b) — Row 15.16 (i), 1 line, form (b):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* (i) **QUARANTINED** — "corrected to QUARANTINED, travelling with L2's Row 17.16 and that row's audit question (*"what does the shipped slice publish for each segment, and is any published value a partial candidate score rather than a mass?"*), as its twin Row 17.18(i) was recorded".`
Proposed RELOCATED; its audit question is added to §11 (§3.4); its §10 entry stands untouched (§3.3).

(dd) §2 (c) — Row 43.7 (ii), 1 line, form (b):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* (ii) **HISTORICAL** — "corrected to HISTORICAL, on the ground of the weight-meaning Ruling 4"; "its reach to 43.7(ii) is this side's reading".`

(ee) §2 (c) — Row 45.13 (ii), 1 line, form (b):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* (ii) **HISTORICAL** — "corrected to HISTORICAL, on the ground of the weight-meaning Ruling 4"; "the reach is this side's reading".`
Their §10 entries stand untouched (§3.3).

(ff) §2 (d) — Row 8.77, 1 line, form (b):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* **HISTORICAL** — "HISTORICAL — a rule replaced by L3-S34, contingent on L3-S34's ratification."; "8.77's contingency now met".`

**Rows 36.5 (ii), 45.14 (i) and 45.15 (i): no line** (Ruling 12 of the part 2 record): not listed under *rows the act
could not place*; their §10 entries stand as they are.
**§L.19's §9 point 1:** nothing is written at §9 (Task 3 (c) item 4, as amended by Ruling 27 of the part 2 record);
list the record's §2 (g) sentence under *points answered by a record's own derivation, nothing written*.

**§L.20 — the boundaries record; every line names it, Ruling 2.** 3 lines, all ruled (Ruling 2 ratifies §2).

(gg) Row 8.42, 1 line, form (b):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2).* **HISTORICAL** — "HISTORICAL — a rule replaced by L3-S37"; "Rows 8.42 and 8.109 HISTORICAL".`

(hh) Row 8.109, 1 line, form (b), the whole row (§L.20's check remark on *Open* point (1)):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2).* **HISTORICAL** — "HISTORICAL — replaced by L3-S37 and mass-and-status Ruling 1"; "Rows 8.42 and 8.109 HISTORICAL".`
Row 8.110 gets no line.

(ii) Row 47.23 (ii), 1 line, form (b):
`*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2).* (ii) **RELOCATED** to ***L1 — Change points, candidates and notated evidence*** — as proposed; "RELOCATED to L1, as proposed — L1 publishes the slices and every change point's metric strength class (charter lines 337–343)".`
Already on §10 (§3.3).

**The count.** Ruled (`*RULED DISPOSITION (`): §L.13 7 + 2 = 9; §L.15 4 + 2 + 2 + 1 = 9; §L.16 3; §L.17 2; §L.19
9 + 1 + 1 + 1 + 1 = 13; §L.20 3 — **39**. Recorded (`*RECORDED DISPOSITION (`): §L.13 1; §L.16 4 + 1 + 1 + 2 = 8; §L.17
7 + 3 + 1 + 6 + 3 + 1 + 1 + 6 + 2 + 1 = 31; §L.18 6 + 3 + 1 + 3 = 13 — **53**. **92 in all.** None opens
`*RULED PLACEMENT (`.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6)

1. **One entry appended (item 5).** Row 38.11 (i) is placed RELOCATED out of UNPLACED, and §10 does not carry it at the
   writing side's search (every RELOCATED row-part of this stretch searched as a bare number with look-around, so that
   entries listing several rows are reached; the hit for Row 38.11 is the entry beginning
   `- Rows 38.7 (i), 38.10 (i), 38.10 (ii), 38.11 (ii), 38.11 (iii),`, which carries claims (ii) and (iii) only). Append
   it **after the last entry under `**To *L2 — The tonal reading. The one entangled decision.***`** — the entry beginning
   `- Rows 57.486 and 57.487 (i)`, whose last line ends `the L2 comparison relocated L2 Rows 53.22 and 53.28 to L3.)*` —
   and before the blank line that precedes `**To *the second axis — voice leading*.**`, as ONE line, in §10's entry form:

   `- Row 38.11 (i) — the key-independent chord symbol for each slice, a judgment of the old layer table's chord-symbol layer. *(cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (a).)*`

   *The subject clause is the writing side's, from the row's heading and its claim (i); the parenthesis names the
   record's section, as the line does; overrulable by the user.* Check at §10 by row number and claim before appending.
2. **Already on §10, nothing appended:** Rows 21.139, 21.143, 21.144 and 21.172 (the entry beginning
   `- Rows 21.139, 21.142, 21.143, 21.144 and 21.172`; the Part 13 record's Ruling 1); Row 41.57 (i) (the entry beginning
   `- Rows 41.48 (i), 41.49 (iii),`); Row 47.23 (ii) (the entry beginning `- Rows 47.6, 47.22 (i), 47.23 (ii),`); the
   §L.17 rows of (m), (p), (r), (t), (u) and (w), each proposed RELOCATED to L2 and on §10 (Row 10.34 in the entry
   beginning `- Rows 10.32, 10.33, 10.34,`); the nine rows of §3.2 (bb), under `**To *the uncertainty surface* (NOT A
   LAYER).**`. Run the same search yourself.
3. **Rows placed by this stretch with a word other than RELOCATED whose proposal was RELOCATED** — Rows 21.27, 21.28,
   21.29, 22.9 and 40.63 (ii) (§L.18), 15.16 (i), 43.7 (ii) and 45.13 (ii) (§L.19), and Row 7.67 (§L.15): **their §10
   entries are not edited and gain no line**, save Row 7.67's line of item 4 below. Task 3 (c) item 6's *LEAVES L3* lines
   are written only for the records of §L.21 to §L.24, and item 5 only appends. List these row-parts in the report under
   *§10 entries left standing for rows now placed otherwise*, a heading of this session's report only. *Authored by the
   writing side, overrulable by the user.*
4. **The Row 7.67 line (item 6).** ONE line is ADDED beneath the §10 entry beginning
   `- Rows 7.60, 7.61, 7.64, 7.65, 7.66, 7.67, 7.277 and 7.278`, after its last line (which ends
   `*(L3-S40 AGREES at Row 7.67, citing L2-S22.)*`), the entry and the other seven rows untouched, exactly as item 6 gives
   it, opening with two spaces (the indentation of the entry's second line):

   `  *Row 7.67 is not transferred (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1)* — re-marked ADOPTED — carried (L3-S40): "proposed RELOCATED to L2 only because L3's right to ask was open".`

   *Reading "at the entry's indentation" as the indentation of the entry's continuation line is the writing side's;
   overrulable by the user.* The other §10 entry that names Row 7.67 (the one ending `as at Rows 10.58 and 7.67; as
   Rows 7.66 and 10.60.)*`) names it only as a comparison and gets nothing. It is not a *LEAVES L3* line.

### 3.4 The audit questions, §11 (Task 3 (c) item 7)

1. **(a) Five entries added**, each a row-part placed QUARANTINED out of another proposal that §11 does not carry (the
   writing side's search of §11, every row number of this stretch as a bare number with look-around: none of the five
   found). Each is ONE line, in §11's entry form, its audit question as the row's line quotes it:
   - under **Member 8** (`cowork_layer6_grouping_design.md`), after the entry `- Row 8.6 (ii) — was the batch gate
     unchanged on all three presets at the build, and on which corpus and run?` and before the entry beginning
     `- Row 8.55 —`:
     `- Row 8.31 (i) — does any built code hand the function layer's open marks to a grouping step, and does that step pass them unchanged? *(cowork_rulings_2026_11_03_l3_key_areas_sitting.md, §2c.)*`
   - under **Member 15** (`ARCHITECTURE.md`, the opening block), after the entry beginning `- Row 15.15 —` (its last
     line ends `under the scoreable filter stated?`) and before the entry beginning `- Row 15.17 (i) —`:
     `- Row 15.16 (i) — what does the shipped slice publish for each segment, and is any published value a partial candidate score rather than a mass? *(cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2.)*`
   - under **Member 21** (`ARCHITECTURE.md`, *4. Existing Components*), after the entry beginning `- Row 21.26 —` (its
     last line ends `and on which arm do they run?`) and before the entry beginning `- Row 21.33 —`, three lines, in
     this order:
     `- Row 21.27 — which fields make two regions' readings the same on each path at the current commit, and which path merges adjacent regions by them? *(cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (b).)*`
     `- Row 21.28 — which fields make two regions' readings the same on each path at the current commit, and which path merges adjacent regions by them? *(cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (b).)*`
     `- Row 21.29 — which fields make two regions' readings the same on each path at the current commit, and which path merges adjacent regions by them? *(cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (b).)*`
   *Where the record is recorded and not ruled, the parenthesis names its section in place of "Ruling N", as the line
   does; one entry per row, as item 7 (a)'s form gives it; both the writing side's, overrulable by the user.* Check each
   at §11 by row number and claim before adding it. List the five under *audit questions added*.
2. **(b) Expected: no NOT QUARANTINED line.** The writing side's search met §11 entries naming claims of these rows of
   this stretch — 1.15, 1.18, 4.23, 5.3, 6.4, 6.6 (as *"Row 6.6, with Rows 6.7 and 6.8"*), 15.23, 15.43, 15.50, 18.4,
   21.188, 22.21, 22.84, 22.86, 28.58, 41.57, 43.7, 45.12 and 45.13 (Rows 1.15 and 5.3 also as mentions inside other
   rows' entries) — and each entry names either a claim this stretch places QUARANTINED or a claim this stretch does not
   place, so no entry gets a line. Run the same
   search yourself; if you find a §11 entry for a claim this stretch places with a word other than QUARANTINED, add the
   NOT QUARANTINED line item 7 (b) gives, and report it.

### 3.5 The file's own statements of its state, and the two corrected labels

1. **The four state sentences** were written by session 10 and are not touched. (They already name the RECORDED
   DISPOSITION lines this stretch writes first.)
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54 at staging) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.20 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.21 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 2 commit, as session 11's
   instruction §3.5 item 3 had it. *Authored by the writing side, overrulable by the user.* Attribute it in the diff
   table to *"session 12's instruction, §3.5 item 3"*.
4. **Two labels session 11 wrote are corrected, in place.** Session 11's instruction (§3.2 (r) and §3.3) gave the label
   *"Its rest:"* and the subject clause *"Row 7.37, its rest —"*, both authored by the writing side. *"rest"* is reserved
   for the silence (`CLAUDE.md`, the reserved-word convention: no NEW collision is introduced, and anything written for
   the user avoids the collided sense). The writing side found its own slip after session 11 ran (entry 1200 §2 item 6),
   and the correction is ordered here:
   - the line that begins `*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* Its rest: **RELOCATED**`
     (beneath Row 7.37; line 3812 at staging): `Its rest:` → `Its remainder:`, nothing else in the line changed;
   - the §10 line that begins `- Row 7.37, its rest — that the DCML conventions` (line 80403 at staging):
     `Row 7.37, its rest —` → `Row 7.37, its remainder —`, nothing else in the line changed.
   Each is found by its text (each occurs exactly once: the Grep tool must count 1 for `Its rest:` and 1 for
   `its rest —` before the edit, and 0 for each after). Their former text is not preserved in the file and stays
   recoverable at the stretch 2 commit, as for the in-progress line (#12's recoverable clause). *Authored by the writing
   side; the user was told of the judgment and has not ruled on it separately, and may overrule it, for example if he
   wants the former text kept in the file's preserved-wording shape.* Attribute both in the diff table to *"session 12's
   instruction, §3.5 item 4"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.13 to
   §L.20 only, in ledger order**, after sessions 10 and 11's §L.1 to §L.12. §L.21 to §L.55 are not applied, read or
   touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1200 and 1201 ARE landed**, with this file, in §5 act 1, as sessions 8 to 11 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the eight records §L.13 to §L.20
   enter only — the seven of §2 item 7 that you read whole, and the pivot-label record by the Grep tool. The writing
   side's search (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case not matched)
   found nine hits: the key-areas record's line 90 (Rows 3.5 (i) and (ii), §3.2 (b); and D-472 on the same and the next
   line, no row) and line 115 (its check correction (6), D-472, no row); the pivot-label record's lines 83 and 86 (Row 3.5
   (iii)'s wobble-suppression, which §L.14 places with no word: no line in this stretch); the edge-of-span record's line
   76 (§3.2 (d) and (e)) and line 91 (its check correction (5), *"the six differing rows decided against" narrowed*, no
   row of its own); the figured-bass record's line 55 (*"decide against"*, §3.2 (i) and (j), form (d), no HISTORICAL
   line); the chord-symbol record's line 65 (§3.2 (m) and (n), form (d), no HISTORICAL line) and line 106 (its check
   correction (10), *"decides against all of them"* bounded, no row of its own); none in the harmonic-rhythm,
   mass-and-status or boundaries records. Nothing is written from a hit without a row. List each hit you find in the
   report. Item 2: reached by Row 3.5 (iii) only (§3.2, §L.14). Item 3: not reached. Item 4: §3.2's §9 remarks at §L.18
   and §L.19. Item 5: §3.3 items 1 and 2. Item 6: §3.3 item 4 (Row 7.67) only. Item 7: §3.4.
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed lines, not in the big dispatch: the in-progress line of §3.5 item 3 and the two labels of §3.5 item 4.**
   Task 3 (f) admits them for this stretch as changed passages of their own kind. Their former texts are the three
   deleted lines this stretch's diff against the stretch 2 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, write the
   in-progress line naming the last entry actually applied instead of §L.20 (and the next one instead of §L.21), commit
   the entries already applied, and report which. If you are inside an entry, do not commit; STOP and report which
   entries were applied to the uncommitted copy and that it is not landed. Make the two corrections of §3.5 item 4
   before the first line of §3.2.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 2 commit:**
     `git diff 402ed789f5caba5de5ca64798b7ecf3d9c599212 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session12_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line before it; the §10 entry of §3.3 item 1; the Row 7.67 line of §3.3 item 4; an §11 entry
     of §3.4 item 1; a NOT QUARANTINED line only if §3.4 item 2 found one; the in-progress line of §3.5 item 3; the two
     corrected labels of §3.5 item 4. Then
     `git diff --numstat 402ed789f5caba5de5ca64798b7ecf3d9c599212 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 3 deleted lines** and **2 × N + 10 added lines**, N being the number of lines of §3.2 you wrote
     (92 less the STOP-and-reports; **194 added** if none), less 1 for each §10 or §11 addition not written under §3.1
     item 9, plus 1 for each NOT QUARANTINED line §3.4 item 2 adds, if any. *The writing side's arithmetic for the 10: 1
     §10 entry, 1 Row 7.67 line, 5 §11 entries, the in-progress line and the two corrected labels (each a replaced line:
     one added, one deleted).*
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 4 deleted lines** (the four lines session 10's state sentences were written into) and **447 +
     2 × N added lines** (**631** if none), with the same two adjustments as above. *The writing side's arithmetic:
     session 11's report gives 440 added and 4 deleted against the Task 2 commit; this stretch adds 2 × N lines, 1 §10
     entry, 1 Row 7.67 line and 5 §11 entries. The in-progress line and the two corrected labels replace lines that are
     themselves additions against the Task 2 commit, so they add no line and delete none there. (Entry 1200 §3 step 1
     wrote "deleted 4 + 2" against the Task 2 commit; that was a slip of the writing side, corrected here: the two lines
     did not exist at the Task 2 commit.)*
   - Then, with the Grep tool in count mode: `\*RULED DISPOSITION \(` must count **212 + 39 = 251**, less the number of
     §3.2's RULED DISPOSITION lines you listed as STOP-and-report; `\*RECORDED DISPOSITION \(` must count **53**, less
     those of §3.2's RECORDED DISPOSITION lines listed as STOP-and-report; `\*RULED PLACEMENT \(` must count **3**;
     `Its rest:` and `its rest —` must each count **0**.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 3 (§L.13 to §L.20): the rows placed by ledger entries thirteen to twenty re-marked in the reading file, the first recorded lines among them, one transfer-list entry, the Row 7.67 line and five audit questions added, two labels of stretch 2 corrected and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_12_task_3_stretch_3_2026_11_23.md`**, as sessions 2 to 11
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.21, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own.** Exactly three paths, all expected
   UNTRACKED: this file, `records/cc/instructions/cc_instruction_l3_application_session_12_task_3_stretch_3_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_one.md`. Run §1 check 2 again immediately
   before staging. Subject exactly:
   `record: handoff entries 1200 and 1201 and the session 12 instruction of the L3 application landed; Task 3 stretch 3 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for §L.13 to §L.20**, as the big dispatch's Task 3 and §3 and §4 above give it: first the two corrections of
   §3.5 item 4; then the lines of §3.2 entry by entry, with §3.3's additions at §L.15 and §L.17 and §3.4's at §L.13,
   §L.18 and §L.19; then §3.4 item 2's search; then §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_12_task_3_stretch_3_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 12 of the L3 application, Task 3 stretch 3 (§L.13 to §L.20) written; stretch 4 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.13 to §L.20, in order: every line by row and claim, written (with its reading-file line number after the
   edit) or STOP-and-report (and why). The same for §3.3's additions, §3.4's additions and search, and §3.5 item 4's two
   corrections.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place*; *rows given no line now*
   (none expected from this stretch); *recorded lines not written: no disposition word* (Row 3.5 (iii), §L.14); *rows
   named by more than one record* — Row 3.1 (the earlier stretches' lines on (i) and (ii), this stretch's on (iii)), Row
   40.24 (the earlier line on (iii), this stretch's on (ii)), Row 3.5 ((i) and (ii) here; (iii) at §L.14 and §L.52), and,
   marked *to be written by a later stretch*, the row numbers of this stretch the writing side's bare-number search met
   in §L.21 to §L.55, not read for claim: 3.1 (§L.29 to §L.33, §L.36, §L.38, §L.44, §L.52), 3.4 (§L.30 to §L.33, §L.36,
   §L.38), 3.5 (§L.23, §L.31 to §L.33, §L.52), 8.12 (§L.25), 8.31 (§L.25, §L.53), 4.17, 4.24, 4.26, 10.14 and 38.11
   (§L.52), 2.6 (§L.21 to §L.23), 21.27, 21.28, 21.29 and 22.9 (§L.53), 40.24 (§L.52, §L.55), 40.41 (§L.52), 40.63 (§L.52,
   §L.53), 7.209 (§L.21), 8.42 (§L.51), 8.109 (§L.23) — some hits for 3.1 and 3.4 may be section numbers, not rows;
   *ADOPTED words read at the row* (Rows 3.1 (iii), 3.4, 8.12, 8.75, 20.47 (ii), 57.278, 57.369; 54.14 (i) and 54.36 (ii),
   their marking portion; 7.67; 4.23 (i), 4.28, 4.29; 4.17, 4.24 (ii), 4.26); *audit questions added* (§3.4); *audit
   questions no longer quarantined* (none expected); *points answered by a record's own derivation, nothing written* (§9
   point 5, the harmonic-rhythm record's §2 (e); §9 point 1, the mass-and-status record's §2 (g)); the decided-against
   hits (§4 item 4).
5. The diff table of §4 item 8, every changed passage attributed, and the four counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: Row 3.5 (iii) (§L.14); Row 22.83 (§L.17);
   Rows 36.5 (ii), 45.14 (i) and 45.15 (i) (§L.19, Ruling 12 of the part 2 record); Row 8.110 (§L.20); Row 4.17's three
   chord-name items (§L.16); and the rows the §L entries of this stretch list as mentioned and not placed by their record
   (§L.13: 3.5 (iii), 8.76, 3.6; §L.14: its §4's rows and the three naming `detectPivotChords`; §L.15: 8.63, 36.27 and the
   40 AGREES row-parts; §L.16: the 28 AGREES row-parts and the pedal-point rows; §L.17: the 47 AGREES row-parts, Rows
   42.10, 42.12, 57.372, 21.77 and the twelve L2 rows of its check correction (8); §L.18: the 3 AGREES row-parts; §L.19:
   the 39 AGREES rows; §L.20: the 26 AGREES row-parts and Row 22.84 (i)). *A heading of this session's report only, as in
   sessions 10 and 11's.*
7. *§10 entries left standing for rows now placed otherwise* (§3.3 item 3).
8. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
9. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
10. The last sentence, exactly: *"Session 12 of the L3 application ends here. Stretch 4 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (a row-part that
  is STOP-and-report under them, or under §3.1 items 5 to 9, is reported and the remaining ones applied, as they say);
- a line an earlier stretch wrote would have to be deleted or edited, other than the two labels of §3.5 item 4 (§3.1
  item 8);
- §3.5 item 4's text is not found exactly once before the edit;
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1200. Read at the objects for this file: the
three git reference files (both refs `760c3cfb…`); entries 1200, 1199 and 1026 whole; session 11's instruction whole;
session 11's report by search (its untracked-path list and its two `--numstat` results); the seven records §L.13 and
§L.15 to §L.20 enter, by sections (the key-areas and edge-of-span records whole; the figured-bass record from its §2 to
the end; the chord-symbol record's §2 and its Ruling 1 documentation by search; the harmonic-rhythm, mass-and-status and
boundaries records at their §2 and the rulings' row sentences by search); the pivot-label record at its §2b; the Part 1b
record's Rulings 2 to 7; the big dispatch at lines 200–260, 1329–2251, 5514–5734 (§L.52 and §L.53's table lines) and
6616–6820, its `### §L.` headings and *Check sum* lines, and a bare-number search of lines 2252–5906 for this stretch's
rows; the reading file, by read-only scripts over the staged copy: each of the 87 rows' heading (once in §6),
`*PROPOSED DISPOSITION.*` paragraph and any existing `*RULED …` line, §10 and §11 searched for this stretch's row numbers
as bare numbers with look-around, each hit read, every RELOCATED row-part of §3.2 found on §10 by row and claim
(Row 38.11 (i) alone not found), the insertion places read, and the two lines of §3.5 item 4. The Part 13 record was not
read: §3.3 item 2's statement for its five rows rests on §10 read directly and on §L.16's transcription. Every
quotation of §3.2 checked against its record by a read-only script (words and punctuation, line breaks read as spaces,
asterisks not compared): all found. Computed as git would on the staged copies: the big dispatch's blob `b5274c2c…` and
the reading file's `34386416…` (counts 212 / 3 / 0). Relayed, not re-checked here: the archive JSON's blob `1df4f207…`
and the 393 untracked paths (from session 11's report), the end of `cowork_handoff.md`'s topmost block at line 255 and
the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol section (as session 11's instruction relays them),
and session 11's 440 added and 4 deleted lines against the Task 2 commit. Every label this file authors was checked
against `CLAUDE.md`'s list of collided words before landing. Checked for coherence, completeness, correctness and
overstated words as a turn of its own by the same sitting before landing: every line of §3.2 rebuilt by script from the
checked data and compared with the text here (all equal); the rows with more than one line, the *as proposed* list, the
counts, the arithmetic, the side-record line ranges and the hit list re-read at their objects. Two corrections were
made in place then, no former wording kept, the file never having landed: §3.4 item 2's list of §11 entries, which
named single claims where §11 carries several; and this provenance, which now says the Part 13 record was not read and
that the RELOCATED rows were found on §10 one by one. The user's words: the opening instruction; "shortened";
"continue" (the check).*
