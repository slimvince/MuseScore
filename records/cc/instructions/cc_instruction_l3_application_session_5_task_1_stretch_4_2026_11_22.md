# CC dispatch — the L3 application, SESSION 5 of several: Task 1 of the L3 application dispatch, fourth stretch (§L.34 to §L.40), and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_six.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Sessions 2, 3 and 4 applied Task 1 for §L.1 to
§L.15, §L.16 to §L.25 and §L.26 to §L.33. Session 4's commits are `49d32b25479f792571688c3658704aa8e28d935e` (the writing
side's two files), `ea784008853a0e02e942f3128a0193c8ad3f597c` (the successor, blob
`b77ee3306957e14a1862dd98d928c1b8005b7824`) and `13d0e22641b61ec6de061aa585be73f26318870b` (its report), all verified at
the objects by the Cowork sitting that wrote this file.

**This is session 5. It continues the big dispatch's Task 1 (the successor file
`cowork_derived_specification_l3_2026_11_08.md`) for the ledger entries §L.34 to §L.40 only, commits and pushes that
fourth stretch, writes its report, and STOPS.** Of these seven entries, only §L.39 and §L.40 order text in the successor:
§L.39 one added statement and one list for the notes, §L.40 one list for the notes. §L.34 to §L.38 each state that the
successor gets no amendment; for them Task 1 writes nothing, and their records are read so that this is confirmed at
the record. Each later stretch gets its own instruction, sized and written after the previous one is verified.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §3,
and only for this session. Where this file and the big dispatch seem to differ on anything §3 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change.** This session writes the successor file by the big dispatch's Task 1, which
places the ruling records' own words; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `13d0e22641b61ec6de061aa585be73f26318870b`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_5_task_1_stretch_4_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The successor stands as session 4 committed it** (replaces the big dispatch's Task 1 *Before the edit* for this
   session). `git hash-object cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"` must print
   `b77ee3306957e14a1862dd98d928c1b8005b7824`, and
   `git ls-tree 13d0e22641b61ec6de061aa585be73f26318870b -- cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"`
   must show the same blob. Anything else: STOP and report.
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 13d0e22641b61ec6de061aa585be73f26318870b -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the two files §4 item 1 lands (this instruction and handoff entry 1187), plus the
     393 untracked paths sessions 2 to 4 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). `.claude/` and
     `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is expected and
     not a STOP. List in the report every untracked path the tool reports outside those. A further untracked
     `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a STOP (the
     big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **The seven ruling records §L.34 to §L.40 name, each WHOLE, in §L's order:**
   - §L.34 `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md`
   - §L.35 `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md`
   - §L.36 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md`
   - §L.37 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md`
   - §L.38 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md`
   - §L.39 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md`
   - §L.40 `records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md`

   They are the authority for every amendment this session applies: **the record's own words govern** (the big
   dispatch, §L's opening). Do NOT read the records of §L.1 to §L.33 or of §L.41 to §L.55. No surface is read: every
   text this stretch writes is a record's own. **Do not read**
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (211,236 bytes): §L.34's
   *Open* point (4) states that release ruling's answer (no successor text), and that is all this session needs of it.
3. **The successor WHOLE, at the git object of session 4's Task 1 commit:**
   `git show ea784008853a0e02e942f3128a0193c8ad3f597c:cowork_derived_specification_l3_2026_11_08.md`, written to a
   scratch path outside the repository and read there with the Read tool in ranges. It is 213,172 bytes, 2,025 lines,
   and has no line longer than 1,211 characters. The derivation is not read.
4. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
5. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard
   (its condition in `CLAUDE.md` is not met).
6. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_seven.md` (the current entry point,
   written by the sitting that wrote this file; untracked, §4 item 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_six.md` (the one before it).
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
   - **lines 3543–4350 (§L.34 to §L.40, your stretch)**;
   - lines 6100–6571 (Task 1, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3542 (§L.1 to §L.33, already applied); lines 4351–6099
   (§L.41 to §L.55, and Task 0); lines 6572–7110 (Tasks 2 to 5); lines 7136 to the end. Nor the derivation, the reading
   file, `FRAMEWORK.md`, `cowork_derived_specification_l0_l1_2026_09_03.md`, `tools/audit/gen_status_batch_bound.py`
   or `records/cowork/handoff/cowork_away_returns.md`: each belongs to a later Task's session or is not needed here.
   When you search the big dispatch, search only inside the ranges above (session 4's whole-file search showed lines
   outside them).

## 3. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 1 applies** (Task 1 (a): *"Each §L entry's Successor — amendments part is applied, in
   ledger order"*) → **§L.34 to §L.40 only, in ledger order.** §L.1 to §L.33 are applied already and are not touched;
   §L.41 to §L.55 are not applied, read or touched. **For §L.34 to §L.38**, the ledger entry states that the successor
   gets no amendment (for §L.34, its *Open* point (4), answered at release: no successor text): confirm that against
   each record read whole and write nothing for it. If a record of §L.34 to §L.38 orders text in the successor after
   all, STOP and report for that entry; apply the rest. Their charter, interface-contract, reading-file and register
   parts belong to Tasks 2 to 4 and are not touched; so do the reading-file, charter and register parts of §L.39 and
   §L.40.
3. **Task 1 (c), split by stretch.** Apply here only the parts whose ordering record is one of §L.34 to §L.40:
   - (c) items 1, 2 and 4: applied by earlier sessions; nothing here.
   - **(c) item 3, the added statement: §L.39's one** (its *Successor* (1)), under **(c) item 3 (i)**: the record
     introduces it *"For the amended L3 specification:"* and quotes its text whole (the §L.39 record, lines 71–72).
     - **Heading** (form (a)):
       `### Added — records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 2, Part A.1`
       (the record names the part *"Part A.1 — the boundary statement"*, its line 66).
     - **Lead-in**, in the shape sessions 2 and 4 used for (i) statements: `*Ruling 2, Part A.1, as the record quotes it:*`
     - **The quotation**, one line, the record's sentence quoted whole without the record's italic marks (as session 4
       wrote §L.27 part E and §L.28 without the record's quotation marks):
       `> A chord-suggestion tool, if one is built, lies outside the analysis. It may read L3's published matches and the same catalog L3 reads. Nothing in the analysis depends on it.`
       No sub-item beneath it.
     - **Place:** in the existing section `## Statements added by the L3 family rulings`, after §L.28's statement (the
       line beginning `> As facts of the published literature`, line 2019 of blob `b77ee330…`) and before the `---`
       that closes the section, separated by one blank line on each side as the other added statements are.
     - §L.26 amendment 1 says §L.48's statement goes directly after §L.26 part C: **that is a later stretch's act; write
       nothing for §L.48 here.**
   - **The notes section — created by this session**, since §L.39 and §L.40 each place a list there (form (a), last
     bullet). **Place:** directly after the `---` that closes the section of added statements and its following blank
     line, and before the `## 5. The blind act's own record — where it stands` heading. Its shape, line by line:
     1. `## Notes — lists the records place here, not ruled`, then a blank line;
     2. **§L.39's list** (its *Successor* (2)):
        - the heading `### records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md, Ruling 1`, a blank line;
        - the lead-in `*The record's own words for this list:*`, a blank line;
        - the §L.39 record's lines 54–56, each line quoted as `> ` followed by the line exactly as the record has it
          (they begin `**How it is recorded — the writing side's proposal as put, not a ruled act:**`), a blank line;
        - the lead-in `*The seven items, as the record gives them (its lines 43–50):*`, a blank line;
        - the §L.39 record's lines 43–50, each quoted the same way (they begin `- 38.81 (ii):` and end
          `with both readings in mind."*`), a blank line;
     3. **§L.40's list** (its *Successor* (2)):
        - the heading `### records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md, Ruling 1`, a blank line;
        - the lead-in `*The list and the record's own words for it, as the record gives them (its lines 34–39):*`, a blank line;
        - the §L.40 record's lines 34–39, each quoted as `> ` followed by the line exactly as the record has it (they
          begin `- **Outside every charter, carried for a display's own specification` and end
          `without adding them to the specification itself.`);
     4. a blank line, `---`, a blank line; then the existing `## 5.` heading follows unchanged.

     *Why §L.40's list is quoted as the record's whole bullet:* the record gives the rows and its "not a ruled act"
     words in one bullet, so quoting the bullet whole carries both, as form (a) requires, and adds nothing. *The two
     list headings* (`### <record file>, Ruling 1`) are the writing side's choice for form (a)'s *"under its record's
     name"*. If a record's line numbers given here do not hold at the record (a line range starting or ending somewhere
     other than the words named), STOP and report for that list; apply the rest.
   - (c) item 5: unchanged; none of §L.34 to §L.40 orders text at OQ-L3-1 or OQ-L3-11 to OQ-L3-14 (if one does, (c)
     item 5 says what follows). (c) item 6: unchanged, for this stretch's entries.
   If you find that a part assigned to this session depends on the words of a record outside §L.34 to §L.40, or a part
   not assigned here is ordered by a record inside it: STOP and report for that part; apply the rest.
