# Cowork handoff entry 1249 — 2026-11-25 — SESSION 30'S STRETCH (§L.45) VERIFIED AT THE OBJECTS, NO FINDING; SESSION 31'S INSTRUCTION (§L.46 ONLY) WRITTEN IN THE SAME SITTING AND LANDED UNCHECKED; ONE DEGRADATION TELL; HANDED OVER TO THE CHECKING SESSION

**The current entry point.** Entry 1248 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried, and what he said to this sitting

As entry 1248 §0, unchanged: one question or a handover per message, never both; the two rulings of 2026-11-24 (entry
1221 §0) with Ruling 1 (b) as narrowed (entry 1241 §0, decision 3); decision 1 (the verification scripts one committed
tool, entry 1244 §2 item 1); Claude Code does every git act, pushing included.

**His words to this sitting:** the opening instruction with Claude Code's closing message for session 30; "shortened"
(the session-start read); "yes" (`python3 -I` in the container, on staged copies only, scripts outside the staged tree,
nothing written to the device by any shell; a later sitting asks again); "yes" (land session 31's instruction
unchecked, Ruling 1 (d)). No report from the external audit came with the opening.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1249 asked for by staging: *"does not
  exist"*. Read whole: entries 1248, 1247, 1221 and 1026 (§0 and §3 carried); the README of
  `tools/audit/stretch_verify/`; session 30's instruction (51,269 bytes, as entry 1248 gives it).
- **Session-start read, shortened:** `STATUS.md` whole (11,726 bytes, 1794136674043, unmoved); `DECISIONS.md` at the
  listing (120,603 bytes, 1794081137207, unmoved); the gating answer at its lines (`open_rows` 247 at lines 26 and 185,
  `non_gating` 25 at line 49, `gating_rows` 222 at line 183, `gating_ids` from line 186). `CLAUDE.md` came with the
  user's second message, whole.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `371fe649373d5003dcc4b67c4291cf1ed9ed06b2` — session 30's report commit.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **Session 31's instruction, WRITTEN, NOT CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_31_task_3_stretch_22_2026_11_25.md`, **54,139
    bytes, 593 lines**, no carriage return, blob `35037a6531b94c83f1f7f60e4c4233f80535757a`. The path staged first and
    found free; landed on the user's word; **proved**: staged back and compared byte for byte with the copy sent,
    identical. Untracked.
  - This entry (untracked).
- **Untracked writing-side files for session 31's act 1:** this entry 1249, the instruction, and the checking
  session's entry 1250 (named in the instruction at §1 check 5, §2 item 4, §4 item 3 and §5 act 1 with its subject).

## 2. What this sitting established

