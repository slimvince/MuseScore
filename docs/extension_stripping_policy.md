# Extension Stripping — Test-Only Utility

Date: 2026-04-25
Status: Direction settled. Stripping is test-infrastructure only; no
production consumer.

## Principle

Inferrers (analyzers) and emitters in the shipping MuseScore product
always produce maximal output. They do not reduce, truncate, or
simplify symbol or Roman-numeral notation under any user preference,
mode flag, idiom-detection scheme, or per-score override. Whatever the
analyzer infers, the emitter writes verbatim. Extensions, alterations,
and chromatic colorations are part of the truth; the truth ships.

This applies uniformly across all emitters:
- `emitHarmonicAnnotations` writes the analyzer's maximal symbol/Roman.
- `emitImplodedChordTrack` writes all inferred chord tones (voicing
  choice remains an emitter concern, but no extension-degree
  reduction).
- `analyzeHarmonicContextRegionallyAtTick` and friends return the
  full `AnalyzedRegion` data for status bar / right-click menu /
  tick-local consumers.

There is no `maxExtensionDegree` on `EmitAnnotationOptions`, no
`extensionPolicy` field, no per-score idiom toggle, no ContextAware
mode. The `EmitAnnotationOptions` struct stays as Phase 3b left it
(only `minimumDisplayDurationBeats` for now). Future emitter knobs
must justify themselves on grounds other than display verbosity.

## Where stripping lives

