# Cowork handoff entry 474 — 2026-11-02 — FREEZE OR REGENERATE IS SETTLED FROM THE RECORD: L3's DERIVING SESSION HAS RUN, SO ITS PACK IS SPENT AND IS FROZEN FIRST; THE NEXT COWORK SESSION WRITES THE FOURTH DISPATCH

**The current entry point.** Entry 473 is superseded as entry point and stands otherwise; its §1 carries unchanged except
where this entry names a change. **[checked]** means read at the object by this sitting; **[relayed]** means not.

## 1. State

- **At boot [checked]:** entry 473 at 7,177 bytes at the handoff folder's listing, no entry 474 before this one.
  `CLAUDE.md` 170,942, `DECISIONS.md` 119,961, `STATUS.md` 12,187 at their staging results — equal to entry 473's
  figures. Booted as entry 291 §4 step 3 states: `CLAUDE.md` at its six spans located by a heading search;
  `DECISIONS.md` whole; `STATUS.md` whole; the gating answer 247 open / 222 gating / 25 not, `gating_ids` read whole;
  entry 118's bridge-fault section; entry 152's (v) to (x); entry 169 whole; entries 473, 472 and 291 whole.
- **The git ref files were not read by this sitting.** Entry 472 records both at
  `1126176e2a4b48fc01bbb5b545210715366cb24a` [relayed]. Nothing is running; no dispatch is out; nothing is awaited.
