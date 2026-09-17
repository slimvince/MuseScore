# CC instruction — §15-12 grammar completion: extend `isLicensedProgression` (small dormant increment)

> **★ CORRECTION + ADDENDUM (Cowork, 2026-07-03):** the "D5 dependency map (binding)" paragraph below is
> **incomplete** — it states the catalog↔grammar coupling correctly but fails to note the grammar's ordinary
> in-layer consumers (`functionresolver`/`functionoutput`/`functioncadence`), whose dormant test oracles encode the
> pre-amendment licensed set. CC correctly STOPPED on the ripple (`cc_grammar_completion_report.md`). The ruling and
> the completing tasks are in **`cc_instruction_grammar_completion_addendum.md`** — execute both together.

> **DISPATCH note (Cowork, 2026-07-03): ACTIVE — this is the one dispatched instruction.** Written just-in-time
> after the user RATIFIED the L5 §15-12 grammar-completion amendment (2026-07-03, at the merged Cowork doc pass).
> Premises verified at source this session: `functionprogression.h` (the licensing grammar + D5 dependency-map
> block), `progressionrecognizer_tests.cpp` (the D5 consistency test — pin + tripwire, 11-motion known-gap list),
> `harmonicvocabulary.h` (the mirrored dependency-map block). Read those three before coding.

## Context (why this exists)

The consumer build's D5 consistency test (2026-07-02) proved the §5.0 licensing grammar omits three theory-licensed
root motions that the catalog's musically-correct entries exercise — 6 entries / **11** motions, all ruled GRAMMAR
GAPS, not catalog errors (the "12" was a corrected arithmetic error; the test's pinned 11 is authoritative). The
user has now **ratified** the L5 §15-12 amendment: the licensed set extends to include the three motions. The L5
spec §5.0 + §15-12, the dictionary §1/§5.1, and the consumer docs are **already amended** (Cowork doc pass,
2026-07-03) — the spec is deliberately ahead of the code; this increment closes that gap.

**D5 dependency map (binding):** the grammar has ONE owner — `functionprogression::isLicensedProgression`. Change
that module only. The catalog (`harmonicvocabulary`) needs **no entry edit**; the only coupling is the one-way
consistency test.

## Task 1 — extend the grammar (`analysis/function/functionprogression.{h,cpp}`)

License three additional root motions, per the ratified §5.0 enumeration (L5 spec, `cowork_layer5_function_design.md`
§5.0 — read the amended passage; mirror its wording in the header comment):

1. **The ascending fifth** — the target root a perfect fifth **above** (pc delta +7): tonic→dominant (I→V) and
   plagal motion (IV→I). Unconditional on quality.
2. **The descending second** — the target root a major or minor second **below** (pc delta +10 / +11): the
   Phrygian/Andalusian step (i→♭VII, ♭VII→♭VI, ♭VI→V). Unconditional on quality.
3. **The diatonic diminished fifth** — the IV→viiᵒ link of the full circle of fifths: the root falls a
   **diminished** fifth (pc delta 6) **and the arriving chord is a diminished triad**. The quality condition is the
   amendment's "diatonic" qualifier made operational — an **unconditional** delta-6 license is explicitly NOT wanted
   (it would license generic tritone root motion, which the grammar has never licensed). If you believe this
   realisation is wrong, STOP and report; do not choose a different shape silently.

Also update, in the same increment:
- the `functionprogression.h` §5.0-mirroring comment block (the enumeration + the "11 motions the §5.0 grammar does
  NOT license" note in the dependency-map block — that note is now historical; say the amendment closed it, dated);
- the mirrored dependency-map block in `harmonicvocabulary.h` (same historical note, same dating);
- keep the applied/leading-tone clause and everything else untouched.

## Task 2 — tests

1. **`functionprogression_tests.cpp`:** must-license cases for each new motion (I→V; IV→I; i→♭VII; ♭VII→♭VI; ♭VI→V;
   IV(major)→viiᵒ(diminished)) and must-NOT-license controls (delta-6 with a **non-diminished** arrival stays
   unlicensed; whatever existing negative controls the suite pins stay green **except** any that pinned the three
   now-licensed motions as unlicensed — those flip deliberately, named in the report as the amendment's effect).
2. **The D5 consistency test (`progressionrecognizer_tests.cpp`):** the test is built to turn RED when a known-gap
   entry starts passing — that is the designed tripwire. Tighten it exactly as its own comment block prescribes:
   **empty the `knownGaps` list** and replace the pin with the clean assert (**every** adjacent catalog pair
   licensed; `failing` empty; any failure red). Do not keep a vestigial list.

## Constraints (standing, all binding)

- **Dormant increment:** `functionprogression` has no production caller path that changes output (L5 is dormant).
  Prove it: gate **53/24/53 byte-identical** (exact sets, all three presets), both suites green, **no snapshot
  refresh**. Any gate diff is a STOP, not a chore.
- **Fork-only** (`origin` = slimvince/MuseScore; never `upstream`). Nothing outside `src/composing` + the two
  headers' comment blocks.
- **Report requirements (total-unification rule):** reuse-vs-new; what retires (expected: nothing retires — the
  known-gap list's deletion is the only removal); every claim cited at source (file + function/anchor, not line
  numbers); deviations flagged, not absorbed.
- **Docs commit rider (natural fold point):** the accumulated uncommitted Cowork doc-pass edits (the seven layer
  specs, the dictionary, ARCHITECTURE.md §2.15, `cowork_target_architecture.md`, `COWORK_HANDOFF.md`, STATUS.md)
  are ready to fold into this increment's docs commit — commit them as a separate `docs(cowork):` commit alongside
  the code commit, per the all-docs-in-sync rule. Do not edit them; commit as-is.

## Acceptance

1. The three motions license; the negative controls hold; the quality condition on delta-6 is tested both ways.
2. The D5 consistency test asserts the clean invariant (empty known-gap list) and is green.
3. Suites green, no refresh; gate 53/24/53 exact; dormancy re-proven (grep: no new production call site).
4. Report delivered (`cc_grammar_completion_report.md`), with the docs commit hash + code commit hash for
   Cowork verification at objects.