4. **Task 1 (a) and (b) are not re-applied.** The file exists (§1 check 4); it is edited in place by targeted edits only,
   never re-typed and never re-made from the derivation. Two lines written by earlier sessions are looked at:
   - **The banner's ANSWERED set**, the parenthesis in the sentence *"The open questions of §4 stand with their ANSWERED
     marks where a ruling answered them (…)"*, is re-taken at the file after this stretch's edits. The writing side's
     expectation: **unchanged — OQ-L3-2, OQ-L3-3, OQ-L3-4, OQ-L3-5, OQ-L3-6, OQ-L3-7, OQ-L3-8 and OQ-L3-10, eight**, as
     no entry of this stretch answers an open question. If the file then carries a different set, write that set and
     report the difference. Nothing else in the banner is touched.
   - **The in-progress line beneath the banner** (line 19) becomes exactly:

     `*Application in progress: this file carries the amendments of §L.1 to §L.40 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.41 to §L.55 are applied by later Claude Code sessions, one stretch each (was: "§L.16 to §L.55"; staleness fix shown, records/cc/instructions/cc_instruction_l3_application_session_4_task_1_stretch_3_2026_11_22.md, §3 item 4); the banner above is true of the file only when the last of them removes this line.*`

     Two ranges change, both the ordinary advance: `§L.1 to §L.33` becomes `§L.1 to §L.40`, and `§L.34 to §L.55`
     becomes `§L.41 to §L.55`. The parenthesis session 4 wrote stays as it is. Attribute the change in the diff table to
     *"session 5's instruction, §3 item 4"*.
