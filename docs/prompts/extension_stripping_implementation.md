# Extension Stripping — `stripSymbol` + Progressive Comparison Protocol

**Scope:** Implement `stripSymbol` as a pure utility function in
the composing module. Implement `classifyComparison` as the
progressive comparison protocol wrapper. Wire composing_tests'
catalog comparison through `classifyComparison`. Report
per-classification counts. Result: composing_tests' actionable
real-diff count drops from 135 to ~23 (Mode 1 QA classification
predicts this distribution).

This is **test-infrastructure-only work.** No production code path
changes; emitters continue to write maximal analyzer output.
`stripSymbol` exists for diff classification when comparing
analyzer output against catalogs/corpora that use less-precise
notation conventions.

**Reference docs (read first, in this order):**
- `docs/extension_stripping_policy.md` — the design memo. Has the
  full spec including `stripSymbol` signature, `classifyComparison`
  result shape, the progressive protocol's 4-step semantics, and
  the "Suggested first step" section listing each implementation
  step.
- `docs/mismatch_classification.md` — Mode 1 QA classification of
  the 135 mismatches (Phase 5 prep work, commit `3378b9c7da`).
  Pattern A (extension stripping) is 112 entries / 83% of total.
  Predicts the post-implementation real-diff baseline at ~23.

**Memory references** (auto-loaded into your CC context):
- `project_no_stripping_in_production` — the principle: shipping
  product never reduces analyzer output. `stripSymbol` is
  test-only utility; never wired into emitters.
- `project_chord_symbol_ban` — content-based ban on user-written
  analytical content as analyzer input, regardless of storage.
  `classifyComparison` runs analyzer output (from notes alone)
  through stripping protocol, compares against catalog. Catalog
  is comparison metadata, not input.
- `project_composing_tests_baseline_synthetic` — context on why
  the 135 baseline isn't a real-music backlog; synthetic
  enumeration catalog. Updated baseline after this work lands
  becomes the new reference.

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).
3. Force rebuild (`cmd.exe //c "C:\s\MS\setup_and_build.bat"`)
   and verify fresh binary timestamps before running tests.
   Build dir is `ninja_build_rel/`.
4. Cache pipeline_snapshot_tests baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_strip_baseline/`

---

## Critical principles (preserve through this work)

- **No stripping in production.** `stripSymbol` is a pure
  utility consumed by test infrastructure (and possibly tools)
  only. Do NOT wire stripping into `emitHarmonicAnnotations`,
  `emitImplodedChordTrack`, `harmonicAnnotation` formatter, or
  any production code path. The shipping product writes maximal
  analyzer output; nothing about that changes.
- **Analyzer behavior unchanged.** This work doesn't touch
  `analyzeSection` or any pass/helper inside it. Per-region
  chord identity, key analysis, KeyArea spans — all preserved
  byte-identical.
- **No catalog edits.** The composing_tests catalog
  (`chordanalyzer_catalog.musicxml`) is the standing
  do-not-touch surface. The progressive comparison protocol
  works against the existing catalog without modification — that's
  the whole point of using stripping for diff classification
  rather than catalog rewriting.
- **No DCML or external corpus reads.** This work targets
  composing_tests' synthetic catalog only. DCML comparison
  tooling is a separate future session.

---

## Work order

### Step A — Implement `stripSymbol` pure function

File: somewhere in `src/composing/` — likely alongside existing
chord symbol formatting code. Grep for `ChordSymbolFormatter` or
similar to find the right location. If the formatter is in
`chordsymbolformatter.h/cpp`, that's a reasonable home.

Signature:

```cpp
QString stripSymbol(const QString& symbol,
                    int maxExtensionDegree,
                    bool preserveAlterationsAboveLimit);
