# Report — the L3 application, session 16: Task 3, seventh stretch (§L.25 to §L.28)

> **STATUS: SESSION REPORT.** Claude Code, 2026-11-23, executing
> `records/cc/instructions/cc_instruction_l3_application_session_16_task_3_stretch_7_2026_11_23.md` (called **the
> instruction** below; blob `60c25745afa00783313adcdce67b343edaf1b27a`) under the big dispatch
> `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`).
> Documentation only. No algorithm change. Nothing in this report is a recommendation.

## 1. The first checks (the instruction's §1), and the repeat of check 2

1. **The tip.** `.git/HEAD` read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` both read `3d1a95a119069b208acfcb0c68c355773446d9f1`. Held.
2. **The big dispatch.** `git hash-object` printed `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Held.
3. **This instruction's own identity.** `git hash-object` printed `60c25745afa00783313adcdce67b343edaf1b27a`.
4. **The reading file.** `git diff --quiet 4ab7231b3091933d087f50b089cb361f7fecd22a -- …` gave exit 0; `git ls-tree` at
   `3d1a95a1…` and `git hash-object` on the working tree both showed `8c9596ccb9b76ef6404fe38204a02e025544878d`. Counts
   with the Grep tool: `*RULED DISPOSITION (` **354**; `*RULED PLACEMENT (` **3**; `*RECORDED DISPOSITION (` **53**;
   `*LEAVES L3 (` **26**; `*Row 7.67 is not transferred` **1**; `*NOT QUARANTINED (` **1**; the four record names
   **0** (searched as one alternation, zero hits). Held.
5. **The working tree**, enumerated with `tools/audit/changed_paths.py` into the session scratchpad and read there with
   the file tools (398 path records).
   - Tracked modifications: exactly one, `tools/audit/claude_md_finer_archive.json`. `git hash-object` printed
     `1df4f20771b6782cbb965c293db4d445bc7ec892` and `git ls-tree 3d1a95a1… --` showed the same blob, so it is not a
     modification and was not landed.
   - Untracked: the three files act 1 lands; 387 paths under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. **One untracked path
     outside those:** `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_ten.md` — a further
     handoff entry, the writing side's under the big dispatch's A1: not landed, not a STOP.
6. **Check 2 repeated immediately before staging act 1:** `b5274c2c7b82c171e1b44c1ed79635a34877b142`, unchanged. In the
   same call the instruction was pinned with `git hash-object -w` (blob `60c25745…`, unmoved since check 3) and the two
   handoff entries' blobs read `64573f95bd9e704b07e0d1c5c607b065f3c168ee` (1208) and
   `8b507617e12dac5bdebe9355c416394518709fe8` (1209), the writing side's.

## 2. The commits

| Act | Full hash | Verified at the object (`git show --stat`) |
|---|---|---|
| 1 — landing | `4b4b4e3777bd8ececcfee02797b21a8d55e64c1c` | subject as §5 act 1 orders; adds exactly the instruction and handoff entries 1208 and 1209, 783 insertions, nothing else |
| 2 — Task 3, stretch 7 | `a3624335004095deb1cc663749b65d8e84adcdb6` | subject as §4 item 8 orders; changes only `ratification_surfaces/cowork_comparison_l3_reading.md`, 109 insertions and 1 deletion; the file's blob at the commit `7103b87c3300f977f30b440b986303756eb46a68`, equal to the working tree |
| 3 — this report | the commit that carries this file | verified in the closing message, which this file cannot contain |

Each push was verified at `.git/refs/remotes/origin/master`: `4b4b4e37…` after act 1, `a3624335…` after act 2.

## 3. The 54 lines, the row shapes, and the §10 and §11 searches

Every line below was written exactly as the instruction's §3.2 gives it, `<claim>` filled from its row list. Line
numbers are the reading file's after the edit (blob `7103b87c…`). **No line was STOP-and-report.**

