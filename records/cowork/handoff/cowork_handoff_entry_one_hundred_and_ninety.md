# Cowork handoff entry 190 — 2026-09-17

**The current entry point.** Entry 189 is superseded as entry point and stands otherwise; its §4 findings, §5
summary-only list and §6 open decisions carry forward unchanged except where this entry names a change.

## 0. State at close [checked at the objects this sitting]

- `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read `5d24edb565b2e0e9efc92e082c163112bd97087f`.
  No commit was made by this side.
- **One dispatch is OUT and RUNNING** (the user confirmed CC started it):
  `records/cc/instructions/cc_instruction_reference_map_check_2026_09_17.md`, 7,565 bytes, committed twice, staged
  back, proved at content (both late edits present, both replaced wordings absent, last line read) and at size.
  **Do not touch it, or the report it checks, until CC returns.**
- The second backup the 188th entry's §5 recommends is still undone.

## 1. What that dispatch is, and why

The user ruled two things this sitting (plain text, his words "Go with B" and "ok, go with recommendation"):

1. **The reference map report is not read whole into one session.** The writing side reads its prose and judgement
   sections word for word; its long listings are checked mechanically.
2. **The mechanical check is done by CC, not by this side**, because `CLAUDE.md` Conventions (D-253) bars the writing
   side from reading working-tree files through a shell or interpreter, and nothing in the record exempts a staged copy.

The dispatch has CC write `tools/audit/check_reference_map.py`, run it once into
`tools/audit/reference_map_check.json`, and report to
`records/cc/reports/cc_report_reference_map_check_2026_09_17.md`. Five checks: §2(b).5 hit lines at file and line,
plus a two-way difference against an independent walk; the quoted deciding lines of §2(b).1 and §2(b).2; Task 2(a)
counts recomputed as lines and as matches; Task 1 root lists and tracked marks; §2(c) coverage. Every difference is
labelled by whether the file changed after the report. CC must establish any new-tool enrolment rule or STOP. Nothing
is committed; the three new files go into the move dispatch.

## 2. Boot order for the next session

1. The ordinary session-start read, as the 186th entry's Boot block orders it, then the 118th's bridge-fault section,
   the 152nd's (v)–(x) and the 169th whole. Then entry 189 whole, then this entry.
2. **Read CC's check report in full** and its chat reply (ask the user to paste it; it is not on disk). Verify any
   mismatch a decision will rest on at the objects.
3. Then do the Grep checks owed below, then put entry 189 §6 decision 1 to the user as a full surface.

## 3. What this sitting read [checked]

**Through the file tools:** entry 169 whole; the 188th at lines 60–254; `DECISIONS.md` whole (861 lines); `STATUS.md`
whole; the gating answer's 222 identities; the dispatch the report answers, whole (141 lines); the 118th's
bridge-fault section; the 152nd's departures (i)–(x).
**Through the shell only (see §5), never re-read through the file tools:** entry 189 whole; the 188th's lines 1–60 and
its landing section; the 186th's Boot block; `CLAUDE.md`'s six ruled spans.

Of the report: lines 1–53; the prose around the Task 1 lists (lines 171–177, 277–291, 867–876, 1253–1262,
1440–1464); §2(b) intro and §2(b).1 whole (7319–7412); the head of §2(b).2 (7413–7442) and its tail (7725–7730);
§2(b).3 and §2(b).4 (7731–7761); §2(c).0 to §2(c).10 whole (9894–11000), except the open-items list, where a Grep over
the pinned report found all 331 lines carry the identical reason; §2(c).11's tail (11385–11399), with a Grep finding
one non-CODE line among the code-type files (the test score `reachback_anchor.musicxml`, UNDECIDED); Declared whole.

**Not read by hand:** §2(b).2's verdict lines 7443–7724, the Task 1 and Task 2(a) listings, §2(b).5. These are what the
dispatch checks. The §2(b).2 verdicts themselves are judgements the check does not reach; a later session that needs a
verdict reads its line.

## 4. Owed before decision 1 is put

- Grep-check at staged copies the deciding lines behind §2(b).1 A and B for the tools decision 1 is about, unless CC's
  check report already covers them without mismatch.
- CC's chat reply to the map batch (pasted by the user this sitting) says all 2123 hit lines are in the report and every
  one of 2259 files is covered in §2(c). **Relayed, not checked** — the running dispatch is what checks it.

## 5. Declared departures of this side

- **Shell reads, against D-253, before that rule was read.** Through `device_bash`: `ls`, `grep`, `find`, `git log`,
  `git status`, and `cat`/`sed` of entry 189, the 188th's head and Boot block, the 186th's Boot block, `CLAUDE.md`'s six
  spans and the report's heading list. One early command timed out on a repository-wide `grep`. **The repository root
  was listed**: the bridge returned its directory names, and `ls` listed root files by pattern. Declared to the user
  in the turn it was found. After that every repository read was Read or Grep over staged copies. Staged sizes matched
  what the shell had shown (`CLAUDE.md` 162,259; entry 189 7,536; map dispatch 7,036; report 803,751). **A matching
  size does not prove matching content: the shell-only reads in §3 are declared, not established.** The next
  session's boot re-reads all of them through the file tools, so nothing carried forward rests on them alone.
- **One container `wc`** on this side's own copy of the dispatch before landing. No claim rests on it.
- Before the folder was connected: an artifact listing, a device-info call, a names-only skeleton of `C:\s\MS` and
  of the user's Downloads folder. One folder-access request (`C:\s\MS`), granted. A task list was used. No WebSearch,
  WebFetch, subagent or popup.
- Memory: five project memory files read (the project index and preferences; dispatch-writing rules, no-shell
  editing, push rule); nothing written.

## 6. Watch line

**(0) THE CHECK DISPATCH IS RUNNING** — read its report whole on return. **(1)** Entry 189 §6's four decisions stand,
one per turn, full surfaces with recommendations. **(2)** Then the move, reference-fix, regenerate, commit and push
dispatch, which also carries the three new check files. **(3)** The second backup stays folded into that move.
