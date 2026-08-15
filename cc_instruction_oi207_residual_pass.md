# CC instruction — Phase 1c: the OI-207 residual second pass (the 6,374 mechanically-unclassifiable clusters)

> **Run AFTER `cc_instruction_spec_completion.md` has landed** (this pass classifies against the
> COMPLETED specifications and the current register; running it earlier re-does work).
>
> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL (the three-phase rule D-231 — this
> is phase 1c); `C:\s\MS\DECISIONS.md` (the INDEX — the register you classify against; full
> entries under `decisions/group_*.md`); `C:\s\MS\STATUS.md`; `C:\s\MS\OPEN_ITEMS.md` (INDEX)
> with `open_items/OI-207.md` and `open_items/OI-208.md`; the disposition machinery
> (`tools/audit/decisions/gen_cluster_dispositions.py`, `disposition_manifest.json`,
> `cluster_dispositions.json`).
>
> **Current state:** the spec-completion dispatch is DELIVERED (its final commit `e406f5edac`);
> expected HEAD is the Cowork verification commit that follows it (rowing OI-258…OI-264) — verify
> the log shows `e406f5edac` as an ancestor and the working tree clean; a local-ahead-of-origin
> state means the verification commit awaits push: push first. ★ THE RESIDUAL IS **5,204**, NOT
> 6,374 — the spec-completion pass regenerated the disposition layer at the ratified 231-entry
> backbone (see OI-207's dated note of 2026-08-02); every count in this dispatch reads 5,204.
>
> **Hard stops:** origin only; no `src/` change; no golden/`tools/corpus/`/`tools/robust_stop/`
> movement; no `ARCHITECTURE.md` edits (the homing pass is done — a residual decision needing a
> spec home gets a ROW, not an edit); no fix, no design. **A NEW DECISION found here is NOT
> ratified by you:** it enters the register data with status from the record ("not stated"
> permitted) and is listed in the report's RATIFICATION QUEUE for the user. A surprise is a STOP
> (#13). VS Code bash rules. A feasibility stop with a measured partition is an accepted and
> expected outcome — 5,204 clusters is large.

**Dispatch author:** Cowork, 2026-08-02.

## The task

The 5,204 clusters dispositioned `unresolved` under bulk rule BR-8 (36 % of the total after the
231-entry regeneration — the record's measured legibility) are the one place decisions may still
be hiding. Work through them
against the completed register and specifications; every cluster moves from `unresolved` to a
final disposition:

- **restates** a register decision (name the D-number) — now checkable against 231+ entries where
  the first pass had 115;
- **not a decision** (narrative, instruction, heading residue) — with the numbered bulk rule you
  applied, if any new bulk rule is defensible (state each rule and its count);
- **a NEW decision** — the valuable class: extract it verbatim, find its status from the record
  only, add the register entry (data + regenerated files, guards passing), give it a home
  judgment (owning spec → a documentation-gap row for the NEXT homing wave, never an
  `ARCHITECTURE.md` edit here), and put it in the report's ratification queue;
- **unresolved** — still permitted, still honest; the remaining count is the finding.

**The completeness check is mechanical and in the report:** every one of the 5,204 carries a
final disposition; the disposition artifacts and manifest are regenerated, never hand-edited.

## Close

Dated notes on OI-207 (this was its last open scope — if the pass completes, propose the row's
closure to the user in the report rather than closing it yourself) and OI-208. New rows for any
documentation gaps. `STATUS.md` pointer entry at the top. Commits per change-class; push origin.

## Report

The disposition table over 5,204 with every bulk rule + count; the NEW-decision count and the
RATIFICATION QUEUE (each: verbatim, proposed status, proposed home); the remaining unresolved
count; guard results; anomalies each diagnosed. If you stop for feasibility: the measured
partition proposal, which task you completed, and the remainder.