5. **Task 1 (d), one commit for the whole of Task 1** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, commit the
   entries already applied, write in the in-progress line the last entry actually applied instead of §L.40 (and the
   entry after it instead of §L.41), set the banner's ANSWERED set to what the file carries, and report which entries
   were applied. If you are inside an entry, do not commit; STOP and report which entries were applied to the
   uncommitted file and that it is not landed.
6. **Task 1 (e), the check before the commit,** is run with these changes for this stretch:
   - **The method:** store the edited successor with `git hash-object -w cowork_derived_specification_l3_2026_11_08.md`
     and diff the two blobs, `git diff -U0 b77ee3306957e14a1862dd98d928c1b8005b7824 <the new blob>`, written to a
     scratch file outside the repository and read with the file tools. The base is session 4's successor, not the
     derivation object.
   - **The attributions available:** only §L.39 *Successor* (1) (the statement, (c) item 3 (i)), §L.39 *Successor* (2)
     and §L.40 *Successor* (2) (the notes lists, form (a) last bullet), the creation of the notes section that carries
     them, and §3 item 4's in-progress line (and the banner, only if the ANSWERED set differed). A changed passage none
     of those accounts for is a STOP-and-report and the file is not committed until it is removed.
   - **Lines removed or replaced:** none, except the in-progress line (and the banner line, only as above). Everything
     else is added lines, in two places only: the statement inside the section of added statements, and the notes
     section between that section's closing `---` and the `## 5.` heading.
   - **Bold text:** no derived statement's bold text changes in this stretch. Bold inside the new quotations is the
     records' own and is checked as part of the quotation.
   - **Every statement, open question and passage that earlier sessions wrote is byte-identical to blob `b77ee330…`**,
     except the line(s) of §3 item 4. L3-S1 to L3-S42 and OQ-L3-1 to OQ-L3-14 are each present exactly once.
   - **Each quotation is checked at its source:** the statement occurs in the §L.39 record, whitespace normalized and
     the record's italic marks set aside; each notes list, with its `> ` prefixes removed, equals its record's lines
     (§L.39 lines 54–56 and 43–50; §L.40 lines 34–39) line for line.
   - **Headings:** count only lines that begin with `#`. Blob `b77ee330…` has 31; the new blob must have 35 — the one
     new `### Added` heading, the `## Notes` heading and the two list headings, and no other. Quoted headings inside
     `> ` lines are not headings of the successor.

   The commit subject is exactly:

   `application L3, Task 1 stretch 4 (§L.34 to §L.40): the derived specification as amended by seven more L3 family ruling records, every amendment citing its record, not ratified`

   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