```

- `maxExtensionDegree`: 7 / 9 / 11 / 13 — meaningful values only.
  Other values (5, 6, 8, 10, 12, 0, negative) should be rejected.
  Recommendation: assert / debug-trap on invalid input; return
  the input unchanged in release. Either way, log enough that
  test failures from invalid input are debuggable.
- `preserveAlterationsAboveLimit`: when `true`, altered tones
  (b9, #11, b13, etc.) above the truncation point survive in
  the output; when `false`, they're dropped along with their
  unaltered counterparts.

Pure function on the symbol string. No analyzer state, no
external dependencies, no side effects. Should handle all
chord symbol shapes the analyzer produces — triads, sevenths,
extensions through 13, alterations (b9 #9 b5 #5 #11 b13),
sus chords, slash chords, diminished/half-diminished, etc.

**Unit tests** in the same module's test directory. Cover:
- Each meaningful degree (7, 9, 11, 13) with both alteration
  modes (`true`/`false`)
- Representative inputs spanning the chord vocabulary
- Edge cases: empty string returns empty string; chord with no
  extensions returns unchanged; alterations on truncated tones
  per the alteration-preservation parameter

### Step B — Implement `classifyComparison` protocol wrapper

Same location as `stripSymbol` (or a sibling file if cleaner).

```cpp
struct ComparisonResult {
    enum Kind { DirectMatch, ConventionDiff, RealDiff };
    Kind kind = RealDiff;
    int matchedAtDegree = 0;            // valid only when kind == ConventionDiff
    bool matchedWithAlterationsPreserved = false;  // ditto
};

ComparisonResult classifyComparison(const QString& analyzerOutput,
                                    const QString& catalogEntry);
```

Protocol implementation per `docs/extension_stripping_policy.md`'s
"Progressive comparison protocol" section:

1. Direct comparison — `analyzerOutput == catalogEntry`?
   If yes → return `{DirectMatch, 0, false}`.
2. Else, try progressive stripping at degrees 13, 11, 9, 7
   (descending — highest cap first, since less stripping is more
   information-preserving). At each degree, try both alteration
   modes (`true` / `false`). Eight combinations total.
3. If any stripping configuration produces a match → return
   `{ConventionDiff, matchedDegree, matchedAlterationsMode}`.
   Use the **highest matching degree** (least aggressive
   stripping) when multiple match — the catalog's effective
   convention is the loosest one that resolves the diff.
4. If no stripping configuration matches → return
   `{RealDiff, 0, false}`.

**Unit tests** for `classifyComparison` covering:
- Direct match cases (analyzerOutput == catalogEntry)
- ConventionDiff at each degree (7, 9, 11, 13) with both
  alteration modes
- RealDiff cases (genuinely different chord identities that
  no stripping resolves)

### Step C — Wire composing_tests to use `classifyComparison`

Locate the composing_tests catalog comparison logic. Likely in
`src/composing/tests/` — a fixture loader followed by entry-by-entry
comparison. The current logic reports a single mismatch count;
modify it to:

1. For each catalog entry, call `classifyComparison(analyzerOutput,
   catalogEntry)`.
2. Bucket results by `Kind` and (for ConventionDiff) by
   `matchedAtDegree` + `matchedWithAlterationsPreserved`.
3. Maintain backward compatibility on the test pass/fail criterion:
   the test passes when `RealDiff` count is at the expected
   baseline (or fewer). Initial expected baseline: ~23 (per Mode 1
   QA classification). Pin the exact number after Step D's
   empirical run.

The mismatch report file (`src/composing/tests/chord_mismatch_report.txt`)
should now show:
- DirectMatch count
- Per-(degree, alterations-mode) ConventionDiff count
- RealDiff count + per-entry detail (mirror the existing entry
  format for the RealDiff bucket)

The DirectMatch and ConventionDiff buckets don't need per-entry
detail in the report — counts are sufficient. Only RealDiff
entries are actionable and warrant detail.

### Step D — Run, observe, pin baseline

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./composing_tests.exe
```

Inspect the per-classification breakdown. Expected distribution
from Mode 1 QA prediction:
- ~112 entries classify as ConventionDiff at degree 7
- ~9 entries classify as ConventionDiff at varying degrees (Pattern B
  alteration ordering entries — these may classify as DirectMatch
  if alteration ordering doesn't affect string equality, or as
  RealDiff if it does; observe and document)
- ~7 entries classify as ConventionDiff at varying degrees (Pattern C
  add-tone vs bare triad)
- ~23 entries classify as RealDiff (the actionable baseline)

If the actual distribution differs substantially:
- More ConventionDiff than predicted → fine; means more entries
  resolved under stripping than expected.
- Fewer ConventionDiff → investigate; might mean the stripping
  function isn't matching the catalog's actual convention.
- More RealDiff than predicted → halt and surface; need to
  investigate which entries unexpectedly fall into RealDiff.

Pin the baseline at whatever Step D produces. Update the test's
pass criterion to that exact count. Update CLAUDE.md and any
other standing-instruction reference to "135 baseline" with the
new number plus a brief explanation that 135 was the pre-stripping
total mismatch count and the new number is the actionable RealDiff
count after the progressive comparison protocol lands.

