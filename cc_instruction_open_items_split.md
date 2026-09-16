# CC instruction — the OPEN_ITEMS register split (index + per-item detail files; user-ruled option 1, 2026-07-26)

> **Read first (every session):** `C:\s\MS\CLAUDE.md` (you will amend its register section in
> this very commit — read it as the outgoing state), `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (the file being split — note
> its own header rules; you are changing the register's SHAPE, never any item's substance).
>
> **Current state:** branch `master`; expected HEAD `cb246a7580` (the P3a STATUS commit,
> pushed) — verify via `git show --stat cb246a7580` and that HEAD matches; mismatch = STOP.
> Riding Cowork edits (verify only non-yours diffs): `cowork_handoff.md` and
> `cc_instruction_notation_seams_2.md` is untracked (ignore-policy) so only the handoff rides.
> This dispatch file stays untracked.
>
> **Hard stops, always:** origin only; NO code, corpus, golden, or `tools/robust_stop/` touch
> of any kind — this is a DOCUMENTATION-STRUCTURE dispatch only; ANY loss or alteration of an
> item's substance is a STOP (#12 — the reconciliation check below is the gate); a surprise is
> a STOP (#13). VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-26, at the user's option-1 ruling (recorded in the
handoff's "QUEUED/RESCHEDULED" block). **Purpose:** `OPEN_ITEMS.md` (too large to render)
becomes the complete lean INDEX; every item's full narrative moves VERBATIM to its own detail
file. **Nothing is reworded, summarized-away, or dropped — this is a pure structural move with
byte-level reconciliation (the ratified 2026-07-18 doc-split discipline).**

**Touchable set:** `OPEN_ITEMS.md`, NEW `open_items/` directory (one `OI-<n>.md` per item),
`CLAUDE.md` (the "open-items register" section only), `cowork_handoff.md` (riding + your
pointer updates), `STATUS.md` (closing entry), NEW `tools/open_items_split_check.py` (the
reconciliation instrument) + its generated report. Nothing else.

---

## Task 1 — the split (ONE commit, everything together)

1. **The index (`OPEN_ITEMS.md` keeps its name and its header rules, amended):** for EVERY
   item row, one index row: **ID | name (a faithful short title drawn from the item's own
   text — no self-invented labels) | a 1–2 sentence description | owning layer/gate (as the
   item states it) | STATUS (verbatim the current status cell's verdict + date, condensed to
   its operative state: OPEN/RESOLVED/EXECUTED/SUPERSEDED/… + the one-line qualifier) | link
   `open_items/OI-<n>.md`**. The A–I section structure and section headings are preserved; the
   two governing header blocks (the register rules; the 2026-07-17 architecture-decision
   block) stay in the index file.
2. **The detail files (`open_items/OI-<n>.md`):** the item's FULL original row content moved
   VERBATIM (the complete item text + source + status cells as they stand today, unmodified),
   preceded by a three-line header: the ID + name; `> STATUS IS AUTHORITATIVE IN THE INDEX
   (OPEN_ITEMS.md) — this file carries narrative and provenance only and is NEVER the status
   of record`; the section (A–I) it belongs to. **Detail files never gain a status line of
   their own** — the two-place drift killer.
3. **The register rules amended (`CLAUDE.md`, the "open-items register" section, same
   commit):** the ONE-home rule now reads: the INDEX is the one home and the authoritative
   status surface; details live in `open_items/OI-<n>.md`; rule (c) becomes "every newly
   discovered issue gets an index row AND its detail file in the same commit that records the
   discovery"; rule (d) "every resolution flips the INDEX row (the detail file gains a dated
   resolution note, never a status of its own)"; session-start rule (a) unchanged (read the
   INDEX at session start; open detail files as needed). Mark the amendment dated +
   user-ratified 2026-07-26.
4. **The reconciliation instrument (#17f / the doc-split discipline):** NEW
   `tools/open_items_split_check.py` — proves, mechanically: (a) every item ID present in the
   pre-split file exists in the index AND has a detail file; (b) every detail file's moved
   content is BYTE-IDENTICAL to the corresponding pre-split row's content (modulo the declared
   three-line header and the mechanical row-to-prose unwrapping you declare in the script —
   if you unwrap the markdown table row into prose paragraphs, the transformation must be
   declared, deterministic, and content-preserving; simplest and preferred: keep the row text
   verbatim as-is, table pipes included); (c) no item lost, none added. It reads the pre-split
   file from git (`git show cb246a7580:OPEN_ITEMS.md`) and the post-split tree, and writes
   `open_items/split_reconciliation.json` (counts + per-item verdict). **The check passing is
   the commit precondition; any mismatch is a STOP.**
5. **Pointers:** `cowork_handoff.md` — a short dated note that the register is now
   index+detail (riding edits included); `STATUS.md` closing entry.
6. Commit everything as ONE commit (the index, the detail files, CLAUDE.md, the instrument +
   its report, the riding/pointer files), message: `register split: OPEN_ITEMS.md -> lean
   index + open_items/ per-item detail files (user-ratified option 1, 2026-07-26; byte-
   reconciled, status authoritative in the index)`. Push origin.

## Report

The hash; the item count (pre == post, from the reconciliation report); the index file's new
size (the render problem should be gone — state the byte count); any row whose condensed
status required judgment (list them — the condensation is the one non-mechanical step, keep it
minimal and quote the operative words); the reconciliation verdict; anomalies. Standing
self-check before reporting: re-read the diff — especially that no item's substance moved
through your hands reworded.
