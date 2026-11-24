# Cowork handoff entry 1235 — 2026-11-24 — SESSION 25 STOPPED AT ACT 1'S PUSH; THE ACT-1 COMMIT CHECKED AT THE OBJECTS; A RESUME INSTRUCTION WRITTEN AND LANDED UNCHECKED; HANDED OVER FOR ITS CHECK

**The current entry point.** Entry 1234 is superseded as entry point and stands otherwise. **[checked]** means read at
the object by this sitting; **[relayed]** means not.

## 0. The user's rules carried

**A message to the user either asks him ONE question or hands over to another session — NEVER BOTH** (entry 1215 §0).
This sitting asked four questions, each in a message of its own (how to proceed after the stop; leave to run
`python3 -I`; the session-start read; whether to land the draft unchecked), and hands over in a later message. **The
user's two rulings of 2026-11-24** (entry 1221 §0, verbatim there) stand and are carried forward unchanged.

**The user's correction of 2026-11-24, carried:** *"Who is the one that should do all git:ing!?"* — Claude Code does
every git act, pushing included; Cowork writes the instruction and the user hands it to Claude Code (D-252; the user's
rule of 2026-09-27). This sitting had told the user to run `git push` himself; that was withdrawn (§2 item 4).

**The user's leave of 2026-11-24 to this sitting, "yes":** to run `python3 -I` in the container, on staged copies only,
the scripts kept in a scratch folder outside the staged tree, writing nothing to the device. That leave was this
sitting's; a later sitting asks again before it needs a script.

## 1. State

- **Boot [checked]:** the device-info call first (`C:\s\MS` connected). Entry 1234 staged and read whole (11,511 bytes);
  entry 1235 asked for by staging: *"does not exist"* (and again before this entry was written). Entries 1233 (14,766
  bytes) and 1221 (16,479) read whole; entry 1026 whole (the file 11,103; its §3 is what is carried).
- **Claude Code's closing message** came with the user's opening instruction: session 25's instruction run; §1's five
  checks passed; act 1's commit made; `git push origin master` failed twice with GitHub's *"Internal Server Error"*;
  stopped under §7; the reading file untouched, no report, no `STATUS.md` entry **[relayed]**.
- **Session-start read, shortened** on the user's word ("shortened"): `STATUS.md` whole (11,726 bytes, 1794136674043,
  unmoved; its latest entry the close of 2026-11-08); `DECISIONS.md` at the listing (120,603 bytes, 1794081137207,
  unmoved); the gating answer at `tools/audit/nongating_apparatus_rows.json` by search (`open_rows` 247 at lines 26 and
  185, `non_gating` 25 at line 49, `gating_ids` from line 186).
- **Git [checked, at the ref files]:** `.git/HEAD` *"ref: refs/heads/master"*; `refs/heads/master`
  **`0a64959261f45cbf218a893144edeb2fed32128c`**; `refs/remotes/origin/master` **still
  `75955ee9d3da2fbeba04742375e3c9364e374106`** (modification time 1795542587032, earlier than the local ref's
  1795544999884; re-staged later in the sitting, unmoved). **The act-1 commit is local only.**
- **The model:** `claude-opus-5-5` throughout.
- **Changed on disk by this sitting:**
  - **The resume instruction, WRITTEN, NOT CHECKED:**
    `records/cc/instructions/cc_instruction_l3_application_session_25_resume_task_3_stretch_16_2026_11_24.md`,
    **10,150 bytes, 122 lines**, no carriage return, blob `016ac5cce5689b2fc9dc9e6940f701aa73cb9022`. Landed on the
    user's word ("yes"), the path staged first and found free; **proved byte for byte**: staged back after the landing and
    compared with the draft by `cmp`, identical. Untracked.
  - This entry (untracked).
- **Untracked writing-side entries: 1235 only.** The resume instruction's §3 act 1 lands 1235 with it (Ruling 1 (f)); the
  checking session adds its own entry 1236, which that act 1 already names.

## 2. What this sitting established

1. **The act-1 commit checked at the objects [checked].** The commit object `0a64959…` decompressed and its SHA-1
   recomputed: tree `b155699e…`, one parent `75955ee9…`, subject *"record: handoff entries 1233 and 1234 and the session
   25 instruction of the L3 application landed; Task 3 stretch 16 follows"* — equal, character for character, to session
   25's §5 act 1 subject. Its tree compared with `75955ee9…`'s tree (`0947c166…`) on every changed path, every tree
   object staged and its SHA-1 recomputed: **exactly three paths ADDED, none changed or deleted** — session 25's
   instruction `b3f7e24b9a16b730f589c54bacc81fea1c535d66`, entry 1233 `c907f11756bddaa3ec6d3ab32d098acbd325cf68`, entry
   1234 `7412b56ec09c08eb69c20d2c34e545d82411131f`; the two entries' blobs equal to the files on disk (14,766 and 11,511
   bytes). Session 25's instruction on disk is still `b3f7e24b…` (51,447 bytes, 587 lines), read whole.
