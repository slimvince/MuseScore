# CC dispatch — the L3 application, SESSION 6 of several: Task 1 of the L3 application dispatch, fifth stretch (§L.41 to §L.48), and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_seven.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Sessions 2 to 5 applied Task 1 for §L.1 to §L.15,
§L.16 to §L.25, §L.26 to §L.33 and §L.34 to §L.40. Session 5's commits are `fc2e099aa79cef0131789e6bffdb78654abdc79b`
(the writing side's two files), `9c26668a8885cdc1f56123624beed4e0b2413f13` (the successor, blob
`a76ffaec74802d82d827cbffeb80930ab3d86687`) and `93d2fad4f8406dee8975d545523ae8e5fd5f2766` (its report), all verified at
the objects by the Cowork sitting that wrote this file.

**This is session 6. It continues the big dispatch's Task 1 (the successor file
`cowork_derived_specification_l3_2026_11_08.md`) for the ledger entries §L.41 to §L.48 only, commits and pushes that
fifth stretch, writes its report, and STOPS.** Of these eight entries, four order text in the successor: §L.41 lists for
the notes; §L.42 one added statement and one row for the notes; §L.43 one list for the notes; §L.48 one added statement.
§L.44 to §L.47 each state that the successor gets no text; for them Task 1 writes nothing, and their records are read so
that this is confirmed at the record. Each later stretch gets its own instruction, sized and written after the previous
one is verified.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §3,
and only for this session. Where this file and the big dispatch seem to differ on anything §3 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change is decided by this session.** This session writes the successor file by the
big dispatch's Task 1, which places the ruling records' own words; it decides nothing. (§L.42's record states an
algorithmic change the user already ruled on 2026-11-07; this session only places that record's words.)

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `93d2fad4f8406dee8975d545523ae8e5fd5f2766`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_6_task_1_stretch_5_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The successor stands as session 5 committed it** (replaces the big dispatch's Task 1 *Before the edit* for this
   session). `git hash-object cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"` must print
   `a76ffaec74802d82d827cbffeb80930ab3d86687`, and
   `git ls-tree 93d2fad4f8406dee8975d545523ae8e5fd5f2766 -- cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"`
   must show the same blob. Anything else: STOP and report.
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 93d2fad4f8406dee8975d545523ae8e5fd5f2766 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the two files §4 item 1 lands (this instruction and handoff entry 1188), plus the
     393 untracked paths sessions 2 to 5 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). `.claude/` and
     `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is expected and
     not a STOP. List in the report every untracked path the tool reports outside those. A further untracked
     `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a STOP (the
     big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **The eight ruling records §L.41 to §L.48 name, each WHOLE, in §L's order:**
   - §L.41 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md`
   - §L.42 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md`
   - §L.43 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md`
   - §L.44 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md`
   - §L.45 `records/cowork/rulings/cowork_rulings_2026_11_08_l3_language_model_family_sitting.md`
   - §L.46 `records/cowork/rulings/cowork_rulings_2026_11_08_l3_phrase_end_evidence_family_sitting.md`
   - §L.47 `records/cowork/rulings/cowork_rulings_2026_11_08_l3_prolongational_reduction_group_sitting.md`
   - §L.48 `records/cowork/rulings/cowork_rulings_2026_11_08_l3_chord_span_pair_group_sitting.md`

   They are the authority for every amendment this session applies: **the record's own words govern** (the big
   dispatch, §L's opening). Do NOT read the records of §L.1 to §L.40 or of §L.49 to §L.55. No surface is read: every
   text this stretch writes is a record's own. **Do not read**
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes): the
   answers it gives that bear on this stretch are quoted in the ledger entries' *Open* points, and none of them orders
   successor text.
3. **The successor WHOLE, at the git object of session 5's Task 1 commit:**
   `git show 9c26668a8885cdc1f56123624beed4e0b2413f13:cowork_derived_specification_l3_2026_11_08.md`, written to a
   scratch path outside the repository and read there with the Read tool in ranges. It is 215,712 bytes, 2,065 lines,
   and has no line longer than 1,205 characters. The derivation is not read.
4. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
5. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard
   (its condition in `CLAUDE.md` is not met).
6. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_eight.md` (the current entry point,
   written by the sitting that wrote this file; untracked, §4 item 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_seven.md` (the one before it).
7. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
8. **`decisions/group_K.md`, D-674 whole** (from its heading `### D-674` to the next `###` heading): the filing
   convention Task 1 applies.
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (a) is the form every amendment is written in, and
     its last bullet is the form of the notes lists**, the premise ledger, the declared start state, the standing bars,
     the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 4351–5209 (§L.41 to §L.48, your stretch)**;
   - lines 6100–6571 (Task 1, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–4350 (§L.1 to §L.40, already applied); lines 5210–6099
   (§L.49 to §L.55, and Task 0); lines 6572–7110 (Tasks 2 to 5); lines 7136 to the end. Nor the derivation, the reading
   file, `FRAMEWORK.md`, `cowork_derived_specification_l0_l1_2026_09_03.md`, `tools/audit/gen_status_batch_bound.py`
   or `records/cowork/handoff/cowork_away_returns.md`: each belongs to a later Task's session or is not needed here.
   When you search the big dispatch, search only inside the ranges above.

## 3. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 1 applies** (Task 1 (a): *"Each §L entry's Successor — amendments part is applied, in
   ledger order"*) → **§L.41 to §L.48 only, in ledger order.** §L.1 to §L.40 are applied already and are not touched;
   §L.49 to §L.55 are not applied, read or touched. **For §L.44 to §L.47**, the ledger entry states that the successor
   gets no statement, no amendment and no list for the notes: confirm that against each record read whole and write
   nothing for it. If a record of §L.44 to §L.47 orders text in the successor after all, STOP and report for that entry;
   apply the rest. The charter, interface-contract, reading-file and register parts of every entry in this stretch
   belong to Tasks 2 to 4 and are not touched.
3. **Task 1 (c), split by stretch.** Apply here only the parts whose ordering record is one of §L.41 to §L.48:
   - (c) items 1, 2 and 4: applied by earlier sessions; nothing here.
   - **(c) item 3, the added statements: §L.42's one and §L.48's one.**
     - **§L.42's statement** (its *Successor — amendments* item 1), under **(c) item 3 (i)**: the record gives it as an
       *"As ruled."* paragraph (the §L.42 record, lines 33–36), and the ledger's check note (big dispatch §L.42, *Open*
       point (2)'s check) says that paragraph, quoted whole, is the statement's text.
       - **Heading** (form (a)), the record naming no part:
         `### Added — records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md, Ruling 1`
       - **Lead-in**, in the shape the successor's first added statement (the key-areas record's, line 1500 of blob
         `a76ffaec…`) uses for an *"As ruled"* text:
         `*Ruling 1, as ruled:*`
       - **The quotation**, one line: the record's lines 33–36 joined with single spaces, without the record's leading
         `**As ruled.**` label (as the successor's key-areas statement quotes that record's *"As ruled:"* texts without
         their label):
         `> For each key area of L2's principal reading (a key area as the key-areas Ruling 2 defines it), L3 publishes D-276's counts: for each scale degree 1..7, the sounding duration and onset count of every chromatic inflection of that degree observed in the key area, computed from L1's published note facts relative to L2's tonic and mode, un-rounded, with their establishment status. No mode label is published (D-276).`
         No sub-item beneath it.
       - **Place:** in the section `## Statements added by the L3 family rulings`, after §L.39's statement (the line
         beginning `> A chord-suggestion tool, if one is built`, line 2025 of blob `a76ffaec…`) and before the `---`
         that closes the section (line 2027 of that blob), separated by one blank line on each side as the other added
         statements are.
     - **§L.48's statement** (its *Successor — amendments* item 1), under **(c) item 3 (i)**: the record quotes its text
       whole (the §L.48 record, lines 34–36).
       - **Heading**, exactly as the ledger gives it (§L.48 amendment 1):
         `### Added — records/cowork/rulings/cowork_rulings_2026_11_08_l3_chord_span_pair_group_sitting.md, Ruling 1, the relation of harmonic spans and phrase units (beside span-kinds part C)`
       - **Lead-in:** `*Ruling 1, as the record quotes it:*`
       - **The quotation**, one line, the record's sentence quoted whole without the record's quotation marks (as session
         4 wrote §L.27 part E and §L.28 without them):
         `> Harmonic spans and phrase units cut across each other: a phrase end may fall inside a harmonic span of L2's reading, and a harmonic span may end inside a phrase unit.`
         No sub-item beneath it.
       - **Place:** directly after the statement added for span-kinds part C (§L.26 amendment 1 and §L.48 amendment 1
         both say so): after that statement's *In short* sub-item (its two lines begin
         `- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1):*` and
         `  > **C (2 row-parts: 38.83 (ii), 57.354) — ADOPTED.**`, lines 1817–1818 of blob `a76ffaec…`) and its following
         blank line, and before the heading
         `### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part A`
         (line 1820 of that blob), followed by one blank line.
   - **The notes section — four more blocks**, in ledger order, each under its record's name (form (a), last bullet).
     **Place:** inside the existing section `## Notes — lists the records place here, not ruled`, after §L.40's list
     (its last line ends `without adding them to the specification itself.`, line 2059 of blob `a76ffaec…`) and its
     following blank line, and before the `---` that closes the notes section (line 2061 of that blob). Each block is
     followed by one blank line. Every quoted record line is written as `> ` followed by the line exactly as the record
     has it.
     1. **§L.41's Ruling 1 list** (its *Successor* (2) (i)):
        - the heading `### records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md, Ruling 1`, a blank line;
        - the lead-in `*The list and the record's own words for it, as the record gives them (its lines 38–44):*`, a blank line;
        - the record's lines 38–44 (they begin `**Rows 21.157** (*"the planned orchestration layer` and end
          `specification itself.`), a blank line.
     2. **§L.41's Ruling 2 lists** (its *Successor* (2) (ii) and (iii)):
        - the heading `### records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md, Ruling 2`, a blank line;
        - the lead-in `*§2A's list and the record's own words for it, as the record gives them (its lines 55–60):*`, a blank line;
        - the record's lines 55–60 (they begin `- **§2A — outside every charter, carried for the application's own
          specification` and end `and the display lists.`), a blank line;
        - the lead-in `*§2B's two rows, which the record adds to the display-family record's list above, as the record gives them (its lines 61–62):*`, a blank line;
        - the record's lines 61–62 (they begin `- **§2B — added to the display list` and end
          `chord-symbol formatter's code).`), a blank line.
     3. **§L.42's row for the display list** (its *Successor — amendments* item 2):
        - the heading `### records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md, Ruling 1`, a blank line;
        - the lead-in `*The row the record adds to the display-family record's list above, and its words, as the record gives them (its lines 48–50):*`, a blank line;
        - the record's lines 48–50 (they begin `- **Outside every charter, carried for a display's own specification (1):**`
          and end `listed with the display list in the amended L3 specification's notes.`), a blank line.
     4. **§L.43's list** (its *Successor* (2)):
        - the heading `### records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md, Ruling 1`, a blank line;
        - the lead-in `*The list and the record's own words for it, as the record gives them (its lines 43–50):*`, a blank line;
        - the record's lines 43–50 (they begin `- **2C — outside every charter, carried for the framework (9):**` and end
          `without adding them to the specification itself.`), a blank line.

     Then the existing `---` and the `## 5.` heading follow unchanged.

     *Why the writing side chose these shapes (each overrulable by the user):* **whole passages.** Where a record gives
     a list's rows and its "not a ruled act" words in one paragraph or bullet, that passage is quoted whole, so both are
     carried as form (a) requires and nothing is added. Session 5 did the same for §L.40. So §L.41's Ruling 1 list is
     its record's whole paragraph, lines 38–44, although the ledger cites lines 42–44 for the words, and §L.43's list is
     its record's whole 2C bullet. **The additions to the display list.** §L.41's §2B and §L.42's one row are written
     under their own records' headings, not inside §L.40's block. Form (a) puts each list *"under its record's name"*,
     and §L.40's block is the display-family record's own quotation, which session 5 wrote and which stays
     byte-identical. Each lead-in says that the rows are added to that list. *The four list headings* (`### <record file>, Ruling N`) follow the
     shape session 5 used. If a record's line numbers given here do not hold at the record (a line range starting or
     ending somewhere other than the words named), STOP and report for that block; apply the rest.
   - (c) item 5: unchanged; none of §L.41 to §L.48 orders text at OQ-L3-1 or OQ-L3-11 to OQ-L3-14 (if one does, (c)
     item 5 says what follows). (c) item 6: unchanged, for this stretch's entries.
   If you find that a part assigned to this session depends on the words of a record outside §L.41 to §L.48, or a part
   not assigned here is ordered by a record inside it: STOP and report for that part; apply the rest.
