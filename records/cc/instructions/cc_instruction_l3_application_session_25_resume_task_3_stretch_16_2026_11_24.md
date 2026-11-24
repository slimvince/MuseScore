# CC dispatch — the L3 application, SESSION 25 RESUMED: the push of session 25's act 1, then session 25's instruction from its act 2 onward, and nothing else

> **STATUS: WRITTEN AND CHECKED 2026-11-24.** Written by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_four.md`, after the first Claude Code
> session to run session 25's instruction stopped at a failed push (§0). Checked as a turn of its own by a NEW Cowork
> session (the user's Ruling 1 (e) of 2026-11-24), the sitting booted on entry 1235: one finding, corrected by item 8 of
> §1; nothing else changed (§4, the check note). Executed by Claude Code when
> the user hands it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop
> at that step and report it. Do not continue to the next one.**

## 0. What this file is, and why it exists

**Session 25's instruction** is
`records/cc/instructions/cc_instruction_l3_application_session_25_task_3_stretch_16_2026_11_24.md` (51,447 bytes, 587
lines, git blob `b3f7e24b9a16b730f589c54bacc81fea1c535d66`). It applies the sixteenth stretch of Task 3 (§L.40) of the
L3 application. **It stays the authority for everything this file does not replace, and it is not edited.**

**What happened when it was first run.** A Claude Code session ran it on 2026-11-24. It passed §1's five checks and made
§5 act 1's commit, `0a64959261f45cbf218a893144edeb2fed32128c`: parent `75955ee9d3da2fbeba04742375e3c9364e374106`, adding
exactly three files (session 25's instruction at `b3f7e24b…`, and handoff entries 1233 and 1234), with act 1's subject.
Then `git push origin master` failed twice, both times *"remote: Internal Server Error … ! [remote rejected] master ->
master (Internal Server Error)"*. Session 25's §7 makes an unverifiable push a STOP, so the session stopped there. It did
not edit the reading file, wrote no report and wrote no `STATUS.md` entry.

**Checked at the objects by the writing side after that stop:** `.git/refs/heads/master` reads
`0a64959261f45cbf218a893144edeb2fed32128c` and `.git/refs/remotes/origin/master` still reads
`75955ee9d3da2fbeba04742375e3c9364e374106`. The commit object `0a64959…` and its tree were decompressed and their
SHA-1s recomputed, and its tree was compared with `75955ee9…`'s on every changed path: exactly the three files are added,
nothing is changed or deleted. Entries 1233 and 1234 as committed equal the files on disk.

**Why session 25's instruction cannot simply be run again.** Its §1 check 1 expects both references at `75955ee9…`, and
its §5 act 1 would make a commit that already exists. **Why the correction is a new file rather than an edit:** session
25's instruction is now tracked, so an edit to it would be a tracked modification, which its own §1 check 5 makes a STOP.

**This session therefore does three things:** it lands this file and the writing side's two new handoff entries in a
commit of their own and pushes, which also carries `0a64959…` to the central repository (§3 act 1); it then executes
session 25's instruction from its §5 act 2 onward, exactly as that instruction gives it; and it STOPS. Nothing in what
the stretch writes into the reading file changes, and no expected count, `--numstat` figure or blob of session 25's
instruction changes: the act-1 commit adds no line to the reading file. **Documentation only; no algorithm changes.**

## 1. What this file replaces in session 25's instruction — the complete list

Nothing outside this list is replaced. Where session 25's instruction and this file seem to differ on anything not
listed here, STOP and report; do not choose.

1. **§1 check 1 (the tip)** → §2 check 1 below.
2. **§1 check 3 (the instruction's own identity)** → §2 check 3 below.
3. **§1 check 5, its sentence on the untracked paths §5 act 1 lands** → §2 check 5 below. Its remainder (the tracked
   modification `tools/audit/claude_md_finer_archive.json` and the paths sessions 2 to 24 left unlanded) stands as
   written.
4. **§2 items 1 and 4 (the first read, and the handoff entries)** → §2a below. §2's other items stand as written.
5. **§4 item 3 (A1, which handoff entries are landed)** → handoff entries **1235 and 1236** are landed with this file,
   in §3 act 1. Entries 1233 and 1234 are already committed in `0a64959…`. Any other untracked handoff entry or ruling
   record stays as the big dispatch's A1 says.
6. **§5 act 1** → §3 act 1 below. Session 25's §5 acts 2 and 3 are executed as written.
7. **§6 item 2 (the commits)** → the report names **four** commits by their full hashes, each verified at the object with
   `git show --stat <hash>; echo "exit:$?"`: `0a64959…` (made by the first run), this session's act 1 commit, the
   stretch commit and the report commit; and `origin/master` at the last. **§6 item 1** adds the results of §2 checks 1
   and 3 below. **§6 item 7** adds, as a departure declared by this file: the first run's stop and its two push errors as
   §0 quotes them, and that act 1 here is this file's and not session 25's.
8. **§0's description of the tip** (session 25's §0: session 24 *"committed its report as
   `75955ee9d3da2fbeba04742375e3c9364e374106`, the current tip"*) → overtaken by the first run: the tip is now
   `0a64959261f45cbf218a893144edeb2fed32128c` (§0 above). It is a description and gives no order; no act or check
   changes because of it, and it is not a STOP.

## 2. First checks — before any other act (replace session 25's §1 checks 1, 3 and 5's sentence as §1 above says)

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`;
   `.git/refs/heads/master` must read `0a64959261f45cbf218a893144edeb2fed32128c`; and
   `.git/refs/remotes/origin/master` must read **either** `75955ee9d3da2fbeba04742375e3c9364e374106` (the push still
   owed) **or** `0a64959261f45cbf218a893144edeb2fed32128c`. Report which. Anything else: STOP and report what you found.
   Do not try to find out what moved it.
