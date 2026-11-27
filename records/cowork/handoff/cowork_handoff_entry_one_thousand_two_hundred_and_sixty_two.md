# Cowork handoff entry 1262 — 2026-11-27 — THE MEASUREMENT OF THE PROCEDURE CHANGES RULED (B); THE CHECK OF THE TWO DROPPED READS MADE, ITS RESULT BELOW; STRETCH 27'S INSTRUCTION NOT BEGUN; HANDED OVER ON A CAPACITY JUDGMENT, NO DEGRADATION TELL MET

**The current entry point.** Entry 1261 is superseded as entry point and stands otherwise, except where §0 and §3
below change its plan. **[checked]** means read at the object by this sitting; **[relayed]** means not.

## 0. The user's rules in force, and his words to this sitting

**Carried unchanged:** entry 1261 §0, and through it entry 1260 §0 (the five rulings of 2026-11-27, ruling 1 as
corrected) and entry 1259 §0. All three read whole by this sitting.

**His words to this sitting:** the opening instruction (entry 1261's §4 step 2 line); *"yes"* (`python3 -I -B` in the
container on staged copies, scripts outside the staged tree, nothing written to the device by any shell); **"B"** (the
measurement, §2 item 1, on a surface delivered whole in an earlier turn); *"yes"* (make the check of §2 item 2 now,
then hand over with this entry).

