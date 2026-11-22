# Cowork handoff entry 1184 — 2026-11-22 — SESSION 1 OF THE L3 APPLICATION VERIFIED AT THE OBJECTS (TASK 0 LANDED AND PUSHED; ITS STOP CORRECT); TASK 1 SIZED AT FOUR STRETCHES; SESSION 2'S INSTRUCTION (STRETCH 1, §L.1 TO §L.15) WRITTEN, LANDED AND GOES TO CLAUDE CODE

**The current entry point.** Entry 1183 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first; `C:\s\MS` connected after one refused access request (the user added
  the folder). Entry 1184 checked by staging in a call of its own: *"does not exist"*. Entry 1183 read whole; entry
  1026 §3 read.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` whole (11,726 bytes, 1794136674043,
  unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207, unmoved, so the last
  full read stands; the gating answer (247 open, 222 gating, 25 non-gating, unchanged); `CLAUDE.md` attached whole by
  the user's app.
- **Git [checked]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and `refs/remotes/origin/master` both
  `cbde76fd78a244540df64895191a511df186cc29`.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** two new files and nothing else — the session 2 instruction
  `records/cc/instructions/cc_instruction_l3_application_session_2_task_1_stretch_1_2026_11_22.md` and this entry.
  Neither is in git; session 2's first act lands both. No ruling was taken, so no ruling record was written.

## 2. What this sitting established

1. **Session 1's commit [checked at the objects].** Commit `cbde76fd…` hashes to itself; parent `e855ff2a…`; subject
   exactly the session 1 instruction's §3 item 5. Its tree against the parent's, folder by folder: **693 added** (598
   handoff entries 586 to 1183, 48 ruling records, 45 surfaces under `ratification_surfaces/`, 2 instructions), **4
   modified** (`docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
   `ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md`,
   `ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md`), **none deleted**. In the tree: the big dispatch
   at blob `b5274c2c…`, the session 1 instruction at `a2b30bad…`, entry 1183 at `4a90cafc…`, the last two equal to the
   disk copies. `tools/audit/guard_state.json` still dated 2026-11-08: not rewritten.