4. **Task 1 (a) and (b) are not re-applied.** The file exists (§1 check 4); it is edited in place by targeted edits only,
   never re-typed and never re-made from the derivation. Two lines written by earlier sessions are looked at:
   - **The banner's ANSWERED set**, the parenthesis in the sentence *"The open questions of §4 stand with their ANSWERED
     marks where a ruling answered them (…)"*, is re-taken at the file after this stretch's edits. The writing side's
     expectation: **unchanged — OQ-L3-2, OQ-L3-3, OQ-L3-4, OQ-L3-5, OQ-L3-6, OQ-L3-7, OQ-L3-8 and OQ-L3-10, eight**, as
     no entry of this stretch answers an open question. If the file then carries a different set, write that set and
     report the difference. Nothing else in the banner is touched.
   - **The in-progress line beneath the banner** (line 19) becomes exactly:

     `*Application in progress: this file carries the amendments of §L.1 to §L.48 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.49 to §L.55 are applied by later Claude Code sessions, one stretch each (was: "§L.16 to §L.55"; staleness fix shown, records/cc/instructions/cc_instruction_l3_application_session_4_task_1_stretch_3_2026_11_22.md, §3 item 4); the banner above is true of the file only when the last of them removes this line.*`

     Two ranges change, both the ordinary advance: `§L.1 to §L.40` becomes `§L.1 to §L.48`, and `§L.41 to §L.55`
     becomes `§L.49 to §L.55`. The parenthesis session 4 wrote stays as it is. Attribute the change in the diff table to
     *"session 6's instruction, §3 item 4"*.