**The ruling of this sitting — process and documentation only; no specification text and no algorithm changes; the
method the specification defines stays as decided.** **Measurement B:** from stretch 27 on, each sitting writes a
short fixed block of figures, taken from the files, into its handoff entry (§2 item 1 gives the fields); at Task 3's
end one summary compares them with the baseline of entry 1259 §2 items 1 and 2, its limit stated (#24). **Declined:**
A (count only at the end), C (B plus the user noting the usage display per sitting: no baseline exists for usage), D (a
script to compute the figures).

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1262 asked for by staging: *"does not
  exist"*. Read whole: entries 1261, 1260 and 1259, session 35's instruction (58,836 bytes), the README of
  `tools/audit/stretch_verify/`.
- **Ruling 2's values, at the listing [checked], all three equal to entry 1261 §1's, so none read in full:**
  - `STATUS.md`: 11,726 bytes, modification time 1794136674043;
  - `DECISIONS.md`: 120,603 bytes, modification time 1794081137207;
  - `tools/audit/nongating_apparatus_rows.json`: 178,066 bytes, modification time 1788814584416.
- **Also at the listing / staging:** `cowork_audit_protocol.md` 122,030 bytes, 1789979289703 (unchanged);
  `records/cowork/handoff/cowork_handoff.md` 1,140,412 bytes, 1789629842494 (unchanged since entry 1260 §1).
  `tools/audit/stretch_verify/rebuild.py` 3,683 bytes.
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master` and
  `refs/remotes/origin/master` both `2226b2476eb0a674ae87930ae2a02951a0d3ae31`, unmoved.
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:** this entry only (untracked).

## 2. What this sitting established

1. **The per-stretch measurement block (ruling B), its fields fixed here so every sitting records the same thing.**
   Written in the handoff entry of the sitting that VERIFIES the stretch (it holds every figure); the writing sitting
   records items (c) and (d) in its own entry when it lands the instruction. Every figure read at a file, the tool
   that produced it named beside it (the protocol's character-figure clause).
   - (a) the Cowork sittings that worked on the stretch (handoff entry numbers, each with its role: writes, compares,
     verifies) and the Claude Code sessions;
   - (b) the reading-file lines added and deleted against the commit before (Claude Code's `--numstat`, confirmed by
     the verifier's rebuild);
   - (c) the instruction's bytes and lines;
   - (d) **the total bytes Claude Code is told to read, under the new list (ruling 1) and, for the same stretch, under
     the old list** (session 35's §2 applied to this stretch's ranges): whole files at their size at the listing;
     line ranges summed in bytes over a staged copy; `CLAUDE.md` excluded from both (it is loaded either way). For
     the two dropped reads the old-list figures measured by this sitting (`python3 -I -B` over staged copies, line
     feed counted): `cowork_handoff.md` lines 1–255, **19,122 bytes**; `cowork_audit_protocol.md`'s 38 sections
     carrying the standing-clause marker, **102,143 bytes** (each section from its heading to the line before the
     next `###` heading, lines joined by line feeds; so the next section's marker line falls inside the figure, and
     the first section's own marker line, above line 237, does not). A later sitting re-measures if either file's size or modification time
     has changed;
   - (e) what each step caught: the record comparison (Ruling A), Claude Code's own checks, the verification — each
     catch named, and whether it changed a byte of the reading file;
   - (f) STOPs, by whom and why;
   - (g) any error that reached a commit (the quality side: dropping the separate check must not let errors through).
   **The limit, stated with the summary (#24):** two to four stretches of uneven size remain; the comparison is
   indicative, not a finding; per-line and per-row-part ratios reduce the size effect and do not remove it; item (d)
   is the one figure free of it, being the same stretch measured both ways.
2. **The check ruling 1 orders before stretch 27's instruction lands [checked at both files, read whole over the
   ranges named]: which rules of `cowork_handoff.md` lines 1–255 and of `cowork_audit_protocol.md` line 180 to the
   end the stretches rely on.** Evidence of reliance taken from session 35's report (staged, read at its §7 and §8):
   Claude Code cited the pin clause P-2 at its §7, and its §8 self-check follows the protocol's checklist items 1 to 4.
   **To carry into stretch 27's instruction (each as an order Claude Code meets without the protocol):**
   - (i) **The pin (protocol, P-2, line 1566 onward).** Pin the instruction with `git hash-object -w` at act 1; where
     the opening line has it read from the working tree first, declare that, and prove the pinned blob equals the hash
     of §1 check 3 before staging. *Session 35's §1 check 3 and act 1 already carry the hash and re-hash; the
     `-w` pin and the declared-departure sentence are the part to add.*
   - (ii) **The report's self-check checklist (protocol, *The writing side runs the standing self-check too*, line
     647 onward), all five items:** the guiding principles touched and conformance; the conventions (American English,
     no self-invented labels, music-theory words in their musical sense only, every non-musical use qualified); every
     figure and premise cited to its object (D-431); the file-tools rule (D-253); and **uncertainty on any comparison
     (#24)** — the fifth item, which session 35's §8 did not answer. Add the list to §6 item 8.
   - (iii) **Figures in the report (protocol, *A figure enters a dispatch or a report by CITATION* and *A published
     CHARACTER FIGURE names the tool that produced it*, lines 512 and 564 onward).** Every number in the report is
     read at the object in that session, with the command or tool named beside it; no figure is copied from the
     instruction as a result. *Session 35's §8 already says this of itself; carry it as an order.*
   - (iv) **The parked-instruction rule (protocol, line 249 onward).** An instruction not the active dispatch carries a
     PARKED banner and is not run without a dated dispatch note. Under Ruling A the instruction lands unchecked and the
     next sitting makes the record comparison before handing it over; **carry as: Claude Code runs the file only if
     its banner records the record comparison as made; otherwise STOP and report.**
   **Not to carry — the stretches do not rely on them** (this sitting's reading of each section, read whole; the facts
   cited inside each item are checked):
   - **The read-first-block clause** (protocol line 274: every dispatch's read-first block names the current handover
     block of `cowork_handoff.md`). This is the rule ruling 1 replaces for these stretches. Its ground (finding F58) is
     the shared finding-number series and a write ordered into a file not ordered read: session 35's report carries no
     finding number (searched for `F` plus two or three digits: none), and a stretch writes only the reading file
     (read where it is edited) and its own new report. **Stretch 27's §4 lists this clause as replaced, citing ruling
     1.**
   - **The handoff block, lines 1–255** (the eighty-eighth entry, 2026-09-01). Its standing content for Claude Code is
     already elsewhere: the guard routing `git status` to `tools/audit/changed_paths.py` (its trap 1) is in session
     35's §1 check 6; the reserved words (trap 4) are in `CLAUDE.md`'s Conventions, loaded in Claude Code's context;
     its session-start read (lines 6–9) is replaced by ruling 1 and ruling 2. The rest is that sitting's own state, or
     binds the writing side.
   - **Every other marked section** binds the writing side (how a dispatch, a ruling record or a decision surface is
     written; homing acts; mechanism changes; generated records) or a kind of act a stretch does not contain. They go
     on binding Cowork; Claude Code's execution of a stretch does not meet them.
   **One point for the writing sitting to settle in the instruction, not put to the user [reading]:** P-3 (protocol,
   line 1579 onward) says movement that no ordered act caused is *"reported and graded, never absorbed and never
   auto-stopped"*. Session 35's §1 check 6 STOPs on any unexpected tracked modification. For the reading file the STOP
   rests on an ordered act's own input (the fingerprint), so it is not movement the batch did not cause; for any
   other tracked path, P-3's form (report and grade) appears to be what the protocol orders. The writing sitting reads
   P-3 at its line and words §1 check 6 accordingly, stating its reading in the instruction's check note.
3. **Capacity, judged out loud to the user, his "yes":** no degradation tell met. Stretch 27's instruction (§L.52: the
   big dispatch's lines 5514–5637, its record whole, 46 row-parts at the reading file, the copy and change, the
   simulation) does not fit after this sitting's reading. The `rebuild.py` extension is left to the sitting that
   writes stretch 27, scoped to the kinds of line §L.52 brings, so that no capability is built that the stretch does
   not use. On the model (2026-11-12): nothing raises a suspicion about Opus.

