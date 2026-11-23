# CC dispatch — the L3 application, SESSION 15 of several: Task 3 of the L3 application dispatch, sixth stretch (§L.24 alone), and nothing else

> **STATUS: WRITTEN 2026-11-23, CHECKED AS A TURN OF ITS OWN AND CORRECTED 2026-11-23 (the same sitting; see the
> provenance), NOT YET RELEASED,** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seven.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn; *"Task 3 in stretches"*, *"one commit per
> stretch, each stopping at an entry boundary"*). Executed by Claude Code when the user hands it over (D-252); the Cowork
> writing side never runs it. **If any expected result does not appear, stop at that step and report it. Do not
> continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 9 executed Task 2 (commit `4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774`,
called **the Task 2 commit** below). Sessions 10 to 13 applied Task 3's first four stretches, §L.1 to §L.22. Session 14
applied the fifth stretch, §L.23, in commit `b897b16ccac7db11954a3e187a3cb4acc361d39e` (called **the stretch 5 commit**
below), and committed its report as `90cddaf575ac83ec444bb637050726eab34a24c2`, the current tip.

**This is session 15. It executes the big dispatch's Task 3 — the reading file
`ratification_surfaces/cowork_comparison_l3_reading.md` — for ONE ledger entry only: §L.24, the L3 fit-and-rest record
(`records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md`). It commits and pushes that sixth
stretch, writes its report, and STOPS.** §L.25 is a later session's.

**What this stretch writes, in one paragraph.** **ONE line**, opening `*RULED DISPOSITION (`, naming
`cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1`, on **Row 37.18**, placing it **HISTORICAL** (§3.2
gives it whole); and the in-progress line brought forward from §L.23 to §L.24 (§3.5). **Nothing at §10 and nothing at
§11** (§3.3 and §3.4 say why). The record's other 76 row-parts get no line: their proposals stand (§3.2, last paragraph).

