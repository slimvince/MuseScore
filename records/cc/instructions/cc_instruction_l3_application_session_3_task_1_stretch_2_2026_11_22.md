# CC dispatch — the L3 application, SESSION 3 of several: Task 1 of the L3 application dispatch, second stretch (§L.16 to §L.25), and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_four.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Session 2 executed Task 1 for §L.1 to §L.15: its
commits are `95286f787d8b1a54ddcadd63ecdff84467497157` (the writing side's two files),
`9987d3c91ad80a59743759dc24e6b87ed098c5c7` (the successor, blob `e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1`) and
`cda8d48206f2b4d3e7bea168ed6a0f9ad7bc69c2` (its report), all verified at the objects by the Cowork sitting that wrote
this file.

**This is session 3. It continues the big dispatch's Task 1 (the successor file
`cowork_derived_specification_l3_2026_11_08.md`) for the ledger entries §L.16 to §L.25 only, commits and pushes that
second stretch, writes its report, and STOPS.** The stretches are no longer four. Entry 1184 had sized them at four, and
the Cowork sitting that wrote this file re-sized them at the objects. Two things had not been counted: the successor
this session reads is larger than the derivation, and §L.25 to §L.27's added statements are copied from surface files
that must be read too. So the second stretch ends at §L.25. Each later stretch gets its own instruction, sized and
written after the previous one is verified.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §3,
and only for this session. Where this file and the big dispatch seem to differ on anything §3 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change.** This session writes the successor file by the big dispatch's Task 1, which
places the ruling records' own words; it decides nothing.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `cda8d48206f2b4d3e7bea168ed6a0f9ad7bc69c2`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_3_task_1_stretch_2_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The successor stands as session 2 committed it** (replaces the big dispatch's Task 1 *Before the edit* for this
   session). `git hash-object cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"` must print
   `e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1`, and
   `git ls-tree cda8d48206f2b4d3e7bea168ed6a0f9ad7bc69c2 -- cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"`
   must show the same blob. Anything else: STOP and report.
5. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`).
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree cda8d48206f2b4d3e7bea168ed6a0f9ad7bc69c2 -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the two files §4 item 1 lands (this instruction and handoff entry 1185), plus the
     393 untracked paths session 2 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). `.claude/` and
     `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is expected and
     not a STOP. List in the report every untracked path the tool reports outside those. A further untracked
     `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a STOP (the
     big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **The ten ruling records §L.16 to §L.25 name, each WHOLE, in §L's order** (the file names are at the `### §L.n`
   headings of the big dispatch). They are the authority for every amendment this session applies: **the record's own
   words govern** (the big dispatch, §L's opening). Do NOT read the records of §L.1 to §L.15 or of §L.26 to §L.55.
3. **The display surface WHOLE:** `ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md` (21,522 bytes),
   the surface §L.25's record names, from which §L.25's four added statements are copied (§3 item 3).
4. **The successor WHOLE, at the git object of session 2's Task 1 commit:**
   `git show 9987d3c91ad80a59743759dc24e6b87ed098c5c7:cowork_derived_specification_l3_2026_11_08.md`, written to a
   scratch path outside the repository and read there with the Read tool in ranges. It is 150,515 bytes, 1,438 lines,
   and has no line longer than 1,205 characters. The derivation is not read: the successor carries every statement this
   stretch amends, and every field this stretch edits is one session 2 left as derived, so the field as the successor
   carries it is the derivation's own text, which is what a `(was: …)` mark quotes. **If an amendment of §L.16 to §L.25
   would edit a field session 2 already edited** (one that already carries a `(was: …)` or `(added; …)` mark), STOP and
   report for that amendment; apply the rest.
5. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
6. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard
   (its condition in `CLAUDE.md` is not met).
7. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 4 to 255 at this writing; the
   dispatch-protocol clause on the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_five.md` (the current entry point,
   written by the sitting that wrote this file; untracked, §4 item 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_four.md` (the one before it).
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
    - **lines 1635–2726 (§L.16 to §L.25, your stretch)**;
    - lines 6100–6571 (Task 1, whole);
    - lines 7111–7135 (*What this batch does NOT do*).

    **Do not read in this session:** lines 38–58; lines 431–1634 (§L.1 to §L.15, already applied); lines 2727–6099
    (§L.26 to §L.55, and Task 0); lines 6572–7110 (Tasks 2 to 5); lines 7136 to the end. Nor the derivation, the reading
    file, `FRAMEWORK.md`, `cowork_derived_specification_l0_l1_2026_09_03.md`, `tools/audit/gen_status_batch_bound.py`
    or `records/cowork/handoff/cowork_away_returns.md`: each belongs to a later Task's session or is not needed here.

## 3. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Which ledger entries Task 1 applies** (Task 1 (a): *"Each §L entry's Successor — amendments part is applied, in
   ledger order"*) → **§L.16 to §L.25 only, in ledger order.** §L.1 to §L.15 are applied already and are not touched;
   §L.26 to §L.55 are not applied, read or touched.
3. **Task 1 (c), split by stretch.** Apply here only the parts whose ordering record is one of §L.16 to §L.25:
   - (c) item 1: **L3-S28** (§L.16, all six fields as given), **L3-S25's Premise** (ordered by the figured-bass record,
     §L.16), **L3-S5 (ii)** (§L.17) and **L3-S39** (§L.20). **Not here:** L3-S7, L3-S16, L3-S17, L3-S23 family (iv),
     L3-S24, L3-S9 and L3-S42 — session 2 applied them and they are not touched.
   - (c) item 2: applied by session 2; nothing here.
   - (c) item 3, the added statements: **§L.25's four only (parts A, B, C and D)**, under (c) item 3 (ii): each part as
     the display surface (§2 item 3) states it, quoted whole, located by the part's heading there, with the record's
     *"In short"* words for the part quoted beneath it as a sub-item. Each is headed
     `### Added — <record file>, Ruling N, <part as the record names it>` (form (a)). They go in the existing section
     `## Statements added by the L3 family rulings`, **after §L.13's statement** (the one headed for the key-areas
     record) and before the `---` line that closes the section, in the order A, B, C, D. No new section is created.
   - (c) item 4 (OQ-L3-9, §L.17 amendment 4): **here**, in the `**RECORDED ANSWER (<record file>, §<section>):**` form
     item 4 gives. It is not counted in the ANSWERED set.
   - (c) item 5: unchanged (§L.17 amendment 5 writes nothing at OQ-L3-1). (c) item 6: unchanged, for this stretch's
     entries.
   - The `## Notes — lists the records place here, not ruled` section (form (a), last bullet): created by this session
     only if one of §L.16 to §L.25 places a list there; otherwise not created. If created, it goes after the section of
     added statements and before the `## 5.` heading.
   If you find that a part assigned to this session depends on the words of a record outside §L.16 to §L.25 (other than
   the statement-texts ruling records whose texts Task 1 (c) item 1 itself carries, and the display surface), or a part
   not assigned here is ordered by a record inside it: STOP and report for that part; apply the rest.
