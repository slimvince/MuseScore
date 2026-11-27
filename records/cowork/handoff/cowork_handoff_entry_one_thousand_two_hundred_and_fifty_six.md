# Cowork handoff entry 1256 — 2026-11-27 — SESSION 33'S STRETCH (§L.49) VERIFIED AT THE OBJECTS, NO FINDING; SESSION 34'S INSTRUCTION (§L.50 ONLY) WRITTEN IN THE SAME SITTING AND LANDED UNCHECKED; THREE DEGRADATION TELLS IN THE WRITING, EACH CAUGHT BEFORE LANDING; HANDED OVER

**The current entry point.** Entry 1255 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried, and what he said to this sitting

As entry 1255 §0, unchanged: one question or a handover per message, never both; the two rulings of 2026-11-24 (entry
1221 §0) with Ruling 1 (b) as narrowed (entry 1241 §0, decision 3); decision 1 (the verification scripts one committed
tool, entry 1244 §2 item 1); Claude Code does every git act, pushing included.

**His words to this sitting:** the opening instruction (entry 1255's §4 step 2 line) with Claude Code's closing message
for session 33; "shortened" (the session-start read); "yes" (`python3 -I` in the container, on staged copies only,
scripts outside the staged tree, nothing written to the device by any shell; a later sitting asks again); "yes" (land
session 34's instruction unchecked, Ruling 1 (d)).

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1256 asked for by staging: *"does not
  exist"* (at boot and again before landing). Read whole: entries 1255, 1253, 1254, 1221, 1241 and 1026 (the parts entry
  1255 §4 names, and more); the README of `tools/audit/stretch_verify/`; session 33's instruction (53,557 bytes, as entry
  1255 gives it). `CLAUDE.md` came with the user's second message, whole.
