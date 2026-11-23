# Cowork handoff entry 1207 — 2026-11-23 — SESSION 14 STOPPED ON A PLACEMENT CONFLICT, RESUMED ON THE USER'S RULING "A", AND FINISHED; SESSION 14 VERIFIED AT THE OBJECTS; HANDED OVER ON TWO DEGRADATION TELLS; SESSION 15'S INSTRUCTION (§L.24 ALONE) IS THE NEXT SESSION'S

**The current entry point.** Entry 1206 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1207 asked for by staging in a call of its
  own, *"does not exist"*; asked once more by staging immediately before this entry was written, in a call made beside
  one tool-loading call, *"does not exist"*. Entry 1206 (10,578 bytes),
  entry 1205 (10,510) and entry 1026 (11,103) read whole.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` read whole (11,726 bytes,
  1794136674043, unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207,
  unmoved; the gating answer 247 open, 222 gating, 25 non-gating (`tools/audit/nongating_apparatus_rows.json` lines
  183–185). `CLAUDE.md` came with the user's second message, whole.
- **Git [checked, at the ref files and the commit objects]:** `.git/HEAD` *"ref: refs/heads/master"*;
  `refs/heads/master` and `refs/remotes/origin/master` both `90cddaf575ac83ec444bb637050726eab34a24c2` (modification
  times 1795465791931 and 1795465795499). The chain from `d56ccc6e…`: act 1 `0ed08e109c8baeb206f285a874ab14685d79688b`,
  act 2 `b897b16ccac7db11954a3e187a3cb4acc361d39e`, act 3 `90cddaf5…`, each with exactly one parent. Nothing is
  running; no dispatch is out.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only (untracked). **Untracked writing-side entries: 1206 and 1207**;
  session 15's act 1 lands both with its instruction.

## 2. What this sitting established

1. **Session 14 stopped after act 1, on a placement conflict, and the record settled it [checked].** At Row 36.111 the
   row's `*PROPOSED DISPOSITION.*` paragraph is followed by a paragraph headed *"The decisions register at this row."*
   The big dispatch's form (b) (its lines 122 and 255) puts a ruled or recorded line *"immediately beneath a row's
   `*PROPOSED DISPOSITION.*` paragraph"*; session 14's instruction §3.1 item 2 said *after the row's last existing
   paragraph*, which on those rows is the register paragraph; its §0 makes the big dispatch the authority for every
   order §4 does not replace, and §4 does not list placement. Every earlier stretch's line on a row carrying a register
   paragraph stands above it: 18 lines on 15 rows, none below (read by script over the working-tree copy staged at
   boot). So no real choice remained; the user ruled **"A"**: the new line directly beneath the proposed paragraph, one
   blank line after it, above the register paragraph. Seven row-parts were affected: 36.111 (ii), 43.19 (ii), 43.124
   (ii), 44.30 (i), (ii), (iii) and 45.21 (i). Documentation only; no disposition, count or algorithm changed.
2. **Two defects of the writing side, found by session 14 and confirmed here [checked]:** (a) session 14's instruction
   §3.1 item 2 assumed that every row's last paragraph is its proposed paragraph; on the five rows above it is not;
   (b) entry 1206 §2 item 1 (and entry 1205 §2 item 1) say every row of the stretch ends with a blank line then `---`;
   Row 17.2 ends at `#### Not a statement, at this member`. CC placed Row 17.2's line under the proposed paragraph, before
   that heading, which is where form (b) puts it; the user confirmed it with the ruling. Neither defect moved any line.
   Corrected forward in §3 step 1 below, not in the landed files.