5. **Task 1 (d), one commit for the whole of Task 1** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, commit the
   entries already applied, write in the in-progress line the last entry actually applied instead of §L.48 (and the
   entry after it instead of §L.49), set the banner's ANSWERED set to what the file carries, and report which entries
   were applied. If you are inside an entry, do not commit; STOP and report which entries were applied to the
   uncommitted file and that it is not landed.
6. **Task 1 (e), the check before the commit,** is run with these changes for this stretch:
   - **The method:** store the edited successor with `git hash-object -w cowork_derived_specification_l3_2026_11_08.md`
     and diff the two blobs, `git diff -U0 a76ffaec74802d82d827cbffeb80930ab3d86687 <the new blob>`, written to a
     scratch file outside the repository and read with the file tools. The base is session 5's successor, not the
     derivation object.
   - **The attributions available:** only §L.42 amendment 1 (its statement, (c) item 3 (i)), §L.48 amendment 1 (its
     statement, (c) item 3 (i)), §L.41 *Successor* (2) (i), (ii) and (iii), §L.42 amendment 2 and §L.43 *Successor* (2)
     (the notes blocks, form (a) last bullet), and §3 item 4's in-progress line (and the banner, only if the ANSWERED set
     differed). A changed passage none of those accounts for is a STOP-and-report and the file is not committed until it
     is removed.
   - **Lines removed or replaced:** none, except the in-progress line (and the banner line, only as above). Everything
     else is added lines, in three places only: §L.48's statement after span-kinds part C's statement; §L.42's statement
     after §L.39's; and the four notes blocks after §L.40's list.
   - **Bold text:** no derived statement's bold text changes in this stretch. Bold inside the new quotations is the
     records' own and is checked as part of the quotation.
   - **Every statement, open question and passage that earlier sessions wrote is byte-identical to blob `a76ffaec…`**,
     except the line(s) of §3 item 4. L3-S1 to L3-S42 and OQ-L3-1 to OQ-L3-14 are each present exactly once.
   - **Each quotation is checked at its source:** §L.42's statement equals the §L.42 record's lines 33–36 with the
     leading `**As ruled.**` label set aside and whitespace normalized; §L.48's statement occurs in the §L.48 record's
     lines 34–36, whitespace normalized and the record's quotation and italic marks set aside; each notes block, with its
     `> ` prefixes removed, equals its record's lines line for line (§L.41 lines 38–44, 55–60 and 61–62; §L.42 lines
     48–50; §L.43 lines 43–50).
   - **Headings:** count only lines that begin with `#`. Blob `a76ffaec…` has 35; the new blob must have 41 — the two
     new `### Added` headings and the four new list headings, and no other. Quoted headings inside `> ` lines are not
     headings of the successor.

   The commit subject is exactly:

   `application L3, Task 1 stretch 5 (§L.41 to §L.48): the derived specification as amended by eight more L3 family ruling records, every amendment citing its record, not ratified`

   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
