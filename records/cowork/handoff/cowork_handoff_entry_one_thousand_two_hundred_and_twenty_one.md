# Cowork handoff entry 1221 — 2026-11-24 — SESSION 19'S STRETCH (§L.32) VERIFIED AT THE OBJECTS, NO FINDING; SESSION 20'S INSTRUCTION (§L.33 AND §L.34) WRITTEN IN THE SAME SITTING AND LANDED UNCHECKED; TWO STANDING RULINGS OF THE USER RECORDED; HANDED OVER AT TWO DEGRADATION TELLS

**The current entry point.** Entry 1220 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried, and his two new rulings of 2026-11-24

**A message to the user either asks him ONE question or hands over to another session — NEVER BOTH** (entry 1215 §0).
This sitting asked two questions, each in a message of its own (the session-start read; whether to land the draft
unchecked), and hands over in a later message.

**The user's two rulings of 2026-11-24, given in his opening message to this sitting, standing until he changes them.
Carry both forward.** In his words, lightly trimmed:

**Ruling 1 — the session that verifies Claude Code's stretch also writes the next stretch's instruction, in the same
sitting.** (a) Finish the verification of the stretch Claude Code just committed, exactly as the handoff entry's plan
gives it: the chain of commits, the tree changes, the reading file rebuilt independently and compared byte for byte,
and the report read in FULL. (b) If the verification found a finding, or anything the session cannot account for, stop
there: report it to him and write no instruction. (c) If two degradation tells have appeared by the end of the
verification, stop there too: write the handoff entry at that verified stop and hand over to a new writing session.
(d) Otherwise, write the next stretch's instruction in this sitting, following the pattern of session 19's instruction,
sized at the files themselves, and land it unchecked on his word, the same way as before. (e) The writer is still never
the checker: the instruction is checked as a separate turn by a NEW Cowork session before anything goes to Claude Code,
exactly as now, and only that checking session tells him what to hand to Claude Code. (f) Act 1 of the instruction
must land every untracked writing-side handoff entry that exists when it is written; the checking session adds its own
entry, as before.

**Ruling 2 — a writing session judges out loud how many ledger entries fit in one stretch, instead of writing one by
default.** After reading the first entry it will write (its §L ledger entry in the big dispatch, its record, and the
rows at the reading file): (a) say out loud whether the next §L entry also fits, judged on the next record's size at
the folder listing, the number of row-parts and lines its §L table gives, and any new kind of line or row shape it
brings; (b) if it fits, add it to the same instruction, and repeat the judgment for the entry after that; (c) stop
adding at an entry boundary when the next one does not fit, when a degradation tell has appeared, or when the
instruction's simulation can no longer be re-run cleanly from its own text in the sitting; (d) one stretch is still one
commit for Claude Code, stopping at an entry boundary, and the counts, the numstat figures and the expected file
fingerprint cover every entry in the stretch; (e) state in the instruction and in the handoff entry which entries the
stretch covers, and why it stopped where it did.

**What the rulings do NOT change** (his words): the checking session as a separate turn; the one-question-or-hand-over
rule; the long opening line for Claude Code; read-only after the handoff entry is landed; and the rule to hand over at
a verified stop on two tells. Where anything in them conflicts with a handoff entry's plan, the rulings govern; where
anything is unclear, the session asks him one question before acting rather than choosing.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1221 asked for by staging before any
  other boot read: *"does not exist"*. Entries 1220 (10,097 bytes) and 1218 (9,162) read whole; entry 1026 at §3 (the
  file 11,103).
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` whole (11,726 bytes, 1794136674043,
  unmoved); `DECISIONS.md` at the listing (120,603 bytes, 1794081137207, unmoved); the gating answer at
  `tools/audit/nongating_apparatus_rows.json` lines 180–186. `CLAUDE.md` came with the user's second message, whole.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `9037f1b24cc6867acd57fcdf8f4b759b2b5b7953` (modification times 1795509342384 and
  1795509349612; re-staged after the chat's pause, unmoved). Nothing has run since session 19.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting [checked]:**
  - **Session 20's instruction, WRITTEN, NOT CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_20_task_3_stretch_11_2026_11_24.md`, **50,427 bytes,
    549 lines**, no carriage return, blob `03118a85afedd9f5c35c980ac5da3ae6f77edcb6`. Landed on the user's word ("Yes"),
    the path staged first and found free; **proved byte for byte**: staged back after the landing, its blob recomputed,
    and compared with the draft by `cmp`, identical. Untracked.
  - This entry (untracked).
