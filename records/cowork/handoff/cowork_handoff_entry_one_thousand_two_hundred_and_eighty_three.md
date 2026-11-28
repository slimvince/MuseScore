# Cowork handoff entry 1283 — 2026-11-28 — A DECISION SURFACE IS OWED ON A DIFFERENT WAY OF APPLYING RULINGS TO THE SPECIFICATIONS (THE USER'S REQUEST); THE NEXT SITTING ALSO VERIFIES SESSION 40 WHEN CLAUDE CODE HAS FINISHED; WRITTEN WHILE CLAUDE CODE RUNS SESSION 40; NO DEGRADATION TELL MET

**The current entry point.** Entry 1282 is superseded as entry point. It stands otherwise, and its §2 and §3 step 1
(what session 40's verification checks) are this entry's §3 part B. **[checked]** means read at the object by the
sitting that wrote this entry (the one booted on entry 1281); **[relayed]** means not; **[reading]** means that
sitting's inference.

## 0. The user's rules in force, and his words

**Carried unchanged:** entry 1282 §0, and through it entries 1281 to 1259 §0.

**His words after entry 1282 was landed** (the sitting was then read only; his last message overruled that for this
entry):
1. *"Handoff is done. Any guess on our progress tempo?"*
2. On the answer's sentence *"The difference is mostly in how the application step is organized, not in how hard the
   analysis is"*: *"This is important. Spend some time on figuring out a different approach that maximizes progress and
   minimizes tokens spent while reasonably handling risk (for errors or omissions in spec."*
3. *"Currently CC is working on its dispatch. You could write a new instruction for cowork for the decision surface above
   AND taking care of cc:s work when it is done."*

No ruling was asked for or given.

## 1. State

- **Git [checked, at the reference files, at that sitting's boot]:** `.git/HEAD` *"ref: refs/heads/master"*;
  `refs/heads/master` and `refs/remotes/origin/master` both `a1938ebc7c57c867ff52b40e09fe8269b7b3fe9e`. **Claude Code is
  now running session 40** on `records/cc/instructions/cc_instruction_l3_application_session_40_task_5_2026_11_28.md`
  [relayed: the user's message 3]; the refs will move as it lands its commits.
- **Changed on disk:** this entry, new and untracked. Session 40's act 1 lands entries 1279 to 1282 only; this entry
  stays untracked until a later landing (the big dispatch's A1: a further untracked handoff entry is the writing side's,
  not landed and not a STOP).
- **The model:** `claude-opus-5-5`.

## 2. What the decision surface is about — the proposal as given to the user, restated so that nothing rests on the chat

**The observation [checked dates and sizes; the conclusion a reading].** L2 took about two and a half weeks from
derivation (`cowork_blind_derivation_l2_2026_09_27.md`) to its ratification sittings (2026-10-13 and 10-14, the
ratification ruling records). L3 has taken about six weeks so far: derivation 2026-10-17, derived specification
2026-11-08, the release period 11-08 to 11-22, the application 11-22 to 11-28 in 40 Claude Code sessions, and its
ratification act still to come. The excess sits in the APPLICATION step. At the listings: the L3 application dispatch
941,330 bytes; `ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md` 1,336,363;
`…_release_edit_order_2026_11_14.md` 573,556; `…_release_site_table_2026_11_12.md` 751,491; `…_release_points_2026_11_09.md`
475,634; about 600 handoff entries in two weeks (entries 586 to 1183, landed by session 1's Task 0, per entry 1184 §2).
Against that, the edits themselves are small: session 39's whole Task 4 was 2 files, 102 insertions, 5 deletions
(session 39's report, its §2).

**Where the cost goes [reading].** The same intent is restated about five times between the user's ruling and the landed
edit, each restatement checked against the one before: ruling records → the dispatch's ledger restating each record →
the release period checking the dispatch → a per-session instruction, written in one Cowork sitting and compared in the
next (Ruling A of 2026-11-27) → Claude Code's report, verified by a third sitting. Each sitting also pays a fixed cost:
boot reads, reference checks, a handoff entry, landing and proving.

**The approach proposed to the user (his request: maximize progress, minimize tokens, handle the risk of errors or
omissions in the specification reasonably):**
1. **The ruling states its amendment as exact edits.** At the ruling sitting, the surface carries an edit list: per
   edit, the file, the exact current text (found once), the new text, the ruling it comes from. The user's ratification
   then covers the words themselves.
2. **One applier tool, written once.** It reads an edit list and applies it, refusing an edit whose current text is not
   found exactly once. It then checks that the diff touches only the listed sites, that each new text is present, and
   that the line counts match. It writes its own short report.
3. **Apply right after each ruling, one family at a time**, in a Claude Code session whose opening line never changes
   (first checks, run the applier, run the guards, commit, push). No carry list, ledger or release period.
4. **Omissions become a count:** a generated table matching each numbered amendment of a ruling record to an edit and a
   landed site.
5. **The existing safety nets stay:** former wordings kept, one revertible commit per edit set, and the audit phase
   comparing specification against code later.

**Risks and what handles each:** wrong words → the user's ratification of the edit list; wrong site → the
found-exactly-once refusal; collateral change → the diff-scope check; a ruled amendment missed → the count table; a
decision missing from the specification altogether → not an application problem (the audit phase); a defect in the
applier → it is established before it is trusted (#19). **The proposed establishment test:** write the edit lists of
one or two L3 families from their ruling records alone, apply them to the commit before the L3 application, and compare
the result with what the 40 sessions produced. A match establishes the tool; a difference shows where one of the two
paths erred. Time and tokens per family are recorded in the same pilot, so the comparison is measured.

**What the sitting said it does not know [reading, and the first work of the surface]:** which standing rulings this
would amend. The candidates it named: Ruling 1 of
`records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`; Ruling A of
2026-11-27 (entry 1259 §2 item 5) and its extension (entry 1280 §0 ruling 2); Ruling 1 of 2026-11-24, its parts (a) and
(f) (named in entries 1280 and 1281; its record not opened); rulings 2 and 5 of 2026-11-27 (entry 1260 §0); the
dispatch-protocol standing clauses of `cowork_audit_protocol.md` (the pin P-2, the footprint P-3, the read-first block,
the parked-instruction rule); D-252 (Cowork writes dispatches and never runs them). It also said: the act is about the
governance apparatus, not the analysis, and is worth its cost only because the application step is, as far as can be
seen, the main time sink.

## 3. The plan — for the next Cowork sitting, in two parts

**Part A — the decision surface on the application approach. It may begin while Claude Code runs session 40, under the
write bar below.**
1. **Fact-check §2 at the objects before anything is presented:** the dates and sizes, and above all the list of
   standing rulings and clauses the approach would amend. Locate each ruling at its record and read it there (search the
   handoff entries 1240 to 1282 and `records/cowork/rulings/` for those not named by file). Correct §2 where it is wrong
   and say so.
2. **Write the surface** in plain, ordinary English, fully self-contained (every identifier re-explained), as the
   decision-surface order in `CLAUDE.md`'s Conventions gives it. It carries all the alternatives, each weighed towards
   the ultimate objective, towards the guiding principles, and marked for its meta level, with a recommendation explained
   on those same three grounds. **The alternatives at least:**
   - **(1)** the approach of §2 (edit lists, the applier, apply per family at ruling time, the count table), with its
     establishment test and pilot;
   - **(2)** apply at ruling time WITHOUT a tool: the ruling sitting writes the exact edits, and Claude Code applies them
     with its edit tool and a fixed check list;
   - **(3)** keep the current form but cut its ceremony: shorter dispatches, no release period, fewer sittings per
     instruction;
   - **(4)** the current form unchanged.
   For each, state which standing rulings and clauses it would amend, quoting them, and say whether it is a
   documentation and process change only. Nothing in any alternative changes an algorithm the specifications define; say so. A
   measured figure is not claimed where only a reading exists, and an expected gain is stated as a prediction to be
   measured.
3. **Run the sitting's own check over the surface** (coherence, completeness, correctness, and overreaching words) as a
   turn of its own. **Then deliver the surface whole, as text, in one turn.** The choice questions come in later turns,
   ONE DECISION PER TURN, plain text, no question widget.
4. **The write bar while session 40 runs:** write NOTHING to the device. In particular, no file goes into
   `records/cowork/rulings/` (`gen_evidence_pin_membership.py` lists that folder on disk, and session 40 regenerates its
   artifact at its act 5: entry 1184 §2 [checked by that sitting]), and no file under any tracked path. Drafts stay in
   the outputs folder. Reading and staging copies are allowed. The surface and any ruling record are landed on the
   device only after Part B's verification is done.

**Part B — session 40's verification, when the user says Claude Code has finished.** This takes priority over Part A:
if the user reports Claude Code done while Part A is in progress, stop Part A at a clean point and do Part B first.
1. Read Claude Code's closing message (the user pastes it or summarizes it), then the three git reference files.
2. Do entry 1282 §3 step 1: verify the landing commit, the close commit and the end-state commit at the objects (by
   explicit hash, as Ruling 1 (a) of 2026-11-24 gives it), each pushed (`origin/master` at the last). Read Claude Code's
   batch report `records/cc/reports/cc_report_l3_application_2026_11_08.md` and the new section and end-state portion of
   `records/cowork/handoff/cowork_away_returns.md` IN FULL, and treat their claims as unverified until checked at the
   objects (the user's rule of 2026-09-03). Check at the objects: the six new `STATUS.md` entries and the four moved ones;
   the tool's five re-aimed constants and its appended aiming row; the archive header; the *Open* pointer list taking
   both labels as entry 1282 §0 ruling 1 has it; E5 as the instruction's §5 act 9 step 2 derives it.
3. If session 40 STOPPED: read its report, establish the cause at the objects, and put the user what he needs to decide,
   on the decision-surface form. Nothing is repaired without his word.

**Capacity.** Part A and Part B may not both fit one sitting. Judge it out loud at boot and again after Part B. Part B
comes first whenever both are open. Hand over at a verified stop, with an entry, if either part does not fit or a
degradation tell appears.

**After both parts:** the L3 ratification act (Task 3 (d): §15 of the reading file still reads NOTHING), and entry 1276
§3 step 3's items, ordered by what the user rules on the surface.

## 4. Who does what, in this order

1. **Claude Code keeps running session 40.** Do not give it anything else.
2. **THE USER may open ONE NEW Cowork session now**, in the Project `C:\s\MS`, with the folder `C:\s\MS` connected,
   and give it exactly this:
   > Read and follow C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_eighty_three.md. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging that entry 1284 does not exist (if it does, report and ask); reads this entry whole,
   then entry 1282 whole; makes the session-start read by ruling 2 against entry 1282 §1's values; reads the three git
   reference files (they may have moved: Claude Code is committing); judges capacity out loud; then starts Part A under
   its write bar.
3. **When Claude Code has finished** (its last message ends *"Session 40 of the L3 application ends here. …"*, or
   reports a STOP), **THE USER tells that Cowork session so in the same chat**, pasting Claude Code's last message. The
   session then does Part B first.
4. **No other Cowork session is open on this work at the same time.** This entry's writing sitting is READ ONLY from
   now on (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Written after entry 1282 was landed**, in a sitting the rule of 2026-10-14 had made read only, on the user's
  message 3 in §0, which overrules that rule for this entry.
- **Entry 1282 §4 step 2 said no Cowork session is opened on this work while Claude Code runs.** This entry permits ONE,
  on the user's message 3, bounded by Part A's write bar so that nothing it does can reach session 40's inputs.
- **The figures in §2 were read at the listings and the reports by the writing sitting**; the conclusions drawn from
  them are readings and are labelled so. Nothing in §2 was measured as tokens or time.
- **Written** with the Write tool in the outputs folder, **landed with the commit tool**, proved by staging back and
  reading with the file tools. No git on the device, no shell write, no widget, task list, subagent or memory write.
- **Capacity:** no degradation tell appeared. On the model (2026-11-12): nothing raises a suspicion about Opus.

*Provenance: Cowork, 2026-11-28 (Stockholm), the sitting booted on entry 1281, after its entry 1282. The user's words as
§0 gives them.*
