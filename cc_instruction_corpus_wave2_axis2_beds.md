# CC INSTRUCTION — Corpus Wave 2: the axis-2 annotation beds (user-ratified core scope, 2026-07-03)

**Status: ACTIVE DISPATCH (the only open instruction). Tools/registry/census work only — NOTHING under `src/`,
nothing touches inference, the frozen gate corpus stays byte-untouched.**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` — bash rules (`; echo "exit:$?"`, no large output), build/test commands (you should not need a
   build), the gate = the 53/24/53 **case-identity sets**.
2. `STATUS.md` header + `BUILD_AND_TEST.md`.
3. `docs/score_inventory.md` + `tools/REPRODUCIBILITY.md` + the Wave-1 record `cc_corpus_wave1_report.md` — the
   established clone/hash-pin mechanism and the registry-v2 conventions this wave follows.
4. `cowork_score_census.md` §3 (inclusion criteria), §4 (overlap rule), §5 (tiers).
5. `cowork_polyphony_phrase_harmony_research.md` **§6b** — the verified finds this wave onboards.

## Context — what this wave is and is not

The user ratified the **core scope**: onboard the three annotation beds the 2026-07-03 targeted sweep verified
(they serve the just-built axis 2: VL-C validation, VL-E footing, VL-F footing) + the census/registry
bookkeeping + the standing re-discovery trigger check. **Out of scope (queued for Wave 3 by the same
ratification):** Tier J (HookTheory/CoCoPops/OpenEWLD) and the Tier G/S remainder. **Already done — do NOT
re-do:** the Tier-C cadence/phrase GT exposure landed at session 21k (`tools/dcml_parser.py`
`DcmlRegion.cadence/phraseend` + `parse_cadence_phrase_markers` — Cowork re-verified at source at dispatch).

Everything below is **research-tier annotation-bed acquisition**: clone + hash-pin + inventory + registry +
census. No analysis integration, no consumer code, no inference work of any kind (standing rule).

## Task 1 — the schema-annotation bed (VL-F footing)

Source: `https://github.com/DCMLab/schema_annotation_data` (Finkensiep et al., ISMIR 2020).

- Clone + hash-pin via the established REPRODUCIBILITY mechanism (research-tier).
- **Verify at the cloned data and report:** the paper's headline numbers (244 expert true instances across
  Mozart's 18 piano sonatas / 54 movements; 10 schema types / 20 subtypes; per-type counts incl. Prinner 32,
  Fonte 49, Quiescenza 46) — report any mismatch, do not silently accept.
- **License:** record the repo's actual license class; unclear → hash-pin-only (the established mechanism).
- **Alignment note (report §):** the annotations are nested note-ID lists against MusicXML scores — document
  precisely WHICH score encoding they index (the repo's own scores vs the DCML `mozart_piano_sonatas` TSVs we
  hold) and what an alignment to our clone would require. **Document only — build nothing.**

## Task 2 — the per-bar texture-annotation bed (VL-C validation + the spec §15-1 reference)

Source: the Couturier/Bigo/Levé ISMIR-2022 dataset — published via `algomus.fr/data` (locate the actual Git
repository from there; the companion descriptor code is at `algomus.fr/code`).

- Clone + hash-pin the ANNOTATION repository (research-tier). Pin the descriptor-code repo too if it is a
  separate small repo (record it as tooling-reference, not our tooling).
- **Verify at the cloned data and report:** 9 movements (K.279/K.280/K.283, all three movements each), 1,164
  bar-level labels; the label syntax matches the paper (M/H/S functions, density, diversity, h/p/o elements).
- **Confirm the target-score identity:** the annotations reference the DCML `mozart_piano_sonatas` corpus we
  already hold (the paper says so) — verify the identifiers actually line up with our clone and record how
  (movement naming, bar indexing).
- License class recorded; unclear → hash-pin-only.

## Task 3 — the Essen phrase-boundary bed (VL-E footing)

- **Choose a hash-pinnable source and document the choice:** candidates include the kern/Humdrum Essen mirrors
  on GitHub and the EsAC distributions; prefer a Git repo that can be cloned + pinned like the others. If no
  pinnable source exists, STOP and report options — do not vendor loose files ad hoc.
- Inventory: piece count (literature figure ≈6,236 European folksongs), presence and encoding of the phrase
  marks, and the coverage caveat recorded verbatim in the registry note: **monophonic folk melodies — a
  single-line vocal bed for the per-voice phrase task, not usable for motion profiles (no voice pairs) nor for
  the harmonic idiom pipeline (no chord symbols).**
- License class recorded (expect non-commercial/unclear → hash-pin-only).

## Task 4 — census + registry bookkeeping

- Registry: one entry per bed in the Wave-1 registry-v2 form (`tools/score_census_registry.json`), with tier /
  license / alignment fields per census §6-1. These are **annotation/validation beds**, not analysis corpora —
  if the schema needs a field or kind to say that, make the smallest additive schema change and document it in
  the report (generator updated accordingly; regeneration deterministic, as Wave 1 established).
- Census (`cowork_score_census.md` §1 enumeration): add the three containers (DCMLab schema data was inside the
  already-enumerated DCMLab org — mark the row; algomus/Dezrann moves from §7 residual risk into the
  enumerated table; the Essen container added). Note in each row that it entered at Wave 2 with this report as
  provenance. Do not otherwise rewrite the census.

## Task 5 — the idiom re-discovery trigger check (standing trigger; check, not run)

The trigger fires on a **material change to the discovery-input corpora**. State the answer explicitly in the
report with reasoning. Expected: **NOT fired** — Tasks 1–2 add *labels over scores already in the discovery
corpus*, and Task 3 adds material outside both discovery views (no chord symbols → no harmonic view; monophonic
→ no voice-pair motion view). If your inventory contradicts this expectation, STOP and surface — the
re-discovery run is its own protocol and its own dispatch.

## Acceptance (ALL required)

1. Three beds cloned + hash-pinned + inventoried; every paper-claim verification reported (match or mismatch).
2. Registry + census updated as Task 4; regeneration deterministic.
3. **No-contamination proof (the Wave-1 pattern):** nothing under `src/`; the frozen gate corpus byte-untouched;
   end-of-run gate reproduction **53/24/53 case-identity sets, set-diff empty both directions, all three
   presets**.
4. Held-out discipline: nothing here creates or touches any held-out designation; the beds are validation
   material, never tuned against.
5. **Reuse-vs-new + what retires** (expected: reuses the clone/pin/registry machinery verbatim; new = the three
   bed entries + any minimal schema field; retires nothing).
6. Report `cc_corpus_wave2_report.md` (force-added per the `/cc_*.md` convention), carrying the commit SHAs
   (report them — do not omit, per the 22g close-out lesson). Commits local/unpushed, fork-only; suggested
   split: clones+pins / registry+census / report.

## STOP conditions

A source is unavailable, moved, or its content contradicts the §6b record; a license forbids even hash-pin
mirroring; the schema/texture annotations do not align with the scores we hold in a way the report can precisely
document; the Task-5 expectation is contradicted; anything would touch `src/` or the frozen gate corpus.
