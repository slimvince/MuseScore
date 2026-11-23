# Cowork handoff entry 1190 — 2026-11-22 — SESSION 7 OF THE L3 APPLICATION VERIFIED AT THE OBJECTS (TASK 1 STRETCH 6, §L.49 TO §L.55, THE LAST, LANDED AND PUSHED, NO STOP); THE FULL TASK 1 CHECK MEASURED AT THE NEW SUCCESSOR AND THE TRACE-THROUGH-EACH-SESSION METHOD TESTED; SESSION 8'S INSTRUCTION NOT YET WRITTEN

**The current entry point.** Entry 1189 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 1. State

- **Boot [checked]:** the device-info call first (no folder connected at the first attempt; `C:\s\MS` was refused by the
  environment's automatic check, the user added it with the desktop app's "Add folder", and the boot started again from
  the device-info call). Entry 1190 checked by staging in a call of its own, *"does not exist"*, at boot and again before
  this entry was written. Entry 1189 staged and read whole (12,891 bytes); entry 1026 §3 read.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` whole (11,726 bytes, 1794136674043,
  unmoved; latest entry 2026-11-08); `DECISIONS.md` at the listing, 120,603 bytes, 1794081137207, unmoved, so the last
  full read stands; the gating answer (247 open, 222 gating, 25 non-gating, unchanged); `CLAUDE.md` attached whole by
  the user's app.
- **Git [checked]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and `refs/remotes/origin/master` both
  `ae8fa501c2d4517f6930ad406030f2119b5f161c`.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry, and nothing else. It is not in git. No ruling was taken, so no ruling
  record was written. No instruction was written.

## 2. What this sitting established

1. **Session 7's three commits [checked at the objects].** `c011244275e9df9916b90241fc277816da501a22` (parent
   `dd9625b9…`), `0241e328f773cafe7ebfeb83b634f26838a8c268`, `ae8fa501c2d4517f6930ad406030f2119b5f161c`; each object
   hashes to itself, each subject exactly the session 7 instruction's (its lines 246, 232, 252), each with a
   `Co-Authored-By:` line as a second paragraph (Claude Code's declared departure 5). Trees against parents, folder by
   folder: the first adds only the session 7 instruction (blob `9e228ab1…`) and entry 1189 (blob `0b9a2e6f…`); the
   second changes only the successor, `668eacc4…` → `b4397e720b52f0f8afb23dbc47e675303cdc212d`; the third adds only the
   report (blob `d85f5518…`). Nothing else modified or deleted. The landed blobs equal the disk copies, and the
   working-tree successor equals `b4397e72…`. Session 7's instruction and report read whole.
2. **The successor [checked].** Diff `668eacc4…` → `b4397e72…` (difflib): two passages only — the in-progress line and
   one blank line next to it removed (difflib pairs the blank before it, old line 18; Claude Code's `git diff` table
   pairs the one after it, old line 20; the two blank lines are identical, so the result is the same file); 6 lines
   inserted at new 2037–2042 (§L.50's statement, after §L.42's, before the section's `---`). Every other line
   byte-identical. By script: the heading, lead-in and quotation each equal the session 7 instruction's lines 160, 162
   and 167 exactly; the quotation occurs in the §L.50 record's lines 32–35 with whitespace normalized and the bold marks
   set aside, beginning and ending at the words named; the record at the working tree is blob
   `a6cad94c90adcd37ac36f70b5abb45147599339a`, the one Claude Code names. The record's lines 62–65 leave the output's
   name and exact form open, and the statement supplies neither. Headings 41 → 42, the new one only; L3-S1 to L3-S42 and
   OQ-L3-1 to OQ-L3-14 each once (at their line-opening bold); the ANSWERED marks under OQ-L3-2, 3, 4, 5, 6, 7, 8 and
   10, eight, and the banner's parenthesis names the same eight; 2,130 lines, 220,485 bytes, longest line 1,205, no
   carriage return. Claude Code's six departures are minor and accepted; its departure 3 (§L.54's four records not
   located by heading) is covered by entry 1189 §2 item 4, which located them by heading search before §L.49.
3. **The full Task 1 (e) diff, measured at the new successor [checked].** Derivation blob
   `c01793f98c51e0267fb0dc7487613ac477cc1fbb` against `b4397e72…` (difflib): 92 changed passages (50 replaced, 41
   inserted, 1 deleted), 279 derivation lines touched, 908 successor lines, 116,648 bytes of successor-side text. Run
   against `668eacc4…` the same script reproduces entry 1189's figures (92; 50/41/1; 279; 904).
4. **The trace-through-each-session method, tested [checked].** The successor-commit chain, walked back by parent from
   session 6's land commit `70ce8ea0…`, every commit and blob a loose object: session 2 `9987d3c91ad80a59743759dc24e6b87ed098c5c7`
   (blob `e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1`), session 3 `fbe355032fdca34c5f6246004c37ab30fc8581cd` (blob
   `32cf8fdb7e942168a4ce153b3ccbcd8be081deca`), session 4 `ea784008853a0e02e942f3128a0193c8ad3f597c` (blob
   `b77ee3306957e14a1862dd98d928c1b8005b7824`), session 5 `9c26668a8885cdc1f56123624beed4e0b2413f13` (blob
   `a76ffaec74802d82d827cbffeb80930ab3d86687`, equal to entry 1189's), session 6 `3c79accb…` (blob `668eacc4…`),
   session 7 `0241e328…` (blob `b4397e72…`). A read-only script diffed each version against the one before and carried
   each line's session of origin forward. Result: every successor line outside the derivation has exactly one session
   of origin (session 2: 214; 3: 252; 4: 355; 5: 40; 6: 61; 7: 6); the derivation lines removed fall to session 2 (280)
   and session 3 (19). Against the direct diff of item 3, the trace disagrees on 20 lines, every one a blank line (19)
   or a `---` (1): the direct diff pairs them with an identical derivation line, the chain counts them as written by a
   session. No line with words differs. **So the method works at the objects**; what it does not yet do is set each
   session's lines against that session's report table, which is session 8's attribution and is not tried here.
5. **Degradation tells (2026-08-15 list):** none met. **On the model (2026-11-12):** nothing met suggests the work
   exceeded it. The sitting hands over now because writing session 8's instruction needs the big dispatch's Task 1 (d),
   (e) and E1 read and the method designed and checked, which this sitting judged would not fit safely beside the
   verification with `CLAUDE.md` loaded whole; told to the user, his word "yes".

## 3. The plan — carried forward

1. **Now: nothing runs.** No instruction is out; nothing is given to Claude Code.
2. **Next Cowork session: write session 8's instruction** — the full Task 1 (e) diff of the successor (`b4397e72…`)
   against the derivation object `c01793f9…`, and E1, with every changed passage attributed. Read the big dispatch's Task
   1 (d) and (e) and E1 again first, and whether Task 1 (e) asks a commit for its check (the successor itself is already
   committed stretch by stretch). The method §2 item 4 tested is available: Claude Code can run the same trace by script
   over the seven blobs named there, then set each session's lines against that session's report table (sessions 2 to
   7), rather than reading the whole ledger; the 20 blank-line pairings are expected and the instruction should say so.
   Size the instruction's reads (the six report tables, Task 1 (e), E1) before writing; if it cannot be made to fit one
   Claude Code session, say so.
3. **Later:** Tasks 2 to 5, each instruction written only when next. The session running the guard set declares both
   reds of entry 1184 §2 item 2; the session running Task 5 adds the regeneration of `evidence_pin_membership.json`.
4. **Open with the user, not ruled:** as entry 1185 §3 step 4.

**Carried rules:** as entry 1026 §3. **Practical notes, no rules:** as entries 908 and 910 to 1189 §3, and: (a) the
read-only scripts this sitting used (`obj.py`: loose-object decompression with hash check and tree parsing; `cmp.py`:
tree comparison; `size.py`: blob diff counts; `walk.py`: one commit's tree, parent and subject; `trace.py`: the
session-of-origin trace) were in `/home/claude/scripts/` of this sitting's container only; a successor rewrites them.
(b) Staging the successor-commit chain took one call per commit; the commits' hashes are now in §2 item 4, so a
successor stages the seven blobs directly. (c) Entry 1191's file name would be
`cowork_handoff_entry_one_thousand_one_hundred_and_ninety_one.md`; check by staging.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** No instruction for session 8 exists yet.
2. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_one_hundred_and_ninety.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1191 exists (if it does, report and ask), reads this entry whole and
   entry 1026 §3, asks the session-start read, then does §3 step 2.
3. **Only the session that writes and checks session 8's instruction tells the user what to hand to Claude Code.**
4. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **The container shell, under the leave:** read-only `python3 -I` scripts on staged copies (object decompression and
  hashing, tree comparison, the blob diffs and counts, the quotation and line checks, the gating answer's counts, the
  trace), with `sed -n` and `head` once each to shorten a script's printed output, and `mkdir` and `cat >` to write the
  scripts into `/home/claude/scripts/`. Nothing written into any staged copy or the repository by a shell. No repository
  tool was run.
- **Staged beyond the boot list:** the three git reference files; loose objects under `.git/objects/` (session 7's
  three commits and their parent; four root trees, three `records`, three `records/cc`, two `records/cowork`, two each
  of `instructions`, `reports` and `handoff`; the commits `70ce8ea0…`, `93d2fad4…`, `9c26668a…`, `fc2e099a…`,
  `13d0e226…`, `ea784008…`, `49d32b25…`, `0b56da6a…`, `fbe35503…`, `85d4e678…`, `cda8d482…`, `9987d3c9…` and the root
  trees of sessions 2 to 5's successor commits; the successor blobs of sessions 2 to 7; the derivation blob
  `c01793f9…`); session 7's instruction and report; the working-tree successor; the §L.50 record; `STATUS.md`;
  `tools/audit/nongating_apparatus_rows.json`. Listed: the repository root once, and `.git/objects/ae`, `02` and `c0`.
- **This entry written in the outputs folder with the Write tool**, shown to the user before landing. No git, widget,
  task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1189. The user's words: the opening
instruction with Claude Code's closing message; "try again" (after the folder was added); "shortened"; "yes" (to
measuring, testing the method and handing over).*
