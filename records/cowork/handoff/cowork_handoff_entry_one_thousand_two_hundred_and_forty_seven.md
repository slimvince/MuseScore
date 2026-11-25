# Cowork handoff entry 1247 — 2026-11-25 — SESSION 29'S STRETCH (§L.44) VERIFIED AT THE OBJECTS, NO FINDING; SESSION 30'S INSTRUCTION (§L.45 ONLY) WRITTEN IN THE SAME SITTING AND LANDED UNCHECKED; AN EXTERNAL AUDIT INSTRUCTION WRITTEN FOR THE USER; HANDED OVER AT THREE DEGRADATION TELLS

**The current entry point.** Entry 1246 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried, and what he said to this sitting

As entry 1246 §0, unchanged: one question or a handover per message, never both; the two rulings of 2026-11-24 (entry
1221 §0) with Ruling 1 (b) as narrowed (entry 1241 §0, decision 3); decision 1 (the verification scripts one committed
tool, entry 1244 §2 item 1); Claude Code does every git act, pushing included.

**His words to this sitting:** "Shortened" (the session-start read); "yes, you may" (`python3 -I` in the container, on
staged copies only, scripts written with the file tools outside the staged tree, nothing written to the device by any
shell; a later sitting asks again); "continue" (write session 30's instruction under Ruling 1 (d)); and, to the
question whether to land the draft unchecked: *"Yes, but first: VERY soon I will run out of credits … I would like to
use another LLM (GPT-6.1 Terra) to do an audit / quality check of our specifications … Land the draft. Do whatever is
needed in order to facilitate an external audit by GPT 6.1 Terra. Write the instruction I will give to Terra. If we then
still have more credits left we can continue following the plan."*

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1247 asked for by staging: *"does not
  exist"*. Read whole: entries 1246, 1245, 1244, 1221 (§0), 1026 (§3); the README of `tools/audit/stretch_verify/`;
  session 29's instruction; Claude Code's closing message (with the user's opening message) and its report.
- **Session-start read, shortened:** `STATUS.md` whole (11,726 bytes, 1794136674043, unmoved); `DECISIONS.md` at the
  listing (120,603 bytes, 1794081137207, unmoved); the gating answer by search (`open_rows` 247 at lines 26 and 185,
  `non_gating` 25 at line 49, `gating_ids` from line 186). `CLAUDE.md` came with the user's second message, whole.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `557849182df3363f38a356de46654aa5bc45355a` — session 29's report commit.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **Session 30's instruction, WRITTEN, NOT CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_30_task_3_stretch_21_2026_11_25.md`, **45,910
    bytes, 507 lines**, no carriage return, blob `e9d1af54b509dabe7bca6d77c6c3d8268a1fe499`. The path staged first and
    found free; landed on the user's word; **proved**: staged back and compared byte for byte with the copy sent,
    identical. Untracked.
  - This entry (untracked).
- **Not landed, given to the user in the chat only:** `external_audit_instruction_terra_2026_11_25.md`, the instruction
  for the external audit (§2 item 5).
- **Untracked writing-side files for session 30's act 1:** this entry 1247, the instruction, and the checking session's
  entry 1248.

## 2. What this sitting established

1. **Session 29's stretch (§L.44) verified at the objects [checked]. No finding.** Scripts staged, their blobs equal to
   entry 1244 §2 item 1, read before running, run with `python3 -I -B`.
   - **The chain** (`gitobj.py`): `8dfffc59c9bbaa4df18e9f92df4f3369cfa5f834` (parent `9da280ac…`),
     `23249f748218582072ae83a5434f58ec8b100144` (parent `8dfffc59…`), `557849182df3363f38a356de46654aa5bc45355a`
     (parent `23249f74…`); one parent each; each subject found word for word in the instruction.
   - **The tree changes** (`treediff.py`, every changed path walked): act 1 adds the instruction (`2f06aa8a…`), entries
     1244 (`49fdaaee…`), 1245 (`c08c293f…`) and 1246 (`5c66e0dc…`), and changes the README `4e14edd8…` → `1bcf458e…`
     (the folder's tree `9977ce1c…` holds exactly the seven files at the established blobs); act 2 changes only the
     reading file `4e15efe3…` → `d53e8247…`; act 3 adds only the report (`1e01b20c…`). Each of these seven committed
     blobs equals the file on disk (`blobhash.py`).
   - **The rebuild, by this sitting's own placement script** (kept in the container only; outside `rebuild.py`'s
     *Limits*: §10 entries, a heading made, lines before a `####` heading), from the loose object `4e15efe3…` and the
     instruction's own text, each insertion point asserted at its object: **byte-identical to the file on disk on the
     first run**, blob `d53e8247…`, 5,346,432 bytes, 84,813 line feeds. Negative test: one character changed in a copy
     of the instruction's Row 23.40 entry → DIFFERS.
   - **Counts** (`counts.py`): 548 / 45 / 53 / 26 / 1 / 1; *as proposed* 128; record names 18 / 12 / 11 / 21 / 17 / 13
     / 36; the style-system phrase 10; 32 added and 1 deleted against `4e15efe3…`, 1,374 and 4 against `48e24b2f…`. The
     10 lines at 33033 … 36827, 36829; the heading at 81314, entries at 81139 and 81316–81322; §10 80219–81334 with
     eleven hits, §11 81335–83487 with none (this sitting's own look-around search). The diff has twelve changed
     passages, as the report's table.
   - **The report**
     (`records/cc/reports/cc_report_l3_application_session_29_task_3_stretch_20_2026_11_25.md`, 21,646 bytes, 272
     lines) **read in full**; its row-heading numbers, line 81312 (Row 7.37's entry), 81324 (the closing note) and
     83488 (`## 12.`) hold at the committed file. **Not re-run here:** the decided-against search and the per-line
     quotation comparisons (the rebuild shows the instruction's text written byte for byte, and the checking session
     compared that text with the sources); the Task 2 commit hash itself [relayed].
   - **The order slip Claude Code declared** (reading-file edits made before act 1's commit, against §5): judged under
     Ruling 1 (b) as narrowed — no discrepancy in the committed files or the instruction, no failed check, and accounted
     for at the objects (act 1's tree keeps the reading file at `4e15efe3…`: the `ratification_surfaces` tree is unchanged
     between `9da280ac…`'s tree and act 1's). Not a stop; told to the user; entry 1241 §2 item 2 the precedent. **The
     adjustment, made in session 30's instruction §5 act 1:** no edit to the reading file before act 1's commit, and,
     immediately before staging act 1, `git diff --quiet <tip> -- <reading file>` must exit 0, else STOP.
2. **Ruling 2's judgment, said to the user before writing** (no objection): §L.45 fits alone; **§L.46 does not** (five
   kinds of act on 6 row-parts — form (b-H), ADOPTED — carried read at the row, RELOCATED to L0 with a §10 entry,
   RELOCATED outside the framework with a second §10 entry, HISTORICAL — a status — two possible two-record meetings,
   with §L.2 and §L.23, and four of five lines not given whole). **The stretch stops at the boundary before §L.46.**
3. **Session 30's instruction, written on session 29's pattern under Ruling 1 (d).** 5 lines on 5 rows, all HISTORICAL,
   quoting the record's ruling sentence (its line 29) whole; Row 57.124's one line names both claims as
   `(i) and (ii) **HISTORICAL** — …`, as §L.45's table orders (*"its line names (i) and (ii)"*) — no line of the L3 or
   the L2 reading file yet names two claims (searched with
   `^\*(RULED|RECORDED)[^*]*\.\* \([ivx]+\)( and|,) \(`: none in either). The rows' shape is new to the run's recent
   stretches but has precedents: each line goes after the blank line that follows the proposed paragraph, directly
   before *At the source now.* (61 ruled lines already stand so; 24 before *The decisions register at this row.*).
   Nothing at §10 or §11 (no hit for the five row numbers in either). The record: 5,500 bytes, blob `ec098d67…`, read
   whole; Ruling 30 of the release part 2 record read whole (lines 1602–1669). **Within `rebuild.py`'s *Limits*: yes**
   — the verifying session can use the established tool.
4. **Simulated** by the established `rebuild.py` on the draft's own text, with this sitting's own check that each line
   lands directly before *At the source now.*: **blob `a11b732d8d4c4a9d617587461c9caacd1ded8672`** (5,347,540 bytes,
   84,823 line feeds); 11 added and 1 deleted against `d53e8247…`, 1,384 and 4 against `48e24b2f…`; counts 553 / 45 /
   53 / 26 / 1 / 1, the language-model record 5, the other seven names unchanged; lines at 74695, 76302, 76334, 76367,
   76400; §10 80229–81344 and §11 81345–83497, no hit. Each line's quotation found once in the record by script. Re-run
   on the final text: the same blob.
5. **The external audit instruction**, on the user's order: a self-contained instruction for GPT-6.1 Terra to audit
   `FRAMEWORK.md` and the three derived specifications (L0/L1 ratified; L2 and L3 not ratified), optionally `CLAUDE.md`'s
   *Guiding principles*, for coherence, completeness for implementation, correctness, fitness for maximum-precision
   inference and testability; read-only; findings with location, kind, documentation-only or algorithm, severity and
   basis. Status banners of the four documents read at their heads for it. **Terra's report, when the user brings it, is
   an untrusted source and evidence, not a ruling: a Cowork session reads it in full, checks each finding at the
   objects, and puts to the user what it bears on, judged against the plan — never acted on as the latest news.**
6. **Degradation tells: three. I have already made two of these.** All in the writing, all caught before landing: (1) a
   precedent named as Row 20.31 without checking it (it is Row 56.2, lines 72268 and 72270); (2) two provenance phrases
   wider than the reads (Task 3's items; Ruling 30, then read whole); (3) a "none found" resting on a print cut to 30
   entries, re-run in full (none). **On the model (2026-11-12):** all late in a sitting that carried a full verification
   and a full writing; nothing separates load from model, so no suspicion about Opus is raised.

## 3. The plan — carried forward

1. **In parallel, independent of the steps below: the user gives GPT-6.1 Terra the external audit instruction** with
   the four documents. Its report comes back to a Cowork session as §2 item 5 says. It changes nothing in the order
   below unless the user rules so.
2. **Now: a NEW Cowork session CHECKS session 30's instruction** as a turn of its own (Ruling 1 (e)), on the pattern of
   entry 1246 §2: every hash re-derived; the record whole; Ruling 30 whole; §L.45 and form (b) with its split-row
   sentence; the 5 rows each found once and read whole (shape, no earlier line, UNPLACED, fit); the settlements (Row
   57.124's `(i) and (ii)` form; the quotation of the whole sentence) — each judged, and, if the check finds the one-line
   form not settled by the record, put to the user; the §10/§11 searches; and a re-simulation by its own script or the
   established `rebuild.py`, which should give `a11b732d…`. It adds its entry 1248 (already named in the instruction at
   §1 check 5, §2 item 4, §4 item 3 and §5 act 1 with its subject), corrects what it finds, lands, and **only it tells
   the user what to hand to Claude Code**.
3. **Then Claude Code executes session 30's instruction**; **then a NEW Cowork session verifies stretch 21** (within
   `rebuild.py`'s *Limits*) and, under Rulings 1 and 2, writes the next stretch's instruction from §L.46 (this entry's
   §2 item 2 remarks to be re-judged at the objects), or hands over on two tells.
4. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above and entry 1221 §0 with Ruling 1 (b) as narrowed. **Practical notes, no
rules:** as entries 908 and 910 to 1246 §3, and: (a) the loose object of the previous stretch's reading-file blob must
be staged before `rebuild.py` or `blobout.py` can read it; (b) a search result printed through `head` is not a search
result — re-run it whole before saying "none"; (c) entry 1248's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_forty_eight.md`; check by staging.

## 4. Who does what, in this order

1. **Whenever the user chooses, independently: THE USER gives GPT-6.1 Terra** the text of
   `external_audit_instruction_terra_2026_11_25.md` (sent in this sitting's chat) together with `FRAMEWORK.md`,
   `cowork_derived_specification_l0_l1_2026_09_03.md`, `cowork_derived_specification_l2_2026_10_10.md`,
   `cowork_derived_specification_l3_2026_11_08.md` and, optionally, `CLAUDE.md`. Terra writes nothing into the
   repository.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_forty_seven.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   (If Terra's report is ready by then, the user may attach it to that message; the session then reads it in full
   after its boot and before §3 step 2, and treats it as §2 item 5 says.) That session checks by staging whether an
   entry 1248 exists (if it does, report and ask), reads this entry whole, entry 1246 whole (the checking pattern),
   entry 1221 §0, entry 1026 §3, `tools/audit/stretch_verify/README.md` and session 30's instruction whole, asks the
   session-start read, reads the three git reference files (they should still read `55784918…`), asks the user's leave
   for `python3 -I`, then does §3 step 2.
3. **Nothing goes to Claude Code from this entry.** The instruction to hand session 30's instruction to Claude Code
   comes only from the session that checks it (Ruling 1 (e); the user's rule of 2026-10-26).
4. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies (`grep`, `sed -n`, `cut`, `wc`, `head`, `diff`, `cmp`, `cat`
  of staged ref files) and, on the user's leave, `python3 -I -B` runs of the seven staged scripts (each read first)
  and of this sitting's own scripts (`place.py`, `fill.py`, `fix2.py`, written with the Write tool in a scratch folder
  outside the staged tree; short ones by `-c`). One command failed on shell quoting and ran nothing; one run failed
  because the loose object `d53e8247…` was not yet staged, and wrote nothing to the device. Outputs only in the
  container. Nothing written by any shell into a staged copy or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the git reference files; the seven script files; the
  commits, trees and blobs of stretch 20 named in §2 item 1, and `48e24b2f…`, `d53e8247…`; the reading file; the report;
  the big dispatch; the language-model record; the release part 2 record; the release part b record; the L2 reading
  file (searched only); entry 1241 (§0 decision 3 and §2 item 2 read); `specification_document_set.json` (keys only);
  `FRAMEWORK.md`, the three derived specifications and the phase-definition surface (heads and `##` headings only, for
  the audit instruction). **Listed:** the repository root; `tools/audit/stretch_verify/`. Paths asked for by staging
  and found free: entry 1247, session 30's instruction path.
- **Session 30's instruction and this entry written in the outputs folder with the Write tool (the instruction filled
  and corrected there by script); both landed with the commit tool**, each landing proved by staging back and
  comparing. The audit instruction written there and sent to the user, not landed. No git on the device, widget, task
  list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-25 (Stockholm), the sitting booted on entry 1246. The user's words: the opening
instruction with Claude Code's closing message; "Shortened"; "yes, you may"; "continue"; "Yes, but first: …" (land
the draft; facilitate the external audit; write Terra's instruction).*