| # | Row-part | Record, part | *as proposed* | Line |
|---|---|---|---|---|
| 1 | 4.2 | display, A | yes | 2170 |
| 2 | 4.3 | display, A | yes | 2185 |
| 3 | 7.329 (ii) | display, A | yes | 8535 |
| 4 | 7.330 | display, A | yes | 8551 |
| 5 | 15.42 (iii) | display, A | yes | 22327 |
| 6 | 19.1 | display, A | yes | 24361 |
| 7 | 19.3 (ii) | display, A | yes | 24391 |
| 8 | 21.191 | display, A | yes | 30823 |
| 9 | 21.205 | display, A | yes | 31029 |
| 10 | 57.119 | display, A | yes | 74412 |
| 11 | 7.5 (i) | display, B | yes | 3332 |
| 12 | 7.5 (ii) | display, B | yes | 3334 |
| 13 | 7.6 | display, B | yes | 3349 |
| 14 | 7.24 | display, B | yes | 3645 |
| 15 | 7.59 | display, B | yes | 4233 |
| 16 | 7.226 (ii) | display, B | yes | 6980 |
| 17 | 7.227 | display, B | yes | 6997 |
| 18 | 7.228 | display, B | yes | 7014 |
| 19 | 7.274 | display, B | yes | 7696 |
| 20 | 7.294 (i) | display, B | yes | 7998 |
| 21 | 8.54 | display, C | yes | 9953 |
| 22 | 19.4 | display, D | yes | 24406 |
| 23 | 19.5 | display, D | yes | 24422 |
| 24 | 19.6 | display, D | yes | 24437 |
| 25 | 19.8 | display, D | yes | 24468 |
| 26 | 19.37 | span kinds, A | yes | 24989 |
| 27 | 19.40 | span kinds, A | yes | 25081 |
| 28 | 38.62 (i) | span kinds, A | yes | 48460 |
| 29 | 38.62 (ii) | span kinds, A | yes | 48462 |
| 30 | 38.64 (i) | span kinds, A | yes | 48497 |
| 31 | 38.64 (ii) | span kinds, A | yes | 48499 |
| 32 | 38.83 (i) | span kinds, A | yes | 48828 |
| 33 | 38.84 | span kinds, A | yes | 48845 |
| 34 | 38.63 | span kinds, B | yes | 48478 |
| 35 | 38.83 (ii) | span kinds, C | yes | 48830 |
| 36 | 57.354 | span kinds, C | yes | 75549 |
| 37 | 19.29 (i) | architecture rules, A | yes | 24821 |
| 38 | 19.29 (ii) | architecture rules, A | yes | 24823 |
| 39 | 19.53 (ii) | architecture rules, A | yes | 25294 |
| 40 | 19.33 | architecture rules, B | yes | 24905 |
| 41 | 19.56 (iii) | architecture rules, C | yes | 25347 |
| 42 | 19.76 (ii) | architecture rules, C | yes | 25683 |
| 43 | 19.77 | architecture rules, C | yes | 25700 |
| 44 | 19.78 | architecture rules, C | yes | 25715 |
| 45 | 19.82 | architecture rules, C | yes | 25774 |
| 46 | 20.7 | architecture rules, D | yes | 26338 |
| 47 | 38.47 | architecture rules, E | **no** (narrower wording) | 48196 |
| 48 | 38.48 | architecture rules, E | **no** (narrower wording) | 48213 |
| 49 | 8.105 (i) | architecture rules, F | yes | 10845 |
| 50 | 36.111 (i) | architecture rules, F | yes | 42848 |
| 51 | 20.31 (i) | literature facts | yes | 26725 |
| 52 | 56.2 (i) | literature facts | yes | 72040 |
| 53 | 56.2 (ii) | literature facts | yes | 72042 |
| 54 | 36.106 (i) | literature facts | **no** (narrower wording) | 42748 |

**The row checks (§3.1 item 4).** Each of the 48 headings matched the pattern `^\*\*Row <n>\.<m> —` exactly once, all
inside §6 (one alternation over the 48 headings returned 48 hits, one per row). Each claim named exists in its row.
Each row's outgoing statement fits what its record says of the part placing it — for example Row 7.294 (i), *"no
three-role prediction target"*, under the display record's part B on the tonic / subdominant / dominant summary; Row
38.83 (ii), nest or cross-cut, under the span-kinds record's part C; Row 36.106 (i), the cues validated on single lines,
under the literature-facts record's narrower sentence. No row was found not to fit.