4. **Task 1 (a) and (b) are not re-applied.** The file exists (§1 check 4); it is edited in place by targeted edits only,
   never re-typed and never re-made from the derivation. Two lines written by session 2 change:
   - **The banner's ANSWERED set**, the parenthesis in the sentence *"The open questions of §4 stand with their ANSWERED
     marks where a ruling answered them (…)"*, is re-taken at the file after this stretch's edits and written as the set
     the file then carries. The writing side's expectation: **OQ-L3-2, OQ-L3-3, OQ-L3-4, OQ-L3-5, OQ-L3-6, OQ-L3-7,
     OQ-L3-8 and OQ-L3-10 — eight**, OQ-L3-7 joining at §L.16 amendment 1. A difference is reported. Nothing else in the
     banner is touched.
   - **The in-progress line beneath the banner**: `§L.1 to §L.15` becomes `§L.1 to §L.25`, and nothing else in it
     changes. Attribute it in the diff table to *"session 3's instruction, §3 item 4"*.
5. **Task 1 (d), one commit for the whole of Task 1** → **one commit for this stretch.** The boundary of D-672 is the
   ledger entry: if signs of context degradation appear, apply no further entry. If you are between entries, commit the
   entries already applied, write in the in-progress line the last entry actually applied instead of §L.25, set the
   banner's ANSWERED set to what the file carries, and report which entries were applied. If you are inside an entry,
   do not commit; STOP and report which entries were applied to the uncommitted file and that it is not landed.
6. **One staleness fix shown, added by this file** (the user's rule of 2026-09-22; nothing in the big dispatch orders
   it). §4 of the successor closes with *"**Questions for the user, counted from the ★ marks: 5 of 14** (OQ-L3-2, 3, 6,
   8, 10)."*, and session 2's stretch answered all five. In that sentence only, `(OQ-L3-2, 3, 6, 8, 10).` becomes:

   `(OQ-L3-2, 3, 6, 8, 10); all five are now ANSWERED, each by the record its ANSWERED mark names. (was: "(OQ-L3-2, 3, 6, 8, 10)."; staleness fix shown, records/cc/instructions/cc_instruction_l3_application_session_3_task_1_stretch_2_2026_11_22.md, §3 item 6)`

   The bold part and the sentence after it (*"DP-N and DP-Q, …"*) are not touched. Attribute it in the diff table to
   *"session 3's instruction, §3 item 6"*.
