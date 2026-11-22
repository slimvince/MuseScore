# Cowork handoff entry 1061 — 2026-11-17 — RELEASE STEP 5, PART 3 SIZED, NOT STARTED: PART 3 PROPOSED AS TWO SITTINGS; NOTHING EDITED BUT THIS ENTRY; HANDED OVER AT A VERIFIED STOP

**The current entry point.** Entry 1060 is superseded as entry point and stands otherwise; its §3 is the plan, carried
forward with the split in §3 below. Release step 5 of entry 767 §3: parts 1 and 2 complete; part 3 (the D-250
revalidation) sized and not started. **[checked]** means read at the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1061 (staging answered *"does not exist"*, in a call of its own, after entry 1060 was
  read and before any other boot read; asked again, in a call of its own, before this entry was written). Entry 1060 at
  14,296 bytes as staged; entry 1059 at 14,944; entry 1053 at 15,142; entry 767 at 10,922; entry 584 at 4,843; the
  working file at 573,300; the dispatch at 874,206; the check file at 307,273, as entry 1060 says. Read: entries 1060,
  1059, 1053, 767 and 584 whole; the working file at lines 1–64; the check file at lines 1–25, at each of findings 1 to
  36 (printed by read-only `python3 -I`, each to the next bold heading or at most 30 lines, each print cut at 800
  characters), at lines 320–325, and from line 2374 to its end. The frozen copy and the findings section not read. The
  handoff folder not listed.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714 (LIVE).
- **Git [checked at boot]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no dispatch
  is out.