3. **Session 14 verified at the objects [checked], on the pattern of entry 1204 §2:**
   - by tree comparison (every changed tree object inflated): act 1 adds exactly the instruction (blob `ad8fb163…`, the
     checked copy) and entries 1204 and 1205 (1205's blob `a648dcb6…`, equal to the file on disk); act 2 changes only
     `ratification_surfaces/cowork_comparison_l3_reading.md`, blob `5bccffae70dcdf713d25549aa7ef7bca4e09bf4a` →
     `39a8a4b3ba86179b205ff2a73d9e709c88821733` (equal to the file on disk, 5,260,516 bytes); act 3 adds only the report
     (blob `ebb1220a…`, equal to the file on disk, 25,582 bytes). Both subjects exactly as the instruction gives them;
   - the reading file against `5bccffae…`: **197 added, 1 deleted**; against the Task 2 commit's blob `48e24b2f…`: **871
     added, 4 deleted**. The 115 non-blank added lines equal, as a multiset, the instruction's §3.2 to §3.5 texts rebuilt
     by script (82 row lines with `<claim>` filled from the row lists, 22 *LEAVES L3*, 9 §11 entries, the NOT QUARANTINED
     line, the in-progress line): none missing, none extra. The one deletion is the former in-progress line;
   - per row (all 77, each heading once): the row's new lines are exactly its expected lines, each with one blank line
     before and after, standing directly beneath the proposed paragraph or after the earlier lines (Rows 2.6, 3.5, 7.189,
     7.209, 9.89, 19.38, 38.26), above the register paragraph on the five rows of item 1; Row 17.2 as item 2 says;
   - every §10 line beneath the old line §3.3 names (after session 13's *LEAVES L3* line on items 2, 3 and 9); every §11
     line between the old lines §3.4 names; Row 35.154's NOT QUARANTINED line beneath old line 82035;
   - counts: `*RULED DISPOSITION (` 353, `*RULED PLACEMENT (` 3, `*RECORDED DISPOSITION (` 53, `*LEAVES L3 (` 26,
     `*Row 7.67 is not transferred` 1, `*NOT QUARANTINED (` 1;
   - **the report read in FULL**: it agrees with all of the above; it declares the STOP and the ruling, Row 17.2, the
     context summary after the STOP (the 119 earlier lines kept and confirmed by the file checks), the late order of
     *LEAVES L3* items 16 to 22, the pin-first departure, extra read-only git commands, and entry 1206 untracked; it
     corrects its STOP message's count of earlier lines from 11 to 18 on 15 rows, stating its patterns.
   Nothing found to correct; nothing corrected.
4. **One error of this sitting's own process, corrected by the user:** the message for Claude Code (the ruling "A")
   was given to the user before this sitting's boot was complete (the session-start read not yet asked), and when the
   user asked which to do first, both were offered as parallel acts. The user: *"giving CC a piece of work out of sync
   with where you are is DANGEROUS … never to give any instructions that even smell like two dispatches at once."* The
   message's content was checked before it was given and did not change; the order did. Re-given as one numbered
   sequence after the boot completed.
5. **Degradation tells (2026-08-15 list): two**, reported to the user as *"I have already made two of these"*; handed
   over at this verified stop on his "yes": (a) an identifier asserted that was never derived — an object path staged
   with a full hash whose tail was made up from the known eight characters `5bccffae`; the device answered *"does not
   exist"*, and the full hash was then taken from the commit tree; nothing rested on it; (b) refuted shortcuts — a
   comparison by Python's `difflib` that ran past the time limit and was stopped, and a placement check that looked lines
   up by text alone (ambiguous where rows without a claim carry identical lines); both redone before any result was used.
   **On the model (2026-11-12):** nothing suggests Opus was not enough for the verification itself; the tells came in the
   mechanics of a long sitting.

## 3. The plan — carried forward

1. **Next Cowork session: write session 15's instruction — §L.24 alone, sized at the objects**, on the pattern of
   session 14's instruction, and check it as a turn of its own before it is handed over (in the same session if capacity
   allows and no tell has appeared, otherwise by the next). **Carry forward from §2 items 1 and 2:** the placement rule
   is written as form (b) gives it — *immediately beneath the row's `*PROPOSED DISPOSITION.*` paragraph, after any
   earlier ruled or recorded lines standing there, and above any paragraph that follows them* (a decisions-register
   paragraph, an *"At the source now."* paragraph), never "after the last existing paragraph"; and the row check reads
   each row's actual shape after the proposed paragraph and its actual ending (`---` or a `####` heading), stating both
   per row rather than assuming one shape. Session 15's act 1 lands the instruction with entries 1206 and 1207. Land on
   the user's word, prove by staging back, then give the user the hand-over to Claude Code with the long opening line of
   2026-10-26 — as ONE numbered sequence, and only once that session's own boot and check are complete (§2 item 4).
2. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1192 §3 step 3, and entry 1205 §2
   item 2's settlements (in session 14's instruction, overrulable; session 14 applied them).

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1206 §3, and: (a) a tree
comparison needs every changed tree object staged by path under `.git/objects/`, level by level (about six rounds for
this repository's depth); take each full hash from the parent tree, never complete one by hand; (b) for the added lines of
an 84,000-line file use `diff --unchanged-line-format='' --old-line-format='' --new-line-format='%dn %L'`, not
`difflib`; (c) rows without a claim share identical line text, so place lines by row heading and row range, not by text;
(d) the reading file now stands at blob `39a8a4b3…`, 84,233 lines; (e) entry 1208's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_eight.md`; check by staging.

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** Session 14 is finished and verified; no dispatch is written for
   session 15 yet. Only the session that writes and checks session 15's instruction tells the user what to hand to
   Claude Code.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_seven.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1208 exists (if it does, report and ask), reads this entry whole,
   entry 1206 whole and entry 1026 §3, asks the session-start read, reads the three git reference files (anything but
   `90cddaf5…` means something ran: find out what first), then does §3 step 1.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only searches and measurements over staged copies (`grep`, `sed -n`, `cut`, `awk`, `diff`,
  `wc`, `python3 -I` reading files, inflating git objects, computing blobs, comparing texts), scripts and outputs under
  `/home/claude/scr`. One comparison was moved to the background by the tool's time limit and stopped with the stop tool.
  Nothing written by any shell into a staged copy, the repository or the device.
- **Staged beyond the boot list:** the git reference files (twice); session 14's instruction; the big dispatch; the
  reading file (twice: mid-stretch and final); `STATUS.md` and the gating JSON; session 14's report; the commit objects
  of `0ed08e10…`, `b897b16c…`, `90cddaf5…` and `d56ccc6e…`, the tree objects along the changed paths, and the blobs
  `5bccffae…` and `48e24b2f…`. One staging of a made-up object path failed (§2 item 5 (a)). **Listed:** the repository
  root; `.git/objects/0e`.
- **This entry written in the outputs folder** with the Write tool and landed with the commit tool. No git on the device,
  widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-23 (Stockholm), the sitting booted on entry 1206. The user's words: the opening instruction
with session 14's STOP message; "shortened"; the correction of the out-of-order hand-over; session 14's closing message;
"yes" (the hand-over and this entry).*