2. **Why a resume instruction and not an edit [checked at session 25's instruction]:** its §1 check 1 expects both refs at
   `75955ee9…`, and its §5 act 1 would make a commit that exists; and it is now TRACKED, so an edit to it is a tracked
   modification, which its own §1 check 5 makes a STOP. So the correction is a new file that replaces, by a complete
   list (its §1), session 25's §1 checks 1 and 3, check 5's sentence on what act 1 lands, §2 items 1 and 4, §4 item 3,
   §5 act 1 and §6 items 1, 2 and 7; everything else of session 25's instruction stands, and its acts 2 and 3 are
   executed as written. **No expected count, `--numstat` figure or blob of session 25's instruction changes**: the act-1
   commit added no line to the reading file. Documentation only; no algorithm change.
3. **What the resume instruction orders:** check the refs (local `0a64959…`; `origin` either `75955ee9…` or
   `0a64959…`); check session 25's instruction at `b3f7e24b…`; land the resume instruction and entries 1235 and 1236 in a
   commit whose parent is `0a64959…`, then push — the one push carries both commits — and verify `origin`; a failed or
   unverifiable push is a STOP, one retry at most, the push's output reported whole; then session 25's acts 2 and 3.
4. **Degradation tells: one.** This sitting told the user to run `git push origin master` himself, against the standing
   split that Claude Code does every git act (the user's rule of 2026-09-27; D-252). The user caught it; it was withdrawn
   and told to him as a tell before anything was written. **On the model (2026-11-12):** the slip came early in a short
   sitting, in the plan put to the user rather than in any check; nothing here separates a lapse of attention from the
   model, so no suspicion about Opus is raised.
5. **GitHub's public status page [relayed, read in the sitting]:** Git Operations operational, no incident today touching
   git. So the first run's *"Internal Server Error"* matches no reported outage; the resume instruction asks for the push's
   output whole if it fails again.

## 3. The plan — carried forward

1. **Now: a NEW Cowork session checks the resume instruction as a turn of its own** (Ruling 1 (e)): its §0 facts against
   the objects (the refs; the commit `0a64959…`, its parent, its three added paths and its subject against session 25's
   §5 act 1); its §1 list against session 25's instruction read whole — **every place in session 25's instruction that
   the stop has made wrong is in the list, and nothing in the list changes what the stretch writes**; its checks, reads
   and acts for consistency with session 25's §1, §2, §4, §5, §6 and §7; its paths and subject. Then it **adds its own
   entry 1236** (already named in the resume instruction's §2 check 5, §2a item 3 and §3 act 1 — so normally only the
   status banner changes), corrects anything it finds (former wording kept or not, as the file is unreleased), lands, and
   **only that session tells the user what to hand to Claude Code** — the long opening line naming the resume
   instruction.
2. **Then Claude Code executes the resume instruction:** lands it and entries 1235 and 1236, pushes (carrying
   `0a64959…`), applies §L.40 by session 25's act 2, writes the report by its act 3, stops.
3. **Then a NEW Cowork session verifies session 25's stretch and, under Rulings 1 and 2, writes the next stretch's
   instruction in the same sitting**, from §L.41, as entry 1234 §3 step 2 gives it; its chain of commits now runs
   `75955ee9…` → `0a64959…` → the resume act-1 commit → the stretch commit → the report commit.
4. **Later:** as entry 1194 §3 step 2. **Open with the user, not ruled:** as entry 1211 §3 step 2; and the duplicate of
   entry 1218 §2 item 5.

**Carried rules:** as entry 1026 §3, §0 above and entry 1221 §0. **Practical notes, no rules:** as entries 908 and 910
to 1234 §3, and: (a) loose git objects stage by their path under `.git/objects/`; a tree diff re-run after each staging
call reached the changed paths here in four runs; (b) entry 1236's file name would be
`cowork_handoff_entry_one_thousand_two_hundred_and_thirty_six.md`; check by staging.

## 4. Who does what, in this order

1. **THE USER opens a NEW Cowork session** (with `C:\s\MS` added before the first message) **and gives it exactly
   this:**
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_one_thousand_two_hundred_and_thirty_five.md`. Make the device-info call first. Read-only searches with the container shell on staged copies are allowed; nothing else in any shell, not even to read that file or to prove a landing: stage it and use the file tools.

   That session checks by staging whether an entry 1236 exists (if it does, report and ask), reads this entry whole,
   entry 1234 whole (the checking pattern), entry 1221 whole (the two rulings) and entry 1026 §3, asks the session-start
   read, reads the three git reference files (they should still read `0a64959…` and `75955ee9…`), then does §3 step 1.
2. **Nothing goes to Claude Code from this entry.** The instruction to hand the resume instruction to Claude Code comes
   only from the checking session (Ruling 1 (e); the user's rule of 2026-10-26). **The user runs no git command himself.**
3. **This session is now read-only** (the user's rule of 2026-10-14).

**If the user overrules any of this or changes the order, the session follows him.**

## 5. Departures, declared

- **Container shell:** read-only work over staged copies (`grep -n` on the staged gating JSON, `grep -c` on the draft,
  `cmp`), and, on the user's leave, `python3 -I` scripts in a scratch folder outside the staged tree (decompressing and
  hashing git objects, walking and comparing trees, hashing files as git blobs), two of them written with the Write tool
  and three short ones given by `-c`. Nothing written by any shell into a staged copy, the outputs folder or the device.
- **Staged beyond the boot list:** `STATUS.md`, the gating JSON, the three git reference files (twice); 14 loose git
  objects (the commits `0a64959…` and `75955ee9…` and the trees on the changed paths); session 25's instruction.
  **Listed:** the repository root. Paths asked for by staging and found free: entry 1235 (twice) and the resume
  instruction's path.
- **Read beyond the boot list:** session 25's instruction whole; `STATUS.md` whole; the gating JSON by search.
- **Web:** GitHub's public status page, read once (§2 item 5).
- **The resume instruction and this entry written in the outputs folder with the Write tool and landed with the commit
  tool**, each proved by staging back and `cmp`. No git on the device, widget, task list, subagent or memory write.

*Provenance: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1234. The user's words: the opening instruction
with Claude Code's closing message; "yes" (the way forward); "yes" (leave for `python3 -I`); "Hmmm. CC is not doing
anything."; "So I will not be able to tell you when git push master origin has gone thorugh!!!"; "Errr . Are you
confused? Who is the one that should do all git:ing!?"; "shortened"; "yes" (land the draft unchecked).*