## 3. The plan — carried forward

1. **Next: a NEW Cowork session writes stretch 27's instruction from §L.52**, as entry 1261 §3 step 2 gives it, with
   these changes: the check of the two dropped reads is DONE (§2 item 2 above) — it carries items (i) to (iv) into the
   instruction, lists the read-first-block clause as replaced, and settles the P-3 point, without re-reading the
   121 KB; it extends `rebuild.py` where §L.52 brings a kind of line outside its *Limits*, establishes the extension
   (stretch 26's objects are a known case for a §11 entry: blob `5809b5b9dd7b041d06c04ddda6be44c38184e9b2` from
   `bb81f43e…`), or uses a placement script of its own if capacity does not allow; it records measurement items (c)
   and (d) for stretch 27 in its entry. It lands the instruction unchecked on the user's word. **It does NOT tell the
   user to hand it to Claude Code.** If capacity does not allow, it hands over at a verified stop.
2. **Then (Ruling A):** the NEXT Cowork session makes the record comparison of the waiting instruction, sets its
   banner to record that the comparison is made, tells the user what to hand to Claude Code, waits, verifies the
   commit, writes the measurement block for stretch 27, and writes the next instruction.
3. **Carried:** entry 1260 §3 steps 5 to 8 (ruling 2; ruling 3 and its proposal, still not ruled; ruling 4's timing,
   still not ruled; after Task 5).

**Practical notes, no rules:** as entry 1261 §3, and: (a) entry 1263's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_sixty_three.md`; check by staging; (b) the protocol's marked sections
are found by the marker line *"★ STANDING CLAUSE — a dispatch's read-first block requires the clause below to be met."*
above each heading; the one unmarked section in the range is *"When a shell-read policy cannot decide, it DENIES"*
(line 896); P-2 to P-5 are paragraphs inside the last section, not marked sections; (c) session 34's report is not at
the name `…session_34_task_3_stretch_25_2026_11_26.md` (staging said it does not exist; not looked for further).

## 4. Who does what, in this order

1. **Nothing goes to Claude Code from this entry.** No instruction is waiting. The instruction to hand stretch 27's
   instruction to Claude Code comes only from the session that makes its record comparison (Ruling A).
2. **THE USER opens ONE NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_sixty_two.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   **No other Cowork session is open on this work at the same time.** That session checks by staging that entry 1263
   does not exist (if it does, report and ask); reads this entry whole, entries 1261 and 1260 whole, session 35's
   instruction whole and the README of `tools/audit/stretch_verify/`; makes the session-start read by ruling 2 against
   §1's values; reads the three git reference files (they should still read `2226b247…`); asks the user's leave for
   `python3 -I`; judges capacity out loud; then does §3 step 1.
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only reads and searches over staged copies (`sed -n`, `cut`, `grep`); on the user's leave,
  `python3 -I -B -c` to measure the two ranges' bytes and list the protocol's `###` sections with their sizes and
  markers. No script file written; nothing written by any shell to a staged copy, the outputs folder or the device.
- **Staged beyond the boot list:** `cowork_handoff.md`, `cowork_audit_protocol.md`, session 35's report; one staging
  of a guessed name for session 34's report, refused (§3 note (c)).
- This entry written in the outputs folder with the Write tool and landed with the commit tool, the landing proved by
  staging back and comparing. No git on the device, widget, task list, subagent, memory write or web access.

*Provenance: Cowork, 2026-11-27 (Stockholm), the sitting booted on entry 1261. The user's words as §0 gives them.*