1. **Session 30's stretch (§L.45) verified at the objects [checked]. No finding.** The scripts staged; their blobs
   equal to the entries of the committed folder tree `9977ce1c…` at the tip (README `1bcf458e…`, `blobhash.py`
   `fb45e467…`, `blobout.py` `d0154de7…`, `counts.py` `e79b3d88…`, `gitobj.py` `dd5db100…`, `rebuild.py` `d994c92f…`,
   `treediff.py` `4250839d…`); read before running; run with `python3 -I -B`.
   - **The chain** (`gitobj.py`): `5f02d6c1d4c2a93c4e3f8fa6287da2ccc52d2845` (parent `55784918…`),
     `d373bbe9370c0df45c51c23172f518d9e9943c53` (parent `5f02d6c1…`), `371fe649373d5003dcc4b67c4291cf1ed9ed06b2`
     (parent `d373bbe9…`); one parent each; each subject found word for word, once, in session 30's instruction.
   - **The tree changes** (`treediff.py`, every changed path walked to the file): act 1 adds exactly the instruction
     (`7bb28568…`), entry 1247 (`e0f9247b…`) and entry 1248 (`4f6506c5…`); act 2 changes only the reading file
     `d53e8247…` → `a11b732d…`; act 3 adds only the report (`3b94cf1a…`). Each committed blob equals the file on disk
     (`blobhash.py`).
   - **The rebuild** (`rebuild.py` from the loose object `d53e8247…` and the instruction's own text): each of the 5
     lines placed directly before *At the source now.*; blob `a11b732d…`, 5,347,540 bytes, 84,823 line feeds,
     **IDENTICAL** to the file on disk on the first run.
   - **Counts** (`counts.py`): 553 / 45 / 53 / 26 / 1 / 1; *as proposed* 128; record names 5 / 18 / 12 / 11 / 21 / 17 /
     13 / 36; 11 added and 1 deleted against `d53e8247…`, 1,384 and 4 against `48e24b2f…`. The lines at 74695, 76302,
     76334, 76367, 76400; §10 80229–81344 and §11 81345–83497, no hit for the five row numbers in either (this
     sitting's own look-around search); the last hit in the file at line 80205.
   - **The report**
     (`records/cc/reports/cc_report_l3_application_session_30_task_3_stretch_21_2026_11_25.md`, 14,123 bytes, 175
     lines) **read in full**. Checked at the objects: its diff table's old line numbers (each the row's *At the source
     now.* line in `d53e8247…`); line 54 before and after (§L.44/§L.45 → §L.45/§L.46); Ruling 30's lines 1639–1640 of
     the release part 2 record (blob `441e0d01…`); the record's line 29 (blob `ec098d67…`).
   - **Claude Code's declared departures**, judged under Ruling 1 (b) as narrowed: `git hash-object -w` at the pin
     (wrote the same object the commit stores); the search without look-around (the instruction allows it); the
     `Co-Authored-By` trailer (as session 29's commits). None is a finding.
2. **Ruling 2's judgment, said to the user before writing:** §L.46 (record 6,478 bytes; 6 row-parts on 5 rows; 6
   lines of five kinds and 2 §10 entries; three rows already carrying an earlier line) is the stretch alone. §L.47 was
   **not** read for the judgment; the stretch stops before it on Ruling 2 (c), a tell having appeared (item 5).
3. **Session 31's instruction, written on session 30's pattern under Ruling 1 (d) [checked at the objects named in its
   §8].** The six lines and their grounds:
   - Rows 7.116 (ii) and 40.6: **HISTORICAL**, form (b-H), quoting the record's line 30; Row 40.6's line quotes *"as
     7.116 (ii)"* then that sentence, joined by a colon (a settlement, overrulable). Both rows already carry a
     HISTORICAL line quoting the disposition-words record, written when §L.2 was applied (big dispatch lines 484 and
     487–499); same part, same word: each record's line written, in ledger order, §L.46's after the earlier one.
   - Row 40.12 (iii): **RELOCATED to *L0 — The notated record***, byte for byte Ruling 33's line (release part 2
     record line 1848; compared by script). §10 entry under the L0 heading.
   - Row 40.12 (iv): **RELOCATED — outside the framework**, byte for byte the working list's item (xxxviii) as the big
     dispatch quotes it at line 4908, with `(iv) ` added under form (b)'s split-row sentence, as §L.46's table says
     *"The line names claim (iv) only"* (a settlement, overrulable). §10 entry under the style-system heading, which
     exists (Task 3 (c) item 5's exception); no heading made.
   - Row 40.40 (iii): **HISTORICAL**, quoting the record's whole cell *"HISTORICAL — a status"* (a settlement,
     overrulable). The row already carries §L.23's line on claim (ii); different parts.
   - Row 56.24: **ADOPTED — carried** (L3-S9 (i)), *Which ADOPTED word* rule (1).
   - Every quotation found exactly once in the record by script; the decided-against search: three hits, lines 30, 41,
     42, as §L.46 says. No line says *as proposed* (every part proposed UNPLACED).
   - **A wrong citation in the big dispatch, recorded, not fixed:** §L.46's *"§L.23's table line 2393"* — line 2393 is
     blank, §L.23's heading is at 2398 and it takes Row 40.40 (ii) by cut at line 2432. The fact holds at the row. The
     instruction tells Claude Code it is not a STOP. Not edited: every instruction pins the big dispatch by its blob.