### Step E — Verify byte-identity in non-target tests

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # PASS without --update-goldens
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_strip_baseline/
                                      # zero output
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` must remain byte-identical (no production
code change, so emitter outputs are unchanged).

`notation_tests` must remain at 53/53.

If either drifts, halt and surface — that means stripping leaked
into production code somehow.

---

## Commit + push

Single commit. Suggested message skeleton:

```
Extension stripping: stripSymbol + progressive comparison protocol

Implements stripSymbol(symbol, maxExtensionDegree,
preserveAlterationsAboveLimit) as a pure utility function in the
composing module, with unit tests covering each meaningful degree
(7/9/11/13) and both alteration modes.

Implements classifyComparison(analyzerOutput, catalogEntry) as the
progressive comparison protocol wrapper. Per-entry classification:
DirectMatch / ConventionDiff(at degree K, alterations preserved or
dropped) / RealDiff.

Wires composing_tests catalog comparison through classifyComparison.
The mismatch report now buckets entries by classification:

- DirectMatch: [N]
- ConventionDiff at degree 7 (alterations dropped): [N]
- ConventionDiff at degree 7 (alterations preserved): [N]
- ConventionDiff at degree 9: [N]
- ...
- RealDiff: [N] (the actionable baseline)

Baseline RealDiff count: [N]. Was 135 (pre-stripping total mismatch
count); is now [N] (real disagreements that no stripping resolves).
The progressive protocol is a more honest accounting — entries that
match the catalog under degree-K stripping are notation-convention
differences, not analyzer errors, and the RealDiff bucket is what's
actionable.

No production code change. emitHarmonicAnnotations,
emitImplodedChordTrack, harmonicAnnotation formatter all unchanged
— shipping product still writes maximal analyzer output per
project_no_stripping_in_production principle. stripSymbol is
test-infrastructure-only utility.

pipeline_snapshot_tests: 10/10 byte-identical.
notation_tests: 53/53.
```

Update CLAUDE.md (or wherever the "135 baseline" reference lives in
standing instructions) to reflect the new number and the framing.

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched count + rough LoC
- Step A unit test summary (count + brief note on coverage)
- Step B unit test summary (count + brief note on coverage)
- Step D classification breakdown:
  - DirectMatch count
  - Per-(degree, alterations-mode) ConventionDiff counts
  - RealDiff count (the new baseline)
  - Whether the breakdown matches Mode 1 QA predictions
- Step E verification: pipeline_snapshot_tests byte-identical
  confirmation, notation_tests 53/53 confirmation
- The new RealDiff baseline number, pinned in test code and
  reflected in CLAUDE.md or standing-instruction docs
- Any deviations and why
- Anything in the Step D distribution that surprised you (e.g.,
  entries that classified differently than the Mode 1 QA prediction
  expected)

---

## Scope guardrails

- **Do not** modify `analyzeSection`, any pass/helper inside it,
  or any per-region or per-section analyzer logic. Analyzer
  behavior stays byte-identical.
- **Do not** modify `emitHarmonicAnnotations`,
  `emitImplodedChordTrack`, `harmonicAnnotation` formatter, or
  any production emitter. Stripping is test-only.
- **Do not** modify the composing_tests catalog
  (`chordanalyzer_catalog.musicxml`). Standing do-not-touch.
- **Do not** introduce DCML reads, Hiromi reads, or any
  external-corpus comparison. This session is composing_tests
  only.
- **Do not** wire `stripSymbol` into `EmitAnnotationOptions` or
  any production options struct (per
  `project_no_stripping_in_production`).
- **Do not** introduce a `[[deprecated]]` attribute on anything
  this session adds (`stripSymbol`, `classifyComparison`,
  `ComparisonResult`) — they're load-bearing test infrastructure,
  not transitional code.
- **Do not** auto-tune the catalog by editing entries that fall
  into RealDiff. Those are real disagreements — Mode 1 QA action
  items investigate them as separate work.
- If Step D's classification breakdown deviates substantially
  from the Mode 1 QA prediction (e.g., RealDiff count > 30 or
  < 15), halt and surface the breakdown for review before
  pinning the baseline.
- If Step E shows pipeline_snapshot_tests or notation_tests
  drift, halt and surface — stripping has leaked into production
  somehow.