7. **E1** is checked for this stretch only, as items 3 to 6 restrict it. The full E1 belongs to the session of the last
   stretch.
8. **Where the batch ends for this session.** After §4's acts, this session STOPS. It does not begin §L.41, Task 2 or
   any later Task.

## 4. The acts, in order

1. **Land the writing side's two files first, in a commit of their own.** Exactly two paths, both expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_5_task_1_stretch_4_2026_11_22.md`, and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_seven.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entry 1187 and the session 5 instruction of the L3 application landed; Task 1 stretch 4 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 1 for §L.34 to §L.40**, as the big dispatch's Task 1 and §3 above give it, ending with §3 item 6's check, its
   commit and its push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_5_task_1_stretch_4_2026_11_22.md` with the
   items of §5. Commit that ONE path alone, subject exactly:
   `report: session 5 of the L3 application, Task 1 stretch 4 (§L.34 to §L.40) written; stretch 5 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 5. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.34 to §L.40, in order: every successor amendment by its number, applied (and where), or
   STOP-and-report (and why); for §L.34 to §L.38, that the record was read whole and orders no successor text (or the
   STOP). The same for the notes section, and for §3 item 4.
4. The ANSWERED set the file carries, set against §3 item 4's eight.
5. The diff table of §3 item 6, every changed passage attributed, with the line numbers of each part in the new blob.
6. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
7. The last sentence, exactly: *"Session 5 of the L3 application ends here. Stretch 5 of Task 1 is not begun. Nothing else was done."*

## 6. What the earlier sessions established, for the record (relayed here; verified by the Cowork sittings at the objects)

Session 1 committed Task 0 as `cbde76fd78a244540df64895191a511df186cc29` and stopped at Task 0's guard-set check: two
tools failing beyond the thirteen of the declared start state, item 2 (`gen_evidence_pin_membership.py`, which counts
the ruling records on disk, and `gen_per_session_reading.py`, which finds handoff entries through git). Session 2 applied
§L.1 to §L.15 and held one amendment as STOP-and-report, §L.15 amendment 4, as that entry's own settled note orders.
Sessions 3 and 4 applied §L.16 to §L.25 and §L.26 to §L.33 with no STOP. **This session runs no guard**, so neither red
bears on its acts; both are declared here so that no later reader takes them for this session's doing.

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

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1186. Read at the objects for this file: the
three git reference files; the commits `49d32b25…`, `ea784008…` and `13d0e226…` and their trees against their parents',
folder by folder; the successor at blobs `32cf8fdb…` and `b77ee330…` (their diff, the ten added parts against the two
surfaces and three records, the counts, the ANSWERED set, the section layout, the line count and longest line); session
4's instruction and report whole; the big dispatch (blob computed from the staged bytes) at the *Successor* lines of
§L.34 to §L.55, the label lines of §L.34 to §L.40, §L.34's *Open* point (4), §L.39's *Successor* and *Open* points,
§L.40's *Successor*, form (a) at lines 178–200, and Task 1 (c) items 3 to 6 and (d); the sizes of the ledger entries
§L.34 to §L.55 and of their records; the §L.39 record at lines 1–90 and the §L.40 record at lines 20–49. The user's
words: the opening instruction with Claude Code's closing message; "shortened"; "continue".*
