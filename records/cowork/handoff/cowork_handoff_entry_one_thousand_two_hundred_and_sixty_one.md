# Cowork handoff entry 1261 — 2026-11-27 — STRETCH 26 (§L.51) VERIFIED AT THE OBJECTS, NO FINDING; HANDED OVER ON A CAPACITY JUDGMENT BEFORE THE `rebuild.py` EXTENSION AND STRETCH 27'S INSTRUCTION; THE USER ASKS THAT THE PROCEDURE CHANGES BE MEASURED

**The current entry point.** Entry 1260 is superseded as entry point and stands otherwise, except where §0 and §3
below change its plan. **[checked]** means read at the object by this sitting; **[relayed]** means not.

## 0. The user's rules in force, and his words to this sitting

**Carried unchanged:** entry 1260 §0 (the five rulings of 2026-11-27, ruling 1 as corrected) and, through it, entry
1259 §0, both read whole by this sitting.

**His words to this sitting:** the opening instruction (entry 1260's §4 step 2 line, with Claude Code's closing
message); *"yes"* (`python3 -I -B` in the container, on staged copies only, the established scripts copied into a
scratch folder outside the staged tree, this sitting's own placement script, nothing written to the device by any
shell); and *"yes. Since we have modified our procedures a lot, we should somehow measure how much better it got."*
(the handover at this stop, and the request recorded at §3 step 1).

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1261 asked for by staging: *"does not
  exist"* (at boot and again before writing). Read whole: entries 1260 and 1259, session 35's instruction (blob
  `131c8083…`), the README of `tools/audit/stretch_verify/`, Claude Code's session 35 report.
- **Ruling 2's values, at the listing [checked], all three equal to entry 1260 §1's, so none read in full:**
  - `STATUS.md`: 11,726 bytes, modification time 1794136674043;
  - `DECISIONS.md`: 120,603 bytes, modification time 1794081137207;
  - `tools/audit/nongating_apparatus_rows.json`: 178,066 bytes, modification time 1788814584416.
- **Also at the listing:** `cowork_audit_protocol.md` 122,030 bytes, 1789979289703 (unchanged).
  `records/cowork/handoff/cowork_handoff.md` not listed by this sitting.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `2226b2476eb0a674ae87930ae2a02951a0d3ae31`, session 35's report commit.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only (untracked).

## 2. What this sitting established

1. **Stretch 26 verified, Ruling 1 (a) [checked], over staged copies, with the established scripts (staged and run,
   not read) and this sitting's own placement script `place40.py` (kept in the container only):**
   - `gitobj.py`: `d164502e…` (parent `89e107d3…`), `383c878a…` (parent `d164502e…`), `2226b247…` (parent
     `383c878a…`), each hash ok; each subject exactly as the instruction's §5 orders.
   - `treediff.py`, every changed path walked: act 1 adds exactly the instruction (`131c8083…`) and entries 1258
     (`9faf3311…`), 1259 (`90855795…`) and 1260 (`56302308…`); act 2 changes only
     `ratification_surfaces/cowork_comparison_l3_reading.md`, `bb81f43e…` → `5809b5b9…`; act 3 adds only the report
     (`abb96b71…`); the root trees change only under `records/` and `ratification_surfaces/`.
   - `blobhash.py`: the reading file, the instruction, entries 1258 to 1260 and the report on disk, each equal to its
     committed blob, no carriage return.
   - **Rebuild:** `place40.py` from `bb81f43e…` (written out by `blobout.py`), taking the two lines, the §11 entry and
     the in-progress line from the instruction's own code blocks and §3.5 item 3, every insertion point asserted:
     blob **`5809b5b9dd7b041d06c04ddda6be44c38184e9b2`**, 5,352,960 bytes, 84,855 line feeds, the lines at 6573 and
     20080, the §11 entry at 81520, line 54 differing only in §L.50 → §L.51 and §L.51 → §L.52; `cmp` with Claude
     Code's file: identical. Negative test (one character changed in a copy of the instruction): a different blob,
     the compare DIFFERS.
   - `counts.py`: 567 / 45 / 53 / 26 / 1 / 1, *as proposed* 128, every record name as the instruction's §4 item 8
     gives it; 6 added and 1 deleted against `bb81f43e…`, 1,416 and 4 against the Task 2 blob `48e24b2f…`.
   - §10 (80257–81375): no hit for 7.199 or 12.35. §11 (81376–83529): 81520, 81763, 81765 only. Hits outside them:
     6560, 8896, 19524, 20058, 20349, 20364, 20367, 20392, as the report lists.
2. **Claude Code's report, read in FULL:** no slip found that bears on anything committed. Not checked here: its §1
   check 6 (the working-tree enumeration) [relayed].