7. **Task 1 (e), the check before the commit,** is run with these changes for this stretch:
   - **The method:** store the edited successor with `git hash-object -w cowork_derived_specification_l3_2026_11_08.md`
     and diff the two blobs, `git diff -U0 e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1 <the new blob>`, written to a
     scratch file outside the repository and read with the file tools. The base is session 2's successor, not the
     derivation object.
   - **The attributions available:** only this stretch's §L entries and their amendment numbers; the (c) parts §3 item 3
     assigns here, by statement and field; §3 item 4's two lines; and §3 item 6's fix. A changed passage none of those
     accounts for is a STOP-and-report and the file is not committed until it is removed.
   - **Bold text:** the only exception is L3-S28's statement, whole ((c) item 1). Any other change to a statement's bold
     text is a STOP-and-report for that amendment.
   - **Every statement and open question that none of §L.16 to §L.25 and none of the (c) parts assigned here names is
     byte-identical to the one in blob `e5c7ef48…`**, and every passage session 2 wrote is unchanged except the two
     lines of §3 item 4. L3-S1 to L3-S42 and OQ-L3-1 to OQ-L3-14 are each present exactly once.

   The commit subject is exactly:

   `application L3, Task 1 stretch 2 (§L.16 to §L.25): the derived specification as amended by ten more L3 family ruling records, every amendment citing its record, not ratified`

   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
8. **E1** is checked for this stretch only, as items 3 to 7 restrict it. The full E1 belongs to the session of the last
   stretch.
9. **Where the batch ends for this session.** After §4's acts, this session STOPS. It does not begin §L.26, Task 2 or
   any later Task.

## 4. The acts, in order

1. **Land the writing side's two files first, in a commit of their own.** Exactly two paths, both expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_3_task_1_stretch_2_2026_11_22.md`, and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_five.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entry 1185 and the session 3 instruction of the L3 application landed; Task 1 stretch 2 follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **Task 1 for §L.16 to §L.25**, as the big dispatch's Task 1 and §3 above give it, ending with §3 item 7's check, its
   commit and its push.
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_3_task_1_stretch_2_2026_11_22.md` with the
   items of §5. Commit that ONE path alone, subject exactly:
   `report: session 3 of the L3 application, Task 1 stretch 2 (§L.16 to §L.25) written; stretch 3 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 5. What the report states, and the same in your closing message to the user

1. §1's five results, the blobs, and the repeat of check 2 before staging.
2. The three commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. For each of §L.16 to §L.25, in order: every amendment by its number, applied (and where), or STOP-and-report (and
   why). The same for each part of (c) §3 item 3 assigns here, and for §3 items 4 and 6.
4. The ANSWERED set the file carries, set against §3 item 4's eight.
5. The diff table of §3 item 7, every changed passage attributed.
6. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
7. The last sentence, exactly: *"Session 3 of the L3 application ends here. Stretch 3 of Task 1 is not begun. Nothing else was done."*

## 6. What the earlier sessions established, for the record (relayed here; verified by the Cowork sitting at the objects)

Session 1 committed Task 0 as `cbde76fd78a244540df64895191a511df186cc29` and stopped at Task 0's guard-set check: two
tools failing beyond the thirteen of the declared start state, item 2 (`gen_evidence_pin_membership.py`, which counts
the ruling records on disk, and `gen_per_session_reading.py`, which finds handoff entries through git). Session 2 applied
§L.1 to §L.15 and held one amendment as STOP-and-report, §L.15 amendment 4, as that entry's own settled note orders.
**This session runs no guard**, so neither red bears on its acts; both are declared here so that no later reader takes
them for this session's doing.

## 7. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 5);
- the big dispatch's Task 1, its forms, its standing bars or its findings rule makes something a STOP (an amendment
  that is STOP-and-report under them is reported and the rest applied, as they say);
- §3 item 7's check finds a changed passage it cannot attribute;
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §3 does not list.

After a STOP, report what you did and what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1184. Read at the objects for this file: the
three git reference files; the commits `95286f78…`, `9987d3c9…` and `cda8d482…` and their trees against their parents',
folder by folder; the successor at blob `e5c7ef48…` (its diff against the derivation, its quotations against the records
they name, its line lengths, its §4 closing paragraph and its added-statements section); session 2's report whole; the
big dispatch (blob computed from the staged bytes) at its `### §L.` headings, line lengths at lines 37–99, 394–431 and
7110–7157, Task 1 at lines 6100–6135, 6157–6275, 6378–6467 and 6504–6571, form (a)'s added-statement bullet at lines
178–200, §L.15 whole, §L.13's amendment 1, and §L.16 to §L.25 by search for their amendment lists, added statements,
RECORDED ANSWER and Notes lists; the sizes of §L.16–§L.55, of their records and of the three tier-3 surfaces §L.25 to
§L.27 name; L3-S5's statement in the successor; `records/cowork/handoff/cowork_handoff.md` at lines 1–5 and 250–258.
The user's words: the opening instruction with Claude Code's closing message; "shortened"; "continue".*