**The quotations (§3.1 item 3).** The nineteen distinct quoted passages of §3.2 were each compared with the record's
own text, line breaks read as spaces and asterisks removed: **each found exactly once**, in the record named.

**Row shapes (§3.1 item 2), as read at the rows.**
- **The 41 rows of the first bullet** were as stated: nothing after the proposed paragraph but a blank line and `---`.
- **Row 7.329:** after the proposed paragraph, one earlier ruled line on claim (i)
  (`cowork_rulings_2026_11_03_l3_cadence_type_sitting.md`, Ruling 2, **HISTORICAL**), then `---`. The new line for
  claim (ii) went after it.
- **Row 7.294:** one earlier ruled line on claim (ii) (`cowork_rulings_2026_11_03_l3_cadence_features_sitting.md`,
  Ruling 1, **RELOCATED**), then `---`. The new line for claim (i) went after it.
- **Row 8.105:** one earlier ruled line on claim (ii) (`cowork_rulings_2026_11_08_l3_disposition_words_sitting.md`,
  Ruling 1, **HISTORICAL**), then `---`. The new line for claim (i) went after it.
- **Row 36.111:** one earlier ruled line on claim (ii) (`cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md`,
  Ruling 1, **HISTORICAL**), then the paragraph *"The decisions register at this row."*, then `---`. The new line for
  claim (i) went between the earlier line and that paragraph.
- **Row 57.119:** the proposed paragraph, then *"At the source now."*, then *"The decisions register at this row."*,
  then `---`. The new line went directly beneath the proposed paragraph.
- **Row 57.354:** the proposed paragraph, then *"At the source now."*, then `---`. The new line went directly beneath
  the proposed paragraph.
- **Row 56.2:** the proposed paragraph, then *"At the source now."*, then *"The decisions register at this row."*, then
  `---`. The two new lines, claim (i) first, went directly beneath the proposed paragraph.
- The six rows with two lines from this stretch (7.5, 38.62, 38.64, 38.83, 19.29, 56.2) carry claim (i)'s line first.

**§10 (§3.3).** Searched (§10 located by its heading at line 79747, §11 at 80834, §12 at 82987, on the pre-edit file)
for every row number of this stretch as a bare number, with a preceding digit or dot and a following digit excluded.
Hits in §10 name only other claims: Row 7.294 (ii) (line 79835), (iii) (line 79984, a line that opens with *"7.294 (iii)
and 7.332"*, read as the search printed it) and (iv) (line 80024); Row 7.226 (i) (line 79979); Row 19.56 (ii) (lines 80564 and 80567); Row 36.106
(iii) (lines 80725 and 80729). **No row-part of this stretch stands in a §10 entry. Nothing appended to §10; no *LEAVES
L3* line written.**

**§11 (§3.4).** Hits: Row 15.42 (i) (line 81314) and (ii) (line 81315); Row 19.3 (i) (line 81419) — other claims, not
touched; and the two member headings reading *4.3* (*"4.3 ChordSymbolFormatter"*, line 80887; *"4.3b HarmonicRhythm"*,
line 80907), not rows. **§11 carries no entry for any row-part of this stretch. No NOT QUARANTINED line written; no
audit question added.**

## 4. The report headings Task 3 names, for this stretch's rows

- **Rows the act could not place:** none.
- **Rows given no line now:** none.
- **Recorded lines not written: no disposition word:** none.
- **Rows named by more than one record:**
  - **Row 7.329** — claim (i) by `cowork_rulings_2026_11_03_l3_cadence_type_sitting.md`, Ruling 2 (§L.6),
    **HISTORICAL**; claim (ii) by the display record, Ruling 1 (§L.25), **ADOPTED — proposed**. Different claims; both
    lines stand.
  - **Row 7.294** — claim (ii) by `cowork_rulings_2026_11_03_l3_cadence_features_sitting.md`, Ruling 1 (§L.5),
    **RELOCATED**; claim (i) by the display record, Ruling 1 (§L.25), **ADOPTED — proposed**. Different claims; both
    lines stand.
  - **Row 8.105** — claim (ii) by `cowork_rulings_2026_11_08_l3_disposition_words_sitting.md`, Ruling 1 (§L.2),
    **HISTORICAL**; claim (i) by the architecture-rules record, Ruling 1 (§L.27), **ADOPTED — proposed**. Different
    claims; both lines stand.
  - **Row 36.111** — claim (ii) by `cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md`, Ruling 1 (§L.23),
    **HISTORICAL**; claim (i) by the architecture-rules record, Ruling 1 (§L.27), **ADOPTED — proposed**. Different
    claims; both lines stand.
  - **Row 36.106** — claim (iii) is among §L.24's relocated row-parts, named there with **no line**; claim (i) by the
    literature-facts record, Ruling 1 (§L.28), **ADOPTED — proposed** in the narrower wording. Only one line stands on
    the row.
  - No earlier line was deleted or edited; no part received two lines with differing words.
- **ADOPTED words read at the row:** all 54 row-parts listed in §3's table. For each, the proposed paragraph read
  **ADOPTED — proposed** for the part named; the line's word is therefore **ADOPTED — proposed** (form (b)'s paragraph,
  item (4)). Lines 1 to 46 and 49 to 53 say *as proposed*; lines 47, 48 and 54 (Rows 38.47, 38.48 and 36.106 (i)) do
  not, their records adopting narrower content than the proposal. For the split rows the proposed word was read at the
  claim named: Rows 7.5 (i) and (ii), 7.226 (ii), 7.294 (i), 7.329 (ii), 15.42 (iii), 19.3 (ii), 19.29 (i) and (ii),
  19.53 (ii), 19.56 (iii), 19.76 (ii), 8.105 (i), 36.111 (i), 20.31 (i), 56.2 (i) and (ii), 36.106 (i), 38.62 (i) and
  (ii), 38.64 (i) and (ii), 38.83 (i) and (ii).