3. **Capacity, judged out loud to the user, his "yes":** no degradation tell met. Not begun, as too large for a clean
   margin after a verification: the stretch 27 instruction (§L.52, 46 row-parts by its check sum as entry 1259 §2 item 4 gives it [relayed], with ruling 1's
   check of `cowork_handoff.md` lines 1–255 and `cowork_audit_protocol.md` line 180 to the end before landing), and
   the `rebuild.py` extension (whose instruction formats for §10 entries and for rows carrying an earlier line this
   sitting did not read). On the model (2026-11-12): nothing raises a suspicion about Opus.

## 3. The plan — carried forward

1. **NEW, the user's request of this sitting: measure how much the procedure changes of 2026-11-27 improved the
   work.** The next sitting puts a decision surface to the user on how, **before** it writes stretch 27's
   instruction, so that stretch 27 is the first stretch measured. A starting outline for that surface, this sitting's
   reading and not ruled:
   - **The baseline already exists at the files:** entry 1259 §2 items 1 and 2 (stretches 1 to 25: Cowork sittings
     per stretch, instruction bytes and lines, reading-file lines per stretch, what each step caught). Stretch 26 is
     the last stretch under the old procedure (Ruling 1 (e), the separate check).
   - **Per stretch, from stretch 27 on, read at the files:** Cowork sittings that worked on it; Claude Code sessions;
     the instruction's bytes and lines; the total bytes of the files on Claude Code's reading list (the cost ruling 1
     targets); reading-file lines added; what each step caught; STOPs; and any error that reached a commit (the
     quality side: dropping the separate check must not let errors through).
   - **Not visible to Cowork:** the usage each sitting consumes. Whether the user can record it per sitting (for
     example from the usage display) is a question for the surface.
   - **Limits to state with it (#24):** only §L.52 to §L.55 remain, so two to four stretches, of uneven size. That
     makes the comparison indicative and not a finding; per-line and per-row-part ratios reduce the size effect, they
     do not remove it. The same per-stretch record can carry into Tasks 4 and 5.
   - **Meta level:** this is a measurement of the process, not of the analysis. The user asked for it; it should be
     derived from files already written, at small cost, with no new tool unless it is cheap.
2. **Then, in the same sitting, where capacity allows, judged out loud:** entry 1260 §3 step 3 unchanged — the
   `rebuild.py` extension and its establishment test, and **stretch 27's instruction from §L.52**, by copy and change
   from session 35's checked instruction (Ruling B), with Ruling C's orders and ruling 1 (corrected): Claude Code's
   reading list as ruling 1 gives it; **before landing**, the check of which rules of `cowork_handoff.md` lines
   1–255 and of `cowork_audit_protocol.md` line 180 to the end the stretches rely on, each carried into the
   instruction; the three files' sizes and modification times (§1 above) given for Claude Code's session-start read;
   the provenance and the check note kept outside the file Claude Code reads. Until `rebuild.py` is extended, a
   verifying sitting rebuilds with a placement script of its own (`place40.py`'s pattern). It lands the instruction
   unchecked on the user's word. **It does NOT tell the user to hand it to Claude Code.** If capacity does not allow,
   it hands over at a verified stop.
3. **From stretch 27 on:** as entry 1260 §3 step 4 (Ruling A).
4. **Carried:** entry 1260 §3 steps 5 to 8 (ruling 2; ruling 3 and its proposal, still not ruled; ruling 4's timing,
   still not ruled; after Task 5).

**Practical notes, no rules:** as entry 1260 §3, and: (a) entry 1262's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_sixty_two.md`; check by staging; (b) the commit objects of this
stretch are loose objects and stage directly; (c) in this sitting a `cat` of staged git reference files in the
container shell was refused by the environment; the Read tool read them.

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** No instruction is waiting. The instruction to hand stretch 27's
   instruction to Claude Code comes only from the session that checks it (Ruling A).
2. **THE USER opens ONE NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_sixty_one.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   **No other Cowork session is open on this work at the same time.** That session checks by staging that entry 1262
   does not exist (if it does, report and ask); reads this entry whole, entries 1260 and 1259 whole, session 35's
   instruction whole and the README of `tools/audit/stretch_verify/`; makes the session-start read by ruling 2
   against §1's values; reads the three git reference files (they should still read `2226b247…`); asks the user's
   leave for `python3 -I`; then does §3 step 1 (the measurement surface, delivered whole before any choice question,
   one decision per turn), then §3 step 2.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only reads and searches over staged copies; a `mkdir` and a `cp` of the staged scripts into
  a scratch folder; on the user's leave, `python3 -I -B` runs of the established `gitobj.py`, `treediff.py`,
  `blobhash.py`, `blobout.py` and `counts.py`, and of this sitting's own `place40.py` (written with the Write tool in
  that scratch folder); `python3 -I -c` for the negative test's changed copy and the §10/§11 searches (outside the
  staged tree); `cmp`. The opening lines of `treediff.py` and `counts.py` were printed once (`sed -n`), which the
  README does not ask for. One `cat` attempt refused by the environment (§3 note (c)).
- This entry written in the outputs folder with the Write tool and landed with the commit tool, the landing proved by
  staging back and comparing. No git on the device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-27 (Stockholm), the sitting booted on entry 1260. The user's words as §0 gives them.*