- **Session-start read, shortened:** `STATUS.md` whole (11,726 bytes, 1794136674043, unmoved); `DECISIONS.md` at the
  listing (120,603 bytes, 1794081137207, unmoved); the gating answer at its lines (`open_rows` 247 at lines 26 and 185,
  `non_gating` 25 at line 49, `gating_rows` 222 at line 183, `gating_ids` from line 186).
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `4df88baa673afe9d8225ec270e555474c4f86553` — session 33's report commit.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **Session 34's instruction, WRITTEN, NOT CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_34_task_3_stretch_25_2026_11_27.md`, **46,800 bytes,
    513 lines**, no carriage return, blob `b80f7c687d12bc5962a3cf0c9d62feeeba0b7d50`. The path staged first and found
    free (twice); landed on the user's word; **proved**: staged back and compared byte for byte with the copy sent
    (`cmp`), identical. Untracked.
  - This entry (untracked).
- **Untracked writing-side files for session 34's act 1:** the instruction, this entry 1256, and the checking session's
  entry 1257 — the three paths its §5 act 1 names (entries 1253 to 1255 were landed by session 33's act 1).

## 2. What this sitting established

1. **Session 33's stretch (§L.49) verified at the objects [checked]. No finding.** The established scripts staged and
   read before running (`gitobj.py`, `treediff.py`, `blobhash.py`, `blobout.py`, `counts.py`; `rebuild.py` not staged
   or run); run with `python3 -I -B`.
   - **The chain** (`gitobj.py`): `70f94eb3e28e05923c8dd8d4a54001722fe694a7` (parent `23cf4329…`),
     `9322716cde8ea1d5836a8770159c241b0989a215` (parent `70f94eb3…`), `4df88baa673afe9d8225ec270e555474c4f86553`
     (parent `9322716c…`); one parent each; each subject found word for word, once, in session 33's instruction (by
     script).
   - **The tree changes** (`treediff.py`, every changed path walked to the file): act 1 adds exactly the instruction
     (`07ab4361…`) and entries 1253 (`b8d1fea8…`), 1254 (`f6e1ef5d…`) and 1255 (`20c4726e…`); act 2 changes only the
     reading file `7a06d634…` → `984bca4715f9d535b1ab7ea23a7dbcce4d2545c1`; act 3 adds only the report (`263ae8eb…`).
     The root trees change only under `records/` and `ratification_surfaces/`. Each committed blob equals the file on
     disk (`blobhash.py`).
   - **The rebuild** — by this sitting's own placement script (`place36.py`, written without reading any earlier
     sitting's, kept in the container only; outside `rebuild.py`'s *Limits*, Row 7.110 having an earlier line), from
     the loose object `7a06d634…` and the instruction's own code blocks and §3.5 item 3's line, each insertion point
     asserted: blob `984bca47…`, 5,351,767 bytes, 84,848 line feeds, **IDENTICAL** to the file on disk on the first run;
     the lines at 4846 and 5133; line 54 differing only in §L.48 → §L.49 and §L.49 → §L.50. **Negative test:** one
     character changed in a copy of the instruction's code block; the rebuild printed **DIFFERS**.
   - **Counts** (`counts.py`): 564 / 45 / 53 / 26 / 1 / 1; *as proposed* 128; the thirteen record names 2 / 2 / 2 / 90 /
     8 / 5 / 18 / 12 / 11 / 21 / 17 / 13 / 36 (remaining cadence type first); 5 added and 1 deleted against
     `7a06d634…`, 1,409 and 4 against `48e24b2f…`. §10 80251–81369 and §11 81370–83522, no hit in either (this
     sitting's own look-around search); first hits after §11 at 83627 and 83684. Both quotations each found exactly once
     in the record (`4fda3898…`). The decided-against search: three occurrences, case matched or not.
   - **The report** (`records/cc/reports/cc_report_l3_application_session_33_task_3_stretch_24_2026_11_27.md`, 17,295
     bytes, 205 lines) **read in full**. Checked at the objects: the row headings at 4827 and 5116, the earlier line at
     5131, §6 at 435, §12 at 83523, the two §10 near-hits at 81049 (*"37.110"*) and 81256 (*"37.96"*), the three changed
     passages (54; after 4845; after 5129), act 1's four paths with their line counts. Its declared departures (the pin
     with `-w`, the trailer, searches without look-around, quotation checks by the Grep tool, one combined pattern, a few
     git commands beyond the ordered ones) bear on nothing committed; none a finding under Ruling 1 (b) as narrowed.
2. **Ruling 2's judgment, said to the user before writing:** §L.50 (record 7,197 bytes; 1 line, Row 48.15 **ADOPTED —
   proposed**, the word named in full, step (1) of *Which ADOPTED word*; proposed UNPLACED, so not *as proposed*; row
   shape: proposed paragraph, blank, `---`, no earlier line) fits. **§L.51 does not fit, and the stretch stops before
   it**: its table (big dispatch from line 5414, read by search only) brings a bare *"ADOPTED"* whose word is read at
   the axis (Row 12.35 (iii)) and a **QUARANTINED** line (Row 7.199) with an audit-question entry for §11; judged with
   the sitting already carrying a full verification.
3. **Session 34's instruction, written on session 33's pattern under Ruling 1 (d) [checked at the objects named in its
   §8].** The line: Row 48.15, `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_bass_role_per_event_group_sitting.md,
   Ruling 1).* **ADOPTED — proposed** — "<the record's sentence, lines 32–35>".`; the in-progress line to §L.50. Release
   part 2 record read: Ruling 9 whole (lines 363–420), Ruling 31 whole (lines 1670–1741: L2 Row 49.17 (i) and the twelve
   L2 rows get nothing and no listing of their own). **Settlements, the writing side's and overrulable:** (1) the line
   quotes the sentence alone, not *"with this sentence as the proposal"*, as §L.50's table orders; (2) the record's bold
   over the sentence not carried, as the big dispatch's §L.50 quotes it (lines 5327–5330), its inner full stop kept, its
   closing full stop replaced by the line's own after the closing mark. **No precedent line is relied on for the marks.**
4. **Simulated** twice: directly from the line text, then by a second script of this sitting's own (`place37.py`, kept in
   the container only) from the landed instruction's own code block and §3.5 item 3's line, each insertion point and the
   row's UNPLACED word and THE DERIVATION IS SILENT axis asserted: **blob `bb81f43efed7748073d2a88527b94aae9390e356`**
   (5,352,271 bytes, 84,850 line feeds), the runs byte-identical; the line at 67145; by `counts.py`: 3 added and 1
   deleted against `984bca47…`, 1,411 and 4 against `48e24b2f…`; 565 / 45 / 53 / 26 / 1 / 1, *as proposed* 128; the new
   record name 1, the thirteen others unchanged; §10 80253–81371 and §11 81372–83524, no hit in either, not even a raw
   `48\.15` hit. The quotation found exactly once in the record by script; the record's apostrophes all straight. The
   decided-against search over the record: one occurrence, line 39, case matched or not.
5. **This stretch lies inside `rebuild.py`'s *Limits* as its README states them** (one line from a `*Row 48.15 — 1
   line:*` block, at a row with no earlier line, plus line 54; no §10 or §11 entry). This sitting did not read
   `rebuild.py` itself. The verifying sitting reads it and says whether it uses it or its own placement script.
6. **Degradation tells: three, all in the writing, each caught before landing**, told to the user as *"I have already
   made two of these"*: (a) a claim against the object — the draft first said `rebuild.py` does not cover this stretch;
   its README says it does; (b) a precedent asserted unexamined — the draft and a chat message said earlier lines quoting
   a record's sentence drop its bold, the precedent line's record not checked; the reliance was removed and the chat
   message corrected in the next message; (c) a count asserted, never derived — the record given as 91 lines; it has 90
   (`blobhash.py`). Hence the handover at this verified stop. **On the model (2026-11-12):** all three came late, in the
   writing, after a full verification; nothing here separates load from model, so no suspicion about Opus is raised.

## 3. The plan — carried forward

1. **Now: a NEW Cowork session CHECKS session 34's instruction** as a turn of its own (Ruling 1 (e)), on the pattern of
   entry 1255 §2: every hash re-derived (the commits `4df88baa…`, `9322716c…`, `4b6dc3bd…`; the tip's tree walked to the
   reading file `984bca47…` and the archive JSON `1df4f207…`; the big dispatch; the record `a6cad94c…`; the release
   part 2 record `441e0d01…`); §L.50's record whole; the release part 2 record's Rulings 3, 9 and 31 whole; §L.50 whole
   (big dispatch lines 5310–5413); form (b) with *Which ADOPTED word*, the two-record rule and the split-row sentence;
   Task 3 (c) items 1, 5, 6 and 7; the words section's *A ruled line*; the row found once and read whole (shape,
   UNPLACED, the axis, the fit); the settlements — judged, and put to the user only where the record does not settle
   them; the §10/§11 searches; `cowork_handoff.md`'s topmost block and `cowork_audit_protocol.md`'s dispatch-protocol
   section at their bounds; the read ranges given to Claude Code at their bounds; and **a re-simulation by its own
   placement script or the established `rebuild.py`** (read first), which should give `bb81f43e…`. Its entry is
   **1257**, as the instruction names it (it checks by staging that 1257 is free). It corrects what it finds (former
   wordings kept or not, the instruction being unreleased), records its check in a note at the end of the instruction's
   §8 and sets the banner to CHECKED, lands, and **only it tells the user what to hand to Claude Code**. It needs the
   user's leave for `python3 -I`, and for any shell copy into the outputs folder (entry 1255 §3 note (b)).
2. **Then Claude Code executes session 34's instruction:** lands it and entries 1256 and 1257 (act 1), applies §L.50
   (act 2), writes `records/cc/reports/cc_report_l3_application_session_34_task_3_stretch_25_2026_11_27.md` (act 3),
   stops.
3. **Then a NEW Cowork session verifies stretch 25** with the established scripts (and `rebuild.py`, if it judges the
   stretch inside its *Limits* after reading it), the report read in FULL, Ruling 1 (b) as narrowed; then, under Rulings
   1 and 2, writes the next stretch's instruction from §L.51 (§2 item 2's remarks are this sitting's reading, to be
   re-judged at the objects), or hands over on two tells.
4. **After the L3 application's Task 5 has closed:** as entry 1254 §3 step 3.
5. **Carried to their acts:** as entry 1254 §3 step 4. **Later:** as entry 1194 §3 step 2. **Open with the user, not
   ruled:** as entry 1211 §3 step 2; and the duplicate of entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above and entry 1221 §0 with Ruling 1 (b) as narrowed. **Practical notes, no
rules:** as entries 908 and 910 to 1255 §3, and: (a) the Grep tool was not offered; read-only `grep`, `sed -n`, `cut`,
`cmp` in the container shell on staged copies served; (b) loose objects staged by full path; an abbreviated hash
(`e7874284`) given as a path was refused by staging — take the full hash from the parent commit's text first; (c) entry
1257's file name would be `cowork_handoff_entry_one_thousand_two_hundred_and_fifty_seven.md`; check by staging.

## 4. Who does what, in this order

1. **THE USER opens ONE NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_fifty_six.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   **No other Cowork session is open on this work at the same time.** That session checks by staging whether an entry
   1257 exists (if it does, report and ask); reads this entry whole, entry 1255 whole (the checking pattern, §2), entry
   1221 §0, entry 1241 §0, entry 1026 §3, `tools/audit/stretch_verify/README.md` whole and session 34's instruction
   whole; asks the session-start read; reads the three git reference files (they should still read `4df88baa…`); asks the
   user's leave for `python3 -I`; then does §3 step 1.
2. **Nothing goes to Claude Code from this entry.** The instruction to hand session 34's instruction to Claude Code
   comes only from the session that checks it (Ruling 1 (e); the user's rule of 2026-10-26).
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies (`grep`, `sed -n`, `cut`, `cmp`, `cat` of the staged scripts to
  read them), and, on the user's leave, `python3 -I -B` runs of the staged `gitobj.py`, `treediff.py`, `blobhash.py`,
  `blobout.py` and `counts.py` (each read first; `rebuild.py` not staged or run) and of this sitting's own scripts
  (`place36.py`, `place37.py`, written with the Write tool in a scratch folder outside the staged tree; the direct
  simulation, the searches, the quotation checks and the negative test's changed copy by `python3 -I -c`). Outputs only
  in scratch folders in the container. Nothing written by any shell into a staged copy, the outputs folder or the
  device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the three git reference files; the five scripts; the
  commits `70f94eb3…`, `9322716c…`, `4df88baa…`, `23cf4329…`, their root trees and the trees down every changed path;
  the loose blobs `7a06d634…` and `48e24b2f…`; the reading file; session 33's report; §L.49's record; the big dispatch;
  §L.50's record; the release part 2 record. **Listed:** the repository root. Paths asked for by staging and found free:
  entry 1256 (twice), session 34's instruction path (twice). One staging call refused for an abbreviated hash given as a
  path (§3 note (b)); nothing staged by it.
- **Messages sent with the user-message tool** (none a question): the verification result; the Ruling 2 judgment (its
  sentence on precedent lines corrected in the next message, §2 item 6 (b)). The draft instruction sent as a file.
- **Session 34's instruction and this entry written in the outputs folder with the Write and Edit tools; both landed
  with the commit tool**, each landing proved by staging back and comparing. No git on the device, widget, task list,
  subagent, memory write or web access.

*Provenance: Cowork, 2026-11-27 (Stockholm), the sitting booted on entry 1255. The user's words: the opening
instruction with Claude Code's closing message; "shortened"; "yes" (`python3 -I`); "yes" (land the draft unchecked).*