- **Audit questions added:** none.
- **Audit questions no longer quarantined:** none.
- **§10 rows a record says leave, not named by row:** none; no record of this stretch says a row leaves §10.
- **The decided-against search (§4 item 4)**, over each record whole, line breaks joined, case not matched, for
  *"decided against"*, *"decides against"* and *"decide against"*: the display record **0**; the span-kinds record
  **0**; the architecture-rules record **0**; the literature-facts record **0**.

## 5. The check before the commit (§4 item 8)

**Against the stretch 6 commit** (`git diff 4ab7231b… -- ratification_surfaces/cowork_comparison_l3_reading.md`,
written to the session scratchpad as `l3_session16_task3_diff.txt` and read with the file tools): 49 changed passages.

| Passage (new-file line) | What it is | Attribution |
|---|---|---|
| 54 | the in-progress line, one line replaced: *§L.24* → *§L.28*, *§L.25 to* → *§L.29 to* | session 16's instruction, §3.5 item 3 |
| 2170 | Row 4.2's line and its blank line | §3.2, §L.25 part A |
| 2185 | Row 4.3 | §3.2, §L.25 part A |
| 3332, 3334 | Row 7.5 (i) and (ii) | §3.2, §L.25 part B |
| 3349 | Row 7.6 | §3.2, §L.25 part B |
| 3645 | Row 7.24 | §3.2, §L.25 part B |
| 4233 | Row 7.59 | §3.2, §L.25 part B |
| 6980 | Row 7.226 (ii) | §3.2, §L.25 part B |
| 6997 | Row 7.227 | §3.2, §L.25 part B |
| 7014 | Row 7.228 | §3.2, §L.25 part B |
| 7696 | Row 7.274 | §3.2, §L.25 part B |
| 7998 | Row 7.294 (i) | §3.2, §L.25 part B |
| 8535 | Row 7.329 (ii) | §3.2, §L.25 part A |
| 8551 | Row 7.330 | §3.2, §L.25 part A |
| 9953 | Row 8.54 | §3.2, §L.25 part C |
| 10845 | Row 8.105 (i) | §3.2, §L.27 part F |
| 22327 | Row 15.42 (iii) | §3.2, §L.25 part A |
| 24361 | Row 19.1 | §3.2, §L.25 part A |
| 24391 | Row 19.3 (ii) | §3.2, §L.25 part A |
| 24406 | Row 19.4 | §3.2, §L.25 part D |
| 24422 | Row 19.5 | §3.2, §L.25 part D |
| 24437 | Row 19.6 | §3.2, §L.25 part D |
| 24468 | Row 19.8 | §3.2, §L.25 part D |
| 24821, 24823 | Row 19.29 (i) and (ii) | §3.2, §L.27 part A |
| 24905 | Row 19.33 | §3.2, §L.27 part B |
| 24989 | Row 19.37 | §3.2, §L.26 part A |
| 25081 | Row 19.40 | §3.2, §L.26 part A |
| 25294 | Row 19.53 (ii) | §3.2, §L.27 part A |
| 25347 | Row 19.56 (iii) | §3.2, §L.27 part C |
| 25683 | Row 19.76 (ii) | §3.2, §L.27 part C |
| 25700 | Row 19.77 | §3.2, §L.27 part C |
| 25715 | Row 19.78 | §3.2, §L.27 part C |
| 25774 | Row 19.82 | §3.2, §L.27 part C |
| 26338 | Row 20.7 | §3.2, §L.27 part D |
| 26725 | Row 20.31 (i) | §3.2, §L.28 |
| 30823 | Row 21.191 | §3.2, §L.25 part A |
| 31029 | Row 21.205 | §3.2, §L.25 part A |
| 42748 | Row 36.106 (i) | §3.2, §L.28 (narrower wording) |
| 42848 | Row 36.111 (i) | §3.2, §L.27 part F |
| 48196 | Row 38.47 | §3.2, §L.27 part E |
| 48213 | Row 38.48 | §3.2, §L.27 part E |
| 48460, 48462 | Row 38.62 (i) and (ii) | §3.2, §L.26 part A |
| 48478 | Row 38.63 | §3.2, §L.26 part B |
| 48497, 48499 | Row 38.64 (i) and (ii) | §3.2, §L.26 part A |
| 48828, 48830 | Row 38.83 (i) (part A) and (ii) (part C) | §3.2, §L.26 parts A and C |
| 48845 | Row 38.84 | §3.2, §L.26 part A |
| 72040, 72042 | Row 56.2 (i) and (ii) | §3.2, §L.28 |
| 74412 | Row 57.119 | §3.2, §L.25 part A |
| 75549 | Row 57.354 | §3.2, §L.26 part C |