- **The user's leave for read-only searches**, carried by entry 1060 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line. Kept: no shell wrote anything (§5).
- **Changed on disk by this sitting:** this entry only (written after the user's "yes" to the handover). **Not edited:**
  the check file (307,273 bytes), the dispatch (874,206 bytes, NOT YET RELEASED), the working file (573,300 bytes) and
  the release list (459,987 bytes [relayed from entry 1060]).
- **Not in git:** as entry 1060 §1 lists, plus entry 1061.

## 2. What this sitting established

1. **D-250's text [checked]:** `DECISIONS.md` line 680, *"Dispatches are written only when they are next; a parked
   instruction is revalidated first"*, LIVE, citing `cowork_audit_protocol.md`. There, lines 249–259: an instruction
   file that is not the active dispatch *"must be revalidated against the then-current `STATUS.md` and HEAD immediately
   before dispatch, receiving a dated dispatch note"*. Entry 767 §3 step 5 adds *"refs, records landed since
   2026-11-08"*.
2. **Observed, not written as a finding:** `STATUS.md`'s modification time is 2026-11-08 12:17:54 (Stockholm), earlier
   than the local ref file's 12:33:25, both as their stagings returned; its latest entry is the close of the second
   resume batch; both refs at `e855ff2a…`. So against `STATUS.md` and HEAD nothing has moved since the tip commit, as far
   as these objects show. Part 3 writes this up at its own reads; this sitting landed nothing in the check file.
3. **Part 3 sized [checked at a listing of `tools/audit/`]:**
   - **Item (b) of entry 1024 §2 item 2** (untracked files outside the three folders: the rulings folder,
     `ratification_surfaces/` and the handoff folder): needs recursive listings of the repository's top-level folders
     other than those three, each file's modification time compared with the local ref file's (12:33:25). The file
     tools cannot tell an untracked file from a tracked one, so a listing gives files changed since the tip commit,
     each then to be judged. How many folders and files that is was not established.
   - **The E5 question** (the third part 2 section, row 14): the three tools `STATUS.md` names stand at
     `gen_governing_surface_split.py` 41,416 bytes, `gen_status_residue_move.py` 27,877 and `gen_status_batch_bound.py`
     352,058. The last cannot be read whole in one sitting; it needs reading by search, at its `--check` path. A2 marks
     as UNSETTLED which guard tools read `STATUS.md`; the guard run counts 87 tools (70 passing, 13 failing, 4 not run
     [relayed from the check file's first part 2 section, row 10]), so the three named tools may not be all of them.
4. **Handed over on capacity before starting any item**, at a verified stop, on the user's word "yes": the boot read,
   the sizing and one large folder listing took most of the sitting's room, and starting either item would have stopped
   inside it. **Degradation tells from the standing list (2026-08-15): none noticed.**
5. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. Nothing this sitting met shows
   whether a different model would have done better or worse.

## 3. The plan — carried forward

1. **Next: part 3, first sitting** (proposed by this sitting, told to the user before his "yes"; open to his overrule):
   the D-250 revalidation against `STATUS.md`, HEAD and the refs as they then stand, written up at its own reads; then
   item (b), the untracked-file question, by the listings in §2 item 3. **Size it out loud after the core check** (how
   many folders, how many files changed since 12:33:25) and stop at an item boundary. **Findings only, no dispatch
   edit.** Anything that needs the user goes to him as a self-contained surface in the form of `CLAUDE.md` lines
   1850–1924, the question in a later turn (check the record first, D-599). Add the results as a new section after the
   sixth part 2 section's provenance line (line 2732) and before slice 1's provenance line (lines 2734–2735, the file's
   last); show the addition before landing, exactly as it will land; land and prove it.
2. **Then part 3, second sitting:** the E5 question, the three tools read at their `STATUS.md` checks
   (`gen_status_batch_bound.py` by search only), and whether any other guard tool reads `STATUS.md`.
3. **Then parts 4 and 5 and step 6**, as entry 1060 §3 step 2 gives them.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1060 §3, and: (a) the
check file's line list is entry 1060 §3 note (a), unmoved. (b) `tools/audit/` lists about 280 entries; list it only if
a proof needs it. (c) Entry 1062 is `cowork_handoff_entry_one_thousand_and_sixty_two.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_sixty_one.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1062 exists (if it does, report and ask). It reads **this entry whole**, **entry 1060 §3 and §5**,
   **entry 1053 §3** (for the findings' line list), **entry 767 whole** (10,922 bytes), **D-250** at `DECISIONS.md`
   line 680 and `cowork_audit_protocol.md` lines 249–259, the working file at **its opening part (lines 1–64)**, and
   **the check file at lines 1–25, at each finding** by the line lists in entry 1053 §3 note (a), entry 1059 §3 note (a)
   and entry 1060 §3 note (a), **at lines 320–325, and from line 2541 to the file's end** (the six part 2 sections;
   slices 45 and 46, lines 2374–2539, are not needed for part 3). It does **not** read the check file's slice tables
   otherwise, the frozen copy or the findings section whole, and does **not** list the handoff folder. It proves this
   entry's size as the device reports it when staged, the working file at 573,300, the dispatch at 874,206 and the
   check file at 307,273, and reads both ref files (anything but `e855ff2a…` means something ran: find out what first).
   The check file is at `C:\s\MS\ratification_surfaces\`, not under `records\cowork\`. It reports the boot with a
   capacity judgment, asks the session-start read, then does §3 step 1. **If the user orders the whole check file read
   instead, it reads it whole** (in parts with the Read tool).
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies only (`cd`, `grep`, `cut`, `sed -n`
  in pipes; `python3 -I` printing findings 1 to 36 and lines 320–325; `date` converting three modification times). **No
  redirect.** No shell wrote or deleted anything, in the container or on the device. This entry written with the Write
  tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted.
- **Entry 584 read whole**, as §4 step 3 of entry 1060 points to it. **Entries 1059 and 1053 read whole**, though only
  their §3 and §5, and §3, were asked.
- **Read beyond entry 1060 §4 step 3's list:** `DECISIONS.md` line 680 and a search for *"D-250"*;
  `cowork_audit_protocol.md` by search and at lines 247–262; `STATUS.md`, the gating JSON and `DECISIONS.md` line 714
  as the session-start read.
- **Folders listed:** `tools/audit/` once (to size the E5 question). The handoff folder not listed.
- **Finding the files:** entries 1059, 1053, 767 and 584 staged by their spelled-out names; the check file at the path
  entry 1060 gives; the working file and the dispatch by the names the check file's opening gives;
  `cowork_audit_protocol.md` at the repository root, from D-250's row; each found at the first try.
- **Landing route:** this entry written in the outputs folder and committed from there by its path, in a call of its
  own after its last edit.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1060. The user's words: the opening
instruction; "shortened" (the session-start read); "yes" (writing this entry, on the sizing and the proposed split
said before that question).*