In tools used for improving our inferrers — comparison frameworks,
test harnesses, batch analyzers measuring against authoritative
corpora. Never in shipping MuseScore code paths. The use case is
diff classification: when the analyzer's output disagrees with a
ground-truth corpus entry, stripping helps decide whether the diff
is a notation-convention difference (catalog uses a less-precise
convention than the analyzer's maximal output) or a real
disagreement (analyzer and catalog actually identify different
content).

## Progressive comparison protocol

The protocol the comparison framework applies per catalog entry:

1. Direct comparison — does `analyzerOutput == catalogEntry`?
   If yes → **direct match**. Done.
2. If no, try progressive stripping at the meaningful degrees:
   - `stripSymbol(analyzerOutput, 13, *)` matches catalog?
   - `stripSymbol(analyzerOutput, 11, *)` matches?
   - `stripSymbol(analyzerOutput, 9, *)` matches?
   - `stripSymbol(analyzerOutput, 7, *)` matches?
   At each degree, try both alteration modes
   (`preserveAlterationsAboveLimit = true / false`) — the catalog's
   alteration convention is observable too.
3. If any stripping degree + alteration mode matches → classify as
   **convention-difference at degree K (alterations: preserved/dropped)**.
   The minimum K that matches is the catalog's effective convention
   for that entry.
4. If no stripping configuration matches → **real diff**. The
   analyzer and catalog identify substantively different content
   (different root, quality, key, or a genuine extension dispute
   that stripping doesn't explain).

The classification is per-entry, not per-catalog. Different entries
in the same catalog may settle at different stripping degrees,
which itself is informative — it tells us the catalog has mixed
convention or per-entry idiom rather than a single uniform cap.

The output of running this against a corpus is a classification
table: how many direct matches, how many at each
convention-difference level, how many real diffs. The real-diff
count is the actionable number — those are cases worth investigating
as analyzer bugs, catalog issues, or genuine ambiguity.

## What this gives us

- **Honest signal.** We don't pre-assume the catalog's convention;
  we discover it per entry. A catalog whose entries match at
  varying degrees has mixed convention; a catalog whose entries
  consistently match at degree 7 uses classical convention.
- **Catalog-convention metadata becomes empirical.** Earlier drafts
  required declaring per-catalog parameters as test fixture setup.
  Under the progressive protocol, the "convention" is a discovered
  property of the comparison run, not a declared input.
- **Actionable diff isolation.** The real-diff bucket is small and
  high-signal; the convention-difference buckets are large but
  expected (and informative about the catalog's notation idiom).

## `stripSymbol` — pure utility function

A single pure function:

```cpp
QString stripSymbol(const QString& symbol,
                    int maxExtensionDegree,
                    bool preserveAlterationsAboveLimit);
```

- `maxExtensionDegree`: 7 / 9 / 11 / 13. Other values rejected.
- `preserveAlterationsAboveLimit`: whether altered tones (b9, #11,
  etc.) above the truncation point survive. The progressive
  comparison protocol tries both modes per degree.

Lives wherever symbol-string formatting lives in the composing
module. Pure function on the symbol string; no analyzer state
involved. Unit-tested against representative inputs at each
meaningful degree and both alteration modes.

The comparison framework that consumes `stripSymbol` (the actual
"progressive comparison protocol" implementation) lives in the
tools/test infrastructure layer that uses it — composing_tests'
catalog harness, batch_analyze's corpus comparison mode, or a
dedicated comparison utility. `stripSymbol` itself doesn't know
anything about catalogs or comparison; it's purely a string
transformation.

## Catalog convention as discovered metadata

Earlier drafts had each catalog declare its stripping convention
as test fixture setup ("this catalog uses degree=7,
preserveAlterations=false"). Under the progressive comparison
protocol, that's no longer needed — the convention is *discovered*
empirically from the comparison run, per entry.

Useful properties this gives us:

- **No declarative input required** for a new catalog. Drop scores
  in, run the comparison, get a per-entry classification table.
- **Mixed-convention catalogs are visible.** If a catalog has some
  entries that match at degree 7 and some at degree 9, the
  classification table shows it. Earlier framing would have forced
  a single per-catalog parameter and reported the mismatched
  subset as "real diffs" incorrectly.
- **Convention drift detectable.** If a catalog gradually shifts
  convention over time (e.g., the synthetic catalog's
  classical-section uses degree 7 but the jazz-section uses
  degree 13), the per-entry classification surfaces it.

For the current composing_tests synthetic catalog: per Pattern A's
profile, most entries probably classify as
"convention-difference at degree 7, alterations dropped." The
expected outcome is a classification table with ~112 entries in
that bucket and the remaining ~23 spread across
direct-match-after-fix, real diffs, formatter bugs, and the
Tristan empty-symbol bug.

## Notation conventions (informational)

Worth knowing when setting per-catalog parameters:

- **Classical Roman numeral analysis** caps at 7ths. Triads and
  seventh chords with figured-bass inversions; chromatic harmonies
  get special-case nomenclature (Neapolitan ♭II, augmented sixths
  It+6/Fr+6/Ger+6, secondary dominants V/V, modal mixture ♭VI).
- **Jazz Roman numeral analysis** (Berklee and successors) extends
  to 9/11/13. Chord-scale theory drives alteration notation.
- **Chord-symbol notation** (jazz lead-sheet style) extends to 13
  with explicit alterations.
- **Classical chord-symbol** is essentially absent — classical
  analysis uses Roman numerals, not chord symbols.

The catalog's target notation convention determines the stripping
parameters. A classical catalog with Roman entries uses
`maxExtensionDegree=7`. A jazz catalog with chord-symbol entries
uses `maxExtensionDegree=13`. Each catalog declares its own.

## Catalog reconciliation for composing_tests

The current 135 mismatches assume the analyzer is wrong. Under
the maximal-output principle, the analyzer is right by design;
the catalog uses a truncated convention for most entries.

Resolution: apply the progressive comparison protocol. Each entry
gets a classification (direct match / convention-difference at
degree K / real diff). The "real diff" count is the actionable
baseline: expected ~23 (Patterns B–G + 3 clear analyzer failures +
3 clear catalog issues + 3 ambiguous + the Tristan empty-symbol
bug, which remains a real diff since `stripSymbol("")` returns
`""` regardless of parameters).

The catalog stays unchanged. No catalog edits required, no
carve-out to the standing do-not-touch rule.

## Suggested first step

A small CC session that:

1. Implements `stripSymbol(symbol, maxExtensionDegree, preserveAlterationsAboveLimit)`
   as a pure function in the composing module. Unit-tests it
   against representative inputs at each meaningful degree
   (7/9/11/13) and both alteration modes (`true`/`false`).
2. Implements the progressive comparison protocol as a small
   utility wrapping `stripSymbol`. Signature roughly:
   ```cpp
   struct ComparisonResult {
       enum Kind { DirectMatch, ConventionDiff, RealDiff };
       Kind kind;
       int matchedAtDegree = 0;            // for ConventionDiff
       bool matchedWithAlterationsPreserved = false;  // for ConventionDiff
   };
   ComparisonResult classifyComparison(const QString& analyzerOutput,
                                       const QString& catalogEntry);
   ```
3. Wires composing_tests' catalog comparison to use
   `classifyComparison` per entry. Test passes when no entries
   classify as `RealDiff` beyond the known-acceptable count.
4. Reports per-classification counts in test output, replacing
   the current "135 mismatches" framing with something like
   "112 convention-diff at degree 7 / 9 convention-diff at varying
   degrees / 23 real diffs."
5. Verifies the real-diff count matches expectation (~23).
   Documents the new baseline; updates any references to
   "135 baseline" in standing instructions (CLAUDE.md and similar).
6. Verifies `pipeline_snapshot_tests` stays byte-identical — no
   production code change since emitters still write maximal output.
7. Verifies `notation_tests` stays at 53/53.

This is a separate CC session from any Phase 4 / Phase 5 work, can
land in parallel.

The Tristan empty-symbol bug at m285 ({C, F#, Bb, D} → "") is
independent and surfaces as a `RealDiff` regardless. Worth fixing
as its own small session — a real bug, not a notation-convention
dispute.

If `classifyComparison`'s logic later wants to live in
`tools/batch_analyze.cpp` for corpus-wide measurement (DCML
scores, future Hiromi/Filo* corpora when per-symbol trust mode
ships), it lifts out cleanly — `stripSymbol` is the pure leaf
and `classifyComparison` is the protocol wrapper, both reusable.