- **Untracked writing-side entries: 1221 only** (1218 to 1220 were landed by session 19's act 1). The instruction's §5
  act 1 lands 1221 with it (Ruling 1 (f)); the checking session adds its own entry 1222.

## 2. What this sitting established

1. **Session 19's stretch (§L.32) verified at the objects, on entry 1218 §2's pattern. No finding [checked].**
   - **The chain:** the three commit objects staged and each SHA-1 recomputed from its decompressed content:
     `c0153261…` (parent `f1e7c914…`), `76b9919c…` (parent `c0153261…`), `9037f1b2…` (parent `76b9919c…`), one parent
     each; each subject exactly the one session 19's instruction gives (found verbatim in it by script).
   - **The tree changes**, every tree object on the path walked with its SHA-1 recomputed: act 1 adds exactly the
     instruction and entries 1218, 1219 and 1220; act 2 changes only `ratification_surfaces/cowork_comparison_l3_reading.md`
     (`27e0d551…` → `9bc1717744a690b557bc33f16ce6c18df095b0c4`); act 3 adds only the report. Every committed blob equals
     the file on disk (the instruction's `b88be586…` is the blob Claude Code pinned).
   - **The reading file rebuilt independently** by this sitting's own script from the stretch 9 blob `27e0d551…`
     (decompressed, its hash checked), the line texts taken from session 19's instruction's own text: **byte-identical
     to `9bc17177…` and to the file on disk, on the first run** (5,297,185 bytes, 84,518 lines). Diff 33 added, 1
     deleted; counts 452 / 3 / 53 / 26 / 1 / 1; the recognition part 2 record named 18, part 1 13, lead rows 23; each
     of the 14 quotations found exactly once in the record; no decided-against phrase in the record.
   - **The report** (`records/cc/reports/cc_report_l3_application_session_19_task_3_stretch_10_2026_11_24.md`, 20,337
     bytes) **read in full**: its 14 line numbers, the §10 lines 80674–80677, act 1's 912 insertions, the shifted
     section bounds and all 12 chunk headers of its diff table hold at the rebuilt file. Its departures (reading before
     pinning, scripts over git-history copies, three read-only git commands) bear on nothing written.
   - **Entry 1220's bound is closed:** blob computation worked in this sitting (`python3 -I` in the container on staged
     copies), so the expected blob `9bc17177…`, the record's and `27e0d551…` are now re-derived.
2. **Session 20's instruction written under Ruling 1 (d)** (the pattern of session 19's instruction).
   - **Ruling 2's judgment, said out loud to the user before writing:** §L.33 (record 8,151 bytes; 23 row-parts; 8
     lines: 5 ADOPTED — proposed, 2 ADOPTED half lines, 1 partial HISTORICAL line under form (b-H), with precedents at
     the reading file's lines 1374 and 1376; nothing at §10 or §11) fits; §L.34 (record 6,881 bytes; 13 row-parts; 2
     ADOPTED — proposed lines, Row 44.4 and Row 46.27's analysis half; no new kind) fits; **§L.35 does not, and the
     stretch stops before it**: its record is small (6,651 bytes, 6 lines), but it brings a RELOCATED line to *the
     second axis — voice leading* with a §10 entry under a heading this run has not written to, a line written as a
     release ruling's item gives it with an ellipsis in its quotation, and a row named by two records by claim (57.401);
     the sitting, already carrying the full verification, judged the margin too thin to add a third record and still
     re-run the simulation cleanly.
   - **What it writes:** 10 `*RULED DISPOSITION (` lines on 10 rows (9 ADOPTED — proposed, 1 HISTORICAL; none *as
     proposed*, every part named being proposed UNPLACED at its row), nothing at §10 or §11, the in-progress line to
     *"§L.1 to §L.34"*. **§L.34's record is itself an algorithm change, already ratified**; the instruction says the
     stretch only writes its placements into the reading file.
   - **Simulated from the instruction's own final text** (lines extracted by script, placed by its §3.1 item 2 rule on
     the rebuilt file): 21 added and 1 deleted; counts 462 / 3 / 53 / 26 / 1 / 1; further rows named 8, substitution
     part 1 named 2, recognition part 2 18; every quotation found once in its record; **expected blob
     `d00497918ff18efe85fb9ed97543decf7df49b25`** (5,301,823 bytes, 84,538 lines; the 4,638 bytes added equal the sum
     from the ten lines, their blanks and the in-progress line's change). Re-run after the last edit to the draft: the
     same blob.
3. **Degradation tells: two, both in the writing, both caught before anything was used or landed** — (1) a broken
   check line in the simulation script, which failed on its first run and was replaced by the check intended; (2) a
   provenance sentence in the draft naming wider line ranges of the list-answers part 2 record than were read
   (*"1–45, 94–137"* where 1–12, 25–45 and 100–137 were read), narrowed before landing. Told to the user as *"I have
   already made two of these"*; hence the handover at this verified stop. **On the model (2026-11-12):** both tells came
   late in a long sitting that carried a full verification and a full writing; nothing here separates load from model,
   so no suspicion about Opus is raised.

## 3. The plan — carried forward

1. **Now: a NEW Cowork session checks session 20's instruction as a turn of its own** (Ruling 1 (e)), on the pattern of
   entry 1220 §2: every quotation, part name and settlement against the two records (read whole); the 10 rows, each
   found once and read whole (shape, no earlier line, UNPLACED at the part named, the fit); the reading file's counts,
   size, headings and line 54; the §10 and §11 searches; the big dispatch's ranges, §L.33 and §L.34 whole, forms (b)
   and (b-H) and the paragraph *Which ADOPTED word*; the list-answers part 2 record's Rulings A, 3 and 4 and the two
   surfaces' §3.2 sentences; the precedents the settlements cite; every hash in the file; **and a re-simulation from the
   instruction's own text, which should give `d0049791…`**. Then it **adds its own entry 1222 to what act 1 lands**
   (§1 item 5, §4 item 3, §5 act 1 and its subject, and, if it judges it right, §2 item 4's two entries to read),
   corrects anything it finds (former wording kept or not, as the instruction is unreleased), lands, and **only that
   session tells the user what to hand to Claude Code**.
2. **Then Claude Code executes session 20's instruction:** lands it and entries 1221 and 1222, applies §L.33 and §L.34,
   writes its report `records/cc/reports/cc_report_l3_application_session_20_task_3_stretch_11_2026_11_24.md`, stops.
3. **Then a NEW Cowork session verifies session 20's stretch and, under Rulings 1 and 2, writes the next stretch's
   instruction in the same sitting**, from §L.35 (the remarks on §L.35 in §2 item 2 above are this sitting's reading,
   to be re-judged at the objects there).
4. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above, and the user's two rulings of 2026-11-24 (§0). **Practical notes, no
rules:** as entries 908 and 910 to 1220 §3, and: (a) in this sitting the container shell ran `python3 -I` scripts on
staged copies (hashing, decompression, simulation), `grep`, `sed -n`, `diff`, `cmp`, `cut`, `tr`, `awk`; the refusals
entry 1220 met did not recur; (b) loose git objects can be staged by their path under `.git/objects/` and walked one
tree level per staging call; (c) entry 1222's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_twenty_two.md`; check by staging.

## 4. Who does what, in this order

1. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_twenty_one.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1222 exists (if it does, report and ask), reads this entry whole,
   entry 1220 whole (the checking pattern) and entry 1026 §3, asks the session-start read, reads the three git reference
   files (they should still read `9037f1b2…`), then does §3 step 1.
2. **Nothing goes to Claude Code from this entry.** The instruction to hand session 20's instruction to Claude Code
   comes only from the checking session (Ruling 1 (e); the user's rule of 2026-10-26).
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies only: `python3 -I` scripts kept in a scratch folder outside
  the staged tree (decompressing and hashing git objects, walking trees, rebuilding and simulating the reading file on
  copies, checking quotations), `grep`, `sed -n` (on staged copies, and once `sed -i` on this sitting's own scratch
  script), `diff`, `cmp`, `cut`, `tr`, `awk`, `cat` of the staged ref files. Nothing written by any shell into a staged
  copy or the outputs folder, except the draft's placeholders filled by a `python3 -I` script in the outputs folder
  (the draft, before landing).
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the git reference files (twice); 25 loose git objects
  (the four commits, their trees on the changed paths, the stretch 9 blob); session 19's instruction and report; the
  reading file (twice); entry 1219; the two records of §L.33 and §L.34 and that of §L.35 (for its size only); the
  list-answers part 2 record; the further-rows and substitution part 1 surfaces; the big dispatch. **Listed:** the
  repository root. Four paths asked for by staging and found free (the session 20 instruction and report paths, entry
  1221, and the instruction path again after the pause).
- **Read beyond the boot list:** session 19's instruction and report whole; entry 1219 whole; the two records whole;
  the big dispatch at lines 99–278, 3450–3655 and 6616–6820, by search for its `### §L.` headings and §L.35's table,
  and at lines 1–5, 395–397 and 7111–7113; the reading file at the 10 rows of §L.33 and §L.34, line 54,
  its headings, and by search; the list-answers part 2 record at lines 1–12, 25–45 and 100–137 and its headings; the
  surfaces at line 116 and lines 162–165.
- **The instruction and this entry written in the outputs folder with the Write tool and landed with the commit tool.**
  No git on the device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1220. The user's words: the opening
instruction with Claude Code's closing message and the two rulings; "shortened"; "Yes" (land the draft unchecked).*
