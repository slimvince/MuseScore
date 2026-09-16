# CC instruction — Phase 1d: the enumeration wave over the never-read surfaces (the user's option (a): knowledge completion before any phase-2 audit)

> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL (the three-phase rule D-231 — this
> dispatch completes phase 1's knowledge base; the decisions-register section; the writing
> conventions). `C:\s\MS\DECISIONS.md` (the INDEX — 254 user-ratified entries; full entries under
> `decisions/group_*.md`). `C:\s\MS\STATUS.md`. `C:\s\MS\OPEN_ITEMS.md` (INDEX) with detail files
> **OI-207** (this is its remaining scope), **OI-265**, **OI-266**, **OI-208** (the register
> rules). `C:\s\MS\cowork_design_doc_template.md` (the writing standards bind every specification
> sentence). The disposition machinery under `tools/audit/decisions/` (the surface partition in
> `disposition_manifest.json` `unresolved_partition_by_surface` is your reading map).
>
> **Current state:** the local branch is ONE commit ahead of origin (`91802e4d37`, the
> residual-queue ratification — Cowork commits cannot push). **Your FIRST act: `git push origin
> master`; then verify HEAD `91802e4d37`; mismatch = STOP.** Your last act is pushing your own
> commits.
>
> **Hard stops:** origin only; **no `src/` change of any kind**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; no fix, no design, no inference change. Specification edits
> (`ARCHITECTURE.md`, `CLAUDE.md`, `cowork_audit_protocol.md`) are permitted ONLY as (i) homing
> acts for decisions this wave finds or OI-266 names, following the phase-1 pattern (the rule in
> the specification's own voice, with its defense, citing the ratifying event), and (ii) the one
> named truth-sync correction OI-265 carries. **Where writing an entry would force you to RESOLVE
> something the record leaves open, you STOP on that entry and record it as a remainder.** A NEW
> decision is NEVER self-ratified: it enters the register with status from the record and goes
> into the report's RATIFICATION QUEUE for the user. A surprise is a STOP (#13). VS Code bash
> rules. A feasibility stop with a measured partition is an accepted outcome.

**Dispatch author:** Cowork, 2026-08-02, at the user's option-(a) ruling.

## Why this dispatch exists

The residual pass measured that **1,533 of the 2,935 remaining unresolved statements live in
surfaces never systematically read for decisions** — the `cowork_*` design documents (870),
`docs/` (407), and the two archives (256). The harvest's vocabulary net touched them but is
proven blind to plainly-worded decisions. Under D-231, phase 2's audits measure code against the
specifications; a decision still hiding in these surfaces would make those audits silently
under-report non-conformance — the Stage-3.1b mechanism built into the method. The user chose
completion first, sequentially. The archives carry the one proven kill (the 3.1b shelving), so
they are read with particular care; note the OI-84 A1 rule does NOT apply here — this is not an
audit of retiring code but a read of the RECORD, whose age does not retire it.

## Task 0 — push, then the two riding acts

1. `git push origin master` (lands `91802e4d37`); verify HEAD.
2. **OI-265:** correct `ARCHITECTURE.md`'s Layer-4 body claim that production chord analysis runs
   the legacy path (the ninth OI-232-class statement; give Layer 4 the same scoping sentence
   Layer 3's correction carries). Flip the row with provenance.
3. **OI-266:** home the six handoff-recorded working-protocol rules (D-249…D-254) into their
   proper homes — the session-method ones into `CLAUDE.md`'s Conventions, the audit/dispatch-
   protocol ones into `cowork_audit_protocol.md` — per the row's analysis; register homes updated,
   former homes into provenance (#12); flip the row.

## Task 1 — the wave: read the unread population IN FULL

Derive the reading list MECHANICALLY: every document that owns at least one of the 1,533
unresolved statements in the `cowork_*`, `docs/`, and archive surfaces (the cluster records carry
the file names; state the list and per-file counts in the report). Read each document IN FULL —
not the statements in isolation; the specification-first lesson is that decisions live in prose
the net cannot see, and context decides what is a ruling versus narrative. For each decision
found: verbatim by line range (never retyped), status/date/ratifier from the record only ("not
stated" permitted, inference forbidden), register entry, home judgment (owning specification →
a homing act now, or a documentation-gap row if the entry would resolve something open),
ratification-queue listing. Special attention in the archives: shelvings, falsifications, dead
ends, and excluded alternatives — the classes with binding force that history has hidden before.
Where an archive decision is ALREADY superseded by a registered ruling, record it as
superseded-by (naming the successor) rather than skipping it — the chain is the value (#12).

## Task 2 — the remaining 1,402 unresolved, settled

The other unresolved statements live in surfaces that were read (or are working prose): cc
reports 316, `tools/` 296, dispatches 294, `src` production comments 277, archives-adjacent rest.
Work them to FINAL dispositions — new numbered bulk rules are permitted where defensible (each
stated with its count and its exclusion vocabulary, the BR-11…BR-13 discipline), per-cluster
judgment where not. `unresolved` remains permitted and honest; the target is that what remains
is a judged residue with a stated reason, not an unread one. The completeness arithmetic over
2,935 is mechanical and in the report; the manifest regenerates, never hand-edited.

## Task 3 — guards, rows, close

The full guard set at the final tree: `gen_decisions_register.py --check` (all files),
`gen_cluster_dispositions.py --verify` (quotes, anchors, references — your specification
insertions SHIFT ANCHORS; use the drift report and the established remap discipline; the
backbone round-trips byte-identical at `json.dumps(indent=2, ensure_ascii=False)`, no trailing
newline), `--check` (dispositions), `tools/open_items_split_check.py`. Rows for every
documentation gap and every conflict found (both sides quoted, no fixes). Dated notes on OI-207
(this completes its scope — propose closure to the user in the report if the arithmetic
supports it) and OI-208. `STATUS.md` pointer entry at the TOP. If the wave finds decisions about
MEASUREMENT TOOLS, register them normally but list them in a distinct report section — the next
dispatch (the sealed measurement-tools partition) must account for them without reading your
findings as its own. Commits per change-class; push origin.

## Report

The reading list with per-file statement counts and a READ-IN-FULL confirmation per file. The
new-decision count and the RATIFICATION QUEUE (verbatim, proposed status, home). The final
disposition table over 2,935 with every new bulk rule + count and the remaining unresolved
count with its character. Homes moved (OI-266's six + any new). OI-265's correction. Guard
results. The measurement-tools flag section (possibly empty — say so). Anomalies each diagnosed;
a surprise is a STOP. Feasibility stop = a measured partition proposal, a successful outcome.
Standing self-check before reporting.
