# CC instruction — Phase 1g: the triage of the 120 unread design documents → an INFORMED exclusion list for the user, plus full reads of the obvious live core

> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL (the three-phase rule D-231; the
> register section; NOTE the local-patches section now has THREE subsections — D-316 is new).
> `C:\s\MS\DECISIONS.md` (the INDEX — 316 user-ratified entries; details under
> `decisions/group_*.md`). `C:\s\MS\STATUS.md`. `C:\s\MS\OPEN_ITEMS.md` (INDEX) with detail files
> **OI-207**, **OI-268/OI-272** (their rulings are pending — do not pre-empt), **OI-271** (open
> on the narrowed upstream-licence question only — nothing here answers it), **OI-269** (its
> banner observation: 101 files carried NO status banner — the reason this triage exists).
> `C:\s\MS\cowork_design_doc_template.md` (the status-banner convention this triage classifies
> against). The manifest's per-file unresolved counts are the priority map.
>
> **Current state:** the local branch is TWO commits ahead of origin (`ee39d02574`,
> `90b4213801`). **FIRST act: `git push origin master`; verify HEAD `90b4213801`; mismatch =
> STOP.** Last act: push.
>
> **Hard stops:** unchanged — origin only; no `src/` change; no golden/`tools/corpus/`/
> `tools/robust_stop/` movement; no fix, no design, no inference change; no `ARCHITECTURE.md`
> edits; NO document's status banner is EDITED by this pass (classifying is not bannering —
> banner corrections are a later act on the user's acceptance); new decisions found during the
> Task-2 full reads are NEVER self-ratified (RATIFICATION QUEUE); a surprise is a STOP (#13);
> VS Code bash rules; a measured feasibility stop is accepted.

**Dispatch author:** Cowork, 2026-08-02, at the user's option (γ) ruling.

## Why a triage, and what it must not be

The user's D-231 end state is: the unread population at ZERO or an EXPLICIT, USER-ACCEPTED
exclusion list. An exclusion list built on unread contents is the blind sweep the guardrails
forbid — so this pass makes the list INFORMED: every proposed exclusion is defensible per file,
by ESTABLISHED supersession or established class, never by guess. The classification cost is
bounded (headers + targeted verification, not full reads); the payoff is that the remaining
full-read set shrinks to the documents that can still bind.

## Task 1 — classify all 120 unread documents

For each document in the unread set (derive the list mechanically from the manifest partition,
as phase 1f did): read its TITLE, STATUS BANNER (where one exists), and OPENING SECTION — enough
to classify, no more. Classify into exactly one of:

- **LIVE-SPEC** — a design/specification document with standing force (ratified banner, or no
  banner but its subject is a live surface). DEFAULT for any unclear case: a document is
  LIVE-SPEC unless established otherwise — doubt keeps it IN the reading set (#19's direction of
  caution).
- **SUPERSEDED-ESTABLISHED** — the document claims supersession AND the claim is VERIFIED: the
  named successor exists, is registered (cite the D-number or the successor document's ratified
  banner), and covers the document's subject. An unverifiable supersession claim → LIVE-SPEC.
- **REPORT/NARRATIVE** — a delivered-work report or session narrative with no specification
  force of its own (the BR-12 character, as a whole document). Its RULINGS, if any are visible
  in the header/structure, disqualify it from this class → LIVE-SPEC.
- **EVIDENCE-FROZEN** — a committed measurement/evidence document (the `docs/p3_*` class): its
  decisions are shelvings/falsifications ALREADY registered (verify: cite the D-number), the
  rest is data. If its decision content is NOT yet registered → LIVE-SPEC.

For every SUPERSEDED-ESTABLISHED and EVIDENCE-FROZEN classification, the verification citation
is MANDATORY in the table. Output: ONE table, all 120 rows — file · clusters · class ·
verification citation (or "—" for LIVE-SPEC/REPORT) · proposed disposition (READ IN FULL /
EXCLUDE with reason). This table IS the user's decision surface; write it to a committed
artifact (`tools/audit/decisions/phase1g_triage.md`) so the acceptance is of a document, not of
report prose.

## Task 2 — begin the full reads of the obvious live core (no triage needed)

These are LIVE-SPEC on their face and read IN FULL this session as capacity allows, highest
cluster count first: `cowork_layer4_chordsymbol_design.md` (43) · `docs/decoder_design.md` (36)
· `cowork_layer5_function_design.md` (36) · `docs/scoring_model.md` (35) · `docs/redesign_plan.md`
(27). Same discipline as every wave: decisions verbatim by line range, status from the record,
register entries, homes judged (rows, not spec edits), the RATIFICATION QUEUE, supersession
chains entered, the standing flag duties (D-282…D-285; OI-268/OI-272 evidence — the rulings are
pending, so evidence is COLLECTED, never acted on; measurement-tools findings fenced).

## Task 3 — dispositions, guards, close

Clusters in fully-read documents reach final dispositions (bulk rules licensed by the read only);
triaged-but-unread documents' clusters stay AS THEY ARE (no rule may sweep them — their fate
follows the user's acceptance of the exclusion list). All four guards at the final tree, with
the anchor-remap discipline (NOTE phase 1f's lesson, confirmed again this session: derive the
remap from the guard's drift report per citation, never from a single assumed threshold — two
anchors above the insertion point were over-shifted by a blanket rule and caught by the guard).
Rows for gaps/conflicts. Dated notes on OI-207. `STATUS.md` pointer at the TOP. Commits per
change-class; push origin.

## Report

The triage table's summary counts per class; the artifact path; the full-read confirmations with
their yields and the RATIFICATION QUEUE; the flag sections; the disposition arithmetic; guard
results; anomalies each diagnosed. **The report's ASK section addresses the user directly: the
proposed exclusion list (per file, with its verification), and the remaining full-read set with
a measured session estimate.** Standing self-check before reporting.
