# Cowork handoff entry 1021 — 2026-11-16 — RELEASE STEP 3 BEGUN: THE GUARD FIGURES (GROUP 1) AND THE REGISTER SUPERSESSIONS (GROUP 2) WRITTEN AT THEIR MARKS; TWO DISPATCH LANDINGS, PROVED; GROUPS 3 AND 4 LEFT; THE PREMISE LEDGER THE DISPATCH NEVER GOT, RAISED; ONE SLIP CAUGHT BEFORE DRAFTING; HANDED OVER AT A VERIFIED STOP

**The current entry point.** Entry 1020 is superseded as entry point and stands otherwise. Release step 3 of entry 767
§3 (Part C's facts at the marks) is begun, not finished. Next is the rest of step 3 (§3 below). **[checked]** means read
at the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1021 (staging answered *"does not exist"*, in a call of its own, after entry 1020 was
  read and before any other boot read; asked again, in a call of its own, before this entry was landed). Entry 1020 at
  14,435 bytes as staged; entry 1019 at 15,697; entry 584 at 4,843; the working file at 572,462 and the dispatch at
  848,829, as entry 1020 says. Read whole: entries 1020, 1019, 584 and 767. The working file at its opening part
  (lines 1–64). The frozen copy and the findings section not read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714, by search (LIVE).
- **Git [checked at boot]:** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both at
  `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no dispatch is out.
- **The user's leave for read-only searches**, carried by entry 1020 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line.
- **Changed on disk by this sitting** (each landing guarded by the device copy's modification time, each proved by
  staging back and comparing the staged-back copy's SHA-256 with the sum taken of the copy sent, identical both times;
  every passage drafted with the Write tool, shown to the user in substance before landing, and checked in the edited
  copy by `python3 -I` against the draft: each new passage once, each old passage gone or standing only inside its own
  kept former wording, the growth equal to the drafts' differences):
  - `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (the dispatch), two landings: first
    **852,134** bytes, SHA-256 `427aecd7…` (group 1; 3,305 bytes added); then **853,426** bytes, SHA-256 `2253bd69…`
    (group 2; 1,292 bytes added). Still NOT YET RELEASED. **6,938 lines** (unchanged: every edit stays inside the
    lines it replaced, so no row of the working file moves). Every passage this sitting wrote carries *"the sitting
    booted on entry 1020"* (9 occurrences in the file [checked after the second landing]).
  - This entry (new).
  - The working file was not edited. Its progress paragraph's *Next* (lines 26–28) still names steps 3, 5 and 6, which
    stays true.
- **Not in git:** as entry 887 §1 lists [relayed], plus entries 888 to 1021, the frozen copy, the surface and ruling
  record of 2026-11-15, and the dispatch edits of the sittings of entries 959 to 1021.

## 2. What this sitting established

1. **The marks, sorted [checked at each line].** The dispatch carried 19 occurrences of *"[AT RELEASE]"* on 17 lines at
   boot (entry 767 §2 item 1 (b) counted 17). Not marks to fill: banner lines 12, 13, 19 and 20 (they describe or record
   the marks' state; line 20 twice); line 70 (inside a kept former wording); line 2376 (§L.23's *Open* note, point (4):
   the derivation's file name, which its own check note says is settled at the words section; a dated note, it
   stands); line 255 (a dated check-turn note of 2026-11-09, which stands); line 6931 (the self-check of the sitting
   booted on entry 638, a dated record of what it left, which stands). The live marks, in four groups by the object
   each fact comes from: **group 1**, the guard figures (lines 242, 5866, 6891, and line 19's E5 part); **group 2**,
   the register supersessions (lines 294, 6862, and line 19's part); **group 3**, Task 0's path list and range (lines
   5797, 5836, 5857); **group 4**, the ordered first reads (line 56, with banner line 13).
2. **The order of step 3, agreed by the user ("agreed"):** groups 1, 2 and 4 in step 3. For group 3, step 3 writes now
   only the part that will not go stale (the records landed since entry 604 that Task 0 must carry); the closing end
   of the range ("the last entry and record written before release") is marked for the releasing sitting of step 6 and
   recorded in the banner, because every sitting until then adds at least one handoff entry.
3. **Group 1, written and landed** ("yes"). Read at `tools/audit/guard_state.json`'s working-tree copy (136,499 bytes;
   modification time 2026-11-08 12:32 Stockholm, before both ref files' 12:33): `summary` run 83, passing 70, failing
   13, not_run 4, historical 20; `the_population`'s `unclassified_candidates` empty, the runner's own STOP condition
   [checked at `tools/audit/gen_guard_state.py` lines 1462–1486, its `--check` mode and its STOP]. Against the L2 act's
   start state (its dispatch lines 277–287: run 80, failing 12), the one added failing tool is
   `decisions/gen_cluster_dispositions.py --verify`. Four failing tools print *"STOP:"* inside their own output; the
   dispatch now says they are failing verdicts, not STOPs of the run. Written: line 242 (the declared start state, item
   2, in the L2 dispatch's guard-FACT form, with *UNSETTLED: whether that copy is the tip's blob*); lines 5866–5868
   (Task 0's guard-set acts: the full guard set by `tools/audit/gen_guard_state.py --check` after act (4) and before
   the batch's first edit; acts (1) to (4) regenerate no artifact; `gen_evidence_pin_membership.py --check` measured
   before accepting, the L2 dispatch's assumption A3, its lines 409–416, relayed and said so); line 6891 (E5 points to
   item 2); banner lines 13 and 19. The dispatch named neither the guard artifact nor the runner before this sitting;
   both come from the L2 application dispatch and the artifact's own `generated_by` field.
4. **Group 2, written and landed** ("yes"). Not a question for the user: **Ruling 4 of
   `records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_part_b_sitting.md`** (B4 ratified as
   written) holds that the batch creates no decisions-register entry and allocates no `D-NNN`, the supersessions a list
   under each entry's *Register*; Task 5's close already restates the lists (dispatch line 6861). So the fact written:
   nothing into `DECISIONS.md`, no `D-NNN`, the lists restated by the close, the register carriage left to the register
   route the records name (§L.2, §L.3, §L.4, §L.52). Written: lines 294–295 (§L's opening), 6862 (Task 5), a dated note
   in line 256 (the standing bars), and banner line 19.
5. **Raised for the rest of step 3, not acted on:** (a) **the premise ledger.** Part C (list line 4132) and banner line
   13 name one; the dispatch has none (searches of the whole dispatch: *"premise ledger"* once, at line 13; *"ASSUMPTION
   A"* none; *"FACT —"* none). The L2 dispatch had one (its FACT, ASSUMPTION and UNSETTLED lines, from its line 277 to
   about 434). Whether step 3 writes one, and in what scope, may be a question for the user; check the record first
   (D-599). (b) **The 13 decisions** the §L *Register* lines name as superseded at L3 or losing their subject there
   (D-081, D-336, D-454, D-455, D-456, D-458, D-472, D-477, D-478, D-479, D-481, D-584; D-495) all stand **LIVE** at
   their `DECISIONS.md` rows [checked], and the register's status words have no form for a supersession at one layer
   only (`DECISIONS.md` lines 96–106 [checked]). Carrying them is a later register act, not this batch's; noted so it
   is not lost. (c) **Entry 767 §3 has a step 4 (Part B)** between steps 3 and 5; entries 1019 and 1020 go from step 3
   to steps 5 and 6. For B4 the record settles it (item 4); B1 to B5 stand ratified in the record named there, B6 to B9
   at the second and third Part B records [relayed from the first record's *Not ruled here* and from the dispatch's
   marks that name the third]. Whether anything of Part B is still open was not checked.
6. **One slip, caught before drafting:** line 2376 was put in group 2 from a search fragment before its line was read;
   reading it showed it is about the derivation's file name. Corrected before any draft and told to the user. No other
   degradation tell noticed. Handed over at a verified stop, judged out loud to the user after the second landing
   ("agreed"): group 4 is the largest part left and is partly the writing side's authoring (the premise ledger), and
   group 3 needs four folder listings, one of them over a thousand entries.
7. **On the model.** `claude-opus-5-5`. Nothing this sitting met shows whether a different model would have done better
   or worse.

## 3. The plan — carried forward

1. **Next: the rest of step 3 of entry 767 §3.** Live marks left [checked after the second landing]: line 13 (as to the
   ordered first reads and the premise ledger), line 56 (the ordered first reads), lines 5797, 5836 and 5857 (Task 0's
   path list and range). Every other occurrence of *"[AT RELEASE]"* (20 in all now, on lines 12, 13, 19, 20, 56, 70,
   242, 255, 295, 2376, 5797, 5836, 5857, 5868, 6862, 6891, 6931) is a description, a dated note or a kept former
   wording, as §2 item 1 sorts them.
   - **Group 4 first:** read line 56's section whole, and the L2 application dispatch
     (`records/cc/instructions/cc_instruction_l2_application_2026_10_10.md`, 782,895 bytes) at its ordered first reads
     (about its lines 100–130) and its premise ledger (its line 277 to about 434) as the model. Settle §2 item 5 (a)
     at the record before writing; if it needs the user, a self-contained surface, the question in a later turn.
   - **Group 3:** as §2 item 2 says. Task 0's items 1 to 3 (dispatch lines 5800–5837) list the records, surfaces and
     entries 586 to 604; the records landed since (the release-period ruling records and surfaces, the site table, the
     list, the working file, the frozen copy, entries 605 onward) are added from folder listings; the closing end of
     the entries' range and of the records is marked for step 6, and the banner says so.
   - Show the writing side's wordings before landing; land and prove each group; read each range by the Read tool
     immediately before its Edits; keep each edit inside its lines where the wording allows, so that no row of the
     working file moves; if a group adds lines, record how many. Judge out loud after each landing whether another fits.
2. **Then steps 5 and 6 of entry 767 §3.** Step 5 also takes everything entries 1015 to 1020 §2 list for it, and §2
   items 5 (b) and (c) above. Step 6 also takes group 3's closing end and keeps the former banner whole, as finding 17
   records [relayed]; line 20's note travels with it.

**Carried rules:** as entry 912 §3 [relayed], the user's ruling "3" (entry 957 §2 item 1), Rulings 12 to 14 of the
record of 2026-11-15, and the user's ruling "A" (entry 1020 §2 item 1). **Practical notes, no rules:** as entries 908
and 910 to 1020 §3, and: (a) the landing route held twice more, the send and the commit in separate steps, each file
sent from its staged copy. (b) The dispatch now costs 853,426 bytes; reading its lines by `python3 -I` printing only
the lines needed, and its long lines in parts, met no trouble. (c) The guard artifact, the L2 dispatch, `CLAUDE.md`,
`BUILD_AND_TEST.md`, the list and the site table stage by their paths with no listing. (d) The cloud environment
restarted once mid-sitting, between landings; the staged copies survived (checked by SHA-256). (e) Entry 1022 is
`cowork_handoff_entry_one_thousand_and_twenty_two.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_twenty_one.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1022 exists (if it does, report and ask). It reads **this entry whole**, **entry 1020 whole**,
   **entry 767 whole** (10,922 bytes), and the working file at **its opening part (lines 1–64)**. It does **not** read
   the frozen copy or the findings section whole, and does not list the handoff folder. It proves this entry's size as
   the device reports it when staged, the working file at 572,462 and the dispatch at 853,426, and reads both ref files
   (anything but `e855ff2a…` means something ran: find out what first). It reports the boot with a capacity judgment,
   asks the session-start read, then does §3 step 1.
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies and scratch drafts (`cd`, `grep`,
  `cut`, `tr`, `wc`, `awk` and `sed -n` to print line lengths, `sha256sum`, `sleep`, `printf` to print counts), and
  `python3 -I`, reading files only (its script given on standard input), to print lines and parts of lines, to read the
  guard artifact's fields, the `DECISIONS.md` rows and the `CLAUDE.md` passages by pattern, and to check the edited
  dispatch against the drafts. Nothing written by any shell, in the container or on the device; no shell deleted
  anything. Drafts and this entry written with the Write tool; the group 1 draft file was rewritten once before it was
  shown, to remove a mistaken first version of edit B.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected. `C:\s\MS` was requested and granted; **`C:\s` was not listed**, and no folder of the repository
  was listed.
- **Read beyond entry 1020 §4 step 3's list:** entry 584 whole (the boot it names); entry 767 whole (the plan's steps,
  as entry 1020 §3 step 1 orders); for groups 1 and 2: the guard artifact; `tools/audit/gen_guard_state.py` at lines
  1455–1490 and by search; the L2 application dispatch at lines 115–125, 277–292, 380–480 and 5866–5876, and by
  search; `BUILD_AND_TEST.md` and `CLAUDE.md` by search, `CLAUDE.md` at lines 600–659; `DECISIONS.md` at lines 85–125
  and the 13 rows; the list at lines 4105–4136 and by search; the site table by search only; the first Part B ruling
  record whole, the second and third by search. The dispatch at the lines §2 names and by search.
- **Landing route:** the staged copy edited with the Edit tool, sent from its staged path, and committed by the identity
  the send returned; this entry written in the outputs folder, sent, and committed by the identity the send returned.
  The wordings were described to the user and offered in full from the draft files; they stand as landed, each
  compared with its draft.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-16 (Stockholm), the sitting booted on entry 1020. The user's words: the opening
instruction; "shortened" (the session-start read); "agreed" (the order of step 3, group 3's handling); "yes" (group 1);
"yes" (group 2); "agreed" (after the second landing, the handover recommended).*
