# Ruling record — 2026-11-22 — the L3 application dispatch is executed by several new Claude Code sessions in turn

*The Cowork sitting booted on `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_two.md`.
**[checked]** means read at the object by this sitting; **[relayed]** means not.*

## 0. What happened

The amended L3 application dispatch (`records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`) was handed
to a new Claude Code session, as entry 1182 §4 ordered. That session could not read the dispatch. Its first read of the
whole file was refused (*"File content (919.3KB) exceeds maximum allowed size (256KB)"*), and a read of lines 1–150 was
refused as about 47,000 tokens against a limit of 25,000. It read lines 1–40, did nothing else, and reported. The user
stopped it and will not reuse it [relayed, from the user's opening message and Claude Code's report].

## 1. The facts the ruling rests on

- **[checked]** Nothing was committed or pushed. `.git/HEAD` reads `ref: refs/heads/master`; `refs/heads/master` and
  `refs/remotes/origin/master` both read `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`, with the modification times entry
  1182 recorded (1794137605021, 1794137607610). `.git/index` and `COMMIT_EDITMSG` carry the commit's modification time
  (1794137605012), and there is no `index.lock`. The dispatch is unchanged: 941,330 bytes, modification time
  1795371843765, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142` (computed from the staged bytes, which contain no
  carriage return). That no working-tree file was edited rests on Claude Code's word [relayed].
- **[checked]** Where the dispatch's size is: lines 1–99 (the heading) 117,665 bytes, of which the former draft banner
  and the construction-state table (lines 38–58) are about 100 KB, two of their lines being 48,153 and 45,556
  characters, and lines 43–44 saying the table *"is not an instruction to Claude Code"*; the ledger §L (lines 395–5906,
  55 entries) 642,100 bytes; Tasks 0 to 5 about 137,000 bytes. Eleven lines are longer than 2,000 characters, line 98
  among them (4,352). Whether Claude Code's file reader cuts such lines was not established; this sitting's own reader
  returned line 98 whole.
- **[checked]** The dispatch's reading order (line 98) puts first the 55 ruling records §L names, each whole (their
  sizes in the rulings folder's listing sum to about 456,000 bytes), then the derivation whole (127,533 bytes),
  `DECISIONS.md` whole (120,603), `BUILD_AND_TEST.md` in full (27,454) and more, all before Task 0. Task 1 (d) and Task 3
  (e) each require one commit for the whole Task (lines 6543 and 6785). Task 1 applies each §L entry's *Successor —
  amendments* part in ledger order (line 6136).
- **[relayed, from Claude Code's context display, pasted by the user]** Claude Code runs `claude-opus-5-5` with a
  context window of 1.0 million tokens; 104.1k are in use at the start of a session, of which `C:\s\MS\CLAUDE.md`, loaded
  whole as a memory file, is 65.4k. Against `CLAUDE.md`'s 170,510 bytes that is about 2.6 bytes per token, the rate
  Claude Code itself gave.
- **[checked, as estimates from file sizes]** The reads every session owes before its own Task (`STATUS.md`,
  `DECISIONS.md`, `BUILD_AND_TEST.md`, the dispatch-protocol standing clauses of `cowork_audit_protocol.md`, the parts of
  the dispatch every session needs) come to roughly 150,000 tokens beyond the 104.1k, at that rate. One session doing
  all of Task 1 would need roughly 800,000 tokens or more in all.

## 2. What was put

The decision surface in the chat, in its own turn: four alternatives, each weighed towards the ultimate objective,
towards the guiding principles and for its meta level — A, hand over the dispatch unchanged with an opening instruction
to read it in pieces; B, amend it in place for a reader that works in pieces and run it in one session; C, split the run
into several new Claude Code sessions, each with a short instruction that cites the unchanged dispatch by line range and
names exactly which of its orders it replaces; D, rewrite it as new self-contained dispatches (weighed and set aside).
The recommendation C, in those three terms. The context size was marked UNSETTLED and asked of the user. Documentation
only; no algorithm change. The choice question alone in a later turn, plain text, no widget.

## 3. Ruling 1 — alternative C (the user's word: "C")

**The L3 application dispatch is executed by several NEW Claude Code sessions in turn, each given a short instruction of
its own.** Each instruction:
1. opens by checking that the git reference files show the commit the previous session pushed (session 1: the current
   commit), and that the dispatch's blob is the one it was written against, and stops otherwise;
2. names exactly what its session reads: the ordinary session-start read; the dispatch's shared sections and its own
   Task's lines, by line range; and, for a stretch of ledger entries, those entries and their ruling records, each
   record read whole just before its entry is applied; with lines longer than 2,000 characters read through the shell
   in pieces;
3. lists exactly which of the dispatch's orders it replaces, and nothing else. The dispatch itself is not edited and
   stays the authority for every other order.

**The cut:** Task 0 alone; Task 1 in stretches of ledger entries; Task 2; Task 3 in stretches; Task 4; Task 5. Each
stretch is sized, when its instruction is written, so that the session's whole reading stays well under half the
window. Each session commits and pushes its own work. Where a Task is cut into stretches, its "one commit for the whole
Task" (Task 1 (d), Task 3 (e)) becomes one commit per stretch, each stopping at an entry boundary (D-672's shape). A
Cowork sitting verifies each finished Task at the objects before the next Task's first instruction is handed over.

**Documentation only. Algorithm: no change.** The L3 method stands as decided: the blind derivation of 2026-10-17 as
amended by the 55 ruling records of 2026-11-02 to 2026-11-08 that the dispatch's ledger names. None of that is in the
new L3 specification yet; writing it is what the dispatch's Task 1 does.

## 4. Applied by this sitting

The instruction for session 1, `records/cc/instructions/cc_instruction_l3_application_session_1_task_0_2026_11_22.md`:
Task 0 alone, its guard-set run, a short report of its own committed separately, and a stop. It adds to Task 0's
lists this record, entry 1183 and itself. Shown whole to the user before landing.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1182. The user's words: the opening instruction
with Claude Code's report; "shortened"; "C"; the pasted context display.*
