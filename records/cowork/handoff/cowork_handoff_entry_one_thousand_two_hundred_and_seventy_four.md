# Cowork handoff entry 1274 — 2026-11-27 — STRETCH 29 (§L.54 AND §L.55, WITH TASK 3 (d)) VERIFIED AT THE OBJECTS, NOTHING DIFFERS; THE MEASUREMENT BLOCK WRITTEN; TASK 3'S EDITS ARE ALL COMMITTED

**The current entry point.** Entry 1273 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not; **[reading]** means this sitting's inference.

## 0. The user's rules in force, and his words to this sitting

**Carried unchanged:** entry 1273 §0, and through it entries 1272 to 1259 §0.

**His words to this sitting:** the opening instruction (entry 1273 §4 step 4's line, given verbatim), with Claude
Code's closing message pasted in the chat; *"yes"* (22:32, leave for `python3 -I` in the container on staged copies).

## 1. State

- **Boot [checked]:** the device-info call came first (`C:\s\MS` connected). Entry 1274 did not exist (staging
  refused). Read whole: entry 1273; Claude Code's report
  `records/cc/reports/cc_report_l3_application_session_38_task_3_stretch_29_2026_11_27.md`; the README of
  `tools/audit/stretch_verify/`. Read for the verification: entries 1270 and 1272 whole (the form of the measurement
  block; the writing side's figures); entry 1259 §2; the instruction at §3.2 and the §13a block.
- **Ruling 2's values, at the listing [checked]:** `STATUS.md` 11,726 / 1794136674043; `DECISIONS.md` 120,603 /
  1794081137207; `tools/audit/nongating_apparatus_rows.json` 178,066 / 1788814584416. All three equal entry 1273 §1, so
  none was read.
- **Git [checked, at the reference files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `b24195e1b824fae274451ab697e33aa39656c83c`, Claude Code's report commit, three
  commits past `0ae03b76…`.
- **Changed on disk by this sitting:** this entry only (untracked).
- **The model:** `claude-opus-5-5` throughout.

## 2. The verification of stretch 29 [checked, `python3 -I` over staged copies]

1. **The commits (`gitobj.py`):** each "hash ok", in a chain from the previous tip:
   `0ae03b7667245d453d2f845684980a30b48e12e0` → `524f0139c04d5c951edd125512861c400d1018cd` →
   `8ce907b9962149eb8c7cdff5a8b1610a966d77cb` → `b24195e1b824fae274451ab697e33aa39656c83c`. Act 1's subject carries
   *"1270 to 1273"*, as entry 1273 §2 item 8 set it; act 2's names §L.54 and §L.55 and Task 3 complete; act 3's is the
   report's.
2. **The trees (`treediff.py`, down every changed path):**
   - act 1 adds exactly the instruction (`9c83e2455d7cfe5514985e781d72d3302212b179`, equal to Claude Code's pin and to
     entry 1273 §2 item 8's landed blob) and entries 1270 (`d7c4f5f1…`), 1271 (`a9f518cc…`), 1272 (`6d0dca18…`) and
     1273 (`a67508f3…`), and nothing else;
   - act 2 changes only `ratification_surfaces/cowork_comparison_l3_reading.md`, `17e24773…` →
     **`a83519b1f14bba9282fb9bf53600d59d5e27b213`**, the blob the writing side simulated (entry 1272 §2 item 5) and the
     comparing side re-simulated (entry 1273 §2 item 5);
   - act 3 adds only the report (`176c761c…`).
3. **The files on disk (`blobhash.py`):** each of the seven landed files equals its committed blob. The reading file is
   `a83519b1…`, 5,375,646 bytes, 85,062 line feeds, no carriage return.
4. **`rebuild.py` does not reach this stretch** (entry 1272 §2 item 7); not run. **In its place, this sitting's own
   placement check, NOT established (#19)**, over `blobout.py` copies of `17e24773…` and the Task 2 blob `48e24b2f…`:
   - `diff` against the stretch 28 file has exactly three passages: lines 54–55 deleted; two lines added after 84717
     (now 84716–84717); 84 lines added after 84852 (now 84853–84936);
   - line 84716 is byte-equal to the sentence in the instruction's §3.2 item 2 code block; lines 84854–84937 (§13a,
     heading to final blank) are byte-equal to the instruction's §3.3 block (its lines 295–378); `## 14.` follows at
     84938; line 54 is `---`.

   **What this check is worth:** it shows Claude Code's file carries the instruction's text where the instruction puts
   it. It does not compare the instruction with the records; entry 1273 did that, and for §13a two independent
   derivations (entries 1272 and 1273) and Claude Code's third agree. The strongest single evidence stays the blob.
5. **The counts (`counts.py` on the reading file):** `*RULED DISPOSITION (` 626; `*RULED PLACEMENT (` 46;
   `*RECORDED DISPOSITION (` 53; `*LEAVES L3 (` 26; `*Row 7.67 is not transferred` 1; `*NOT QUARANTINED (` 1; *as
   proposed* 128; the application surface record's name 0; the disposition words record's name 90; `*Application in
   progress: ` 0; `## 13a. ` 1; `distribution of the PROPOSALS` 1. Against `17e24773…`: 86 added, 2 deleted. Against
   `48e24b2f…`: 1,623 added, 4 deleted. Every figure as the instruction's §4 item 8 gives it. *That `48e24b2f…` is the
   Task 2 commit's reading file stays [relayed], as in entry 1270 §2 item 5.*
6. **§L.55's lines, by place:** the disposition words record's 90 lines lie 87 before `## 7.` (79917) and 3 in §10
   (80575, 80576, 81199); the thirteen row headings Claude Code's report §3 tabulates each match once at the line it
   gives. These are the committed file's line numbers; entry 1273's 80577, 80578 and 81201 are the same lines before
   the two-line removal at 54.
7. **Claude Code's report, read in full:** it covers every check and act, ends with the exact last sentence, and
   declares four departures (§6): the pin taken after the first read (the declared route); a git object written with
   `git hash-object -w` to copy the edited file to its scratchpad; the §L.55 count check placed by its script over the
   scratchpad copy rather than from the too-large Grep listing; `git rev-parse HEAD` run to learn each new hash, every
   push then verified at the ref file and every commit at its object. None changed a byte of the reading file, and the
   blob check of item 2 does not rest on them. Its act 1 figure of 1,175 insertions equals the five files' line feeds
   (571 + 159 + 113 + 181 + 151). It counts 579 `@@` lines for the whole-Task diff and calls that *"not a check"* —
   entry 1273's correction of the 589 figure held.
8. **Verdict: nothing differs.** No error reached a commit that this verification can see.

## 3. The measurement block for stretch 29 (ruling B, entry 1262 §2 item 1)

- **(a) Who worked on the stretch:** Cowork entries 1272 (writes), 1273 (compares, under Ruling A), 1274 (verifies);
  Claude Code session 38.
- **(b) Reading-file lines against the commit before:** 86 added, 2 deleted (Claude Code's `--numstat`, report §5).
  Confirmed here by `counts.py`'s `diff` count and the placement check of §2 item 4, **not by the rebuild**, which does
  not reach this stretch.
- **(c) The instruction:** as written, 50,857 bytes and 564 line feeds (entry 1272 §2 item 8 [relayed]); as landed,
  after entry 1273's banner replacement and two corrected descriptions, 51,638 bytes and 571 line feeds (`blobhash.py`,
  this sitting).
- **(d) Bytes Claude Code is told to read:** 145,185 under the instruction's list — entry 1272's 144,404 [relayed] with
  the instruction's 50,857 replaced by its landed 51,638 (arithmetic on the relayed figure, as entry 1270 did). The
  old-list figure was not computed, and is not here.
- **(e) What each step caught:**
  - the record comparison (entry 1273): nothing in the instruction differed from the records; it corrected two
    descriptions in §4 item 8 (the "35 entries" that are 34 and a heading; the "589 changed passages" that git would
    count as 579), the second of which could have made Claude Code stop; no act, line or required count changed;
  - Claude Code's own checks: every check held; no STOP; §13a derived a third time and identical to the block;
  - this verification: nothing caught.
- **(f) STOPs:** none.
- **(g) Errors that reached a commit:** none found.
- **A gap in the measurement itself, stated:** item (b)'s *"confirmed by the verifier's rebuild"* could not be met, for
  the reason in §2 item 4.

## 4. Where the work stands [reading, from the records named]

Task 3's edits are all committed: Claude Code's report says *"Task 3 is complete"*, and the reading file now carries
§13a and no in-progress line. **What remains of Task 3 is its end-of-task points** (entry 1273 §3 step 2): the ruling-B
summary against entry 1259 §2 items 1 and 2, its limit stated (#24). Then Task 4 and Task 5, as the big dispatch gives
them. Carried: entry 1262 §3 steps 2 and 3; entry 1264 §6 items 1 and 2.

## 5. The plan — carried forward

1. **Next: the ruling-B summary for Task 3** — the measurement blocks of the stretches run under Ruling B, gathered and
   set against entry 1259 §2 items 1 (cost) and 2 (what the steps caught), with its limit stated (#24). Documentation
   only; it changes no line of the reading file and no algorithm. It may be written by this sitting if the user says
   so, or by a new Cowork session booted on this entry.
   - **Boot list for a new session:** this entry whole; entry 1259 §2; entry 1262 §2 item 1 (the block's definition);
     the measurement blocks of entries 1263 onward, as the summary needs them.
2. **Then:** Task 4 and Task 5 of the big dispatch.
3. **Carried:** as §4.

## 6. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** No instruction is waiting.
2. **If the user says "continue" in this session,** this sitting writes the ruling-B summary (§5 step 1) and lands it.
3. **Otherwise, THE USER opens ONE NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it
   exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_seventy_four.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging that entry 1275 does not exist (if it does, report and ask); reads its boot list as
   §5 step 1 gives it; makes the session-start read by ruling 2 against §1's values; reads the three git reference files
   (they should still read `b24195e1…`); asks the user's leave for `python3 -I` if it needs a script; judges capacity
   out loud; then does §5 step 1.

**If the user overrules any of this or changes the order, the session follows him.**

## 7. Departures, declared

- **Container shell.** Read-only searches over staged copies (`grep`, `sed -n`, `cut`, `awk`, `diff`, `wc`). On the
  user's leave, the committed scripts of `tools/audit/stretch_verify/` run with `python3 -I` from their staged folder,
  `blobout.py` writing three blobs into a container scratch folder outside the staged tree. One inline `python3 -I -c` line,
  not a scratch-folder script, printed object paths built by slicing three hashes; it read no file. Nothing written
  to the device by any shell.
- **The scripts were read before being run**, which entry 1259 §2 item 6 (b) says is not needed each time; it cost a
  few small reads and changed nothing.
- **Landed with the commit tool**, and proved by staging back and reading with the file tools. No git on the device, no
  widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-27 (Stockholm), the sitting booted on entry 1273. The user's words as §0 gives them.*

## 8. Added after landing, on the user's word "continue" (2026-11-27, 22:36) — the ruling-B summary for Task 3

**What it is:** the measurement ruled B in entry 1262 §0 — the per-stretch blocks of stretches 27 to 29 set against the
baseline of entry 1259 §2 items 1 and 2, with the limit entry 1262 §2 item 1 fixes. **Documentation and process
only:** it changes no line of the reading file, no specification text and no algorithm; it decides nothing.
**Sources [checked at each entry, read at the block]:** entry 1259 §2 items 1 to 4; entry 1262 §2 item 1; the blocks
of entries 1267 §3 (stretch 27), 1270 §3 (stretch 28) and §3 above (stretch 29); items (c) and (d) at entries 1265 §2
item 5, 1268 §2 item 5 with entry 1269 §2 item 7's correction, and 1272 §2 item 8; item (a) at entries 1263 §2 item 6
and 1264 §2 item 8, and at the headings of 1271 to 1273. Stretch 26 (§L.51) ran under the old orders and is in
neither set. Ratios below are arithmetic on those figures (`python3 -I`).

1. **Cost.**

   | | Baseline: stretches 1–25 (entry 1259 §2 item 1) | Ruling B: stretches 27–29 |
   |---|---|---|
   | Ledger entries applied | 50 (§L.1–§L.50) | 4 (§L.52–§L.55), and Task 3 (d) |
   | Cowork sittings | 65 (2.6 per stretch; 1.3 per ledger entry) | 12 (4.0 per stretch; 3.0 per ledger entry) |
   | Claude Code sessions | 26 | 3 |
   | Instruction bytes | 1,375,531 in 26 files (55,021 per stretch) | 174,849 as landed (58,283 per stretch) |
   | Reading-file lines added / deleted | 1,438 / 31 | 211 / 4 (103/1, 22/1, 86/2) |
   | Instruction bytes per added line | 957 overall; 6,571 for stretches 21–25 | 829 |

   - **Sittings per stretch did not fall.** By role under B: 3 prepared (1263, 1264, 1271), 3 wrote (1265, 1268,
     1272), 3 compared (1266, 1269, 1273), 3 verified (1267, 1270, 1274). No sitting verified one stretch and wrote the
     next, which 12 baseline sittings did and Ruling A foresaw; each of the three preparing sittings handed over on a
     capacity judgment before writing.
   - **Bytes Claude Code is told to read (item (d))** — the one figure free of the size effect, measured both ways
     once: stretch 27, **181,324 under the new list against 649,418 under the old**, the new list 28 % of the old.
     Stretches 28 and 29 have the new-list figure only (128,189; 145,185), the old-list figure not computed.
   - **`rebuild.py` reached none of the three stretches**: stretch 27's rows all carried earlier lines, stretch 28
     added §11 entries, stretch 29 wrote no row line. Each verifying sitting used its own unestablished placement check
     (entries 1267, 1270, 1274), against entry 1259 §2 item 6 (a)'s settlement that the script be extended; entries
     1268 and 1272 settled not to extend it, each for its one stretch. Ruling C's third step (no `counts.py` re-run on a
     byte-identical rebuild) therefore never applied.

2. **What the steps caught.**

   | Step | Baseline (entry 1259 §2 item 2) | Ruling B: stretches 27–29 |
   |---|---|---|
   | Check before the commit | separate checks; byte-changing catches at stretches 1 and 5 only; from stretch 8 on, descriptions and bookkeeping, three of which would have made Claude Code stop | record comparison (Ruling A): nothing at 27 and 28; at 29, two descriptions corrected, one of which could have made Claude Code stop; no byte of the reading file changed by any |
   | Claude Code's own checks | caught two real instruction errors a check had passed (stretches 3 and 5) | every check held; one predicted STOP-and-report at 27; §13a derived a third time and identical at 29 |
   | Verification | one committed error caught (stretch 2, corrected at 3) | nothing caught |
   | Errors that reached a commit | one in 25 stretches | none found in 3 |
   | Fingerprint match | every report from stretch 9 on, none a mismatch | each of the three, none a mismatch |

   **On the quality side Ruling A was meant to protect (entry 1262 §2 item 1 (g)):** dropping the separate check let no
   error through that the verifications can see. One catch of the kind the separate check used to make (a description
   that could have stopped Claude Code) was made by the record comparison at stretch 29.

3. **The limit (#24), as entry 1262 §2 item 1 fixes it.** Three stretches of very uneven size (22 to 103 added lines)
   against twenty-five. The comparison is **indicative, not a finding**: no sampling uncertainty can be put on three
   observations, and per-stretch and per-line ratios carry the size effect without removing it. Stretch 29 is also not
   like the others (no row line; §13a and Task 3 (d)). The only figure free of the size effect, item (d), was measured
   both ways for one stretch.

4. **What is NOT claimed:** that Ruling A, B or C saved or cost sittings overall; that the lower error count is a
   difference; that the old-list reading figure for stretches 28 and 29 would resemble stretch 27's.

## 9. Where the work stands now, and who does what — supersedes §5 and §6

1. **Task 3 is complete**, its end-of-task point (§8) included. **Next: Task 4 of the big dispatch** — *"the charter
   (`FRAMEWORK.md`) and the ratified L1 interface contract: the amendments written where the records give the words,
   the rest listed for the user"*, its heading at the big dispatch's line 6821 (blob `b5274c2c…` [checked]), Task 5
   from line 7021. How Task 4 is prepared and handed to Claude Code is the next sitting's to read at the dispatch; this
   entry does not judge it. **Carried:** entry 1262 §3 steps 2 and 3; entry 1264 §6 items 1 and 2.
2. **Nothing goes to Claude Code from this entry.** No instruction is waiting.
3. **THE USER opens ONE NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_seventy_four.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging that entry 1275 does not exist (if it does, report and ask); reads this entry whole
   and the big dispatch's Task 4 (lines 6821–7020) and its own reading list for Task 4 as that Task gives it; makes the
   session-start read by ruling 2 against §1's values; reads the three git reference files (they should still read
   `b24195e1…`); asks the user's leave for `python3 -I` if it needs a script; judges capacity out loud; then begins §9
   step 1.
4. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

*§8 and §9 provenance: the same sitting, after the user's "continue". Staged and read for them, beyond §7's list:
entries 1260 to 1269 and 1271 (at their headings and measurement items), the big dispatch (blob recomputed; Task 3's
end and the Task headings). Capacity: no degradation tell appeared; I stop here, at a landed and checked point. On the
model (2026-11-12): nothing raises a suspicion about Opus.*
