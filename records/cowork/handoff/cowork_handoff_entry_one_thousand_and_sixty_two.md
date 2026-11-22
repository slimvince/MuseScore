# Cowork handoff entry 1062 — 2026-11-17 — RELEASE STEP 5, PART 3, FIRST SITTING: THE D-250 REVALIDATION AT THE TIP DONE (NOTHING MOVED); ONE NEW FINDING (48, FOR STEP 6); ITEM (b) SIZED AND NOT TAKEN; THE CHECK FILE LANDED AND PROVED; NO DISPATCH EDIT; HANDED OVER AT A VERIFIED STOP

**The current entry point.** Entry 1061 is superseded as entry point and stands otherwise. Release step 5 of entry 767
§3: parts 1 and 2 complete; part 3 (the D-250 revalidation) begun: its check at the tip is done, item (b) and the E5
question are next (§3 below). **[checked]** means read at the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** no entry 1062 (staging answered *"does not exist"*, in a call of its own, after entry 1061 was
  read and before any other boot read; asked again, in a call of its own, before this entry was written). Entry 1061 at
  10,979 bytes as staged; entry 1060 at 14,296; entry 1059 at 14,944; entry 1053 at 15,142; entry 767 at 10,922; entry
  584 at 4,843; the working file at 573,300; the dispatch at 874,206; the check file at 307,273, as entry 1061 says.
  Read: entries 1061, 1060, 767 and 584 whole; entry 1053 §3 and entry 1059 §3; D-250 at `DECISIONS.md` line 680 and
  `cowork_audit_protocol.md` lines 249–259; the working file at lines 1–64; the check file at lines 1–25, at each of
  findings 1 to 47 (printed by read-only `python3 -I`, each to the next bold heading or at most 30 lines, each print cut
  at 800 characters, in two prints; the first print's output was itself cut by the tool after finding 38, and findings
  39 to 47 were printed again), at lines 320–325, and from line 2541 to its end. The frozen copy and the findings
  section not read. The handoff folder not listed.
- **Session-start read shortened** on the user's word ("shortened"): `STATUS.md` whole (latest entry still the close
  of the second resume batch, 2026-11-08); `tools/audit/nongating_apparatus_rows.json` lines 24–59 (`open_rows` 247,
  `non_gating` 25); D-599 at `DECISIONS.md` line 714 (LIVE).
