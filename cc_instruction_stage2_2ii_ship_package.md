# CC Instruction: Stage 2.2-ii — Ship the decided re-baseline package

## Context

Cowork/user adopted your §6 recommendation with roadmap additions (see updated
`docs/implementation_roadmap.md` rows 2.2 / 2.4 / 5.2). The package, exactly:

1. `--section-level` diagnostic flag committed (default OFF).
2. F-1 letter-`o` diminished fix in `extract_quality`.
3. F-2: stop the It6→Maj misparse. Treatment: route `It6` (and variants like `It6/x`)
   to the SAME unparseable→root-only fallback as Ger/Fr/N — do NOT invent a root
   mapping unless you can establish the principled one from how DCML encodes it
   (investigate; if unclear, fallback is the decided safe choice — say which you did).
4. Rider 1: `analyze_inversion_errors.py` `--corpus-dir` (reads BOTH .ours.json and
   .music21.json from the given dir; manifest validation via
   `characterise_bir_false.validate_corpus_dir`; fixes the `:93` hardcoded read;
   `--ours-dir` kept as deprecated alias).
5. Rider 2: dead-shim removal in `notationcomposingbridgehelpers.{h,cpp}` (the 6
   symbols from dossier §5.2) — AFTER a full-repo qualified-caller sweep incl. tests.
6. Docs: STATUS provenance wording is Cowork's; you update CLAUDE.md's gate-policy
   section with ONE sentence: the 13/7 gate is batch-granularity; user-visible
   per-beat root-error rate is ~7× higher (measure-aligned view via
   `batch_analyze --section-level`; see `cc_stage2_2_ab_dossier.md`). Also sync
   BUILD_AND_TEST.md for the new flag + `analyze_inversion_errors --corpus-dir`.

NOT in the package: section-level as default (decided NO); Ger/Fr/N parsing changes
beyond It6 routing; cadence/pivot schema (deferred, Stage 6); any touch on the 3
genuine-regression cases (they are 2.4's evidence — leave the behavior alone).

Standing rules: never guess; explicit staging; `muse` never.

## Tasks

1. **Metric-test updates are deliberate re-pins** (the only time this is allowed):
   Stage-1d tests pinned F-1/F-2 as *suspect current behavior*. Update them to pin the
   *corrected* behavior, each with a comment `// re-pinned 2026-06-10: intentional
   metric correction (Stage 2.2-ii; dossier §4)`. Add new cases: letter-`o` →
   Dim/Dim7 (both `viio6` and `iio65` shapes), `It6` → fallback path (not Maj), and
   keep the °-sigil case. Run the full Python suite.
2. Apply the package per the list above. Rider 2 in its own commit (byte-identical
   claim verified by build + full suites).
3. **Verification gate:**
   - Build + composing 498 / notation 52 / snapshots 11/11 zero diffs (C++ touched:
     batch flag + shim removal).
   - Python suite green (count reported; deliberate re-pins listed).
   - Both presets regenerated per-preset; `characterise_bir_false --corpus-dir` →
     Baroque 13, Jazz 7, exact identity sets; `analyze_inversion_errors --corpus-dir`
     → 24/13 and 35/7 (closing F-3 with reproducible provenance).
   - Flag-off byte-identity spot-check (3 scores vs committed corpus) still holds.
   - One flag-on smoke run (1 score) — sane output, no crash.
4. **Commits (4, in order; propose all, commit after Cowork confirms the set):**
   - C1 `tools: add --section-level diagnostic flag to batch_analyze (Stage 2.2-ii)`
   - C2 `tools: metric corrections — letter-o diminished, It6 routing; analyze_inversion_errors --corpus-dir (Stage 2.2-ii)` (+ updated tests)
   - C3 `refactor: remove dead weight/pitch-context shims from notation bridge helpers (Stage 2.2-ii rider)` (byte-identical)
   - C4 `docs: gate-granularity note (CLAUDE.md) + BUILD_AND_TEST sync (Stage 2.2-ii)`

## Report — `cc_stage2_2ii_report.md`

Per-commit diffs summary; the It6 treatment you chose and why; re-pinned test list;
verification table (incl. both identity sets + 24/13 & 35/7 reproduction); sweep
evidence for the shim removal; deviations/unknowns.

Stop conditions: any gate number or identity-set change (the package is measured to be
gate-neutral — movement means something unmeasured happened); any caller found in the
shim sweep; snapshots diff; It6 treatment requiring new theory you can't establish.
