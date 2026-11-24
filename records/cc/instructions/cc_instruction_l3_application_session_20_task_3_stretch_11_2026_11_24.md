# CC dispatch — the L3 application, SESSION 20 of several: Task 3 of the L3 application dispatch, eleventh stretch (§L.33 and §L.34), and nothing else

> **STATUS: WRITTEN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty.md`, the sitting that verified
> session 19 (the user's ruling of 2026-11-24: the session that verifies a stretch also writes the next stretch's
> instruction). CHECKED AS A TURN OF ITS OWN 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_one.md` (its check note closes §8),
> and released with that check.** Under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 18 applied Task 3's first nine stretches, §L.1 to §L.31. Session 19
applied the tenth stretch, §L.32, in commit `76b9919c2bba21fd7e8db4c6969f8ac5d7b75c13` (called **the stretch 10
commit** below), and committed its report as `9037f1b24cc6867acd57fcdf8f4b759b2b5b7953`, the current tip.

**This is session 20. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for TWO ledger entries, in ledger order: §L.33, the fifth
record of family 1 (the catalog's further rows), and §L.34, the sixth (the catalog's substitution rows, part 1). It
commits that eleventh stretch as ONE commit, pushes it, writes its report, and STOPS.** §L.35 is a later session's.

**Why the stretch covers two entries and stops at §L.35** (the user's ruling of 2026-11-24: a writing session judges
how many ledger entries fit). §L.33 gives 8 lines, nothing at §10 and nothing at §11; §L.34 gives 2 lines, nothing at
§10 and nothing at §11; neither brings a row named by another record's line. §L.35 brings three kinds of case these two
do not (a RELOCATED line to *the second axis — voice leading* with a §10 entry under that heading, a line written as a
release ruling's item gives it, with an ellipsis in its quotation, and a row named by two records by claim), so the
stretch stops at the boundary before it.

**What this stretch writes, in one paragraph.** **10 lines, all opening `*RULED DISPOSITION (`, on 10 rows.**
**§L.33** (`cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md`, Ruling 1, the record's one ruling): **8
lines** — 7 with the word **ADOPTED — proposed** (the five rows of the record's §3.1, and one half each of Rows
57.107 (ii) and 57.433 (ii), from its §3.3) and 1 with the word **HISTORICAL** (one half of Row 57.399, form (b-H): the
record decides against that half). **§L.34** (`cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md`,
Ruling 1, the record's one ruling): **2 lines**, both **ADOPTED — proposed** (Row 44.4; Row 46.27's analysis half).
**No line says *as proposed*:** every row-part named is proposed UNPLACED at its row. §3.2 gives every line with its
exact text. **Nothing at §10** (no part is RELOCATED, §3.3). **Nothing at §11** (§3.4). And the in-progress line
brought forward from §L.32 to §L.34 (§3.5). **The other row-parts the two records place get no line** (§3.2's last
paragraph); nineteen of them are listed in the report under *rows given no line now*.

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line, the remaining lines applied (the big dispatch's *Findings in this batch*).

**Documentation only.** This session copies into the reading file the placements the two records already make; it
decides nothing and changes no algorithm. §L.33's record states *"Documentation only. Algorithm: no change."* **§L.34's
record is itself an algorithm change, ratified by the user** (its *"**Algorithm: a change.**"*: L3 recognizes a named
progression with one chord replaced by a substitute, matched through the catalog's substitution mappings, and the match
states which member and which operation); this session writes only that record's two placements into the reading file,
and writes nothing in the successor or in `FRAMEWORK.md` for it (§L.34 *Open* point (4), answered at release by
Ruling 29 of `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`, and Task 4's
*Not written* item 2). Neither record orders an amendment of the successor, the charter or the interface contract that
belongs to Task 3 (§L.33 and §L.34, *Successor*, *Charter*, *Interface contract*).

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `9037f1b24cc6867acd57fcdf8f4b759b2b5b7953`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_20_task_3_stretch_11_2026_11_24.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 10 commit left it.**
   `git diff --quiet 76b9919c2bba21fd7e8db4c6969f8ac5d7b75c13 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 9037f1b24cc6867acd57fcdf8f4b759b2b5b7953 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `9bc1717744a690b557bc33f16ce6c18df095b0c4`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **452**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting` must count
   **18**; `cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting` must count **0**; and
   `cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting` must count **0**. Any other result: STOP and
   report, the file not touched. (The writing side's staged copy: 5,297,185 bytes, 84,518 lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 9037f1b24cc6867acd57fcdf8f4b759b2b5b7953 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1221 and 1222), plus the
     paths sessions 2 to 19 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_two.md` (written by the sitting that
   checked this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_one.md` (written by the sitting that
   wrote this file; untracked, §5 act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The two records this stretch rests on, WHOLE** — they are the authority for every line this session writes (**the
   record's own words govern**, the big dispatch, §L's opening):
   - `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md` (§L.33; 8,151 bytes, 101
     lines by `wc -l`);
   - `records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md` (§L.34; 6,881 bytes,
     93 lines by `wc -l`).

   **Do NOT read the records of §L.1 to §L.32 or of §L.35 to §L.55, and do not open the records' surfaces** (the lines
   quote the records only).
8. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b), its paragraph *Which ADOPTED word, and when as
     proposed is written*, and form (b-H)**, the premise ledger, the declared start state, the standing bars, the
     findings rule);
   - lines 395–430 (how §L is written);
   - **lines 3450–3655 (§L.33 and §L.34, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–3449 (§L.1 to §L.32, applied); lines 3656–5906 (§L.35 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary);
   - **each of the 10 rows §3.2 names, whole, at §6** (lines 435–79484): find each by its heading with the Grep tool,
     pattern `^\*\*Row <n>\.<m> —` (the dot escaped), which must match **exactly once** in the file; read from that
     heading to the row's closing `---`. The writing side found every one exactly once, inside §6;
   - §10 (lines 79943–81039), searched with the Grep tool for every row number of this stretch (§3.3);
   - §11 (lines 81040–83192), searched with the Grep tool for every row number of this stretch (§3.4).

## 3. What this stretch writes

### 3.1 The rules every line follows

1. **The form.** Form (b) of the big dispatch: one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*`
   paragraph and every other sentence of the row untouched. Row 57.399's HISTORICAL line is **form (b-H)**: the record
   decides against one half of the row (its line 49, *"decided against in so far as a style subset selects the catalog
   L3 reads"*), so the line names that half, gives the word **HISTORICAL** and quotes the record's sentence that decides
   against it; the row's other half is moved by the record to the idiom-tag surface and gets no line here (form (b-H):
   *"the rest of the row keeps what the record says of it"*). Every line names its record's file and Ruling 1 (each
   record has one ruling), the record file written as its bare file name, as sessions 10 to 19 wrote theirs. Where §3.2
   names a claim, the line names it (form (b)'s split-row rule); otherwise the line names none. **Each row-part, and each
   half of a split row-part that a record places at L3 or decides against, gets exactly one line**, and no row gets more
   than one line from this stretch.
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"At the
   source now."*). Each new line is followed by one blank line. Read each row's actual shape from its proposed
   paragraph to its end before writing. **The writing side read all 10 rows at the staged copy; none carries an earlier
   ruled or recorded line, and every one ends with a blank line and then `---`.** Their shapes after the proposed
   paragraph:
   - **8 rows with a paragraph headed *"At the source now."* directly after the proposed paragraph; the new line goes
     directly beneath the proposed paragraph, above it:** Rows 57.427, 57.428, 57.430, 57.503, 57.504, 57.107, 57.433
     and 57.399 (all §L.33's). Row 57.107 carries a further paragraph after *At the source now.*, headed *"The
     decisions register at this row."*; it is not touched, and the line goes above *At the source now.* as at the
     others. *(The reading file already carries 23 ruled lines placed this way, directly above an* At the source now.
     *paragraph, by earlier stretches.)*
   - **2 rows: nothing after the proposed paragraph** — Rows 44.4 and 46.27 (§L.34's). Each such row ends, after the
     edit: proposed paragraph, blank line, **the new line, followed by a blank line**, `---`.
   If you find a different shape at a row (an earlier line, a further paragraph, or an ending other than `---`), state
   it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, that line
   is a STOP-and-report.
3. **The quotation.** Each line quotes the record's words §3.2 gives for it: for §L.33's §3.1 rows, the record's §3.1
   bullet whole; for its three §3.3 lines, its §3.3 bullet whole; for §L.34's Row 44.4, the record's *ADOPTED —
   proposed* bullet of *The placements* whole; for Row 46.27, its *Split* bullet whole — in each case the bullet's bold
   lead included as words, its marks dropped. **The writing side checked every quotation against its record by a
   read-only script (words and punctuation, line breaks read as spaces, asterisks not compared): each found exactly
   once.** Before writing each line, find its quoted passage in the record yourself and compare it the same way: every
   word and every punctuation mark must match, line breaks read as spaces. The line keeps its marks exactly as §3.2
   gives them. A difference is a STOP-and-report for that line: no line written, listed in the report under *rows the
   act could not place* with both texts. **The further-rows record spells *"recognise"* (British spelling) in its §3.3
   bullet; the quotation and the half name keep the record's spelling, as a quotation must** (as session 19's lines
   did; the record governs).
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once in the file; the claim §3.2 names
   exists in the row; the row's `*PROPOSED DISPOSITION.*` for that part is **UNPLACED** (item 5); and **the row's
   outgoing statement fits what the record says of the part placing it.** The fit, row by row: Row 57.427, the
   glossary's *Progression* (the record's gloss: *"the glossary's *progression*, a term of the catalog L3 reads"*); Row
   57.428, the glossary's *Schema* (*"*schema*"*); Row 57.430 (i), an entry as one catalog record (*"*entry*"*); Row
   57.503, a progression entry's functional skeleton as a key-relative sequence of (scale degree, chord quality) pairs
   (*"the functional skeleton as a key-relative sequence of (degree, quality) pairs"*); Row 57.504 (i), one entry
   instantiating in every tonality (*"one entry instantiates in every key"*); Row 57.107 (ii), the component read both
   ways, forward for the analysis and predictively for a suggestion tool (the half named: *"read forward for the
   analysis"*); Row 57.399, the browse query, which takes the style subset and loads the active catalog (the half named:
   *"loading the catalog L3 reads from the active styles"*); Row 57.433 (ii), the span as the input to recognize and to
   suggest (the half named: *"input to recognise"*); Row 44.4, the term *Substitution* (*"the term *substitution*, of the
   catalog L3 reads"*); Row 46.27, each operation over the skeleton, inverted in analysis and offered in composition
   (the half named: *"the analysis half"*). A row that does not fit is a STOP-and-report for that row-part: no line,
   listed under *rows the act could not place* with what was read.
5. **The word, and why no line says *as proposed*** (form (b)'s paragraph *Which ADOPTED word, and when as proposed is
   written*; §L.33's and §L.34's *Open* point (1), answered at release by Ruling 9 of
   `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`). **Each record names the
   word in full** for its ADOPTED lines (§L.33: *"ADOPTED — proposed:"* before §3.1's five, *"read forward for the
   analysis ADOPTED — proposed"* for Row 57.107 (ii) and *"input to recognise ADOPTED — proposed"* for Row 57.433 (ii);
   §L.34: *"ADOPTED — proposed:"* before Row 44.4 and *"the analysis half ADOPTED — proposed"* for Row 46.27), so item
   (1) of the paragraph gives **ADOPTED — proposed** for all nine. For Row 57.399 the word is form (b-H)'s, HISTORICAL.
   **The writing side read the proposed paragraph at every one of the row-parts this stretch names: each is UNPLACED**
   (for the rows with claims, at the claim named: Rows 57.430 (i), 57.504 (i), 57.107 (ii), 57.433 (ii); Row 57.504's
   claim (ii) is proposed RELOCATED and gets nothing here). So no line's word is the row's own proposed word, and **no
   line says *as proposed***: the paragraph's *"Otherwise as proposed is not written, and the placement is given in the
   record's words"*. If you find a row-part's proposed word for the part named other than UNPLACED, that line is a
   STOP-and-report. No other wording (such as *"placed from"*) is added. Every one of the 9 ADOPTED lines is listed in
   the report under *ADOPTED words read at the row*, with the proposed word read (UNPLACED) and that its line does not
   say *as proposed*.
6. **The split row-parts, by half.** Four row-parts are split by their records into two halves, one of which gets a
   line here:
   - **Row 57.107 (ii):** *"read forward for the analysis ADOPTED — proposed, read predictively moved to the
     chord-suggestion-tool surface"*. One line: `(ii), its half "read forward for the analysis":`.
   - **Row 57.399 (no claims):** *"loading the catalog L3 reads from the active styles **decided against in so far as a
     style subset selects the catalog L3 reads** (as lead-rows Row 38.79 (i)), listing entries by style moved to the
     idiom-tag surface"*. One line: `Its half on loading the catalog L3 reads from the active styles:`.
   - **Row 57.433 (ii):** *"input to recognise ADOPTED — proposed, input to suggest moved to the chord-suggestion-tool
     surface"*. One line: `(ii), its half "input to recognise":`.
   - **Row 46.27 (no claims):** *"the analysis half ADOPTED — proposed; the composition half moved to the
     chord-suggestion-tool surface"*. One line: `Its analysis half:`.
   The moved halves get no line from these records (form (b): *"A part a record says it moves to another record gets no
   line from the record that moves it"*); they are met at the chord-suggestion-tool record's entry (Rows 57.107 (ii),
   57.433 (ii), 46.27) and at the idiom-tag records' entries (Row 57.399).
7. **Rows named by more than one record** (form (b)'s two-record rule, by part). **No row this stretch writes carries an
   earlier record's line**: the writing side read all 10 at the staged copy and found no `*RULED ` or `*RECORDED ` line
   in any of them, and the two records of this stretch give no row a line each. §L.33's *Rows named by more than one
   record* names **Row 57.393** ((i) here, given no line now; (ii) at §L.32, given no line now); neither gets a line
   from this stretch. **Rows 57.392 (ii), 57.434 (ii) and 57.402** are named by both records of this stretch — §L.33's
   record places them *"waiting wholly"* (its §3.4) and §L.34's names them among what is *"Not decided"* (its §1) —
   and get no line from either. List all four in the report under *rows named by more than one record*, each with what
   §L.33 or §L.34 says of it. If you find an earlier record's line on any part this stretch writes, apply the rule by
   part as the big dispatch gives it; if an earlier stretch's line would have to be deleted or edited, STOP, do not
   commit, and report.

### 3.2 The lines, with their exact text

Each line below is given whole, as it is to be written. Where a block serves several rows, `<claim>` is filled in from
the row list (written `(i)` as the list gives it); where the list gives no claim, `<claim>` and the space after it are
dropped.

**§L.33 — the catalog's further rows record (`cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md`): 8
lines.**

*§3.1's ADOPTED rows — 5 lines, none* as proposed. Rows, in this order: 57.427; 57.428; 57.430, written `(i)`; 57.503;
57.504, written `(i)`.
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md, Ruling 1).* <claim> **ADOPTED — proposed** — "§3.1, follow wholly (5): ADOPTED — proposed: 57.427 (the glossary's *progression*, a term of the catalog L3 reads), 57.428 (*schema*), 57.430 (i) (*entry*), 57.503 (the functional skeleton as a key-relative sequence of (degree, quality) pairs), 57.504 (i) (one entry instantiates in every key)".
```

*§3.3's split row-parts — 3 lines, in the order in which the record names them.* Every one of the three quotes the same
passage, written here once as `<Q>`:
`"§3.3, split by use (3): 57.107 (ii) — read forward for the analysis ADOPTED — proposed, read predictively moved to the chord-suggestion-tool surface; 57.399 — loading the catalog L3 reads from the active styles **decided against in so far as a style subset selects the catalog L3 reads** (as lead-rows Row 38.79 (i)), listing entries by style moved to the idiom-tag surface; 57.433 (ii) — input to recognise ADOPTED — proposed, input to suggest moved to the chord-suggestion-tool surface"`.
The three lines, in this order, each with `<Q>` written out in full where it stands:
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md, Ruling 1).* (ii), its half "read forward for the analysis": **ADOPTED — proposed** — <Q>.
```
— that one at Row 57.107;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md, Ruling 1).* Its half on loading the catalog L3 reads from the active styles: **HISTORICAL** — <Q>.
```
— that one at Row 57.399;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md, Ruling 1).* (ii), its half "input to recognise": **ADOPTED — proposed** — <Q>.
```
— that one at Row 57.433. Each line ends with the closing quotation mark of `<Q>` followed by a period, as the lines
above it do.

**§L.34 — the catalog's substitution part 1 record
(`cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md`): 2 lines.**
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md, Ruling 1).* **ADOPTED — proposed** — "ADOPTED — proposed: Row 44.4 (the term *substitution*, of the catalog L3 reads)".
```
— that one at Row 44.4;
```
*RULED DISPOSITION (cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md, Ruling 1).* Its analysis half: **ADOPTED — proposed** — "Split: Row 46.27 — the analysis half ADOPTED — proposed; the composition half moved to the chord-suggestion-tool surface".
```
— that one at Row 46.27.

**The count.** `*RULED DISPOSITION (`: **10** — 9 **ADOPTED — proposed**, 1 **HISTORICAL**; 8 naming the further-rows
record, 2 naming the substitution part 1 record. None opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlements in §3.2, the writing side's and overrulable by the user:* (1) each line quotes, as the record's
placement, the record's bullet whole, its bold lead's marks dropped as sessions 17 to 19 dropped them — §L.33's §3.1
bullet is the record's list of ADOPTED rows alone, as the recognition records' were; its §3.3 bullet whole for each of
its three half lines, since its one sentence places every half of all three rows, as session 19 quoted the part 2
record's §3.3 bullet whole for each of its eight part lines; §L.34's two bullets of *The placements* each whole. The
records' inner emphasis is kept: the italics around *progression*, *schema*, *entry* and *substitution*, and the bold
around the further-rows record's *"decided against in so far as a style subset selects the catalog L3 reads"*, as
earlier stretches kept a record's own emphasis inside a quotation (the cadence-features record's bold, kept at the
reading file's line 1331 and others; the part 2 record's `*"Layer 5"*`, kept by session 19); (2) each half is named in
the record's own words: where the record names the halves of a claim by phrases of its own (Rows 57.107 (ii) and
57.433 (ii)), the phrase stands in quotation marks after *"its half"*, on the shape of session 19's `(i), its half "to
recognise":` and §10's existing entry `Row 46.46 (i), its "ranked" half`; where it names a half by its subject (Row
57.399), *"its half on"* and the subject, on the shape of session 19's *"Its half on the decided chords and the catalog
as inputs:"*; Row 46.27, whose record names *"the analysis half"*, takes `Its analysis half:`, on the shape of the
existing line *"Its perfect/imperfect half:"* (the reading file's line 1374) and *"Its confidence half:"* (line 1376); a
row with no claims opens with *"Its"*, as those lines do; (3) Row 57.399's HISTORICAL line names the half that is
decided against and quotes the whole §3.3 bullet as *"the record's sentence that decides against it"* (form (b-H)),
the bullet being one sentence; the earlier partial HISTORICAL lines at lines 1374 and 1376 are the precedent for a
half named on a row with no claims; (4) the lines follow ledger order (§L.33's before §L.34's) and, within §L.33, the
record's order.

**What this stretch gives no line** (Task 3 (a)), as §L.33 and §L.34 name them:
- **§L.33's ten §3.2 row-parts — Rows 57.107 (i), 57.108, 57.109, 57.111, 57.390, 57.391, 57.393 (i), 57.430 (ii),
  57.431 and 57.433 (i):** *"No line from this record; listed in the report"*, as Ruling 3 of
  `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part2_sitting.md` rules it, in
  the form of that record's Ruling A, quoting the further-rows surface's §3.2 sentence *"Each row's one disposition is
  written when what it waits for is settled."* (§L.33's table and its *Open* point (2)). Each is listed in the report
  under *rows given no line now*, with §L.33 and those words; each keeps its proposed UNPLACED.
- **§L.34's nine row-parts — Rows 46.24, 46.25, 46.30, 46.31, 46.32, 46.34, 46.26, 46.28 and 46.29:** *"No line from
  this record; listed in the report"*, as Ruling 4 of the same list-answers part 2 record rules it, in the form of its
  Ruling A, quoting the substitution part 1 surface's §3.2 sentence *"Each row's one disposition is written when what it
  waits for is settled."* (§L.34's table and its *Open* point (2)). Each is listed in the report under *rows given no
  line now*, with §L.34 and those words; each keeps its proposed UNPLACED.
- **§L.33's four §3.4 row-parts — Rows 57.392 (ii), 57.434 (ii), 57.402 and 57.453:** *"No line from this record."*
  Not listed under *rows given no line now* (Task 3 (a): that name covers the row-parts a §L entry lists in the report,
  and §L.33 does not list these).
- **§L.33's Row 57.396 (ii) (§3.5):** *"No line from this record."* The record moves it to the
  catalog-and-pairwise-grammar surface, with D-406; it is met at that record's entry. Not listed under *rows given no
  line now*.
- **§L.34's Rows 46.33 and 46.35 (i):** *"No line from this record."* §L.34's *Open* point (3), answered at release by
  the working list's item (xxx), ratified by Ruling 2 of
  `records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_list_answers_part3_sitting.md`: each keeps
  its proposed UNPLACED, and that ruling does not add the two rows to the report. Not listed under *rows given no line
  now*.
- **The moved halves** of Rows 57.107 (ii), 57.433 (ii) and 46.27 (to the chord-suggestion-tool surface) and of Row
  57.399 (to the idiom-tag surface): no line from these records.
- **Rows the records name and do not place:** §L.33's Rows 38.79 (i), 19.39 (v), 24.2, 57.454 and 38.79 (ii); §L.34's
  Rows 57.392 (ii), 57.434 (ii), 57.402, 57.490 (i), 57.487 (ii) and 57.118. No line from these records, not touched.
- **The other claims of the rows this stretch writes** — Rows 57.430 (ii) (above, given no line now), 57.504 (ii),
  57.107 (i) (above) and 57.433 (i) (above) — get nothing from this stretch.

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — nothing written

- **Item 5:** neither record places a part RELOCATED (§L.33: *"No RELOCATED placement is made by this record"*;
  §L.34's table names none), so nothing is appended. The writing side searched §10 (lines 79943–81039) for the row
  number of every row-part the two records place (§L.33's 23, §L.34's 13) as a bare number with look-around. Hits: line
  80649 (the entry for *"Rows 57.392 (i), 57.434 (i) and 57.504 (ii)"*), line 80652 (*"Row 57.396 (i)"*), and lines
  80749 and 80755 (the entry for *"Rows 46.21 (i), 46.22, 46.35 (ii) and 46.36"*) — each **another claim** than any
  this stretch writes or the records place. The rows the records name and do not place (§3.2's last paragraph) add four
  hits, each another claim or part than the one the record names: line 80347 (Row 19.39 (i)), line 80664 (Row 57.487
  (i)), line 80674 (Row 24.2, its part on the prior) and line 80853 (Row 57.490 (ii)). Run the same search with the
  Grep tool and report it; nothing is written at §10.
- **Item 6:** *LEAVES L3* lines belong to the records of §L.21 to §L.24 only, so this stretch writes none.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for any row of this stretch. The writing side's search of §11 (lines 81040–83192) for
  the row number of every row-part the two records place, and of every row they name and do not place, found none. Run the same search with the Grep tool; if you find an entry for a
  row-part this stretch writes, add the NOT QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report
  it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.34 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.35 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 10 commit, as in sessions 11 to 19.
   Attribute it in the diff table to *"session 20's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.33 and
   §L.34 only, in that order**, after sessions 10 to 19's §L.1 to §L.32. §L.35 to §L.55 are not applied, read or
   touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1221 and 1222 ARE landed**, with this file, in §5 act 1, as sessions 8 to 19 landed theirs. Any other untracked handoff entry
   or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** **Item 1 (the decided-against search)** is run over the two records this stretch
   enters (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case matched and not). The
   writing side's search: **in the further-rows record, one hit, *"decided against"*, at its line 49, lowercase**, so a
   search that matches case finds it too, naming Row 57.399 — the hit §L.33 already places, written as Row 57.399's
   HISTORICAL line (§3.2); *"decides against"* and *"decide against"* do not occur. **In the substitution part 1
   record, none of the three, in either search** (as §L.34's *The act's search* says). List the hit and its line in the
   report. Item 2: not reached. Item 3: not reached. Item 4: not reached. Item 5: nothing appended (§3.3). Item 6:
   nothing written (§3.3). Item 7: nothing written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 10 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch, covering both entries.** The
   boundary of D-672 is the ledger entry: if signs of context degradation appear before §L.33 is applied, do not
   commit; STOP and report which lines were applied to the uncommitted copy and that it is not landed. If they appear
   after §L.33's eight lines are written and before §L.34's two are, do not write §L.34's lines and do not commit; STOP
   and report that §L.33 stands applied to the uncommitted copy and §L.34 not begun, so that the user can decide; do
   not commit §L.33 alone on your own judgment, as the checks of §4 item 8 cover both entries.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 10 commit:**
     `git diff 76b9919c2bba21fd7e8db4c6969f8ac5d7b75c13 -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session20_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** a line
     of §3.2 with the blank line after it; the in-progress line of §3.5 item 3; and a NOT QUARANTINED line only if
     §3.4 (b) found an entry. Then
     `git diff --numstat 76b9919c2bba21fd7e8db4c6969f8ac5d7b75c13 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 21 added lines and 1 deleted line** (the 10 lines and their 10 blank lines, 20; the
     in-progress line, a replaced line, one added and one deleted), **less 2 added for each line of §3.2 that was
     STOP-and-report**, plus 1 added for each NOT QUARANTINED line §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 1,099 added lines and 4 deleted lines** (`1099` and `4`), with the same adjustments as above.
     *The writing side's arithmetic: after session 19 the file stood at 1,079 added and 4 deleted against the Task 2
     commit (session 19's report, its §5, as read by the sitting that wrote this file [relayed: the numstat itself not
     re-run here]); this stretch adds 20 lines. The in-progress line replaces a line that is itself an addition against
     the Task 2 commit, so it adds no line and deletes none there.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **462** (452 + 10, less 1
     for each line that was STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must
     count **3**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
     `\*NOT QUARANTINED \(` must count **1**, plus 1 for each entry §3.4 (b) found; and the record names:
     `cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting` **8** (less 1 for each of §L.33's lines that was
     STOP-and-report, plus 1 for a NOT QUARANTINED line naming it),
     `cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting` **2** (the same adjustments for §L.34's lines),
     `cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting` **18** (unchanged).
   - **Then, if every line of §3.2 was written and §3.4 (b) found nothing:**
     `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must print
     **`d00497918ff18efe85fb9ed97543decf7df49b25`** — the blob of the writing side's simulated edit (§8 below: 5,301,823 bytes,
     84,538 lines, line feeds only). A different blob with every count above as given means a byte differs
     somewhere in what was written: do not commit; STOP and report the blob found.
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 11 (§L.33 and §L.34): the 10 lines of the catalog's further rows and substitution part 1 row-parts written in the reading file under their ratifications, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_20_task_3_stretch_11_2026_11_24.md`**, as sessions 2 to 19
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.35, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's two files first, in a commit of their own, before any edit to the reading file.**
   Exactly three paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_20_task_3_stretch_11_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_one.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_twenty_two.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1221 and 1222 and the session 20 instruction of the L3 application landed; Task 3 stretch 11 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: §L.33, then §L.34; for each
   row-part (and each half), the row check of §3.1 item 4 and the word check of §3.1 item 5, then its line of §3.2;
   then the §10 search of §3.3 and the §11 search of §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the
   push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_20_task_3_stretch_11_2026_11_24.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 20 of the L3 application, Task 3 stretch 11 (§L.33 and §L.34) written; stretch 12 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The 10 lines of §3.2, each written (with its reading-file line number after the edit) or STOP-and-report (and why);
   each row's shape as read at the row (§3.1 item 2), stated for Row 57.107 and as one sentence for the other nine if
   they were as stated; the §10 search of §3.3 and the §11 search of §3.4, with their results.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (§L.33's ten and §L.34's nine row-parts, each with its §L entry and the words that list it);
   *recorded lines not written: no disposition word* (none expected); *rows named by more than one record* (Rows
   57.393, 57.392 (ii), 57.434 (ii) and 57.402, as §3.1 item 7 says); *ADOPTED words read at the row* (all 9 ADOPTED
   lines, each with the proposed word read and that its line does not say *as proposed*); *audit questions added*
   (none); *audit questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by row*
   (none: neither record says a row leaves §10); the decided-against search (§4 item 4), with its result, the one hit
   listed with its line and the line written for it.
5. The diff table of §4 item 8, every changed passage attributed, the counts, the two `--numstat` results and the blob.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: §3.2's last paragraph, each with §L.33 or
   §L.34. *A heading of this session's report only, as in sessions 10 to 19's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 20 of the L3 application ends here. Stretch 12 of Task 3 is not begun. Nothing else was done."*

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

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1220, which first verified session 19's stretch at the
objects (no finding; entry 1221 §2) and then, under the user's ruling of 2026-11-24, wrote this file. Read at the
objects for this file, over staged copies: the three git reference files (both refs `9037f1b2…`); the three commit
objects of session 19 and their trees, each SHA-1 recomputed; the reading file at the stretch 10 commit's blob, rebuilt
independently from blob `27e0d551…` and byte-identical to `9bc17177…` and to the file on disk (5,297,185 bytes, 84,518
lines, no carriage return), its `##` headings (§6 at 435, §7 79485, §10 79943, §11 81040, §12 83193) and line 54 in
full; session 19's instruction whole (blob `b88be586…`) and report whole (blob `9297897b…`); the big dispatch at lines
99–278, 3450–3655 and 6616–6820, by search for its `### §L.` headings, and at lines 1, 395 and 7111 for their
headings, its blob recomputed on the staged copy (`b5274c2c…`, 941,330 bytes, 7,157 lines); the two records whole —
the further-rows record (blob `cd71cda104fda65f2a111742b50dc480154e7f85`, 8,151 bytes, 101 lines by `wc -l`, no
carriage return) and the substitution part 1 record (blob `d34e404d5c6bb9cfed87ff4e4709d3ce80bd0ddf`, 6,881 bytes, 93
lines, no carriage return); the list-answers part 2 record at its `##` headings and lines 1–12, 25–45 and 100–137 (Ruling
A's opening and its ruling, Ruling 3's ruling, Ruling 4 whole); the further-rows surface's §3.2 sentence at its line 116 and the substitution part 1 surface's at
its line 164; §L.35's table and its *Rows named by more than one record* paragraph, by search, for the judgment of
where the stretch stops. Each of the 10 rows found exactly once by its heading, inside §6, and read whole from its
heading to its closing `---`: its shape, no earlier ruled or recorded line, its proposed word for the part named
(UNPLACED at each) and its outgoing statement, as §3.1 items 2, 4 and 5 state; the reading file's existing partial
HISTORICAL lines at lines 1331, 1335, 1374 and 1376 and the 23 ruled lines directly above an *At the source now.*
paragraph, by script; §10 and §11 searched for the row number of every row-part the two records place as a bare number
with look-around (§10: the four hits §3.3 names first, each another claim; §11: none); the counts §1 check 4 gives. Every quotation of §3.2 checked
against its record by a read-only script (line breaks joined, asterisks removed): each found exactly once. The two
records searched for the three decided-against phrases (line breaks joined, case matched and not): the further-rows
record one hit, *"decided against"*, line 49; the substitution part 1 record none. **The edit simulated on a copy of the
reading file in the container** by §3.1 item 2's placement rule and §3.5 item 3's line, the lines taken by script from
this file's own text, gives, against the staged file, **21 added lines and 1 deleted**, the counts **462 / 3 / 53 / 26 /
1 / 1**, the record names **8** (further rows), **2** (substitution part 1) and **18** (recognition part 2), every
quotation found exactly once in its record, no line saying *as proposed*, and the blob **`d0049791…`** (5,301,823
bytes, 84,538 lines; the 4,638 bytes added equal the sum computed from the ten lines, their blank lines and the
in-progress line's change); each new line's place in the copy read back at Rows 57.107 and 44.4. Relayed, not re-checked here: the archive JSON's blob `1df4f207…` and the
untracked paths (session 19's report, §1 item 5); the Task 2 commit `4b6dc3bd…` (the same text session 19's instruction
gives for the same object); the 1,079 added and 4 deleted lines against the Task 2 commit after session 19 (session
19's report, not re-run); the end of `cowork_handoff.md`'s topmost block at line 255 and the line-180 start of
`cowork_audit_protocol.md`'s dispatch-protocol section (as session 19's instruction gives them, checked there by the
sitting booted on entry 1219).*

*Check note: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1221, checking this file as a turn of its own
(the user's Ruling 1 (e) of 2026-11-24). Read at the objects, over staged copies: the three git reference files (both
refs `9037f1b2…`); the blobs of the big dispatch (`b5274c2c…`), the reading file (`9bc17177…`, 5,297,185 bytes,
84,518 lines), the two records (`cd71cda1…`, `d34e404d…`) and this file as written (`03118a85…`), each recomputed; the
two records whole; the big dispatch at lines 118–137, 159–274, 3450–3655 and 6616–6820, and its `### §L.` and Task
headings; the 10 rows and Row 57.393, each found once inside §6 and read whole (shape, no earlier line, UNPLACED at the
part named, the fit); line 54; the starting counts; the precedents at lines 1331, 1335, 1374, 1376, 77382, 77906 and
80671, and the 23 ruled lines above an* At the source now. *paragraph; §10 and §11 searched as §3.3 and §3.4 now state;
the list-answers part 2 record at lines 9–45 and 94–137; the list-answers part 3 record at its headings and lines
44–62; the release part 2 record's Ruling 9 at lines 388–404 and its headings; the two surfaces' §3.2 sentences
(further rows, line 116; substitution part 1, line 164). Every quotation of §3.2 found exactly once in its record,
emphasis marks included, the bold leads' own marks dropped; the decided-against search as §4 item 4 gives it.
**Re-simulated from this file's own text: the blob `d00497918ff18efe85fb9ed97543decf7df49b25`, 21 added and 1 deleted,
the counts as §4 item 8 gives them.** Corrected, no former wording kept (unreleased): handoff entry 1222 added to what
act 1 lands (§1 item 5, §2 item 4, §4 item 3 and its heading, §5 act 1 and its subject), in place of entry 1220 at §2
item 4; the §10 and §11 searches stated at the reach they had (§3.3, §3.4, the provenance above), with the four further
§10 hits for the rows the records name and do not place; the banner. No line of §3.2, row, disposition word, count or
the expected blob changed. Relayed, not re-checked: the archive JSON's blob, the Task 2 commit and the 1,079 added and 4
deleted lines against it, `cowork_handoff.md`'s line 255, `cowork_audit_protocol.md`'s line 180, and Ruling 29 of the
release part 2 record (read only as §L.34's* Open *point (4) gives it).*