2. **Session 25's check 2 (the big dispatch unchanged)**, as written.
3. **The two instructions' identities.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_25_task_3_stretch_16_2026_11_24.md; echo "exit:$?"`
   must print `b3f7e24b9a16b730f589c54bacc81fea1c535d66`. Anything else: STOP and report. Then
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_25_resume_task_3_stretch_16_2026_11_24.md; echo "exit:$?"`:
   record the hash for the report. There is no expected value.
4. **Session 25's check 4 (the reading file)**, as written: every expected value there still holds, because the
   act-1 commit added no line to the reading file.
5. **Session 25's check 5 (the working tree)**, as written, except its sentence on what §5 act 1 lands: **the untracked
   paths expected beside the ones it lists are exactly the three this file's §3 act 1 lands** — this file, and handoff
   entries 1235 and 1236 (§3). Session 25's instruction and entries 1233 and 1234 are now TRACKED and must not appear as
   untracked or as modified: if any of the three does, STOP and report.

## 2a. What you read, in this order (replaces session 25's §2 items 1 and 4)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **Session 25's instruction, whole** — your second read, alone. Then follow its §2 items 2, 3 and 5 to 10 as written,
   in its order.
3. **In place of its §2 item 4:** `records/cowork/handoff/cowork_handoff.md` at its topmost block (lines 1 to 255), and
   handoff entries **1233, 1234, 1235 and 1236, whole**. Entries 1233 and 1234 are committed; entries 1235 and 1236 are
   untracked and §3 act 1 lands them.

## 3. The acts, in order

1. **Land this session's writing-side files, in a commit of their own, before any edit to the reading file.** Exactly
   these paths, all expected UNTRACKED: this file,
   `records/cc/instructions/cc_instruction_l3_application_session_25_resume_task_3_stretch_16_2026_11_24.md`;
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_five.md` (the writing sitting's
   entry); and `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_thirty_six.md` (the checking
   session's entry). Run session 25's §1 check 2 again immediately before staging. The commit's parent must be
   `0a64959261f45cbf218a893144edeb2fed32128c`. Subject exactly:
   `record: handoff entries 1235 and 1236 and the session 25 resume instruction of the L3 application landed; the act-1 commit 0a64959 goes out with them; Task 3 stretch 16 follows`
   Then PUSH (`git push origin master; echo "exit:$?"`). The push carries both `0a64959…` and this commit. Verify at
   `.git/refs/remotes/origin/master` that it equals this commit. **If the push fails or cannot be verified, STOP** (session
   25's §7, unchanged): report the push's own output whole, do not retry more than once, and do not try to repair
   anything.
2. **Session 25's §5 act 2**, as written.
3. **Session 25's §5 act 3**, as written (its report path, its subject and its last sentence unchanged).

After act 3, this session STOPS. It does not begin §L.41, Task 4 or any later Task.

## 4. Provenance

*Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1234, after the first run of session 25's instruction stopped
at act 1's push. Read at the objects for this file, over staged copies: the three git reference files (`.git/HEAD`
*"ref: refs/heads/master"*; `refs/heads/master` `0a64959…`; `refs/remotes/origin/master` `75955ee9…`, its modification
time earlier than the local ref's); the commit objects `0a64959…` and `75955ee9…` and the trees on every changed path
between them (`b155699e…` against `0947c166…`, then `4775cc4a…`/`96d0add9…`, `a2668a71…`/`f8c74c27…`,
`a4d7d5d7…`/`c1d4b491…`, `1e62d928…`/`fc9acd7d…` and `44c7a701…`/`874de880…`), each decompressed and its SHA-1
recomputed by a `python3 -I` script (on the user's leave): exactly three paths added, none changed or deleted; entries
1233 (`c907f117…`, 14,766 bytes) and 1234 (`7412b56e…`, 11,511 bytes) as committed equal to the files on disk; session
25's instruction on disk at `b3f7e24b…` (51,447 bytes, 587 lines), read whole. The first run's stop and its push errors
are relayed from that session's closing message, not checked here.*

*Check note: Cowork, 2026-11-24 (Stockholm), the sitting booted on entry 1235, checking this file as a turn of its own
(Ruling 1 (e)), over staged copies. Read at the objects: the three git reference files (`.git/HEAD` *"ref:
refs/heads/master"*; `refs/heads/master` `0a64959…`; `refs/remotes/origin/master` `75955ee9…`); this file as landed
unchecked (10,150 bytes, 122 lines, no carriage return, blob `016ac5cc…` recomputed) whole; session 25's instruction
whole (51,447 bytes, 587 lines, blob `b3f7e24b…` recomputed). By this sitting's own `python3 -I` script (on the user's
leave), each object decompressed and its SHA-1 recomputed: the commit `0a64959…` (one parent, `75955ee9…`; tree
`b155699e…`; subject equal, character for character, to session 25's §5 act 1 subject) and the commit `75955ee9…`
(tree `0947c166…`), and the trees on every changed path between them (`0947c166…`/`b155699e…`, `96d0add9…`/`4775cc4a…`,
`c1d4b491…`/`a4d7d5d7…`, `f8c74c27…`/`a2668a71…`, `874de880…`/`44c7a701…`, `fc9acd7d…`/`1e62d928…`): exactly three
paths added, none changed or deleted; the three blobs equal to the files on disk (session 25's instruction `b3f7e24b…`,
entry 1233 `c907f117…` at 14,766 bytes, entry 1234 `7412b56e…` at 11,511 bytes). §1's list compared with session 25's
instruction, place by place: every order the stop has made wrong is in it, and nothing in it changes what the stretch
writes. **One finding:** session 25's §0 calls `75955ee9…` *"the current tip"*, which the stop has made untrue and which
§1 did not list, while §1's opening makes any unlisted difference a STOP; corrected by adding item 8. Edits of this
check: the status banner, §1 item 8, this note. Former wordings not kept, the file being unreleased.*
