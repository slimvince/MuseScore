# Cowork handoff entry 1215 — 2026-11-24 — SESSION 17 VERIFIED AT THE OBJECTS; NOTHING TO CORRECT; THE HASH MEASUREMENT RAN; THE USER'S RULE THAT A MESSAGE NEVER BOTH ASKS AND HANDS OVER; HANDED OVER BEFORE WRITING SESSION 18'S INSTRUCTION, ON A CAPACITY JUDGMENT; SESSION 18'S INSTRUCTION IS THE NEXT SESSION'S

**The current entry point.** Entry 1214 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rule of 2026-11-24 — read this first

**A message to the user either asks him ONE question or hands over to another session — NEVER BOTH.** A hand-over comes
only after every question of the sitting has been answered, and it is the last thing the sitting sends. *The user's
words, at this sitting's opening:* *"you did two concurrent things (which OF COURSE is impossible to do): you gave me a
handoff to another session AND asked me a yes/no question at the same time."* And: *"If CC you or CC does anyting out
of sync we are in deep shit."* The error was the previous sitting's (entry 1214's); its message is not quoted here
because this sitting did not see it. It sharpens the user's rule of 2026-09-27 (who does what, and in what order, at
every handover, with zero room for confusion). This sitting asked its last question (whether to hand over) in one turn
and handed over only after the user's "yes".

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1214 read whole (11,995 bytes). Entry 1215
  asked for by staging, in a call of its own, before any other boot read: *"does not exist"*; asked once more, in a
  call of its own, immediately before this entry was landed. Entry 1213 (10,536 bytes), entry 1211 (10,503) and entry
  1026 (11,103) read whole.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` read whole (11,726 bytes,
  1794136674043, unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207,
  unmoved (772 lines by `wc -l`); the gating answer 247 open, 222 gating, 25 non-gating
  (`tools/audit/nongating_apparatus_rows.json` lines 183–185). `CLAUDE.md` came with the user's first message, whole.
- **Git [checked, at the ref files and the commit objects]:** `.git/HEAD` *"ref: refs/heads/master"*;
  `refs/heads/master` and `refs/remotes/origin/master` both `03a15953c701aeaece39a2932f8132719bc2c465` (modification
  times 1795476766357 and 1795476772108, as entry 1214 gives them). Nothing is running; no dispatch is out.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only (untracked). **Untracked writing-side entries: 1214 and 1215**;
  session 18's act 1 lands both with its instruction.

## 2. What this sitting established

1. **The hash measurement ran, unrefused [checked].** A `python3 -I` script on standard input over staged copies
   computed blobs, inflated git objects and compared texts; nothing was refused this sitting. With entry 1214 §2 item
   1's two refusals and entry 1213's unrefused run, the app's check is not consistent across sittings; the next
   sitting tries once and, if refused, reports to the user and lets him decide.
2. **Session 17 verified at the objects [checked], on the pattern of entry 1211 §2 item 1:**
   - the chain `8771c9b8…` → act 1 `20bb213f0d20e43ef9a8138da38b05cf6cf680e7` → act 2
     `e61ad38abad3fcf6637f668c55defe0aef5fe3e6` → act 3 `03a15953…`, each commit object's hash recomputed, each with
     exactly one parent; each subject exactly as session 17's instruction gives it (§5 act 1, §4 item 8, §5 act 3),
     each message ending with the `Co-Authored-By` line;
   - by tree comparison (every changed tree object inflated, from the root trees down the changed paths): **act 1** adds
     exactly five files — the instruction (blob `29c2d8cc56b61a5ef8eac5985933d1f40b9e724a`, equal to the file on disk,
     50,719 bytes, 536 lines, no carriage return) and entries 1210 (`c3c3aca1…`), 1211 (`6fe8bafc…`), 1212 (`c9caf97d…`)
     and 1213 (`63e155c5…`), each equal to the file on disk; their lines 536 + 117 + 116 + 137 + 118 = 1,024, the report's
     insertions; **act 2** changes only `ratification_surfaces/cowork_comparison_l3_reading.md`, `7103b87c…` →
     `b98e85128b11e363a0f909fb79fc5c3389499be7`, equal to the file on disk (5,280,457 bytes, 84,462 lines, no carriage
     return, device modification time 1795476624782); **act 3** adds only the report (blob
     `c0bcadfd38e02292299874931aa165610d1e9ef0`, equal to the file on disk, 19,859 bytes, 240 lines);
   - **the reading file rebuilt independently and found byte-identical to the file on disk:** from the old blob
     inflated, the 19 lines, the four §10 entries and the in-progress line each taken from the instruction's own text
     (§3.2 lines 240, 245, 250, 255–269; §3.3 lines 320–323; §3.5 item 3, line 347), each row's line(s) placed after the
     blank line following its `*PROPOSED DISPOSITION.*` paragraph, the §10 entries after the blank-line-terminated entry
     opening `- Row 38.11 (i) — the key-independent chord symbol for each slice`. Rows 46.18 and 46.19 carry the
     decisions-register paragraph after the new line; the other 13 nothing. So every line's text and place, the four §10
     entries (lines 80618–80621) and line 54 are as the instruction orders;
   - from the old blob to the file on disk: 43 added, 1 deleted; counts after `*RULED DISPOSITION (` 427,
     `*RULED PLACEMENT (` 3, `*RECORDED DISPOSITION (` 53, `*LEAVES L3 (` 26, `*Row 7.67 is not transferred` 1,
     `*NOT QUARANTINED (` 1; record names lead-rows 23, key 0. The report's 19 line numbers each found at its row;
   - **the report read in FULL**: it agrees with all of the above. Its §7 declares six departures (the pin taken after
     the read, by the declared-departure route; the quotation check and decided-against search by a read-only script;
     the §10/§11 searches by a bare-number pattern; field-name lines seen in the gating JSON; further read-only git
     commands; `DECISIONS.md` in five ranges, which fits its 772 lines). None touches the result, which the
     byte-identical rebuild settles.
   - **Not checked here [relayed]:** the untracked-path listing of the report's §1 item 5 (needs git's working-tree
     listing); the 1,023 added and 4 deleted against the Task 2 commit (follows by derivation from entry 1211's 981
     and 4 plus this stretch's 42 added lines). The quotations were checked against the record by entry 1214's sitting,
     not again here.
   Nothing found to correct in session 17's work; nothing corrected.
3. **One small error in entry 1214, not corrected there (a landed entry of a read-only session):** its §1 and §3 step
   2 say the report's §7 declares *"four departures"*; it declares **six**. The figure was taken from Claude Code's
   closing message, which lists four bullets, not from the report.
4. **Handed over before writing session 18's instruction, on a capacity judgment, on the user's "yes"** to
   recommendation 1 (hand over now), put against option 2 (write it in this sitting). No degradation tell (2026-08-15
   list) appeared. The judgment: this sitting holds `CLAUDE.md` whole (about 170 KB), session 17's instruction whole,
   its report whole and the whole verification; entry 1211 handed over at the same point, and entry 1213's sitting got
   two tells writing an instruction in a similar load. **On the model (2026-11-12):** nothing suggests Opus was not
   enough; the concern was the sitting's load.

## 3. The plan — carried forward

1. **Next Cowork session: write session 18's instruction — §L.31 onward, sized at the objects** — on the pattern of
   session 17's instruction (`records/cc/instructions/cc_instruction_l3_application_session_17_task_3_stretch_8_2026_11_24.md`,
   read whole), and check it as a turn of its own before it is handed over (in the same session only if capacity allows
   and no tell has appeared, otherwise by the next). §L.31 has 28 row-parts (entry 1212 §2 item 3 [relayed]). Size the
   stretch at the big dispatch and the rows, judging out loud whether more than one entry fits, stopping at an entry
   boundary (Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md`).
   Read the stretch's records whole and every row-part at the reading file, stating each one's word, whether *as
   proposed* is written, its shape after the proposed paragraph and its ending; search §10 and §11 for each. Carry
   forward entry 1207 §3 step 1's placement and row-shape rules and the form-(b) two-record rule by part. **Session 18's
   act 1 lands the instruction with entries 1214 and 1215.** Land on the user's word, prove by staging back. **Only after
   that session's own check is complete and every question of it is answered** does it give the user the hand-over to
   Claude Code with the long opening line of 2026-10-26, as ONE numbered sequence (§0 above; entry 1207 §2 item 4).
2. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2.

**Carried rules:** as entry 1026 §3, and §0 above. **Practical notes, no rules:** as entries 908 and 910 to 1214 §3, and:
(a) session 17's expected start state for session 18: the tip `03a15953…`; the reading file at blob `b98e8512…`, 84,462
lines; counts 427 / 3 / 53 / 26 / 1 / 1; against the Task 2 commit 1,023 added and 4 deleted [relayed by derivation];
(b) the reading file's `##` headings now: §6 at line 435, §7 at 79435, §10 at 79893, §11 at 80984, §12 at 83137;
(c) the strongest check of a stretch, used here: rebuild the new file from the old blob with the instruction's own
texts and placement rule and compare bytes with the file on disk (this sitting's script `sim17.py` is not carried; a
new session has a fresh container); (d) loose git objects stage and inflate quickly — walk the changed tree paths from
the root trees; (e) entry 1216's file name would be `cowork_handoff_entry_one_thousand_two_hundred_and_sixteen.md`;
check by staging.

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** Session 17 is finished and verified; no instruction is written for
   session 18 yet. Only the session that writes and checks session 18's instruction tells the user what to hand to
   Claude Code.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_fifteen.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1216 exists (if it does, report and ask), reads this entry whole,
   entry 1214 whole, entry 1213 whole, entry 1212 whole and entry 1026 §3, asks the session-start read, reads the three
   git reference files (both at `03a15953…` when this entry was written; anything else means something ran: find out
   what first), then does §3 step 1.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only measurements over staged copies (`wc -l`, `grep`, `awk`, `cut`; `python3 -I` with its
  script on standard input or as a file under `/home/claude/scr`, the paths passed as arguments: computing blobs,
  inflating git objects, comparing trees, rebuilding the reading file in memory and comparing bytes). Two helper
  scripts written under `/home/claude/scr` in the container. Nothing written by any shell into a staged copy, the
  repository or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON and `DECISIONS.md`; the git reference files; session
  17's instruction and report; entries 1210 and 1212; the reading file; the commit objects of `20bb213f…`, `e61ad38a…`,
  `03a15953…` and `8771c9b8…`, the tree objects along the changed paths and the blob `7103b87c…`. **Listed:** the
  repository root.
- **One message sent with the verbatim message tool** at the opening (who does what). This entry written in the
  outputs folder with the Write tool, sent to the user and landed with the commit tool. No git on the device, widget,
  task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1214. The user's words: the opening instruction
with Claude Code session 17's closing message; the rule of §0; "shortened"; "yes" (hand over before session 18's
instruction is written, this entry and the hand-over).*
