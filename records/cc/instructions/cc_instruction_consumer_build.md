# CC instruction — the PROGRESSION-RECOGNITION CONSUMER: dormant build + dev-bed validation

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Mandatory, in FULL: **`cowork_progression_schema_design.md` (v4, FULLY RATIFIED 2026-07-02 — THE spec, §0–§10)**;
> its §0 cites everything else you need (`cowork_progression_schema_dictionary.md`, L4 §7, L5 §5.5/§7/§8, the
> confidence contract).
>
> **Dispatch state: ACTIVE (2026-07-02, forward-sequence step 2/3, on the full ratification).** Dormant build (no
> production consumer — byte-identical by construction), commits one change-class each, local/unpushed/fork-only.
> **No θ, no tuning** (every §4.5/§4.6 value = declared default; the firewall). Bash rules; cite by anchor;
> plain-vocabulary + §0-terms discipline applies to everything you write (the template's writing standards).

## Task 1 — the module (commit 1)

A new dormant module (placement + naming yours, declared; beside the L5 units) implementing §3/§4 exactly:
- **§4.1** recognition over the committed progression (the Vocabulary's recognise form; exact matches only, v1);
  overlap preference longer-then-more-specific; carry all admitted recognitions.
- **§4.5** the three-phase mixture: (1) weight-free recognition → (2) `w = blend(seed, idiom-evidence histogram)`
  (seed = preset-as-idiom-weights or all-equal; blend direction per spec, rate = declared default) → (3) prior
  strength `matchScore × max(w over the entry's IdiomSet)`, admission threshold, the mode-cue and chords-only
  factors (declared defaults).
- **§4.2/§4.4** the annotation: one **progression-schema-span** per admitted recognition (name, idiom set, span,
  match score, substituted-member read-outs; the D7 "chords-only" mark on `voiceLeadingDefined` entries).
- **§4.3** the evidence contribution: the §5.5 functional-plausibility feature (abstained positions) + the F-B
  override path (committed positions) — SELECTION-only, exactly as §4.3 states both conditions.
- **§4.6** the harmonic-sequence output — ALWAYS emitted (typed: progression, transposition step, span,
  repetitions, prior strength). **Do NOT wire §5.3 consumption** (that wiring is gated on declaring frame F-C in
  the confidence contract — a later, separate step; the output existing is this build's whole obligation).

## Task 2 — the D5 riders (same commit or commit 2; the user's make-it-VERY-clear directive)

1. **The consistency test:** every adjacent pair of every catalog entry passes `isLicensedProgression` — a unit
   test; a failure names the entry (mis-encoded OR a grammar gap — the test output must say both possibilities).
2. **The mirrored cross-referencing comment blocks** at `functionprogression.h` AND `harmonicvocabulary.h`, stating
   the D5 dependency map verbatim (grammar changes → functionprogression only; catalog changes → Vocabulary only;
   the consistency test is the one one-way coupling).
3. **Doc-sync in the same commit set:** the dictionary §5.1 owner note + §1 map restatement; the L5 spec §5.0 map
   restatement (per D5's build-rider list).

## Task 3 — tests + validation (tests in commit 2; validation read-only, report)

- **Tests (oracle-asserted):** recognition of seeded catalog cases (a ii–V–I; a substituted ii–(subV)–I; a Monte
  chain); the three-phase mixture (no evidence → seed; evidence moves w; max-not-sum); admission + both §4.5
  factors; the §4.3 abstained-feature and committed-override paths (selection-only, F-B semantics); the §4.6
  always-emit; the D7 mark; nothing-recognised → nothing emitted.
- **§7 validation (dev beds, read-only, via a default-OFF dump — the established pattern):** recognised-span
  precision/recall where the GT annotates cadences/schemata; the evidence contribution measured as RN-accuracy
  change on exactly the covered positions; per-corpus tables + exemplars. Jazz/pop recognitions carry the
  "empirically-unvalidated" mark in the dump.

## Gate + deliverable

Dormancy grep-proof; suites green, NO golden refresh; corpus **53/24/53** exact once at the end.
`cc_consumer_build_report.md` (HELD, line count at end): module + reuse-vs-new, the D5 riders shown verbatim,
test table, validation tables, declared decisions, Unknowns. **Stop conditions:** any production reach; any
§5.3/F-C wiring; any tuning; a catalog entry failing the consistency test is REPORTED (both readings), never
tagged around. **On your report: Cowork verifies at committed objects before ratifying.**