Every changed passage is one of the kinds §4 item 8 admits; no other kind occurs; the one deleted line is the former
in-progress line.

- `git diff --numstat 4ab7231b3091933d087f50b089cb361f7fecd22a -- …`: **109 added, 1 deleted** (expected 109 and 1:
  no line was STOP-and-report and no NOT QUARANTINED line was found owed).
- `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- …`: **981 added, 4 deleted** (expected 981 and 4).
- Counts with the Grep tool after the edit: `*RULED DISPOSITION (` **408**; `*RECORDED DISPOSITION (` **53**;
  `*RULED PLACEMENT (` **3**; `*LEAVES L3 (` **26**; `*Row 7.67 is not transferred` **1**; `*NOT QUARANTINED (` **1**;
  `cowork_rulings_2026_11_04_l3_display_sitting` **25**; `cowork_rulings_2026_11_04_l3_span_kinds_sitting` **11**;
  `cowork_rulings_2026_11_04_l3_architecture_rules_sitting` **14**;
  `cowork_rulings_2026_11_04_l3_literature_facts_sitting` **4**. Every count as expected.

## 6. Row-parts this stretch gives no line, and why

- **§L.25 (the display record):** the seventeen traveling row-parts. Fourteen of them — 8.17, 8.29, 8.46, 8.63 (ii),
  8.74, 8.79 (i), 8.53, 8.76, 8.82, 8.117, 8.145, 7.69, 7.70 (ii) and 7.303 — under Ruling 13 of
  `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`, in §L.25 *Open* point
  (3)'s words: *"no line from this record … each keeps its proposed **ADOPTED — proposed**, as a proposal, the proposed
  paragraph untouched, and is not counted in the ruled distribution"*; they have no listing of their own here. Rows
  8.48 (i), 8.89 and 8.91 are §L.53's. Item 13's remaining cuts are §L.26 to §L.28 themselves.