- **Git [checked]:** `.git/HEAD` is `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both at `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`. Nothing is running; no dispatch
  is out.
- **The user's leave for read-only searches**, carried by entry 1061 §4 step 2's opening line, which the user gave this
  sitting. Carried to the next session by §4 step 2's opening line. Kept: no shell wrote anything (§5).
- **Changed on disk by this sitting** (the section's text sent to the user in full before landing, his word "yes" given
  after the question whether to land; the landing guarded by the device copy's modification time, checked at a listing
  of `ratification_surfaces/` just before, unchanged since staging; proved by staging back, the device's byte count and
  moved modification time read from the staging result, and the landed passage read with the Read tool from line 2730
  to the file's end; no shell used for the proof):
  - **The check file** (`ratification_surfaces/cowork_l3_application_release_check_2026_11_16.md`), one landing: the
    section *Part 3, first sitting — the D-250 revalidation at the tip, and item (b) sized*, after the sixth part 2
    section's provenance line (2732, read unchanged after landing) and before slice 1's provenance line. Now
    **314,255** bytes. The section stands at lines 2734–2757; slice 1's provenance line at 2759–2760, still the file's
    last line. The edit inserted text only. The landed text is the text shown [checked: the section compared with its
    draft by a read-only `python3 -I` over the edited copy, ending at the LAST occurrence of slice 1's provenance line,
    before sending: *True*]. The first commit landed the current text (not stale).
  - This entry (new).
  - **Not edited:** the dispatch (874,206 bytes, NOT YET RELEASED), the working file (573,300 bytes) and the release
    list (459,987 bytes, at the `ratification_surfaces/` listing).
- **Not in git:** as entry 1061 §1 lists, plus entry 1062.

## 2. What this sitting established

1. **The D-250 revalidation at the tip: nothing has moved [checked].** HEAD, both ref files, every other file under
   `.git/refs` (none later than 2026-06-30), `packed-refs`, `FETCH_HEAD`, `ORIG_HEAD`, the index and `COMMIT_EDITMSG`
   (both at 2026-11-08 12:33:25, the local ref file's second), no `index.lock`; `STATUS.md` at 2026-11-08 12:17:54 with
   the same latest entry. No record committed since 2026-11-08. Written up as item 1 of the landed section.
2. **Finding 48 (new, for step 6):** D-250 asks for the revalidation *"immediately before dispatch"*, *"receiving a
   dated dispatch note"*; parts 4 and 5 come between, and the dispatch names no place for the note (a whole-dispatch
   search for *"PARKED"*, *"dispatch note"*, *"revalidat"* and *"immediately before"* found none). Proposed: the
   releasing sitting repeats the check at the objects as they then stand, and its release statement carries the dated
   note. Not a question for the user (D-250's own words); open to his overrule. Not a dispatch edit by part 4.
3. **Item (b) sized, not taken [checked at the top-level listing and `.gitignore`]:** 47 top-level folders; 11 ignored
   as whole folders; `ratification_surfaces/` one of the three; 34 to list with their subfolders, named in the landed
   section. Several probably exceed one listing's 2,000-entry cap. Did not fit this sitting.
4. **Degradation tells from the standing list (2026-08-15): none noticed.** Two drafting slips caught before showing:
   the folder count (first written 45, with `buildscripts` missing from the list; recounted as 47 and 34) and
   `.gitignore`'s length (first written 137 lines; the Read tool shows 136). **Handed over on capacity**, at a verified
   stop, after landing, as said to the user before the landing question.
5. **On the model, as the user asked to be told (2026-11-12).** `claude-opus-5-5`. Nothing this sitting met shows
   whether a different model would have done better or worse.

## 3. The plan — carried forward

1. **Next: part 3, second sitting:** item (b) (entry 1024 §2 item 2 (b)), by recursive listings of the 34 folders the
   check file's line 2753 names, each file's modification time compared with the local ref file's (2026-11-08
   12:33:25); **size it out loud before starting** (start with the small folders and `records`' other subfolders; list
   a large folder in parts, by its subfolders, if one listing hits the cap) and stop at a folder boundary if it does not
   fit. Each file changed since then is judged for whether it belongs in Task 0 (the file tools cannot tell untracked
   from tracked). **Findings only, no dispatch edit.** Anything that needs the user goes to him as a self-contained
   surface in the form of `CLAUDE.md` lines 1850–1924, the question in a later turn (check the record first, D-599). Add
   the results as a new section after the part 3 first section's provenance line (line 2757) and before slice 1's
   provenance line (lines 2759–2760, the file's last); show the addition before landing, exactly as it will land; land
   and prove it.
2. **Then part 3's E5 question:** the three tools `STATUS.md` names, read at their `--check` paths
   (`gen_status_batch_bound.py`, 352,058 bytes, by search only), and whether any other guard tool reads `STATUS.md`
   (entry 1061 §2 item 3).
3. **Then parts 4 and 5 and step 6**, as entry 1060 §3 step 2 gives them; finding 48 is for step 6.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1061 §3, and: (a) in the
check file [checked at the staged copy of 314,255 bytes]: lines up to 2732 unmoved (entry 1060 §3 note (a)); the part 3
first section at 2734–2757, finding 48 at 2751, item 2's folder list at 2753; slice 1's provenance line at 2759. (b) The
repository's top-level listing returns about 350 entries and `ratification_surfaces/`' about 190; list each only when a
proof or the item needs it. (c) Entry 1063 is `cowork_handoff_entry_one_thousand_and_sixty_three.md`.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** The dispatch is NOT YET RELEASED; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** (on the model of his choice) **and gives it exactly this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_and_sixty_two.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 584 §4 step 3 says. Before booting it checks by staging, in a call of its own,
   whether an entry 1063 exists (if it does, report and ask). It reads **this entry whole**, **entry 1061 §2 and §3**,
   **entry 1053 §3** (for the findings' line list), **entry 767 whole** (10,922 bytes), the working file at **its
   opening part (lines 1–64)**, and **the check file at lines 1–25, at each finding** by the line lists in entry 1053
   §3 note (a), entry 1059 §3 note (a), entry 1060 §3 note (a) and §3 note (a) above, **at lines 320–325, and from line
   2541 to the file's end**. It does **not** read the check file's slice tables otherwise, the frozen copy or the
   findings section whole, and does **not** list the handoff folder. It proves this entry's size as the device reports
   it when staged, the working file at 573,300, the dispatch at 874,206 and the check file at 314,255, and reads both
   ref files (anything but `e855ff2a…` means something ran: find out what first). The check file is at
   `C:\s\MS\ratification_surfaces\`, not under `records\cowork\`. It reports the boot with a capacity judgment, asks the
   session-start read, then does §3 step 1. **If the user orders the whole check file read instead, it reads it whole**
   (in parts with the Read tool).
4. **Only the session that releases the dispatch tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- **The container shell, under the leave:** read-only commands over staged copies only (`cd`, `grep`, `sed -n`, `cut`
  in pipes; `python3 -I` printing findings 1 to 47, the dispatch's hits for *"PARKED"*, *"D-250"*, *"dispatch note"*,
  *"revalidat"*, *"release statement"* and *"immediately before"*, the dispatch's last lines, and the comparison of the
  edited check file with the draft; `date` converting modification times). One `grep -o` with a long context pattern
  was refused by the shell's own limit and redone with `python3 -I`. **No redirect.** No shell wrote or deleted
  anything, in the container or on the device. **No shell used to prove the landing.** The draft written and corrected
  with the Write and Edit tools in the container's working directory; the check file's section made with the Edit tool
  on the staged copy; this entry with the Write tool.
- Before the device-info call, one tool-loading lookup only (the device-info tool and the commit tool together). No
  folder was connected; `C:\s\MS` was requested and granted.
- **Entries 1060, 767 and 584 read whole**, entry 1060 beyond its asked §3 and §5. **Entry 1059 §3** read for its note
  (a), which entry 1061 §4 step 3 names.
- **Read beyond entry 1061 §4 step 3's list:** the dispatch at lines 1–8 and 7083–7103, and searched; `.gitignore`
  whole; `STATUS.md`, the gating JSON and `DECISIONS.md` line 714 as the session-start read.
- **Folders listed:** `.git/refs` with its subfolders and `.git/` once each (the revalidation); the repository's top
  level once (item (b)'s sizing); `ratification_surfaces/` once (before the landing, to check the check file's
  modification time). The handoff folder not listed.
- **Finding the files:** entries 1060, 1059, 1053, 767 and 584 staged by their spelled-out names; the check file at the
  path entry 1061 gives; the working file and the dispatch by the names the check file's opening gives;
  `cowork_audit_protocol.md` at the repository root; each found at the first try.
- **Landing route:** the check file edited in its staged copy with the Edit tool, sent from its staged path, and
  committed by the identity the send returned, guarded by the staged modification time, in a call of its own; this
  entry written in the outputs folder and committed from there by its path, in a call of its own after its last edit.
- No memory tool, git, widget, task list, subagent or web access. Nothing published as an artifact.

*Provenance: Cowork, 2026-11-17 (Stockholm), the sitting booted on entry 1061. The user's words: the opening
instruction; "shortened" (the session-start read); "yes" (landing the part 3 first section; this entry written after
it, on the handover said before that question).*
