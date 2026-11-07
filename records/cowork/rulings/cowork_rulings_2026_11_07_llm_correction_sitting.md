# Cowork ruling record — 2026-11-07 — the language-model correction: the scope document's derivations ratified

> **A RULING RECORD.** Cowork, 2026-11-07 (Stockholm), the sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_six.md`. It records one ratification by the user.
> **Documentation only; algorithm: no change.** Nothing is applied by this record; the correction act is a later
> dispatch for Claude Code.

## 0. What was put, and the user's word

The question put, in plain text and alone, after the scope document's §8 had been written and checked (its §9):
*"Do you ratify derivations 1 to 7 as written? If you prefer the alternative for point 3, say so."*

**The user's word: "ratified".** The alternative for point 3 was not taken.

**What it rests on.** `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`, Ruling 1 and
Ruling 2. The user's words, as the scope document §0 quotes them:

> Ruling 1: "LLM:S are only to be used during development of the software solution (in order to better it). Never at
> run-time in the finished product." … "It might ONLY be used for getting an LLM:s second opinion when we test our
> product, and our product struggles with inference."

> Ruling 2: "confliciting entries must be corrected - AND any down-stream effects of the corrections too."

**The source of the derivations.** `ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md`, §8B, as
corrected by its check (§9). 38,702 bytes as staged back after its last landing in this sitting.

## 1. Ruling 1 — the derivations of the scope document §8B are RATIFIED

These are derivations: the record decides each one (D-599), and the user ratified them as written. In plain words:

1. **D-440, D-441, D-442, D-443, D-446, D-447 and D-448 are marked SUPERSEDED BY Ruling 1 of the language-model record.**
   Each decides something about a language model in the shipped product. The register's status guide defines
   SUPERSEDED BY as *"A later ruling replaces it. The replacement is named."* (`DECISIONS.md` line 101). Their present
   statuses (DEFERRED for D-440 and D-441; NOT STATED for the others) no longer fit. The quoted wording and the
   2026-08-04 entry ratification are kept. The change is made in the register's data file and regenerated.
2. **D-444 and D-445 keep their status (NOT STATED), with a provenance note.** The note says that Ruling 1 removes the
   language-model bridge as one of the core access layer's two consumers. The rules themselves use no language model,
   and Ruling 1 does not speak to the other consumer, a future plugin interface.
3. **`docs/llm_integration.md` and `ARCHITECTURE.md` §19 are each marked superseded by Ruling 1.** Their text is kept
   (#12) under a banner that points to `docs/llm_triage_design.md`, the existing design of the test-time second
   opinion. Neither is rewritten. `docs/llm_integration.md` §2.5, lines 117–118, which does not conflict, is kept under
   the same banner.
4. **The 2026-08-08 delegation gets a note.** In `records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md`,
   route (i), third bullet (lines 33–37), a note names Ruling 1, with the bullet's wording kept. The delegation lines in
   `ARCHITECTURE.md` fall under point 3's banner.
5. **The reading files' stale descriptions are annotated, with their wording kept.** The L2 reading file's description
   of the integration as *"a product tool outside the analysis"* (lines 72465–72469 and the items at 72557–72590), and
   the L0/L1 reading file's manifest description at line 10142. The dispositions are not changed.
6. **Row 21.102's defense loses its language-model half.** An annotation goes at the L3 reading file's line 30465,
   with the wording kept. The other half (the Authoritative Chord Symbol Mode) stands. Row 21.102's proposed
   QUARANTINED is not changed.
7. **No act now** on: Ruling 57 clause (ii) and Ruling 62 item 11 (they still hold for any reader outside the analysis,
   a test-time second opinion included); the DESIGN-INTENT seed list (amended by its own act when the framework phase
   consumes it); the document's membership of the specification document set; the four leak-check records.

## 2. What this record does not do

- It changes no algorithm. The method that stands is the one the scope document §5 states.
- It edits no tracked file. The correction act is a dispatch for Claude Code, written by a later Cowork session; that
  session checks each step at its object before the dispatch is handed over.
- It does not close what the scope document leaves open: its §3D (places not searched: `src/`, the `docs`
  sub-folders, `DECISIONS.md` beyond the rows read), §7 item 3 (a search of the whole rulings folder), and the re-test
  of L3 family 7.

*Provenance: Cowork, 2026-11-07 (Stockholm), the sitting booted on entry 566. The user's words: the opening instruction;
"shortened"; "continue"; "continue"; "ratified".*
