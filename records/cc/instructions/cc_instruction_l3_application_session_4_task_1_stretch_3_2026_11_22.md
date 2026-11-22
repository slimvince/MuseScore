# CC dispatch — the L3 application, SESSION 4 of several: Task 1 of the L3 application dispatch, third stretch (§L.26 to §L.33), and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_five.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Session 2 applied Task 1 for §L.1 to §L.15.
Session 3 applied Task 1 for §L.16 to §L.25: its commits are `85d4e678ffec05274b4593f1878d57cecda54651` (the writing
side's two files), `fbe355032fdca34c5f6246004c37ab30fc8581cd` (the successor, blob
`32cf8fdb7e942168a4ce153b3ccbcd8be081deca`) and `0b56da6ad42e6e0dd5b6ec41d15f87a299db7b65` (its report), all verified at
the objects by the Cowork sitting that wrote this file.

**This is session 4. It continues the big dispatch's Task 1 (the successor file
`cowork_derived_specification_l3_2026_11_08.md`) for the ledger entries §L.26 to §L.33 only, commits and pushes that
third stretch, writes its report, and STOPS.** Of these eight entries, only §L.26, §L.27 and §L.28 order text in the
successor (ten added statements). §L.29 to §L.33 each state *"no amendment"* for the successor; for them Task 1 writes
nothing, and their records are read so that this is confirmed at the record. Each later stretch gets its own
instruction, sized and written after the previous one is verified.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §3,
and only for this session. Where this file and the big dispatch seem to differ on anything §3 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change.** This session writes the successor file by the big dispatch's Task 1, which
places the ruling records' own words; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `0b56da6ad42e6e0dd5b6ec41d15f87a299db7b65`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_4_task_1_stretch_3_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The successor stands as session 3 committed it** (replaces the big dispatch's Task 1 *Before the edit* for this
   session). `git hash-object cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"` must print
   `32cf8fdb7e942168a4ce153b3ccbcd8be081deca`, and
   `git ls-tree 0b56da6ad42e6e0dd5b6ec41d15f87a299db7b65 -- cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"`
   must show the same blob. Anything else: STOP and report.
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command (session 3's first run was refused for that).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree 0b56da6ad42e6e0dd5b6ec41d15f87a299db7b65 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the two files §4 item 1 lands (this instruction and handoff entry 1186), plus the
     393 untracked paths sessions 2 and 3 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). `.claude/` and
     `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is expected and
     not a STOP. List in the report every untracked path the tool reports outside those. A further untracked
     `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a STOP (the
     big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **The eight ruling records §L.26 to §L.33 name, each WHOLE, in §L's order** (the file names are at the `### §L.n`
   headings of the big dispatch: the span-kinds, architecture-rules and literature-facts records of 2026-11-04, and the
   catalog key, catalog lead-rows, catalog recognition part 1, catalog recognition part 2 and catalog further-rows
   records of 2026-11-06). They are the authority for every amendment this session applies: **the record's own words
   govern** (the big dispatch, §L's opening). Do NOT read the records of §L.1 to §L.25 or of §L.34 to §L.55.
3. **Two surfaces WHOLE**, from which §L.26's and §L.27's added statements are copied (§3 item 3):
   `ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md` (21,940 bytes, the surface §L.26's record
   names) and `ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md` (26,148 bytes, the surface
   §L.27's record names). The literature-facts surface is not read: §L.28's statement is the record's own quoted text.
4. **The successor WHOLE, at the git object of session 3's Task 1 commit:**
   `git show fbe355032fdca34c5f6246004c37ab30fc8581cd:cowork_derived_specification_l3_2026_11_08.md`, written to a
   scratch path outside the repository and read there with the Read tool in ranges. It is 179,789 bytes, 1,670 lines,
   and has no line longer than 1,211 characters. The derivation is not read.
5. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
6. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard
   (its condition in `CLAUDE.md` is not met).
7. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 4 to 255 at this writing; the
   dispatch-protocol clause on the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_six.md` (the current entry point,
   written by the sitting that wrote this file; untracked, §4 item 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_five.md` (the one before it).
8. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
9. **`decisions/group_K.md`, D-674 whole** (from its heading `### D-674` to the next `###` heading): the filing
   convention Task 1 applies.
10. **The big dispatch, at these lines only, with the Read tool by line range:**
    - lines 1–37;
    - lines 59–97;
    - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
      `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
    - lines 99–394 (the words, the ruling ledger, **the forms — form (a) is the form every amendment is written in**, the
      premise ledger, the declared start state, the standing bars, the findings rule);
    - lines 395–430 (how §L is written);
    - **lines 2727–3542 (§L.26 to §L.33, your stretch)**;
    - lines 6100–6571 (Task 1, whole);
    - lines 7111–7135 (*What this batch does NOT do*).

    **Do not read in this session:** lines 38–58; lines 431–2726 (§L.1 to §L.25, already applied); lines 3543–6099
    (§L.34 to §L.55, and Task 0); lines 6572–7110 (Tasks 2 to 5); lines 7136 to the end. Nor the derivation, the reading
    file, `FRAMEWORK.md`, `cowork_derived_specification_l0_l1_2026_09_03.md`, `tools/audit/gen_status_batch_bound.py`
    or `records/cowork/handoff/cowork_away_returns.md`: each belongs to a later Task's session or is not needed here.

## 3. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 1 applies** (Task 1 (a): *"Each §L entry's Successor — amendments part is applied, in
   ledger order"*) → **§L.26 to §L.33 only, in ledger order.** §L.1 to §L.25 are applied already and are not touched;
   §L.34 to §L.55 are not applied, read or touched. **For §L.29 to §L.33**, the ledger entry states that the successor
   gets no amendment: confirm that against each record read whole and write nothing for it. If a record of §L.29 to
   §L.33 orders text in the successor after all, STOP and report for that entry; apply the rest. Their charter,
   interface-contract, reading-file and register parts belong to Tasks 2 to 4 and are not touched.
3. **Task 1 (c), split by stretch.** Apply here only the parts whose ordering record is one of §L.26 to §L.33:
   - (c) items 1, 2 and 4: applied by sessions 2 and 3; nothing here.
   - (c) item 3, the added statements: **§L.26's three (parts A, B and C), §L.27's six (parts A to F) and §L.28's one**,
     ten in all:
     - **§L.26 parts A, B, C and §L.27 parts A, B, C, D, F: under (c) item 3 (ii).** Each part as its surface (§2
       item 3) states it, quoted whole, from the part's heading there to the line before the next `## ` heading, located
       by that heading; with the record's *"In short"* bullet for the part quoted whole beneath it as a sub-item. Use the
       shape session 3 used for §L.25's parts: a one-line lead-in *Part X, as `<surface file>` states it after the
       check:*, the quotation, then `- *In short (<record file>, Ruling 1):*` and the bullet quoted beneath it.
     - **§L.27 part E: under (c) item 3 (i)**, as (c) item 3 itself says (Ruling 34 of the part 2 ruling record): the
       record's quoted sentence, quoted whole, with **no** sub-item beneath it. The surface's §6 is not quoted.
     - **§L.28's statement: under (c) item 3 (i)**: the record's quoted text, from *"As facts of the published
       literature, recorded with D-607's standing:"* through *"…and L3's phrase model rests on fitted terms instead."*,
       quoted whole, with no sub-item.
     - For each (i) statement, use the shape session 2 used for §L.13's key-areas statements: a one-line italic lead-in
       naming what is quoted (for example *Ruling 1, part E, as the record quotes it:*), then the quotation.
     - **Headings** (form (a)): `### Added — <record file>, Ruling 1, part <X>` for each lettered part, and
       `### Added — <record file>, Ruling 1` for §L.28's, which the record gives no part (§L.28 amendment 1).
     - **Place and order:** in the existing section `## Statements added by the L3 family rulings`, **after §L.25's
       part D statement and its *In short* sub-item**, and before the `---` line that closes the section, in this order:
       §L.26 A, B, C; §L.27 A, B, C, D, E, F; §L.28. No new section is created. §L.26 amendment 1 says §L.48's statement
       goes directly after §L.26 part C: **that is a later stretch's act; write nothing for §L.48 here.**
   - (c) item 5: unchanged; none of §L.26 to §L.33 orders text at OQ-L3-1 or OQ-L3-11 to OQ-L3-14 (if one does, (c)
     item 5 says what follows). (c) item 6: unchanged, for this stretch's entries.
   - The `## Notes — lists the records place here, not ruled` section (form (a), last bullet): created by this session
     only if one of §L.26 to §L.33 places a list there; otherwise not created. If created, it goes after the section of
     added statements and before the `## 5.` heading.
   If you find that a part assigned to this session depends on the words of a record outside §L.26 to §L.33 (other than
   the two surfaces of §2 item 3), or a part not assigned here is ordered by a record inside it: STOP and report for that
   part; apply the rest.
4. **Task 1 (a) and (b) are not re-applied.** The file exists (§1 check 4); it is edited in place by targeted edits only,
   never re-typed and never re-made from the derivation. Two lines written by earlier sessions are looked at:
   - **The banner's ANSWERED set**, the parenthesis in the sentence *"The open questions of §4 stand with their ANSWERED
     marks where a ruling answered them (…)"*, is re-taken at the file after this stretch's edits. The writing side's
     expectation: **unchanged — OQ-L3-2, OQ-L3-3, OQ-L3-4, OQ-L3-5, OQ-L3-6, OQ-L3-7, OQ-L3-8 and OQ-L3-10, eight**, as
     no entry of this stretch answers an open question. If the file then carries a different set, write that set and
     report the difference. Nothing else in the banner is touched.
   - **The in-progress line beneath the banner** becomes exactly:

     `*Application in progress: this file carries the amendments of §L.1 to §L.33 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.34 to §L.55 are applied by later Claude Code sessions, one stretch each (was: "§L.16 to §L.55"; staleness fix shown, records/cc/instructions/cc_instruction_l3_application_session_4_task_1_stretch_3_2026_11_22.md, §3 item 4); the banner above is true of the file only when the last of them removes this line.*`

     Two ranges change: `§L.1 to §L.25` becomes `§L.1 to §L.33`, which is the ordinary advance; and `§L.16 to §L.55`
     becomes `§L.34 to §L.55`, with its mark. That second range is a staleness fix under the user's rule of 2026-09-22:
     after session 3 the line said the file carries §L.1 to §L.25 and, in its next sentence, that §L.16 to §L.55 are
     still to be applied. The fault is the writing side's own: session 3's instruction ordered that nothing else in the
     line change. Attribute both changes in the diff table to *"session 4's instruction, §3 item 4"*.
5. **Task 1 (d), one commit for the whole of Task 1** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, commit the
   entries already applied, write in the in-progress line the last entry actually applied instead of §L.33 (and the
   entry after it instead of §L.34), set the banner's ANSWERED set to what the file carries, and report which entries
   were applied. If you are inside an entry, do not commit; STOP and report which entries were applied to the
   uncommitted file and that it is not landed.
6. **Task 1 (e), the check before the commit,** is run with these changes for this stretch:
   - **The method:** store the edited successor with `git hash-object -w cowork_derived_specification_l3_2026_11_08.md`
     and diff the two blobs, `git diff -U0 32cf8fdb7e942168a4ce153b3ccbcd8be081deca <the new blob>`, written to a
     scratch file outside the repository and read with the file tools. The base is session 3's successor, not the
     derivation object.
   - **The attributions available:** only §L.26, §L.27 and §L.28, amendment 1 each, with (c) item 3 (i) or (ii) as §3
     item 3 assigns it; and §3 item 4's in-progress line (and the banner, only if the ANSWERED set differed). A changed
     passage none of those accounts for is a STOP-and-report and the file is not committed until it is removed.
   - **Lines removed or replaced:** none, except the in-progress line (and the banner line, only as above). Everything
     else is added lines, all inside the section of added statements, after §L.25's part D *In short* sub-item and before
     the `---` that closes the section.
   - **Bold text:** no derived statement's bold text changes in this stretch. Bold inside the new quotations is the
     sources' own and is checked as part of the quotation.
   - **Every statement, open question and passage that earlier sessions wrote is byte-identical to blob `32cf8fdb…`**,
     except the line(s) of §3 item 4. L3-S1 to L3-S42 and OQ-L3-1 to OQ-L3-14 are each present exactly once.
   - **Each quotation is checked at its source:** each (ii) part equals its surface section line for line, each
     *In short* sub-item equals the record's bullet, and each (i) statement occurs in its record, whitespace normalized.
   - **Headings:** when counting headings of the successor, count only lines that begin with `#`. The quoted surface
     sections carry their own headings as lines beginning `> ## ` (session 3's parts carry `> ## 2.` to `> ## 5.`, and
     this stretch adds more); those are inside quotations and are not headings of the successor.

   The commit subject is exactly:

   `application L3, Task 1 stretch 3 (§L.26 to §L.33): the derived specification as amended by eight more L3 family ruling records, every amendment citing its record, not ratified`

   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
7. **E1** is checked for this stretch only, as items 3 to 6 restrict it. The full E1 belongs to the session of the last
   stretch.
8. **Where the batch ends for this session.** After §4's acts, this session STOPS. It does not begin §L.34, Task 2 or
   any later Task.

## 4. The acts, in order

1. **Land the writing side's two files first, in a commit of their own.** Exactly two paths, both expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_4_task_1_stretch_3_2026_11_22.md`, and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_six.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entry 1186 and the session 4 instruction of the L3 application landed; Task 1 stretch 3 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 1 for §L.26 to §L.33**, as the big dispatch's Task 1 and §3 above give it, ending with §3 item 6's check, its
   commit and its push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_4_task_1_stretch_3_2026_11_22.md` with the
   items of §5. Commit that ONE path alone, subject exactly:
   `report: session 4 of the L3 application, Task 1 stretch 3 (§L.26 to §L.33) written; stretch 4 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 5. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.26 to §L.33, in order: every amendment by its number, applied (and where), or STOP-and-report (and
   why); for §L.29 to §L.33, that the record was read whole and orders no successor text (or the STOP). The same for
   each part of (c) §3 item 3 assigns here, and for §3 item 4.
4. The ANSWERED set the file carries, set against §3 item 4's eight.
5. The diff table of §3 item 6, every changed passage attributed.
6. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
7. The last sentence, exactly: *"Session 4 of the L3 application ends here. Stretch 4 of Task 1 is not begun. Nothing else was done."*

## 6. What the earlier sessions established, for the record (relayed here; verified by the Cowork sittings at the objects)

Session 1 committed Task 0 as `cbde76fd78a244540df64895191a511df186cc29` and stopped at Task 0's guard-set check: two
tools failing beyond the thirteen of the declared start state, item 2 (`gen_evidence_pin_membership.py`, which counts
the ruling records on disk, and `gen_per_session_reading.py`, which finds handoff entries through git). Session 2 applied
§L.1 to §L.15 and held one amendment as STOP-and-report, §L.15 amendment 4, as that entry's own settled note orders.
Session 3 applied §L.16 to §L.25 with no STOP. **This session runs no guard**, so neither red bears on its acts; both
are declared here so that no later reader takes them for this session's doing.

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 5);
- the big dispatch's Task 1, its forms, its standing bars or its findings rule makes something a STOP (an amendment
  that is STOP-and-report under them is reported and the rest applied, as they say);
- §3 item 6's check finds a changed passage it cannot attribute;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §3 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1185. Read at the objects for this file: the
three git reference files; the commits `85d4e678…`, `fbe35503…` and `0b56da6a…` and their trees against their parents',
folder by folder; the successor at blobs `e5c7ef48…` and `32cf8fdb…` (their diff passage by passage, the quotations
against the records and the display surface, the marks against the big dispatch, the counts, the line lengths, the
added-statements section and the in-progress line); session 3's instruction and report whole; the big dispatch (blob
computed from the staged bytes) at its `### §L.` headings, form (a) at lines 178–200, §L.26 to §L.28's successor
amendments, §L.29 to §L.55's *Successor* lines, §L.29's *Open* notes, and Task 1 (c) items 2 to 6; the sizes of the
ledger entries §L.26 to §L.55, of their records and of the surfaces; the section headings of the span-kinds and
architecture-rules surfaces and the *In short* bullets of the three 2026-11-04 records; `records/cowork/handoff/cowork_handoff.md`
at its size and time stamp only (2026-09-17, older than session 3's instruction; the range "lines 4 to 255" is carried
from that instruction, not re-read). The user's words: the opening instruction with Claude Code's
closing message; "shortened"; "continue".*