- **THE QUESTION ENTRY 473 LEFT UNSETTLED IS SETTLED FROM THE RECORD (D-599): THE L3 PACK IS FROZEN BEFORE RULING 1's
  EDIT, NOT REGENERATED AT IT. NO QUESTION WENT TO THE USER.** The ground, at three objects:
  - **The rule [checked]:** `tools/audit/gen_derivation_boot_pack.py`, its docstring (the paragraph opening *"AND, SINCE
    2026-08-31, A SPENT SUBJECT IS FROZEN RATHER THAN RE-RENDERED"*, located by search) and its `FROZEN` table's
    preamble quoting Ruling 17(a) of `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *"A subject whose deriving
    session HAS RUN is SPENT: its pack is no longer an input to be kept current, it is the RECORD OF WHAT THAT SESSION WAS
    GIVEN."* D-646 is cited there as the ruled shape (*"a generated record that must outlive its own writer is frozen at
    an established snapshot, and the freeze is enforced by a hash STOP"*; its index row read in `DECISIONS.md`; its home
    in `cowork_audit_protocol.md` NOT read).
  - **The fact [checked at the away-returns section; the report it points to not read]:**
    `records/cowork/handoff/cowork_away_returns.md`, section *"THE L3 BLIND DERIVATION COMMITTED: THE DERIVATION, THE
    RELEASED BRIEF AND ITS ENTRIES IN GIT"* (located by search): the batch of
    `records/cc/instructions/cc_instruction_l3_derivation_commit_2026_10_17.md` landed
    `cowork_blind_derivation_l3_2026_10_17.md` and the released `cowork_blind_session_brief_l3.md`. **L3's deriving
    session has run; L3 is a spent subject.**
  - **The gap [checked]:** the `FROZEN` table carries `harmony-boundary`, `scoring-model`, `l0-l1` and `l2`, and no `l3`;
    the L3 block (its comment heading *"L3, THE THIRD DERIVING SUBJECT"*, located by search) carries no freeze. A search
    of the tool for a record of L3's session having run found none. So the tool still treats L3 as live, which is what
    turned `--check` red at the third run (report §4 [checked]).
  - **Why regenerate is excluded, on the tool's own recorded ground for `l0-l1` and `l2` [checked]:** re-rendering would
    put a `CLAUDE.md` text dated 2026-11-01 into the record of what a session that ran by 2026-10-17 was given (#12).
- **No algorithm change decided; documentation and one measurement-tool table only.** The decided method for L3 is
  `FRAMEWORK.md` §5's L3 block with DP-I [relayed: entries 469 to 473]. **Entries 472, 473 and 474 are NOT in git**;
  the next dispatch's Task 0 lands them.
- **Told to the user this sitting (his rule of 2026-09-26):** this is the fifth sitting running in which the ruled boot
  left no room for the dispatch itself; the boot reads alone took most of this context.

## 2. What the next session does

1. **Write the fourth dispatch of Ruling 1** (moving the two former wordings of `CLAUDE.md`'s decision-surface block to
   `CLAUDE_ARCHIVE.md`), executing the third dispatch's Ruling 1 steps by citation at its pinned git object, with **one
   task put BEFORE the `CLAUDE.md` edit: freeze `l3` in `gen_derivation_boot_pack.py`'s `FROZEN` table** — finding, date
   and reason (the tool STOPS on a freeze record missing any of the three), digests = the git blob hashes of the L3 pack
   directory's files on disk, proved equal to their blobs at the dispatch's Task 0 commit; `--check` green after the
   freeze and still green after the `CLAUDE.md` edit. Do not re-open freeze-or-regenerate unless a read contradicts §1.
2. **Read at least, each located by search:** the third dispatch
   `records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md` whole (41,161 bytes at its
   staging result this sitting; NOT read by this sitting); the tool's freeze machinery — `write_all`, `check_all`'s
   frozen branch, `verify_frozen`, `frozen_from_disk`, and `build_subject`'s leak-list scan for a frozen subject; the
   `l2` freeze precedent — `records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md` and
   `cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md`, and the away-returns sections of the L3 pack build's
   second half (one stopped, one resumed), because the first `l2` freeze attempt STOPPED (*"THE L2 FREEZE MOVES L2's
   RECORD BEYOND THE FROZEN SHAPE"*) and the same may happen to `l3`; the report's §8 (read by this sitting).
3. **Settle at the objects, as premises of the dispatch:** whether the L3 pack files changed between L3's session boot and
   the Task 0 commit (if they did, the files the session was given are the ones to pin, from git objects, as `l2`'s
   finding states it did); and whether `l3` needs a `RENDERED_BEFORE_THE_SCOPING_RULINGS` entry (by the tool's own
   comment it does not: that list is for packs rendered before 2026-09-21 and 2026-09-27, and L3's was rendered
   by the resumed second half of L3's pack build, after its verdicts were ruled on 2026-10-15 [checked: the tool's
   `VERDICT_DATE` comment and the comment under `FROZEN`'s `l2` entry; the render date itself not read]).
4. Check the dispatch at its sources **in a turn of its own**, land and prove it, write entry 475, and **that session —
   the one that wrote and checked the dispatch — tells the user to hand it to Claude Code** with the longer opening
   line. Step 4's second dispatch (the measurement tool extended and re-run) follows after that batch returns, as
   entry 473 settled.
- **Not read by this sitting:** the third dispatch's text; the freeze machinery's functions; the `l2` freeze rulings and
  batch sections; the L3 derivation-commit report; D-646 at its home; `OPEN_ITEMS.md`; any git object; the report's
  §0–§2, §5–§7, §9–§12 and appendix.
- **Capacity:** boot, the step-2 reads named in §1, and this entry in one context; no summary of context fell. This
  sitting hands over because the remaining room would not hold the third dispatch's whole read, the freeze machinery,
  the dispatch and its separate check.

## 3. Who does what, in this order

1. **Nothing is given to Claude Code now.** No dispatch is written; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** and gives it exactly this:
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_four_hundred_and_seventy_four.md`. Make the device-info call first. Use no shell at any point, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 291 §4 step 3 states, reads this entry and entry 473 whole, proves this entry's size
   at the handoff folder's listing, reports the boot with a capacity judgment, then does §2.

**If the user overrules any of this or changes the order, the session follows him.**

**This session is now read-only** (the user's rule of 2026-10-14).

## 4. Departures, declared

No shell command and no git command, in the container or on the device. No memory tool, widget, task list, subagent or
web access. Device-info call first; `C:\s\MS` requested after it. Folders listed: the handoff folder only; never the
repository's top folder. Every repository file staged by its path and read with the file tools; `cowork_away_returns.md`
staged whole and read at the sections named, located by search; entries 467 and 469 staged and not read. One
mid-sitting message to the user (the boot report) went through the verbatim message channel. This entry was written to
the outputs folder with the file tools and landed by `device_commit_files`. **This entry's size is proved by the next
Cowork session at a listing.**

*Provenance: Cowork, 2026-11-02 (Stockholm), the sitting booted on entry 473. The user's words: the opening
instruction.*