- **§L.26 (the span-kinds record):** Row 19.39 (ii) (*"UNPLACED, tier item 14's"*; its line is §L.48's); Row 19.38
  (*"keeps its own placements"*); item 13's remaining cuts; the traveling row-parts.
- **§L.27 (the architecture-rules record):** Rows 8.105 (ii) and 36.111 (ii) (each already carrying an earlier
  stretch's line, §3 above); item 13's last cut (§L.28); Row 19.39 (ii); the traveling row-parts.
- **§L.28 (the literature-facts record):** Rows 8.105 (ii), 36.111 (ii) and 19.39 (ii); the traveling row-parts.
- **The other claims of the split rows** get nothing from this stretch: Row 7.226 (i), Row 7.294 (ii) to (v), Row 7.329
  (i), Row 8.105 (ii), Row 15.42 (i) and (ii), Row 19.3 (i), Row 19.53 (i) and (iii), Row 19.56 (i) and (ii), Row 19.76
  (i), Row 20.31 (ii), Row 36.106 (ii) and (iii), Row 36.111 (ii).

## 7. Departures, declared

1. **The pin was taken after the read**, by the declared-departure route of the standing clause (P-2): the instruction
   was read first, as the user's opening line orders, then pinned with `git hash-object -w` immediately before
   staging act 1; its blob `60c25745…` equals the identity recorded at check 3, so it was unmoved.
2. **The §10 and §11 searches and the quotation comparison were made by two read-only scripts** in the session
   scratchpad (`sec10_11_search.py`, `quote_check.py`), run with `python -I` and the repository paths passed as
   arguments, their output written to the scratchpad and read with the file tools — not with the Grep tool the
   instruction names for §10 and §11. The scripts locate §10 and §11 by their headings, use the bare-number rule with
   look-around, and compare with line breaks joined and asterisks removed, as the instruction states. The same
   quotation script ran the decided-against search.
3. **The gating answer** was located with the Grep tool and read with the Read tool at lines 180–439 of
   `tools/audit/nongating_apparatus_rows.json`: the `gating_ids` list (lines 186–409) and about 35 lines either side of
   it (the counts above it and the opening of the next field below). Nothing in those lines was used.
4. **`DECISIONS.md`** was read whole in ranges of 150 lines, save the last, of 174 lines.
5. **Read-only git commands beyond those the instruction names:** `git diff --cached --name-status` before each
   commit, `git rev-parse HEAD` after each commit, and `git ls-tree` and `git hash-object` on the reading file after act
   2's commit.
6. **The reading file was edited with the Edit tool, several edits per turn.** Every edit inserted text only, anchored
   on the next row's unique heading or on the paragraph that follows the insertion point; the diff above is the proof
   that nothing else moved.
7. Git printed its line-ending notice (`LF will be replaced by CRLF`) on each path it touched. The committed blobs are
   the line-feed identities the checks name; no byte of any file was changed by it.

## 8. The self-check after the work (`CLAUDE.md`, its last section), over the diff

Re-read the actual diff (`l3_session16_task3_diff.txt`) against the guiding principles, the conventions, the gate
policies and `DEFECT_TYPES.md`:

- **#6, #12:** no proposed paragraph and no existing line edited; every former text stands; the only replaced line is
  the in-progress line the instruction orders replaced, its former text recoverable at the stretch 6 commit.
- **#10, #14:** documentation only, no behavior change; nothing ruled, weighed or recommended.
- **#17(f), D-431:** every count in this report is the output of a command named beside it.
- **Reserved words:** the added lines are the records' words placed under form (b). This report's own prose uses
  *part* only as the name the records and the dispatch already give their lettered sections, and no other collided
  word in a non-musical sense.
- **The file-tools rule:** working-tree content was read with the file tools; the shell ran git object queries, the
  sanctioned `changed_paths.py`, and two scratchpad scripts reading files passed as arguments (declared above).
- **`DEFECT_TYPES.md`:** DT-11 (hand-transcribed figure) — none; DT-12 (stale anchor) — the line numbers above are of
  blob `7103b87c…` and are stated as such; DT-26 (scope-assumed enumeration) — the §10 and §11 searches covered the
  whole of each section, located by heading, and the row-heading search covered the whole file.

No violation found.

Session 16 of the L3 application ends here. Stretch 8 of Task 3 is not begun. Nothing else was done.
