# Rulings — language models: test-time second opinion only, never in the finished product, 2026-11-07

> **STATUS: RULING RECORD.** Cowork, 2026-11-07 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_two.md`. An interim carrier under the standing
> clause that a sitting record is written in the turn its ruling is given and lands in git at the next dispatch's
> Task 0. **No act of this sitting is a commit.** **[checked]** means read at the object by this sitting; **[relayed]**
> means not.

---

## 0. How it arose

Not put as a question. While the family-7 surface
(`ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md`, landed unchecked) was being reported,
the user asked where the idea of a language model in the software came from. The writing side answered from the record
and described the integration as attached to the composing side of the product — read from section titles, not from
the integration's purpose. The user corrected it in three statements, then gave the instruction in Ruling 2.

## 1. Ruling 1 — what a language model may be used for (the user's words, verbatim)

> "The llm-integration is part of another workflow - to be used for comparing our (non LLM-based, procedural software
> solution) with a 2nd opinion for difficult cases (where there is no ground truth or otherwise not apparent from music
> theory community what is "right")."

> "LLM:S are only to be used during development of the software solution (in order to better it). Never at run-time in
> the finished product."

> "I repeat: llm-integration is NOT for finished shipped product. It might ONLY be used for getting an LLM:s second
> opinion when we test our product, and our product struggles with inference. LLM is NOT allowed anywhere near the
> finished product."

**In plain terms:** the product's analysis is procedural and uses no language model. A language model may be used only
during development, when the product is tested, to give a second opinion on cases where the product struggles with
inference and no ground truth or settled music-theory answer exists. No language model is used at run-time, and none
is part of, or shipped with, the finished product.

## 2. Ruling 2 — conflicting entries corrected, with their downstream effects (the user's words, verbatim)

> "confliciting entries must be corrected - AND any down-stream effects of the corrections too."

**Conflicts known at this ruling** (from titles only — the full entries, their homes and every other place were not read
by this sitting): `DECISIONS.md` group N, *"Generation, constraints, visualization, and the LLM integration"*, rows
D-440 to D-448 **[titles and statuses checked at `DECISIONS.md` lines 590–602]**. Titles that describe use inside the
product with a user present: D-441 (*"Analysis and modification are phases of ONE conversation; a follow-up
instruction re-uses the reasoning rather than re-analysing"*, DEFERRED), D-442 (*"A validation failure goes back to the
language model as a tool-call error and is never shown to the user"*, NOT STATED), D-446 (*"The language model
resolves how the user names a passage; no index is built and the kinds of reference are not enumerated"*, NOT STATED).
Their homes as listed: `ARCHITECTURE.md` (D-440, D-441) and `docs/llm_integration.md` (D-442 to D-448). Also known:
`ARCHITECTURE.md` §19.3 *Relationship to the composing module* and `docs/llm_integration.md` §7.3 and its section
*Relationship to the Composing Module* carry the sentences of L3 family 7 **[relayed from the L3 reading file's
entries, read by this sitting]**.

**Not yet established — the scope of the correction.** Which of D-440 to D-448 conflict (each read whole at
`decisions/group_N.md`); every passage of `docs/llm_integration.md`, `ARCHITECTURE.md` and any other document that
describes run-time or shipped use; any other register entry, open item, reading-file row or ruling record that rests on
those passages (the downstream effects).

**Documentation or algorithm.** The analysis's algorithm is not changed: no language model is part of L2's or L3's
method as decided. What is corrected is the record of the product's scope and of the integration's purpose.

## 3. Bearing on work in hand

- **L3 family 7:** its surface describes the language model as *"a planned consumer outside the analysis"* and its
  placement as carried for *"the language-model bridge's own specification"*. Both are to be corrected at the surface's
  check by Ruling 1, the former wordings kept, and the placement re-tested against it (whether the code-interfaces
  Ruling 1, *"carried for the build of the analysis"*, or the suggestion-tool Ruling 1 reaches a test-time tool).
- **The order** — whether the correction's scoping comes before family 7's check and question — is for the next
  session to propose and the user to decide.

## 4. What this ruling does NOT do

It edits no tracked document, writes no dispatch (D-250), re-marks no row and allocates no decisions-register identity.
The corrections are made by the act the next session scopes; tracked documents are changed by a Claude Code dispatch
**[the writing side's reading of how earlier corrections were made]**.

## 5. Departures and bounds

As the family-6 ruling record of today, §4.

*Provenance: Cowork, 2026-11-07 (Stockholm), the sitting booted on entry 562. The user's words: the question
"Where did the idea of letting a language model be part of the software solution come from?"; the three statements
quoted in §1; the instruction quoted in §2.*
