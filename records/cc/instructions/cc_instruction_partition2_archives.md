# CC instruction — Phase 1e: the second enumeration partition (the two archives + the remaining design-document clusters)

> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL (the three-phase rule D-231 — this
> completes phase 1's knowledge base; the decisions-register section; the conventions).
> `C:\s\MS\DECISIONS.md` (the INDEX — 285 user-ratified entries; full entries under
> `decisions/group_*.md`). `C:\s\MS\STATUS.md`. `C:\s\MS\OPEN_ITEMS.md` (INDEX) with detail files
> **OI-207** (this is its remaining scope), **OI-268**, **OI-269**, **OI-270** (ruled — note its
> flag duty below), **OI-259**. `C:\s\MS\cowork_design_doc_template.md` (the writing standards).
> The disposition machinery under `tools/audit/decisions/` (the surface partition in
> `disposition_manifest.json` is your reading map).
>
> **Current state:** the local branch is THREE commits ahead of origin (`d1eadc076c`,
> `1bd6022ee4`, `1743cb3e29` — the D-278/D-266/OI-270 rulings and the queue ratification; Cowork
> commits cannot push). **Your FIRST act: `git push origin master`; then verify HEAD
> `1743cb3e29`; mismatch = STOP.** Your last act is pushing your own commits.
>
> **Hard stops:** origin only; **no `src/` change**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; no fix, no design, no inference change; no `ARCHITECTURE.md`
> edits (a decision needing a specification home gets a documentation-gap ROW — the homing wave
> for this partition's findings is a separate act after the user's ratification). **A NEW
> decision is NEVER self-ratified** (status from the record; the RATIFICATION QUEUE is the
> user's). Where entering something would require resolving what the record leaves open: STOP on
> that item, record it as a remainder. A surprise is a STOP (#13). VS Code bash rules. **A
> feasibility stop with a measured partition is EXPECTED — the archives alone measure ≈421k
> tokens; if one session cannot finish, the archives take priority and the design documents are
> the declared remainder.**

**Dispatch author:** Cowork, 2026-08-02.

## Why the archives take priority

They are the one surface class with a proven kill (the Stage-3.1b shelving hid there and a later
build contradicted it), the phase-1d review of their clusters confirmed they carry the binding
class ("Gate M … DEFERRED — do not retry"; "key-as-distribution SHELVED"), and they are swept by
no bulk rule. Their decisions are disproportionately shelvings, falsifications, dead ends and
excluded alternatives — the classes with binding force that ONLY the archives record.

## Task 0 — push, then the riding acts

1. `git push origin master`; verify HEAD.
2. **OI-269 (ruled by the user, 2026-08-02 — the reconciliation adopted):** annotate the commit
   lesson at `docs/iteration_path1_summary.md:112-116` so it reads as a rule about COMMIT
   CONTENT, not commit timing — in the commit the user asks for, nothing pipeline-affecting is
   left behind; sessions do not commit on their own judgment (`CLAUDE.md`: commit only when
   explicitly asked). A dated annotation beneath the lesson, both texts preserved; flip the row
   with provenance; the register entry for the Conventions rule needs no change.

## Task 1 — the archives, read IN FULL

`cowork_handoff_archive.md` and `STATUS_ARCHIVE.md`, in full — partitioned into as many sessions
as the token measurement demands (state the split and what each session covered; a measured
partial with a declared remainder beats a thin skim of everything). For every decision found:
verbatim by line range, status/date/ratifier from the record only, register entry, home judgment
(documentation-gap rows, no specification edits), ratification-queue listing. Three standing
duties while reading:
- **the D-282…D-285 flag duty (OI-270's ruling):** anything that refines, confirms, dates, or
  contradicts the four ruled meta-findings is FLAGGED in a distinct report section — their
  superseded-by statuses were ruled on the record's dates, and the archives are where an original
  ratification event would sit if one exists;
- **supersession chains:** an archive decision already superseded by a registered ruling is
  entered superseded-by (successor named), never skipped — the chain is the value (#12);
- **the OI-268 evidence duty:** where an archive ruling shows how delegated contract documents
  were treated (as homes or as drafts), record it — the user rules OI-268 (does ruling 2 reach
  ratified contract documents `ARCHITECTURE.md` delegates to, or does the register need a fifth
  home case) with this evidence in the report.

## Task 2 — the remaining design-document clusters (as capacity allows)

The 1,084 unresolved clusters in `cowork_*` and `docs/` documents not yet read: same discipline
as phase 1d (documents read IN FULL, never statements in isolation). If capacity ends first,
the remainder is measured per file and declared — the same honest shape as before.

## Task 3 — dispositions, guards, close

Every cluster this partition reads reaches a final disposition; the manifest regenerates with
the completeness arithmetic; the surviving unresolved surfaces keep generated stated reasons.
All guards at the final tree (`gen_decisions_register.py --check`, `gen_cluster_dispositions.py
--verify` with the anchor-remap discipline, dispositions `--check`,
`tools/open_items_split_check.py`). Rows for gaps and conflicts (both sides quoted, no fixes).
Dated notes on OI-207 (if the arithmetic completes its scope, PROPOSE closure to the user in the
report) and OI-268. `STATUS.md` pointer at the TOP. Commits per change-class; push origin.

## Report

Per-archive and per-file read-in-full confirmations with cluster counts; the new-decision count
and RATIFICATION QUEUE; the D-282…D-285 flag section (possibly empty — say so); the OI-268
evidence section; the final disposition arithmetic; the measured remainder if any; guard
results; anomalies each diagnosed. Standing self-check before reporting.
