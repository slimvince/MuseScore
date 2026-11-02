# Cowork rulings — 2026-11-02 — the Cowork start-up chain (candidate (e) of the pruning iteration)

**What this record is.** The user's ruling on candidate (e) of the pruning iteration, given in the Cowork sitting that
booted on handoff entry 476. Documentation and working practice only. **No algorithm change is decided.** The currently
decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I [relayed from entries 469 to 476; `FRAMEWORK.md` not
read by this sitting].

## The question as it was put

Candidate (e) was first named in entry 461 §2 — *"the Cowork boot chain (entries 118, 152, 169, 291; about 40 KB per
sitting) — a handoff entry can carry the few paragraphs itself and point at the four; the writing side's own practice,
proposed and not done"* — and routed to the user by entries 461 to 464 and 476.

**The facts the surface stated, each read at its object by this sitting:**

- A new Cowork session is told, by entry 291 §4 step 3 and by every later entry that says it *"boots as entry 291 §4
  step 3 states"*, to read entry 118's bridge-fault section, entry 152's items (v) to (x), entry 169 whole and entry 291
  whole: 2,075 + 3,580 + 24,913 + 9,655 = 40,223 characters per sitting (the values of
  `tools/audit/per_session_reading.json` → `the_cowork_boot_chain`, unchanged by the 2026-11-02 batch).
- In each, the paragraphs that govern how a session works are a part: entry 118's first paragraph of "THE BRIDGE FAULT"
  (the rest is a running tally of landings); entry 152's (vi) (the other five items are that sitting's own housekeeping);
  entry 169's "Boot" block and "The cadence for your session" (the rest is the 2026-09-13 state of the second
  extractions and the Task B gate); entry 291's §3 and §4 (§1 and §2 are the 2026-10-05 state of the L2 sizing). The
  size of the working parts was not measured.
- The reading is this side's own instruction: the measurement tool's authored text reads *"the writing side's own boot
  instruction — entry 291 §4 step 3 and entry 169's Boot block; no user ruling names these reads"* (this side's wording;
  no search of the record for a contrary ruling was run).

**The alternatives put:** A — copy the working paragraphs into every new handoff entry and treat the four as history;
B — read only the working sections at their own places, entry 291 §4 step 3 amended to say so, former wording kept;
C — keep reading all four whole. This side recommended B: most of the saving, each rule keeping its one home (#6), no
copy that can drift.

## Ruling 1 — (e): B

**The user's word: "B".**

**What it means.** From the next Cowork session on, the start-up chain is read at these sections only, each located by
a heading search, and not as whole entries:

1. **Entry 118** — the section headed *"THE BRIDGE FAULT — READ THIS BEFORE YOU WRITE ANYTHING"*, its first paragraph
   (the one ending *"stage the landed copy back and READ it before re-committing."*).
2. **Entry 152** — item **(vi)** (the one opening *"THE BRIDGE FAULT FIRED IN BOTH SHAPES IN THIS SITTING."*).
3. **Entry 169** — the block headed *"Boot"* and the block headed *"The cadence for your session"*.
4. **Entry 291** — §3 (*"Carried, for the next writer"*) and §4 (*"What happens next — who does what, in this order"*).

The remainder of each entry is history, opened at need. Nothing is copied into later entries.

**What it does NOT do.** It does not touch the ordinary session-start read (`CLAUDE.md` at its six ruled spans,
`DECISIONS.md` whole, `STATUS.md`, the gating answer); whether a sitting narrows that read stays the user's word per
sitting, as entries 475 and 476 recorded. It moves no text, deletes nothing, and changes no tool.

## The amendment to entry 291 §4 step 3 — to be applied by the next Claude Code dispatch

This side runs no shell and cannot edit a repository file in place except by retyping it whole, which the standing
practice forbids. **So the next Claude Code dispatch applies this amendment with the file-editing tool, at its Task 0 or
a task of its own**, inserting the paragraph below directly after the last line of step 3 (the line ending *"It
proves this entry's, the record's and the surface's sizes at a listing."*), at step 3's indentation, the wording above
it untouched:

> ★ AMENDED 2026-11-02 by Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md` (the
> user's word: "B"). The start-up chain is now read at these sections, each located by a heading search, not as whole
> entries: entry 118, the first paragraph of "THE BRIDGE FAULT"; entry 152, item (vi); entry 169, its "Boot" block and
> "The cadence for your session"; this entry, §3 and §4. The wording of step 3 above is the former wording, kept (#12).

**Until it is applied, this record is the instruction's home**: the current handoff entry names it when it states how
the next session boots.

## Ruling 2 — (d), the dispatch form: A

**The question as it was put.** Whether a Claude Code dispatch keeps restating standing text (the first-read rule,
commit-and-push, report form, checks, stops) or points at where that text already lives. **The facts the surface
stated:** the measurement of the 2026-11-02 batch (`tools/audit/per_session_reading.json` → `the_arc_dispatches` →
`the_invariant_share`, read at the object by this sitting): over the thirty dispatches of the L3 comparison arc
(2026-10-18 to 2026-10-31), 1,579,730 of 4,883,215 characters (32.35 %) stand on lines identical to lines of the
dispatch before; per member 50–55 % early in the arc and 16–29 % late; reports 19.0 %. The measure is a line match and
does not say which repeated lines are standing clauses, so it is an upper bound on what pointing could save, not a
measured saving. And the 2026-11-02 batch, told to execute its close by citation of the fourth dispatch's Task 3, had
to read back through the fourth, third, second and first dispatches to execute it, and declared those reads as a
departure (its report §10, departure 1). That the dispatch-protocol section's marked clauses are their one home under
the user's Ruling 3 of 2026-08-19 is relayed from entry 464 §1; that ruling was not read by this sitting.

**The alternatives put:** A — a writing rule from the next dispatch on (below); B — a further measurement sorting the
repeated lines into standing clauses and task content, then a ruling; C — no change, every dispatch fully
self-contained. This side recommended A.

**The user's word: "A".**

**What it means.** From the next dispatch on, the writing side writes dispatches so that:

1. **A dispatch points to a standing clause by its section, instead of restating it, only where that clause lives in a
   file Claude Code already reads at every batch** — in practice the dispatch-protocol section of
   `cowork_audit_protocol.md`.
2. **A dispatch never sends Claude Code through a chain of earlier dispatches.** What it needs from an earlier dispatch,
   it states itself.
3. **The effect is measured on later dispatches by the same tool** (`tools/audit/gen_per_session_reading.py`'s
   invariant share), when the populations it measures include them.

**What it does NOT do.** It moves no text, edits no existing dispatch or protocol clause, and adds no tool. It does not
change the user's rule of 2026-09-03 (Claude Code's output is read in full and verified at the objects) or the
first-read rule of 2026-10-26.

*Provenance: Cowork, 2026-11-02 (Stockholm), the sitting booted on entry 476. The user's words: "narrow"; "continue";
"continue"; "B"; "continue"; "continue"; "A".*
