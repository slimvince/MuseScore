# Cowork handoff entry 1251 — 2026-11-25 — SESSION 31'S STRETCH (§L.46) VERIFIED AT THE OBJECTS, NO FINDING; CLAUDE CODE'S ORDER-OF-ACTS SLIP JUDGED NOT A STOP; SESSION 32'S INSTRUCTION (§L.47 AND §L.48) WRITTEN IN THE SAME SITTING AND LANDED UNCHECKED; TWO DEGRADATION TELLS; HANDED OVER TO THE CHECKING SESSION

**The current entry point.** Entry 1250 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried, and what he said to this sitting

As entry 1250 §0, unchanged: one question or a handover per message, never both; the two rulings of 2026-11-24 (entry
1221 §0) with Ruling 1 (b) as narrowed (entry 1241 §0, decision 3, read at its source by this sitting); decision 1 (the
verification scripts one committed tool, entry 1244 §2 item 1); Claude Code does every git act, pushing included.

**His words to this sitting:** the opening instruction (entry 1250's §4 step 2 line) with Claude Code's closing message
for session 31; "shortened" (the session-start read); "yes" (`python3 -I` in the container, on staged copies only,
scripts outside the staged tree, nothing written to the device by any shell; a later sitting asks again); "yes" (land
session 32's instruction unchecked, Ruling 1 (d)). No report from the external audit came with the opening.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1251 asked for by staging: *"does not
  exist"*. Read whole: entries 1250, 1249, 1221 and 1026 (§0 and §3 carried); the README of
  `tools/audit/stretch_verify/`; session 31's instruction (58,674 bytes, as entry 1250 gives it); entry 1241 §0.
- **Session-start read, shortened:** `STATUS.md` whole (11,726 bytes, 1794136674043, unmoved); `DECISIONS.md` at the
  listing (120,603 bytes, 1794081137207, unmoved); the gating answer at its lines (`open_rows` 247 at lines 26 and 185,
  `non_gating` 25 at line 49, `gating_rows` 222 at line 183, `gating_ids` from line 186).
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `4fa74ea2094c1f8c353d19b7fe35fe059e364ccd` — session 31's report commit.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **Session 32's instruction, WRITTEN, NOT CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_32_task_3_stretch_23_2026_11_25.md`, **54,805
    bytes, 582 lines**, no carriage return, blob `696cbd03290416b833cdcc43d8b16534381f1a8c`. The path staged first and
    found free; landed on the user's word; **proved**: staged back and compared byte for byte with the copy sent,
    identical. Untracked.
  - This entry (untracked).
- **Untracked writing-side files for session 32's act 1:** this entry 1251, the instruction, and the checking session's
  entry 1252 (named in the instruction at §1 check 5, §2 item 4, §4 item 3 and §5 act 1 with its subject).

## 2. What this sitting established

1. **Session 31's stretch (§L.46) verified at the objects [checked]. No finding.** The scripts staged; their blobs equal
   to those entry 1249 gives (README `1bcf458e…`, `blobhash.py` `fb45e467…`, `blobout.py` `d0154de7…`, `counts.py`
   `e79b3d88…`, `gitobj.py` `dd5db100…`, `treediff.py` `4250839d…`; `rebuild.py` not staged or run); read before running;
   run with `python3 -I -B`.
   - **The chain** (`gitobj.py`): `7539cb4f8d60d648ad68fb653240630c03337780` (parent `371fe649…`),
     `b2f5fe446b79a9cc903b52b7dbd2f021e3e7600a` (parent `7539cb4f…`), `4fa74ea2094c1f8c353d19b7fe35fe059e364ccd`
     (parent `b2f5fe44…`); one parent each; each subject found word for word, once, in session 31's instruction.
   - **The tree changes** (`treediff.py`, every changed path walked to the file): act 1 adds exactly the instruction
     (`ebb90b60…`), entry 1249 (`2340b747…`) and entry 1250 (`d48694a2…`), `ratification_surfaces/` unchanged; act 2
     changes only the reading file `a11b732d…` → `d8139936…`; act 3 adds only the report (`20a7b49d…`). Each committed
     blob equals the file on disk (`blobhash.py`).
   - **The rebuild** — by this sitting's own placement script (`place22.py`, written without reading any earlier
     sitting's, kept in the container only; outside `rebuild.py`'s *Limits*), from the loose object `a11b732d…` and the
     instruction's own code blocks, each insertion point asserted: blob `d81399363f717fefad3a6a88c0780481999a2e3e`,
     5,349,632 bytes, 84,837 line feeds, **IDENTICAL** to the file on disk on the first run; the 6 lines at 5250, 55069,
     55187, 55189, 55688, 72701 and the entries at 80323 and 81346.
   - **Counts** (`counts.py`): 559 / 45 / 53 / 26 / 1 / 1; *as proposed* 128; record names 8 / 5 / 18 / 12 / 11 / 21 /
     17 / 13 / 36; 15 added and 1 deleted against `a11b732d…`, 1,398 and 4 against `48e24b2f…`; eight changed passages;
     line 54 differing only in §L.45 → §L.46 and §L.46 → §L.47. §10 80241–81358 with hits at 80293, 80323, 80404,
     80785, 80793 and 81346; §11 81359–83511, none (this sitting's own look-around search).
   - **The report**
     (`records/cc/reports/cc_report_l3_application_session_31_task_3_stretch_22_2026_11_25.md`, 21,367 bytes, 245
     lines) **read in full**. Checked at the objects: its line numbers and diff table; the L0 block's last line before
     the edit (`  unmarked.)*`, line 80310 of `a11b732d…`) and the style-system block's last entry (Row 23.41, line
     81332); its next hit after §11 at 83707, inside §12 (heading at 83512); act 1's 947 insertions (633 + 136 + 178).
   - **Claude Code's declared departures**, judged under Ruling 1 (b) as narrowed (entry 1241 §0, decision 3, read at
     its source: a verifying sitting STOPS on a discrepancy in the committed files or the instruction, on a failed
     check, or on anything it cannot account for). **(a) The reading file edited before act 1** (its report §7 item 1),
     against §5 act 1's *"Make NO edit to the reading file before act 1's commit is made and pushed"*, the edits then
     reversed and the file proved at `a11b732d…` before act 1. **Not a STOP:** none of the three conditions holds, at
     the objects — act 1's tree leaves `ratification_surfaces/` unchanged, act 2 starts from `a11b732d…` and gives the
     expected blob, and the not-yet-touched check before act 1 ran and held. Recorded here; session 32's instruction
     opens §5 with a rule that the reading file is opened by no Edit or Write call until act 1's push is verified, and
     asks the report to say so (§6 item 1). Told to the user, overrulable. (b) `git hash-object -w` at the pin; (c) the
     check script over git-object copies; (d) the search without look-around; (e) the `Co-Authored-By` trailer: as
     sessions 29 and 30, none a finding.
2. **Ruling 2's judgment, said to the user before writing:** §L.47 (record 4,680 bytes; 4 rows; 1 line, RELOCATED to
   L2, form (b), and 1 §10 entry under an existing heading; 3 rows held by Ruling 11 with no line) fits; §L.48 (record
   5,589 bytes; 2 lines, form (b-H), given verbatim by Ruling 10) fits; **§L.49 does not, and the stretch stops before
   it**: its record is small (6,076 bytes, 2 lines), but both lines are HISTORICAL for only part of the row (*"in so far
   as"*), a kind whose precedent would have to be found and checked, and the sitting had carried a full verification
   (Ruling 2 (c)). §L.49 was read at its opening and table only.
3. **Session 32's instruction, written on session 31's pattern under Ruling 1 (d) [checked at the objects named in its
   §8].** The lines and their grounds:
   - Row 7.47: **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.***, form (b), quoting the
     record's Ruling 1 (lines 37–39), the two sentences §L.47's table quotes (Ruling 11: the line carries *"it does not
     foreclose DP-O"*); the shape of the reading file's earlier ruled RELOCATED lines to that charter (e.g. its lines
     1303, 4887, 4908) — a settlement, overrulable, as is the quotation's handling (italics dropped, inner quotation
     marks kept). §10 entry under the L2 heading (line 80444), after the block's last entry (Row 57.514, line 80983);
     the subject clause the writing side's.
   - Rows 19.39 (ii) and 57.511: **HISTORICAL**, form (b-H), each line exactly Ruling 10's (release part 2 record lines
     451 and 453). Both also named by the disposition-words record (*"stay UNPLACED; the act marks them
     STOP-and-report"*), answered by Ruling 10: no line from it, no STOP; listed under *rows named by more than one
     record* with both records' words. Row 19.39 already carries the disposition-words record's line on claim (iv);
     different parts.
   - Rows 7.48 (i), 7.294 (v), 7.331: no line, each proposed UNPLACED at the row, listed in the report as *held by
     ruling* (Ruling 11). Row 10.123: no line, no listing (Ruling 17). Row 3.3: §L.12's, nothing here.
   - Every proposed word at the parts named is UNPLACED, so no line says *as proposed*. Each quotation found exactly once
     in its record by script; the decided-against search: §L.47's record none, §L.48's record two hits (lines 25 and 29),
     case matched or not. Nothing at §11.
4. **Simulated** by this sitting's own placement script (`place23.py`, kept in the container only; outside
   `rebuild.py`'s *Limits*: a row with an earlier line, a §10 entry, rows named by two records), from the instruction's
   own code blocks, each insertion point asserted: **blob `7a06d634f65fc18614adba312426677682115367`** (5,351,019 bytes,
   84,844 line feeds); by `counts.py`: 8 added and 1 deleted against `d8139936…`, 1,405 and 4 against `48e24b2f…`;
   562 / 45 / 53 / 26 / 1 / 1, *as proposed* 128; the two new record names 2 each, the disposition-words 90, the other
   nine unchanged; lines at 4050, 25090, 76453, the entry at 80990; §10 80247–81365 with five hits (80336, 80485,
   80525, 80652, 80990), §11 81366–83518 with none. **Re-run on the final text, after the self-check's edits:** the same
   file, byte for byte.
5. **Degradation tells: two**, both in the draft, both caught in the self-check before anything was landed: (1) a
   quotation of the disposition-words record attributed to §L.2's settled note, where §L.48 quotes it (big dispatch line
   5145); (2) Row 3.3's line called *"written by an earlier stretch"*, unchecked at the reading file (narrowed to §L.12
   placing it, as §L.47's text says). Told to the user as two; this sitting ends at this verified stop, its work done, in
   any case (Ruling 1 (e)). **On the model (2026-11-12):** both came late in a sitting that carried a full verification
   and a full writing; nothing separates load from model, so no suspicion about Opus is raised.

## 3. The plan — carried forward

1. **In parallel, independent of the steps below:** the external audit, as entry 1247 §3 step 1 and §2 item 5 give it.
   Its report, when the user brings it, is an untrusted source and evidence, not a ruling: a Cowork session reads it in
   full, checks each finding at the objects, and puts to the user what it bears on, judged against the plan.
2. **Now: a NEW Cowork session CHECKS session 32's instruction** as a turn of its own (Ruling 1 (e)), on the pattern of
   entry 1250 §2: every hash re-derived; both records whole; the release part 2 record's Rulings 3, 10, 11 and 17 whole
   (this sitting read 10, 11 and 17 whole, 3 at its heading only); §L.47 and §L.48 whole; forms (b) and (b-H) with the
   two-record rule and the split-row sentence; §L.2's lines 484–505; Task 3 (c) items 5 to 7; the 6 rows each found once
   and read whole (shape, the earlier line, UNPLACED, fit; the 3 held rows' parts); §10's L2 block; the settlements (Row
   7.47's line shape and quotation handling; the §10 subject clause) — each judged, and put to the user only where the
   record does not settle it; the §10/§11 searches; `cowork_handoff.md`'s topmost block and `cowork_audit_protocol.md`'s
   dispatch-protocol section at their bounds; the new §5 opening rule against act 1's wording; and **a re-simulation by
   its own placement script**, which should give `7a06d634…`. It adds its entry 1252 (already named in the
   instruction), corrects what it finds, lands, and **only it tells the user what to hand to Claude Code**.
3. **Then Claude Code executes session 32's instruction; then a NEW Cowork session verifies stretch 23** with the
   established scripts for the chain, the tree changes, the counts and the blobs, and its own placement script for the
   rebuild (or `rebuild.py` extended and established again first, as the README says — the verifying sitting says
   which), and, under Rulings 1 and 2, writes the next stretch's instruction from §L.49, or hands over on two tells.
4. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above and entry 1221 §0 with Ruling 1 (b) as narrowed. **Practical notes, no
rules:** as entries 908 and 910 to 1250 §3, and: (a) a placement script for rows with earlier lines skips, after the
proposed paragraph's blank, every `*RULED`/`*RECORDED` line with its blank, and asserts `---` or `*At the source now.*`
follows; a §10 entry goes before the first blank line after the block's heading-and-blank, asserted to be followed by
the next `**To ` heading; (b) a print of more than about 30 KB from the container shell is cut off — print narrower
ranges; (c) entry 1252's file name would be `cowork_handoff_entry_one_thousand_two_hundred_and_fifty_two.md`; check by
staging.

## 4. Who does what, in this order

1. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_fifty_one.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   (If the external audit's report is ready by then, the user may attach it; the session reads it in full after its
   boot and treats it as §3 step 1 says.) That session checks by staging whether an entry 1252 exists (if it does,
   report and ask), reads this entry whole, entry 1250 whole (the checking pattern, §2), entry 1221 §0, entry 1241 §0,
   entry 1026 §3, `tools/audit/stretch_verify/README.md` and session 32's instruction whole, asks the session-start
   read, reads the three git reference files (they should still read `4fa74ea2…`), asks the user's leave for
   `python3 -I`, then does §3 step 2.
2. **Nothing goes to Claude Code from this entry.** The instruction to hand session 32's instruction to Claude Code
   comes only from the session that checks it (Ruling 1 (e); the user's rule of 2026-10-26).
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies (`grep`, `sed -n`, `awk`, `cut`, `cmp`, `diff`), and, on the
  user's leave, `python3 -I -B` runs of the staged `gitobj.py`, `treediff.py`, `blobhash.py`, `blobout.py` and
  `counts.py` (each read with the Read tool first; `rebuild.py` not run) and of this sitting's own scripts (`place22.py`
  written with the Write tool, `place23.py` and `check23.py` by heredoc, all in a scratch folder outside the staged
  tree; short ones by `-c` or standard input). One command printed more than the tool returns (a `grep` for Task 3's
  headings that matched the big dispatch's very long line 52); the part needed was read with the Read tool instead. Outputs only in the container, except the
  instruction's placeholders filled by a `python3 -I` script in the outputs folder (the draft, before landing). Nothing
  written by any shell into a staged copy or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the three git reference files; the six script files;
  the commits `371fe649…`, `7539cb4f…`, `b2f5fe44…`, `4fa74ea2…`, their root trees and the trees down every changed path;
  the loose blobs `a11b732d…` and `48e24b2f…`; the reading file; session 31's report; entry 1241; the big dispatch; the
  records of §L.47, §L.48 and §L.49 (the last for its size and table only); the release part 2 record. **Listed:** the
  repository root; `tools/audit/stretch_verify/`. Paths asked for by staging and found free: entry 1251 (twice),
  session 32's instruction path.
- **Session 32's instruction and this entry written in the outputs folder with the Write and Edit tools; both landed
  with the commit tool**, each landing proved by staging back and comparing. Two messages sent with the user-message
  tool (the verification result; the Ruling 2 judgment; neither a question) and the draft sent as a file. No git on the
  device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-25 (Stockholm), the sitting booted on entry 1250. The user's words: the opening
instruction with Claude Code's closing message; "shortened"; "yes" (`python3 -I`); "yes" (land the draft).*