**The big dispatch stays the authority for every order it gives.** This file replaces or adds to only the orders listed
in §4, and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list,
STOP and report; do not choose. **Where this file's text of a line and the record's own words differ, the record
governs**: STOP-and-report for that line (the big dispatch's *Findings in this batch*).

**Documentation only. No algorithm change.** This session copies into the reading file the disposition the record
already places; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `90cddaf575ac83ec444bb637050726eab34a24c2`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_15_task_3_stretch_6_2026_11_23.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The reading file is as the stretch 5 commit left it.**
   `git diff --quiet b897b16ccac7db11954a3e187a3cb4acc361d39e -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   must give exit 0. Then `git ls-tree 90cddaf575ac83ec444bb637050726eab34a24c2 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
   and `git hash-object ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"` must both show
   `39a8a4b3ba86179b205ff2a73d9e709c88821733`. Then, with the **Grep tool** counting matching lines in that file:
   `\*RULED DISPOSITION \(` must count **353**; `\*RULED PLACEMENT \(` must count **3**; `\*RECORDED DISPOSITION \(`
   must count **53**; `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**;
   `\*NOT QUARANTINED \(` must count **1**; and `cowork_rulings_2026_11_04_l3_fit_and_rest_sitting` must count **0**.
   Any other result: STOP and report, the file not touched. (The writing side's staged copy: 5,260,516 bytes, 84,310
   lines, line feeds only.)
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command, and do not put a repository path inside a `python -c` string (the guard refuses it).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 90cddaf575ac83ec444bb637050726eab34a24c2 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the three files §5 act 1 lands (this instruction and handoff entries 1206 and 1207),
     plus the paths sessions 2 to 14 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
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
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seven.md` (written by the sitting that
   verified session 14; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_six.md` (the one before it; untracked, §5
   act 1 lands it).
5. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
6. **`DEFECT_TYPES.md` whole**, for the self-check after the work.
7. **The record this stretch rests on, WHOLE** — it is the authority for the line this session writes (**the record's
   own words govern**, the big dispatch, §L's opening):
   `records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md` (§L.24; 6,293 bytes, 86 lines).
   **Do NOT read the records of §L.1 to §L.23 or of §L.25 to §L.55, and do not open the record's three cut surfaces**
   (the record quotes what it rests on, and §L.24 lists the relocated rows by row).
8. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger, **the forms — form (b) is the form this stretch's line is written in**,
     the premise ledger, the declared start state, the standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 2516–2617 (§L.24, your stretch)**;
   - lines 6616–6820 (Task 3, whole);
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–2515 (§L.1 to §L.23, applied); lines 2618–5906 (§L.25 to
   §L.55); lines 5907–6615 (Tasks 0 to 2, executed and checked); lines 6821–7110 (Tasks 4 and 5); lines 7136 to the
   end. Nor the derivation, the successor, `FRAMEWORK.md` or `cowork_derived_specification_l0_l1_2026_09_03.md`.
9. **The reading file `ratification_surfaces/cowork_comparison_l3_reading.md`, only where this stretch needs it**, with
   the Read tool by offset and the Grep tool (never with a shell text tool on the working-tree file):
   - lines 1–60 (the title, the banner, the in-progress line at line 54, §0's heading);
   - lines 368–434 (§5, the closed vocabulary);
   - **Row 37.18, whole, at §6** (lines 435–79286): find it with the Grep tool, pattern `^\*\*Row 37\.18 —`, which must
     match **exactly once** in the file; read from that heading to the row's closing `---` (the writing side read it at
     lines 44268–44285);
   - §10 (lines 79745–80831) and §11 (lines 80832–82984), each searched with the Grep tool for `37\.18` (§3.3, §3.4);
   - §10, by search, at the 50 relocated row-parts §L.24's table names, for the report (§6 item 4).

## 3. What this stretch writes

### 3.1 The rules the line follows

1. **The form.** Form (b) of the big dispatch: one line ADDED to the row, the row's `*PROPOSED DISPOSITION.*`
   paragraph and every other sentence of the row untouched. The line names
   `cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1` as its record and ruling, the record file written
   as its bare file name, as sessions 10 to 14 wrote theirs. Row 37.18 is not split into claims, so the line names none.
2. **Where the line goes.** Form (b) places a ruled line *"immediately beneath a row's `*PROPOSED DISPOSITION.*`
   paragraph"* (the big dispatch's words section, *A ruled line*): **one blank line after the proposed paragraph, after
   any earlier ruled or recorded line standing there, and above any paragraph that follows them** (such as *"The
   decisions register at this row."* or *"At the source now."*). Read the row's actual shape from its proposed paragraph
   to its end before writing. **The writing side read Row 37.18 at the staged copy:** its `*PROPOSED DISPOSITION.*`
   paragraph (two lines, opening `*PROPOSED DISPOSITION.* **UNPLACED** — a rule on L3's own subject`), then one blank
   line, then the row's closing `---`; no earlier `*RULED …` or `*RECORDED …` line and no other paragraph after the
   proposed one. So the row ends, after the edit: proposed paragraph, blank line, **the new line**, blank line, `---`.
   If you find a different shape at the row (an earlier line, a further paragraph, or an ending other than `---`), state
   it in the report and place the line by the rule in bold above; if the rule does not settle where it goes, the line
   is a STOP-and-report.
3. **The quotation.** The line quotes the record's words that §3.2 gives. **The writing side checked them against the
   record by a read-only script (words and punctuation, line breaks read as spaces, asterisks not compared): found, in
   the record's §1, *The rows, as ratified with them*, item 1 (record lines 47–48).** Before writing the line, find the
   quoted passage in the record yourself and compare it the same way: every word and every punctuation mark must match,
   line breaks read as spaces. The line keeps its marks exactly as §3.2 gives them. A difference is a STOP-and-report
   for the line: no line written, listed in the report under *rows the act could not place* with both texts.
4. **The row is checked first** (Task 3 (b)): the row's heading matches exactly once; the derived statement that speaks
   to it is **L3-S42**, at **DIFFERS**; and **the row's outgoing statement fits what the record says of it** (the record:
   the old rule that the harmonic-grouping unit is always the punctuation-span and never "phrase"; the row's outgoing
   statement: *"The harmonic-grouping unit is always the **punctuation-span** … never "phrase"."*). A row that does not fit
   is a STOP-and-report: no line, listed under *rows the act could not place* with what was read.
5. **Not *as proposed*.** The row is proposed **UNPLACED** and the record places it **HISTORICAL**, so the line does not
   say *as proposed* (form (b)'s paragraph *Which ADOPTED word, and when as proposed is written*: *"Otherwise as
   proposed is not written, and the placement is given in the record's words"*). If you find the row proposed
   HISTORICAL, the line is a STOP-and-report.
6. **No other record's line on this row.** The writing side found none at the row (§3.1 item 2), and §L.24's writer saw
   none in §L.1 to §L.23, comparing row numbers only (§L.24, *Rows named by more than one record*). If you find one, apply form (b)'s two-record rule by part as the big dispatch gives it, and list
   the row under *rows named by more than one record*; if an earlier stretch's line would have to be deleted or edited,
   STOP, do not commit, and report.

### 3.2 The line, with its exact text

**Row 37.18 — 1 line, HISTORICAL** (§L.24's table; the record's §1, *The rows, as ratified with them*, item 1):
```
*RULED DISPOSITION (cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1).* **HISTORICAL** — "the old rule that the harmonic-grouping unit is always the punctuation-span and never "phrase" is replaced by the charter's L3 block and L3-S42".
```

**The count.** `*RULED DISPOSITION (`: **1**, HISTORICAL. None opens `*RECORDED DISPOSITION (` or `*RULED PLACEMENT (`.

*The settlement in §3.2, the writing side's and overrulable by the user:* the quotation is §L.24's table's quotation,
which stops at *"L3-S42"*, where the record's sentence goes on (*"which keep the two senses apart by two names …"*); the
line quotes what §L.24 quotes and no more, and the inner *"phrase"* keeps the record's straight double quotation marks.

**The record's other row-parts get no line from this stretch** (§L.24's table, second line; Task 3 (a)): the 76
agreeing row-parts, *"their proposals stand, not re-marked (the boundaries precedent)"* — L3-S41's 3, L3-S14's 32 and
L3-S42's 41. Of them, the 50 proposed RELOCATED are listed by row in §L.24's table, each staying on §10 under its
destination (the writing side found each of the 50 under that destination's heading at the staged copy); the other 26
(L3-S14's 15 and L3-S42's 11, ADOPTED — carried) are named by count only, as the record names them. **Nor do the claims
the record mentions and does not place** (§L.24, *Claims the record mentions and does not place*; the record names none
of them by row).

### 3.3 The transfer list, §10 (Task 3 (c) items 5 and 6) — nothing written

- **Item 5:** Row 37.18 is placed HISTORICAL, not RELOCATED, so nothing is appended to §10.
- **Item 6:** *"no *LEAVES L3* line is written on account of §L.24, and no §10 entry holding one of the row-parts it
  names is edited"* (item 6's own words, under the release list's item (xlvii)). Row 37.18 stands in no §10 entry: the
  writing side's search of §10 for `37.18` as a bare number with look-around found no hit, and no range in §10 (*"n to
  m"*) covers it. Run the same search with the Grep tool; if you find Row 37.18 in a §10 entry, STOP and report before
  writing anything there.

### 3.4 The audit questions, §11 (Task 3 (c) item 7) — nothing written

- **(a):** this stretch places nothing QUARANTINED, so no entry is added.
- **(b):** §11 carries no entry for Row 37.18 (the writing side's search of §11 for `37.18` found no hit), so no NOT
  QUARANTINED line is written. Run the same search with the Grep tool; if you find an entry for Row 37.18, add the NOT
  QUARANTINED line item 7 (b) gives beneath it, at its indentation, and report it.

### 3.5 The file's own statements of its state

1. **The four state sentences** were written by session 10 and are not touched.
2. **Not written in this stretch: the sentence beneath §13's heading, and §13a** (session 10's instruction §3.5 item 2,
   unchanged).
3. **The in-progress line (line 54) is replaced, in place, by this text, exactly:**

   `*Application in progress: the RULED DISPOSITION, RULED PLACEMENT and RECORDED DISPOSITION lines in this file are those of §L.1 to §L.24 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.25 to §L.55 are applied by later Claude Code sessions, one stretch each, and the ruled distribution (§13a) is written by the last of them, which removes this line.*`

   Its former text is not preserved in the file and stays recoverable at the stretch 5 commit, as in sessions 11 to 14.
   Attribute it in the diff table to *"session 15's instruction, §3.5 item 3"*.

## 4. The orders of the big dispatch this session replaces or adds to — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 3 applies** (Task 3 (b): *"§L.1 to §L.55, in ledger order, are the list"*) → **§L.24
   only**, after sessions 10 to 14's §L.1 to §L.23. §L.25 to §L.55 are not applied, read or touched.
3. **A1, for two paths only.** A1 says a further untracked `cowork_handoff_entry_*.md` is not landed. **Handoff entries
   1206 and 1207 ARE landed**, with this file, in §5 act 1, as sessions 8 to 14 landed theirs. Any other untracked
   handoff entry or ruling record stays as A1 says.
4. **Task 3 (c), split by stretch.** Item 1 (the decided-against search) is run over the one record §L.24 enters
   (*"decided against"*, *"decides against"*, *"decide against"*, line breaks joined, case not matched). §L.24 says none
   occurs; the writing side's search found none. List the result in the report. Item 2: not reached. Item 3: not
   reached. Item 4: not reached. Item 5: nothing to append (§3.3). Item 6: nothing written (§3.3). Item 7: nothing
   written (§3.4).
5. **Task 3 (d), split by stretch** → §3.5 items 1 and 2.
6. **Changed line, not in the big dispatch: the in-progress line of §3.5 item 3.** Task 3 (f) admits it for this
   stretch as a changed passage of its own kind. Its former text is the one deleted line this stretch's diff against the
   stretch 5 commit may show.
7. **Task 3 (e), one commit for the whole of Task 3** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry, and this stretch is one entry: if signs of context degradation appear before the line is applied, do
   not commit; STOP and report what was applied to the uncommitted copy and that it is not landed.
8. **Task 3 (f), the check before the commit**, is run twice:
   - **Against the stretch 5 commit:**
     `git diff b897b16ccac7db11954a3e187a3cb4acc361d39e -- ratification_surfaces/cowork_comparison_l3_reading.md > "<your scratchpad>/l3_session15_task3_diff.txt"; echo "exit:$?"`,
     read with the Read tool, every changed passage attributed in a table in the report. **The kinds admitted:** the
     line of §3.2 with the blank line after it; the in-progress line of §3.5 item 3; and a NOT QUARANTINED line only if
     §3.4 (b) found an entry. Then
     `git diff --numstat b897b16ccac7db11954a3e187a3cb4acc361d39e -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 3 added lines and 1 deleted line** (the line and its blank line, 2; the in-progress line, a
     replaced line, one added and one deleted), or 1 added and 1 deleted if the line of §3.2 was STOP-and-report, plus 1
     added for a NOT QUARANTINED line §3.4 (b) found.
   - **Against the Task 2 commit:**
     `git diff --numstat 4b6dc3bd4bb71e5dc7bc62b6a251af4ae9630774 -- ratification_surfaces/cowork_comparison_l3_reading.md; echo "exit:$?"`
     must show **exactly 873 added lines and 4 deleted lines** (871 if the line of §3.2 was STOP-and-report), with the
     same adjustment as above. *The writing side's arithmetic: after session 14 the file stood at 871 added and 4 deleted
     against the Task 2 commit (session 14's report, and the verification of entry 1207 §2 item 3); this stretch adds
     2 lines. The in-progress line replaces a line that is itself an addition against the Task 2 commit, so it adds no
     line and deletes none there. The 4 deleted are the four lines session 10's state sentences were written into.*
   - Then, with the Grep tool counting matching lines: `\*RULED DISPOSITION \(` must count **354** (353 if the line was
     STOP-and-report); `\*RECORDED DISPOSITION \(` must count **53**; `\*RULED PLACEMENT \(` must count **3**;
     `\*LEAVES L3 \(` must count **26**; `\*Row 7\.67 is not transferred` must count **1**; `\*NOT QUARANTINED \(` must
     count **1**, or 2 if §3.4 (b) found an entry; and `cowork_rulings_2026_11_04_l3_fit_and_rest_sitting` must count
     **1** (0 if the line was STOP-and-report; 2 with a NOT QUARANTINED line).
   Any other count, or a changed passage of another kind: do not commit; STOP and report. The commit subject is exactly:

   `application L3, Task 3 stretch 6 (§L.24): Row 37.18 re-marked HISTORICAL in the reading file under the L3 fit-and-rest ratification, and the in-progress line brought forward, proposals elsewhere standing`

   Commit that ONE path alone. PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
9. **E3** is checked for this stretch only, as items 2 to 8 restrict it. The full E3 belongs to the session of the last
   stretch, or to a check session after it.
10. **The report** this stretch's results go to → **this session's own report,
    `records/cc/reports/cc_report_l3_application_session_15_task_3_stretch_6_2026_11_23.md`**, as sessions 2 to 14
    each wrote theirs. Task 5's report, when its session writes it, points at this one.
11. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin §L.25, Task 4 or
    any later Task.

## 5. The acts, in order

1. **Land the writing side's three files first, in a commit of their own, before any edit to the reading file.**
   Exactly three paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_15_task_3_stretch_6_2026_11_23.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_six.md`; and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_seven.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entries 1206 and 1207 and the session 15 instruction of the L3 application landed; Task 3 stretch 6 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 3 for this stretch**, as the big dispatch's Task 3 and §3 and §4 above give it: the row check of §3.1 item 4;
   the line of §3.2; the searches of §3.3 and §3.4; §3.5 item 3; then §4 item 8's checks, the commit and the push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_15_task_3_stretch_6_2026_11_23.md` with
   the items of §6. Commit that ONE path alone, subject exactly:
   `report: session 15 of the L3 application, Task 3 stretch 6 (§L.24) written; stretch 7 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging act 1.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The line of §3.2, written (with its reading-file line number after the edit) or STOP-and-report (and why); Row
   37.18's shape as read at the row (§3.1 item 2); the results of the §10 and §11 searches of §3.3 and §3.4.
4. The report headings Task 3 names, for this stretch's rows: *rows the act could not place* (none expected); *rows
   given no line now* (none expected); *recorded lines not written: no disposition word* (none expected); *rows named
   by more than one record* (none expected); *ADOPTED words read at the row* (none expected); *audit questions added*
   (none); *audit questions no longer quarantined* (none expected); *§10 rows a record says leave, not named by row*:
   the 50 relocated row-parts §L.24's table lists by row, each by row and destination, stating that the release list's
   item (xlvii) governs them, that no *LEAVES L3* line is written on their account and that no §10 entry holding one of
   them is edited (Task 3 (c) item 6) — and that each was found by the Grep tool in §10 under its destination's heading,
   or, for any not found there, which; the decided-against search (§4 item 4). *(Listing the 50 under that heading is
   the writing side's settlement, on the shape of session 14's report, which listed there the 16 AGREES row-parts its
   record kept; overrulable by the user.)*
5. The diff table of §4 item 8, every changed passage attributed, and the seven counts and two `--numstat` results.
6. **Row-parts this stretch gives no line, and why**, as a list of its own: the 76 agreeing row-parts (*"their
   proposals stand, not re-marked"*; L3-S41's 3 by row, the other 73 as §L.24's table names them — 47 by row, 26 by
   count only); and the claims the record mentions and does not place (named by the record by description only). *A
   heading of this session's report only, as in sessions 10 to 14's.*
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The self-check after the work (`CLAUDE.md`, its last section), over the diff.
9. The last sentence, exactly: *"Session 15 of the L3 application ends here. Stretch 7 of Task 3 is not begun. Nothing else was done."*

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 2);
- the big dispatch's Task 3, its forms, its standing bars or its findings rule makes something a STOP (the line of
  §3.2, if STOP-and-report under them or under §3.1 items 2 to 6, is reported and the rest of this stretch applied, as
  they say);
- a line an earlier stretch wrote would have to be deleted or edited (§3.1 item 6);
- Row 37.18 is found in a §10 entry (§3.3);
- §4 item 8's checks find a changed passage they cannot attribute, or a count other than the ones they give;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1207. Read at the objects for this file: the
three git reference files (both refs `90cddaf5…`); entries 1207, 1206 and 1026 whole; session 14's instruction whole;
session 14's report at its §1 and §2; the fit-and-rest record whole; the big dispatch at lines 118–125, 159–274,
2516–2617 and 6616–6820, its `##` headings, the `###` headings of §L.23 to §L.26, and the boundary lines of every
range §2 item 8 names; the release list
`ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md` at its item (xlvii) (lines 1740–1759). The
reading file, by read-only searches and scripts over the staged copy: its blob computed as git would
(`39a8a4b3…`, 84,310 lines, no carriage return); its `##` headings; Row 37.18 at lines 44268–44300; every line in the
file naming `37.18` as a bare number with look-around (the row's heading; two quoted notes at the head of member 37,
§6.37; member 37's distribution, its UNPLACED line and its DIFFERS sentence; a table row of member 57's first portion
naming Row 37.18 as a cross-reference; §7's DIFFERS entry; §12's proposal sentence; none in §10 or §11),
and §10 searched for ranges covering it (none); the in-progress line at line 54; the six counts (353 / 3 / 53 / 26 / 1 /
1) and the record's name (0). The record's quotation checked against the record by a read-only script (line breaks
joined): found. The record searched for the three decided-against phrases: none. Each of the 50 relocated row-parts of
§L.24's table found at §6 exactly once and in §10 under its named destination's heading. Relayed, not re-checked here:
the archive JSON's blob `1df4f207…` and the untracked paths (session 14's report, §1 item 5); the end of
`cowork_handoff.md`'s topmost block at line 255 and the line-180 start of `cowork_audit_protocol.md`'s dispatch-protocol
section (as session 14's instruction gives them); the 871 added and 4 deleted lines against the Task 2 commit (session
14's report, as verified by the sitting booted on entry 1206 and recorded in entry 1207 §2 item 3); the big dispatch's
blob `b5274c2c…` (entry 1207 and session 14's report).*

*The check, as a turn of its own: Cowork, 2026-11-23 (Stockholm), the same sitting, the file not yet handed to Claude
Code, so its corrections keep no former wording (as entry 1203 §2 item 4 did). Read at the objects: this file whole;
the big dispatch at the first and last line of every range §2 item 8 names and of the ranges it bars (lines 1, 37, 38,
58, 59, 97, 99, 394, 395, 430, 431, 2515, 2617, 2618, 5906, 5907, 6615, 6820, 6821, 7110, 7111, 7135, 7136; 7,157 lines
in all), and line 98's length (4,384 bytes with its line feed); the reading file at every `37.18` hit by its enclosing
heading. By read-only script over the staged copies: every full hash in this file one of the six objects it names; the
line of §3.2 written once and its quotation found in the record (asterisks not compared, line breaks joined); the
in-progress line of §3.5 equal to the current line 54 with *§L.23* and *§L.24 to* moved on by one. Corrected: §3.1 item
6, which said §L.24 *"found none"* where §L.24's writer says he saw none, comparing row numbers only; the provenance's
account of the `37.18` hits (one was called *"the L2 cross-reference table"*; it is a table row of member 57's first
portion) and of the big dispatch's headings read. No line, row, disposition word, count, command or commit subject
changed.*
