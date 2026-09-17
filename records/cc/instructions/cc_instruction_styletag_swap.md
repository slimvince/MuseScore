# CC instruction — the StyleTag swap: re-tag the Harmonic Vocabulary with the five ratified idioms

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Mandatory for this task: **`cowork_idiom_entry_mapping.md` (the per-entry mapping — THE spec for this swap)**,
> `cowork_style_taxonomy_proposal.md` (the ratified five idioms + the two cross-axes),
> `cowork_progression_schema_dictionary.md` §5/§12.1 (the catalog being re-tagged).
>
> **Dispatch state: ACTIVE (2026-07-02, ratified forward-sequence step 1 — mechanical).** ONE commit, dormant-module
> only, local/unpushed/fork-only. No θ, no judgment calls: **the mapping doc decides every tag; anything it does not
> cover goes on a STOP list in the report — never guessed.**

## The task

In `analysis/vocabulary/harmonicvocabulary.{h,cpp}` (dormant — no production consumer):
1. **Replace the placeholder `StyleTag {Baroque, Jazz, Default}`** with the ratified idiom set:
   `{DiatonicFunctional, ChromaticFunctional, SeventhFunctional, TriadicModal, ChromaticColoristic}` —
   **multi-valued per entry** (the mapping is explicitly multi-tag: e.g. plain ii–V–I = Diatonic-functional, with
   sevenths = Seventh-functional) → a set/bitmask, your representation call, declared.
2. **Add the two cross-attributes** the taxonomy ratifies, tagged separately per entry where the mapping specifies
   them: `mode {major, minor, both}` and `chromaticism {diatonic, chromatic, both}`.
3. **Re-tag every §5 catalog entry verbatim from `cowork_idiom_entry_mapping.md`** — including the parenthetical
   dual-tags (e.g. tritone sub = ChromaticColoristic, with its enharmonic Ger-6 reading noted → ChromaticFunctional).
   An entry absent from the mapping, or a mapping row without a matching entry → the STOP list (report §, no guess).
4. **Consumers/queries:** any query filtering by the old 3-value tag updates to filter by idiom-set intersection;
   semantics = "entry is admissible under any of the requested idioms" (declare if any call site forces a different
   reading). No weighting, no ranking change — tags are tags; the idiom-mixture *weighting* is the recognition
   consumer's job (next step), NOT this one.
5. **Tests:** update the existing vocabulary tests to the new tags (oracle-asserted against the mapping doc); add
   one multi-tag test (an entry retrievable under each of its idioms) and one cross-attribute test.
6. **Doc-sync (same commit):** `cowork_progression_schema_dictionary.md` — the §12.1/StyleTag placeholder note flips
   to the ratified taxonomy (pointing at the proposal + mapping docs); `cowork_style_taxonomy_proposal.md` status
   line gains "EXECUTED (StyleTag swap, this commit)".

## Gate

Dormant-module change only: grep-proof no production consumer; composing/notation/snapshot suites green, NO golden
refresh; corpus gate **53/24/53** byte-identical by construction (one end-of-run reproduction). Report
`cc_styletag_swap_report.md` (HELD, line count at end): the representation choice, the re-tag table count, the STOP
list (ideally empty), suite/gate proof.

## Stop conditions

Any entry↔mapping mismatch → STOP list, not a guess. Any production reach → STOP. Anything tempting a weighting
decision → out of scope (the consumer's design owns it). No θ.
