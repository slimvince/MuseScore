# Cowork handoff entry 1218 — 2026-11-24 — SESSION 18 (§L.31) VERIFIED AT THE OBJECTS: NO FINDING; THE READING FILE REBUILT INDEPENDENTLY AND BYTE-IDENTICAL; §L.32 IS THE NEXT WRITING SESSION'S

**The current entry point.** Entry 1217 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rule of 2026-11-24, carried

**A message to the user either asks him ONE question or hands over to another session — NEVER BOTH** (entry 1215 §0).
This sitting asked one question (the session-start read) and hands over in a later message.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1218 asked for by staging, in a call of
  its own, before any other boot read: *"does not exist"*; asked once more, in a call of its own, immediately before this
  entry was written. Entry 1217 (10,684 bytes), entry 1216 (10,910) and entry 1026 (11,103) read whole.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` read whole (11,726 bytes,
  1794136674043, unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207,
  unmoved; the gating answer 247 open, 222 gating, 25 non-gating (`tools/audit/nongating_apparatus_rows.json` lines
  183–185). `CLAUDE.md` came with the user's second message, whole.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `f1e7c9144b9f78b0287f12a5573cb8523263fd6d` (modification times 1795506176897 and
  1795506179415) — exactly the tip Claude Code's closing message reported. Nothing is running; no dispatch is out.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only (untracked). **Untracked writing-side entries: 1218.**

## 2. What this sitting established — entry 1217 §3 step 2, done

1. **The chain [checked, at the loose objects, each SHA-1 recomputed from the decompressed object]:** `03a15953…` →
   `93695bde8e80b844eba3b8af1ed377536bd824d8` (act 1) → `51543b657ed1d3777f25812abede359615816369` (act 2) →
   `f1e7c9144b9f78b0287f12a5573cb8523263fd6d` (act 3), one parent each. Each subject found, backticked and exact, in
   the instruction (§5 act 1, §4 item 8, §5 act 3).
2. **The tree changes [checked, by walking the tree objects]:** act 1 adds exactly five files — the instruction at blob
   `6cc7f8be…` and entries 1214 (`0cbbaed2…`), 1215 (`92f68e5f…`), 1216 (`8731cc77…`), 1217 (`df32bd47…`) — each blob
   equal to the file on disk; act 2 changes only `ratification_surfaces/cowork_comparison_l3_reading.md`, `b98e8512…`
   → `27e0d551…`, equal to the file on disk; act 3 adds only
   `records/cc/reports/cc_report_l3_application_session_18_task_3_stretch_9_2026_11_24.md` (`c4b2d9b7…`), equal to the
   file on disk. No other path changes in any of the three.
3. **The reading file rebuilt independently [checked]:** from blob `b98e8512…` (decompressed, SHA-1 verified), by this
   sitting's own script from the instruction's §3.2, §3.3 and §3.5 item 3 text and §3.1 item 2's placement rule: **byte-
   identical to blob `27e0d551…` and to the file on disk** (5,286,365 bytes, 84,486 lines). Against `b98e8512…`: 25
   lines added, 1 deleted. `*RULED DISPOSITION (` at line start 438; the part-1 record named 13 times, the lead-rows
   record 23. The rows' shapes as the script met them: earlier ruled lines skipped at Row 8.52 (one) and Row 44.34
   (two); the new lines above *"The decisions register at this row."* at Rows 44.28 and 44.37; `---` after the rest.
4. **The report read in FULL [checked]** (21,196 bytes, 263 lines): it covers §6 items 1 to 9; its eleven line numbers
   and the two §10 line numbers (80644, 80645) were each checked at the rebuilt file and hold. Its nine declared
   departures were read; none bears on the result.
5. **The untracked duplicate [checked, not acted on]:**
   `records/cc/instructions/cc_instruction_l3_application_session_18_task_3_stretch_9_2026_11_24-1.md` is byte-
   identical to the instruction (`cmp`; blob `6cc7f8be…`). Its modification time, 1795504941270, lies between the
   draft's landing (1795504356703) and the corrected instruction's (1795505574857); how it came to exist is **not
   established**. It is in no commit. Whether to remove it is the user's; this sitting did not touch it.
6. **No finding against Claude Code's work.** Nothing was corrected.
7. **One slip of this sitting's own, caught before use:** the rebuild script's first run dropped *", Ruling 1"* from one
   §10 entry (a `.replace` bound to the last string literal only); the byte comparison exposed it, the script was fixed
   and re-run, and only the fixed run's result is stated above. Counted as one degradation tell (a refuted shortcut). No
   second. **On the model (2026-11-12):** nothing here suggests Opus was not enough.

## 3. The plan — carried forward

1. **Next: a NEW Cowork session writes §L.32's instruction** (session 19; 24 row-parts: 14 lines, a three-line
   row-part, 4 RELOCATED parts, as entries 1216 and 1217 carry it), sized at the objects, on the pattern of session
   18's instruction. It is **checked as a turn of its own** before it is handed over, by a session that did not write
   it, as sessions 17 and 18's were.
2. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   §2 item 5.

**Carried rules:** as entry 1026 §3, and §0. **Practical notes, no rules:** as entries 908 and 910 to 1217 §3, and:
(a) the scripts `obj.py`, `tree.py`, `blob.py`, `subj.py`, `rebuild.py` are not carried (fresh container); the rebuild
logic is entry 1216 §3 note (a); (b) the reading file's `##` headings at blob `27e0d551…`: §6 at 435, §7 79457, §10
79915, §11 81008, §12 83161 [checked, at the rebuilt copy, which is byte-identical to the file];
(c) the big dispatch's §L.31 *Open* line citations noticed stale by entry 1217 §2 item 4 stay noticed, not acted on;
(d) entry 1219's file name would be `cowork_handoff_entry_one_thousand_two_hundred_and_nineteen.md`; check by staging.

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** §L.32's instruction is not written. Only the session that checks it
   tells the user what to hand to Claude Code.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_eighteen.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1219 exists (if it does, report and ask), reads this entry whole,
   entry 1217 whole and entry 1026 §3, asks the session-start read, reads the three git reference files (both at
   `f1e7c914…` when this entry was written; anything else means something ran: find out what first), then does §3
   step 1.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only measurements over staged copies (`python3 -I` decompressing git objects and
  recomputing their SHA-1, walking trees, computing blobs, comparing subjects, rebuilding the reading file; `cmp`,
  `grep`, `sed -n`, `wc`, `diff`, `cut`). Written in the container: five helper scripts and two copies of the reading
  file (`old.md`, `rebuilt.md`) under `/home/claude/scr`. Nothing written by any shell into the repository or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the git reference files; the three commit objects, the
  parent commit `03a15953…`, and the tree objects on the changed paths; the instruction and its `-1` duplicate; entries
  1214 and 1215; the report; the reading file; blob `b98e8512…`. **Listed:** the repository root; `.git/objects/93`,
  `/51`, `/f1`.
- **Read beyond the boot list:** the instruction at lines 140–464; the report whole; the reading file by script and
  search only.
- **This entry written in the outputs folder** with the Write and Edit tools and landed with the commit tool. **Landed
  three times:** the first send carried the copy from before an edit to §3 note (b) (the edit had not yet reached the
  stored file); staging back exposed it by `cmp`, and the second send, guarded by the first's modification time, landed
  the edited copy, proved identical. This sentence was then added and landed the same way, guarded and proved. No git
  on the device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1217. The user's words: the opening
instruction with Claude Code's closing message; "shortened".*