4. **Simulated** by this sitting's own placement script (`place46.py`, kept in the container only), **not by
   `rebuild.py`**: the stretch is outside its *Limits* on three counts (rows with earlier lines, §10 entries, rows named
   by two records). Each insertion point asserted at its object. **Blob `d81399363f717fefad3a6a88c0780481999a2e3e`**
   (5,349,632 bytes, 84,837 line feeds); 15 added and 1 deleted against `a11b732d…`, 1,398 and 4 against `48e24b2f…`;
   counts 559 / 45 / 53 / 26 / 1 / 1, *as proposed* 128, the phrase-end record 8, the other eight names unchanged;
   lines at 5250, 55069, 55187, 55189, 55688, 72701; entries at 80323 and 81346; §10 80241–81358 with six hits (as the
   instruction's §3.3 lists), §11 81359–83511 with none. **Re-run from the instruction's own final text** (lines and
   entries extracted from its code blocks): the same blob, byte-identical.
5. **Degradation tells: one.** The first draft of Row 40.12 (iii)'s line took its bold form from older lines
   (`**RELOCATED** to ***L0 — …***`) where a ruled text existed (Ruling 33's `**RELOCATED to *L0 — …***`). Caught when
   Ruling 33 was read whole, before anything was landed; the line now equals the ruled text by script. One tell, so the
   rule to hand over on two is not met; this sitting ends at this verified stop in any case, its work done (Ruling 1
   (e)). **On the model (2026-11-12):** the tell came late, after a full verification; nothing separates load from
   model, so no suspicion about Opus is raised.

## 3. The plan — carried forward

1. **In parallel, independent of the steps below:** the external audit, as entry 1247 §3 step 1 and §2 item 5 give it
   (model recommended in entry 1248 §0). Its report, when the user brings it, is an untrusted source and evidence, not
   a ruling: a Cowork session reads it in full, checks each finding at the objects, and puts to the user what it bears
   on, judged against the plan.
2. **Now: a NEW Cowork session CHECKS session 31's instruction** as a turn of its own (Ruling 1 (e)), on the pattern of
   entry 1248 §2: every hash re-derived; the record whole; the release part 2 record's Rulings 2, 3, 16 and 33 whole
   (this sitting read 2 and 33 whole, 3 and 16 at their headings only); §L.46 whole; forms (b) and (b-H) with
   *Which ADOPTED word*, the two-record rule and the split-row sentence; §L.2's lines 484–499; Task 3 (c) items 5 and 6;
   the 5 rows each found once and read whole (shape, the earlier lines, UNPLACED, fit); §10's L0 and style-system
   blocks; the settlements (Row 40.6's colon form; Row 40.40 (iii)'s whole-cell quotation; Row 40.12 (iv)'s `(iv) `;
   Row 56.24's `(L3-S9 (i))` placement; the §10 subject clauses) — each judged, and put to the user only where the
   record does not settle it; the §10/§11 searches; `cowork_handoff.md`'s topmost block and
   `cowork_audit_protocol.md`'s dispatch-protocol section at their bounds (the instruction now names them by heading,
   not by line); and **a re-simulation by its own placement script** (`rebuild.py` cannot do it), which should give
   `d8139936…`. It adds its entry 1250 (already named in the instruction), corrects what it finds, lands, and **only it
   tells the user what to hand to Claude Code**.
3. **Then Claude Code executes session 31's instruction; then a NEW Cowork session verifies stretch 22** with the
   established scripts for the chain, the tree changes, the counts and the blobs, and **its own placement script for the
   rebuild** (outside `rebuild.py`'s *Limits*, as stretch 20's verifier did and declared; or `rebuild.py` extended and
   established again first, as the README says — the verifying sitting says which), and, under Rulings 1 and 2, writes
   the next stretch's instruction from §L.47, or hands over on two tells.
4. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above and entry 1221 §0 with Ruling 1 (b) as narrowed. **Practical notes, no
rules:** as entries 908 and 910 to 1248 §3, and: (a) this sitting's placement script is not kept; a verifying or
checking sitting writes its own, asserting each insertion point (after the proposed paragraph, then after every earlier
`*RULED`/`*RECORDED` line with its blank; a §10 entry after the last entry line of its named block); (b) the Edit tool
dropped a trailing space from a replacement string once; compare a ruled line by script, not by eye; (c) entry 1250's
file name would be `cowork_handoff_entry_one_thousand_two_hundred_and_fifty.md`; check by staging.

## 4. Who does what, in this order

1. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_forty_nine.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   (If the external audit's report is ready by then, the user may attach it; the session reads it in full after its
   boot and treats it as §3 step 1 says.) That session checks by staging whether an entry 1250 exists (if it does,
   report and ask), reads this entry whole, entry 1248 whole (the checking pattern, §2 item 1), entry 1221 §0, entry
   1026 §3, `tools/audit/stretch_verify/README.md` and session 31's instruction whole, asks the session-start read,
   reads the three git reference files (they should still read `371fe649…`), asks the user's leave for `python3 -I`,
   then does §3 step 2.
2. **Nothing goes to Claude Code from this entry.** The instruction to hand session 31's instruction to Claude Code
   comes only from the session that checks it (Ruling 1 (e); the user's rule of 2026-10-26).
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies (`grep`, `sed -n`, `awk`, `cut`, `tr`, `cmp`, `diff`,
  `head`), and, on the user's leave, `python3 -I -B` runs of the staged `gitobj.py`, `treediff.py`, `blobhash.py`,
  `blobout.py`, `rebuild.py` and `counts.py` (each read with the Read tool first) and of this sitting's own scripts
  (`place46.py`, `lines46.py`, written with the Write tool in a scratch folder outside the staged tree; short ones by
  `-c`). Two commands printed nothing useful (a `grep` whose pattern did not match the tree print's format; an
  extraction that took the wrong delimiter) and were re-run correctly before any result was used. Outputs only in the
  container, except the instruction filled by script in the outputs folder. Nothing written by any shell into a staged
  copy or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the three git reference files; the six script files;
  the commits, trees and blobs of stretch 21 named in §2 item 1, the parent commit `55784918…` and its root tree, the
  trees down to `tools/audit/stretch_verify/`, and `d53e8247…`, `48e24b2f…`, `a11b732d…`; the reading file; the
  report; the big dispatch; the language-model record; the phrase-end evidence record; the release part 2 record.
  **Listed:** the repository root; `tools/audit/stretch_verify/`. Paths asked for by staging and found free: entry
  1249 (twice), session 31's instruction path.
- **Session 31's instruction and this entry written in the outputs folder** (the instruction from a draft filled by
  script from the simulation's own text); **both landed with the commit tool**, each landing proved by staging back and
  comparing. One message sent with the user-message tool (the verification result, mid-sitting). No git on the device,
  widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-25 (Stockholm), the sitting booted on entry 1248. The user's words: the opening
instruction with Claude Code's closing message; "shortened"; "yes" (`python3 -I`); "yes" (land the draft).*