7. **E1** is checked for this stretch only, as items 3 to 6 restrict it. The full E1 belongs to the session of the last
   stretch.
8. **Where the batch ends for this session.** After §4's acts, this session STOPS. It does not begin §L.49, Task 2 or
   any later Task.

## 4. The acts, in order

1. **Land the writing side's two files first, in a commit of their own.** Exactly two paths, both expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_6_task_1_stretch_5_2026_11_22.md`, and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_eight.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entry 1188 and the session 6 instruction of the L3 application landed; Task 1 stretch 5 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 1 for §L.41 to §L.48**, as the big dispatch's Task 1 and §3 above give it, ending with §3 item 6's check, its
   commit and its push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_6_task_1_stretch_5_2026_11_22.md` with the
   items of §5. Commit that ONE path alone, subject exactly:
   `report: session 6 of the L3 application, Task 1 stretch 5 (§L.41 to §L.48) written; stretch 6 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 5. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.41 to §L.48, in order: every successor amendment and list by its number, applied (and where), or
   STOP-and-report (and why); for §L.44 to §L.47, that the record was read whole and orders no successor text (or the
   STOP). The same for §3 item 4.
4. The ANSWERED set the file carries, set against §3 item 4's eight.
5. The diff table of §3 item 6, every changed passage attributed, with the line numbers of each part in the new blob.
6. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
7. The last sentence, exactly: *"Session 6 of the L3 application ends here. Stretch 6 of Task 1 is not begun. Nothing else was done."*

## 6. What the earlier sessions established, for the record (relayed here; verified by the Cowork sittings at the objects)

Session 1 committed Task 0 as `cbde76fd78a244540df64895191a511df186cc29` and stopped at Task 0's guard-set check: two
tools failing beyond the thirteen of the declared start state, item 2 (`gen_evidence_pin_membership.py`, which counts
the ruling records on disk, and `gen_per_session_reading.py`, which finds handoff entries through git). Session 2 applied
§L.1 to §L.15 and held one amendment as STOP-and-report, §L.15 amendment 4, as that entry's own settled note orders.
Sessions 3, 4 and 5 applied §L.16 to §L.25, §L.26 to §L.33 and §L.34 to §L.40 with no STOP. **This session runs no
guard**, so neither red bears on its acts; both are declared here so that no later reader takes them for this session's
doing.

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 4);
- the big dispatch's Task 1, its forms, its standing bars or its findings rule makes something a STOP (an amendment
  that is STOP-and-report under them is reported and the rest applied, as they say);
- §3 item 6's check finds a changed passage it cannot attribute;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §3 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1187. Read at the objects for this file: the
three git reference files; the commits `fc2e099a…`, `9c26668a…` and `93d2fad4…` and their trees against their parents',
folder by folder; the successor at blobs `b77ee330…` and `a76ffaec…` (their diff, the inserted parts against the §L.39
and §L.40 records, the counts, the ANSWERED set, the section layout, the line count and longest line); session 5's
instruction and report whole; the big dispatch (blob computed from the staged bytes) at its §L headings, the *Successor*
and *Open* lines of §L.41 to §L.55, §L.41 to §L.43 whole (lines 4351–4673), §L.48 at lines 5104–5135 and 5164–5209,
form (a) at lines 178–200, and Task 1 (c) items 3 to 6 to the end of Task 1 (lines 6513–6570); the sizes of the ledger
entries §L.41 to §L.55 and of their records; the §L.41 record at lines 36–66, the §L.42 record at lines 24–56, the §L.43
record at lines 34–52, the §L.48 record at lines 14–45, and the key-areas record's *"As ruled"* lines (46–48 and 73);
the successor at lines 1496–1507 and 1760–1822 and its headings. The user's words: the opening instruction with Claude
Code's closing message; "shortened"; "continue".*