2. **Session 1's STOP was correct** by the big dispatch's own words (line 6083: a red outside the thirteen whose cause is
   not a landed record's PINNED sentence is a STOP-and-report). **Its two causes [checked at the tools and artifacts]:**
   - `gen_evidence_pin_membership.py` lists every `cowork_rulings_*.md` in `records/cowork/rulings/` **on disk**
     (`os.listdir`), not in git. Its artifact (2026-11-07 19:04) records 218 records read, 7 members, 5 pinned. The 48
     new records were written to disk from 2026-11-08 12:52, after that artifact and after `e855ff2a…` (12:33). **So
     this red existed before session 1 began**; Claude Code's wording *"because the 48 records just landed joined its
     list"* is imprecise on the cause and right on the figures. The declared start state's item 2 was therefore already
     overtaken at the tree session 1 met — the shape the standing clause *"A dispatch's DECLARED START STATE is stated
     at the tree the dispatch will meet"* (`cowork_audit_protocol.md`) exists against.
   - `gen_per_session_reading.py` finds handoff entries through `git log --diff-filter=A`; Task 0's commit moved it (505
     to 1103 [relayed figures], +598 [checked]).
   - **What follows needs no ruling** (the user's rule of 2026-09-22 on staleness): `per_session_reading.json` is
     already regenerated at the big dispatch's Task 5 (d), and assumption A5 already admits movement of
     `evidence_pin_membership.json`; **owed: the regeneration of `evidence_pin_membership.json` at the close, to be
     written into the instruction of the session that runs Task 5**, and both reds declared in the start state of the
     session that next runs the guard set. Both move again whenever this side writes a ruling record (the first) or a
     commit lands handoff entries (the second).
   - The other guard figures (83 run, 15 failing, 4 not run, 20 historical, zero STOPs) and the 395 untracked paths are
     **[relayed]** from Claude Code's closing message.
3. **`tools/audit/claude_md_finer_archive.json` [checked]:** raw blob `fb5249c1…` with 122 carriage returns; with CRLF
   normalised, `1df4f207…`, the hash Claude Code named as the tip's. The tip's own entry for that path was **not** read
   by this sitting; session 2's §1 check 5 reads it with `git ls-tree`.
4. **Task 1 sized [checked sizes; token figures are estimates].** §L.1 to §L.55 come to 637,901 bytes and their 55 ruling
   records to 456,191 bytes. The records must be read whole (§L's opening: *"the record's own words govern"*). A stretch
   session's fixed reading is about 529 KB (≈203k tokens at the relayed 2.6 bytes per token) on top of the 104.1k at
   start [relayed], so about 307k before any ledger work; against a ceiling of about 450k, that leaves about 290 KB of
   entries-plus-records per session. **Four stretches:** §L.1–§L.15 (282 KB), §L.16–§L.28 (266 KB), §L.29–§L.41
   (296 KB), §L.42–§L.55 (250 KB). Entry 1183's estimate of three is superseded.
5. **Session 2's instruction written**, shown whole to the user, landed on his word ("yes"), proved byte-identical at
   the staged copy. Its three authored choices, shown to the user: Task 1 (c)'s parts split by the stretch of the
   record that ordered each; one in-progress line added beneath the ratified banner (#10), removed by the last stretch;
   the D-672 boundary at the ledger entry.
6. **Degradation tells (2026-08-15 list):** none noticed. **On the model (2026-11-12):** nothing met suggests the work
   exceeded it.

## 3. The plan — carried forward

1. **Now: Claude Code session 2 runs** (§4). The writing side writes nothing into the repository while it runs.
2. **Next Cowork session, after session 2 reports:** read Claude Code's closing message and its report file in full as
   unverified, and verify at the objects: the three commits by hash, `origin/master` at the last, the successor's diff
   against the derivation object passage by passage against the report's table, the ANSWERED set, the in-progress line.
   Then write **session 3's instruction: Task 1, stretch 2 (§L.16 to §L.28)**, sized out loud first. It must:
   - replace Task 1's *Before the edit* check (the successor now exists, at session 2's Task 1 commit);
   - read the successor at session 2's Task 1 commit instead of the derivation whole, and diff against that commit;
   - carry (c) item 1's L3-S28 and L3-S25 (§L.16), L3-S5 (ii) (§L.17), L3-S39 (§L.20), (c) item 4 (OQ-L3-9, §L.17) and
     the added statements of §L.25 to §L.28;
   - add L3-S28's statement to the bold-text exceptions;
   - re-take the ANSWERED set (OQ-L3-7, §L.16, expected to join);
   - name session 2's report commit as its starting point and list the untracked files this side adds.
3. **Later:** stretches 3 and 4, then Tasks 2 to 5, each instruction written only when next. The session running the
   guard set declares both reds of §2 item 2; the session running Task 5 adds the regeneration of
   `evidence_pin_membership.json`. The last stretch removes the in-progress line and runs the full E1.
4. **Open with the user, not ruled:** as entry 1181 §3 step 3.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1183 §3, and: (a) a stretch
session's sizes are in §2 item 4; recompute them from the objects, not from this entry. (b) Entry 1185's file name would
be `cowork_handoff_entry_one_thousand_one_hundred_and_eighty_five.md`; check by staging. (c) Loose git objects can be
read on staged copies with a read-only `python3 -I` script (zlib, sha1 check); the tree comparison of §2 item 1 was done
that way, staging each missing object as the script named it.

## 4. Who does what, in this order

1. **THE USER now opens a NEW Claude Code session in `C:\s\MS`.** Not session 1. He gives it exactly this:
   > Read and execute `records/cc/instructions/cc_instruction_l3_application_session_2_task_1_stretch_1_2026_11_22.md`. Your first tool call must be one read of that file and nothing else: no other file in that call, and nothing read in parallel with it. Then follow the order it gives.

   That instruction carries the three commits and the PUSH to `origin` after each (its §4).
2. **While Claude Code runs, and after it ends:** no Cowork session writes anything into the repository. When it ends
   with *"Session 2 of the L3 application ends here. Stretch 2 of Task 1 is not begun. Nothing else was done."*, or
   stops and reports, the user does **not** ask it to go on with stretch 2 or to repair anything, whatever it offers.
3. **Then the user opens a NEW Cowork session** (with `C:\s\MS` added before the first message), and gives it Claude
   Code's closing message together with exactly this:
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_one_hundred_and_eighty_four.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1185 exists (if it does, report and ask), reads this entry whole and
   entry 1026 §3, asks the session-start read, then does §3 step 2.
4. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **The device-info call was made first**; only a tool-loading lookup came before it. The first folder-access request
  was refused by the app; the user then added the folder himself.
- **One shell read refused and not retried another way:** a `cat` of the three git reference files; they were read with
  the Read tool instead.
- **The container shell, under the leave:** read-only `grep`, `sed -n`, `awk`, `cut`, `fold`, `cmp`, `wc` on staged
  copies, and read-only `python3 -I` scripts (object decompression and hashing, the tree comparison, sizes, JSON
  fields). One script file was written to the container's own scratch folder (`/home/claude/scripts/treediff.py`) and
  its output to `/home/claude/`; nothing written into any staged copy or the repository by a shell. No shell on the
  device. No repository tool was run or imported.
- **Staged beyond the boot list:** the three git reference files and 22 loose objects under `.git/objects/`; the session
  1 instruction; the big dispatch; the 55 ruling records §L names (for their sizes); `cowork_audit_protocol.md`;
  `cowork_handoff.md`; the derivation; `BUILD_AND_TEST.md` (size only); `decisions/group_K.md` (D-674's heading only);
  `tools/audit/gen_evidence_pin_membership.py`, `gen_per_session_reading.py`, `guard_state.json`,
  `evidence_pin_membership.json`, `per_session_reading.json`, `claude_md_finer_archive.json`. Listed: the repository
  root, `.git/objects/cb`, the rulings folder.
- **The two files written in the session's outputs with the Write tool** and committed to the device with the commit
  tool, then staged back and compared. No git, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1183. The user's words: the opening instruction
with Claude Code's closing message; "try again"; "shortened"; "continue"; "continue"; "yes".*
